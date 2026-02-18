"""Batch 015 - passing/01_2ops
201 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a slight trapezoidal form, featuring a uniform dark gray finish and no visible holes, slots, or additional features—appearing to be a simple structural or trim component with clean, angled edges.
def model_51913_1fa125b4_0001():
    """Model: Deck v4"""
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
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.3758110477, perimeter: 82.4547411633
            with BuildLine():
                _nurbs_edge([(26, -0.6), (27.4235077625, -0.6), (28.6693075108, -0.4802850813), (29.7668613404, -0.2566653487), (31.3492084447, 0.0657279836), (32.6256766884, 0.6013819187), (33.7697716145, 1.2357793289), (34.7393908103, 1.7734304387), (35.6184703267, 2.3786106611), (36.5173590679, 3.0130926804), (37.3145928355, 3.5758213781), (38.1289407816, 4.1631489734), (39.0038371944, 4.7723490683), (39.1153949023, 4.85002794), (39.2278694203, 4.9280812855), (39.3412852597, 5.0065181143)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.2046920518, 0.2046920518, 0.2046920518, 0.4997972819, 0.4997972819, 0.4997972819, 0.749898641, 0.749898641, 0.749898641, 0.9717161358, 0.9717161358, 0.9717161358, 1, 1, 1, 1], 3)
                Line((39.3412852597, 5.0065181143), (39, 5.5))
                _nurbs_edge([(26, 0), (26.8153069584, 0), (28.3418454789, 0.0652907744), (30.3197249681, 0.3589220255), (32.43383419, 1.0869377135), (34.6004403394, 2.3639765559), (36.2534474862, 3.5564515235), (37.5777806228, 4.5083874852), (38.5165936729, 5.1656828575), (39, 5.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (26, 0))
                Line((0, -0.6), (0, 0))
                Line((0, -0.6), (26, -0.6))
            make_face()
            # Profile area: 23.9741677436, perimeter: 81.108729534
            with BuildLine():
                Line((0, -0.6), (0, 0))
                Line((0, 0), (-26, 0))
                _nurbs_edge([(-26, 0), (-27.0468021105, 0), (-28.9777553664, 0.0203162587), (-31.3866797801, 0.1116985895), (-33.7653993036, 0.350666433), (-35.8663308946, 0.865038396), (-37.1951919182, 1.5084463453), (-38.1160918135, 2.1730647778), (-38.7088845752, 2.7088845752), (-39, 3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((-39.4242640687, 2.5757359313), (-39, 3))
                _nurbs_edge([(-26, -0.6), (-27.6734682369, -0.6), (-29.0961246137, -0.5690204164), (-30.3085167319, -0.5070660592), (-32.0134744874, -0.4199411428), (-33.310400975, -0.2737529782), (-34.3976237956, -0.0502254598), (-35.3122985564, 0.1378270495), (-36.0815202939, 0.3822113711), (-36.7849788066, 0.7067413929), (-37.5419555746, 1.0559612581), (-38.2214628375, 1.4991389066), (-38.8663053273, 2.0562669515), (-39.055469705, 2.2197003195), (-39.2413567292, 2.3928285918), (-39.4242640687, 2.5757359313)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1909879462, 0.1909879462, 0.1909879462, 0.4595696825, 0.4595696825, 0.4595696825, 0.685526065, 0.685526065, 0.685526065, 0.92867293, 0.92867293, 0.92867293, 1, 1, 1, 1], 3)
                Line((0, -0.6), (-26, -0.6))
            make_face()
        # TwoSides extrude (symmetric), distance=10.25
        extrude(amount=10.25, both=True)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slightly curved upper right edge, featuring a simple rectangular geometry with no holes, slots, or additional features.
def model_51913_1fa125b4_0002():
    """Model: Griptape v5"""
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
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2315935481, perimeter: 81.0035325145
            with BuildLine():
                Line((0, 0), (0, 0.08))
                Line((0, 0), (26, 0))
                _nurbs_edge([(26, 0), (26.8153069584, 0), (28.3418454789, 0.0652907744), (30.3197249681, 0.3589220255), (32.43383419, 1.0869377135), (34.6004403394, 2.3639765559), (36.2534474862, 3.5564515235), (37.5777806228, 4.5083874852), (38.5165936729, 5.1656828575), (39, 5.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((38.9544952987, 5.5657975848), (39, 5.5))
                _nurbs_edge([(26, 0.08), (27.3505499498, 0.08), (28.5225942701, 0.190348174), (29.5497148167, 0.3933131428), (31.4089319501, 0.7607052165), (32.8026671168, 1.423288591), (34.1052392362, 2.2184613244), (34.950133815, 2.7342386251), (35.7580880179, 3.3063499639), (36.6060087939, 3.9095504881), (37.3503316705, 4.439052727), (38.1260763842, 4.9928744997), (38.9544952987, 5.5657975848)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1994058674, 0.1994058674, 0.1994058674, 0.5603555207, 0.5603555207, 0.5603555207, 0.7944802964, 0.7944802964, 0.7944802964, 1, 1, 1, 1], 3)
                Line((0, 0.08), (26, 0.08))
            make_face()
            # Profile area: 3.1729290622, perimeter: 79.5340243074
            with BuildLine():
                _nurbs_edge([(-26, 0.08), (-27.6751012076, 0.08), (-29.0938897573, 0.1112585753), (-30.2954299549, 0.1731569393), (-32.1609411435, 0.2692603329), (-33.5118726933, 0.4365604745), (-34.6103028905, 0.6923897275), (-35.4829871705, 0.8956417576), (-36.1987907237, 1.1556437329), (-36.8547208788, 1.4984802286), (-37.4710664981, 1.8206269855), (-38.0346832763, 2.2176312852), (-38.5803290039, 2.7110118095), (-38.702434144, 2.8214209907), (-38.8234489892, 2.9365860742), (-38.9434314575, 3.0565685425)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1921389645, 0.1921389645, 0.1921389645, 0.4904539012, 0.4904539012, 0.4904539012, 0.7274600909, 0.7274600909, 0.7274600909, 0.9501632639, 0.9501632639, 0.9501632639, 1, 1, 1, 1], 3)
                Line((-38.9434314575, 3.0565685425), (-39, 3))
                _nurbs_edge([(-26, 0), (-27.0468021105, 0), (-28.9777553664, 0.0203162587), (-31.3866797801, 0.1116985895), (-33.7653993036, 0.350666433), (-35.8663308946, 0.865038396), (-37.1951919182, 1.5084463453), (-38.1160918135, 2.1730647778), (-38.7088845752, 2.7088845752), (-39, 3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (-26, 0))
                Line((0, 0), (0, 0.08))
                Line((0, 0.08), (-26, 0.08))
            make_face()
        # TwoSides extrude (symmetric), distance=10.25
        extrude(amount=10.25, both=True)
    return part.part


# Description: This is a torus or ring-shaped seal/gasket featuring a smooth, rounded cross-section with a uniform circular band and a hollow center, designed for sealing or containment applications.
def model_51913_1fa125b4_0004():
    """Model: Washer2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3632466506, perimeter: 5.8119464091
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a rectangular tray or channel with upturned flanges on both ends and a central longitudinal slot or opening running along its length.
def model_51913_1fa125b4_0008():
    """Model: Ramp v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18459.925266583, perimeter: 1631.6272003423
            with BuildLine():
                Line((-96.5775545279, 72.6968032234), (-150, 72.6968032234))
                Line((-150, 72.6968032234), (-150, -10))
                Line((550, -10), (-150, -10))
                Line((550, 72.6968032234), (550, -10))
                Line((496.5775545279, 72.6968032234), (550, 72.6968032234))
                CenterArc((400, 100.4999435298), 100.4999435298, -90, 73.9397327526)
                Line((0, 0), (400, 0))
                CenterArc((0, 100.4999435298), 100.4999435298, -163.9397327526, 73.9397327526)
            make_face()
        # OneSide extrude, distance=300
        extrude(amount=300)
    return part.part


# Description: This is a cylindrical rod or pin with a tapered end, featuring a rounded tip at one end and a slightly conical or beveled point at the opposite end.
def model_51913_1fa125b4_0014():
    """Model: RodAxle v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=19
        extrude(amount=19)
    return part.part


# Description: This is a 3D rectangular channel or hollow box frame with open top and bottom, featuring parallel flanges on the sides and a continuous rectangular cutout through its center.
def model_51914_fb924efa_0009():
    """Model: uszczelka guzik"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1424, perimeter: 14.24
            with BuildLine():
                Line((-1.025, 4.475), (-1.025, 6.025))
                Line((1.025, 4.475), (-1.025, 4.475))
                Line((1.025, 6.025), (1.025, 4.475))
                Line((-1.025, 6.025), (1.025, 6.025))
            make_face()
            with BuildLine():
                Line((1.005, 6.005), (1.005, 4.495))
                Line((1.005, 4.495), (-1.005, 4.495))
                Line((-1.005, 4.495), (-1.005, 6.005))
                Line((-1.005, 6.005), (1.005, 6.005))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved belt or band-like component with an oval/elliptical cross-section, featuring a hollow interior channel and mesh or perforated sections along its length, designed for applications such as conveyance or structural support.
def model_51916_fa226b15_0002():
    """Model: D-loop"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7122455489, perimeter: 10.3138950898
            with BuildLine():
                Line((-3.7465001216, -1.1585574037), (-3.7465001216, -0.7620000243))
                CenterArc((-2.5400000811, -0.7620000243), 1.2700000405, -161.805127954, 143.6102559081)
                Line((-1.3335000405, -0.7620000243), (-1.3335000405, -1.1585574037))
                Line((-3.7465001216, -0.7620000243), (-1.3335000405, -0.7620000243))
            make_face()
            with BuildLine():
                Line((-3.3655001094, -1.2153385783), (-3.3655001094, -1.0795000243))
                Line((-3.3655001094, -1.0795000243), (-1.7145000811, -1.0795000243))
                Line((-1.7145000811, -1.0795000243), (-1.7145000811, -1.2153385783))
                CenterArc((-2.5400000952, -0.7466834696), 0.9492564903, -150.4154383488, 120.8308766976)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a cylindrical pen or stylus with a rounded tip at one end, a tapered body with blue and dark gray striping, and a flat or rounded base at the opposite end, designed for writing or touch-screen input.
def model_51916_fa226b15_0013():
    """Model: Weight Arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.5049100955, perimeter: 37.9808688736
            with BuildLine():
                CenterArc((0, -10.1600000811), 0.9525, 179.9987559551, 177.4631398689)
                Line((0.9515655898, -10.2021803892), (0.9515758494, -10.1180518647))
                Line((0.9515758494, -10.1180518647), (0.9524999929, -2.5401162402))
                CenterArc((0, -2.5400000811), 0.9525, -0.0069873282, 180.0069873299)
                Line((-0.9524999998, -10.1599793997), (-0.9525, -2.5400000811))
            make_face()
            with BuildLine():
                Line((-0.2406484251, -2.5577208453), (-0.2412999991, -10.1599793997))
                CenterArc((0, -2.5400000811), 0.2413, -0.0000000067, 184.2115204031)
                Line((0.2412999991, -10.1599793997), (0.2413, -2.5400000811))
                CenterArc((0, -10.1600000811), 0.2413, 179.9950892963, 180.0098214075)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a uniform diameter that gradually reduces toward one end, forming a conical taper.
def model_51932_c1f74efe_0002():
    """Model: Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-2.8574999571, 3.8099999428)):
                Circle(0.3175)
        # TwoSides extrude, along=-17.78, against=0.3175
        extrude(amount=-17.78)
        extrude(sk.sketch, amount=0.3175)
    return part.part


# Description: This is a rectangular box or enclosure with a pyramidal or peaked roof-like top feature, appearing to be a housing or container component with a tapered upper section and what may be ventilation or access openings at the top.
def model_51940_aa0fca73_0011():
    """Model: head v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8420315668, perimeter: 6.1273840497
            with BuildLine():
                Line((0.7499716462, -0.0065214926), (-0.0135113205, 0.7498782863))
                Line((-0.7499716462, -0.0065214926), (-0.0135113205, 0.7498782863))
                Line((-0.7499716462, -0.0065214926), (0.0135113205, -0.7498782863))
                Line((0.7499716462, -0.0065214926), (0.0135113205, -0.7498782863))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a hollow core, featuring a solid base section and a mesh-textured upper portion with regular perforations throughout.
def model_51940_aa0fca73_0015():
    """Model: blocco 1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.8407044967, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 4.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a dark blue/gray elongated cylindrical component with a tapered rounded end, featuring longitudinal slots or grooves along its length and a textured grip surface, characteristic of a stylus or pen-like tool.
def model_51940_aa0fca73_0016():
    """Model: Attacco v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.5965298705, perimeter: 27.8439969461
            with BuildLine():
                CenterArc((2.1084888205, -1.5977704341), 1, 94.6290521578, 85.3709478422)
                Line((1.1084888205, -9.2977929046), (1.1084888205, -1.5977704341))
                CenterArc((1.4584888205, -9.2977929046), 0.35, -180, 90)
                Line((2.4870801475, -9.6477929046), (1.4584888205, -9.6477929046))
                CenterArc((2.4870801475, -9.1877929046), 0.46, -90, 90)
                Line((2.9470801475, -1.5977704341), (2.9470801475, -9.1877929046))
                CenterArc((1.9470801475, -1.5977704341), 1, 0, 85.3709478422)
            make_face()
            with BuildLine():
                CenterArc((2, -2), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -4), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0068031748, -8.6817792701), 0.5575350793, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a toroidal (donut-shaped) ring featuring a smooth, curved surface with a central hollow opening and an elliptical or oval cross-section, commonly used as a structural or seal component in mechanical assemblies.
def model_51940_aa0fca73_0023():
    """Model: Rondelle v1 (1)"""
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
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a polyhedral container or enclosure with an irregular, faceted geometric shape featuring multiple triangular and trapezoidal faces, internal structural elements, and what appears to be cutout openings or slots on its sides.
def model_51940_aa0fca73_0025():
    """Model: Dadi v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.265068328, perimeter: 6.0707963268
            with BuildLine():
                Line((-0.4732737292, 0.5818178213), (-0.7405058783, -0.1189581618))
                Line((-0.7405058783, -0.1189581618), (-0.267232149, -0.7007759831))
                Line((-0.267232149, -0.7007759831), (0.4732737292, -0.5818178213))
                Line((0.4732737292, -0.5818178213), (0.7405058783, 0.1189581618))
                Line((0.7405058783, 0.1189581618), (0.267232149, 0.7007759831))
                Line((0.267232149, 0.7007759831), (-0.4732737292, 0.5818178213))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a flat rectangular panel or plate with a slightly beveled or folded edge, featuring a central vertical seam or fold line running down its length.
def model_51942_f6e66631_0006():
    """Model: Backplate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.864, perimeter: 10.12
            with BuildLine():
                Line((0, 0.4), (4.66, 0.4))
                Line((0, 0), (0, 0.4))
                Line((0, 0), (4.66, 0))
                Line((4.66, 0), (4.66, 0.4))
            make_face()
            # Profile area: 33.086, perimeter: 23.52
            with BuildLine():
                Line((4.66, 7.5), (0, 7.5))
                Line((0, 0.4), (0, 7.5))
                Line((0, 0.4), (4.66, 0.4))
                Line((4.66, 0.4), (4.66, 7.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a ring-shaped component with an oval or elliptical profile, featuring radial ridges or fins around its outer and inner surfaces, likely designed for heat dissipation or structural reinforcement.
def model_51942_f6e66631_0007():
    """Model: Locking Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6787885743, perimeter: 8.9535390627
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a shallow 3D depth, featuring a triangular internal division and dark shaded edges that give it a beveled or chamfered appearance.
def model_51942_f6e66631_0008():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70.5, perimeter: 39.4
            with BuildLine():
                Line((0, -4.7), (15, -4.7))
                Line((15, -4.7), (15, 0))
                Line((0, 0), (15, 0))
                Line((0, 0), (0, -4.7))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a triangular prism or wedge-shaped structural component with a rectangular base and an angled top surface, featuring internal triangulation and edge reinforcement lines.
def model_51942_f6e66631_0009():
    """Model: Casing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.986, perimeter: 39.92
            with BuildLine():
                Line((0, 0), (0.1, 0))
                Line((0.1, 0), (0.1, 7.6))
                Line((0.1, 7.6), (-4.76, 7.6))
                Line((-4.76, 0), (-4.76, 7.6))
                Line((-4.66, 0), (-4.76, 0))
                Line((-4.66, 7.5), (-4.66, 0))
                Line((0, 7.5), (-4.66, 7.5))
                Line((0, 0), (0, 7.5))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a parallelpiped or skewed rectangular block with a trapezoidal profile, featuring flat faces with a tilted/angled geometry and no visible holes, slots, or curved features.
def model_52004_186af290_0005():
    """Model: Ball Box"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4193443459, perimeter: 10.1600003242
            with BuildLine():
                Line((1.7780000567, 1.0160000324), (-1.7780000567, 1.0160000324))
                Line((1.7780000567, 2.5400000811), (1.7780000567, 1.0160000324))
                Line((-1.7780000567, 2.5400000811), (1.7780000567, 2.5400000811))
                Line((-1.7780000567, 1.0160000324), (-1.7780000567, 2.5400000811))
            make_face()
        # OneSide extrude, distance=4.064
        extrude(amount=4.064)
    return part.part


# Description: This is a cylindrical air or fluid filter cartridge with a dark gray body and a blue mesh or perforated top surface, designed for filtration applications.
def model_52004_186af290_0006():
    """Model: Sleeve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a parallelogram-shaped frame or border with a hollow rectangular center, featuring dark structural sides and lighter-shaded top and bottom edges, resembling a skewed picture frame or window opening.
def model_52004_186af290_0007():
    """Model: Frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.6774032738, perimeter: 76.2000019455
            with BuildLine():
                Line((5.8420001864, -0.2540000081), (-5.5880001783, -0.2540000081))
                Line((5.8420001864, 7.8740002513), (5.8420001864, -0.2540000081))
                Line((-5.5880001783, 7.8740002513), (5.8420001864, 7.8740002513))
                Line((-5.5880001783, -0.2540000081), (-5.5880001783, 7.8740002513))
            make_face()
            with BuildLine():
                Line((5.5880001783, 0), (5.5880001783, 7.62))
                Line((-5.3340001702, 0), (5.5880001783, 0))
                Line((-5.3340001702, 7.62), (-5.3340001702, 0))
                Line((5.5880001783, 7.62), (-5.3340001702, 7.62))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


# Description: This is a rectangular tray or shallow pan with a flat bottom, raised walls, and angled corner flanges, featuring a central slot or opening running lengthwise along the top surface.
def model_52006_d21e4570_0001():
    """Model: Sump"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.9880532894, perimeter: 29.0398223686
            with BuildLine():
                Line((0, 0), (0, 3.75))
                Line((0, 0), (7, 0))
                Line((7, 3.75), (7, 0))
                Line((3.5, 3.75), (7, 3.75))
                Line((0, 3.75), (3.5, 3.75))
            make_face()
            with BuildLine():
                CenterArc((6.25, 2), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.75, 2), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 23.9880532894, perimeter: 29.0398223686
            with BuildLine():
                Line((0, 11.25), (3.5, 11.25))
                Line((3.5, 11.25), (7, 11.25))
                Line((7, 11.25), (7, 15))
                Line((7, 15), (0, 15))
                Line((0, 15), (0, 11.25))
            make_face()
            with BuildLine():
                CenterArc((6.25, 13), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.75, 13), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical stand or support post with a dark blue vertical body, featuring a gray rectangular cap on top and a wide gray base flange at the bottom for stability.
def model_52006_d21e4570_0003():
    """Model: Connecting_Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1521844322, perimeter: 1.7281751206
            with BuildLine():
                CenterArc((0, -8.5), 1.2000000179, 167.9753070027, 12.0246929973)
                Line((-1.8000000268, -8.2500001229), (-1.1736695039, -8.2500001229))
                Line((-1.8000000268, -8.5), (-1.8000000268, -8.2500001229))
                Line((-1.1999998912, -8.5), (-1.8000000268, -8.5))
            make_face()
            # Profile area: 0.6283186326, perimeter: 3.94159264
            with BuildLine():
                Line((0, -7.2999999821), (0, -7.7000001147))
                CenterArc((0, -8.5), 1.2000000179, 90, 61.5086716294)
                CenterArc((0, -8.5), 1.2000000179, 151.5086716294, 16.4666353732)
                CenterArc((0, -8.5), 1.2000000179, 167.9753070027, 12.0246929973)
                Line((-1.1999998912, -8.5), (-0.7999998853, -8.5))
                CenterArc((0, -8.5), 0.7999998853, 90, 90)
            make_face()
            # Profile area: 0.1521844322, perimeter: 1.7281751206
            with BuildLine():
                CenterArc((0, -8.5), 1.2000000179, 0, 12.0246929973)
                Line((1.1999998912, -8.5), (1.8000000268, -8.5))
                Line((1.8000000268, -8.5), (1.8000000268, -8.2500001229))
                Line((1.8000000268, -8.2500001229), (1.1736695039, -8.2500001229))
            make_face()
            # Profile area: 0.0633227211, perimeter: 1.8386060481
            with BuildLine():
                Line((-0.5000000075, 0), (-0.575, 0))
                CenterArc((0, 0), 0.575, -180, 29.5918442905)
                CenterArc((0, 0), 0.575, -150.4081557095, 60.4081557095)
                Line((0, -0.5000000075), (0, -0.575))
                CenterArc((0, 0), 0.5000000075, -180, 90)
            make_face()
            # Profile area: 0.6283186326, perimeter: 3.94159264
            with BuildLine():
                CenterArc((0, -8.5), 1.2000000179, 28.4913283706, 61.5086716294)
                Line((0, -7.2999999821), (0, -7.7000001147))
                CenterArc((0, -8.5), 0.7999998853, 0, 90)
                Line((0.7999998853, -8.5), (1.1999998912, -8.5))
                CenterArc((0, -8.5), 1.2000000179, 0, 12.0246929973)
                CenterArc((0, -8.5), 1.2000000179, 12.0246929973, 16.4666353732)
            make_face()
            # Profile area: 0.7531708363, perimeter: 16.5772649849
            with BuildLine():
                CenterArc((0, 0), 0.575, -29.5918442905, 29.5918442905)
                Line((0.5000000075, -0.2839454042), (1.0546671995, -7.9275690949))
                CenterArc((0, -8.5), 1.2000000179, 12.0246929973, 16.4666353732)
                Line((0.575, 0), (1.1736695039, -8.2500001229))
            make_face()
            # Profile area: 0.0633227211, perimeter: 1.8386060481
            with BuildLine():
                Line((0, -0.5000000075), (0, -0.575))
                CenterArc((0, 0), 0.575, -90, 60.4081557095)
                CenterArc((0, 0), 0.575, -29.5918442905, 29.5918442905)
                Line((0.575, 0), (0.5000000075, 0))
                CenterArc((0, 0), 0.5000000075, -90, 90)
            make_face()
            # Profile area: 0.7531708363, perimeter: 16.5772649849
            with BuildLine():
                Line((-0.575, 0), (-1.1736695039, -8.2500001229))
                CenterArc((0, -8.5), 1.2000000179, 151.5086716294, 16.4666353732)
                Line((-0.5000000075, -0.2839454042), (-1.0546671995, -7.9275690949))
                CenterArc((0, 0), 0.575, -180, 29.5918442905)
            make_face()
            # Profile area: 0.1266454421, perimeter: 3.5272121111
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 0, 180)
                Line((0.575, 0), (0.5000000075, 0))
                CenterArc((0, 0), 0.575, 0, 180)
                Line((-0.5000000075, 0), (-0.575, 0))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


# Description: This is a rectangular prism or block with a cylindrical hole drilled through its length, featuring a curved or rounded top surface and vertical ribbing or fluting on one of its larger faces.
def model_52012_77070fda_0013():
    """Model: Door Hinge v4 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4728124095, perimeter: 2.7849184504
            with BuildLine():
                Line((0.5000000075, -0.2500000149), (0.5000000075, -1.0000000149))
                CenterArc((0.2500000045, -0.2500000037), 0.250000003, -0.0000025613, 183.5877988535)
                Line((0.0004899808, -1.0000000149), (0.0004899815, -0.2656444898))
                Line((0.5000000075, -1.0000000149), (0.0004899808, -1.0000000149))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: A dark gray cylindrical bar or rod with rounded ends featuring two small rectangular slots or cutouts on the upper surface near each end.
def model_52012_77070fda_0024():
    """Model: Axel v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a circular disk or plate with a flat face and curved cylindrical edge, featuring a mesh or textured surface pattern on its outer rim.
