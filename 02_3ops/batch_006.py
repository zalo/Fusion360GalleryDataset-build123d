"""Batch 006 - passing/02_3ops
141 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_50817_b89fb3ae_0001():
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
            # Profile area: 30.5187792549, perimeter: 19.5834187724
            with BuildLine():
                CenterArc((0, 0), 3.1167979003, -2.5887690372, 5.1775380744)
                CenterArc((0, 0), 3.1167979003, 2.5887690372, 354.8224619256)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

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
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_50833_d533dcbc_0003():
    """Model: left spur gear 1"""
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
            # Profile area: 5.46930434, perimeter: 8.290313947
            with BuildLine():
                CenterArc((0, 0), 1.3194444444, 8.2665492276, 343.4669015447)
                CenterArc((0, 0), 1.3194444444, -8.2665492276, 16.5330984553)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2376095519, perimeter: 1.8933152172
            with BuildLine():
                Line((1.3057352839, 0.1897076974), (1.5495365349, 0.2251290991))
                CenterArc((0, 0), 1.3194444444, -8.2665492276, 16.5330984553)
                Line((1.3057352839, -0.1897076974), (1.5495365349, -0.2251290991))
                _nurbs_edge([(1.5495365349, -0.2251290991), (1.5637360203, -0.225423757), (1.5925184925, -0.226021031), (1.6358232208, -0.2192986508), (1.6795320271, -0.2095727603), (1.723494155, -0.1963257708), (1.7675778359, -0.1800973344), (1.8116810633, -0.1609935426), (1.8556722493, -0.139111852), (1.8995618824, -0.1147010408), (1.9281081621, -0.096552744), (1.9425324824, -0.0873824827)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0425312788, 0.0862112476, 0.1309906176, 0.1768606247, 0.2238163465, 0.2718541955, 0.3209712752, 0.3711651412, 0.4224336927, 0.4224336927, 0.4224336927, 0.4224336927], 3)
                CenterArc((-0.0533342115, 0), 1.9977786559, -2.5069069843, 5.0138139687)
                _nurbs_edge([(1.5495365349, 0.2251290991), (1.5637360203, 0.225423757), (1.5925184925, 0.226021031), (1.6358232208, 0.2192986508), (1.6795320271, 0.2095727603), (1.723494155, 0.1963257708), (1.7675778359, 0.1800973344), (1.8116810633, 0.1609935426), (1.8556722493, 0.139111852), (1.8995618824, 0.1147010408), (1.9281081621, 0.096552744), (1.9425324824, 0.0873824827)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0425312788, 0.0862112476, 0.1309906176, 0.1768606247, 0.2238163465, 0.2718541955, 0.3209712752, 0.3711651412, 0.4224336927, 0.4224336927, 0.4224336927, 0.4224336927], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_50833_d533dcbc_0005():
    """Model: left spur gear 3"""
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
            # Profile area: 23.0438002802, perimeter: 17.0169602069
            with BuildLine():
                CenterArc((0, 0), 2.7083333333, 4.926553838, 350.1468923239)
                CenterArc((0, 0), 2.7083333333, -4.926553838, 9.8531076761)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2565923877, perimeter: 1.9857994066
            with BuildLine():
                Line((2.6983276736, 0.2325880702), (2.8605963858, 0.2465751656))
                CenterArc((0, 0), 2.7083333333, -4.926553838, 9.8531076761)
                Line((2.6983276736, -0.2325880702), (2.8605963858, -0.2465751656))
                _nurbs_edge([(2.8605963858, -0.2465751656), (2.8778635658, -0.2462996002), (2.912713805, -0.2457434284), (2.9648497104, -0.2373328824), (3.0172435058, -0.2260136072), (3.0697765057, -0.2113278569), (3.1223804758, -0.1938433396), (3.1749973342, -0.173695599), (3.2275470725, -0.1510042031), (3.280061828, -0.1260278633), (3.3145261109, -0.1076463493), (3.3318911197, -0.0983847276)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0517447222, 0.1044360425, 0.1580395095, 0.2125510588, 0.2679689615, 0.3242921639, 0.3815198999, 0.4396515576, 0.4986866214, 0.4986866214, 0.4986866214, 0.4986866214], 3)
                CenterArc((-0.0231855093, 0), 3.3565188427, -1.6796679612, 3.3593359224)
                _nurbs_edge([(2.8605963858, 0.2465751656), (2.8778635658, 0.2462996002), (2.912713805, 0.2457434284), (2.9648497104, 0.2373328824), (3.0172435058, 0.2260136072), (3.0697765057, 0.2113278569), (3.1223804758, 0.1938433396), (3.1749973342, 0.173695599), (3.2275470725, 0.1510042031), (3.280061828, 0.1260278633), (3.3145261109, 0.1076463493), (3.3318911197, 0.0983847276)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0517447222, 0.1044360425, 0.1580395095, 0.2125510588, 0.2679689615, 0.3242921639, 0.3815198999, 0.4396515576, 0.4986866214, 0.4986866214, 0.4986866214, 0.4986866214], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_50914_57d3d851_0004():
    """Model: fixturepart6 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6102563891, perimeter: 10.9699111843
            with BuildLine():
                Line((1.0438133513, -0.5919912901), (1.0345861717, 0.607973234))
                Line((1.0345861717, 0.607973234), (-0.0092271796, 1.1999645241))
                Line((-0.0092271796, 1.1999645241), (-1.0438133513, 0.5919912901))
                Line((-1.0438133513, 0.5919912901), (-1.0345861717, -0.607973234))
                Line((-1.0345861717, -0.607973234), (0.0092271796, -1.1999645241))
                Line((0.0092271796, -1.1999645241), (1.0438133513, -0.5919912901))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_50914_f539e302_0000():
    """Model: fixtureassem v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.8413579328, perimeter: 69.2957307073
            with BuildLine():
                Line((-1.9957829895, 0.75), (-9.6967448839, 0.75))
                CenterArc((-10.9957829895, 0), 1.5, 30, 300)
                Line((-1.9957829895, -0.75), (-9.6967448839, -0.75))
                Line((-1.9957829895, -0.5), (-1.9957829895, -0.75))
                Line((-1.9957829895, -0.5), (2.0042170105, -0.5))
                Line((2.0042170105, -0.5), (2.0042170105, -1))
                Line((6, -1), (2.0042170105, -1))
                Line((6, 1), (6, -1))
                Line((6, 1), (2.0042170105, 1))
                Line((2.0042170105, 0.5), (2.0042170105, 1))
                Line((-1.9957829895, 0.5), (2.0042170105, 0.5))
                Line((-1.9957829895, 0.75), (-1.9957829895, 0.5))
            make_face()
            with BuildLine():
                Line((-2.2957829895, 0.25), (-2.2957829895, -0.25))
                Line((-2.2957829895, -0.25), (-9.5167630438, -0.25))
                CenterArc((-10.9957829895, 0), 1.5, -9.5940682269, 19.1881364537)
                Line((-2.2957829895, 0.25), (-9.5167630438, 0.25))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4.5, 0.5), (2.3042170105, 0.5))
                Line((4.5, 0.5), (4.5, -0.5))
                Line((4.5, -0.5), (2.3042170105, -0.5))
                Line((2.3042170105, 0.5), (2.3042170105, -0.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.9957829895, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True)
    return part.part


def model_50947_49287c16_0005():
    """Model: Wire"""
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
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 2.5399999619)):
                Circle(0.635)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


def model_51022_47816098_0008():
    """Model: cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_51024_b2fd60ca_0001():
    """Model: Rotation gear 1"""
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
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

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
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_51341_6ba06c4a_0007():
    """Model: Hinge"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4196979417, perimeter: 3.8199977125
            with BuildLine():
                CenterArc((-3.1326667693, 0.254), 0.4233333441, 36.8698965487, 286.2602069026)
                Line((-2.7940000892, 0.508), (-2.7940000892, 0))
            make_face()
            with BuildLine():
                CenterArc((-3.1326667693, 0.254), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1.27
        extrude(amount=1.27, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4196979417, perimeter: 3.8199977125
            with BuildLine():
                CenterArc((-3.1326667693, 0.254), 0.4233333441, 36.8698965487, 286.2602069026)
                Line((-2.7940000892, 0.508), (-2.7940000892, 0))
            make_face()
            with BuildLine():
                CenterArc((-3.1326667693, 0.254), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.635
        extrude(amount=0.635, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_51345_4b292361_0010():
    """Model: Handle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21.3736079063, perimeter: 22.2495086728
            with BuildLine():
                Line((-5, 0), (5, 0))
                CenterArc((0, -2.6666666667), 5.6666666667, 28.0724869359, 123.8550261283)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_51535_f818cb2a_0001():
    """Model: Arm Middle Rotation Gear 1"""
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
            # Profile area: 10.8816430725, perimeter: 11.6937059884
            with BuildLine():
                CenterArc((0, 0), 1.8611111111, -4.499385751, 8.998771502)
                CenterArc((0, 0), 1.8611111111, 4.499385751, 351.001228498)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0453774683, perimeter: 0.9045440143
            with BuildLine():
                _nurbs_edge([(1.855375492, -0.146001204), (1.8690051999, -0.141907854), (1.8972565147, -0.1323993612), (1.9396827151, -0.1154478541), (1.9829529962, -0.0954220951), (2.0260464921, -0.0727902333), (2.0689886261, -0.0477924602), (2.0969184432, -0.0293882548), (2.1110228496, -0.0200942306)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1337760629, 0.1337760629, 0.1337760629, 0.1337760629, 0.1764735634, 0.2231251709, 0.2707817888, 0.3194422916, 0.3691057661, 0.4197714458, 0.4197714458, 0.4197714458, 0.4197714458], 3)
                CenterArc((-0.1763294621, 0), 2.2874405732, -0.503326482, 1.0066529639)
                _nurbs_edge([(1.855375492, 0.146001204), (1.8690051999, 0.141907854), (1.8972565147, 0.1323993612), (1.9396827151, 0.1154478541), (1.9829529962, 0.0954220951), (2.0260464921, 0.0727902333), (2.0689886261, 0.0477924602), (2.0969184432, 0.0293882548), (2.1110228496, 0.0200942306)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1337760629, 0.1337760629, 0.1337760629, 0.1337760629, 0.1764735634, 0.2231251709, 0.2707817888, 0.3194422916, 0.3691057661, 0.4197714458, 0.4197714458, 0.4197714458, 0.4197714458], 3)
                CenterArc((0, 0), 1.8611111111, -4.499385751, 8.998771502)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_51536_a18dc325_0010():
    """Model: Minute Hand v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2057125482, perimeter: 3.6289790482
            with BuildLine():
                CenterArc((0, 0), 0.15, 5.3793789107, 169.2412421786)
                Line((0, 1.6000000238), (0.1493393655, 0.0140624998))
                Line((0, 1.6000000238), (-0.1493393655, 0.0140624998))
            make_face()
            # Profile area: 0.0392699082, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.15, 174.6206210893, 190.7587578214)
                CenterArc((0, 0), 0.15, 5.3793789107, 169.2412421786)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0392699082, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.15, 174.6206210893, 190.7587578214)
                CenterArc((0, 0), 0.15, 5.3793789107, 169.2412421786)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.ADD)
    return part.part


def model_51567_5f9bb333_0013():
    """Model: Switch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.44, perimeter: 3
            with BuildLine():
                Line((1.6000000075, 2.1000000373), (0.5000000075, 2.1000000373))
                Line((1.6000000075, 2.5000000373), (1.6000000075, 2.1000000373))
                Line((0.5000000075, 2.5000000373), (1.6000000075, 2.5000000373))
                Line((0.5000000075, 2.1000000373), (0.5000000075, 2.5000000373))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_51579_d0c3e154_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            Circle(25)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_51586_2ad96f8c_0002():
    """Model: Spring Axis v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # Symmetric extrude, each_side=0.95
        extrude(amount=0.95, both=True)
    return part.part


def model_51601_2616f89b_0017():
    """Model: base bolt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_51736_e8b2b138_0010():
    """Model: Heads overlay v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0400720225, perimeter: 21.0121065843
            with BuildLine():
                CenterArc((0, 0), 1.7691806277, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.7931132763, perimeter: 9.8960168588
            Circle(1.575)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0400720225, perimeter: 21.0121065843
            with BuildLine():
                CenterArc((0, 0), 1.7691806277, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_51777_87ff5835_0004():
    """Model: Table-007"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 226.61245, perimeter: 163.195
            with BuildLine():
                Line((1.905, 1.27), (1.905, 0.3175))
                Line((1.905, 0.3175), (0.9525, 0.3175))
                Line((0.9525, 0.3175), (0.9525, -1.5875))
                Line((36.83, -1.5875), (0.9525, -1.5875))
                Line((36.83, 1.5875), (36.83, -1.5875))
                Line((-36.83, 1.5875), (36.83, 1.5875))
                Line((-36.83, -1.5875), (-36.83, 1.5875))
                Line((-0.9525, -1.5875), (-36.83, -1.5875))
                Line((-0.9525, -1.5875), (-0.9525, 0.3175))
                Line((-0.9525, 0.3175), (-1.905, 0.3175))
                Line((-1.905, 0.3175), (-1.905, 1.27))
                Line((1.905, 1.27), (-1.905, 1.27))
            make_face()
        # Symmetric extrude, each_side=34.29
        extrude(amount=34.29, both=True)
    return part.part


def model_51777_87ff5835_0006():
    """Model: Table-011"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 924.6814578256, perimeter: 296.634911335
            with BuildLine():
                Line((39.37, -7.62), (-39.37, -7.62))
                Line((39.37, 7.62), (39.37, -7.62))
                Line((-39.37, 7.62), (39.37, 7.62))
                Line((-39.37, -7.62), (-39.37, 7.62))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((7.3025, 3.4925), (7.3025, -3.4925))
                Line((26.9875, 3.4925), (7.3025, 3.4925))
                Line((26.9875, -3.4925), (26.9875, 3.4925))
                Line((7.3025, -3.4925), (26.9875, -3.4925))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-26.9875, 3.4925), (-7.3025, 3.4925))
                Line((-7.3025, 3.4925), (-7.3025, -3.4925))
                Line((-7.3025, -3.4925), (-26.9875, -3.4925))
                Line((-26.9875, -3.4925), (-26.9875, 3.4925))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 16.532225, perimeter: 104.14
            with BuildLine():
                Line((7.3025, -3.4925), (26.9875, -3.4925))
                Line((26.9875, -3.4925), (26.9875, 3.4925))
                Line((26.9875, 3.4925), (7.3025, 3.4925))
                Line((7.3025, 3.4925), (7.3025, -3.4925))
            make_face()
            with BuildLine():
                Line((26.67, 3.175), (7.62, 3.175))
                Line((26.67, -3.175), (26.67, 3.175))
                Line((7.62, -3.175), (26.67, -3.175))
                Line((7.62, 3.175), (7.62, -3.175))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 120.9675, perimeter: 50.8
            with BuildLine():
                Line((7.62, 3.175), (7.62, -3.175))
                Line((7.62, -3.175), (26.67, -3.175))
                Line((26.67, -3.175), (26.67, 3.175))
                Line((26.67, 3.175), (7.62, 3.175))
            make_face()
            # Profile area: 16.532225, perimeter: 104.14
            with BuildLine():
                Line((-26.9875, -3.4925), (-26.9875, 3.4925))
                Line((-7.3025, -3.4925), (-26.9875, -3.4925))
                Line((-7.3025, 3.4925), (-7.3025, -3.4925))
                Line((-26.9875, 3.4925), (-7.3025, 3.4925))
            make_face()
            with BuildLine():
                Line((-26.67, -3.175), (-26.67, 3.175))
                Line((-26.67, 3.175), (-7.62, 3.175))
                Line((-7.62, 3.175), (-7.62, -3.175))
                Line((-7.62, -3.175), (-26.67, -3.175))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 120.9675, perimeter: 50.8
            with BuildLine():
                Line((-7.62, -3.175), (-26.67, -3.175))
                Line((-7.62, 3.175), (-7.62, -3.175))
                Line((-26.67, 3.175), (-7.62, 3.175))
                Line((-26.67, -3.175), (-26.67, 3.175))
            make_face()
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.532225, perimeter: 104.14
            with BuildLine():
                Line((-26.9875, -3.4925), (-26.9875, 3.4925))
                Line((-7.3025, -3.4925), (-26.9875, -3.4925))
                Line((-7.3025, 3.4925), (-7.3025, -3.4925))
                Line((-26.9875, 3.4925), (-7.3025, 3.4925))
            make_face()
            with BuildLine():
                Line((-26.67, -3.175), (-26.67, 3.175))
                Line((-26.67, 3.175), (-7.62, 3.175))
                Line((-7.62, 3.175), (-7.62, -3.175))
                Line((-7.62, -3.175), (-26.67, -3.175))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 16.532225, perimeter: 104.14
            with BuildLine():
                Line((7.3025, -3.4925), (26.9875, -3.4925))
                Line((26.9875, -3.4925), (26.9875, 3.4925))
                Line((26.9875, 3.4925), (7.3025, 3.4925))
                Line((7.3025, 3.4925), (7.3025, -3.4925))
            make_face()
            with BuildLine():
                Line((26.67, 3.175), (7.62, 3.175))
                Line((26.67, -3.175), (26.67, 3.175))
                Line((7.62, -3.175), (26.67, -3.175))
                Line((7.62, 3.175), (7.62, -3.175))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.SUBTRACT)
    return part.part


def model_51777_87ff5835_0008():
    """Model: Table-002"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.4986626045, perimeter: 42.2696453401
            with BuildLine():
                Line((0.9525, -7.62), (-0.9525, -7.62))
                Line((0.9525, 7.62), (0.9525, -7.62))
                Line((-0.9525, 7.62), (0.9525, 7.62))
                Line((-0.9525, -7.62), (-0.9525, 7.62))
            make_face()
            with BuildLine():
                CenterArc((0, -6.35), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 6.35), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


