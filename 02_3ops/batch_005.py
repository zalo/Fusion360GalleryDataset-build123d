"""Batch 005 - passing/02_3ops
155 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a linear rail or slide bar component with an elongated rectangular profile, featuring a central slot running along its length and mounting flanges on the sides for attachment.
def model_38287_88ec74de_0069():
    """Model: zabezpieczenie v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 51.6251352938, perimeter: 48.539782879
            with BuildLine():
                Line((-1.7500000149, 15), (-1.7500000149, 0))
                CenterArc((-1.0000000149, 0), 0.75, 180, 180)
                Line((-0.2500000149, 0), (3.2499999851, 0))
                CenterArc((3.9999999851, 0), 0.75, 180, 203.3681149557)
                Line((-0.8000000119, 13.0000002086), (4.6884816071, 0.2974778247))
                Line((-0.8000000119, 14.0000002086), (-0.8000000119, 13.0000002086))
                Line((0.5000000075, 14.0000002086), (-0.8000000119, 14.0000002086))
                Line((-0.7500000149, 15), (0.5000000075, 14.0000002086))
                Line((-1.7500000149, 15), (-0.7500000149, 15))
            make_face()
            with BuildLine():
                CenterArc((-1.0000000149, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.9999999851, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal ring or band with a hollow center and textured surface finish, featuring flat faceted sides and a uniform cross-sectional profile.
def model_38287_88ec74de_0082():
    """Model: Uchwyt v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2360619776, perimeter: 23.8527638725
            with BuildLine():
                Line((-1.9999998942, 1.0000000149), (-1.9999998942, 0.0006506319))
                CenterArc((0, 0), 2, 179.9813607687, 0.0372784626)
                Line((-1.9999998942, -0.0006506319), (-1.9999998942, -1.0000000149))
                Line((-1.9999998942, -1.0000000149), (-1.2000000825, -1.5999999381))
                CenterArc((0, 0), 2, -126.869900601, 253.739801202)
                Line((-1.9999998942, 1.0000000149), (-1.2000000825, 1.5999999381))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal or polygonal container/enclosure with mesh or perforated side panels and solid top/bottom faces, designed as a ventilated basket or cage structure.
def model_38287_88ec74de_0088():
    """Model: śróba12 v1 (5)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0860517445, perimeter: 9.3124738511
            with BuildLine():
                Line((0.8000000119, -0.4618802222), (0.8000000119, 0.4618802222))
                Line((0.8000000119, 0.4618802222), (0, 0.9237604445))
                Line((0, 0.9237604445), (-0.8000000119, 0.4618802222))
                Line((-0.8000000119, 0.4618802222), (-0.8000000119, -0.4618802222))
                Line((-0.8000000119, -0.4618802222), (0, -0.9237604445))
                Line((0, -0.9237604445), (0.8000000119, -0.4618802222))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a tweezers or forceps tool featuring two curved, tapered arms that converge at a base, with a circular loop handle at the top for gripping, designed for precise picking or manipulation tasks.
def model_38288_740bfe5a_0007():
    """Model: Legs v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.2644396678, perimeter: 61.1823195912
            with BuildLine():
                CenterArc((14, 29.0125314072), 4.9874685928, -90, 180)
                CenterArc((14, 29.0125314072), 4.9874685928, 90, 180)
            make_face()
            with BuildLine():
                CenterArc((14, 29), 4.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 20.2167840314, perimeter: 42.1015874644
            with BuildLine():
                CenterArc((-29.3885743139, 10.6910732549), 43.4035194642, -8.8345810093, 17.6691620187)
                Line((13.5, 4.0250628145), (14.5, 4.0250628145))
                CenterArc((-34.5057283289, 11.1006891684), 49.5138960025, -8.2157976336, 16.4315952672)
                Line((14.5, 18.1763155224), (14.5, 24.0250628145))
                Line((14, 24.0250628145), (14.5, 24.0250628145))
                Line((13.5, 24.0250628145), (14, 24.0250628145))
                Line((13.5, 17.3570836954), (13.5, 24.0250628145))
            make_face()
            # Profile area: 88.390742474, perimeter: 142.4171885964
            with BuildLine():
                CenterArc((5.7248987653, 0.0291372818), 8.74183162, 27.2003862931, 56.4143311354)
                Line((5.8504793667, 9.9177456917), (6.6971098703, 8.7167391166))
                Line((5.0331465268, 9.341579892), (5.8504793667, 9.9177456917))
                Line((5.8973952264, 8.1155806321), (5.0331465268, 9.341579892))
                CenterArc((5.2533107488, -0.1229670601), 8.2636863984, -20.3744282599, 105.9041728741)
                Line((13, -3), (18, -3))
                CenterArc((26.5538730647, -0.650553295), 8.8706619949, 148.3814078501, 46.9769795915)
                CenterArc((2.8273201633, 19.5583776143), 22.4414502003, -43.8909122077, 59.361336182)
                Line((24.2354522516, 26.3401332611), (24.4556778666, 25.5444305835))
                Line((23.2716839786, 26.0733923457), (24.2354522516, 26.3401332611))
                Line((23.6717953517, 24.6277399362), (23.2716839786, 26.0733923457))
                CenterArc((-3.4180130765, 21.5220952055), 27.2672468333, -34.6984918722, 41.2384744229)
                CenterArc((-18.1282908933, 18.9153111637), 39.310497925, -19.1805540089, 23.8767033447)
                Line((20.2255473485, 23.3205712555), (21.0502374207, 22.1337216821))
                Line((20.2255473485, 23.3205712555), (19.4043359276, 22.7499472092))
                Line((20.2602719971, 21.5181300779), (19.4043359276, 22.7499472092))
                CenterArc((2.6731774411, 17.6144339123), 18.015125275, -48.9669659216, 61.4816563858)
                Line((13.5, 4.0250628145), (14.5, 4.0250628145))
            make_face()
            with BuildLine():
                CenterArc((13.1100115695, 10.6699652915), 7.7214277811, -83.3812538416, 23.6324053291)
                CenterArc((11.0612966026, 3.2193516987), 5.9897921344, -60.618751902, 68.1074014499)
                CenterArc((7.89648118, 0.5), 6.5956760068, -22.2739957228, 44.5479914457)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a complex geometric bracket or structural component featuring an irregular polyhedron shape with multiple angular faces, internal voids or cutouts, and protruding flanges, designed for assembly or mounting purposes.
def model_38454_24787d99_0003():
    """Model: Fron Foot"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4650000437, perimeter: 7.3071068901
            with BuildLine():
                Line((17.5000002608, 2.5000000373), (19.0000002831, 2.5000000373))
                Line((18.5000002757, 3.0000000447), (19.0000002831, 2.5000000373))
                Line((18.5000002757, 4.0000000596), (18.5000002757, 3.0000000447))
                Line((17.5000002608, 4.0000000596), (18.5000002757, 4.0000000596))
                Line((17.5000002608, 2.5000000373), (17.5000002608, 4.0000000596))
            make_face()
            with BuildLine():
                Line((17.8000002652, 3.3000000492), (18.2000002712, 3.3000000492))
                Line((17.8000002652, 3.7000000551), (17.8000002652, 3.3000000492))
                Line((18.2000002712, 3.7000000551), (17.8000002652, 3.7000000551))
                Line((18.2000002712, 3.3000000492), (18.2000002712, 3.7000000551))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((18.2000002712, 3.3000000492), (18.2000002712, 3.7000000551))
                Line((18.2000002712, 3.7000000551), (17.8000002652, 3.7000000551))
                Line((17.8000002652, 3.7000000551), (17.8000002652, 3.3000000492))
                Line((17.8000002652, 3.3000000492), (18.2000002712, 3.3000000492))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a tapered roller or conical shaft featuring a cylindrical body with longitudinal grooves or flutes running along its length and a larger hexagonal or flattened end section, commonly used in mechanical assemblies for power transmission or precise alignment.
def model_38739_f321c899_0005():
    """Model: Brake Pedal v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 57.2211797527, perimeter: 62.7597013989
            with BuildLine():
                Line((-0.0000000005, 0), (0, 21.59))
                CenterArc((1.2699999227, -0.0006256233), 1.2700000773, 179.971775139, 180.028224861)
                Line((2.54, -0.0006256233), (2.54, 12.2675743767))
                CenterArc((2.0827955053, 14.3256004431), 2.1082, -77.4747641115, 77.4747520684)
                Line((4.1909957776, 15.621), (4.1909955053, 14.3256))
                Line((1.905, 21.59), (4.1909957776, 15.621))
                Line((0, 21.59), (1.905, 21.59))
            make_face()
            with BuildLine():
                CenterArc((2.0827955053, 14.3256004431), 1.508125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2699999227, -0.0006256233), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a rectangular base plate with two angled flanges extending upward from opposite sides, forming a V-shaped or boat-like channel structure with triangular reinforcement webs connecting the internal surfaces.
def model_38739_f321c899_0008():
    """Model: ToePad v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 24 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.887093, perimeter: 12.0904
            with BuildLine():
                Line((5.715, 0), (5.715, -0.3302))
                Line((0, 0), (5.715, 0))
                Line((0, 0), (0, -0.3302))
                Line((5.715, -0.3302), (0, -0.3302))
            make_face()
            # Profile area: 0.2736688075, perimeter: 4.19735
            with BuildLine():
                Line((-5.715, 0.3302), (-5.5753, 0.3302))
                Line((-5.5753, 2.289175), (-5.5753, 0.3302))
                Line((-5.715, 2.289175), (-5.5753, 2.289175))
                Line((-5.715, 0.3302), (-5.715, 2.289175))
            make_face()
            # Profile area: 0.3659266875, perimeter: 5.51815
            with BuildLine():
                Line((5.715, 0.3302), (5.715, 0))
                Line((5.715, 0), (5.715, -0.3302))
                Line((5.715, -0.3302), (5.8547, -0.3302))
                Line((5.8547, -0.3302), (5.8547, 2.289175))
                Line((5.8547, 2.289175), (5.715, 2.289175))
                Line((5.715, 2.289175), (5.715, 0.3302))
            make_face()
            # Profile area: 1.887093, perimeter: 12.0904
            with BuildLine():
                Line((0, 0.3302), (0, 0))
                Line((0, 0), (5.715, 0))
                Line((5.715, 0.3302), (5.715, 0))
                Line((0, 0.3302), (5.715, 0.3302))
            make_face()
            # Profile area: 0.09225788, perimeter: 1.6002
            with BuildLine():
                Line((-5.715, -0.3302), (-5.715, 0.3302))
                Line((-5.5753, -0.3302), (-5.715, -0.3302))
                Line((-5.5753, 0.3302), (-5.5753, -0.3302))
                Line((-5.715, 0.3302), (-5.5753, 0.3302))
            make_face()
            # Profile area: 3.68192812, perimeter: 12.4714
            with BuildLine():
                Line((0, -0.3302), (-5.5753, -0.3302))
                Line((0, 0), (0, -0.3302))
                Line((0, 0.3302), (0, 0))
                Line((-5.5753, 0.3302), (0, 0.3302))
                Line((-5.5753, 0.3302), (-5.5753, -0.3302))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a hollow cylindrical or capsule-shaped component with a rounded oval cross-section, featuring a smooth curved surface with vertical ribbing or fluting patterns on its exterior.
def model_38739_f321c899_0010():
    """Model: 10-32 Bolt v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6640097489, perimeter: 2.8886316131
            Circle(0.45974)
        # OneSide extrude, distance=0.29464
        extrude(amount=0.29464)
    return part.part


# Description: This is a cylindrical sleeve or tube with a large circular opening or hole on one end, featuring a rounded rectangular body with smooth, curved transitions and what appears to be internal or external ribbing/texture along its length.
def model_38739_f321c899_0014():
    """Model: Bearing Bushing"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.395865218, perimeter: 4.9872783376
            with BuildLine():
                CenterArc((-0.2668669232, 3.460923971), 0.47625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.2668669232, 3.460923971), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.635
        extrude(amount=0.635, both=True)
    return part.part


# Description: This is a flat elliptical disk or plate with a smooth, curved edge and a uniformly dark surface, featuring no visible holes, slots, or protrusions.
def model_38740_c9ed5246_0001():
    """Model: Component6"""
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
            # Profile area: 6866.7253323419, perimeter: 293.7512815857
            with BuildLine():
                CenterArc((0, 0), 46.7519685039, -0.583331238, 1.166662476)
                CenterArc((0, 0), 46.7519685039, 0.583331238, 358.833337524)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.574522617, perimeter: 3.1613178614
            with BuildLine():
                _nurbs_edge([(46.7495455154, -0.4759759403), (46.8048836947, -0.4583333417), (46.9812879269, -0.4009656735), (47.2781056681, -0.298777718), (47.5174093036, -0.2084015248), (47.6375168163, -0.163041329)], [1, 1, 1, 1, 1, 1], [2.419287591, 2.419287591, 2.419287591, 2.419287591, 2.5935309317, 2.9757540577, 3.3608997146, 3.3608997146, 3.3608997146, 3.3608997146], 3)
                CenterArc((-0.0936933779, 0), 47.7314886535, -0.1957114363, 0.3914228727)
                _nurbs_edge([(46.7495455154, 0.4759759403), (46.8048836947, 0.4583333417), (46.9812879269, 0.4009656735), (47.2781056681, 0.298777718), (47.5174093036, 0.2084015248), (47.6375168163, 0.163041329)], [1, 1, 1, 1, 1, 1], [2.419287591, 2.419287591, 2.419287591, 2.419287591, 2.5935309317, 2.9757540577, 3.3608997146, 3.3608997146, 3.3608997146, 3.3608997146], 3)
                CenterArc((0, 0), 46.7519685039, -0.583331238, 1.166662476)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


# Description: This is a circular disc or wheel with a mesh or perforated rim section, featuring a large flat face and a textured edge band that appears to have a grid or lattice pattern around a portion of its circumference.
def model_38740_c9ed5246_0003():
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
            # Profile area: 402.4928200342, perimeter: 71.1187313313
            with BuildLine():
                CenterArc((0, 0), 11.3188976378, -2.2031797598, 4.4063595196)
                CenterArc((0, 0), 11.3188976378, 2.2031797598, 355.5936404804)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.5586181825, perimeter: 3.057318916
            with BuildLine():
                _nurbs_edge([(11.3105305327, -0.4351353859), (11.3191333053, -0.4337174049), (11.3692461313, -0.4251538985), (11.4608345199, -0.4071290096), (11.5848239521, -0.3766562394), (11.7088636536, -0.3411980636), (11.8328986853, -0.3010525461), (11.9568434058, -0.2564773996), (12.080774974, -0.2079780918), (12.1626163404, -0.1725963575), (12.203744513, -0.1548157882)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2222565622, 0.2222565622, 0.2222565622, 0.2222565622, 0.2483952499, 0.3746638673, 0.5022921237, 0.6312783944, 0.7616218896, 0.8933221423, 1.0263788383, 1.1607917466, 1.1607917466, 1.1607917466, 1.1607917466], 3)
                CenterArc((-0.0255927063, 0), 12.2303171158, -0.7252901203, 1.4505802406)
                _nurbs_edge([(11.3105305327, 0.4351353859), (11.3191333053, 0.4337174049), (11.3692461313, 0.4251538985), (11.4608345199, 0.4071290096), (11.5848239521, 0.3766562394), (11.7088636536, 0.3411980636), (11.8328986853, 0.3010525461), (11.9568434058, 0.2564773996), (12.080774974, 0.2079780918), (12.1626163404, 0.1725963575), (12.203744513, 0.1548157882)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2222565622, 0.2222565622, 0.2222565622, 0.2222565622, 0.2483952499, 0.3746638673, 0.5022921237, 0.6312783944, 0.7616218896, 0.8933221423, 1.0263788383, 1.1607917466, 1.1607917466, 1.1607917466, 1.1607917466], 3)
                CenterArc((0, 0), 11.3188976378, -2.2031797598, 4.4063595196)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


# Description: This is a knurled knob or dial featuring a cylindrical body with a textured knurled surface on the upper half for grip, a smooth flat circular face, and a small protruding pin or pointer on the side for rotational indication.
def model_38740_c9ed5246_0004():
    """Model: Component3"""
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
            # Profile area: 56.2729092055, perimeter: 26.5922212804
            with BuildLine():
                CenterArc((0, 0), 4.2322834646, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 4.2322834646, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.5205381827, perimeter: 2.834565713
            with BuildLine():
                Line((4.2187148687, 0.3386269058), (4.4251679432, 0.3551984372))
                CenterArc((0, 0), 4.2322834646, -4.5891664191, 9.1783328383)
                Line((4.2187148687, -0.3386269058), (4.4251679432, -0.3551984372))
                _nurbs_edge([(4.4251679432, -0.3551984372), (4.4505154681, -0.3547084118), (4.5016516477, -0.3537198331), (4.5781213589, -0.3413998179), (4.6549393344, -0.3249309153), (4.7319403541, -0.3036665082), (4.8090351852, -0.2784230679), (4.8861464554, -0.2493988888), (4.9631664625, -0.2167683545), (5.0401434929, -0.1809035093), (5.0907047647, -0.1545369181), (5.1161720923, -0.1412562669)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.075968201, 0.1532584969, 0.2318232643, 0.3116570743, 0.3927576934, 0.475123798, 0.5587544458, 0.6436488941, 0.7298065228, 0.7298065228, 0.7298065228, 0.7298065228], 3)
                CenterArc((-0.0303951976, 0), 5.1485054338, -1.5721851245, 3.144370249)
                _nurbs_edge([(4.4251679432, 0.3551984372), (4.4505154681, 0.3547084118), (4.5016516477, 0.3537198331), (4.5781213589, 0.3413998179), (4.6549393344, 0.3249309153), (4.7319403541, 0.3036665082), (4.8090351852, 0.2784230679), (4.8861464554, 0.2493988888), (4.9631664625, 0.2167683545), (5.0401434929, 0.1809035093), (5.0907047647, 0.1545369181), (5.1161720923, 0.1412562669)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.075968201, 0.1532584969, 0.2318232643, 0.3116570743, 0.3927576934, 0.475123798, 0.5587544458, 0.6436488941, 0.7298065228, 0.7298065228, 0.7298065228, 0.7298065228], 3)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated filter housing with a solid domed end cap and an open mesh-textured side, featuring a small protruding nozzle or connector on one side.
def model_38741_e08013e7_0002():
    """Model: Component11"""
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
            # Profile area: 2.1134888681, perimeter: 5.1535312559
            with BuildLine():
                CenterArc((0, 0), 0.8202099738, 6.8054379143, 346.3891241714)
                CenterArc((0, 0), 0.8202099738, -6.8054379143, 13.6108758286)
            make_face()
        # OneSide extrude, distance=1.000000032
        extrude(amount=1.000000032)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0546620001, perimeter: 0.9104152508
            with BuildLine():
                Line((0.8144309924, 0.0971934134), (0.9182846109, 0.1095872046))
                CenterArc((0, 0), 0.8202099738, -6.8054379143, 13.6108758286)
                Line((0.8144309924, -0.0971934134), (0.9182846109, -0.1095872046))
                _nurbs_edge([(0.9182846109, -0.1095872046), (0.9254259793, -0.1096159485), (0.9398745063, -0.1096741035), (0.9615504372, -0.106216063), (0.9833846498, -0.1013760231), (1.0053134206, -0.0949248669), (1.0272888036, -0.0871201426), (1.0492726204, -0.0780173292), (1.0712145047, -0.0676663694), (1.0931243505, -0.0561850932), (1.1074326835, -0.047686394), (1.1146541654, -0.0433970612)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213911057, 0.0432788157, 0.0656435775, 0.0884825085, 0.111794151, 0.1355775015, 0.1598317729, 0.1845563082, 0.2097505423, 0.2097505423, 0.2097505423, 0.2097505423], 3)
                CenterArc((-0.0175422086, 0), 1.1330277729, -2.1950713549, 4.3901427099)
                _nurbs_edge([(0.9182846109, 0.1095872046), (0.9254259793, 0.1096159485), (0.9398745063, 0.1096741035), (0.9615504372, 0.106216063), (0.9833846498, 0.1013760231), (1.0053134206, 0.0949248669), (1.0272888036, 0.0871201426), (1.0492726204, 0.0780173292), (1.0712145047, 0.0676663694), (1.0931243505, 0.0561850932), (1.1074326835, 0.047686394), (1.1146541654, 0.0433970612)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213911057, 0.0432788157, 0.0656435775, 0.0884825085, 0.111794151, 0.1355775015, 0.1598317729, 0.1845563082, 0.2097505423, 0.2097505423, 0.2097505423, 0.2097505423], 3)
            make_face()
        # OneSide extrude, distance=1.000000032
        extrude(amount=1.000000032, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical electric motor or rotor component with a solid end cap on one side and internal fan blades or cooling fins visible through the mesh pattern on the curved surface.
def model_38741_e08013e7_0003():
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
            # Profile area: 2.1134888681, perimeter: 5.1535312559
            with BuildLine():
                CenterArc((0, 0), 0.8202099738, 6.8054379143, 346.3891241714)
                CenterArc((0, 0), 0.8202099738, -6.8054379143, 13.6108758286)
            make_face()
        # OneSide extrude, distance=2.000000064
        extrude(amount=2.000000064)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0546620001, perimeter: 0.9104152508
            with BuildLine():
                Line((0.8144309924, 0.0971934134), (0.9182846109, 0.1095872046))
                CenterArc((0, 0), 0.8202099738, -6.8054379143, 13.6108758286)
                Line((0.8144309924, -0.0971934134), (0.9182846109, -0.1095872046))
                _nurbs_edge([(0.9182846109, -0.1095872046), (0.9254259793, -0.1096159485), (0.9398745063, -0.1096741035), (0.9615504372, -0.106216063), (0.9833846498, -0.1013760231), (1.0053134206, -0.0949248669), (1.0272888036, -0.0871201426), (1.0492726204, -0.0780173292), (1.0712145047, -0.0676663694), (1.0931243505, -0.0561850932), (1.1074326835, -0.047686394), (1.1146541654, -0.0433970612)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213911057, 0.0432788157, 0.0656435775, 0.0884825085, 0.111794151, 0.1355775015, 0.1598317729, 0.1845563082, 0.2097505423, 0.2097505423, 0.2097505423, 0.2097505423], 3)
                CenterArc((-0.0175422086, 0), 1.1330277729, -2.1950713549, 4.3901427099)
                _nurbs_edge([(0.9182846109, 0.1095872046), (0.9254259793, 0.1096159485), (0.9398745063, 0.1096741035), (0.9615504372, 0.106216063), (0.9833846498, 0.1013760231), (1.0053134206, 0.0949248669), (1.0272888036, 0.0871201426), (1.0492726204, 0.0780173292), (1.0712145047, 0.0676663694), (1.0931243505, 0.0561850932), (1.1074326835, 0.047686394), (1.1146541654, 0.0433970612)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213911057, 0.0432788157, 0.0656435775, 0.0884825085, 0.111794151, 0.1355775015, 0.1598317729, 0.1845563082, 0.2097505423, 0.2097505423, 0.2097505423, 0.2097505423], 3)
            make_face()
        # OneSide extrude, distance=2.000000064
        extrude(amount=2.000000064, mode=Mode.ADD)
    return part.part


# Description: This is a knurled knob or dial with a cylindrical body featuring a textured knurled surface on the curved section and a small protruding pointer or tab on the side for manual rotation and positioning.
def model_38741_e08013e7_0004():
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
            # Profile area: 2.1134888681, perimeter: 5.1535312559
            with BuildLine():
                CenterArc((0, 0), 0.8202099738, 6.8054379143, 346.3891241714)
                CenterArc((0, 0), 0.8202099738, -6.8054379143, 13.6108758286)
            make_face()
        # OneSide extrude, distance=0.500000016
        extrude(amount=0.500000016)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0546620001, perimeter: 0.9104152508
            with BuildLine():
                Line((0.8144309924, 0.0971934134), (0.9182846109, 0.1095872046))
                CenterArc((0, 0), 0.8202099738, -6.8054379143, 13.6108758286)
                Line((0.8144309924, -0.0971934134), (0.9182846109, -0.1095872046))
                _nurbs_edge([(0.9182846109, -0.1095872046), (0.9254259793, -0.1096159485), (0.9398745063, -0.1096741035), (0.9615504372, -0.106216063), (0.9833846498, -0.1013760231), (1.0053134206, -0.0949248669), (1.0272888036, -0.0871201426), (1.0492726204, -0.0780173292), (1.0712145047, -0.0676663694), (1.0931243505, -0.0561850932), (1.1074326835, -0.047686394), (1.1146541654, -0.0433970612)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213911057, 0.0432788157, 0.0656435775, 0.0884825085, 0.111794151, 0.1355775015, 0.1598317729, 0.1845563082, 0.2097505423, 0.2097505423, 0.2097505423, 0.2097505423], 3)
                CenterArc((-0.0175422086, 0), 1.1330277729, -2.1950713549, 4.3901427099)
                _nurbs_edge([(0.9182846109, 0.1095872046), (0.9254259793, 0.1096159485), (0.9398745063, 0.1096741035), (0.9615504372, 0.106216063), (0.9833846498, 0.1013760231), (1.0053134206, 0.0949248669), (1.0272888036, 0.0871201426), (1.0492726204, 0.0780173292), (1.0712145047, 0.0676663694), (1.0931243505, 0.0561850932), (1.1074326835, 0.047686394), (1.1146541654, 0.0433970612)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213911057, 0.0432788157, 0.0656435775, 0.0884825085, 0.111794151, 0.1355775015, 0.1598317729, 0.1845563082, 0.2097505423, 0.2097505423, 0.2097505423, 0.2097505423], 3)
            make_face()
        # OneSide extrude, distance=0.500000016
        extrude(amount=0.500000016, mode=Mode.ADD)
    return part.part


# Description: This is a elongated rectangular prism or bar stock with a uniform cross-section, featuring a slight trapezoidal profile and beveled edges, oriented at an angle.
def model_38953_19054857_0000():
    """Model: Burta I"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18, perimeter: 22
            with BuildLine():
                Line((-2.5, 9.5), (-0.5, 9.5))
                Line((-2.5, 0.5), (-2.5, 9.5))
                Line((-0.5, 0.5), (-2.5, 0.5))
                Line((-0.5, 9.5), (-0.5, 0.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a T-shaped wrench or toggle tool featuring a vertical shaft with a horizontal handle bar, commonly used as a hex key holder, drum key, or adjustable wrench-style tool with a simple tubular construction.
def model_39124_28e99e62_0002():
    """Model: Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 131.0251271652, perimeter: 138.9521179949
            with BuildLine():
                Line((-34, -10.4053028232), (-34, -12.4053028232))
                Line((-34, -12.4053028232), (-10.7377967941, -12.4053028232))
                Line((4.9999196949, -12.4053028216), (-10.7377967941, -12.4053028232))
                Line((5, -10.4053028232), (4.9999196949, -12.4053028216))
                Line((-9.7354873735, -10.4053028232), (5, -10.4053028232))
                Line((-9.7354873735, 16.5), (-9.7354873735, -10.4053028232))
                Line((-11.7354873735, 16.5), (-9.7354873735, 16.5))
                Line((-11.7354873735, -10.4053028232), (-11.7354873735, 16.5))
                Line((-11.7354873735, -10.4053028232), (-34, -10.4053028232))
            make_face()
            with BuildLine():
                CenterArc((-10.7354873735, 14.1946971768), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a long, slender angle or corner trim piece with a triangular/V-shaped cross-section, featuring a pointed tip at one end and a hollow channel running along its length, typically used for edge protection or structural reinforcement in assembly applications.
def model_39406_55dd02e2_0009():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.56, perimeter: 30
            with BuildLine():
                Line((1.2, 0), (1.2, 1.2))
                Line((1.2, 0), (15, 0))
                Line((15, 0), (15, 1.2))
                Line((15, 1.2), (1.2, 1.2))
            make_face()
            # Profile area: 16.56, perimeter: 30
            with BuildLine():
                Line((1.2, 15), (0, 15))
                Line((0, 15), (0, 1.2))
                Line((1.2, 1.2), (0, 1.2))
                Line((1.2, 1.2), (1.2, 15))
            make_face()
            # Profile area: 1.44, perimeter: 4.8
            with BuildLine():
                Line((1.2, 1.2), (0, 1.2))
                Line((0, 1.2), (0, 0))
                Line((0, 0), (1.2, 0))
                Line((1.2, 0), (1.2, 1.2))
            make_face()
        # Symmetric extrude, each_side=60
        extrude(amount=60, both=True)
    return part.part


# Description: This is a circular disc or plate with a textured/knurled rim edge, featuring a large flat central face and a small protruding tab or lug on one side.
def model_39468_15fb2e60_0001():
    """Model: Drive wheel"""
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
            # Profile area: 37.9154308177, perimeter: 21.8279489568
            with BuildLine():
                CenterArc((0, 0), 3.474025974, 1.6336090834, 356.7327818331)
                CenterArc((0, 0), 3.474025974, -1.6336090834, 3.2672181669)
            make_face()
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0566449452, perimeter: 0.9431934839
            with BuildLine():
                Line((3.4726140067, 0.0990375128), (3.6120189477, 0.103013284))
                CenterArc((0, 0), 3.474025974, -1.6336090834, 3.2672181669)
                Line((3.4726140067, -0.0990375128), (3.6120189477, -0.103013284))
                _nurbs_edge([(3.6120189477, -0.103013284), (3.6176881898, -0.1028779981), (3.629054311, -0.1026067666), (3.6460728227, -0.1009394422), (3.663110311, -0.09881124), (3.680157992, -0.0961597515), (3.6972141024, -0.0930869403), (3.7142766621, -0.0896231572), (3.7313420529, -0.0857942504), (3.7484155234, -0.0816475617), (3.7597592047, -0.0786264162), (3.7654438671, -0.0771124287)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0170070456, 0.0340969992, 0.0512670124, 0.0685168137, 0.0858463135, 0.1032554705, 0.1207442618, 0.1383126731, 0.1559606948, 0.1559606948, 0.1559606948, 0.1559606948], 3)
                CenterArc((0.0018603429, 0), 3.7643734233, -1.173774564, 2.3475491279)
                _nurbs_edge([(3.6120189477, 0.103013284), (3.6176881898, 0.1028779981), (3.629054311, 0.1026067666), (3.6460728227, 0.1009394422), (3.663110311, 0.09881124), (3.680157992, 0.0961597515), (3.6972141024, 0.0930869403), (3.7142766621, 0.0896231572), (3.7313420529, 0.0857942504), (3.7484155234, 0.0816475617), (3.7597592047, 0.0786264162), (3.7654438671, 0.0771124287)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0170070456, 0.0340969992, 0.0512670124, 0.0685168137, 0.0858463135, 0.1032554705, 0.1207442618, 0.1383126731, 0.1559606948, 0.1559606948, 0.1559606948, 0.1559606948], 3)
            make_face()
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)
    return part.part


# Description: This is a circular disk or wheel with a textured/knurled rim edge, featuring a flat face and a slight protrusion or hub on one side, likely designed for grip or assembly purposes.
def model_39468_15fb2e60_0002():
    """Model: Part13"""
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
            # Profile area: 35.6865963846, perimeter: 21.1766615909
            with BuildLine():
                CenterArc((0, 0), 3.3703703704, 1.9170584953, 356.1658830093)
                CenterArc((0, 0), 3.3703703704, -1.9170584953, 3.8341169907)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0733809523, perimeter: 1.0712871962
            with BuildLine():
                Line((3.3684839756, 0.1127481242), (3.5231620561, 0.1179254275))
                CenterArc((0, 0), 3.3703703704, -1.9170584953, 3.8341169907)
                Line((3.3684839756, -0.1127481242), (3.5231620561, -0.1179254275))
                _nurbs_edge([(3.5231620561, -0.1179254275), (3.5297928341, -0.1177671174), (3.5430930932, -0.1174495732), (3.5630039773, -0.1153578116), (3.582942352, -0.112673175), (3.6028958278, -0.1093144003), (3.6228613864, -0.1054114461), (3.6428359071, -0.1010024524), (3.6628139575, -0.0961199448), (3.6828025895, -0.0908241504), (3.6960736583, -0.0869615979), (3.7027270298, -0.0850251302)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0198902654, 0.0398966281, 0.0600150918, 0.0802452727, 0.1005870429, 0.1210403428, 0.1416051386, 0.162281409, 0.183069139, 0.183069139, 0.183069139, 0.183069139], 3)
                CenterArc((0.002249991, 0), 3.7014537128, -1.3162422155, 2.632484431)
                _nurbs_edge([(3.5231620561, 0.1179254275), (3.5297928341, 0.1177671174), (3.5430930932, 0.1174495732), (3.5630039773, 0.1153578116), (3.582942352, 0.112673175), (3.6028958278, 0.1093144003), (3.6228613864, 0.1054114461), (3.6428359071, 0.1010024524), (3.6628139575, 0.0961199448), (3.6828025895, 0.0908241504), (3.6960736583, 0.0869615979), (3.7027270298, 0.0850251302)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0198902654, 0.0398966281, 0.0600150918, 0.0802452727, 0.1005870429, 0.1210403428, 0.1416051386, 0.162281409, 0.183069139, 0.183069139, 0.183069139, 0.183069139], 3)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a structural bracket or frame component with an elongated trapezoidal base featuring internal ribbed/lattice reinforcement, a central void or opening, and angled side flanges for mounting or support applications.
def model_39637_ca6a9a60_0003():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7536504592, perimeter: 7.1707963268
            with BuildLine():
                Line((0.65, 0.75), (0.65, -0.75))
                Line((-0.65, 0.75), (0.65, 0.75))
                Line((-0.65, 0.75), (-0.65, -0.75))
                Line((0.65, -0.75), (-0.65, -0.75))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3, perimeter: 3.4
            with BuildLine():
                Line((0.65, -0.75), (0.85, -0.75))
                Line((0.85, -0.75), (0.85, 0.75))
                Line((0.85, 0.75), (0.65, 0.75))
                Line((0.65, 0.75), (0.65, -0.75))
            make_face()
            # Profile area: 0.3, perimeter: 3.4
            with BuildLine():
                Line((-0.85, 0.75), (-0.65, 0.75))
                Line((-0.85, -0.75), (-0.85, 0.75))
                Line((-0.65, -0.75), (-0.85, -0.75))
                Line((-0.65, 0.75), (-0.65, -0.75))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3, perimeter: 3.4
            with BuildLine():
                Line((0.65, -0.75), (0.85, -0.75))
                Line((0.85, -0.75), (0.85, 0.75))
                Line((0.85, 0.75), (0.65, 0.75))
                Line((0.65, 0.75), (0.65, -0.75))
            make_face()
            # Profile area: 0.3, perimeter: 3.4
            with BuildLine():
                Line((-0.85, 0.75), (-0.65, 0.75))
                Line((-0.85, -0.75), (-0.85, 0.75))
                Line((-0.65, -0.75), (-0.85, -0.75))
                Line((-0.65, 0.75), (-0.65, -0.75))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical socket or sleeve with a rounded end, featuring a hollow interior bore and uniform diameter throughout its length.
def model_40061_d07e8764_0002():
    """Model: Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5)

        # Sketch1 -> Extrude2 (Join)
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
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or spacer with a flanged head at the top, featuring a textured or knurled surface on the head and a smooth cylindrical shaft.
def model_40061_d07e8764_0017():
    """Model: Bolt_a"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-6.7
        extrude(amount=-6.7)

        # Sketch1 -> Extrude2 (Join)
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
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a suppressor or silencer with an elongated cylindrical body featuring a threaded attachment point at one end and a tapered muzzle end, designed to reduce firearm noise.
def model_40061_d07e8764_0018():
    """Model: Pivot_2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.5815778498, perimeter: 13.9340216976
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                Line((0.55, 0.5099019514), (0.55, -0.5099019514))
                CenterArc((0, 0), 0.75, -137.1665719339, 94.3331438679)
                Line((-0.55, -0.5099019514), (-0.55, 0.5099019514))
                CenterArc((0, 0), 0.75, 42.8334280661, 94.3331438679)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4870056208, perimeter: 4.5092437368
            with BuildLine():
                CenterArc((0, 0), 0.75, 42.8334280661, 94.3331438679)
                Line((-0.55, -0.5099019514), (-0.55, 0.5099019514))
                CenterArc((0, 0), 0.75, -137.1665719339, 94.3331438679)
                Line((0.55, 0.5099019514), (0.55, -0.5099019514))
            make_face()
        # OneSide extrude, distance=26
        extrude(amount=26, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or adapter with a tapered head featuring an angled top surface and internal cavity, likely designed for fluid transfer, pneumatic, or mechanical coupling applications.
def model_40061_d07e8764_0022():
    """Model: Bolt_b"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2023639218, perimeter: 2.8216287657
            with BuildLine():
                CenterArc((0, 0), 0.6, 54.3146652873, 71.3706694253)
                Line((-0.35, 0), (-0.35, 0.4873397172))
                CenterArc((0, 0), 0.35, 0, 180)
                Line((0.35, 0.4873397172), (0.35, 0))
            make_face()
            # Profile area: 0.2023639218, perimeter: 2.8216287657
            with BuildLine():
                CenterArc((0, 0), 0.35, -180, 180)
                Line((-0.35, -0.4873397172), (-0.35, 0))
                CenterArc((0, 0), 0.6, -125.6853347127, 71.3706694253)
                Line((0.35, 0), (0.35, -0.4873397172))
            make_face()
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 180)
                CenterArc((0, 0), 0.35, -180, 180)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 180)
                CenterArc((0, 0), 0.35, -180, 180)
            make_face()
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.ADD)
    return part.part


# Description: This is a curved automotive hood or bonnet panel with a tapered, aerodynamic profile featuring a central ridge and downward-facing flanges at both ends.
def model_40070_be9c502b_0016():
    """Model: skrzydlo przod v16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45, perimeter: 36.6569206467
            with BuildLine():
                Line((0, 0), (-15, 2))
                Line((-15, 2), (-15, 0))
                Line((0, -4), (-15, 0))
                Line((0, -4), (0, 0))
            make_face()
            # Profile area: 45, perimeter: 36.6569206467
            with BuildLine():
                Line((0, 0), (15, 2))
                Line((0, -4), (0, 0))
                Line((0, -4), (15, 0))
                Line((15, 2), (15, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical housing or sleeve component with a curved, tapered top surface and vertical ribbed reinforcement features along its sidewalls.
def model_40072_b44084ae_0015():
    """Model: laczenie v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            Circle(0.65)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cutting tool or insert with an elongated, tapered body featuring a sharp pointed tip on one end and a blue-coated cutting surface along its top edge, designed for machining operations.
def model_40176_01ed49ea_0003():
    """Model: Component24"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6237131351, perimeter: 10.2220516135
            with BuildLine():
                Line((0.9, 0.159), (1.5000000224, 0))
                Line((1.5000000224, 0), (2.8383235356, 0))
                CenterArc((2.8383235356, 1.0956254031), 1.0956254031, -90, 75.6996216794)
                Line((3.9, 0.825), (0.9, 0.825))
                Line((0.9, 0.744), (0.9, 0.825))
                Line((0, 0.744), (0.9, 0.744))
                Line((0, 0.744), (0, 0.159))
                Line((0, 0.159), (0.9, 0.159))
            make_face()
            with BuildLine():
                Line((0.6000000089, 0.5515), (0.2394246006, 0.5515))
                CenterArc((0.6000000089, 0.4515), 0.1, -90, 180)
                Line((0.2394246006, 0.3515), (0.6000000089, 0.3515))
                CenterArc((0.2394246006, 0.4515), 0.1, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.064
        extrude(amount=0.064)
    return part.part


# Description: This is a cylindrical connector or coupling with a rounded end cap, featuring multiple small holes or ports along its body and textured surface details, designed for fluid or pneumatic connections.
def model_40176_01ed49ea_0005():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3957904089, perimeter: 6.3837162721
            with BuildLine():
                CenterArc((0, 0), 0.57, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.446, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.092
        extrude(amount=2.092)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3012001957, perimeter: 4.8192031306
            with BuildLine():
                CenterArc((0, 0), 0.446, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.321, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a TIE fighter component or angular spacecraft part featuring a tall, tapered conical upper section that narrows to a point, connected to a broader polygonal base with geometric faceting and reinforcing struts or internal structural elements visible throughout.
def model_40352_a9774a3f_0007():
    """Model: bottomHingePlate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.1988117831, perimeter: 17.7234241584
            with BuildLine():
                Line((2.2536687434, 1.9532026047), (3.5248312566, 5.4127973953))
                CenterArc((3.048, 5.588), 0.508, -20.1748990292, 161.5150907751)
                Line((2.6513186448, 5.9053450842), (0.1113186448, 2.7303450842))
                CenterArc((0.508, 2.413), 0.508, 141.3401917459, 38.6598082541)
                Line((0, 2.413), (0, 0.508))
                CenterArc((0.508, 0.508), 0.508, 180, 90)
                Line((0.508, 0), (3.048, 0))
                CenterArc((3.048, 0.508), 0.508, -90, 154.9423845817)
                Line((3.2631529412, 0.9681882353), (2.5153470588, 1.3178117647))
                CenterArc((2.7305, 1.778), 0.508, 159.8251009708, 85.1172836109)
            make_face()
        # OneSide extrude, distance=0.238125
        extrude(amount=0.238125)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered, rounded end, featuring a smooth, uniform diameter along its length.
def model_40413_c590b4b4_0007():
    """Model: Plastic Housing v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0288567463, perimeter: 14.522954519
            with BuildLine():
                CenterArc((0, 0), 1.2954, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.016, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.537815
        extrude(amount=15.537815)
    return part.part


# Description: This is a hexagonal or diamond-shaped 3D solid with a pointed left end and a flattened right end, featuring faceted surfaces and internal geometric divisions indicated by visible edge lines.
def model_40500_6055e3d7_0002():
    """Model: guma skos v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.6313972081, perimeter: 32
            with BuildLine():
                Line((0, 0), (11, 0))
                Line((13.5, 4.3301270189), (11, 0))
                Line((2.5, 4.3301270189), (13.5, 4.3301270189))
                Line((0, 0), (2.5, 4.3301270189))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a satellite dish antenna featuring a large parabolic reflector surface with radial mesh ribbing, a central feed horn or probe extending perpendicular from the dish, and a curved rim for structural support.
def model_40513_89770261_0000():
    """Model: shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.9761035644, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 3.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)
    return part.part


# Description: This is a pentahedron or wedge-shaped solid with an irregular polygonal base, featuring a sloped top surface and multiple planar faces in varying shades of blue and dark gray.
def model_40705_5ff43505_0030():
    """Model: Servo2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.99, perimeter: 12.8
            with BuildLine():
                Line((0, 3.7), (0, 0))
                Line((0, 0), (2.7, 0))
                Line((2.7, 0), (2.7, 3.7))
                Line((2.7, 3.7), (0, 3.7))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a 3D boomerang or curved lever part with a bent angular shape, featuring two cylindrical rounded ends connected by straight segments that form a sharp chevron or "less-than" symbol (< ) profile.
def model_40705_5ff43505_0035():
    """Model: BracketR"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5295974187, perimeter: 7.1591565336
            with BuildLine():
                Line((-1.9582686831, 1.2511619019), (-0.3535533906, -0.3535533906))
                CenterArc((0, 0), 0.5, -135, 180)
                Line((0.3535533906, 0.3535533906), (-1.2302962434, 1.9374030246))
                Line((-1.2884875265, 1.7628291755), (-1.2302962434, 1.9374030246))
                CenterArc((-2, 2), 0.75, -45, 26.5650511771)
                CenterArc((-2, 2), 0.75, -86.8103148958, 41.8103148958)
            make_face()
            # Profile area: 0.4044945869, perimeter: 2.6021019972
            with BuildLine():
                Line((-1.2302962434, 1.9374030246), (-1.6464466094, 2.3535533906))
                CenterArc((-2, 2), 0.5, 45, 26.5650511771)
                Line((-2, 2), (-1.841886117, 2.474341649))
                Line((-1.4696699141, 1.4696699141), (-2, 2))
                CenterArc((-2, 2), 0.75, -45, 26.5650511771)
                Line((-1.2884875265, 1.7628291755), (-1.2302962434, 1.9374030246))
            make_face()
            # Profile area: 0.6796834701, perimeter: 3.6952148042
            with BuildLine():
                CenterArc((-2, 2), 0.75, -86.8103148958, 41.8103148958)
                Line((-1.4696699141, 1.4696699141), (-2, 2))
                Line((-2, 2), (-1.841886117, 2.474341649))
                CenterArc((-2, 2), 0.5, 71.5650511771, 145.2791938936)
                CenterArc((-1.6255809509, 2.3326877321), 1, -140.7645530626, 5.7645530626)
                Line((-2.3326877321, 1.6255809509), (-1.9582686831, 1.2511619019))
            make_face()
            # Profile area: 9.9132970152, perimeter: 17.4819588592
            with BuildLine():
                CenterArc((-2, 2), 0.5, 71.5650511771, 145.2791938936)
                CenterArc((-2, 2), 0.5, 45, 26.5650511771)
                Line((-1.2302962434, 1.9374030246), (-1.6464466094, 2.3535533906))
                Line((-1.2302962434, 1.9374030246), (0.7115124735, 7.7628291755))
                CenterArc((0, 8), 0.75, -18.4349488229, 180)
                Line((-0.7115124735, 8.2371708245), (-2.574264249, 2.6489154981))
                CenterArc((-1.6255809509, 2.3326877321), 1, 161.5650511771, 57.6703957604)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular duct or channel component with a hollow interior cavity, featuring angled end faces, side flanges or mounting ears, and a longitudinal slot or opening along its length.
def model_40723_f18d24a6_0012():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36.77505537, perimeter: 31.5578810164
            with BuildLine():
                Line((1.2276563931, 3.8099574791), (1.2978160668, -1.2119783421))
                CenterArc((3.8375682259, -1.1764963708), 2.54, -179.1995931772, 90.0361859228)
                Line((3.8746542048, -3.7162256142), (10.6543045432, -3.6172268844))
                Line((10.6543045432, -3.6172268844), (10.6543045432, -1.0772268844))
                Line((10.6543045432, -1.0772268844), (6.3426112514, -1.0772268844))
                CenterArc((6.3426112514, 1.4627731156), 2.54, -180, 90)
                Line((3.8026112514, 1.4627731156), (3.8026112514, 3.8099574791))
                Line((1.2276563931, 3.8099574791), (3.8026112514, 3.8099574791))
            make_face()
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)
    return part.part


# Description: This is a brake caliper assembly with an angular, multi-faceted body featuring two mounting flanges on the left side, a central cylindrical piston bore, and a curved upper surface with integrated cooling passages or relief features.
def model_40782_3383cd58_0004():
    """Model: Dzignia_trzymak v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.9133643693, perimeter: 27.2776223923
            with BuildLine():
                Line((5.4797958971, 1.2), (6.5, 1.2))
                Line((6.5, 1.2), (6.5, 2))
                Line((6.5, 2), (5.55, 2))
                CenterArc((4.5, 1), 1.45, 43.6028189727, 92.7943620546)
                Line((3.45, 2), (0, 2))
                Line((0, 2), (0, 1.375))
                Line((0, 1.375), (1.13, 1.375))
                Line((1.13, 1.375), (1.13, 0.625))
                Line((0, 0.625), (1.13, 0.625))
                Line((0, 0.625), (0, 0))
                Line((0, 0), (3.45, 0))
                CenterArc((4.5, 1), 1.45, -136.3971810273, 92.7943620546)
                Line((5.55, 0), (6.5, 0))
                Line((6.5, 0), (6.5, 0.8))
                Line((5.4797958971, 0.8), (6.5, 0.8))
                CenterArc((4.5, 1), 1, 11.5369590328, 336.9260819344)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical mesh or perforated filter cup with a solid dark base, featuring an open top with a mesh/screen surface and reinforced rim edges.
def model_40782_3383cd58_0005():
    """Model: Dzignia_lozysko v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1335176878, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)
    return part.part


# Description: A cylindrical rod or shaft with a slightly tapered or rounded end, featuring a uniform diameter along its length and a subtle taper at the top.
def model_40782_3383cd58_0021():
    """Model: Raczka v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


# Description: This is a polyhedron with an irregular, roughly cuboid shape featuring multiple flat faceted surfaces in varying shades of blue and dark gray, with no apparent holes, slots, or curved features—appearing to be a geometric solid composed of planar faces at different angles.
def model_40999_cad6be09_0008():
    """Model: Wheel 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 161.2899951553, perimeter: 50.7999992371
            with BuildLine():
                Line((-114.2999982834, 63.4999990463), (-126.9999980927, 63.4999990463))
                Line((-126.9999980927, 63.4999990463), (-126.9999980927, 50.7999992371))
                Line((-126.9999980927, 50.7999992371), (-114.2999982834, 50.7999992371))
                Line((-114.2999982834, 50.7999992371), (-114.2999982834, 63.4999990463))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


# Description: This is an angular, polyhedron-shaped structural component with multiple flat faceted surfaces in varying shades of blue and dark gray, featuring a complex geometric form composed of triangular and quadrilateral faces with no apparent holes or curved surfaces.
def model_40999_cad6be09_0009():
    """Model: Wheels"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 160.0008790824, perimeter: 50.59658156
            with BuildLine():
                Line((221.0363236568, 126.511544484), (221.0363240662, 113.862344484))
                Line((221.0363240662, 113.862344484), (233.6855240662, 113.8623448953))
                Line((233.6855236549, 126.5113264553), (233.6855240662, 113.8623448953))
                Line((221.0363236568, 126.511544484), (233.6855236549, 126.5113264553))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


# Description: This is a mummy-style sleeping bag featuring a tapered, cocoon-shaped design with a rounded foot section, a narrow shoulder area, and a drawstring hood at the head end for thermal efficiency and weather protection.
def model_41010_212b5129_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((1.25, 0), 1.25, 0, 180)
                Line((0, 0), (2.5, 0))
            make_face()
            # Profile area: 18.75, perimeter: 20
            with BuildLine():
                Line((0, 0), (2.5, 0))
                Line((0, -7.5), (0, 0))
                Line((2.5, -7.5), (0, -7.5))
                Line((2.5, 0), (2.5, -7.5))
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((1.25, -7.5), 1.25, 180, 180)
                Line((2.5, -7.5), (0, -7.5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is an elongated hexagonal prism or coffin-shaped box with tapered ends, featuring a faceted top surface with angular planes and slight geometric complexity along its length.
def model_41026_295d1dc8_0008():
    """Model: Component20"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(12.7000004053, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 32.1680396376, perimeter: 22.8316660112
            with BuildLine():
                Line((-1.2700000405, 1.2700000405), (-7.62, 1.2700000405))
                Line((-1.2700000405, 6.3358330867), (-1.2700000405, 1.2700000405))
                Line((-7.62, 6.3358330867), (-1.2700000405, 6.3358330867))
                Line((-7.62, 6.3358330867), (-7.62, 1.2700000405))
            make_face()
        # OneSide extrude, distance=30.48
        extrude(amount=30.48)
    return part.part


# Description: This is a knife blade or cutting tool holder featuring an elongated, tapered body with a curved cutting edge, a mounting hole at the upper end, and a dark finish typical of hardened steel or tool steel components.
def model_41031_57b1ef09_0001():
    """Model: Saw Blade"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.5112428612, perimeter: 15.5464753942
            with BuildLine():
                Line((-6.1477476224, 0.8644448596), (-1.6695169702, 1.1999999957))
                CenterArc((-6.1440115812, 0.8145846351), 0.05, 94.2851817462, 65.3328867141)
                Line((-6.5, 0), (-6.1908811745, 0.8319984578))
                Line((-0.6, 0), (-6.5, 0))
                CenterArc((-0.6, 0.6), 0.6, -90, 180)
                Line((-1.6695169702, 1.1999999957), (-0.6, 1.2))
            make_face()
            with BuildLine():
                CenterArc((-0.6, 0.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a toroidal (doughnut-shaped) mesh or perforated ring featuring a solid base band at the bottom and an open mesh or latticed structure on the upper portion, creating a lightweight, ventilated ring component.
def model_41124_a5855c0d_0003():
    """Model: Union Seat"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
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
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rubber or elastomer belt/ring with a circular torus shape, featuring a braided or textured reinforced outer surface, designed for use as a drive belt, sealing ring, or mechanical coupling component.
def model_41124_a5855c0d_0005():
    """Model: Exterior Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.3044239038, perimeter: 51.5221195189
            with BuildLine():
                CenterArc((0, 0), 4.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.3097335529, perimeter: 56.5486677646
            with BuildLine():
                CenterArc((0, 0), 4.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or sleeve with an open top, featuring a mesh or perforated grid panel on the upper section and vertical slot or channel details along its sides.
def model_41125_711db4bf_0030():
    """Model: balance_bar_weight v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1789380461, perimeter: 2.9823007676
            with BuildLine():
                CenterArc((-0.125, -0.075), 0.17, 180, 90)
                Line((-0.125, -0.245), (0.125, -0.245))
                CenterArc((0.125, -0.075), 0.17, -90, 90)
                Line((0.295, -0.075), (0.295, 0.075))
                CenterArc((0.125, 0.075), 0.17, 0, 90)
                Line((0.125, 0.245), (-0.125, 0.245))
                CenterArc((-0.125, 0.075), 0.17, 90, 90)
                Line((-0.295, 0.075), (-0.295, -0.075))
            make_face()
            with BuildLine():
                Line((-0.125, -0.125), (0.125, -0.125))
                CenterArc((-0.125, -0.075), 0.05, 180, 90)
                Line((-0.175, 0.075), (-0.175, -0.075))
                CenterArc((-0.125, 0.075), 0.05, 90, 90)
                Line((0.125, 0.125), (-0.125, 0.125))
                CenterArc((0.125, 0.075), 0.05, 0, 90)
                Line((0.175, -0.075), (0.175, 0.075))
                CenterArc((0.125, -0.075), 0.05, -90, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0853539816, perimeter: 1.1141592654
            with BuildLine():
                CenterArc((0.125, -0.075), 0.05, -90, 90)
                Line((0.175, -0.075), (0.175, 0.075))
                CenterArc((0.125, 0.075), 0.05, 0, 90)
                Line((0.125, 0.125), (-0.125, 0.125))
                CenterArc((-0.125, 0.075), 0.05, 90, 90)
                Line((-0.175, 0.075), (-0.175, -0.075))
                CenterArc((-0.125, -0.075), 0.05, 180, 90)
                Line((-0.125, -0.125), (0.125, -0.125))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0853539816, perimeter: 1.1141592654
            with BuildLine():
                CenterArc((0.125, -0.075), 0.05, -90, 90)
                Line((0.175, -0.075), (0.175, 0.075))
                CenterArc((0.125, 0.075), 0.05, 0, 90)
                Line((0.125, 0.125), (-0.125, 0.125))
                CenterArc((-0.125, 0.075), 0.05, 90, 90)
                Line((-0.175, 0.075), (-0.175, -0.075))
                CenterArc((-0.125, -0.075), 0.05, 180, 90)
                Line((-0.125, -0.125), (0.125, -0.125))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical foam roller with a textured, mesh-patterned surface and slightly tapered rounded ends, designed for muscle recovery and massage applications.
def model_41128_ee74f244_0019():
    """Model: 16-handle shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.6609615365, perimeter: 6.7826985391
            with Locations((-7.1217271586, 5.3367146559)):
                Circle(1.0795)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a cylindrical sleeve or tube with a smooth, rounded end cap on one side and textured surface detailing along its length, featuring a uniform hollow bore throughout.
def model_41142_1bf94ee2_0005():
    """Model: Cone v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3048358038, perimeter: 1.9572122232
            Circle(0.3115)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a J-shaped or hook-shaped bracket with two perpendicular rectangular sections connected at a right angle, featuring beveled or chamfered edges at both ends and a hollow tubular construction.
def model_41211_11f6b8a0_0000():
    """Model: coffeepothandle"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.9031841112, perimeter: 30.4800005836
            with BuildLine():
                Line((-10.6680003891, 12.4460003972), (-8.3820002675, 12.4460003972))
                Line((-8.3820002675, 12.4460003972), (-8.3820002675, 13.9700004458))
                Line((-8.3820002675, 13.9700004458), (-12.1920003891, 13.9700004458))
                Line((-12.1920003891, 13.9700004458), (-12.1920003891, 4.8260003972))
                Line((-12.1920003891, 4.8260003972), (-8.3820002675, 4.8260003972))
                Line((-8.3820002675, 4.8260003972), (-8.3820002675, 6.3500002027))
                Line((-8.3820002675, 6.3500002027), (-10.6680003891, 6.3500002027))
                Line((-10.6680003891, 12.4460003972), (-10.6680003891, 6.3500002027))
            make_face()
        # Symmetric extrude, each_side=1.016
        extrude(amount=1.016, both=True)
    return part.part


# Description: This is a cylindrical housing or drum with a solid flat end face and a curved, ribbed or finned section on the opposite end, featuring a mesh-like structural pattern that suggests internal ribbing or cooling fins.
def model_41234_74275eb0_0006():
    """Model: Support Displays"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((94.8735518454, 8.6270717169)):
                Circle(1.905)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a hexagonal cylindrical component with a large central circular bore and a rectangular slot or cutout on the top surface, featuring a hollow interior cavity.
def model_41473_c2137170_0022():
    """Model: clamp_nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3141612887, perimeter: 4.5082678703
            with BuildLine():
                Line((20.2181367451, 34.5928763163), (20.4616478251, 34.9853501209))
                Line((20.4616478251, 34.9853501209), (20.24351108, 35.3924738045))
                Line((20.24351108, 35.3924738045), (19.7818632549, 35.4071236837))
                Line((19.7818632549, 35.4071236837), (19.5383521749, 35.0146498791))
                Line((19.5383521749, 35.0146498791), (19.75648892, 34.6075261955))
                Line((19.75648892, 34.6075261955), (20.2181367451, 34.5928763163))
            make_face()
            with BuildLine():
                CenterArc((20, 35), 0.27645, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical or curved container/vessel with a curved sidewall and an open top featuring a radial ribbed or flange pattern around the rim.
def model_41474_57d78888_0008():
    """Model: bear"""
    with BuildPart() as part:
        # Sketch2 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078849323, perimeter: 0.3628049657
            with BuildLine():
                CenterArc((0.8252264606, -1.2510358017), 0.0658090813, 133.8440660504, 202.6198464168)
                CenterArc((1.0000000149, -1.0000000149), 0.3, -137.2676230383, 24.8432245941)
            make_face()
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)
    return part.part


# Description: This is a cylindrical sleeve or tube with a dark gray finish, featuring a slightly tapered or rounded top end and textured surface details along its length.
def model_41501_b627682a_0018():
    """Model: Pivot-Long v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a roofing nail gun nozzle or attachment piece featuring a blue triangular base with a sloped profile and a dark gray rectangular head mounted at an angled orientation on top.
def model_41501_b627682a_0030():
    """Model: Gear Stand v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.208449852, perimeter: 2.2867135849
            with BuildLine():
                CenterArc((0, 0.2999999933), 0.0999999978, -129.8055710923, 79.6111421845)
                Line((-0.5000000075, -0.1500000022), (-0.0640184385, 0.2231778671))
                Line((-0.5000000075, -0.1500000022), (0.5000000075, -0.1500000022))
                Line((0.0640184385, 0.2231778671), (0.5000000075, -0.1500000022))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159251, perimeter: 0.6283185167
            with BuildLine():
                CenterArc((0, 0.2999999933), 0.0999999978, -50.1944289077, 280.3888578155)
                CenterArc((0, 0.2999999933), 0.0999999978, -129.8055710923, 79.6111421845)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal prism or elongated hex-shaped structural component with tapered or beveled ends, featuring a hollow or chamfered interior core running lengthwise through its center.
def model_41504_ed0ad3ae_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 184.784014077, perimeter: 64.5869516681
            with BuildLine():
                Line((12.6999998093, -6.3499999046), (12.6999998093, 0))
                Line((12.6999998093, 0), (5.0799999237, -1.2699999809))
                Line((5.0799999237, -1.2699999809), (2.6733024894, -0.4579609058))
                Line((2.6733024894, -0.4579609058), (-12.5255223295, -0.8639804434))
                Line((-12.5255223295, -0.8639804434), (-10.1599998474, -10.1599998474))
                Line((-10.1599998474, -10.1599998474), (12.6999998093, -6.3499999046))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a cylindrical sleeve or collar with an elliptical cross-section, featuring a solid dark lower body and a mesh-textured upper rim or flange that appears slightly tilted or angled relative to the base.
def model_41508_f30b6f68_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-1.5, 1)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rubber or plastic grip sleeve with a tapered, cylindrical shape featuring a rounded end cap and a textured or ribbed surface pattern along its length.
def model_41512_c1a779f2_0001():
    """Model: big knife v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9051971927, perimeter: 5.5402629236
            with BuildLine():
                Line((-5, 3), (-5, 1.5))
                Line((-3.7298685382, 1.5), (-5, 1.5))
                Line((-3.7298685382, 3), (-3.7298685382, 1.5))
                Line((-5, 3), (-3.7298685382, 3))
            make_face()
        # Symmetric extrude, each_side=0.08
        extrude(amount=0.08, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.7806647084, perimeter: 13.2189600595
            with BuildLine():
                Line((-3.7298685382, 1.5), (1.5966977429, 1.5))
                CenterArc((0.5, 1.8490846869), 1.1509153131, -17.6565477406, 107.6565477406)
                Line((-3.7298685382, 3), (0.5, 3))
                Line((-3.7298685382, 3), (-3.7298685382, 1.5))
            make_face()
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal-profile steel rod or shaft with a uniform cross-section and chamfered or beveled ends, designed for fastening or mechanical assembly applications.
def model_41520_60018d18_0005():
    """Model: Component18"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 232.2576148247, perimeter: 60.9600019455
            with BuildLine():
                Line((30.4800009727, 15.2400004864), (30.4800009727, 0))
                Line((15.2400004864, 15.2400004864), (30.4800009727, 15.2400004864))
                Line((15.2400004864, 0), (15.2400004864, 15.2400004864))
                Line((30.4800009727, 0), (15.2400004864, 0))
            make_face()
        # OneSide extrude, distance=304.8
        extrude(amount=304.8)
    return part.part


# Description: This is a rectangular base plate or mounting bracket with multiple parallel vertical fins or ribs extending from one side, featuring through-holes or slots along its length for fastening or structural support.
def model_41648_577daf16_0001():
    """Model: Camera Mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 49 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1112251015, perimeter: 1.6418056167
            with BuildLine():
                Line((-2.101015013, -0.6897869721), (-2.75, -0.6897869721))
                CenterArc((-1.8739583413, -0.5851673382), 0.25, 163.4056828888, 41.3328854019)
                Line((-2.75, -0.5137690095), (-2.1135460677, -0.5137690095))
                Line((-2.75, -0.6897869721), (-2.75, -0.5137690095))
            make_face()
            # Profile area: 0.1036310898, perimeter: 1.6791017559
            with BuildLine():
                Line((-1.75, -0.5137690095), (-1.75, -0.3680629172))
                Line((-2.1135460677, -0.5137690095), (-1.75, -0.5137690095))
                CenterArc((-1.8739583413, -0.5851673382), 0.25, 163.4056828888, 41.3328854019)
                Line((-1.75, -0.6897869721), (-2.101015013, -0.6897869721))
                Line((-1.75, -0.8022717592), (-1.75, -0.6897869721))
                CenterArc((-1.8739583413, -0.5851673382), 0.25, -60.2752816059, 120.5505632118)
            make_face()
            # Profile area: 9.2705419721, perimeter: 41.2333848723
            with BuildLine():
                Line((-2.75, 0), (-1.75, 0))
                Line((-2.75, -0.2137690095), (-2.75, 0))
                Line((-1.75, -0.2137690095), (-2.75, -0.2137690095))
                Line((-1.75, -0.3680629172), (-1.75, -0.2137690095))
                CenterArc((-1.8739583413, -0.5851673382), 0.25, -60.2752816059, 120.5505632118)
                Line((-1.75, -0.9897869721), (-1.75, -0.8022717592))
                Line((-2.75, -0.9897869721), (-1.75, -0.9897869721))
                Line((-2.75, -1.2), (-2.75, -0.9897869721))
                Line((-1.75, -1.2), (-2.75, -1.2))
                Line((-1.75, -1.5), (-1.75, -1.2))
                Line((-2.75, -1.5), (-1.75, -1.5))
                CenterArc((-2.25, -1.5), 0.5, 180, 90)
                Line((2.25, -2), (-2.25, -2))
                CenterArc((2.25, -1.5), 0.5, -90, 90)
                Line((2.75, 1.5), (2.75, -1.5))
                CenterArc((2.25, 1.5), 0.5, 0, 90)
                Line((-2.25, 2), (2.25, 2))
                CenterArc((-2.25, 1.5), 0.5, 90, 90)
                Line((-2.75, 1.3296688174), (-2.75, 1.5))
                Line((-2.75, 1.3296688174), (-1.75, 1.3296688174))
                Line((-1.75, 1.3296688174), (-1.75, 1.0296688174))
                Line((-1.75, 1.0296688174), (-2.75, 1.0296688174))
                Line((-2.75, 0.7691009838), (-2.75, 1.0296688174))
                Line((-1.75, 0.7691009838), (-2.75, 0.7691009838))
                Line((-1.75, 0.4691009838), (-1.75, 0.7691009838))
                Line((-2.75, 0.4691009838), (-1.75, 0.4691009838))
                Line((-2.75, 0.3), (-2.75, 0.4691009838))
                Line((-1.75, 0.3), (-2.75, 0.3))
                Line((-1.75, 0), (-1.75, 0.3))
            make_face()
            with BuildLine():
                Line((-1.4947907751, -1.5416660183), (2.0052092249, -1.5416660183))
                Line((-1.4947907751, 1.4583339817), (-1.4947907751, -1.5416660183))
                Line((2.0052092249, 1.4583339817), (-1.4947907751, 1.4583339817))
                Line((2.0052092249, -1.5416660183), (2.0052092249, 1.4583339817))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 49 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.3743362939, perimeter: 14.2566370614
            with BuildLine():
                Line((2.0052092249, -1.5416660183), (2.0052092249, 1.4583339817))
                Line((2.0052092249, 1.4583339817), (-1.4947907751, 1.4583339817))
                Line((-1.4947907751, 1.4583339817), (-1.4947907751, -1.5416660183))
                Line((-1.4947907751, -1.5416660183), (2.0052092249, -1.5416660183))
            make_face()
            with BuildLine():
                CenterArc((-0.070496546, -0.4716647785), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)
    return part.part


# Description: A horizontal cylindrical rod or shaft with rounded ends and a slightly tapered or beveled edge profile.
def model_41648_577daf16_0013():
    """Model: Small Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1017760705, perimeter: 4.1482476527
            with BuildLine():
                CenterArc((0, 0), 0.6, 9.4748566538, 160.996989143)
                Line((-0.5917226285, 0.0993193383), (-0.5000000075, 0.0993193383))
                Line((-0.5000000075, 0.0993193383), (-0.5000000075, -0.0500000007))
                Line((-0.5000000075, -0.0500000007), (-0.5979130371, -0.0500000007))
                CenterArc((0, 0), 0.6, -175.2198080814, 170.4396161628)
                Line((0.5000000075, -0.0500000007), (0.5979130371, -0.0500000007))
                Line((0.5000000075, 0.0987688645), (0.5000000075, -0.0500000007))
                Line((0.5918147611, 0.0987688645), (0.5000000075, 0.0987688645))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a hexagonal prism or hex-shaped geometric solid with triangulated faceting on its left side, featuring a combination of flat faces and angular surface divisions that create a faceted, crystalline appearance.
def model_41648_577daf16_0014():
    """Model: Leg Bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8136805462, perimeter: 5.4053930313
            with BuildLine():
                Line((0.65, -0.55), (0.65, 0.9937090687))
                CenterArc((0.55, 0.9937090687), 0.1, 0, 114.7751405688)
                Line((0.5080941823, 1.0845050072), (-0.5919058177, 0.5768126995))
                CenterArc((-0.55, 0.4860167611), 0.1, 114.7751405688, 65.2248594312)
                Line((-0.65, -0.55), (-0.65, 0.4860167611))
                Line((0.65, -0.55), (-0.65, -0.55))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a cylindrical sleeve or tube with rounded ends and a longitudinal slot or cutout running along one side of its length.
def model_41653_71b50655_0002():
    """Model: Latch Piece 2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 2.1424777961
            with BuildLine():
                Line((0, 0), (0, -0.6))
                CenterArc((0, 0), 0.6, -90, 90)
                Line((0, 0), (0.6, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a curved automotive door panel or fender component with a streamlined, aerodynamic shape featuring a smooth convex surface and a textured edge detail along one side.
def model_41672_5407972e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36.1371669412, perimeter: 25.4247779608
            with BuildLine():
                Line((7.5, -0.5), (7.5, -1.5))
                CenterArc((4.5, -0.5), 3, 0, 90)
                Line((0.5, 2.5), (4.5, 2.5))
                CenterArc((0.5, -0.5), 3, 90, 90)
                Line((-2.5, -1.5), (-2.5, -0.5))
                Line((7.5, -1.5), (-2.5, -1.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a hexagonal prism or elongated box-shaped part with beveled/chamfered edges on the top corners and ends, featuring a faceted top surface with triangular subdivisions and a flat rectangular base.
def model_41696_de0790a1_0001():
    """Model: base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 156.9029220149, perimeter: 54.8640017509
            with BuildLine():
                Line((-9.652000308, 4.0640001297), (9.652000308, 4.0640001297))
                Line((-9.652000308, -4.0640001297), (-9.652000308, 4.0640001297))
                Line((9.652000308, -4.0640001297), (-9.652000308, -4.0640001297))
                Line((9.652000308, 4.0640001297), (9.652000308, -4.0640001297))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a rectangular box or housing with a recessed rectangular pocket or slot cut into one side, featuring a hollow interior cavity and angular geometric surfaces with multiple faces and edges.
def model_41714_1d49f4d1_0001():
    """Model: letter_n"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0789594121, perimeter: 2.224825514
            with BuildLine():
                Line((-4.749800154, 3.8100001216), (-4.749800154, 4.2011064961))
                Line((-4.749800154, 4.2011064961), (-5.1562001621, 4.2011064961))
                Line((-5.1562001621, 4.2011064961), (-5.1562001621, 3.8100001216))
                Line((-5.0800001621, 3.8100001216), (-5.1562001621, 3.8100001216))
                Line((-5.0800001621, 4.1249064961), (-5.0800001621, 3.8100001216))
                Line((-4.826000154, 4.1249064961), (-5.0800001621, 4.1249064961))
                Line((-4.826000154, 3.8100001216), (-4.826000154, 4.1249064961))
                Line((-4.749800154, 3.8100001216), (-4.826000154, 3.8100001216))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a wedge-shaped or tapered prismatic component with a rectangular base that slopes upward on one end, featuring a flat top surface and angled side faces, commonly used as a support block, shim, or positioning wedge in assemblies.
def model_41714_1d49f4d1_0018():
    """Model: Component33"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 48.3870030885, perimeter: 27.9400008917
            with BuildLine():
                Line((15.2400004864, 1.2700000405), (7.6200002432, 1.2700000405))
                Line((7.6200002432, 1.2700000405), (7.6200002432, -5.0800001621))
                Line((7.6200002432, -5.0800001621), (15.2400004864, -5.0800001621))
                Line((15.2400004864, -5.0800001621), (15.2400004864, 1.2700000405))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is an elliptical composite or reinforced panel featuring a curved, streamlined shape with radial internal ribs or stringers running from the center to the perimeter for structural reinforcement, and a raised outer flange or rim around its circumference.
def model_41717_ab2075ac_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or gasket with a rounded rectangular cross-section, featuring a hollow central opening and a textured or meshed surface pattern on the outer edges.
def model_41717_eb1c1e6b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 223.178742111, perimeter: 139.4867138194
            with BuildLine():
                CenterArc((0, 0), 12.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 9.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a sheet metal bracket or mounting component with a trapezoidal main body, two perpendicular flanges extending upward at opposite ends, and an angular, asymmetrical design typical of a support or mounting bracket used in industrial assemblies.
def model_41729_b5092135_0006():
    """Model: Holder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6505382387, perimeter: 16.9053823869
            with BuildLine():
                Line((0, -1.5), (3.5, -1.5))
                Line((3.5, -1.5), (6, 1))
                Line((5.8585786438, 1.1414213562), (6, 1))
                Line((3.4171572875, -1.3), (5.8585786438, 1.1414213562))
                Line((0.2, -1.3), (3.4171572875, -1.3))
                Line((0.2, 0), (0.2, -1.3))
                Line((0, 0), (0.2, 0))
                Line((0, 0), (0, -1.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a tapered or beveled left end, featuring a flat rectangular base and angled top surfaces with internal diagonal ribbing or reinforcement features.
def model_41733_1ec9b00c_0002():
    """Model: arm rest 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 53.75, perimeter: 30.7531245119
            with BuildLine():
                Line((0, -0.5), (0, 4.75))
                Line((-10, 5), (0, 4.75))
                Line((-10, -0.5), (-10, 5))
                Line((0, -0.5), (-10, -0.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a composite connector or junction piece featuring two triangular pyramid-shaped sections joined to a rectangular base, creating a distinctive angular, bifurcated structure with faceted surfaces.
def model_41733_1ec9b00c_0020():
    """Model: cubicle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12491.1650483087, perimeter: 1304.9704637596
            with BuildLine():
                Line((-68.1638649278, -163.7639865005), (-68.1638649278, 75))
                Line((-50, -175), (-68.1638649278, -163.7639865005))
                Line((100, -175), (-50, -175))
                Line((117.6599016329, -162.2330120008), (100, -175))
                Line((117.6599016329, 75), (117.6599016329, -162.2330120008))
                Line((100, 75), (117.6599016329, 75))
                Line((100, -150), (100, 75))
                Line((-50, -150), (100, -150))
                Line((-50, 75), (-50, -150))
                Line((-68.1638649278, 75), (-50, 75))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a long, tapered tubular body featuring rounded ends and a slightly textured surface finish.
def model_41739_1bc15d9f_0006():
    """Model: Pedal Pipe 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7747301555, perimeter: 5.9049375517
            Circle(0.9398)
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)
    return part.part


# Description: This is a flat parallelogram or rhombus-shaped plate with a shallow rectangular border/frame and internal diagonal cross-bracing, featuring a slightly beveled or angled edge on one side.
def model_41744_5c450f9d_0001():
    """Model: puzzle_board v4"""
    with BuildPart() as part:
        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 258.064, perimeter: 203.2
            with BuildLine():
                Line((-16.51, -11.43), (16.51, -11.43))
                Line((16.51, -11.43), (16.51, 11.43))
                Line((16.51, 11.43), (-16.51, 11.43))
                Line((-16.51, 11.43), (-16.51, -11.43))
            make_face()
            with BuildLine():
                Line((-13.97, -8.89), (13.97, -8.89))
                Line((-13.97, 8.89), (-13.97, -8.89))
                Line((13.97, 8.89), (-13.97, 8.89))
                Line((13.97, -8.89), (13.97, 8.89))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 496.7732, perimeter: 91.44
            with BuildLine():
                Line((13.97, -8.89), (13.97, 8.89))
                Line((13.97, 8.89), (-13.97, 8.89))
                Line((-13.97, 8.89), (-13.97, -8.89))
                Line((-13.97, -8.89), (13.97, -8.89))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a mounting bracket or adapter plate featuring an elongated oval disc body with a small cylindrical protrusion or tab extending from one edge, designed for fastening or positioning applications.
def model_41780_da6cd1db_0010():
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
            # Profile area: 1.6135568935, perimeter: 4.5029494701
            with BuildLine():
                CenterArc((0, 0), 0.7166666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 0.7166666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0149257962, perimeter: 0.4799864607
            with BuildLine():
                Line((0.7143690511, 0.0573408227), (0.7493284384, 0.0601469354))
                CenterArc((0, 0), 0.7166666667, -4.5891664191, 9.1783328383)
                Line((0.7143690511, -0.0573408227), (0.7493284384, -0.0601469354))
                _nurbs_edge([(0.7493284384, -0.0601469354), (0.7536206193, -0.0600639577), (0.762279679, -0.0598965584), (0.7752285501, -0.0578103692), (0.788236394, -0.055021635), (0.8012752333, -0.0514208621), (0.814329958, -0.0471463062), (0.8273874665, -0.0422315452), (0.840429521, -0.036706108), (0.8534642981, -0.0306329942), (0.8620260068, -0.0261682515), (0.8663384743, -0.0239193945)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0128639487, 0.0259517721, 0.0392554061, 0.0527739312, 0.0665069694, 0.0804542965, 0.0946157528, 0.1089912127, 0.1235805712, 0.1235805712, 0.1235805712, 0.1235805712], 3)
                CenterArc((-0.0051469201, 0), 0.8718135868, -1.5721851245, 3.144370249)
                _nurbs_edge([(0.7493284384, 0.0601469354), (0.7536206193, 0.0600639577), (0.762279679, 0.0598965584), (0.7752285501, 0.0578103692), (0.788236394, 0.055021635), (0.8012752333, 0.0514208621), (0.814329958, 0.0471463062), (0.8273874665, 0.0422315452), (0.840429521, 0.036706108), (0.8534642981, 0.0306329942), (0.8620260068, 0.0261682515), (0.8663384743, 0.0239193945)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0128639487, 0.0259517721, 0.0392554061, 0.0527739312, 0.0665069694, 0.0804542965, 0.0946157528, 0.1089912127, 0.1235805712, 0.1235805712, 0.1235805712, 0.1235805712], 3)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical ring or band component with an oval/elliptical cross-section, featuring an internal ribbed or latticed reinforcement structure visible through cutout sections on the top surface.
def model_41785_e15d763c_0000():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.1311604971, perimeter: 8.7776098741
            Circle(1.397)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a disc or diaphragm component with an elliptical/oval shape, featuring a central dark slot or opening running along its length and radial ribbing or striations extending outward from the center, creating a reinforced, spoke-like structural pattern.
def model_41868_42350264_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5585166327, perimeter: 12.8805298797
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.015
        extrude(amount=0.015, mode=Mode.ADD)
    return part.part


# Description: This is an elliptical or oval-shaped dish with a ribbed internal framework consisting of radial ribs and concentric rings that provide structural support, featuring a curved perimeter flange or rim around the outer edge.
def model_41868_df8c70ca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0498892065, perimeter: 27.3318560862
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch1 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2332961007, perimeter: 24.1902634326
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075, mode=Mode.ADD)
    return part.part


# Description: This is a thin-walled, elongated diamond or rhombus-shaped plate with a shallow depth, featuring a tapered profile that narrows toward one end and includes subtle ribbing or internal reinforcement features on its upper surface.
def model_41903_21ab17c0_0000():
    """Model: Case Base v4"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3122.5744, perimeter: 223.52
            with BuildLine():
                Line((55.88, -55.88), (0, -55.88))
                Line((55.88, 0), (55.88, -55.88))
                Line((0, 0), (55.88, 0))
                Line((0, -55.88), (0, 0))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a utility knife or box cutter blade featuring an elongated curved body with a sharp pointed tip, a blue metallic upper surface, a black handle grip section, and a slot opening for blade retention.
def model_41907_7bcecdb1_0007():
    """Model: Short Knife"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5941471794, perimeter: 11.4598308239
            with BuildLine():
                CenterArc((2.0000000112, 2.0000000391), 2.5000000186, 126.8698974324, 53.130102781)
                Line((-0.5000000075, 2.0000000298), (-0.5, -0.0000000019))
                CenterArc((0, 0), 0.5, -179.9999997866, 180)
                Line((0.5000000075, 4.0000000596), (0.5, 0.0000000019))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)
    return part.part


# Description: This is a cylindrical shell or ring-like component with an elliptical or oval cross-section, featuring a curved sidewall and an open top with a mesh or latticed internal structure visible on the upper surface.
def model_41930_2e5f07db_0002():
    """Model: Black Dial"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2429278662, perimeter: 6.3837162721
            Circle(1.016)
        # Symmetric extrude, each_side=0.381
        extrude(amount=0.381, both=True)
    return part.part


# Description: This is a cylindrical cap or end cover with a mesh or perforated pattern on the curved side surface and a solid flat circular face, featuring a domed or slightly rounded top profile.
def model_41938_1c6ad017_0005():
    """Model: Wheel 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((0.0764447157, -1.6842705814)):
                Circle(0.175)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a boat hull or kayak component featuring an elongated, tapered oval shape with a curved top surface, internal ribbed reinforcement structure (visible in blue), and a flat bottom base.
def model_41941_79d46bb4_0000():
    """Model: iron base"""
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
            # Profile area: 5.232655208, perimeter: 8.6823253131
            with BuildLine():
                _nurbs_edge([(22.2250007093, -14.8590004742), (22.2417497688, -14.7780142515), (22.2716236816, -14.6168171808), (22.3055619664, -14.3773478712), (22.3289788139, -14.062725501), (22.3214646916, -13.6782757989), (22.2768934994, -13.3055761689), (22.1954485224, -12.9503997927), (22.0781205352, -12.6221872161), (21.9271324359, -12.3353274992), (21.7463087421, -12.1091922407), (21.5411406168, -11.9631428523), (21.318927937, -11.912382156), (21.0889917359, -11.9630981048), (20.8627937089, -12.1083657243), (20.6525645766, -12.3330809864), (20.4699943266, -12.618217418), (20.3249855971, -12.9449302579), (20.2240657645, -13.2992279607), (20.1708483397, -13.6719106956), (20.1669536834, -14.0573396686), (20.2035406986, -14.373586452), (20.2531749889, -14.6147515586), (20.2960881456, -14.7772904885), (20.3200006485, -14.8590004742)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((20.3200006485, -14.8590004742), (22.2250007093, -14.8590004742))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring a slight taper or rounded edges at both ends and a smooth, featureless surface throughout its length.
def model_41943_c6aa8bc9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539819, perimeter: 0.31415927
            Circle(0.0500000007)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9)
    return part.part


# Description: This is a circular disk or wheel with a textured/knurled rim edge and a small rectangular tab or lug protruding from the side, featuring a smooth flat face and a beveled or curved outer edge.
def model_41948_c0d68e8c_0001():
    """Model: Smal sun gear"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 3, 39.5883004515, 354)
                CenterArc((0, 0), 3, 33.5883004515, 6)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1408198294, perimeter: 1.5354233322
            with BuildLine():
                CenterArc((0, 0), 3, 33.5883004515, 6)
                Line((2.7134874382, 1.818812645), (2.4991026705, 1.6596643765))
                Line((2.869669758, 2.0555703552), (2.7134874382, 1.818812645))
                Line((2.7981424463, 2.1519230598), (2.869669758, 2.0555703552))
                Line((2.5263149255, 2.0709481915), (2.7981424463, 2.1519230598))
                Line((2.3119301577, 1.911799923), (2.5263149255, 2.0709481915))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a torus-shaped ring or tire with a circular cross-section, featuring a textured or patterned surface on the outer diameter and a smooth inner bore, commonly used as a seal, gasket, or O-ring component.
def model_41948_c0d68e8c_0005():
    """Model: Ring Gear"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 91.8915851175, perimeter: 122.52211349
            with BuildLine():
                CenterArc((0, 0), 10.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 9, 34.9483434591, 357.85)
                CenterArc((0, 0), 9, 32.7983434591, 2.15)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1589641015, perimeter: 1.6282375107
            with BuildLine():
                CenterArc((0, 0), 9, 32.7983434591, 2.15)
                Line((7.1553369708, 5.0067242507), (7.3770195101, 5.1555390743))
                Line((6.967700811, 4.7496621537), (7.1553369708, 5.0067242507))
                Line((7.0345838778, 4.6500295517), (6.967700811, 4.7496621537))
                Line((7.3435578462, 4.726340344), (7.0345838778, 4.6500295517))
                Line((7.5652403856, 4.8751551677), (7.3435578462, 4.726340344))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a tweezers or forceps tool with an elongated, tapered body featuring a dark gray exterior and blue accent strip, designed with a pointed tip for precision gripping or handling of small objects.
def model_41970_24ba0c1b_0008():
    """Model: Knife"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8599720529, perimeter: 21.8780646256
            with BuildLine():
                CenterArc((0, 0), 0.5000000076, 126.320643967, 180.0140806891)
                Line((0.2962507597, -0.4027846755), (0.2962507597, -0.2299140869))
                CenterArc((0, 0), 0.375, 0.1021650149, 322.0835358036)
                Line((0.3749994038, 0.0006686681), (8.9926420975, 0.514751338))
                CenterArc((8.892982693, 0.5229977367), 0.1, -4.7302099012, 84.1292978649)
                Line((7.5166864357, 0.8823236495), (8.9113793927, 0.6212909788))
                Line((-0.2961517648, 0.4028574684), (7.5166864357, 0.8823236495))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.499893681, perimeter: 18.2420319418
            with BuildLine():
                Line((0.2962507597, -0.4027846755), (7.9960480523, -0.4027846755))
                CenterArc((7.9960480523, 0.5972153245), 1, -90, 85.2697900988)
                Line((0.3749994038, 0.0006686681), (8.9926420975, 0.514751338))
                CenterArc((0, 0), 0.375, -37.8142991815, 37.9164641964)
                Line((0.2962507597, -0.4027846755), (0.2962507597, -0.2299140869))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with a dark gray body and blue mesh top surface, featuring a closed bottom and open mesh construction for filtering or ventilation purposes.
def model_41970_24ba0c1b_0009():
    """Model: Scissor Pivot"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a cylindrical rod or tube with a uniform hollow circular cross-section, featuring a slightly tapered or rounded top end and a straight, elongated body angled diagonally.
def model_42042_e61e4667_0002():
    """Model: redbarb v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.12, perimeter: 4.9
            with BuildLine():
                Line((-0.5, 0.5), (-0.5, -0.5))
                Line((-0.5, -0.5), (0.5, -0.5))
                Line((0.5, -0.5), (0.5, -0.45))
                Line((0.5, -0.45), (0.45, -0.45))
                Line((0.45, -0.45), (-0.45, -0.45))
                Line((-0.45, -0.45), (-0.45, 0.45))
                Line((-0.45, 0.45), (0, 0.45))
                Line((0, 0.45), (0, 0.5))
                Line((0, 0.5), (-0.5, 0.5))
            make_face()
            # Profile area: 0.07, perimeter: 2.9
            with BuildLine():
                Line((0, 0.45), (0, 0.5))
                Line((0, 0.45), (0.45, 0.45))
                Line((0.45, 0.45), (0.45, -0.45))
                Line((0.5, -0.45), (0.45, -0.45))
                Line((0.5, -0.45), (0.5, 0.5))
                Line((0.5, 0.5), (0, 0.5))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a cylindrical tube or rod with a uniform diameter and smooth surface, featuring a slightly tapered or rounded end at the top.
def model_42042_e61e4667_0003():
    """Model: greenbarb v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1675, perimeter: 6.8
            with BuildLine():
                Line((-0.45, -0.45), (-0.45, 0.45))
                Line((-0.45, 0.45), (0.45, 0.45))
                Line((0.45, 0.45), (0.45, 0))
                Line((0.45, 0), (0.5, 0))
                Line((0.5, 0.5), (0.5, 0))
                Line((-0.5, 0.5), (0.5, 0.5))
                Line((-0.5, -0.5), (-0.5, 0.5))
                Line((0.5, -0.5), (-0.5, -0.5))
                Line((0.5, -0.5), (0.5, -0.45))
                Line((0.5, -0.45), (0.45, -0.45))
                Line((0.45, -0.45), (-0.45, -0.45))
            make_face()
            # Profile area: 0.0225, perimeter: 1
            with BuildLine():
                Line((0.5, -0.45), (0.45, -0.45))
                Line((0.5, 0), (0.5, -0.45))
                Line((0.45, 0), (0.5, 0))
                Line((0.45, 0), (0.45, -0.45))
            make_face()
        # OneSide extrude, distance=27
        extrude(amount=27)
    return part.part


# Description: This is a mesh filter or strainer cap featuring a cylindrical body with a solid bottom section and mesh/perforated sides, designed to allow fluid or air flow while blocking particles.
def model_42329_df7f540f_0038():
    """Model: Pistao (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0603185789, perimeter: 1.5079644737
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.02136283, perimeter: 2.1362830044
            with BuildLine():
                CenterArc((0, 0), 0.18, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02)
    return part.part


# Description: This is a torus or ring-shaped seal/gasket with a circular cross-section and a smooth, curved toroidal geometry, featuring a continuous loop design with no breaks or additional features.
def model_42329_df7f540f_0076():
    """Model: O-ring Piston (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0452389342, perimeter: 2.2619467106
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.01
        extrude(amount=0.01, both=True)
    return part.part


# Description: This is a pentagonal or wedge-shaped structural component featuring a dark ribbed/fluted face on one side, a flat panel surface on another, and a light blue triangulated or faceted top surface, with clean angular edges and geometric construction lines visible throughout.
def model_42333_53c85dac_0043():
    """Model: Gear_Large_3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0204326615, perimeter: 0.5868470976
            with BuildLine():
                CenterArc((0, 0), 1.575, 88.8637872112, 2.2724255777)
                CenterArc((0.74, 1.248), 0.837570404, 157.0426876311, 12.2545873775)
                CenterArc((0, 0), 1.406, 86.6157068903, 6.7685862193)
                CenterArc((-0.74, 1.248), 0.837570404, 10.7027249914, 12.2545873775)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered, rounded top end and a hollow interior, appearing to be a seamless metal or composite component.
def model_42429_5c0a47d5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1669032122, perimeter: 1.4726248864
            with BuildLine():
                CenterArc((0, 0), 0.23875, 40.5361216294, 278.9277567413)
                Line((0.1814491347, 0.1551701454), (0.1814491347, -0.1551701454))
            make_face()
            # Profile area: 0.0121724778, perimeter: 0.6481661873
            with BuildLine():
                Line((0.1814491347, 0.1551701454), (0.1814491347, -0.1551701454))
                CenterArc((0, 0), 0.23875, -40.5361216294, 81.0722432587)
            make_face()
        # OneSide extrude, distance=1.82626
        extrude(amount=1.82626)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0121724778, perimeter: 0.6481661873
            with BuildLine():
                Line((0.1814491347, 0.1551701454), (0.1814491347, -0.1551701454))
                CenterArc((0, 0), 0.23875, -40.5361216294, 81.0722432587)
            make_face()
        # OneSide extrude, distance=0.47752
        extrude(amount=0.47752, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hammer or mallet consisting of a rounded, textured cylindrical head with a long handle extending horizontally from one side.
def model_42429_78ffab1b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1875956541, perimeter: 4.9872783376
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=4.1402
        extrude(amount=4.1402, mode=Mode.ADD)
    return part.part


# Description: These are two identical cylindrical rollers or pins with a slightly tapered or rounded end design, commonly used as support rollers, guide pins, or mechanical fasteners in machinery or assemblies.
def model_42586_517832f9_0016():
    """Model: Handle (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((-38.0999994278, 0)):
                Circle(1.905)
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((7.6200005722, 0)):
                Circle(1.905)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a cylindrical sleeve or tube with a curved, tapered top edge and vertical ribbed or fluted surface texture running along its length.
def model_42601_bfe96b47_0000():
    """Model: Blade Sleeve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6478292514, perimeter: 26.5590242934
            with BuildLine():
                CenterArc((0, 0), 2.2885, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.9385, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.15
        extrude(amount=6.15)
    return part.part


# Description: This is a rectangular box-shaped enclosure or housing with an open top, featuring ventilation slots or ribbed patterns on its sides and a curved or domed upper edge design.
def model_43529_4804941b_0026():
    """Model: Solid30_tuerca union"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0774021508, perimeter: 2.6422776544
            with BuildLine():
                CenterArc((0, 0), 1.2, -119.9999993496, 59.9999987314)
                Line((-0.5999999882, -1.0392304914), (0, -1.3856406461))
                Line((0, -1.3856406461), (0.5999999888, -1.039230491))
            make_face()
            # Profile area: 2.5132741229, perimeter: 12.5663706018
            with BuildLine():
                CenterArc((0, 0), 1.2, -60.0000006182, 59.9999998391)
                CenterArc((0, 0), 1.2, -0.0000007791, 60.0000013364)
                CenterArc((0, 0), 1.2, 60.0000005573, 59.9999996927)
                CenterArc((0, 0), 1.2, 120.00000025, 59.99999975)
                CenterArc((0, 0), 1.2, -179.9999994016, 60.0000000519)
                CenterArc((0, 0), 1.2, -119.9999993496, 59.9999987314)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0774021508, perimeter: 2.6422777096
            with BuildLine():
                Line((-0.6000000045, 1.0392304819), (-1.2, 0.692820323))
                Line((-1.2, 0.692820323), (-1.2, -0.0000000125))
                CenterArc((0, 0), 1.2, 120.00000025, 59.99999975)
            make_face()
            # Profile area: 0.0774021508, perimeter: 2.6422776946
            with BuildLine():
                Line((0.5999999899, 1.0392304904), (0, 1.3856406461))
                Line((0, 1.3856406461), (-0.6000000045, 1.0392304819))
                CenterArc((0, 0), 1.2, 60.0000005573, 59.9999996927)
            make_face()
            # Profile area: 0.0774021508, perimeter: 2.6422777635
            with BuildLine():
                Line((1.2, -0.0000000163), (1.2, 0.692820323))
                Line((1.2, 0.692820323), (0.5999999899, 1.0392304904))
                CenterArc((0, 0), 1.2, -0.0000007791, 60.0000013364)
            make_face()
            # Profile area: 0.0774021508, perimeter: 2.6422777097
            with BuildLine():
                CenterArc((0, 0), 1.2, -179.9999994016, 60.0000000519)
                Line((-1.2, -0.0000000125), (-1.2, -0.692820323))
                Line((-1.2, -0.692820323), (-0.5999999882, -1.0392304914))
            make_face()
            # Profile area: 0.0774021508, perimeter: 2.6422777008
            with BuildLine():
                Line((0.5999999888, -1.039230491), (1.2, -0.692820323))
                Line((1.2, -0.692820323), (1.2, -0.0000000163))
                CenterArc((0, 0), 1.2, -60.0000006182, 59.9999998391)
            make_face()
        # TwoSides extrude (symmetric), distance=0.65
        extrude(amount=0.65, both=True)
    return part.part


# Description: This is a cylindrical container or housing with a rectangular cross-section, featuring a slotted or mesh panel on one side, an open top with a raised lip or flange, and tapered end caps, commonly used as a protective enclosure or filter housing.
def model_43529_4804941b_0028():
    """Model: solid28_tubo hexagonal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0774021508, perimeter: 2.6422776544
            with BuildLine():
                CenterArc((0, 0), 1.2, -119.9999993496, 59.9999987314)
                Line((-0.5999999882, -1.0392304914), (0, -1.3856406461))
                Line((0, -1.3856406461), (0.5999999888, -1.039230491))
            make_face()
            # Profile area: 2.5132741229, perimeter: 12.5663706018
            with BuildLine():
                CenterArc((0, 0), 1.2, -60.0000006182, 59.9999998391)
                CenterArc((0, 0), 1.2, -0.0000007791, 60.0000013364)
                CenterArc((0, 0), 1.2, 60.0000005573, 59.9999996927)
                CenterArc((0, 0), 1.2, 120.00000025, 59.99999975)
                CenterArc((0, 0), 1.2, -179.9999994016, 60.0000000519)
                CenterArc((0, 0), 1.2, -119.9999993496, 59.9999987314)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0774021508, perimeter: 2.6422777096
            with BuildLine():
                Line((-0.6000000045, 1.0392304819), (-1.2, 0.692820323))
                Line((-1.2, 0.692820323), (-1.2, -0.0000000125))
                CenterArc((0, 0), 1.2, 120.00000025, 59.99999975)
            make_face()
            # Profile area: 0.0774021508, perimeter: 2.6422776946
            with BuildLine():
                Line((0.5999999899, 1.0392304904), (0, 1.3856406461))
                Line((0, 1.3856406461), (-0.6000000045, 1.0392304819))
                CenterArc((0, 0), 1.2, 60.0000005573, 59.9999996927)
            make_face()
            # Profile area: 0.0774021508, perimeter: 2.6422777635
            with BuildLine():
                Line((1.2, -0.0000000163), (1.2, 0.692820323))
                Line((1.2, 0.692820323), (0.5999999899, 1.0392304904))
                CenterArc((0, 0), 1.2, -0.0000007791, 60.0000013364)
            make_face()
            # Profile area: 0.0774021508, perimeter: 2.6422777097
            with BuildLine():
                CenterArc((0, 0), 1.2, -179.9999994016, 60.0000000519)
                Line((-1.2, -0.0000000125), (-1.2, -0.692820323))
                Line((-1.2, -0.692820323), (-0.5999999882, -1.0392304914))
            make_face()
            # Profile area: 0.0774021508, perimeter: 2.6422777008
            with BuildLine():
                Line((0.5999999888, -1.039230491), (1.2, -0.692820323))
                Line((1.2, -0.692820323), (1.2, -0.0000000163))
                CenterArc((0, 0), 1.2, -60.0000006182, 59.9999998391)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a polyhedron or geometric box-shaped component with an irregular hexagonal or octagonal form, featuring multiple planar faceted surfaces and triangular and polygonal faces with some mesh or lattice-textured regions creating a complex, faceted geometric structure.
def model_43628_a95b7e66_0021():
    """Model: M2 nut v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0725071219, perimeter: 1.8283185307
            with BuildLine():
                Line((-0.1, -0.1732050808), (0.1, -0.1732050808))
                Line((0.1, -0.1732050808), (0.2, 0))
                Line((0.2, 0), (0.1, 0.1732050808))
                Line((0.1, 0.1732050808), (-0.1, 0.1732050808))
                Line((-0.1, 0.1732050808), (-0.2, 0))
                Line((-0.2, 0), (-0.1, -0.1732050808))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a parallelogram-shaped box or housing with a slanted, trapezoidal profile, featuring flat front and back faces and angled side walls that create a wedge-like 3D form.
def model_43934_912ff891_0010():
    """Model: Crankrod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((1, -0.5), (1, 0.5))
                Line((1, 0.5), (-1, 0.5))
                Line((-1, 0.5), (-1, -0.5))
                Line((-1, -0.5), (1, -0.5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: A parallelogram-shaped flat plate or panel with a slightly tapered 3D form, featuring clean edges and a uniform thickness with no holes or slots visible.
def model_43934_912ff891_0027():
    """Model: Steam Chest Cover v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.4, perimeter: 15.2
            with BuildLine():
                Line((1.8, -2), (1.8, 2))
                Line((1.8, 2), (-1.8, 2))
                Line((-1.8, 2), (-1.8, -2))
                Line((-1.8, -2), (1.8, -2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved tubular structural beam or pipe with a hexagonal cross-section, featuring a triangulated lattice pattern on its surface, designed to provide strength while minimizing weight.
def model_44021_f141414b_0001():
    """Model: Handle v17"""
    with BuildPart() as part:
        # Sketch9 -> Extrude6 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 38, perimeter: 43.8378165389
            with BuildLine():
                CenterArc((3.975276337, -31.7060500806), 34.7211746746, 88.3087879902, 32.8695496925)
                Line((-14, -4), (-14, -2))
                CenterArc((3.975276337, -33.7060500806), 34.7211746746, 88.3087879902, 32.8695496925)
                Line((5, 1), (5, 3))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)
    return part.part


# Description: This is a hexagonal or elongated prismatic component with a tapered, faceted top surface featuring multiple triangular facets and internal ribbing or bracing, combined with a solid dark base section, suggesting a lightweight structural part or aerospace component.
def model_44211_88463ca8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64.9519052838, perimeter: 30
            with BuildLine():
                Line((5, 0), (0, 0))
                Line((0, 0), (-2.5, -4.3301270189))
                Line((-2.5, -4.3301270189), (0, -8.6602540378))
                Line((0, -8.6602540378), (5, -8.6602540378))
                Line((5, -8.6602540378), (7.5, -4.3301270189))
                Line((7.5, -4.3301270189), (5, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a satellite component featuring a central cylindrical or box-shaped body with two large rectangular solar panel wings extending in opposite directions, connected by a central hub structure with internal geometric framing.
def model_44223_74bf8b6f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.5673101382, perimeter: 64.8638687089
            with BuildLine():
                CenterArc((7.5, -6.25), 1.25, -90, 180)
                Line((3.1180339887, -5), (7.5, -5))
                CenterArc((3.1180339887, -4), 1, -153.4349488229, 63.4349488229)
                Line((0, 0), (2.2236067977, -4.4472135955))
                Line((0, 0), (-0.2236067977, 0))
                Line((-0.2236067977, 0), (2.1, -4.6472135955))
                CenterArc((2.994427191, -4.2), 1, -153.4349488229, 63.4349488229)
                Line((2.994427191, -5.2), (7.3, -5.2))
                Line((7.3, -5.2), (7.3, -7.3))
                Line((7.3, -7.3), (0.5603418117, -7.3))
                CenterArc((0.5603418117, -8.3), 1, 90, 70.0168934781)
                Line((-0.3794516118, -7.9582569369), (-2.2128127256, -13))
                Line((-2, -13), (-2.2128127256, -13))
                Line((-0.2393661589, -8.1582569369), (-2, -13))
                CenterArc((0.7004272646, -8.5), 1, 90, 70.0168934781)
                Line((4.1363949847, -7.5), (0.7004272646, -7.5))
                CenterArc((4.1363949847, -8.5), 1, 24.4439547804, 65.5560452196)
                Line((5.0467614622, -8.0861970557), (7.280308255, -13))
                Line((7.5, -13), (7.280308255, -13))
                Line((5.642637702, -8.9138029443), (7.5, -13))
                CenterArc((6.5530041794, -8.5), 1, 90, 114.4439547804)
                Line((7.5, -7.5), (6.5530041794, -7.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a blue and dark gray composite part with an aerodynamic, elongated shape featuring a curved pillow-block or bearing housing on the right end and a flat mounting base on the left, designed for mechanical assembly or motion applications.
def model_44441_63f1bade_0003():
    """Model: Ball joint 2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.42, perimeter: 3.4
            with BuildLine():
                Line((-0.88, 0), (-2.28, 0))
                Line((-0.88, 0.2), (-0.88, 0))
                Line((-0.88, 0.3), (-0.88, 0.2))
                Line((-2.28, 0.3), (-0.88, 0.3))
                Line((-2.28, 0), (-2.28, 0.3))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3507984941, perimeter: 3.0607873897
            with BuildLine():
                Line((-0.88, 0), (0.4, 0))
                CenterArc((0, 0), 0.4, 0, 150)
                Line((-0.88, 0.2), (-0.3464101615, 0.2))
                Line((-0.88, 0.2), (-0.88, 0))
            make_face()
        # Symmetric extrude, each_side=0.175
        extrude(amount=0.175, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical container or sleeve with a flat top surface and curved sides, featuring a simple geometric form with no visible holes, slots, or flanges.
def model_44519_90af0df6_0018():
    """Model: Component74"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.907342772, perimeter: 12.2324193153
            with Locations((70, 50)):
                Circle(1.94685)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a gradually narrowing diameter that transitions from a thicker upper end to a pointed lower end, commonly used as a drift pin, taper pin, or alignment tool.
def model_44522_a7c79550_0007():
    """Model: Component36"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2, 5)):
                Circle(0.3)
        # OneSide extrude, distance=18.3
        extrude(amount=18.3)
    return part.part


# Description: This is a rectangular box or housing with a triangular flange or wedge extension on the left side, featuring internal diagonal bracing and structural ribbing throughout for reinforcement.
def model_44545_8f5b08e7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch13 -> Extrude7 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.0293015153, perimeter: 22.2509923055
            with BuildLine():
                Line((-10, 5.0655171325), (-7.1858238153, 0))
                Line((-12.5, 0), (-10, 5.0655171325))
                Line((-12.1356549951, 0), (-12.5, 0))
                Line((-10, 4.5), (-12.1356549951, 0))
                Line((-7.5, 0), (-10, 4.5))
                Line((-7.1858238153, 0), (-7.5, 0))
            make_face()
        # OneSide extrude, distance=9.1427
        extrude(amount=9.1427)
    return part.part


# Description: This is a cylindrical knurled knob or wheel featuring a smooth flat face on one side and a textured knurled surface on the opposite side for grip.
def model_44999_3e76c729_0000():
    """Model: Gear 1"""
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
            # Profile area: 68.8451804788, perimeter: 29.4131612192
            with BuildLine():
                CenterArc((0, 0), 4.68125, -2.3449905753, 4.6899811506)
                CenterArc((0, 0), 4.68125, 2.3449905753, 355.3100188494)
            make_face()
        # OneSide extrude, distance=2.9
        extrude(amount=2.9)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.11005806, perimeter: 1.3543559087
            with BuildLine():
                _nurbs_edge([(4.6773298006, -0.1915398093), (4.686686326, -0.1902048439), (4.7137164475, -0.1857510671), (4.7583318064, -0.1769188875), (4.8111062086, -0.1638519435), (4.8639038837, -0.1486319644), (4.9167002618, -0.1313865908), (4.9694573548, -0.1122262595), (5.0222082436, -0.0913683772), (5.0570350402, -0.0761458482), (5.0745387639, -0.0684951031)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0773544043, 0.0773544043, 0.0773544043, 0.0773544043, 0.1056992534, 0.1594520863, 0.2137978689, 0.268735884, 0.3242657805, 0.3803873485, 0.4371004457, 0.4944049664, 0.4944049664, 0.4944049664, 0.4944049664], 3)
                CenterArc((-0.0111068635, 0), 5.0861068635, -0.7716312427, 1.5432624854)
                _nurbs_edge([(4.6773298006, 0.1915398093), (4.686686326, 0.1902048439), (4.7137164475, 0.1857510671), (4.7583318064, 0.1769188875), (4.8111062086, 0.1638519435), (4.8639038837, 0.1486319644), (4.9167002618, 0.1313865908), (4.9694573548, 0.1122262595), (5.0222082436, 0.0913683772), (5.0570350402, 0.0761458482), (5.0745387639, 0.0684951031)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0773544043, 0.0773544043, 0.0773544043, 0.0773544043, 0.1056992534, 0.1594520863, 0.2137978689, 0.268735884, 0.3242657805, 0.3803873485, 0.4371004457, 0.4944049664, 0.4944049664, 0.4944049664, 0.4944049664], 3)
                CenterArc((0, 0), 4.68125, -2.3449905753, 4.6899811506)
            make_face()
        # OneSide extrude, distance=2.9
        extrude(amount=2.9, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated basket with a solid circular base and an open mesh-sided body, featuring a small protruding spout or nozzle on the front.
def model_44999_3e76c729_0004():
    """Model: Drive"""
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
            # Profile area: 15.6403453948, perimeter: 14.0193572166
            with BuildLine():
                CenterArc((0, 0), 2.23125, 4.0580273665, 351.8839452671)
                CenterArc((0, 0), 2.23125, -4.0580273665, 8.1160547329)
            make_face()
        # OneSide extrude, distance=2.9
        extrude(amount=2.9)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1045729733, perimeter: 1.2765625408
            with BuildLine():
                Line((2.2256560142, 0.1578982872), (2.2964458502, 0.1629204441))
                CenterArc((0, 0), 2.23125, -4.0580273665, 8.1160547329)
                Line((2.2256560142, -0.1578982872), (2.2964458502, -0.1629204441))
                _nurbs_edge([(2.2964458502, -0.1629204441), (2.3084913218, -0.1626254799), (2.3327749589, -0.1620308329), (2.369069384, -0.1562093625), (2.4055074098, -0.1485092162), (2.4420171767, -0.1386420902), (2.4785639685, -0.1269825342), (2.5151165879, -0.113623923), (2.5516307776, -0.0986479989), (2.5881300062, -0.082225471), (2.6121355859, -0.0701730535), (2.62422071, -0.0641055074)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0361085433, 0.0727947231, 0.1100380221, 0.1478362131, 0.1861884257, 0.2250941681, 0.2645531031, 0.304564972, 0.3451295627, 0.3451295627, 0.3451295627, 0.3451295627], 3)
                CenterArc((-0.01209502, 0), 2.63709502, -1.3929482385, 2.785896477)
                _nurbs_edge([(2.2964458502, 0.1629204441), (2.3084913218, 0.1626254799), (2.3327749589, 0.1620308329), (2.369069384, 0.1562093625), (2.4055074098, 0.1485092162), (2.4420171767, 0.1386420902), (2.4785639685, 0.1269825342), (2.5151165879, 0.113623923), (2.5516307776, 0.0986479989), (2.5881300062, 0.082225471), (2.6121355859, 0.0701730535), (2.62422071, 0.0641055074)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0361085433, 0.0727947231, 0.1100380221, 0.1478362131, 0.1861884257, 0.2250941681, 0.2645531031, 0.304564972, 0.3451295627, 0.3451295627, 0.3451295627, 0.3451295627], 3)
            make_face()
        # OneSide extrude, distance=2.9
        extrude(amount=2.9, mode=Mode.ADD)
    return part.part


# Description: This is an elongated wedge or tapered duct component with a triangular profile that narrows to a sharp point on one end and terminates with a small rectangular flange on the other end, featuring a dark navy top surface and lighter blue side panel.
def model_45235_14713966_0002():
    """Model: Shade Bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.080625, perimeter: 18.7939348228
            with BuildLine():
                Line((-8.255, 2.54), (-7.62, 3.81))
                Line((-3.175, 0), (-8.255, 2.54))
                Line((0, 0), (-3.175, 0))
                Line((-7.62, 3.81), (0, 0))
            make_face()
        # OneSide extrude, distance=-0.762
        extrude(amount=-0.762)
    return part.part


# Description: This is a triangular mounting bracket with three corner holes for fastening, featuring a hollow interior frame structure and reinforced edges.
def model_45235_14713966_0004():
    """Model: Top Bracket"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.3824185347, perimeter: 15.8387587317
            with BuildLine():
                CenterArc((-19.6789660364, 15.6209997711), 0.381, 151.4504830006, 118.5495169994)
                Line((-19.6789660364, 15.2399997711), (-15.940270492, 15.2399997711))
                CenterArc((-15.940270492, 15.6209997711), 0.381, -90, 122.9009660011)
                Line((-15.6203788128, 15.8279546299), (-17.651195633, 18.9670034375))
                CenterArc((-17.9710873122, 18.7600485787), 0.381, 32.9009660011, 118.5495169994)
                Line((-18.3057593914, 18.9421353695), (-20.0136381156, 15.803086562))
            make_face()
            with BuildLine():
                CenterArc((-17.9710873122, 18.7600485787), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-19.6789660364, 15.6209997711), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-15.940270492, 15.6209997711), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1397
        extrude(amount=0.1397)
    return part.part


# Description: A set of four identical parallelogram-shaped mounting brackets with flanged tabs positioned at alternating corners for securing or pivoting applications.
def model_45307_b9b4bca0_0006():
    """Model: Component38"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 57 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0002159845, perimeter: 0.096393798
            with BuildLine():
                CenterArc((-0.16, 0.125), 0.025, -90, 90)
                Line((-0.16, 0.1), (-0.16, 0.095))
                CenterArc((-0.16, 0.125), 0.03, -90, 41.8103148958)
                CenterArc((-0.16, 0.125), 0.03, -48.1896851042, 28.7184644697)
                CenterArc((-0.16, 0.125), 0.03, -19.4712206345, 19.4712206345)
                Line((-0.13, 0.125), (-0.135, 0.125))
            make_face()
            # Profile area: 0.0002159845, perimeter: 0.096393798
            with BuildLine():
                CenterArc((0.16, 0.125), 0.03, 180, 19.4712206345)
                CenterArc((0.16, 0.125), 0.03, -160.5287793655, 28.7184644697)
                CenterArc((0.16, 0.125), 0.03, -131.8103148958, 41.8103148958)
                Line((0.16, 0.095), (0.16, 0.1))
                CenterArc((0.16, 0.125), 0.025, 180, 90)
                Line((0.135, 0.125), (0.13, 0.125))
            make_face()
            # Profile area: 0.0002159845, perimeter: 0.096393798
            with BuildLine():
                CenterArc((0.16, -0.125), 0.03, 90, 41.8103148958)
                CenterArc((0.16, -0.125), 0.03, 131.8103148958, 28.7184644697)
                CenterArc((0.16, -0.125), 0.03, 160.5287793655, 19.4712206345)
                Line((0.13, -0.125), (0.135, -0.125))
                CenterArc((0.16, -0.125), 0.025, 90, 90)
                Line((0.16, -0.1), (0.16, -0.095))
            make_face()
            # Profile area: 0.0002159845, perimeter: 0.096393798
            with BuildLine():
                CenterArc((-0.16, -0.125), 0.03, 0, 19.4712206345)
                CenterArc((-0.16, -0.125), 0.03, 19.4712206345, 28.7184644697)
                CenterArc((-0.16, -0.125), 0.03, 48.1896851042, 41.8103148958)
                Line((-0.16, -0.095), (-0.16, -0.1))
                CenterArc((-0.16, -0.125), 0.025, 0, 90)
                Line((-0.135, -0.125), (-0.13, -0.125))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 57 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0083144739, perimeter: 0.3618920018
            with BuildLine():
                Line((-0.14, 0.03125), (-0.14, 0.1026393202))
                Line((-0.04, 0.03125), (-0.14, 0.03125))
                Line((-0.04, 0.03125), (-0.04, 0.115))
                Line((-0.04, 0.115), (-0.1317157288, 0.115))
                CenterArc((-0.16, 0.125), 0.03, -48.1896851042, 28.7184644697)
            make_face()
            # Profile area: 0.0083144739, perimeter: 0.3618920018
            with BuildLine():
                CenterArc((0.16, 0.125), 0.03, -160.5287793655, 28.7184644697)
                Line((0.04, 0.115), (0.1317157288, 0.115))
                Line((0.04, 0.03125), (0.04, 0.115))
                Line((0.04, 0.03125), (0.14, 0.03125))
                Line((0.14, 0.03125), (0.14, 0.1026393202))
            make_face()
            # Profile area: 0.0083144739, perimeter: 0.3618920018
            with BuildLine():
                CenterArc((0.16, -0.125), 0.03, 131.8103148958, 28.7184644697)
                Line((0.14, -0.03125), (0.14, -0.1026393202))
                Line((0.04, -0.03125), (0.14, -0.03125))
                Line((0.04, -0.03125), (0.04, -0.115))
                Line((0.04, -0.115), (0.1317157288, -0.115))
            make_face()
            # Profile area: 0.0083144739, perimeter: 0.3618920018
            with BuildLine():
                CenterArc((-0.16, -0.125), 0.03, 19.4712206345, 28.7184644697)
                Line((-0.04, -0.115), (-0.1317157288, -0.115))
                Line((-0.04, -0.03125), (-0.04, -0.115))
                Line((-0.04, -0.03125), (-0.14, -0.03125))
                Line((-0.14, -0.03125), (-0.14, -0.1026393202))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


# Description: This is a boat or watercraft hull with an elongated, streamlined shape featuring a curved bow (front), a flat or slightly angled deck area, and internal ribbed or braced structural elements visible through openings on the sides.
def model_45359_1768ab3f_0001():
    """Model: Beam Linkage (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4056637061, perimeter: 6.5132741229
            with BuildLine():
                Line((0, 0.4), (-1.6, 0.4))
                CenterArc((-1.6, 0), 0.4, 90, 180)
                Line((0, -0.4), (-1.6, -0.4))
                Line((0, 0.4), (0, -0.4))
            make_face()
            with BuildLine():
                CenterArc((-1.6, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a linear bearing block or slider rail component with an elongated rectangular body featuring a blue anodized top surface, dark end caps, and a streamlined profile designed for smooth linear motion along a shaft or rail.
def model_45359_1768ab3f_0032():
    """Model: Valve Linkage (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6456637061, perimeter: 12.1132741229
            with BuildLine():
                Line((0, 0.4), (-4.4, 0.4))
                CenterArc((-4.4, 0), 0.4, 90, 180)
                Line((0, -0.4), (-4.4, -0.4))
                Line((0, 0.4), (0, -0.4))
            make_face()
            with BuildLine():
                CenterArc((-4.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a disc sander pad or backing plate with a large flat circular base featuring a radial line pattern, a cylindrical central arbor for attachment, and a curved outer flange edge for securing sanding material.
def model_45466_5f662bcb_0000():
    """Model: Feet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7503826165, perimeter: 9.9745566751
            with BuildLine():
                CenterArc((-34.2562393079, 7.3291199317), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-34.2562393079, 7.3291199317), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-34.2562393079, 7.3291199317)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-34.2562393079, 7.3291199317)):
                Circle(0.3175)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical coupling or connector with a hollow tubular body featuring a protruding flange on one side, an internal stepped bore, and a side-mounted rectangular slot or port for fluid/gas passage or component attachment.
def model_45915_8f1885d2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 34.3068422566, perimeter: 50.3948778808
            with BuildLine():
                CenterArc((5.0914591213, 3.7896299742), 0.0630087607, -114.018921465, 149.5289470036)
                CenterArc((2.7731995345, 0.7588215129), 3.8760482215, 52.3141730894, 6.4447405459)
                CenterArc((4.2648339068, 3.2178213648), 1, 58.7589136353, 10.8732062248)
                CenterArc((2.7443553019, -0.8776482861), 5.368606969, 69.6321198601, 37.1947861842)
                CenterArc((1.6244658446, 2.8253191029), 1.5, 106.8269060443, 18.8955402305)
                CenterArc((3.7215247045, -0.090635803), 5.0917194872, 125.7224462748, 75.3600994515)
                CenterArc((-2.6322441292, -2.2251576244), 1.6312542089, -88.4471097156, 99.1505703192)
                CenterArc((-2.4796386588, -7.85434367), 4, 91.5528902844, 30.7485043178)
                CenterArc((-6.9155483781, -0.8378064876), 4.3011498643, -75.174205152, 17.4755997541)
                CenterArc((-5.6870253459, -5.4791178517), 0.5, 104.825794848, 145.6144981427)
                CenterArc((-0.6499970739, 8.6980422711), 15.5453821142, -109.5597070093, 3.2992990863)
                CenterArc((-4.7227535913, -5.2655101135), 1, -106.2604079229, 82.3325980018)
                CenterArc((-1.2251668892, -6.8174586462), 2.826441818, 12.4114648352, 143.6607252437)
                CenterArc((2.0235336233, -6.1025039976), 0.5, -167.5885351648, 92.7167795083)
                CenterArc((0.5012106374, -0.4715622408), 6.3330928625, -74.8717556565, 15.2395139151)
                CenterArc((0.5012106374, -0.4715622408), 6.3330928625, -59.6322417415, 1.3481509314)
                CenterArc((0, 0), 7, -56.8232302536, 27.1379276997)
                CenterArc((5.6469307722, -3.2190329067), 0.5, -29.685302554, 138.7649524956)
                CenterArc((3.3772835191, 3.3428538538), 6.4433173996, -93.9880244496, 23.0676743913)
                CenterArc((2.9987118516, -2.0872831431), 1, -108.5650019282, 14.5769774786)
                CenterArc((3.8945196557, 0.5799442237), 3.8136406039, 129.364716886, 122.0702811858)
                CenterArc((2.1099553329, 2.7552381408), 1, 114.116174055, 15.248542831)
                CenterArc((3.4346884951, 1.0188097301), 3.1658149074, 58.9871526904, 64.2093321485)
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


# Description: This is a flat parallelogram plate or panel with a trapezoidal appearance, featuring a simple geometric shape with no holes, slots, or protrusions, rendered in blue with subtle shading to show depth and 3D perspective.
def model_46087_bab56a97_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1238.7072, perimeter: 142.24
            with BuildLine():
                Line((-20.32, 15.24), (20.32, 15.24))
                Line((-20.32, -15.24), (-20.32, 15.24))
                Line((20.32, -15.24), (-20.32, -15.24))
                Line((20.32, 15.24), (20.32, -15.24))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a thin, elongated parallelogram-shaped plate or panel with a slightly beveled edge, featuring a flat top surface and a recessed bottom rim, typical of a cover panel or mounting bracket.
def model_46090_18310182_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2612.898, perimeter: 213.36
            with BuildLine():
                Line((-19.05, 34.29), (19.05, 34.29))
                Line((-19.05, -34.29), (-19.05, 34.29))
                Line((19.05, -34.29), (-19.05, -34.29))
                Line((19.05, 34.29), (19.05, -34.29))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a composite part consisting of a cylindrical barrel or tube mounted on a rectangular prismatic base, featuring a tapered or wedge-shaped top section with a faceted surface.
def model_47790_f29fe247_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 91.7725005337, perimeter: 45.6359910305
            with BuildLine():
                Line((11.3910046982, 2.5), (-5, 2.5))
                CenterArc((-5, 0), 2.5, 90, 180)
                Line((11.3910046982, -2.5), (-5, -2.5))
                Line((11.3910046982, 2.5), (11.3910046982, -2.5))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a slightly conical shape, featuring a uniform diameter that gradually reduces from one end to the other.
def model_48224_53cae924_0008():
    """Model: cylinder2 pt2 v1 v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=210
        extrude(amount=210)
    return part.part


# Description: This is a parallelogram-shaped flat plate or base component with a uniform thickness and angled edges, featuring a trapezoidal profile when viewed from certain angles.
def model_48290_3a237df1_0000():
    """Model: Base Plate"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 16.7617487475, perimeter: 28.9364543471
            with BuildLine():
                Line((-6.5991135768, 1.2700000405), (-6.5991135768, 0.0000000405))
                Line((-6.5991135768, 0.0000000405), (6.5991135768, 0.0000000008))
                Line((6.5991135768, 0.0000000008), (6.5991135768, 1.2700000405))
                Line((6.5991135768, 1.2700000405), (-6.5991135768, 1.2700000405))
            make_face()
        # TwoSides extrude, along=5.08, against=-10.16
        extrude(amount=5.08)
        extrude(sk.sketch, amount=-10.16)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slight 3D depth, featuring a simple geometric form with no holes, slots, or protrusions—likely used as a structural backing panel or mounting plate in an assembly.
def model_48290_3a237df1_0008():
    """Model: Front Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.08), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.3455451609, perimeter: 23.5640905203
            with BuildLine():
                CenterArc((0, 15.2400004864), 6.5991135768, 90, 90)
                Line((0, 21.8391140632), (-6.5991135768, 21.8391140632))
                Line((-6.5991135768, 21.8391140632), (-6.5991135768, 15.2400004864))
            make_face()
            # Profile area: 9.3455451609, perimeter: 23.5640903039
            with BuildLine():
                CenterArc((0, 15.2400004864), 6.5991135768, 0.0000009394, 89.9999990606)
                Line((6.5991135768, 15.2400005946), (6.5991135768, 21.8391140632))
                Line((6.5991135768, 21.8391140632), (0, 21.8391140632))
            make_face()
            # Profile area: 115.973729543, perimeter: 61.869954995
            with BuildLine():
                Line((-6.5991135768, 1.2700000405), (6.5991135768, 1.2700000405))
                Line((6.5991135768, 1.2700000405), (6.5991135768, 15.2400005946))
                CenterArc((0, 15.2400004864), 6.5991135768, 180, 180.0000009394)
                Line((-6.5991135768, 15.2400004864), (-6.5991135768, 1.2700000405))
            make_face()
            # Profile area: 135.5442506586, perimeter: 45.4532761365
            with BuildLine():
                CenterArc((0, 15.2400004864), 6.5991135768, 180, 180.0000009394)
                CenterArc((0, 15.2400004864), 6.5991135768, 0.0000009394, 89.9999990606)
                CenterArc((0, 15.2400004864), 6.5991135768, 90, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 15.2400004864), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


# Description: This is a clamp or gripper mechanism featuring a symmetrical design with two parallel jaw-like flanges connected by a central cylindrical pivot shaft, creating a pinching or holding assembly with curved grip surfaces.
def model_48322_87521a02_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.3386946944, perimeter: 15.67551631
            with BuildLine():
                Line((-3.3541019662, 1), (3.3541019662, 1))
                CenterArc((0, 0), 3.5, 16.601549599, 146.796900802)
            make_face()
            # Profile area: 8.0964396912, perimeter: 12.3200579776
            with BuildLine():
                CenterArc((0, 0), 3.5, -106.601549599, 33.203099198)
                Line((-1, -7.5), (-1, -3.3541019662))
                Line((1, -7.5), (-1, -7.5))
                Line((1, -3.3541019662), (1, -7.5))
            make_face()
            # Profile area: 3.7175671928, perimeter: 8.1777291662
            with BuildLine():
                CenterArc((0, 0), 3.5, -163.398450401, 56.796900802)
                Line((-1, -3.3541019662), (-1, -1))
                Line((-1, -1), (-3.3541019662, -1))
            make_face()
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((1, -1), (-1, -1))
                Line((1, 0), (1, -1))
                Line((-1, 0), (1, 0))
                Line((-1, -1), (-1, 0))
            make_face()
            # Profile area: 3.7175671928, perimeter: 8.1777291662
            with BuildLine():
                Line((3.3541019662, -1), (1, -1))
                Line((1, -1), (1, -3.3541019662))
                CenterArc((0, 0), 3.5, -73.398450401, 56.796900802)
            make_face()
            # Profile area: 8.0964396912, perimeter: 12.3200579776
            with BuildLine():
                Line((-3.3541019662, -1), (-7.5, -1))
                CenterArc((0, 0), 3.5, 163.398450401, 33.203099198)
                Line((-7.5, 1), (-3.3541019662, 1))
                Line((-7.5, -1), (-7.5, 1))
            make_face()
            # Profile area: 4.9035603088, perimeter: 8.7364658426
            with BuildLine():
                Line((1, -1), (1, -3.3541019662))
                Line((1, -1), (-1, -1))
                Line((-1, -3.3541019662), (-1, -1))
                CenterArc((0, 0), 3.5, -106.601549599, 33.203099198)
            make_face()
            # Profile area: 8.0964396912, perimeter: 12.3200579776
            with BuildLine():
                CenterArc((0, 0), 3.5, -16.601549599, 33.203099198)
                Line((7.5, -1), (3.3541019662, -1))
                Line((7.5, 1), (7.5, -1))
                Line((3.3541019662, 1), (7.5, 1))
            make_face()
            # Profile area: 11.8071206177, perimeter: 19.4729316851
            with BuildLine():
                Line((-1, -1), (-3.3541019662, -1))
                Line((-1, -1), (-1, 0))
                Line((-1, 0), (1, 0))
                Line((1, 0), (1, -1))
                Line((3.3541019662, -1), (1, -1))
                CenterArc((0, 0), 3.5, -16.601549599, 33.203099198)
                Line((-3.3541019662, 1), (3.3541019662, 1))
                CenterArc((0, 0), 3.5, 163.398450401, 33.203099198)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a fin or blade assembly with an elongated, tapered body featuring a streamlined profile with integrated blue and dark gray coloring, designed for hydrodynamic or aerodynamic applications.
def model_48475_02526608_0001():
    """Model: Knife_handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 44 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.3267315484, perimeter: 21.8158837686
            with BuildLine():
                Line((10.4885328757, -7.6188699632), (9.4699997883, -8.5099998098))
                CenterArc((9.8188400954, -6.8534324036), 1.0170462514, -48.8168341994, 152.5727662451)
                Line((8.4601850458, -6.1389631273), (9.5770002699, -5.8655576259))
                CenterArc((7.9846121303, -4.1963282151), 2, -90, 13.7559320457)
                Line((2.835886311, -6.1963282151), (7.9846121303, -6.1963282151))
                Line((2.835886311, -7.6410186102), (2.835886311, -6.1963282151))
                Line((4.2063777233, -7.8758462367), (2.835886311, -7.6410186102))
                CenterArc((4.3752620602, -6.8902103603), 1, -99.722958392, 9.722958392)
                Line((6.1535127989, -7.8902103603), (4.3752620602, -7.8902103603))
                CenterArc((6.1535127989, -6.8902103603), 1, -90, 7.6250450606)
                Line((8.1049511814, -7.6378858925), (6.2862024554, -7.8813679942))
                CenterArc((8.1077152097, -9.1378833459), 1.5, 25.0336048125, 65.0719733498)
                Line((9.4699997883, -8.5099998098), (9.4668048487, -8.5031587182))
            make_face()
            with BuildLine():
                CenterArc((9.6000000671, -6.9000001058), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3000000671, -7.1000001058), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((9.6000000671, -6.9000001058)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((4.3000000671, -7.1000001058)):
                Circle(0.200000003)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 44 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.0162968018, perimeter: 27.849450779
            with BuildLine():
                Line((2.835886311, -18.6963282151), (-6.4678646393, -19.000121697))
                Line((-6.4678646393, -19.000121697), (-9.1281158207, -19.2957051616))
                Line((-9.1281158207, -19.2957051616), (-6.9257337361, -20.5095313092))
                CenterArc((-4.6329718762, -16.3495141152), 4.75, -118.8610226231, 3.844129145)
                Line((-6.6416778366, -20.6538840302), (-6.3709523682, -20.7802225821))
                CenterArc((-4.3622464079, -16.4758526671), 4.75, -115.0168934781, 12.4880857689)
                Line((-5.3926660825, -21.112741203), (-3.2000000477, -21.6000003219))
                Line((-3.2000000477, -21.6000003219), (-0.9227649423, -21.9960412098))
                CenterArc((-0.837094355, -21.5034353323), 0.5, -99.8658069431, 5.2918856832)
                Line((-0.8769669661, -22.0018429716), (1.4706207144, -22.189649986))
                CenterArc((1.7297926868, -18.9500003308), 3.25, -94.5739212599, 4.5739212599)
                Line((1.7297926868, -22.2000003308), (2.7000000402, -22.2000003308))
                Line((2.7000000402, -22.2000003308), (2.835886311, -20.1410186102))
                Line((2.835886311, -20.1410186102), (2.835886311, -18.6963282151))
            make_face()
            # Profile area: 13.3267315484, perimeter: 21.8158837686
            with BuildLine():
                Line((2.835886311, -20.1410186102), (2.835886311, -18.6963282151))
                Line((4.2063777233, -20.3758462367), (2.835886311, -20.1410186102))
                CenterArc((4.3752620602, -19.3902103603), 1, -99.722958392, 9.722958392)
                Line((6.1535127989, -20.3902103603), (4.3752620602, -20.3902103603))
                CenterArc((6.1535127989, -19.3902103603), 1, -90, 7.6250450606)
                Line((8.1049511814, -20.1378858925), (6.2862024554, -20.3813679942))
                CenterArc((8.1077152097, -21.6378833459), 1.5, 25.0336048125, 65.0719733498)
                Line((9.4699997883, -21.0099998098), (9.4668048487, -21.0031587182))
                Line((10.4885328757, -20.1188699632), (9.4699997883, -21.0099998098))
                CenterArc((9.8188400954, -19.3534324036), 1.0170462514, -48.8168341994, 152.5727662451)
                Line((8.4601850458, -18.6389631273), (9.5770002699, -18.3655576259))
                CenterArc((7.9846121303, -16.6963282151), 2, -90, 13.7559320457)
                Line((2.835886311, -18.6963282151), (7.9846121303, -18.6963282151))
            make_face()
            with BuildLine():
                CenterArc((4.3000000671, -19.6000001058), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.6000000671, -19.4000001058), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a nail or fastener pin with a cylindrical shaft and a slightly enlarged head at the top, designed for driving into materials.
def model_48475_02526608_0003():
    """Model: Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34.5575191895, perimeter: 50.2654824574
            with BuildLine():
                CenterArc((5, 5), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, 5), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 8), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8, 5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 2), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((5, 5)):
                Circle(2)
        # OneSide extrude, distance=-80
        extrude(amount=-80, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical bowl or container with an elliptical cross-section, featuring a flat bottom section (dark) and a flared, open top rim (light blue), with vertical ribbed or corrugated surface detailing throughout.
def model_48729_39a46f5b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a blue and dark gray plastic or composite housing/enclosure with an elongated rectangular shape, featuring a curved upper section, an open cavity or slot along the top surface, and angled side flanges.
def model_48907_25974aa4_0007():
    """Model: handlebar to holder adapter v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2653144439, perimeter: 3.4539052255
            with BuildLine():
                CenterArc((2.5, 0), 0.45, 90, 179.3830309314)
                Line((2.5, 0.45), (1.9638097703, 0.45))
                CenterArc((2.5, 0), 0.6999999732, 139.9947972726, 27.6293909114)
                CenterArc((2.5, 0), 0.6999999732, 167.624188184, 24.7472512139)
                CenterArc((2.5, 0), 0.6999999732, -167.628560602, 27.6309755737)
                Line((2.4951544299, -0.4499739109), (1.9637878759, -0.4499739109))
            make_face()
            # Profile area: 0.3985893994, perimeter: 4.5553091604
            with BuildLine():
                CenterArc((2.5, 0), 0.45, 90, 179.3830309314)
                Line((2.5048455701, -0.4499739109), (2.4951544299, -0.4499739109))
                CenterArc((2.5, 0), 0.45, -89.3830309314, 179.3830309314)
            make_face()
            with BuildLine():
                CenterArc((2.5, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5416184064, perimeter: 4.2348653214
            with BuildLine():
                Line((1.8162660349, 0.1500260891), (0, 0.1500260891))
                Line((0, 0.1500260891), (0, -0.1499739109))
                Line((1.8162545879, -0.1499739109), (0, -0.1499739109))
                CenterArc((2.5, 0), 0.6999999732, 167.624188184, 24.7472512139)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5624361097, perimeter: 4.4176063923
            with BuildLine():
                Line((1.9638097703, 0.45), (0, 0.45))
                Line((0, 0.45), (0, 0.1500260891))
                Line((1.8162660349, 0.1500260891), (0, 0.1500260891))
                CenterArc((2.5, 0), 0.6999999732, 139.9947972726, 27.6293909114)
            make_face()
            # Profile area: 0.5624796452, perimeter: 4.4176185004
            with BuildLine():
                Line((1.8162545879, -0.1499739109), (0, -0.1499739109))
                Line((0, -0.1499739109), (0, -0.4499739109))
                Line((1.9637878759, -0.4499739109), (0, -0.4499739109))
                CenterArc((2.5, 0), 0.6999999732, -167.628560602, 27.6309755737)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a boat hull or marine vessel structure featuring an elongated, curved asymmetrical shape with a tapered bow section, a wider stern area, and ribbed internal framing or stringers running along its length.
def model_48907_25974aa4_0008():
    """Model: handlebar clamp v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9533370622, perimeter: 6.8983252322
            with BuildLine():
                Line((-1.1634431658, -0.25), (-2.750000041, -0.25))
                Line((-2.750000041, -0.25), (-2.750000041, -0.75))
                CenterArc((0, 3.9166666555), 5.4166666778, -120.5102378396, 30.5102378396)
                Line((0, -1.1900000565), (0, -1.5000000224))
                CenterArc((0, 0), 1.19, -167.872723127, 77.872723127)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a surfboard or hydrofoil wing featuring an elongated elliptical shape with a curved, streamlined profile, a textured grip surface in the center marked by blue striations, and tapered edges that transition from a thicker dark gray core to thinner dark edges for hydrodynamic efficiency.
def model_49016_cd1b47bf_0001():
    """Model: podstawa 2 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 691.1503837898, perimeter: 99.4525880335
            Ellipse(20, 11, rotation=90)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a rounded rectangular sleeve or housing with a curved, elongated body featuring a longitudinal slot or groove running along the top surface and a solid cylindrical base, commonly used as a structural component or mounting bracket.
def model_49016_cd1b47bf_0002():
    """Model: kojec v17"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1178.0972450962, perimeter: 127.6349943246
            Ellipse(25, 15)
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is an oval/elliptical flat plate or tray with a slightly domed or curved surface, featuring a fine grid or mesh pattern across its top face and a raised perimeter rim.
def model_49016_cd1b47bf_0021():
    """Model: podstawa v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2199.1148575129, perimeter: 176.0158110126
            Ellipse(35, 20)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a wedge-shaped or trapezoidal prism component with a tapered profile, featuring a flat base, angled top surface, and triangulated faceting on the upper portion, commonly used as a structural bracket, wedge, or geometric spacer element.
def model_49019_748c9a9f_0007():
    """Model: noga v2 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.6602540378, perimeter: 14
            with BuildLine():
                Line((0, 0), (-1, -1.7320508076))
                Line((-1, -1.7320508076), (5, -1.7320508076))
                Line((4, 0), (5, -1.7320508076))
                Line((0, 0), (4, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with an open top, featuring a solid dark outer wall and a lighter mesh or latticed upper section, designed for filtration or ventilation purposes.
def model_49024_b7f02205_0006():
    """Model: nakretka v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2591814016, perimeter: 3.4557519704
            with BuildLine():
                CenterArc((0, 0), 0.3500000052, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a flat parallelogram or trapezoidal plate with a thin, uniform thickness and diagonal internal ribs or reinforcing webs visible on its top surface.
def model_49134_e9867f8b_0002():
    """Model: Podst_dol"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 143.36, perimeter: 716.8
            with BuildLine():
                Line((110, -70), (0, -70))
                Line((110, 0), (110, -70))
                Line((0, 0), (110, 0))
                Line((0, -70), (0, 0))
            make_face()
            with BuildLine():
                Line((0.4, -69.6), (0.4, -0.4))
                Line((0.4, -0.4), (109.6, -0.4))
                Line((109.6, -0.4), (109.6, -69.6))
                Line((109.6, -69.6), (0.4, -69.6))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7556.64, perimeter: 356.8
            with BuildLine():
                Line((109.6, -69.6), (0.4, -69.6))
                Line((109.6, -0.4), (109.6, -69.6))
                Line((0.4, -0.4), (109.6, -0.4))
                Line((0.4, -69.6), (0.4, -0.4))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 143.36, perimeter: 716.8
            with BuildLine():
                Line((110, -70), (0, -70))
                Line((110, 0), (110, -70))
                Line((0, 0), (110, 0))
                Line((0, -70), (0, 0))
            make_face()
            with BuildLine():
                Line((0.4, -69.6), (0.4, -0.4))
                Line((0.4, -0.4), (109.6, -0.4))
                Line((109.6, -0.4), (109.6, -69.6))
                Line((109.6, -69.6), (0.4, -69.6))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a simple planar geometry and no distinctive features, holes, or protrusions.
def model_49134_e9867f8b_0013():
    """Model: Grill_boczna_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2762.9535450916, perimeter: 569.6902604182
            with BuildLine():
                Line((-40, 45), (-40, 95))
                Line((-40, 95), (-110, 95))
                Line((-110, 95), (-110, 45))
                Line((-110, 45), (-40, 45))
            make_face()
            with BuildLine():
                CenterArc((-108, 47), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-42, 47), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-42, 93), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-108, 93), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-97.5, 80), (-52.5, 80))
                CenterArc((-97.5, 82.5), 2.5, 90, 180)
                Line((-52.5, 85), (-97.5, 85))
                CenterArc((-52.5, 82.5), 2.5, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-97.5, 75), (-52.5, 75))
                CenterArc((-52.5, 72.5), 2.5, -90, 180)
                Line((-52.5, 70), (-97.5, 70))
                CenterArc((-97.5, 72.5), 2.5, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-97.5, 60), (-52.5, 60))
                CenterArc((-97.5, 62.5), 2.5, 90, 180)
                Line((-52.5, 65), (-97.5, 65))
                CenterArc((-52.5, 62.5), 2.5, -90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 244.6349540849, perimeter: 105.7079632679
            with BuildLine():
                CenterArc((-52.5, 82.5), 2.5, -90, 180)
                Line((-52.5, 85), (-97.5, 85))
                CenterArc((-97.5, 82.5), 2.5, 90, 180)
                Line((-97.5, 80), (-52.5, 80))
            make_face()
            # Profile area: 244.6349540849, perimeter: 105.7079632679
            with BuildLine():
                CenterArc((-97.5, 72.5), 2.5, 90, 180)
                Line((-52.5, 70), (-97.5, 70))
                CenterArc((-52.5, 72.5), 2.5, -90, 180)
                Line((-97.5, 75), (-52.5, 75))
            make_face()
            # Profile area: 244.6349540849, perimeter: 105.7079632679
            with BuildLine():
                CenterArc((-52.5, 62.5), 2.5, -90, 180)
                Line((-52.5, 65), (-97.5, 65))
                CenterArc((-97.5, 62.5), 2.5, 90, 180)
                Line((-97.5, 60), (-52.5, 60))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cutting tool insert with an elongated hexagonal or prismatic shape, featuring multiple sharp cutting edges and faceted surfaces designed for machining operations.
def model_49145_4a5b250e_0010():
    """Model: zaciski"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.1946903509, perimeter: 19.4265482457
            with BuildLine():
                Line((3, 0.5), (3, -0.7))
                Line((-3, 0.5), (3, 0.5))
                Line((-3, -0.7), (-3, 0.5))
                Line((3, -0.7), (-3, -0.7))
            make_face()
            with BuildLine():
                CenterArc((1.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-1.5, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((1.5, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)
    return part.part


# Description: This is an open-end wrench (or spanner) featuring a flat rectangular handle with a U-shaped jaw at one end for gripping fasteners, characterized by its simple tool design with a curved head and straight shaft.
def model_49596_4d060b33_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 23.8924330015, perimeter: 28.9977865137
            with BuildLine():
                Line((1, 1), (1, 3))
                Line((1, 3), (-5, 3))
                CenterArc((-7, 2), 2.2360679775, 26.5650511771, 126.8698976458)
                Line((-9, 3), (-7.7020074894, 3))
                Line((-7.7020074894, 3), (-7, 2))
                Line((-7, 2), (-7.7020074894, 1.071377979))
                Line((-7.7020074894, 1.071377979), (-9.0341241708, 1.071377979))
                CenterArc((-7, 2), 2.2360679775, -155.4622687972, 128.8972176202)
                Line((1, 1), (-5, 1))
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is an aerodynamic fairing or cowling with an elongated, streamlined teardrop shape featuring a curved upper surface, flat lower base with a dark rim or flange around the perimeter, and a tapered nose section.
def model_49603_143b8bd2_0007():
    """Model: blaszka2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.1015926536, perimeter: 18.8831853072
            with BuildLine():
                CenterArc((1.2, -1.95), 1, -90, 90)
                Line((2.2, -1.95), (2.2, 1.95))
                CenterArc((1.2, 1.95), 1, 0, 90)
                Line((1.2, 2.95), (-1.2, 2.95))
                CenterArc((-1.2, 1.95), 1, 90, 90)
                Line((-2.2, 1.95), (-2.2, -1.95))
                CenterArc((-1.2, -1.95), 1, 180, 90)
                Line((-1.2, -2.95), (1.2, -2.95))
            make_face()
        # OneSide extrude, distance=0.24
        extrude(amount=0.24)
    return part.part


# Description: This is a flat, elongated panel or cover with a tapered parallelogram shape, featuring a dark border frame and a central vertical slot or ridge running along its length.
def model_49603_143b8bd2_0008():
    """Model: blaszka1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 79.8015926536, perimeter: 34.8831853072
            with BuildLine():
                CenterArc((-2.7, 4.45), 1, 90, 90)
                Line((-3.7, 4.45), (-3.7, -4.45))
                CenterArc((-2.7, -4.45), 1, 180, 90)
                Line((-2.7, -5.45), (2.7, -5.45))
                CenterArc((2.7, -4.45), 1, -90, 90)
                Line((3.7, -4.45), (3.7, 4.45))
                CenterArc((2.7, 4.45), 1, 0, 90)
                Line((2.7, 5.45), (-2.7, 5.45))
            make_face()
        # OneSide extrude, distance=0.24
        extrude(amount=0.24)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform diameter and slightly rounded ends, appearing to be a simple structural or mechanical component.
def model_49613_1b97c07b_0015():
    """Model: height adjustment"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=40
        extrude(amount=40)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, slightly tapered at one end, presented at an angle in 3D isometric view.
def model_49613_1b97c07b_0017():
    """Model: leg (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.926990817, perimeter: 35.7079632679
            with BuildLine():
                CenterArc((-2.5, 0), 1.5, 90, 180)
                Line((2.5, -1.5), (-2.5, -1.5))
                CenterArc((2.5, 0), 1.5, -90, 180)
                Line((-2.5, 1.5), (2.5, 1.5))
            make_face()
            with BuildLine():
                Line((-2.5, 1), (2.5, 1))
                CenterArc((2.5, 0), 1, -90, 180)
                Line((2.5, -1), (-2.5, -1))
                CenterArc((-2.5, 0), 1, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=100
        extrude(amount=100)
    return part.part


# Description: This is a cylindrical knob or dial with a rounded dome-shaped top and a small protruding pin or indicator on one side, featuring a textured mesh surface on the upper portion.
def model_49703_b92021be_0011():
    """Model: Gear 27"""
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
            # Profile area: 35.1260647452, perimeter: 21.0096917591
            with BuildLine():
                CenterArc((0, 0), 3.3437962963, 3.8417458476, 352.3165083048)
                CenterArc((0, 0), 3.3437962963, -3.8417458476, 7.6834916952)
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2486903385, perimeter: 1.9557936284
            with BuildLine():
                Line((3.3362825055, 0.2240373057), (3.5160285917, 0.2361075752))
                CenterArc((0, 0), 3.3437962963, -3.8417458476, 7.6834916952)
                Line((3.3362825055, -0.2240373057), (3.5160285917, -0.2361075752))
                _nurbs_edge([(3.5160285917, -0.2361075752), (3.5322104842, -0.235747152), (3.564802038, -0.2350212325), (3.6135405447, -0.2277382072), (3.6624550182, -0.2181112692), (3.7114639117, -0.2057873993), (3.760529014, -0.191242135), (3.8096165568, -0.1745979232), (3.8586777664, -0.1559611571), (3.9077422859, -0.1355492617), (3.94008218, -0.1205733912), (3.9563510045, -0.1130396681)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0485120217, 0.0977068762, 0.1475604158, 0.1980700681, 0.2492348525, 0.3010542289, 0.3535278352, 0.4066553983, 0.4604366969, 0.4604366969, 0.4604366969, 0.4604366969], 3)
                CenterArc((-0.0063341734, 0), 3.9642971364, -1.6339778955, 3.267955791)
                _nurbs_edge([(3.5160285917, 0.2361075752), (3.5322104842, 0.235747152), (3.564802038, 0.2350212325), (3.6135405447, 0.2277382072), (3.6624550182, 0.2181112692), (3.7114639117, 0.2057873993), (3.760529014, 0.191242135), (3.8096165568, 0.1745979232), (3.8586777664, 0.1559611571), (3.9077422859, 0.1355492617), (3.94008218, 0.1205733912), (3.9563510045, 0.1130396681)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0485120217, 0.0977068762, 0.1475604158, 0.1980700681, 0.2492348525, 0.3010542289, 0.3535278352, 0.4066553983, 0.4604366969, 0.4604366969, 0.4604366969, 0.4604366969], 3)
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7, mode=Mode.ADD)
    return part.part


# Description: This is a circular disc or wheel with a textured/ribbed rim section featuring a smooth flat face on one side and a small protruding tab or lug on the edge, likely designed for mechanical engagement or mounting purposes.
def model_49703_b92021be_0013():
    """Model: Gear 29"""
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
            # Profile area: 151.520993521, perimeter: 43.6356386506
            with BuildLine():
                CenterArc((0, 0), 6.9448275862, 3.2012317353, 353.5975365293)
                CenterArc((0, 0), 6.9448275862, -3.2012317353, 6.4024634707)
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.8999622618, perimeter: 3.7291304765
            with BuildLine():
                Line((6.9339906266, 0.3878197937), (7.472823215, 0.4179568323))
                CenterArc((0, 0), 6.9448275862, -3.2012317353, 6.4024634707)
                Line((6.9339906266, -0.3878197937), (7.472823215, -0.4179568323))
                _nurbs_edge([(7.472823215, -0.4179568323), (7.4966232277, -0.4175156483), (7.5444565985, -0.4166289548), (7.6160584113, -0.4077427162), (7.6878509064, -0.3960425078), (7.7597576195, -0.3811233625), (7.8317464327, -0.3635793103), (7.9037898716, -0.3435743018), (7.9758460246, -0.3212490601), (8.0479498091, -0.2968772003), (8.0956761269, -0.2790173214), (8.1196439903, -0.2700482)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0713655967, 0.1434308918, 0.2161714184, 0.2895846867, 0.3636698035, 0.4384263098, 0.5138539179, 0.5899524234, 0.6667216682, 0.6667216682, 0.6667216682, 0.6667216682], 3)
                CenterArc((0.0080733803, 0), 8.1160645507, -1.9067712483, 3.8135424966)
                _nurbs_edge([(7.472823215, 0.4179568323), (7.4966232277, 0.4175156483), (7.5444565985, 0.4166289548), (7.6160584113, 0.4077427162), (7.6878509064, 0.3960425078), (7.7597576195, 0.3811233625), (7.8317464327, 0.3635793103), (7.9037898716, 0.3435743018), (7.9758460246, 0.3212490601), (8.0479498091, 0.2968772003), (8.0956761269, 0.2790173214), (8.1196439903, 0.2700482)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0713655967, 0.1434308918, 0.2161714184, 0.2895846867, 0.3636698035, 0.4384263098, 0.5138539179, 0.5899524234, 0.6667216682, 0.6667216682, 0.6667216682, 0.6667216682], 3)
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3, mode=Mode.ADD)
    return part.part


# Description: This is a half-cylindrical or curved channel extrusion with a semi-circular cross-section, featuring a flat base and a smooth, arched top surface.
def model_50001_e86a6698_0010():
    """Model: Roof"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 228.0914384369, perimeter: 62.8015469389
            with BuildLine():
                Line((58.4199994278, 0), (78.7399994278, 0))
                CenterArc((58.4199994278, -5.9266666667), 21.1666666667, 16.2602047083, 73.7397952917)
                Line((58.4199994278, 0), (58.4199994278, 15.24))
            make_face()
            # Profile area: 228.0914384369, perimeter: 62.8015469389
            with BuildLine():
                Line((58.4199994278, 0), (58.4199994278, 15.24))
                CenterArc((58.4199994278, -5.9266666667), 21.1666666667, 90, 73.7397952917)
                Line((38.0999994278, 0), (58.4199994278, 0))
            make_face()
        # OneSide extrude, distance=40.64
        extrude(amount=40.64)
    return part.part


# Description: This is a rectangular parallelepiped (box-shaped) part with an elongated central slot or cutout running along its length, featuring angled or beveled edges on its ends.
def model_50134_aa4781f7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.1567065042, perimeter: 18.171564534
            with BuildLine():
                Line((-3.81, 0), (-2.54, 0))
                Line((-2.54, 0), (-2.54, 0.0508))
                CenterArc((-2.286, 0.0508), 0.254, 90, 90)
                Line((2.286, 0.3048), (-2.286, 0.3048))
                CenterArc((2.286, 0.0508), 0.254, 0, 90)
                Line((2.54, 0), (2.54, 0.0508))
                Line((2.54, 0), (3.81, 0))
                Line((3.81, 0), (3.81, 1.27))
                Line((3.81, 1.27), (-3.81, 1.27))
                Line((-3.81, 1.27), (-3.81, 0))
            make_face()
            # Profile area: 8.1567065042, perimeter: 18.171564534
            with BuildLine():
                Line((-3.81, -1.27), (3.81, -1.27))
                Line((3.81, -1.27), (3.81, 0))
                Line((2.54, 0), (3.81, 0))
                Line((2.54, -0.0508), (2.54, 0))
                CenterArc((2.286, -0.0508), 0.254, -90, 90)
                Line((-2.286, -0.3048), (2.286, -0.3048))
                CenterArc((-2.286, -0.0508), 0.254, 180, 90)
                Line((-2.54, -0.0508), (-2.54, 0))
                Line((-3.81, 0), (-2.54, 0))
                Line((-3.81, 0), (-3.81, -1.27))
            make_face()
        # OneSide extrude, distance=0.9398
        extrude(amount=0.9398)
    return part.part


# Description: This is a boot or protective sleeve component with an L-shaped curved profile featuring a textured upper section, smooth rounded lower portion, and a flat base designed for mounting or support applications.
def model_50136_229717c0_0000():
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
        # Sketch14 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5362000902, perimeter: 14.4080051997
            with BuildLine():
                CenterArc((-2.5749665485, 0.0136762423), 0.1833147184, 132.1508029254, 180)
                _nurbs_edge([(-2.4519469283, -0.1222298247), (-2.337016453, -0.0181969162), (-2.2288013817, 0.035222725), (-2.1043710734, 0.0596155427), (-1.9821251577, 0.0835801409), (-1.8361872423, 0.0767491407), (-1.6583404622, 0.0332754196), (-1.4769490506, -0.0110647682), (-1.2661728523, -0.0953024915), (-1.045498552, -0.1846357317), (-0.8524085392, -0.2628023169), (-0.6547913659, -0.3442179868), (-0.4430767393, -0.3863074423), (-0.3134519544, -0.4120772094), (-0.1745947248, -0.4232412841), (-0.0302544771, -0.3942101781), (0.0955898124, -0.3688991579), (0.222229918, -0.3084257741), (0.321854517, -0.2226903627), (0.4400049939, -0.1210118633), (0.5198198709, 0.0070936559), (0.5781296186, 0.1396448212), (0.673972385, 0.3575169756), (0.7209321804, 0.5984542576), (0.7622922397, 0.8520882841), (0.8172814684, 1.189301037), (0.8588537027, 1.5446023765), (0.9252680378, 1.854731708), (0.9890926358, 2.152767966), (1.0748843819, 2.4074440374), (1.1836962417, 2.6017782677), (1.3037864929, 2.8162553163), (1.4464141247, 2.9612832025), (1.6269415462, 3.0637771825)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1000134909, 0.1000134909, 0.1000134909, 0.1982712301, 0.1982712301, 0.1982712301, 0.2984873264, 0.2984873264, 0.2984873264, 0.3861764106, 0.3861764106, 0.3861764106, 0.4398650898, 0.4398650898, 0.4398650898, 0.4866740277, 0.4866740277, 0.4866740277, 0.5421874088, 0.5421874088, 0.5421874088, 0.6334338337, 0.6334338337, 0.6334338337, 0.7547482272, 0.7547482272, 0.7547482272, 0.8713321302, 0.8713321302, 0.8713321302, 1, 1, 1, 1], 3)
                CenterArc((1.5341393872, 3.2218879411), 0.1833337195, -59.5894529264, 178.3501711821)
                _nurbs_edge([(-2.6979861687, 0.1495823093), (-2.6506428578, 0.1924365854), (-2.5534705469, 0.270200178), (-2.4002543003, 0.363009114), (-2.1809956906, 0.438900489), (-1.8827742522, 0.4555130983), (-1.5635696429, 0.4006849829), (-1.2300398813, 0.2892484128), (-0.8943103678, 0.1486745865), (-0.573435598, 0.018116658), (-0.2851689206, -0.0607722305), (-0.0444354211, -0.0513870483), (0.1401360772, 0.0703610371), (0.2708666429, 0.3061743919), (0.359422522, 0.6383885163), (0.4229165846, 1.037731401), (0.4807973048, 1.4694221762), (0.5517481996, 1.899282692), (0.6499879643, 2.3009244906), (0.7840463912, 2.6582577857), (0.9586372434, 2.962138109), (1.1322347656, 3.1593746419), (1.2816422362, 3.2811263193), (1.3897489855, 3.3507096073), (1.4459278605, 3.3826050194)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True)
    return part.part


# Description: This is an oval/elliptical shell or cover with a ribbed or reinforced surface pattern, featuring vertical and diagonal structural ribs or struts that traverse across the interior of the curved form for structural support.
def model_50382_cb85058c_0019():
    """Model: Front Suspension v2 (1)"""
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
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a bent metal bracket or connector consisting of two parallel flat planes joined at an angle by a narrow reinforcing rib or flange, creating a chevron-like 3D structure.
def model_50382_cb85058c_0022():
    """Model: Rear Wing v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.3992236574, perimeter: 11.359689463
            with BuildLine():
                Line((5, 0), (10, 0))
                Line((10, 0), (10, 0.6798447315))
                Line((5, 0.6798447315), (10, 0.6798447315))
                Line((5, 0), (5, 0.6798447315))
            make_face()
            # Profile area: 3.3992236574, perimeter: 11.359689463
            with BuildLine():
                Line((5, 0), (5, 0.6798447315))
                Line((0, 0.6798447315), (5, 0.6798447315))
                Line((0, 0), (0, 0.6798447315))
                Line((0, 0), (5, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8472733921, perimeter: 17.1454426389
            with BuildLine():
                Line((0, 0), (0, 0.6798447315))
                Line((0, 0.6798447315), (0, 8.472721169))
                Line((-0.1000001505, 8.472721169), (0, 8.472721169))
                Line((-0.1000001505, 8.472721169), (-0.1000001505, 0))
                Line((-0.1000001505, 0), (0, 0))
            make_face()
            # Profile area: 0.8472733921, perimeter: 17.1454426389
            with BuildLine():
                Line((10, 8.472721169), (10.1000001505, 8.472721169))
                Line((10, 0.6798447315), (10, 8.472721169))
                Line((10, 0), (10, 0.6798447315))
                Line((10.1000001505, 0), (10, 0))
                Line((10.1000001505, 8.472721169), (10.1000001505, 0))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


# Description: This is an elliptical aerospace or structural component featuring a dark outer rim/flange with an internal radial spoke or rib pattern supporting a curved blue membrane or panel surface.
def model_50681_eb7a9f92_0001():
    """Model: Glass Top v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            Circle(2.4)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 30.7876080052
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: A long, slender fastener with a hexagonal head at one end and a tapered pointed tip at the other, featuring a cylindrical threaded or smooth shaft along its length.
def model_50681_eb7a9f92_0017():
    """Model: Second Hand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.031415144, perimeter: 0.6283146165
            with BuildLine():
                CenterArc((0, 0), 0.1, 179.9432850127, 182.9226989272)
                CenterArc((0, 0), 0.1, 2.8659839399, 171.4656405989)
                Line((-0.099999951, 0.0000989863), (-0.0995110238, 0.0098770511))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1844227487, perimeter: 4.2893717866
            with BuildLine():
                CenterArc((0, 0), 0.1, 2.8659839399, 171.4656405989)
                Line((0, 2.0000000298), (0.0998749218, 0.0049999999))
                Line((-0.0995110238, 0.0098770511), (0, 2.0000000298))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cymbal, a percussion instrument with a flat, circular disc shape that tapers slightly at the edges, featuring a central dome and radial grooves across its surface for acoustic resonance.
def model_50681_eb7a9f92_0018():
    """Model: WatchFace v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.5549540826, perimeter: 16.8393341347
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                Line((0, 1.9000000283), (0.200000003, 2.1000000313))
                Line((-0.200000003, 2.1000000313), (0, 1.9000000283))
                Line((0, 2.3000000343), (-0.200000003, 2.1000000313))
                Line((0.200000003, 2.1000000313), (0, 2.3000000343))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0800000024, perimeter: 1.1313708668
            with BuildLine():
                Line((0.200000003, 2.1000000313), (0, 2.3000000343))
                Line((0, 2.3000000343), (-0.200000003, 2.1000000313))
                Line((-0.200000003, 2.1000000313), (0, 1.9000000283))
                Line((0, 1.9000000283), (0.200000003, 2.1000000313))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a tapered cylindrical shaft or pin with an elongated conical shape, featuring a pointed end and a slightly wider base, commonly used as a drive shaft, alignment pin, or taper pin in mechanical assemblies.
def model_50681_eb7a9f92_0019():
    """Model: Minute Hand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3372208571, perimeter: 4.4889309488
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 11.421186275, 157.15762745)
                Line((0, 2.0000000298), (0.1960396069, 0.039603961))
                Line((-0.1960396069, 0.039603961), (0, 2.0000000298))
            make_face()
            # Profile area: 0.0627791548, perimeter: 1.0281865993
            with BuildLine():
                Line((-0.200000003, 0), (-0.1960396069, 0.039603961))
                Line((0.200000003, 0), (-0.200000003, 0))
                Line((0.1960396069, 0.039603961), (0.200000003, 0))
                CenterArc((0, 0), 0.200000003, 11.421186275, 157.15762745)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0627791548, perimeter: 1.0281865993
            with BuildLine():
                Line((-0.200000003, 0), (-0.1960396069, 0.039603961))
                Line((0.200000003, 0), (-0.200000003, 0))
                Line((0.1960396069, 0.039603961), (0.200000003, 0))
                CenterArc((0, 0), 0.200000003, 11.421186275, 157.15762745)
            make_face()
            # Profile area: 0.0628318549, perimeter: 1.028318546
            with BuildLine():
                CenterArc((0, 0), 0.200000003, -180, 180)
                Line((0.200000003, 0), (-0.200000003, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a tapered conical pin or dowel with a pointed end on one side and a slightly enlarged cylindrical head on the other, commonly used as a fastener or alignment pin in mechanical assemblies.
def model_50777_2934de55_0002():
    """Model: Minute Hand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0392636225, perimeter: 1.570775357
            with BuildLine():
                CenterArc((0, 0), 0.15, -180, 184.3012222405)
                CenterArc((0, 0), 0.15, 4.3012222405, 167.1204712293)
                Line((-0.15, 0), (-0.1483219391, 0.0223741451))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2650854459, perimeter: 4.4150676256
            with BuildLine():
                CenterArc((0, 0), 0.15, 4.3012222405, 167.1204712293)
                Line((0, 2.0000000298), (0.1495775301, 0.0112499998))
                Line((-0.1483219391, 0.0223741451), (0, 2.0000000298))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


MODELS = {
    "model_38287_88ec74de_0069": {"func": model_38287_88ec74de_0069, "volume": 51.6251352938, "area": 151.7900534667},
    "model_38287_88ec74de_0082": {"func": model_38287_88ec74de_0082, "volume": 3.2360619776, "area": 30.3248878277},
    "model_38287_88ec74de_0088": {"func": model_38287_88ec74de_0088, "volume": 0.5430258722, "area": 6.8283404145},
    "model_38288_740bfe5a_0007": {"func": model_38288_740bfe5a_0007, "volume": 115.8719661732, "area": 475.4450279984},
    "model_38454_24787d99_0003": {"func": model_38454_24787d99_0003, "volume": 0.8925000266, "area": 6.9035535419},
    "model_38739_f321c899_0005": {"func": model_38739_f321c899_0005, "volume": 72.67089828, "area": 194.1471802821},
    "model_38739_f321c899_0008": {"func": model_38739_f321c899_0008, "volume": 62.3923123119, "area": 262.47221699},
    "model_38739_f321c899_0010": {"func": model_38739_f321c899_0010, "volume": 0.1956438324, "area": 2.1791259163},
    "model_38739_f321c899_0014": {"func": model_38739_f321c899_0014, "volume": 0.5027488269, "area": 7.1255739248},
    "model_38740_c9ed5246_0001": {"func": model_38740_c9ed5246_0001, "volume": 17442.9419283675, "area": 14483.9217135918},
    "model_38740_c9ed5246_0003": {"func": model_38740_c9ed5246_0003, "volume": 1023.7513240806, "area": 990.0879798427},
    "model_38740_c9ed5246_0004": {"func": model_38740_c9ed5246_0004, "volume": 144.2559754782, "area": 184.8867794809},
    "model_38741_e08013e7_0002": {"func": model_38741_e08013e7_0002, "volume": 2.1681590432, "area": 10.0105569761},
    "model_38741_e08013e7_0003": {"func": model_38741_e08013e7_0003, "volume": 4.3363017122, "area": 15.6848122158},
    "model_38741_e08013e7_0004": {"func": model_38741_e08013e7_0004, "volume": 1.0840795216, "area": 7.1734293562},
    "model_38953_19054857_0000": {"func": model_38953_19054857_0000, "volume": 9, "area": 47},
    "model_39124_28e99e62_0002": {"func": model_39124_28e99e62_0002, "volume": 262.0502543304, "area": 539.9544903202},
    "model_39406_55dd02e2_0009": {"func": model_39406_55dd02e2_0009, "volume": 4147.2, "area": 7269.12},
    "model_39468_15fb2e60_0001": {"func": model_39468_15fb2e60_0001, "volume": 20.8846617104, "area": 88.250367413},
    "model_39468_15fb2e60_0002": {"func": model_39468_15fb2e60_0002, "volume": 21.4560133696, "area": 84.598077334},
    "model_39637_ca6a9a60_0003": {"func": model_39637_ca6a9a60_0003, "volume": 0.2953650459, "area": 6.184380551},
    "model_40061_d07e8764_0002": {"func": model_40061_d07e8764_0002, "volume": 3.3143802495, "area": 15.1424765903},
    "model_40061_d07e8764_0017": {"func": model_40061_d07e8764_0017, "volume": 37.6991118431, "area": 77.3617190946},
    "model_40061_d07e8764_0018": {"func": model_40061_d07e8764_0018, "volume": 122.385813887, "area": 205.1105174577},
    "model_40061_d07e8764_0022": {"func": model_40061_d07e8764_0022, "volume": 0.9660892988, "area": 6.8861156227},
    "model_40070_be9c502b_0016": {"func": model_40070_be9c502b_0016, "volume": 90, "area": 245.3138412934},
    "model_40072_b44084ae_0015": {"func": model_40072_b44084ae_0015, "volume": 1.3273228961, "area": 6.738716242},
    "model_40176_01ed49ea_0003": {"func": model_40176_01ed49ea_0003, "volume": 0.1679176406, "area": 5.9016375734},
    "model_40176_01ed49ea_0005": {"func": model_40176_01ed49ea_0005, "volume": 1.0087136528, "area": 15.9588571404},
    "model_40352_a9774a3f_0007": {"func": model_40352_a9774a3f_0007, "volume": 3.1429670558, "area": 30.6180139439},
    "model_40413_c590b4b4_0007": {"func": model_40413_c590b4b4_0007, "volume": 31.5240007856, "area": 229.7126940625},
    "model_40500_6055e3d7_0002": {"func": model_40500_6055e3d7_0002, "volume": 285.7883832489, "area": 287.2627944163},
    "model_40513_89770261_0000": {"func": model_40513_89770261_0000, "volume": 9.7248000592, "area": 71.2670293467},
    "model_40705_5ff43505_0030": {"func": model_40705_5ff43505_0030, "volume": 24.975, "area": 51.98},
    "model_40705_5ff43505_0035": {"func": model_40705_5ff43505_0035, "volume": 6.7635362455, "area": 38.1061632056},
    "model_40723_f18d24a6_0012": {"func": model_40723_f18d24a6_0012, "volume": 747.2691251189, "area": 714.8062529942},
    "model_40782_3383cd58_0004": {"func": model_40782_3383cd58_0004, "volume": 9.9133643693, "area": 47.1043511308},
    "model_40782_3383cd58_0005": {"func": model_40782_3383cd58_0005, "volume": 0.2126858226, "area": 3.1070351344},
    "model_40782_3383cd58_0021": {"func": model_40782_3383cd58_0021, "volume": 3.6756634047, "area": 25.0699093756},
    "model_40999_cad6be09_0008": {"func": model_40999_cad6be09_0008, "volume": 1638.7063507782, "area": 838.7079825592},
    "model_40999_cad6be09_0009": {"func": model_40999_cad6be09_0009, "volume": 1625.6089314777, "area": 834.0630268145},
    "model_41010_212b5129_0001": {"func": model_41010_212b5129_0001, "volume": 7.0976215564, "area": 54.1736715327},
    "model_41026_295d1dc8_0008": {"func": model_41026_295d1dc8_0008, "volume": 980.4818481535, "area": 760.2452592963},
    "model_41031_57b1ef09_0001": {"func": model_41031_57b1ef09_0001, "volume": 0.9766864294, "area": 15.3544570316},
    "model_41124_a5855c0d_0003": {"func": model_41124_a5855c0d_0003, "volume": 2.5289820861, "area": 17.3415914478},
    "model_41124_a5855c0d_0005": {"func": model_41124_a5855c0d_0005, "volume": 15.9592906802, "area": 96.0070714937},
    "model_41125_711db4bf_0030": {"func": model_41125_711db4bf_0030, "volume": 0.2224380452, "area": 3.4748671201},
    "model_41128_ee74f244_0019": {"func": model_41128_ee74f244_0019, "volume": 27.896526908, "area": 59.0060859409},
    "model_41142_1bf94ee2_0005": {"func": model_41142_1bf94ee2_0005, "volume": 0.7620895094, "area": 5.5027021655},
    "model_41211_11f6b8a0_0000": {"func": model_41211_11f6b8a0_0000, "volume": 42.4752701139, "area": 103.7417294083},
    "model_41234_74275eb0_0006": {"func": model_41234_74275eb0_0006, "volume": 21.7187493228, "area": 45.6036731188},
    "model_41473_c2137170_0022": {"func": model_41473_c2137170_0022, "volume": 0.1570806443, "area": 2.8824565124},
    "model_41474_57d78888_0008": {"func": model_41474_57d78888_0008, "volume": 0.0007884932, "area": 0.0520503611},
    "model_41501_b627682a_0018": {"func": model_41501_b627682a_0018, "volume": 0.0314159275, "area": 0.691150395},
    "model_41501_b627682a_0030": {"func": model_41501_b627682a_0030, "volume": 0.0167056776, "area": 0.7058361717},
    "model_41504_ed0ad3ae_0000": {"func": model_41504_ed0ad3ae_0000, "volume": 938.7027915109, "area": 697.6697426278},
    "model_41508_f30b6f68_0000": {"func": model_41508_f30b6f68_0000, "volume": 3.1415926536, "area": 12.5663706144},
    "model_41512_c1a779f2_0001": {"func": model_41512_c1a779f2_0001, "volume": 1.0828980217, "area": 21.2800618759},
    "model_41520_60018d18_0005": {"func": model_41520_60018d18_0005, "volume": 70792.1209985615, "area": 19045.1238226364},
    "model_41648_577daf16_0001": {"func": model_41648_577daf16_0001, "volume": 19.8597344573, "area": 71.1176986295},
    "model_41648_577daf16_0013": {"func": model_41648_577daf16_0013, "volume": 22.0355214097, "area": 85.1685051947},
    "model_41648_577daf16_0014": {"func": model_41648_577daf16_0014, "volume": 2.5391527647, "area": 11.1949113363},
    "model_41653_71b50655_0002": {"func": model_41653_71b50655_0002, "volume": 0.4241150082, "area": 3.7792033718},
    "model_41672_5407972e_0000": {"func": model_41672_5407972e_0000, "volume": 18.0685834706, "area": 84.9867228627},
    "model_41696_de0790a1_0001": {"func": model_41696_de0790a1_0001, "volume": 597.8001328767, "area": 522.8376907009},
    "model_41714_1d49f4d1_0001": {"func": model_41714_1d49f4d1_0001, "volume": 0.0501392267, "area": 1.5706830256},
    "model_41714_1d49f4d1_0018": {"func": model_41714_1d49f4d1_0018, "volume": 61.4514939224, "area": 132.2578073094},
    "model_41717_ab2075ac_0000": {"func": model_41717_ab2075ac_0000, "volume": 5.6548667765, "area": 60.3185789489},
    "model_41717_eb1c1e6b_0000": {"func": model_41717_eb1c1e6b_0000, "volume": 446.357484222, "area": 725.3309118608},
    "model_41729_b5092135_0006": {"func": model_41729_b5092135_0006, "volume": 4.9516147161, "area": 54.0172236381},
    "model_41733_1ec9b00c_0002": {"func": model_41733_1ec9b00c_0002, "volume": 161.25, "area": 199.7593735356},
    "model_41733_1ec9b00c_0020": {"func": model_41733_1ec9b00c_0020, "volume": 1561395.6310385885, "area": 188103.6380665613},
    "model_41739_1bc15d9f_0006": {"func": model_41739_1bc15d9f_0006, "volume": 42.2868875704, "area": 95.5407085988},
    "model_41744_5c450f9d_0001": {"func": model_41744_5c450f9d_0001, "volume": 643.192262, "area": 1709.674},
    "model_41780_da6cd1db_0010": {"func": model_41780_da6cd1db_0010, "volume": 0.0814244839, "area": 3.4946316616},
    "model_41785_e15d763c_0000": {"func": model_41785_e15d763c_0000, "volume": 3.8932869156, "area": 17.8361032642},
    "model_41868_42350264_0000": {"func": model_41868_42350264_0000, "volume": 0.1257029761, "area": 25.2599757312},
    "model_41868_df8c70ca_0000": {"func": model_41868_df8c70ca_0000, "volume": 1.1415762305, "area": 32.8453511933},
    "model_41903_21ab17c0_0000": {"func": model_41903_21ab17c0_0000, "volume": 19828.34744, "area": 7664.5008},
    "model_41907_7bcecdb1_0007": {"func": model_41907_7bcecdb1_0007, "volume": 0.3594147179, "area": 8.3342774412},
    "model_41930_2e5f07db_0002": {"func": model_41930_2e5f07db_0002, "volume": 2.4711110341, "area": 11.3502475318},
    "model_41938_1c6ad017_0005": {"func": model_41938_1c6ad017_0005, "volume": 0.0144316913, "area": 0.3573561643},
    "model_41941_79d46bb4_0000": {"func": model_41941_79d46bb4_0000, "volume": 1.3290959907, "area": 12.6706309728},
    "model_41943_c6aa8bc9_0000": {"func": model_41943_c6aa8bc9_0000, "volume": 0.0149225655, "area": 0.6126105768},
    "model_41948_c0d68e8c_0001": {"func": model_41948_c0d68e8c_0001, "volume": 28.4151537117, "area": 77.2152866771},
    "model_41948_c0d68e8c_0005": {"func": model_41948_c0d68e8c_0005, "volume": 184.1010984379, "area": 432.4018004394},
    "model_41970_24ba0c1b_0008": {"func": model_41970_24ba0c1b_0008, "volume": 1.8719731469, "area": 23.2214174285},
    "model_41970_24ba0c1b_0009": {"func": model_41970_24ba0c1b_0009, "volume": 0.012566371, "area": 0.314159271},
    "model_42042_e61e4667_0002": {"func": model_42042_e61e4667_0002, "volume": 4.75, "area": 190.38},
    "model_42042_e61e4667_0003": {"func": model_42042_e61e4667_0003, "volume": 5.13, "area": 205.58},
    "model_42329_df7f540f_0038": {"func": model_42329_df7f540f_0038, "volume": 0.0064591145, "area": 0.3568849254},
    "model_42329_df7f540f_0076": {"func": model_42329_df7f540f_0076, "volume": 0.0009047787, "area": 0.1357168026},
    "model_42333_53c85dac_0043": {"func": model_42333_53c85dac_0043, "volume": 0.0040865323, "area": 0.1582347424},
    "model_42429_5c0a47d5_0000": {"func": model_42429_5c0a47d5_0000, "volume": 0.321226168, "area": 3.0846182409},
    "model_42429_78ffab1b_0000": {"func": model_42429_78ffab1b_0000, "volume": 1.0819154755, "area": 8.5633563967},
    "model_42586_517832f9_0016": {"func": model_42586_517832f9_0016, "volume": 289.5833243042, "area": 349.6281605773},
    "model_42601_bfe96b47_0000": {"func": model_42601_bfe96b47_0000, "volume": 28.5841498958, "area": 172.6336579074},
    "model_43529_4804941b_0026": {"func": model_43529_4804941b_0026, "volume": 3.8709931358, "area": 23.2978838137},
    "model_43529_4804941b_0028": {"func": model_43529_4804941b_0028, "volume": 14.8884351375, "area": 72.6573346654},
    "model_43628_a95b7e66_0021": {"func": model_43628_a95b7e66_0021, "volume": 0.0108760683, "area": 0.4192620234},
    "model_43934_912ff891_0010": {"func": model_43934_912ff891_0010, "volume": 0.6, "area": 5.8},
    "model_43934_912ff891_0027": {"func": model_43934_912ff891_0027, "volume": 7.2, "area": 36.4},
    "model_44021_f141414b_0001": {"func": model_44021_f141414b_0001, "volume": 76, "area": 163.6756330778},
    "model_44211_88463ca8_0000": {"func": model_44211_88463ca8_0000, "volume": 64.9519052838, "area": 159.9038105677},
    "model_44223_74bf8b6f_0000": {"func": model_44223_74bf8b6f_0000, "volume": 47.8365506908, "area": 343.453963821},
    "model_44441_63f1bade_0003": {"func": model_44441_63f1bade_0003, "volume": 0.3747794729, "area": 4.5128725746},
    "model_44519_90af0df6_0018": {"func": model_44519_90af0df6_0018, "volume": 35.7220283159, "area": 60.5119434898},
    "model_44522_a7c79550_0007": {"func": model_44522_a7c79550_0007, "volume": 5.1742031005, "area": 35.0601740141},
    "model_44545_8f5b08e7_0000": {"func": model_44545_8f5b08e7_0000, "volume": 27.6959949644, "area": 209.4927503823},
    "model_44999_3e76c729_0000": {"func": model_44999_3e76c729_0000, "volume": 199.9704100429, "area": 224.9137926473},
    "model_44999_3e76c729_0004": {"func": model_44999_3e76c729_0004, "volume": 45.6604469068, "area": 74.0148391629},
    "model_45235_14713966_0002": {"func": model_45235_14713966_0002, "volume": 7.68143625, "area": 34.482228335},
    "model_45235_14713966_0004": {"func": model_45235_14713966_0004, "volume": 1.4504238693, "area": 22.9775116643},
    "model_45307_b9b4bca0_0006": {"func": model_45307_b9b4bca0_0006, "volume": 0.0003584971, "area": 0.0930836465},
    "model_45359_1768ab3f_0001": {"func": model_45359_1768ab3f_0001, "volume": 0.2811327412, "area": 4.1139822369},
    "model_45359_1768ab3f_0032": {"func": model_45359_1768ab3f_0032, "volume": 1.0936991118, "area": 10.9253096491},
    "model_45466_5f662bcb_0000": {"func": model_45466_5f662bcb_0000, "volume": 3.418692023, "area": 16.4679930707},
    "model_45915_8f1885d2_0000": {"func": model_45915_8f1885d2_0000, "volume": 411.6821070793, "area": 673.3522190823},
    "model_46087_bab56a97_0000": {"func": model_46087_bab56a97_0000, "volume": 1858.0608, "area": 2690.7744},
    "model_46090_18310182_0000": {"func": model_46090_18310182_0000, "volume": 7838.694, "area": 5865.876},
    "model_47790_f29fe247_0000": {"func": model_47790_f29fe247_0000, "volume": 1009.4975058703, "area": 685.5409024023},
    "model_48224_53cae924_0008": {"func": model_48224_53cae924_0008, "volume": 2638.9378290154, "area": 2664.0705702441},
    "model_48290_3a237df1_0000": {"func": model_48290_3a237df1_0000, "volume": 255.4490509118, "area": 474.5150617448},
    "model_48290_3a237df1_0008": {"func": model_48290_3a237df1_0008, "volume": 343.1655195648, "area": 631.2542624258},
    "model_48322_87521a02_0000": {"func": model_48322_87521a02_0000, "volume": 31.38691454, "area": 148.9385336836},
    "model_48475_02526608_0001": {"func": model_48475_02526608_0001, "volume": 22.2075497828, "area": 139.3867874899},
    "model_48475_02526608_0003": {"func": model_48475_02526608_0003, "volume": 1022.5884087435, "area": 1112.1237993708},
    "model_48729_39a46f5b_0000": {"func": model_48729_39a46f5b_0000, "volume": 39.2699081699, "area": 70.6858347058},
    "model_48907_25974aa4_0007": {"func": model_48907_25974aa4_0007, "volume": 1.0607880763, "area": 10.0198404253},
    "model_48907_25974aa4_0008": {"func": model_48907_25974aa4_0008, "volume": 2.9300055932, "area": 14.2541619726},
    "model_49016_cd1b47bf_0001": {"func": model_49016_cd1b47bf_0001, "volume": 1727.8759594744, "area": 1630.9322376632},
    "model_49016_cd1b47bf_0002": {"func": model_49016_cd1b47bf_0002, "volume": 58904.8622548086, "area": 8737.9442064225},
    "model_49016_cd1b47bf_0021": {"func": model_49016_cd1b47bf_0021, "volume": 5497.7871437821, "area": 4838.2692425573},
    "model_49019_748c9a9f_0007": {"func": model_49019_748c9a9f_0007, "volume": 17.3205080757, "area": 45.3205080757},
    "model_49024_b7f02205_0006": {"func": model_49024_b7f02205_0006, "volume": 0.0777544205, "area": 1.5550883944},
    "model_49134_e9867f8b_0002": {"func": model_49134_e9867f8b_0002, "volume": 3796.8, "area": 19128},
    "model_49134_e9867f8b_0013": {"func": model_49134_e9867f8b_0013, "volume": 1675.0387174477, "area": 7151.7123889804},
    "model_49145_4a5b250e_0010": {"func": model_49145_4a5b250e_0010, "volume": 3.2858407346, "area": 22.9823007676},
    "model_49596_4d060b33_0000": {"func": model_49596_4d060b33_0000, "volume": 11.9462165008, "area": 62.2837592599},
    "model_49603_143b8bd2_0007": {"func": model_49603_143b8bd2_0007, "volume": 6.0243822369, "area": 54.7351497809},
    "model_49603_143b8bd2_0008": {"func": model_49603_143b8bd2_0008, "volume": 19.1523822369, "area": 167.9751497809},
    "model_49613_1b97c07b_0015": {"func": model_49613_1b97c07b_0015, "volume": 502.6548245744, "area": 527.7875658031},
    "model_49613_1b97c07b_0017": {"func": model_49613_1b97c07b_0017, "volume": 892.6990816987, "area": 3588.6503084289},
    "model_49703_b92021be_0011": {"func": model_49703_b92021be_0011, "volume": 95.5122033427, "area": 130.3348890995},
    "model_49703_b92021be_0013": {"func": model_49703_b92021be_0013, "volume": 350.5691403571, "area": 410.2110674372},
    "model_50001_e86a6698_0010": {"func": model_50001_e86a6698_0010, "volume": 18539.2721161478, "area": 4778.1682889425},
    "model_50134_aa4781f7_0000": {"func": model_50134_aa4781f7_0000, "volume": 15.3313455453, "area": 62.0079147149},
    "model_50136_229717c0_0000": {"func": model_50136_229717c0_0000, "volume": 6.0870895236, "area": 39.6487008265},
    "model_50382_cb85058c_0019": {"func": model_50382_cb85058c_0019, "volume": 1.2566370614, "area": 26.3893782902},
    "model_50382_cb85058c_0022": {"func": model_50382_cb85058c_0022, "volume": 23.743915156, "area": 378.5351515135},
    "model_50681_eb7a9f92_0001": {"func": model_50681_eb7a9f92_0001, "volume": 2.5792475686, "area": 53.1557476987},
    "model_50681_eb7a9f92_0017": {"func": model_50681_eb7a9f92_0017, "volume": 0.0247253037, "area": 0.9264230876},
    "model_50681_eb7a9f92_0018": {"func": model_50681_eb7a9f92_0018, "volume": 1.9714954087, "area": 40.9538415833},
    "model_50681_eb7a9f92_0019": {"func": model_50681_eb7a9f92_0019, "volume": 0.0525611022, "area": 1.4933092785},
    "model_50777_2934de55_0002": {"func": model_50777_2934de55_0002, "volume": 0.0304349068, "area": 1.207282435},
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