def model_52012_77070fda_0025():
    """Model: Headlight v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((1.5, 1.5)):
                Circle(1.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a hexahedral (box-like) 3D part with a rectangular base body and two opposing angled or chamfered end faces, creating a wedge-like or truncated geometric form with faceted surfaces.
def model_52012_77070fda_0026():
    """Model: Bottom seat v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 48, perimeter: 28
            with BuildLine():
                Line((-8, 6), (-8, 0))
                Line((-8, 0), (0, 0))
                Line((0, 0), (0, 6))
                Line((0, 6), (-8, 6))
            make_face()
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a circular elastomeric O-ring or gasket seal featuring a torus (donut) shape with a uniform cross-section, designed for sealing applications in mechanical assemblies.
def model_52024_97da327b_0003():
    """Model: Balance Rod Split Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.204312922, perimeter: 8.5179897841
            with BuildLine():
                Line((-0.9143999889, -1.8287999779), (-0.990599988, -1.8287999779))
                Line((-0.990599988, -1.8287999779), (-0.990599988, -1.8874622598))
                CenterArc((-0.8890000284, -2.5400000811), 0.6604, 98.8498795561, 342.3002340188)
                Line((-0.7873999905, -1.8287999779), (-0.7873999905, -1.887462272))
                Line((-0.8635999896, -1.8287999779), (-0.7873999905, -1.8287999779))
                Line((-0.8635999896, -1.9309294792), (-0.8635999896, -1.8287999779))
                CenterArc((-0.8890000284, -2.5400000811), 0.6096, 92.3880117548, 355.2239691312)
                Line((-0.9143999889, -1.8287999779), (-0.9143999889, -1.930929476))
            make_face()
            with BuildLine():
                CenterArc((-0.952500006, -1.8796000117), 0.0254000002, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.8255000052, -1.8796000117), 0.0254000002, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0508
        extrude(amount=0.0508)
    return part.part


# Description: This is a hexagonal or octagonal box-like container with angled top faces and internal structural ribbing, featuring a open or recessed top design with faceted surfaces and what appears to be internal bracing or support elements.
def model_52024_97da327b_0004():
    """Model: Screw Nut (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7110385763, perimeter: 5.0356599679
            with BuildLine():
                Line((-3.5167061755, -1.7780000567), (-4.1032940677, -1.7780000567))
                Line((-4.1032940677, -1.7780000567), (-4.3965880138, -2.286000073))
                Line((-4.3965880138, -2.286000073), (-4.1032940677, -2.7940000892))
                Line((-4.1032940677, -2.7940000892), (-3.5167061755, -2.7940000892))
                Line((-3.5167061755, -2.7940000892), (-3.2234122294, -2.286000073))
                Line((-3.2234122294, -2.286000073), (-3.5167061755, -1.7780000567))
            make_face()
            with BuildLine():
                CenterArc((-3.8100001216, -2.286000073), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


# Description: This is an elongated rectangular channel or tray with a dark gray/black outer frame and blue interior surface, featuring two parallel slots or grooves running lengthwise along the bottom.
def model_52024_97da327b_0010():
    """Model: Arrow Rest Bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9976861243, perimeter: 18.198088256
            with BuildLine():
                CenterArc((6.8580002189, 0), 0.635, -90, 180)
                Line((6.8580002189, 0.635), (1.2700000405, 0.635))
                CenterArc((1.2700000405, 0), 0.635, 90, 180)
                Line((1.2700000405, -0.635), (6.8580002189, -0.635))
            make_face()
            with BuildLine():
                CenterArc((1.2700000405, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.8580002189, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a cylindrical mesh or perforated filter with a solid central core, featuring a netted or screened outer surface on the top and sides, designed for fluid filtration or straining applications.
def model_52024_97da327b_0012():
    """Model: Bearing Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5415436183, perimeter: 3.7903315366
            with BuildLine():
                CenterArc((-1.2700000405, -2.5400000811), 0.4445, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.2700000405, -2.5400000811), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)
    return part.part


# Description: This is a cylindrical sleeve or tube with threaded ends at both the top and bottom, featuring a smooth cylindrical body with ribbed or textured surface details along its length.
def model_52027_790dbc09_0012():
    """Model: Spacer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6602193749, perimeter: 26.0001088352
            with BuildLine():
                CenterArc((3.9245588257, -2.212563174), 2.2098, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.9245588257, -2.212563174), 1.928245842, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=11.43
        extrude(amount=11.43)
    return part.part


# Description: This is a pentahedron (five-faced polyhedron) or wedge-shaped block featuring a rectangular base with a slanted top face and angled sides, commonly used as a structural support or geometric reference component.
def model_52028_7396037a_0015():
    """Model: Exterior (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4516004118, perimeter: 10.1600003242
            with BuildLine():
                Line((-1.2700000405, 1.2700000405), (-1.2700000405, -1.2700000405))
                Line((-1.2700000405, -1.2700000405), (1.2700000405, -1.2700000405))
                Line((1.2700000405, -1.2700000405), (1.2700000405, 1.2700000405))
                Line((1.2700000405, 1.2700000405), (-1.2700000405, 1.2700000405))
            make_face()
        # OneSide extrude, distance=4.318
        extrude(amount=4.318)
    return part.part


# Description: This is a cylindrical ring or bushing with an elliptical or oval cross-section, featuring a central slot or groove running along its length and mesh or perforated sections on the upper surfaces.
def model_52229_996054ef_0011():
    """Model: Washer v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a hollow tubular body, featuring two circular holes or openings on opposite ends and a textured mesh-like surface pattern running along its length.
def model_52230_60438ea5_0007():
    """Model: mounting wheels"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((1, 1), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, 1), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3
        extrude(amount=-3)
    return part.part


# Description: This is a hexagonal or polygonal prism-shaped component with a flat base, slanted top surfaces, and triangulated faceting across its upper faces, featuring clean edges and no holes or slots visible.
def model_52352_adac16c3_0024():
    """Model: Underground"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 170), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 68000, perimeter: 1080
            with BuildLine():
                Line((-170, 0), (170, 0))
                Line((-170, -200), (-170, 0))
                Line((170, -200), (-170, -200))
                Line((170, 0), (170, -200))
            make_face()
        # OneSide extrude, distance=-340
        extrude(amount=-340)
    return part.part


# Description: This is an elliptical or oval-shaped structural panel or cover featuring a reinforced framework with internal radial ribs or braces that extend from the center to the perimeter, creating a lightweight yet rigid design.
def model_52358_1bb3de48_0000():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 92.1541293735, perimeter: 34.0300300228
            Circle(5.4160474917)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is an oval or elliptical disk with radial fins or ribs extending from a central hub, resembling a cooling fan or heat dissipation component.
def model_52365_274736ef_0002():
    """Model: piston"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 113.0659196027, perimeter: 38.3274303738
            with BuildLine():
                CenterArc((30, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((30, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a uniform thickness, featuring a clean, simple geometric form with no holes, slots, or curves—just four slanted sides forming a basic quadrilateral prism.
def model_52365_274736ef_0003():
    """Model: table top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 500.027293308, perimeter: 210.0109173232
            with BuildLine():
                Line((-50.0346245527, -5), (49.9708341089, -5))
                Line((49.9708341089, -5), (49.9708341089, 0))
                Line((-50.0346245527, 0), (49.9708341089, 0))
                Line((-50.0346245527, 0), (-50.0346245527, -5))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)
    return part.part


# Description: This is a rectangular duct or plenum box with two pyramidal inlet ports on top, designed for air distribution or ventilation systems, featuring a main chamber with angled transition sections and side flanges.
def model_52449_3da8c6e5_0000():
    """Model: Mesa trabajo alumnos v2"""
    with BuildPart() as part:
        # Sketch1 -> ancho de la mesa (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4600, perimeter: 570
            with BuildLine():
                Line((-20, -55), (-20, 0))
                Line((-80, -55), (-20, -55))
                Line((-80, 0), (-80, -55))
                Line((-100, 0), (-80, 0))
                Line((-100, -55), (-100, 0))
                Line((-160, -55), (-100, -55))
                Line((-160, -70), (-160, -55))
                Line((0, -70), (-160, -70))
                Line((0, 0), (0, -70))
                Line((-20, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a rectangular cylindrical housing or enclosure with a rounded top surface, featuring vertical slots or ribs on the upper face and corner flanges at each end for mounting or structural support.
def model_52557_e6a00b06_0006():
    """Model: filter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 44.3600885142, perimeter: 33.9681408993
            with BuildLine():
                CenterArc((-37.7, 0.85), 0.5, -90, 90)
                Line((-37.2, 0.85), (-37.2, 4.15))
                CenterArc((-37.7, 4.15), 0.5, 0, 90)
                Line((-37.7, 4.65), (-47.3, 4.65))
                CenterArc((-47.3, 4.15), 0.5, 90, 90)
                Line((-47.8, 4.15), (-47.8, 0.85))
                CenterArc((-47.3, 0.85), 0.5, 180, 90)
                Line((-47.3, 0.35), (-37.7, 0.35))
            make_face()
            with BuildLine():
                CenterArc((-46.5, 2.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-38.5, 2.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8)
    return part.part


# Description: This is a toroidal or doughnut-shaped magnetic core with a central rectangular slot and two symmetrical circular openings on opposite sides, featuring a smooth curved outer surface and a densely meshed geometric pattern typical of electromagnetic or magnetic component designs.
def model_52557_e6a00b06_0008():
    """Model: circlet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6964600329, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((20, 1), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((20, 1), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a flat, elongated rectangular bar or strip with a tapered wedge shape, featuring subtle surface detail lines running along its length and appearing to be made of a dark material, likely a metal or composite sleeve, shim, or mounting bracket.
def model_52557_e6a00b06_0011():
    """Model: handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((83, 0), (83, 1))
                Line((83, 1), (77, 1))
                Line((77, 1), (77, 0))
                Line((77, 0), (83, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a curved duct or pipe elbow component with a 90-degree bend, featuring a rounded rectangular cross-section, smooth transitions, and internal flow passages shown in blue mesh, designed to redirect fluid or air flow directionally.
def model_52557_e6a00b06_0012():
    """Model: hook"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3285305684, perimeter: 7.0672810876
            with BuildLine():
                Line((91.0951164684, 0.1072341351), (91.023515287, 0.1770668416))
                CenterArc((91.200001359, 0), 0.25, 134.9058822038, 279.0396776507)
                CenterArc((90.6008940516, -1.1060240206), 1.5060242916, 60.2968054128, 59.7403101047)
                CenterArc((90, 0), 0.25, 127.7234824125, 273.8694097773)
                Line((90.1248534449, 0.0831361371), (90.186970112, 0.1659583599))
                CenterArc((90, 0), 0.15, 104.9543246425, 288.7041221042)
                CenterArc((90.6006043331, -0.9615039867), 1.2778470024, 59.9229731658, 60.0971262084)
                CenterArc((91.200001359, 0), 0.15, 134.3654680903, 299.7663976345)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a pair of parallel elongated channel or rail sections with tapered ends, featuring internal ribbing or structural supports along their length for reinforcement.
def model_52558_c0e0653f_0002():
    """Model: leg1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4514739581, perimeter: 8.3142568697
            with BuildLine():
                Line((0.2500000037, -0.072), (-0.2500000037, -0.072))
                Line((0.2500000037, -0.072), (0.2500000037, 0))
                Line((0.2500000037, 0), (0.5000000075, 0))
                Line((0.7, 1.8000000268), (0.5000000075, 0))
                Line((0.7, 1.8000000268), (0.3768858629, 1.8000000268))
                Line((0.2435525346, 0.6000000089), (0.3768858629, 1.8000000268))
                Line((-0.2435525346, 0.6000000089), (0.2435525346, 0.6000000089))
                Line((-0.2435525346, 0.6000000089), (-0.3768858629, 1.8000000268))
                Line((-0.7, 1.8000000268), (-0.3768858629, 1.8000000268))
                Line((-0.7, 1.8000000268), (-0.5000000075, 0))
                Line((-0.2500000037, 0), (-0.5000000075, 0))
                Line((-0.2500000037, -0.072), (-0.2500000037, 0))
            make_face()
        # Symmetric extrude, each_side=0.072
        extrude(amount=0.072, both=True)
    return part.part


# Description: This is a flat cylindrical disk featuring a smooth face on one side and a series of parallel radial ribs or fins extending across the opposite curved surface, resembling a heat sink or cooling component.
def model_52576_6a9d504d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.0618344098, perimeter: 16.650441064
            Circle(2.65)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4)
    return part.part


# Description: This is a pentahedron or wedge-shaped solid with a rectangular prism base and a triangular wedge section, featuring flat faces and sharp edges with no holes, slots, or curved surfaces.
def model_52771_3d59c5f9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 40, perimeter: 26
            with BuildLine():
                Line((4, -2.5), (-1, -2.5))
                Line((4, 5.5), (4, -2.5))
                Line((-1, 5.5), (4, 5.5))
                Line((-1, -2.5), (-1, 5.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a parallelogram-shaped flat plate with internal cross-bracing, featuring a skewed rectangular form with diagonal and horizontal reinforcing ribs running across its surface for structural support.
def model_52772_a6e6e320_0001():
    """Model: top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 26 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.9309670845, 1.1841875692), x_dir=(1, 0, 0), z_dir=(0, 0.9271838546, 0.3746065934))):
            # Profile area: 2.8667601896, perimeter: 10.2991659514
            with BuildLine():
                Line((-27.635, 18.8442191455), (-27.635, 14.3296361698))
                Line((-27.635, 14.3296361698), (-27, 14.3296361698))
                Line((-27, 14.3296361698), (-27, 18.8442191455))
                Line((-27.635, 18.8442191455), (-27, 18.8442191455))
            make_face()
            # Profile area: 8.0116663805, perimeter: 21.6291659514
            with BuildLine():
                Line((-28.435, 4.3150531941), (-28.435, 14.3296361698))
                Line((-27.635, 4.3150531941), (-28.435, 4.3150531941))
                Line((-27.635, 7.3150531941), (-27.635, 4.3150531941))
                Line((-27.635, 7.3150531941), (-27.635, 9.8150531941))
                Line((-27.635, 14.3296361698), (-27.635, 9.8150531941))
                Line((-28.435, 14.3296361698), (-27.635, 14.3296361698))
            make_face()
            # Profile area: 2.8667601896, perimeter: 10.2991659514
            with BuildLine():
                Line((-27.635, 14.3296361698), (-27.635, 9.8150531941))
                Line((-27.635, 9.8150531941), (-27, 9.8150531941))
                Line((-27, 9.8150531941), (-27, 14.3296361698))
                Line((-27.635, 14.3296361698), (-27, 14.3296361698))
            make_face()
            # Profile area: 135.1968701717, perimeter: 47.0291659514
            with BuildLine():
                Line((-27, 9.8150531941), (-27, 14.3296361698))
                Line((-27, 9.8150531941), (-27, 7.3150531941))
                Line((-27, 4.3150531941), (-27, 7.3150531941))
                Line((-13.5, 4.3150531941), (-27, 4.3150531941))
                Line((-13.5, 14.3296361698), (-13.5, 4.3150531941))
                Line((-27, 14.3296361698), (-13.5, 14.3296361698))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((-27, 4.3150531941), (-27, 7.3150531941))
                Line((-27, 7.3150531941), (-27.635, 7.3150531941))
                Line((-27.635, 7.3150531941), (-27.635, 4.3150531941))
                Line((-27, 4.3150531941), (-27.635, 4.3150531941))
            make_face()
            # Profile area: 135.1968701717, perimeter: 47.0291659514
            with BuildLine():
                Line((-13.5, 14.3296361698), (0, 14.3296361698))
                Line((0, 18.8442191455), (0, 14.3296361698))
                Line((0, 18.8442191455), (0, 21.3442191455))
                Line((0, 24.3442191455), (0, 21.3442191455))
                Line((-13.5, 24.3442191455), (0, 24.3442191455))
                Line((-13.5, 24.3442191455), (-13.5, 14.3296361698))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((0, 24.3442191455), (0, 21.3442191455))
                Line((0, 21.3442191455), (0.635, 21.3442191455))
                Line((0.635, 21.3442191455), (0.635, 24.3442191455))
                Line((0, 24.3442191455), (0.635, 24.3442191455))
            make_face()
            # Profile area: 8.0116663805, perimeter: 21.6291659514
            with BuildLine():
                Line((0.635, 21.3442191455), (0.635, 24.3442191455))
                Line((0.635, 21.3442191455), (0.635, 18.8442191455))
                Line((0.635, 14.3296361698), (0.635, 18.8442191455))
                Line((0.635, 14.3296361698), (1.435, 14.3296361698))
                Line((1.435, 24.3442191455), (1.435, 14.3296361698))
                Line((0.635, 24.3442191455), (1.435, 24.3442191455))
            make_face()
            # Profile area: 2.8667601896, perimeter: 10.2991659514
            with BuildLine():
                Line((0, 14.3296361698), (0.635, 14.3296361698))
                Line((0.635, 14.3296361698), (0.635, 18.8442191455))
                Line((0.635, 18.8442191455), (0, 18.8442191455))
                Line((0, 18.8442191455), (0, 14.3296361698))
            make_face()
            # Profile area: 135.1968701717, perimeter: 47.0291659514
            with BuildLine():
                Line((-13.5, 14.3296361698), (-13.5, 4.3150531941))
                Line((0, 4.3150531941), (-13.5, 4.3150531941))
                Line((0, 7.3150531941), (0, 4.3150531941))
                Line((0, 9.8150531941), (0, 7.3150531941))
                Line((0, 14.3296361698), (0, 9.8150531941))
                Line((-13.5, 14.3296361698), (0, 14.3296361698))
            make_face()
            # Profile area: 2.8667601896, perimeter: 10.2991659514
            with BuildLine():
                Line((0, 14.3296361698), (0, 9.8150531941))
                Line((0.635, 9.8150531941), (0, 9.8150531941))
                Line((0.635, 9.8150531941), (0.635, 14.3296361698))
                Line((0, 14.3296361698), (0.635, 14.3296361698))
            make_face()
            # Profile area: 8.0116663805, perimeter: 21.6291659514
            with BuildLine():
                Line((0.635, 14.3296361698), (1.435, 14.3296361698))
                Line((0.635, 9.8150531941), (0.635, 14.3296361698))
                Line((0.635, 7.3150531941), (0.635, 9.8150531941))
                Line((0.635, 4.3150531941), (0.635, 7.3150531941))
                Line((1.435, 4.3150531941), (0.635, 4.3150531941))
                Line((1.435, 14.3296361698), (1.435, 4.3150531941))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((0.635, 4.3150531941), (0.635, 7.3150531941))
                Line((0, 7.3150531941), (0.635, 7.3150531941))
                Line((0, 7.3150531941), (0, 4.3150531941))
                Line((0.635, 4.3150531941), (0, 4.3150531941))
            make_face()
            # Profile area: 8.0116663805, perimeter: 21.6291659514
            with BuildLine():
                Line((-27.635, 24.3442191455), (-27.635, 21.3442191455))
                Line((-28.435, 24.3442191455), (-27.635, 24.3442191455))
                Line((-28.435, 14.3296361698), (-28.435, 24.3442191455))
                Line((-28.435, 14.3296361698), (-27.635, 14.3296361698))
                Line((-27.635, 18.8442191455), (-27.635, 14.3296361698))
                Line((-27.635, 21.3442191455), (-27.635, 18.8442191455))
            make_face()
            # Profile area: 135.1968701717, perimeter: 47.0291659514
            with BuildLine():
                Line((-27, 18.8442191455), (-27, 21.3442191455))
                Line((-27, 14.3296361698), (-27, 18.8442191455))
                Line((-27, 14.3296361698), (-13.5, 14.3296361698))
                Line((-13.5, 24.3442191455), (-13.5, 14.3296361698))
                Line((-27, 24.3442191455), (-13.5, 24.3442191455))
                Line((-27, 21.3442191455), (-27, 24.3442191455))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((-27, 21.3442191455), (-27.635, 21.3442191455))
                Line((-27, 21.3442191455), (-27, 24.3442191455))
                Line((-27.635, 24.3442191455), (-27, 24.3442191455))
                Line((-27.635, 24.3442191455), (-27.635, 21.3442191455))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635)
    return part.part


# Description: This is a hexagonal prism or bar stock with a long, slender cylindrical or prismatic shape, featuring a central longitudinal slot or groove running along its entire length.
def model_52879_de812eb3_0010():
    """Model: parallel key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.56, perimeter: 3
            with BuildLine():
                Line((0.4, -0.35), (0.4, 0.35))
                Line((0.4, 0.35), (-0.4, 0.35))
                Line((-0.4, 0.35), (-0.4, -0.35))
                Line((-0.4, -0.35), (0.4, -0.35))
            make_face()
        # OneSide extrude, distance=5.6
        extrude(amount=5.6)
    return part.part


# Description: This is an oval or elliptical shell structure with a wireframe mesh surface featuring prominent vertical and diagonal ridge lines or reinforcing ribs running across its curved surface, giving it a reinforced, skeletal appearance.
def model_52884_c8150d6e_0002():
    """Model: g2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.5175863288, perimeter: 17.9070781255
            Circle(2.85)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a hollow ellipsoidal or egg-shaped shell with a smooth, curved outer surface and visible mesh pattern indicating it's likely a thin-walled structure, possibly used as an aerodynamic fairing, enclosure, or structural component.
def model_52884_c8150d6e_0005():
    """Model: knob v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


# Description: This is a bent metal duct or channel with an angular L-shaped profile, featuring a hollow tubular construction with angular faceted surfaces and internal ribbing or bracing elements visible through the translucent geometry.
def model_52884_c8150d6e_0006():
    """Model: needle 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6499758145, perimeter: 5.2302489815
            with BuildLine():
                Line((-1.1351683945, 2.6466940034), (-0.8350217193, 2.5812774204))
                Line((-1.0466636056, 2.3696355341), (-1.1351683945, 2.6466940034))
                Line((0, 1.8000000268), (-1.0466636056, 2.3696355341))
                Line((0.9000000134, 1.8000000268), (0, 1.8000000268))
                Line((1.2000000179, 2.0000000298), (0.9000000134, 1.8000000268))
                Line((0.9000000134, 2.1000000313), (1.2000000179, 2.0000000298))
                Line((0, 2.1000000313), (0.9000000134, 2.1000000313))
                Line((-0.8350217193, 2.5812774204), (0, 2.1000000313))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


# Description: This is a curved ducting or air-flow component with an hourglass-pinched shape, featuring open ends, mesh-textured cylindrical sections on the sides, and a smooth curved body designed for channeling or directing flow.
def model_52884_c8150d6e_0010():
    """Model: side aattach v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2930463288, perimeter: 9.1369555922
            with BuildLine():
                CenterArc((2.2180999836, 0.1921000164), 0.3, -90, 90)
                Line((2.5180999836, 0.8000000164), (2.5180999836, 0.1921000164))
                CenterArc((2.2180999836, 0.8000000164), 0.3, 0, 90)
                Line((-0.8000000164, 1.1000000164), (2.2180999836, 1.1000000164))
                CenterArc((-0.8000000164, 0.8000000164), 0.3, 90, 90)
                Line((-1.1000000164, 0.1921000164), (-1.1000000164, 0.8000000164))
                CenterArc((-0.8000000164, 0.1921000164), 0.3, 180, 90)
                Line((2.2180999836, -0.1078999836), (-0.8000000164, -0.1078999836))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a solid curved sidewall and perforated top and bottom surfaces, featuring a slightly tapered or rounded profile.
def model_52884_c8150d6e_0013():
    """Model: nob v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a cylindrical connector or coupling with a hexagonal cross-section, featuring a central longitudinal slot or groove running along its length and ribbed or textured surface details on its outer faces.
def model_52884_c8150d6e_0037():
    """Model: cahin 2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0536114728, perimeter: 3.819961726
            with BuildLine():
                CenterArc((0.2083428935, -0.3539484563), 0.25, -90, 90)
                Line((0.4583428935, -0.3539484563), (0.4583428935, 0.3539484563))
                CenterArc((0.2083428935, 0.3539484563), 0.25, 0, 90)
                Line((0.2083428935, 0.6039484563), (-0.2083428935, 0.6039484563))
                CenterArc((-0.2083428935, 0.3539484563), 0.25, 90, 90)
                Line((-0.4583428935, 0.3539484563), (-0.4583428935, -0.3539484563))
                CenterArc((-0.2083428935, -0.3539484563), 0.25, -180, 90)
                Line((-0.2083428935, -0.6039484563), (0.2083428935, -0.6039484563))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


# Description: This is an elliptical or oval-shaped structural panel with a curved, aerodynamic surface featuring multiple internal radial ribs or reinforcing struts that extend from the center toward the perimeter for structural support.
def model_52886_5743bcf0_0000():
    """Model: glass"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.5175863288, perimeter: 17.9070781255
            with Locations((-14, 0)):
                Circle(2.85)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: These are two dark gray oval washers or spacers with elongated slot holes running lengthwise through their centers, featuring a slightly domed or curved profile.
def model_52886_5743bcf0_0002():
    """Model: hook glass"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1649336143, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((4, -7.5), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4, -7.5), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.7, -7.5)):
                Circle(0.2)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a dark gray, elongated elliptical or oval-shaped plate with gently curved edges and a slightly domed or convex top surface, featuring no visible holes or slots.
def model_52973_475412f8_0000():
    """Model: Cubierta Escritorio"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 90), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3623.4429482432, perimeter: 409.4395102393
            with BuildLine():
                CenterArc((-60, 153.2050807569), 200, -120, 60)
                Line((-160, -20), (40, -20))
            make_face()
            # Profile area: 3623.4429482432, perimeter: 409.4395102393
            with BuildLine():
                Line((40, 20), (-160, 20))
                CenterArc((-60, -153.2050807569), 200, 60, 60)
            make_face()
            # Profile area: 7648.4407848791, perimeter: 564.5579797074
            with BuildLine():
                Line((-160, -20), (40, -20))
                Line((40, -20), (40, 20))
                Line((40, 20), (-160, 20))
                Line((-160, 20), (-160, -20))
            make_face()
            with BuildLine():
                CenterArc((-26.4575131106, 0), 33, -36.7031466772, 73.4062933544)
                CenterArc((26.4575131106, 0), 33, 143.2968533228, 73.4062933544)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 351.5592151209, perimeter: 84.5579797074
            with BuildLine():
                CenterArc((26.4575131106, 0), 33, 143.2968533228, 73.4062933544)
                CenterArc((-26.4575131106, 0), 33, -36.7031466772, 73.4062933544)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a smooth, elongated tubular body and slightly rounded ends, featuring a uniform diameter throughout its length.
def model_52985_475fe7b2_0015():
    """Model: Calf"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.4815179042), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-10, 28.5)):
                Circle(1.25)
        # TwoSides extrude, along=6.5, against=-3.5
        extrude(amount=6.5)
        extrude(sk.sketch, amount=-3.5)
    return part.part


# Description: This is a thin, elongated flat bar or plate with a parallelogram shape, featuring beveled or chamfered edges on the ends and a slightly curved or warped surface, commonly used as a structural support or connector component.
def model_52985_475fe7b2_0019():
    """Model: Board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6000, perimeter: 460
            with BuildLine():
                Line((160, -100), (-40, -100))
                Line((160, -70), (160, -100))
                Line((-40, -70), (160, -70))
                Line((-40, -100), (-40, -70))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a tilted/angled open slot running along its length, featuring a mesh or perforated surface texture on the upper rim.
def model_52987_387431ac_0001():
    """Model: Second step screw cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.045463494, perimeter: 47.4380490692
            with BuildLine():
                CenterArc((0, 0), 4.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a solid base band and an open mesh top section, featuring a slightly tapered, curved form typical of an air or fluid filter component.
def model_52987_387431ac_0002():
    """Model: First step screw spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.5557513161, perimeter: 17.5929188601
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is an elliptical or oval-shaped shell structure with a curved, boat-like profile featuring internal reinforcing ribs that radiate from the center to the outer perimeter, creating a lightweight yet structurally rigid design.
def model_52987_387431ac_0005():
    """Model: Bottom cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 76.9768739946, perimeter: 31.1017672705
            Circle(4.95)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a bicycle helmet shell or aerodynamic fairing with an elongated, streamlined shape featuring ventilation openings, internal ribbed reinforcement structures, and a curved profile designed for wind resistance reduction and airflow management.
def model_52987_387431ac_0007():
    """Model: Upper setting panel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.3488674095, perimeter: 55.0765467219
            with BuildLine():
                Line((-4.5, 0.4188611699), (-4.5, -0.4188611699))
                CenterArc((-3, -0.4188611699), 1.5, -180, 71.5650511771)
                Line((-3.474341649, -1.841886117), (-0.8983245637, -2.7005584788))
                CenterArc((0.6828142663, 2.0428580115), 5, -108.4349488229, 21.4477363271)
                Line((0.9456084319, -2.9502311352), (8.7420470665, -2.5398922597))
                CenterArc((8.7, -1.7409979962), 0.8, -86.9872124958, 86.9872124958)
                Line((9.5, 1.7409979962), (9.5, -1.7409979962))
                CenterArc((8.7, 1.7409979962), 0.8, 0, 86.9872124958)
                Line((8.7420470665, 2.5398922597), (0.9456084319, 2.9502311352))
                CenterArc((0.6828142663, -2.0428580115), 5, 86.9872124958, 21.4477363271)
                Line((-0.8983245637, 2.7005584788), (-3.474341649, 1.841886117))
                CenterArc((-3, 0.4188611699), 1.5, 108.4349488229, 71.5650511771)
            make_face()
            with BuildLine():
                CenterArc((7.5, -1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.5, 1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.1, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a reinforced cylindrical belt or band featuring a continuous loop shape with a solid base material reinforced by a textured mesh or fabric overlay on the outer surface.
def model_52987_387431ac_0009():
    """Model: Second step screw spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.8446882407, perimeter: 43.3539786195
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.435
        extrude(amount=1.435)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a simple geometric form, featuring a uniform thickness and beveled edges that give it a 3D appearance.
def model_53075_6438cc56_0010():
    """Model: small plug"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.56, perimeter: 13.6
            with BuildLine():
                Line((46.7, 3.3), (46.7, 6.7))
                Line((46.7, 6.7), (43.3, 6.7))
                Line((43.3, 6.7), (43.3, 3.3))
                Line((43.3, 3.3), (46.7, 3.3))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical tapered pin or conical dowel with a uniform diameter that gradually decreases toward one end, commonly used for alignment, fastening, or positioning in mechanical assemblies.
def model_53078_b592f2bd_0001():
    """Model: crank"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(68.8500011548, -51.9999999851, 13.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((5, 70)):
                Circle(0.6)
        # OneSide extrude, distance=-28.9
        extrude(amount=-28.9)
    return part.part


# Description: This is a circular flange connector or coupling adapter featuring a large circular disk body with a protruding conical or tapered spout extending from one side, designed for fluid transfer or mechanical connection applications.
def model_53078_b592f2bd_0008():
    """Model: switch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.7075743969, perimeter: 12.4696349993
            with BuildLine():
                CenterArc((-34.7943516087, 26.9222203988), 0.05, 63.357590036, 152.0247881199)
                Line((-34.8351169047, 26.8932688766), (-33.8884699086, 25.5603391364))
                Line((-33.8884699086, 25.5603391364), (-33.9382231409, 25.5010455431))
                Line((-33.7108782014, 25.3102804883), (-33.9382231409, 25.5010455431))
                CenterArc((-32.5, 25), 1.25, 165.6275343876, 311.4714219402)
                Line((-33.0694108643, 26.1127763781), (-33.2780322024, 26.2878304659))
                Line((-33.2780322024, 26.2878304659), (-33.3195990649, 26.2382930082))
                Line((-34.7719305681, 26.966911527), (-33.3195990649, 26.2382930082))
            make_face()
            with BuildLine():
                CenterArc((-32.5, 25), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a flat parallelogram plate or panel with a trapezoidal appearance, featuring small notches or slots along its top and bottom edges, likely designed as a connector or mounting component in an assembly.
def model_53091_ff6e681c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5500, perimeter: 324
            with BuildLine():
                Line((-25, 60), (20, 60))
                Line((-25, 55), (-25, 60))
                Line((-27, 55), (-25, 55))
                Line((-27, 60), (-27, 55))
                Line((-72, 60), (-27, 60))
                Line((-72, 0), (-72, 60))
                Line((-27, 0), (-72, 0))
                Line((-27, 5), (-27, 0))
                Line((-25, 5), (-27, 5))
                Line((-25, 0), (-25, 5))
                Line((20, 0), (-25, 0))
                Line((20, 60), (20, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a gradual conical shape that narrows from one end to the other, commonly used as a drift pin, taper pin, or alignment tool.
def model_53119_aabd4fc1_0024():
    """Model: Axis"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=-210
        extrude(amount=-210)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a trapezoidal appearance, featuring a dark blue-gray color and what appears to be subtle surface details or relief lines across its face.
def model_53182_1ee4339e_0001():
    """Model: Component8"""
    with BuildPart() as part:
        # Tormach 3rd center brace -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4441.7524407606, perimeter: 518.6171090858
            with BuildLine():
                Line((132.661930597, -64.967828667), (157.6774682892, -64.967828667))
                Line((157.6774682892, -42.031628667), (157.6774682892, -64.967828667))
                Line((158.4394682892, -42.031628667), (157.6774682892, -42.031628667))
                Line((158.4394682892, -64.967828667), (158.4394682892, -42.031628667))
                Line((158.4394682892, -64.967828667), (181.429930597, -64.967828667))
                Line((181.429930597, -42.031628667), (181.429930597, -64.967828667))
                Line((182.191930597, -42.031628667), (181.429930597, -42.031628667))
                Line((182.191930597, -64.967828667), (182.191930597, -42.031628667))
                Line((182.191930597, -64.967828667), (205.5585216846, -64.967828667))
                Line((205.5585216846, -42.1078741241), (205.5585216846, -64.967828667))
                Line((206.3205216846, -42.1078741241), (205.5585216846, -42.1078741241))
                Line((206.3205216846, -64.967828667), (206.3205216846, -42.1078741241))
                Line((206.3205216846, -64.967828667), (207.590660597, -64.967828667))
                Line((207.590660597, -64.967828667), (207.590660597, -19.247828667))
                Line((207.590660597, -19.247828667), (108.530660597, -19.247828667))
                Line((108.530660597, -19.247828667), (108.530660597, -64.967828667))
                Line((108.530660597, -64.967828667), (109.7964148938, -64.9678277776))
                Line((109.7964148938, -42.1078277776), (109.7964148938, -64.9678277776))
                Line((110.5584148938, -42.1078277776), (109.7964148938, -42.1078277776))
                Line((110.5584148938, -64.9678277776), (110.5584148938, -42.1078277776))
                Line((110.5584148938, -64.9678277776), (131.899930597, -64.967828667))
                Line((131.899930597, -42.031628667), (131.899930597, -64.967828667))
                Line((132.661930597, -42.031628667), (131.899930597, -42.031628667))
                Line((132.661930597, -64.967828667), (132.661930597, -42.031628667))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a cylindrical filter or strainer component with a solid outer wall and perforated mesh openings at both the top and bottom ends, designed to allow fluid or air flow while blocking larger particles.
def model_53198_6f2c7c22_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3284509096, perimeter: 2.0316091796
            with Locations((-2.7823955514, 0.0228610393)):
                Circle(0.3233406434)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a curved pipe or duct component with a bulbous head at the top and a tapered, flexible body featuring multiple longitudinal ribs or grooves running along its length for structural reinforcement and flexibility.
def model_53216_2857e8ac_0001():
    """Model: handle clamp"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.6040671662, perimeter: 17.0448391857
            with BuildLine():
                CenterArc((-50.0000007451, 0), 2.3000000343, -62.9643082961, 62.9929554364)
                Line((-47.7000009983, 0.0011499699), (-47.7005007477, 2.0001998996))
                CenterArc((-48.5000007227, 2.0000000298), 0.7995, 0.0143235702, 257.5593770943)
                CenterArc((-50.0000007451, 0), 1.8027756646, -54.5406134703, 97.0963260762)
                CenterArc((-48.2000007376, -2.5272943631), 1.3, 125.4593865297, 54.5406134703)
                Line((-49.5000007376, -2.5272943631), (-49.5000007376, -2.7500000432))
                CenterArc((-49.3500007376, -2.7500000432), 0.15, -180, 90)
                Line((-49.3500007376, -2.9000000432), (-49.3499907376, -2.9000000432))
                CenterArc((-49.3500007331, -2.7500000432), 0.1500000003, -89.9961819889, 89.9961819889)
                Line((-49.200000733, -2.7500000432), (-49.2000007331, -2.4494897752))
                CenterArc((-48.7500007331, -2.4494897752), 0.45, 117.0356917039, 62.9643082961)
            make_face()
            with BuildLine():
                CenterArc((-48.4022034645, 1.8886288505), 0.5000000075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a curved plastic or composite bracket component with a serpentine S-shaped profile, featuring multiple rectangular slots and openings arranged vertically along its length, likely designed for mounting, ventilation, or cable management purposes.
def model_53216_2857e8ac_0002():
    """Model: brake"""
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
        # Sketch has 37 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.8036986391, perimeter: 48.7481841051
            with BuildLine():
                CenterArc((8.2228919927, 3.019573357), 0.2, 102.05091172, 67.0013548074)
                Line((7.9819877855, 2.8272754905), (8.0265318257, 3.0575560477))
                CenterArc((17.799996139, 0.9281409583), 10, 169.0522665274, 6.444818227)
                CenterArc((1.6500000246, 2.2000000328), 6.2, -38.8914546366, 34.3885393909)
                CenterArc((2.5840041813, 1.446583657), 5, -57.4140983372, 18.5226437006)
                Line((1.2307182636, -5.3525294923), (5.2768215455, -2.7663410567))
                CenterArc((1.5, -5.7738219637), 0.5, 122.5859016628, 57.4140983372)
                Line((1, -5.7738219637), (1, -5.8426580218))
                CenterArc((1.5, -5.8426580218), 0.5, 180, 93.1497295769)
                _nurbs_edge([(1.5274727336, -6.3419027002), (1.5607196366, -6.3393777538), (1.6260656523, -6.3325381433), (1.7206413046, -6.3169095629), (1.8398484233, -6.2853222948), (1.9774332904, -6.2281130646), (2.1038618541, -6.1538619545), (2.2197239424, -6.0640178891), (2.3260537496, -5.9610841959), (2.4244513434, -5.8488759793), (2.517088842, -5.7319917537), (2.6067353601, -5.6153149799), (2.6967538928, -5.5035141241), (2.7911684779, -5.4005253992), (2.894543116, -5.3090938874), (3.0108956233, -5.2307145555), (3.1426411403, -5.1654959942), (3.2896865173, -5.1120986762), (3.4480444747, -5.0675114042), (3.6101290815, -5.0273413542), (3.7671380048, -4.9867287324), (3.9109740887, -4.9411291514), (4.0361941192, -4.8870890919), (4.1423385452, -4.8231734461), (4.2348978825, -4.7503737091), (4.3220766776, -4.6709292864), (4.4124170551, -4.5874706844), (4.5118910033, -4.5019717329), (4.6217833099, -4.4149770393), (4.7403732266, -4.3261258705), (4.8642177612, -4.2345401769), (4.9894965826, -4.1392367658), (5.1135215767, -4.0395888531), (5.2355221565, -3.9355637435), (5.3559598059, -3.8275034911), (5.4761687858, -3.7160071945), (5.597869651, -3.6017738332), (5.7227410745, -3.4854633812), (5.8519625143, -3.3675488368), (5.9863025322, -3.2483473295), (6.1262065538, -3.1280512032), (6.2427479743, -3.0310172235), (6.3327776805, -2.9578089954), (6.3939623606, -2.9088113751), (6.4248459197, -2.8842645313)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((3.4027573318, 1.0990733362), 5, -52.8130470935, 20.6796523968)
                CenterArc((1.6500000246, 2.2000000328), 7.0698303721, -32.1333946966, 37.1171172653)
                CenterArc((8.2448035876, 2.7750827397), 0.45, 4.9837225687, 83.0879997694)
                CenterArc((8.2750871848, 2.7750827397), 0.45, 91.9282776619, 10.122634058)
            make_face()
            with BuildLine():
                _nurbs_edge([(1.6430168079, -5.279580154), (1.6602905815, -5.2715515065), (1.6957220532, -5.2544811138), (1.7493127182, -5.2268059075), (1.8211856853, -5.1860320165), (1.9120662793, -5.1289851654), (2.0058033708, -5.065939194), (2.1029833668, -4.998456384), (2.2050687148, -4.9277278095), (2.3131672804, -4.8550334918), (2.4276948109, -4.7816293871), (2.5479610131, -4.7086296601), (2.6719625688, -4.6369244677), (2.7968975539, -4.5672215493), (2.9195322926, -4.500062957), (3.0366314555, -4.4358459993), (3.1453237613, -4.374838879), (3.2240104691, -4.3286776061), (3.2778827908, -4.2955819824), (3.3114685657, -4.2741872023), (3.3276980791, -4.2636415014), (3.3277559426, -4.2636038999)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1024529989, 0.1024529989, 0.1024529989, 0.1024529989, 0.1024529989, 0.1024529989, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.9001789274, 0.9001789274, 0.9001789274, 0.9001789274, 0.9001789274, 0.9001789274], 5)
                CenterArc((3.6000000536, -4.5000000671), 0.3605551329, 111.8910420458, 27.1403831909)
                CenterArc((3.6000000536, -4.5000000671), 0.3605551329, -70.7359980219, 182.6270400678)
                CenterArc((3.6000000536, -4.5000000671), 0.3605551329, -77.7656572511, 7.0296592291)
                _nurbs_edge([(3.6764055139, -4.8523666511), (3.6666843277, -4.8551346527), (3.6391530264, -4.8630187035), (3.5950238475, -4.8758697273), (3.536510161, -4.8934185265), (3.4667050041, -4.9153257942), (3.3956413462, -4.9389700596), (3.3290051584, -4.9626315183), (3.2642654694, -4.9871963653), (3.1977055481, -5.0139599167), (3.1255328163, -5.0443162339), (3.0448942111, -5.0794787845), (2.9547938676, -5.1202208648), (2.8574222603, -5.1665180628), (2.7579390643, -5.2175586647), (2.6627567086, -5.2721098305), (2.5782842131, -5.3287735237), (2.5094212662, -5.3862944206), (2.4582927872, -5.4438188887), (2.4224598147, -5.5012456291), (2.395974893, -5.5590787728), (2.3713245707, -5.6181280008), (2.3409184936, -5.679282854), (2.2990770613, -5.7432106361), (2.2422826295, -5.8103111309), (2.1685178543, -5.880805058), (2.095228018, -5.9399837619), (2.0321383854, -5.9859384763), (1.9864784782, -6.017271168), (1.9627484667, -6.0331115707)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0185018086, 0.0185018086, 0.0185018086, 0.0185018086, 0.0185018086, 0.0185018086, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((1.7000000253, -5.7000000849), 0.424264075, 125.0155816921, 183.2497454233)
                CenterArc((1.7000000253, -5.7000000849), 0.424264075, 97.7187646213, 27.2968170708)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((5.2336825012, -3.3315482625), 0.9725960548, 0.2366861811, 0, 360, -143.5614516638)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((7.1768606217, -1.4248662665), 1.1331197284, 0.2223393419, 0, 360, -125.1824866817)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((8.1759424973, 1.0700945834), 1.2377155272, 0.2384661319, 0, 360, -101.4087375766)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.2750871848, 2.7750827397), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a cylindrical form, featuring smoothly curved ends and a uniform diameter throughout its length.
def model_53216_2857e8ac_0006():
    """Model: stere"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2566370614, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-50, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-50, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is an elongated rectangular duct or channel with a curved/bent profile, featuring a hollow interior cavity and reinforcing ribs or internal structure along its length.
def model_53221_74fa81cd_0007():
    """Model: Pusch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4643.3453863804, perimeter: 361.3791822958
            with BuildLine():
                Line((359.7630678306, 24.8681232059), (335, 24.8681232059))
                Line((335, 24.8681232059), (335, -90))
                Line((335, -90), (410, -100))
                Line((410, -100), (410, -86.0916639386))
                Line((410, -86.0916639386), (359.7630678306, -37.2226190652))
                Line((359.7630678306, -37.2226190652), (359.7630678306, 24.8681232059))
            make_face()
        # Symmetric extrude, each_side=180
        extrude(amount=180, both=True)
    return part.part


# Description: This is a cylindrical sleeve or tube with an open top and a slightly tapered or curved upper edge, featuring a smooth curved sidewall and a flat or recessed bottom surface.
def model_53222_e9c623af_0004():
    """Model: pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


# Description: This is a cylindrical container or vessel with an open top, featuring a slightly tapered or curved wall profile and a flat or slightly domed bottom surface.
def model_53222_e9c623af_0005():
    """Model: crank pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a long, narrow structural beam or rail with a rectangular cross-section, featuring a hollow channel design and small flanged or reinforced ends on both sides.
def model_53233_8dbca22c_0002():
    """Model: Curved Whiteboard Frame Top v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1237.2720139687, perimeter: 263.335450619
            with BuildLine():
                CenterArc((0, 0), 60.96, 175.2198081528, 9.5603836944)
                Line((60.747964575, -5.08), (-60.747964575, -5.08))
                CenterArc((0, 0), 60.96, -4.7801918472, 9.5603836944)
                Line((-60.747964575, 5.08), (60.747964575, 5.08))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a flat, dark gray parallelogram or skewed rectangular plate with no holes, slots, or other features—a simple planar geometric shape.
def model_53233_8dbca22c_0014():
    """Model: Whiteboard Wall v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7116.3341544, perimeter: 360.46664
            with BuildLine():
                Line((-121.81332, 58.42), (0, 58.42))
                Line((-121.81332, 0), (-121.81332, 58.42))
                Line((0, 0), (-121.81332, 0))
                Line((0, 58.42), (0, 0))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a long, slender cylindrical rod or tube with a uniform diameter, slightly tapered at the top end, featuring a smooth exterior surface and appears to be made of a dark material.
def model_53233_8dbca22c_0026():
    """Model: Vertical Trim with Finished Edge v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6761879242, perimeter: 10.3242583224
            with BuildLine():
                Line((58.207964575, 5.08), (58.207964575, 2.54))
                Line((58.207964575, 2.54), (60.9070603461, 2.54))
                CenterArc((0, 0), 60.96, 2.3880154633, 2.3921763839)
                Line((58.207964575, 5.08), (60.747964575, 5.08))
            make_face()
        # OneSide extrude, distance=55.88
        extrude(amount=55.88)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends featuring two conical/tapered holes or recesses at each end and a central longitudinal slot or channel running along its length.
def model_53459_ce174d0e_0002():
    """Model: Handle Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-4.6793136539, 3.7174012589)):
                Circle(0.5)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a gradual conical shape that decreases in diameter from one end to the other, commonly used as a drift pin, taper pin, or alignment tool.
def model_53459_ce174d0e_0010():
    """Model: Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((12.436535915, 5.7225962773)):
                Circle(2.5)
        # OneSide extrude, distance=100
        extrude(amount=100)
    return part.part


# Description: This is a cylindrical bushing or sleeve with a hollow center bore and rounded edges, featuring a thick-walled tubular structure with a symmetrical, compact design.
def model_53470_39f2e9dc_0008():
    """Model: fan"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((150, 25), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((150, 25), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a solid dark body and an open mesh top, designed for filtering, straining, or ventilation applications.
def model_53590_a324861b_0000():
    """Model: Front Wheel  Attachment"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((-6.5, -0.5)):
                Circle(0.95)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a skylight or roof window frame with a parallelogram shape, featuring a black structural frame (flanges) surrounding a blue translucent glass or polycarbonate panel, and internal support cables or bracing for structural stability.
def model_53620_99bef654_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 44 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.1865010537, perimeter: 27.7130964915
            with BuildLine():
                CenterArc((-1.89, -2.525), 0.65, -180, 90)
                Line((-1.89, -3.175), (1.89, -3.175))
                CenterArc((1.89, -2.525), 0.65, -90, 90)
                Line((2.54, -2.525), (2.54, 2.525))
                CenterArc((1.89, 2.525), 0.65, 0, 90)
                Line((1.89, 3.175), (-1.89, 3.175))
                CenterArc((-1.89, 2.525), 0.65, 90, 90)
                Line((-2.54, 2.525), (-2.54, -2.525))
            make_face()
            with BuildLine():
                CenterArc((-1.905, 2.54), 0.2375, -90, 90)
                CenterArc((-1.905, 2.54), 0.2375, 0, 270)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.905, 2.54), 0.2375, -90, 270)
                CenterArc((1.905, 2.54), 0.2375, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.905, -2.54), 0.2375, 90, 90)
                CenterArc((1.905, -2.54), 0.2375, 180, 270)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.905, -2.54), 0.2375, 0, 90)
                CenterArc((-1.905, -2.54), 0.2375, 90, 270)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a simple geometric form, featuring clean faces and edges with no holes, slots, or other features—appearing to be a basic structural or mounting component.
def model_53627_7b1adb8e_0000():
    """Model: Component35"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.05), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.035, perimeter: 0.75
            with BuildLine():
                Line((-0.0875, 0.1), (0.0875, 0.1))
                Line((-0.0875, -0.1), (-0.0875, 0.1))
                Line((0.0875, -0.1), (-0.0875, -0.1))
                Line((0.0875, 0.1), (0.0875, -0.1))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


# Description: This is a blue anodized aluminum structural bracket or connector with a complex geometric shape featuring multiple angular faces, internal ribbing, and cutout windows or slots for weight reduction and fastening.
def model_53724_20b71853_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6157.496475383, perimeter: 1214.8197085653
            with BuildLine():
                Line((-1.6771948236, 4.3836143984), (4.6677114522, -4.8853828213))
                Line((4.6677114522, -4.8853828213), (154.4965737552, -4.8853828213))
                CenterArc((152.7003992628, 41.0685275476), 45.989, -87.7616517003, 175.5515286632)
                Line((150.9268629758, 87.0233171787), (154.4739355499, 87.0233171787))
                Line((46.2882909733, 87.0233171787), (150.9268629758, 87.0233171787))
                Line((-1.6771948236, 4.3836143984), (46.2882909733, 87.0233171787))
            make_face()
            with BuildLine():
                Line((65.493288487, 77.0233171787), (106.7898575219, 5.1146171787))
                Line((65.493288487, 77.0233171787), (106.7898575219, 77.0233171787))
                Line((106.7898575219, 43.7537236393), (106.7898575219, 77.0233171787))
                Line((106.7898575219, 38.383331456), (106.7898575219, 43.7537236393))
                Line((106.7898575219, 5.1146171787), (106.7898575219, 38.383331456))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((10.3094609786, 5.1146171787), (52.0464906687, 77.0233171787))
                Line((52.0464906687, 77.0233171787), (55.5929663631, 77.0233171787))
                Line((55.5929663631, 77.0233171787), (96.889535398, 5.1146171787))
                Line((10.3094609786, 5.1146171787), (96.889535398, 5.1146171787))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((116.7898575219, 77.0233171787), (154.2692279926, 77.0233171787))
                CenterArc((152.7003992628, 41.0685275476), 35.989, -87.4696684252, 174.9712450886)
                Line((116.7898575219, 5.1146171787), (154.2892511078, 5.1146171787))
                Line((116.7898575219, 5.1146171787), (116.7898575219, 77.0233171787))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=75
        extrude(amount=75)
    return part.part


# Description: This is a tapered airfoil or wing component with a streamlined, elongated shape that narrows from a wider rounded leading edge to a sharp trailing point, featuring internal ribbing or structural reinforcement elements visible through the semi-transparent surface.
def model_53841_c93c3cd8_0003():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 189 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8134512728, perimeter: 4.9472620393
            with BuildLine():
                CenterArc((0.325698715, 0.4866945668), 0.003, 28.0366073125, 61.9633926875)
                Line((0.325698715, 0.4896945668), (0.2795019905, 0.4896945668))
                CenterArc((0.2795019905, 0.4956945668), 0.006, 180, 90)
                Line((0.2735019905, 0.4956945668), (0.2735019905, 0.5004416489))
                CenterArc((0.2795019905, 0.5004416489), 0.006, 90, 90)
                Line((0.2795019905, 0.5064416489), (0.3259533286, 0.5064416489))
                CenterArc((0.3259533286, 0.5094416489), 0.003, -90, 54.5471631429)
                Line((0.3283971083, 0.507701551), (0.3299999926, 0.5099526292))
                Line((0.3299999926, 0.534999988), (0.3299999926, 0.5099526292))
                Line((0.3299999926, 0.534999988), (0.3283953683, 0.5373014356))
                CenterArc((0.3259344674, 0.5355856365), 0.003, 34.8851316367, 55.1148683633)
                Line((0.3259344674, 0.5385856365), (0.279656221, 0.5385856365))
                CenterArc((0.279656221, 0.5445856365), 0.006, 180, 90)
                Line((0.273656221, 0.5445856365), (0.273656221, 0.5493967614))
                CenterArc((0.279656221, 0.5493967614), 0.006, 90, 90)
                Line((0.279656221, 0.5553967614), (0.3245861059, 0.5553967614))
                CenterArc((0.3245861059, 0.5583967614), 0.003, -90, 48.5906090247)
                Line((0.3268361139, 0.556412457), (0.3299999926, 0.5599999875))
                Line((0.3299999926, 0.624999986), (0.3299999926, 0.5599999875))
                Line((0.3299999926, 0.624999986), (0.3267907797, 0.6278302228))
                CenterArc((0.3248064753, 0.6255802147), 0.003, 48.5906090247, 41.4093909753)
                Line((0.3248064753, 0.6285802147), (0.279000013, 0.6285802147))
                CenterArc((0.279000013, 0.6345802147), 0.006, 180, 90)
                Line((0.273000013, 0.6389999856), (0.273000013, 0.6345802147))
                CenterArc((0.279000013, 0.6389999856), 0.006, 90, 90)
                Line((0.3245118142, 0.6449999856), (0.279000013, 0.6449999856))
                CenterArc((0.3245118142, 0.6479999856), 0.003, -90, 50.9259506094)
                Line((0.3268408101, 0.6461090128), (0.3299999926, 0.6499999855))
                Line((0.3299999926, 0.7169999839), (0.3299999926, 0.6499999855))
                CenterArc((0.3269999926, 0.7169999839), 0.003, 0, 90)
                Line((0.3269999926, 0.7199999839), (-0.2498360793, 0.7199999839))
                CenterArc((-0.2498360793, 0.7169999839), 0.003, 90, 90)
                Line((-0.2528360793, 0.7169999839), (-0.2528360793, 0.6409210892))
                CenterArc((-0.2498360793, 0.6409210892), 0.003, 180, 90)
                Line((-0.2498360793, 0.6379210892), (-0.2092551783, 0.6379210892))
                CenterArc((-0.2092551783, 0.6349210892), 0.003, 0, 90)
                Line((-0.2062551783, 0.6349210892), (-0.2062551783, 0.537999988))
                CenterArc((-0.2092551783, 0.537999988), 0.003, -90, 90)
                Line((-0.2092551783, 0.534999988), (-0.2483156345, 0.534999988))
                CenterArc((-0.2483156345, 0.531999988), 0.003, 90, 90)
                Line((-0.2513156345, 0.531999988), (-0.2513156345, 0.4960641626))
                CenterArc((-0.2483156345, 0.4960641626), 0.003, 180, 90)
                Line((-0.2483156345, 0.4930641626), (-0.2112551783, 0.4930641626))
                CenterArc((-0.2112551783, 0.4880641626), 0.005, 0, 90)
                Line((-0.2062551783, 0.4880641626), (-0.2062551783, 0.4782983796))
                CenterArc((-0.2112551783, 0.4782983796), 0.005, -90, 90)
                Line((-0.2112551783, 0.4732983796), (-0.2722081134, 0.4732983796))
                CenterArc((-0.2722081134, 0.4702983796), 0.003, 90, 48.8140748343)
                Line((-0.2744658435, 0.4722738934), (-0.2764720855, 0.4699810454))
                Line((-0.2764720855, 0.4699810454), (-0.2764720855, 0.4149999907))
                Line((-0.2764720855, 0.4149999907), (-0.2744177266, 0.4132024266))
                CenterArc((-0.2724422127, 0.4154601567), 0.003, -131.1859251657, 41.1859251657)
                Line((-0.2724422127, 0.4124601567), (-0.2349999949, 0.4124601567))
                CenterArc((-0.2349999949, 0.4074601567), 0.005, 0.7840445298, 89.2159554702)
                CenterArc((-0.2349999949, 0.4075285834), 0.005, -90, 89.9999449337)
                Line((-0.2349999949, 0.4025285834), (-0.2720892064, 0.4025285834))
                CenterArc((-0.2720892064, 0.3995285834), 0.003, 90, 52.5238204386)
                Line((-0.2744700255, 0.401353878), (-0.27674853, 0.3983819156))
                Line((-0.27674853, 0.3983819156), (-0.2751589741, 0.0182853326))
                Line((-0.2751589741, 0.0182853326), (-0.2742750241, 0.0157556408))
                CenterArc((-0.2714429459, 0.0167452535), 0.003, -160.7390587628, 70.978667119)
                Line((-0.2714304001, 0.0137452798), (-0.2324335654, 0.0139083637))
                CenterArc((-0.2324126557, 0.0089084074), 0.005, 0, 90.2396083562)
                Line((-0.2274126557, 0.0089084074), (-0.2274126557, 0.0041455068))
                CenterArc((-0.2324126557, 0.0041455068), 0.005, -89.7603916438, 89.7603916438)
                Line((-0.232391746, -0.0008544495), (-0.2550980817, -0.0009494069))
                CenterArc((-0.2550855359, -0.0039493807), 0.003, 90.2396083562, 48.4794426645)
                Line((-0.2573399865, -0.0019701252), (-0.2600000123, -0.0050000002))
                Line((-0.2600000123, -0.0050000002), (-0.2597646487, -0.0612804488))
                CenterArc((-0.2567646749, -0.061267903), 0.003, -179.7603916438, 55.0080507672)
                Line((-0.2584747659, -0.0637327739), (-0.2487769922, -0.0704609458))
                CenterArc((-0.2470669012, -0.0679960749), 0.003, -124.7523408765, 34.9919492328)
                Line((-0.2470543554, -0.0709960487), (-0.2354045804, -0.0709473295))
                CenterArc((-0.2354171262, -0.0679473558), 0.003, -89.7603916438, 90)
                Line((-0.2324171525, -0.0679348099), (-0.232508583, -0.0460718345))
                CenterArc((-0.2295086092, -0.0460592886), 0.003, 137.3049480217, 42.9346603345)
                Line((-0.2317135287, -0.044025), (-0.2288859243, -0.0409602235))
                CenterArc((-0.2266810048, -0.0429945121), 0.003, 90.2396083562, 47.0653396655)
                Line((-0.2266935506, -0.0399945383), (-0.2131827381, -0.0399380364))
                CenterArc((-0.2131576465, -0.0459379839), 0.006, 0, 90.2396083562)
                Line((-0.2071576465, -0.0459379839), (-0.2071576465, -0.0471746432))
                Line((-0.2071576465, -0.0471746432), (-0.2068409898, -0.1228939673))
                Line((-0.2068409898, -0.1228939673), (-0.2012284706, -0.5036105201))
                Line((-0.2012284706, -0.5036105201), (-0.2040201556, -0.7057063525))
                CenterArc((-0.2010204418, -0.7057477896), 0.003, 179.2085853851, 38.7565140295)
                Line((-0.2033855987, -0.7075933336), (-0.1829008365, -0.733845579))
                CenterArc((-0.1805356797, -0.7320000349), 0.003, -142.0349005854, 52.0349005854)
                Line((-0.1805356797, -0.7350000349), (0.1470000071, -0.7350000349))
                CenterArc((0.1470000071, -0.7320000349), 0.003, -90, 90)
                Line((0.1500000071, -0.7320000349), (0.1500000071, -0.6950005672))
                CenterArc((0.1530000071, -0.6950005672), 0.003, 90, 90)
                Line((0.1780100085, -0.6920005672), (0.1530000071, -0.6920005672))
                CenterArc((0.1780100085, -0.6950005672), 0.003, 0, 90)
                Line((0.1810100085, -0.6950005672), (0.1810100085, -0.7320000349))
                CenterArc((0.1840100085, -0.7320000349), 0.003, 180, 90)
                Line((0.1840100085, -0.7350000349), (0.3075452931, -0.7350000349))
                CenterArc((0.3075452931, -0.7320000349), 0.003, -90, 51.73816006)
                Line((0.3099008601, -0.7338578036), (0.3293555596, -0.7091901212))
                CenterArc((0.3269999926, -0.7073323526), 0.003, -38.26183994, 38.26183994)
                Line((0.3299999926, -0.7073323526), (0.3299999926, 0.3963635566))
                CenterArc((0.3269999926, 0.3963635566), 0.003, 0, 35.0361996399)
                Line((0.3294563611, 0.3980858382), (0.32884123, 0.3989631561))
                CenterArc((0.3263848616, 0.3972408746), 0.003, 35.0361996399, 54.9638003601)
                Line((0.3263848616, 0.4002408746), (0.278000013, 0.4002408746))
                CenterArc((0.278000013, 0.4062408746), 0.006, 180, 90)
                Line((0.272000013, 0.4062408746), (0.272000013, 0.4116849069))
                CenterArc((0.278000013, 0.4116849069), 0.006, 90.000000374, 89.999999626)
                Line((0.278000013, 0.417684992), (0.3262201684, 0.4176998689))
                CenterArc((0.3262192481, 0.4206998687), 0.003, -89.982424277, 40.7771679679)
                Line((0.3281793016, 0.4184287037), (0.3299999926, 0.4199999906))
                Line((0.3299999926, 0.4849999892), (0.3299999926, 0.4199999906))
                Line((0.3299999926, 0.4849999892), (0.3283466573, 0.4881046736))
            make_face()
        # OneSide extrude, distance=0.002
        extrude(amount=0.002)
    return part.part


# Description: This is a shoe sole or insole component with an elongated, curved elliptical shape featuring a textured/mesh upper surface, a smooth underside, and what appears to be a reinforced or translucent panel section in the mid-foot area.
def model_53846_89405f98_0019():
    """Model: złączka v4 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8567124957, perimeter: 7.286339711
            with BuildLine():
                CenterArc((0.0000040405, 0.4017928632), 0.4000009988, -0.1280425883, 180.2560851766)
                Line((-0.3982081492, -0.3990990465), (-0.3999959595, 0.4008989558))
                CenterArc((0.0018080495, -0.398205103), 0.4000171976, -179.8719574117, 179.2271247799)
                Line((0.4000040405, 0.4008989558), (0.4017999137, -0.4027069825))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.105, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0000040405, 0.4517928632), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0000040405, -0.4481725479), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.14
        extrude(amount=0.14)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow tubular body, featuring a mesh or perforated section on the upper portion and a solid lower section, with an open central cavity running through its length.
def model_53846_89405f98_0025():
    """Model: nakrętka v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow central bore, featuring a uniform outer diameter and inner cavity, suitable for use as a spacer, bearing insert, or mechanical connector.
def model_53848_7c64ed9f_0005():
    """Model: Greep (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 64), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 18.8495559215, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-8
        extrude(amount=-8)
    return part.part


# Description: This is a cylindrical housing or barrel-shaped component with rounded ends, featuring a central rectangular slot or opening running along its length and circular holes at both ends, typical of a mechanical assembly or connector body.
def model_53927_ef5208b9_0005():
    """Model: bar short"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((60, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((60, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends and three horizontal slots or grooves cut into its top surface, featuring a symmetrical design with semi-circular end caps.
def model_53927_ef5208b9_0007():
    """Model: bar long"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((62.5, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((62.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5.2
        extrude(amount=-5.2)
    return part.part


# Description: This is a sheet metal bracket or duct component with a trapezoidal profile, featuring angled sides, a curved bottom surface, and multiple bends that create a three-dimensional box-like structure with open ends.
def model_53927_ef5208b9_0010():
    """Model: switch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3035841133, perimeter: 6.2198406026
            with BuildLine():
                Line((-63.7000009492, -0.8000000119), (-61.3000009134, -0.8000000119))
                Line((-61.3000009134, -0.8000000119), (-61.3000009134, -0.5000000075))
                Line((-61.3000009134, -0.5000000075), (-61.4000009149, -0.400000006))
                Line((-61.4000009149, -0.400000006), (-62.5000009313, -0.0500000007))
                Line((-62.5000009313, -0.0500000007), (-63.6000009477, -0.400000006))
                Line((-63.7000009492, -0.5000000075), (-63.6000009477, -0.400000006))
                Line((-63.7000009492, -0.8000000119), (-63.7000009492, -0.5000000075))
            make_face()
            with BuildLine():
                CenterArc((-62.5000009313, -0.200000003), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a toroidal ring or torus characterized by a smooth, symmetrical doughnut shape with a large central circular void and uniform cross-section throughout its circumference.
def model_54177_2b99e039_0003():
    """Model: hoop hitch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.061575216, perimeter: 6.157521601
            with BuildLine():
                CenterArc((-14.5, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-14.5, 0), 0.48, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a rubber-lined metal loop or handle bracket with an elongated oval shape, featuring a textured dark rubber or elastomer coating on the outer surfaces and a smooth metallic inner channel, designed for gripping or securing applications.
def model_54177_2b99e039_0006():
    """Model: ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12, perimeter: 42.8495559215
            with BuildLine():
                CenterArc((5, 29), 2.5, 180, 90)
                Line((5, 26.5), (8, 26.5))
                CenterArc((8, 29), 2.5, -90, 90)
                Line((10.5, 29), (10.5, 31))
                CenterArc((10, 31), 0.5, 0, 90)
                Line((10, 31.5), (3, 31.5))
                CenterArc((3, 31), 0.5, 90, 90)
                Line((2.5, 31), (2.5, 29))
            make_face()
            with BuildLine():
                Line((5.5, 27), (7.5, 27))
                CenterArc((5.5, 29.5), 2.5, 180, 90)
                Line((3, 30.5), (3, 29.5))
                CenterArc((3.5, 30.5), 0.5, 90, 90)
                Line((9.5, 31), (3.5, 31))
                CenterArc((9.5, 30.5), 0.5, 0, 90)
                Line((10, 29.5), (10, 30.5))
                CenterArc((7.5, 29.5), 2.5, -90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: This is a curved metal rod or lever arm with a tapered, chisel-like pointed end at one terminus and a rectangular block or stop at the other end, featuring a slight bend or curve along its length.
def model_54177_2b99e039_0007():
    """Model: beam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.7810874245, perimeter: 21.7278647735
            with BuildLine():
                Line((25, -2.5961574738), (25, -3.1))
                CenterArc((25.6895243624, 15.4739266025), 18.5867208856, -92.1260287654, 10.8252359609)
                Line((30, -2.5), (28.5007127828, -2.8989722691))
                Line((30, -2.5), (35, -2.5))
                Line((35, -2.5), (35, -2.3000000343))
                Line((34.5000005141, -2.3000000343), (35, -2.3000000343))
                Line((34.5000005141, -2.3000000343), (34.5000005141, -2))
                Line((34.5000005141, -2), (30.0085773467, -2))
                Line((30.0085773467, -2), (28.499520882, -2.375432481))
                CenterArc((25.4718721765, 17.7746957371), 20.3763177216, -88.5148000279, 7.0598295287)
                Line((26.0000003874, -2.9000000432), (26.0000003874, -2.5947766292))
                Line((25.5001937344, -2.9000000432), (26.0000003874, -2.9000000432))
                Line((25.5001937344, -2.601602302), (25.5001937344, -2.9000000432))
                CenterArc((25.4718721765, 17.7746957371), 20.3763177216, -91.3269670051, 1.4066038796)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a long, slender rectangular bar or beam with a hexagonal cross-section, featuring a slot or groove running along its top surface and angled end cuts on both ends.
def model_54177_2b99e039_0008():
    """Model: torsion beam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2500000075, perimeter: 2.0000000298
            with BuildLine():
                Line((-5.0000000745, 0.5000000075), (-4.5000000671, 0.5000000075))
                Line((-5.0000000745, 0.5000000075), (-5.0000000745, 0))
                Line((-4.5000000671, 0), (-5.0000000745, 0))
                Line((-4.5000000671, 0.5000000075), (-4.5000000671, 0))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11)
    return part.part


# Description: This is a timing belt with a smooth outer surface and regularly spaced teeth on the inner surface, featuring an oval/elliptical loop shape designed to transmit rotational power between pulleys.
def model_54177_2b99e039_0012():
    """Model: wheel rim small"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, -15), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -15), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a conveyor belt or drive belt featuring an elongated elliptical loop shape with a textured, ribbed surface on the inner edges for grip and traction.
def model_54177_2b99e039_0013():
    """Model: wheel rim large"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 50.8938009882
            with BuildLine():
                CenterArc((0, -35), 4.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -35), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a cylindrical toroidal (doughnut-shaped) component with a central hollow core, featuring a rounded rectangular cross-section and symmetrical design typical of a bearing housing, pulley, or coupling element.
def model_54285_76f37095_0001():
    """Model: Pad3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0942477824, perimeter: 1.8849556202
            with BuildLine():
                CenterArc((-0.3500000052, 0.200000003), 0.200000003, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.3500000052, 0.200000003), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a toroidal (donut-shaped) component featuring a hollow center with a smooth, rounded outer surface and internal mesh pattern, commonly used as a structural ring, bearing surface, or flow conduit in mechanical assemblies.
def model_54285_76f37095_0008():
    """Model: Pad1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with hemispherical end caps, featuring a central longitudinal cavity or channel running through its length.
def model_54285_76f37095_0010():
    """Model: Main_rivet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or washer with a large central oval hole and a textured or mesh-patterned surface finish.
def model_54285_76f37095_0011():
    """Model: Pad05"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0942477824, perimeter: 1.8849556202
            with BuildLine():
                CenterArc((-0.8000000119, 0.6000000089), 0.200000003, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.8000000119, 0.6000000089), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or washer with a circular cross-section, featuring a smooth outer surface and a large central hole, commonly used as a bearing, spacer, or mechanical component.
def model_54374_5c085a74_0002():
    """Model: Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a torus or ring gasket with a circular cross-section, featuring a textured or knurled surface pattern on the outer edges and a smooth inner bore, designed for sealing applications.
def model_54374_5c085a74_0005():
    """Model: Wooden Corps"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.6393797974, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform circular cross-section, featuring slightly rounded or beveled edges at both ends and a subtle surface texture.
def model_54374_5c085a74_0013():
    """Model: Holder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1865320722, perimeter: 2.984513049
            with BuildLine():
                CenterArc((0, 0), 0.3000000045, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a cylindrical bearing or pulley with an oval/elliptical cross-section, featuring a central through-hole and symmetrical curved flanges on both sides that taper toward the center.
def model_54383_13d47b0e_0003():
    """Model: circle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 690.6203707367, perimeter: 109.2477796077
            with BuildLine():
                CenterArc((-100, 50), 15, 0, 360)
            make_face()
            with BuildLine():
                Line((-97.8349364905, 48.75), (-97.8349364905, 51.25))
                Line((-100, 47.5), (-97.8349364905, 48.75))
                Line((-102.1650635095, 48.75), (-100, 47.5))
                Line((-102.1650635095, 51.25), (-102.1650635095, 48.75))
                Line((-100, 52.5), (-102.1650635095, 51.25))
                Line((-97.8349364905, 51.25), (-100, 52.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a simple cylindrical rod or shaft with rounded ends, featuring a smooth, uniform diameter throughout its length with no holes, slots, or flanges.
def model_54383_13d47b0e_0011():
    """Model: support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.0159289474, perimeter: 30.1592894745
            with BuildLine():
                CenterArc((100, 2), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((100, 2), 2.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-50
        extrude(amount=-50)
    return part.part


# Description: This is a cylindrical rod or shaft with a slight taper at one end, featuring a smooth, rounded tip suitable for applications requiring a tapered insertion or connection point.
def model_54384_7ba07a68_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=24.4851
        extrude(amount=24.4851)
    return part.part


# Description: This is a complex sheet metal or cast bracket component featuring two opposing box-like structures with internal ribbing, connected by a central web, with multiple rectangular openings and curved transitions throughout its angular geometry.
def model_54480_e96c0f36_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.7157082647, perimeter: 19.7123889804
            with BuildLine():
                Line((1.5, 0), (2.25, 0))
                Line((2.25, 3.5), (2.25, 0))
                Line((0.75, 3.5), (2.25, 3.5))
                Line((0.75, 2.5), (0.75, 3.5))
                Line((-0.75, 2.5), (0.75, 2.5))
                Line((-0.75, 3.5), (-0.75, 2.5))
                Line((-2.25, 3.5), (-0.75, 3.5))
                Line((-2.25, 0), (-2.25, 3.5))
                Line((-1.5, 0), (-2.25, 0))
                CenterArc((0, 0), 1.5, 0, 180)
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a simple cylindrical/prismatic shape, featuring smoothly rounded ends and a uniform cross-section along its length.
def model_54509_e0930519_0002():
    """Model: BIJAGARI v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5, 5)):
                Circle(0.25)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a rectangular prism or block with a ribbed/finned surface on one face, featuring vertical parallel grooves or corrugations running along its length, and a smooth opposing face, appearing to be a heat sink or structural component with enhanced surface area.
def model_54593_6710154c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 8.926990817
            with BuildLine():
                Line((0, 0), (0, 2.5))
                Line((0, 0), (2.5, 0))
                CenterArc((0, 0), 2.5, 0, 90)
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a curved tubular duct or pipe component with a crescent-shaped cross-section, featuring a reinforced mesh or lattice pattern along the upper surface and rounded end caps on both sides.
def model_54659_e1303e28_0010():
    """Model: Connector 1 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.6695089794, perimeter: 14.0502338313
            with BuildLine():
                CenterArc((4.0000000298, 0.300000003), 0.5, -121.2644609172, 181.19104708)
                CenterArc((2.0000000298, -3.1538723266), 4.491144456, 59.926576745, 60.14684651)
                CenterArc((0.0000000298, 0.300000003), 0.5, 120.0734138372, 181.19104708)
                CenterArc((2.0000000298, -2.9940231379), 3.3536461244, 58.7355390829, 62.5289218343)
            make_face()
            with BuildLine():
                CenterArc((4.0000000298, 0.300000003), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0000000298, 0.300000003), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a horizontal cylindrical rod or shaft with rounded ends and two rectangular slot features or vents positioned symmetrically on the upper surface near each end.
def model_54659_e1303e28_0016():
    """Model: Pin 25mm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a shoe sole or insole component with a curved, elongated hourglass shape featuring a textured surface with mesh patterns and ventilation holes along the top surface for breathability and moisture management.
def model_54659_e1303e28_0023():
    """Model: Connector 2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.0071838581, perimeter: 13.7628416038
            with BuildLine():
                Line((-0.9797958971, 0.5), (-2, 0.5))
                CenterArc((-2, 0), 0.5, 90, 180)
                Line((-0.9797958971, -0.5), (-2, -0.5))
                CenterArc((0, -2.8), 2.5, 66.9260819344, 46.1478361313)
                Line((0.9797958971, -0.5), (2, -0.5))
                CenterArc((2, 0), 0.5, -90, 180)
                Line((0.9797958971, 0.5), (2, 0.5))
                CenterArc((0, 2.8), 2.5, -113.0739180656, 46.1478361313)
            make_face()
            with BuildLine():
                CenterArc((-2, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a cylindrical shaft or rod with rounded ends featuring two sets of rectangular slots or grooves on opposite sides near each end.
def model_54659_e1303e28_0029():
    """Model: Pin 8x40mm v1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is an elliptical disk or plate with a central oval depression or cavity, featuring a smooth curved top surface that tapers toward a recessed central area, and a flat or slightly curved bottom base.
def model_54659_e1303e28_0031():
    """Model: Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.0637157898, perimeter: 15.0796447372
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.31
        extrude(amount=0.31)
    return part.part


# Description: This is a cylindrical container or tube with a rounded top cap and vertical ribbed detailing along its sides, featuring what appears to be a mesh or textured band near the top opening.
def model_54659_e1303e28_0032():
    """Model: Bushing v1 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rounded rectangular bar or spacer with a long, flat prismatic body featuring smoothly rounded ends and edges.
def model_54659_e1303e28_0034():
    """Model: Pin 50mm v3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a dark blue elongated hexagonal or trapezoidal bracket or housing with multiple circular holes along its length, featuring triangular cutouts or slots on the sides and a curved or chamfered top surface.
def model_54659_e1303e28_0037():
    """Model: Control panel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 62.1825229575, perimeter: 62.9911485751
            with BuildLine():
                Line((8, -2.25), (-8, -2.25))
                Line((8, 2.25), (8, -2.25))
                Line((-8, 2.25), (8, 2.25))
                Line((-8, -2.25), (-8, 2.25))
            make_face()
            with BuildLine():
                CenterArc((-6, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is a rounded rectangular bar or spacer with a simple cylindrical or pill-shaped profile, featuring smoothly rounded ends and a uniform cross-section along its length.
def model_54659_e1303e28_0039():
    """Model: Pin 40mm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends and two symmetrical trapezoidal cutouts or slots on the top surface, featuring a dark gray finish with blue accent lines indicating the slot geometry.
def model_54659_e1303e28_0040():
    """Model: Pin 20mm v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a rounded rectangular bar or spacer with a dark gray finish, featuring two sets of parallel horizontal slots or vents positioned symmetrically on opposite ends.
def model_54659_e1303e28_0041():
    """Model: Pin 30mm v1 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a rectangular box or enclosure with a complex polygonal top surface featuring multiple angled facets and internal triangulated geometry, appearing to be a housing or container component with an irregular, non-planar lid design.
def model_54787_92b88ea1_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28, perimeter: 25.6568542495
            with BuildLine():
                Line((7, -1), (6, 0))
                Line((10, -1), (7, -1))
                Line((10, 2), (10, -1))
                Line((7, 2), (10, 2))
                Line((6, 3), (7, 2))
                Line((2, 3), (6, 3))
                Line((0, 1), (2, 3))
                Line((0, 0), (0, 1))
                Line((6, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)
    return part.part


# Description: This is a complex geometric bracket or connector with an angular, fragmented appearance featuring multiple intersecting planar surfaces in dark and light blue tones, composed of interconnected polygonal faces that create an abstract, faceted form with no obvious holes or slots.
def model_54820_a9ecc8b7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.0811368254, perimeter: 47.2575937052
            with BuildLine():
                Line((-4, -2.5), (0, -1.5))
                Line((-0.5, -6.5), (-4, -2.5))
                Line((1.1622736507, -2.1754526985), (-0.5, -6.5))
                Line((3, 1.5), (1.1622736507, -2.1754526985))
                Line((1, 2.5), (3, 1.5))
                Line((4, 3.5), (1, 2.5))
                Line((4, 5.5), (4, 3.5))
                Line((0, 4.5), (4, 5.5))
                Line((-2.5, 2.5), (0, 4.5))
                Line((-5.5, 4), (-2.5, 2.5))
                Line((-5.5, 0), (-5.5, 4))
                Line((0, 0), (-5.5, 0))
                Line((0, -1.5), (0, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a flat parallelogram plate or panel with a simple rectangular shape, featuring beveled edges on its sides to give it a subtle 3D depth appearance.
def model_54979_6bd8ad31_0011():
    """Model: mudflap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -19.9999997567, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 30, perimeter: 62
            with BuildLine():
                Line((22.3621502921, 38.9999961061), (-7.6378497079, 38.9999961061))
                Line((22.3621502921, 39.9999961061), (22.3621502921, 38.9999961061))
                Line((-7.6378497079, 39.9999961061), (22.3621502921, 39.9999961061))
                Line((-7.6378497079, 38.9999961061), (-7.6378497079, 39.9999961061))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a right triangular prism or wedge with a solid, uniform dark blue/gray color, featuring three planar faces meeting at right angles with no holes, slots, or additional features.
def model_54979_6bd8ad31_0012():
    """Model: reflection triangle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 38.9999961061), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 104.7485670797, perimeter: 46.6953852156
            with BuildLine():
                Line((-188.6149048597, 72.5906924886), (-196.8602918657, 59.5268961353))
                Line((-196.8602918657, 59.5268961353), (-180.823825245, 59.5268961353))
                Line((-180.823825245, 59.5268961353), (-188.6149048597, 72.5906924886))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a truck or vehicle body component with an angular, faceted geometric design featuring a boxy upper cabin structure, curved lower base, and multiple planar surfaces with some recessed sections and openings.
def model_55024_4cf14b6f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.404441049, perimeter: 17.147177981
            with BuildLine():
                CenterArc((0.7859349391, -1.605198257), 1.3565466827, 153.5042430501, 55.129992679)
                Line((-2.3562602434, -1), (-0.4281301217, -1))
                Line((-2.3562602434, -0.4375911881), (-2.3562602434, -1))
                Line((-2.3562602434, -0.4375911881), (-6.2833606491, -0.4375911881))
                Line((-6.2833606491, -0.4375911881), (-6.2833606491, 0))
                Line((-6.2833606491, 0), (-6.7097315503, 0))
                Line((-6.7097315503, 0), (-6.7097315503, -2.2552776616))
                Line((-6.7097315503, -2.2552776616), (-5.1613319618, -2.2552776616))
                Line((-5.1613319618, -2.2552776616), (-2.7153094234, -2.2552776616))
                Line((-2.7153094234, -2.2552776616), (-0.4047017267, -2.2552776616))
            make_face()
            # Profile area: 1.7750915937, perimeter: 5.8221945498
            with BuildLine():
                Line((-5.1613319618, -2.2552776616), (-2.7153094234, -2.2552776616))
                CenterArc((-3.9383206926, -1.9747704897), 1.2547672446, -167.0821871561, 154.1643743121)
            make_face()
            # Profile area: 21.6872577709, perimeter: 21.1972711125
            with BuildLine():
                Line((-2.3562602434, 1.8289067604), (-2.3562602434, -0.4375911881))
                Line((-2.3562602434, -0.4375911881), (-2.3562602434, -1))
                Line((-2.3562602434, -1), (-0.4281301217, -1))
                CenterArc((0.7859349391, -1.605198257), 1.3565466827, 153.5042430501, 55.129992679)
                CenterArc((0.7859349391, -1.605198257), 1.3565466827, -151.3657642708, 124.870007321)
                Line((4.2637090119, -2.2103965141), (2, -2.2103965141))
                Line((4.2637090119, 0), (4.2637090119, -2.2103965141))
                Line((2.5, 0), (4.2637090119, 0))
                Line((1.5, 1.8289067604), (2.5, 0))
                Line((-2.3562602434, 1.8289067604), (1.5, 1.8289067604))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a rectangular box or base plate with a sloped or wedge-shaped top surface that features triangulated facets, giving it an angular, geometric appearance with no holes or slots visible.
def model_55027_b152933c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 39, perimeter: 32
            with BuildLine():
                Line((6, 0), (-7, 0))
                Line((6, 3), (6, 0))
                Line((-7, 3), (6, 3))
                Line((-7, 0), (-7, 3))
            make_face()
        # TwoSides extrude (symmetric), distance=5
        extrude(amount=5, both=True)
    return part.part


# Description: This is a welding helmet or protective head gear with an angular, futuristic design featuring a dark gray body, blue-tinted viewing window, curved protective shell, and a hinged or articulated lower section for operational flexibility.
def model_55057_4fbc0f08_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.9995242057, perimeter: 30.8021717165
            with BuildLine():
                CenterArc((10.0645421835, 4.1764979576), 0.9985703792, 123.8032860384, 180)
                Line((6.0182678978, 2.6691350137), (9.5089942701, 5.0062625737))
                CenterArc((5.4619246245, 3.5000875768), 1, -90, 33.8032860384)
                Line((0, 2.5000875768), (5.4619246245, 2.5000875768))
                Line((0, 2.5000437884), (0, 2.5000875768))
                CenterArc((0, 1.2500437884), 1.25, -90, 180)
                Line((0, 0), (0, 0.0000437884))
                Line((5.3175651516, 0), (0, 0))
                CenterArc((5.3175651516, 1), 1, -90, 30.2609504944)
                CenterArc((6.2619074905, 0.860883727), 0.8479583948, 8.7540878674, 229.9559797713)
                Line((10.6200900969, 3.3467333416), (7.099987725, 0.989937824))
            make_face()
            # Profile area: 0.9831090242, perimeter: 3.6449081532
            with BuildLine():
                Line((6.866591802, 0.8336734865), (6.0567026495, 0.2914326869))
                CenterArc((6.2619074905, 0.860883727), 0.6052962199, -2.5765194889, 252.7596110545)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                Line((0, 0.0000437884), (0, 2.5000437884))
                CenterArc((0, 1.2500437884), 1.25, -90, 180)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((0, 1.2500437884), 1.25, 90, 180)
                Line((0, 0.0000437884), (0, 2.5000437884))
            make_face()
            # Profile area: 1.2512276316, perimeter: 4.5888714433
            with BuildLine():
                CenterArc((10.0645421835, 4.1764979576), 0.8925, -56.1967139616, 180)
                Line((9.568005812, 4.9181231202), (10.561078555, 3.434872795))
            make_face()
            # Profile area: 1.2512276316, perimeter: 4.5888714433
            with BuildLine():
                Line((9.568005812, 4.9181231202), (10.561078555, 3.434872795))
                CenterArc((10.0645421835, 4.1764979576), 0.8925, 123.8032860384, 180)
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a dark blue plastic or metal bracket with a parallelogram-like overall shape, featuring a lightning bolt-shaped cutout through its center and flanged edges on the sides.
def model_55058_3a36a12b_0000():
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
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5900979221, perimeter: 5.4205263479
            with BuildLine():
                Line((0.0268466514, 0.1529132483), (0.0268466514, 0.0320000015))
                _nurbs_edge([(0.0268466514, 0.1529132483), (0.0275875145, 0.1577327809), (0.0292531123, 0.1672006053), (0.0323031084, 0.1808886335), (0.0374912517, 0.1980948938), (0.0459721715, 0.217744072), (0.0566262138, 0.2353694061), (0.0696291962, 0.2508071557), (0.0850743106, 0.2639705307), (0.1028615693, 0.2749526504), (0.1228128552, 0.2839193963), (0.1403623724, 0.2896134227), (0.1543611429, 0.2931047807), (0.1640594232, 0.2950917117), (0.169000008, 0.2960000141)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0.2930000139, 0.2938903164), (0.169000008, 0.2960000141))
                Line((0.2930000139, 0.1760937175), (0.2930000139, 0.2938903164))
                Line((0.2009014643, 0.1760937175), (0.2930000139, 0.1760937175))
                _nurbs_edge([(0.2009014643, 0.1760937175), (0.1996723826, 0.1759114504), (0.197250157, 0.1754997392), (0.1937246286, 0.1747406453), (0.1892431183, 0.1734407737), (0.1840313122, 0.1713038557), (0.179244311, 0.1686092766), (0.1749165658, 0.165311811), (0.1710664892, 0.1613872877), (0.1676747045, 0.1568611434), (0.1647064347, 0.1517790315), (0.1626427348, 0.1473051883), (0.1612587202, 0.1437348301), (0.1604076382, 0.141260606), (0.1599999964, 0.1399999969)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0.156621595, 0.0324150279), (0.1599999964, 0.1399999969))
                Line((0.2856017688, 0.0324150279), (0.156621595, 0.0324150279))
                Line((0.2695000072, -0.0949999979), (0.2856017688, 0.0324150279))
                Line((0.1599999964, -0.0949999979), (0.2695000072, -0.0949999979))
                Line((0.1599999964, -0.4250000202), (0.1599999964, -0.0949999979))
                Line((0.379000018, -0.4250000202), (0.1599999964, -0.4250000202))
                _nurbs_edge([(0.379000018, -0.4250000202), (0.3805150276, -0.4248757803), (0.3834932315, -0.4245771614), (0.3878050967, -0.4239788211), (0.3932382069, -0.4228752152), (0.3994669799, -0.4209512946), (0.4050823645, -0.4184338297), (0.4100335267, -0.415273631), (0.4142913109, -0.4114424861), (0.4178813816, -0.4069652295), (0.4208533914, -0.4018899071), (0.4227767441, -0.39739009), (0.4239799252, -0.3937836365), (0.4246774087, -0.3912780821), (0.4249999905, -0.3899999913)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0.4249999905, 0.3849999914), (0.4249999905, -0.3899999913))
                _nurbs_edge([(0.4249999905, 0.3849999914), (0.4248860606, 0.386398993), (0.4245892649, 0.3891462196), (0.4239372687, 0.3931147333), (0.4226474886, 0.3980963897), (0.4202872037, 0.4037724563), (0.4171129921, 0.4088490029), (0.4130599688, 0.4132782366), (0.4080955401, 0.4170361498), (0.4022591071, 0.4201517644), (0.39561786, 0.4226745711), (0.3897145339, 0.4242579939), (0.3849761878, 0.4252165948), (0.3816813919, 0.4257555623), (0.380000018, 0.4260000202)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.3910000186, 0.4260000202), (0.380000018, 0.4260000202))
                _nurbs_edge([(-0.4300000204, 0.3900000185), (-0.4295681506, 0.3912432658), (-0.4286740796, 0.3936841717), (-0.4272419821, 0.397208769), (-0.4251475157, 0.4016301684), (-0.4222001066, 0.4066619335), (-0.4188937018, 0.4111541203), (-0.4151986298, 0.415062132), (-0.4110980142, 0.4183606029), (-0.4066070496, 0.4210723707), (-0.4017548381, 0.4232411768), (-0.3976076023, 0.4245772195), (-0.3943573145, 0.4253690377), (-0.3921293087, 0.4258050108), (-0.3910000186, 0.4260000202)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.4310000205, -0.3890000185), (-0.4300000204, 0.3900000185))
                _nurbs_edge([(-0.4310000205, -0.3890000185), (-0.4305553236, -0.3900381878), (-0.4296330982, -0.3920866927), (-0.4281512677, -0.3950759516), (-0.4259752443, -0.3988918654), (-0.4228988648, -0.403359656), (-0.4194344808, -0.4074985095), (-0.4155507292, -0.4112818373), (-0.4112310389, -0.4146955909), (-0.4064933209, -0.4177549548), (-0.401369392, -0.4204869021), (-0.3969867667, -0.4224321333), (-0.3935504939, -0.423764482), (-0.3911943715, -0.4245973775), (-0.3899999913, -0.4249999905)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0.0268466514, -0.4249999905), (-0.3899999913, -0.4249999905))
                Line((0.0268466514, -0.0960000046), (0.0268466514, -0.4249999905))
                Line((-0.085000004, -0.0960000046), (0.0268466514, -0.0960000046))
                Line((-0.085000004, 0.0320000015), (-0.085000004, -0.0960000046))
                Line((0.0268466514, 0.0320000015), (-0.085000004, 0.0320000015))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a hexahedron-based structural component with an elongated, wedge-like shape featuring multiple angled facets, a central concave underside, and asymmetrical geometry suggesting it may function as a bracket, connector, or aerodynamic component.
def model_55060_980d5147_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32, perimeter: 24
            with BuildLine():
                Line((8, -4), (0, -4))
                Line((8, 0), (8, -4))
                Line((0, 0), (8, 0))
                Line((0, -4), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a polygonal housing or bracket component with a trapezoidal prism overall shape, featuring internal ribbing/reinforcement walls and a central rectangular slot or opening running through its length, designed for structural support and component mounting.
def model_55077_dd176614_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 28.8844648643, perimeter: 33.5776931847
            with BuildLine():
                Line((6.5, 5.5), (6.5, 2.75))
                Line((-0.5, 5.5), (6.5, 5.5))
                Line((-3.5, 0), (-0.5, 5.5))
                Line((6.5, 2.75), (-3.5, 0))
            make_face()
            with BuildLine():
                CenterArc((1.1367624735, 3.2515560481), 1.1445590944, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


# Description: This is a toroidal (donut-shaped) ring with a circular cross-section, featuring a hollow center opening and a textured or patterned surface finish on its outer edges.
def model_55110_ccc772b9_0005():
    """Model: tire"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 44.7676953137, perimeter: 59.6902604182
            with BuildLine():
                CenterArc((38.5, -0.5), 5.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((38.5, -0.5), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)
    return part.part


# Description: This is a curved fender or mud guard with a distinctive arc shape, textured ribbed surface for structural reinforcement, and a solid dark finish, designed to protect wheels or undercarriage components.
def model_55110_ccc772b9_0010():
    """Model: brake"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3213431072, perimeter: 4.490105093
            with BuildLine():
                CenterArc((37.5, -0.5), 7.2956327806, 176.0702019496, 6.659387184)
                Line((30.2126447372, -0.847434805), (30.8238835998, -0.847434805))
                CenterArc((37.5, -0.5), 6.6851507936, 175.7106926704, 7.2683755308)
                Line((30.833573586, 0), (30.2215209233, 0))
            make_face()
            with BuildLine():
                CenterArc((30.5, -0.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.2149457066, perimeter: 38.0279465049
            with BuildLine():
                Line((30.833573586, 0), (30.2215209233, 0))
                CenterArc((37.5, -0.5), 6.6851507936, 26.5684090761, 149.1422835943)
                Line((43.4792054205, 2.4900407477), (44.1547662617, 2.4900407477))
                CenterArc((37.5, -0.5), 7.2956327806, 24.1947722716, 151.8754296779)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or bushing with a circular hollow center, featuring a uniform cross-section and smooth curved geometry throughout.
def model_55114_7bf17f6a_0002():
    """Model: SMALL RIM"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 63.6172512352, perimeter: 84.8230016469
            with BuildLine():
                CenterArc((0, 0), 7.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6, 70, 40)
                CenterArc((0, 0), 6, 110, 320)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a toroidal (ring-shaped) part with a hollow center and a uniform circular cross-section, featuring a smooth curved outer surface with visible mesh geometry typical of CAD models.
def model_55114_7bf17f6a_0004():
    """Model: BIG RIM"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 87.1791961371, perimeter: 116.2389281828
            with BuildLine():
                CenterArc((0, 0), 10, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 8.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is an elongated elliptical or leaf-shaped aerodynamic cover or fairing with a smooth, curved surface featuring multiple longitudinal ribs or stringers running along its length for structural reinforcement.
def model_55199_4d57661f_0000():
    """Model: rubber pad"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 283.5287369865, perimeter: 59.6902604182
            Circle(9.5)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical bearing or bushing component with a rounded rectangular cross-section, featuring a central slot or keyway running along its length and internal geometric divisions suggesting a segmented or multi-part assembly structure.
def model_55212_29e38f0c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.4159265359, perimeter: 19.8691765316
            Circle(3.1622776602)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a right-angle lever or crank arm with a horizontal top arm and a vertically-oriented lower arm connected by zigzag bends, featuring a flat rectangular profile throughout.
def model_55216_d28562a7_0000():
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
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.8509236845, perimeter: 64.4046529516
            with BuildLine():
                Line((-7.5000004704, 10.4999999439), (-5.5000000734, 10.4999999793))
                Line((-5.5000000734, 10.4999999793), (-5.5000000392, 8.5714285329))
                Line((-5.5000000392, 8.5714285329), (-4.5000000145, 8.5714285506))
                Line((-4.5000000145, 8.5714285506), (-4.4999999805, 6.6506528992))
                _nurbs_edge([(-4.4999999805, 6.6506528992), (-4.3906548564, 6.6106026707), (-4.2813097324, 6.5705524422), (-4.1719646084, 6.5305022137), (-3.8171754563, 6.4005523259), (-3.5116297909, 6.2449911786), (-3.2721061107, 6.0693570405), (-3.0064075165, 5.8745297753), (-2.8221729672, 5.65664144), (-2.6798110351, 5.3826457155), (-2.6082226401, 5.2448636986), (-2.548121273, 5.0936424474), (-2.5000009357, 4.9306243328)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [-0.1026713113, -0.1026713113, -0.1026713113, -0.1026713113, 0, 0, 0, 0.3653716485, 0.3653716485, 0.3653716485, 0.7706707539, 0.7706707539, 0.7706707539, 0.9744802415, 0.9744802415, 0.9744802415, 0.9744802415], 3)
                Line((-2.5000009357, 4.9306243328), (-2.5000007594, 0.0000002168))
                Line((-2.5000007594, 0.0000002168), (-1.9999989351, 0.0000002301))
                Line((-1.9999991138, 5.0000021388), (-1.9999989351, 0.0000002301))
                _nurbs_edge([(-3.9999988509, 7.0000024017), (-3.9360987504, 6.9765974742), (-3.8103498913, 6.9283632666), (-3.627880293, 6.8517391301), (-3.3971002586, 6.7408853571), (-3.1309264114, 6.5868332687), (-2.8891632498, 6.4158315807), (-2.6739924317, 6.2263654551), (-2.4869299342, 6.017382271), (-2.3273286292, 5.7893313626), (-2.1933052071, 5.5435204091), (-2.1049669515, 5.3337619526), (-2.0486726266, 5.1695278074), (-2.0154978267, 5.0570146495), (-1.9999991138, 5.0000021388)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.9999988876, 9.0714297596), (-3.9999988509, 7.0000024017))
                Line((-5.0000006184, 9.0714297419), (-3.9999988876, 9.0714297596))
                Line((-5.0000006526, 10.9999999823), (-5.0000006184, 9.0714297419))
                Line((-6.9999999918, 10.9999999469), (-5.0000006526, 10.9999999823))
                Line((-6.9999999918, 10.9999999469), (-6.9999999813, 12.7000000339))
                Line((-6.9999999813, 12.7000000339), (6.9999999427, 12.6999998961))
                Line((6.9999999427, 12.6999998961), (7.4999996651, 12.6999998894))
                Line((7.4999996631, 13.2000004211), (7.4999996651, 12.6999998894))
                Line((-7.5000004537, 13.2000004211), (7.4999996631, 13.2000004211))
                Line((-7.5000004704, 10.4999999439), (-7.5000004537, 13.2000004211))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hydraulic or mechanical actuator arm featuring an elongated cylindrical body with a split-jaw clamping head at the top, a mounting flange at the bottom, and internal articulated joints that allow for angular movement and precise positioning.
def model_55245_473548f5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 21 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 52.8640480896, perimeter: 64.1177790114
            with BuildLine():
                Line((-0.5, -8.3571764006), (-0.5, -11.1961524227))
                Line((-0.5, -11.1961524227), (0.7113248654, -9.0980762114))
                CenterArc((-0.1547005384, -8.5980762114), 1, -30, 60)
                Line((0.7113248654, -8.0980762114), (-0.5, -6))
                Line((-0.5, -6), (-0.5, 4))
                Line((-0.5, 4), (0.5669872981, 5.8480762114))
                CenterArc((-0.7320508076, 6.5980762114), 1.5, -30, 60)
                Line((0.5669872981, 7.3480762114), (-0.5, 9.1961524227))
                Line((-0.5, 9.1961524227), (-0.5, 5.8759498715))
                CenterArc((-1.5, 5.8759498715), 1, -90, 90)
                Line((-2.5, 4.8759498715), (-1.5, 4.8759498715))
                CenterArc((-2.5, 5.8759498715), 1, 180, 90)
                Line((-3.5, 9.1961524227), (-3.5, 5.8759498715))
                Line((-3.5, 9.1961524227), (-4.7113248654, 7.0980762114))
                CenterArc((-3.8452994616, 6.5980762114), 1, 150, 60)
                Line((-4.7113248654, 6.0980762114), (-3.5, 4))
                Line((-3.5, -6), (-3.5, 4))
                Line((-3.5, -6), (-4.7113248654, -8.0980762114))
                CenterArc((-3.8452994616, -8.5980762114), 1, 150, 60)
                Line((-4.7113248654, -9.0980762114), (-3.5, -11.1961524227))
                Line((-3.5, -8.3571764006), (-3.5, -11.1961524227))
                CenterArc((-2.5, -8.3571764006), 1, 90, 90)
                Line((-2.5, -7.3571764006), (-1.5, -7.3571764006))
                CenterArc((-1.5, -8.3571764006), 1, 0, 90)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a tapered nose cone at one end and threaded mounting provisions, featuring a streamlined tubular body designed to reduce firearm noise.
def model_55255_e0101aad_0005():
    """Model: shaft v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a rectangular prism or box-shaped solid block with a elongated, tall rectangular form and beveled or chamfered edges on the top corners.
def model_55323_716f61f1_0001():
    """Model: spigot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2, perimeter: 2.4
            with BuildLine():
                Line((0.0999999985, 1.1000000313), (-0.1000000015, 1.1000000313))
                Line((0.0999999985, 2.1000000313), (0.0999999985, 1.1000000313))
                Line((-0.1000000015, 2.1000000313), (0.0999999985, 2.1000000313))
                Line((-0.1000000015, 1.1000000313), (-0.1000000015, 2.1000000313))
            make_face()
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True)
    return part.part


# Description: This is a cylindrical sleeve or tube with a straight, uniform hollow body and textured or mesh-patterned ends, designed as a simple tubular component.
def model_55351_303fec3a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((4.1000000611, -1.1000000164)):
                Circle(0.5)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a rectangular box-shaped bracket or enclosure with an open or cutout section on one side, featuring a bent or folded flange design that creates an angular, asymmetrical profile.
def model_55391_a3016f11_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 162.5, perimeter: 61.1803398875
            with BuildLine():
                Line((5, 2.5), (-5, 2.5))
                Line((-5, 2.5), (-5, -15))
                Line((-5, -15), (-2.5, -15))
                Line((-2.5, -15), (0, -10))
                Line((0, -10), (2.5, -15))
                Line((2.5, -15), (5, -15))
                Line((5, -15), (5, 2.5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a cylindrical knurled knob or grip wheel with a flat circular face and a textured knurled edge around its circumference for improved grip and handling.
def model_55403_d243028d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: A rectangular prism or box-shaped component with vertical ribbed/grooved detailing on one face and a mesh or perforated section across the top edge.
def model_55419_09442d50_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 44.3490150332, perimeter: 26.8264040089
            with BuildLine():
                Line((0, 0), (7.5, 0))
                CenterArc((0, 0), 7.5, 0, 90.3470715365)
                Line((0, 0), (-0.04543128, 7.4998623987))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a hollow box-like structural component with an irregular trapezoidal profile, featuring internal diagonal bracing/webbing, open sections, and angled surfaces that suggest it functions as a lightweight reinforced frame or chassis element.
def model_55473_64d24a1b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19, perimeter: 24.3245553203
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (5, 0))
                Line((5, 0), (5, 5))
                Line((5, 5), (4, 5))
                Line((4, 5), (3, 2))
                Line((3, 2), (2, 2))
                Line((2, 2), (1, 5))
                Line((1, 5), (0, 5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a dark gray plastic or composite enclosure with a curved, organic pod-like shape featuring a blue interior cavity, two circular openings or ports on the sides, and a streamlined, ergonomic design suitable for a handheld device or electronic component housing.
def model_55519_da060af7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.3149087569, perimeter: 25.2051156414
            with BuildLine():
                CenterArc((7, 2), 2.4149980727, 83.8433449069, 192.3133101862)
                CenterArc((7, 2), 2.4149980727, -83.8433449069, 167.6866898138)
            make_face()
            with BuildLine():
                CenterArc((7, 2), 1.5965206728, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 22.4971104771, perimeter: 39.3335500453
            with BuildLine():
                CenterArc((-5, 2), 3.7020217441, 83.5259253933, 192.9481492133)
                CenterArc((-5, 2), 3.7020217441, -83.5259253933, 167.0518507867)
            make_face()
            with BuildLine():
                CenterArc((-5, 2), 2.5581071749, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 43.1372199506, perimeter: 42.7201334367
            with BuildLine():
                CenterArc((-5, 2), 3.7020217441, -83.5259253933, 167.0518507867)
                Line((-4.5825836198, -1.6784138646), (7.259001874, -0.4010692869))
                CenterArc((7, 2), 2.4149980727, 83.8433449069, 192.3133101862)
                Line((-4.5825836198, 5.6784138646), (7.259001874, 4.4010692869))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a toroidal (donut-shaped) component with a hollow center and a smooth, curved outer surface, featuring a fine mesh or textured pattern on the upper surface, likely designed as a ring-type seal, spacer, or structural support element.
def model_55605_2f8bc12e_0006():
    """Model: Washer M10 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1233405041, perimeter: 10.9955744046
            with BuildLine():
                CenterArc((0, 0), 1.2500000186, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a truncated polyhedron or geodesic dome-like structure with an elongated hexagonal/octagonal base featuring multiple triangular facets, internal ribbing, and a complex faceted surface with both solid and mesh-patterned panels.
def model_55605_2f8bc12e_0056():
    """Model: Nut M10mm v1 (15)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.431626913, perimeter: 8.6841553672
            with BuildLine():
                Line((0.8000000119, -0.4618802222), (0.8000000119, 0.4618802222))
                Line((0.8000000119, 0.4618802222), (0, 0.9237604445))
                Line((0, 0.9237604445), (-0.8000000119, 0.4618802222))
                Line((-0.8000000119, 0.4618802222), (-0.8000000119, -0.4618802222))
                Line((-0.8000000119, -0.4618802222), (0, -0.9237604445))
                Line((0, -0.9237604445), (0.8000000119, -0.4618802222))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical mesh or perforated tube with an open top end and a closed or solid bottom end, featuring a uniform circular cross-section with a textured mesh surface throughout its length.
def model_55611_69142616_0018():
    """Model: pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((15, -67)):
                Circle(0.4)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a curved rubber or foam tube/hose with a smooth, elongated U-shaped bend and rounded ends, commonly used as a protective sleeve, cable guide, or flexible connector in mechanical assemblies.
def model_55625_453e11ac_0004():
    """Model: Ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0000736793, perimeter: 0.1182940504
            with BuildLine():
                CenterArc((-0.0007415631, -0.0007362659), 1.075, 70.5363174849, 1.5654150229)
                CenterArc((0.3992584369, 1.1311083943), 0.125446723, -136.1988425203, 26.7351600052)
                CenterArc((-1.789811624, -0.9682192126), 2.9075722569, 43.2023450299, 0.5988124498)
            make_face()
            # Profile area: 0.0000736793, perimeter: 0.1182940504
            with BuildLine():
                CenterArc((1.7883284979, -0.9682192126), 2.9075722569, 136.1988425203, 0.5988124498)
                CenterArc((-0.4007415631, 1.1311083943), 0.125446723, -70.5363174849, 26.7351600052)
                CenterArc((-0.0007415631, -0.0007362659), 1.075, 107.8982674923, 1.5654150229)
            make_face()
            # Profile area: 0.910978683, perimeter: 13.1956865616
            with BuildLine():
                CenterArc((-0.0007415631, -0.0007362659), 1.075, 107.8982674923, 1.5654150229)
                CenterArc((-0.4007415631, 1.1311083943), 0.125446723, -70.5363174849, 26.7351600052)
                CenterArc((-0.4007415631, 1.1311083943), 0.125446723, -43.8011574797, 178.0696841295)
                CenterArc((0.9426313914, -0.2470106982), 2.0499890396, 134.2685266498, 31.1005267346)
                CenterArc((-0.0007415631, -0.0007362659), 1.075, 165.3690533844, 209.2618932311)
                CenterArc((-0.9441145175, -0.2470106982), 2.0499890396, 14.6309466156, 31.1005267346)
                CenterArc((0.3992584369, 1.1311083943), 0.125446723, 45.7314733502, 178.0696841295)
                CenterArc((0.3992584369, 1.1311083943), 0.125446723, -136.1988425203, 26.7351600052)
                CenterArc((-0.0007415631, -0.0007362659), 1.075, 70.5363174849, 1.5654150229)
                CenterArc((-1.789811624, -0.9682192126), 2.9075722569, 37.2643765115, 5.9379685184)
                CenterArc((0, 0), 0.95, 123.7053566527, 292.8062213767)
                CenterArc((1.7883284979, -0.9682192126), 2.9075722569, 136.7976549701, 5.9872343251)
            make_face()
            with BuildLine():
                CenterArc((0.3992584369, 1.1311083943), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.4007415631, 1.1311083943), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a retaining ring (or snap ring) with an open C-shaped design featuring two protruding ears or tabs on opposite ends for installation and removal, commonly used to secure components on shafts or in grooves.
def model_55625_453e11ac_0010():
    """Model: Ring_2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2790043953, perimeter: 22.3863228644
            with BuildLine():
                CenterArc((-0.9962194881, 1.1208589886), 0.3264466031, 30.5906906551, 57.282117666)
                CenterArc((-0.5, 1.4142135624), 0.25, -149.4093093449, 191.0979645719)
                CenterArc((-0.8022151251, 0.9724637518), 0.780204774, 51.1973321635, 42.9775183202)
                CenterArc((0, 0), 1.95, 116.1370758604, 307.7258482791)
                CenterArc((0.8022151251, 0.9724637518), 0.780204774, 85.8251495163, 28.5828326162)
                CenterArc((0, 0), 1.75, 55.7819256107, 18.3050879202)
                CenterArc((0, 0), 1.75, 124.2180743893, 291.5638512215)
            make_face()
            with BuildLine():
                CenterArc((-0.5, 1.4142135624), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2201290466, perimeter: 2.2294617741
            with BuildLine():
                CenterArc((0.8022151251, 0.9724637518), 0.780204774, 114.4079821324, 14.394685704)
                CenterArc((0.5, 1.4142135624), 0.25, 138.311344773, 191.0979645719)
                CenterArc((0.9962194881, 1.1208589886), 0.3264466031, 92.1271916789, 57.282117666)
                CenterArc((0, 0), 1.75, 55.7819256107, 18.3050879202)
            make_face()
            with BuildLine():
                CenterArc((0.5, 1.4142135624), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a solid base ring and an open mesh top section featuring a central oval or elongated hole, designed for filtering or ventilation applications.
def model_55633_282eaae6_0001():
    """Model: penutup2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0628318531, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a wrist-worn device or sensor band featuring a flexible dark gray elastomeric band with an integrated blue rectangular module or display mounted on top, designed to wrap around the wrist with a smooth curved ergonomic form.
def model_55633_282eaae6_0010():
    """Model: pengatur gas v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1616087185, perimeter: 4.0969270007
            with BuildLine():
                Line((0.0000218084, 0.6000000008), (-0.0499563822, 0.5499999877))
                Line((-0.0499563822, 0.5499999877), (-0.0999782273, 0.6000000008))
                Line((-0.0999782273, 0.6000000008), (-0.0999782273, 0.2828504093))
                CenterArc((0, 0), 0.3, 109.4668101818, 321.0575441466)
                Line((0.1000218441, 0.6000000008), (0.1000218441, 0.2828349885))
                Line((0.0499999989, 0.5499999877), (0.1000218441, 0.6000000008))
                Line((0.0000218084, 0.6000000008), (0.0499999989, 0.5499999877))
            make_face()
            with BuildLine():
                Line((0, 0.2451751461), (-0.0078108169, 0.2373715255))
                Line((0, 0.2451751461), (0.0078033759, 0.2373717703))
                CenterArc((0, 0), 0.2375, 91.8846633965, 356.2324692956)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a slightly conical shape that gradually reduces in diameter from one end to the other, commonly used as a drift pin, taper pin, or alignment tool.
def model_55634_3b61fa4d_0004():
    """Model: bar rudder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((9.5, 11.5)):
                Circle(0.1)
        # OneSide extrude, distance=4.7199
        extrude(amount=4.7199)
    return part.part


# Description: This is a cylindrical rod or shaft with a rounded rectangular cross-section, featuring smooth, rounded ends and a uniform diameter throughout its length.
def model_55634_3b61fa4d_0006():
    """Model: aileron bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-4.5000000671, 4.0000000596)):
                Circle(0.1)
        # OneSide extrude, distance=5.1705
        extrude(amount=5.1705)
    return part.part


# Description: This is a simple rectangular bar or flat plate with a uniform thickness, featuring a long, straight horizontal profile with no holes, slots, or additional features.
def model_55634_3b61fa4d_0009():
    """Model: bar elevator"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-9.5000001416, 4.0000000596)):
                Circle(0.1)
        # OneSide extrude, distance=9.3833
        extrude(amount=9.3833)
    return part.part


# Description: This is a simple tapered cylindrical rod or pin with a gradual diameter reduction from one end to the other, featuring a smooth conical shape.
def model_55707_c78416ed_0010():
    """Model: Horizontal Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=41.91
        extrude(amount=41.91)
    return part.part


# Description: This is a straight cylindrical rod or shaft with a uniform diameter, featuring a simple linear form that tapers slightly at the ends.
def model_55707_c78416ed_0011():
    """Model: Lead Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=57.9374
        extrude(amount=57.9374)
    return part.part


# Description: This is a long, slender hexagonal or prismatic shaft/bar with a tapered or beveled pointed end, featuring a smooth cylindrical or grooved central channel running along its length.
def model_55707_c78416ed_0018():
    """Model: Cherry 2x4 21 inch v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.8709, perimeter: 25.4
            with BuildLine():
                Line((0, 3.81), (0, 0))
                Line((0, 0), (8.89, 0))
                Line((8.89, 0), (8.89, 3.81))
                Line((8.89, 3.81), (0, 3.81))
            make_face()
        # OneSide extrude, distance=53.34
        extrude(amount=53.34)
    return part.part


# Description: This is a long, slender hexagonal or prismatic bar with a tapered pointed end on one side and a flat end on the other, featuring a grooved or channeled surface running along its length.
def model_55707_c78416ed_0019():
    """Model: Cherry 2x4 24 inch v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.8709, perimeter: 25.4
            with BuildLine():
                Line((0, 3.81), (0, 0))
                Line((0, 0), (8.89, 0))
                Line((8.89, 0), (8.89, 3.81))
                Line((8.89, 3.81), (0, 3.81))
            make_face()
        # OneSide extrude, distance=60.96
        extrude(amount=60.96)
    return part.part


# Description: This is a trapezoidal or wedge-shaped structural component with an open framework design featuring internal ribs and reinforcement members, characterized by angled sides, a flat base, and multiple parallel bracing elements visible through its semi-transparent mesh surfaces.
def model_55707_c78416ed_0022():
    """Model: Motor Mount Support Plate v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.1867477314, perimeter: 36.7976537923
            with BuildLine():
                Line((5.0800001621, -5.08), (0, -5.08))
                Line((5.0800001621, 0), (5.0800001621, -5.08))
                Line((0, 0), (5.0800001621, 0))
                Line((0, -5.08), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((2.5400000811, -2.9464), 0.9525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.635, -4.445), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.4450001621, -4.445), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.4450001621, -0.9525), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.635, -0.9525), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9525, -2.9464), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a long, slender hexagonal or prismatic bar with a tapered wedge-shaped end on one side, featuring a smooth cylindrical channel or groove running along its upper surface.
def model_55707_c78416ed_0026():
    """Model: Cherry 2x4 20 inch v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.8709, perimeter: 25.4
            with BuildLine():
                Line((0, 3.81), (0, 0))
                Line((0, 0), (8.89, 0))
                Line((8.89, 0), (8.89, 3.81))
                Line((8.89, 3.81), (0, 3.81))
            make_face()
        # OneSide extrude, distance=50.8
        extrude(amount=50.8)
    return part.part


# Description: This is a tapered cylindrical rod or needle with a slender, elongated shape that gradually decreases in diameter from one end to the other, featuring a smooth conical or pointed tip.
def model_55707_c78416ed_0028():
    """Model: Motion Rod for Bed v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=58.42
        extrude(amount=58.42)
    return part.part


# Description: This is a long, slender hexagonal or chamfered rod with tapered ends, featuring a primarily prismatic shape with angled faces along its length.
def model_55707_c78416ed_0029():
    """Model: Cherry 2x4 22.5 inch v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.8709, perimeter: 25.4
            with BuildLine():
                Line((0, 3.81), (0, 0))
                Line((0, 0), (8.89, 0))
                Line((8.89, 0), (8.89, 3.81))
                Line((8.89, 3.81), (0, 3.81))
            make_face()
        # OneSide extrude, distance=57.15
        extrude(amount=57.15)
    return part.part


# Description: A simple cylindrical rod or shaft with a straight, tapered or uniform cross-section, shown at an angle.
def model_55707_c78416ed_0030():
    """Model: Vertical Drop Rod v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=60.0075
        extrude(amount=60.0075)
    return part.part


# Description: This is a complex injection-molded or cast housing component with an irregular polygonal shape featuring multiple internal cavities, mesh-textured openings, ventilation slots, and angled surfaces designed for structural support and thermal or fluid management.
def model_55707_c78416ed_0032():
    """Model: Bearing for Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.7173451754, perimeter: 12.9132741229
            with BuildLine():
                Line((0.6, -0.1), (1.6, -0.1))
                Line((1.6, -0.1), (1.6, 0.5))
                Line((1.6, 0.5), (1.5, 0.5))
                Line((1.5, 0.5), (1.5, 1.5))
                Line((1.5, 1.5), (0.7, 1.5))
                Line((0.7, 1.5), (0.7, 1.8))
                Line((-0.7, 1.8), (0.7, 1.8))
                Line((-0.7, 1.5), (-0.7, 1.8))
                Line((-1.5, 1.5), (-0.7, 1.5))
                Line((-1.5, 0.5), (-1.5, 1.5))
                Line((-1.6, 0.5), (-1.5, 0.5))
                Line((-1.6, -0.1), (-1.6, 0.5))
                Line((-0.6, -0.1), (-1.6, -0.1))
                Line((-0.6, -0.1), (-0.6, 0))
                Line((0.6, 0), (-0.6, 0))
                Line((0.6, -0.1), (0.6, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 1.05), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a flat parallelogram-shaped sheet metal or plate part with internal diagonal reinforcement ribs or braces running across its surface.
def model_55707_c78416ed_0034():
    """Model: Heated Bed v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 676.8965708265, perimeter: 110.7123889804
            with BuildLine():
                Line((0, 21.5), (0, 0))
                Line((0, 0), (31.5, 0))
                Line((31.5, 0), (31.5, 21.5))
                Line((31.5, 21.5), (0, 21.5))
            make_face()
            with BuildLine():
                CenterArc((0.3, 21.2), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3, 0.3), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((31.2, 0.3), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((31.2, 21.2), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((15.45, 0.3), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical metal rod or shaft with a slightly tapered or rounded end, featuring a smooth uniform diameter throughout its length with a dark blue or black finish.
def model_55715_525d1d3e_0005():
    """Model: Motor Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.794), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0476092803, perimeter: 3.81
            with BuildLine():
                Line((0.5499261314, 0.3175), (0, 0.635))
                Line((0, 0.635), (-0.5499261314, 0.3175))
                Line((-0.5499261314, 0.3175), (-0.5499261314, -0.3175))
                Line((-0.5499261314, -0.3175), (0, -0.635))
                Line((0, -0.635), (0.5499261314, -0.3175))
                Line((0.5499261314, -0.3175), (0.5499261314, 0.3175))
            make_face()
        # OneSide extrude, distance=17.78
        extrude(amount=17.78)
    return part.part


# Description: This is an elliptical or oval-shaped ring/band with a hollow interior, featuring a solid outer wall and an open mesh or latticed top surface with curved internal ribbing or support structures.
def model_55715_525d1d3e_0009():
    """Model: Button"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=0.238125
        extrude(amount=0.238125)
    return part.part


# Description: This is a textured cylindrical ring or band with a uniform circular cross-section and brushed/grooved surface finish throughout its entire outer surface.
def model_55715_525d1d3e_0011():
    """Model: Back Face"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.9516069895, perimeter: 125.6794141069
            with BuildLine():
                CenterArc((0, 0), 10.16, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 9.8425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a hexagonal or elongated prismatic connector/spacer with a hollow central channel or slot running lengthwise through its center, featuring tapered pointed ends and faceted side surfaces that create a geometric, angular appearance.
def model_55715_525d1d3e_0012():
    """Model: Nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3579067176, perimeter: 4.3420776189
            with BuildLine():
                Line((0.2309401077, -0.4), (0.4618802154, 0))
                Line((0.4618802154, 0), (0.2309401077, 0.4))
                Line((0.2309401077, 0.4), (-0.2309401077, 0.4))
                Line((-0.2309401077, 0.4), (-0.4618802154, 0))
                Line((-0.4618802154, 0), (-0.2309401077, -0.4))
                Line((-0.2309401077, -0.4), (0.2309401077, -0.4))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or washer with a smooth, curved oval cross-section and textured surface finish, featuring a central hollow opening and symmetrical geometry.
def model_55715_525d1d3e_0013():
    """Model: Washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3063052837, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254)
    return part.part


# Description: This is a long, tapered composite or carbon fiber structural beam with a pointed nose cone, featuring longitudinal slots or cutouts along its sides for weight reduction and internal ribbing for structural reinforcement.
def model_55715_525d1d3e_0014():
    """Model: Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.187941083, perimeter: 10.2535928806
            with BuildLine():
                Line((0.5080000162, -2.5400000811), (-0.5080000162, -2.5400000811))
                Line((0.5080000162, 0), (0.5080000162, -2.5400000811))
                Line((-0.5080000162, 0), (0.5080000162, 0))
                Line((-0.5080000162, -2.5400000811), (-0.5080000162, 0))
            make_face()
            with BuildLine():
                CenterArc((0, -2.1590000689), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.3810000122), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or torus featuring a smooth, curved outer surface with a large central hole and a mesh or lattice pattern visible on portions of its surface, appearing to be a structural component or bearing element.
def model_55715_525d1d3e_0015():
    """Model: Base"""
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
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 444.6344601155, perimeter: 155.6033785295
            with BuildLine():
                CenterArc((0, 0), 15.24, 0, 360)
            make_face()
            with BuildLine():
                _nurbs_edge([(-9.5241085834, -2.6703099441), (-9.5243182406, -2.6756000402), (-9.5249635095, -2.6941596573), (-9.5255714627, -2.7265939782), (-9.5253748349, -2.774465086), (-9.5235010395, -2.8407247628), (-9.5202993078, -2.9060311337), (-9.5171035616, -2.9579367878), (-9.514621559, -2.9938360988), (-9.5132926727, -3.0121096142)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.7799194708, 0.7799194708, 0.7799194708, 0.7799194708, 0.7799194708, 0.7799194708, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, -2.5399999619), 9.525, 179.9930313612, 0.7908473719)
                CenterArc((0, -2.5399999619), 9.525, 0, 179.9930313612)
                CenterArc((0, -2.5399999619), 9.525, -0.7838787332, 0.7838787332)
                _nurbs_edge([(9.5241085834, -2.6703099441), (9.5243244723, -2.6756003196), (9.5249906978, -2.6941588934), (9.5256301022, -2.7265912096), (9.5254650857, -2.7744601889), (9.5236042348, -2.840719069), (9.5203818365, -2.9060262177), (9.5171520204, -2.9579338063), (9.5146390822, -2.9938350052), (9.5132926727, -3.0121096142)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.7799162836, 0.7799162836, 0.7799162836, 0.7799162836, 0.7799162836, 0.7799162836, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, -2.5399999619), 9.525, -177.1589523904, 174.3179047808)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 83.412822336, perimeter: 52.9435945828
            with BuildLine():
                _nurbs_edge([(-9.4790597316, -2.4067530672), (-9.4885844018, -2.4329888568), (-9.4979406897, -2.459315605), (-9.5071286903, -2.4857333002), (-9.5161484369, -2.5122419242), (-9.5249999295, -2.5388414772)], [1, 1, 1, 1, 1, 1], [0.9844035252, 0.9844035252, 0.9844035252, 0.9844035252, 0.9844035252, 0.9844035252, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-9.2663617248, -1.9065181102), (-9.2745134811, -1.9226288487), (-9.2929718069, -1.9594936898), (-9.3209420374, -2.0167499294), (-9.3568309517, -2.0932638335), (-9.3977291442, -2.1860202259), (-9.4319690502, -2.2701840103), (-9.4544924862, -2.3311702424), (-9.4684442464, -2.3726233668), (-9.4761932603, -2.3973306173), (-9.4790597316, -2.4067530672)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.3113428106, 0.3113428106, 0.3113428106, 0.3113428106, 0.3113428106, 0.3113428106, 0.35, 0.4, 0.45, 0.5, 0.55, 0.581590637, 0.581590637, 0.581590637, 0.581590637, 0.581590637, 0.581590637], 5)
                _nurbs_edge([(-8.8899998665, -1.2699999809), (-8.9313182033, -1.3288308377), (-9.011457959, -1.4477347353), (-9.0894403796, -1.5735752078), (-9.1621673912, -1.701800238), (-9.2298713887, -1.8325210454), (-9.2638053269, -1.9013160402), (-9.2663617248, -1.9065181102)], [1, 1, 1, 1, 1, 1, 1, 1], [0.8402218773, 0.8402218773, 0.8402218773, 0.8402218773, 0.8402218773, 0.8402218773, 0.88, 0.92, 0.9232694354, 0.9232694354, 0.9232694354, 0.9232694354, 0.9232694354, 0.9232694354], 5)
                _nurbs_edge([(-2.5399999619, 1.2699999809), (-2.5762029643, 1.2796337215), (-2.7049790694, 1.3127532985), (-2.9270956193, 1.3627987566), (-3.2442728743, 1.4163988579), (-3.6598018702, 1.4517102433), (-4.1402632937, 1.442798109), (-4.6278616387, 1.3826112192), (-5.1206115361, 1.2710459111), (-5.6140750864, 1.1110058929), (-6.1007926614, 0.9092129007), (-6.5717058977, 0.6746387192), (-7.017398805, 0.4171656611), (-7.4294739188, 0.1461260723), (-7.8017339688, -0.1309515578), (-8.1318603811, -0.4100491046), (-8.4214828132, -0.6908383169), (-8.6241453791, -0.9186172934), (-8.7618652398, -1.0924751504), (-8.8479824546, -1.2101872417), (-8.8897693981, -1.2696718299), (-8.8899998665, -1.2699999809)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.8402218773, 0.8402218773, 0.8402218773, 0.8402218773, 0.8402218773, 0.8402218773], 5)
                _nurbs_edge([(0, 0), (-0.0891007144, 0.0646539552), (-0.2675409299, 0.1906113302), (-0.5359176531, 0.3694957423), (-0.8951894707, 0.5878529415), (-1.3467696712, 0.8266941), (-1.765503218, 1.0144746183), (-2.0954651211, 1.1376113361), (-2.3352974735, 1.2134663699), (-2.4837572332, 1.2550336018), (-2.5399999619, 1.2699999809)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574], 5)
                _nurbs_edge([(0, 0), (0.0891053187, 0.0646560344), (0.2675548541, 0.1906174888), (0.5359458918, 0.3695077819), (0.8952374654, 0.5878723463), (1.3468434849, 0.8267217643), (1.7655730328, 1.0144956937), (2.0955259051, 1.1376271722), (2.3353437069, 1.2134775075), (2.4837831898, 1.25503984), (2.5399999619, 1.2699999809)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666], 5)
                _nurbs_edge([(2.5399999619, 1.2699999809), (2.5762344688, 1.2796425362), (2.7050477768, 1.3127722357), (2.9272075812, 1.3628264037), (3.2444346819, 1.4164296787), (3.6600208003, 1.4517316786), (4.1405131566, 1.4427953653), (4.6281414647, 1.3825729978), (5.1209189749, 1.2709621608), (5.6144056878, 1.1108710057), (6.1011401024, 0.9090283823), (6.5720628622, 0.6744131905), (7.0177576042, 0.416913523), (7.4298272757, 0.1458641359), (7.8020756649, -0.1312088282), (8.1321862786, -0.4102970657), (8.4217889869, -0.6910864949), (8.6243715934, -0.9188181528), (8.7620246003, -1.0926392447), (8.8480837504, -1.210311111), (8.8898187742, -1.2697420583), (8.8899998665, -1.2699999809)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.8401743455, 0.8401743455, 0.8401743455, 0.8401743455, 0.8401743455, 0.8401743455], 5)
                _nurbs_edge([(8.8899998665, -1.2699999809), (8.9313666828, -1.3289171107), (9.0115477055, -1.4479296265), (9.0894845937, -1.5737682069), (9.1621676616, -1.7020013064), (9.2298288761, -1.8327403781), (9.2636923797, -1.9014443978), (9.2661840411, -1.9065181102)], [1, 1, 1, 1, 1, 1, 1, 1], [0.8401743455, 0.8401743455, 0.8401743455, 0.8401743455, 0.8401743455, 0.8401743455, 0.88, 0.92, 0.9231869504, 0.9231869504, 0.9231869504, 0.9231869504, 0.9231869504, 0.9231869504], 5)
                _nurbs_edge([(9.2661840411, -1.9065181102), (9.2743276997, -1.9226354085), (9.2927634911, -1.9595081354), (9.3206963861, -2.0167734457), (9.3565356612, -2.0932969914), (9.3973839357, -2.1860618376), (9.4315945877, -2.270217536), (9.4541186062, -2.3311947207), (9.4680839225, -2.3726389872), (9.4758456582, -2.3973380644), (9.4787165462, -2.4067530672)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.3113296013, 0.3113296013, 0.3113296013, 0.3113296013, 0.3113296013, 0.3113296013, 0.35, 0.4, 0.45, 0.5, 0.55, 0.5815667267, 0.5815667267, 0.5815667267, 0.5815667267, 0.5815667267, 0.5815667267], 5)
                _nurbs_edge([(9.4787165462, -2.4067530672), (9.4883154307, -2.4332167563), (9.497743149, -2.4597733032), (9.5069997994, -2.4864226957), (9.5160854164, -2.5131649152), (9.525, -2.5399999619)], [1, 1, 1, 1, 1, 1], [0.9842800968, 0.9842800968, 0.9842800968, 0.9842800968, 0.9842800968, 0.9842800968, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, -2.5399999619), 9.525, 0, 179.9930313612)
            make_face()
            # Profile area: 1.4767932873, perimeter: 11.5588444269
            with BuildLine():
                _nurbs_edge([(0, 0), (0.0891053187, 0.0646560344), (0.2675548541, 0.1906174888), (0.5359458918, 0.3695077819), (0.8952374654, 0.5878723463), (1.3468434849, 0.8267217643), (1.7655730328, 1.0144956937), (2.0955259051, 1.1376271722), (2.3353437069, 1.2134775075), (2.4837831898, 1.25503984), (2.5399999619, 1.2699999809)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666, 0.2243227666], 5)
                _nurbs_edge([(0, 0), (-0.0891007144, 0.0646539552), (-0.2675409299, 0.1906113302), (-0.5359176531, 0.3694957423), (-0.8951894707, 0.5878529415), (-1.3467696712, 0.8266941), (-1.765503218, 1.0144746183), (-2.0954651211, 1.1376113361), (-2.3352974735, 1.2134663699), (-2.4837572332, 1.2550336018), (-2.5399999619, 1.2699999809)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574, 0.2243354574], 5)
                _nurbs_edge([(-2.5399999619, 1.2699999809), (-2.4510680861, 1.2005961722), (-2.2762018635, 1.0659078447), (-2.0228948824, 0.8762330954), (-1.7032697388, 0.6482296679), (-1.3342946005, 0.4059691466), (-0.9956015403, 0.2083242942), (-0.6854445475, 0.0574945837), (-0.3998492512, -0.0443355957), (-0.1312912808, -0.095586365), (0.1312912808, -0.095586365), (0.3998492512, -0.0443355957), (0.6854445475, 0.0574945837), (0.9956015403, 0.2083242942), (1.3342946005, 0.4059691466), (1.7032697388, 0.6482296679), (2.0228948824, 0.8762330954), (2.2762018635, 1.0659078447), (2.4510680861, 1.2005961722), (2.5399999619, 1.2699999809)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 0.0015329212, perimeter: 0.5396206642
            with BuildLine():
                _nurbs_edge([(9.4787165462, -2.4067530672), (9.4883154307, -2.4332167563), (9.497743149, -2.4597733032), (9.5069997994, -2.4864226957), (9.5160854164, -2.5131649152), (9.525, -2.5399999619)], [1, 1, 1, 1, 1, 1], [0.9842800968, 0.9842800968, 0.9842800968, 0.9842800968, 0.9842800968, 0.9842800968, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(9.4787165462, -2.4067530672), (9.4803929907, -2.4122509232), (9.4864484719, -2.4324797711), (9.4958531751, -2.4663455074), (9.506657455, -2.5119766776), (9.515503359, -2.5628262961), (9.5204653879, -2.6082149651), (9.5227799383, -2.6415436942), (9.5237869999, -2.6624295115), (9.5241085834, -2.6703099441)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5815667267, 0.5815667267, 0.5815667267, 0.5815667267, 0.5815667267, 0.5815667267, 0.6, 0.65, 0.7, 0.75, 0.7799162836, 0.7799162836, 0.7799162836, 0.7799162836, 0.7799162836, 0.7799162836], 5)
                CenterArc((0, -2.5399999619), 9.525, -0.7838787332, 0.7838787332)
            make_face()
            # Profile area: 0.0015327636, perimeter: 0.5395178066
            with BuildLine():
                _nurbs_edge([(-9.4790597316, -2.4067530672), (-9.4807301604, -2.4122439757), (-9.4867686075, -2.4324667552), (-9.4961405387, -2.4663282599), (-9.5068879804, -2.5119581162), (-9.5156556943, -2.5628095551), (-9.5205468056, -2.608205264), (-9.522814917, -2.6415388866), (-9.5237961995, -2.6624278373), (-9.5241085834, -2.6703099441)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.581590637, 0.581590637, 0.581590637, 0.581590637, 0.581590637, 0.581590637, 0.6, 0.65, 0.7, 0.75, 0.7799194708, 0.7799194708, 0.7799194708, 0.7799194708, 0.7799194708, 0.7799194708], 5)
                _nurbs_edge([(-9.4790597316, -2.4067530672), (-9.4885844018, -2.4329888568), (-9.4979406897, -2.459315605), (-9.5071286903, -2.4857333002), (-9.5161484369, -2.5122419242), (-9.5249999295, -2.5388414772)], [1, 1, 1, 1, 1, 1], [0.9844035252, 0.9844035252, 0.9844035252, 0.9844035252, 0.9844035252, 0.9844035252, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, -2.5399999619), 9.525, 179.9930313612, 0.7908473719)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a cylindrical connector or coupling featuring two circular flanges with central holes connected by a smaller diameter cylindrical shaft, designed to join or align two components.
def model_55779_eb7520c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with Locations((-7.25, 2)):
                Circle(2.25)
            # Profile area: 26.0025117044, perimeter: 18.0764266099
            with Locations((-3.2465225894, -1.2027819285)):
                Circle(2.8769526484)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a complex polyhedron or irregular geometric solid featuring multiple faceted surfaces in blue and dark gray, with an angular, somewhat blocky form that appears to have concave and convex sections, resembling a stylized or abstracted 3D shape without obvious functional features like holes or slots.
def model_55800_176b03e0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.1780534114, perimeter: 12.3424427291
            with BuildLine():
                Line((3.6712213646, 2.5), (3.6712213646, 0))
                Line((0, 2.5), (3.6712213646, 2.5))
                Line((0, 0), (0, 2.5))
                Line((3.6712213646, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a cylindrical capsule or obround-shaped part with rounded ends, featuring a smooth curved surface and what appears to be a central axis or bore running through its length.
def model_55803_c1fcf701_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36.6575260539, perimeter: 21.4628063915
            with Locations((-2.2328049353, 1.6856937922)):
                Circle(3.4159117298)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cylindrical housing or barrel component with a rounded bottom end and a tapered, multi-faceted top section featuring a textured or mesh-patterned surface.
def model_55810_5892fd63_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.1109008208, perimeter: 17.5554504104
            with BuildLine():
                CenterArc((0, 0), 4, 90, 136.8717449653)
                Line((0, 0), (-2.7345350611, -2.9193009436))
                Line((0, 4), (0, 0))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a cylindrical capsule or tank with hemispherical end caps, featuring a smooth curved body with what appears to be internal ribbing or reinforcement patterns visible through the transparent sections.
def model_55832_7404ec69_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 26.7035375555, perimeter: 18.3184756363
            Circle(2.9154759474)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a cylindrical capsule or rounded-end barrel-shaped part with two hemispherical end caps connected by a central cylindrical body, featuring a smooth, symmetrical geometry suitable for pressure vessels or storage containers.
def model_55863_23c2eb8c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 34.0692529318, perimeter: 20.6912266165
            Circle(3.2931109947)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is an elliptical or oval-shaped membrane or diaphragm with a reinforced perimeter rim and internal radial support ribs or stringers running from the center toward the edges, designed to provide structural stiffness while maintaining flexibility.
def model_55878_8dd0c6d0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform diameter and rounded ends, featuring a simple tubular shape with no additional features like holes, slots, or flanges.
def model_55927_f8b31711_0002():
    """Model: Pin 1,5X11 (for Piston rod) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # Symmetric extrude, each_side=0.55
        extrude(amount=0.55, both=True)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an open top and curved, tapered geometry, featuring a mesh or perforated surface on portions of its exterior.
def model_55927_f8b31711_0003():
    """Model: Distance ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a cylindrical mesh filter or strainer basket with an elliptical cross-section, featuring a solid lower half and a perforated mesh upper half for fluid or particle separation.
def model_55927_f8b31711_0004():
    """Model: Eye for Piston rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # Symmetric extrude, each_side=0.145
        extrude(amount=0.145, both=True)
    return part.part


# Description: This is a cylindrical sleeve or tube with a closed bottom end and an open top end, featuring a slightly textured or ribbed surface finish and a subtle flange or lip at the upper rim.
def model_55927_f8b31711_0005():
    """Model: Pin 1,5X9 (for Piston rod) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # Symmetric extrude, each_side=0.45
        extrude(amount=0.45, both=True)
    return part.part


# Description: This is a cylindrical sleeve or housing with an open top, featuring a curved rim edge and a mesh-textured surface that suggests it's designed for structural analysis or contains internal ribbing/reinforcement.
def model_55927_f8b31711_0011():
    """Model: Piston v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # Symmetric extrude, each_side=0.35
        extrude(amount=0.35, both=True)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or bearing component with a uniform cross-section, featuring a dark gray material with a textured mesh surface pattern visible on the inner and outer walls.
def model_55927_f8b31711_0016():
    """Model: Slider ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a cylindrical tube or sleeve with a closed top end, featuring a dark gray finish and blue text marking on the upper portion, appearing to be a simple hollow or solid cylindrical component.
def model_55927_f8b31711_0018():
    """Model: Pin 4X17 (for Crank swing arm) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=0.85
        extrude(amount=0.85, both=True)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender tubular shape, featuring rounded ends and a uniform diameter throughout its length.
def model_55927_f8b31711_0019():
    """Model: Pin 6X60 (for Crank swing arm) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


# Description: This is a cylindrical mesh or perforated filter/screen component with a closed bottom and open top, featuring a fine mesh or perforated pattern on its curved sidewalls and a denser mesh cap on the upper end.
def model_55927_f8b31711_0026():
    """Model: Pin 3X5 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a metal pry bar tool featuring a elongated shaft with a curved hook at the top for leverage and a circular loop handle at the bottom, designed for prying, lifting, and demolition work.
def model_55928_1ccd0821_0001():
    """Model: Hour Hand"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.2373334792, perimeter: 9.1338488746
            with BuildLine():
                CenterArc((5.3491288629, -0.0600364824), 0.4, 152.3034988539, 64.5925318344)
                CenterArc((5.4291014882, 0), 0.5, -143.1039693117, 118.8267274817)
                CenterArc((5.5202581542, -0.0411152312), 0.4, -24.2772418301, 52.6273777073)
                CenterArc((8.1784526862, 1.3931768527), 2.6204622084, -174.5738870567, 22.924022934)
                CenterArc((5.7741924174, 1.1294762409), 0.2050772178, 98.2423549381, 77.3097157862)
                CenterArc((5.7828465575, 1.5971114496), 0.2673979744, -146.9979496711, 48.8162554405)
                CenterArc((5.6582028988, 1.5000000224), 0.1108038477, 152.5377635748, 53.4385143215)
                CenterArc((5.8385120083, 1.2102212109), 0.4402618746, 84.4702029975, 44.7917280643)
                CenterArc((6.5121838286, 2.5359872137), 1.089138526, -169.5063240812, 44.0850724484)
                CenterArc((4.289504807, 2.6122536355), 1.1840452407, -54.4891541973, 41.0778148515)
                CenterArc((5.019690968, 1.2102212109), 0.4402618746, 50.7380689383, 44.7917280643)
                CenterArc((5.2000000775, 1.5000000224), 0.1108038477, -25.9762778964, 53.4385143215)
                CenterArc((5.0753564189, 1.5971114496), 0.2673979744, -81.8183057694, 48.8162554405)
                CenterArc((5.0840105589, 1.1294762409), 0.2050772178, 4.2073361456, 77.5503089163)
                CenterArc((2.6647869517, 1.3490654281), 2.6317090379, -27.6965011461, 23.2388231478)
            make_face()
            with BuildLine():
                CenterArc((5.4291014882, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a rivet or fastener with a rounded hemispherical head on one end and a tapered, pointed shaft extending to the other end, designed for joining or securing materials.
def model_55928_1ccd0821_0002():
    """Model: Minute Hand"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.85), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3471017142, perimeter: 4.226614746
            with BuildLine():
                CenterArc((5.4291014882, 0), 0.4, 48.4068381562, 263.1863236877)
                CenterArc((6.0265547517, -0.6730895913), 0.5, 105.7593340642, 25.8338277797)
                CenterArc((5.5202581542, -0.0411152312), 0.4, -22.143163122, 50.4932989993)
                CenterArc((8.1784526862, 1.3931768527), 2.6204622084, -153.1305607842, 1.4806966615)
                CenterArc((6.0265547517, 0.6730895913), 0.5, -131.5931618438, 19.7966279256)
            make_face()
            with BuildLine():
                CenterArc((5.4291014882, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9847388243, perimeter: 6.7255092835
            with BuildLine():
                CenterArc((6.0265547517, -0.6730895913), 0.5, 85.2055250273, 20.5538090369)
                CenterArc((6.9280820794, 10.0753429515), 10.2861741896, -94.7944749727, 16.4149202894)
                CenterArc((6.9280820794, -10.0753429515), 10.2861741896, 78.3795546833, 16.4149202894)
                CenterArc((6.0265547517, 0.6730895913), 0.5, -111.7965339182, 26.5910088909)
                CenterArc((8.1784526862, 1.3931768527), 2.6204622084, -153.1305607842, 1.4806966615)
                CenterArc((5.5202581542, -0.0411152312), 0.4, -22.143163122, 50.4932989993)
            make_face()
            # Profile area: 0.1649336143, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((5.4291014882, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.4291014882, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a slotted spring pin or roll pin with a cylindrical body featuring a longitudinal slot running along its length for compression and spring retention.
def model_56013_752d02cb_0001():
    """Model: link v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 79.3561944902, perimeter: 61.4247779608
            with BuildLine():
                CenterArc((19, 1), 1, 180, 90)
                Line((19, 0), (44, 0))
                CenterArc((44, 1), 1, -90, 90)
                Line((45, 1), (45, 2))
                CenterArc((44, 2), 1, 0, 90)
                Line((44, 3), (19, 3))
                CenterArc((19, 2), 1, 90, 90)
                Line((18, 2), (18, 1))
            make_face()
            with BuildLine():
                CenterArc((44, 1.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: A rectangular bar or shaft with rounded ends and a uniform cylindrical profile, appearing to be a simple mechanical component such as a pin, rod, or spacer.
def model_56013_752d02cb_0003():
    """Model: shaft600 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=60
        extrude(amount=60)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a simple elongated tubular shape with no visible holes, slots, or flanges.
def model_56013_752d02cb_0004():
    """Model: shaft500 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a rounded rectangular bar or rod with a simple cylindrical or prismatic shape, featuring uniformly rounded edges at both ends.
def model_56013_752d02cb_0007():
    """Model: handle rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=35
        extrude(amount=35)
    return part.part


MODELS = {
    "model_51913_1fa125b4_0001": {"func": model_51913_1fa125b4_0001, "volume": 991.1926741943, "area": 3425.149862506},
    "model_51913_1fa125b4_0002": {"func": model_51913_1fa125b4_0002, "volume": 131.2830975901, "area": 3300.5582403978},
    "model_51913_1fa125b4_0004": {"func": model_51913_1fa125b4_0004, "volume": 0.0363246651, "area": 1.3076879421},
    "model_51913_1fa125b4_0008": {"func": model_51913_1fa125b4_0008, "volume": 5537977.5799748916, "area": 526408.0106358496},
    "model_51913_1fa125b4_0014": {"func": model_51913_1fa125b4_0014, "volume": 9.5504416669, "area": 48.7575179837},
    "model_51914_fb924efa_0009": {"func": model_51914_fb924efa_0009, "volume": 0.0712, "area": 7.4048},
    "model_51916_fa226b15_0002": {"func": model_51916_fa226b15_0002, "volume": 0.5436379618, "area": 6.6991527888},
    "model_51916_fa226b15_0013": {"func": model_51916_fa226b15_0013, "volume": 4.2878089553, "area": 39.0687460584},
    "model_51932_c1f74efe_0002": {"func": model_51932_c1f74efe_0002, "volume": 5.7313366269, "area": 36.7362922346},
    "model_51940_aa0fca73_0011": {"func": model_51940_aa0fca73_0011, "volume": 1.6840631336, "area": 13.9388312331},
    "model_51940_aa0fca73_0015": {"func": model_51940_aa0fca73_0015, "volume": 122.52211349, "area": 204.2035224833},
    "model_51940_aa0fca73_0016": {"func": model_51940_aa0fca73_0016, "volume": 7.2982649353, "area": 43.1150582141},
    "model_51940_aa0fca73_0023": {"func": model_51940_aa0fca73_0023, "volume": 0.5277875658, "area": 7.037167544},
    "model_51940_aa0fca73_0025": {"func": model_51940_aa0fca73_0025, "volume": 1.265068328, "area": 8.6009329829},
    "model_51942_f6e66631_0006": {"func": model_51942_f6e66631_0006, "volume": 6.99, "area": 74.764},
    "model_51942_f6e66631_0007": {"func": model_51942_f6e66631_0007, "volume": 0.0839394287, "area": 3.8052541017},
    "model_51942_f6e66631_0008": {"func": model_51942_f6e66631_0008, "volume": 28.2, "area": 156.76},
    "model_51942_f6e66631_0009": {"func": model_51942_f6e66631_0009, "volume": 29.79, "area": 602.772},
    "model_52004_186af290_0005": {"func": model_52004_186af290_0005, "volume": 22.0242154218, "area": 52.1289300096},
    "model_52004_186af290_0006": {"func": model_52004_186af290_0006, "volume": 144.7916621521, "area": 174.8140802886},
    "model_52004_186af290_0007": {"func": model_52004_186af290_0007, "volume": 12.2903021577, "area": 116.1288090183},
    "model_52006_d21e4570_0001": {"func": model_52006_d21e4570_0001, "volume": 47.9761065788, "area": 154.0318578949},
    "model_52006_d21e4570_0003": {"func": model_52006_d21e4570_0003, "volume": 5.3130220909, "area": 81.6392179891},
    "model_52012_77070fda_0013": {"func": model_52012_77070fda_0013, "volume": 0.7092186145, "area": 5.1230024946},
    "model_52012_77070fda_0024": {"func": model_52012_77070fda_0024, "volume": 56.5486677646, "area": 119.3805208364},
    "model_52012_77070fda_0025": {"func": model_52012_77070fda_0025, "volume": 3.5342917353, "area": 18.8495559215},
    "model_52012_77070fda_0026": {"func": model_52012_77070fda_0026, "volume": 864, "area": 600},
    "model_52024_97da327b_0003": {"func": model_52024_97da327b_0003, "volume": 0.0103790964, "area": 0.8413397251},
    "model_52024_97da327b_0004": {"func": model_52024_97da327b_0004, "volume": 0.3612075968, "area": 3.9801924163},
    "model_52024_97da327b_0010": {"func": model_52024_97da327b_0010, "volume": 2.0314122756, "area": 20.6176866657},
    "model_52024_97da327b_0012": {"func": model_52024_97da327b_0012, "volume": 0.5158202964, "area": 4.6933780251},
    "model_52027_790dbc09_0012": {"func": model_52027_790dbc09_0012, "volume": 41.836307455, "area": 304.5016827359},
    "model_52028_7396037a_0015": {"func": model_52028_7396037a_0015, "volume": 27.8580105781, "area": 56.7740822237},
    "model_52229_996054ef_0011": {"func": model_52229_996054ef_0011, "volume": 0.0147262156, "area": 0.5301437603},
    "model_52230_60438ea5_0007": {"func": model_52230_60438ea5_0007, "volume": 2.9452431127, "area": 25.5254403104},
    "model_52352_adac16c3_0024": {"func": model_52352_adac16c3_0024, "volume": 23120000, "area": 503200},
    "model_52358_1bb3de48_0000": {"func": model_52358_1bb3de48_0000, "volume": 18.4308258747, "area": 191.1142647516},
    "model_52365_274736ef_0002": {"func": model_52365_274736ef_0002, "volume": 56.5329598013, "area": 245.2955543923},
    "model_52365_274736ef_0003": {"func": model_52365_274736ef_0003, "volume": 50002.7293307958, "area": 22001.1463189342},
    "model_52449_3da8c6e5_0000": {"func": model_52449_3da8c6e5_0000, "volume": 230000, "area": 37700},
    "model_52557_e6a00b06_0006": {"func": model_52557_e6a00b06_0006, "volume": 35.4880708114, "area": 115.894689748},
    "model_52557_e6a00b06_0008": {"func": model_52557_e6a00b06_0008, "volume": 1.3571680264, "area": 7.916813487},
    "model_52557_e6a00b06_0011": {"func": model_52557_e6a00b06_0011, "volume": 0.6, "area": 13.4},
    "model_52557_e6a00b06_0012": {"func": model_52557_e6a00b06_0012, "volume": 0.4927958526, "area": 11.2579827683},
    "model_52558_c0e0653f_0002": {"func": model_52558_c0e0653f_0002, "volume": 0.20901225, "area": 4.1002009054},
    "model_52576_6a9d504d_0000": {"func": model_52576_6a9d504d_0000, "volume": 30.8865681738, "area": 67.4342863093},
    "model_52771_3d59c5f9_0000": {"func": model_52771_3d59c5f9_0000, "volume": 80, "area": 132},
    "model_52772_a6e6e320_0001": {"func": model_52772_a6e6e320_0001, "volume": 375.8699537242, "area": 1263.1401146926},
    "model_52879_de812eb3_0010": {"func": model_52879_de812eb3_0010, "volume": 3.136, "area": 17.92},
    "model_52884_c8150d6e_0002": {"func": model_52884_c8150d6e_0002, "volume": 7.6552758986, "area": 56.4072960952},
    "model_52884_c8150d6e_0005": {"func": model_52884_c8150d6e_0005, "volume": 0.0009424778, "area": 0.081681409},
    "model_52884_c8150d6e_0006": {"func": model_52884_c8150d6e_0006, "volume": 0.0194992744, "area": 1.4568590984},
    "model_52884_c8150d6e_0010": {"func": model_52884_c8150d6e_0010, "volume": 4.2930463288, "area": 17.7230482498},
    "model_52884_c8150d6e_0013": {"func": model_52884_c8150d6e_0013, "volume": 0.0078539816, "area": 0.2199114858},
    "model_52884_c8150d6e_0037": {"func": model_52884_c8150d6e_0037, "volume": 1.6857783565, "area": 8.2191617072},
    "model_52886_5743bcf0_0000": {"func": model_52886_5743bcf0_0000, "volume": 2.5517586329, "area": 52.8258804701},
    "model_52886_5743bcf0_0002": {"func": model_52886_5743bcf0_0002, "volume": 0.014529866, "area": 0.7539822369},
    "model_52973_475412f8_0000": {"func": model_52973_475412f8_0000, "volume": 38727.0901770754, "area": 31760.9245049885},
    "model_52985_475fe7b2_0015": {"func": model_52985_475fe7b2_0015, "volume": 49.0873852123, "area": 88.3572933822},
    "model_52985_475fe7b2_0019": {"func": model_52985_475fe7b2_0019, "volume": 12000, "area": 12920},
    "model_52987_387431ac_0001": {"func": model_52987_387431ac_0001, "volume": 58.7045857231, "area": 239.5621477995},
    "model_52987_387431ac_0002": {"func": model_52987_387431ac_0002, "volume": 14.7780518425, "area": 45.7415890363},
    "model_52987_387431ac_0005": {"func": model_52987_387431ac_0005, "volume": 23.0930621984, "area": 163.2842781703},
    "model_52987_387431ac_0007": {"func": model_52987_387431ac_0007, "volume": 19.0046602229, "area": 143.2206988356},
    "model_52987_387431ac_0009": {"func": model_52987_387431ac_0009, "volume": 34.2171276255, "area": 109.9023358005},
    "model_53075_6438cc56_0010": {"func": model_53075_6438cc56_0010, "volume": 2.312, "area": 25.84},
    "model_53078_b592f2bd_0001": {"func": model_53078_b592f2bd_0001, "volume": 32.6851299679, "area": 111.2123799371},
    "model_53078_b592f2bd_0008": {"func": model_53078_b592f2bd_0008, "volume": 4.5660595176, "area": 21.3908567933},
    "model_53091_ff6e681c_0000": {"func": model_53091_ff6e681c_0000, "volume": 5500, "area": 11324},
    "model_53119_aabd4fc1_0024": {"func": model_53119_aabd4fc1_0024, "volume": 4123.3403578366, "area": 3337.9421944392},
    "model_53182_1ee4339e_0001": {"func": model_53182_1ee4339e_0001, "volume": 2820.5128003133, "area": 9212.8267457907},
    "model_53198_6f2c7c22_0000": {"func": model_53198_6f2c7c22_0000, "volume": 0.3284509096, "area": 2.6885109987},
    "model_53216_2857e8ac_0001": {"func": model_53216_2857e8ac_0001, "volume": 4.6852873148, "area": 29.3664252738},
    "model_53216_2857e8ac_0002": {"func": model_53216_2857e8ac_0002, "volume": 20.4110964872, "area": 159.8519336956},
    "model_53216_2857e8ac_0006": {"func": model_53216_2857e8ac_0006, "volume": 37.6991118431, "area": 379.5043925536},
    "model_53221_74fa81cd_0007": {"func": model_53221_74fa81cd_0007, "volume": 1671604.3390969327, "area": 139383.1963992648},
    "model_53222_e9c623af_0004": {"func": model_53222_e9c623af_0004, "volume": 15.5508836353, "area": 34.8716784548},
    "model_53222_e9c623af_0005": {"func": model_53222_e9c623af_0005, "volume": 4.7123889804, "area": 15.7079632679},
    "model_53233_8dbca22c_0002": {"func": model_53233_8dbca22c_0002, "volume": 3142.6709154805, "area": 3143.4160725095},
    "model_53233_8dbca22c_0014": {"func": model_53233_8dbca22c_0014, "volume": 4518.872188044, "area": 14461.5646252},
    "model_53233_8dbca22c_0026": {"func": model_53233_8dbca22c_0026, "volume": 373.0653812041, "area": 590.2719309052},
    "model_53459_ce174d0e_0002": {"func": model_53459_ce174d0e_0002, "volume": 3.5342917353, "area": 15.7079632679},
    "model_53459_ce174d0e_0010": {"func": model_53459_ce174d0e_0010, "volume": 1963.4954084936, "area": 1610.0662349648},
    "model_53470_39f2e9dc_0008": {"func": model_53470_39f2e9dc_0008, "volume": 37.6991118431, "area": 100.5309649149},
    "model_53590_a324861b_0000": {"func": model_53590_a324861b_0000, "volume": 8.5058621096, "area": 23.5776528652},
    "model_53620_99bef654_0000": {"func": model_53620_99bef654_0000, "volume": 6.2373002107, "area": 67.9156214056},
    "model_53627_7b1adb8e_0000": {"func": model_53627_7b1adb8e_0000, "volume": 0.000875, "area": 0.08875},
    "model_53724_20b71853_0000": {"func": model_53724_20b71853_0000, "volume": 461812.2356537282, "area": 103426.4710931621},
    "model_53841_c93c3cd8_0003": {"func": model_53841_c93c3cd8_0003, "volume": 0.0016269021, "area": 1.6367966811},
    "model_53846_89405f98_0019": {"func": model_53846_89405f98_0019, "volume": 0.1199397494, "area": 2.733512551},
    "model_53846_89405f98_0025": {"func": model_53846_89405f98_0025, "volume": 0.0141371669, "area": 0.471238898},
    "model_53848_7c64ed9f_0005": {"func": model_53848_7c64ed9f_0005, "volume": 150.7964473723, "area": 339.2920065877},
    "model_53927_ef5208b9_0005": {"func": model_53927_ef5208b9_0005, "volume": 0.5277875658, "area": 6.0318578949},
    "model_53927_ef5208b9_0007": {"func": model_53927_ef5208b9_0007, "volume": 1.9603538158, "area": 20.3575203953},
    "model_53927_ef5208b9_0010": {"func": model_53927_ef5208b9_0010, "volume": 1.3035841133, "area": 8.8270088291},
    "model_54177_2b99e039_0003": {"func": model_54177_2b99e039_0003, "volume": 0.0184725648, "area": 1.9704069123},
    "model_54177_2b99e039_0006": {"func": model_54177_2b99e039_0006, "volume": 2.4, "area": 32.5699111843},
    "model_54177_2b99e039_0007": {"func": model_54177_2b99e039_0007, "volume": 2.3905437122, "area": 20.4261072357},
    "model_54177_2b99e039_0008": {"func": model_54177_2b99e039_0008, "volume": 2.750000082, "area": 22.5000003427},
    "model_54177_2b99e039_0012": {"func": model_54177_2b99e039_0012, "volume": 0.1413716694, "area": 3.7699111843},
    "model_54177_2b99e039_0013": {"func": model_54177_2b99e039_0013, "volume": 1.5268140296, "area": 35.6256606917},
    "model_54285_76f37095_0001": {"func": model_54285_76f37095_0001, "volume": 0.0282743347, "area": 0.7539822509},
    "model_54285_76f37095_0008": {"func": model_54285_76f37095_0008, "volume": 0.009424778, "area": 0.3769911184},
    "model_54285_76f37095_0010": {"func": model_54285_76f37095_0010, "volume": 0.1570796327, "area": 1.6493361431},
    "model_54285_76f37095_0011": {"func": model_54285_76f37095_0011, "volume": 0.0047123891, "area": 0.2827433458},
    "model_54374_5c085a74_0002": {"func": model_54374_5c085a74_0002, "volume": 0.0259181394, "area": 0.8639379797},
    "model_54374_5c085a74_0005": {"func": model_54374_5c085a74_0005, "volume": 4.3196898987, "area": 34.5575191895},
    "model_54374_5c085a74_0013": {"func": model_54374_5c085a74_0013, "volume": 0.4663301806, "area": 7.834346767},
    "model_54383_13d47b0e_0003": {"func": model_54383_13d47b0e_0003, "volume": 6906.2037073675, "area": 2473.7185375504},
    "model_54383_13d47b0e_0011": {"func": model_54383_13d47b0e_0011, "volume": 150.7964473723, "area": 1513.996331618},
    "model_54384_7ba07a68_0000": {"func": model_54384_7ba07a68_0000, "volume": 76.9222102824, "area": 160.127605872},
    "model_54480_e96c0f36_0000": {"func": model_54480_e96c0f36_0000, "volume": 42.8628330588, "area": 100.280972451},
    "model_54509_e0930519_0002": {"func": model_54509_e0930519_0002, "volume": 0.9817477042, "area": 8.2466807157},
    "model_54593_6710154c_0000": {"func": model_54593_6710154c_0000, "volume": 49.0873852123, "area": 99.0873852123},
    "model_54659_e1303e28_0010": {"func": model_54659_e1303e28_0010, "volume": 2.3347544897, "area": 16.3641348744},
    "model_54659_e1303e28_0016": {"func": model_54659_e1303e28_0016, "volume": 0.3141592654, "area": 3.3929200659},
    "model_54659_e1303e28_0023": {"func": model_54659_e1303e28_0023, "volume": 2.003591929, "area": 14.8957885181},
    "model_54659_e1303e28_0029": {"func": model_54659_e1303e28_0029, "volume": 2.0106192983, "area": 11.0584061406},
    "model_54659_e1303e28_0031": {"func": model_54659_e1303e28_0031, "volume": 3.7397518948, "area": 28.8021214481},
    "model_54659_e1303e28_0032": {"func": model_54659_e1303e28_0032, "volume": 0.1570796327, "area": 3.4557519189},
    "model_54659_e1303e28_0034": {"func": model_54659_e1303e28_0034, "volume": 0.6283185307, "area": 6.5345127195},
    "model_54659_e1303e28_0037": {"func": model_54659_e1303e28_0037, "volume": 186.5475688726, "area": 313.3384916404},
    "model_54659_e1303e28_0039": {"func": model_54659_e1303e28_0039, "volume": 0.5026548246, "area": 5.277875658},
    "model_54659_e1303e28_0040": {"func": model_54659_e1303e28_0040, "volume": 0.2513274123, "area": 2.7646015352},
    "model_54659_e1303e28_0041": {"func": model_54659_e1303e28_0041, "volume": 0.3769911184, "area": 4.0212385966},
    "model_54787_92b88ea1_0001": {"func": model_54787_92b88ea1_0001, "volume": 100.8, "area": 148.3646752982},
    "model_54820_a9ecc8b7_0000": {"func": model_54820_a9ecc8b7_0000, "volume": 147.2434104761, "area": 239.9350547663},
    "model_54979_6bd8ad31_0011": {"func": model_54979_6bd8ad31_0011, "volume": 600, "area": 1300},
    "model_54979_6bd8ad31_0012": {"func": model_54979_6bd8ad31_0012, "volume": 52.3742835399, "area": 232.8448267672},
    "model_55024_4cf14b6f_0000": {"func": model_55024_4cf14b6f_0000, "volume": 203.2007424818, "area": 257.8314762152},
    "model_55027_b152933c_0000": {"func": model_55027_b152933c_0000, "volume": 390, "area": 398},
    "model_55057_4fbc0f08_0000": {"func": model_55057_4fbc0f08_0000, "volume": 109.575308057, "area": 215.0069450541},
    "model_55058_3a36a12b_0000": {"func": model_55058_3a36a12b_0000, "volume": 0.0590097922, "area": 1.7222484812},
    "model_55060_980d5147_0000": {"func": model_55060_980d5147_0000, "volume": 64, "area": 112},
    "model_55077_dd176614_0000": {"func": model_55077_dd176614_0000, "volume": 158.8645567535, "area": 242.4462422445},
    "model_55110_ccc772b9_0005": {"func": model_55110_ccc772b9_0005, "volume": 67.1515429705, "area": 179.0707812546},
    "model_55110_ccc772b9_0010": {"func": model_55110_ccc772b9_0010, "volume": 23.0725776276, "area": 105.6604701725},
    "model_55114_7bf17f6a_0002": {"func": model_55114_7bf17f6a_0002, "volume": 318.086256176, "area": 551.349510705},
    "model_55114_7bf17f6a_0004": {"func": model_55114_7bf17f6a_0004, "volume": 435.8959806856, "area": 755.5530331883},
    "model_55199_4d57661f_0000": {"func": model_55199_4d57661f_0000, "volume": 56.7057473973, "area": 578.9955260566},
    "model_55212_29e38f0c_0000": {"func": model_55212_29e38f0c_0000, "volume": 94.2477796077, "area": 122.4393826666},
    "model_55216_d28562a7_0000": {"func": model_55216_d28562a7_0000, "volume": 15.8510507472, "area": 96.106780596},
    "model_55245_473548f5_0000": {"func": model_55245_473548f5_0000, "volume": 105.7280961793, "area": 233.963654202},
    "model_55255_e0101aad_0005": {"func": model_55255_e0101aad_0005, "volume": 15.3938040026, "area": 47.0610579508},
    "model_55323_716f61f1_0001": {"func": model_55323_716f61f1_0001, "volume": 0.48, "area": 6.16},
    "model_55351_303fec3a_0000": {"func": model_55351_303fec3a_0000, "volume": 3.1415926536, "area": 14.1371669412},
    "model_55391_a3016f11_0000": {"func": model_55391_a3016f11_0000, "volume": 1625, "area": 936.803398875},
    "model_55403_d243028d_0000": {"func": model_55403_d243028d_0000, "volume": 19.6349540849, "area": 54.9778714378},
    "model_55419_09442d50_0000": {"func": model_55419_09442d50_0000, "volume": 886.9803006638, "area": 625.2261102434},
    "model_55473_64d24a1b_0000": {"func": model_55473_64d24a1b_0000, "volume": 190, "area": 281.2455532034},
    "model_55519_da060af7_0000": {"func": model_55519_da060af7_0000, "volume": 303.7969567387, "area": 429.7370783017},
    "model_55605_2f8bc12e_0006": {"func": model_55605_2f8bc12e_0006, "volume": 1.2370021512, "area": 11.5453533296},
    "model_55605_2f8bc12e_0056": {"func": model_55605_2f8bc12e_0056, "volume": 0.7158134565, "area": 7.2053315095},
    "model_55611_69142616_0018": {"func": model_55611_69142616_0018, "volume": 1.0053096491, "area": 6.0318578949},
    "model_55625_453e11ac_0004": {"func": model_55625_453e11ac_0004, "volume": 0.0911126042, "area": 3.1303170337},
    "model_55625_453e11ac_0010": {"func": model_55625_453e11ac_0010, "volume": 0.2499133442, "area": 7.3480259287},
    "model_55633_282eaae6_0001": {"func": model_55633_282eaae6_0001, "volume": 0.0062831853, "area": 0.2513274123},
    "model_55633_282eaae6_0010": {"func": model_55633_282eaae6_0010, "volume": 0.0161608718, "area": 0.732910137},
    "model_55634_3b61fa4d_0004": {"func": model_55634_3b61fa4d_0004, "volume": 0.1482800317, "area": 3.0284324862},
    "model_55634_3b61fa4d_0006": {"func": model_55634_3b61fa4d_0006, "volume": 0.1624360482, "area": 3.3115528161},
    "model_55634_3b61fa4d_0009": {"func": model_55634_3b61fa4d_0009, "volume": 0.2947850635, "area": 5.9585331224},
    "model_55707_c78416ed_0010": {"func": model_55707_c78416ed_0010, "volume": 21.0662636979, "area": 106.3366281387},
    "model_55707_c78416ed_0011": {"func": model_55707_c78416ed_0011, "volume": 16.3814139187, "area": 109.7749128025},
    "model_55707_c78416ed_0018": {"func": model_55707_c78416ed_0018, "volume": 1806.673806, "area": 1422.5778},
    "model_55707_c78416ed_0019": {"func": model_55707_c78416ed_0019, "volume": 2064.770064, "area": 1616.1258},
    "model_55707_c78416ed_0022": {"func": model_55707_c78416ed_0022, "volume": 13.4535848094, "area": 65.7400056208},
    "model_55707_c78416ed_0026": {"func": model_55707_c78416ed_0026, "volume": 1720.64172, "area": 1358.0618},
    "model_55707_c78416ed_0028": {"func": model_55707_c78416ed_0028, "volume": 29.3650948516, "area": 147.8307839073},
    "model_55707_c78416ed_0029": {"func": model_55707_c78416ed_0029, "volume": 1935.721935, "area": 1519.3518},
    "model_55707_c78416ed_0030": {"func": model_55707_c78416ed_0030, "volume": 30.1630593856, "area": 151.8206065774},
    "model_55707_c78416ed_0032": {"func": model_55707_c78416ed_0032, "volume": 14.1520355263, "area": 48.1745127195},
    "model_55707_c78416ed_0034": {"func": model_55707_c78416ed_0034, "volume": 135.3793141653, "area": 1375.935619449},
    "model_55715_525d1d3e_0005": {"func": model_55715_525d1d3e_0005, "volume": 18.6264930041, "area": 69.8370185606},
    "model_55715_525d1d3e_0009": {"func": model_55715_525d1d3e_0009, "volume": 0.1696777291, "area": 2.1376721774},
    "model_55715_525d1d3e_0011": {"func": model_55715_525d1d3e_0011, "volume": 76.0156226299, "area": 518.7417817261},
    "model_55715_525d1d3e_0012": {"func": model_55715_525d1d3e_0012, "volume": 0.0454541531, "area": 1.2672572927},
    "model_55715_525d1d3e_0013": {"func": model_55715_525d1d3e_0013, "volume": 0.0077801542, "area": 0.7163459569},
    "model_55715_525d1d3e_0014": {"func": model_55715_525d1d3e_0014, "volume": 0.2778685175, "area": 5.6780884619},
    "model_55715_525d1d3e_0015": {"func": model_55715_525d1d3e_0015, "volume": 1344.9991018749, "area": 1437.0879240202},
    "model_55779_eb7520c9_0000": {"func": model_55779_eb7520c9_0000, "volume": 209.5341225658, "area": 244.8816167814},
    "model_55800_176b03e0_0000": {"func": model_55800_176b03e0_0000, "volume": 22.9451335285, "area": 49.2122136456},
    "model_55803_c1fcf701_0000": {"func": model_55803_c1fcf701_0000, "volume": 183.2876302696, "area": 180.6290840654},
    "model_55810_5892fd63_0000": {"func": model_55810_5892fd63_0000, "volume": 152.887206566, "area": 178.6654049245},
    "model_55832_7404ec69_0000": {"func": model_55832_7404ec69_0000, "volume": 267.0353755551, "area": 236.5918314738},
    "model_55863_23c2eb8c_0000": {"func": model_55863_23c2eb8c_0000, "volume": 340.6925293185, "area": 275.0507720288},
    "model_55878_8dd0c6d0_0000": {"func": model_55878_8dd0c6d0_0000, "volume": 7.6969020013, "area": 81.367249728},
    "model_55927_f8b31711_0002": {"func": model_55927_f8b31711_0002, "volume": 0.0194386045, "area": 0.5537057052},
    "model_55927_f8b31711_0003": {"func": model_55927_f8b31711_0003, "volume": 0.1099557429, "area": 2.638937829},
    "model_55927_f8b31711_0004": {"func": model_55927_f8b31711_0004, "volume": 0.1844900286, "area": 2.0923007073},
    "model_55927_f8b31711_0005": {"func": model_55927_f8b31711_0005, "volume": 0.0159043128, "area": 0.4594579256},
    "model_55927_f8b31711_0011": {"func": model_55927_f8b31711_0011, "volume": 0.7916813487, "area": 4.9008845396},
    "model_55927_f8b31711_0016": {"func": model_55927_f8b31711_0016, "volume": 0.4523893421, "area": 6.7858401318},
    "model_55927_f8b31711_0018": {"func": model_55927_f8b31711_0018, "volume": 0.2136283004, "area": 2.3876104167},
    "model_55927_f8b31711_0019": {"func": model_55927_f8b31711_0019, "volume": 1.6964600329, "area": 11.8752202306},
    "model_55927_f8b31711_0026": {"func": model_55927_f8b31711_0026, "volume": 0.0353429174, "area": 0.6126105675},
    "model_55928_1ccd0821_0001": {"func": model_55928_1ccd0821_0001, "volume": 0.1856000219, "area": 3.8447442896},
    "model_55928_1ccd0821_0002": {"func": model_55928_1ccd0821_0002, "volume": 0.2245161229, "area": 4.3689261159},
    "model_56013_752d02cb_0001": {"func": model_56013_752d02cb_0001, "volume": 79.3561944902, "area": 220.1371669412},
    "model_56013_752d02cb_0003": {"func": model_56013_752d02cb_0003, "volume": 294.524311274, "area": 481.0563750809},
    "model_56013_752d02cb_0004": {"func": model_56013_752d02cb_0004, "volume": 245.4369260617, "area": 402.5165587412},
    "model_56013_752d02cb_0007": {"func": model_56013_752d02cb_0007, "volume": 61.8501053675, "area": 168.4679060488},
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
