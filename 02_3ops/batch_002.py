"""Batch 002 - passing/02_3ops
114 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a dark blue plastic or composite cover panel with a trapezoidal shape, featuring a notched cutout at the bottom edge and rounded corners, designed as a protective enclosure or access cover for electronic equipment.
def model_130757_b2c47f8d_0009():
    """Model: Micro SD"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 37 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3789098992, perimeter: 4.8941645734
            with BuildLine():
                CenterArc((0.6757523087, 0.4683930357), 0.08, 0, 90)
                Line((-0.6105856431, 0.5483930357), (0.6757523087, 0.5483930357))
                CenterArc((-3.5324284413, -0.0015276505), 2.9731427981, -10.6589610047, 21.3179220095)
                Line((-0.2291122606, -0.5514483367), (-0.6105856431, -0.5514483367))
                Line((-0.2291122606, -0.5514483367), (-0.1612376987, -0.486041732))
                CenterArc((-0.1404208671, -0.5076440355), 0.03, 90, 43.9391796601)
                Line((-0.1404208671, -0.4776440355), (-0.0300981056, -0.4776440355))
                Line((-0.0300981056, -0.5514483367), (-0.0300981056, -0.4776440355))
                Line((0.1291928792, -0.5514483367), (-0.0300981056, -0.5514483367))
                Line((0.1291928792, -0.5514483367), (0.2473425141, -0.4375946889))
                CenterArc((0.2820372335, -0.4735985281), 0.05, 90, 43.9391796601)
                Line((0.6757523087, -0.4235985281), (0.2820372335, -0.4235985281))
                CenterArc((0.6757523087, -0.3435985281), 0.08, -90, 90)
                Line((0.7557523087, 0.4683930357), (0.7557523087, -0.3435985281))
            make_face()
            # Profile area: 0.056414374, perimeter: 2.3149757678
            with BuildLine():
                Line((-0.6618650022, 0.5483930357), (-0.6105856431, 0.5483930357))
                CenterArc((-3.5849045434, -0.0015276505), 2.9743189003, -10.6546969742, 21.3093939485)
                Line((-0.6105856431, -0.5514483367), (-0.6618650022, -0.5514483367))
                CenterArc((-3.5324284413, -0.0015276505), 2.9731427981, -10.6589610047, 21.3179220095)
            make_face()
            # Profile area: 0.1264592515, perimeter: 2.3150162398
            with BuildLine():
                CenterArc((-3.5849045434, -0.0015276505), 2.9743189003, -10.6546969742, 21.3093939485)
                Line((-0.6792476913, 0.5483930357), (-0.6618650022, 0.5483930357))
                CenterArc((-0.6792476913, 0.4833930357), 0.065, 90, 90)
                Line((-0.7442476913, -0.4864483367), (-0.7442476913, 0.4833930357))
                CenterArc((-0.6792476913, -0.4864483367), 0.065, 180, 90)
                Line((-0.6618650022, -0.5514483367), (-0.6792476913, -0.5514483367))
            make_face()
        # OneSide extrude, distance=0.077
        extrude(amount=0.077)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 37 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.056414374, perimeter: 2.3149757678
            with BuildLine():
                Line((-0.6618650022, 0.5483930357), (-0.6105856431, 0.5483930357))
                CenterArc((-3.5849045434, -0.0015276505), 2.9743189003, -10.6546969742, 21.3093939485)
                Line((-0.6105856431, -0.5514483367), (-0.6618650022, -0.5514483367))
                CenterArc((-3.5324284413, -0.0015276505), 2.9731427981, -10.6589610047, 21.3179220095)
            make_face()
            # Profile area: 0.1264592515, perimeter: 2.3150162398
            with BuildLine():
                CenterArc((-3.5849045434, -0.0015276505), 2.9743189003, -10.6546969742, 21.3093939485)
                Line((-0.6792476913, 0.5483930357), (-0.6618650022, 0.5483930357))
                CenterArc((-0.6792476913, 0.4833930357), 0.065, 90, 90)
                Line((-0.7442476913, -0.4864483367), (-0.7442476913, 0.4833930357))
                CenterArc((-0.6792476913, -0.4864483367), 0.065, 180, 90)
                Line((-0.6618650022, -0.5514483367), (-0.6792476913, -0.5514483367))
            make_face()
        # OneSide extrude, distance=0.095
        extrude(amount=0.095, mode=Mode.ADD)
    return part.part


# Description: This is a low-poly geometric elephant figurine with an angular, faceted design featuring a curved trunk, blocky body, and a flat base, rendered in dark blue and gray tones.
def model_130834_62ed16e7_0000():
    """Model: Monitor Headphone Mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 49 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.3155152343, perimeter: 16.7345218976
            with BuildLine():
                CenterArc((1.24, 1.44), 0.2, 0, 90)
                Line((1.24, 1.64), (-1.45, 1.64))
                Line((-1.45, 1.64), (-1.45, -0.63))
                Line((-1.45, -0.63), (-0.63, -1.45))
                Line((-0.63, -1.45), (1.44, -1.45))
                Line((1.44, -1.45), (1.44, -1.15))
                Line((1.44, -1.15), (1.44, 0.94))
                Line((1.44, 0.94), (1.44, 1.44))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # Symmetric extrude, full_length=True, total=2.8875
        extrude(amount=1.44375, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 49 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5579060332, perimeter: 12.4376670256
            with BuildLine():
                Line((1.44, -1.15), (1.44, 0.94))
                CenterArc((1.64, -1.15), 0.2, 109.9225018722, 70.0774981278)
                Line((5.2422246415, 0.3683184563), (1.571850239, -0.9619691247))
                CenterArc((5.14, 0.6503647693), 0.3, -70.0774981278, 70.0774981278)
                Line((5.44, 1.54), (5.44, 0.6503647693))
                CenterArc((5.34, 1.54), 0.1, 0, 90)
                Line((5.04, 1.64), (5.34, 1.64))
                CenterArc((5.04, 1.54), 0.1, 90, 90)
                Line((4.94, 0.94), (4.94, 1.54))
                CenterArc((4.74, 0.94), 0.2, -90, 90)
                Line((1.64, 0.74), (4.74, 0.74))
                CenterArc((1.64, 0.94), 0.2, -180, 90)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is an oval or elliptical basin/container with a curved bottom, featuring a reinforced rim with vertical ribbing around the perimeter and internal cross-bracing or support structures visible through the open top.
def model_130917_2e98fb39_0000():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.7450173055, perimeter: 26.7035375555
            Circle(4.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a black plastic connector or clip component with an elongated body featuring two opposing curved flanges, a central slot or channel running lengthwise, and circular openings or holes on each end for fastening or assembly.
def model_130975_dfe64cd6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 94.4374418325, perimeter: 99.3854319816
            with BuildLine():
                CenterArc((-8, 0), 4, 74.7385195751, 225.2614804249)
                CenterArc((-6.5, -2.5980762114), 1, -60, 179.9999006802)
                CenterArc((-8, 0), 2, 0, 300.0000496599)
                CenterArc((5.1799497484, 4.3598994969), 12, -158.6954659384, 33.5573558172)
                CenterArc((0, -3), 3, -125.1379719553, 35.1379719553)
                Line((0, -6), (8.9970905626, -2.8294540834))
                CenterArc((8, 0), 3, 90, 199.4122945221)
                Line((8, 3), (3.8729833462, 3))
                CenterArc((3.8729833462, 4), 1, -165.5224878141, 75.5224878141)
                CenterArc((0, 3), 3, 14.4775121859, 120.2610073892)
                CenterArc((-5.6309792769, 8.6826114052), 5, -105.2614804249, 60)
            make_face()
            with BuildLine():
                CenterArc((-2.5, 0.8), 2.035849779, 110.8037765449, 92.3347981036)
                CenterArc((-5.531665636, 8.779331734), 6.5, -69.1962234551, 22.9418729712)
                CenterArc((0, 3), 1.5, 0, 133.7456495161)
                Line((1.5, -3), (1.5, 3))
                CenterArc((0, -3), 1.5, -125.1381561765, 125.1381561765)
                CenterArc((5.1799497484, 4.3598994969), 10.5, -151.549054452, 26.4108982755)
                CenterArc((5.1799497484, 4.3598994969), 10.5, -155.4662914801, 3.9172370281)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 21.2057504117, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((8, 0), 3, -70.5877054779, 160.5877054779)
                CenterArc((8, 0), 3, 90, 199.4122945221)
            make_face()
            with BuildLine():
                CenterArc((8, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular wedge or tapered block with a sloped top surface, featuring a prismatic shape that transitions from a thicker section on one end to a thinner edge on the opposite end, with clean planar faces and internal geometric divisions visible through the semi-transparent rendering.
def model_131394_cff473cf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 77.447997, perimeter: 35.204
            with BuildLine():
                Line((0, 0), (8.899, 0))
                Line((8.899, 0), (8.899, 8.703))
                Line((0, 8.703), (8.899, 8.703))
                Line((0, 0), (0, 8.703))
            make_face()
        # OneSide extrude, distance=2.783
        extrude(amount=2.783)
    return part.part


# Description: This is a tweezers or forceps tool with a hinged pivot design, featuring two elongated arms with tapered, pointed tips and a central fulcrum joint that allows the arms to open and close.
def model_131494_c8a441d0_0000():
    """Model: Nowy test v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.2361740347, perimeter: 34.6064811156
            with BuildLine():
                Line((0, -1.2), (7.6, -1.2000000179))
                Line((7.6000000001, -0.5636037861), (7.6, -1.2000000179))
                Line((7.6000000001, -0.5636037861), (3.2681968869, 3.7827865531))
                Line((3.0727763076, 3.7827865531), (3.2681968869, 3.7827865531))
                Line((3.0727763076, 3.7827865531), (0, 3.7827865531))
                Line((0, 3.7827865531), (0, 3.1800061274))
                Line((2.5994556208, 3.1800061274), (0, 3.1800061274))
                Line((5.3167619572, 0.4520261784), (2.5994556208, 3.1800061274))
                Line((5.3167619572, 0.4520261784), (6.0661852779, -0.3))
                Line((6.0661852779, -0.3), (0.8, -0.3))
                Line((0.8, -0.3), (0, -0.3))
                Line((0, -0.3), (0, -1.2))
            make_face()
            with BuildLine():
                CenterArc((7.1500001132, -0.75), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0727763076, 3.3327865531), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.64, perimeter: 3.2
            with BuildLine():
                Line((0.8, -0.3), (0, -0.3))
                Line((0.8, 0.5), (0.8, -0.3))
                Line((0, 0.5), (0.8, 0.5))
                Line((0, -0.3), (0, 0.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


# Description: This is a polymer or composite clamp or bracket with an angular, curved upper arm and a rectangular base, featuring a slot or opening on the side and designed for securing or holding components in place.
def model_131709_8b86dfb6_0000():
    """Model: light clip"""
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
        # Sketch has 24 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3100045276, perimeter: 2.2737326249
            with BuildLine():
                Line((0.8838834765, 0.8838834765), (1.0960155108, 1.0960155108))
                _nurbs_edge([(0.8838834765, 0.8838834765), (0.8780491971, 0.8977476371), (0.8664441413, 0.9263829896), (0.8492271108, 0.9720570624), (0.8266533399, 1.0384205633), (0.7993197367, 1.1302908297), (0.7735889128, 1.2302756841), (0.7509076379, 1.3365685596), (0.7336662221, 1.4459898707), (0.7255435008, 1.5534771691), (0.7305900182, 1.6528380669), (0.7521663881, 1.7376412081), (0.7918866183, 1.8020726843), (0.8485787887, 1.8417923552), (0.9170115515, 1.8549258752), (0.9894705262, 1.841425508), (1.0575045691, 1.8023437353), (1.1136346493, 1.7391755293), (1.1529498919, 1.6532459675), (1.1724648071, 1.5456877988), (1.1706571649, 1.4173963182), (1.1517186421, 1.2986896536), (1.1276772474, 1.200788439), (1.1072951689, 1.1315942708), (1.0960155108, 1.0960155108)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 2.5551079413, perimeter: 10.3761593792
            with BuildLine():
                Line((0, -3), (1, -3))
                Line((1, -3), (1, -1.1842719282))
                CenterArc((0, 0), 1.55, -49.8222304599, 94.8222304599)
                Line((0.8838834765, 0.8838834765), (1.0960155108, 1.0960155108))
                CenterArc((0, 0), 1.25, -90, 135)
                Line((0, -1.25), (0, -3))
            make_face()
            # Profile area: 2.5551079413, perimeter: 10.3761593792
            with BuildLine():
                Line((-0.8838834765, 0.8838834765), (-1.0960155108, 1.0960155108))
                CenterArc((0, 0), 1.55, 135, 94.8222304599)
                Line((-1, -3), (-1, -1.1842719282))
                Line((0, -3), (-1, -3))
                Line((0, -1.25), (0, -3))
                CenterArc((0, 0), 1.25, 135, 135)
            make_face()
            # Profile area: 0.3100045276, perimeter: 2.2737326249
            with BuildLine():
                _nurbs_edge([(-0.8838834765, 0.8838834765), (-0.8780491971, 0.8977476371), (-0.8664441413, 0.9263829896), (-0.8492271108, 0.9720570624), (-0.8266533399, 1.0384205633), (-0.7993197367, 1.1302908297), (-0.7735889128, 1.2302756841), (-0.7509076379, 1.3365685596), (-0.7336662221, 1.4459898707), (-0.7255435008, 1.5534771691), (-0.7305900182, 1.6528380669), (-0.7521663881, 1.7376412081), (-0.7918866183, 1.8020726843), (-0.8485787887, 1.8417923552), (-0.9170115515, 1.8549258752), (-0.9894705262, 1.841425508), (-1.0575045691, 1.8023437353), (-1.1136346493, 1.7391755293), (-1.1529498919, 1.6532459675), (-1.1724648071, 1.5456877988), (-1.1706571649, 1.4173963182), (-1.1517186421, 1.2986896536), (-1.1276772474, 1.200788439), (-1.1072951689, 1.1315942708), (-1.0960155108, 1.0960155108)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.8838834765, 0.8838834765), (-1.0960155108, 1.0960155108))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a curved sheet metal bracket or shield with two vertical flanges on the sides and a central rectangular cutout, designed to wrap around and protect or mount a cylindrical component.
def model_131823_4d7d57e7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.042034334, perimeter: 20.8203532403
            with BuildLine():
                CenterArc((0.0000005808, 0.0000005808), 3.9000005808, -168.7499932963, 146.2499932963)
                Line((-3.8250624934, -0.7608522359), (-4.0212196497, -0.7998703203))
                CenterArc((0, 0), 4.1, -168.75, 146.2500106041)
                Line((3.6031312941, -1.4924650277), (3.7879063737, -1.5690013716))
            make_face()
            # Profile area: 2.042034334, perimeter: 20.8203532403
            with BuildLine():
                CenterArc((0.0000005808, -0.0000005808), 3.9000005808, 22.5, 146.2499932963)
                Line((3.6031312941, 1.4924650277), (3.7879063737, 1.5690013716))
                CenterArc((0, 0), 4.1, 22.4999893959, 146.2500106041)
                Line((-3.8250624934, 0.7608522359), (-4.0212196497, 0.7998703203))
            make_face()
        # TwoSides extrude (symmetric), distance=2.25
        extrude(amount=2.25, both=True)
    return part.part


# Description: This is a rectangular box-shaped component with a sloped top surface featuring multiple parallel vertical slots or fins running across its length, and ribbed internal structure visible through cutout sections on the sides.
def model_131876_b2384623_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.5873982719, perimeter: 20.837167544
            with BuildLine():
                Line((-2.5, 1), (-2.5, -3.8))
                Line((-0.4, -3.8), (-2.5, -3.8))
                Line((-0.4, 1), (-0.4, -3.8))
                Line((-2.5, 1), (-0.4, 1))
            make_face()
            with BuildLine():
                CenterArc((-1.5000000224, 0), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5000000224, -3.5000000522), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5000000224, -3.0000000447), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5000000224, -2.5000000373), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5000000224, -2.0000000298), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5000000224, -1.5000000224), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5000000224, -1.0000000149), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5000000224, -0.5000000075), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.4, perimeter: 10.6
            with BuildLine():
                Line((-2.5, 1), (-3, 1))
                Line((-3, 1), (-3, -3.8))
                Line((-3, -3.8), (-2.5, -3.8))
                Line((-2.5, 1), (-2.5, -3.8))
            make_face()
            # Profile area: 2.4000000213, perimeter: 10.6000000596
            with BuildLine():
                Line((-0.4, 1), (-0.4, -3.8))
                Line((-0.4, -3.8), (0.1000000015, -3.8000000566))
                Line((0.1000000015, 1), (0.1000000015, -3.8000000566))
                Line((-0.4, 1), (0.1000000015, 1))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a coffin-shaped structural frame or bracket with an elongated hexagonal perimeter, featuring internal triangular bracing/webbing for reinforcement and a central oval cutout.
def model_132148_a107f53e_0001():
    """Model: Middle in wood"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 773.9776531589, perimeter: 443.1592631886
            with BuildLine():
                Line((14.1421356237, -35.3553390593), (35, -15))
                Line((35, -15), (35.3553390593, 14.1421356237))
                Line((35.3553390593, 14.1421356237), (15, 35))
                Line((15, 35), (-14.1421356237, 35.3553390593))
                Line((-14.1421356237, 35.3553390593), (-35, 15))
                Line((-35, 15), (-35.3553390593, -14.1421356237))
                Line((-35.3553390593, -14.1421356237), (-15, -35))
                Line((-15, -35), (14.1421356237, -35.3553390593))
            make_face()
            with BuildLine():
                Line((-31.8449581415, -12.7379832566), (-13.5106715091, -31.5249001879))
                Line((-31.5249001879, 13.5106715091), (-31.8449581415, -12.7379832566))
                Line((-12.7379832566, 31.8449581415), (-31.5249001879, 13.5106715091))
                Line((13.5106715091, 31.5249001879), (-12.7379832566, 31.8449581415))
                Line((31.8449581415, 12.7379832566), (13.5106715091, 31.5249001879))
                Line((31.5249001879, -13.5106715091), (31.8449581415, 12.7379832566))
                Line((12.7379832566, -31.8449581415), (31.5249001879, -13.5106715091))
                Line((-13.5106715091, -31.5249001879), (12.7379832566, -31.8449581415))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 637.2779620672, perimeter: 364.8886126923
            with BuildLine():
                Line((22.1314314009, -22.6778042491), (31.6849143879, -0.3863439461))
                Line((31.6849143879, -0.3863439461), (22.6778042491, 22.1314314009))
                Line((22.6778042491, 22.1314314009), (0.3863439461, 31.6849143879))
                Line((0.3863439461, 31.6849143879), (-22.1314314009, 22.6778042491))
                Line((-22.1314314009, 22.6778042491), (-31.6849143879, 0.3863439461))
                Line((-31.6849143879, 0.3863439461), (-22.6778042491, -22.1314314009))
                Line((-22.6778042491, -22.1314314009), (-0.3863439461, -31.6849143879))
                Line((-0.3863439461, -31.6849143879), (22.1314314009, -22.6778042491))
            make_face()
            with BuildLine():
                Line((19.9719810153, 19.4907991498), (10.1561139877, 23.6975993045))
                Line((23.9381902372, 9.5752760949), (19.9719810153, 19.4907991498))
                Line((27.9043994592, -0.34024696), (23.9381902372, 9.5752760949))
                Line((23.6975993045, -10.1561139877), (27.9043994592, -0.34024696))
                Line((19.4907991498, -19.9719810153), (23.6975993045, -10.1561139877))
                Line((9.5752760949, -23.9381902372), (19.4907991498, -19.9719810153))
                Line((-0.34024696, -27.9043994592), (9.5752760949, -23.9381902372))
                Line((-10.1561139877, -23.6975993045), (-0.34024696, -27.9043994592))
                Line((-19.9719810153, -19.4907991498), (-10.1561139877, -23.6975993045))
                Line((-23.9381902372, -9.5752760949), (-19.9719810153, -19.4907991498))
                Line((-27.9043994592, 0.34024696), (-23.9381902372, -9.5752760949))
                Line((-23.6975993045, 10.1561139877), (-27.9043994592, 0.34024696))
                Line((-19.4907991498, 19.9719810153), (-23.6975993045, 10.1561139877))
                Line((-9.5752760949, 23.9381902372), (-19.4907991498, 19.9719810153))
                Line((0.34024696, 27.9043994592), (-9.5752760949, 23.9381902372))
                Line((10.1561139877, 23.6975993045), (0.34024696, 27.9043994592))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 510.9842314283, perimeter: 292.576141671
            with BuildLine():
                Line((10.1561139877, 23.6975993045), (-9.5752760949, 23.9381902372))
                Line((-9.5752760949, 23.9381902372), (-23.6975993045, 10.1561139877))
                Line((-23.6975993045, 10.1561139877), (-23.9381902372, -9.5752760949))
                Line((-23.9381902372, -9.5752760949), (-10.1561139877, -23.6975993045))
                Line((-10.1561139877, -23.6975993045), (9.5752760949, -23.9381902372))
                Line((9.5752760949, -23.9381902372), (23.6975993045, -10.1561139877))
                Line((23.6975993045, -10.1561139877), (23.9381902372, 9.5752760949))
                Line((23.9381902372, 9.5752760949), (10.1561139877, 23.6975993045))
            make_face()
            with BuildLine():
                Line((14.5472974081, 14.1968116101), (8.6667854967, 20.2224994924))
                Line((20.4278093195, 8.1711237278), (14.5472974081, 14.1968116101))
                Line((20.3251544059, -0.2478308845), (20.4278093195, 8.1711237278))
                Line((20.2224994924, -8.6667854967), (20.3251544059, -0.2478308845))
                Line((14.1968116101, -14.5472974081), (20.2224994924, -8.6667854967))
                Line((8.1711237278, -20.4278093195), (14.1968116101, -14.5472974081))
                Line((-0.2478308845, -20.3251544059), (8.1711237278, -20.4278093195))
                Line((-8.6667854967, -20.2224994924), (-0.2478308845, -20.3251544059))
                Line((-14.5472974081, -14.1968116101), (-8.6667854967, -20.2224994924))
                Line((-20.4278093195, -8.1711237278), (-14.5472974081, -14.1968116101))
                Line((-20.3251544059, 0.2478308845), (-20.4278093195, -8.1711237278))
                Line((-20.2224994924, 8.6667854967), (-20.3251544059, 0.2478308845))
                Line((-14.1968116101, 14.5472974081), (-20.2224994924, 8.6667854967))
                Line((-8.1711237278, 20.4278093195), (-14.1968116101, 14.5472974081))
                Line((0.2478308845, 20.3251544059), (-8.1711237278, 20.4278093195))
                Line((8.6667854967, 20.2224994924), (0.2478308845, 20.3251544059))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 394.3040386066, perimeter: 225.768129749
            with BuildLine():
                Line((14.5472974081, 14.1968116101), (0.2478308845, 20.3251544059))
                Line((0.2478308845, 20.3251544059), (-14.1968116101, 14.5472974081))
                Line((-14.1968116101, 14.5472974081), (-20.3251544059, 0.2478308845))
                Line((-20.3251544059, 0.2478308845), (-14.5472974081, -14.1968116101))
                Line((-14.5472974081, -14.1968116101), (-0.2478308845, -20.3251544059))
                Line((-0.2478308845, -20.3251544059), (14.1968116101, -14.5472974081))
                Line((14.1968116101, -14.5472974081), (20.3251544059, -0.2478308845))
                Line((20.3251544059, -0.2478308845), (14.5472974081, 14.1968116101))
            make_face()
            with BuildLine():
                Line((-6.0216040364, -14.0504094182), (-0.2017338985, -16.5446394773))
                Line((-11.8414741742, -11.5561793591), (-6.0216040364, -14.0504094182))
                Line((-14.1930568258, -5.6772227303), (-11.8414741742, -11.5561793591))
                Line((-16.5446394773, 0.2017338985), (-14.1930568258, -5.6772227303))
                Line((-14.0504094182, 6.0216040364), (-16.5446394773, 0.2017338985))
                Line((-11.5561793591, 11.8414741742), (-14.0504094182, 6.0216040364))
                Line((-5.6772227303, 14.1930568258), (-11.5561793591, 11.8414741742))
                Line((0.2017338985, 16.5446394773), (-5.6772227303, 14.1930568258))
                Line((6.0216040364, 14.0504094182), (0.2017338985, 16.5446394773))
                Line((11.8414741742, 11.5561793591), (6.0216040364, 14.0504094182))
                Line((14.1930568258, 5.6772227303), (11.8414741742, 11.5561793591))
                Line((16.5446394773, -0.2017338985), (14.1930568258, 5.6772227303))
                Line((14.0504094182, -6.0216040364), (16.5446394773, -0.2017338985))
                Line((11.5561793591, -11.8414741742), (14.0504094182, -6.0216040364))
                Line((5.6772227303, -14.1930568258), (11.5561793591, -11.8414741742))
                Line((-0.2017338985, -16.5446394773), (5.6772227303, -14.1930568258))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 286.5055966092, perimeter: 164.0455749265
            with BuildLine():
                Line((-6.0216040364, -14.0504094182), (5.6772227303, -14.1930568258))
                Line((5.6772227303, -14.1930568258), (14.0504094182, -6.0216040364))
                Line((14.0504094182, -6.0216040364), (14.1930568258, 5.6772227303))
                Line((14.1930568258, 5.6772227303), (6.0216040364, 14.0504094182))
                Line((6.0216040364, 14.0504094182), (-5.6772227303, 14.1930568258))
                Line((-5.6772227303, 14.1930568258), (-14.0504094182, 6.0216040364))
                Line((-14.0504094182, 6.0216040364), (-14.1930568258, -5.6772227303))
                Line((-14.1930568258, -5.6772227303), (-6.0216040364, -14.0504094182))
            make_face()
            with BuildLine():
                Line((10.682675908, 4.2730703632), (4.5322755454, 10.575309606))
                Line((10.575309606, -4.5322755454), (10.682675908, 4.2730703632))
                Line((4.2730703632, -10.682675908), (10.575309606, -4.5322755454))
                Line((-4.5322755454, -10.575309606), (4.2730703632, -10.682675908))
                Line((-10.682675908, -4.2730703632), (-4.5322755454, -10.575309606))
                Line((-10.575309606, 4.5322755454), (-10.682675908, -4.2730703632))
                Line((-4.2730703632, 10.682675908), (-10.575309606, 4.5322755454))
                Line((4.5322755454, 10.575309606), (-4.2730703632, 10.682675908))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5)
    return part.part


# Description: This is a curved duct or cowling component with a streamlined, asymmetrical shape featuring a rounded left side, a flat bottom edge, an angled right end with a triangular flange or lip, and what appears to be an open interior channel or slot running along its length.
def model_132863_90d729e2_0001():
    """Model: Eindstukje"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0487478566, perimeter: 1.7218696416
            with BuildLine():
                Line((23.0604431222, 0.7398117745), (23.0604431222, 1.5398117745))
                Line((23.0604431222, 1.5398117745), (22.9995083015, 1.5398117745))
                Line((22.9995083015, 1.5398117745), (22.9995083015, 0.7398117745))
                Line((22.9995083015, 0.7398117745), (23.0604431222, 0.7398117745))
            make_face()
            # Profile area: 1.1708953768, perimeter: 4.3562276035
            with BuildLine():
                Line((22.9995083015, 1.5398117745), (22.9995083015, 0.7398117745))
                Line((22.9995083015, 1.5398117745), (21.8354431222, 1.5398117745))
                CenterArc((21.8354431222, 1.1648117745), 0.375, 90, 90)
                Line((21.4604431222, 1.1648117745), (21.4604431222, 1.1148117745))
                CenterArc((21.8354431222, 1.1148117745), 0.375, -180, 90)
                Line((21.8354431222, 0.7398117745), (22.9995083015, 0.7398117745))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0487478566, perimeter: 1.7218696416
            with BuildLine():
                Line((23.0604431222, 0.7398117745), (23.0604431222, 1.5398117745))
                Line((23.0604431222, 1.5398117745), (22.9995083015, 1.5398117745))
                Line((22.9995083015, 1.5398117745), (22.9995083015, 0.7398117745))
                Line((22.9995083015, 0.7398117745), (23.0604431222, 0.7398117745))
            make_face()
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45, mode=Mode.ADD)
    return part.part