def model_51777_87ff5835_0009():
    """Model: Table-001"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33725.3092475099, perimeter: 681.9787204071
            with BuildLine():
                CenterArc((-50.8, 0), 76.2, 90, 180)
                Line((-50.8, -76.2), (50.8, -76.2))
                CenterArc((50.8, 0), 76.2, -90, 180)
                Line((-50.8, 76.2), (50.8, 76.2))
            make_face()
        # Symmetric extrude, each_side=5.08
        extrude(amount=5.08, both=True)
    return part.part


def model_51862_e5f65013_0001():
    """Model: spur gear3 (1)"""
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
            # Profile area: 0.4194212086, perimeter: 2.2957792469
            with BuildLine():
                CenterArc((0, 0), 0.3653846154, 8.2665492276, 343.4669015447)
                CenterArc((0, 0), 0.3653846154, -8.2665492276, 16.5330984553)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0182214189, perimeter: 0.5243026755
            with BuildLine():
                Line((0.3615882325, 0.0525344393), (0.4291024251, 0.0623434428))
                CenterArc((0, 0), 0.3653846154, -8.2665492276, 16.5330984553)
                Line((0.3615882325, -0.0525344393), (0.4291024251, -0.0623434428))
                _nurbs_edge([(0.4291024251, -0.0623434428), (0.4330345902, -0.0624250404), (0.441005121, -0.0625904393), (0.4529971996, -0.0607288571), (0.4651011767, -0.0580355336), (0.4772753045, -0.0543671365), (0.489483093, -0.049873108), (0.5016962945, -0.0445828272), (0.513878469, -0.0385232821), (0.5260325213, -0.0317633652), (0.5339376449, -0.026737683), (0.5379320721, -0.024198226)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0117778926, 0.0238738839, 0.0362743249, 0.0489767884, 0.0619799113, 0.0752827003, 0.0888843531, 0.102784193, 0.116981638, 0.116981638, 0.116981638, 0.116981638], 3)
                CenterArc((-0.0147694739, 0), 0.5532310124, -2.5069069843, 5.0138139687)
                _nurbs_edge([(0.4291024251, 0.0623434428), (0.4330345902, 0.0624250404), (0.441005121, 0.0625904393), (0.4529971996, 0.0607288571), (0.4651011767, 0.0580355336), (0.4772753045, 0.0543671365), (0.489483093, 0.049873108), (0.5016962945, 0.0445828272), (0.513878469, 0.0385232821), (0.5260325213, 0.0317633652), (0.5339376449, 0.026737683), (0.5379320721, 0.024198226)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0117778926, 0.0238738839, 0.0362743249, 0.0489767884, 0.0619799113, 0.0752827003, 0.0888843531, 0.102784193, 0.116981638, 0.116981638, 0.116981638, 0.116981638], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_51862_e5f65013_0002():
    """Model: spur gear1 (1)"""
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
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 1.75, -2.6788395466, 5.3576790932)
                CenterArc((0, 0), 1.75, 2.6788395466, 354.6423209068)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0211079173, perimeter: 0.5895110416
            with BuildLine():
                _nurbs_edge([(1.7480876073, -0.0817906913), (1.7500094028, -0.0816610168), (1.7590006194, -0.0809481254), (1.7750383362, -0.0784434465), (1.7961607495, -0.074204276), (1.8173049581, -0.0688763649), (1.838460406, -0.06265518), (1.8596160201, -0.0555925665), (1.880754998, -0.0477334611), (1.9018907922, -0.0391671579), (1.9158362463, -0.0329091682), (1.9228471549, -0.0297630395)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0152492069, 0.0152492069, 0.0152492069, 0.0152492069, 0.0210294705, 0.0423206841, 0.0638645651, 0.0856602136, 0.107707315, 0.1300057118, 0.1525553079, 0.1753560363, 0.1984078462, 0.1984078462, 0.1984078462, 0.1984078462], 3)
                CenterArc((-0.0047169955, 0), 1.9277939186, -0.8846196078, 1.7692392156)
                _nurbs_edge([(1.7480876073, 0.0817906913), (1.7500094028, 0.0816610168), (1.7590006194, 0.0809481254), (1.7750383362, 0.0784434465), (1.7961607495, 0.074204276), (1.8173049581, 0.0688763649), (1.838460406, 0.06265518), (1.8596160201, 0.0555925665), (1.880754998, 0.0477334611), (1.9018907922, 0.0391671579), (1.9158362463, 0.0329091682), (1.9228471549, 0.0297630395)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0152492069, 0.0152492069, 0.0152492069, 0.0152492069, 0.0210294705, 0.0423206841, 0.0638645651, 0.0856602136, 0.107707315, 0.1300057118, 0.1525553079, 0.1753560363, 0.1984078462, 0.1984078462, 0.1984078462, 0.1984078462], 3)
                CenterArc((0, 0), 1.75, -2.6788395466, 5.3576790932)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_51872_765c2fb4_0001():
    """Model: Cross Mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.200000155, perimeter: 21.8000003248
            with BuildLine():
                Line((-3.0000000447, 0.200000003), (-3.0000000447, -2.5000000373))
                Line((-3.0000000447, -2.5000000373), (-2.5000000373, -2.5000000373))
                Line((-2.5000000373, -2.5000000373), (-2.5000000373, -0.3000000045))
                Line((-2.5000000373, -0.3000000045), (2.5000000373, -0.3000000045))
                Line((2.5000000373, -0.3000000045), (2.5000000373, -2.5000000373))
                Line((2.5000000373, -2.5000000373), (3.0000000447, -2.5000000373))
                Line((3.0000000447, -2.5000000373), (3.0000000447, 0.200000003))
                Line((-3.0000000447, 0.200000003), (3.0000000447, 0.200000003))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_51877_0032e502_0001():
    """Model: Base part 1 v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.0000003576, perimeter: 14.0000002086
            with BuildLine():
                Line((3.0000000447, -4.0000000596), (0, -4.0000000596))
                Line((3.0000000447, 0), (3.0000000447, -4.0000000596))
                Line((0, 0), (3.0000000447, 0))
                Line((0, -4.0000000596), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_51877_0032e502_0004():
    """Model: Fourth v3"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.605198751, perimeter: 9.1106188312
            with BuildLine():
                CenterArc((1.4500000216, 0), 1.4500000216, -58.8526100785, 297.705220157)
                CenterArc((1.4500000216, 0), 1.4500000216, -121.1473899215, 62.294779843)
            make_face()
            # Profile area: 0.5513039659, perimeter: 4.0945764037
            with BuildLine():
                Line((0.7000000104, -1.7500000261), (2.2000000328, -1.7500000261))
                Line((2.2000000328, -1.7500000261), (2.2000000328, -1.2409673831))
                CenterArc((1.4500000216, 0), 1.4500000216, -121.1473899215, 62.294779843)
                Line((0.7000000104, -1.7500000261), (0.7000000104, -1.2409673831))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_51877_0032e502_0014():
    """Model: Handle thing v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            with Locations((0.1500000022, 0)):
                Circle(0.1500000022)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_51877_0032e502_0015():
    """Model: Leg attachment v3 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2750000082, perimeter: 2.1099019828
            with BuildLine():
                Line((0, -0.6000000089), (0, 0))
                Line((0, 0), (-0.5000000075, 0))
                Line((-0.5000000075, 0), (-0.5000000075, -0.5000000075))
                Line((-0.5000000075, -0.5000000075), (0, -0.6000000089))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_51891_9455ea02_0004():
    """Model: BallCasterConnect v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.4300169546, perimeter: 18.5764917153
            with BuildLine():
                CenterArc((-2.54, 0), 0.635, 120, 120)
                Line((-2.8575, -0.5499261314), (-0.9525, -1.6497783942))
                CenterArc((0, 0), 1.905, -120, 60)
                Line((2.8575, -0.5499261314), (0.9525, -1.6497783942))
                CenterArc((2.54, 0), 0.635, -60, 120)
                Line((2.8575, 0.5499261314), (0.9525, 1.6497783942))
                CenterArc((0, 0), 1.905, 60, 60)
                Line((-2.8575, 0.5499261314), (-0.9525, 1.6497783942))
            make_face()
            with BuildLine():
                CenterArc((2.54, 0), 0.24892, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.54, 0), 0.2489117541, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((2.54, 0)):
                Circle(0.24892)
            # Profile area: 0.1946438487, perimeter: 1.5639586761
            with Locations((-2.54, 0)):
                Circle(0.2489117541)
        # OneSide extrude, distance=3.048
        extrude(amount=3.048)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((2.54, 0)):
                Circle(0.24892)
            # Profile area: 0.1946438487, perimeter: 1.5639586761
            with Locations((-2.54, 0)):
                Circle(0.2489117541)
        # OneSide extrude, distance=1.016
        extrude(amount=1.016, mode=Mode.SUBTRACT)
    return part.part


def model_51914_fb924efa_0004():
    """Model: rdzen poziom"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 29.5385621722)):
                Circle(0.5)
        # TwoSides extrude (symmetric), distance=2.5
        extrude(amount=2.5, both=True)
    return part.part


def model_51915_e704f5dd_0001():
    """Model: Rotor circle gear"""
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
            # Profile area: 276.1165418194, perimeter: 58.9048622548
            with BuildLine():
                CenterArc((0, 0), 9.375, 3.0994134585, 353.8011730829)
                CenterArc((0, 0), 9.375, -3.0994134585, 6.1988269171)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.8817096894, perimeter: 3.7738221475
            with BuildLine():
                Line((9.3612864739, 0.5068930395), (9.3831402771, 0.5080763748))
                CenterArc((0, 0), 9.375, -3.0994134585, 6.1988269171)
                Line((9.3612864739, -0.5068930395), (9.3831402771, -0.5080763748))
                _nurbs_edge([(9.3831402771, -0.5080763748), (9.424245084, -0.5067099235), (9.5070073786, -0.5039586481), (9.6306137665, -0.4844594246), (9.7545837508, -0.4591508326), (9.8787123046, -0.4271665295), (10.0029230338, -0.3896922994), (10.1271402638, -0.347037388), (10.2512517345, -0.299470528), (10.3753374833, -0.2475329323), (10.4571376742, -0.209540132), (10.4982779921, -0.1904321585)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.123271535, 0.2482005364, 0.3747292293, 0.5028517667, 0.6325660481, 0.763870987, 0.8967658966, 1.0312502841, 1.1673237655, 1.1673237655, 1.1673237655, 1.1673237655], 3)
                CenterArc((-0.0305478943, 0), 10.5305478943, -1.0361810088, 2.0723620176)
                _nurbs_edge([(9.3831402771, 0.5080763748), (9.424245084, 0.5067099235), (9.5070073786, 0.5039586481), (9.6306137665, 0.4844594246), (9.7545837508, 0.4591508326), (9.8787123046, 0.4271665295), (10.0029230338, 0.3896922994), (10.1271402638, 0.347037388), (10.2512517345, 0.299470528), (10.3753374833, 0.2475329323), (10.4571376742, 0.209540132), (10.4982779921, 0.1904321585)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.123271535, 0.2482005364, 0.3747292293, 0.5028517667, 0.6325660481, 0.763870987, 0.8967658966, 1.0312502841, 1.1673237655, 1.1673237655, 1.1673237655, 1.1673237655], 3)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_51916_fa226b15_0003():
    """Model: D-loop Bracket"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2531664312, perimeter: 4.1718936208
            with BuildLine():
                Line((-0.5079999939, -1.0160000203), (-0.5079999939, -1.2064999847))
                CenterArc((-0.4444999939, -1.2064999847), 0.0635, 180, 90)
                Line((-0.3809999954, -1.2699999847), (-0.4444999939, -1.2699999847))
                Line((-0.3809999954, -1.2699999847), (-0.3809999954, 0))
                Line((-0.3809999954, 0), (-0.4444999939, 0))
                CenterArc((-0.4444999939, -0.0635), 0.0635, 90, 90)
                Line((-0.5079999939, -0.0635), (-0.5079999939, -0.2540000203))
                CenterArc((-0.6349999939, -0.2540000203), 0.127, -90.0000039708, 90.0000039708)
                CenterArc((-0.6350000203, -0.6350000203), 0.254, 89.9999960292, 180.0000078714)
                CenterArc((-0.6349999939, -1.0160000203), 0.127, 0, 90.0000039708)
            make_face()
            with BuildLine():
                CenterArc((-0.6350000203, -0.6350000203), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5875
        extrude(amount=1.5875)
    return part.part


def model_51916_fa226b15_0007():
    """Model: Handle Sleeve"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8732719702, perimeter: 23.4601572999
            with BuildLine():
                CenterArc((3.8100001216, -2.5400000811), 2.032, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.8100001216, -2.5400000811), 1.7018, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-9.525
        extrude(amount=-9.525)
    return part.part