# Description: This is a black cable tray cover with an elongated, slightly curved channel shape designed to snap or clip over cable trays, featuring textured grip surfaces on both ends and a protective hood-like top.
def model_133072_95309b10_0000():
    """Model: Blade"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1073080483, perimeter: 2.4727365861
            with BuildLine():
                CenterArc((0.7818181935, 0.0715909102), 0.0738636375, -75.7499673022, 98.3698322502)
                CenterArc((0.400000006, -0.0875000013), 0.4875000073, 22.619864948, 134.7602701039)
                CenterArc((0.0181818185, 0.0715909102), 0.0738636375, 157.380135052, 98.3698322502)
                CenterArc((0.400000006, -0.1166666684), 0.4166666729, 16.2602047083, 147.4795905834)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a polyhedron or irregular geometric solid with an angular, faceted structure featuring multiple planar surfaces, internal geometric divisions, and a complex non-uniform shape with no obvious holes or slots.
def model_133248_c7255340_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.892, perimeter: 19.96
            with BuildLine():
                Line((5.18, -5), (0.1, -5))
                Line((5.18, -0.1), (5.18, -5))
                Line((0.1, -0.1), (5.18, -0.1))
                Line((0.1, -5), (0.1, -0.1))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.036, perimeter: 40.72
            with BuildLine():
                Line((5.28, -5.1), (0, -5.1))
                Line((5.28, 0), (5.28, -5.1))
                Line((0, 0), (5.28, 0))
                Line((0, -5.1), (0, 0))
            make_face()
            with BuildLine():
                Line((0.1, -5), (0.1, -0.1))
                Line((0.1, -0.1), (5.18, -0.1))
                Line((5.18, -0.1), (5.18, -5))
                Line((5.18, -5), (0.1, -5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.9
        extrude(amount=5.9, mode=Mode.ADD)
    return part.part


# Description: This is a bicycle wheel rim with an elliptical/oval shape, featuring a hollow spoke structure with radial tensioning wires connecting the outer rim to a central hub area, designed for lightweight strength and aerodynamic performance.
def model_133249_b81dc8d6_0000():
    """Model: lid v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9762827633, perimeter: 41.4690230274
            with BuildLine():
                CenterArc((0, 0), 3.42, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.18, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.4947076679, perimeter: 38.8300851984
            with BuildLine():
                CenterArc((0, 0), 3.18, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4947076679, perimeter: 38.8300851984
            with BuildLine():
                CenterArc((0, 0), 3.18, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a long, slender rectangular bar or rail with a hexagonal/beveled cross-section, featuring a central slot or groove running along its length and angled end caps on both sides.
def model_133402_47273d61_0020():
    """Model: Mid Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 125.8062, perimeter: 104.14
            with BuildLine():
                Line((103.505, -62.23), (53.975, -62.23))
                Line((103.505, -59.69), (103.505, -62.23))
                Line((53.975, -59.69), (103.505, -59.69))
                Line((53.975, -62.23), (53.975, -59.69))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a curved blade or fin component with an elongated, crescent-like shape featuring a tapered profile and a textured or dimpled surface along its upper edge.
def model_133424_315bcaeb_0001():
    """Model: curvey pull left v1"""
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
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.2135781836, perimeter: 27.0819760795
            with BuildLine():
                _nurbs_edge([(12.9264790981, 0.8765059763), (12.5572337791, 0.9466887212), (11.8261441536, 1.083345447), (10.7517146172, 1.2771997586), (9.3642657936, 1.5130838027), (7.7122037849, 1.7649151552), (6.1550578738, 1.9623231902), (4.7119052182, 2.084415937), (3.4054931075, 2.1025813947), (2.2643377866, 1.9712779884), (1.3084357691, 1.6475499316), (0.6898269802, 1.2312274299), (0.3053866095, 0.8318345405), (0.0837840206, 0.5276125734), (-0.0183400078, 0.3660030223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (-0.0183400078, 0.3660030223))
                _nurbs_edge([(0, 0), (0.0935540425, 0.0428713349), (0.29544648, 0.1250701824), (0.6426301151, 0.2377389237), (1.1957613221, 0.3663381731), (2.0447762725, 0.4893101519), (3.0578003195, 0.5729690074), (4.230796357, 0.6182824376), (5.5491917825, 0.6287435079), (6.9960433746, 0.6084135233), (8.5552678601, 0.5611476582), (9.8826786256, 0.5041514234), (10.9198976054, 0.4514180919), (11.6295923514, 0.4118962841), (11.9889936344, 0.391043804)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((12.9264790981, 0.8765059763), (11.9889936344, 0.391043804))
            make_face()
        # OneSide extrude, distance=1.1176
        extrude(amount=1.1176)
    return part.part


# Description: This is a split retaining ring or snap ring with a circular band shape featuring a radial slot or gap on one side for elastic compression and insertion onto shafts or into grooves.
def model_133564_b5340c41_0004():
    """Model: aftercooler"""
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
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0351638358, perimeter: 1.3728375237
            with BuildLine():
                CenterArc((0, 0), 1.5, 178.9239735597, 2.1097229818)
                Line((-1.4997354857, 0.0281686504), (-2.105903095, 0.0281686504))
                _nurbs_edge([(-2.105903095, 0.0281686504), (-2.1092583104, 0.0281686504), (-2.1155792158, 0.0277722795), (-2.1238920547, 0.0259886959), (-2.1326791512, 0.0214308733), (-2.1400155108, 0.0131907924), (-2.1438917989, 0.0037683266), (-2.1444781948, -0.0054875283), (-2.1419429274, -0.0134992477), (-2.1365159274, -0.0197560575), (-2.1284127736, -0.0241203944), (-2.119911964, -0.0261455116), (-2.1124354555, -0.0268942556), (-2.1069634328, -0.0270606441), (-2.1041054965, -0.0270606441)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-1.4997558873, -0.0270606441), (-2.1041054965, -0.0270606441))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3430308594, perimeter: 17.9070781255
            with BuildLine():
                CenterArc((0, 0), 1.5, -178.9663034586, 357.8902770182)
                CenterArc((0, 0), 1.5, 178.9239735597, 2.1097229818)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: A cylindrical rod or bar with rounded ends, featuring a smooth, elongated rectangular profile with hemispherical or rounded terminals at both ends.
def model_133596_89dea5d1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Horizontal Pipe -> Horizontal pipe (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.777858341, perimeter: 19.4464585257
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=43.3
        extrude(amount=21.65, both=True)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a uniform thickness, featuring a slightly beveled or angled edge along one side and a clean, simple geometric form suitable for structural or assembly applications.
def model_133634_76b946d7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((2, -2), (2, 2))
                Line((2, 2), (-2, 2))
                Line((-2, 2), (-2, -2))
                Line((-2, -2), (2, -2))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is an L-shaped bracket or angle bracket with two perpendicular flat planes connected at a 90-degree angle, featuring triangulated internal geometry and a dark edge reinforcement along the bend.
def model_133710_00be7f31_0004():
    """Model: Colchoneta"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 438.2237519386, perimeter: 227.1150829816
            with BuildLine():
                Line((-82.7791933585, 43.4474557752), (-22.7809060963, 43.0037868829))
                Line((-22.7809060963, 43.0037868829), (-15.0482224264, 62.2761812912))
                Line((-15.0482224264, 62.2761812912), (-3.3170539653, 91.5141166708))
                Line((-3.3170539653, 91.5141166708), (-7.029382714, 93.0036183531))
                Line((-7.029382714, 93.0036183531), (-25.477942832, 47.0237306405))
                Line((-82.7791933585, 47.4474557752), (-25.477942832, 47.0237306405))
                Line((-82.7791933585, 43.4474557752), (-82.7791933585, 47.4474557752))
            make_face()
        # OneSide extrude, distance=-57
        extrude(amount=-57)
    return part.part


# Description: This is a long, narrow rectangular tray or pan with a shallow depth, featuring beveled or angled edges on the sides and a slightly recessed central surface.
def model_133710_00be7f31_0005():
    """Model: Travesaño delantero"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.4194147129, perimeter: 17.6358806111
            with BuildLine():
                Line((-79.2345815527, 9.3980663087), (-84.9795884316, 9.3980663087))
                Line((-79.2345815527, 9.3980663087), (-78.9177872917, 12.3980663087))
                Line((-78.9177872917, 12.3980663087), (-84.7857235547, 12.3980663087))
                Line((-84.9795884316, 9.3980663087), (-84.7857235547, 12.3980663087))
            make_face()
        # OneSide extrude, distance=-57
        extrude(amount=-57)
    return part.part


# Description: This is a wing or airfoil component featuring a streamlined, elongated shape with curved aerodynamic surfaces, two circular end plates or flanges, and internal structural ribbing that provides stiffness while minimizing weight.
def model_133824_6521bcf0_0000():
    """Model: Estructura 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 294.5398163397, perimeter: 91.4159265359
            with BuildLine():
                Line((0, 0), (-3, 0))
                Line((-3, 0), (-3, -3))
                Line((-3, -3), (0, -3))
                CenterArc((5, -3), 5, 180, 180)
                Line((13, -3), (10, -3))
                Line((13, 0), (13, -3))
                Line((10, 0), (13, 0))
                Line((10, 12), (10, 0))
                Line((13, 12), (10, 12))
                Line((13, 15), (13, 12))
                Line((10, 15), (13, 15))
                CenterArc((5, 15), 5, 0, 180)
                Line((-3, 15), (0, 15))
                Line((-3, 12), (-3, 15))
                Line((0, 12), (-3, 12))
                Line((0, 0), (0, 12))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a circular disk or plate with a flat face and reinforced rim edge, featuring a slightly beveled or flanged perimeter that provides structural rigidity.
def model_133841_1a1b322e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 13.7824443112, perimeter: 13.1603686569
            with Locations((-8.8900002837, 0)):
                Circle(2.0945377247)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is an elongated hexagonal prism or wedge-shaped component with a tapered left end, featuring a flat bottom face and angled top surfaces that converge toward the narrow end.
def model_134027_a6a95d00_0000():
    """Model: Rigid joint"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.9031996124, perimeter: 15.2399997711
            with BuildLine():
                Line((-3.8099999428, 2.5399999619), (-3.8099999428, 0))
                Line((-3.8099999428, 0), (1.2699999809, 0))
                Line((1.2699999809, 0), (1.2699999809, 2.5399999619))
                Line((1.2699999809, 2.5399999619), (-3.8099999428, 2.5399999619))
            make_face()
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)
    return part.part


# Description: This is a rectangular tray or channel with two vertical flanges on opposite ends and an open top, featuring a sloped interior base and a recessed central cavity.
def model_134027_a6a95d00_0004():
    """Model: Bridge"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((-20.799588147, 2.415929119), (-22.069588147, 2.415929119))
                Line((-22.069588147, 2.415929119), (-22.069588147, 1.145929119))
                Line((-22.069588147, 1.145929119), (-20.799588147, 1.145929119))
                Line((-20.799588147, 1.145929119), (-20.799588147, 2.415929119))
            make_face()
            # Profile area: 12.9032, perimeter: 22.86
            with BuildLine():
                Line((-22.069588147, 1.145929119), (-20.799588147, 1.145929119))
                Line((-22.069588147, 1.145929119), (-22.069588147, -0.124070881))
                Line((-22.069588147, -0.124070881), (-11.909588147, -0.124070881))
                Line((-11.909588147, -0.124070881), (-11.909588147, 1.145929119))
                Line((-11.909588147, 1.145929119), (-13.179588147, 1.145929119))
                Line((-13.179588147, 1.145929119), (-20.799588147, 1.145929119))
            make_face()
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((-11.909588147, 1.145929119), (-13.179588147, 1.145929119))
                Line((-11.909588147, 2.415929119), (-11.909588147, 1.145929119))
                Line((-13.179588147, 2.415929119), (-11.909588147, 2.415929119))
                Line((-13.179588147, 1.145929119), (-13.179588147, 2.415929119))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a U-shaped channel or trough with cylindrical posts at each corner, featuring a ribbed/grooved base surface and raised flanged edges, designed for structural support or component mounting.
def model_134497_43d339c0_0000():
    """Model: saddle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.660292984, perimeter: 3.3942502087
            with BuildLine():
                CenterArc((-3.175, 0), 0.635, 84.2608295227, 191.4783409545)
                CenterArc((0, 0), 3.175, -180, 11.4783409545)
                CenterArc((0, 0), 3.175, 168.5216590455, 11.4783409545)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124868
            with BuildLine():
                Line((-2.54, 0.0000000073), (-3.175, 0))
                CenterArc((0, 0), 3.175, -180, 11.4783409545)
                CenterArc((-3.175, 0), 0.635, -84.2608295227, 84.2608301841)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124795
            with BuildLine():
                Line((2.54, 0), (3.175, 0))
                CenterArc((3.175, 0), 0.635, -180, 84.2608295227)
                CenterArc((0, 0), 3.175, -11.4783409545, 11.4783409545)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124795
            with BuildLine():
                CenterArc((0, 0), 3.175, 0, 11.4783409545)
                CenterArc((3.175, 0), 0.635, 95.7391704773, 84.2608295227)
                Line((2.54, 0), (3.175, 0))
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124721
            with BuildLine():
                CenterArc((0, 0), 3.175, 168.5216590455, 11.4783409545)
                Line((-2.54, 0.0000000073), (-3.175, 0))
                CenterArc((-3.175, 0), 0.635, 0.0000006614, 84.2608288614)
            make_face()
            # Profile area: 5.0939834261, perimeter: 18.549774484
            with BuildLine():
                CenterArc((0, 0), 2.54, -180, 180)
                CenterArc((-3.175, 0), 0.635, -84.2608295227, 84.2608301841)
                CenterArc((0, 0), 3.175, -168.5216590455, 157.0433180909)
                CenterArc((3.175, 0), 0.635, -180, 84.2608295227)
            make_face()
            # Profile area: 0.660292984, perimeter: 3.3942502087
            with BuildLine():
                CenterArc((0, 0), 3.175, -11.4783409545, 11.4783409545)
                CenterArc((3.175, 0), 0.635, -95.7391704773, 191.4783409545)
                CenterArc((0, 0), 3.175, 0, 11.4783409545)
            make_face()
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3032378569, perimeter: 2.2049124795
            with BuildLine():
                Line((2.54, 0), (3.175, 0))
                CenterArc((3.175, 0), 0.635, -180, 84.2608295227)
                CenterArc((0, 0), 3.175, -11.4783409545, 11.4783409545)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124795
            with BuildLine():
                CenterArc((0, 0), 3.175, 0, 11.4783409545)
                CenterArc((3.175, 0), 0.635, 95.7391704773, 84.2608295227)
                Line((2.54, 0), (3.175, 0))
            make_face()
            # Profile area: 0.660292984, perimeter: 3.3942502087
            with BuildLine():
                CenterArc((0, 0), 3.175, -11.4783409545, 11.4783409545)
                CenterArc((3.175, 0), 0.635, -95.7391704773, 191.4783409545)
                CenterArc((0, 0), 3.175, 0, 11.4783409545)
            make_face()
            # Profile area: 0.660292984, perimeter: 3.3942502087
            with BuildLine():
                CenterArc((-3.175, 0), 0.635, 84.2608295227, 191.4783409545)
                CenterArc((0, 0), 3.175, -180, 11.4783409545)
                CenterArc((0, 0), 3.175, 168.5216590455, 11.4783409545)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124868
            with BuildLine():
                Line((-2.54, 0.0000000073), (-3.175, 0))
                CenterArc((0, 0), 3.175, -180, 11.4783409545)
                CenterArc((-3.175, 0), 0.635, -84.2608295227, 84.2608301841)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124721
            with BuildLine():
                CenterArc((0, 0), 3.175, 168.5216590455, 11.4783409545)
                Line((-2.54, 0.0000000073), (-3.175, 0))
                CenterArc((-3.175, 0), 0.635, 0.0000006614, 84.2608288614)
            make_face()
        # Symmetric extrude, each_side=0.98298
        extrude(amount=0.98298, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or blade with a tapered profile, featuring a subtle curved or beveled edge along its length and a streamlined, aerodynamic form.
def model_135006_db473e01_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 140, perimeter: 51
            with BuildLine():
                Line((-4, 8.75), (4, 8.75))
                Line((-4, -8.75), (-4, 8.75))
                Line((4, -8.75), (-4, -8.75))
                Line((4, 8.75), (4, -8.75))
            make_face()
        # OneSide extrude, distance=0.175
        extrude(amount=0.175)
    return part.part


# Description: This is a cylindrical housing or sleeve component with a split or open vertical slot, featuring a curved top, ribbed/finned exterior surfaces on the sides, and internal structural details visible through the opening.
def model_135996_868f18fc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4137166941, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.7, 139.9947991151, 80.0104017697)
                CenterArc((0, 0), 0.7, -139.9947991151, 9.9895982303)
                CenterArc((0, 0), 0.7, -130.0052008849, 80.0104017697)
                CenterArc((0, 0), 0.7, -49.9947991151, 9.9895982303)
                CenterArc((0, 0), 0.7, -40.0052008849, 80.0104017697)
                CenterArc((0, 0), 0.7, 40.0052008849, 9.9895982303)
                CenterArc((0, 0), 0.7, 49.9947991151, 80.0104017697)
                CenterArc((0, 0), 0.7, 130.0052008849, 9.9895982303)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1627839211, perimeter: 7.8027513691
            with BuildLine():
                Line((0.5361902647, -0.45), (1.4, -0.45))
                Line((1.4, -0.45), (1.4, -1.1313708499))
                CenterArc((0, 0), 1.8, -38.942441269, 77.884882538)
                Line((1.4, 1.1313708499), (1.4, 0.45))
                Line((0.5361902647, 0.45), (1.4, 0.45))
                CenterArc((0, 0), 0.7, -40.0052008849, 80.0104017697)
            make_face()
            with BuildLine():
                CenterArc((1.2, 0), 0.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1627839211, perimeter: 7.8027513691
            with BuildLine():
                Line((-1.4, 0.45), (-1.4, 1.1313708499))
                CenterArc((0, 0), 1.8, 141.057558731, 77.884882538)
                Line((-1.4, -1.1313708499), (-1.4, -0.45))
                Line((-0.5361902647, -0.45), (-1.4, -0.45))
                CenterArc((0, 0), 0.7, 139.9947991151, 80.0104017697)
                Line((-0.5361902647, 0.45), (-1.4, 0.45))
            make_face()
            with BuildLine():
                CenterArc((-1.2, 0), 0.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1627839211, perimeter: 7.8027513691
            with BuildLine():
                CenterArc((0, 0), 0.7, 49.9947991151, 80.0104017697)
                Line((0.45, 1.4), (0.45, 0.5361902647))
                Line((0.45, 1.4), (1.1313708499, 1.4))
                CenterArc((0, 0), 1.8, 51.057558731, 77.884882538)
                Line((-1.1313708499, 1.4), (-0.45, 1.4))
                Line((-0.45, 1.4), (-0.45, 0.5361902647))
            make_face()
            with BuildLine():
                CenterArc((0, 1.2000438543), 0.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1627839211, perimeter: 7.8027513691
            with BuildLine():
                Line((-0.45, -0.5361902647), (-0.45, -1.4))
                Line((-0.45, -1.4), (-1.1313708499, -1.4))
                CenterArc((0, 0), 1.8, -128.942441269, 77.884882538)
                Line((1.1313708499, -1.4), (0.45, -1.4))
                Line((0.45, -0.5361902647), (0.45, -1.4))
                CenterArc((0, 0), 0.7, -130.0052008849, 80.0104017697)
            make_face()
            with BuildLine():
                CenterArc((0, -1.2), 0.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical disc or pulley with a flat front face and a textured or ribbed cylindrical edge, featuring a curved rim design typical of a wheel, gear, or mechanical transmission component.
def model_136120_901bb8da_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is an elongated linear guide rail or channel with a rectangular profile, featuring a central recessed slot running its length, black end caps, and blue-gray anodized surfaces typical of aluminum extrusion components used in machinery or automation systems.
def model_136341_7052a4b8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.4236467852, perimeter: 32.9707816311
            with BuildLine():
                Line((0, 11.8), (0, 0))
                Line((0, 0), (0.5, 0))
                Line((0.5, 0), (0.5, 0.5))
                CenterArc((0.75, 0.5), 0.25, 0, 180)
                Line((1, 0.5), (1, 0))
                Line((1, 0), (3.4, 0))
                Line((3.4, 0), (3.4, 11.8))
                Line((3.4, 11.8), (1.9, 11.8))
                Line((1.2000146959, 11.8), (1.9, 11.8))
                Line((1.2, 11.3), (1.2000146959, 11.8))
                CenterArc((0.95, 11.3), 0.25, 180, 180)
                Line((0.7, 11.8), (0.7, 11.3))
                Line((0, 11.8), (0.7, 11.8))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular prism or block with a diagonal slot or groove cut through one of its vertical faces, creating an angled chamfered or beveled edge along the length of the part.
def model_136804_344e4929_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (1, 0))
                Line((1, 0), (1, 2))
                Line((1, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a bolt or fastener with a hexagonal head on one end and a cylindrical shaft that tapers to a rounded tip, featuring a threaded or smooth cylindrical body.
def model_136821_0f4b88d0_0002():
    """Model: Bolt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=23
        extrude(amount=23)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.8357293382, perimeter: 23.5619449019
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or dodecahedral solid block with two large cylindrical holes drilled through it and curved or saddle-shaped internal surfaces connecting them.
def model_136821_0f4b88d0_0005():
    """Model: bolt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.1083310657, perimeter: 30.2093876516
            with BuildLine():
                Line((3.4637710933, -0.0478519906), (1.7733265861, 2.9757877644))
                Line((1.7733265861, 2.9757877644), (-1.6904445072, 3.023639755))
                Line((-1.6904445072, 3.023639755), (-3.4637710933, 0.0478519906))
                Line((-3.4637710933, 0.0478519906), (-1.7733265861, -2.9757877644))
                Line((-1.7733265861, -2.9757877644), (1.6904445072, -3.023639755))
                Line((1.6904445072, -3.023639755), (3.4637710933, -0.0478519906))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a molded plastic handle or grip featuring an elongated tapered body with a circular opening at one end and a curved, ergonomic design with textured surfaces for enhanced grip.
def model_137098_0a45d1c8_0000():
    """Model: Servo Motor Clip"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6672142311, perimeter: 5.8587446861
            with BuildLine():
                Line((-1.5044051848, 0.19995148), (-0.0351439064, 0.3482311113))
                CenterArc((-1.5, 0), 0.2, 91.2620945373, 177.4758109254)
                Line((-1.5044051848, -0.19995148), (-0.0351439064, -0.3482311113))
                CenterArc((0, 0), 0.3500000015, 95.7628474185, 168.474305163)
            make_face()
            with BuildLine():
                CenterArc((-1.5, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.6, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1884955625, perimeter: 3.7699111937
            with BuildLine():
                CenterArc((0, 0), 0.3500000015, 95.7628474185, 168.474305163)
                CenterArc((0, 0), 0.3500000015, -95.7628474185, 191.525694837)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.2
        extrude(amount=0.1, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1884955625, perimeter: 3.7699111937
            with BuildLine():
                CenterArc((0, 0), 0.3500000015, 95.7628474185, 168.474305163)
                CenterArc((0, 0), 0.3500000015, -95.7628474185, 191.525694837)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.4
        extrude(amount=0.2, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a simple cylindrical rod or shaft with a straight, tapered appearance, featuring a uniform diameter along its length with slightly angled ends.
def model_137098_0a45d1c8_0008():
    """Model: Connecting Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0063617251, perimeter: 0.2827433388
            Circle(0.045)
        # Symmetric extrude, full_length=True, total=6.8
        extrude(amount=3.4, both=True)
    return part.part


# Description: This is a cylindrical tube or shaft with a hexagonal blue head or connector at the top end, featuring a dark gray body and tapered or beveled edges on the upper component.
def model_137099_58f819ec_0001():
    """Model: Long Screw"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1154196045, perimeter: 3.6492572959
            with BuildLine():
                Line((0.2439324686, -0.245961279), (0.3349749502, 0.0882710752))
                Line((0.3349749502, 0.0882710752), (0.0910424816, 0.3342323541))
                Line((0.0910424816, 0.3342323541), (-0.2439324686, 0.245961279))
                Line((-0.2439324686, 0.245961279), (-0.3349749502, -0.0882710752))
                Line((-0.3349749502, -0.0882710752), (-0.0910424816, -0.3342323541))
                Line((-0.0910424816, -0.3342323541), (0.2439324686, -0.245961279))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-4.3
        extrude(amount=-4.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical knurled knob or wheel with a flat circular face and a textured grip surface on the curved edge, commonly used as a manual control handle or adjustment dial.
def model_137189_cdfeb18a_0000():
    """Model: Healical Gear (26R@0.00)"""
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
        # Gear (0.060 module; 1.560 pitch dia) -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.5614500887, perimeter: 4.4296456416
            Circle(0.705)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical component with a fine mesh or lattice pattern covering its curved surface and a solid circular base, featuring a tapered or conical top section.
def model_137209_c0c9a7dd_0001():
    """Model: pin1"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2.4534515988, 0)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular box or enclosure with a sloped/angled top surface, featuring multiple horizontal slot cutouts or vents along the upper portion, and appears to be designed as a housing or container component with ventilation features.
def model_137348_de92dc85_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7075180715, perimeter: 4.14969736
            with BuildLine():
                Line((-0.9693730447, -0.1611717963), (-0.9693730447, 0.384145263))
                Line((-0.9693730447, 0.384145263), (-0.7709997562, 0.5825185515))
                Line((-0.7709997562, 0.5825185515), (-0.370293573, 0.5825185515))
                Line((-0.370293573, 0.5825185515), (-0.370293573, 0.8420726095))
                Line((-1.5000000224, 0.8420726412), (-0.370293573, 0.8420726095))
                Line((-1.5000000224, -0.1611717963), (-1.5000000224, 0.8420726412))
                Line((-0.9693730447, -0.1611717963), (-1.5000000224, -0.1611717963))
            make_face()
            # Profile area: 0.7075180715, perimeter: 4.1496974234
            with BuildLine():
                Line((-1.5000000224, 0.8420726412), (-0.370293573, 0.8420726095))
                Line((-0.370293573, 1.1016267309), (-0.370293573, 0.8420726095))
                Line((-0.7709997562, 1.1016267309), (-0.370293573, 1.1016267309))
                Line((-0.9693730447, 1.3000000194), (-0.7709997562, 1.1016267309))
                Line((-0.9693730447, 1.8453170787), (-0.9693730447, 1.3000000194))
                Line((-0.9693730447, 1.8453170787), (-1.5000000224, 1.8453170787))
                Line((-1.5000000224, 1.8453170787), (-1.5000000224, 0.8420726412))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a rubber drive belt featuring a continuous loop design with a textured inner surface for grip and a smooth outer surface, used to transmit power between rotating shafts in mechanical systems.
def model_137447_6c8e2c63_0000():
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
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.704331275, perimeter: 74.20672302
            with BuildLine():
                _nurbs_edge([(-1.5075129477, 0.7732910317), (-1.865021086, 1.584174256), (-2.2770980426, 2.2041999076), (-2.7472257006, 2.6270915342), (-3.1883227874, 3.0238694334), (-3.6835521379, 3.2439152543), (-4.2022743945, 3.2839452623), (-4.7942890839, 3.3296312771), (-5.4144600277, 3.1410612046), (-5.9708018961, 2.7807619193), (-6.611833112, 2.3656159414), (-7.1642574534, 1.7262611113), (-7.4551483443, 0.9812268661), (-7.6720490635, 0.425697392), (-7.7409036158, -0.1879681304), (-7.6233037623, -0.8177836732), (-7.4782938362, -1.5943960798), (-7.0526547252, -2.3932870135), (-6.3463401175, -3.1844820784), (-5.3208493453, -4.3332098963), (-3.7102282524, -5.4696608916), (-1.5459326626, -6.5888267443), (-1.5337729733, -6.595114568), (-1.5216132841, -6.6014023916), (-1.5094535949, -6.6076902152)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0117745848, 0.0117745848, 0.0117745848, 0.0117745848, 0.1361678114, 0.1361678114, 0.1361678114, 0.2528797064, 0.2528797064, 0.2528797064, 0.3860823122, 0.3860823122, 0.3860823122, 0.5395617342, 0.5395617342, 0.5395617342, 0.6540025711, 0.6540025711, 0.6540025711, 0.7951171796, 0.7951171796, 0.7951171796, 1, 1, 1, 1.0011545932, 1.0011545932, 1.0011545932, 1.0011545932], 3)
                _nurbs_edge([(-1.5075129477, 0.7732910317), (-1.1647181771, 1.6778127277), (-0.7248376967, 2.3444935479), (-0.1877916833, 2.7645228866), (0.2491280207, 3.1062423849), (0.7511451435, 3.2806367122), (1.2774147884, 3.2928985228), (1.900545058, 3.3074171359), (2.5583412634, 3.0961994081), (3.1270818572, 2.7209078488), (3.5951988889, 2.4120141762), (3.9990368763, 1.9928875392), (4.2656118343, 1.5081409783), (4.501967472, 1.0783459841), (4.6277456519, 0.5972398457), (4.6276897909, 0.101520629), (4.6276254117, -0.4697897803), (4.4620726095, -1.0584735348), (4.1877943099, -1.6261327782), (3.8895176901, -2.2434600717), (3.4678513329, -2.8367759794), (3.0118766607, -3.3779192465), (2.5637971939, -3.9096926133), (2.0851210942, -4.3913901663), (1.6000771795, -4.8111173962), (0.7868823063, -5.5148063221), (-0.051596789, -6.0432378988), (-0.8983629789, -6.3895088042), (-1.0884310366, -6.4672339652), (-1.2790637189, -6.5358878411), (-1.4702459231, -6.5954709113), (-1.483315147, -6.5995440126), (-1.4963843709, -6.6036171139), (-1.5094535949, -6.6076902152)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0099772185, 0.0099772185, 0.0099772185, 0.0099772185, 0.125, 0.125, 0.125, 0.2185780517, 0.2185780517, 0.2185780517, 0.3293792677, 0.3293792677, 0.3293792677, 0.4205771476, 0.4205771476, 0.4205771476, 0.5014367047, 0.5014367047, 0.5014367047, 0.5946263676, 0.5946263676, 0.5946263676, 0.6959697757, 0.6959697757, 0.6959697757, 0.7955584218, 0.7955584218, 0.7955584218, 0.9625226368, 0.9625226368, 0.9625226368, 1, 1, 1, 1.0026001088, 1.0026001088, 1.0026001088, 1.0026001088], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-1.5, 0.5), (-1.4158788224, 0.7438869279), (-1.2372519221, 1.2041435083), (-0.9381569063, 1.8119762855), (-0.4768087296, 2.4566443878), (0.2008165919, 2.9842575946), (0.9665766819, 3.2348894695), (1.7929377026, 3.2164295994), (2.6309999678, 2.9476426698), (3.4067365504, 2.4614775863), (4.0382392896, 1.7997929899), (4.4517354771, 1.0091557899), (4.5963195713, 0.1367392478), (4.4644320303, -0.7741359398), (4.0941298468, -1.6864063229), (3.5474426393, -2.5687291696), (2.8930949725, -3.3958407641), (2.1925771209, -4.1484888506), (1.4738660936, -4.8141436223), (0.7405530403, -5.3863482196), (-0.0003814105, -5.8621570342), (-0.5978828303, -6.1653376825), (-1.0480998813, -6.3494337953), (-1.3492075726, -6.4530046438), (-1.5, -6.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1.5, 0.5), (-1.610550268, 0.769697993), (-1.8405507969, 1.2756314804), (-2.212254937, 1.9341415406), (-2.761626556, 2.6099381162), (-3.5343714296, 3.1124330334), (-4.3776247066, 3.2729734219), (-5.2576508827, 3.1039491745), (-6.1117080006, 2.6412012761), (-6.8549039665, 1.9397730475), (-7.3971417279, 1.0615488316), (-7.6554649664, 0.0671812147), (-7.5725031009, -0.9946062977), (-7.1210328797, -2.0906305311), (-6.2919681585, -3.1990149013), (-5.0881896009, -4.3071072184), (-3.8318133329, -5.1884247724), (-2.7281957145, -5.8456614962), (-1.9212631406, -6.2821631555), (-1.5, -6.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a curved sheet metal or composite bracket with a smooth, flowing S-shaped profile, featuring a mesh-patterned upper section and a solid lower section, likely designed for aerodynamic or structural purposes in an automotive or industrial application.
def model_137717_63e1ca8f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 75.184600085, perimeter: 48.1878084741
            with BuildLine():
                CenterArc((-2.2, 2.5), 7.8160092119, 73.6518284526, 212.6963430947)
                CenterArc((3.0589471063, 2.5), 8.0998245289, 112.1885635502, 135.6228728997)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a complex polyhedron or geometric solid with an irregular, faceted shape featuring multiple triangular and rectangular faces in varying shades of blue and dark gray, with internal geometric divisions and what appears to be a central cavity or hollow section.
def model_137744_580caf3a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.7418965734, perimeter: 25.1744897097
            with BuildLine():
                Line((1.443375673, 2.5), (-1.443375673, 2.5))
                Line((-1.443375673, 2.5), (-2.8867513459, 0))
                Line((-2.8867513459, 0), (-1.443375673, -2.5))
                Line((-1.443375673, -2.5), (1.443375673, -2.5))
                Line((1.443375673, -2.5), (2.8867513459, 0))
                Line((2.8867513459, 0), (1.443375673, 2.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a trapezoidal or wedge-shaped bracket or panel with a slanted profile, featuring a flat base, angled side surfaces, and internal diagonal reinforcement ribs or bracing elements.
def model_137837_9c9f163d_0004():
    """Model: WEDGE PLATE (1)"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.4999421005, perimeter: 8.9999669145
            with BuildLine():
                Line((-6.1178551814, 5.8859174408), (-7.3721430048, 2.6183859481))
                Line((-7.3721430048, 2.6183859481), (-6.4385780222, 2.2600239269))
                Line((-5.1842901988, 5.5275554196), (-6.4385780222, 2.2600239269))
                Line((-6.1178551814, 5.8859174408), (-5.1842901988, 5.5275554196))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


# Description: This is an elongated rectangular extrusion or beam with a tapered hexagonal cross-section, featuring a recessed or grooved channel running along its length and angled end faces.
def model_137837_9c9f163d_0007():
    """Model: GUIDE RAILS"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2, perimeter: 8.2
            with BuildLine():
                Line((0, 0.8), (0, 1.6))
                Line((0, 0.8), (1, 0.8))
                Line((1, 0), (1, 0.8))
                Line((2.5, 0), (1, 0))
                Line((2.5, 1.6), (2.5, 0))
                Line((0, 1.6), (2.5, 1.6))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9)
    return part.part


# Description: This is an elongated, flat rectangular plate or panel with a tapered wedge-shaped profile, featuring a central longitudinal slot or groove running along its length and angled side edges.
def model_137837_9c9f163d_0010():
    """Model: EJECTOR PLATE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 262.8, perimeter: 77.2
            with BuildLine():
                Line((-7.3, 12), (7.3, 12))
                Line((-7.3, -12), (-7.3, 12))
                Line((0, -12), (-7.3, -12))
                Line((0, -12), (0, 0))
                Line((7.3, 0), (0, 0))
                Line((7.3, 12), (7.3, 0))
            make_face()
            # Profile area: 87.6, perimeter: 38.6
            with BuildLine():
                Line((7.3, -12), (0, -12))
                Line((7.3, 0), (7.3, -12))
                Line((7.3, 0), (0, 0))
                Line((0, -12), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a circular disc or wheel with a flat front face and a textured or ribbed cylindrical edge/rim running around its perimeter.
def model_137907_ff5b17ca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Base circule -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a triangular prism or wedge-shaped structural component with a rectangular base and an angled top face, featuring clean edges and flat surfaces typical of a machined or molded part.
def model_138124_2366c1e3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 180, perimeter: 58
            with BuildLine():
                Line((33, 8), (13, 8))
                Line((33, 17), (33, 8))
                Line((13, 17), (33, 17))
                Line((13, 8), (13, 17))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered or rounded end, featuring a uniform hollow cylindrical body oriented at an angle.
def model_138134_2a26ecee_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1.5416662293, -1.6627354998)):
                Circle(0.25)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)
    return part.part


# Description: This is a long, slender hexagonal prism or tube with a central slot or groove running along its length, featuring a tapered or beveled end at the top.
def model_138138_c62f4894_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2800000083, perimeter: 3.2000000477
            with BuildLine():
                Line((1.9000000283, 1.1000000164), (1.7000000253, 1.1000000164))
                Line((1.9000000283, 2.5000000373), (1.9000000283, 1.1000000164))
                Line((1.7000000253, 2.5000000373), (1.9000000283, 2.5000000373))
                Line((1.7000000253, 1.1000000164), (1.7000000253, 2.5000000373))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: This is a set of three identical straight cylindrical rods arranged in a parallel, slightly fanned configuration, commonly used as structural supports, pins, or dowels in mechanical assemblies.
def model_138210_482aa6e2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                CenterArc((-1, 1), 0.15, -90, 90)
                Line((-1, 1), (-0.85, 1))
                Line((-1, 0.85), (-1, 1))
            make_face()
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                Line((-1, 0.85), (-1, 1))
                Line((-1, 1), (-0.85, 1))
                CenterArc((-1, 1), 0.15, 0, 270)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((1, 1), (1, 0.85))
                Line((0.85, 1), (1, 1))
                CenterArc((1, 1), 0.15, 180, 90)
            make_face()
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                CenterArc((1, 1), 0.15, -90, 270)
                Line((0.85, 1), (1, 1))
                Line((1, 1), (1, 0.85))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                CenterArc((1, -1), 0.15, 90, 90)
                Line((1, -1), (0.85, -1))
                Line((1, -0.85), (1, -1))
            make_face()
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                Line((1, -0.85), (1, -1))
                Line((1, -1), (0.85, -1))
                CenterArc((1, -1), 0.15, 180, 270)
            make_face()
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                Line((-0.85, -1), (-1, -1))
                Line((-1, -1), (-1, -0.85))
                CenterArc((-1, -1), 0.15, 90, 270)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                CenterArc((-1, -1), 0.15, 0, 90)
                Line((-1, -1), (-1, -0.85))
                Line((-0.85, -1), (-1, -1))
            make_face()
        # OneSide extrude, distance=14
        extrude(amount=14)
    return part.part


# Description: A cylindrical rubber or foam sleeve with a hollow core, designed to slide onto a cricket bat handle to reduce vibration and noise upon ball impact.
def model_138535_c0da19b3_0009():
    """Model: Нижняя часть (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8790651059, perimeter: 7.9329640216
            with BuildLine():
                CenterArc((0, 0), 0.45, 90, 270)
                Line((0, 1), (0, 0.45))
                CenterArc((0, 0), 1, 90, 270)
                Line((0.45, 0), (1, 0))
            make_face()
            # Profile area: 0.6263550353, perimeter: 3.3776546739
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 90)
                Line((0.45, 0), (1, 0))
                CenterArc((0, 0), 1, 0, 90)
                Line((0, 1), (0, 0.45))
            make_face()
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                CenterArc((0, 0), 1, 0, 90)
                Line((1, 0), (1, 1))
                Line((1, 1), (0, 1))
            make_face()
        # OneSide extrude, distance=8.8
        extrude(amount=8.8)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4771293843, perimeter: 3.0205750412
            with BuildLine():
                CenterArc((0, 0), 0.45, 90, 270)
                Line((0, 0), (0.45, 0))
                Line((0, 0.45), (0, 0))
            make_face()
            # Profile area: 0.1590431281, perimeter: 1.6068583471
            with BuildLine():
                Line((0, 0.45), (0, 0))
                Line((0, 0), (0.45, 0))
                CenterArc((0, 0), 0.45, 0, 90)
            make_face()
        # OneSide extrude, distance=16.6
        extrude(amount=16.6, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or sleeve with a dark gray body, a blue hexagonal cap or end piece at the top, and what appears to be a seam or joint running along its length.
def model_138535_c0da19b3_0013():
    """Model: Верхняя часть (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 8.0685834706
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 270)
                Line((0, 1), (0, 0.5))
                CenterArc((0, 0), 1, 90, 270)
                Line((0.5, 0), (1, 0))
            make_face()
            # Profile area: 0.5890486225, perimeter: 3.3561944902
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 90)
                Line((0.5, 0), (1, 0))
                CenterArc((0, 0), 1, 0, 90)
                Line((0, 1), (0, 0.5))
            make_face()
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                CenterArc((0, 0), 1, 0, 90)
                Line((1, 0), (1, 1))
                Line((1, 1), (0, 1))
            make_face()
        # OneSide extrude, distance=-8.8
        extrude(amount=-8.8)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5890486225, perimeter: 3.3561944902
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 270)
                Line((0, 0), (0.5, 0))
                Line((0, 0.5), (0, 0))
            make_face()
            # Profile area: 0.1963495408, perimeter: 1.7853981634
            with BuildLine():
                Line((0, 0.5), (0, 0))
                Line((0, 0), (0.5, 0))
                CenterArc((0, 0), 0.5, 0, 90)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an open top slot and a mesh or perforated section on the upper portion, designed for containment or filtering applications.
def model_138642_bd3f2dbd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1865599103, perimeter: 9.7860611159
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with an open top and bottom, featuring a fine mesh screen surface on the upper portion and solid cylindrical walls, designed to filter liquids or gases while allowing flow-through capability.
def model_138775_4626dfa8_0006():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0914420404, perimeter: 1.0719582869
            Circle(0.1706074601)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform hollow circular cross-section, featuring slightly rounded edges at both ends and a slight diagonal orientation.
def model_139258_43c33f60_0039():
    """Model: M16 Stud v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


# Description: This is a cylindrical bearing or bushing with an eccentric or offset design, featuring a circular outer ring with internal concentric cylindrical bores and radial slots or cutouts distributed around its circumference.
def model_139330_fc67535e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 103.5593808624, perimeter: 92.8329533515
            with BuildLine():
                CenterArc((0, 0), 8.5029571769, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.2718662308, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 30.7713644459, perimeter: 73.5577113054
            with BuildLine():
                CenterArc((0, 0), 6.2718662308, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.435207126, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 92.8072855561, perimeter: 34.1504135555
            Circle(5.435207126)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30.7713644459, perimeter: 73.5577113054
            with BuildLine():
                CenterArc((0, 0), 6.2718662308, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.435207126, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)
    return part.part


# Description: This is a flat elliptical disc or plate with a smooth, curved edge and a slightly beveled or rounded perimeter, featuring a simple oval shape without any holes, slots, or additional features.
def model_139785_ce182c73_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a triangular prism or wedge-shaped solid with a rectangular base and sloped top surface, featuring clean edges and flat faces with no holes or additional features.
def model_140462_343115e7_0002():
    """Model: Heat sink"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 3.8, perimeter: 7.8
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (1.9, 0))
                Line((1.9, 0), (1.9, 2))
                Line((1.9, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a pair of oval-shaped mesh speaker covers or acoustic grilles with a slightly curved, dome-like profile and perforated mesh surface on the front and sides.
def model_140462_c2442684_0003():
    """Model: Lens base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.17, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.7466191291, perimeter: 3.0630528373
            with Locations((-0.95, 1.5)):
                Circle(0.4875)
            # Profile area: 0.7466191291, perimeter: 3.0630528373
            with Locations((-0.95, 0.5)):
                Circle(0.4875)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a snow plow or blade attachment featuring an angled rectangular blade with a trapezoidal cross-section, mounted to a bracket with two vertical handles or tines extending upward for attachment to a vehicle or equipment.
def model_140842_5958dd74_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 48 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 135.4836, perimeter: 69.85
            with BuildLine():
                Line((120.015, 45.4025), (124.46, 45.4025))
                Line((120.015, 45.4025), (120.015, 14.9225))
                Line((120.015, 14.9225), (124.46, 14.9225))
                Line((124.46, 45.4025), (124.46, 14.9225))
            make_face()
            # Profile area: 27254.2682486179, perimeter: 1057.7702816431
            with BuildLine():
                Line((25.4, -4.1275), (-139.5759025805, -4.1275))
                Line((-139.5759025805, -4.1275), (-139.5759025805, -57.1739634063))
                Line((-139.5759025805, -57.1739634063), (227.965, -61.0243452072))
                Line((227.965, -61.0243452072), (227.965, 45.4025))
                Line((124.46, 45.4025), (227.965, 45.4025))
                Line((124.46, 45.4025), (124.46, 14.9225))
                Line((120.015, 14.9225), (124.46, 14.9225))
                Line((120.015, 45.4025), (120.015, 14.9225))
                Line((108.4679462774, 45.4025), (120.015, 45.4025))
                Line((108.4679462774, 45.4025), (108.4679462774, 28.8925))
                Line((108.4679462774, 28.8925), (80.5279462774, 28.8925))
                Line((80.5279462774, 28.8925), (80.5279462774, 12.3825))
                Line((80.5279462774, 12.3825), (52.5879462774, 12.3825))
                Line((52.5879462774, 12.3825), (52.5879462774, -4.1275))
                Line((52.5879462774, -4.1275), (29.845, -4.1275))
                Line((29.845, -4.1275), (29.845, -30.48))
                Line((29.845, -30.48), (25.4, -30.48))
                Line((25.4, -4.1275), (25.4, -30.48))
            make_face()
            # Profile area: 117.1368625, perimeter: 61.595
            with BuildLine():
                Line((25.4, -4.1275), (25.4, -30.48))
                Line((29.845, -30.48), (25.4, -30.48))
                Line((29.845, -4.1275), (29.845, -30.48))
                Line((29.845, -4.1275), (25.4, -4.1275))
            make_face()
        # OneSide extrude, distance=30.48
        extrude(amount=30.48)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 48 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 291.4870610526, perimeter: 140.0427833757
            with BuildLine():
                Line((4.445, 71.12), (4.445, 81.28))
                CenterArc((10.16, 81.28), 5.715, 90, 90)
                Line((10.16, 86.995), (25.4, 86.995))
                Line((25.4, 91.44), (25.4, 86.995))
                Line((10.16, 91.44), (25.4, 91.44))
                CenterArc((10.16, 81.28), 10.16, 90, 90)
                Line((0, 71.12), (0, 81.28))
                CenterArc((10.16, 71.12), 10.16, 180, 90)
                Line((10.16, 60.96), (25.4, 60.96))
                Line((25.4, 65.405), (25.4, 60.96))
                Line((10.16, 65.405), (25.4, 65.405))
                CenterArc((10.16, 71.12), 5.715, 180, 90)
            make_face()
            # Profile area: 165.4538156496, perimeter: 83.3349114284
            with BuildLine():
                Line((120.015, 82.6249557142), (124.46, 82.6249557142))
                Line((120.015, 45.4025), (120.015, 82.6249557142))
                Line((120.015, 45.4025), (124.46, 45.4025))
                Line((124.46, 45.4025), (124.46, 82.6249557142))
            make_face()
            # Profile area: 462.9023, perimeter: 217.17
            with BuildLine():
                Line((124.46, 132.3975), (124.46, 136.8425))
                Line((224.155, 132.3975), (124.46, 132.3975))
                Line((224.155, 132.3975), (228.6, 132.3975))
                Line((228.6, 132.3975), (228.6, 136.8425))
                Line((228.6, 136.8425), (124.46, 136.8425))
            make_face()
            # Profile area: 450.852592001, perimeter: 212.3895545133
            with BuildLine():
                Line((29.845, 38.8964631217), (108.4679462774, 82.6249557142))
                Line((108.4679462774, 82.6249557142), (120.015, 82.6249557142))
                Line((120.015, 82.6249557142), (120.015, 87.0699557142))
                Line((107.315, 87.0699557142), (120.015, 87.0699557142))
                Line((29.845, 43.9827085232), (107.315, 87.0699557142))
                Line((29.845, 38.8964631217), (29.845, 43.9827085232))
            make_face()
            # Profile area: 19.758025, perimeter: 17.78
            with BuildLine():
                Line((120.015, 132.3975), (120.015, 136.8425))
                Line((124.46, 132.3975), (120.015, 132.3975))
                Line((124.46, 132.3975), (124.46, 136.8425))
                Line((124.46, 136.8425), (120.015, 136.8425))
            make_face()
            # Profile area: 450.559698095, perimeter: 212.2444739049
            with BuildLine():
                Line((52.9513442304, 101.5202887491), (29.845, 88.8117994224))
                Line((108.4679462774, 132.3975), (52.9513442304, 101.5202887491))
                Line((120.015, 132.3975), (108.4679462774, 132.3975))
                Line((120.015, 132.3975), (120.015, 136.8425))
                Line((120.015, 136.8425), (107.315, 136.8425))
                Line((107.315, 136.8425), (50.8, 105.41))
                Line((50.8, 105.41), (29.845, 93.88475))
                Line((29.845, 88.8117994224), (29.845, 93.88475))
            make_face()
            # Profile area: 22.1907908374, perimeter: 19.5025583784
            with BuildLine():
                Line((25.4, 86.995), (26.5417283229, 86.995))
                Line((29.845, 88.8117994224), (26.5417283229, 86.995))
                Line((29.845, 88.8117994224), (29.845, 93.88475))
                Line((29.845, 93.88475), (25.4, 91.44))
                Line((25.4, 91.44), (25.4, 86.995))
            make_face()
            # Profile area: 460.079725, perimeter: 215.9
            with BuildLine():
                Line((124.46, 82.6249557142), (124.46, 87.0699557142))
                Line((124.46, 82.6249557142), (227.965, 82.6249557142))
                Line((227.965, 87.0699557142), (227.965, 82.6249557142))
                Line((124.46, 87.0699557142), (227.965, 87.0699557142))
            make_face()
            # Profile area: 19.758025, perimeter: 17.78
            with BuildLine():
                Line((120.015, 87.0699557142), (124.46, 87.0699557142))
                Line((120.015, 82.6249557142), (120.015, 87.0699557142))
                Line((120.015, 82.6249557142), (124.46, 82.6249557142))
                Line((124.46, 82.6249557142), (124.46, 87.0699557142))
            make_face()
            # Profile area: 201.4809343504, perimeter: 99.5450885716
            with BuildLine():
                Line((124.46, 132.3975), (120.015, 132.3975))
                Line((120.015, 87.0699557142), (120.015, 132.3975))
                Line((120.015, 87.0699557142), (124.46, 87.0699557142))
                Line((124.46, 87.0699557142), (124.46, 132.3975))
            make_face()
            # Profile area: 408.0402035376, perimeter: 193.4184566457
            with BuildLine():
                Line((25.4, 65.405), (25.4, 60.96))
                Line((25.4, 60.96), (25.4, 0))
                Line((25.4, 0), (25.4, -4.1275))
                Line((29.845, -4.1275), (25.4, -4.1275))
                Line((29.845, 0), (29.845, -4.1275))
                Line((29.845, 0), (29.845, 38.8964631217))
                Line((29.845, 38.8964631217), (29.845, 43.9827085232))
                Line((29.845, 43.9827085232), (29.845, 88.8117994224))
                Line((29.845, 88.8117994224), (26.5417283229, 86.995))
                Line((25.4, 86.995), (26.5417283229, 86.995))
                Line((25.4, 86.995), (25.4, 65.405))
            make_face()
        # OneSide extrude, distance=4.445
        extrude(amount=4.445, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular duct or channel component with a curved cylindrical section, featuring two flat vertical flanges on the sides and a central ribbed or corrugated interior surface, designed for airflow or fluid conveyance.
def model_140941_7fb9203a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8493842569, perimeter: 12.2931360319
            with BuildLine():
                CenterArc((0, 0), 1.5875, 113.5781784782, 132.8436430436)
                Line((-0.635, -1.4549677831), (-0.635, -2.4996722124))
                Line((-0.3175, -2.4996722124), (-0.635, -2.4996722124))
                Line((-0.3175, -1.2296722124), (-0.3175, -2.4996722124))
                CenterArc((0, 0), 1.27, 104.4775121859, 151.0449756281)
                Line((-0.3175, 1.2296722124), (-0.3175, 2.4996722124))
                Line((-0.635, 2.4996722124), (-0.3175, 2.4996722124))
                Line((-0.635, 1.4549677831), (-0.635, 2.4996722124))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is an elongated oval or elliptical mesh container/basket with a shallow depth, featuring a solid rim or flange around the perimeter and an open lattice or perforated mesh top surface.
def model_140993_248dc00c_0000():
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
            # Profile area: 9370.5977227282, perimeter: 424.8284732259
            with BuildLine():
                _nurbs_edge([(172.1887931423, -10.2157135446), (179.2504908761, -14.3584644923), (181.8986792033, -19.8475371772), (182.4503312746, -23.4724037492)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(142.617968333, -2.4481299379), (152.2174723028, -3.7945213852), (165.1270954084, -6.0729970482), (172.1887931423, -10.2157135446)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(93.0757021046, 0.0374994754), (111.7229718446, 0.4518063368), (133.0184643632, -1.1017384907), (142.617968333, -2.4481299379)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(49.9330391577, -2.9659782474), (65.1598378157, -1.6195868001), (74.428363462, -0.376772228), (93.0757021046, 0.0374994754)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(7.7835286555, -9.4907464745), (9.8799690936, -8.9728981651), (34.7062771044, -4.3123344358), (49.9330391577, -2.9659782474)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.6473445385, -18.7359905517), (4.6328707737, -13.7662136708), (5.6870882173, -10.0085942457), (7.7835286555, -9.4907464745)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0, -29.8945812708), (0.661853764, -23.7057319045), (2.6473445385, -18.7359905517)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(2.6473335034, -41.0532408925), (0.661853764, -36.0834672415), (0, -29.8945812708)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(7.7835178894, -50.2984515949), (5.6870774513, -49.7806393517), (4.6328600077, -46.0229843986), (2.6473335034, -41.0532408925)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(49.9330305449, -56.82325535), (34.7062663383, -55.4768281057), (9.8799249528, -50.8163370472), (7.7835178894, -50.2984515949)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(93.0756934918, -59.8267317271), (74.4283203978, -59.4124242265), (65.1598292028, -58.1696093853), (49.9330305449, -56.82325535)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(142.6179597202, -57.3410675932), (133.0184471375, -58.6874948376), (111.722954619, -60.2410392276), (93.0756934918, -59.8267317271)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(172.1887931423, -49.573522206), (165.1270954084, -53.716239779), (152.2175067542, -55.994713558), (142.6179597202, -57.3410675932)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(182.4503312746, -36.3167975501), (181.8986792033, -39.9416985735), (179.2504908761, -45.4307744881), (172.1887931423, -49.573522206)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(183.0020522486, -29.8945812708), (183.0020522486, -32.6919632762), (182.4503312746, -36.3167975501)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(182.4503312746, -23.4724037492), (183.0020522486, -27.0972337166), (183.0020522486, -29.8945812708)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a dark blue bracket or mounting clamp with an angular, open-frame design featuring two large rectangular openings and reinforcing ribs, designed to hold or secure a component between its flanged arms.
def model_141453_50ec6f25_0000():
    """Model: Untitled v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 32 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 144.9155478333, perimeter: 111.8047259022
            with BuildLine():
                Line((-1.2255772701, 10.4428302978), (-1.2255772701, 9.2428302978))
                Line((-1.2255772701, 9.2428302978), (-8.2370193267, 9.2428302978))
                Line((-8.2370193267, 9.2428302978), (-8.2370193267, 10.4428302978))
                Line((-11.0494678217, 10.4428302978), (-8.2370193267, 10.4428302978))
                Line((-11.0494678217, 7.842955546), (-11.0494678217, 10.4428302978))
                Line((-3.0115217141, -1.1482779706), (-11.0494678217, 7.842955546))
                Line((11.3527862895, -1.1482779706), (-3.0115217141, -1.1482779706))
                Line((11.3527862895, 7.842955546), (11.3527862895, -1.1482779706))
                Line((11.3527862895, 10.4428302978), (11.3527862895, 7.842955546))
                Line((-1.2255772701, 10.4428302978), (11.3527862895, 10.4428302978))
            make_face()
            with BuildLine():
                Line((0.2604110674, 6.7548943583), (-1.6733192878, 0.9749530767))
                Line((-1.6733192878, 0.9749530767), (-2.7135396954, 0.9749530767))
                CenterArc((-2.7135396954, 1.8831845675), 0.9082314908, -138.2040532496, 48.2040532496)
                Line((-3.3906472974, 1.2778666872), (-6.6719085125, 4.9482801758))
                CenterArc((-5.9948009106, 5.5535980561), 0.9082314908, 160.5115143818, 61.2844323686)
                Line((-6.850998507, 5.8565998989), (-6.3238919805, 7.3460540126))
                CenterArc((-5.467694384, 7.0430521699), 0.9082314908, 90, 70.5115143818)
                Line((-5.467694384, 7.9512836607), (-0.600895798, 7.9512836607))
                CenterArc((-0.600895798, 7.0430521699), 0.9082314908, -18.4981194473, 108.4981194473)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((7.1730457361, -0.2599874304), (1.1049466429, -0.2599874304))
                Line((1.1049466429, -0.2599874304), (3.0765183297, 5.633062007))
                Line((3.0765183297, 5.633062007), (7.1730457361, 5.633062007))
                CenterArc((7.1730457361, 4.7248305162), 0.9082314908, 0, 90)
                Line((8.0812772269, 4.7248305162), (8.0812772269, 0.6482440604))
                CenterArc((7.1730457361, 0.6482440604), 0.9082314908, -90, 90)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a hexagonal or irregular polyhedron-shaped structural component with angular faceted surfaces, featuring a hollow or recessed interior cavity visible on the left side and triangulated internal geometry.
def model_141504_becd21e8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.7954991735, perimeter: 28.6985837839
            with BuildLine():
                Line((-0.1000000015, 5.4300000015), (-0.1000000015, -0.1000000015))
                Line((-0.1000000015, -0.1000000015), (6.9600000015, -0.1000000015))
                Line((6.9600000015, -0.1000000015), (6.9600000015, 5.4300000015))
                Line((6.9600000015, 5.4300000015), (-0.1000000015, 5.4300000015))
            make_face()
            with BuildLine():
                CenterArc((1.53, 5.07), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.4, 0.25), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.61, 3.55), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.61, 0.76), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((1.53, 5.07)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((1.4, 0.25)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((6.61, 3.55)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((6.61, 0.76)):
                Circle(0.14)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


# Description: This is a dark gray plastic or composite bracket or mounting plate with an organic, curved shape featuring two large oval holes on the sides and a smaller central opening, designed for lightweight structural support or cable management.
def model_141638_a21f336f_0015():
    """Model: Bottom Plate (2) (1)"""
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
        # OneSide extrude, distance=0.32
        extrude(amount=0.32)
    return part.part


# Description: This is a curved metal bracket or clamp with two flat flanges at the base and a cylindrical or semi-cylindrical body featuring internal grooves or ridges, designed to hold or secure a round component.
def model_142246_0851be5e_0005():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.5498055942, perimeter: 32.660440934
            with BuildLine():
                Line((3, 0), (6, 0))
                Line((6, 0), (6, 1))
                Line((6, 1), (4.2848570571, 1))
                CenterArc((0, 0), 4.4, 13.1365587869, 153.7268824261)
                Line((-6, 1), (-4.2848570571, 1))
                Line((-6, 0), (-6, 1))
                Line((-3, 0), (-6, 0))
                CenterArc((0, 0), 3, 0, 180)
            make_face()
        # Symmetric extrude, full_length=True, total=8
        extrude(amount=4, both=True)
    return part.part


# Description: This is a waist/hip pack or utility pouch featuring an elongated rectangular shape with a blue fabric panel on top, a dark gray/black structural base with mesh ventilation areas, and curved ergonomic sides designed to conform to the body.
def model_142246_0851be5e_0010():
    """Model: Component37"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 189.58324782, perimeter: 104.2476866969
            with BuildLine():
                CenterArc((0, 0), 1.9, -180, 270)
                Line((-1.9, 0), (-1.9, -14))
                CenterArc((1.9, -14), 3.8, 0, 180)
                Line((5.7, -14), (5.7, -5.7))
                Line((24.1, -5.7), (5.7, -5.7))
                CenterArc((24.1, -3.8), 1.9, 70.6154843206, 199.3845156794)
                Line((24.730621802, -2.0077064574), (13.930621802, 1.7922935426))
                CenterArc((13.3, 0), 1.9, 90, 340.6154843206)
                Line((0, 1.9), (13.3, 1.9))
            make_face()
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((13.3, 0), 1.9, 90, 340.6154843206)
                CenterArc((13.3, 0), 1.9, 70.6154843206, 19.3845156794)
            make_face()
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((24.1, -3.8), 1.9, 70.6154843206, 199.3845156794)
                CenterArc((24.1, -3.8), 1.9, -90, 160.6154843206)
            make_face()
            # Profile area: 45.3645979178, perimeter: 23.8761041673
            with BuildLine():
                CenterArc((1.9, -14), 3.8, 0, 180)
                CenterArc((1.9, -14), 3.8, 180, 180)
            make_face()
            # Profile area: 10.9327424223, perimeter: 14.2034867972
            with BuildLine():
                CenterArc((0, 0), 1.9, 90, 90)
                CenterArc((0, 0), 1.9, -180, 270)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3605551329, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4084070571, perimeter: 2.2654347136
            Circle(0.3605551329)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.3645979178, perimeter: 23.8761041673
            with BuildLine():
                CenterArc((1.9, -14), 3.8, 0, 180)
                CenterArc((1.9, -14), 3.8, 180, 180)
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4, mode=Mode.ADD)
    return part.part


# Description: This is a complex polyhedral bracket or connector with an irregular geometric shape featuring multiple angular faces, internal voids (dark recessed areas), and protruding flanges, designed for structural support or mechanical assembly applications.
def model_142246_0851be5e_0014():
    """Model: Component31"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.25, perimeter: 24
            with BuildLine():
                Line((0, 1.5), (0, 0))
                Line((0, 0), (4, 0))
                Line((4, 0), (4, 3))
                Line((4, 3), (7.5, 3))
                Line((7.5, 3), (7.5, 4.5))
                Line((7.5, 4.5), (3, 4.5))
                Line((3, 4.5), (3, 1.5))
                Line((3, 1.5), (0, 1.5))
            make_face()
        # Symmetric extrude, full_length=True, total=6
        extrude(amount=3, both=True)
    return part.part


# Description: This is a cylindrical or capsule-shaped housing component with a curved body, featuring a segmented upper surface with blue-highlighted panels, dark recessed areas, and what appears to be internal ribbing or structural supports along its length.
def model_142246_0851be5e_0017():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.7033414751, perimeter: 24.157498157
            with BuildLine():
                CenterArc((0, 0), 3, -90, 28.3593500282)
                Line((4.5225, -0.9679843749), (1.425, -2.639957386))
                CenterArc((4, 0), 1.1, -61.6406499718, 123.2812999437)
                Line((4.5225, 0.9679843749), (1.7, 2.49151749))
                Line((1.7, 3.8), (1.7, 2.49151749))
                Line((0, 3.8), (1.7, 3.8))
                Line((0, 3), (0, 3.8))
                Line((0, -3), (0, 3))
            make_face()
            with BuildLine():
                CenterArc((4, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


# Description: This is a protective belt or waist pack with a curved, ergonomic design featuring dark gray/black outer panels, internal blue compartments with mesh or perforated detailing, and a contoured shape designed to fit around the torso.
def model_142246_0851be5e_0032():
    """Model: Component13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 84.5888197429, perimeter: 51.234619374
            with BuildLine():
                CenterArc((6.2, 0), 2, -71.180936631, 142.361873262)
                Line((6.8451612903, 1.8930839679), (1.2903225806, 3.7861679358))
                CenterArc((0, 0), 4, 71.180936631, 37.638126738)
                Line((-6.8451612903, 1.8930839679), (-1.2903225806, 3.7861679358))
                CenterArc((-6.2, 0), 2, 108.819063369, 142.361873262)
                Line((-6.8451612903, -1.8930839679), (-1.2903225806, -3.7861679358))
                CenterArc((0, 0), 4, -108.819063369, 37.638126738)
                Line((6.8451612903, -1.8930839679), (1.2903225806, -3.7861679358))
            make_face()
            with BuildLine():
                CenterArc((-6.2, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal tube with a tilted/angled top surface and hollow interior cavity, featuring clean geometric faces and edges typical of an extruded polygonal shape.
def model_142504_3fe2ab83_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.78, perimeter: 8.2
            with BuildLine():
                Line((-1.35, 0.7), (1.35, 0.7))
                Line((-1.35, -0.7), (-1.35, 0.7))
                Line((1.35, -0.7), (-1.35, -0.7))
                Line((1.35, 0.7), (1.35, -0.7))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


# Description: This is a shoulder bolt or carriage bolt consisting of a cylindrical shaft with a larger flat circular head/flange at one end, designed for use as a fastener or pivot point in mechanical assemblies.
def model_142800_fc51c220_0000():
    """Model: niete v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrusion2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a coffin-shaped or elongated hexagonal enclosure with a flat top surface featuring a grid-like panel pattern, tapered curved sides, and a ribbed or corrugated cylindrical base, resembling an aerospace or industrial component housing.
def model_143646_e3f1ab5c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.2831853072, perimeter: 18.2831853072
            with BuildLine():
                Line((-2, -4), (-2, 0))
                CenterArc((0, -4), 2, 180, 180)
                Line((2, 0), (2, -4))
                Line((0, 0), (2, 0))
                Line((-2, 0), (0, 0))
            make_face()
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a fin or blade component with an elongated, tapered body featuring two parallel slots or channels running along its length and angular fins or flanges at both ends for attachment or hydrodynamic purposes.
def model_143678_6d68b8bc_0002():
    """Model: Raptor 2.0 Proximal v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1200000054, perimeter: 1.4000000268
            with BuildLine():
                Line((-3.6000000596, 2.1000000224), (-3.6000000596, 2.4000000358))
                Line((-3.6000000596, 2.4000000358), (-4.0000000596, 2.4000000358))
                Line((-4.0000000596, 2.4000000358), (-4.0000000596, 2.1000000224))
                Line((-4.0000000596, 2.1000000224), (-3.6000000596, 2.1000000224))
            make_face()
            # Profile area: 0.9647831039, perimeter: 5.215043805
            with BuildLine():
                CenterArc((-4.0000000596, 1.5000000224), 0.6, 90, 180)
                CenterArc((-4.0000000596, 1.5000000224), 0.6, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((-4.0000000596, 1.5000000224), 0.23, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9500176184, perimeter: 5.277875658
            with BuildLine():
                CenterArc((-1.7000000596, 1.5000000224), 0.6, 90, 180)
                CenterArc((-1.7000000596, 1.5000000224), 0.6, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((-1.7000000596, 1.5000000224), 0.24, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6290266447, perimeter: 8.3699111843
            with BuildLine():
                CenterArc((-1.7000000596, 1.5000000224), 0.6, 90, 180)
                Line((-3.6000000596, 2.1000000224), (-1.7000000596, 2.1000000224))
                Line((-4.0000000596, 2.1000000224), (-3.6000000596, 2.1000000224))
                CenterArc((-4.0000000596, 1.5000000224), 0.6, -90, 180)
                Line((-1.7000000596, 0.9000000224), (-4.0000000596, 0.9000000224))
            make_face()
        # OneSide extrude, distance=0.26
        extrude(amount=0.26)
    return part.part


# Description: This is a flat parallelogram plate or panel with a slanted rectangular shape and no holes or additional features.
def model_143786_f34f7c93_0006():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 867.8816, perimeter: 117.84
            with BuildLine():
                Line((0, 29.56), (0, 0))
                Line((0, 0), (29.36, 0))
                Line((29.36, 0), (29.36, 29.56))
                Line((29.36, 29.56), (0, 29.56))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a complex sheet metal or molded plastic housing with an irregular, asymmetrical shape featuring multiple internal compartments, recessed sections, triangular reinforcement ribs, and mounting flanges designed for electronic component assembly or enclosure.
def model_144491_cbdce23f_0000():
    """Model: Bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 117.9314165294, perimeter: 69.4247779608
            with BuildLine():
                Line((7.5, -2.5), (7.5, -5))
                Line((7.5, -2.5), (2.5, -2.5))
                Line((2.5, -2.5), (2.5, 2.5))
                Line((2.5, 2.5), (7.5, 2.5))
                Line((7.5, 5), (7.5, 2.5))
                Line((-7.5, 5), (7.5, 5))
                Line((-7.5, -5), (-7.5, 5))
                Line((7.5, -5), (-7.5, -5))
            make_face()
            with BuildLine():
                CenterArc((-3.75, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((7.5, 2.5), (7.5, -2.5))
                Line((2.5, 2.5), (7.5, 2.5))
                Line((2.5, -2.5), (2.5, 2.5))
                Line((7.5, -2.5), (2.5, -2.5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


# Description: This is a rounded rectangular bar or spacer with a elongated cylindrical shape featuring hemispherical ends and a flat top surface.
def model_144935_1f83b45b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.322179003, perimeter: 7.8724533315
            with BuildLine():
                Line((12, -0.024376457), (12, -1.25))
                CenterArc((12, -1.5), 0.25, -90, 180)
                Line((12, -1.75), (12, -2.975623543))
                CenterArc((12, -1.5), 1.475623543, -90, 180)
            make_face()
            # Profile area: 62.1252716118, perimeter: 55.3774790776
            with BuildLine():
                CenterArc((-11, -1.5), 1.4829440923, -90, 180)
                Line((-11, -3), (-11, -2.9829440923))
                Line((12, -3), (-11, -3))
                Line((12, -2.975623543), (12, -3))
                CenterArc((12, -1.5), 1.475623543, 90, 180)
                Line((12, 0), (12, -0.024376457))
                Line((-11, 0), (12, 0))
                Line((-11, -0.0170559077), (-11, 0))
            make_face()
            # Profile area: 3.0616755331, perimeter: 9.6162871043
            with BuildLine():
                CenterArc((-11, -1.5), 0.4, 0, 90)
                Line((-10.6, -1.5), (-10.35, -1.5))
                CenterArc((-10.2, -1.5), 0.15, 0, 360)
                CenterArc((-11, -1.5), 0.4, -90, 90)
                Line((-11, -1.9), (-11, -2.25))
                CenterArc((-11, -2.4), 0.15, -90, 180)
                Line((-11, -2.9829440923), (-11, -2.55))
                CenterArc((-11, -1.5), 1.4829440923, -90, 180)
                Line((-11, -0.45), (-11, -0.0170559077))
                CenterArc((-11, -0.6), 0.15, -90, 180)
                Line((-11, -1.1), (-11, -0.75))
            make_face()
            # Profile area: 3.0616755331, perimeter: 9.6162871043
            with BuildLine():
                CenterArc((-11.8, -1.5), 0.15, 0, 360)
                Line((-11.4, -1.5), (-11.65, -1.5))
                CenterArc((-11, -1.5), 0.4, 90, 90)
                Line((-11, -1.1), (-11, -0.75))
                CenterArc((-11, -0.6), 0.15, 90, 180)
                Line((-11, -0.45), (-11, -0.0170559077))
                CenterArc((-11, -1.5), 1.4829440923, 90, 180)
                Line((-11, -2.9829440923), (-11, -2.55))
                CenterArc((-11, -2.4), 0.15, 90, 180)
                Line((-11, -1.9), (-11, -2.25))
                CenterArc((-11, -1.5), 0.4, 180, 90)
            make_face()
            # Profile area: 3.322179003, perimeter: 7.8724533315
            with BuildLine():
                CenterArc((12, -1.5), 1.475623543, 90, 180)
                Line((12, -1.75), (12, -2.975623543))
                CenterArc((12, -1.5), 0.25, 90, 180)
                Line((12, -0.024376457), (12, -1.25))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is an axe or hatchet featuring a long cylindrical handle with a flat, rectangular blade head at one end, suitable for chopping or splitting applications.
def model_145201_a104c55b_0006():
    """Model: Terasse Gammel Pilar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1710.840734641, perimeter: 242.8318530718
            with BuildLine():
                Line((2011.5, 447.5), (1966.5, 447.5))
                Line((2011.5, 492.5), (2011.5, 447.5))
                Line((1966.5, 492.5), (2011.5, 492.5))
                Line((1966.5, 447.5), (1966.5, 492.5))
            make_face()
            with BuildLine():
                CenterArc((1989, 470), 10, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1710.840734641, perimeter: 242.8318530718
            with BuildLine():
                Line((1966.5, 92.5), (2011.5, 92.5))
                Line((1966.5, 47.5), (1966.5, 92.5))
                Line((2011.5, 47.5), (1966.5, 47.5))
                Line((2011.5, 92.5), (2011.5, 47.5))
            make_face()
            with BuildLine():
                CenterArc((1989, 70), 10, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            with Locations((1989, 70)):
                Circle(10)
            # Profile area: 314.159265359, perimeter: 62.8318530718
            with Locations((1989, 470)):
                Circle(10)
        # OneSide extrude, distance=236
        extrude(amount=236, mode=Mode.ADD)
    return part.part


# Description: This is a flat diamond-shaped or rhombus-shaped plate with a triangular peak at the top and visible fold or crease lines running diagonally across its surface.
def model_145355_cedfad61_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 240, perimeter: 64
            with BuildLine():
                Line((10, -6), (10, 6))
                Line((10, 6), (-10, 6))
                Line((-10, 6), (-10, -6))
                Line((-10, -6), (10, -6))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a bent or curved duct elbow connector with two rectangular flanged ends positioned at approximately 90 degrees to each other, featuring mesh or perforated sections on the interior surfaces for structural support or airflow distribution.
def model_145587_b07d242e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Top -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.2044436014, perimeter: 2.6338732608
            with BuildLine():
                Line((-1.5870900617, -2.6930730184), (-2.0388066519, -1.563781543))
                Line((-2.2000000328, -1.7000000253), (-2.0388066519, -1.563781543))
                Line((-2.2000000328, -1.7000000253), (-1.89339738, -2.4665066572))
                Line((-1.89339738, -2.4665066572), (-1.5870900617, -2.6930730184))
            make_face()
            # Profile area: 0.4168008772, perimeter: 4.0329889621
            with BuildLine():
                CenterArc((-0.5127339276, -2.5003322093), 0.799930397, -149.4172622232, 15.8571780631)
                Line((-1.2013902893, -2.9073224493), (-1.8145955949, -1.3743091856))
                Line((-2.0388066519, -1.563781543), (-1.8145955949, -1.3743091856))
                Line((-1.5870900617, -2.6930730184), (-2.0388066519, -1.563781543))
                Line((-1.5870900617, -2.6930730184), (-1.0639778614, -3.0800034657))
            make_face()
            # Profile area: 2.8063616733, perimeter: 13.9394368335
            with BuildLine():
                CenterArc((0.5127339276, -2.5003322093), 0.799930397, -46.4399158398, 15.8571780631)
                Line((1.2013902893, -2.9073224493), (1.8145955949, -1.3743091856))
                Line((1.8145955949, -1.3743091856), (1.4884260432, -1.0986755271))
                CenterArc((0, 0), 1.85, -74.9740625916, 38.5413268242)
                Line((0.4796241302, -2.0004153486), (0.4796241302, -1.7867458392))
                CenterArc((0.5, -2.5), 0.5, -90, 182.3355494337)
                Line((0.5, -3), (0, -3))
                Line((-0.5, -3), (0, -3))
                CenterArc((-0.5, -2.5), 0.5, 87.6644505663, 182.3355494337)
                Line((-0.4796241302, -2.0004153486), (-0.4796241302, -1.7867458392))
                CenterArc((0, 0), 1.85, -143.5672642326, 38.5413268242)
                Line((-1.8145955949, -1.3743091856), (-1.4884260432, -1.0986755271))
                Line((-1.2013902893, -2.9073224493), (-1.8145955949, -1.3743091856))
                CenterArc((-0.5127339276, -2.5003322093), 0.799930397, -149.4172622232, 15.8571780631)
                CenterArc((-0.5127339276, -2.5003322093), 0.799930397, -133.5600841602, 43.5628178706)
                Line((-0.5126957611, -3.3002626054), (0, -3.3002381435))
                Line((0.5126957611, -3.3002626054), (0, -3.3002381435))
                CenterArc((0.5127339276, -2.5003322093), 0.799930397, -90.0027337104, 43.5628178706)
            make_face()
            # Profile area: 0.4168008772, perimeter: 4.0329889621
            with BuildLine():
                Line((1.5870900617, -2.6930730184), (2.0388066519, -1.563781543))
                Line((2.0388066519, -1.563781543), (1.8145955949, -1.3743091856))
                Line((1.2013902893, -2.9073224493), (1.8145955949, -1.3743091856))
                CenterArc((0.5127339276, -2.5003322093), 0.799930397, -46.4399158398, 15.8571780631)
                Line((1.5870900617, -2.6930730184), (1.0639778614, -3.0800034657))
            make_face()
            # Profile area: 0.2044436014, perimeter: 2.6338732608
            with BuildLine():
                Line((2.2000000328, -1.7000000253), (2.0388066519, -1.563781543))
                Line((1.5870900617, -2.6930730184), (2.0388066519, -1.563781543))
                Line((1.89339738, -2.4665066572), (1.5870900617, -2.6930730184))
                Line((2.2000000328, -1.7000000253), (1.89339738, -2.4665066572))
            make_face()
        # TwoSides extrude, along=0.9, against=-0.3
        extrude(amount=0.9)
        extrude(sk.sketch, amount=-0.3)

        # Top -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4168008772, perimeter: 4.0329889621
            with BuildLine():
                CenterArc((-0.5127339276, -2.5003322093), 0.799930397, -149.4172622232, 15.8571780631)
                Line((-1.2013902893, -2.9073224493), (-1.8145955949, -1.3743091856))
                Line((-2.0388066519, -1.563781543), (-1.8145955949, -1.3743091856))
                Line((-1.5870900617, -2.6930730184), (-2.0388066519, -1.563781543))
                Line((-1.5870900617, -2.6930730184), (-1.0639778614, -3.0800034657))
            make_face()
            # Profile area: 0.4168008772, perimeter: 4.0329889621
            with BuildLine():
                Line((1.5870900617, -2.6930730184), (2.0388066519, -1.563781543))
                Line((2.0388066519, -1.563781543), (1.8145955949, -1.3743091856))
                Line((1.2013902893, -2.9073224493), (1.8145955949, -1.3743091856))
                CenterArc((0.5127339276, -2.5003322093), 0.799930397, -46.4399158398, 15.8571780631)
                Line((1.5870900617, -2.6930730184), (1.0639778614, -3.0800034657))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a uniform thickness, featuring a simple geometric form with no holes, slots, or additional features—appearing to be a basic structural or mounting component.
def model_145702_e28c737e_0048():
    """Model: ?????? v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((5, -5), (5, 5))
                Line((5, 5), (-5, 5))
                Line((-5, 5), (-5, -5))
                Line((-5, -5), (5, -5))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a straight cylindrical rod or pin with a uniform diameter and tapered or rounded ends, appearing to be a simple mechanical component used for alignment, support, or fastening purposes.
def model_146004_f79f7c2f_0002():
    """Model: pole for the wheel v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # Symmetric extrude, each_side=3.25
        extrude(amount=3.25, both=True)
    return part.part


# Description: This is a truncated octahedron or rounded cube polyhedron featuring a regular geometric shape with multiple flat faceted surfaces, hexagonal and square faces, and no holes, slots, or curves—purely angular geometric form.
def model_146075_8bb6e65a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4871392896, perimeter: 2.5980762114
            with BuildLine():
                Line((0.2165063509, 0.375), (-0.2165063509, 0.375))
                Line((-0.2165063509, 0.375), (-0.4330127019, 0))
                Line((-0.4330127019, 0), (-0.2165063509, -0.375))
                Line((-0.2165063509, -0.375), (0.2165063509, -0.375))
                Line((0.2165063509, -0.375), (0.4330127019, 0))
                Line((0.4330127019, 0), (0.2165063509, 0.375))
            make_face()
        # OneSide extrude, distance=0.313
        extrude(amount=0.313)
    return part.part


# Description: A dark gray parallelogram-shaped flat plate with rounded corners and subtle surface detailing or markings on its upper face.
def model_146131_6ddecf51_0000():
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
        with BuildSketch(Plane.XY):
            # Profile area: 14.5487005046, perimeter: 91.4376520109
            with BuildLine():
                Line((7.9483269215, -2.7994331222), (9.5381802575, 1.6620685159))
                _nurbs_edge([(9.5381802575, 1.6620685159), (9.7612548937, 2.2852623038), (9.2974012509, 2.9403240126), (8.6387984518, 2.9403240126)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((8.6387984518, 2.9403240126), (-6.9799982367, 2.9403240126))
                _nurbs_edge([(-6.9799982367, 2.9403240126), (-7.3836579383, 2.9403240126), (-7.7448269886, 2.6853811853), (-7.879380245, 2.3065074944)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-7.879380245, 2.3065074944), (-9.4692327706, -2.1549936035))
                _nurbs_edge([(-9.4692327706, -2.1549936035), (-9.6923078795, -2.7781876615), (-9.2319942126, -3.4332493702), (-8.5698507623, -3.4332493702)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-8.5698507623, -3.4332493702), (7.0489451158, -3.4332493702))
                _nurbs_edge([(7.0489451158, -3.4332493702), (7.4526045472, -3.4332493702), (7.8137741378, -3.1783060027), (7.9483269215, -2.7994331222)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(7.0489451158, -3.1145707011), (7.3180517636, -3.1145707011), (7.5588307703, -2.9446086362), (7.650893713, -2.6896658089)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-8.5698507623, -3.1145707011), (7.0489451158, -3.1145707011))
                _nurbs_edge([(-9.1717993596, -2.2647609167), (-9.3205160651, -2.6790430786), (-9.012460025, -3.1145707011), (-8.5698507623, -3.1145707011)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-7.581946834, 2.1967404512), (-9.1717993596, -2.2647609167))
                _nurbs_edge([(-6.9799982367, 2.6216453434), (-7.2491046144, 2.6216453434), (-7.4898841614, 2.4516832785), (-7.581946834, 2.1967404512)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((8.6387973713, 2.6216453434), (-6.9799982367, 2.6216453434))
                _nurbs_edge([(9.2407459685, 1.7718355591), (9.389463113, 2.1861177209), (9.081406634, 2.6216453434), (8.6387973713, 2.6216453434)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((7.650893713, -2.6896658089), (9.2407459685, 1.7718355591))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 63.3253265716, perimeter: 152.7937073021
            with BuildLine():
                Line((7.650893713, -2.6896658089), (9.2407459685, 1.7718355591))
                _nurbs_edge([(9.2407459685, 1.7718355591), (9.389463113, 2.1861177209), (9.081406634, 2.6216453434), (8.6387973713, 2.6216453434)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((8.6387973713, 2.6216453434), (-6.9799982367, 2.6216453434))
                _nurbs_edge([(-6.9799982367, 2.6216453434), (-7.2491046144, 2.6216453434), (-7.4898841614, 2.4516832785), (-7.581946834, 2.1967404512)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-7.581946834, 2.1967404512), (-9.1717993596, -2.2647609167))
                _nurbs_edge([(-9.1717993596, -2.2647609167), (-9.3205160651, -2.6790430786), (-9.012460025, -3.1145707011), (-8.5698507623, -3.1145707011)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-8.5698507623, -3.1145707011), (7.0489451158, -3.1145707011))
                _nurbs_edge([(7.0489451158, -3.1145707011), (7.3180517636, -3.1145707011), (7.5588307703, -2.9446086362), (7.650893713, -2.6896658089)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-6.8596084632, -2.2045656248), (-6.6861055782, -2.1797796141), (-6.5126026932, -2.1408297829), (-6.3532633586, -2.0664717509)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.9602263874, 0.2882095266), (-6.3036910672, -0.5261915167), (-6.6188289163, -1.3547558404), (-6.8596084632, -2.2045656248)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.1499600315, -1.510554625), (-6.7887908461, -0.887360567), (-6.4028356501, -0.2783303296), (-5.9602263874, 0.2882095266)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.3270037366, -1.7584158121), (-7.270349805, -1.751334172), (-7.2243183336, -1.6380263088), (-7.1499600315, -1.510554625)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.3553307024, -1.5034729849), (-7.3588715224, -1.6274035784), (-7.3765758929, -1.7654974523), (-7.3270037366, -1.7584158121)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.1180921105, 0.2350964151), (-7.2136957383, -0.3420661715), (-7.3376263319, -0.9192287581), (-7.3553307024, -1.5034729849)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.0351785569, -2.3532827693), (-7.7696129993, -1.475145884), (-7.4969656664, -0.5970089988), (-7.1180921105, 0.2350964151)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.5698505935, -2.4772133628), (-8.3042850696, -2.480754453), (-8.1237004094, -2.3993142406), (-8.0351785569, -2.3532827693)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.49195137, -2.208106715), (-8.516737482, -2.2966285675), (-8.5415235939, -2.3886915103), (-8.5698505935, -2.4772133628)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.0154068426, 1.8072443001), (-7.7873173698, -0.1119093549), (-8.2759579688, -1.4539009636), (-8.49195137, -2.208106715)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.3497225386, 1.7859991095), (-6.5550933445, 1.8674393219), (-6.7958726213, 1.839112221), (-7.0154068426, 1.8072443001)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.6719421629, -0.0517146032), (-6.5869612655, 0.5643972743), (-6.470112312, 1.1769686019), (-6.3497225386, 1.7859991095)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.2272655564, 1.8603574116), (-5.7548558516, 1.2584088143), (-6.2293327651, 0.6139698359), (-6.6719421629, -0.0517146032)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.7138388117, 1.7576720086), (-4.8590145958, 1.8532755013), (-5.0537626714, 1.8603574116), (-5.2272655564, 1.8603574116)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.3532633586, -2.0664717509), (-5.8858680853, -0.7634305138), (-5.3653597004, 0.5325296235), (-4.7138388117, 1.7576720086)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(-2.8300936276, 1.4744023506), (-2.8336347178, 1.4921067211), (-2.8832067391, 1.7859993796), (-3.2089670484, 1.8249489407)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.1664766672, 0.2315553249), (-2.8938294695, 0.791013541), (-2.7840621562, 1.244245534), (-2.8300936276, 1.4744023506)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.1933301567, -1.3618380208), (-3.7790479949, -0.8873611073), (-3.439123865, -0.3385256216), (-3.1664766672, 0.2315553249)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.1847751753, -2.0487673804), (-4.788197384, -1.9885726287), (-4.4588959844, -1.6663528694), (-4.1933301567, -1.3618380208)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.6061392474, -1.8717236753), (-5.4786678338, -2.1302075928), (-5.1989387257, -2.0523084706), (-5.1847751753, -2.0487673804)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.4467999128, -0.4872416855), (-5.6698750893, -1.1210579336), (-5.7194471106, -1.6415668587), (-5.6061392474, -1.8717236753)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.2499843584, 1.4779434409), (-4.5615813874, 1.1946735127), (-5.0785489522, 0.5643978146), (-5.4467999128, -0.4872416855)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.3151938117, 1.9347159838), (-3.8144572762, 1.8886845125), (-4.1083493944, 1.6089556746), (-4.2499843584, 1.4779434409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.3116527215, 1.8355714009), (-3.3116527215, 1.8674393219), (-3.3081116313, 1.9028480629), (-3.3151938117, 1.9347159838)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.2089670484, 1.8249489407), (-3.2408352395, 1.8355714009), (-3.2762439805, 1.8355714009), (-3.3116527215, 1.8355714009)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(-2.3131263329, 0.3306999078), (-2.1360826279, 0.6635418572), (-1.9519572826, 0.9928432567), (-1.7465864767, 1.3115219259)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.5022663798, 0.3590270086), (-1.6474424341, 0.3979768399), (-1.9236301818, 0.3731902889), (-2.3131263329, 0.3306999078)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.8528126997, -0.1721041066), (-1.721800466, -0.0056831319), (-1.6084926028, 0.1749016634), (-1.5022663798, 0.3590270086)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.6211822717, -0.253544319), (-2.3662394445, -0.2075128476), (-2.1112966172, -0.1756451968), (-1.8528126997, -0.1721041066)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.9929740524, -1.0396182615), (-2.8832067391, -0.7705116136), (-2.7521945054, -0.5120282365), (-2.6211822717, -0.253544319)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.1608686385, -0.9369331286), (-2.4405974764, -0.9510964089), (-2.7167857644, -0.9971278803), (-2.9929740524, -1.0396182615)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.4087298256, -1.5211773554), (-2.3166668829, -1.32997037), (-2.2210633902, -1.1387628444), (-2.1608686385, -0.9369331286)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.7719663547, -1.7796612729), (-3.3187343617, -1.6875983301), (-2.8655023686, -1.5990764776), (-2.4087298256, -1.5211773554)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.6657401317, -1.404328402), (-3.7082305128, -1.5282589955), (-3.7400987039, -1.6557306793), (-3.7719663547, -1.7796612729)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.3662394445, 1.1982140627), (-3.2904078011, -0.395179283), (-3.6338724809, -1.3122659995), (-3.6657401317, -1.404328402)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.1148371671, 1.768294739), (-2.1998179294, 1.5770874835), (-2.2635537713, 1.3787983177), (-2.3662394445, 1.1982140627)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.7996995882, 1.8426530411), (-1.9059258113, 1.8284894907), (-2.0121520343, 1.80370348), (-2.1148371671, 1.768294739)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.5851796633, 1.8249486706), (-0.7976321094, 1.8886845125), (-1.2189959114, 1.9276340736), (-1.7996995882, 1.8426530411)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.9428081637, 1.3363079365), (-0.8047142898, 1.4850245407), (-0.6878653364, 1.6514457856), (-0.5851796633, 1.8249486706)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.7465864767, 1.3115219259), (-1.3712536058, 1.4000437784), (-1.0915247679, 1.3575533972), (-0.9428081637, 1.3363079365)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(-0.4541668893, 1.5487603826), (-0.4577079795, 1.5416787425), (-0.549770382, 1.3150624758), (-0.3798083171, 1.2867359152)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.254007931, 1.9807469149), (0.1052913268, 2.0055329256), (-0.2877459146, 1.913470253), (-0.4541668893, 1.5487603826)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.254007931, 1.5664647531), (0.2610901114, 1.5770874835), (0.5124913082, 1.9382565338), (0.254007931, 1.9807469149)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.4470852492, 0.9149441345), (-0.1744380514, 1.0778245593), (0.0734231357, 1.3044402857), (0.254007931, 1.5664647531)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.6489149649, 0.8866170337), (-0.620587864, 0.791013541), (-0.4789529, 0.897239764), (-0.4470852492, 0.9149441345)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.262959904, 1.2867359152), (-0.3514817565, 1.1238554904), (-0.5037394509, 1.0034659871), (-0.6489149649, 0.8866170337)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.3798083171, 1.2867359152), (-0.3408595664, 1.2761131848), (-0.298368645, 1.283194825), (-0.262959904, 1.2867359152)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(-0.2027656926, -0.8059203546), (-0.2169289729, -0.8094614449), (-0.5426898224, -0.890901117), (-0.5993434839, -0.6182539192)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.2398435701, -0.3279023509), (0.2575479406, -0.4447513043), (0.1052902462, -0.7386439628), (-0.2027656926, -0.8059203546)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.1567347615, 0.0261850592), (-0.0363452582, -0.1048271745), (0.211515929, -0.1543997361), (0.2398435701, -0.3279023509)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.0611312688, 0.7733097108), (-0.1921435025, 0.5573161745), (-0.3231557362, 0.2138514947), (-0.1567347615, 0.0261850592)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.8969722174, 1.9170121536), (1.4826895153, 1.963043625), (0.5054091277, 1.7116413477), (-0.0611312688, 0.7733097108)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.1731599651, 1.6797736969), (2.2262730766, 1.9063896934), (1.9075944075, 1.9170121536), (1.8969722174, 1.9170121536)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6916008712, 1.0494979987), (2.0633926518, 1.3858810384), (2.1660777847, 1.6549874161), (2.1731599651, 1.6797736969)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.0223758821, 0.8264228223), (1.2560737889, 0.8441271928), (1.5180982563, 0.8901586642), (1.6916008712, 1.0494979987)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.433117494, 1.3186041063), (1.4295764038, 1.2973586456), (1.3127279907, 1.1132333003), (1.0223758821, 0.8264228223)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.3693821924, 1.3858804981), (1.3870865629, 1.3823394079), (1.4401996744, 1.3610944875), (1.433117494, 1.3186041063)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.685993923, 1.0317930879), (0.9409372906, 1.3044402857), (1.2312883186, 1.4071259588), (1.3693821924, 1.3858804981)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.4629192869, 0.514825253), (0.4062650851, 0.6918689581), (0.5585233198, 0.8936986738), (0.685993923, 1.0317930879)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.8134656068, 0.2067693142), (0.7001572033, 0.3129955373), (0.508950218, 0.3661086488), (0.4629192869, 0.514825253)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.8949052789, -0.2393810387), (0.9019874593, -0.2252177584), (1.0223769627, 0.0084801484), (0.8134656068, 0.2067693142)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.2079759193, -1.0254549812), (0.5018680375, -0.8377885457), (0.7568114051, -0.5580597078), (0.8949052789, -0.2393810387)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.847204671, -1.3228881896), (-0.6489155052, -1.3547558404), (-0.2381744336, -1.3122654592), (0.2079759193, -1.0254549812)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.0667387572, -1.1139768337), (-1.0915247679, -1.259152888), (-0.9038583325, -1.3158065494), (-0.847204671, -1.3228881896)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.6205884043, -0.5014055061), (-0.9463487136, -0.8554929162), (-1.063197667, -1.0891908231), (-1.0667387572, -1.1139768337)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.5993434839, -0.6182539192), (-0.6170473141, -0.5757640783), (-0.6205884043, -0.5403553373), (-0.6205884043, -0.5014055061)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(3.961302467, -1.4078700325), (4.1454283525, -1.1316817445), (4.3295531574, -0.7421855933), (4.198541464, -0.4376707448)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6384888402, -2.470132263), (2.1058846539, -2.5197042843), (3.2743731074, -2.434723522), (3.961302467, -1.4078700325)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.905527469, -1.9283784174), (0.8878230985, -2.3674465898), (1.4720673252, -2.4524278925), (1.6384888402, -2.470132263)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.001131502, -1.7690390828), (0.9621816707, -1.8150705542), (0.9090685592, -1.8646425755), (0.905527469, -1.9283784174)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6101622797, -1.3299709103), (1.475609496, -1.3653796513), (1.2348294088, -1.4928513351), (1.001131502, -1.7690390828)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.730551783, -1.6061591983), (1.6632753912, -1.5318006261), (1.6278666502, -1.4291154932), (1.6101622797, -1.3299709103)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.424563323, -1.7265487016), (2.1944065064, -1.7761207229), (1.8863500273, -1.7796618132), (1.730551783, -1.6061591983)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.3133229386, -0.9758835002), (3.2779141976, -1.184794856), (2.976939899, -1.6132408385), (2.424563323, -1.7265487016)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.0973294023, -0.6642864712), (3.1079515924, -0.6678275614), (3.3522727699, -0.7386450434), (3.3133229386, -0.9758835002)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.2546017984, -0.6713681113), (2.5343306363, -0.6395004605), (2.8317638447, -0.5722235284), (3.0973294023, -0.6642864712)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.4741364249, -0.0304696828), (2.3537469216, -0.2216766682), (2.1908664968, -0.455374575), (2.2546017984, -0.6713681113)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.8550773245, 0.3873535692), (3.4443357126, 0.1394923821), (2.9486133384, 0.0545116198), (2.4741364249, -0.0304696828)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.3614218888, 1.0813651093), (4.3791262593, 0.7945540909), (4.0993974214, 0.5360707137), (3.8550773245, 0.3873535692)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.198541464, 1.2584088143), (4.3507986182, 1.244245534), (4.3614218888, 1.0884467494), (4.3614218888, 1.0813651093)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.6901288806, 0.6316742064), (3.3593538697, 1.0494974585), (3.9011082556, 1.2867359152), (4.198541464, 1.2584088143)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.6795066906, 0.9255668649), (2.6724245101, 0.8299633722), (2.6759656003, 0.7308187893), (2.6901288806, 0.6316742064)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.7609463627, 1.2938175553), (2.7538641822, 1.283194825), (2.7007510707, 1.1628053216), (2.6795066906, 0.9255668649)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.1044115828, 1.5168927318), (2.8777958564, 1.3929621382), (2.7680285431, 1.3079813759), (2.7609463627, 1.2938175553)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.5136790429, 1.9807474552), (4.2410313049, 1.9595022646), (3.7346867406, 1.8568168617), (3.1044115828, 1.5168927318)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.3457844568, 1.6620687861), (5.2041494927, 1.9240935236), (4.8111122514, 2.0055334659), (4.5136790429, 1.9807474552)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.11208655, 0.7308187893), (5.3068346256, 0.9857616166), (5.5015827012, 1.378798858), (5.3457844568, 1.6620687861)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.8515351537, -0.1366953656), (4.1171007113, -0.0446324228), (4.6588540166, 0.1465745626), (5.11208655, 0.7308187893)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.198541464, -0.4376707448), (4.1135607017, -0.2287583083), (3.9294348162, -0.1650224664), (3.8515351537, -0.1366953656)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(6.1672655194, 0.1465745626), (6.4115856163, 0.5183663432), (6.6771511739, 0.8795353935), (6.9604211021, 1.2230000733)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(7.477388937, 0.1465745626), (7.275558681, 0.2775867963), (6.7550508364, 0.3767313792), (6.1672655194, 0.1465745626)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(7.6190239011, -0.6324177398), (7.6650548322, -0.4943238659), (7.7996086964, -0.0623367933), (7.477388937, 0.1465745626)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.7196420954, -1.8858869556), (7.1233015268, -1.5672082865), (7.4490623764, -1.1175173836), (7.6190239011, -0.6324177398)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.4959735918, -2.349741679), (4.8819286528, -2.5090810136), (5.8556690307, -2.5657352154), (6.7196420954, -1.8858869556)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.1135596211, -1.9531638877), (4.1489683621, -2.133748683), (4.3260120672, -2.278924197), (4.4959735918, -2.349741679)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.1383461721, -1.8717236753), (4.1312639916, -1.8858869556), (4.102937431, -1.9142140565), (4.1135596211, -1.9531638877)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.7686213299, -1.1812532255), (4.5278423232, -1.3795423913), (4.3047666065, -1.6096992079), (4.1383461721, -1.8717236753)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.8217344414, -1.3972467618), (4.7969478905, -1.3264292798), (4.7827846102, -1.2520707076), (4.7686213299, -1.1812532255)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.1651996615, -1.7336298015), (4.8748475529, -1.6486490392), (4.8252755316, -1.4149511324), (4.8217344414, -1.3972467618)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.1106134789, -1.5211773554), (5.6219732851, -1.8894280458), (5.1970683929, -1.7442525319), (5.1651996615, -1.7336298015)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.5744682023, -0.8236252654), (6.5638460122, -0.9758829599), (6.4328332382, -1.2768572585), (6.1106134789, -1.5211773554)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.2097586021, -0.4766194954), (6.2274629726, -0.4766194954), (6.5992547532, -0.5049465963), (6.5744682023, -0.8236252654)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.189987293, -0.7457261433), (5.5086659622, -0.5970095391), (5.8592122821, -0.4447518446), (6.2097586021, -0.4766194954)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.9067173649, -0.4518334848), (4.9279628256, -0.5863868087), (5.0589745191, -0.7032357621), (5.189987293, -0.7457261433)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.2183138536, 0.0297256091), (5.1120876306, -0.1296137254), (5.0058614075, -0.28895306), (4.9067173649, -0.4518334848)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.4859463497, 1.7789174693), (6.4363743284, 1.7258043578), (5.9831417951, 1.1628053216), (5.2183138536, 0.0297256091)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.8223293894, 1.8922253325), (6.7585940878, 1.8886845125), (6.5992547532, 1.909929703), (6.4859463497, 1.7789174693)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(8.6387973713, 1.8993069727), (8.0333076838, 1.9453384441), (7.4278179963, 1.9347157137), (6.8223293894, 1.8922253325)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(8.3732318136, 1.2407044438), (8.4865402171, 1.4496157997), (8.5750620697, 1.6726909762), (8.6387973713, 1.8993069727)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.9604211021, 1.2230000733), (7.2153655502, 1.2548677241), (7.6898435443, 1.2867359152), (8.3732318136, 1.2407044438)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.3167177205, perimeter: 25.1722732042
            with BuildLine():
                _nurbs_edge([(-6.3532633586, -2.0664717509), (-5.8858680853, -0.7634305138), (-5.3653597004, 0.5325296235), (-4.7138388117, 1.7576720086)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.7138388117, 1.7576720086), (-4.8590145958, 1.8532755013), (-5.0537626714, 1.8603574116), (-5.2272655564, 1.8603574116)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.2272655564, 1.8603574116), (-5.7548558516, 1.2584088143), (-6.2293327651, 0.6139698359), (-6.6719421629, -0.0517146032)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.6719421629, -0.0517146032), (-6.5869612655, 0.5643972743), (-6.470112312, 1.1769686019), (-6.3497225386, 1.7859991095)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.3497225386, 1.7859991095), (-6.5550933445, 1.8674393219), (-6.7958726213, 1.839112221), (-7.0154068426, 1.8072443001)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.0154068426, 1.8072443001), (-7.7873173698, -0.1119093549), (-8.2759579688, -1.4539009636), (-8.49195137, -2.208106715)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.49195137, -2.208106715), (-8.516737482, -2.2966285675), (-8.5415235939, -2.3886915103), (-8.5698505935, -2.4772133628)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.5698505935, -2.4772133628), (-8.3042850696, -2.480754453), (-8.1237004094, -2.3993142406), (-8.0351785569, -2.3532827693)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.0351785569, -2.3532827693), (-7.7696129993, -1.475145884), (-7.4969656664, -0.5970089988), (-7.1180921105, 0.2350964151)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.1180921105, 0.2350964151), (-7.2136957383, -0.3420661715), (-7.3376263319, -0.9192287581), (-7.3553307024, -1.5034729849)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.3553307024, -1.5034729849), (-7.3588715224, -1.6274035784), (-7.3765758929, -1.7654974523), (-7.3270037366, -1.7584158121)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.3270037366, -1.7584158121), (-7.270349805, -1.751334172), (-7.2243183336, -1.6380263088), (-7.1499600315, -1.510554625)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.1499600315, -1.510554625), (-6.7887908461, -0.887360567), (-6.4028356501, -0.2783303296), (-5.9602263874, 0.2882095266)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.9602263874, 0.2882095266), (-6.3036910672, -0.5261915167), (-6.6188289163, -1.3547558404), (-6.8596084632, -2.2045656248)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.8596084632, -2.2045656248), (-6.6861055782, -2.1797796141), (-6.5126026932, -2.1408297829), (-6.3532633586, -2.0664717509)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 4.529562844, perimeter: 16.7929365652
            with BuildLine():
                _nurbs_edge([(-3.2089670484, 1.8249489407), (-3.2408352395, 1.8355714009), (-3.2762439805, 1.8355714009), (-3.3116527215, 1.8355714009)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.3116527215, 1.8355714009), (-3.3116527215, 1.8674393219), (-3.3081116313, 1.9028480629), (-3.3151938117, 1.9347159838)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.3151938117, 1.9347159838), (-3.8144572762, 1.8886845125), (-4.1083493944, 1.6089556746), (-4.2499843584, 1.4779434409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.2499843584, 1.4779434409), (-4.5615813874, 1.1946735127), (-5.0785489522, 0.5643978146), (-5.4467999128, -0.4872416855)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.4467999128, -0.4872416855), (-5.6698750893, -1.1210579336), (-5.7194471106, -1.6415668587), (-5.6061392474, -1.8717236753)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.6061392474, -1.8717236753), (-5.4786678338, -2.1302075928), (-5.1989387257, -2.0523084706), (-5.1847751753, -2.0487673804)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.1847751753, -2.0487673804), (-4.788197384, -1.9885726287), (-4.4588959844, -1.6663528694), (-4.1933301567, -1.3618380208)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.1933301567, -1.3618380208), (-3.7790479949, -0.8873611073), (-3.439123865, -0.3385256216), (-3.1664766672, 0.2315553249)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.1664766672, 0.2315553249), (-2.8938294695, 0.791013541), (-2.7840621562, 1.244245534), (-2.8300936276, 1.4744023506)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.8300936276, 1.4744023506), (-2.8336347178, 1.4921067211), (-2.8832067391, 1.7859993796), (-3.2089670484, 1.8249489407)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-3.7896707252, 0.0934609107), (-3.7967523654, 0.0686749001), (-3.810916186, 0.0438888894), (-3.8250794662, 0.0155617886)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.8250794662, 0.0155617886), (-4.1756257862, -0.696154122), (-4.5084682759, -1.1741721257), (-4.7704927433, -1.3264292798)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.7704927433, -1.3264292798), (-4.7775743834, -1.32997037), (-4.9616999988, -1.439737143), (-5.0289766608, -1.2910205388)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.0289766608, -1.2910205388), (-5.0997941428, -1.128140114), (-5.0112722903, -0.7740527039), (-4.8377694053, -0.3385256216)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.8377694053, -0.3385256216), (-4.5261723763, 0.4404666807), (-4.1260537649, 0.9114030443), (-3.8640292975, 1.0955283895)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.8640292975, 1.0955283895), (-3.810916186, 1.1344782208), (-3.6161681104, 1.2761131848), (-3.5099418873, 1.1380187707)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.5099418873, 1.1380187707), (-3.3860112938, 0.9822205263), (-3.5595139086, 0.5643972743), (-3.7896707252, 0.0934609107)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7700136869, perimeter: 6.2970165798
            with BuildLine():
                _nurbs_edge([(-3.5099418873, 1.1380187707), (-3.3860112938, 0.9822205263), (-3.5595139086, 0.5643972743), (-3.7896707252, 0.0934609107)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.8640292975, 1.0955283895), (-3.810916186, 1.1344782208), (-3.6161681104, 1.2761131848), (-3.5099418873, 1.1380187707)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.8377694053, -0.3385256216), (-4.5261723763, 0.4404666807), (-4.1260537649, 0.9114030443), (-3.8640292975, 1.0955283895)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.0289766608, -1.2910205388), (-5.0997941428, -1.128140114), (-5.0112722903, -0.7740527039), (-4.8377694053, -0.3385256216)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.7704927433, -1.3264292798), (-4.7775743834, -1.32997037), (-4.9616999988, -1.439737143), (-5.0289766608, -1.2910205388)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.8250794662, 0.0155617886), (-4.1756257862, -0.696154122), (-4.5084682759, -1.1741721257), (-4.7704927433, -1.3264292798)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.7896707252, 0.0934609107), (-3.7967523654, 0.0686749001), (-3.810916186, 0.0438888894), (-3.8250794662, 0.0155617886)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 3.2962891604, perimeter: 13.9782078832
            with BuildLine():
                _nurbs_edge([(-1.7465864767, 1.3115219259), (-1.3712536058, 1.4000437784), (-1.0915247679, 1.3575533972), (-0.9428081637, 1.3363079365)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.9428081637, 1.3363079365), (-0.8047142898, 1.4850245407), (-0.6878653364, 1.6514457856), (-0.5851796633, 1.8249486706)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.5851796633, 1.8249486706), (-0.7976321094, 1.8886845125), (-1.2189959114, 1.9276340736), (-1.7996995882, 1.8426530411)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.7996995882, 1.8426530411), (-1.9059258113, 1.8284894907), (-2.0121520343, 1.80370348), (-2.1148371671, 1.768294739)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.1148371671, 1.768294739), (-2.1998179294, 1.5770874835), (-2.2635537713, 1.3787983177), (-2.3662394445, 1.1982140627)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.3662394445, 1.1982140627), (-3.2904078011, -0.395179283), (-3.6338724809, -1.3122659995), (-3.6657401317, -1.404328402)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.6657401317, -1.404328402), (-3.7082305128, -1.5282589955), (-3.7400987039, -1.6557306793), (-3.7719663547, -1.7796612729)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.7719663547, -1.7796612729), (-3.3187343617, -1.6875983301), (-2.8655023686, -1.5990764776), (-2.4087298256, -1.5211773554)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.4087298256, -1.5211773554), (-2.3166668829, -1.32997037), (-2.2210633902, -1.1387628444), (-2.1608686385, -0.9369331286)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.1608686385, -0.9369331286), (-2.4405974764, -0.9510964089), (-2.7167857644, -0.9971278803), (-2.9929740524, -1.0396182615)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.9929740524, -1.0396182615), (-2.8832067391, -0.7705116136), (-2.7521945054, -0.5120282365), (-2.6211822717, -0.253544319)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.6211822717, -0.253544319), (-2.3662394445, -0.2075128476), (-2.1112966172, -0.1756451968), (-1.8528126997, -0.1721041066)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.8528126997, -0.1721041066), (-1.721800466, -0.0056831319), (-1.6084926028, 0.1749016634), (-1.5022663798, 0.3590270086)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.5022663798, 0.3590270086), (-1.6474424341, 0.3979768399), (-1.9236301818, 0.3731902889), (-2.3131263329, 0.3306999078)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.3131263329, 0.3306999078), (-2.1360826279, 0.6635418572), (-1.9519572826, 0.9928432567), (-1.7465864767, 1.3115219259)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 0.5080779611, perimeter: 3.5835362472
            with BuildLine():
                _nurbs_edge([(-0.3798083171, 1.2867359152), (-0.3408595664, 1.2761131848), (-0.298368645, 1.283194825), (-0.262959904, 1.2867359152)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.262959904, 1.2867359152), (-0.3514817565, 1.1238554904), (-0.5037394509, 1.0034659871), (-0.6489149649, 0.8866170337)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.6489149649, 0.8866170337), (-0.620587864, 0.791013541), (-0.4789529, 0.897239764), (-0.4470852492, 0.9149441345)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.4470852492, 0.9149441345), (-0.1744380514, 1.0778245593), (0.0734231357, 1.3044402857), (0.254007931, 1.5664647531)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.254007931, 1.5664647531), (0.2610901114, 1.5770874835), (0.5124913082, 1.9382565338), (0.254007931, 1.9807469149)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.254007931, 1.9807469149), (0.1052913268, 2.0055329256), (-0.2877459146, 1.913470253), (-0.4541668893, 1.5487603826)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.4541668893, 1.5487603826), (-0.4577079795, 1.5416787425), (-0.549770382, 1.3150624758), (-0.3798083171, 1.2867359152)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 3.0491035806, perimeter: 13.3417979929
            with BuildLine():
                _nurbs_edge([(-0.5993434839, -0.6182539192), (-0.6170473141, -0.5757640783), (-0.6205884043, -0.5403553373), (-0.6205884043, -0.5014055061)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.6205884043, -0.5014055061), (-0.9463487136, -0.8554929162), (-1.063197667, -1.0891908231), (-1.0667387572, -1.1139768337)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.0667387572, -1.1139768337), (-1.0915247679, -1.259152888), (-0.9038583325, -1.3158065494), (-0.847204671, -1.3228881896)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.847204671, -1.3228881896), (-0.6489155052, -1.3547558404), (-0.2381744336, -1.3122654592), (0.2079759193, -1.0254549812)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.2079759193, -1.0254549812), (0.5018680375, -0.8377885457), (0.7568114051, -0.5580597078), (0.8949052789, -0.2393810387)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.8949052789, -0.2393810387), (0.9019874593, -0.2252177584), (1.0223769627, 0.0084801484), (0.8134656068, 0.2067693142)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.8134656068, 0.2067693142), (0.7001572033, 0.3129955373), (0.508950218, 0.3661086488), (0.4629192869, 0.514825253)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.4629192869, 0.514825253), (0.4062650851, 0.6918689581), (0.5585233198, 0.8936986738), (0.685993923, 1.0317930879)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.685993923, 1.0317930879), (0.9409372906, 1.3044402857), (1.2312883186, 1.4071259588), (1.3693821924, 1.3858804981)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.3693821924, 1.3858804981), (1.3870865629, 1.3823394079), (1.4401996744, 1.3610944875), (1.433117494, 1.3186041063)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.433117494, 1.3186041063), (1.4295764038, 1.2973586456), (1.3127279907, 1.1132333003), (1.0223758821, 0.8264228223)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.0223758821, 0.8264228223), (1.2560737889, 0.8441271928), (1.5180982563, 0.8901586642), (1.6916008712, 1.0494979987)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6916008712, 1.0494979987), (2.0633926518, 1.3858810384), (2.1660777847, 1.6549874161), (2.1731599651, 1.6797736969)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.1731599651, 1.6797736969), (2.2262730766, 1.9063896934), (1.9075944075, 1.9170121536), (1.8969722174, 1.9170121536)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.8969722174, 1.9170121536), (1.4826895153, 1.963043625), (0.5054091277, 1.7116413477), (-0.0611312688, 0.7733097108)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.0611312688, 0.7733097108), (-0.1921435025, 0.5573161745), (-0.3231557362, 0.2138514947), (-0.1567347615, 0.0261850592)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.1567347615, 0.0261850592), (-0.0363452582, -0.1048271745), (0.211515929, -0.1543997361), (0.2398435701, -0.3279023509)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.2398435701, -0.3279023509), (0.2575479406, -0.4447513043), (0.1052902462, -0.7386439628), (-0.2027656926, -0.8059203546)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.2027656926, -0.8059203546), (-0.2169289729, -0.8094614449), (-0.5426898224, -0.890901117), (-0.5993434839, -0.6182539192)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 6.9058716567, perimeter: 20.7276435962
            with BuildLine():
                _nurbs_edge([(4.198541464, -0.4376707448), (4.1135607017, -0.2287583083), (3.9294348162, -0.1650224664), (3.8515351537, -0.1366953656)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.8515351537, -0.1366953656), (4.1171007113, -0.0446324228), (4.6588540166, 0.1465745626), (5.11208655, 0.7308187893)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.11208655, 0.7308187893), (5.3068346256, 0.9857616166), (5.5015827012, 1.378798858), (5.3457844568, 1.6620687861)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.3457844568, 1.6620687861), (5.2041494927, 1.9240935236), (4.8111122514, 2.0055334659), (4.5136790429, 1.9807474552)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.5136790429, 1.9807474552), (4.2410313049, 1.9595022646), (3.7346867406, 1.8568168617), (3.1044115828, 1.5168927318)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.1044115828, 1.5168927318), (2.8777958564, 1.3929621382), (2.7680285431, 1.3079813759), (2.7609463627, 1.2938175553)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.7609463627, 1.2938175553), (2.7538641822, 1.283194825), (2.7007510707, 1.1628053216), (2.6795066906, 0.9255668649)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.6795066906, 0.9255668649), (2.6724245101, 0.8299633722), (2.6759656003, 0.7308187893), (2.6901288806, 0.6316742064)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.6901288806, 0.6316742064), (3.3593538697, 1.0494974585), (3.9011082556, 1.2867359152), (4.198541464, 1.2584088143)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.198541464, 1.2584088143), (4.3507986182, 1.244245534), (4.3614218888, 1.0884467494), (4.3614218888, 1.0813651093)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.3614218888, 1.0813651093), (4.3791262593, 0.7945540909), (4.0993974214, 0.5360707137), (3.8550773245, 0.3873535692)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.8550773245, 0.3873535692), (3.4443357126, 0.1394923821), (2.9486133384, 0.0545116198), (2.4741364249, -0.0304696828)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.4741364249, -0.0304696828), (2.3537469216, -0.2216766682), (2.1908664968, -0.455374575), (2.2546017984, -0.6713681113)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.2546017984, -0.6713681113), (2.5343306363, -0.6395004605), (2.8317638447, -0.5722235284), (3.0973294023, -0.6642864712)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.0973294023, -0.6642864712), (3.1079515924, -0.6678275614), (3.3522727699, -0.7386450434), (3.3133229386, -0.9758835002)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.3133229386, -0.9758835002), (3.2779141976, -1.184794856), (2.976939899, -1.6132408385), (2.424563323, -1.7265487016)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.424563323, -1.7265487016), (2.1944065064, -1.7761207229), (1.8863500273, -1.7796618132), (1.730551783, -1.6061591983)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.730551783, -1.6061591983), (1.6632753912, -1.5318006261), (1.6278666502, -1.4291154932), (1.6101622797, -1.3299709103)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6101622797, -1.3299709103), (1.475609496, -1.3653796513), (1.2348294088, -1.4928513351), (1.001131502, -1.7690390828)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.001131502, -1.7690390828), (0.9621816707, -1.8150705542), (0.9090685592, -1.8646425755), (0.905527469, -1.9283784174)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.905527469, -1.9283784174), (0.8878230985, -2.3674465898), (1.4720673252, -2.4524278925), (1.6384888402, -2.470132263)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6384888402, -2.470132263), (2.1058846539, -2.5197042843), (3.2743731074, -2.434723522), (3.961302467, -1.4078700325)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.961302467, -1.4078700325), (4.1454283525, -1.1316817445), (4.3295531574, -0.7421855933), (4.198541464, -0.4376707448)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 7.2186180728, perimeter: 20.7733838501
            with BuildLine():
                _nurbs_edge([(6.9604211021, 1.2230000733), (7.2153655502, 1.2548677241), (7.6898435443, 1.2867359152), (8.3732318136, 1.2407044438)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(8.3732318136, 1.2407044438), (8.4865402171, 1.4496157997), (8.5750620697, 1.6726909762), (8.6387973713, 1.8993069727)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(8.6387973713, 1.8993069727), (8.0333076838, 1.9453384441), (7.4278179963, 1.9347157137), (6.8223293894, 1.8922253325)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.8223293894, 1.8922253325), (6.7585940878, 1.8886845125), (6.5992547532, 1.909929703), (6.4859463497, 1.7789174693)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.4859463497, 1.7789174693), (6.4363743284, 1.7258043578), (5.9831417951, 1.1628053216), (5.2183138536, 0.0297256091)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.2183138536, 0.0297256091), (5.1120876306, -0.1296137254), (5.0058614075, -0.28895306), (4.9067173649, -0.4518334848)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.9067173649, -0.4518334848), (4.9279628256, -0.5863868087), (5.0589745191, -0.7032357621), (5.189987293, -0.7457261433)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.189987293, -0.7457261433), (5.5086659622, -0.5970095391), (5.8592122821, -0.4447518446), (6.2097586021, -0.4766194954)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.2097586021, -0.4766194954), (6.2274629726, -0.4766194954), (6.5992547532, -0.5049465963), (6.5744682023, -0.8236252654)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.5744682023, -0.8236252654), (6.5638460122, -0.9758829599), (6.4328332382, -1.2768572585), (6.1106134789, -1.5211773554)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.1106134789, -1.5211773554), (5.6219732851, -1.8894280458), (5.1970683929, -1.7442525319), (5.1651996615, -1.7336298015)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.1651996615, -1.7336298015), (4.8748475529, -1.6486490392), (4.8252755316, -1.4149511324), (4.8217344414, -1.3972467618)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.8217344414, -1.3972467618), (4.7969478905, -1.3264292798), (4.7827846102, -1.2520707076), (4.7686213299, -1.1812532255)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.7686213299, -1.1812532255), (4.5278423232, -1.3795423913), (4.3047666065, -1.6096992079), (4.1383461721, -1.8717236753)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.1383461721, -1.8717236753), (4.1312639916, -1.8858869556), (4.102937431, -1.9142140565), (4.1135596211, -1.9531638877)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.1135596211, -1.9531638877), (4.1489683621, -2.133748683), (4.3260120672, -2.278924197), (4.4959735918, -2.349741679)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.4959735918, -2.349741679), (4.8819286528, -2.5090810136), (5.8556690307, -2.5657352154), (6.7196420954, -1.8858869556)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.7196420954, -1.8858869556), (7.1233015268, -1.5672082865), (7.4490623764, -1.1175173836), (7.6190239011, -0.6324177398)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(7.6190239011, -0.6324177398), (7.6650548322, -0.4943238659), (7.7996086964, -0.0623367933), (7.477388937, 0.1465745626)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(7.477388937, 0.1465745626), (7.275558681, 0.2775867963), (6.7550508364, 0.3767313792), (6.1672655194, 0.1465745626)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.1672655194, 0.1465745626), (6.4115856163, 0.5183663432), (6.6771511739, 0.8795353935), (6.9604211021, 1.2230000733)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 14.5487005046, perimeter: 91.4376520109
            with BuildLine():
                Line((7.9483269215, -2.7994331222), (9.5381802575, 1.6620685159))
                _nurbs_edge([(9.5381802575, 1.6620685159), (9.7612548937, 2.2852623038), (9.2974012509, 2.9403240126), (8.6387984518, 2.9403240126)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((8.6387984518, 2.9403240126), (-6.9799982367, 2.9403240126))
                _nurbs_edge([(-6.9799982367, 2.9403240126), (-7.3836579383, 2.9403240126), (-7.7448269886, 2.6853811853), (-7.879380245, 2.3065074944)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-7.879380245, 2.3065074944), (-9.4692327706, -2.1549936035))
                _nurbs_edge([(-9.4692327706, -2.1549936035), (-9.6923078795, -2.7781876615), (-9.2319942126, -3.4332493702), (-8.5698507623, -3.4332493702)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-8.5698507623, -3.4332493702), (7.0489451158, -3.4332493702))
                _nurbs_edge([(7.0489451158, -3.4332493702), (7.4526045472, -3.4332493702), (7.8137741378, -3.1783060027), (7.9483269215, -2.7994331222)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(7.0489451158, -3.1145707011), (7.3180517636, -3.1145707011), (7.5588307703, -2.9446086362), (7.650893713, -2.6896658089)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-8.5698507623, -3.1145707011), (7.0489451158, -3.1145707011))
                _nurbs_edge([(-9.1717993596, -2.2647609167), (-9.3205160651, -2.6790430786), (-9.012460025, -3.1145707011), (-8.5698507623, -3.1145707011)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-7.581946834, 2.1967404512), (-9.1717993596, -2.2647609167))
                _nurbs_edge([(-6.9799982367, 2.6216453434), (-7.2491046144, 2.6216453434), (-7.4898841614, 2.4516832785), (-7.581946834, 2.1967404512)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((8.6387973713, 2.6216453434), (-6.9799982367, 2.6216453434))
                _nurbs_edge([(9.2407459685, 1.7718355591), (9.389463113, 2.1861177209), (9.081406634, 2.6216453434), (8.6387973713, 2.6216453434)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((7.650893713, -2.6896658089), (9.2407459685, 1.7718355591))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.3167177205, perimeter: 25.1722732042
            with BuildLine():
                _nurbs_edge([(-6.3532633586, -2.0664717509), (-5.8858680853, -0.7634305138), (-5.3653597004, 0.5325296235), (-4.7138388117, 1.7576720086)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.7138388117, 1.7576720086), (-4.8590145958, 1.8532755013), (-5.0537626714, 1.8603574116), (-5.2272655564, 1.8603574116)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.2272655564, 1.8603574116), (-5.7548558516, 1.2584088143), (-6.2293327651, 0.6139698359), (-6.6719421629, -0.0517146032)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.6719421629, -0.0517146032), (-6.5869612655, 0.5643972743), (-6.470112312, 1.1769686019), (-6.3497225386, 1.7859991095)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.3497225386, 1.7859991095), (-6.5550933445, 1.8674393219), (-6.7958726213, 1.839112221), (-7.0154068426, 1.8072443001)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.0154068426, 1.8072443001), (-7.7873173698, -0.1119093549), (-8.2759579688, -1.4539009636), (-8.49195137, -2.208106715)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.49195137, -2.208106715), (-8.516737482, -2.2966285675), (-8.5415235939, -2.3886915103), (-8.5698505935, -2.4772133628)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.5698505935, -2.4772133628), (-8.3042850696, -2.480754453), (-8.1237004094, -2.3993142406), (-8.0351785569, -2.3532827693)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-8.0351785569, -2.3532827693), (-7.7696129993, -1.475145884), (-7.4969656664, -0.5970089988), (-7.1180921105, 0.2350964151)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.1180921105, 0.2350964151), (-7.2136957383, -0.3420661715), (-7.3376263319, -0.9192287581), (-7.3553307024, -1.5034729849)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.3553307024, -1.5034729849), (-7.3588715224, -1.6274035784), (-7.3765758929, -1.7654974523), (-7.3270037366, -1.7584158121)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.3270037366, -1.7584158121), (-7.270349805, -1.751334172), (-7.2243183336, -1.6380263088), (-7.1499600315, -1.510554625)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-7.1499600315, -1.510554625), (-6.7887908461, -0.887360567), (-6.4028356501, -0.2783303296), (-5.9602263874, 0.2882095266)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.9602263874, 0.2882095266), (-6.3036910672, -0.5261915167), (-6.6188289163, -1.3547558404), (-6.8596084632, -2.2045656248)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-6.8596084632, -2.2045656248), (-6.6861055782, -2.1797796141), (-6.5126026932, -2.1408297829), (-6.3532633586, -2.0664717509)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 4.529562844, perimeter: 16.7929365652
            with BuildLine():
                _nurbs_edge([(-3.2089670484, 1.8249489407), (-3.2408352395, 1.8355714009), (-3.2762439805, 1.8355714009), (-3.3116527215, 1.8355714009)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.3116527215, 1.8355714009), (-3.3116527215, 1.8674393219), (-3.3081116313, 1.9028480629), (-3.3151938117, 1.9347159838)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.3151938117, 1.9347159838), (-3.8144572762, 1.8886845125), (-4.1083493944, 1.6089556746), (-4.2499843584, 1.4779434409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.2499843584, 1.4779434409), (-4.5615813874, 1.1946735127), (-5.0785489522, 0.5643978146), (-5.4467999128, -0.4872416855)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.4467999128, -0.4872416855), (-5.6698750893, -1.1210579336), (-5.7194471106, -1.6415668587), (-5.6061392474, -1.8717236753)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.6061392474, -1.8717236753), (-5.4786678338, -2.1302075928), (-5.1989387257, -2.0523084706), (-5.1847751753, -2.0487673804)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.1847751753, -2.0487673804), (-4.788197384, -1.9885726287), (-4.4588959844, -1.6663528694), (-4.1933301567, -1.3618380208)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.1933301567, -1.3618380208), (-3.7790479949, -0.8873611073), (-3.439123865, -0.3385256216), (-3.1664766672, 0.2315553249)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.1664766672, 0.2315553249), (-2.8938294695, 0.791013541), (-2.7840621562, 1.244245534), (-2.8300936276, 1.4744023506)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.8300936276, 1.4744023506), (-2.8336347178, 1.4921067211), (-2.8832067391, 1.7859993796), (-3.2089670484, 1.8249489407)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-3.7896707252, 0.0934609107), (-3.7967523654, 0.0686749001), (-3.810916186, 0.0438888894), (-3.8250794662, 0.0155617886)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.8250794662, 0.0155617886), (-4.1756257862, -0.696154122), (-4.5084682759, -1.1741721257), (-4.7704927433, -1.3264292798)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.7704927433, -1.3264292798), (-4.7775743834, -1.32997037), (-4.9616999988, -1.439737143), (-5.0289766608, -1.2910205388)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-5.0289766608, -1.2910205388), (-5.0997941428, -1.128140114), (-5.0112722903, -0.7740527039), (-4.8377694053, -0.3385256216)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-4.8377694053, -0.3385256216), (-4.5261723763, 0.4404666807), (-4.1260537649, 0.9114030443), (-3.8640292975, 1.0955283895)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.8640292975, 1.0955283895), (-3.810916186, 1.1344782208), (-3.6161681104, 1.2761131848), (-3.5099418873, 1.1380187707)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.5099418873, 1.1380187707), (-3.3860112938, 0.9822205263), (-3.5595139086, 0.5643972743), (-3.7896707252, 0.0934609107)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.2962891604, perimeter: 13.9782078832
            with BuildLine():
                _nurbs_edge([(-1.7465864767, 1.3115219259), (-1.3712536058, 1.4000437784), (-1.0915247679, 1.3575533972), (-0.9428081637, 1.3363079365)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.9428081637, 1.3363079365), (-0.8047142898, 1.4850245407), (-0.6878653364, 1.6514457856), (-0.5851796633, 1.8249486706)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.5851796633, 1.8249486706), (-0.7976321094, 1.8886845125), (-1.2189959114, 1.9276340736), (-1.7996995882, 1.8426530411)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.7996995882, 1.8426530411), (-1.9059258113, 1.8284894907), (-2.0121520343, 1.80370348), (-2.1148371671, 1.768294739)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.1148371671, 1.768294739), (-2.1998179294, 1.5770874835), (-2.2635537713, 1.3787983177), (-2.3662394445, 1.1982140627)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.3662394445, 1.1982140627), (-3.2904078011, -0.395179283), (-3.6338724809, -1.3122659995), (-3.6657401317, -1.404328402)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.6657401317, -1.404328402), (-3.7082305128, -1.5282589955), (-3.7400987039, -1.6557306793), (-3.7719663547, -1.7796612729)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-3.7719663547, -1.7796612729), (-3.3187343617, -1.6875983301), (-2.8655023686, -1.5990764776), (-2.4087298256, -1.5211773554)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.4087298256, -1.5211773554), (-2.3166668829, -1.32997037), (-2.2210633902, -1.1387628444), (-2.1608686385, -0.9369331286)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.1608686385, -0.9369331286), (-2.4405974764, -0.9510964089), (-2.7167857644, -0.9971278803), (-2.9929740524, -1.0396182615)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.9929740524, -1.0396182615), (-2.8832067391, -0.7705116136), (-2.7521945054, -0.5120282365), (-2.6211822717, -0.253544319)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.6211822717, -0.253544319), (-2.3662394445, -0.2075128476), (-2.1112966172, -0.1756451968), (-1.8528126997, -0.1721041066)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.8528126997, -0.1721041066), (-1.721800466, -0.0056831319), (-1.6084926028, 0.1749016634), (-1.5022663798, 0.3590270086)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.5022663798, 0.3590270086), (-1.6474424341, 0.3979768399), (-1.9236301818, 0.3731902889), (-2.3131263329, 0.3306999078)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.3131263329, 0.3306999078), (-2.1360826279, 0.6635418572), (-1.9519572826, 0.9928432567), (-1.7465864767, 1.3115219259)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 0.5080779611, perimeter: 3.5835362472
            with BuildLine():
                _nurbs_edge([(-0.3798083171, 1.2867359152), (-0.3408595664, 1.2761131848), (-0.298368645, 1.283194825), (-0.262959904, 1.2867359152)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.262959904, 1.2867359152), (-0.3514817565, 1.1238554904), (-0.5037394509, 1.0034659871), (-0.6489149649, 0.8866170337)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.6489149649, 0.8866170337), (-0.620587864, 0.791013541), (-0.4789529, 0.897239764), (-0.4470852492, 0.9149441345)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.4470852492, 0.9149441345), (-0.1744380514, 1.0778245593), (0.0734231357, 1.3044402857), (0.254007931, 1.5664647531)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.254007931, 1.5664647531), (0.2610901114, 1.5770874835), (0.5124913082, 1.9382565338), (0.254007931, 1.9807469149)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.254007931, 1.9807469149), (0.1052913268, 2.0055329256), (-0.2877459146, 1.913470253), (-0.4541668893, 1.5487603826)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.4541668893, 1.5487603826), (-0.4577079795, 1.5416787425), (-0.549770382, 1.3150624758), (-0.3798083171, 1.2867359152)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 3.0491035806, perimeter: 13.3417979929
            with BuildLine():
                _nurbs_edge([(-0.5993434839, -0.6182539192), (-0.6170473141, -0.5757640783), (-0.6205884043, -0.5403553373), (-0.6205884043, -0.5014055061)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.6205884043, -0.5014055061), (-0.9463487136, -0.8554929162), (-1.063197667, -1.0891908231), (-1.0667387572, -1.1139768337)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.0667387572, -1.1139768337), (-1.0915247679, -1.259152888), (-0.9038583325, -1.3158065494), (-0.847204671, -1.3228881896)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.847204671, -1.3228881896), (-0.6489155052, -1.3547558404), (-0.2381744336, -1.3122654592), (0.2079759193, -1.0254549812)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.2079759193, -1.0254549812), (0.5018680375, -0.8377885457), (0.7568114051, -0.5580597078), (0.8949052789, -0.2393810387)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.8949052789, -0.2393810387), (0.9019874593, -0.2252177584), (1.0223769627, 0.0084801484), (0.8134656068, 0.2067693142)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.8134656068, 0.2067693142), (0.7001572033, 0.3129955373), (0.508950218, 0.3661086488), (0.4629192869, 0.514825253)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.4629192869, 0.514825253), (0.4062650851, 0.6918689581), (0.5585233198, 0.8936986738), (0.685993923, 1.0317930879)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.685993923, 1.0317930879), (0.9409372906, 1.3044402857), (1.2312883186, 1.4071259588), (1.3693821924, 1.3858804981)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.3693821924, 1.3858804981), (1.3870865629, 1.3823394079), (1.4401996744, 1.3610944875), (1.433117494, 1.3186041063)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.433117494, 1.3186041063), (1.4295764038, 1.2973586456), (1.3127279907, 1.1132333003), (1.0223758821, 0.8264228223)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.0223758821, 0.8264228223), (1.2560737889, 0.8441271928), (1.5180982563, 0.8901586642), (1.6916008712, 1.0494979987)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6916008712, 1.0494979987), (2.0633926518, 1.3858810384), (2.1660777847, 1.6549874161), (2.1731599651, 1.6797736969)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.1731599651, 1.6797736969), (2.2262730766, 1.9063896934), (1.9075944075, 1.9170121536), (1.8969722174, 1.9170121536)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.8969722174, 1.9170121536), (1.4826895153, 1.963043625), (0.5054091277, 1.7116413477), (-0.0611312688, 0.7733097108)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.0611312688, 0.7733097108), (-0.1921435025, 0.5573161745), (-0.3231557362, 0.2138514947), (-0.1567347615, 0.0261850592)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.1567347615, 0.0261850592), (-0.0363452582, -0.1048271745), (0.211515929, -0.1543997361), (0.2398435701, -0.3279023509)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.2398435701, -0.3279023509), (0.2575479406, -0.4447513043), (0.1052902462, -0.7386439628), (-0.2027656926, -0.8059203546)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-0.2027656926, -0.8059203546), (-0.2169289729, -0.8094614449), (-0.5426898224, -0.890901117), (-0.5993434839, -0.6182539192)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 6.9058716567, perimeter: 20.7276435962
            with BuildLine():
                _nurbs_edge([(4.198541464, -0.4376707448), (4.1135607017, -0.2287583083), (3.9294348162, -0.1650224664), (3.8515351537, -0.1366953656)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.8515351537, -0.1366953656), (4.1171007113, -0.0446324228), (4.6588540166, 0.1465745626), (5.11208655, 0.7308187893)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.11208655, 0.7308187893), (5.3068346256, 0.9857616166), (5.5015827012, 1.378798858), (5.3457844568, 1.6620687861)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.3457844568, 1.6620687861), (5.2041494927, 1.9240935236), (4.8111122514, 2.0055334659), (4.5136790429, 1.9807474552)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.5136790429, 1.9807474552), (4.2410313049, 1.9595022646), (3.7346867406, 1.8568168617), (3.1044115828, 1.5168927318)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.1044115828, 1.5168927318), (2.8777958564, 1.3929621382), (2.7680285431, 1.3079813759), (2.7609463627, 1.2938175553)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.7609463627, 1.2938175553), (2.7538641822, 1.283194825), (2.7007510707, 1.1628053216), (2.6795066906, 0.9255668649)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.6795066906, 0.9255668649), (2.6724245101, 0.8299633722), (2.6759656003, 0.7308187893), (2.6901288806, 0.6316742064)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.6901288806, 0.6316742064), (3.3593538697, 1.0494974585), (3.9011082556, 1.2867359152), (4.198541464, 1.2584088143)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.198541464, 1.2584088143), (4.3507986182, 1.244245534), (4.3614218888, 1.0884467494), (4.3614218888, 1.0813651093)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.3614218888, 1.0813651093), (4.3791262593, 0.7945540909), (4.0993974214, 0.5360707137), (3.8550773245, 0.3873535692)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.8550773245, 0.3873535692), (3.4443357126, 0.1394923821), (2.9486133384, 0.0545116198), (2.4741364249, -0.0304696828)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.4741364249, -0.0304696828), (2.3537469216, -0.2216766682), (2.1908664968, -0.455374575), (2.2546017984, -0.6713681113)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.2546017984, -0.6713681113), (2.5343306363, -0.6395004605), (2.8317638447, -0.5722235284), (3.0973294023, -0.6642864712)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.0973294023, -0.6642864712), (3.1079515924, -0.6678275614), (3.3522727699, -0.7386450434), (3.3133229386, -0.9758835002)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.3133229386, -0.9758835002), (3.2779141976, -1.184794856), (2.976939899, -1.6132408385), (2.424563323, -1.7265487016)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.424563323, -1.7265487016), (2.1944065064, -1.7761207229), (1.8863500273, -1.7796618132), (1.730551783, -1.6061591983)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.730551783, -1.6061591983), (1.6632753912, -1.5318006261), (1.6278666502, -1.4291154932), (1.6101622797, -1.3299709103)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6101622797, -1.3299709103), (1.475609496, -1.3653796513), (1.2348294088, -1.4928513351), (1.001131502, -1.7690390828)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.001131502, -1.7690390828), (0.9621816707, -1.8150705542), (0.9090685592, -1.8646425755), (0.905527469, -1.9283784174)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.905527469, -1.9283784174), (0.8878230985, -2.3674465898), (1.4720673252, -2.4524278925), (1.6384888402, -2.470132263)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6384888402, -2.470132263), (2.1058846539, -2.5197042843), (3.2743731074, -2.434723522), (3.961302467, -1.4078700325)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.961302467, -1.4078700325), (4.1454283525, -1.1316817445), (4.3295531574, -0.7421855933), (4.198541464, -0.4376707448)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 7.2186180728, perimeter: 20.7733838501
            with BuildLine():
                _nurbs_edge([(6.9604211021, 1.2230000733), (7.2153655502, 1.2548677241), (7.6898435443, 1.2867359152), (8.3732318136, 1.2407044438)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(8.3732318136, 1.2407044438), (8.4865402171, 1.4496157997), (8.5750620697, 1.6726909762), (8.6387973713, 1.8993069727)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(8.6387973713, 1.8993069727), (8.0333076838, 1.9453384441), (7.4278179963, 1.9347157137), (6.8223293894, 1.8922253325)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.8223293894, 1.8922253325), (6.7585940878, 1.8886845125), (6.5992547532, 1.909929703), (6.4859463497, 1.7789174693)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.4859463497, 1.7789174693), (6.4363743284, 1.7258043578), (5.9831417951, 1.1628053216), (5.2183138536, 0.0297256091)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.2183138536, 0.0297256091), (5.1120876306, -0.1296137254), (5.0058614075, -0.28895306), (4.9067173649, -0.4518334848)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.9067173649, -0.4518334848), (4.9279628256, -0.5863868087), (5.0589745191, -0.7032357621), (5.189987293, -0.7457261433)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.189987293, -0.7457261433), (5.5086659622, -0.5970095391), (5.8592122821, -0.4447518446), (6.2097586021, -0.4766194954)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.2097586021, -0.4766194954), (6.2274629726, -0.4766194954), (6.5992547532, -0.5049465963), (6.5744682023, -0.8236252654)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.5744682023, -0.8236252654), (6.5638460122, -0.9758829599), (6.4328332382, -1.2768572585), (6.1106134789, -1.5211773554)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.1106134789, -1.5211773554), (5.6219732851, -1.8894280458), (5.1970683929, -1.7442525319), (5.1651996615, -1.7336298015)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.1651996615, -1.7336298015), (4.8748475529, -1.6486490392), (4.8252755316, -1.4149511324), (4.8217344414, -1.3972467618)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.8217344414, -1.3972467618), (4.7969478905, -1.3264292798), (4.7827846102, -1.2520707076), (4.7686213299, -1.1812532255)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.7686213299, -1.1812532255), (4.5278423232, -1.3795423913), (4.3047666065, -1.6096992079), (4.1383461721, -1.8717236753)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.1383461721, -1.8717236753), (4.1312639916, -1.8858869556), (4.102937431, -1.9142140565), (4.1135596211, -1.9531638877)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.1135596211, -1.9531638877), (4.1489683621, -2.133748683), (4.3260120672, -2.278924197), (4.4959735918, -2.349741679)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.4959735918, -2.349741679), (4.8819286528, -2.5090810136), (5.8556690307, -2.5657352154), (6.7196420954, -1.8858869556)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.7196420954, -1.8858869556), (7.1233015268, -1.5672082865), (7.4490623764, -1.1175173836), (7.6190239011, -0.6324177398)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(7.6190239011, -0.6324177398), (7.6650548322, -0.4943238659), (7.7996086964, -0.0623367933), (7.477388937, 0.1465745626)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(7.477388937, 0.1465745626), (7.275558681, 0.2775867963), (6.7550508364, 0.3767313792), (6.1672655194, 0.1465745626)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.1672655194, 0.1465745626), (6.4115856163, 0.5183663432), (6.6771511739, 0.8795353935), (6.9604211021, 1.2230000733)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875, mode=Mode.ADD)
    return part.part


# Description: This is a wedge or tapered block with a rectangular base that slopes upward, featuring a curved or contoured top surface with multiple triangulated facets and what appears to be an internal cavity or hollow section on the underside.
def model_146135_0ca63e9c_0003():
    """Model: Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.975625, perimeter: 6.9
            with BuildLine():
                Line((-0.8625, 0.8625), (0.8625, 0.8625))
                Line((-0.8625, -0.8625), (-0.8625, 0.8625))
                Line((0.8625, -0.8625), (-0.8625, -0.8625))
                Line((0.8625, 0.8625), (0.8625, -0.8625))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is an oval/elliptical boat hull or watercraft shell featuring a streamlined design with a curved bottom, internal ribbed reinforcement structure along the sides, and a tapered pointed bow, designed for hydrodynamic performance.
def model_146580_daeba71e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.9022104447, perimeter: 16.9646003294
            with BuildLine():
                CenterArc((0, 0), 2.7, 91.1013069522, 357.7931097844)
                CenterArc((0, 0), 2.7, 88.8944167366, 2.2068902156)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0066966081, perimeter: 0.3481857425
            with BuildLine():
                Line((-0.0149999997, 2.7999999381), (-0.0518946718, 2.6995012397))
                CenterArc((0, 0), 2.7, 88.8944167366, 2.2068902156)
                Line((0.051910574, 2.6999052106), (0.0520961508, 2.699497359))
                Line((0.0149999997, 2.7999999381), (0.051910574, 2.6999052106))
                Line((-0.0149999997, 2.7999999381), (0.0149999997, 2.7999999381))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a hex bolt or machine screw featuring a long cylindrical shaft with a hexagonal head at one end, designed for fastening applications.
def model_146769_3c88fc97_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6696758629, perimeter: 5.0348979419
            with BuildLine():
                Line((-0.0407356736, 0.5759113979), (-0.5191217377, 0.2526775708))
                Line((-0.5191217377, 0.2526775708), (-0.4783860641, -0.3232338271))
                Line((-0.4783860641, -0.3232338271), (0.0407356736, -0.5759113979))
                Line((0.0407356736, -0.5759113979), (0.5191217377, -0.2526775708))
                Line((0.5191217377, -0.2526775708), (0.4783860641, 0.3232338271))
                Line((0.4783860641, 0.3232338271), (-0.0407356736, 0.5759113979))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


# Description: This is a dark metal angled bracket or mounting arm featuring a rectangular upper section, a long tapered shaft, and a hexagonal base connector, designed for structural support or component mounting applications.
def model_146857_25b972d7_0007():
    """Model: Forks v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 112.4439870851, perimeter: 68.7928481097
            with BuildLine():
                Line((2.5, 3), (4, 4.2586494468))
                Line((2.5, 0), (2.5, 3))
                Line((6, 0), (2.5, 0))
                Line((6, 16), (6, 0))
                Line((4.5, 28), (6, 16))
                Line((0, 28), (4.5, 28))
                Line((0, 13), (0, 28))
                Line((4, 13), (0, 13))
                Line((4, 4.2586494468), (4, 13))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a truss or structural framework component with a parallelogram/rhomboidal overall shape, featuring a hollow interior with diagonal cross-bracing, perimeter flanges, and internal triangulated support members for lightweight rigidity.
def model_147134_273aac81_0002():
    """Model: Основа"""
    with BuildPart() as part:
        # Основа -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 89.8088188471, perimeter: 66.0499503056
            with BuildLine():
                Line((4.9968414101, -4.9968414101), (4.9968414101, 4.9968414101))
                Line((-4.9968414101, 4.9968414101), (4.9968414101, 4.9968414101))
                Line((-4.9968414101, -4.9968414101), (-4.9968414101, 4.9968414101))
                Line((4.9968414101, -4.9968414101), (-4.9968414101, -4.9968414101))
            make_face()
            with BuildLine():
                CenterArc((3.6187347112, -3.7283761045), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6187347112, 3.7220589247), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.6124175315, -3.7283761045), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.6124175315, 3.7220589247), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -1.25), 1.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 1.25), 1.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.3006357817, perimeter: 6.4402649399
            with Locations((0, -1.25)):
                Circle(1.025)
            # Profile area: 3.3006357817, perimeter: 6.4402649399
            with Locations((0, 1.25)):
                Circle(1.025)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Основа -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3006357817, perimeter: 6.4402649399
            with Locations((0, -1.25)):
                Circle(1.025)
            # Profile area: 3.3006357817, perimeter: 6.4402649399
            with Locations((0, 1.25)):
                Circle(1.025)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a drone frame assembly with a distinctive elongated diamond or X-shaped configuration, featuring four blue and black composite arms with integrated motor mounts, a central control board hub with antenna, and a rectangular landing gear skid at the base.
def model_147673_79b26fed_0000():
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
            # Profile area: 17928.3256946444, perimeter: 1435.8465884729
            with BuildLine():
                Line((241.6540093994, -416.4115594482), (241.6540093994, -416.4110426839))
                _nurbs_edge([(241.6540093994, -416.4110426839), (251.8293572998, -415.7366135661), (254.8562009684, -412.3621166992), (254.9247239176, -401.6673948161)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(254.9247239176, -401.6673948161), (255.1117926025, -372.4457417806), (255.1922269694, -343.7617561849), (253.4427988688, -313.4397052002)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(253.4427988688, -313.4397052002), (252.6524853516, -299.742479248), (250.592972819, -297.6242364502), (238.9486706543, -296.8130198161)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(238.9486706543, -296.8130198161), (207.5100857544, -294.622791748), (39.6864664714, -292.153433431), (22.7793201701, -298.0216282145)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(22.7793201701, -298.0216282145), (16.958221995, -300.0422542318), (16.8611203639, -305.8189042155), (16.4287904867, -311.4508085124)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(16.4287904867, -311.4508085124), (14.9778147761, -330.3510502116), (12.8299274699, -403.7427720133), (16.1102327347, -410.799214681)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(16.1102327347, -410.799214681), (18.0596825409, -414.9926021322), (22.2464489492, -416.0845251465), (26.7274318949, -416.3774271647)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(26.7274318949, -416.3774271647), (27.2396648407, -416.4110168457), (27.7516329447, -416.4433146159), (28.2638658905, -416.4763875326)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((28.2638658905, -416.4763875326), (32.5403264364, -427.9357655843))
                _nurbs_edge([(32.5403264364, -427.9357655843), (32.8983084615, -428.8946217855), (32.9591606903, -429.7965822347), (33.7494709778, -429.7965822347)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((33.7494709778, -429.7965822347), (33.7494709778, -430.7268613688))
                Line((33.7494709778, -430.7268613688), (33.0520296987, -430.7268613688))
                Line((33.0520296987, -430.7268613688), (33.0520296987, -432.0992582194))
                _nurbs_edge([(33.0520296987, -432.0992582194), (33.0520296987, -432.4310467529), (33.3269321696, -432.9599550374), (33.8650937653, -432.9599550374)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((33.8650937653, -432.9599550374), (54.4509980774, -432.9599550374))
                Line((54.4509980774, -432.9599550374), (47.3329118856, -447.4514477539))
                _nurbs_edge([(47.3329118856, -447.4514477539), (46.1613361104, -449.8369352214), (48.8061133067, -452.28831014), (51.4662319438, -452.28831014)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((51.4662319438, -452.28831014), (61.4251460266, -452.28831014))
                _nurbs_edge([(61.4251460266, -452.28831014), (64.0855327352, -452.28831014), (65.7756879679, -450.1038956706), (65.9804752096, -447.4514477539)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((65.9804752096, -447.4514477539), (67.1007233683, -432.9599550374))
                Line((67.1007233683, -432.9599550374), (198.7079098511, -432.9599550374))
                Line((198.7079098511, -432.9599550374), (199.8281515503, -447.4514477539))
                _nurbs_edge([(199.8281515503, -447.4514477539), (200.0332036336, -450.1038956706), (201.7233588664, -452.28831014), (204.3834807332, -452.28831014)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((204.3834807332, -452.28831014), (214.3423948161, -452.28831014))
                _nurbs_edge([(214.3423948161, -452.28831014), (217.0027750651, -452.28831014), (219.6475490316, -449.8369352214), (218.4757084147, -447.4514477539)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((218.4757084147, -447.4514477539), (211.3576286825, -432.9599550374))
                Line((211.3576286825, -432.9599550374), (235.8882114665, -432.9599550374))
                _nurbs_edge([(235.8882114665, -432.9599550374), (236.4340437826, -432.9599550374), (236.6806437174, -432.4593654378), (236.6806437174, -432.1225384521)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((236.6806437174, -432.1225384521), (236.6806437174, -430.727119751))
                Line((236.6806437174, -430.727119751), (235.983192749, -430.727119751))
                Line((235.983192749, -430.727119751), (235.983192749, -429.7968406169))
                _nurbs_edge([(235.983192749, -429.7968406169), (237.006334432, -429.7968406169), (237.2442010498, -428.9086260986), (237.5617010498, -427.9360239665)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((237.5617010498, -427.9360239665), (241.3142885335, -416.4337803141))
                Line((241.3142885335, -416.4337803141), (241.6540093994, -416.4115594482))
            make_face()
            with BuildLine():
                Line((37.449907252, -312.0612363688), (37.4496520996, -312.0612363688))
                _nurbs_edge([(37.4496520996, -312.0612363688), (90.4859109497, -309.6768082682), (142.2571953328, -309.8892759196), (192.935755717, -312.3424853516)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(192.935755717, -312.3424853516), (195.704088033, -312.4766373698), (197.968665568, -314.8996936035), (197.9739494832, -317.6682843018)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((197.9739494832, -317.6682843018), (198.1147031657, -394.8938031006))
                _nurbs_edge([(198.1147031657, -394.8938031006), (198.1197286987, -397.6637373861), (195.8461594645, -399.8777624512), (193.0754500326, -399.9330562337)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(193.0754500326, -399.9330562337), (167.4002859497, -400.4460740153), (142.4685906982, -400.5365594482), (117.1656907145, -400.4347052002)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(117.1656907145, -400.4347052002), (90.3123362732, -400.326494751), (65.3187391154, -400.4706978353), (36.6045615641, -399.5110406494)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(36.6045615641, -399.5110406494), (33.8354314931, -399.4186948649), (31.5348807017, -397.2432979329), (31.565308431, -394.4717875163)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((31.565308431, -394.4717875163), (32.4093299103, -317.387035319))
                _nurbs_edge([(32.4093299103, -317.387035319), (32.4397576396, -314.6152665202), (34.6810420227, -312.1858540853), (37.449907252, -312.0612363688)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((163.5730906169, -414.1554956055), (163.5730906169, -410.2168988037))
                Line((163.5730906169, -410.2168988037), (191.7062312826, -410.2168988037))
                Line((191.7062312826, -410.2168988037), (191.7062312826, -414.1554956055))
                Line((191.7062312826, -414.1554956055), (163.5730906169, -414.1554956055))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((69.69125, -414.1554956055), (69.69125, -410.2168988037))
                Line((69.69125, -410.2168988037), (97.8243971252, -410.2168988037))
                Line((97.8243971252, -410.2168988037), (97.8243971252, -414.1554956055))
                Line((97.8243971252, -414.1554956055), (69.69125, -414.1554956055))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4960.7547826854, perimeter: 391.589797591
            with BuildLine():
                Line((144.6357839966, -253.2787778727), (144.6357969157, -253.2787520345))
                Line((144.6357969157, -253.2787520345), (172.2704667155, -252.8218290202))
                Line((172.2704667155, -252.8218290202), (179.1684177653, -271.6183561198))
                Line((179.1684177653, -271.6183561198), (192.4933666992, -270.2771718343))
                Line((192.4933666992, -270.2771718343), (186.1804057821, -252.8218290202))
                Line((186.1804057821, -252.8218290202), (186.1804057821, -149.2800612386))
                _nurbs_edge([(186.1804057821, -149.2800612386), (186.1804057821, -141.5433758545), (179.8505079142, -135.2134909058), (172.1143651326, -135.2134909058)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((172.1143651326, -135.2134909058), (165.7357880656, -135.2134909058))
                Line((165.7357880656, -135.2134909058), (165.7357880656, -139.1520747884))
                Line((165.7357880656, -139.1520747884), (151.6692177327, -139.1520747884))
                Line((151.6692177327, -139.1520747884), (151.6692177327, -135.2134909058))
                Line((151.6692177327, -135.2134909058), (143.9806947835, -135.2134909058))
                Line((143.9806947835, -135.2134909058), (144.3082458496, -177.2012768555))
                Line((144.3082458496, -177.2012768555), (148.2468297323, -177.2012768555))
                Line((148.2468297323, -177.2012768555), (148.2468297323, -194.535451355))
                Line((148.2468297323, -194.535451355), (144.3709422811, -194.535451355))
                Line((144.3709422811, -194.535451355), (144.6357839966, -234.8037040202))
                Line((144.6357839966, -234.8037040202), (156.863771464, -234.8037040202))
                Line((156.863771464, -234.8037040202), (156.863771464, -238.7423008219))
                Line((156.863771464, -238.7423008219), (144.6357839966, -238.7423008219))
                Line((144.6357839966, -238.7423008219), (144.6357839966, -253.2787778727))
            make_face()
            # Profile area: 4960.7548924876, perimeter: 391.5897802799
            with BuildLine():
                Line((207.1615928141, -253.2787778727), (207.1616057332, -253.2787520345))
                Line((207.1616057332, -253.2787520345), (234.7962626139, -252.8218290202))
                Line((234.7962626139, -252.8218290202), (241.6942136637, -271.6183561198))
                Line((241.6942136637, -271.6183561198), (255.0191625977, -270.2771718343))
                Line((255.0191625977, -270.2771718343), (248.7062145996, -252.8218290202))
                Line((248.7062145996, -252.8218290202), (248.7062145996, -149.2800612386))
                _nurbs_edge([(248.7062145996, -149.2800612386), (248.7062145996, -141.5433758545), (242.3763167318, -135.2134909058), (234.6401739502, -135.2134909058)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((234.6401739502, -135.2134909058), (228.2615968831, -135.2134909058))
                Line((228.2615968831, -135.2134909058), (228.2615968831, -139.1520747884))
                Line((228.2615968831, -139.1520747884), (214.1950265503, -139.1520747884))
                Line((214.1950265503, -139.1520747884), (214.1950265503, -135.2134909058))
                Line((214.1950265503, -135.2134909058), (206.5065036011, -135.2134909058))
                Line((206.5065036011, -135.2134909058), (206.8340546672, -177.2012768555))
                Line((206.8340546672, -177.2012768555), (210.7726385498, -177.2012768555))
                Line((210.7726385498, -177.2012768555), (210.7726385498, -194.535451355))
                Line((210.7726385498, -194.535451355), (206.8967510986, -194.535451355))
                Line((206.8967510986, -194.535451355), (207.1615928141, -234.8037040202))
                Line((207.1615928141, -234.8037040202), (219.3895802816, -234.8037040202))
                Line((219.3895802816, -234.8037040202), (219.3895802816, -238.7423008219))
                Line((219.3895802816, -238.7423008219), (207.1615928141, -238.7423008219))
                Line((207.1615928141, -238.7423008219), (207.1615928141, -253.2787778727))
            make_face()
            # Profile area: 4397.4514705365, perimeter: 364.0719583333
            with BuildLine():
                Line((93.4256979167, -267.6794875), (87.3709729167, -267.6794875))
                Line((93.4256979167, -271.618075), (93.4256979167, -267.6794875))
                Line((110.7596104167, -271.618075), (93.4256979167, -271.618075))
                Line((110.7596104167, -267.6794875), (110.7596104167, -271.618075))
                Line((116.8143354167, -267.6794875), (110.7596104167, -267.6794875))
                Line((116.8143354167, -122.9640458333), (116.8143354167, -267.6794875))
                Line((110.7596104167, -122.9640458333), (116.8143354167, -122.9640458333))
                Line((110.7596104167, -119.0254583333), (110.7596104167, -122.9640458333))
                Line((93.4256979167, -119.0254583333), (110.7596104167, -119.0254583333))
                Line((93.4256979167, -122.9640458333), (93.4256979167, -119.0254583333))
                Line((87.3709729167, -122.9640458333), (93.4256979167, -122.9640458333))
                Line((87.3709729167, -267.6794875), (87.3709729167, -122.9640458333))
            make_face()
            # Profile area: 12102.6012753097, perimeter: 667.5505103129
            with BuildLine():
                Line((-0.0000004037, -182.2621824137), (0, -182.2621953328))
                Line((0, -182.2621953328), (0, -210.3953489176))
                Line((0, -210.3953489176), (3.9385875161, -210.3953489176))
                Line((3.9385875161, -210.3953489176), (3.9385875161, -258.1100333659))
                Line((3.9385875161, -258.1100333659), (46.1388342539, -258.1100333659))
                _nurbs_edge([(46.1388342539, -258.1100333659), (53.8749867249, -258.1100333659), (60.2048781331, -251.780135498), (60.2048781331, -244.0434501139)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((60.2048781331, -244.0434501139), (60.2048781331, -227.5914052327))
                Line((60.2048781331, -227.5914052327), (30.7615170542, -227.5914052327))
                Line((30.7615170542, -227.5914052327), (30.7615170542, -223.652808431))
                Line((30.7615170542, -223.652808431), (60.2048781331, -223.652808431))
                Line((60.2048781331, -223.652808431), (60.2048781331, -78.937365214))
                Line((60.2048781331, -78.937365214), (30.7615170542, -78.937365214))
                Line((30.7615170542, -78.937365214), (30.7615170542, -74.9987748718))
                Line((30.7615170542, -74.9987748718), (60.2048781331, -74.9987748718))
                Line((60.2048781331, -74.9987748718), (60.2048781331, -55.3833636475))
                _nurbs_edge([(60.2048781331, -55.3833636475), (60.2048781331, -47.6466814931), (53.8749867249, -41.3167900848), (46.1388342539, -41.3167900848)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((46.1388342539, -41.3167900848), (3.9385871124, -41.3167900848))
                Line((3.9385871124, -41.3167900848), (3.9385871124, -88.3803417969))
                Line((3.9385871124, -88.3803417969), (-0.0000004037, -88.3803417969))
                Line((-0.0000004037, -88.3803417969), (-0.0000004037, -116.5134824626))
                Line((-0.0000004037, -116.5134824626), (3.9385871124, -116.5134824626))
                Line((3.9385871124, -116.5134824626), (3.9385871124, -182.2621824137))
                Line((3.9385871124, -182.2621824137), (-0.0000004037, -182.2621824137))
            make_face()
            # Profile area: 4255.7098026165, perimeter: 430.835898641
            with BuildLine():
                Line((244.533213501, -104.7659953817), (244.533213501, -90.6994250488))
                Line((244.533213501, -90.6994250488), (240.5946166992, -90.6994250488))
                Line((240.5946166992, -90.6994250488), (240.5946166992, -83.0111604818))
                Line((240.5946166992, -83.0111604818), (95.8791734823, -83.0111604818))
                Line((95.8791734823, -83.0111604818), (95.8791734823, -90.6994250488))
                Line((95.8791734823, -90.6994250488), (91.9405831401, -90.6994250488))
                Line((91.9405831401, -90.6994250488), (91.9405831401, -104.7659953817))
                Line((91.9405831401, -104.7659953817), (95.8791734823, -104.7659953817))
                Line((95.8791734823, -104.7659953817), (95.8791734823, -112.4542599487))
                Line((95.8791734823, -112.4542599487), (240.5946166992, -112.4542599487))
                Line((240.5946166992, -112.4542599487), (240.5946166992, -104.7659953817))
                Line((240.5946166992, -104.7659953817), (244.533213501, -104.7659953817))
            make_face()
            with BuildLine():
                Line((182.9588582357, -95.7635539246), (153.5152290853, -95.7635539246))
                Line((182.9588582357, -99.7021442668), (182.9588582357, -95.7635539246))
                Line((153.5152290853, -99.7021442668), (182.9588582357, -99.7021442668))
                Line((153.5152290853, -95.7635539246), (153.5152290853, -99.7021442668))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1795.3388278138, perimeter: 411.4292434573
            with BuildLine():
                Line((144.8207339478, -75.3842875163), (174.264104716, -75.3842875163))
                Line((174.264104716, -75.3842875163), (174.264104716, -71.4456971741))
                Line((174.264104716, -71.4456971741), (180.6421520996, -71.4456971741))
                Line((180.6421520996, -71.4456971741), (180.6421520996, -56.531135966))
                _nurbs_edge([(180.6421520996, -56.531135966), (180.6421520996, -54.3176341248), (178.2373505656, -52.3157924906), (174.3585563151, -50.8751375326)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((174.3585563151, -50.8751375326), (194.1745302327, -31.0591700745))
                Line((194.1745302327, -31.0591700745), (193.3850177002, -30.2696543121))
                Line((193.3850177002, -30.2696543121), (213.6081760661, -10.0467559433))
                _nurbs_edge([(213.6081760661, -10.0467559433), (215.4859296672, -10.7994958496), (217.713196818, -10.4158500163), (219.2342667643, -8.8947598839)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(219.2342667643, -8.8947598839), (221.2691813151, -6.8598493703), (221.2691813151, -3.5607597224), (219.2342667643, -1.5258492088)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(219.2342667643, -1.5258492088), (217.1993522135, 0.5090613047), (213.9002641805, 0.5090613047), (211.8653625488, -1.5258492088)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(211.8653625488, -1.5258492088), (210.3442667643, -3.0469389375), (209.9603625488, -5.2739368057), (210.713365682, -7.1516847547)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((210.713365682, -7.1516847547), (190.4902073161, -27.3748471578))
                Line((190.4902073161, -27.3748471578), (189.7006947835, -26.5853297806))
                Line((189.7006947835, -26.5853297806), (167.165067749, -49.1209487406))
                _nurbs_edge([(167.165067749, -49.1209487406), (164.8007546997, -48.7756661987), (162.2305885824, -48.5862268575), (159.5424193319, -48.5862268575)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(159.5424193319, -48.5862268575), (155.6861172485, -48.5862268575), (152.0719063314, -48.9759575907), (148.9612047323, -49.6562003072)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((148.9612047323, -49.6562003072), (125.890067749, -26.5853281657))
                Line((125.890067749, -26.5853281657), (125.1005552165, -27.374843928))
                Line((125.1005552165, -27.374843928), (104.877390391, -7.1516807175))
                _nurbs_edge([(104.877390391, -7.1516807175), (105.6301286825, -5.2739327685), (105.2464828491, -3.0466704623), (103.7253935242, -1.5258451716)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(103.7253935242, -1.5258451716), (101.6904854329, 0.5090653419), (98.3913909403, 0.5090653419), (96.3564828491, -1.5258451716)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(96.3564828491, -1.5258451716), (94.3215747579, -3.5607556852), (94.3215747579, -6.8598453331), (96.3564828491, -8.8947558467)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(96.3564828491, -8.8947558467), (97.8775721741, -10.4158451716), (100.1048328654, -10.7997558467), (101.9825800069, -10.0467519061)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((101.9825800069, -10.0467519061), (122.2057448324, -30.2696510824))
                Line((122.2057448324, -30.2696510824), (121.4162322998, -31.0591668447))
                Line((121.4162322998, -31.0591668447), (142.3053448486, -51.9482858531))
                _nurbs_edge([(142.3053448486, -51.9482858531), (139.872495931, -53.2431551361), (138.4426865641, -54.8243086243), (138.4426865641, -56.531135966)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((138.4426865641, -56.531135966), (138.4426865641, -71.4456971741))
                Line((138.4426865641, -71.4456971741), (144.8207339478, -71.4456971741))
                Line((144.8207339478, -71.4456971741), (144.8207339478, -75.3842875163))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a cylindrical sleeve or tube with a smooth outer surface and visible vertical ridging or knurling pattern on its curved walls, featuring an open top and bottom.
def model_148051_c59af578_0004():
    """Model: BT-56 x 2 in"""
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
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a rectangular flat bar or plate with a simple, elongated shape featuring rounded ends and a uniform thickness throughout.
def model_148051_c59af578_0007():
    """Model: Dowel 1/8 in x 4.75 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=12.065
        extrude(amount=12.065)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a simple cylindrical or slightly tapered profile, featuring smoothly rounded ends and a uniform cross-section along its length.
def model_148051_c59af578_0012():
    """Model: Dowel 1/12 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0351880194, perimeter: 0.664970445
            Circle(0.1058333333)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a hollow cylindrical vessel with a domed or rounded top cap, featuring a uniform cylindrical body and a curved upper surface, commonly used as a container or pressure vessel component.
def model_20276_d041fa0f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2370217423, perimeter: 3.9426987803
            Circle(0.6275)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)
    return part.part


# Description: This is a hexagonal prism or bar stock with a beveled/chamfered top edge, featuring an elongated rectangular shape with angled surfaces on the upper end.
def model_20342_c140780b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1328425284, perimeter: 1.4589144659
            with BuildLine():
                Line((0.4293056418, 1.2161619426), (0.4293056418, 0.837852633))
                Line((0.4293056418, 0.837852633), (0.7804535651, 0.837852633))
                Line((0.7804535651, 0.837852633), (0.7804535651, 1.2161619426))
                Line((0.7804535651, 1.2161619426), (0.4293056418, 1.2161619426))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a curved composite bracket or mounting arm with an angular, bent V-shaped profile featuring two flat panel sections (one vertical and one horizontal) connected at a sharp angle, with reinforcing ribs or internal webbing visible through the semi-transparent blue material representation.
def model_20591_20e06209_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 121.1111124515, perimeter: 165.8702779834
            with BuildLine():
                CenterArc((-65.4902244258, 193.3358155586), 3.6289139962, -177.412793247, 81.6740518841)
                Line((-55.8334663006, 188.7181548549), (-65.8530887831, 189.7250890043))
                CenterArc((-55.4113679813, 194.9955380598), 6.2915583835, -93.8468420773, 55.8124874382)
                Line((-45.8823618426, 196.9656974882), (-50.4558757481, 191.1190959258))
                CenterArc((-41.5389679508, 193.7567353114), 5.4002322868, 97.4847461918, 46.0577293509)
                Line((-22.1019650411, 201.7570410554), (-42.2424142837, 199.11095533))
                Line((-22.2769035179, 203.0885699167), (-22.1019650411, 201.7570410554))
                Line((-42.5465336266, 200.4255121942), (-22.2769035179, 203.0885699167))
                CenterArc((-41.1093673045, 192.950445304), 7.6119689996, 100.8829655505, 39.9496489491)
                Line((-52.4673323202, 191.0601179444), (-47.0109583334, 197.7580741767))
                CenterArc((-55.3603204188, 195.1778154721), 5.0323764832, -96.6026621988, 41.6935503316)
                Line((-65.8223379776, 191.3228278632), (-55.9389597068, 190.178816608))
                CenterArc((-64.9757370118, 193.6684139747), 2.493693526, 179.5170908666, 70.6366899099)
                Line((-67.3511254556, 207.7151482112), (-67.4693419659, 193.6894314586))
                CenterArc((-79.3927451107, 208.2337299535), 12.0527810459, -2.4659636762, 21.7371122971)
                Line((-71.5737647717, 222.3893848411), (-68.0153143757, 212.2116189429))
                Line((-72.9096588738, 221.6496173694), (-71.5737647717, 222.3893848411))
                Line((-69.7945395737, 212.7398528782), (-72.9096588738, 221.6496173694))
                CenterArc((-84.3302192451, 207.8444199565), 15.3379023012, -0.4829091334, 19.0957831279)
                Line((-69.1154393746, 193.1720066255), (-68.9928617212, 207.7151482112))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


# Description: This is a dark blue and black molded plastic component with an elongated, curved streamlined shape featuring a central oval opening, ribbed reinforcement patterns on the upper surface, and tapered ends—appearing to be an aerodynamic fairing or ducting element.
def model_20951_2918f2fa_0000():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 76.1662708482, perimeter: 93.7263446882
            with BuildLine():
                CenterArc((-1.6916734857, 0.4914593323), 0.4914593323, -90, 44.4193194141)
                Line((-1.347699029, 0.1404410301), (-0.978147436, 0.5025768721))
                CenterArc((-3.2594507316, 2.8305962761), 3.2594507316, -45.5806805859, 45.5806805859)
                Line((0, 2.8305962761), (0, 7.5045465251))
                CenterArc((-2.6484182803, 7.5045465251), 2.6484182803, 0, 79.8728204957)
                Line((-2.1827370237, 10.1117021313), (-10.7230638003, 11.6371462193))
                CenterArc((-11.2185330031, 8.8632202963), 2.8178280213, 79.8728204957, 140.7624619933)
                Line((-7.5330410086, 0.2417832626), (-13.3568993357, 7.0281333269))
                CenterArc((-7.0069398677, 0.6932687417), 0.6932687417, -139.364717511, 49.364717511)
                Line((-1.6916734857, 0), (-7.0069398677, 0))
            make_face()
            with BuildLine():
                CenterArc((-11.2185330031, 8.8632202963), 2.18694, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-9.1888250366, 4.3445200153), (-9.1888250366, 4.9922200153))
                CenterArc((-9.3729750366, 4.3445200153), 0.18415, 180, 180)
                Line((-9.5571250366, 4.9922200153), (-9.5571250366, 4.3445200153))
                CenterArc((-9.3729750366, 4.9922200153), 0.18415, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5394345682, 8.0134847239), (-0.9974276304, 8.471477786))
                CenterArc((-0.669648282, 7.8832710101), 0.18415, -135, 180)
                Line((-1.2578550607, 8.2110503613), (-0.7998619957, 7.7530572963))
                CenterArc((-1.1276413442, 8.3412640723), 0.18415, 45, 179.9999987926)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.0841411733, 9.7381955016), (-4.7318411733, 9.7381955016))
                CenterArc((-4.0841411733, 9.5540455016), 0.18415, -90, 180)
                Line((-4.7318411733, 9.3698955016), (-4.0841411733, 9.3698955016))
                CenterArc((-4.7318411733, 9.5540455016), 0.18415, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.8015155488, 3.1307368545), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9190463116, 6.9561810776), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.7371273765, 8.6652168367), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.405884078, 4.3560503205), 2.9201254007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 15.0253158045, perimeter: 13.7409492757
            with Locations((-11.2185330031, 8.8632202963)):
                Circle(2.18694)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-0.9190463116, 6.9561810776)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-6.7371273765, 8.6652168367)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-8.8015155488, 3.1307368545)):
                Circle(0.635)
        # OneSide extrude, distance=0.0635
        extrude(amount=0.0635, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling with a rounded rectangular profile, featuring two circular end faces connected by curved side walls and internal geometric details suggesting mounting points or alignment features.
def model_21180_594c9e3e_0000():
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
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.2965878794, perimeter: 9.5755745265
            Circle(1.5240000188)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a elongated hexagonal or coffin-shaped container or enclosure with a tapered left end, featuring a recessed top surface with cross-bracing or internal ribbing, and angled side panels.
def model_21231_eb9826e5_0008():
    """Model: Box - Batteray Cover v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.72, perimeter: 4.0970562748
            with BuildLine():
                Line((0, -2.51), (1.2, -3.71))
                Line((0, -3.71), (0, -2.51))
                Line((1.2, -3.71), (0, -3.71))
            make_face()
            # Profile area: 0.72, perimeter: 4.0970562748
            with BuildLine():
                Line((14.2, -2.51), (14.2, -3.71))
                Line((13, -3.71), (14.2, -2.51))
                Line((14.2, -3.71), (13, -3.71))
            make_face()
            # Profile area: 51.242, perimeter: 34.4141125497
            with BuildLine():
                Line((14.2, 0), (14.2, -2.51))
                Line((0, 0), (14.2, 0))
                Line((0, -2.51), (0, 0))
                Line((0, -2.51), (1.2, -3.71))
                Line((13, -3.71), (1.2, -3.71))
                Line((13, -3.71), (14.2, -2.51))
            make_face()
        # OneSide extrude, distance=1.85
        extrude(amount=1.85)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.72, perimeter: 4.0970562748
            with BuildLine():
                Line((0, -2.51), (1.2, -3.71))
                Line((0, -3.71), (0, -2.51))
                Line((1.2, -3.71), (0, -3.71))
            make_face()
            # Profile area: 0.72, perimeter: 4.0970562748
            with BuildLine():
                Line((14.2, -2.51), (14.2, -3.71))
                Line((13, -3.71), (14.2, -2.51))
                Line((14.2, -3.71), (13, -3.71))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shell or bucket-like component with a curved body, angular top edges, and internal ribbing or reinforcement structures along its sides.
def model_21233_05d745b4_0015():
    """Model: Foot v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6683980934, perimeter: 11.9320789386
            with BuildLine():
                Line((-0.3, 0), (-0.3, -1.0000000149))
                CenterArc((1.0000000171, -1.0000000149), 1.3000000171, -180, 85.5915450502)
                CenterArc((1.0000000171, -2.300000032), 0.1, 2.2042274749, 175.5915450502)
                CenterArc((1.0000000171, -1.0000000149), 1.3000000171, -85.5915450502, 85.5915450502)
                Line((2.3000000343, 0), (2.3000000343, -1.0000000149))
                Line((2, 0), (2.3000000343, 0))
                Line((2, 0), (2, -1))
                CenterArc((1, -1), 1, 180, 180)
                Line((0, -1), (0, 0))
                Line((0, 0), (-0.3, 0))
            make_face()
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0, -1), (0, 0))
                Line((2, -1), (0, -1))
                Line((2, 0), (2, -1))
                Line((0, 0), (2, 0))
            make_face()
            # Profile area: 0.0154515151, perimeter: 0.5065144025
            with BuildLine():
                CenterArc((1.0000000171, -2.300000032), 0.1, 2.2042274749, 175.5915450502)
                CenterArc((1.0000000171, -1.0000000149), 1.3000000171, -94.4084549498, 8.8169098996)
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((2, -1), (0, -1))
                CenterArc((1, -1), 1, 180, 180)
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0154515151, perimeter: 0.5065144025
            with BuildLine():
                CenterArc((1.0000000171, -2.300000032), 0.1, 2.2042274749, 175.5915450502)
                CenterArc((1.0000000171, -1.0000000149), 1.3000000171, -94.4084549498, 8.8169098996)
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a triangular pyramid or tetrahedron-based connector piece featuring a pointed apex with flange-like extensions and internal geometric subdivisions, appearing to serve as a structural or mechanical junction component.
def model_21235_01764fc7_0027():
    """Model: 5-LEFT JAW v8 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 74.09259375, perimeter: 43.3153841816
            with BuildLine():
                Line((-5.08, 0), (5.08, 0))
                Line((5.08, 0), (5.08, 9.525))
                Line((5.08, 9.525), (-5.08, 9.525))
                Line((-0.3175, 4.7625), (-5.08, 9.525))
                Line((-5.08, 0), (-0.3175, 4.7625))
            make_face()
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)
    return part.part


# Description: This is an elliptical cylindrical bowl or container with a solid dark base and an open top featuring a mesh or perforated upper surface, designed as a strainer, basket, or ventilated enclosure.
def model_21246_c66f2b12_0031():
    """Model: Tire Back v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8141308887, perimeter: 10.5243353895
            Circle(1.675)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a window guide rail assembly featuring a trapezoidal frame with two cylindrical roller or pulley components mounted internally along the top edge, designed to guide and support window movement.
def model_21256_433456a3_0000():
    """Model: Bottom Frame v9"""
    with BuildPart() as part:
        # Sketch5 -> Extrude14 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 88 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 31.2
            with BuildLine():
                Line((15.375, -6.35), (15.375, -6.95))
                Line((15.375, -6.35), (14.675, -6.35))
                Line((8.675, -6.35), (14.675, -6.35))
                Line((8.675, -6.35), (7.675, -6.35))
                Line((4.275, -6.35), (7.675, -6.35))
                Line((4.275, -6.35), (3.375, -6.35))
                Line((0.375, -6.35), (3.375, -6.35))
                Line((0.375, -6.95), (0.375, -6.35))
                Line((15.375, -6.95), (0.375, -6.95))
            make_face()
            # Profile area: 8.89, perimeter: 26.8
            with BuildLine():
                Line((15.375, 6.35), (15.375, -6.35))
                Line((14.675, 6.35), (15.375, 6.35))
                Line((14.675, -6.35), (14.675, 6.35))
                Line((15.375, -6.35), (14.675, -6.35))
            make_face()
            # Profile area: 9, perimeter: 31.2
            with BuildLine():
                Line((0.375, 6.95), (0.375, 6.35))
                Line((0.375, 6.35), (3.375, 6.35))
                Line((3.375, 6.35), (4.275, 6.35))
                Line((4.275, 6.35), (7.675, 6.35))
                Line((7.675, 6.35), (8.675, 6.35))
                Line((8.675, 6.35), (14.675, 6.35))
                Line((14.675, 6.35), (15.375, 6.35))
                Line((15.375, 6.35), (15.375, 6.95))
                Line((15.375, 6.95), (0.375, 6.95))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch5 -> Extrude16 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 88 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0216803378, perimeter: 4.0168600567
            with BuildLine():
                Line((3.375, -1.7749597193), (3.375, -0.6694512863))
                Line((4.275, -1.7749597193), (3.375, -1.7749597193))
                Line((4.275, -0.6694512863), (4.275, -1.7749597193))
                CenterArc((3.825, -2.925), 2.3, 78.717175712, 22.5656485759)
            make_face()
            # Profile area: 0.2689192546, perimeter: 2.6547202996
            with BuildLine():
                Line((3.125, -1.7749597193), (3.125, -0.73410977))
                Line((3.375, -1.7749597193), (3.125, -1.7749597193))
                Line((3.375, -1.7749597193), (3.375, -0.6694512863))
                CenterArc((3.825, -2.925), 2.3, 101.282824288, 6.4361075854)
            make_face()
            # Profile area: 0.2689192546, perimeter: 2.6547202996
            with BuildLine():
                CenterArc((3.825, -2.925), 2.3, 72.2810681266, 6.4361075854)
                Line((4.275, -0.6694512863), (4.275, -1.7749597193))
                Line((4.525, -1.7749597193), (4.275, -1.7749597193))
                Line((4.525, -0.73410977), (4.525, -1.7749597193))
            make_face()
            # Profile area: 1.9865452703, perimeter: 6.1894118405
            with BuildLine():
                Line((1.5745833719, -2.45), (3.375, -2.45))
                Line((3.375, -2.45), (3.375, -1.7749597193))
                Line((3.375, -1.7749597193), (3.125, -1.7749597193))
                Line((3.125, -1.7749597193), (3.125, -0.73410977))
                CenterArc((3.825, -2.925), 2.3, 107.7189318734, 60.3624733957)
            make_face()
            # Profile area: 1.7418669285, perimeter: 5.5077193694
            with BuildLine():
                Line((3.375, -3.4), (3.375, -2.45))
                Line((1.5745833719, -2.45), (3.375, -2.45))
                CenterArc((3.825, -2.925), 2.3, 168.0814052691, 23.8371894617)
                Line((3.375, -3.4), (1.5745833719, -3.4))
            make_face()
            # Profile area: 1.6292165904, perimeter: 5.3669406181
            with BuildLine():
                Line((4.275, -3.4), (4.275, -5.1805487137))
                Line((4.275, -3.4), (3.375, -3.4))
                Line((3.375, -5.1805487137), (3.375, -3.4))
                CenterArc((3.825, -2.925), 2.3, -101.282824288, 22.5656485759)
            make_face()
            # Profile area: 1.9865452703, perimeter: 6.1894118405
            with BuildLine():
                Line((4.525, -0.73410977), (4.525, -1.7749597193))
                Line((4.525, -1.7749597193), (4.275, -1.7749597193))
                Line((4.275, -1.7749597193), (4.275, -2.45))
                Line((4.275, -2.45), (6.0754166281, -2.45))
                CenterArc((3.825, -2.925), 2.3, 11.9185947309, 60.3624733957)
            make_face()
            # Profile area: 1.7418669285, perimeter: 5.5077193694
            with BuildLine():
                CenterArc((3.825, -2.925), 2.3, -11.9185947309, 23.8371894617)
                Line((4.275, -2.45), (6.0754166281, -2.45))
                Line((4.275, -2.45), (4.275, -3.4))
                Line((6.0754166281, -3.4), (4.275, -3.4))
            make_face()
            # Profile area: 2.2554645249, perimeter: 6.2624322415
            with BuildLine():
                Line((3.375, -5.1805487137), (3.375, -3.4))
                Line((3.375, -3.4), (1.5745833719, -3.4))
                CenterArc((3.825, -2.925), 2.3, -168.0814052691, 66.7985809812)
            make_face()
            # Profile area: 2.2554645249, perimeter: 6.2624322415
            with BuildLine():
                Line((6.0754166281, -3.4), (4.275, -3.4))
                Line((4.275, -3.4), (4.275, -5.1805487137))
                CenterArc((3.825, -2.925), 2.3, -78.717175712, 66.7985809812)
            make_face()
            # Profile area: 2.2554645249, perimeter: 6.2624322415
            with BuildLine():
                Line((3.375, 3.4), (1.5745833719, 3.4))
                Line((3.375, 3.4), (3.375, 5.1805487137))
                CenterArc((3.825, 2.925), 2.3, 101.282824288, 66.7985809812)
            make_face()
            # Profile area: 1.9865452703, perimeter: 6.1894118405
            with BuildLine():
                Line((3.125, 0.73410977), (3.125, 1.7749597193))
                Line((3.125, 1.7749597193), (3.375, 1.7749597193))
                Line((3.375, 1.7749597193), (3.375, 2.45))
                Line((1.5745833719, 2.45), (3.375, 2.45))
                CenterArc((3.825, 2.925), 2.3, -168.0814052691, 60.3624733957)
            make_face()
            # Profile area: 1.0216803378, perimeter: 4.0168600567
            with BuildLine():
                Line((3.375, 1.7749597193), (4.275, 1.7749597193))
                Line((3.375, 0.6694512863), (3.375, 1.7749597193))
                CenterArc((3.825, 2.925), 2.3, -101.282824288, 22.5656485759)
                Line((4.275, 1.7749597193), (4.275, 0.6694512863))
            make_face()
            # Profile area: 0.2689192546, perimeter: 2.6547202996
            with BuildLine():
                CenterArc((3.825, 2.925), 2.3, -107.7189318734, 6.4361075854)
                Line((3.375, 0.6694512863), (3.375, 1.7749597193))
                Line((3.125, 1.7749597193), (3.375, 1.7749597193))
                Line((3.125, 0.73410977), (3.125, 1.7749597193))
            make_face()
            # Profile area: 0.2689192546, perimeter: 2.6547202996
            with BuildLine():
                Line((4.525, 1.7749597193), (4.525, 0.73410977))
                Line((4.275, 1.7749597193), (4.525, 1.7749597193))
                Line((4.275, 1.7749597193), (4.275, 0.6694512863))
                CenterArc((3.825, 2.925), 2.3, -78.717175712, 6.4361075854)
            make_face()
            # Profile area: 1.6292165904, perimeter: 5.3669406181
            with BuildLine():
                CenterArc((3.825, 2.925), 2.3, 78.717175712, 22.5656485759)
                Line((3.375, 3.4), (3.375, 5.1805487137))
                Line((4.275, 3.4), (3.375, 3.4))
                Line((4.275, 5.1805487137), (4.275, 3.4))
            make_face()
            # Profile area: 1.9865452703, perimeter: 6.1894118405
            with BuildLine():
                Line((4.275, 2.45), (6.0754166281, 2.45))
                Line((4.275, 2.45), (4.275, 1.7749597193))
                Line((4.275, 1.7749597193), (4.525, 1.7749597193))
                Line((4.525, 1.7749597193), (4.525, 0.73410977))
                CenterArc((3.825, 2.925), 2.3, -72.2810681266, 60.3624733957)
            make_face()
            # Profile area: 1.7418669285, perimeter: 5.5077193694
            with BuildLine():
                Line((1.5745833719, 2.45), (3.375, 2.45))
                Line((3.375, 2.45), (3.375, 3.4))
                Line((3.375, 3.4), (1.5745833719, 3.4))
                CenterArc((3.825, 2.925), 2.3, 168.0814052691, 23.8371894617)
            make_face()
            # Profile area: 2.2554645249, perimeter: 6.2624322415
            with BuildLine():
                Line((4.275, 5.1805487137), (4.275, 3.4))
                Line((6.0754166281, 3.4), (4.275, 3.4))
                CenterArc((3.825, 2.925), 2.3, 11.9185947309, 66.7985809812)
            make_face()
            # Profile area: 1.7418669285, perimeter: 5.5077193694
            with BuildLine():
                Line((6.0754166281, 3.4), (4.275, 3.4))
                Line((4.275, 3.4), (4.275, 2.45))
                Line((4.275, 2.45), (6.0754166281, 2.45))
                CenterArc((3.825, 2.925), 2.3, -11.9185947309, 23.8371894617)
            make_face()
            # Profile area: 0.6075362526, perimeter: 3.1500805614
            with BuildLine():
                Line((4.275, -1.7749597193), (4.275, -2.45))
                Line((4.275, -1.7749597193), (3.375, -1.7749597193))
                Line((3.375, -2.45), (3.375, -1.7749597193))
                Line((3.375, -2.45), (4.275, -2.45))
            make_face()
            # Profile area: 0.855, perimeter: 3.7
            with BuildLine():
                Line((4.275, -2.45), (4.275, -3.4))
                Line((3.375, -2.45), (4.275, -2.45))
                Line((3.375, -3.4), (3.375, -2.45))
                Line((4.275, -3.4), (3.375, -3.4))
            make_face()
            # Profile area: 0.6075362526, perimeter: 3.1500805614
            with BuildLine():
                Line((3.375, 2.45), (4.275, 2.45))
                Line((3.375, 1.7749597193), (3.375, 2.45))
                Line((3.375, 1.7749597193), (4.275, 1.7749597193))
                Line((4.275, 2.45), (4.275, 1.7749597193))
            make_face()
            # Profile area: 0.855, perimeter: 3.7
            with BuildLine():
                Line((4.275, 3.4), (3.375, 3.4))
                Line((3.375, 2.45), (3.375, 3.4))
                Line((3.375, 2.45), (4.275, 2.45))
                Line((4.275, 3.4), (4.275, 2.45))
            make_face()
        # OneSide extrude, distance=1.266
        extrude(amount=1.266)
    return part.part


# Description: This is a hexagonal or octagonal box-shaped component with a saddle or curved waist profile, featuring faceted surfaces and angled top and bottom planes that taper inward at the center, creating a pinched or hourglass-like geometry.
def model_21604_520e1ae2_0000():
    """Model: Base Support v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.36, perimeter: 5.6828427125
            with BuildLine():
                Line((0, 0), (2.3, 0))
                Line((0, -0.4), (0, 0))
                Line((0.2, -0.6), (0, -0.4))
                Line((2.3, -0.6), (0.2, -0.6))
                Line((2.3, 0), (2.3, -0.6))
            make_face()
            # Profile area: 1.36, perimeter: 5.6828427125
            with BuildLine():
                Line((2.3, 0), (2.3, 0.6))
                Line((2.3, 0.6), (0.2, 0.6))
                Line((0.2, 0.6), (0, 0.4))
                Line((0, 0.4), (0, 0))
                Line((0, 0), (2.3, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is an oval-shaped composite or layered vessel/container featuring a curved, boat-like form with a ribbed or corrugated exterior wall and an internal framework of diagonal bracing supports.
def model_21604_520e1ae2_0011():
    """Model: Flywheel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # Symmetric extrude, each_side=0.425
        extrude(amount=0.425, both=True)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an elliptical cross-section, featuring a hollow central bore and a mesh or perforated band around the upper half of its outer surface.
def model_21636_f65686bc_0000():
    """Model: wheel v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.6576320931, perimeter: 20.4203522483
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical spacer or bushing with a hollow tubular shape, featuring a rounded domed end on one side and a flat or slightly tapered end on the other, designed for use as a mechanical component in assemblies.
def model_21638_0a984848_0009():
    """Model: Crankshaft pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)
    return part.part


# Description: This is a drive belt or pulley belt, featuring a closed-loop toroidal shape with a flat inner surface and a ribbed outer surface designed for grip and power transmission in mechanical systems.
def model_21644_aa203dc5_0006():
    """Model: PT-201-P-013 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8773225947, perimeter: 21.6769893098
            with BuildLine():
                CenterArc((0, 0), 1.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a elongated trapezoidal channel or trough with a curved bottom surface, tapered ends, and an open top design, resembling a boat-like or scoop-shaped structural component.
def model_21644_aa203dc5_0017():
    """Model: PT-201-P-039 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30, perimeter: 29
            with BuildLine():
                Line((-6, 1.25), (6, 1.25))
                Line((-6, -1.25), (-6, 1.25))
                Line((6, -1.25), (-6, -1.25))
                Line((6, 1.25), (6, -1.25))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is a curved mesh or perforated ring-shaped component with an oval/elliptical cross-section, featuring internal structural ribs or supports and open mesh sections on the sides, designed for lightweight strength and ventilation.
def model_21646_a2dd0d00_0049():
    """Model: Mars Drive v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 35.9084040305
            with BuildLine():
                CenterArc((0, 0), 3.175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.54, 96.2301356872, 347.5397286257)
                CenterArc((0, 0), 2.54, 83.7698643128, 12.4602713743)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with BuildLine():
                CenterArc((0, 0), 1.27, 23.7699312424, 132.4601375153)
                CenterArc((0, 0), 1.27, 156.2300687576, 227.5398624847)
            make_face()
            # Profile area: 1.6307425419, perimeter: 7.8878561172
            with BuildLine():
                CenterArc((0, 0), 1.27, 23.7699312424, 132.4601375153)
                Line((1.1622675789, 0.5118926402), (0.2756464675, 2.5249988168))
                CenterArc((0, 0), 2.54, 83.7698643128, 12.4602713743)
                Line((-1.1622675789, 0.5118926402), (-0.2756464675, 2.5249988168))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical motor or pump housing with a rounded/domed top end, a flat circular base, and internal radial vanes or impeller blades visible through the semi-transparent mesh, featuring a small protruding nozzle or port on the lower right side.
def model_21697_06656699_0008():
    """Model: 7. Idler Gear (Return) v2"""
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
            # Profile area: 2.5398289225, perimeter: 5.6494629423
            with BuildLine():
                CenterArc((0, 0), 0.8991399531, 7.2244057436, 345.5511885127)
                CenterArc((0, 0), 0.8991399531, -7.2244057436, 14.4488114873)
            make_face()
        # OneSide extrude, distance=1.5875
        extrude(amount=1.5875)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0769101739, perimeter: 1.078977438
            with BuildLine():
                Line((0.8920018827, 0.1130720856), (1.0202948812, 0.1293347833))
                CenterArc((0, 0), 0.8991399531, -7.2244057436, 14.4488114873)
                Line((0.8920018827, -0.1130720856), (1.0202948812, -0.1293347833))
                _nurbs_edge([(1.0202948812, -0.1293347833), (1.0286320059, -0.1294075214), (1.0455088936, -0.1295547655), (1.0708473347, -0.1255376927), (1.0963850971, -0.119863173), (1.1220438211, -0.1122533177), (1.1477617094, -0.1030138107), (1.1734900217, -0.0922088711), (1.1991649176, -0.0798966197), (1.2247966112, -0.0662171527), (1.2415163966, -0.0560785794), (1.2499578905, -0.0509598114)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0249718287, 0.0505506115, 0.0767119078, 0.1034519158, 0.1307686481, 0.1586607103, 0.1871269974, 0.2161665826, 0.2457786684, 0.2457786684, 0.2457786684, 0.2457786684], 3)
                CenterArc((-0.0232285707, 0), 1.2742058967, -2.2920636578, 4.5841273156)
                _nurbs_edge([(1.0202948812, 0.1293347833), (1.0286320059, 0.1294075214), (1.0455088936, 0.1295547655), (1.0708473347, 0.1255376927), (1.0963850971, 0.119863173), (1.1220438211, 0.1122533177), (1.1477617094, 0.1030138107), (1.1734900217, 0.0922088711), (1.1991649176, 0.0798966197), (1.2247966112, 0.0662171527), (1.2415163966, 0.0560785794), (1.2499578905, 0.0509598114)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0249718287, 0.0505506115, 0.0767119078, 0.1034519158, 0.1307686481, 0.1586607103, 0.1871269974, 0.2161665826, 0.2457786684, 0.2457786684, 0.2457786684, 0.2457786684], 3)
            make_face()
        # OneSide extrude, distance=1.5875
        extrude(amount=1.5875, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated cage-like component with a solid rounded front end and an open, latticed back section, featuring a small protruding nozzle or connector on one side.
def model_21697_06656699_0010():
    """Model: 15. Idler Gear (Feed) v3"""
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
            # Profile area: 2.5398289225, perimeter: 5.6494629423
            with BuildLine():
                CenterArc((0, 0), 0.8991399531, 7.2244057436, 345.5511885127)
                CenterArc((0, 0), 0.8991399531, -7.2244057436, 14.4488114873)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0769101739, perimeter: 1.078977438
            with BuildLine():
                Line((0.8920018827, 0.1130720856), (1.0202948812, 0.1293347833))
                CenterArc((0, 0), 0.8991399531, -7.2244057436, 14.4488114873)
                Line((0.8920018827, -0.1130720856), (1.0202948812, -0.1293347833))
                _nurbs_edge([(1.0202948812, -0.1293347833), (1.0286320059, -0.1294075214), (1.0455088936, -0.1295547655), (1.0708473347, -0.1255376927), (1.0963850971, -0.119863173), (1.1220438211, -0.1122533177), (1.1477617094, -0.1030138107), (1.1734900217, -0.0922088711), (1.1991649176, -0.0798966197), (1.2247966112, -0.0662171527), (1.2415163966, -0.0560785794), (1.2499578905, -0.0509598114)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0249718287, 0.0505506115, 0.0767119078, 0.1034519158, 0.1307686481, 0.1586607103, 0.1871269974, 0.2161665826, 0.2457786684, 0.2457786684, 0.2457786684, 0.2457786684], 3)
                CenterArc((-0.0232285707, 0), 1.2742058967, -2.2920636578, 4.5841273156)
                _nurbs_edge([(1.0202948812, 0.1293347833), (1.0286320059, 0.1294075214), (1.0455088936, 0.1295547655), (1.0708473347, 0.1255376927), (1.0963850971, 0.119863173), (1.1220438211, 0.1122533177), (1.1477617094, 0.1030138107), (1.1734900217, 0.0922088711), (1.1991649176, 0.0798966197), (1.2247966112, 0.0662171527), (1.2415163966, 0.0560785794), (1.2499578905, 0.0509598114)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0249718287, 0.0505506115, 0.0767119078, 0.1034519158, 0.1307686481, 0.1586607103, 0.1871269974, 0.2161665826, 0.2457786684, 0.2457786684, 0.2457786684, 0.2457786684], 3)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with an open top end, featuring a solid dark gray sidewall with vertical ribbing and a perforated blue mesh cap at the top.
def model_21702_3390d14a_0003():
    """Model: Pump Lever v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)
    return part.part


# Description: This is a paraglider wing canopy with an elliptical planform featuring a ribbed upper surface, internal cell structure with radial bracing lines, and a solid leading edge that tapers toward the wingtips.
def model_21703_42d28e69_0012():
    """Model: Adjusting Handle Knob v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.3720615334, perimeter: 10.8523176626
            Circle(1.7272)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


MODELS = {
    "model_130757_b2c47f8d_0009": {"func": model_130757_b2c47f8d_0009, "volume": 0.1235490567, "area": 3.5597313218},
    "model_130834_62ed16e7_0000": {"func": model_130834_62ed16e7_0000, "volume": 29.348005771, "area": 67.443749986},
    "model_130917_2e98fb39_0000": {"func": model_130917_2e98fb39_0000, "volume": 85.1175259582, "area": 153.5453409442},
    "model_130975_dfe64cd6_0000": {"func": model_130975_dfe64cd6_0000, "volume": 115.6431922442, "area": 338.0637437021},
    "model_131394_cff473cf_0000": {"func": model_131394_cff473cf_0000, "volume": 215.537775651, "area": 252.868726},
    "model_131494_c8a441d0_0000": {"func": model_131494_c8a441d0_0000, "volume": 6.9380870174, "area": 45.8555886273},
    "model_131709_8b86dfb6_0000": {"func": model_131709_8b86dfb6_0000, "volume": 5.7302248047, "area": 32.0602349928},
    "model_131823_4d7d57e7_0000": {"func": model_131823_4d7d57e7_0000, "volume": 18.3783090064, "area": 195.5513164992},
    "model_131876_b2384623_0000": {"func": model_131876_b2384623_0000, "volume": 21.5810974398, "area": 63.0305479919},
    "model_132148_a107f53e_0001": {"func": model_132148_a107f53e_0001, "volume": 9110.6731865458, "area": 10422.6309915365},
    "model_132863_90d729e2_0001": {"func": model_132863_90d729e2_0001, "volume": 0.1439008588, "area": 3.6619375301},
    "model_133072_95309b10_0000": {"func": model_133072_95309b10_0000, "volume": 0.5365402413, "area": 12.5782990272},
    "model_133248_c7255340_0000": {"func": model_133248_c7255340_0000, "volume": 16.9908, "area": 290.112},
    "model_133249_b81dc8d6_0000": {"func": model_133249_b81dc8d6_0000, "volume": 12.0720095944, "area": 91.5862223116},
    "model_133402_47273d61_0020": {"func": model_133402_47273d61_0020, "volume": 319.547748, "area": 516.128},
    "model_133424_315bcaeb_0001": {"func": model_133424_315bcaeb_0001, "volume": 15.8850970946, "area": 58.6939847093},
    "model_133564_b5340c41_0004": {"func": model_133564_b5340c41_0004, "volume": 1.791653104, "area": 27.8202797447},
    "model_133596_89dea5d1_0000": {"func": model_133596_89dea5d1_0000, "volume": 33.6812661665, "area": 843.5873708458},
    "model_133634_76b946d7_0000": {"func": model_133634_76b946d7_0000, "volume": 3.2, "area": 35.2},
    "model_133710_00be7f31_0004": {"func": model_133710_00be7f31_0004, "volume": 24978.7538605021, "area": 13822.0072338275},
    "model_133710_00be7f31_0005": {"func": model_133710_00be7f31_0005, "volume": 992.9066386365, "area": 1040.0840242563},
    "model_133824_6521bcf0_0000": {"func": model_133824_6521bcf0_0000, "volume": 206.1778714378, "area": 653.0707812546},
    "model_133841_1a1b322e_0000": {"func": model_133841_1a1b322e_0000, "volume": 3.500740855, "area": 30.9076222612},
    "model_134027_a6a95d00_0000": {"func": model_134027_a6a95d00_0000, "volume": 196.6447620934, "area": 258.0639957367},
    "model_134027_a6a95d00_0004": {"func": model_134027_a6a95d00_0004, "volume": 122.90298, "area": 245.1608},
    "model_134497_43d339c0_0000": {"func": model_134497_43d339c0_0000, "volume": 33.7669725957, "area": 127.7717285564},
    "model_135006_db473e01_0000": {"func": model_135006_db473e01_0000, "volume": 24.5, "area": 288.925},
    "model_135996_868f18fc_0000": {"func": model_135996_868f18fc_0000, "volume": 21.9338416713, "area": 116.6173700737},
    "model_136120_901bb8da_0000": {"func": model_136120_901bb8da_0000, "volume": 1570.7963267949, "area": 942.4777960769},
    "model_136341_7052a4b8_0000": {"func": model_136341_7052a4b8_0000, "volume": 19.7118233926, "area": 95.3326843859},
    "model_136804_344e4929_0000": {"func": model_136804_344e4929_0000, "volume": 0.8, "area": 6.4},
    "model_136821_0f4b88d0_0002": {"func": model_136821_0f4b88d0_0002, "volume": 180.2488784997, "area": 258.0032966761},
    "model_136821_0f4b88d0_0005": {"func": model_136821_0f4b88d0_0005, "volume": 84.3791587298, "area": 153.9495189119},
    "model_137098_0a45d1c8_0000": {"func": model_137098_0a45d1c8_0000, "volume": 0.2088410712, "area": 3.9794726138},
    "model_137098_0a45d1c8_0008": {"func": model_137098_0a45d1c8_0008, "volume": 0.0432597308, "area": 1.9353781542},
    "model_137099_58f819ec_0001": {"func": model_137099_58f819ec_0001, "volume": 1.0001875983, "area": 8.4171929805},
    "model_137189_cdfeb18a_0000": {"func": model_137189_cdfeb18a_0000, "volume": 0.4684350266, "area": 4.4517938698},
    "model_137209_c0c9a7dd_0001": {"func": model_137209_c0c9a7dd_0001, "volume": 0.7853981634, "area": 4.7123889804},
    "model_137348_de92dc85_0000": {"func": model_137348_de92dc85_0000, "volume": 2.8300722859, "area": 14.9100360554},
    "model_137447_6c8e2c63_0000": {"func": model_137447_6c8e2c63_0000, "volume": 7.4087497331, "area": 155.8228707304},
    "model_137717_63e1ca8f_0000": {"func": model_137717_63e1ca8f_0000, "volume": 375.9230004252, "area": 391.3082425406},
    "model_137744_580caf3a_0000": {"func": model_137744_580caf3a_0000, "volume": 33.4837931468, "area": 83.8327725661},
    "model_137837_9c9f163d_0004": {"func": model_137837_9c9f163d_0004, "volume": 17.4997105024, "area": 51.9997187736},
    "model_137837_9c9f163d_0007": {"func": model_137837_9c9f163d_0007, "volume": 28.8, "area": 80.2},
    "model_137837_9c9f163d_0010": {"func": model_137837_9c9f163d_0010, "volume": 525.6, "area": 816.6},
    "model_137907_ff5b17ca_0000": {"func": model_137907_ff5b17ca_0000, "volume": 75.3982236862, "area": 138.230076758},
    "model_138124_2366c1e3_0000": {"func": model_138124_2366c1e3_0000, "volume": 900, "area": 650},
    "model_138134_2a26ecee_0000": {"func": model_138134_2a26ecee_0000, "volume": 0.7068583471, "area": 6.0475658582},
    "model_138138_c62f4894_0000": {"func": model_138138_c62f4894_0000, "volume": 0.0560000017, "area": 1.2000000262},
    "model_138210_482aa6e2_0000": {"func": model_138210_482aa6e2_0000, "volume": 3.9584067435, "area": 53.344243258},
    "model_138535_c0da19b3_0009": {"func": model_138535_c0da19b3_0009, "volume": 34.49665711, "area": 87.835392436},
    "model_138535_c0da19b3_0013": {"func": model_138535_c0da19b3_0013, "volume": 23.4084058392, "area": 90.2858347058},
    "model_138642_bd3f2dbd_0000": {"func": model_138642_bd3f2dbd_0000, "volume": 0.9492479282, "area": 10.2019687134},
    "model_138775_4626dfa8_0006": {"func": model_138775_4626dfa8_0006, "volume": 0.0320047141, "area": 0.5580694811},
    "model_139258_43c33f60_0039": {"func": model_139258_43c33f60_0039, "volume": 26.1380508779, "area": 69.3663657913},
    "model_139330_fc67535e_0000": {"func": model_139330_fc67535e_0000, "volume": 804.4995503768, "area": 908.783873755},
    "model_139785_ce182c73_0000": {"func": model_139785_ce182c73_0000, "volume": 157.0796326795, "area": 659.7344572539},
    "model_140462_343115e7_0002": {"func": model_140462_343115e7_0002, "volume": 1.9, "area": 11.5},
    "model_140462_c2442684_0003": {"func": model_140462_c2442684_0003, "volume": 0.2986476516, "area": 4.2116976512},
    "model_140842_5958dd74_0000": {"func": model_140842_5958dd74_0000, "volume": 851534.1112078517, "area": 95478.9606030019},
    "model_140941_7fb9203a_0000": {"func": model_140941_7fb9203a_0000, "volume": 11.7435900314, "area": 81.7601823161},
    "model_140993_248dc00c_0000": {"func": model_140993_248dc00c_0000, "volume": 187411.9544545648, "area": 27237.764893144},
    "model_141453_50ec6f25_0000": {"func": model_141453_50ec6f25_0000, "volume": 173.8986574, "area": 423.9967667493},
    "model_141504_becd21e8_0000": {"func": model_141504_becd21e8_0000, "volume": 85.8919600825, "area": 133.4796001013},
    "model_141638_a21f336f_0015": {"func": model_141638_a21f336f_0015, "volume": 13.054928767, "area": 99.9750217609},
    "model_142246_0851be5e_0005": {"func": model_142246_0851be5e_0005, "volume": 156.398444754, "area": 300.3831386607},
    "model_142246_0851be5e_0010": {"func": model_142246_0851be5e_0010, "volume": 715.186149565, "area": 809.4322133909},
    "model_142246_0851be5e_0014": {"func": model_142246_0851be5e_0014, "volume": 85.5, "area": 172.5},
    "model_142246_0851be5e_0017": {"func": model_142246_0851be5e_0017, "volume": 45.5473512451, "area": 94.5531788956},
    "model_142246_0851be5e_0032": {"func": model_142246_0851be5e_0032, "volume": 338.3552789716, "area": 374.1161169816},
    "model_142504_3fe2ab83_0000": {"func": model_142504_3fe2ab83_0000, "volume": 22.68, "area": 56.76},
    "model_142800_fc51c220_0000": {"func": model_142800_fc51c220_0000, "volume": 47.9092879672, "area": 92.6769832809},
    "model_143646_e3f1ab5c_0000": {"func": model_143646_e3f1ab5c_0000, "volume": 26.7398223686, "area": 66.506192983},
    "model_143678_6d68b8bc_0002": {"func": model_143678_6d68b8bc_0002, "volume": 0.9525951168, "area": 10.4276369043},
    "model_143786_f34f7c93_0006": {"func": model_143786_f34f7c93_0006, "volume": 347.15264, "area": 1782.8992},
    "model_144491_cbdce23f_0000": {"func": model_144491_cbdce23f_0000, "volume": 503.7942495883, "area": 524.1371669412},
    "model_144935_1f83b45b_0000": {"func": model_144935_1f83b45b_0000, "volume": 37.446490342, "area": 181.4016917237},
    "model_145201_a104c55b_0006": {"func": model_145201_a104c55b_0006, "volume": 182499.9879422587, "area": 40099.9975884517},
    "model_145355_cedfad61_0001": {"func": model_145355_cedfad61_0001, "volume": 120, "area": 512},
    "model_145587_b07d242e_0000": {"func": model_145587_b07d242e_0000, "volume": 4.358459704, "area": 30.2400427474},
    "model_145702_e28c737e_0048": {"func": model_145702_e28c737e_0048, "volume": 90, "area": 236},
    "model_146004_f79f7c2f_0002": {"func": model_146004_f79f7c2f_0002, "volume": 0.8168141143, "area": 8.4194684408},
    "model_146075_8bb6e65a_0000": {"func": model_146075_8bb6e65a_0000, "volume": 0.1524745977, "area": 1.7874764334},
    "model_146131_6ddecf51_0000": {"func": model_146131_6ddecf51_0000, "volume": 25.0572941925, "area": 263.0247705468},
    "model_146135_0ca63e9c_0003": {"func": model_146135_0ca63e9c_0003, "volume": 1.785375, "area": 10.09125},
    "model_146580_daeba71e_0000": {"func": model_146580_daeba71e_0000, "volume": 18.3271256422, "area": 59.668042963},
    "model_146769_3c88fc97_0000": {"func": model_146769_3c88fc97_0000, "volume": 1.4124837971, "area": 11.8194856193},
    "model_146857_25b972d7_0007": {"func": model_146857_25b972d7_0007, "volume": 224.8879741701, "area": 362.4736703895},
    "model_147134_273aac81_0002": {"func": model_147134_273aac81_0002, "volume": 76.467945172, "area": 236.6437701495},
    "model_147673_79b26fed_0000": {"func": model_147673_79b26fed_0000, "volume": 201603.7469843755, "area": 117173.5282197497},
    "model_148051_c59af578_0004": {"func": model_148051_c59af578_0004, "volume": 2.8973776874, "area": 109.7787833954},
    "model_148051_c59af578_0007": {"func": model_148051_c59af578_0007, "volume": 0.9552227711, "area": 12.1926487158},
    "model_148051_c59af578_0012": {"func": model_148051_c59af578_0012, "volume": 0.1787551385, "area": 3.4484258994},
    "model_20276_d041fa0f_0000": {"func": model_20276_d041fa0f_0000, "volume": 1.3607239165, "area": 6.8110121429},
    "model_20342_c140780b_0000": {"func": model_20342_c140780b_0000, "volume": 0.1859795398, "area": 2.3081653091},
    "model_20591_20e06209_0000": {"func": model_20591_20e06209_0000, "volume": 1230.4889025072, "area": 1927.4642492148},
    "model_20951_2918f2fa_0000": {"func": model_20951_2918f2fa_0000, "volume": 46.5666454517, "area": 229.8563051427},
    "model_21180_594c9e3e_0000": {"func": model_21180_594c9e3e_0000, "volume": 18.5333332136, "area": 38.915135056},
    "model_21231_eb9826e5_0008": {"func": model_21231_eb9826e5_0008, "volume": 94.7977, "area": 166.1501082169},
    "model_21233_05d745b4_0015": {"func": model_21233_05d745b4_0015, "volume": 8.3827110723, "area": 24.5431668965},
    "model_21235_01764fc7_0027": {"func": model_21235_01764fc7_0027, "volume": 188.195188125, "area": 258.2062633213},
    "model_21246_c66f2b12_0031": {"func": model_21246_c66f2b12_0031, "volume": 7.051304711, "area": 26.0477300891},
    "model_21256_433456a3_0000": {"func": model_21256_433456a3_0000, "volume": 51.4908716481, "area": 187.0868585049},
    "model_21604_520e1ae2_0000": {"func": model_21604_520e1ae2_0000, "volume": 1.632, "area": 9.499411255},
    "model_21604_520e1ae2_0011": {"func": model_21604_520e1ae2_0011, "volume": 24.0331838, "area": 72.5707902979},
    "model_21636_f65686bc_0000": {"func": model_21636_f65686bc_0000, "volume": 7.6576320931, "area": 35.7356164346},
    "model_21638_0a984848_0009": {"func": model_21638_0a984848_0009, "volume": 4.2976987501, "area": 16.587609211},
    "model_21644_aa203dc5_0006": {"func": model_21644_aa203dc5_0006, "volume": 2.9263935568, "area": 22.7608387753},
    "model_21644_aa203dc5_0017": {"func": model_21644_aa203dc5_0017, "volume": 36, "area": 94.8},
    "model_21646_a2dd0d00_0049": {"func": model_21646_a2dd0d00_0049, "volume": 22.985394228, "area": 93.0922081109},
    "model_21697_06656699_0008": {"func": model_21697_06656699_0008, "volume": 4.1540869079, "area": 15.1949598254},
    "model_21697_06656699_0010": {"func": model_21697_06656699_0010, "volume": 3.3232695263, "area": 13.2026634989},
    "model_21702_3390d14a_0003": {"func": model_21702_3390d14a_0003, "volume": 39.4081382466, "area": 68.6123835544},
    "model_21703_42d28e69_0012": {"func": model_21703_42d28e69_0012, "volume": 5.9512590737, "area": 25.6353447825},
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