def model_51916_fa226b15_0012():
    """Model: Cantilever"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3979387501, perimeter: 6.9657979481
            with BuildLine():
                Line((5.9690001621, -1.0158000324), (5.9690001621, -1.0162000324))
                CenterArc((5.9690001905, -0.5078000162), 0.5080000162, -90.0000031999, 180.0000063891)
                Line((5.0800001621, 0.0002), (5.9690001622, 0.0002))
                CenterArc((5.0800001621, -0.5080000162), 0.5082000162, 90, 180)
                Line((5.9690001621, -1.0162000324), (5.0800001621, -1.0162000324))
            make_face()
            with BuildLine():
                CenterArc((5.5245001621, -0.5080000162), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_51940_aa0fca73_0022():
    """Model: blocco 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 91.6088417787, perimeter: 50.8938009882
            with BuildLine():
                CenterArc((0, 0), 5.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_51942_f6e66631_0005():
    """Model: Bearing Bush"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6597344573, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_52012_77070fda_0017():
    """Model: LEFT Side view mirror v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3026548246, perimeter: 4.5132741229
            with BuildLine():
                CenterArc((-2.5, 2.5), 0.4, 0, 180)
                Line((-2.9, 2.5), (-2.9, 1.5))
                CenterArc((-2.5, 1.5), 0.4, 180, 180)
                Line((-2.1, 1.5), (-2.1, 2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_52557_e6a00b06_0014():
    """Model: fan"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.4950302329, perimeter: 13.9935979241
            with BuildLine():
                CenterArc((-65, 15), 1.5, 0, 360)
            make_face()
            with BuildLine():
                Line((-65.5, 15.5590169944), (-65.5, 14.4409830056))
                CenterArc((-65, 15), 0.75, -131.8103148958, 263.6206297916)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_52660_3593651a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1214, perimeter: 174
            with BuildLine():
                Line((-100, 50), (-50, 50))
                Line((-100, 25), (-100, 50))
                Line((-100, 25), (-50, 25))
                Line((-50, 50), (-50, 25))
            make_face()
            with BuildLine():
                Line((-99, 43), (-99, 49))
                Line((-99, 49), (-93, 49))
                Line((-93, 49), (-93, 43))
                Line((-93, 43), (-99, 43))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1214, perimeter: 174
            with BuildLine():
                Line((-50, 25), (-50, 0))
                Line((0, 0), (-50, 0))
                Line((0, 25), (0, 0))
                Line((-50, 25), (0, 25))
            make_face()
            with BuildLine():
                Line((-8.0123804599, 1), (-2.0123804599, 1))
                Line((-8.0123804599, 7), (-8.0123804599, 1))
                Line((-2.0123804599, 7), (-8.0123804599, 7))
                Line((-2.0123804599, 1), (-2.0123804599, 7))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1214, perimeter: 174
            with BuildLine():
                Line((-50, 50), (-50, 25))
                Line((-50, 25), (0, 25))
                Line((0, 50), (0, 25))
                Line((-50, 50), (0, 50))
            make_face()
            with BuildLine():
                Line((-7, 43), (-1, 43))
                Line((-7, 49), (-7, 43))
                Line((-1, 49), (-7, 49))
                Line((-1, 43), (-1, 49))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1214, perimeter: 174
            with BuildLine():
                Line((-100, 0), (-100, 25))
                Line((-50, 0), (-100, 0))
                Line((-50, 25), (-50, 0))
                Line((-100, 25), (-50, 25))
            make_face()
            with BuildLine():
                Line((-93, 7), (-93, 1))
                Line((-93, 1), (-99, 1))
                Line((-99, 1), (-99, 7))
                Line((-99, 7), (-93, 7))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-93, 43), (-99, 43))
                Line((-93, 49), (-93, 43))
                Line((-99, 49), (-93, 49))
                Line((-99, 43), (-99, 49))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-2.0123804599, 1), (-2.0123804599, 7))
                Line((-2.0123804599, 7), (-8.0123804599, 7))
                Line((-8.0123804599, 7), (-8.0123804599, 1))
                Line((-8.0123804599, 1), (-2.0123804599, 1))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-1, 43), (-1, 49))
                Line((-1, 49), (-7, 49))
                Line((-7, 49), (-7, 43))
                Line((-7, 43), (-1, 43))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-99, 7), (-93, 7))
                Line((-99, 1), (-99, 7))
                Line((-93, 1), (-99, 1))
                Line((-93, 7), (-93, 1))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-1, 43), (-1, 49))
                Line((-1, 49), (-7, 49))
                Line((-7, 49), (-7, 43))
                Line((-7, 43), (-1, 43))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-2.0123804599, 1), (-2.0123804599, 7))
                Line((-2.0123804599, 7), (-8.0123804599, 7))
                Line((-8.0123804599, 7), (-8.0123804599, 1))
                Line((-8.0123804599, 1), (-2.0123804599, 1))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-93, 43), (-99, 43))
                Line((-93, 49), (-93, 43))
                Line((-99, 49), (-93, 49))
                Line((-99, 43), (-99, 49))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-99, 7), (-93, 7))
                Line((-99, 1), (-99, 7))
                Line((-93, 1), (-99, 1))
                Line((-93, 7), (-93, 1))
            make_face()
        # OneSide extrude, distance=-46
        extrude(amount=-46, mode=Mode.ADD)
    return part.part


def model_52879_de812eb3_0008():
    """Model: collar v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8981192229, perimeter: 12.8805298797
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_52884_c8150d6e_0034():
    """Model: chain part v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.842743396, perimeter: 5.0849556756
            with BuildLine():
                CenterArc((0.5000000119, -0.3000000089), 0.3, -90, 90)
                Line((0.8000000119, -0.3000000089), (0.8000000119, 0.3000000089))
                CenterArc((0.5000000119, 0.3000000089), 0.3, 0, 90)
                Line((0.5000000119, 0.6000000089), (-0.5000000119, 0.6000000089))
                CenterArc((-0.5000000119, 0.3000000089), 0.3, 90, 90)
                Line((-0.8000000119, 0.3000000089), (-0.8000000119, -0.3000000089))
                CenterArc((-0.5000000119, -0.3000000089), 0.3, 180, 90)
                Line((-0.5000000119, -0.6000000089), (0.5000000119, -0.6000000089))
            make_face()
        # Symmetric extrude, each_side=0.9014
        extrude(amount=0.9014, both=True)
    return part.part


def model_53078_b592f2bd_0002():
    """Model: fan"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.0796447372, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((75, 25), 2.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((75, 25), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_53222_e9c623af_0001():
    """Model: piston pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3375527072, perimeter: 4.0997784129
            Circle(0.6525)
        # OneSide extrude, distance=5.98
        extrude(amount=5.98)
    return part.part


def model_53448_2f7c767c_0018():
    """Model: fanshaft2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6597344573, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_53448_2f7c767c_0022():
    """Model: rivet0.2 v1 (2) (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_53846_89405f98_0016():
    """Model: holder v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0283528737, perimeter: 0.5969026042
            Circle(0.095)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


def model_53927_ef5208b9_0006():
    """Model: top link"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.8581040454, perimeter: 23.6414440046
            with BuildLine():
                Line((51.3651212352, 2.3887558973), (53.079759424, -0.270920391))
                CenterArc((53.5, 0), 0.5, -147.1909630107, 186.2149914903)
                Line((53.8884409856, 0.3148231261), (51.5157667299, 4.3065692097))
                CenterArc((51, 4), 0.6, 30.7270417062, 130.0846600486)
                Line((49.0442134762, 0.2055690753), (50.4333338902, 4.1972042596))
                CenterArc((49.5, 0), 0.5, 155.7236482857, 202.0399482108)
                Line((49.9996191623, -0.019511347), (50.9221089025, 2.3441873709))
                CenterArc((51.1550009472, 2.2532957017), 0.25, 32.8090369893, 125.8715628897)
            make_face()
            with BuildLine():
                CenterArc((49.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((51, 4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((53.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.8581040454, perimeter: 23.6414440046
            with BuildLine():
                Line((51.3651212352, 2.3887558973), (53.079759424, -0.270920391))
                CenterArc((53.5, 0), 0.5, -147.1909630107, 186.2149914903)
                Line((53.8884409856, 0.3148231261), (51.5157667299, 4.3065692097))
                CenterArc((51, 4), 0.6, 30.7270417062, 130.0846600486)
                Line((49.0442134762, 0.2055690753), (50.4333338902, 4.1972042596))
                CenterArc((49.5, 0), 0.5, 155.7236482857, 202.0399482108)
                Line((49.9996191623, -0.019511347), (50.9221089025, 2.3441873709))
                CenterArc((51.1550009472, 2.2532957017), 0.25, 32.8090369893, 125.8715628897)
            make_face()
            with BuildLine():
                CenterArc((49.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((51, 4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((53.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_53927_ef5208b9_0008():
    """Model: middle link"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.4810968206, perimeter: 24.8980649546
            with BuildLine():
                CenterArc((46.5, 0), 0.5, -87.3627978277, 126.3868263074)
                Line((46.8884409856, 0.3148231261), (44.5157667299, 4.3065692097))
                CenterArc((44, 4), 0.6, 30.7270417062, 130.0846600486)
                Line((42.0442134762, 0.2055690753), (43.4333338902, 4.1972042596))
                CenterArc((42.5, 0), 0.5, 155.7236482857, 202.0399482108)
                Line((42.9996191623, -0.019511347), (43.9221089025, 2.3441873709))
                CenterArc((44.1550009472, 2.2532957017), 0.25, 32.8090369893, 125.8715628897)
                Line((44.3651212352, 2.3887558973), (46.079759424, -0.270920391))
                CenterArc((46.5, 0), 0.5, -147.1909630107, 54.568844627)
                Line((46.5230058053, -0.4994704525), (46.477125687, -0.4994764917))
            make_face()
            with BuildLine():
                CenterArc((44, 4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((46.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((42.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.4810968206, perimeter: 24.8980649546
            with BuildLine():
                CenterArc((46.5, 0), 0.5, -87.3627978277, 126.3868263074)
                Line((46.8884409856, 0.3148231261), (44.5157667299, 4.3065692097))
                CenterArc((44, 4), 0.6, 30.7270417062, 130.0846600486)
                Line((42.0442134762, 0.2055690753), (43.4333338902, 4.1972042596))
                CenterArc((42.5, 0), 0.5, 155.7236482857, 202.0399482108)
                Line((42.9996191623, -0.019511347), (43.9221089025, 2.3441873709))
                CenterArc((44.1550009472, 2.2532957017), 0.25, 32.8090369893, 125.8715628897)
                Line((44.3651212352, 2.3887558973), (46.079759424, -0.270920391))
                CenterArc((46.5, 0), 0.5, -147.1909630107, 54.568844627)
                Line((46.5230058053, -0.4994704525), (46.477125687, -0.4994764917))
            make_face()
            with BuildLine():
                CenterArc((44, 4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((46.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((42.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_54037_43125db1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59.4280476548, perimeter: 37.1228584952
            with BuildLine():
                Line((2.3819238499, -0.3412951185), (2.3819238499, -4.5730103971))
                Line((2.3819238499, -4.5730103971), (6.7226103373, -4.5730103971))
                Line((6.7226103373, -4.5730103971), (6.7226103373, 3.6179921378))
                Line((-3.6478163754, 3.6179921378), (6.7226103373, 3.6179921378))
                Line((-3.6478163754, -0.3412951185), (-3.6478163754, 3.6179921378))
                Line((2.3819238499, -0.3412951185), (-3.6478163754, -0.3412951185))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_54273_21c2b38f_0046():
    """Model: corner piece v4 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.24, perimeter: 7.2
            with BuildLine():
                Line((-0.9, 0.9), (0.9, 0.9))
                Line((-0.9, -0.9), (-0.9, 0.9))
                Line((0.9, -0.9), (-0.9, -0.9))
                Line((0.9, 0.9), (0.9, -0.9))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_54285_76f37095_0005():
    """Model: Rivet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


def model_54374_5c085a74_0011():
    """Model: big gear"""
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
            # Profile area: 11.2914621373, perimeter: 11.9118721449
            with BuildLine():
                CenterArc((0, 0), 1.8958333333, 2.1910921689, 355.6178156623)
                CenterArc((0, 0), 1.8958333333, -2.1910921689, 4.3821843377)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0239105934, perimeter: 0.6110478413
            with BuildLine():
                Line((1.8944472375, 0.0724823574), (1.934877529, 0.0740292375))
                CenterArc((0, 0), 1.8958333333, -2.1910921689, 4.3821843377)
                Line((1.8944472375, -0.0724823574), (1.934877529, -0.0740292375))
                _nurbs_edge([(1.934877529, -0.0740292375), (1.9403441472, -0.0738542886), (1.9513251307, -0.0735028627), (1.9677426548, -0.0713393152), (1.9841908761, -0.0685681452), (2.0006532747, -0.0651032723), (2.0171255274, -0.0610742593), (2.0336029107, -0.0565175243), (2.0500777145, -0.0514643119), (2.0665581978, -0.0459742569), (2.0774717795, -0.0419693563), (2.0829500819, -0.039959012)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0163986856, 0.0329406016, 0.0496208086, 0.0664388281, 0.0833944987, 0.1004877432, 0.1177185169, 0.1350867906, 0.1525925432, 0.1525925432, 0.1525925432, 0.1525925432], 3)
                CenterArc((0.000014848, 0), 2.0833184853, -1.0990269414, 2.1980538828)
                _nurbs_edge([(1.934877529, 0.0740292375), (1.9403441472, 0.0738542886), (1.9513251307, 0.0735028627), (1.9677426548, 0.0713393152), (1.9841908761, 0.0685681452), (2.0006532747, 0.0651032723), (2.0171255274, 0.0610742593), (2.0336029107, 0.0565175243), (2.0500777145, 0.0514643119), (2.0665581978, 0.0459742569), (2.0774717795, 0.0419693563), (2.0829500819, 0.039959012)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0163986856, 0.0329406016, 0.0496208086, 0.0664388281, 0.0833944987, 0.1004877432, 0.1177185169, 0.1350867906, 0.1525925432, 0.1525925432, 0.1525925432, 0.1525925432], 3)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_54374_5c085a74_0014():
    """Model: planet (1)"""
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
                CenterArc((0, 0), 0.3958333333, 7.7459236004, 344.5081527993)
                CenterArc((0, 0), 0.3958333333, -7.7459236004, 15.4918472007)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0212568927, perimeter: 0.5672574041
            with BuildLine():
                Line((0.3922215478, 0.0533505881), (0.4795747785, 0.0652325112))
                CenterArc((0, 0), 0.3958333333, -7.7459236004, 15.4918472007)
                Line((0.3922215478, -0.0533505881), (0.4795747785, -0.0652325112))
                _nurbs_edge([(0.4795747785, -0.0652325112), (0.4832929905, -0.0653114216), (0.4908150952, -0.065471061), (0.5021320512, -0.0638774818), (0.5135437511, -0.0615709597), (0.5250191621, -0.0584326688), (0.5365311835, -0.0545954109), (0.5480595818, -0.050087635), (0.5595779227, -0.0449347393), (0.5710901739, -0.0391978874), (0.5786193315, -0.034933781), (0.5824189, -0.0327819116)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.011140107, 0.0225369213, 0.0341797486, 0.0460668219, 0.0581971933, 0.0705701885, 0.0831852688, 0.0960419786, 0.1091399224, 0.1091399224, 0.1091399224, 0.1091399224], 3)
                CenterArc((-0.0047302501, 0), 0.5880635834, -3.195639726, 6.391279452)
                _nurbs_edge([(0.4795747785, 0.0652325112), (0.4832929905, 0.0653114216), (0.4908150952, 0.065471061), (0.5021320512, 0.0638774818), (0.5135437511, 0.0615709597), (0.5250191621, 0.0584326688), (0.5365311835, 0.0545954109), (0.5480595818, 0.050087635), (0.5595779227, 0.0449347393), (0.5710901739, 0.0391978874), (0.5786193315, 0.034933781), (0.5824189, 0.0327819116)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.011140107, 0.0225369213, 0.0341797486, 0.0460668219, 0.0581971933, 0.0705701885, 0.0831852688, 0.0960419786, 0.1091399224, 0.1091399224, 0.1091399224, 0.1091399224], 3)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_54375_f795a300_0004():
    """Model: timon v1"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # TwoSides extrude, along=20, against=-2
        extrude(amount=20)
        extrude(sk.sketch, amount=-2)
    return part.part


def model_54501_96041527_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.5, perimeter: 23
            with BuildLine():
                Line((5, -6.5), (0, -6.5))
                Line((5, 0), (5, -6.5))
                Line((0, 0), (5, 0))
                Line((0, -6.5), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_54608_56e6ef8c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.7079632679, perimeter: 14.0496294621
            Circle(2.2360679775)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_54761_cec613c4_0015():
    """Model: Component18"""
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
            # Profile area: 2.0907690721, perimeter: 5.1257564348
            with BuildLine():
                CenterArc((0, 0), 0.8157894737, 5.8236408384, 348.3527183231)
                CenterArc((0, 0), 0.8157894737, -5.8236408384, 11.6472816769)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0359825066, perimeter: 0.740670891
            with BuildLine():
                Line((0.8115791249, 0.0827755366), (0.8855926255, 0.0903244089))
                CenterArc((0, 0), 0.8157894737, -5.8236408384, 11.6472816769)
                Line((0.8115791249, -0.0827755366), (0.8855926255, -0.0903244089))
                _nurbs_edge([(0.8855926255, -0.0903244089), (0.8916694393, -0.0902839702), (0.9039485589, -0.0902022575), (0.9223404077, -0.087240227), (0.9408432592, -0.0831799838), (0.9594094944, -0.0778442841), (0.9780075459, -0.0714428065), (0.9966115421, -0.0640232973), (1.0151866659, -0.0556282554), (1.0337431461, -0.0463533407), (1.045893261, -0.0395082837), (1.0520202361, -0.0360565061)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0182056819, 0.0367873279, 0.0557307954, 0.0750342385, 0.0946968006, 0.1147179244, 0.1350971865, 0.1558342396, 0.1769287867, 0.1769287867, 0.1769287867, 0.1769287867], 3)
                CenterArc((-0.0109659286, 0), 1.0635975075, -1.9427288204, 3.8854576409)
                _nurbs_edge([(0.8855926255, 0.0903244089), (0.8916694393, 0.0902839702), (0.9039485589, 0.0902022575), (0.9223404077, 0.087240227), (0.9408432592, 0.0831799838), (0.9594094944, 0.0778442841), (0.9780075459, 0.0714428065), (0.9966115421, 0.0640232973), (1.0151866659, 0.0556282554), (1.0337431461, 0.0463533407), (1.045893261, 0.0395082837), (1.0520202361, 0.0360565061)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0182056819, 0.0367873279, 0.0557307954, 0.0750342385, 0.0946968006, 0.1147179244, 0.1350971865, 0.1558342396, 0.1769287867, 0.1769287867, 0.1769287867, 0.1769287867], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_54761_cec613c4_0017():
    """Model: Component16"""
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
            # Profile area: 7.4091898169, perimeter: 9.649177436
            with BuildLine():
                CenterArc((0, 0), 1.5357142857, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.5357142857, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0685368192, perimeter: 1.0285424158
            with BuildLine():
                Line((1.5307908238, 0.1228731915), (1.6057037965, 0.1288862901))
                CenterArc((0, 0), 1.5357142857, -4.5891664191, 9.1783328383)
                Line((1.5307908238, -0.1228731915), (1.6057037965, -0.1288862901))
                _nurbs_edge([(1.6057037965, -0.1288862901), (1.614901327, -0.1287084809), (1.633456455, -0.128349768), (1.661204036, -0.1238793625), (1.689077987, -0.1179035036), (1.717018357, -0.1101875616), (1.7449927672, -0.1010277989), (1.7729731424, -0.0904961682), (1.8009204021, -0.0786559458), (1.8288520674, -0.0656421305), (1.847198586, -0.0560748246), (1.8564395878, -0.0512558454)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0275656044, 0.0556109403, 0.0841187273, 0.1130869955, 0.1425149344, 0.1724020638, 0.2027480417, 0.2335525987, 0.2648155097, 0.2648155097, 0.2648155097, 0.2648155097], 3)
                CenterArc((-0.0110291146, 0), 1.8681719717, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.6057037965, 0.1288862901), (1.614901327, 0.1287084809), (1.633456455, 0.128349768), (1.661204036, 0.1238793625), (1.689077987, 0.1179035036), (1.717018357, 0.1101875616), (1.7449927672, 0.1010277989), (1.7729731424, 0.0904961682), (1.8009204021, 0.0786559458), (1.8288520674, 0.0656421305), (1.847198586, 0.0560748246), (1.8564395878, 0.0512558454)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0275656044, 0.0556109403, 0.0841187273, 0.1130869955, 0.1425149344, 0.1724020638, 0.2027480417, 0.2335525987, 0.2648155097, 0.2648155097, 0.2648155097, 0.2648155097], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_54761_cec613c4_0018():
    """Model: Component14"""
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
            # Profile area: 19.0444630415, perimeter: 15.4699638245
            with BuildLine():
                CenterArc((0, 0), 2.4621212121, 3.4192817783, 353.1614364435)
                CenterArc((0, 0), 2.4621212121, -3.4192817783, 6.8385635565)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0800995674, perimeter: 1.1282182005
            with BuildLine():
                Line((2.4577381759, 0.1468465926), (2.4871578428, 0.1486043786))
                CenterArc((0, 0), 2.4621212121, -3.4192817783, 6.8385635565)
                Line((2.4577381759, -0.1468465926), (2.4871578428, -0.1486043786))
                _nurbs_edge([(2.4871578428, -0.1486043786), (2.4987686025, -0.1482513248), (2.5221561447, -0.1475401687), (2.5570929554, -0.1419905845), (2.5921440379, -0.1347420463), (2.6272477206, -0.1255387315), (2.662378676, -0.1147247068), (2.6975127699, -0.1023883881), (2.7326147958, -0.0886067887), (2.7677074988, -0.0735368501), (2.790823792, -0.0625008184), (2.8024536908, -0.0569485471)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0348150304, 0.0701278831, 0.1059211116, 0.1421929132, 0.1789426234, 0.2161698881, 0.2538744771, 0.2920562209, 0.3307149849, 0.3307149849, 0.3307149849, 0.3307149849], 3)
                CenterArc((-0.0094918183, 0), 2.8125221214, -1.1602164388, 2.3204328775)
                _nurbs_edge([(2.4871578428, 0.1486043786), (2.4987686025, 0.1482513248), (2.5221561447, 0.1475401687), (2.5570929554, 0.1419905845), (2.5921440379, 0.1347420463), (2.6272477206, 0.1255387315), (2.662378676, 0.1147247068), (2.6975127699, 0.1023883881), (2.7326147958, 0.0886067887), (2.7677074988, 0.0735368501), (2.790823792, 0.0625008184), (2.8024536908, 0.0569485471)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0348150304, 0.0701278831, 0.1059211116, 0.1421929132, 0.1789426234, 0.2161698881, 0.2538744771, 0.2920562209, 0.3307149849, 0.3307149849, 0.3307149849, 0.3307149849], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_54761_cec613c4_0019():
    """Model: Component17"""
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
            # Profile area: 8.3344880861, perimeter: 10.2339760685
            with BuildLine():
                CenterArc((0, 0), 1.6287878788, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.6287878788, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0770960546, perimeter: 1.0908783198
            with BuildLine():
                Line((1.6235660252, 0.1303200516), (1.7030191781, 0.1366975804))
                CenterArc((0, 0), 1.6287878788, -4.5891664191, 9.1783328383)
                Line((1.6235660252, -0.1303200516), (1.7030191781, -0.1366975804))
                _nurbs_edge([(1.7030191781, -0.1366975804), (1.7127741347, -0.1365089948), (1.7324538159, -0.1361285418), (1.7618830684, -0.1313872026), (1.7914463499, -0.1250491704), (1.8210800757, -0.1168655956), (1.8507499046, -0.1071506958), (1.8804260601, -0.0959807845), (1.9100670932, -0.0834229728), (1.9396915867, -0.0696204414), (1.9591500155, -0.0594732988), (1.9689510779, -0.0543622603)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0292362471, 0.0589813003, 0.089216832, 0.1199407528, 0.1511522032, 0.1828506738, 0.2150358019, 0.2477073017, 0.2808649345, 0.2808649345, 0.2808649345, 0.2808649345], 3)
                CenterArc((-0.0116975458, 0), 1.9813945155, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.7030191781, 0.1366975804), (1.7127741347, 0.1365089948), (1.7324538159, 0.1361285418), (1.7618830684, 0.1313872026), (1.7914463499, 0.1250491704), (1.8210800757, 0.1168655956), (1.8507499046, 0.1071506958), (1.8804260601, 0.0959807845), (1.9100670932, 0.0834229728), (1.9396915867, 0.0696204414), (1.9591500155, 0.0594732988), (1.9689510779, 0.0543622603)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0292362471, 0.0589813003, 0.089216832, 0.1199407528, 0.1511522032, 0.1828506738, 0.2150358019, 0.2477073017, 0.2808649345, 0.2808649345, 0.2808649345, 0.2808649345], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_54761_cec613c4_0021():
    """Model: Component20"""
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
            # Profile area: 466.6369556748, perimeter: 76.5763209313
            with BuildLine():
                CenterArc((0, 0), 12.1875, 1.0026382562, 357.9947234875)
                CenterArc((0, 0), 12.1875, -1.0026382562, 2.0052765125)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2174877427, perimeter: 1.8536678747
            with BuildLine():
                Line((12.1856339777, 0.2132623065), (12.3082115423, 0.2154075518))
                CenterArc((0, 0), 12.1875, -1.0026382562, 2.0052765125)
                Line((12.1856339777, -0.2132623065), (12.3082115423, -0.2154075518))
                _nurbs_edge([(12.3082115423, -0.2154075518), (12.3245297844, -0.2149069867), (12.3572335904, -0.2139037914), (12.4061857169, -0.2090647853), (12.4551740232, -0.2030097417), (12.5041760561, -0.1955757623), (12.5531902337, -0.1870337959), (12.6022127976, -0.1774654), (12.6512359346, -0.1669400005), (12.7002737529, -0.1555834822), (12.7328674182, -0.1473389852), (12.7491956006, -0.1432088068)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0489643022, 0.098130609, 0.1474920007, 0.1970478241, 0.2467978669, 0.296742033, 0.3468802701, 0.3972125466, 0.4477388418, 0.4477388418, 0.4477388418, 0.4477388418], 3)
                CenterArc((0.0017257647, 0), 12.7482742353, -0.6436504779, 1.2873009557)
                _nurbs_edge([(12.3082115423, 0.2154075518), (12.3245297844, 0.2149069867), (12.3572335904, 0.2139037914), (12.4061857169, 0.2090647853), (12.4551740232, 0.2030097417), (12.5041760561, 0.1955757623), (12.5531902337, 0.1870337959), (12.6022127976, 0.1774654), (12.6512359346, 0.1669400005), (12.7002737529, 0.1555834822), (12.7328674182, 0.1473389852), (12.7491956006, 0.1432088068)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0489643022, 0.098130609, 0.1474920007, 0.1970478241, 0.2467978669, 0.296742033, 0.3468802701, 0.3972125466, 0.4477388418, 0.4477388418, 0.4477388418, 0.4477388418], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_54761_cec613c4_0022():
    """Model: Component19"""
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
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.5, 8.2665492276, 343.4669015447)
                CenterArc((0, 0), 0.5, -8.2665492276, 16.5330984553)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0341209949, perimeter: 0.7174668192
            with BuildLine():
                Line((0.4948049497, 0.0718892327), (0.5871927922, 0.0853120797))
                CenterArc((0, 0), 0.5, -8.2665492276, 16.5330984553)
                Line((0.4948049497, -0.0718892327), (0.5871927922, -0.0853120797))
                _nurbs_edge([(0.5871927922, -0.0853120797), (0.5925736498, -0.0854237395), (0.6034806919, -0.0856500749), (0.6198909047, -0.0831026466), (0.6364542418, -0.079417046), (0.6531135745, -0.0743971342), (0.6698189694, -0.0682474109), (0.6865317714, -0.0610080793), (0.7032021155, -0.0527160702), (0.7198339765, -0.0434656576), (0.7306515141, -0.0365884083), (0.7361175723, -0.0331133619)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0161171162, 0.0326695254, 0.0496385498, 0.0670208683, 0.0848146155, 0.103018432, 0.1216312201, 0.1406520535, 0.1600801362, 0.1600801362, 0.1600801362, 0.1600801362], 3)
                CenterArc((-0.0202108591, 0), 0.7570529643, -2.5069069843, 5.0138139687)
                _nurbs_edge([(0.5871927922, 0.0853120797), (0.5925736498, 0.0854237395), (0.6034806919, 0.0856500749), (0.6198909047, 0.0831026466), (0.6364542418, 0.079417046), (0.6531135745, 0.0743971342), (0.6698189694, 0.0682474109), (0.6865317714, 0.0610080793), (0.7032021155, 0.0527160702), (0.7198339765, 0.0434656576), (0.7306515141, 0.0365884083), (0.7361175723, 0.0331133619)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0161171162, 0.0326695254, 0.0496385498, 0.0670208683, 0.0848146155, 0.103018432, 0.1216312201, 0.1406520535, 0.1600801362, 0.1600801362, 0.1600801362, 0.1600801362], 3)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_54979_6bd8ad31_0014():
    """Model: registration"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000000044, 0.0000000198, -1.9685677366), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 170.0335370299, perimeter: 86.7730084572
            with BuildLine():
                Line((-88.3321265605, -3.0770754218), (-88.3321265605, 1.2794050707))
                Line((-88.3321265605, 1.2794050707), (-127.3621502966, 1.2794050707))
                Line((-127.3621502966, 1.2794050707), (-127.3621502966, -3.0770754218))
                Line((-127.3621502966, -3.0770754218), (-88.3321265605, -3.0770754218))
            make_face()
            # Profile area: 2168.6656256547, perimeter: 193.636684371
            with BuildLine():
                Line((-127.3621502966, -3.0770754218), (-88.3321265605, -3.0770754218))
                Line((-127.3621502966, 1.2794050707), (-127.3621502966, -3.0770754218))
                Line((-127.3621502966, 1.2794050707), (-134.5621502966, 1.2794050707))
                Line((-134.5621502966, 1.2794050707), (-134.5621502966, -49.3089133787))
                Line((-134.5621502966, -49.3089133787), (-88.3321265605, -49.3089133787))
                Line((-88.3321265605, -49.3089133787), (-88.3321265605, -3.0770754218))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_54987_c8dbbe1e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1218.5804457044, perimeter: 123.7462464244
            Circle(19.6948268075)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_55017_d18176a6_0000():
    """Model: Component1"""
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
        # OneSide extrude, distance=2
        extrude(amount=2)

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
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_55084_fc00f917_0002():
    """Model: base disc"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 121.9330648675, perimeter: 42.4115008235
            with BuildLine():
                CenterArc((0, 0), 6.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((5, 0)):
                Circle(0.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_55135_f1186d58_0006():
    """Model: 4. Korkociag"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.160730099, perimeter: 2.7707963566
            with BuildLine():
                CenterArc((6.7000000983, 0.4000000075), 0.1, 90, 90)
                Line((6.6000000983, 0.2000000015), (6.6000000983, 0.4000000075))
                CenterArc((6.7000000983, 0.2000000015), 0.1, 180, 90)
                Line((7.1000001073, 0.1000000015), (6.7000000983, 0.1000000015))
                CenterArc((7.1000001073, 0.2000000015), 0.1, -90, 90)
                Line((7.2000001073, 0.4000000075), (7.2000001073, 0.2000000015))
                CenterArc((7.1000001073, 0.4000000075), 0.1, 0, 90)
                Line((6.7000000983, 0.5000000075), (7.1000001073, 0.5000000075))
            make_face()
            with BuildLine():
                CenterArc((6.9000001028, 0.3000000045), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_55271_cf70456e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10, perimeter: 13
            with BuildLine():
                Line((2.5, -4), (0, -4))
                Line((2.5, 0), (2.5, -4))
                Line((0, 0), (2.5, 0))
                Line((0, -4), (0, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_55278_d699fcaa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_55289_292737cb_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.8082331783, perimeter: 9.9056121447
            Circle(1.5765271372)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_55296_3173b45d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25, perimeter: 25
            with BuildLine():
                Line((0, 5), (-2.5, 5))
                Line((-2.5, 5), (-2.5, -5))
                Line((-2.5, -5), (0, -5))
                Line((0, -5), (0, 5))
            make_face()
            # Profile area: 7.5, perimeter: 17
            with BuildLine():
                Line((-2.5, -5), (0, -5))
                Line((-5, -5), (-2.5, -5))
                Line((-5, -6), (-5, -5))
                Line((2.5, -6), (-5, -6))
                Line((2.5, -5), (2.5, -6))
                Line((2.5, -5), (0, -5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_55302_13bb4506_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 58.0984658225, perimeter: 53.0871208605
            with BuildLine():
                Line((2.2870336968, 3.4106261925), (-5.365642962, 3.4106261925))
                CenterArc((-5.365642962, 1.4106261925), 2, 90, 35.1958180174)
                Line((-6.5183883055, 3.0450001317), (-7.1527453435, 2.5975798051))
                CenterArc((-6, 0.9632058659), 2, 125.1958180174, 54.8041819826)
                Line((-8, 0.9632058659), (-8, 0))
                Line((-4.6999744105, 0.0078474368), (-8, 0))
                CenterArc((-3.4431227921, 0.2696502169), 1.2838289163, -11.8200285748, 203.586512769)
                Line((3.5260920693, 0.0177792254), (-2.1865163839, 0.0066729911))
                CenterArc((4.9248600978, -0.0000548019), 1.3988817141, -0.0000791471, 179.2696083986)
                Line((10, -0.0000567342), (6.3237418118, -0.0000567342))
                Line((10, -0.0000567342), (10, 1.2192235936))
                CenterArc((9, 1.2192235936), 1, 0, 75.9637565321)
                Line((9.242535625, 2.1893660937), (6.1343569581, 2.9664107605))
                CenterArc((6.2556247706, 3.4514820105), 0.5, -135, 30.9637565321)
                Line((5.9020713801, 3.0979286199), (1.3535533906, 7.6464466094))
                CenterArc((1, 7.2928932188), 0.5, 45, 90)
                Line((0.6464466094, 7.6464466094), (0.3473534411, 7.3473534411))
                CenterArc((0.7009068317, 6.9938000505), 0.5, 135, 88.9863940348)
                Line((0.3411544618, 6.6465562855), (2.6467860667, 4.2578699576))
                CenterArc((2.2870336968, 3.9106261925), 0.5, -90, 133.9863940348)
            make_face()
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((-3.4431227921, 0.2696502169)):
                Circle(0.9)
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((4.9248600978, -0.0000548019)):
                Circle(0.9)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


def model_55342_4090e441_0000():
    """Model: Component1"""
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
            # Profile area: 3.9760782022, perimeter: 7.0685834706
            with BuildLine():
                CenterArc((0, 0), 1.125, 4.4405614833, 351.1188770334)
                CenterArc((0, 0), 1.125, -4.4405614833, 8.8811229666)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0337348394, perimeter: 0.7224282121
            with BuildLine():
                Line((1.1216229644, 0.0871029606), (1.1710685068, 0.0909428009))
                CenterArc((0, 0), 1.125, -4.4405614833, 8.8811229666)
                Line((1.1216229644, -0.0871029606), (1.1710685068, -0.0909428009))
                _nurbs_edge([(1.1710685068, -0.0909428009), (1.177617915, -0.0908066099), (1.1908281397, -0.0905319111), (1.2105797069, -0.0873527235), (1.2304178765, -0.0831154981), (1.2503009761, -0.077656044), (1.2702071518, -0.0711833343), (1.2901172816, -0.0637484987), (1.3100046149, -0.055396443), (1.3298817282, -0.0462223922), (1.3429425714, -0.0394811792), (1.3495202692, -0.0360861717)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0196300986, 0.0395941134, 0.0598800669, 0.080486613, 0.1014132059, 0.1226595266, 0.1442253498, 0.1661104996, 0.1883148293, 0.1883148293, 0.1883148293, 0.1883148293], 3)
                CenterArc((-0.0074716577, 0), 1.3574716577, -1.5232943703, 3.0465887407)
                _nurbs_edge([(1.1710685068, 0.0909428009), (1.177617915, 0.0908066099), (1.1908281397, 0.0905319111), (1.2105797069, 0.0873527235), (1.2304178765, 0.0831154981), (1.2503009761, 0.077656044), (1.2702071518, 0.0711833343), (1.2901172816, 0.0637484987), (1.3100046149, 0.055396443), (1.3298817282, 0.0462223922), (1.3429425714, 0.0394811792), (1.3495202692, 0.0360861717)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0196300986, 0.0395941134, 0.0598800669, 0.080486613, 0.1014132059, 0.1226595266, 0.1442253498, 0.1661104996, 0.1883148293, 0.1883148293, 0.1883148293, 0.1883148293], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_55346_5e81d5e1_0000():
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
            # Profile area: 3.6305030103, perimeter: 6.7544242052
            with BuildLine():
                CenterArc((0, 0), 1.075, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.075, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0335830414, perimeter: 0.7199796911
            with BuildLine():
                Line((1.0715535766, 0.0860112341), (1.1239926576, 0.090220403))
                CenterArc((0, 0), 1.075, -4.5891664191, 9.1783328383)
                Line((1.0715535766, -0.0860112341), (1.1239926576, -0.090220403))
                _nurbs_edge([(1.1239926576, -0.090220403), (1.1304309289, -0.0900959366), (1.1434195185, -0.0898448376), (1.1628428252, -0.0867155537), (1.1823545909, -0.0825324525), (1.2019128499, -0.0771312931), (1.221494937, -0.0707194592), (1.2410811997, -0.0633473177), (1.2606442815, -0.055059162), (1.2801964472, -0.0459494914), (1.2930390102, -0.0392523772), (1.2995077114, -0.0358790918)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192959231, 0.0389276582, 0.0588831091, 0.0791608969, 0.0997604541, 0.1206814447, 0.1419236292, 0.1634868191, 0.1853708568, 0.1853708568, 0.1853708568, 0.1853708568], 3)
                CenterArc((-0.0077203802, 0), 1.3077203802, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.1239926576, 0.090220403), (1.1304309289, 0.0900959366), (1.1434195185, 0.0898448376), (1.1628428252, 0.0867155537), (1.1823545909, 0.0825324525), (1.2019128499, 0.0771312931), (1.221494937, 0.0707194592), (1.2410811997, 0.0633473177), (1.2606442815, 0.055059162), (1.2801964472, 0.0459494914), (1.2930390102, 0.0392523772), (1.2995077114, 0.0358790918)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192959231, 0.0389276582, 0.0588831091, 0.0791608969, 0.0997604541, 0.1206814447, 0.1419236292, 0.1634868191, 0.1853708568, 0.1853708568, 0.1853708568, 0.1853708568], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_55395_c160dca4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.5131093442, perimeter: 25.734066742
            with BuildLine():
                Line((-1.012099026, -1.5124852176), (0.5948520912, -1.5124852176))
                Line((0.5948520912, -1.5124852176), (0.6074724578, -1.8092032709))
                Line((0.6074724578, -1.8092032709), (0.9661596035, -2.1059213242))
                Line((1.182202761, -2.1059213242), (0.9661596035, -2.1059213242))
                CenterArc((1.682202761, -2.1059213242), 0.5, 180, 270)
                Line((1.682202761, -0.339821225), (1.682202761, -1.6059213242))
                Line((1.2418970746, -0.339821225), (1.682202761, -0.339821225))
                Line((1.2418970746, 0.5705363483), (1.2418970746, -0.339821225))
                Line((1.2418970746, 0.5705363483), (1.682202761, 0.5705363483))
                Line((1.682202761, 1.3940786758), (1.682202761, 0.5705363483))
                CenterArc((1.682202761, 1.8940786758), 0.5, -90, 270)
                Line((0.8411013805, 1.8940786758), (1.182202761, 1.8940786758))
                Line((0.8411013805, 1.8940786758), (0.5, 1.3058327963))
                Line((0.5, 0.7175869167), (0.5, 1.3058327963))
                Line((-1.012099026, 0.7175869167), (0.5, 0.7175869167))
                Line((-1.012099026, 1.3058327963), (-1.012099026, 0.7175869167))
                Line((-1.4149481325, 1.8940786758), (-1.012099026, 1.3058327963))
                Line((-1.817797239, 1.8940786758), (-1.4149481325, 1.8940786758))
                CenterArc((-2.317797239, 1.8940786758), 0.5, 0, 270)
                Line((-2.317797239, 0.5705363483), (-2.317797239, 1.3940786758))
                Line((-2.317797239, 0.5705363483), (-1.9088986195, 0.5705363483))
                Line((-1.9088986195, 0.5705363483), (-1.9088986195, -0.339821225))
                Line((-2.317797239, -0.339821225), (-1.9088986195, -0.339821225))
                Line((-2.317797239, -1.6059213242), (-2.317797239, -0.339821225))
                CenterArc((-2.317797239, -2.1059213242), 0.5, 90, 270)
                Line((-1.4149481325, -2.1059213242), (-1.817797239, -2.1059213242))
                Line((-1.012099026, -1.8092032709), (-1.4149481325, -2.1059213242))
                Line((-1.012099026, -1.5124852176), (-1.012099026, -1.8092032709))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_55625_453e11ac_0005():
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
            # Profile area: 0.0239078941, perimeter: 0.5481199304
            with BuildLine():
                CenterArc((0, 0), 0.0872359963, 8.2665492276, 343.4669015447)
                CenterArc((0, 0), 0.0872359963, -8.2665492276, 16.5330984553)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0010386593, perimeter: 0.1251778656
            with BuildLine():
                Line((0.0863296055, 0.0125426577), (0.1024486965, 0.0148845685))
                CenterArc((0, 0), 0.0872359963, -8.2665492276, 16.5330984553)
                Line((0.0863296055, -0.0125426577), (0.1024486965, -0.0148845685))
                _nurbs_edge([(0.1024486965, -0.0148845685), (0.1033875055, -0.0149040501), (0.1052904788, -0.0149435392), (0.1081536014, -0.0144990844), (0.1110434398, -0.0138560503), (0.1139500268, -0.0129802162), (0.1168646503, -0.0119072618), (0.1197805662, -0.0106442012), (0.1226890743, -0.0091974778), (0.1255908683, -0.0075835399), (0.1274782256, -0.0063836525), (0.1284318997, -0.0057773542)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0028119854, 0.0056999172, 0.0086605367, 0.0116932644, 0.014797775, 0.0179738311, 0.0212212413, 0.024539844, 0.0279295003, 0.0279295003, 0.0279295003, 0.0279295003], 3)
                CenterArc((-0.0035262289, 0), 0.1320845392, -2.5069069843, 5.0138139687)
                _nurbs_edge([(0.1024486965, 0.0148845685), (0.1033875055, 0.0149040501), (0.1052904788, 0.0149435392), (0.1081536014, 0.0144990844), (0.1110434398, 0.0138560503), (0.1139500268, 0.0129802162), (0.1168646503, 0.0119072618), (0.1197805662, 0.0106442012), (0.1226890743, 0.0091974778), (0.1255908683, 0.0075835399), (0.1274782256, 0.0063836525), (0.1284318997, 0.0057773542)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0028119854, 0.0056999172, 0.0086605367, 0.0116932644, 0.014797775, 0.0179738311, 0.0212212413, 0.024539844, 0.0279295003, 0.0279295003, 0.0279295003, 0.0279295003], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_55633_282eaae6_0002():
    """Model: penutup1 v1"""
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
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.06
        extrude(amount=0.06)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.ADD)
    return part.part


def model_55636_6180bfce_0000():
    """Model: tela sombrilla"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2386.1435935395, perimeter: 2386.1435935394
            with BuildLine():
                Line((100, -173.2050807569), (200, 0))
                Line((200, 0), (100, 173.2050807569))
                Line((100, 173.2050807569), (-100, 173.2050807569))
                Line((-100, 173.2050807569), (-200, 0))
                Line((-200, 0), (-100, -173.2050807569))
                Line((-100, -173.2050807569), (100, -173.2050807569))
            make_face()
            with BuildLine():
                Line((-98.8452994616, -171.2050807569), (98.8452994616, -171.2050807569))
                Line((-197.6905989232, 0), (-98.8452994616, -171.2050807569))
                Line((-98.8452994616, 171.2050807569), (-197.6905989232, 0))
                Line((98.8452994616, 171.2050807569), (-98.8452994616, 171.2050807569))
                Line((197.6905989232, 0), (98.8452994616, 171.2050807569))
                Line((98.8452994616, -171.2050807569), (197.6905989232, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_55715_525d1d3e_0000():
    """Model: Shaft Cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -12.7571703401, 20.701), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7765376444, perimeter: 8.5977872041
            with BuildLine():
                CenterArc((0, 12.7571703401), 0.762, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.5499261314, 13.0746703401), (0, 13.3921703401))
                Line((0, 13.3921703401), (0.5499261314, 13.0746703401))
                Line((0.5499261314, 13.0746703401), (0.5499261314, 12.4396703401))
                Line((0.5499261314, 12.4396703401), (0, 12.1221703401))
                Line((0, 12.1221703401), (-0.5499261314, 12.4396703401))
                Line((-0.5499261314, 12.4396703401), (-0.5499261314, 13.0746703401))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-6.985
        extrude(amount=-6.985)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -12.7571703401, 20.701), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7765376444, perimeter: 8.5977872041
            with BuildLine():
                CenterArc((0, 12.7571703401), 0.762, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.5499261314, 13.0746703401), (0, 13.3921703401))
                Line((0, 13.3921703401), (0.5499261314, 13.0746703401))
                Line((0.5499261314, 13.0746703401), (0.5499261314, 12.4396703401))
                Line((0.5499261314, 12.4396703401), (0, 12.1221703401))
                Line((0, 12.1221703401), (-0.5499261314, 12.4396703401))
                Line((-0.5499261314, 12.4396703401), (-0.5499261314, 13.0746703401))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0476092803, perimeter: 3.81
            with BuildLine():
                Line((-0.5499261314, 12.4396703401), (-0.5499261314, 13.0746703401))
                Line((0, 12.1221703401), (-0.5499261314, 12.4396703401))
                Line((0.5499261314, 12.4396703401), (0, 12.1221703401))
                Line((0.5499261314, 13.0746703401), (0.5499261314, 12.4396703401))
                Line((0, 13.3921703401), (0.5499261314, 13.0746703401))
                Line((-0.5499261314, 13.0746703401), (0, 13.3921703401))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


def model_55758_efbfee69_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 40, perimeter: 26
            with BuildLine():
                Line((0.5, 8.5), (0.5, 0.5))
                Line((0.5, 0.5), (5.5, 0.5))
                Line((5.5, 0.5), (5.5, 8.5))
                Line((5.5, 8.5), (0.5, 8.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_55791_2eb44ee9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 82.6631566976, perimeter: 32.2300459698
            with Locations((-0.25, 0)):
                Circle(5.1295711322)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


def model_55796_cb1b98f1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.7321048417, perimeter: 54.9069334127
            with BuildLine():
                Line((-8, 0.6), (-8.2, 0.6))
                CenterArc((-8.2, 1.6), 1, -126.8698976458, 36.8698976458)
                CenterArc((-9.4, 0), 1, 53.1301023542, 253.3138732416)
                CenterArc((-8.211927034, -1.6088762002), 1, 88.7262060265, 37.7177695693)
                Line((-8.1896969665, -0.6091233187), (-2.423691068, -0.7373337021))
                CenterArc((-2.4459211355, -1.7370865836), 1, 35.3822668624, 53.3439391641)
                CenterArc((0, 0), 2, -144.6177331376, 289.264881685)
                CenterArc((-2.446812626, 1.7358306292), 1, -88.6018987229, 53.2490472703)
                Line((-8, 0.6), (-2.4224135769, 0.7361283304))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.4, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-7.737124347, 0.2105753691), (-2.4431231913, 0.2106652527))
                CenterArc((-2.4431197956, 0.0106652528), 0.2, -90.0000646758, 180.001037466)
                Line((-2.4431200214, -0.1893347472), (-7.7431197956, -0.1893347472))
                CenterArc((-7.7431197956, 0.0106652528), 0.2, 91.7197724395, 178.2802275605)
                CenterArc((-7.7431197956, 0.0106652528), 0.2, 88.2821731421, 3.4375992974)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_55866_b041060d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((-8, 3), (-3, 3))
                Line((-8, 0), (-8, 3))
                Line((-3, 0), (-8, 0))
                Line((-3, 3), (-3, 0))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


def model_55915_4badf6b0_0005():
    """Model: pasek"""
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
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.9178491972, perimeter: 58.5265546437
            with BuildLine():
                _nurbs_edge([(-4.4954556027, 0.7876827644), (-4.573716054, 0.7296506467), (-4.7332729206, 0.5997959699), (-4.9817247833, 0.3635989241), (-5.3279845744, -0.0321134451), (-5.7669248316, -0.6469328453), (-6.1854448485, -1.3478920445), (-6.5564967615, -2.0913678914), (-6.8502428252, -2.7872781155), (-7.0593031925, -3.3972976064), (-7.1978621525, -3.9589224508), (-7.2849070894, -4.5321332676), (-7.3354809261, -5.1800174203), (-7.3449073985, -5.9285194906), (-7.2921773381, -6.7646803332), (-7.1527804357, -7.6530276864), (-6.9113436152, -8.5469594587), (-6.5687734214, -9.4004732289), (-6.1654695647, -10.1828982481), (-5.7646761837, -10.8845014671), (-5.3933821893, -11.4979758108), (-5.1333139362, -11.9168203671), (-4.9607167955, -12.1904011977), (-4.8556679642, -12.3548577286), (-4.8056430766, -12.4326021976)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(7.8006332304, -16.4268416018), (7.7203562159, -16.4820505311), (7.5457725378, -16.5908676719), (7.2417639174, -16.7492852568), (6.7551409332, -16.9484891558), (6.0311960117, -17.164302026), (5.2323902773, -17.3328612206), (4.4087611531, -17.4427289718), (3.6551987042, -17.4948962567), (3.0103498775, -17.4948119043), (2.4341450916, -17.4437325926), (1.863687853, -17.340166187), (1.2344221399, -17.1778817127), (0.5233224067, -16.9440412179), (-0.2505389113, -16.6229741307), (-1.0456576825, -16.2029995409), (-1.8129649848, -15.6846895413), (-2.5092390288, -15.0838213784), (-3.1185695529, -14.4485582645), (-3.6522612312, -13.8418824006), (-4.1121551257, -13.2916936998), (-4.4240129752, -12.9098417125), (-4.6268282018, -12.657845229), (-4.7483252992, -12.5051374595), (-4.8056430766, -12.4326021976)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(7.7439674676, -16.3444462662), (7.75002206, -16.3413592668), (7.7616978869, -16.3356022146), (7.7779115742, -16.3282174557), (7.7968867596, -16.3209140807), (7.8159048048, -16.3163077718), (7.8298141443, -16.3166166995), (7.8382170341, -16.322223545), (7.8409318567, -16.3333030479), (7.8382242042, -16.3495996743), (7.8305203265, -16.3707033164), (7.8206966887, -16.3911081394), (7.8114020524, -16.4082656918), (7.8043632416, -16.4205145451), (7.8006332304, -16.4268416018)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(7.7439674676, -16.3444462662), (7.473007358, -16.5307937235), (7.0906768125, -16.7123207528), (6.6224870373, -16.870086543), (6.1901957444, -17.0157556306), (5.6851573565, -17.1397308374), (5.1669193228, -17.2270125324), (4.7324052461, -17.3001934312), (4.2936821023, -17.3477612337), (3.9008248119, -17.3710343638), (3.5259819731, -17.3932403057), (3.1938211373, -17.3939913397), (2.8868218218, -17.3745518802), (2.5261191353, -17.3517118771), (2.1944533005, -17.3014142672), (1.8286742537, -17.2183098768), (1.4918846043, -17.1417918291), (1.1238363168, -17.0371302832), (0.720925321, -16.8937941638), (0.1969466276, -16.7073880508), (-0.3828334379, -16.4524665447), (-0.9447841807, -16.1182490708), (-1.3928894441, -15.8517406427), (-1.8257785009, -15.5341334517), (-2.2160536635, -15.1880731101), (-2.6854337656, -14.7718697387), (-3.0959951391, -14.3211230088), (-3.4533681453, -13.9113940376), (-3.8522363474, -13.4540907291), (-4.1847795974, -13.0459122902), (-4.4546040848, -12.7116299658), (-4.5528328042, -12.5899355822), (-4.642686906, -12.477500098), (-4.724173681, -12.3744097721)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1053751762, 0.1053751762, 0.1053751762, 0.2026707037, 0.2026707037, 0.2026707037, 0.28424765, 0.28424765, 0.28424765, 0.3620838896, 0.3620838896, 0.3620838896, 0.4535360176, 0.4535360176, 0.4535360176, 0.5377402125, 0.5377402125, 0.5377402125, 0.6472462932, 0.6472462932, 0.6472462932, 0.7345675607, 0.7345675607, 0.7345675607, 0.8395879908, 0.8395879908, 0.8395879908, 0.9568025242, 0.9568025242, 0.9568025242, 0.9994740905, 0.9994740905, 0.9994740905, 0.9994740905], 3)
                _nurbs_edge([(-4.4358921542, 0.7073572043), (-4.7000457304, 0.5114806003), (-4.9957595837, 0.2086902019), (-5.2968428259, -0.1830247346), (-5.5748404902, -0.5447049021), (-5.8559105684, -0.9822357425), (-6.1065515341, -1.4441533328), (-6.316700193, -1.8314458165), (-6.50398535, -2.2310268004), (-6.6534136484, -2.5951005194), (-6.7959899195, -2.942479656), (-6.9044281958, -3.2564422735), (-6.9856068634, -3.553151721), (-7.0809861102, -3.9017645335), (-7.1409745878, -4.2318152237), (-7.1809933687, -4.6047752054), (-7.2178405072, -4.948176673), (-7.2382033543, -5.3302747436), (-7.2332889697, -5.7578941567), (-7.2268978986, -6.3140057142), (-7.1737927113, -6.9451235619), (-7.0398953418, -7.5850934453), (-6.9331242115, -8.0954119684), (-6.7730814276, -8.6079093544), (-6.5723027788, -9.0893243487), (-6.3308282714, -9.6683174306), (-6.0376012697, -10.2028744261), (-5.7659245692, -10.6738150442), (-5.4627030185, -11.1994373895), (-5.184440144, -11.646387525), (-4.9557377789, -12.010042794), (-4.8724794332, -12.1424303017), (-4.7952634135, -12.2638929874), (-4.724173681, -12.3744097721)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1053751762, 0.1053751762, 0.1053751762, 0.2026707037, 0.2026707037, 0.2026707037, 0.28424765, 0.28424765, 0.28424765, 0.3620838896, 0.3620838896, 0.3620838896, 0.4535360176, 0.4535360176, 0.4535360176, 0.5377402125, 0.5377402125, 0.5377402125, 0.6472462932, 0.6472462932, 0.6472462932, 0.7345675607, 0.7345675607, 0.7345675607, 0.8395879908, 0.8395879908, 0.8395879908, 0.9568025242, 0.9568025242, 0.9568025242, 0.9994740905, 0.9994740905, 0.9994740905, 0.9994740905], 3)
                _nurbs_edge([(-4.4358921542, 0.7073572043), (-4.4310083681, 0.7120833325), (-4.4217757532, 0.7212608815), (-4.4095316773, 0.7342030964), (-4.3964689651, 0.7497839339), (-4.3859436312, 0.7662800387), (-4.381724723, 0.7795377147), (-4.3843032342, 0.7893048307), (-4.3939033621, 0.7954662584), (-4.4101972473, 0.7981903578), (-4.4326587069, 0.7977473304), (-4.4551466112, 0.7950724805), (-4.474391205, 0.7918448685), (-4.4882608157, 0.789159135), (-4.4954556027, 0.7876827644)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


def model_55927_f8b31711_0017():
    """Model: Crank swing arm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8465525046, perimeter: 7.6114771856
            with BuildLine():
                CenterArc((0, 0), 1.2, -114.8331202957, 49.6662405914)
                CenterArc((1.5, -1), 1, 107.511378211, 77.597108526)
                CenterArc((0, 0), 1.2, -2.2132553477, 184.4265106953)
                CenterArc((-1.5, -1), 1, -5.108486737, 77.597108526)
            make_face()
        # Symmetric extrude, each_side=0.225
        extrude(amount=0.225, both=True)
    return part.part


def model_56065_00bbe5da_0022():
    """Model: Air_Channel_Packing_2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_56157_d9157017_0003():
    """Model: 2_bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((5, -27.5), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, -27.5), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.4
        extrude(amount=8.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((5, -27.5), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, -27.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((5, -27.5), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, -27.5), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_56167_90101372_0013():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((-12, 15), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-12, 15), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=24
        extrude(amount=24)
    return part.part


def model_56321_07658e97_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 74.0343535884, perimeter: 51.7346200654
            with BuildLine():
                Line((-18.5747449631, -15.6586414649), (-13.3270598338, -18.5767117378))
                Line((-13.3270598338, -18.5767117378), (-8.1760942828, -15.4911182413))
                Line((-8.1760942828, -15.4911182413), (-8.2728138611, -9.4874544718))
                Line((-8.2728138611, -9.4874544718), (-13.5204989904, -6.5693841989))
                Line((-13.5204989904, -6.5693841989), (-18.6714645413, -9.6549776955))
                Line((-18.6714645413, -9.6549776955), (-18.5747449631, -15.6586414649))
            make_face()
            with BuildLine():
                CenterArc((-13.4237794121, -12.5730479684), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-13.4237794121, -12.5730479684)):
                Circle(2.5)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-13.4237794121, -12.5730479684)):
                Circle(2.5)
        # OneSide extrude, distance=-44.5
        extrude(amount=-44.5, mode=Mode.ADD)
    return part.part


def model_56322_d0bb31b7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.7594458332, perimeter: 22.6936330127
            with BuildLine():
                CenterArc((-2.6107084324, 3.1031413952), 1.6, 90, 53.1301023542)
                Line((-5.2707084324, 2.2231413952), (-3.8907084324, 4.0631413952))
                CenterArc((-5.5107084324, 2.4031413952), 0.3, -90, 53.1301023542)
                Line((-5.8107084324, 2.1031413952), (-5.5107084324, 2.1031413952))
                Line((-5.8107084324, 1.1031413952), (-5.8107084324, 2.1031413952))
                Line((-3.4107084324, 1.1031413952), (-5.8107084324, 1.1031413952))
                Line((-3.4107084324, 1.1031413952), (-3.4107084324, 0.2031413952))
                Line((-3.4107084324, 0.2031413952), (-1.8107084324, 0.2031413952))
                Line((-1.8107084324, 0.2031413952), (-1.8107084324, 1.1031413952))
                Line((-1.8107084324, 1.1031413952), (0.5892915676, 1.1031413952))
                Line((0.5892915676, 2.1031413952), (0.5892915676, 1.1031413952))
                Line((0.5892915676, 2.1031413952), (0.2892915676, 2.1031413952))
                CenterArc((0.2892915676, 2.4031413952), 0.3, -143.1301023542, 53.1301023542)
                Line((0.0492915676, 2.2231413952), (-1.3307084324, 4.0631413952))
                CenterArc((-2.6107084324, 3.1031413952), 1.6, 36.8698976458, 53.1301023542)
            make_face()
            with BuildLine():
                CenterArc((-2.6107084324, 3.1031413952), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.7947904058, perimeter: 10.1618609142
            with BuildLine():
                Line((-2.6107084324, 4.7031413952), (0.5892915676, 4.7031413952))
                CenterArc((-2.6107084324, 3.1031413952), 1.6, 36.8698976458, 53.1301023542)
                Line((0.0492915676, 2.2231413952), (-1.3307084324, 4.0631413952))
                CenterArc((0.2892915676, 2.4031413952), 0.3, -143.1301023542, 53.1301023542)
                Line((0.5892915676, 2.1031413952), (0.2892915676, 2.1031413952))
                Line((0.5892915676, 4.7031413952), (0.5892915676, 2.1031413952))
            make_face()
            # Profile area: 15.7594458332, perimeter: 22.6936330127
            with BuildLine():
                CenterArc((-2.6107084324, 3.1031413952), 1.6, 90, 53.1301023542)
                Line((-5.2707084324, 2.2231413952), (-3.8907084324, 4.0631413952))
                CenterArc((-5.5107084324, 2.4031413952), 0.3, -90, 53.1301023542)
                Line((-5.8107084324, 2.1031413952), (-5.5107084324, 2.1031413952))
                Line((-5.8107084324, 1.1031413952), (-5.8107084324, 2.1031413952))
                Line((-3.4107084324, 1.1031413952), (-5.8107084324, 1.1031413952))
                Line((-3.4107084324, 1.1031413952), (-3.4107084324, 0.2031413952))
                Line((-3.4107084324, 0.2031413952), (-1.8107084324, 0.2031413952))
                Line((-1.8107084324, 0.2031413952), (-1.8107084324, 1.1031413952))
                Line((-1.8107084324, 1.1031413952), (0.5892915676, 1.1031413952))
                Line((0.5892915676, 2.1031413952), (0.5892915676, 1.1031413952))
                Line((0.5892915676, 2.1031413952), (0.2892915676, 2.1031413952))
                CenterArc((0.2892915676, 2.4031413952), 0.3, -143.1301023542, 53.1301023542)
                Line((0.0492915676, 2.2231413952), (-1.3307084324, 4.0631413952))
                CenterArc((-2.6107084324, 3.1031413952), 1.6, 36.8698976458, 53.1301023542)
            make_face()
            with BuildLine():
                CenterArc((-2.6107084324, 3.1031413952), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.7947904058, perimeter: 10.1618609142
            with BuildLine():
                Line((-5.8107084324, 4.7031413952), (-2.6107084324, 4.7031413952))
                Line((-5.8107084324, 2.1031413952), (-5.8107084324, 4.7031413952))
                Line((-5.8107084324, 2.1031413952), (-5.5107084324, 2.1031413952))
                CenterArc((-5.5107084324, 2.4031413952), 0.3, -90, 53.1301023542)
                Line((-5.2707084324, 2.2231413952), (-3.8907084324, 4.0631413952))
                CenterArc((-2.6107084324, 3.1031413952), 1.6, 90, 53.1301023542)
            make_face()
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-2.6107084324, 3.1031413952)):
                Circle(0.6)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


def model_56343_60e8809c_0008():
    """Model: Rivet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # Symmetric extrude, each_side=0.65
        extrude(amount=0.65, both=True)
    return part.part


def model_56345_80dc7bcc_0007():
    """Model: Motor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_56430_4f35ba2f_0002():
    """Model: HandleFrame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 136.2484503443, perimeter: 63.8888502163
            with BuildLine():
                Line((37.497536674, 100.0001493523), (62.5023906252, 100.0001493523))
                Line((35.9206818263, 94.8745025636), (37.497536674, 100.0001493523))
                Line((35.9206818263, 94.8745025636), (39.1872080651, 94.8745025636))
                Line((39.1872080651, 94.8745025636), (60.8127192341, 94.8745025636))
                Line((60.8127192341, 94.8745025636), (64.0792454729, 94.8745025636))
                Line((64.0792454729, 94.8745025636), (62.5023906252, 100.0001493523))
            make_face()
            # Profile area: 352.7052936995, perimeter: 239.1788227196
            with BuildLine():
                Line((60.8127192341, 94.8745025636), (64.0792454729, 94.8745025636))
                Line((89.9999272992, 0), (60.8127192341, 94.8745025636))
                Line((110, 0), (89.9999272992, 0))
                Line((110, 0), (110, 2.5))
                Line((110, 2.5), (92.4973531138, 2.5))
                Line((92.4973531138, 2.5), (64.0792454729, 94.8745025636))
            make_face()
            # Profile area: 352.7052936995, perimeter: 239.1788227196
            with BuildLine():
                Line((35.9206818263, 94.8745025636), (39.1872080651, 94.8745025636))
                Line((7.5025741854, 2.5), (35.9206818263, 94.8745025636))
                Line((-10.0000727008, 2.5), (7.5025741854, 2.5))
                Line((-10.0000727008, 0), (-10.0000727008, 2.5))
                Line((-10.0000727008, 0), (10, 0))
                Line((10, 0), (39.1872080651, 94.8745025636))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_56430_4f35ba2f_0019():
    """Model: AxleBearing (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 150.1825229575, perimeter: 90.853981634
            with BuildLine():
                Line((-15, 0), (-15, 4))
                Line((-15, 4), (-27.5, 4))
                Line((-27.5, 4), (-32.5, 4))
                CenterArc((-35, 4), 2.5, -180, 180)
                Line((-37.5, 4), (-42.5, 4))
                Line((-42.5, 4), (-55, 4))
                Line((-55, 4), (-55, 0))
                Line((-15, 0), (-55, 0))
            make_face()
            # Profile area: 78.5398163397, perimeter: 41.4159265359
            with BuildLine():
                CenterArc((-35, 4), 7.5, 0, 180)
                Line((-37.5, 4), (-42.5, 4))
                CenterArc((-35, 4), 2.5, 0, 180)
                Line((-27.5, 4), (-32.5, 4))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_56470_68037e69_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.8781495367, perimeter: 53.391329227
            with BuildLine():
                Line((2.5980762114, 4.5), (-2.5980762114, 4.5))
                Line((-2.5980762114, 4.5), (-5.1961524227, 0))
                Line((-5.1961524227, 0), (-2.5980762114, -4.5))
                Line((-2.5980762114, -4.5), (2.5980762114, -4.5))
                Line((2.5980762114, -4.5), (5.1961524227, 0))
                Line((5.1961524227, 0), (2.5980762114, 4.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5355339059, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 37.9223779587
            with BuildLine():
                CenterArc((0, 0), 3.5355339059, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 37.9223779587
            with BuildLine():
                CenterArc((0, 0), 3.5355339059, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)
    return part.part


def model_56471_65d573ce_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 48.3570423716, perimeter: 37.1375908819
            with BuildLine():
                Line((2.3094010768, 4), (-2.3094010768, 4))
                Line((-2.3094010768, 4), (-4.6188021535, 0))
                Line((-4.6188021535, 0), (-2.3094010768, -4))
                Line((-2.3094010768, -4), (2.3094010768, -4))
                Line((2.3094010768, -4), (4.6188021535, 0))
                Line((4.6188021535, 0), (2.3094010768, 4))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-27.5
        extrude(amount=-27.5, mode=Mode.ADD)
    return part.part


def model_56477_620f7fc8_0007():
    """Model: Bottom plastic table shield v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_56477_620f7fc8_0008():
    """Model: Table plastic shield v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.25, perimeter: 18
            with BuildLine():
                Line((-1.75, 0.75), (-1.75, -0.75))
                Line((-1.75, -0.75), (1.75, -0.75))
                Line((1.75, -0.75), (1.75, 0.75))
                Line((1.75, 0.75), (-1.75, 0.75))
            make_face()
            with BuildLine():
                Line((1.5, 0.5), (-1.5, 0.5))
                Line((1.5, -0.5), (1.5, 0.5))
                Line((-1.5, -0.5), (1.5, -0.5))
                Line((-1.5, 0.5), (-1.5, -0.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.25, perimeter: 18
            with BuildLine():
                Line((-1.75, 0.75), (-1.75, -0.75))
                Line((-1.75, -0.75), (1.75, -0.75))
                Line((1.75, -0.75), (1.75, 0.75))
                Line((1.75, 0.75), (-1.75, 0.75))
            make_face()
            with BuildLine():
                Line((1.5, 0.5), (-1.5, 0.5))
                Line((1.5, -0.5), (1.5, 0.5))
                Line((-1.5, -0.5), (1.5, -0.5))
                Line((-1.5, 0.5), (-1.5, -0.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3, perimeter: 8
            with BuildLine():
                Line((-1.5, 0.5), (-1.5, -0.5))
                Line((-1.5, -0.5), (1.5, -0.5))
                Line((1.5, -0.5), (1.5, 0.5))
                Line((1.5, 0.5), (-1.5, 0.5))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)
    return part.part


def model_56477_620f7fc8_0013():
    """Model: Handle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.ADD)
    return part.part


def model_56486_82b3e23a_0031():
    """Model: Nakretka v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1912868499, perimeter: 2.8477336844
            with BuildLine():
                Line((0.158771324, -0.275), (0.3175426481, 0))
                Line((0.3175426481, 0), (0.158771324, 0.275))
                Line((0.158771324, 0.275), (-0.158771324, 0.275))
                Line((-0.158771324, 0.275), (-0.3175426481, 0))
                Line((-0.3175426481, 0), (-0.158771324, -0.275))
                Line((-0.158771324, -0.275), (0.158771324, -0.275))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.12
        extrude(amount=0.12, both=True)
    return part.part


def model_56799_4512d89e_0016():
    """Model: Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_57129_75609244_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0533214608, perimeter: 19.444670942
            with BuildLine():
                CenterArc((0.25, 0.6785714286), 2.8324828656, -13.861027563, 207.722055126)
                CenterArc((0.25, 0.25), 2.7613402543, -5.1944289077, 190.3888578155)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_57535_ccee1266_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2875, perimeter: 6.16
            with BuildLine():
                Line((0, 0.3), (0, -0.3))
                Line((0, 0.625), (0, 0.3))
                Line((-1.83, 0.625), (0, 0.625))
                Line((-1.83, -0.625), (-1.83, 0.625))
                Line((0, -0.625), (-1.83, -0.625))
                Line((0, -0.3), (0, -0.625))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.87, perimeter: 24.1
            with BuildLine():
                Line((0, -0.3), (11.45, -0.3))
                Line((11.45, -0.3), (11.45, 0.3))
                Line((11.45, 0.3), (0, 0.3))
                Line((0, 0.3), (0, -0.3))
            make_face()
        # OneSide extrude, distance=1.05
        extrude(amount=1.05, mode=Mode.ADD)
    return part.part


def model_57546_0a71bb94_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2025, perimeter: 180
            with BuildLine():
                Line((35, -38.5), (-10, -38.5))
                Line((35, 6.5), (35, -38.5))
                Line((-10, 6.5), (35, 6.5))
                Line((-10, -38.5), (-10, 6.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_57983_e5b4e62e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.4799984646, perimeter: 72.800000608
            with BuildLine():
                Line((6, 10), (6, 0))
                Line((0, 10), (6, 10))
                Line((0, 0), (0, 10))
                Line((6, 0), (0, 0))
            make_face()
            with BuildLine():
                Line((0.200000003, 5.2000000775), (0.200000003, 9.800000146))
                Line((0.200000003, 9.800000146), (5.8000000864, 9.800000146))
                Line((5.8000000864, 9.800000146), (5.8000000864, 5.2000000775))
                Line((5.8000000864, 5.2000000775), (0.200000003, 5.2000000775))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.200000003, 0.200000003), (5.8000000864, 0.200000003))
                Line((0.200000003, 4.8000000715), (0.200000003, 0.200000003))
                Line((5.8000000864, 4.8000000715), (0.200000003, 4.8000000715))
                Line((5.8000000864, 0.200000003), (5.8000000864, 4.8000000715))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.4799984646, perimeter: 72.800000608
            with BuildLine():
                Line((6, 10), (6, 0))
                Line((0, 10), (6, 10))
                Line((0, 0), (0, 10))
                Line((6, 0), (0, 0))
            make_face()
            with BuildLine():
                Line((0.200000003, 5.2000000775), (0.200000003, 9.800000146))
                Line((0.200000003, 9.800000146), (5.8000000864, 9.800000146))
                Line((5.8000000864, 9.800000146), (5.8000000864, 5.2000000775))
                Line((5.8000000864, 5.2000000775), (0.200000003, 5.2000000775))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.200000003, 0.200000003), (5.8000000864, 0.200000003))
                Line((0.200000003, 4.8000000715), (0.200000003, 0.200000003))
                Line((5.8000000864, 4.8000000715), (0.200000003, 4.8000000715))
                Line((5.8000000864, 0.200000003), (5.8000000864, 4.8000000715))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 25.7600007677, perimeter: 20.400000304
            with BuildLine():
                Line((5.8000000864, 5.2000000775), (0.200000003, 5.2000000775))
                Line((5.8000000864, 9.800000146), (5.8000000864, 5.2000000775))
                Line((0.200000003, 9.800000146), (5.8000000864, 9.800000146))
                Line((0.200000003, 5.2000000775), (0.200000003, 9.800000146))
            make_face()
            # Profile area: 25.7600007677, perimeter: 20.400000304
            with BuildLine():
                Line((5.8000000864, 0.200000003), (5.8000000864, 4.8000000715))
                Line((5.8000000864, 4.8000000715), (0.200000003, 4.8000000715))
                Line((0.200000003, 4.8000000715), (0.200000003, 0.200000003))
                Line((0.200000003, 0.200000003), (5.8000000864, 0.200000003))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_60292_ac2b9317_0000():
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
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2797179833, perimeter: 36.0897751211
            with BuildLine():
                CenterArc((8.2299350416, -2.6682601155), 1.7057337141, 90, 180)
                Line((8.2299350416, 0), (8.2299350416, -0.9625264014))
                _nurbs_edge([(0, 0), (0.160044008, -0.0380985432), (0.4805322802, -0.1109476161), (0.9624654328, -0.210177384), (1.6074841732, -0.322063856), (2.4181002238, -0.4255972825), (3.2334384289, -0.4896314016), (4.0538708327, -0.5110541843), (4.8795759391, -0.4883725015), (5.7103165671, -0.423570298), (6.545700783, -0.3199259711), (7.2174122542, -0.2085363192), (7.722988071, -0.1100027904), (8.0608221274, -0.0377599453), (8.2299350416, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0, -0.8597202705), (0, 0))
                CenterArc((0, -2.6682601155), 1.808539845, -90, 180)
                Line((0, -5.336520231), (0, -4.4767999605))
                _nurbs_edge([(0, -5.336520231), (0.1600771761, -5.3108774081), (0.4806288893, -5.2618453074), (0.9626485187, -5.1950576579), (1.6077649042, -5.119752062), (2.418471583, -5.0500700624), (3.2338661734, -5.0069745122), (4.0543179163, -4.9925594778), (4.8800037664, -5.0078285195), (5.7106880597, -5.0514451212), (6.5459816549, -5.1212023535), (7.2175954484, -5.1961709185), (7.7230847424, -5.2624862554), (8.0608553178, -5.3111071051), (8.2299350416, -5.336520231)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((8.2299350416, -4.3739938296), (8.2299350416, -5.336520231))
            make_face()
            with BuildLine():
                EllipticalCenterArc((4.1149675208, -2.5446092759), 1.0446092759, 0.4278262304, 0, 360, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.4040130958, perimeter: 4.8310398237
            with Locations((4.1149675208, -2.5446092759)):
                Ellipse(1.0446092759, 0.4278262304, rotation=90)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4040130958, perimeter: 4.8310398237
            with Locations((4.1149675208, -2.5446092759)):
                Ellipse(1.0446092759, 0.4278262304, rotation=90)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)
    return part.part


def model_60710_e4b3ae4f_0002():
    """Model: suporrter v1"""
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
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.2328724468, perimeter: 29.8258836446
            with BuildLine():
                Line((0, -5), (0, 0))
                Line((0, -5), (2, -5))
                Line((2, -5), (2, 0))
                _nurbs_edge([(0, 0), (0.0514483931, 0.0004839528), (0.1520178217, 0.0063114756), (0.2958905734, 0.0296322971), (0.4737447106, 0.089895565), (0.671103369, 0.2117973055), (0.8384696658, 0.3738736234), (0.9660214088, 0.5633958907), (1.0369552483, 0.7585472728), (1.0376310693, 0.9386506448), (0.9664353651, 1.093236234), (0.846855471, 1.2350681585), (0.7226401902, 1.3962398952), (0.6404635493, 1.6124480885), (0.6362532984, 1.9107369344), (0.7201165613, 2.2959102944), (0.8823761026, 2.7558676002), (1.0991528292, 3.2665212577), (1.3380851924, 3.7968419605), (1.5639925684, 4.3138566716), (1.7444882805, 4.7875932734), (1.8557643878, 5.1962033487), (1.8879711843, 5.5306664357), (1.8517309687, 5.8006619564), (1.7727666413, 6.0279398263), (1.6849198066, 6.2378297799), (1.6239815807, 6.451957555), (1.620678833, 6.6792034825), (1.695677279, 6.9114632852), (1.858881919, 7.1302924229), (2.1079713447, 7.311311846), (2.4269834741, 7.4296034835), (2.7854930243, 7.4643530504), (3.1453580988, 7.4001980272), (3.4666669457, 7.2287196369), (3.7142680007, 6.950064746), (3.8634078784, 6.5741551402), (3.9073949175, 6.1230384304), (3.8574069718, 5.6287062374), (3.7363819579, 5.1274961341), (3.5746287693, 4.6554505609), (3.4048030724, 4.2433867295), (3.2570461759, 3.9118462821), (3.1543285524, 3.6666226842), (3.1070289585, 3.4926993668), (3.1098157811, 3.3527416898), (3.1482521814, 3.2038277357), (3.2043144245, 3.0128396006), (3.2614727167, 2.7690158371), (3.3044969374, 2.4763925568), (3.3200308478, 2.1488281472), (3.2968268786, 1.8043627445), (3.2262291777, 1.4591122818), (3.1022086159, 1.1240601772), (2.92081557, 0.8066605337), (2.6797713552, 0.511277622), (2.4383614846, 0.2943268252), (2.2298511805, 0.1428108435), (2.0786495225, 0.0467745724), (2, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0181818182, 0.0363636364, 0.0545454545, 0.0727272727, 0.0909090909, 0.1090909091, 0.1272727273, 0.1454545455, 0.1636363636, 0.1818181818, 0.2, 0.2181818182, 0.2363636364, 0.2545454545, 0.2727272727, 0.2909090909, 0.3090909091, 0.3272727273, 0.3454545455, 0.3636363636, 0.3818181818, 0.4, 0.4181818182, 0.4363636364, 0.4545454545, 0.4727272727, 0.4909090909, 0.5090909091, 0.5272727273, 0.5454545455, 0.5636363636, 0.5818181818, 0.6, 0.6181818182, 0.6363636364, 0.6545454545, 0.6727272727, 0.6909090909, 0.7090909091, 0.7272727273, 0.7454545455, 0.7636363636, 0.7818181818, 0.8, 0.8181818182, 0.8363636364, 0.8545454545, 0.8727272727, 0.8909090909, 0.9090909091, 0.9272727273, 0.9454545455, 0.9636363636, 0.9818181818, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)
    return part.part


def model_60716_dcd9370c_0008():
    """Model: gear v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.8495559215, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_60717_7ba1f3ab_0001():
    """Model: base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_60720_ef9a0a95_0006():
    """Model: DRAWER v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.25, perimeter: 10
            with BuildLine():
                Line((0, 2), (0, 2.5))
                Line((0, 2.5), (-2.5, 2.5))
                Line((-2.5, 2.5), (-2.5, 0))
                Line((-2.5, 0), (-2, 0))
                Line((-2, 0), (-2, 2))
                Line((-2, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=5.6
        extrude(amount=5.6)
    return part.part


def model_60759_23829707_0004():
    """Model: small whell v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 276.4601535159, perimeter: 69.115038379
            with BuildLine():
                CenterArc((0, 0), 9.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True)
    return part.part


def model_60787_6f3aa359_0000():
    """Model: shield v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 85.47, perimeter: 37.6
            with BuildLine():
                Line((4.7, -3.85), (3.85, -3.85))
                Line((4.7, 3.85), (4.7, -3.85))
                Line((3.85, 3.85), (4.7, 3.85))
                Line((3.85, 4.7), (3.85, 3.85))
                Line((-3.85, 4.7), (3.85, 4.7))
                Line((-3.85, 3.85), (-3.85, 4.7))
                Line((-4.7, 3.85), (-3.85, 3.85))
                Line((-4.7, -3.85), (-4.7, 3.85))
                Line((-3.85, -3.85), (-4.7, -3.85))
                Line((-3.85, -4.7), (-3.85, -3.85))
                Line((3.85, -4.7), (-3.85, -4.7))
                Line((3.85, -3.85), (3.85, -4.7))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5)
    return part.part


def model_61198_0c99f50a_0013():
    """Model: 電力裝置"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 80.64, perimeter: 36.8
            with BuildLine():
                Line((12.534364035, -71.4728099729), (23.734364035, -71.4728099729))
                Line((12.534364035, -78.6728099729), (12.534364035, -71.4728099729))
                Line((23.734364035, -78.6728099729), (12.534364035, -78.6728099729))
                Line((23.734364035, -71.4728099729), (23.734364035, -78.6728099729))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.36, perimeter: 76.8
            with BuildLine():
                Line((24.134364035, -79.0728099729), (12.134364035, -79.0728099729))
                Line((24.134364035, -71.0728099729), (24.134364035, -79.0728099729))
                Line((12.134364035, -71.0728099729), (24.134364035, -71.0728099729))
                Line((12.134364035, -79.0728099729), (12.134364035, -71.0728099729))
            make_face()
            with BuildLine():
                Line((23.734364035, -71.4728099729), (23.734364035, -78.6728099729))
                Line((23.734364035, -78.6728099729), (12.534364035, -78.6728099729))
                Line((12.534364035, -78.6728099729), (12.534364035, -71.4728099729))
                Line((12.534364035, -71.4728099729), (23.734364035, -71.4728099729))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 80.64, perimeter: 36.8
            with BuildLine():
                Line((12.534364035, -71.4728099729), (23.734364035, -71.4728099729))
                Line((12.534364035, -78.6728099729), (12.534364035, -71.4728099729))
                Line((23.734364035, -78.6728099729), (12.534364035, -78.6728099729))
                Line((23.734364035, -71.4728099729), (23.734364035, -78.6728099729))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_61379_d9f89cb9_0000():
    """Model: Big_gear"""
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
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 97.9347876525, perimeter: 35.0811179651
            with BuildLine():
                CenterArc((0, 0), 5.5833333333, -3.348226589, 1.4526872711)
                CenterArc((0, 0), 5.5833333333, -1.8955393179, 3.7910786358)
                CenterArc((0, 0), 5.5833333333, 1.8955393179, 1.4526872711)
                CenterArc((0, 0), 5.5833333333, 3.348226589, 353.303546822)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3189238162, perimeter: 2.2413177029
            with BuildLine():
                _nurbs_edge([(5.9007715896, -0.2882825633), (5.9140987845, -0.2848276111), (5.9537578093, -0.2740357105), (6.0195179225, -0.2538807922), (6.0979143259, -0.2264861785), (6.1762402785, -0.1958942101), (6.2545465053, -0.1624532027), (6.3061372202, -0.137969636), (6.3320908086, -0.1256527606)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2760029471, 0.2760029471, 0.2760029471, 0.2760029471, 0.3173011329, 0.3992728814, 0.4822965614, 0.5663716781, 0.6514978696, 0.7376748494, 0.7376748494, 0.7376748494, 0.7376748494], 3)
                CenterArc((-0.0207295123, 0), 6.3540628457, -1.13310843, 2.2662168599)
                _nurbs_edge([(5.9007715896, 0.2882825633), (5.9140987845, 0.2848276111), (5.9537578093, 0.2740357105), (6.0195179225, 0.2538807922), (6.0979143259, 0.2264861785), (6.1762402785, 0.1958942101), (6.2545465053, 0.1624532027), (6.3061372202, 0.137969636), (6.3320908086, 0.1256527606)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2760029471, 0.2760029471, 0.2760029471, 0.2760029471, 0.3173011329, 0.3992728814, 0.4822965614, 0.5663716781, 0.6514978696, 0.7376748494, 0.7376748494, 0.7376748494, 0.7376748494], 3)
                CenterArc((5.6339011472, 0.566327872), 0.3853946377, -97.9979702105, 51.8231409971)
                CenterArc((0, 0), 5.5833333333, -1.8955393179, 3.7910786358)
                CenterArc((5.6339011472, -0.566327872), 0.3853946377, 46.1748292134, 51.8231409971)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_61379_d9f89cb9_0001():
    """Model: Little_gear"""
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
            # Profile area: 7.8757982496, perimeter: 9.9483767364
            with BuildLine():
                CenterArc((0, 0), 1.5833333333, 8.2665492276, 343.4669015447)
                CenterArc((0, 0), 1.5833333333, -8.2665492276, 16.5330984553)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3421577547, perimeter: 2.2719782607
            with BuildLine():
                Line((1.5668823406, 0.2276492369), (1.8594438419, 0.270154919))
                CenterArc((0, 0), 1.5833333333, -8.2665492276, 16.5330984553)
                Line((1.5668823406, -0.2276492369), (1.8594438419, -0.270154919))
                _nurbs_edge([(1.8594438419, -0.270154919), (1.8764832244, -0.2705085084), (1.911022191, -0.2712252372), (1.962987865, -0.263158381), (2.0154384325, -0.2514873123), (2.0681929861, -0.2355909249), (2.1210934031, -0.2161168013), (2.174017276, -0.1931922511), (2.2268066991, -0.1669342224), (2.2794742589, -0.137641249), (2.3137297945, -0.1158632929), (2.3310389789, -0.1048589792)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0510375346, 0.1034534971, 0.1571887411, 0.2122327497, 0.2685796158, 0.3262250345, 0.3851655303, 0.4453981695, 0.5069204312, 0.5069204312, 0.5069204312, 0.5069204312], 3)
                CenterArc((-0.0640010538, 0), 2.3973343871, -2.5069069843, 5.0138139687)
                _nurbs_edge([(1.8594438419, 0.270154919), (1.8764832244, 0.2705085084), (1.911022191, 0.2712252372), (1.962987865, 0.263158381), (2.0154384325, 0.2514873123), (2.0681929861, 0.2355909249), (2.1210934031, 0.2161168013), (2.174017276, 0.1931922511), (2.2268066991, 0.1669342224), (2.2794742589, 0.137641249), (2.3137297945, 0.1158632929), (2.3310389789, 0.1048589792)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0510375346, 0.1034534971, 0.1571887411, 0.2122327497, 0.2685796158, 0.3262250345, 0.3851655303, 0.4453981695, 0.5069204312, 0.5069204312, 0.5069204312, 0.5069204312], 3)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_62390_8695c82f_0000():
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
            # Profile area: 4.9157786748, perimeter: 26.9317921224
            with BuildLine():
                Line((-4.9963397253, -2.3795753433), (-4.7596841043, -2.6794014395))
                _nurbs_edge([(-4.7596841043, -2.6794014395), (-4.6256174911, -2.4791498646), (-4.3571473101, -2.0955763291), (-3.9534312008, -1.5710036528), (-3.4131064503, -0.9738977798), (-2.7342877207, -0.3995255232), (-2.0521536948, 0.0061137495), (-1.3670353777, 0.2563436153), (-0.6796068061, 0.3795136505), (0.0089366943, 0.4271070063), (0.6970672298, 0.4654710037), (1.3832079435, 0.5633952949), (2.0659552891, 0.7824388304), (2.7443979402, 1.1631905122), (3.4180849166, 1.7264800465), (4.0868492339, 2.4807596348), (4.6179311637, 3.2373958919), (5.0140665574, 3.8898579986), (5.2771967511, 4.3623276305), (5.4085218258, 4.6079363761)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((5.0036602747, 4.6204246567), (5.4085218258, 4.6079363761))
                _nurbs_edge([(-4.9963397253, -2.3795753433), (-4.8702621033, -2.1773873209), (-4.6167021088, -1.789883453), (-4.2321479829, -1.259242881), (-3.7109185862, -0.6536999047), (-3.0451283638, -0.0683887751), (-2.3654126695, 0.3479818838), (-1.6729947592, 0.607525941), (-0.9704163183, 0.7364774324), (-0.2622597797, 0.7831853507), (0.4454943765, 0.8112297773), (1.146575165, 0.8875367198), (1.8352546418, 1.0734882967), (2.5075566454, 1.4121465356), (3.1614803391, 1.9258025888), (3.7962214701, 2.62400284), (4.2886459793, 3.331102615), (4.6494427917, 3.9439188717), (4.8862143972, 4.3888569147), (5.0036602747, 4.6204246567)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


def model_63475_d64bec59_0001():
    """Model: ????? v1"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8681001348, perimeter: 11.0851251684
            with BuildLine():
                Line((-1.6, 0.9237604307), (-1.6, -0.9237604307))
                Line((-1.6, -0.9237604307), (0, -1.8475208614))
                Line((0, -1.8475208614), (1.6, -0.9237604307))
                Line((1.6, -0.9237604307), (1.6, 0.9237604307))
                Line((1.6, 0.9237604307), (0, 1.8475208614))
                Line((0, 1.8475208614), (-1.6, 0.9237604307))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_65391_b6004d3f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 2.4067279439, perimeter: 6.6921372127
            with BuildLine():
                Line((1.1000000164, -0.1000000015), (-1.1993854948, -0.1000000015))
                Line((1.1000000164, 0.9466830937), (1.1000000164, -0.1000000015))
                Line((-1.1993854948, 0.9466830937), (1.1000000164, 0.9466830937))
                Line((-1.1993854948, -0.1000000015), (-1.1993854948, 0.9466830937))
            make_face()
        # TwoSides offset extrude, full=25, trim=8
        extrude(amount=25)
        extrude(sk.sketch, amount=8, mode=Mode.SUBTRACT)
    return part.part


def model_65813_123f1f95_0002():
    """Model: -4 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.7624877163, perimeter: 15.0694645048
            with BuildLine():
                CenterArc((12.2258530811, 7.3423563761), 1.581584872, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12.2258530811, 7.3423563761), 0.8167948937, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


def model_65858_61e9b51a_0002():
    """Model: 1st Level"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8502295699, perimeter: 17.9542020153
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_66288_5cea5285_0002():
    """Model: table 3 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.2992222566, perimeter: 25.679062669
            with BuildLine():
                Line((2.5000000373, -4.5000000671), (3.00000006, -4.0000000443))
                CenterArc((4.8440014974, -1.5), 3.1064998829, 126.4125077083, 107.1749859592)
                Line((2.4962231303, 1.5037768697), (3, 1))
                CenterArc((-0.0100819482, 4.0997714613), 3.6084280603, -133.9298313575, 87.9227753823)
                Line((-3.020831426, 0.9937122213), (-2.5135259569, 1.5010176904))
                CenterArc((-4.637343165, -1.5099306678), 2.9801573648, -56.6731110747, 113.824241632)
                Line((-2.5, -4.5), (-3, -4))
                CenterArc((-0.0000000143, -6.9585020992), 3.5063132347, 44.5204991704, 90.9590001224)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_66364_f554a8fb_0000():
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
        # Sketch6 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5809.4539483962, perimeter: 319.6486756681
            with BuildLine():
                Line((27.8929530774, -51.961299915), (27.8929530774, 51.961299915))
                Line((27.8929530774, 51.961299915), (-28.0087849267, 51.961299915))
                Line((-28.0087849267, 51.961299915), (-28.0087849267, -51.961299915))
                Line((-28.0087849267, -51.961299915), (27.8929530774, -51.961299915))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_67262_a2ac1dc4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3934069766, perimeter: 14.071915278
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                Line((0.6, -0.45), (0.6, 0.45))
                CenterArc((0, 0), 0.75, 36.8698976458, 286.2602047083)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_67262_d9978c87_0000():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.8989376624, perimeter: 34.1104803083
            with BuildLine():
                Line((-5.07, 1.4), (-3.67, 0))
                Line((-1.4, 0), (-3.67, 0))
                Line((0, 1.4), (-1.4, 0))
                Line((0, 1.4), (0, 8.76))
                Line((-1.4, 10.16), (0, 8.76))
                Line((-5.07, 10.16), (-1.4, 10.16))
                Line((-5.07, 8.26), (-5.07, 10.16))
                Line((-2.535, 8.26), (-5.07, 8.26))
                CenterArc((-2.535, 7.625), 0.635, 0, 90)
                Line((-1.9, 2.535), (-1.9, 7.625))
                CenterArc((-2.535, 2.535), 0.635, -90, 90)
                Line((-3.07, 1.9), (-2.535, 1.9))
                Line((-3.07, 2.0579360056), (-3.07, 1.9))
                Line((-5.07, 2.0579360056), (-3.07, 2.0579360056))
                Line((-5.07, 1.4), (-5.07, 2.0579360056))
            make_face()
        # Symmetric extrude, full_length=True, total=1.9
        extrude(amount=0.95, both=True)
    return part.part


def model_68956_dbfcec3f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5500, perimeter: 320
            with BuildLine():
                Line((-55, 25), (-55, -25))
                Line((-55, -25), (55, -25))
                Line((55, -25), (55, 25))
                Line((55, 25), (-55, 25))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_69139_450e1e08_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.8589567924, perimeter: 54.9778714378
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -4.2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_69470_88ad0eac_0001():
    """Model: body"""
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
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.237735614, perimeter: 3.96145597
            with BuildLine():
                _nurbs_edge([(-0.535817133, 0.35), (-0.5399267729, 0.336), (-0.5477871599, 0.308), (-0.5585010946, 0.266), (-0.5705973386, 0.21), (-0.5818217021, 0.14), (-0.5888019478, 0.07), (-0.5911917232, 0), (-0.5888019478, -0.07), (-0.5818217021, -0.14), (-0.5705973386, -0.21), (-0.5585010946, -0.266), (-0.5477871599, -0.308), (-0.5399267729, -0.336), (-0.535817133, -0.35)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.64, -146.8471120714, 113.6942241428)
                _nurbs_edge([(0.535817133, 0.35), (0.5399267729, 0.336), (0.5477871599, 0.308), (0.5585010946, 0.266), (0.5705973386, 0.21), (0.5818217021, 0.14), (0.5888019478, 0.07), (0.5911917232, 0), (0.5888019478, -0.07), (0.5818217021, -0.14), (0.5705973386, -0.21), (0.5585010946, -0.266), (0.5477871599, -0.308), (0.5399267729, -0.336), (0.535817133, -0.35)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.64, 33.1528879286, 113.6942241428)
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


def model_72083_3ff9e2cf_0000():
    """Model: lamp_base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 325.1442220938, perimeter: 69.4213964281
            with BuildLine():
                CenterArc((-8, -4), 3, -180, 90)
                Line((-8, -7), (7, -7))
                CenterArc((7, 0.0017528928), 7.0017528928, -90, 178.1868028064)
                Line((7.2215423167, 7), (-8, 7))
                CenterArc((-8, 4), 3, 90, 90)
                Line((-11, 4), (-11, -4))
            make_face()
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)
    return part.part


def model_72162_28bdbc9a_0001():
    """Model: Table"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 33 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0088357293, perimeter: 0.385619449
            with BuildLine():
                CenterArc((-0.075, 9), 0.075, 0, 180)
                Line((-0.15, 9), (0, 9))
            make_face()
            # Profile area: 32.8218581963, perimeter: 67.5407075111
            with BuildLine():
                Line((-30, 8), (-0.4, 8))
                CenterArc((-0.4, 8.4), 0.4, -90, 90)
                Line((0, 9), (0, 8.4))
                Line((-0.15, 9), (0, 9))
                Line((-30, 9), (-0.15, 9))
                CenterArc((-30, 7), 2, 90, 90)
                Line((-32, 6.5), (-32, 7))
                Line((-32, 6.5), (-31, 6.5))
                Line((-31, 6.5), (-31, 7))
                CenterArc((-30, 7), 1, 90, 90)
            make_face()
            # Profile area: 3.9832233447, perimeter: 9.9664466895
            with BuildLine():
                Line((-32, 2.5167766553), (-32, 6.5))
                Line((-32, 2.5167766553), (-31, 2.5167766553))
                Line((-31, 2.5167766553), (-31, 6.5))
                Line((-32, 6.5), (-31, 6.5))
            make_face()
            # Profile area: 28.1875500482, perimeter: 58.1690823332
            with BuildLine():
                Line((-32, 2.5167766553), (-31, 2.5167766553))
                Line((-32, 2.0167766553), (-32, 2.5167766553))
                CenterArc((-30, 2.0167766553), 2, 180, 90)
                Line((-4.9999718543, 0.0167766553), (-30, 0.0167766553))
                CenterArc((-4.9999718543, 0.4167766553), 0.4, -90, 90)
                Line((-4.5999718543, 0.6167766553), (-4.5999718543, 0.4167766553))
                CenterArc((-4.9999718543, 0.6167766553), 0.4, 0, 90)
                Line((-4.9999718543, 1.0167766553), (-30, 1.0167766553))
                CenterArc((-30, 2.0167766553), 1, -180, 90)
                Line((-31, 2.0167766553), (-31, 2.5167766553))
            make_face()
        # Symmetric extrude, each_side=22.5
        extrude(amount=22.5, both=True)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 33 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.9832233447, perimeter: 9.9664466895
            with BuildLine():
                Line((-32, 2.5167766553), (-32, 6.5))
                Line((-32, 2.5167766553), (-31, 2.5167766553))
                Line((-31, 2.5167766553), (-31, 6.5))
                Line((-32, 6.5), (-31, 6.5))
            make_face()
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_72966_11b78e5e_0002():
    """Model: Healical Gear (16R@0.00) (1)"""
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
        # Gear (0.300 module; 4.800 pitch dia) -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 12.8824933751, perimeter: 12.723450247
            Circle(2.025)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_73651_a41647f8_0002():
    """Model: Patas"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 135, perimeter: 153.6
            with BuildLine():
                Line((107.0264859806, 55), (107.0264859806, 0))
                Line((107.0264859806, 0), (108.8264859806, 0))
                Line((108.8264859806, 0), (108.8264859806, 75))
                Line((107.0264859806, 75), (108.8264859806, 75))
                Line((107.0264859806, 75), (107.0264859806, 55))
            make_face()
            # Profile area: 135, perimeter: 153.6
            with BuildLine():
                Line((-49.3735140194, 75), (-51.1735140194, 75))
                Line((-51.1735140194, 75), (-51.1735140194, 0))
                Line((-51.1735140194, 0), (-49.3735140194, 0))
                Line((-49.3735140194, 0), (-49.3735140194, 55))
                Line((-49.3735140194, 55), (-49.3735140194, 75))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 108, perimeter: 123.6
            with BuildLine():
                Line((118.8264859806, 137.5), (118.8264859806, 77.5))
                Line((117.0264859806, 137.5), (118.8264859806, 137.5))
                Line((117.0264859806, 77.5), (117.0264859806, 137.5))
                Line((118.8264859806, 77.5), (117.0264859806, 77.5))
            make_face()
            # Profile area: 108, perimeter: 123.6
            with BuildLine():
                Line((-59.3735140194, 137.5), (-59.3735140194, 77.5))
                Line((-61.1735140194, 137.5), (-59.3735140194, 137.5))
                Line((-61.1735140194, 77.5), (-61.1735140194, 137.5))
                Line((-59.3735140194, 77.5), (-61.1735140194, 77.5))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_73655_a9997148_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3186.6611963268, perimeter: 227.7415926536
            with BuildLine():
                CenterArc((23.13, -32.02), 1, -90, 90)
                Line((24.13, -32.02), (24.13, 33.02))
                Line((24.13, 33.02), (-24.13, 33.02))
                Line((-24.13, 33.02), (-24.13, -32.02))
                CenterArc((-23.13, -32.02), 1, 180, 90)
                Line((-23.13, -33.02), (23.13, -33.02))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_74277_b2a1723a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 625, perimeter: 100
            with BuildLine():
                Line((-15, -50), (-40, -50))
                Line((-15, -25), (-15, -50))
                Line((-40, -25), (-15, -25))
                Line((-40, -50), (-40, -25))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


def model_75860_f6e0212c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 48, perimeter: 32
            with BuildLine():
                Line((13, -12), (13, -8))
                Line((13, -8), (1, -8))
                Line((1, -8), (1, -12))
                Line((1, -12), (13, -12))
            make_face()
        # Symmetric extrude, full_length=True, total=1.5
        extrude(amount=0.75, both=True)
    return part.part


def model_76298_af8ea172_0007():
    """Model: M8 25mm countersunk v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_77291_7a76bde8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.000043998, perimeter: 0.3292384444
            with BuildLine():
                CenterArc((0, 0), 2.05, -0.4820104437, 4.6006328131)
                CenterArc((0.400199309, 0.0127047609), 1.65, -1.0400807184, 5.7167733627)
            make_face()
            # Profile area: 2.0908383899, perimeter: 12.5355347092
            with BuildLine():
                CenterArc((0, 0), 2.05, -179.9751607142, 179.4931502706)
                CenterArc((0.400199309, 0.0127047609), 1.65, -173.4516133997, 172.4115326813)
                CenterArc((-1.6250127709, 0.0024307366), 0.425, -179.5524860795, 154.8076371753)
            make_face()
            # Profile area: 2.0033407842, perimeter: 12.3057171167
            with BuildLine():
                CenterArc((-1.6250127709, 0.0024307366), 0.425, 25.3261738814, 154.0549032751)
                CenterArc((0.400199309, 0.0127047609), 1.65, 4.6766926442, 169.3562457328)
                CenterArc((0, 0), 2.05, 4.1186223694, 175.6851294219)
            make_face()
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3178390067, perimeter: 4.3872393527
            with BuildLine():
                CenterArc((0, 0), 2.05, 179.8037517914, 0.2210874944)
                CenterArc((-1.6250127709, 0.0024307366), 0.425, -179.5524860795, 154.8076371753)
                CenterArc((0.400199309, 0.0127047609), 1.65, 174.032938377, 12.5154482232)
                CenterArc((-1.6250127709, 0.0024307366), 0.425, 25.3261738814, 154.0549032751)
            make_face()
            with BuildLine():
                CenterArc((-1.6250127709, 0.0024307366), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.4723303859, perimeter: 19.8029999064
            with BuildLine():
                CenterArc((0.400199309, 0.0127047609), 1.65, -173.4516133997, 172.4115326813)
                CenterArc((0, 0), 2.05, -0.4820104437, 4.6006328131)
                CenterArc((0.400199309, 0.0127047609), 1.65, 4.6766926442, 169.3562457328)
                CenterArc((-1.6250127709, 0.0024307366), 0.425, -24.7448489041, 50.0710227856)
            make_face()
            with BuildLine():
                CenterArc((0.400199309, 0.0127047609), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.012028145, perimeter: 0.7318283233
            with BuildLine():
                CenterArc((-1.6250127709, 0.0024307366), 0.425, -24.7448489041, 50.0710227856)
                CenterArc((0.400199309, 0.0127047609), 1.65, 174.032938377, 12.5154482232)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_77397_df713db5_0002():
    """Model: Component C v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 51.0415362018, perimeter: 27.3101761242
            with BuildLine():
                Line((-3.25, 0), (3.25, 0))
                Line((3.25, 0), (3.25, 5.3))
                CenterArc((0, 5.3), 3.25, 0, 180)
                Line((-3.25, 5.3), (-3.25, 0))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


def model_77561_5df8176f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1339726135, perimeter: 1.7221112452
            with BuildLine():
                Line((-0.2534675973, 20.905259091), (-0.3854399362, 20.682481115))
                Line((0.3477894368, 20.6907004585), (-0.3854399362, 20.682481115))
                Line((0.3477894368, 20.6907004585), (0.2240889712, 20.9106123973))
                Line((0.2240889712, 20.9106123973), (-0.2534675973, 20.905259091))
            make_face()
            # Profile area: 0.0652796014, perimeter: 1.1078732262
            with BuildLine():
                Line((-0.5484518541, 20.9019523809), (-0.6804241929, 20.679174405))
                Line((-0.3854399362, 20.682481115), (-0.6804241929, 20.679174405))
                Line((-0.2534675973, 20.905259091), (-0.3854399362, 20.682481115))
                Line((-0.2534675973, 20.905259091), (-0.5484518541, 20.9019523809))
            make_face()
            # Profile area: 0.3875553838, perimeter: 3.6569692162
            with BuildLine():
                Line((0.8866072359, 19.7328021489), (1.0312356694, 19.989919364))
                Line((1.1237209267, 19.3112666987), (0.8866072359, 19.7328021489))
                Line((0.652465051, 19.3165493756), (1.1237209267, 19.3112666987))
                Line((0.5115333565, 19.0660041409), (0.652465051, 19.3165493756))
                Line((0.5115333565, 19.0660041409), (1.5575335407, 19.054278704))
                Line((1.5575335407, 19.054278704), (1.0312356694, 19.989919364))
            make_face()
            # Profile area: 0.0986992313, perimeter: 1.4325196942
            with BuildLine():
                Line((-0.9422220609, 19.742596319), (-0.6988076774, 19.3316968521))
                Line((-0.9422220609, 19.742596319), (-1.1824249312, 19.3371180974))
                Line((-1.1824249312, 19.3371180974), (-0.6988076774, 19.3316968521))
            make_face()
            # Profile area: 0.1750786228, perimeter: 1.9713762015
            with BuildLine():
                Line((0.2592337981, 19.0688323647), (0.4001654926, 19.3193775994))
                Line((-0.4398901214, 19.328794442), (0.4001654926, 19.3193775994))
                Line((-0.4398901214, 19.328794442), (-0.2895342981, 19.0749839369))
                Line((-0.2895342981, 19.0749839369), (0.2592337981, 19.0688323647))
            make_face()
            # Profile area: 0.3559253836, perimeter: 3.7281494267
            with BuildLine():
                Line((1.5575335407, 20.925560024), (0.5115333565, 20.913834587))
                Line((0.6352338221, 20.6939226482), (0.5115333565, 20.913834587))
                Line((1.1767616887, 20.6999930591), (0.6352338221, 20.6939226482))
                Line((0.9042904523, 20.21559975), (1.1767616887, 20.6999930591))
                Line((1.0312356694, 19.989919364), (0.9042904523, 20.21559975))
                Line((1.0312356694, 19.989919364), (1.5575335407, 20.925560024))
            make_face()
            # Profile area: 0.0636110384, perimeter: 1.0795557091
            with BuildLine():
                Line((0.5115333565, 20.913834587), (0.2240889712, 20.9106123973))
                Line((0.3477894368, 20.6907004585), (0.2240889712, 20.9106123973))
                Line((0.6352338221, 20.6939226482), (0.3477894368, 20.6907004585))
                Line((0.6352338221, 20.6939226482), (0.5115333565, 20.913834587))
            make_face()
            # Profile area: 0.0636110384, perimeter: 1.0795557091
            with BuildLine():
                Line((0.5115333565, 19.0660041409), (0.652465051, 19.3165493756))
                Line((0.4001654926, 19.3193775994), (0.652465051, 19.3165493756))
                Line((0.2592337981, 19.0688323647), (0.4001654926, 19.3193775994))
                Line((0.2592337981, 19.0688323647), (0.5115333565, 19.0660041409))
            make_face()
            # Profile area: 0.1303292315, perimeter: 1.6461319082
            with BuildLine():
                Line((-0.2895342981, 19.0749839369), (0.2592337981, 19.0688323647))
                Line((-0.2895342981, 19.0749839369), (-0.0062730052, 18.5968202699))
                Line((-0.0062730052, 18.5968202699), (0.2592337981, 19.0688323647))
            make_face()
            # Profile area: 0.1339726135, perimeter: 1.7221112452
            with BuildLine():
                Line((0.8866072359, 19.7328021489), (0.7596620188, 19.9584825348))
                Line((0.4001654926, 19.3193775994), (0.7596620188, 19.9584825348))
                Line((0.4001654926, 19.3193775994), (0.652465051, 19.3165493756))
                Line((0.652465051, 19.3165493756), (0.8866072359, 19.7328021489))
            make_face()
            # Profile area: 0.0652796014, perimeter: 1.1078732262
            with BuildLine():
                Line((1.0312356694, 19.989919364), (0.9042904523, 20.21559975))
                Line((0.7596620188, 19.9584825348), (0.9042904523, 20.21559975))
                Line((0.8866072359, 19.7328021489), (0.7596620188, 19.9584825348))
                Line((0.8866072359, 19.7328021489), (1.0312356694, 19.989919364))
            make_face()
            # Profile area: 0.0986992313, perimeter: 1.4325196942
            with BuildLine():
                Line((0.652465051, 19.3165493756), (0.8866072359, 19.7328021489))
                Line((0.652465051, 19.3165493756), (1.1237209267, 19.3112666987))
                Line((1.1237209267, 19.3112666987), (0.8866072359, 19.7328021489))
            make_face()
            # Profile area: 0.1750786228, perimeter: 1.9713762015
            with BuildLine():
                Line((0.6352338221, 20.6939226482), (0.3477894368, 20.6907004585))
                Line((0.7596620188, 19.9584825348), (0.3477894368, 20.6907004585))
                Line((0.7596620188, 19.9584825348), (0.9042904523, 20.21559975))
                Line((0.9042904523, 20.21559975), (0.6352338221, 20.6939226482))
            make_face()
            # Profile area: 0.1303292315, perimeter: 1.6461319082
            with BuildLine():
                Line((0.9042904523, 20.21559975), (0.6352338221, 20.6939226482))
                Line((0.9042904523, 20.21559975), (1.1767616887, 20.6999930591))
                Line((1.1767616887, 20.6999930591), (0.6352338221, 20.6939226482))
            make_face()
            # Profile area: 0.3875553838, perimeter: 3.6569692162
            with BuildLine():
                Line((-0.6988076774, 19.3316968521), (-0.5484518541, 19.077886347))
                Line((-1.1824249312, 19.3371180974), (-0.6988076774, 19.3316968521))
                Line((-0.9422220609, 19.742596319), (-1.1824249312, 19.3371180974))
                Line((-1.0887347517, 19.989919364), (-0.9422220609, 19.742596319))
                Line((-1.0887347517, 19.989919364), (-1.6218893701, 19.0899193506))
                Line((-1.6218893701, 19.0899193506), (-0.5484518541, 19.077886347))
            make_face()
            # Profile area: 0.3559253836, perimeter: 3.7281494267
            with BuildLine():
                Line((0.2592337981, 19.0688323647), (0.5115333565, 19.0660041409))
                Line((-0.0062730052, 18.5968202699), (0.2592337981, 19.0688323647))
                Line((-0.2895342981, 19.0749839369), (-0.0062730052, 18.5968202699))
                Line((-0.5484518541, 19.077886347), (-0.2895342981, 19.0749839369))
                Line((-0.5484518541, 19.077886347), (-0.0013122093, 18.1542786906))
                Line((-0.0013122093, 18.1542786906), (0.5115333565, 19.0660041409))
            make_face()
            # Profile area: 0.1303292315, perimeter: 1.6461319082
            with BuildLine():
                Line((-0.6804241929, 20.679174405), (-0.9601356589, 20.207003079))
                Line((-0.6804241929, 20.679174405), (-1.2361567222, 20.672944763))
                Line((-1.2361567222, 20.672944763), (-0.9601356589, 20.207003079))
            make_face()
            # Profile area: 0.0986992313, perimeter: 1.4325196942
            with BuildLine():
                Line((0.2240889712, 20.9106123973), (-0.2534675973, 20.905259091))
                Line((0.2240889712, 20.9106123973), (-0.0069640342, 21.3213732958))
                Line((-0.0069640342, 21.3213732958), (-0.2534675973, 20.905259091))
            make_face()
            # Profile area: 0.3559253836, perimeter: 3.7281494267
            with BuildLine():
                Line((-0.9601356589, 20.207003079), (-1.0887347517, 19.989919364))
                Line((-1.2361567222, 20.672944763), (-0.9601356589, 20.207003079))
                Line((-0.6804241929, 20.679174405), (-1.2361567222, 20.672944763))
                Line((-0.5484518541, 20.9019523809), (-0.6804241929, 20.679174405))
                Line((-0.5484518541, 20.9019523809), (-1.6218893701, 20.8899193774))
                Line((-1.6218893701, 20.8899193774), (-1.0887347517, 19.989919364))
            make_face()
            # Profile area: 0.1750786228, perimeter: 1.9713762015
            with BuildLine():
                Line((-0.9601356589, 20.207003079), (-0.8136229681, 19.959680034))
                Line((-0.3854399362, 20.682481115), (-0.8136229681, 19.959680034))
                Line((-0.3854399362, 20.682481115), (-0.6804241929, 20.679174405))
                Line((-0.6804241929, 20.679174405), (-0.9601356589, 20.207003079))
            make_face()
            # Profile area: 0.1339726135, perimeter: 1.7221112452
            with BuildLine():
                Line((-0.6988076774, 19.3316968521), (-0.4398901214, 19.328794442))
                Line((-0.8136229681, 19.959680034), (-0.4398901214, 19.328794442))
                Line((-0.8136229681, 19.959680034), (-0.9422220609, 19.742596319))
                Line((-0.9422220609, 19.742596319), (-0.6988076774, 19.3316968521))
            make_face()
            # Profile area: 0.3875553838, perimeter: 3.6569692162
            with BuildLine():
                Line((-0.2534675973, 20.905259091), (-0.5484518541, 20.9019523809))
                Line((-0.0069640342, 21.3213732958), (-0.2534675973, 20.905259091))
                Line((0.2240889712, 20.9106123973), (-0.0069640342, 21.3213732958))
                Line((0.5115333565, 20.913834587), (0.2240889712, 20.9106123973))
                Line((0.5115333565, 20.913834587), (-0.0013122093, 21.8255600374))
                Line((-0.0013122093, 21.8255600374), (-0.5484518541, 20.9019523809))
            make_face()
            # Profile area: 0.0652796014, perimeter: 1.1078732262
            with BuildLine():
                Line((-0.5484518541, 19.077886347), (-0.2895342981, 19.0749839369))
                Line((-0.4398901214, 19.328794442), (-0.2895342981, 19.0749839369))
                Line((-0.6988076774, 19.3316968521), (-0.4398901214, 19.328794442))
                Line((-0.6988076774, 19.3316968521), (-0.5484518541, 19.077886347))
            make_face()
            # Profile area: 0.0636110384, perimeter: 1.0795557091
            with BuildLine():
                Line((-1.0887347517, 19.989919364), (-0.9422220609, 19.742596319))
                Line((-0.8136229681, 19.959680034), (-0.9422220609, 19.742596319))
                Line((-0.9601356589, 20.207003079), (-0.8136229681, 19.959680034))
                Line((-0.9601356589, 20.207003079), (-1.0887347517, 19.989919364))
            make_face()
            # Profile area: 1.6051690731, perimeter: 4.7201514983
            with BuildLine():
                Line((0.7596620188, 19.9584825348), (0.3477894368, 20.6907004585))
                Line((0.3477894368, 20.6907004585), (-0.3854399362, 20.682481115))
                Line((-0.3854399362, 20.682481115), (-0.8136229681, 19.959680034))
                Line((-0.8136229681, 19.959680034), (-0.4398901214, 19.328794442))
                Line((-0.4398901214, 19.328794442), (0.4001654926, 19.3193775994))
                Line((0.4001654926, 19.3193775994), (0.7596620188, 19.9584825348))
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


def model_77578_fc4eb62f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 706.8583470577, perimeter: 94.2477796077
            Circle(15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_77692_170bc334_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.7699111843, perimeter: 30.1592894745
            with BuildLine():
                CenterArc((0, 0), 2.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_77777_8c6ab6b8_0000():
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
        # Sketch2 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.7457627571, 4.0501678161)):
                Circle(0.1)
        # TwoSides extrude (symmetric), distance=1.5
        extrude(amount=1.5, both=True)
    return part.part


MODELS = {
    "model_50817_b89fb3ae_0001": {"func": model_50817_b89fb3ae_0001, "volume": 15.2901721968, "area": 71.1750992276},
    "model_50833_d533dcbc_0003": {"func": model_50833_d533dcbc_0003, "volume": 11.4138456967, "area": 30.2581405991},
    "model_50833_d533dcbc_0005": {"func": model_50833_d533dcbc_0005, "volume": 46.6009905524, "area": 82.7432925936},
    "model_50914_57d3d851_0004": {"func": model_50914_57d3d851_0004, "volume": 2.6102563891, "area": 16.1904239624},
    "model_50914_f539e302_0000": {"func": model_50914_f539e302_0000, "volume": 54.8192590387, "area": 211.9924695631},
    "model_50947_49287c16_0005": {"func": model_50947_49287c16_0005, "volume": 16.0879624613, "area": 53.2042853052},
    "model_51022_47816098_0008": {"func": model_51022_47816098_0008, "volume": 42.4115008235, "area": 84.8230016469},
    "model_51024_b2fd60ca_0001": {"func": model_51024_b2fd60ca_0001, "volume": 3.155205063, "area": 17.2992362112},
    "model_51341_6ba06c4a_0007": {"func": model_51341_6ba06c4a_0007, "volume": 0.5330163859, "area": 6.5301888615},
    "model_51345_4b292361_0010": {"func": model_51345_4b292361_0010, "volume": 42.7472158125, "area": 87.2462331581},
    "model_51535_f818cb2a_0001": {"func": model_51535_f818cb2a_0001, "volume": 7.6489124659, "area": 30.2635921988},
    "model_51536_a18dc325_0010": {"func": model_51536_a18dc325_0010, "volume": 0.0060777464, "area": 0.6233614087},
    "model_51567_5f9bb333_0013": {"func": model_51567_5f9bb333_0013, "volume": 0.22, "area": 2.38},
    "model_51579_d0c3e154_0000": {"func": model_51579_d0c3e154_0000, "volume": 1963.4954084936, "area": 4084.0704496667},
    "model_51586_2ad96f8c_0002": {"func": model_51586_2ad96f8c_0002, "volume": 0.0596902622, "area": 1.2566370811},
    "model_51601_2616f89b_0017": {"func": model_51601_2616f89b_0017, "volume": 5.3014376029, "area": 17.6714586764},
    "model_51736_e8b2b138_0010": {"func": model_51736_e8b2b138_0010, "volume": 2.170644262, "area": 23.9907992011},
    "model_51777_87ff5835_0004": {"func": model_51777_87ff5835_0004, "volume": 15541.081821, "area": 11645.138},
    "model_51777_87ff5835_0006": {"func": model_51777_87ff5835_0006, "volume": 3005.1976543769, "area": 3146.3628904421},
    "model_51777_87ff5835_0008": {"func": model_51777_87ff5835_0008, "volume": 201.9198090464, "area": 375.0920227007},
    "model_51777_87ff5835_0009": {"func": model_51777_87ff5835_0009, "volume": 342649.1419547008, "area": 74379.5222943558},
    "model_51862_e5f65013_0001": {"func": model_51862_e5f65013_0001, "volume": 0.8752852012, "area": 6.0937103422},
    "model_51862_e5f65013_0002": {"func": model_51862_e5f65013_0002, "volume": 19.2844886, "area": 41.8000753238},
    "model_51872_765c2fb4_0001": {"func": model_51872_765c2fb4_0001, "volume": 2.6000000775, "area": 21.3000004724},
    "model_51877_0032e502_0001": {"func": model_51877_0032e502_0001, "volume": 4.8000001431, "area": 29.6000007987},
    "model_51877_0032e502_0004": {"func": model_51877_0032e502_0004, "volume": 8.5878032603, "area": 26.3756130868},
    "model_51877_0032e502_0014": {"func": model_51877_0032e502_0014, "volume": 0.1413716736, "area": 2.0263272939},
    "model_51877_0032e502_0015": {"func": model_51877_0032e502_0015, "volume": 0.1650000049, "area": 1.8159412061},
    "model_51891_9455ea02_0004": {"func": model_51891_9455ea02_0004, "volume": 47.8217504845, "area": 81.9037485065},
    "model_51914_fb924efa_0004": {"func": model_51914_fb924efa_0004, "volume": 3.926990817, "area": 17.2787595947},
    "model_51915_e704f5dd_0001": {"func": model_51915_e704f5dd_0001, "volume": 276.9991747905, "area": 614.6466125626},
    "model_51916_fa226b15_0003": {"func": model_51916_fa226b15_0003, "volume": 0.4019017096, "area": 7.1292139853},
    "model_51916_fa226b15_0007": {"func": model_51916_fa226b15_0007, "volume": 36.8929155164, "area": 231.2045422224},
    "model_51916_fa226b15_0012": {"func": model_51916_fa226b15_0012, "volume": 5.3261466382, "area": 29.3355676826},
    "model_51940_aa0fca73_0022": {"func": model_51940_aa0fca73_0022, "volume": 183.2176835574, "area": 285.0052855337},
    "model_51942_f6e66631_0005": {"func": model_51942_f6e66631_0005, "volume": 0.8670795724, "area": 11.0584061406},
    "model_52012_77070fda_0017": {"func": model_52012_77070fda_0017, "volume": 1.3026548246, "area": 7.118583772},
    "model_52557_e6a00b06_0014": {"func": model_52557_e6a00b06_0014, "volume": 27.4751511647, "area": 80.9580500861},
    "model_52660_3593651a_0000": {"func": model_52660_3593651a_0000, "volume": 19624, "area": 15196},
    "model_52879_de812eb3_0008": {"func": model_52879_de812eb3_0008, "volume": 2.8981192229, "area": 18.6767683256},
    "model_52884_c8150d6e_0034": {"func": model_52884_c8150d6e_0034, "volume": 3.3220977944, "area": 12.8526448841},
    "model_53078_b592f2bd_0002": {"func": model_53078_b592f2bd_0002, "volume": 27.143360527, "area": 64.0884901332},
    "model_53222_e9c623af_0001": {"func": model_53222_e9c623af_0001, "volume": 7.9985651892, "area": 27.1917803238},
    "model_53448_2f7c767c_0018": {"func": model_53448_2f7c767c_0018, "volume": 9.8960168588, "area": 199.2398060907},
    "model_53448_2f7c767c_0022": {"func": model_53448_2f7c767c_0022, "volume": 0.0062831853, "area": 0.1884955592},
    "model_53846_89405f98_0016": {"func": model_53846_89405f98_0016, "volume": 0.0737174716, "area": 1.6086525183},
    "model_53927_ef5208b9_0006": {"func": model_53927_ef5208b9_0006, "volume": 1.9716208091, "area": 44.1607049825},
    "model_53927_ef5208b9_0008": {"func": model_53927_ef5208b9_0008, "volume": 1.8962193641, "area": 42.9040002735},
    "model_54037_43125db1_0000": {"func": model_54037_43125db1_0000, "volume": 297.140238274, "area": 304.4703877856},
    "model_54273_21c2b38f_0046": {"func": model_54273_21c2b38f_0046, "volume": 5.832, "area": 19.44},
    "model_54285_76f37095_0005": {"func": model_54285_76f37095_0005, "volume": 0.037699113, "area": 0.816814103},
    "model_54374_5c085a74_0011": {"func": model_54374_5c085a74_0011, "volume": 5.6576982007, "area": 28.7472047695},
    "model_54374_5c085a74_0014": {"func": model_54374_5c085a74_0014, "volume": 0.2567482673, "area": 2.447136894},
    "model_54375_f795a300_0004": {"func": model_54375_f795a300_0004, "volume": 622.0353454108, "area": 471.2388980385},
    "model_54501_96041527_0000": {"func": model_54501_96041527_0000, "volume": 65, "area": 111},
    "model_54608_56e6ef8c_0000": {"func": model_54608_56e6ef8c_0000, "volume": 15.7079632679, "area": 45.465555998},
    "model_54761_cec613c4_0015": {"func": model_54761_cec613c4_0015, "volume": 4.2535030667, "area": 15.3230076877},
    "model_54761_cec613c4_0017": {"func": model_54761_cec613c4_0017, "volume": 14.9555174577, "area": 35.3268489021},
    "model_54761_cec613c4_0018": {"func": model_54761_cec613c4_0018, "volume": 38.2492623172, "area": 70.2700110187},
    "model_54761_cec613c4_0019": {"func": model_54761_cec613c4_0019, "volume": 16.8232404828, "area": 38.4291939495},
    "model_54761_cec613c4_0021": {"func": model_54761_cec613c4_0021, "volume": 933.7095498812, "area": 1088.8626753511},
    "model_54761_cec613c4_0022": {"func": model_54761_cec613c4_0022, "volume": 0.819519108, "area": 5.2095396922},
    "model_54979_6bd8ad31_0014": {"func": model_54979_6bd8ad31_0014, "volume": 467.7398325369, "area": 4716.1256622434},
    "model_54987_c8dbbe1e_0000": {"func": model_54987_c8dbbe1e_0000, "volume": 1218.5804457044, "area": 2560.9071378333},
    "model_55017_d18176a6_0000": {"func": model_55017_d18176a6_0000, "volume": 12.6208202518, "area": 31.3346465861},
    "model_55084_fc00f917_0002": {"func": model_55084_fc00f917_0002, "volume": 62.5373287605, "area": 269.784269127},
    "model_55135_f1186d58_0006": {"func": model_55135_f1186d58_0006, "volume": 0.0321460198, "area": 0.8756194693},
    "model_55271_cf70456e_0000": {"func": model_55271_cf70456e_0000, "volume": 1, "area": 21.3},
    "model_55278_d699fcaa_0000": {"func": model_55278_d699fcaa_0000, "volume": 35.3429173529, "area": 61.261056745},
    "model_55289_292737cb_0000": {"func": model_55289_292737cb_0000, "volume": 7.8082331783, "area": 25.5220785012},
    "model_55296_3173b45d_0000": {"func": model_55296_3173b45d_0000, "volume": 32.5, "area": 102},
    "model_55302_13bb4506_0000": {"func": model_55302_13bb4506_0000, "volume": 315.9392296067, "area": 448.3599639099},
    "model_55342_4090e441_0000": {"func": model_55342_4090e441_0000, "volume": 8.0196599804, "area": 22.9041229143},
    "model_55346_5e81d5e1_0000": {"func": model_55346_5e81d5e1_0000, "volume": 7.3282035543, "area": 21.5881490443},
    "model_55395_c160dca4_0000": {"func": model_55395_c160dca4_0000, "volume": 72.565546721, "area": 157.6965523986},
    "model_55625_453e11ac_0005": {"func": model_55625_453e11ac_0005, "volume": 0.0498931038, "area": 1.2957980864},
    "model_55633_282eaae6_0002": {"func": model_55633_282eaae6_0002, "volume": 0.0050265482, "area": 0.2293362637},
    "model_55636_6180bfce_0000": {"func": model_55636_6180bfce_0000, "volume": 4772.2871870789, "area": 9544.5743741578},
    "model_55715_525d1d3e_0000": {"func": model_55715_525d1d3e_0000, "volume": 5.8874487652, "area": 64.9199354198},
    "model_55758_efbfee69_0000": {"func": model_55758_efbfee69_0000, "volume": 40, "area": 106},
    "model_55791_2eb44ee9_0000": {"func": model_55791_2eb44ee9_0000, "volume": 289.3210484415, "area": 278.1314742894},
    "model_55796_cb1b98f1_0000": {"func": model_55796_cb1b98f1_0000, "volume": 13.7321048417, "area": 82.3711430961},
    "model_55866_b041060d_0000": {"func": model_55866_b041060d_0000, "volume": 67.5, "area": 102},
    "model_55915_4badf6b0_0005": {"func": model_55915_4badf6b0_0005, "volume": 23.3370630402, "area": 474.0980286149},
    "model_55927_f8b31711_0017": {"func": model_55927_f8b31711_0017, "volume": 1.7309486271, "area": 11.1182697428},
    "model_56065_00bbe5da_0022": {"func": model_56065_00bbe5da_0022, "volume": 0.0219911486, "area": 0.879645943},
    "model_56157_d9157017_0003": {"func": model_56157_d9157017_0003, "volume": 22.6069007352, "area": 115.484945946},
    "model_56167_90101372_0013": {"func": model_56167_90101372_0013, "volume": 131.9468914508, "area": 538.7831400906},
    "model_56321_07658e97_0000": {"func": model_56321_07658e97_0000, "volume": 1295.2673413096, "area": 1048.4629363588},
    "model_56322_d0bb31b7_0000": {"func": model_56322_d0bb31b7_0000, "volume": 59.150780833, "area": 120.685992628},
    "model_56343_60e8809c_0008": {"func": model_56343_60e8809c_0008, "volume": 0.0408407045, "area": 0.879645943},
    "model_56345_80dc7bcc_0007": {"func": model_56345_80dc7bcc_0007, "volume": 4.9087385212, "area": 17.6714586764},
    "model_56430_4f35ba2f_0002": {"func": model_56430_4f35ba2f_0002, "volume": 12624.8855661489, "area": 9621.0239359928},
    "model_56430_4f35ba2f_0019": {"func": model_56430_4f35ba2f_0019, "volume": 3430.8350894591, "area": 2141.4933011426},
    "model_56470_68037e69_0000": {"func": model_56470_68037e69_0000, "volume": 325.4837367219, "area": 501.6200471558},
    "model_56471_65d573ce_0000": {"func": model_56471_65d573ce_0000, "volume": 360.6629229675, "area": 453.1710843689},
    "model_56477_620f7fc8_0007": {"func": model_56477_620f7fc8_0007, "volume": 0.2827433388, "area": 2.4504422698},
    "model_56477_620f7fc8_0008": {"func": model_56477_620f7fc8_0008, "volume": 9.1875, "area": 76},
    "model_56477_620f7fc8_0013": {"func": model_56477_620f7fc8_0013, "volume": 6.5345127195, "area": 33.6778732465},
    "model_56486_82b3e23a_0031": {"func": model_56486_82b3e23a_0031, "volume": 0.045908844, "area": 1.0660297841},
    "model_56799_4512d89e_0016": {"func": model_56799_4512d89e_0016, "volume": 0.7539822369, "area": 4.7752208335},
    "model_57129_75609244_0000": {"func": model_57129_75609244_0000, "volume": 1.5266607304, "area": 15.8289783927},
    "model_57535_ccee1266_0000": {"func": model_57535_ccee1266_0000, "volume": 8.35725, "area": 46.1},
    "model_57546_0a71bb94_0000": {"func": model_57546_0a71bb94_0000, "volume": 10125, "area": 4950},
    "model_57983_e5b4e62e_0000": {"func": model_57983_e5b4e62e_0000, "volume": 55.4399953938, "area": 354.4000018239},
    "model_60292_ac2b9317_0000": {"func": model_60292_ac2b9317_0000, "volume": 14.1398595739, "area": 74.6043235609},
    "model_60710_e4b3ae4f_0002": {"func": model_60710_e4b3ae4f_0002, "volume": 227.0962703101, "area": 318.8990282052},
    "model_60716_dcd9370c_0008": {"func": model_60716_dcd9370c_0008, "volume": 28.2743338823, "area": 65.9734457254},
    "model_60717_7ba1f3ab_0001": {"func": model_60717_7ba1f3ab_0001, "volume": 2.8863382505, "area": 22.5409272895},
    "model_60720_ef9a0a95_0006": {"func": model_60720_ef9a0a95_0006, "volume": 12.6, "area": 60.5},
    "model_60759_23829707_0004": {"func": model_60759_23829707_0004, "volume": 552.9203070318, "area": 691.1503837898},
    "model_60787_6f3aa359_0000": {"func": model_60787_6f3aa359_0000, "volume": 470.085, "area": 377.74},
    "model_61198_0c99f50a_0013": {"func": model_61198_0c99f50a_0013, "volume": 261.12, "area": 310.4},
    "model_61379_d9f89cb9_0000": {"func": model_61379_d9f89cb9_0000, "volume": 49.1268487682, "area": 214.7992094037},
    "model_61379_d9f89cb9_0001": {"func": model_61379_d9f89cb9_0001, "volume": 2.465390908, "area": 19.8278883154},
    "model_62390_8695c82f_0000": {"func": model_62390_8695c82f_0000, "volume": 34.4104294698, "area": 198.3539825411},
    "model_63475_d64bec59_0001": {"func": model_63475_d64bec59_0001, "volume": 15.9625802426, "area": 37.6894255727},
    "model_65391_b6004d3f_0000": {"func": model_65391_b6004d3f_0000, "volume": 40.9143750461, "area": 118.5797885044},
    "model_65813_123f1f95_0002": {"func": model_65813_123f1f95_0002, "volume": 8.0674828028, "area": 32.6222257393},
    "model_65858_61e9b51a_0002": {"func": model_65858_61e9b51a_0002, "volume": 39.4155080303, "area": 238.7858995247},
    "model_66288_5cea5285_0002": {"func": model_66288_5cea5285_0002, "volume": 9.6496111283, "area": 51.4379758477},
    "model_66364_f554a8fb_0000": {"func": model_66364_f554a8fb_0000, "volume": 34856.7236903774, "area": 13536.7999508012},
    "model_67262_a2ac1dc4_0000": {"func": model_67262_a2ac1dc4_0000, "volume": 21.5736279065, "area": 67.0744750651},
    "model_67262_d9978c87_0000": {"func": model_67262_d9978c87_0000, "volume": 54.9079815586, "area": 122.6077879106},
    "model_68956_dbfcec3f_0000": {"func": model_68956_dbfcec3f_0000, "volume": 4400, "area": 11256},
    "model_69139_450e1e08_0000": {"func": model_69139_450e1e08_0000, "volume": 19.9294783962, "area": 107.2068493038},
    "model_69470_88ad0eac_0001": {"func": model_69470_88ad0eac_0001, "volume": 9.2830171874, "area": 32.1863910886},
    "model_72083_3ff9e2cf_0000": {"func": model_72083_3ff9e2cf_0000, "volume": 1170.5191995378, "area": 900.2054713289},
    "model_72162_28bdbc9a_0001": {"func": model_72162_28bdbc9a_0001, "volume": 2805.5693289942, "area": 5888.2594998686},
    "model_72966_11b78e5e_0002": {"func": model_72966_11b78e5e_0002, "volume": 12.8824933751, "area": 38.4884369973},
    "model_73651_a41647f8_0002": {"func": model_73651_a41647f8_0002, "volume": 16740.0000000006, "area": 20040.0000000004},
    "model_73655_a9997148_0000": {"func": model_73655_a9997148_0000, "volume": 2549.3289570614, "area": 6555.5156667765},
    "model_74277_b2a1723a_0000": {"func": model_74277_b2a1723a_0000, "volume": 4687.5, "area": 2000},
    "model_75860_f6e0212c_0000": {"func": model_75860_f6e0212c_0000, "volume": 72, "area": 144},
    "model_76298_af8ea172_0007": {"func": model_76298_af8ea172_0007, "volume": 1.2566370614, "area": 7.2884949563},
    "model_77291_7a76bde8_0000": {"func": model_77291_7a76bde8_0000, "volume": 1.9330648107, "area": 30.6285457994},
    "model_77397_df713db5_0002": {"func": model_77397_df713db5_0002, "volume": 71.4581506825, "area": 140.3173189774},
    "model_77561_5df8176f_0000": {"func": model_77561_5df8176f_0000, "volume": 2.918261196, "area": 18.0317573624},
    "model_77578_fc4eb62f_0000": {"func": model_77578_fc4eb62f_0000, "volume": 212.0575041173, "area": 1441.9910279977},
    "model_77692_170bc334_0000": {"func": model_77692_170bc334_0000, "volume": 9.4247779608, "area": 82.9380460548},
    "model_77777_8c6ab6b8_0000": {"func": model_77777_8c6ab6b8_0000, "volume": 0.0942477796, "area": 1.9477874452},
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
