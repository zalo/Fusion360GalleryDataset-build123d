"""Batch 001 - passing/02_3ops
94 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a curved bracket or support arm with a complex wireframe structure, featuring a bent tubular body, a flat mounting flange at the bottom, and what appears to be a mounting plate or socket at the upper end.
def model_101190_cfdcb477_0001():
    """Model: Trigger"""
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
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.360228377, perimeter: 7.6391956089
            with BuildLine():
                CenterArc((4.8331596783, 0.5540798114), 0.0637362699, 125.8335695596, 140.0504989231)
                _nurbs_edge([(4.8285850211, 0.490507926), (4.8363355927, 0.4881725264), (4.8529157063, 0.4845704665), (4.8810227487, 0.4823735655), (4.9250199755, 0.4859036187), (4.9907987326, 0.5012404528), (5.0666007339, 0.527486687), (5.1504758705, 0.5642025274), (5.2387398118, 0.6102489021), (5.326796817, 0.6641494297), (5.4098785557, 0.7243998764), (5.4838479533, 0.7897823034), (5.5458903614, 0.8596218025), (5.5955842013, 0.9341544287), (5.6348683937, 1.0144999628), (5.6668235646, 1.1022101283), (5.6892374968, 1.1795833311), (5.7055164594, 1.2422628921), (5.7162975836, 1.2861954001), (5.7216702524, 1.3086981882)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(5.7216702524, 1.3086981882), (5.7256161499, 1.3252251132), (5.73272027, 1.3606588507), (5.7410134263, 1.4209491295), (5.747658886, 1.514647852), (5.750449047, 1.6483322311), (5.7501454888, 1.7912171936), (5.7492947889, 1.935675364), (5.7501667432, 2.0750817642), (5.7542230053, 2.2055163593), (5.7620476259, 2.3259478067), (5.7736695467, 2.43712852), (5.7887507914, 2.5409185747), (5.8067940963, 2.6395487781), (5.8273464796, 2.7348523604), (5.8501098981, 2.8278904896), (5.8699387387, 2.9009675221), (5.8856800316, 2.9551060977), (5.8965578487, 2.9909036274), (5.9020926689, 3.0087286541)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((5.5859556995, 2.8594866078), 0.349593724, 25.2710746202, 126.8251275318)
                Line((5.0000000745, 2.5000000373), (5.2770076257, 3.0230924131))
                _nurbs_edge([(4.7958463769, 0.6057521409), (4.8128447799, 0.618026922), (4.8458302454, 0.642317818), (4.892274136, 0.677978037), (4.9488655536, 0.7246646156), (5.0142642973, 0.7854079609), (5.0777748344, 0.8531729779), (5.1407713301, 0.9320561902), (5.2010254242, 1.0244918242), (5.2542105764, 1.1317675383), (5.2950836554, 1.2542963306), (5.3186644942, 1.3919056476), (5.3217249828, 1.5440429939), (5.3027586128, 1.7099633891), (5.2613022063, 1.8888774633), (5.1975703309, 2.08006494), (5.1291632109, 2.2423787491), (5.0682796364, 2.3692186623), (5.023464308, 2.4560308663), (5.0000000745, 2.5000000373)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((5.5859556995, 2.8594866078), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6813499051, perimeter: 4.04038586
            with BuildLine():
                _nurbs_edge([(5.7216702524, 1.3086981882), (5.7256161499, 1.3252251132), (5.73272027, 1.3606588507), (5.7410134263, 1.4209491295), (5.747658886, 1.514647852), (5.750449047, 1.6483322311), (5.7501454888, 1.7912171936), (5.7492947889, 1.935675364), (5.7501667432, 2.0750817642), (5.7542230053, 2.2055163593), (5.7620476259, 2.3259478067), (5.7736695467, 2.43712852), (5.7887507914, 2.5409185747), (5.8067940963, 2.6395487781), (5.8273464796, 2.7348523604), (5.8501098981, 2.8278904896), (5.8699387387, 2.9009675221), (5.8856800316, 2.9551060977), (5.8965578487, 2.9909036274), (5.9020926689, 3.0087286541)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((5.8854843878, 1.2695866304), 0.1684184814, 100.6691673543, 65.9025289322)
                CenterArc((5.5859556995, 2.8594866078), 1.4494502935, -79.3308326457, 28.5587259257)
                Line((5.9020926689, 3.0087286541), (6.5025974774, 1.7366892064))
            make_face()
        # Symmetric extrude, each_side=0.275
        extrude(amount=0.275, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical dowel pin or shaft with a smooth, rounded tubular body and hemispherical ends, designed for alignment or fastening purposes.
def model_102314_91648bfc_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0735362071, perimeter: 12.9847971539
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7965946521, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


# Description: This is a sheet metal duct or air intake component with a trapezoidal cross-section, featuring a tapered/wedge-shaped body that transitions from a narrower left end to a wider right end, with a curved or angled inlet on the left side and flat parallel flanges on the top and bottom.
def model_102416_eba35f73_0016():
    """Model: corner v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.01, perimeter: 14
            with BuildLine():
                Line((1.0815143057, 0.7301583257), (1.0815143057, 3.6301583257))
                Line((1.0815143057, 3.6301583257), (1.0815143057, 3.9301583257))
                Line((1.0815143057, 3.9301583257), (0.7815143057, 3.9301583257))
                Line((0.7815143057, 3.9301583257), (0.7815143057, 0.4301583257))
                Line((0.7815143057, 0.4301583257), (4.2815143057, 0.4301583257))
                Line((4.2815143057, 0.4301583257), (4.2815143057, 0.7301583257))
                Line((4.2815143057, 0.7301583257), (3.9815143057, 0.7301583257))
                Line((3.9815143057, 0.7301583257), (1.0815143057, 0.7301583257))
            make_face()
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.205, perimeter: 9.9012193309
            with BuildLine():
                Line((3.9815143057, 0.7301583257), (1.0815143057, 0.7301583257))
                Line((1.0815143057, 3.6301583257), (3.9815143057, 0.7301583257))
                Line((1.0815143057, 0.7301583257), (1.0815143057, 3.6301583257))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical disc or wheel with a flat, circular face and a thin, ribbed or meshed edge section, featuring a slightly curved or domed profile when viewed from the side.
def model_103284_e25015aa_0003():
    """Model: Lever Switch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            with Locations((1.6994660914, 1.7998556733)):
                Circle(2.54)
        # OneSide extrude, distance=0.889
        extrude(amount=0.889)
    return part.part


# Description: This is a sheet metal enclosure or duct component with a trapezoidal/wedge shape, featuring angled side panels, a rectangular opening on top, and what appears to be a mounting flange or lip around the upper edge.
def model_104453_aba0f2d1_0008():
    """Model: LegRestSymmetric v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 272.4051625849, perimeter: 86.9255613946
            with BuildLine():
                Line((-7.5, 29), (-7.5, 36.5))
                Line((-7.5, 0), (-7.5, 29))
                Line((0, 0), (-7.5, 0))
                Line((0, 33.9966695942), (0, 0))
                CenterArc((-2.5033304058, 33.9966695942), 2.5033304058, 0, 90)
                Line((-2.5033304058, 36.5), (-7.5, 36.5))
            make_face()
        # Symmetric extrude, each_side=12.5
        extrude(amount=12.5, both=True)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 51.280031761, perimeter: 36.6491133503
            with BuildLine():
                CenterArc((-12.1, 32.75), 3.75, 90, 180)
                Line((-12.1, 29), (-7.5, 29))
                Line((-7.5, 29), (-7.5, 36.5))
                Line((-7.5, 36.5), (-12.1, 36.5))
            make_face()
            with BuildLine():
                CenterArc((-12.1, 32.75), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a multi-chambered enclosure or manifold block with an elongated, curved profile featuring internal compartments, rectangular slots on the upper surfaces, and a stepped/tiered design that transitions from a larger upper section to a narrower lower section.
def model_104892_5fcd41a9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude7 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 75 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3244779289, perimeter: 6.8566897772
            with BuildLine():
                Line((44.0303562271, 10.4836850714), (44.0303562271, 10.6399997622))
                Line((43.2899990324, 10.6399997622), (44.0303562271, 10.6399997622))
                Line((43.2499990333, 10.6399997622), (43.2899990324, 10.6399997622))
                Line((43.211466725, 10.6517179647), (43.2499990333, 10.6399997622))
                Line((43.1420833619, 10.6905266776), (43.211466725, 10.6517179647))
                Line((42.9999990389, 10.7699997593), (43.1420833619, 10.6905266776))
                Line((42.9316715625, 10.8082178751), (42.9999990389, 10.7699997593))
                Line((42.8578630263, 10.8543845351), (42.9316715625, 10.8082178751))
                Line((42.7806251098, 10.9026962456), (42.8578630263, 10.8543845351))
                Line((42.7551107982, 10.9186552472), (42.7806251098, 10.9026962456))
                Line((42.7320443309, 10.9330831415), (42.7551107982, 10.9186552472))
                Line((42.7274680883, 10.4442357302), (42.7320443309, 10.9330831415))
                Line((42.7000006363, 10.400000155), (42.7274680883, 10.4442357302))
                Line((42.1137836973, 9.4559139127), (42.7000006363, 10.400000155))
                Line((42.0746541771, 9.4145070477), (42.1137836973, 9.4559139127))
                Line((42.0500006266, 9.4000001401), (42.0746541771, 9.4145070477))
                Line((41.9000006244, 9.3117355234), (42.0500006266, 9.4000001401))
                Line((41.9000006244, 9.3000001386), (41.9000006244, 9.3117355234))
                Line((41.9000006244, 9.2569616381), (41.9000006244, 9.3000001386))
                Line((44.0303562271, 9.2569616381), (41.9000006244, 9.2569616381))
                Line((44.0303562271, 10.4836850714), (44.0303562271, 9.2569616381))
            make_face()
            # Profile area: 2.0423687943, perimeter: 6.5212770887
            with BuildLine():
                Line((44.0303562271, 10.6399997622), (44.8500006683, 10.6399997622))
                Line((44.8500006683, 10.6399997622), (44.8599995174, 10.6425610886))
                Line((44.8599995174, 10.6425610886), (44.8679318642, 10.6483495579))
                Line((44.8679318642, 10.6483495579), (45.139998991, 10.7999997586))
                Line((45.139998991, 10.7999997586), (45.1430188495, 10.8016830275))
                Line((45.1430188495, 10.8016830275), (45.1478801192, 10.8066168644))
                Line((45.1478801192, 10.8066168644), (45.150472797, 10.8133273246))
                Line((45.150472797, 10.8133273246), (45.4017531716, 11.1241698686))
                Line((45.4017531716, 11.1241698686), (45.4118816967, 11.1366992056))
                Line((45.4118816967, 11.1366992056), (45.4269439828, 11.1553317764))
                Line((45.4269439828, 11.1553317764), (45.4343149164, 11.1744094868))
                Line((45.4343149164, 11.1744094868), (45.4599989839, 11.3399997465))
                Line((45.4599989839, 11.3399997465), (45.4599989839, 11.5399997421))
                Line((45.4599989839, 11.5399997421), (45.4599989839, 11.5430005483))
                Line((45.4599989839, 11.5430005483), (45.4599989839, 11.5499997418))
                Line((45.4599989839, 11.5499997418), (45.4582071942, 11.5536422572))
                Line((45.4582071942, 11.5536422572), (45.4550940907, 11.5599708612))
                Line((45.4550940907, 11.5599708612), (45.4499989841, 11.5649997415))
                Line((45.4499989841, 11.5649997415), (45.4414601937, 11.5713580924))
                Line((45.4414601937, 11.5713580924), (45.4327164241, 11.5778690797))
                Line((45.4327164241, 11.5778690797), (45.4205353941, 11.5834974124))
                Line((45.4205353941, 11.5834974124), (45.3999989852, 11.5899997409))
                Line((45.3999989852, 11.5899997409), (45.379927324, 11.596354919))
                Line((45.379927324, 11.596354919), (45.3631595685, 11.5998738141))
                Line((45.3631595685, 11.5998738141), (44.8000006676, 11.5998738141))
                Line((44.8000006676, 11.5998738141), (44.7745444938, 11.596354919))
                Line((44.7745444938, 11.596354919), (42.7124925592, 11.2291425255))
                Line((42.7124925592, 11.2291425255), (42.6964382757, 11.2215783936))
                Line((42.6964382757, 11.2215783936), (42.6843062947, 11.2087327667))
                Line((42.6843062947, 11.2087327667), (42.6757425435, 11.1876802116))
                Line((42.6757425435, 11.1876802116), (42.6757425435, 11.1699997503))
                Line((42.6757425435, 11.1699997503), (42.6757425435, 11.0299997535))
                Line((42.6757425435, 11.0299997535), (42.6757425435, 11.0099997539))
                Line((42.6757425435, 11.0099997539), (42.6757425435, 10.9799997546))
                Line((42.6757425435, 10.9799997546), (42.676002027, 10.9770005214))
                Line((42.676002027, 10.9770005214), (42.6762631168, 10.9739827222))
                Line((42.6762631168, 10.9739827222), (42.6780020271, 10.9710005211))
                Line((42.6780020271, 10.9710005211), (42.6810020272, 10.968000521))
                Line((42.6810020272, 10.968000521), (42.6889880258, 10.9600145223))
                Line((42.6889880258, 10.9600145223), (42.7049990455, 10.9499997552))
                Line((42.7049990455, 10.9499997552), (42.7320443309, 10.9330831415))
                Line((42.7320443309, 10.9330831415), (42.7551107982, 10.9186552472))
                Line((42.7551107982, 10.9186552472), (42.7806251098, 10.9026962456))
                Line((42.7806251098, 10.9026962456), (42.8578630263, 10.8543845351))
                Line((42.8578630263, 10.8543845351), (42.9316715625, 10.8082178751))
                Line((42.9316715625, 10.8082178751), (42.9999990389, 10.7699997593))
                Line((42.9999990389, 10.7699997593), (43.1420833619, 10.6905266776))
                Line((43.1420833619, 10.6905266776), (43.211466725, 10.6517179647))
                Line((43.211466725, 10.6517179647), (43.2499990333, 10.6399997622))
                Line((43.2499990333, 10.6399997622), (43.2899990324, 10.6399997622))
                Line((43.2899990324, 10.6399997622), (44.0303562271, 10.6399997622))
            make_face()
            # Profile area: 345.3199250029, perimeter: 120.8675511574
            with BuildLine():
                Line((41.9000006244, 9.2569616381), (38.2000005692, 9.2569616381))
                CenterArc((38.2000005692, 11.1973378404), 1.9403762023, -121.849522372, 31.849522372)
                Line((32.3276015516, 11.9385512598), (37.1760830921, 9.5491106696))
                CenterArc((32.9112517272, 13.0058474039), 1.216457392, -138.5126917246, 19.8406776613)
                CenterArc((28.5774802188, -4.6351213112), 17.1794924431, 78.5085754266, 10.4954462754)
                CenterArc((27.2134293419, -31.7908693941), 44.3638127378, 87.8521635587, 7.2086003466)
                CenterArc((23.2697405977, 8.2716884918), 4.1284225906, 89.5800402165, 18.3322440921)
                CenterArc((23.747775809, 7.1055614682), 5.3859098525, 108.9358222501, 9.2763601617)
                CenterArc((32.5471033093, -13.1956544331), 27.4970236362, 114.3686807311, 14.2107151506)
                CenterArc((15.88333357, 16.7500002496), 8.4638119808, -105.6509381713, 12.3772319265)
                CenterArc((15.005498021, -31.6840341129), 40.3085454817, 91.9982219429, 17.1255774965)
                CenterArc((1.8963047378, 5.4827946993), 0.9222474374, 95.9939782991, 70.3838937333)
                Line((0.7404981216, 4.6291575185), (1.0000000149, 5.7000000849))
                CenterArc((0.7262761174, 4.4000000656), 0.2295983528, 86.4486556416, 93.5513443584)
                Line((0.4966777645, 3.4250621397), (0.4966777645, 4.4000000656))
                Line((0.6827657802, 2.4076503406), (0.4966777645, 3.4250621397))
                Line((0.800274513, 2.2041588219), (0.6827657802, 2.4076503406))
                Line((0.8199999817, 2.1699999515), (0.800274513, 2.2041588219))
                Line((0.8249999816, 2.1426631084), (0.8199999817, 2.1699999515))
                Line((0.8249999816, 2.1000000313), (0.8249999816, 2.1426631084))
                Line((0.8249999816, 1.94818468), (0.8249999816, 2.1000000313))
                Line((0.8899999801, 1.8299999591), (0.8249999816, 1.94818468))
                Line((0.8999999799, 1.7676415594), (0.8899999801, 1.8299999591))
                Line((0.8999999799, 0.9099999797), (0.8999999799, 1.7676415594))
                Line((0.7499999832, 0.7199999839), (0.8999999799, 0.9099999797))
                Line((0.7349999836, 0.6970840579), (0.7499999832, 0.7199999839))
                Line((0.7299999837, 0.6799999848), (0.7349999836, 0.6970840579))
                Line((0.7299999837, 0.6599999852), (0.7299999837, 0.6799999848))
                Line((0.7399999835, 0.6399999857), (0.7299999837, 0.6599999852))
                Line((0.759999983, 0.6199999861), (0.7399999835, 0.6399999857))
                Line((0.7907208154, 0.5958035405), (0.759999983, 0.6199999861))
                Line((1.1299999747, 0.4099999908), (0.7907208154, 0.5958035405))
                CenterArc((1.9539812574, 1.9145981401), 1.7154476806, -118.7069684063, 26.9037031124)
                Line((5.0699451298, 0.1001996306), (1.9000000283, 0.200000003))
                Line((5.0699451298, 0.1001996306), (5.0699451298, 2.2001996306))
                CenterArc((8.9956110125, 2.0722520521), 3.9277504001, 6.2521435879, 171.8810999637)
                Line((12.9000001922, 0.400000006), (12.9000001922, 2.5000000373))
                Line((33.0000004917, 0.400000006), (12.9000001922, 0.400000006))
                Line((33.0000004917, 0.400000006), (33.0000004917, 2.5000000373))
                CenterArc((36.8284005558, 2.1603998991), 3.8434327501, 11.0947576063, 163.8360597958)
                Line((40.600000605, 0.8000000119), (40.600000605, 2.9000000432))
                Line((45.0499989931, 1.4699999671), (40.600000605, 0.8000000119))
                Line((45.3399989866, 1.5699999649), (45.0499989931, 1.4699999671))
                Line((45.4599989839, 1.6699999627), (45.3399989866, 1.5699999649))
                Line((45.4899989832, 1.7299999613), (45.4599989839, 1.6699999627))
                Line((45.500000678, 1.8000000268), (45.4899989832, 1.7299999613))
                Line((45.500000678, 1.8512914191), (45.500000678, 1.8000000268))
                Line((45.7500006817, 1.8512914191), (45.500000678, 1.8512914191))
                Line((45.7500006817, 2.5350092767), (45.7500006817, 1.8512914191))
                Line((45.6096795126, 2.5350092767), (45.7500006817, 2.5350092767))
                Line((45.638040249, 2.6229859449), (45.6096795126, 2.5350092767))
                Line((45.7998139552, 3.1248174734), (45.638040249, 2.6229859449))
                Line((45.7998139552, 3.4000000507), (45.7998139552, 3.1248174734))
                Line((45.6000006795, 3.4000000507), (45.7998139552, 3.4000000507))
                CenterArc((44.9528445166, 4.0498932733), 0.9171544581, -45.1209065315, 45.1209065315)
                Line((45.8699989747, 5.2899998818), (45.8699989747, 4.0498932733))
                Line((45.8549070954, 5.3169135951), (45.8699989747, 5.2899998818))
                Line((45.8295573006, 5.3410467027), (45.8549070954, 5.3169135951))
                Line((45.700000681, 5.4000000805), (45.8295573006, 5.3410467027))
                Line((45.260478379, 5.6000000834), (45.700000681, 5.4000000805))
                Line((45.260478379, 5.9881453847), (45.260478379, 5.6000000834))
                Line((45.1945125229, 6.2000000924), (45.260478379, 5.9881453847))
                Line((45.1945125229, 7.3602190786), (45.1945125229, 6.2000000924))
                Line((45.1841123578, 7.4387388831), (45.1945125229, 7.3602190786))
                Line((44.8345387816, 8.5614228302), (45.1841123578, 7.4387388831))
                Line((44.8266999259, 8.5865979524), (44.8345387816, 8.5614228302))
                Line((44.8183577991, 8.603282206), (44.8266999259, 8.5865979524))
                Line((44.6299990024, 8.9799997993), (44.8183577991, 8.603282206))
                Line((44.6199990027, 8.9999997988), (44.6299990024, 8.9799997993))
                Line((44.5999990031, 9.0199997984), (44.6199990027, 8.9999997988))
                Line((44.5799990036, 9.0299997982), (44.5999990031, 9.0199997984))
                Line((44.5500006638, 9.037352682), (44.5799990036, 9.0299997982))
                Line((44.3000006601, 9.037352682), (44.5500006638, 9.037352682))
                Line((44.3000006601, 9.2569616381), (44.3000006601, 9.037352682))
                Line((44.0303562271, 9.2569616381), (44.3000006601, 9.2569616381))
                Line((44.0303562271, 9.2569616381), (41.9000006244, 9.2569616381))
            make_face()
            # Profile area: 10.6313786416, perimeter: 37.2959000818
            with BuildLine():
                CenterArc((36.7699991781, 2.3299999479), 3.2529683161, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((36.7699991781, 2.3299999479), 2.682858539, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 10.3929753501, perimeter: 37.348709965
            with BuildLine():
                CenterArc((9.0500001349, 2.2500000335), 3.2503845612, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((9.0500001349, 2.2500000335), 2.6938472478, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.9132278719, perimeter: 31.7704330183
            with BuildLine():
                CenterArc((36.7699991781, 2.3299999479), 2.682858539, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((36.7699991781, 2.3299999479), 2.3735629201, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 17.6991076307, perimeter: 14.913535665
            with Locations((36.7699991781, 2.3299999479)):
                Circle(2.3735629201)
            # Profile area: 4.7984876979, perimeter: 31.9654866229
            with BuildLine():
                CenterArc((9.0500001349, 2.2500000335), 2.6938472478, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((9.0500001349, 2.2500000335), 2.3936179565, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 17.9994626949, perimeter: 15.0395451754
            with Locations((9.0500001349, 2.2500000335)):
                Circle(2.3936179565)
        # OneSide extrude, distance=17.9
        extrude(amount=17.9)
    return part.part


# Description: This is a flat parallelogram plate or shim with a simple rectangular shape, featuring parallel top and bottom edges that are slightly offset, creating a skewed geometry typical of a wedge or angled spacer component.
def model_106059_5d7ef4ef_0000():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 88.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.592424971, perimeter: 8.4584796501
            with BuildLine():
                Line((-10.5605291547, 3.7982550415), (-10.1414291547, 3.7982550415))
                Line((-10.5605291547, 3.7982550415), (-10.2619034462, 0))
                Line((-10.2619034462, 0), (-9.8425, 0))
                Line((-9.8425, 0), (-10.1414291547, 3.7982550415))
            make_face()
            # Profile area: 38.9062134105, perimeter: 28.1063379596
            with BuildLine():
                Line((-9.8425, 0), (-10.1414291547, 3.7982550415))
                Line((-9.8425, 0), (0.1019034462, 0))
                Line((0.4005291547, 3.7982550415), (0.1019034462, 0))
                Line((-10.1414291547, 3.7982550415), (0.4005291547, 3.7982550415))
            make_face()
        # OneSide extrude, distance=0.1016
        extrude(amount=0.1016)
    return part.part


# Description: This is a cylindrical disc or wheel with a flat face, curved perimeter edge, and a textured or meshed rim section on the side, suggesting it may be a fan blade, pulley, or similar rotating component.
def model_106325_dce63a49_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2118648941, perimeter: 7.2751532793
            Circle(1.1578766061)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a parallelepiped or wedge-shaped block with a slanted top surface and a darker left side face, featuring a simple angular geometry without holes, slots, or curves.
def model_106726_19e9c7f3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.390454, perimeter: 2.77
            with BuildLine():
                Line((-0.4955, 0.197), (0.4955, 0.197))
                Line((-0.4955, -0.197), (-0.4955, 0.197))
                Line((0.4955, -0.197), (-0.4955, -0.197))
                Line((0.4955, 0.197), (0.4955, -0.197))
            make_face()
        # OneSide extrude, distance=0.147
        extrude(amount=0.147)
    return part.part


# Description: This is a cylindrical mesh or perforated filter container with a curved, tapered design and an open top rim, featuring a textured mesh surface on the sides and a solid base.
def model_107247_b9ff3971_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3436116965, perimeter: 5.4977871438
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.794
        extrude(amount=0.794)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3626134233, perimeter: 3.3536501577
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is an oval or elliptical cylindrical shell with a ribbed or finned interior structure, featuring vertical reinforcement ribs running along the length of the basin-like form, commonly used as a structural component or containment vessel.
def model_108856_09f25b7b_0010():
    """Model: Logo3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8168879732, perimeter: 7.7801542066
            Circle(1.23825)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a cylindrical bushing or sleeve with a central bore, featuring two protruding flanges or tabs on opposite sides that extend radially outward from the main body.
def model_109880_aebcec75_0002():
    """Model: YRS75ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2725660089, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.8
        extrude(amount=-3.8)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.2938046055, perimeter: 27.6460153516
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal tube with a tapered top section, featuring a hollow interior cavity and angled top faces that form a pyramid-like cap.
def model_109946_242843a6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30, perimeter: 26
            with BuildLine():
                Line((0, 20), (1.5, 20))
                Line((-1.5, 20), (0, 20))
                Line((-1.5, 20), (-1.5, 10))
                Line((-1.5, 10), (1.5, 10))
                Line((1.5, 10), (1.5, 20))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is a cylindrical connector or coupling sleeve with a tapered end, featuring a flange on one end and internal geometry designed for joining or mounting purposes.
def model_110324_300f25b9_0000():
    """Model: left handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.9425229575, perimeter: 28.253981634
            with BuildLine():
                Line((3.8, 2.55), (-3.8, 2.55))
                Line((-3.8, 2.55), (-3.8, -2.55))
                Line((-3.8, -2.55), (-2.5, -2.55))
                CenterArc((0, -2.55), 2.5, 0, 180)
                Line((2.5, -2.55), (3.8, -2.55))
                Line((3.8, -2.55), (3.8, 2.55))
            make_face()
            # Profile area: 12.8648219165, perimeter: 22.3920337176
            with BuildLine():
                Line((2.5, -2.55), (3.8, -2.55))
                CenterArc((0, -2.55), 2.5, -180, 180)
                Line((-3.8, -2.55), (-2.5, -2.55))
                CenterArc((0, -2.55), 3.8, 180, 180)
            make_face()
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                Line((-2.5, -2.55), (2.5, -2.55))
                CenterArc((0, -2.55), 2.5, 0, 180)
            make_face()
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                CenterArc((0, -2.55), 2.5, -180, 180)
                Line((-2.5, -2.55), (2.5, -2.55))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                Line((-2.5, -2.55), (2.5, -2.55))
                CenterArc((0, -2.55), 2.5, 0, 180)
            make_face()
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                CenterArc((0, -2.55), 2.5, -180, 180)
                Line((-2.5, -2.55), (2.5, -2.55))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal bracket or channel with a parallelogram-shaped profile, featuring two vertical flanges on the left side and a large flat back panel, designed for structural support or mounting applications.
def model_110344_a5d1ecce_0003():
    """Model: Lower Bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.36, perimeter: 12.5
            with BuildLine():
                Line((-1.85, -2.725), (-2.65, -2.725))
                Line((-1.85, 2.725), (-1.85, -2.725))
                Line((-2.65, 2.725), (-1.85, 2.725))
                Line((-2.65, -2.725), (-2.65, 2.725))
            make_face()
            # Profile area: 4.36, perimeter: 12.5
            with BuildLine():
                Line((1.85, -2.725), (1.85, 2.725))
                Line((2.65, -2.725), (1.85, -2.725))
                Line((2.65, 2.725), (2.65, -2.725))
                Line((1.85, 2.725), (2.65, 2.725))
            make_face()
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.165, perimeter: 18.3
            with BuildLine():
                Line((-1.85, -2.725), (1.85, -2.725))
                Line((1.85, -2.725), (1.85, 2.725))
                Line((1.85, 2.725), (-1.85, 2.725))
                Line((-1.85, 2.725), (-1.85, -2.725))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)
    return part.part


# Description: A rectangular box-shaped structural component with a sloped top surface, featuring multiple vertical ribs or fins on its sides and internal cross-bracing elements visible through semi-transparent surfaces.
def model_110440_85dae82d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1280201159, perimeter: 1.4687880714
            with BuildLine():
                CenterArc((0, 0), 0.28575, -90, 77.2187493585)
                Line((0.2786696297, -0.0632162953), (0.2841593358, 0.0301087091))
                CenterArc((0, 0), 0.28575, 6.0483293147, 83.9516706853)
                Line((0, 0), (0, 0.28575))
                Line((0, 0), (0, -0.28575))
            make_face()
            # Profile area: 0.0766447694, perimeter: 1.3454926091
            with BuildLine():
                Line((-0.3062307636, 0.4053229816), (-0.2841593358, 0.0301087091))
                CenterArc((0, 0), 0.28575, 90, 83.9516706853)
                Line((0, 0.28575), (0, 0.508))
                CenterArc((0, 0), 0.508, 90, 37.0718794403)
            make_face()
            # Profile area: 0.1280201159, perimeter: 1.4687880714
            with BuildLine():
                CenterArc((0, 0), 0.28575, -167.2187493585, 77.2187493585)
                Line((0, 0), (0, -0.28575))
                Line((0, 0), (0, 0.28575))
                CenterArc((0, 0), 0.28575, 90, 83.9516706853)
                Line((-0.2841593358, 0.0301087091), (-0.2786696297, -0.0632162953))
            make_face()
            # Profile area: 0.0766447694, perimeter: 1.3454926091
            with BuildLine():
                Line((0, 0.28575), (0, 0.508))
                CenterArc((0, 0), 0.28575, 6.0483293147, 83.9516706853)
                Line((0.2841593358, 0.0301087091), (0.3062307636, 0.4053229816))
                CenterArc((0, 0), 0.508, 52.9281205597, 37.0718794403)
            make_face()
            # Profile area: 0.0662795996, perimeter: 1.2522177405
            with BuildLine():
                CenterArc((0, 0), 0.508, -120.3389581134, 30.3389581134)
                Line((0, -0.28575), (0, -0.508))
                CenterArc((0, 0), 0.28575, -167.2187493585, 77.2187493585)
                Line((-0.2786696297, -0.0632162953), (-0.2565982019, -0.4384305678))
            make_face()
            # Profile area: 0.0627035782, perimeter: 1.0668883979
            with BuildLine():
                Line((-0.3189430517, 0.6214318786), (-0.3062307636, 0.4053229816))
                CenterArc((0, 0), 0.508, 90, 37.0718794403)
                Line((0, 0.508), (0, 0.6985))
                CenterArc((0, 0), 0.6985, 90, 27.1686615271)
            make_face()
            # Profile area: 0.0662795996, perimeter: 1.2522177405
            with BuildLine():
                CenterArc((0, 0), 0.508, -90, 30.3389581134)
                Line((0.2565982019, -0.4384305678), (0.2786696297, -0.0632162953))
                CenterArc((0, 0), 0.28575, -90, 77.2187493585)
                Line((0, -0.28575), (0, -0.508))
            make_face()
            # Profile area: 0.1543847639, perimeter: 1.8979490906
            with BuildLine():
                Line((0, -0.84455), (0, -1.5621))
                CenterArc((0, 0), 0.84455, -106.1324134161, 16.1324134161)
                Line((-0.2346650936, -0.8112934095), (-0.1905, -1.5621))
                Line((-0.1905, -1.5621), (0, -1.5621))
            make_face()
            # Profile area: 0.0627035782, perimeter: 1.0668883979
            with BuildLine():
                CenterArc((0, 0), 0.6985, 62.8313384729, 27.1686615271)
                Line((0, 0.508), (0, 0.6985))
                CenterArc((0, 0), 0.508, 52.9281205597, 37.0718794403)
                Line((0.3062307636, 0.4053229816), (0.3189430517, 0.6214318786))
            make_face()
            # Profile area: 0.1543847639, perimeter: 1.8979490906
            with BuildLine():
                Line((0, -1.5621), (0.1905, -1.5621))
                Line((0.1905, -1.5621), (0.2346650936, -0.8112934095))
                CenterArc((0, 0), 0.84455, -90, 16.1324134161)
                Line((0, -0.84455), (0, -1.5621))
            make_face()
            # Profile area: 0.0491992428, perimeter: 0.9251105977
            with BuildLine():
                CenterArc((0, 0), 0.6985, -90, 20.4357402002)
                Line((0.2438859138, -0.6545394648), (0.2565982019, -0.4384305678))
                CenterArc((0, 0), 0.508, -90, 30.3389581134)
                Line((0, -0.508), (0, -0.6985))
            make_face()
            # Profile area: 0.0487785465, perimeter: 0.9713305638
            with BuildLine():
                Line((-0.328163872, 0.7781858233), (-0.3189430517, 0.6214318786))
                CenterArc((0, 0), 0.6985, 90, 27.1686615271)
                Line((0, 0.6985), (0, 0.84455))
                CenterArc((0, 0), 0.84455, 90, 22.865334743)
            make_face()
            # Profile area: 0.0487785465, perimeter: 0.9713305638
            with BuildLine():
                Line((0, 0.6985), (0, 0.84455))
                CenterArc((0, 0), 0.6985, 62.8313384729, 27.1686615271)
                Line((0.3189430517, 0.6214318786), (0.328163872, 0.7781858233))
                CenterArc((0, 0), 0.84455, 67.134665257, 22.865334743)
            make_face()
            # Profile area: 0.0479126176, perimeter: 1.0087489452
            with BuildLine():
                Line((-0.3735294118, 1.5494), (0, 1.5494))
                Line((0, 1.5494), (0, 1.6764))
                Line((-0.381, 1.6764), (0, 1.6764))
                Line((-0.381, 1.6764), (-0.3735294118, 1.5494))
            make_face()
            # Profile area: 0.2559409509, perimeter: 2.1879658254
            with BuildLine():
                Line((-0.3735294118, 1.5494), (-0.328163872, 0.7781858233))
                CenterArc((0, 0), 0.84455, 90, 22.865334743)
                Line((0, 0.84455), (0, 1.5494))
                Line((-0.3735294118, 1.5494), (0, 1.5494))
            make_face()
            # Profile area: 0.0479126176, perimeter: 1.0087489452
            with BuildLine():
                Line((0, 1.5494), (0, 1.6764))
                Line((0, 1.5494), (0.3735294118, 1.5494))
                Line((0.3735294118, 1.5494), (0.381, 1.6764))
                Line((0, 1.6764), (0.381, 1.6764))
            make_face()
            # Profile area: 0.0491992428, perimeter: 0.9251105977
            with BuildLine():
                CenterArc((0, 0), 0.6985, -110.4357402002, 20.4357402002)
                Line((0, -0.508), (0, -0.6985))
                CenterArc((0, 0), 0.508, -120.3389581134, 30.3389581134)
                Line((-0.2565982019, -0.4384305678), (-0.2438859138, -0.6545394648))
            make_face()
            # Profile area: 0.0355371902, perimeter: 0.7900042193
            with BuildLine():
                CenterArc((0, 0), 0.84455, -106.1324134161, 16.1324134161)
                Line((0, -0.6985), (0, -0.84455))
                CenterArc((0, 0), 0.6985, -110.4357402002, 20.4357402002)
                Line((-0.2438859138, -0.6545394648), (-0.2346650936, -0.8112934095))
            make_face()
            # Profile area: 0.0355371902, perimeter: 0.7900042193
            with BuildLine():
                Line((0.2346650936, -0.8112934095), (0.2438859138, -0.6545394648))
                CenterArc((0, 0), 0.6985, -90, 20.4357402002)
                Line((0, -0.6985), (0, -0.84455))
                CenterArc((0, 0), 0.84455, -90, 16.1324134161)
            make_face()
            # Profile area: 0.2559409509, perimeter: 2.1879658254
            with BuildLine():
                Line((0, 1.5494), (0.3735294118, 1.5494))
                Line((0, 0.84455), (0, 1.5494))
                CenterArc((0, 0), 0.84455, 67.134665257, 22.865334743)
                Line((0.328163872, 0.7781858233), (0.3735294118, 1.5494))
            make_face()
        # OneSide extrude, distance=1.4859
        extrude(amount=1.4859)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0060943344, perimeter: 0.7697283756
            with BuildLine():
                CenterArc((0, 0), 0.508, 48.4160129384, 4.5121076213)
                Line((0.2841593358, 0.0301087091), (0.3062307636, 0.4053229816))
                Line((0.3371683342, 0.3799756761), (0.2841593358, 0.0301087091))
            make_face()
            # Profile area: 0.0093496905, perimeter: 0.5297964527
            with BuildLine():
                CenterArc((0, 0), 0.6985, 58.0707817335, 4.7605567395)
                Line((0.3062307636, 0.4053229816), (0.3189430517, 0.6214318786))
                CenterArc((0, 0), 0.508, 48.4160129384, 4.5121076213)
                Line((0.3694165355, 0.5928184151), (0.3371683342, 0.3799756761))
            make_face()
            # Profile area: 0.0820625473, perimeter: 1.7958977058
            with BuildLine():
                CenterArc((0, 0), 0.84455, 112.865334743, 4.8566378879)
                Line((-0.3735294118, 1.5494), (-0.328163872, 0.7781858233))
                Line((-0.51435, 1.5494), (-0.3735294118, 1.5494))
                Line((-0.51435, 1.5494), (-0.3928690826, 0.7476085784))
            make_face()
            # Profile area: 0.0820625473, perimeter: 1.7958977058
            with BuildLine():
                Line((0.328163872, 0.7781858233), (0.3735294118, 1.5494))
                CenterArc((0, 0), 0.84455, 62.2780273692, 4.8566378879)
                Line((0.51435, 1.5494), (0.3928690826, 0.7476085784))
                Line((0.3735294118, 1.5494), (0.51435, 1.5494))
            make_face()
            # Profile area: 0.0094671744, perimeter: 0.4432059125
            with BuildLine():
                CenterArc((0, 0), 0.84455, 62.2780273692, 4.8566378879)
                Line((0.3189430517, 0.6214318786), (0.328163872, 0.7781858233))
                CenterArc((0, 0), 0.6985, 58.0707817335, 4.7605567395)
                Line((0.3928690826, 0.7476085784), (0.3694165355, 0.5928184151))
            make_face()
            # Profile area: 0.0060943344, perimeter: 0.7697283756
            with BuildLine():
                Line((-0.3371683342, 0.3799756761), (-0.2841593358, 0.0301087091))
                Line((-0.3062307636, 0.4053229816), (-0.2841593358, 0.0301087091))
                CenterArc((0, 0), 0.508, 127.0718794403, 4.5121076213)
            make_face()
            # Profile area: 0.0093496905, perimeter: 0.5297964527
            with BuildLine():
                Line((-0.3694165355, 0.5928184151), (-0.3371683342, 0.3799756761))
                CenterArc((0, 0), 0.508, 127.0718794403, 4.5121076213)
                Line((-0.3189430517, 0.6214318786), (-0.3062307636, 0.4053229816))
                CenterArc((0, 0), 0.6985, 117.1686615271, 4.7605567395)
            make_face()
            # Profile area: 0.0094671744, perimeter: 0.4432059125
            with BuildLine():
                Line((-0.3928690826, 0.7476085784), (-0.3694165355, 0.5928184151))
                CenterArc((0, 0), 0.6985, 117.1686615271, 4.7605567395)
                Line((-0.328163872, 0.7781858233), (-0.3189430517, 0.6214318786))
                CenterArc((0, 0), 0.84455, 112.865334743, 4.8566378879)
            make_face()
        # OneSide extrude, distance=1.3652
        extrude(amount=1.3652, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical gear or pulley with a flat face and radial teeth or grooves around its outer edge, featuring a smooth circular hub on one side and a textured toothed rim on the other.
def model_110506_6f8424d2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.6941366846, perimeter: 45.5530934771
            with BuildLine():
                CenterArc((7, 5), 3.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7, 5), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with Locations((7, 5)):
                Circle(3.5)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with Locations((7, 5)):
                Circle(3.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a lathe tool holder or insert block with a rectangular body featuring multiple rectangular slots or pockets on the top surface and a pointed cutting edge at one end, designed to hold and position cutting inserts for machining operations.
def model_110783_5d025c90_0002():
    """Model: B_TremoloSadle v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6223254213, perimeter: 6.2430553805
            with BuildLine():
                Line((0.1, 0.99), (0.1, 0.2879215656))
                CenterArc((0, -0.1199999973), 0.4200000018, -90, 166.2258530618)
                Line((0, -0.5399999991), (0, -0.99))
                Line((0, -0.99), (0.525, -0.99))
                Line((0.525, -0.99), (0.525, 0.99))
                Line((0.525, 0.99), (0.1, 0.99))
            make_face()
            with BuildLine():
                CenterArc((0.3411906168, 0.7682824979), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6223254213, perimeter: 6.2430553805
            with BuildLine():
                Line((0, -0.5399999991), (0, -0.99))
                CenterArc((0, -0.1199999973), 0.4200000018, 103.7741469382, 166.2258530618)
                Line((-0.1, 0.99), (-0.1, 0.2879215656))
                Line((-0.1, 0.99), (-0.525, 0.99))
                Line((-0.525, 0.99), (-0.525, -0.99))
                Line((-0.525, -0.99), (0, -0.99))
            make_face()
            with BuildLine():
                CenterArc((-0.3411906168, 0.7682824979), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0694002696, perimeter: 1.593048201
            with BuildLine():
                Line((0, 0.99), (0, 0.3000000045))
                CenterArc((0, -0.1199999973), 0.4200000018, 76.2258530618, 13.7741469382)
                Line((0.1, 0.99), (0.1, 0.2879215656))
                Line((0.1, 0.99), (0, 0.99))
            make_face()
            # Profile area: 0.0694002696, perimeter: 1.593048201
            with BuildLine():
                Line((0, 0.99), (-0.1, 0.99))
                Line((-0.1, 0.99), (-0.1, 0.2879215656))
                CenterArc((0, -0.1199999973), 0.4200000018, 90, 13.7741469382)
                Line((0, 0.99), (0, 0.3000000045))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a toroidal (donut-shaped) component with a large central hole and a rounded, cylindrical cross-section, featuring a smooth, curved geometry typical of a ring or bushing part.
def model_111313_a904bb4b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.638937829, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((-1.8624104969, 1.7428458211), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.8624104969, 1.7428458211), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a cylindrical roller or drum with rounded ends and a hollowed-out interior core, featuring a smooth curved outer surface and concentric internal structure.
def model_111493_9c64d90b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 3.0574309968, perimeter: 6.1984523095
            Circle(0.9865143246)
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


# Description: This is a flat, parallelogram-shaped panel or cover with a curved flange on one end and a triangulated mesh internal structure, featuring a slightly raised edge lip around its perimeter.
def model_111872_8817499c_0001():
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
        # Sketch on YZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6338478254, perimeter: 6.2708327677
            with BuildLine():
                Line((-0.3810000122, 0.1270000041), (0, 0.1270000041))
                Line((-0.3810000122, 0.6350000203), (-0.3810000122, 0.1270000041))
                Line((-0.6350000203, 0.6350000203), (-0.3810000122, 0.6350000203))
                _nurbs_edge([(-2.5400000811, -0.5080000162), (-2.5535429544, -0.5018734426), (-2.5758270951, -0.4886074403), (-2.5948475837, -0.4656695838), (-2.5912870443, -0.4289857539), (-2.5392679337, -0.3732267579), (-2.4429629947, -0.3086602729), (-2.3095659041, -0.237578395), (-2.1487509547, -0.162976813), (-1.9716515018, -0.0881876231), (-1.7897298124, -0.0164706323), (-1.6137544533, 0.0493632438), (-1.4526692182, 0.1073789083), (-1.3126315787, 0.156874524), (-1.1955424519, 0.1989623684), (-1.0993882212, 0.2363560893), (-1.0198114419, 0.2726212291), (-0.9513003076, 0.3115791492), (-0.8883911468, 0.3567151503), (-0.82709052, 0.4104373586), (-0.765139617, 0.4740060463), (-0.7141494996, 0.5331723911), (-0.6749470962, 0.5822603949), (-0.6483866102, 0.6170723847), (-0.6350000203, 0.6350000203)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0, 0), (-0.0456979311, -0.0045816794), (-0.1350851567, -0.0125168082), (-0.2631402527, -0.0207349123), (-0.4216288512, -0.0242008658), (-0.5999738473, -0.016618759), (-0.7628206884, -0.0002550871), (-0.9209258353, 0.0172437334), (-1.0949245504, 0.0214331016), (-1.3117544409, -0.0065037978), (-1.601170416, -0.0873649669), (-1.9137160419, -0.210454526), (-2.2039372265, -0.3428044178), (-2.4236130174, -0.4498064844), (-2.5400000811, -0.5080000162)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0.1270000041), (0, 0))
            make_face()
        # OneSide extrude, distance=4.572
        extrude(amount=4.572)
    return part.part


# Description: This is a dark blue metal bracket or mounting plate with a trapezoidal overall shape, featuring two rectangular slots or cutouts on its upper surface and angular flanges along its edges for structural reinforcement and assembly.
def model_112099_2c7f567f_0000():
    """Model: v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.4114285714, perimeter: 11.6896309997
            with BuildLine():
                Line((6.2, 3.2), (6.6571428571, 0))
                Line((6.2, 3.2), (3.8, 3.2))
                Line((3.8, 3.2), (3.8, 0))
                Line((3.8, 0), (6.6571428571, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.4285714286, perimeter: 13.5753452854
            with BuildLine():
                Line((10, 0), (10, 3.2))
                Line((10, 3.2), (6.2, 3.2))
                Line((6.2, 3.2), (6.6571428571, 0))
                Line((6.6571428571, 0), (10, 0))
            make_face()
            # Profile area: 8.4114285714, perimeter: 11.6896309997
            with BuildLine():
                Line((6.2, 3.2), (6.6571428571, 0))
                Line((6.2, 3.2), (3.8, 3.2))
                Line((3.8, 3.2), (3.8, 0))
                Line((3.8, 0), (6.6571428571, 0))
            make_face()
            # Profile area: 12.16, perimeter: 14
            with BuildLine():
                Line((3.8, 3.2), (3.8, 0))
                Line((3.8, 3.2), (0, 3.2))
                Line((0, 3.2), (0, 0))
                Line((0, 0), (3.8, 0))
            make_face()
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45, mode=Mode.ADD)
    return part.part


# Description: This is a rounded rectangular bar or spacer with a dark gray finish, featuring two small blue slot or groove details near each end, and fully rounded corners and edges.
def model_112738_1107ad1c_0002():
    """Model: Plunger"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring a slight taper or rounded end at the top and a tapered or pointed end at the bottom.
def model_113001_c1b164a3_0001():
    """Model: Antenna v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a toroidal (donut-shaped) ring with a hollow center and textured surface finish, featuring a smooth, continuous curved profile without any holes, slots, or flanges.
def model_113191_87565693_0001():
    """Model: Cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.127), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7228804696, perimeter: 11.1212379937
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.82, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a grooved elastic band or pulley belt with a circular ring shape and parallel ribbed grooves running circumferentially around its surface for grip and traction.
def model_113935_329e18e4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4818581963, perimeter: 49.6371639267
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.2
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a flat, trapezoidal plate or base component with a shallow depth, featuring diagonal internal ribs or reinforcement patterns on its upper surface and a recessed dark edge or flange around its perimeter.
def model_114110_e6175b0c_0000():
    """Model: base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 44.7853981634, perimeter: 27.1415926536
            with BuildLine():
                CenterArc((-4, -2), 0.5, 180, 90)
                Line((-4, -2.5), (4, -2.5))
                CenterArc((4, -2), 0.5, -90, 90)
                Line((4.5, -2), (4.5, 2))
                CenterArc((4, 2), 0.5, 0, 90)
                Line((4, 2.5), (-4, 2.5))
                CenterArc((-4, 2), 0.5, 90, 90)
                Line((-4.5, 2), (-4.5, -2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a flat, parallelogram-shaped plate or panel with a dark blue-gray color, featuring a simple rectangular form with no holes, slots, or other distinctive features—appearing to be a basic structural or cover component.
def model_114111_59282658_0003():
    """Model: Drawer Front"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 29.21), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 773.7920008, perimeter: 122.60072
            with BuildLine():
                Line((0, 0), (-43.52036, 0))
                Line((0, 17.78), (0, 0))
                Line((-43.52036, 17.78), (0, 17.78))
                Line((-43.52036, 0), (-43.52036, 17.78))
            make_face()
            # Profile area: 22.5806, perimeter: 38.1
            with BuildLine():
                Line((-43.52036, 0), (-43.52036, 17.78))
                Line((-44.79036, 17.78), (-43.52036, 17.78))
                Line((-44.79036, 0), (-44.79036, 17.78))
                Line((-43.52036, 0), (-44.79036, 0))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


# Description: This is a dark gray composite panel or trim piece with an elongated, angled rectangular shape featuring a large curved cutout on the upper surface and small rectangular notches or slots along the edges, typical of an automotive interior or exterior trim component.
def model_114345_228b4786_0001():
    """Model: Contacto_Cobre v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0684140004, perimeter: 12.1532685854
            with BuildLine():
                Line((0.1330041249, -0.0000879292), (2.0033332641, -0.0000879292))
                Line((2.0033332641, -0.0000879292), (2.0199999548, 0.0470525144))
                Line((2.0199999548, 0.0470525144), (2.1699999548, 0.0470525144))
                Line((2.1699999548, 0.0470525144), (2.1999999982, 0.1319053128))
                Line((2.1999999982, 0.1319053128), (2.1999999982, 0.4851471889))
                Line((2.1699999548, 0.5699999873), (2.1999999982, 0.4851471889))
                Line((2.0199999548, 0.5699999873), (2.1699999548, 0.5699999873))
                Line((2.0033332641, 0.6171404308), (2.0199999548, 0.5699999873))
                Line((2.0033332641, 0.6171404308), (0.1330041249, 0.6171404308))
                Line((0.1330041249, 0.6171404308), (0.0999708058, 0.5670525098))
                Line((0.0999708058, 0.5670525098), (-0.0000291957, 0.5670525098))
                Line((-0.0000291957, 0.5670525098), (-0.0000291957, 0.0499999918))
                Line((0.0999708058, 0.0499999918), (-0.0000291957, 0.0499999918))
                Line((0.1330041249, -0.0000879292), (0.0999708058, 0.0499999918))
            make_face()
            with BuildLine():
                Line((0.4999708043, 0.4585262508), (1.3999708043, 0.4585262508))
                Line((1.3999708043, 0.6000000089), (1.3999708043, 0.4585262508))
                Line((1.3999708043, 0.6000000089), (1.6999708043, 0.6000000089))
                Line((1.6999708043, 0.6000000089), (1.6999708043, 0.5727797781))
                Line((1.6999708043, 0.5727797781), (1.7808101791, 0.513915566))
                Line((1.7808101791, 0.513915566), (1.8426473111, 0.513915566))
                CenterArc((1.8777180788, 0.4972147638), 0.0388442472, -84.8677064876, 239.4037798683)
                Line((1.8788987309, 0.4585262508), (1.8811929173, 0.4585262508))
                Line((0.7000000104, 0.400000006), (1.8788987309, 0.4585262508))
                Line((0.7000000104, 0.400000006), (0.7000000104, 0.2170524957))
                Line((1.8811929173, 0.1585262508), (0.7000000104, 0.2170524957))
                CenterArc((1.8777180788, 0.1198377379), 0.0388442472, -154.5360733807, 239.4037798683)
                Line((1.7808101791, 0.1031369356), (1.8426473111, 0.1031369356))
                Line((1.6999708043, 0.0442727235), (1.7808101791, 0.1031369356))
                Line((1.6999708043, 0.0170524927), (1.6999708043, 0.0442727235))
                Line((1.3999708043, 0.0170524927), (1.6999708043, 0.0170524927))
                Line((1.3999708043, 0.1585262508), (1.3999708043, 0.0170524927))
                Line((0.4999708043, 0.1585262508), (1.3999708043, 0.1585262508))
                Line((0.4999708043, 0.4585262508), (0.4999708043, 0.1585262508))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0513953968, 0.3085262508), 0.065, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.013273229, perimeter: 0.408407045
            with Locations((2.0513953968, 0.3085262508)):
                Circle(0.065)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.013273229, perimeter: 0.408407045
            with Locations((2.0513953968, 0.3085262508)):
                Circle(0.065)
        # TwoSides extrude, along=0.07, against=-0.0180788314
        extrude(amount=0.07, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.0180788314, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular duct or channel component with a elongated box shape, featuring two circular mounting holes or ports on opposite sides and a central slot or groove running along its length.
def model_115330_1c326f55_0001():
    """Model: naamplaat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.8330198321, perimeter: 14.1234081882
            with BuildLine():
                CenterArc((4.7042930727, 1.4704223961), 0.3, 9.7046615429, 80.2953384571)
                Line((4.7042930727, 2.1704223961), (4.7042930727, 1.7704223961))
                CenterArc((4.6042930727, 2.1704223961), 0.1, 0, 90)
                Line((0.6042930727, 2.2704223961), (4.6042930727, 2.2704223961))
                CenterArc((0.6042930727, 2.1704223961), 0.1, 90, 90)
                Line((0.5042930727, 1.7704223961), (0.5042930727, 2.1704223961))
                CenterArc((0.5042930727, 1.4704223961), 0.3, 90, 180)
                Line((0.5042930727, 0.7704223961), (0.5042930727, 1.1704223961))
                CenterArc((0.6042930727, 0.7704223961), 0.1, 180, 90)
                Line((4.6042930727, 0.6704223961), (0.6042930727, 0.6704223961))
                CenterArc((4.6042930727, 0.7704223961), 0.1, -90, 90)
                Line((4.7042930727, 1.1704223961), (4.7042930727, 0.7704223961))
                CenterArc((4.7042930727, 1.4704223961), 0.3, -90, 80.2953384571)
                Line((5, 1.4198515236), (5, 1.5209932687))
            make_face()
            with BuildLine():
                CenterArc((0.5042930727, 1.4704223961), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7042930727, 1.4704223961), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a pipe elbow or angle connector with a 90-degree bend, featuring a cylindrical shaft with a curved junction that transitions to a horizontal outlet, commonly used in plumbing, HVAC, or fluid transfer applications.
def model_115430_bb9dd4dc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1700000051, perimeter: 3.4283185844
            with BuildLine():
                Line((-2.2000000328, 0.3000000075), (-2.2000000328, -0.400000006))
                CenterArc((-2.0000000328, 0.3000000075), 0.2, 90, 90)
                Line((-1.5000000224, 0.5000000075), (-2.0000000328, 0.5000000075))
                Line((-1.5000000224, 0.5000000075), (-1.5000000224, 0.6000000089))
                Line((-1.5000000224, 0.6000000089), (-2.1000000343, 0.6000000089))
                CenterArc((-2.1000000343, 0.4000000089), 0.2, 90, 90)
                Line((-2.3000000343, 0.4000000089), (-2.3000000343, -0.400000006))
                Line((-2.2000000328, -0.400000006), (-2.3000000343, -0.400000006))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a rectangular box or enclosure with a sloped, triangular roof-like top section featuring internal ribbing and structural bracing, resembling a compact housing or protective cover component.
def model_115518_3e1d2cc3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6453889135, perimeter: 10.6074199379
            with BuildLine():
                Line((-7, 4.5), (-3.5, 4.5))
                Line((-3.5, 4.5), (-3, 4.5))
                Line((-3, 4.5), (-5.25, 6.5646172949))
                Line((-7.5, 4.5), (-5.25, 6.5646172949))
                Line((-7.5, 4.5), (-7, 4.5))
            make_face()
            # Profile area: 9, perimeter: 18
            with BuildLine():
                Line((-7, 4.5), (-7, 1.5))
                Line((-7, 1.5), (-3.5, 1.5))
                Line((-3.5, 1.5), (-3.5, 4.5))
                Line((-7, 4.5), (-3.5, 4.5))
            make_face()
            with BuildLine():
                Line((-6, 3.5), (-4.5, 3.5))
                Line((-4.5, 3.5), (-4.5, 2.5))
                Line((-6, 2.5), (-4.5, 2.5))
                Line((-6, 3.5), (-6, 2.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((-6, 3.5), (-6, 2.5))
                Line((-6, 2.5), (-4.5, 2.5))
                Line((-4.5, 3.5), (-4.5, 2.5))
                Line((-6, 3.5), (-4.5, 3.5))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


# Description: This is a small boat or canoe with a pointed bow, featuring a blue hull with internal ribbing/structural bracing, a black stem/prow detail, and a tapered triangular profile when viewed from above.
def model_115518_a1bf907b_0000():
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
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0660595118, perimeter: 0.995000963
            with BuildLine():
                CenterArc((-4.7917066607, 4.336946794), 0.2866062019, 48.0189324485, 58.0567471116)
                Line((-4.9171406295, 4.5990693109), (-4.8710698683, 4.6123457705))
                Line((-4.8547030309, 4.3824040413), (-4.9171406295, 4.5990693109))
                Line((-4.6465209589, 4.336946794), (-4.8547030309, 4.3824040413))
                Line((-4.6000000685, 4.5500000678), (-4.6465209589, 4.336946794))
            make_face()
            # Profile area: 0.0087015851, perimeter: 0.4746034133
            with BuildLine():
                Line((-4.6544925402, 4.3004390773), (-4.8429406654, 4.3415873517))
                _nurbs_edge([(-4.824999107, 4.2793281895), (-4.8254388191, 4.2833987083), (-4.8265905545, 4.2932418165), (-4.8286321414, 4.3075004713), (-4.831864461, 4.3235022277), (-4.8356664453, 4.3341942139), (-4.8391568848, 4.3393056045), (-4.8416514682, 4.341096274), (-4.8429406654, 4.3415873517)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-4.824999107, 3.8411357035), 0.438192486, 68.6757964801, 21.3242035199)
                Line((-4.6544925402, 4.3004390773), (-4.6656526997, 4.2493285223))
            make_face()
            # Profile area: 5.6497240997, perimeter: 10.7972267372
            with BuildLine():
                CenterArc((-4.824999107, 3.8411357035), 0.438192486, 68.6757964801, 21.3242035199)
                _nurbs_edge([(-4.8669032199, 4.2773199537), (-4.866797812, 4.2752763829), (-4.8662705285, 4.2652683428), (-4.8652283605, 4.2472571888), (-4.8635579136, 4.2217147084), (-4.8613525143, 4.1907321052), (-4.8593240267, 4.1590837999), (-4.8584640034, 4.1309031954), (-4.8593099187, 4.1033028425), (-4.8622470677, 4.0728064767), (-4.8674188476, 4.0363878315), (-4.8746532948, 3.992392647), (-4.8833455951, 3.9417884489), (-4.8924930286, 3.8882478651), (-4.900905081, 3.8368893372), (-4.9073670698, 3.7933742155), (-4.9108221924, 3.7628633036), (-4.9105467619, 3.7490296787), (-4.9063285546, 3.753047655), (-4.8986496966, 3.7725621527), (-4.8884571023, 3.8030099547), (-4.8769192477, 3.8390315674), (-4.8652067744, 3.875723937), (-4.8542216287, 3.9102484417), (-4.844511808, 3.9421602209), (-4.8363728741, 3.9724469104), (-4.829897591, 4.0029278376), (-4.8250463699, 4.0354987917), (-4.8217065087, 4.0714713774), (-4.8197597902, 4.1107972764), (-4.8190908482, 4.1523380962), (-4.8195899841, 4.1942430468), (-4.8209495213, 4.228961581), (-4.8225427104, 4.253378702), (-4.8239123416, 4.2689352236), (-4.8247766709, 4.2772690449), (-4.824999107, 4.2793281895)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1435774952, 0.1435774952, 0.1435774952, 0.1435774952, 0.1435774952, 0.1435774952, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777], 5)
                CenterArc((-4.824999107, 3.8411357035), 0.438192486, 95.4875504302, 42.3872578511)
                Line((-6.9000001028, 2.2000000328), (-5.149998147, 4.1350545338))
                CenterArc((-5.149998147, 1.6000000238), 1.850001853, 161.0753749669, 18.9246250331)
                Line((-7, 1.5), (-7, 1.6000000238))
                Line((-7, 1.5), (-4, 1.5))
                CenterArc((-5.5615495055, 1.9499999145), 1.6250959298, -16.0756719709, 32.151351531)
                Line((-4.5000000671, 4.1350545338), (-4.0000000596, 2.4000000358))
                CenterArc((-4.824999107, 3.8411357035), 0.438192486, 42.1251917187, 26.5506047614)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0075852229, perimeter: 0.4858210037
            with BuildLine():
                Line((-4.6465209589, 4.336946794), (-4.8547030309, 4.3824040413))
                Line((-4.8429406654, 4.3415873517), (-4.8547030309, 4.3824040413))
                Line((-4.6544925402, 4.3004390773), (-4.8429406654, 4.3415873517))
                Line((-4.6465209589, 4.336946794), (-4.6544925402, 4.3004390773))
            make_face()
            # Profile area: 0.0184136639, perimeter: 1.111238328
            with BuildLine():
                _nurbs_edge([(-4.8669032199, 4.2773199537), (-4.866797812, 4.2752763829), (-4.8662705285, 4.2652683428), (-4.8652283605, 4.2472571888), (-4.8635579136, 4.2217147084), (-4.8613525143, 4.1907321052), (-4.8593240267, 4.1590837999), (-4.8584640034, 4.1309031954), (-4.8593099187, 4.1033028425), (-4.8622470677, 4.0728064767), (-4.8674188476, 4.0363878315), (-4.8746532948, 3.992392647), (-4.8833455951, 3.9417884489), (-4.8924930286, 3.8882478651), (-4.900905081, 3.8368893372), (-4.9073670698, 3.7933742155), (-4.9108221924, 3.7628633036), (-4.9105467619, 3.7490296787), (-4.9063285546, 3.753047655), (-4.8986496966, 3.7725621527), (-4.8884571023, 3.8030099547), (-4.8769192477, 3.8390315674), (-4.8652067744, 3.875723937), (-4.8542216287, 3.9102484417), (-4.844511808, 3.9421602209), (-4.8363728741, 3.9724469104), (-4.829897591, 4.0029278376), (-4.8250463699, 4.0354987917), (-4.8217065087, 4.0714713774), (-4.8197597902, 4.1107972764), (-4.8190908482, 4.1523380962), (-4.8195899841, 4.1942430468), (-4.8209495213, 4.228961581), (-4.8225427104, 4.253378702), (-4.8239123416, 4.2689352236), (-4.8247766709, 4.2772690449), (-4.824999107, 4.2793281895)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1435774952, 0.1435774952, 0.1435774952, 0.1435774952, 0.1435774952, 0.1435774952, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777, 0.9083982777], 5)
                CenterArc((-4.824999107, 3.8411357035), 0.438192486, 90, 5.4875504302)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a protective car cover with a low-poly geometric design, featuring a draped fabric-like form that conforms to a sedan's silhouette, complete with cutouts for wheels and a triangulated surface pattern suggesting fabric folds and tension.
def model_115518_ce8600fe_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4974959235, perimeter: 2.7846909224
            with BuildLine():
                Line((-1.4000000209, 1.5000000224), (-0.3945952306, 1.5))
                Line((-1.4000000209, 1.4000000209), (-1.4000000209, 1.5000000224))
                CenterArc((-0.8972976257, 1.4000000209), 0.5027023951, 180, 180)
                Line((-0.3945952306, 1.5), (-0.3945952306, 1.4000000209))
            make_face()
            # Profile area: 0.4926990081, perimeter: 2.7707961542
            with BuildLine():
                CenterArc((-4.5000000298, 1.4000000209), 0.4999999702, 180, 180)
                Line((-4.0000000596, 1.4000000209), (-4.0000000596, 1.5000000224))
                Line((-5, 1.5), (-4.0000000596, 1.5000000224))
                Line((-5, 1.5), (-5, 1.4000000209))
            make_face()
            # Profile area: 12.4720938254, perimeter: 16.7159854274
            with BuildLine():
                Line((-5, 1.5), (-4.0000000596, 1.5000000224))
                Line((-4.0000000596, 1.5000000224), (-1.4000000209, 1.5000000224))
                Line((-1.4000000209, 1.5000000224), (-0.3945952306, 1.5))
                Line((-0.3945952306, 1.5), (0.5, 1.5))
                Line((0.5, 1.5), (0.5, 3))
                Line((0.5, 3), (-0.5, 3))
                Line((-0.5, 3), (-2, 4))
                Line((-2, 4), (-3.5, 4))
                Line((-3.5, 4), (-4.5, 3))
                Line((-4.5, 3), (-6.111689584, 2.7574712399))
                Line((-6.111689584, 2.7574712399), (-6.111689584, 1.7000000253))
                Line((-6.111689584, 1.7000000253), (-6.111689584, 1.5000000224))
                Line((-6.111689584, 1.5000000224), (-5, 1.5))
            make_face()
            # Profile area: 0.0388310519, perimeter: 1.0251000024
            with BuildLine():
                Line((-6.111689584, 1.7000000253), (-6.111689584, 1.5000000224))
                Line((-6.5000000969, 1.7000000253), (-6.111689584, 1.7000000253))
                Line((-6.111689584, 1.5000000224), (-6.5000000969, 1.7000000253))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a flat parallelogram or trapezoidal plate with a uniform thickness, featuring a simple geometric form with no holes, slots, or curves—essentially a basic extruded quadrilateral prism used as a structural or mounting component.
def model_115524_4490925e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 262 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.4035171413, perimeter: 79.1966483369
            with BuildLine():
                Line((9.3587452964, 7.7153817426), (9.7753870362, 8.3000001535))
                Line((9.3000001386, 7.5000001118), (9.3587452964, 7.7153817426))
                Line((9.1868152376, 7.2780477056), (9.3000001386, 7.5000001118))
                Line((9.0957848004, 6.9442962144), (9.1868152376, 7.2780477056))
                Line((8.8462201865, 6.5442431419), (9.0957848004, 6.9442962144))
                Line((8.7484831872, 6.185902896), (8.8462201865, 6.5442431419))
                Line((8.5000001267, 6.0000000894), (8.7484831872, 6.185902896))
                Line((8.4215224675, 5.7122717582), (8.5000001267, 6.0000000894))
                Line((8.3000001237, 5.5621775499), (8.4215224675, 5.7122717582))
                Line((8.1447517322, 5.5621775499), (8.3000001237, 5.5621775499))
                Line((8.0306265217, 5.3708072733), (8.1447517322, 5.5621775499))
                Line((8.1895033436, 5.1369102685), (8.0306265217, 5.3708072733))
                Line((8.0306265217, 5.0810614522), (8.1895033436, 5.1369102685))
                Line((7.8923526554, 4.9102771681), (8.0306265217, 5.0810614522))
                Line((8.0306265217, 4.7983250514), (7.8923526554, 4.9102771681))
                Line((8.1895033436, 4.6696919483), (8.0306265217, 4.7983250514))
                Line((8.1000001207, 4.5591450729), (8.1895033436, 4.6696919483))
                Line((7.9612529226, 4.5591450729), (8.1000001207, 4.5591450729))
                Line((7.802054368, 4.3625163684), (7.9612529226, 4.5591450729))
                Line((7.8792692646, 4.3000000641), (7.802054368, 4.3625163684))
                Line((7.8792692646, 4.1297646952), (7.8792692646, 4.3000000641))
                Line((7.7248394714, 4.2000000626), (7.8792692646, 4.1297646952))
                Line((7.7248394714, 4.0199185973), (7.7248394714, 4.2000000626))
                Line((7.546784523, 3.8000000566), (7.7248394714, 4.0199185973))
                Line((7.546784523, 3.5737716706), (7.546784523, 3.8000000566))
                Line((7.7874197942, 3.5737716706), (7.546784523, 3.5737716706))
                Line((7.850000117, 3.3968583089), (7.7874197942, 3.5737716706))
                Line((7.7248394714, 3.3051112885), (7.850000117, 3.3968583089))
                Line((7.3687295747, 2.8652742071), (7.7248394714, 3.3051112885))
                Line((7.4912054158, 2.5190373738), (7.3687295747, 2.8652742071))
                Line((7.6963807538, 2.4257227035), (7.4912054158, 2.5190373738))
                Line((8.0000001192, 1.9104324729), (7.6963807538, 2.4257227035))
                Line((7.7874197942, 1.9104324729), (8.0000001192, 1.9104324729))
                Line((7.6053417133, 1.5100888653), (7.7874197942, 1.9104324729))
                Line((7.2000001073, 1.6000000238), (7.6053417133, 1.5100888653))
                Line((7.2374590376, 1.2582357672), (7.2000001073, 1.6000000238))
                Line((7.5000001118, 1.2000000179), (7.2374590376, 1.2582357672))
                Line((7.5789779717, 1.2582357672), (7.5000001118, 1.2000000179))
                Line((7.7248394714, 1.2582357672), (7.5789779717, 1.2582357672))
                Line((7.8764262992, 0.9781481296), (7.7248394714, 1.2582357672))
                Line((7.850000117, 0.8000000119), (7.8764262992, 0.9781481296))
                Line((7.7248394714, 0.9013351345), (7.850000117, 0.8000000119))
                Line((7.4858439553, 0.9858835828), (7.7248394714, 0.9013351345))
                Line((7.4773116133, 0.9704126763), (7.4858439553, 0.9858835828))
                Line((7.5789779717, 0.7124086687), (7.4773116133, 0.9704126763))
                Line((7.7862560766, 0.5980929567), (7.5789779717, 0.7124086687))
                Line((7.720079461, 0.4781010219), (7.7862560766, 0.5980929567))
                Line((7.6785584292, 0.336311926), (7.720079461, 0.4781010219))
                Line((7.6121714576, 0.1096087759), (7.6785584292, 0.336311926))
                Line((7.4658988371, -0.0589139197), (7.6121714576, 0.1096087759))
                Line((7.6121714576, -0.275585957), (7.4658988371, -0.0589139197))
                Line((7.5457844859, -0.3959593111), (7.6121714576, -0.275585957))
                Line((7.6785584292, -0.5163326651), (7.5457844859, -0.3959593111))
                Line((7.5985837281, -0.5468652254), (7.6785584292, -0.5163326651))
                Line((7.4929852437, -0.6351692998), (7.5985837281, -0.5468652254))
                Line((7.3274694799, -0.6547620223), (7.4929852437, -0.6351692998))
                Line((7.1107974426, -0.5312546666), (7.3274694799, -0.6547620223))
                Line((6.9502996372, -0.5624757842), (7.1107974426, -0.5312546666))
                Line((6.7114232871, -0.500033549), (6.9502996372, -0.5624757842))
                Line((6.1839226165, -0.5624757842), (6.7114232871, -0.500033549))
                Line((5.9047956515, -0.7958886825), (6.1839226165, -0.5624757842))
                Line((5.7345665033, -0.816039346), (5.9047956515, -0.7958886825))
                Line((5.3119348631, -0.8660678402), (5.7345665033, -0.816039346))
                Line((4.8838454855, -0.7660108517), (5.3119348631, -0.8660678402))
                Line((4.5109004753, -0.7246861445), (4.8838454855, -0.7660108517))
                Line((3.9000000581, -0.6569944469), (4.5109004753, -0.7246861445))
                Line((3.7147804088, -0.6569944469), (3.9000000581, -0.6569944469))
                Line((3.3808091796, -0.5893027493), (3.7147804088, -0.6569944469))
                Line((3.3000000492, -0.7246861445), (3.3808091796, -0.5893027493))
                Line((2.9284889851, -0.7246861445), (3.3000000492, -0.7246861445))
                Line((2.5585746108, -1.007449536), (2.9284889851, -0.7246861445))
                Line((2.3615072926, -1.007449536), (2.5585746108, -1.007449536))
                Line((2.2503126322, -0.8864909418), (2.3615072926, -1.007449536))
                Line((2.1595191787, -0.8864909418), (2.2503126322, -0.8864909418))
                Line((1.8884398747, -0.7246861445), (2.1595191787, -0.8864909418))
                Line((1.7097372784, -0.8384876327), (1.8884398747, -0.7246861445))
                Line((1.4843342606, -0.7039465996), (1.7097372784, -0.8384876327))
                Line((1.0725221829, -0.6108846563), (1.4843342606, -0.7039465996))
                Line((0.8249335311, -0.8384876327), (1.0725221829, -0.6108846563))
                Line((0.6419892656, -1.006664401), (0.8249335311, -0.8384876327))
                Line((0.3604377058, -0.9430389352), (0.6419892656, -1.006664401))
                Line((0.2450015759, -1.0702898668), (0.3604377058, -0.9430389352))
                Line((-0.0044681331, -1.1132505318), (0.2450015759, -1.0702898668))
                Line((-0.3481105299, -1.273543722), (-0.0044681331, -1.1132505318))
                Line((-0.4642667701, -1.3803236806), (-0.3481105299, -1.273543722))
                Line((-0.5740115222, -1.3992225984), (-0.4642667701, -1.3803236806))
                Line((-0.9203955378, -1.5731446467), (-0.5740115222, -1.3992225984))
                Line((-1.1364903573, -1.7717960135), (-0.9203955378, -1.5731446467))
                Line((-1.1897123463, -1.9794360868), (-1.1364903573, -1.7717960135))
                Line((-1.5471175389, -1.8878265292), (-1.1897123463, -1.9794360868))
                Line((-1.9120176391, -2.0710456443), (-1.5471175389, -1.8878265292))
                Line((-2.3000000343, -2.1000000313), (-1.9120176391, -2.0710456443))
                Line((-2.7000000402, -2.1000000313), (-2.3000000343, -2.1000000313))
                Line((-2.9839624745, -2.2953752624), (-2.7000000402, -2.1000000313))
                Line((-3.2894678527, -2.3479857146), (-2.9839624745, -2.2953752624))
                Line((-3.3819614078, -2.5397795898), (-3.2894678527, -2.3479857146))
                Line((-3.4915628978, -2.5361632607), (-3.3819614078, -2.5397795898))
                Line((-3.6017086251, -2.6098523249), (-3.4915628978, -2.5361632607))
                Line((-3.8434389229, -2.6869349988), (-3.6017086251, -2.6098523249))
                Line((-4.5000000671, -2.8000000417), (-3.8434389229, -2.6869349988))
                Line((-4.7750319293, -2.9840002845), (-4.5000000671, -2.8000000417))
                Line((-5.5545232606, -3.2325635663), (-4.7750319293, -2.9840002845))
                Line((-6.5500000976, -3.5500000529), (-5.5545232606, -3.2325635663))
                Line((-7.234921065, -3.5851632545), (-6.5500000976, -3.5500000529))
                Line((-7.3874449556, -3.6165495401), (-7.234921065, -3.5851632545))
                Line((-7.5500001125, -3.6500000544), (-7.3874449556, -3.6165495401))
                Line((-7.8141397398, -3.7470484053), (-7.5500001125, -3.6500000544))
                Line((-8.0020979767, -3.7089424712), (-7.8141397398, -3.7470484053))
                Line((-8.084248432, -3.7851543393), (-8.0020979767, -3.7089424712))
                Line((-8.5238150358, -3.8438895321), (-8.084248432, -3.7851543393))
                Line((-8.5000001267, -4.3500000648), (-8.5238150358, -3.8438895321))
                Line((-8.6480920622, -4.3804743451), (-8.5000001267, -4.3500000648))
                Line((-8.6848631449, -4.4145872772), (-8.6480920622, -4.3804743451))
                Line((-8.7065084248, -4.4540250008), (-8.6848631449, -4.4145872772))
                Line((-8.9010357385, -4.4145872772), (-8.7065084248, -4.4540250008))
                Line((-8.9945535383, -4.5013447541), (-8.9010357385, -4.4145872772))
                Line((-8.9882841334, -4.6736799797), (-8.9945535383, -4.5013447541))
                Line((-8.9945535383, -4.7046039372), (-8.9882841334, -4.6736799797))
                Line((-9.0936867699, -4.7965709112), (-8.9945535383, -4.7046039372))
                Line((-9.2134798797, -4.7722845142), (-9.0936867699, -4.7965709112))
                Line((-9.3707386216, -4.9181751543), (-9.2134798797, -4.7722845142))
                Line((-9.5906737766, -4.8735863422), (-9.3707386216, -4.9181751543))
                Line((-9.6852561053, -4.9181751543), (-9.5906737766, -4.8735863422))
                Line((-9.8178839599, -4.9806997143), (-9.6852561053, -4.9181751543))
                Line((-9.8178839599, -5.5051920135), (-9.8178839599, -4.9806997143))
                Line((-9.7699903513, -5.5051920135), (-9.8178839599, -5.5051920135))
                Line((-9.6676583519, -5.4334650517), (-9.7699903513, -5.5051920135))
                Line((-9.5500001423, -5.5500000827), (-9.6676583519, -5.4334650517))
                Line((-9.4284539837, -5.670385948), (-9.5500001423, -5.5500000827))
                Line((-9.3409145791, -5.4530147414), (-9.4284539837, -5.670385948))
                Line((-9.4010535598, -5.3672151763), (-9.3409145791, -5.4530147414))
                Line((-9.4200003961, -5.1985883326), (-9.4010535598, -5.3672151763))
                Line((-9.4200003961, -5.1814245813), (-9.4200003961, -5.1985883326))
                Line((-9.2897225419, -5.1814245813), (-9.4200003961, -5.1814245813))
                Line((-9.3138981125, -5.280059729), (-9.2897225419, -5.1814245813))
                Line((-9.2059011451, -5.4695280927), (-9.3138981125, -5.280059729))
                Line((-9.1603336296, -5.7302952577), (-9.2059011451, -5.4695280927))
                Line((-9.1717968397, -5.7770645953), (-9.1603336296, -5.7302952577))
                Line((-9.3626134541, -5.7302952577), (-9.1717968397, -5.7770645953))
                Line((-9.4200003961, -5.8238339328), (-9.3626134541, -5.7302952577))
                Line((-9.6000001431, -5.9500000887), (-9.4200003961, -5.8238339328))
                Line((-9.7353165607, -6.1705610384), (-9.6000001431, -5.9500000887))
                Line((-9.7353165607, -6.214249857), (-9.7353165607, -6.1705610384))
                Line((-9.5100884195, -6.3000000939), (-9.7353165607, -6.214249857))
                Line((-9.5100884195, -6.6001830593), (-9.5100884195, -6.3000000939))
                Line((-9.800000146, -6.8000001013), (-9.5100884195, -6.6001830593))
                Line((-9.800000146, -7.3883116656), (-9.800000146, -6.8000001013))
                Line((-9.800000146, -7.7950055992), (-9.800000146, -7.3883116656))
                Line((-9.6706329754, -7.7950055992), (-9.800000146, -7.7950055992))
                Line((-9.5100884195, -7.3733256925), (-9.6706329754, -7.7950055992))
                Line((-9.2690322103, -7.0181255041), (-9.5100884195, -7.3733256925))
                Line((-9.3403772054, -6.8772655436), (-9.2690322103, -7.0181255041))
                Line((-9.5000001416, -6.8000001013), (-9.3403772054, -6.8772655436))
                Line((-9.3514326126, -6.4941125143), (-9.5000001416, -6.8000001013))
                Line((-9.3293217983, -6.4775046845), (-9.3514326126, -6.4941125143))
                Line((-9.3173722365, -6.447343638), (-9.3293217983, -6.4775046845))
                Line((-9.2412448654, -6.4775046845), (-9.3173722365, -6.447343638))
                Line((-9.1574075608, -6.510720344), (-9.2412448654, -6.4775046845))
                Line((-9.1127742747, -6.5485921767), (-9.1574075608, -6.510720344))
                Line((-9.1000001356, -6.5594311739), (-9.1127742747, -6.5485921767))
                Line((-9.0216941002, -6.5594311739), (-9.1000001356, -6.5594311739))
                Line((-8.9718970389, -6.6016845265), (-9.0216941002, -6.5594311739))
                Line((-8.8704543511, -6.6016845265), (-8.9718970389, -6.6016845265))
                Line((-8.7160861381, -6.4197561615), (-8.8704543511, -6.6016845265))
                Line((-8.7233434745, -6.4022169511), (-8.7160861381, -6.4197561615))
                Line((-8.7495572687, -6.3388646102), (-8.7233434745, -6.4022169511))
                Line((-8.7160861381, -6.2903604155), (-8.7495572687, -6.3388646102))
                Line((-8.7495572687, -6.2465381037), (-8.7160861381, -6.2903604155))
                Line((-8.7160861381, -6.198033909), (-8.7495572687, -6.2465381037))
                Line((-8.6000001281, -6.1500000916), (-8.7160861381, -6.198033909))
                Line((-8.6000001281, -6.0000000894), (-8.6000001281, -6.1500000916))
                Line((-8.5518269109, -5.9301905828), (-8.6000001281, -6.0000000894))
                Line((-8.4222359656, -5.8494372722), (-8.5518269109, -5.9301905828))
                Line((-8.2320650222, -5.7309341374), (-8.4222359656, -5.8494372722))
                Line((-8.0920375185, -5.7309341374), (-8.2320650222, -5.7309341374))
                Line((-8.0984411385, -5.7154581512), (-8.0920375185, -5.7309341374))
                Line((-8.0250623095, -5.6850956186), (-8.0984411385, -5.7154581512))
                Line((-7.8910077095, -5.6296267971), (-8.0250623095, -5.6850956186))
                Line((-7.5676202153, -5.6296267971), (-7.8910077095, -5.6296267971))
                Line((-7.5207650699, -5.5930025706), (-7.5676202153, -5.6296267971))
                Line((-7.4677468394, -5.562735824), (-7.5207650699, -5.5930025706))
                Line((-7.450000111, -5.562735824), (-7.4677468394, -5.562735824))
                Line((-7.355025776, -5.562735824), (-7.450000111, -5.562735824))
                Line((-7.1692451201, -5.528809192), (-7.355025776, -5.562735824))
                Line((-7.1412757565, -5.4703184215), (-7.1692451201, -5.528809192))
                Line((-7.0485735475, -5.4533894591), (-7.1412757565, -5.4703184215))
                Line((-7.0426141881, -5.4332506862), (-7.0485735475, -5.4533894591))
                Line((-7.0156459633, -5.3768535415), (-7.0426141881, -5.4332506862))
                Line((-6.8891579946, -5.3537547385), (-7.0156459633, -5.3768535415))
                Line((-6.8678357714, -5.309164762), (-6.8891579946, -5.3537547385))
                Line((-6.6806915024, -5.2234631809), (-6.8678357714, -5.309164762))
                Line((-6.6806915024, -5.2234631809), (-6.5407705536, -5.1360125879))
                Line((-6.5407705536, -5.1360125879), (-6.5617586959, -5.0652847756))
                Line((-6.425209022, -5.0716709597), (-6.5617586959, -5.0652847756))
                CenterArc((-6.4000000954, -5.1043486543), 0.0412713182, 90, 37.648081673)
                Line((-6.3038966891, -5.0630773361), (-6.4000000954, -5.0630773361))
                Line((-6.3276255918, -5.0457759199), (-6.3038966891, -5.0630773361))
                Line((-6.2801677864, -4.9806875113), (-6.3276255918, -5.0457759199))
                Line((-6.1880609715, -4.9981988916), (-6.2801677864, -4.9806875113))
                Line((-6.2000000924, -4.9631761311), (-6.1880609715, -4.9981988916))
                Line((-6.0853236119, -4.9631761311), (-6.2000000924, -4.9631761311))
                Line((-5.9000000879, -4.900000073), (-6.0853236119, -4.9631761311))
                Line((-5.6127465165, -4.802076464), (-5.9000000879, -4.900000073))
                Line((-5.597616439, -4.7936179462), (-5.6127465165, -4.802076464))
                Line((-5.481675107, -4.728800577), (-5.597616439, -4.7936179462))
                Line((-5.3765514716, -4.6700308754), (-5.481675107, -4.728800577))
                Line((-5.2687815493, -4.6097817587), (-5.3765514716, -4.6700308754))
                Line((-5.1965263794, -4.5098702268), (-5.2687815493, -4.6097817587))
                Line((-5.1675851987, -4.5616384345), (-5.1965263794, -4.5098702268))
                Line((-5.1223219351, -4.5943724417), (-5.1675851987, -4.5616384345))
                Line((-4.9500000738, -4.5943724417), (-5.1223219351, -4.5943724417))
                Line((-4.8598416059, -4.5943724417), (-4.9500000738, -4.5943724417))
                CenterArc((-4.8395368242, -4.5834409254), 0.0230604035, -151.7032424957, 90.9107539268)
                Line((-4.7532804327, -4.5616384345), (-4.8282839446, -4.6035693856))
                Line((-4.70000007, -4.4879645001), (-4.7532804327, -4.5616384345))
                Line((-4.6273515787, -4.4879645001), (-4.70000007, -4.4879645001))
                Line((-4.6273515787, -4.5616384345), (-4.6273515787, -4.4879645001))
                Line((-4.5500000678, -4.70000007), (-4.6273515787, -4.5616384345))
                Line((-4.4542081234, -4.6029164559), (-4.5500000678, -4.70000007))
                Line((-4.4839326062, -4.5203604132), (-4.4542081234, -4.6029164559))
                Line((-4.3939569994, -4.4879645001), (-4.4839326062, -4.5203604132))
                Line((-4.2827962423, -4.5203604132), (-4.3939569994, -4.4879645001))
                Line((-4.0947684019, -4.4784084367), (-4.2827962423, -4.5203604132))
                Line((-3.9574800364, -4.4212188252), (-4.0947684019, -4.4784084367))
                Line((-3.8571822495, -4.4504489103), (-3.9574800364, -4.4212188252))
                Line((-3.7874375073, -4.4213956493), (-3.8571822495, -4.4504489103))
                CenterArc((-3.7783449085, -4.4212188252), 0.0090943181, -178.8859073098, 136.0855417051)
                Line((-3.7000000551, -4.3500000648), (-3.7716721751, -4.4273979231))
                Line((-3.5000000522, -4.2500000633), (-3.7000000551, -4.3500000648))
                Line((-3.4677567156, -4.1653110056), (-3.5000000522, -4.2500000633))
                Line((-3.3593179803, -4.1201391578), (-3.4677567156, -4.1653110056))
                Line((-3.236957828, -4.1360301853), (-3.3593179803, -4.1201391578))
                Line((-3.2396615479, -4.1042481304), (-3.236957828, -4.1360301853))
                Line((-3.2593934062, -4.0859759954), (-3.2396615479, -4.1042481304))
                Line((-3.2199296897, -4.0433596037), (-3.2593934062, -4.0859759954))
                Line((-3.1833063929, -4.0038105471), (-3.2199296897, -4.0433596037))
                Line((-3.1043121943, -3.9185056644), (-3.1833063929, -4.0038105471))
                Line((-2.9955235134, -3.8010260794), (-3.1043121943, -3.9185056644))
                Line((-2.9762843829, -3.8010260794), (-2.9955235134, -3.8010260794))
                Line((-2.8800887306, -3.8010260794), (-2.9762843829, -3.8010260794))
                Line((-2.7644849641, -3.8010260794), (-2.8800887306, -3.8010260794))
                Line((-2.735201902, -3.7694036537), (-2.7644849641, -3.8010260794))
                Line((-2.6609852449, -3.6892579804), (-2.735201902, -3.7694036537))
                Line((-2.530543229, -3.6781611939), (-2.6609852449, -3.6892579804))
                Line((-2.5061482217, -3.6892579804), (-2.530543229, -3.6781611939))
                Line((-2.4558577578, -3.6670644073), (-2.5061482217, -3.6892579804))
                Line((-2.3943301689, -3.600621506), (-2.4558577578, -3.6670644073))
                Line((-2.3239029591, -3.6326573937), (-2.3943301689, -3.600621506))
                Line((-2.2587125171, -3.5622590213), (-2.3239029591, -3.6326573937))
                Line((-2.193522075, -3.5561295371), (-2.2587125171, -3.5622590213))
                CenterArc((-2.1704340196, -3.5175424328), 0.0449669092, -120.8936040003, 36.9420136155)
                Line((-2.0500000305, -3.5500000529), (-2.1656959146, -3.5622590213))
                Line((-2.0018740175, -3.4977423272), (-2.0500000305, -3.5500000529))
                Line((-1.9846362973, -3.4598471846), (-2.0018740175, -3.4977423272))
                Line((-1.854803946, -3.4025511577), (-1.9846362973, -3.4598471846))
                Line((-1.7499090669, -3.4502656785), (-1.854803946, -3.4025511577))
                Line((-1.6417883338, -3.4025511577), (-1.7499090669, -3.4502656785))
                Line((-1.5368934547, -3.4502656785), (-1.6417883338, -3.4025511577))
                Line((-1.5214057538, -3.4025511577), (-1.5368934547, -3.4502656785))
                Line((-1.5000000224, -3.4002830374), (-1.5214057538, -3.4025511577))
                Line((-1.3945922814, -3.4002830374), (-1.5000000224, -3.4002830374))
                Line((-1.3527283908, -3.271308731), (-1.3945922814, -3.4002830374))
                Line((-1.2320570031, -3.2585225655), (-1.3527283908, -3.271308731))
                Line((-1.2655465893, -3.1822407303), (-1.2320570031, -3.2585225655))
                Line((-1.16637511, -3.0809236524), (-1.2655465893, -3.1822407303))
                Line((-1.0264541612, -2.9379754805), (-1.16637511, -3.0809236524))
                Line((-0.9487520162, -2.9631968923), (-1.0264541612, -2.9379754805))
                Line((-0.8913032447, -2.9379754805), (-0.9487520162, -2.9631968923))
                Line((-0.8408396663, -2.9631968923), (-0.8913032447, -2.9379754805))
                Line((-0.7259421234, -2.9127540686), (-0.8408396663, -2.9631968923))
                Line((-0.5298198663, -2.9127540686), (-0.7259421234, -2.9127540686))
                Line((-0.5000000075, -2.8996624233), (-0.5298198663, -2.9127540686))
                Line((-0.4349701504, -2.8996624233), (-0.5000000075, -2.8996624233))
                Line((0.021362944, -2.6993210648), (-0.4349701504, -2.8996624233))
                Line((0.0500000007, -2.6000000387), (0.021362944, -2.6993210648))
                Line((0.2500000037, -2.4500000365), (0.0500000007, -2.6000000387))
                Line((0.430277732, -2.3975247179), (0.2500000037, -2.4500000365))
                Line((0.6232161203, -2.1132269101), (0.430277732, -2.3975247179))
                Line((0.6810293447, -2.0280381972), (0.6232161203, -2.1132269101))
                Line((0.735277785, -2.0060763639), (0.6810293447, -2.0280381972))
                Line((0.8000000119, -2.0500000305), (0.735277785, -2.0060763639))
                Line((0.8497585613, -2.0692714035), (0.8000000119, -2.0500000305))
                Line((0.9196704807, -2.0863561305), (0.8497585613, -2.0692714035))
                Line((0.9721893915, -2.0521866766), (0.9196704807, -2.0863561305))
                Line((1.1284437578, -2.0159451048), (0.9721893915, -2.0521866766))
                Line((1.2106910088, -1.8807130955), (1.1284437578, -2.0159451048))
                Line((1.2933148542, -1.8269569983), (1.2106910088, -1.8807130955))
                Line((1.3324363992, -1.8507504741), (1.2933148542, -1.8269569983))
                Line((1.3283518067, -1.910675717), (1.3324363992, -1.8507504741))
                Line((1.3895879709, -1.9728043647), (1.3283518067, -1.910675717))
                Line((1.4491017077, -2.0090002422), (1.3895879709, -1.9728043647))
                Line((1.5096130358, -2.0131247832), (1.4491017077, -2.0090002422))
                Line((1.7067003317, -2.0553666981), (1.5096130358, -2.0131247832))
                Line((1.6372456209, -2.0131247832), (1.7067003317, -2.0553666981))
                Line((1.6399939199, -1.9728043647), (1.6372456209, -2.0131247832))
                Line((1.7734067434, -1.9818979787), (1.6399939199, -1.9728043647))
                Line((2.0864868831, -1.9728043647), (1.7734067434, -1.9818979787))
                Line((2.4111836682, -2.0534452018), (2.0864868831, -1.9728043647))
                Line((2.5318048503, -2.0984569716), (2.4111836682, -2.0534452018))
                Line((2.7870843542, -2.1937186999), (2.5318048503, -2.0984569716))
                Line((3.5670639268, -2.1122282968), (2.7870843542, -2.1937186999))
                Line((4.0411909796, -2.0984569716), (3.5670639268, -2.1122282968))
                Line((4.173002235, -2.0846856464), (4.0411909796, -2.0984569716))
                Line((4.2839015058, -2.1122282968), (4.173002235, -2.0846856464))
                Line((4.2839015058, -2.1831103701), (4.2839015058, -2.1122282968))
                Line((4.3500621302, -2.2235709179), (4.2839015058, -2.1831103701))
                Line((4.4189187562, -2.265680206), (4.3500621302, -2.2235709179))
                Line((4.5000000671, -2.1814616297), (4.4189187562, -2.265680206))
                Line((4.5500000678, -2.1814616297), (4.5000000671, -2.1814616297))
                Line((4.6235213018, -2.1814616297), (4.5500000678, -2.1814616297))
                Line((4.69166795, -2.1227166238), (4.6235213018, -2.1814616297))
                Line((4.788777204, -2.1814616297), (4.69166795, -2.1227166238))
                Line((4.9074183456, -2.2532320766), (4.788777204, -2.1814616297))
                Line((4.9796084244, -2.2204315661), (4.9074183456, -2.2532320766))
                Line((5.0681383721, -2.2532320766), (4.9796084244, -2.2204315661))
                Line((5.2592213392, -2.2532320766), (5.0681383721, -2.2532320766))
                Line((5.4208920418, -2.2532320766), (5.2592213392, -2.2532320766))
                Line((5.4930821207, -2.2204315661), (5.4208920418, -2.2532320766))
                Line((5.6646186451, -2.1424916933), (5.4930821207, -2.2204315661))
                Line((5.9916411317, -2.0531605729), (5.6646186451, -2.1424916933))
                Line((6.1235027847, -2.0171405753), (5.9916411317, -2.0531605729))
                Line((6.2004282751, -1.9961272184), (6.1235027847, -2.0171405753))
                Line((6.2502864134, -1.9533036064), (6.2004282751, -1.9961272184))
                Line((6.3142153785, -1.978419319), (6.2502864134, -1.9533036064))
                Line((6.3726981929, -1.9281878937), (6.3142153785, -1.978419319))
                Line((6.4519401178, -1.9281878937), (6.3726981929, -1.9281878937))
                Line((6.5672454852, -1.8291510569), (6.4519401178, -1.9281878937))
                Line((6.8435581108, -1.5918236102), (6.5672454852, -1.8291510569))
                Line((6.8932498926, -1.6043124542), (6.8435581108, -1.5918236102))
                Line((6.9500001036, -1.5472595426), (6.8932498926, -1.6043124542))
                Line((7.0284755827, -1.5472595426), (6.9500001036, -1.5472595426))
                Line((7.0984251709, -1.564839703), (7.0284755827, -1.5472595426))
                Line((7.1793043823, -1.5296793822), (7.0984251709, -1.564839703))
                Line((7.250000108, -1.6000000238), (7.1793043823, -1.5296793822))
                Line((7.3257613327, -1.6307196427), (7.250000108, -1.6000000238))
                Line((7.5500001125, -1.6307196427), (7.3257613327, -1.6307196427))
                Line((7.7170418419, -1.6307196427), (7.5500001125, -1.6307196427))
                Line((7.8480812567, -1.6614392617), (7.7170418419, -1.6307196427))
                Line((7.9500001185, -1.6000000238), (7.8480812567, -1.6614392617))
                Line((8.1500001214, -1.6000000238), (7.9500001185, -1.6000000238))
                Line((8.4000001252, -1.4492937717), (8.1500001214, -1.6000000238))
                Line((8.5000001267, -1.4492937717), (8.4000001252, -1.4492937717))
                Line((8.4463863962, -1.5079710875), (8.5000001267, -1.4492937717))
                Line((8.5000001267, -1.6205609846), (8.4463863962, -1.5079710875))
                Line((8.5455072777, -1.6205609846), (8.5000001267, -1.6205609846))
                Line((8.5455072777, -1.7198548252), (8.5455072777, -1.6205609846))
                Line((8.5455072777, -1.7579804793), (8.5455072777, -1.7198548252))
                Line((8.6613445235, -1.8638214979), (8.5455072777, -1.7579804793))
                Line((8.702024915, -1.9492511268), (8.6613445235, -1.8638214979))
                Line((8.7500001304, -2.0500000305), (8.702024915, -1.9492511268))
                Line((8.7991187495, -1.9492511268), (8.7500001304, -2.0500000305))
                Line((8.9411596362, -1.8816132481), (8.7991187495, -1.9492511268))
                Line((8.9411596362, -1.7848996516), (8.9411596362, -1.8816132481))
                Line((9.088701227, -1.7146424147), (8.9411596362, -1.7848996516))
                Line((9.2281586797, -1.7395281469), (9.088701227, -1.7146424147))
                Line((9.1807112543, -1.7764328117), (9.2281586797, -1.7395281469))
                Line((9.275606105, -1.7933664915), (9.1807112543, -1.7764328117))
                Line((9.2986203055, -1.84008068), (9.275606105, -1.7933664915))
                Line((9.275606105, -1.9690502334), (9.2986203055, -1.84008068))
                Line((9.3216345059, -2.0624786105), (9.275606105, -1.9690502334))
                Line((9.3099649831, -2.150000032), (9.3216345059, -2.0624786105))
                Line((9.3099649831, -2.3018298615), (9.3099649831, -2.150000032))
                Line((9.3599997908, -2.3499999475), (9.3099649831, -2.3018298615))
                Line((9.5099997874, -2.369999947), (9.3599997908, -2.3499999475))
                Line((9.5608522478, -2.2336597759), (9.5099997874, -2.369999947))
                Line((9.6704500397, -2.2336597759), (9.5608522478, -2.2336597759))
                Line((9.6941192725, -2.3000000343), (9.6704500397, -2.2336597759))
                Line((9.6941192725, -2.414999946), (9.6941192725, -2.3000000343))
                Line((9.6941192725, -2.60718134), (9.6941192725, -2.414999946))
                Line((9.7600240255, -2.7918995514), (9.6941192725, -2.60718134))
                Line((9.800000146, -2.9039448462), (9.7600240255, -2.7918995514))
                Line((9.800000146, -1.8667307519), (9.800000146, -2.9039448462))
                Line((9.7950073307, -1.8659146099), (9.800000146, -1.8667307519))
                Line((9.7250407204, -1.8142001588), (9.7950073307, -1.8659146099))
                Line((9.5478878922, -1.7247613981), (9.7250407204, -1.8142001588))
                Line((9.3904178014, -1.5358547307), (9.5478878922, -1.7247613981))
                Line((9.2641737002, -1.4902243327), (9.3904178014, -1.5358547307))
                Line((9.03602171, -1.3016186875), (9.2641737002, -1.4902243327))
                Line((8.9265873329, -1.1981897853), (9.03602171, -1.3016186875))
                Line((8.9042450181, -1.0749877106), (8.9265873329, -1.1981897853))
                Line((8.9265873329, -0.9198443572), (8.9042450181, -1.0749877106))
                Line((8.9042450181, -0.8679640485), (8.9265873329, -0.9198443572))
                Line((8.9265873329, -0.8164188227), (8.9042450181, -0.8679640485))
                Line((8.9773352229, -0.8022894886), (8.9265873329, -0.8164188227))
                Line((9.0000001341, -0.7500000112), (8.9773352229, -0.8022894886))
                Line((9.0235141107, -0.7306404421), (9.0000001341, -0.7500000112))
                Line((9.0705321073, -0.7175495926), (9.0235141107, -0.7306404421))
                Line((9.0909699202, -0.6703981813), (9.0705321073, -0.7175495926))
                Line((9.0500942945, -0.5235864683), (9.0909699202, -0.6703981813))
                Line((9.1318455459, -0.4681034167), (9.0500942945, -0.5235864683))
                Line((9.2809048461, -0.4057418727), (9.1318455459, -0.4681034167))
                Line((9.2809048461, -0.3327332358), (9.2809048461, -0.4057418727))
                Line((9.1979582308, -0.242993453), (9.2809048461, -0.3327332358))
                Line((9.1637868245, -0.1500000022), (9.1979582308, -0.242993453))
                Line((9.1637868245, -0.119022961), (9.1637868245, -0.1500000022))
                Line((9.232129637, -0.072639967), (9.1637868245, -0.119022961))
                Line((9.232129637, -0.0167757096), (9.232129637, -0.072639967))
                Line((9.1637868245, 0.0307889352), (9.232129637, -0.0167757096))
                Line((9.232129637, 0.1289866626), (9.1637868245, 0.0307889352))
                Line((9.1500001363, 0.2500000037), (9.232129637, 0.1289866626))
                Line((8.9767021925, 0.5053450748), (9.1500001363, 0.2500000037))
                Line((9.0405847498, 0.5707486453), (8.9767021925, 0.5053450748))
                Line((9.0405847498, 0.631589176), (9.0405847498, 0.5707486453))
                Line((8.9767021925, 0.7578332773), (9.0405847498, 0.631589176))
                Line((8.8474160648, 0.9084135908), (8.9767021925, 0.7578332773))
                Line((8.7698443881, 1.0270526257), (8.8474160648, 0.9084135908))
                Line((8.7698443881, 1.1441706473), (8.7698443881, 1.0270526257))
                Line((8.8291639056, 1.2293473903), (8.7698443881, 1.1441706473))
                Line((8.865668224, 1.3327762925), (8.8291639056, 1.2293473903))
                Line((8.9212281056, 1.375364664), (8.865668224, 1.3327762925))
                Line((8.9310717945, 1.5748654422), (8.9212281056, 1.375364664))
                Line((8.9113844166, 1.7008615034), (8.9310717945, 1.5748654422))
                Line((8.9310717945, 1.8164585117), (8.9113844166, 1.7008615034))
                Line((8.8916970387, 1.9139251999), (8.9310717945, 1.8164585117))
                Line((8.8717522771, 2.0415684754), (8.8916970387, 1.9139251999))
                Line((8.8552719691, 2.1470398032), (8.8717522771, 2.0415684754))
                Line((8.7774494545, 2.2332161471), (8.8552719691, 2.1470398032))
                Line((8.632953194, 2.2849305982), (8.7774494545, 2.2332161471))
                Line((8.3637338456, 2.5830491987), (8.632953194, 2.2849305982))
                Line((8.1260755225, 2.5830491987), (8.3637338456, 2.5830491987))
                Line((8.1260755225, 2.7199403929), (8.1260755225, 2.5830491987))
                Line((8.0554387983, 2.7698645896), (8.1260755225, 2.7199403929))
                Line((8.0747413247, 2.8258072283), (8.0554387983, 2.7698645896))
                Line((8.1000001207, 2.8500000425), (8.0747413247, 2.8258072283))
                Line((8.0596351638, 2.892143557), (8.1000001207, 2.8500000425))
                Line((8.0747413247, 2.9359242769), (8.0596351638, 2.892143557))
                Line((8.1774097203, 2.9990463275), (8.0747413247, 2.9359242769))
                Line((8.1991288907, 3.0887290408), (8.1774097203, 2.9990463275))
                Line((8.2496578505, 3.0712944577), (8.1991288907, 3.0887290408))
                Line((8.4428265355, 3.2644631428), (8.2496578505, 3.0712944577))
                Line((8.5033049304, 3.4397418044), (8.4428265355, 3.2644631428))
                Line((8.584029707, 3.5204665811), (8.5033049304, 3.4397418044))
                Line((8.5949278623, 3.6127751811), (8.584029707, 3.5204665811))
                Line((8.60259928, 3.6777529514), (8.5949278623, 3.6127751811))
                Line((8.5949278623, 3.7861706937), (8.60259928, 3.6777529514))
                Line((8.6755415655, 3.8667843969), (8.5949278623, 3.7861706937))
                Line((8.6246322633, 3.9519611399), (8.6755415655, 3.8667843969))
                Line((8.6090506281, 4.1721715066), (8.6246322633, 3.9519611399))
                Line((8.6402138984, 4.3531618379), (8.6090506281, 4.1721715066))
                Line((8.5295242918, 4.4310803193), (8.6402138984, 4.3531618379))
                Line((8.5500001274, 4.5500000678), (8.5295242918, 4.4310803193))
                Line((8.6527263665, 4.6151229247), (8.5500001274, 4.5500000678))
                Line((8.6527263665, 4.6151229247), (8.6615897396, 4.8006865434))
                Line((8.6615897396, 4.8006865434), (8.6527263665, 4.9147625384))
                Line((8.6704531127, 5.1135753602), (8.6527263665, 4.9147625384))
                Line((8.7152665683, 5.214995286), (8.6704531127, 5.1135753602))
                Line((8.7673828694, 5.300000079), (8.7152665683, 5.214995286))
                Line((8.7673828694, 5.3838432271), (8.7673828694, 5.300000079))
                Line((8.8133507357, 5.4369752439), (8.7673828694, 5.3838432271))
                Line((8.883695469, 5.5961764825), (8.8133507357, 5.4369752439))
                Line((8.8500001319, 5.7000000849), (8.883695469, 5.5961764825))
                Line((8.7767013396, 5.7634155034), (8.8500001319, 5.7000000849))
                Line((8.8276841868, 5.8036881161), (8.7767013396, 5.7634155034))
                Line((8.9397067513, 5.8921775122), (8.8276841868, 5.8036881161))
                Line((8.9873492854, 6.0000000894), (8.9397067513, 5.8921775122))
                Line((8.9873492854, 6.1650354447), (8.9873492854, 6.0000000894))
                Line((9.0162485375, 6.2304390152), (8.9873492854, 6.1650354447))
                Line((9.1228628052, 6.2962956065), (9.0162485375, 6.2304390152))
                Line((9.1228628052, 6.3456354256), (9.1228628052, 6.2962956065))
                Line((9.1971054019, 6.3722003509), (9.1228628052, 6.3456354256))
                Line((9.3128461248, 6.490532284), (9.1971054019, 6.3722003509))
                Line((9.5166619027, 6.6989111017), (9.3128461248, 6.490532284))
                Line((9.433393568, 6.9316261317), (9.5166619027, 6.6989111017))
                Line((9.3554264891, 7.0750160572), (9.433393568, 6.9316261317))
                Line((9.433393568, 7.1438105386), (9.3554264891, 7.0750160572))
                Line((9.5000001416, 7.3500001095), (9.433393568, 7.1438105386))
                Line((9.6500001438, 7.4000001103), (9.5000001416, 7.3500001095))
                Line((9.7004974402, 7.5563212558), (9.6500001438, 7.4000001103))
                Line((9.7500001453, 7.6000001132), (9.7004974402, 7.5563212558))
                Line((9.7345048029, 7.7027798585), (9.7500001453, 7.6000001132))
                Line((9.800000146, 7.7605698671), (9.7345048029, 7.7027798585))
                Line((9.800000146, 8.3000001535), (9.800000146, 7.7605698671))
                Line((9.7753870362, 8.3000001535), (9.800000146, 8.3000001535))
            make_face()
            # Profile area: 8.4103040373, perimeter: 21.9944820339
            with BuildLine():
                Line((9.800000146, 7.7605698671), (9.7345048029, 7.7027798585))
                Line((9.7345048029, 7.7027798585), (9.7500001453, 7.6000001132))
                Line((9.7500001453, 7.6000001132), (9.7004974402, 7.5563212558))
                Line((9.7004974402, 7.5563212558), (9.6500001438, 7.4000001103))
                Line((9.6500001438, 7.4000001103), (9.5000001416, 7.3500001095))
                Line((9.5000001416, 7.3500001095), (9.433393568, 7.1438105386))
                Line((9.433393568, 7.1438105386), (9.3554264891, 7.0750160572))
                Line((9.3554264891, 7.0750160572), (9.433393568, 6.9316261317))
                Line((9.433393568, 6.9316261317), (9.5166619027, 6.6989111017))
                Line((9.5166619027, 6.6989111017), (9.3128461248, 6.490532284))
                Line((9.3128461248, 6.490532284), (9.1971054019, 6.3722003509))
                Line((9.1971054019, 6.3722003509), (9.1228628052, 6.3456354256))
                Line((9.1228628052, 6.3456354256), (9.1228628052, 6.2962956065))
                Line((9.1228628052, 6.2962956065), (9.0162485375, 6.2304390152))
                Line((9.0162485375, 6.2304390152), (8.9873492854, 6.1650354447))
                Line((8.9873492854, 6.1650354447), (8.9873492854, 6.0000000894))
                Line((8.9873492854, 6.0000000894), (8.9397067513, 5.8921775122))
                Line((8.9397067513, 5.8921775122), (8.8276841868, 5.8036881161))
                Line((8.8276841868, 5.8036881161), (8.7767013396, 5.7634155034))
                Line((8.7767013396, 5.7634155034), (8.8500001319, 5.7000000849))
                Line((8.8500001319, 5.7000000849), (8.883695469, 5.5961764825))
                Line((8.883695469, 5.5961764825), (8.8133507357, 5.4369752439))
                Line((8.8133507357, 5.4369752439), (8.7673828694, 5.3838432271))
                Line((8.7673828694, 5.3838432271), (8.7673828694, 5.300000079))
                Line((8.7673828694, 5.300000079), (8.7152665683, 5.214995286))
                Line((8.7152665683, 5.214995286), (8.6704531127, 5.1135753602))
                Line((8.6704531127, 5.1135753602), (8.6527263665, 4.9147625384))
                Line((8.6615897396, 4.8006865434), (8.6527263665, 4.9147625384))
                Line((8.6527263665, 4.6151229247), (8.6615897396, 4.8006865434))
                Line((8.6527263665, 4.6151229247), (8.5500001274, 4.5500000678))
                Line((8.5500001274, 4.5500000678), (8.5295242918, 4.4310803193))
                Line((8.5295242918, 4.4310803193), (8.6402138984, 4.3531618379))
                Line((8.6402138984, 4.3531618379), (8.6090506281, 4.1721715066))
                Line((8.6090506281, 4.1721715066), (8.6246322633, 3.9519611399))
                Line((8.6246322633, 3.9519611399), (8.6755415655, 3.8667843969))
                Line((8.6755415655, 3.8667843969), (8.5949278623, 3.7861706937))
                Line((8.5949278623, 3.7861706937), (8.60259928, 3.6777529514))
                Line((8.60259928, 3.6777529514), (8.5949278623, 3.6127751811))
                Line((8.5949278623, 3.6127751811), (8.584029707, 3.5204665811))
                Line((8.584029707, 3.5204665811), (8.5033049304, 3.4397418044))
                Line((8.5033049304, 3.4397418044), (8.4428265355, 3.2644631428))
                Line((8.4428265355, 3.2644631428), (8.2496578505, 3.0712944577))
                Line((8.2496578505, 3.0712944577), (8.1991288907, 3.0887290408))
                Line((8.1991288907, 3.0887290408), (8.1774097203, 2.9990463275))
                Line((8.1774097203, 2.9990463275), (8.0747413247, 2.9359242769))
                Line((8.0747413247, 2.9359242769), (8.0596351638, 2.892143557))
                Line((8.0596351638, 2.892143557), (8.1000001207, 2.8500000425))
                Line((8.1000001207, 2.8500000425), (8.0747413247, 2.8258072283))
                Line((8.0747413247, 2.8258072283), (8.0554387983, 2.7698645896))
                Line((8.0554387983, 2.7698645896), (8.1260755225, 2.7199403929))
                Line((8.1260755225, 2.7199403929), (8.1260755225, 2.5830491987))
                Line((8.1260755225, 2.5830491987), (8.3637338456, 2.5830491987))
                Line((8.3637338456, 2.5830491987), (8.632953194, 2.2849305982))
                Line((8.632953194, 2.2849305982), (8.7774494545, 2.2332161471))
                Line((8.7774494545, 2.2332161471), (8.8552719691, 2.1470398032))
                Line((8.8552719691, 2.1470398032), (8.8717522771, 2.0415684754))
                Line((8.8717522771, 2.0415684754), (8.8916970387, 1.9139251999))
                Line((8.8916970387, 1.9139251999), (8.9310717945, 1.8164585117))
                Line((8.9310717945, 1.8164585117), (8.9113844166, 1.7008615034))
                Line((8.9113844166, 1.7008615034), (8.9310717945, 1.5748654422))
                Line((8.9310717945, 1.5748654422), (8.9212281056, 1.375364664))
                Line((8.9212281056, 1.375364664), (8.865668224, 1.3327762925))
                Line((8.865668224, 1.3327762925), (8.8291639056, 1.2293473903))
                Line((8.8291639056, 1.2293473903), (8.7698443881, 1.1441706473))
                Line((8.7698443881, 1.1441706473), (8.7698443881, 1.0270526257))
                Line((8.7698443881, 1.0270526257), (8.8474160648, 0.9084135908))
                Line((8.8474160648, 0.9084135908), (8.9767021925, 0.7578332773))
                Line((8.9767021925, 0.7578332773), (9.0405847498, 0.631589176))
                Line((9.0405847498, 0.631589176), (9.0405847498, 0.5707486453))
                Line((9.0405847498, 0.5707486453), (8.9767021925, 0.5053450748))
                Line((8.9767021925, 0.5053450748), (9.1500001363, 0.2500000037))
                Line((9.1500001363, 0.2500000037), (9.232129637, 0.1289866626))
                Line((9.232129637, 0.1289866626), (9.1637868245, 0.0307889352))
                Line((9.1637868245, 0.0307889352), (9.232129637, -0.0167757096))
                Line((9.232129637, -0.0167757096), (9.232129637, -0.072639967))
                Line((9.232129637, -0.072639967), (9.1637868245, -0.119022961))
                Line((9.1637868245, -0.119022961), (9.1637868245, -0.1500000022))
                Line((9.1637868245, -0.1500000022), (9.1979582308, -0.242993453))
                Line((9.1979582308, -0.242993453), (9.2809048461, -0.3327332358))
                Line((9.2809048461, -0.3327332358), (9.2809048461, -0.4057418727))
                Line((9.2809048461, -0.4057418727), (9.1318455459, -0.4681034167))
                Line((9.1318455459, -0.4681034167), (9.0500942945, -0.5235864683))
                Line((9.0500942945, -0.5235864683), (9.0909699202, -0.6703981813))
                Line((9.0909699202, -0.6703981813), (9.0705321073, -0.7175495926))
                Line((9.0705321073, -0.7175495926), (9.0235141107, -0.7306404421))
                Line((9.0235141107, -0.7306404421), (9.0000001341, -0.7500000112))
                Line((9.0000001341, -0.7500000112), (8.9773352229, -0.8022894886))
                Line((8.9773352229, -0.8022894886), (8.9265873329, -0.8164188227))
                Line((8.9265873329, -0.8164188227), (8.9042450181, -0.8679640485))
                Line((8.9042450181, -0.8679640485), (8.9265873329, -0.9198443572))
                Line((8.9265873329, -0.9198443572), (8.9042450181, -1.0749877106))
                Line((8.9042450181, -1.0749877106), (8.9265873329, -1.1981897853))
                Line((8.9265873329, -1.1981897853), (9.03602171, -1.3016186875))
                Line((9.03602171, -1.3016186875), (9.2641737002, -1.4902243327))
                Line((9.2641737002, -1.4902243327), (9.3904178014, -1.5358547307))
                Line((9.3904178014, -1.5358547307), (9.5478878922, -1.7247613981))
                Line((9.5478878922, -1.7247613981), (9.7250407204, -1.8142001588))
                Line((9.7250407204, -1.8142001588), (9.7950073307, -1.8659146099))
                Line((9.7950073307, -1.8659146099), (9.800000146, -1.8667307519))
                Line((9.800000146, 7.7605698671), (9.800000146, -1.8667307519))
            make_face()
            # Profile area: 294.7661843575, perimeter: 127.7996519213
            with BuildLine():
                Line((-10, 8.3000001535), (9.7753870362, 8.3000001535))
                Line((-10, -8.8), (-10, 8.3000001535))
                Line((9.800000146, -8.8), (-10, -8.8))
                Line((9.800000146, -2.9039448462), (9.800000146, -8.8))
                Line((9.800000146, -2.9039448462), (9.7600240255, -2.7918995514))
                Line((9.7600240255, -2.7918995514), (9.6941192725, -2.60718134))
                Line((9.6941192725, -2.60718134), (9.6941192725, -2.414999946))
                Line((9.6941192725, -2.414999946), (9.6941192725, -2.3000000343))
                Line((9.6941192725, -2.3000000343), (9.6704500397, -2.2336597759))
                Line((9.6704500397, -2.2336597759), (9.5608522478, -2.2336597759))
                Line((9.5608522478, -2.2336597759), (9.5099997874, -2.369999947))
                Line((9.5099997874, -2.369999947), (9.3599997908, -2.3499999475))
                Line((9.3599997908, -2.3499999475), (9.3099649831, -2.3018298615))
                Line((9.3099649831, -2.3018298615), (9.3099649831, -2.150000032))
                Line((9.3099649831, -2.150000032), (9.3216345059, -2.0624786105))
                Line((9.3216345059, -2.0624786105), (9.275606105, -1.9690502334))
                Line((9.275606105, -1.9690502334), (9.2986203055, -1.84008068))
                Line((9.2986203055, -1.84008068), (9.275606105, -1.7933664915))
                Line((9.275606105, -1.7933664915), (9.1807112543, -1.7764328117))
                Line((9.1807112543, -1.7764328117), (9.2281586797, -1.7395281469))
                Line((9.2281586797, -1.7395281469), (9.088701227, -1.7146424147))
                Line((9.088701227, -1.7146424147), (8.9411596362, -1.7848996516))
                Line((8.9411596362, -1.7848996516), (8.9411596362, -1.8816132481))
                Line((8.9411596362, -1.8816132481), (8.7991187495, -1.9492511268))
                Line((8.7991187495, -1.9492511268), (8.7500001304, -2.0500000305))
                Line((8.7500001304, -2.0500000305), (8.702024915, -1.9492511268))
                Line((8.702024915, -1.9492511268), (8.6613445235, -1.8638214979))
                Line((8.6613445235, -1.8638214979), (8.5455072777, -1.7579804793))
                Line((8.5455072777, -1.7579804793), (8.5455072777, -1.7198548252))
                Line((8.5455072777, -1.7198548252), (8.5455072777, -1.6205609846))
                Line((8.5455072777, -1.6205609846), (8.5000001267, -1.6205609846))
                Line((8.5000001267, -1.6205609846), (8.4463863962, -1.5079710875))
                Line((8.4463863962, -1.5079710875), (8.5000001267, -1.4492937717))
                Line((8.5000001267, -1.4492937717), (8.4000001252, -1.4492937717))
                Line((8.4000001252, -1.4492937717), (8.1500001214, -1.6000000238))
                Line((8.1500001214, -1.6000000238), (7.9500001185, -1.6000000238))
                Line((7.9500001185, -1.6000000238), (7.8480812567, -1.6614392617))
                Line((7.8480812567, -1.6614392617), (7.7170418419, -1.6307196427))
                Line((7.7170418419, -1.6307196427), (7.5500001125, -1.6307196427))
                Line((7.5500001125, -1.6307196427), (7.3257613327, -1.6307196427))
                Line((7.3257613327, -1.6307196427), (7.250000108, -1.6000000238))
                Line((7.250000108, -1.6000000238), (7.1793043823, -1.5296793822))
                Line((7.1793043823, -1.5296793822), (7.0984251709, -1.564839703))
                Line((7.0984251709, -1.564839703), (7.0284755827, -1.5472595426))
                Line((7.0284755827, -1.5472595426), (6.9500001036, -1.5472595426))
                Line((6.9500001036, -1.5472595426), (6.8932498926, -1.6043124542))
                Line((6.8932498926, -1.6043124542), (6.8435581108, -1.5918236102))
                Line((6.8435581108, -1.5918236102), (6.5672454852, -1.8291510569))
                Line((6.5672454852, -1.8291510569), (6.4519401178, -1.9281878937))
                Line((6.4519401178, -1.9281878937), (6.3726981929, -1.9281878937))
                Line((6.3726981929, -1.9281878937), (6.3142153785, -1.978419319))
                Line((6.3142153785, -1.978419319), (6.2502864134, -1.9533036064))
                Line((6.2502864134, -1.9533036064), (6.2004282751, -1.9961272184))
                Line((6.2004282751, -1.9961272184), (6.1235027847, -2.0171405753))
                Line((6.1235027847, -2.0171405753), (5.9916411317, -2.0531605729))
                Line((5.9916411317, -2.0531605729), (5.6646186451, -2.1424916933))
                Line((5.6646186451, -2.1424916933), (5.4930821207, -2.2204315661))
                Line((5.4930821207, -2.2204315661), (5.4208920418, -2.2532320766))
                Line((5.4208920418, -2.2532320766), (5.2592213392, -2.2532320766))
                Line((5.2592213392, -2.2532320766), (5.0681383721, -2.2532320766))
                Line((5.0681383721, -2.2532320766), (4.9796084244, -2.2204315661))
                Line((4.9796084244, -2.2204315661), (4.9074183456, -2.2532320766))
                Line((4.9074183456, -2.2532320766), (4.788777204, -2.1814616297))
                Line((4.788777204, -2.1814616297), (4.69166795, -2.1227166238))
                Line((4.69166795, -2.1227166238), (4.6235213018, -2.1814616297))
                Line((4.6235213018, -2.1814616297), (4.5500000678, -2.1814616297))
                Line((4.5500000678, -2.1814616297), (4.5000000671, -2.1814616297))
                Line((4.5000000671, -2.1814616297), (4.4189187562, -2.265680206))
                Line((4.4189187562, -2.265680206), (4.3500621302, -2.2235709179))
                Line((4.3500621302, -2.2235709179), (4.2839015058, -2.1831103701))
                Line((4.2839015058, -2.1831103701), (4.2839015058, -2.1122282968))
                Line((4.2839015058, -2.1122282968), (4.173002235, -2.0846856464))
                Line((4.173002235, -2.0846856464), (4.0411909796, -2.0984569716))
                Line((4.0411909796, -2.0984569716), (3.5670639268, -2.1122282968))
                Line((3.5670639268, -2.1122282968), (2.7870843542, -2.1937186999))
                Line((2.7870843542, -2.1937186999), (2.5318048503, -2.0984569716))
                Line((2.5318048503, -2.0984569716), (2.4111836682, -2.0534452018))
                Line((2.4111836682, -2.0534452018), (2.0864868831, -1.9728043647))
                Line((2.0864868831, -1.9728043647), (1.7734067434, -1.9818979787))
                Line((1.7734067434, -1.9818979787), (1.6399939199, -1.9728043647))
                Line((1.6399939199, -1.9728043647), (1.6372456209, -2.0131247832))
                Line((1.6372456209, -2.0131247832), (1.7067003317, -2.0553666981))
                Line((1.7067003317, -2.0553666981), (1.5096130358, -2.0131247832))
                Line((1.5096130358, -2.0131247832), (1.4491017077, -2.0090002422))
                Line((1.4491017077, -2.0090002422), (1.3895879709, -1.9728043647))
                Line((1.3895879709, -1.9728043647), (1.3283518067, -1.910675717))
                Line((1.3283518067, -1.910675717), (1.3324363992, -1.8507504741))
                Line((1.3324363992, -1.8507504741), (1.2933148542, -1.8269569983))
                Line((1.2933148542, -1.8269569983), (1.2106910088, -1.8807130955))
                Line((1.2106910088, -1.8807130955), (1.1284437578, -2.0159451048))
                Line((1.1284437578, -2.0159451048), (0.9721893915, -2.0521866766))
                Line((0.9721893915, -2.0521866766), (0.9196704807, -2.0863561305))
                Line((0.9196704807, -2.0863561305), (0.8497585613, -2.0692714035))
                Line((0.8497585613, -2.0692714035), (0.8000000119, -2.0500000305))
                Line((0.8000000119, -2.0500000305), (0.735277785, -2.0060763639))
                Line((0.735277785, -2.0060763639), (0.6810293447, -2.0280381972))
                Line((0.6810293447, -2.0280381972), (0.6232161203, -2.1132269101))
                Line((0.6232161203, -2.1132269101), (0.430277732, -2.3975247179))
                Line((0.430277732, -2.3975247179), (0.2500000037, -2.4500000365))
                Line((0.2500000037, -2.4500000365), (0.0500000007, -2.6000000387))
                Line((0.0500000007, -2.6000000387), (0.021362944, -2.6993210648))
                Line((0.021362944, -2.6993210648), (-0.4349701504, -2.8996624233))
                Line((-0.4349701504, -2.8996624233), (-0.5000000075, -2.8996624233))
                Line((-0.5000000075, -2.8996624233), (-0.5298198663, -2.9127540686))
                Line((-0.5298198663, -2.9127540686), (-0.7259421234, -2.9127540686))
                Line((-0.7259421234, -2.9127540686), (-0.8408396663, -2.9631968923))
                Line((-0.8408396663, -2.9631968923), (-0.8913032447, -2.9379754805))
                Line((-0.8913032447, -2.9379754805), (-0.9487520162, -2.9631968923))
                Line((-0.9487520162, -2.9631968923), (-1.0264541612, -2.9379754805))
                Line((-1.0264541612, -2.9379754805), (-1.16637511, -3.0809236524))
                Line((-1.16637511, -3.0809236524), (-1.2655465893, -3.1822407303))
                Line((-1.2655465893, -3.1822407303), (-1.2320570031, -3.2585225655))
                Line((-1.2320570031, -3.2585225655), (-1.3527283908, -3.271308731))
                Line((-1.3527283908, -3.271308731), (-1.3945922814, -3.4002830374))
                Line((-1.3945922814, -3.4002830374), (-1.5000000224, -3.4002830374))
                Line((-1.5000000224, -3.4002830374), (-1.5214057538, -3.4025511577))
                Line((-1.5214057538, -3.4025511577), (-1.5368934547, -3.4502656785))
                Line((-1.5368934547, -3.4502656785), (-1.6417883338, -3.4025511577))
                Line((-1.6417883338, -3.4025511577), (-1.7499090669, -3.4502656785))
                Line((-1.7499090669, -3.4502656785), (-1.854803946, -3.4025511577))
                Line((-1.854803946, -3.4025511577), (-1.9846362973, -3.4598471846))
                Line((-1.9846362973, -3.4598471846), (-2.0018740175, -3.4977423272))
                Line((-2.0018740175, -3.4977423272), (-2.0500000305, -3.5500000529))
                Line((-2.0500000305, -3.5500000529), (-2.1656959146, -3.5622590213))
                CenterArc((-2.1704340196, -3.5175424328), 0.0449669092, -120.8936040003, 36.9420136155)
                Line((-2.193522075, -3.5561295371), (-2.2587125171, -3.5622590213))
                Line((-2.2587125171, -3.5622590213), (-2.3239029591, -3.6326573937))
                Line((-2.3239029591, -3.6326573937), (-2.3943301689, -3.600621506))
                Line((-2.3943301689, -3.600621506), (-2.4558577578, -3.6670644073))
                Line((-2.4558577578, -3.6670644073), (-2.5061482217, -3.6892579804))
                Line((-2.5061482217, -3.6892579804), (-2.530543229, -3.6781611939))
                Line((-2.530543229, -3.6781611939), (-2.6609852449, -3.6892579804))
                Line((-2.6609852449, -3.6892579804), (-2.735201902, -3.7694036537))
                Line((-2.735201902, -3.7694036537), (-2.7644849641, -3.8010260794))
                Line((-2.7644849641, -3.8010260794), (-2.8800887306, -3.8010260794))
                Line((-2.8800887306, -3.8010260794), (-2.9762843829, -3.8010260794))
                Line((-2.9762843829, -3.8010260794), (-2.9955235134, -3.8010260794))
                Line((-2.9955235134, -3.8010260794), (-3.1043121943, -3.9185056644))
                Line((-3.1043121943, -3.9185056644), (-3.1833063929, -4.0038105471))
                Line((-3.1833063929, -4.0038105471), (-3.2199296897, -4.0433596037))
                Line((-3.2199296897, -4.0433596037), (-3.2593934062, -4.0859759954))
                Line((-3.2593934062, -4.0859759954), (-3.2396615479, -4.1042481304))
                Line((-3.2396615479, -4.1042481304), (-3.236957828, -4.1360301853))
                Line((-3.236957828, -4.1360301853), (-3.3593179803, -4.1201391578))
                Line((-3.3593179803, -4.1201391578), (-3.4677567156, -4.1653110056))
                Line((-3.4677567156, -4.1653110056), (-3.5000000522, -4.2500000633))
                Line((-3.5000000522, -4.2500000633), (-3.7000000551, -4.3500000648))
                Line((-3.7000000551, -4.3500000648), (-3.7716721751, -4.4273979231))
                CenterArc((-3.7783449085, -4.4212188252), 0.0090943181, -178.8859073098, 136.0855417051)
                Line((-3.7874375073, -4.4213956493), (-3.8571822495, -4.4504489103))
                Line((-3.8571822495, -4.4504489103), (-3.9574800364, -4.4212188252))
                Line((-3.9574800364, -4.4212188252), (-4.0947684019, -4.4784084367))
                Line((-4.0947684019, -4.4784084367), (-4.2827962423, -4.5203604132))
                Line((-4.2827962423, -4.5203604132), (-4.3939569994, -4.4879645001))
                Line((-4.3939569994, -4.4879645001), (-4.4839326062, -4.5203604132))
                Line((-4.4839326062, -4.5203604132), (-4.4542081234, -4.6029164559))
                Line((-4.4542081234, -4.6029164559), (-4.5500000678, -4.70000007))
                Line((-4.5500000678, -4.70000007), (-4.6273515787, -4.5616384345))
                Line((-4.6273515787, -4.5616384345), (-4.6273515787, -4.4879645001))
                Line((-4.6273515787, -4.4879645001), (-4.70000007, -4.4879645001))
                Line((-4.70000007, -4.4879645001), (-4.7532804327, -4.5616384345))
                Line((-4.7532804327, -4.5616384345), (-4.8282839446, -4.6035693856))
                CenterArc((-4.8395368242, -4.5834409254), 0.0230604035, -151.7032424957, 90.9107539268)
                Line((-4.8598416059, -4.5943724417), (-4.9500000738, -4.5943724417))
                Line((-4.9500000738, -4.5943724417), (-5.1223219351, -4.5943724417))
                Line((-5.1223219351, -4.5943724417), (-5.1675851987, -4.5616384345))
                Line((-5.1675851987, -4.5616384345), (-5.1965263794, -4.5098702268))
                Line((-5.1965263794, -4.5098702268), (-5.2687815493, -4.6097817587))
                Line((-5.2687815493, -4.6097817587), (-5.3765514716, -4.6700308754))
                Line((-5.3765514716, -4.6700308754), (-5.481675107, -4.728800577))
                Line((-5.481675107, -4.728800577), (-5.597616439, -4.7936179462))
                Line((-5.597616439, -4.7936179462), (-5.6127465165, -4.802076464))
                Line((-5.6127465165, -4.802076464), (-5.9000000879, -4.900000073))
                Line((-5.9000000879, -4.900000073), (-6.0853236119, -4.9631761311))
                Line((-6.0853236119, -4.9631761311), (-6.2000000924, -4.9631761311))
                Line((-6.2000000924, -4.9631761311), (-6.1880609715, -4.9981988916))
                Line((-6.1880609715, -4.9981988916), (-6.2801677864, -4.9806875113))
                Line((-6.2801677864, -4.9806875113), (-6.3276255918, -5.0457759199))
                Line((-6.3276255918, -5.0457759199), (-6.3038966891, -5.0630773361))
                Line((-6.3038966891, -5.0630773361), (-6.4000000954, -5.0630773361))
                CenterArc((-6.4000000954, -5.1043486543), 0.0412713182, 90, 37.648081673)
                Line((-6.425209022, -5.0716709597), (-6.5617586959, -5.0652847756))
                Line((-6.5407705536, -5.1360125879), (-6.5617586959, -5.0652847756))
                Line((-6.6806915024, -5.2234631809), (-6.5407705536, -5.1360125879))
                Line((-6.6806915024, -5.2234631809), (-6.8678357714, -5.309164762))
                Line((-6.8678357714, -5.309164762), (-6.8891579946, -5.3537547385))
                Line((-6.8891579946, -5.3537547385), (-7.0156459633, -5.3768535415))
                Line((-7.0156459633, -5.3768535415), (-7.0426141881, -5.4332506862))
                Line((-7.0426141881, -5.4332506862), (-7.0485735475, -5.4533894591))
                Line((-7.0485735475, -5.4533894591), (-7.1412757565, -5.4703184215))
                Line((-7.1412757565, -5.4703184215), (-7.1692451201, -5.528809192))
                Line((-7.1692451201, -5.528809192), (-7.355025776, -5.562735824))
                Line((-7.355025776, -5.562735824), (-7.450000111, -5.562735824))
                Line((-7.450000111, -5.562735824), (-7.4677468394, -5.562735824))
                Line((-7.4677468394, -5.562735824), (-7.5207650699, -5.5930025706))
                Line((-7.5207650699, -5.5930025706), (-7.5676202153, -5.6296267971))
                Line((-7.5676202153, -5.6296267971), (-7.8910077095, -5.6296267971))
                Line((-7.8910077095, -5.6296267971), (-8.0250623095, -5.6850956186))
                Line((-8.0250623095, -5.6850956186), (-8.0984411385, -5.7154581512))
                Line((-8.0984411385, -5.7154581512), (-8.0920375185, -5.7309341374))
                Line((-8.0920375185, -5.7309341374), (-8.2320650222, -5.7309341374))
                Line((-8.2320650222, -5.7309341374), (-8.4222359656, -5.8494372722))
                Line((-8.4222359656, -5.8494372722), (-8.5518269109, -5.9301905828))
                Line((-8.5518269109, -5.9301905828), (-8.6000001281, -6.0000000894))
                Line((-8.6000001281, -6.0000000894), (-8.6000001281, -6.1500000916))
                Line((-8.6000001281, -6.1500000916), (-8.7160861381, -6.198033909))
                Line((-8.7160861381, -6.198033909), (-8.7495572687, -6.2465381037))
                Line((-8.7495572687, -6.2465381037), (-8.7160861381, -6.2903604155))
                Line((-8.7160861381, -6.2903604155), (-8.7495572687, -6.3388646102))
                Line((-8.7495572687, -6.3388646102), (-8.7233434745, -6.4022169511))
                Line((-8.7233434745, -6.4022169511), (-8.7160861381, -6.4197561615))
                Line((-8.7160861381, -6.4197561615), (-8.8704543511, -6.6016845265))
                Line((-8.8704543511, -6.6016845265), (-8.9718970389, -6.6016845265))
                Line((-8.9718970389, -6.6016845265), (-9.0216941002, -6.5594311739))
                Line((-9.0216941002, -6.5594311739), (-9.1000001356, -6.5594311739))
                Line((-9.1000001356, -6.5594311739), (-9.1127742747, -6.5485921767))
                Line((-9.1127742747, -6.5485921767), (-9.1574075608, -6.510720344))
                Line((-9.1574075608, -6.510720344), (-9.2412448654, -6.4775046845))
                Line((-9.2412448654, -6.4775046845), (-9.3173722365, -6.447343638))
                Line((-9.3173722365, -6.447343638), (-9.3293217983, -6.4775046845))
                Line((-9.3293217983, -6.4775046845), (-9.3514326126, -6.4941125143))
                Line((-9.3514326126, -6.4941125143), (-9.5000001416, -6.8000001013))
                Line((-9.5000001416, -6.8000001013), (-9.3403772054, -6.8772655436))
                Line((-9.3403772054, -6.8772655436), (-9.2690322103, -7.0181255041))
                Line((-9.2690322103, -7.0181255041), (-9.5100884195, -7.3733256925))
                Line((-9.5100884195, -7.3733256925), (-9.6706329754, -7.7950055992))
                Line((-9.6706329754, -7.7950055992), (-9.800000146, -7.7950055992))
                Line((-9.800000146, -7.7950055992), (-9.800000146, -7.3883116656))
                Line((-9.800000146, -7.3883116656), (-9.800000146, -6.8000001013))
                Line((-9.800000146, -6.8000001013), (-9.5100884195, -6.6001830593))
                Line((-9.5100884195, -6.6001830593), (-9.5100884195, -6.3000000939))
                Line((-9.5100884195, -6.3000000939), (-9.7353165607, -6.214249857))
                Line((-9.7353165607, -6.214249857), (-9.7353165607, -6.1705610384))
                Line((-9.7353165607, -6.1705610384), (-9.6000001431, -5.9500000887))
                Line((-9.6000001431, -5.9500000887), (-9.4200003961, -5.8238339328))
                Line((-9.4200003961, -5.8238339328), (-9.3626134541, -5.7302952577))
                Line((-9.3626134541, -5.7302952577), (-9.1717968397, -5.7770645953))
                Line((-9.1717968397, -5.7770645953), (-9.1603336296, -5.7302952577))
                Line((-9.1603336296, -5.7302952577), (-9.2059011451, -5.4695280927))
                Line((-9.2059011451, -5.4695280927), (-9.3138981125, -5.280059729))
                Line((-9.3138981125, -5.280059729), (-9.2897225419, -5.1814245813))
                Line((-9.2897225419, -5.1814245813), (-9.4200003961, -5.1814245813))
                Line((-9.4200003961, -5.1814245813), (-9.4200003961, -5.1985883326))
                Line((-9.4200003961, -5.1985883326), (-9.4010535598, -5.3672151763))
                Line((-9.4010535598, -5.3672151763), (-9.3409145791, -5.4530147414))
                Line((-9.3409145791, -5.4530147414), (-9.4284539837, -5.670385948))
                Line((-9.4284539837, -5.670385948), (-9.5500001423, -5.5500000827))
                Line((-9.5500001423, -5.5500000827), (-9.6676583519, -5.4334650517))
                Line((-9.6676583519, -5.4334650517), (-9.7699903513, -5.5051920135))
                Line((-9.7699903513, -5.5051920135), (-9.8178839599, -5.5051920135))
                Line((-9.8178839599, -5.5051920135), (-9.8178839599, -4.9806997143))
                Line((-9.8178839599, -4.9806997143), (-9.6852561053, -4.9181751543))
                Line((-9.6852561053, -4.9181751543), (-9.5906737766, -4.8735863422))
                Line((-9.5906737766, -4.8735863422), (-9.3707386216, -4.9181751543))
                Line((-9.3707386216, -4.9181751543), (-9.2134798797, -4.7722845142))
                Line((-9.2134798797, -4.7722845142), (-9.0936867699, -4.7965709112))
                Line((-9.0936867699, -4.7965709112), (-8.9945535383, -4.7046039372))
                Line((-8.9945535383, -4.7046039372), (-8.9882841334, -4.6736799797))
                Line((-8.9882841334, -4.6736799797), (-8.9945535383, -4.5013447541))
                Line((-8.9945535383, -4.5013447541), (-8.9010357385, -4.4145872772))
                Line((-8.9010357385, -4.4145872772), (-8.7065084248, -4.4540250008))
                Line((-8.7065084248, -4.4540250008), (-8.6848631449, -4.4145872772))
                Line((-8.6848631449, -4.4145872772), (-8.6480920622, -4.3804743451))
                Line((-8.6480920622, -4.3804743451), (-8.5000001267, -4.3500000648))
                Line((-8.5000001267, -4.3500000648), (-8.5238150358, -3.8438895321))
                Line((-8.5238150358, -3.8438895321), (-8.084248432, -3.7851543393))
                Line((-8.084248432, -3.7851543393), (-8.0020979767, -3.7089424712))
                Line((-8.0020979767, -3.7089424712), (-7.8141397398, -3.7470484053))
                Line((-7.8141397398, -3.7470484053), (-7.5500001125, -3.6500000544))
                Line((-7.5500001125, -3.6500000544), (-7.3874449556, -3.6165495401))
                Line((-7.3874449556, -3.6165495401), (-7.234921065, -3.5851632545))
                Line((-7.234921065, -3.5851632545), (-6.5500000976, -3.5500000529))
                Line((-6.5500000976, -3.5500000529), (-5.5545232606, -3.2325635663))
                Line((-5.5545232606, -3.2325635663), (-4.7750319293, -2.9840002845))
                Line((-4.7750319293, -2.9840002845), (-4.5000000671, -2.8000000417))
                Line((-4.5000000671, -2.8000000417), (-3.8434389229, -2.6869349988))
                Line((-3.8434389229, -2.6869349988), (-3.6017086251, -2.6098523249))
                Line((-3.6017086251, -2.6098523249), (-3.4915628978, -2.5361632607))
                Line((-3.4915628978, -2.5361632607), (-3.3819614078, -2.5397795898))
                Line((-3.3819614078, -2.5397795898), (-3.2894678527, -2.3479857146))
                Line((-3.2894678527, -2.3479857146), (-2.9839624745, -2.2953752624))
                Line((-2.9839624745, -2.2953752624), (-2.7000000402, -2.1000000313))
                Line((-2.7000000402, -2.1000000313), (-2.3000000343, -2.1000000313))
                Line((-2.3000000343, -2.1000000313), (-1.9120176391, -2.0710456443))
                Line((-1.9120176391, -2.0710456443), (-1.5471175389, -1.8878265292))
                Line((-1.5471175389, -1.8878265292), (-1.1897123463, -1.9794360868))
                Line((-1.1897123463, -1.9794360868), (-1.1364903573, -1.7717960135))
                Line((-1.1364903573, -1.7717960135), (-0.9203955378, -1.5731446467))
                Line((-0.9203955378, -1.5731446467), (-0.5740115222, -1.3992225984))
                Line((-0.5740115222, -1.3992225984), (-0.4642667701, -1.3803236806))
                Line((-0.4642667701, -1.3803236806), (-0.3481105299, -1.273543722))
                Line((-0.3481105299, -1.273543722), (-0.0044681331, -1.1132505318))
                Line((-0.0044681331, -1.1132505318), (0.2450015759, -1.0702898668))
                Line((0.2450015759, -1.0702898668), (0.3604377058, -0.9430389352))
                Line((0.3604377058, -0.9430389352), (0.6419892656, -1.006664401))
                Line((0.6419892656, -1.006664401), (0.8249335311, -0.8384876327))
                Line((0.8249335311, -0.8384876327), (1.0725221829, -0.6108846563))
                Line((1.0725221829, -0.6108846563), (1.4843342606, -0.7039465996))
                Line((1.4843342606, -0.7039465996), (1.7097372784, -0.8384876327))
                Line((1.7097372784, -0.8384876327), (1.8884398747, -0.7246861445))
                Line((1.8884398747, -0.7246861445), (2.1595191787, -0.8864909418))
                Line((2.1595191787, -0.8864909418), (2.2503126322, -0.8864909418))
                Line((2.2503126322, -0.8864909418), (2.3615072926, -1.007449536))
                Line((2.3615072926, -1.007449536), (2.5585746108, -1.007449536))
                Line((2.5585746108, -1.007449536), (2.9284889851, -0.7246861445))
                Line((2.9284889851, -0.7246861445), (3.3000000492, -0.7246861445))
                Line((3.3000000492, -0.7246861445), (3.3808091796, -0.5893027493))
                Line((3.3808091796, -0.5893027493), (3.7147804088, -0.6569944469))
                Line((3.7147804088, -0.6569944469), (3.9000000581, -0.6569944469))
                Line((3.9000000581, -0.6569944469), (4.5109004753, -0.7246861445))
                Line((4.5109004753, -0.7246861445), (4.8838454855, -0.7660108517))
                Line((4.8838454855, -0.7660108517), (5.3119348631, -0.8660678402))
                Line((5.3119348631, -0.8660678402), (5.7345665033, -0.816039346))
                Line((5.7345665033, -0.816039346), (5.9047956515, -0.7958886825))
                Line((5.9047956515, -0.7958886825), (6.1839226165, -0.5624757842))
                Line((6.1839226165, -0.5624757842), (6.7114232871, -0.500033549))
                Line((6.7114232871, -0.500033549), (6.9502996372, -0.5624757842))
                Line((6.9502996372, -0.5624757842), (7.1107974426, -0.5312546666))
                Line((7.1107974426, -0.5312546666), (7.3274694799, -0.6547620223))
                Line((7.3274694799, -0.6547620223), (7.4929852437, -0.6351692998))
                Line((7.4929852437, -0.6351692998), (7.5985837281, -0.5468652254))
                Line((7.5985837281, -0.5468652254), (7.6785584292, -0.5163326651))
                Line((7.6785584292, -0.5163326651), (7.5457844859, -0.3959593111))
                Line((7.5457844859, -0.3959593111), (7.6121714576, -0.275585957))
                Line((7.6121714576, -0.275585957), (7.4658988371, -0.0589139197))
                Line((7.4658988371, -0.0589139197), (7.6121714576, 0.1096087759))
                Line((7.6121714576, 0.1096087759), (7.6785584292, 0.336311926))
                Line((7.6785584292, 0.336311926), (7.720079461, 0.4781010219))
                Line((7.720079461, 0.4781010219), (7.7862560766, 0.5980929567))
                Line((7.7862560766, 0.5980929567), (7.5789779717, 0.7124086687))
                Line((7.5789779717, 0.7124086687), (7.4773116133, 0.9704126763))
                Line((7.4773116133, 0.9704126763), (7.4858439553, 0.9858835828))
                Line((7.4858439553, 0.9858835828), (7.7248394714, 0.9013351345))
                Line((7.7248394714, 0.9013351345), (7.850000117, 0.8000000119))
                Line((7.850000117, 0.8000000119), (7.8764262992, 0.9781481296))
                Line((7.8764262992, 0.9781481296), (7.7248394714, 1.2582357672))
                Line((7.7248394714, 1.2582357672), (7.5789779717, 1.2582357672))
                Line((7.5789779717, 1.2582357672), (7.5000001118, 1.2000000179))
                Line((7.5000001118, 1.2000000179), (7.2374590376, 1.2582357672))
                Line((7.2374590376, 1.2582357672), (7.2000001073, 1.6000000238))
                Line((7.2000001073, 1.6000000238), (7.6053417133, 1.5100888653))
                Line((7.6053417133, 1.5100888653), (7.7874197942, 1.9104324729))
                Line((7.7874197942, 1.9104324729), (8.0000001192, 1.9104324729))
                Line((8.0000001192, 1.9104324729), (7.6963807538, 2.4257227035))
                Line((7.6963807538, 2.4257227035), (7.4912054158, 2.5190373738))
                Line((7.4912054158, 2.5190373738), (7.3687295747, 2.8652742071))
                Line((7.3687295747, 2.8652742071), (7.7248394714, 3.3051112885))
                Line((7.7248394714, 3.3051112885), (7.850000117, 3.3968583089))
                Line((7.850000117, 3.3968583089), (7.7874197942, 3.5737716706))
                Line((7.7874197942, 3.5737716706), (7.546784523, 3.5737716706))
                Line((7.546784523, 3.5737716706), (7.546784523, 3.8000000566))
                Line((7.546784523, 3.8000000566), (7.7248394714, 4.0199185973))
                Line((7.7248394714, 4.0199185973), (7.7248394714, 4.2000000626))
                Line((7.7248394714, 4.2000000626), (7.8792692646, 4.1297646952))
                Line((7.8792692646, 4.1297646952), (7.8792692646, 4.3000000641))
                Line((7.8792692646, 4.3000000641), (7.802054368, 4.3625163684))
                Line((7.802054368, 4.3625163684), (7.9612529226, 4.5591450729))
                Line((7.9612529226, 4.5591450729), (8.1000001207, 4.5591450729))
                Line((8.1000001207, 4.5591450729), (8.1895033436, 4.6696919483))
                Line((8.1895033436, 4.6696919483), (8.0306265217, 4.7983250514))
                Line((8.0306265217, 4.7983250514), (7.8923526554, 4.9102771681))
                Line((7.8923526554, 4.9102771681), (8.0306265217, 5.0810614522))
                Line((8.0306265217, 5.0810614522), (8.1895033436, 5.1369102685))
                Line((8.1895033436, 5.1369102685), (8.0306265217, 5.3708072733))
                Line((8.0306265217, 5.3708072733), (8.1447517322, 5.5621775499))
                Line((8.1447517322, 5.5621775499), (8.3000001237, 5.5621775499))
                Line((8.3000001237, 5.5621775499), (8.4215224675, 5.7122717582))
                Line((8.4215224675, 5.7122717582), (8.5000001267, 6.0000000894))
                Line((8.5000001267, 6.0000000894), (8.7484831872, 6.185902896))
                Line((8.7484831872, 6.185902896), (8.8462201865, 6.5442431419))
                Line((8.8462201865, 6.5442431419), (9.0957848004, 6.9442962144))
                Line((9.0957848004, 6.9442962144), (9.1868152376, 7.2780477056))
                Line((9.1868152376, 7.2780477056), (9.3000001386, 7.5000001118))
                Line((9.3000001386, 7.5000001118), (9.3587452964, 7.7153817426))
                Line((9.3587452964, 7.7153817426), (9.7753870362, 8.3000001535))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


# Description: This is an elliptical or oblong ring-shaped component with a hollow center, featuring a ribbed or finned exterior surface and an internal framework of triangulated cross-bracing, suggesting it functions as a structural reinforcement or suspension element.
def model_115617_418b75dd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 477.6609031879, perimeter: 79.1104540339
            with BuildLine():
                CenterArc((0, 0), 10.0443407203, 0, 180)
                Line((-10.0443407203, 0), (-10.0443407203, -8))
                CenterArc((0, -8), 10.0443407203, 180, 180)
                Line((10.0443407203, -8), (10.0443407203, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a hexagonal or irregularly-shaped hollow box structure with multiple interconnected cubic/prismatic chambers, featuring open passages and internal dividers that create a complex multi-chambered geometry with angular facets and recessed sections.
def model_115637_5c72f933_0000():
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
        # Sketch2 -> Extrude1 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0300000035, perimeter: 0.7000000365
            with BuildLine():
                Line((0.1000000015, -0.3499999922), (-0.1000000015, -0.3499999922))
                Line((-0.1000000015, -0.5000000075), (-0.1000000015, -0.3499999922))
                Line((0.1000000015, -0.5000000075), (-0.1000000015, -0.5000000075))
                Line((0.1000000015, -0.3499999922), (0.1000000015, -0.5000000075))
            make_face()
            # Profile area: 0.0299999979, perimeter: 0.6999999769
            with BuildLine():
                Line((-0.2499999944, -0.1499999966), (-0.1000000015, -0.1499999966))
                Line((-0.2499999944, -0.3499999922), (-0.2499999944, -0.1499999966))
                Line((-0.1000000015, -0.3499999922), (-0.2499999944, -0.3499999922))
                Line((-0.1000000015, -0.3499999922), (-0.1000000015, -0.1499999966))
            make_face()
            # Profile area: 0.0399999997, perimeter: 0.799999997
            with BuildLine():
                Line((-0.1000000015, -0.3499999922), (-0.1000000015, -0.1499999966))
                Line((0.1000000015, -0.3499999922), (-0.1000000015, -0.3499999922))
                Line((0.1000000015, -0.1499999966), (0.1000000015, -0.3499999922))
                Line((-0.1000000015, -0.1499999966), (0.1000000015, -0.1499999966))
            make_face()
            # Profile area: 0.0299999979, perimeter: 0.6999999769
            with BuildLine():
                Line((0.1000000015, -0.1499999966), (0.1000000015, -0.3499999922))
                Line((0.2499999944, -0.3499999922), (0.1000000015, -0.3499999922))
                Line((0.2499999944, -0.1499999966), (0.2499999944, -0.3499999922))
                Line((0.1000000015, -0.1499999966), (0.2499999944, -0.1499999966))
            make_face()
            # Profile area: 0.0299999998, perimeter: 0.6999999993
            with BuildLine():
                Line((-0.1000000015, -0.1499999966), (-0.1000000015, 0))
                Line((-0.1000000015, -0.1499999966), (0.1000000015, -0.1499999966))
                Line((0.1000000015, 0), (0.1000000015, -0.1499999966))
                Line((-0.1000000015, 0), (0.1000000015, 0))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a mounting bracket or clamp assembly with an angled rectangular base plate featuring two cylindrical protrusions (pins or posts) extending perpendicular from opposite sides, designed for mechanical attachment or pivot applications.
def model_116416_b2565d0a_0007():
    """Model: Shaft Mount Chrome"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.9522131577, perimeter: 43.0796447372
            with BuildLine():
                Line((-17.974886704, -4.6571825243), (-17.974886704, 5.3428174757))
                Line((-17.974886704, 5.3428174757), (-21.974886704, 5.3428174757))
                Line((-21.974886704, 5.3428174757), (-21.974886704, -4.6571825243))
                Line((-21.974886704, -4.6571825243), (-17.974886704, -4.6571825243))
            make_face()
            with BuildLine():
                CenterArc((-19.974886704, -2.6571825243), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-19.974886704, 3.3428174757), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.5132741229, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-19.974886704, -2.6571825243), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-19.974886704, -2.6571825243), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-19.974886704, -2.6571825243)):
                Circle(0.8)
            # Profile area: 2.5132741229, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-19.974886704, 3.3428174757), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-19.974886704, 3.3428174757), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-19.974886704, 3.3428174757)):
                Circle(0.8)
        # OneSide extrude, distance=-0.75
        extrude(amount=-0.75)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5132741229, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-19.974886704, 3.3428174757), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-19.974886704, 3.3428174757), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.5132741229, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-19.974886704, -2.6571825243), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-19.974886704, -2.6571825243), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


# Description: This is a triangular pyramid or wedge-shaped component with a flat rectangular base and a pointed apex, featuring a sloped upper surface and what appears to be an internal triangular cavity or cutout on one side.
def model_117699_6deeac69_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3925876575, perimeter: 5.6989153551
            with BuildLine():
                Line((-2.8494576776, -0.925844923), (-1.0883959833, 0.3536412923))
                Line((-0.6726657109, -0.925844923), (-2.8494576776, -0.925844923))
                Line((-1.0883959833, 0.3536412923), (-0.6726657109, -0.925844923))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved belt or band component with a hollow C-shaped cross-section, featuring a mesh or textured outer surface and smooth inner surfaces, designed to wrap around or guide cylindrical objects.
def model_117852_77bf0ad1_0000():
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
        # Sketch has 33 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1816233191, perimeter: 1.9529865527
            with BuildLine():
                Line((1.7, 2.95), (1.7, 2.7))
                CenterArc((1.7, 1.9), 1.05, 90, 44.9999984632)
                Line((1.1343145902, 2.4656854401), (0.9575378997, 2.6424621402))
                CenterArc((1.7, 1.9), 0.8, 90, 44.9999984632)
            make_face()
            # Profile area: 1.2784410199, perimeter: 6.8156015239
            with BuildLine():
                Line((0.7807612091, 2.8192388402), (0.7100505329, 2.8899495202))
                _nurbs_edge([(0.7100505329, 2.8899495202), (0.6781001184, 2.8651183509), (0.6056071292, 2.8046326981), (0.4964934305, 2.697836701), (0.3591057222, 2.525293241), (0.2102978255, 2.2563684817), (0.0899981961, 1.9126903433), (0.0286707852, 1.5839868235), (0.0052130293, 1.3049447289), (0, 1.1041152757), (0, 1)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4233405789, 0.4233405789, 0.4233405789, 0.4233405789, 0.4233405789, 0.4233405789, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (0, 1))
                Line((0, 0), (0.65, 0))
                Line((0.65, 1.1335145142), (0.65, 0))
                CenterArc((1.7, 1.9), 1.3, -180, 36.1289274719)
                CenterArc((1.7, 1.9), 1.3, 134.9999984632, 45.0000015368)
            make_face()
            # Profile area: 0.042499861, perimeter: 2.179174301
            with BuildLine():
                Line((1.7, 3.2), (1.6210569629, 3.2))
                _nurbs_edge([(1.6210569629, 3.2), (1.5865742231, 3.1992545808), (1.5023746849, 3.1954126998), (1.3701284856, 3.1813984364), (1.1928314535, 3.144596724), (1.011061086, 3.0780950931), (0.8672044948, 3.001269323), (0.77142633, 2.9367681861), (0.719778511, 2.8975098939), (0.7100505329, 2.8899495202)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0312973239, 0.0312973239, 0.0312973239, 0.0312973239, 0.0312973239, 0.0312973239, 0.1, 0.2, 0.3, 0.4, 0.4233405789, 0.4233405789, 0.4233405789, 0.4233405789, 0.4233405789, 0.4233405789], 5)
                Line((0.7807612091, 2.8192388402), (0.7100505329, 2.8899495202))
                CenterArc((1.7, 1.9), 1.3, 90, 44.9999984632)
            make_face()
            # Profile area: 0.2307107156, perimeter: 2.3456857411
            with BuildLine():
                Line((0.9575378997, 2.6424621402), (0.7807612091, 2.8192388402))
                CenterArc((1.7, 1.9), 1.3, 134.9999984632, 45.0000015368)
                Line((0.65, 1.9), (0.400000006, 1.9))
                CenterArc((1.7, 1.9), 1.05, 134.9999984632, 45.0000015368)
            make_face()
            # Profile area: 0.1304257026, perimeter: 1.8362248414
            with BuildLine():
                Line((0.65, 1.9), (0.400000006, 1.9))
                CenterArc((1.7, 1.9), 1.3, -180, 36.1289274719)
                Line((0.65, 1.9), (0.65, 1.1335145142))
            make_face()
            # Profile area: 0.2481092204, perimeter: 2.6193793302
            with BuildLine():
                CenterArc((1.7, 1.9), 1.3, -143.8710725281, 15.8912000832)
                Line((0.65, 1.1335145142), (0.65, 0))
                Line((0.65, 0), (0.9, 0))
                Line((0.9, 0.8753049234), (0.9, 0))
            make_face()
            # Profile area: 0.3632466506, perimeter: 3.4059732046
            with BuildLine():
                CenterArc((1.7, 1.9), 0.8, 0, 90)
                Line((2.5, 1.9), (2.75, 1.9))
                CenterArc((1.7, 1.9), 1.05, 0, 90)
                Line((1.7, 2.95), (1.7, 2.7))
            make_face()
            # Profile area: 0.1105384254, perimeter: 2.211441719
            with BuildLine():
                CenterArc((1.7, 1.9), 1.05, -180, 40.3675935442)
                Line((0.65, 1.9), (0.65, 1.1335145142))
                CenterArc((1.7, 1.9), 1.3, -143.8710725281, 15.8912000832)
                Line((0.9, 1.2199264746), (0.9, 0.8753049234))
            make_face()
            # Profile area: 0.461421421, perimeter: 4.191371368
            with BuildLine():
                Line((3, 1.9), (2.75, 1.9))
                CenterArc((1.7, 1.9), 1.3, 0, 90)
                Line((1.7, 3.2), (1.7, 2.95))
                CenterArc((1.7, 1.9), 1.05, 0, 90)
            make_face()
            # Profile area: 0.1163523542, perimeter: 1.6698483148
            with BuildLine():
                Line((0.9, 1.9), (0.65, 1.9))
                CenterArc((1.7, 1.9), 1.05, -180, 40.3675935442)
                Line((0.9, 1.9), (0.9, 1.2199264746))
            make_face()
            # Profile area: 0.1816233315, perimeter: 1.9529866519
            with BuildLine():
                Line((1.1343145902, 2.4656854401), (0.9575378997, 2.6424621402))
                CenterArc((1.7, 1.9), 1.05, 134.9999984632, 45.0000015368)
                Line((0.9, 1.9), (0.65, 1.9))
                CenterArc((1.7, 1.9), 0.8, 134.9999984632, 45.0000015368)
            make_face()
            # Profile area: 0.2307107026, perimeter: 2.345685621
            with BuildLine():
                Line((1.7, 3.2), (1.7, 2.95))
                CenterArc((1.7, 1.9), 1.3, 90, 44.9999984632)
                Line((0.9575378997, 2.6424621402), (0.7807612091, 2.8192388402))
                CenterArc((1.7, 1.9), 1.05, 90, 44.9999984632)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a black plastic clip or fastener with an elongated, curved rectangular body featuring a central slot and a protruding base flange for mounting or securing purposes.
def model_118022_d715d1fb_0000():
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
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 171.2774344061, perimeter: 60.2932550569
            with BuildLine():
                Line((1.4940071994, 4.5175931981), (0.5691455998, -16.0427915931))
                _nurbs_edge([(1.4940071994, 4.5175931981), (1.7436194614, 5.0001769046), (2.2728285107, 5.8877645618), (3.1565937274, 6.9864068172), (4.4975320164, 7.9915342523), (6.3392408847, 8.5217419813), (8.2030992132, 8.3888270946), (9.9310483756, 7.6765890707), (11.3747615582, 6.4879901151), (12.4172815435, 4.9429692694), (13.0020646879, 3.1789035765), (13.1355222043, 1.3422271671), (12.866368557, -0.4279766868), (12.2722538466, -2.0138268472), (11.4436807673, -3.3343950594), (10.4700757888, -4.3595661003), (9.4235643242, -5.1289430686), (8.348374271, -5.7582855865), (7.2706370749, -6.3971336053), (6.2047819957, -7.1950826676), (5.1613330667, -8.2634130505), (4.1535475635, -9.6415277248), (3.2058292929, -11.2522112229), (2.3508127159, -12.9297547274), (1.6240626615, -14.4633253696), (1.0596745322, -15.6339508662), (0.7601540119, -16.1309143769), (0.6285157645, -16.203632989), (0.5820550265, -16.118635186), (0.5691455998, -16.0427915931)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=2.7891
        extrude(amount=2.7891)
    return part.part


# Description: This is a dark blue/gray composite or plastic U-shaped channel or tray with a curved bottom, raised flanges on both sides, and textured cylindrical posts or bosses at each corner for mounting or assembly purposes.
def model_118360_4167ef76_0000():
    """Model: saddle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.660297301, perimeter: 3.3942615051
            with BuildLine():
                CenterArc((3.1749994914, -0.0017970644), 0.6350020343, -95.7716185977, 191.4783778501)
                CenterArc((0, 0), 3.175, -0.0324296726, 11.4783778501)
                CenterArc((0, 0), 3.175, -11.5108075227, 11.4783778501)
            make_face()
            # Profile area: 0.3032397546, perimeter: 2.2049173101
            with BuildLine():
                CenterArc((3.1749994914, -0.0017970644), 0.6350020343, -179.9027112938, 84.1310926961)
                CenterArc((0, 0), 3.175, -11.5108075227, 11.4783778501)
                Line((3.1749994914, -0.0017970644), (2.5399995931, -0.0014376515))
                CenterArc((0, 0), 2.54, -0.0648593453, 0.0324296726)
            make_face()
            # Profile area: 5.0939815283, perimeter: 18.5468999154
            with BuildLine():
                CenterArc((0, 0), 2.54, 179.9675703231, 179.9675703316)
                CenterArc((-3.1749994914, 0.0017970644), 0.635, -84.2932591954, 84.2608295397)
                CenterArc((0, 0), 3.175, -168.5540887181, 157.0432811954)
                CenterArc((3.1749994914, -0.0017970644), 0.6350020343, -179.9027112938, 84.1310926961)
            make_face()
            # Profile area: 0.3032397546, perimeter: 2.2049173101
            with BuildLine():
                CenterArc((0, 0), 3.175, -0.0324296726, 11.4783778501)
                CenterArc((3.1749994914, -0.0017970644), 0.6350020343, 95.7067592524, 84.1310926961)
                CenterArc((0, 0), 2.54, -0.0324296726, 0.0324296726)
                Line((3.1749994914, -0.0017970644), (2.5399995931, -0.0014376515))
            make_face()
            # Profile area: 0.660292984, perimeter: 3.3942502087
            with BuildLine():
                CenterArc((0, 0), 3.175, 179.9675703274, 11.4783409545)
                CenterArc((0, 0), 3.175, 168.4892293728, 11.4783409545)
                CenterArc((-3.1749994914, 0.0017970644), 0.635, 84.2283998501, 191.4783409545)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124796
            with BuildLine():
                Line((-2.5399995931, 0.0014376517), (-3.1749994914, 0.0017970644))
                CenterArc((0, 0), 3.175, 179.9675703274, 11.4783409545)
                CenterArc((-3.1749994914, 0.0017970644), 0.635, -84.2932591954, 84.2608295397)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124793
            with BuildLine():
                CenterArc((-3.1749994914, 0.0017970644), 0.635, -0.0324296556, 84.2608295057)
                CenterArc((0, 0), 3.175, 168.4892293728, 11.4783409545)
                Line((-2.5399995931, 0.0014376517), (-3.1749994914, 0.0017970644))
            make_face()
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.660297301, perimeter: 3.3942615051
            with BuildLine():
                CenterArc((3.1749994914, -0.0017970644), 0.6350020343, -95.7716185977, 191.4783778501)
                CenterArc((0, 0), 3.175, -0.0324296726, 11.4783778501)
                CenterArc((0, 0), 3.175, -11.5108075227, 11.4783778501)
            make_face()
            # Profile area: 0.3032397546, perimeter: 2.2049173101
            with BuildLine():
                CenterArc((3.1749994914, -0.0017970644), 0.6350020343, -179.9027112938, 84.1310926961)
                CenterArc((0, 0), 3.175, -11.5108075227, 11.4783778501)
                Line((3.1749994914, -0.0017970644), (2.5399995931, -0.0014376515))
                CenterArc((0, 0), 2.54, -0.0648593453, 0.0324296726)
            make_face()
            # Profile area: 0.3032397546, perimeter: 2.2049173101
            with BuildLine():
                CenterArc((0, 0), 3.175, -0.0324296726, 11.4783778501)
                CenterArc((3.1749994914, -0.0017970644), 0.6350020343, 95.7067592524, 84.1310926961)
                CenterArc((0, 0), 2.54, -0.0324296726, 0.0324296726)
                Line((3.1749994914, -0.0017970644), (2.5399995931, -0.0014376515))
            make_face()
            # Profile area: 0.660292984, perimeter: 3.3942502087
            with BuildLine():
                CenterArc((0, 0), 3.175, 179.9675703274, 11.4783409545)
                CenterArc((0, 0), 3.175, 168.4892293728, 11.4783409545)
                CenterArc((-3.1749994914, 0.0017970644), 0.635, 84.2283998501, 191.4783409545)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124796
            with BuildLine():
                Line((-2.5399995931, 0.0014376517), (-3.1749994914, 0.0017970644))
                CenterArc((0, 0), 3.175, 179.9675703274, 11.4783409545)
                CenterArc((-3.1749994914, 0.0017970644), 0.635, -84.2932591954, 84.2608295397)
            make_face()
            # Profile area: 0.3032378569, perimeter: 2.2049124793
            with BuildLine():
                CenterArc((-3.1749994914, 0.0017970644), 0.635, -0.0324296556, 84.2608295057)
                CenterArc((0, 0), 3.175, 168.4892293728, 11.4783409545)
                Line((-2.5399995931, 0.0014376517), (-3.1749994914, 0.0017970644))
            make_face()
        # Symmetric extrude, each_side=0.508
        extrude(amount=0.508, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an elongated cylindrical housing or enclosure with an oval shape, featuring a mesh or perforated pattern on its outer surface, two small rectangular mounting holes on opposite sides, and a split or open design along its length.
def model_118459_55a06bd6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.780972451, perimeter: 47.1238898038
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


# Description: This is a clamp or bracket component with an elongated, tapered body featuring two cylindrical holes or mounting points along its length and a curved grip section at the bottom.
def model_118700_df55782f_0000():
    """Model: right panel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 47 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 37.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9274.3595429319, perimeter: 503.8570705894
            with BuildLine():
                Line((5, -22.5), (5, 22.5))
                Line((5, -105), (5, -22.5))
                CenterArc((7.5, -105), 2.5, 180, 90)
                Line((15, -107.5), (7.5, -107.5))
                CenterArc((15, -105), 2.5, -90, 90)
                Line((17.5, -105), (17.5, -95))
                CenterArc((22.5, -95), 5, 90, 90)
                Line((22.5, -90), (37.5, -90))
                CenterArc((37.5, -95), 5, 0, 90)
                Line((42.5, -95), (42.5, -105.1))
                CenterArc((44.9, -105.1), 2.4, -180, 90)
                Line((52.5, -107.5), (44.9, -107.5))
                CenterArc((52.5, -105), 2.5, -90, 90)
                Line((55, -67.5), (55, -105))
                CenterArc((55, -55.5), 12, -90, 90)
                Line((67, -34.5), (67, -55.5))
                CenterArc((55, -34.5), 12, 0, 90)
                Line((55, 22.5), (55, -22.5))
                CenterArc((55, 34.5), 12, -90, 90)
                Line((67, 55.5), (67, 34.5))
                CenterArc((55, 55.5), 12, 0, 90)
                Line((5, 67.5), (55, 67.5))
                Line((5, 22.5), (5, 67.5))
            make_face()
            # Profile area: 256.7634483774, perimeter: 91.201925721
            with BuildLine():
                CenterArc((5, -10.5), 12, 180, 65.3756816478)
                Line((0, 21.4087121146), (0, -21.4087121146))
                CenterArc((5, 10.5), 12, 114.6243183522, 65.3756816478)
                Line((-7, 10.5), (-7, -10.5))
            make_face()
            # Profile area: 221.431222681, perimeter: 98.1320345806
            with BuildLine():
                Line((0, 21.4087121146), (0, -21.4087121146))
                CenterArc((5, -10.5), 12, -114.6243183522, 24.6243183522)
                Line((5, -22.5), (5, 22.5))
                CenterArc((5, 10.5), 12, 90, 24.6243183522)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a hexagonal or polygonal prism-shaped component with a tapered top surface featuring multiple triangular facets, resembling a truncated pyramidal form with flat side faces and a subdivided upper surface.
def model_119790_1ed376f0_0003():
    """Model: Mutteri M8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0227092639, perimeter: 1.4275265604
            with BuildLine():
                CenterArc((0, 0), 0.65, 90.1635611341, 59.8366437499)
                Line((-0.0018555397, 0.6499973515), (-0.3752807332, 0.6499973515))
                Line((-0.3752807332, 0.6499973515), (-0.5629176746, 0.3249979871))
            make_face()
            # Profile area: 0.0227097576, perimeter: 1.4312264075
            with BuildLine():
                Line((-0.5629148659, -0.3250028519), (-0.3752761459, -0.65))
                Line((-0.3752761459, -0.65), (0, -0.65))
                CenterArc((0, 0), 0.65, -149.9997097241, 59.9997097241)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312356957
            with BuildLine():
                Line((-0.5629176746, 0.3249979871), (-0.7505553499, -0.0000026485))
                Line((-0.7505553499, -0.0000026485), (-0.5629148659, -0.3250028519))
                CenterArc((0, 0), 0.65, 150.000204884, 60.0000853919)
            make_face()
            # Profile area: 0.6648675431, perimeter: 3.3438894378
            with BuildLine():
                CenterArc((0, 0), 0.65, 150.000204884, 60.0000853919)
                CenterArc((0, 0), 0.65, -149.9997097241, 59.9997097241)
                Line((0.0018555397, 0.6499973515), (0, -0.65))
                Line((0.0018555397, 0.6499973515), (-0.0018555397, 0.6499973515))
                CenterArc((0, 0), 0.65, 90.1635611341, 59.8366437499)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a trapezoidal frame or bezel with a hollow rectangular opening, featuring a sloped left side, parallel top and bottom edges, and a perpendicular right side, with what appears to be reinforced or textured inner walls.
def model_119880_14a41c0d_0000():
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
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.526138021, perimeter: 58.6291773607
            with BuildLine():
                _nurbs_edge([(3.5, 7.5), (3.4391384029, 7.4275012873), (3.3203347706, 7.2770641379), (3.1508881128, 7.0350890467), (2.9427641341, 6.6792815282), (2.714044343, 6.17595214), (2.5187578538, 5.6103298672), (2.358126042, 4.980139045), (2.2306901223, 4.2880976803), (2.1334813014, 3.5397372244), (2.0633280044, 2.7409669521), (2.0267096139, 2.0656104464), (2.0094510434, 1.5400787104), (2.0024067458, 1.1814117151), (2, 1)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((12.72874955, 1), (2, 1))
                Line((13, 1), (12.72874955, 1))
                _nurbs_edge([(10.5, 7.5), (10.5924829801, 7.3916284577), (10.7737102689, 7.1729819826), (11.0343353815, 6.8393021975), (11.3590331739, 6.3827869369), (11.7243472856, 5.7914943623), (12.0455772057, 5.1777581392), (12.3192783979, 4.5398246239), (12.5438538311, 3.8768807541), (12.7215723292, 3.1900816077), (12.8561063665, 2.4812968736), (12.9320887135, 1.898158399), (12.9724167704, 1.4523234512), (12.9920194275, 1.1513924589), (13, 1)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((3.5, 7.5), (10.5, 7.5))
            make_face()
            with BuildLine():
                Line((3.8455356699, 6.8), (10.1713769485, 6.8))
                _nurbs_edge([(10.1713769485, 6.8), (10.6363998824, 6.2236976565), (11.03380203, 5.619201896), (11.3479092061, 4.9819551395), (11.6689103177, 4.3307222716), (11.9012156049, 3.6392594123), (12.0579698056, 2.8920802145), (12.1386541262, 2.5074930983), (12.1997311742, 2.1093910058), (12.2429792882, 1.7)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0476617325, 0.0476617325, 0.0476617325, 0.0476617325, 0.3808025958, 0.3808025958, 0.3808025958, 0.7212551404, 0.7212551404, 0.7212551404, 0.8964924365, 0.8964924365, 0.8964924365, 0.8964924365], 3)
                Line((12.2429792882, 1.7), (2.7167762105, 1.7))
                _nurbs_edge([(3.8455356699, 6.8), (3.554243891, 6.3802884241), (3.3055027556, 5.8341869024), (3.1222893348, 5.119500822), (2.8901821172, 4.2140879065), (2.7631611715, 3.0371520879), (2.7167762105, 1.7)], [1, 1, 1, 1, 1, 1, 1], [0.0783830178, 0.0783830178, 0.0783830178, 0.0783830178, 0.4490476892, 0.4490476892, 0.4490476892, 0.9186308951, 0.9186308951, 0.9186308951, 0.9186308951], 3)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rubber or elastomer O-ring seal, characterized by its circular torus shape with a uniform cross-section, designed to create a watertight or airtight seal in mechanical assemblies.
def model_119881_f122be32_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.3517687778, perimeter: 53.407075111
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a curved bucket or scoop with a cylindrical body, reinforcing ribs on the interior surface, a flat rectangular top opening, and angled side flanges for structural support.
def model_119886_382e5a3f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.839791435, perimeter: 14.4942077007
            with BuildLine():
                CenterArc((1.298961345, 3.8998764925), 0.3, 27.2618859097, 62.7330532551)
                Line((-0.0999911687, 4.2000000607), (1.2989878435, 4.1998764914))
                CenterArc((-0.1000000015, 4.1000000611), 0.1, 89.9949391647, 90)
                Line((-0.2000265188, 3.799790745), (-0.2000000011, 4.1000088939))
                CenterArc((-2.200026511, 3.7999674015), 2, -90.0050608352, 90)
                Line((-2.1961151333, 1.7999670482), (-2.2002031675, 1.7999674093))
                CenterArc((-2.1961946287, 0.8999670517), 0.9, 89.9949391648, 90.0050600669)
                Line((-3.0961946287, 0.8999670638), (-3.0961946408, 0.000000026))
                Line((-3.0961946408, 0.000000026), (-3.0961946408, -0.4082878122))
                Line((1.5656379862, 4.0372939916), (-3.0961946408, -0.4082878122))
            make_face()
            # Profile area: 2.2161813068, perimeter: 16.9305280417
            with BuildLine():
                Line((1.505998059, 3.6827686873), (-2.4341232329, -0.0745801756))
                CenterArc((1.298961345, 3.8998764925), 0.3, -46.360202922, 73.6220888317)
                Line((1.5656379862, 4.0372939916), (-3.0961946408, -0.4082878122))
                Line((-3.0961946408, -0.4082878122), (-3.0961946408, -0.8561069578))
                CenterArc((-2.9961946408, -0.8561069578), 0.1, 180, 90)
                Line((-2.9961946408, -0.9561069578), (-1.8104584968, -0.9561069578))
                Line((-1.8104584968, -0.9561069578), (-0.9088622956, -0.9561069578))
                CenterArc((-1.1259017649, -1.1632153081), 0.3, 43.6587052382, 26.8761929067)
                Line((-2.3627452861, -0.4078876391), (-1.025931971, -0.880361918))
                CenterArc((-2.2960987569, -0.2193187124), 0.2, 133.639797078, 116.8951010669)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a low-poly 3D model of a stylized fish or aquatic creature featuring a segmented geometric body composed of angular, faceted sections with a dark silhouette and blue-shaded interior surfaces, including a prominent head section, elongated body segments, and a tail fin.
def model_119902_a18122ad_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 55 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3286149195, perimeter: 11.1095687511
            with BuildLine():
                Line((10.1130176098, 1.5256808177), (9.2275182715, 2.5038994822))
                Line((10.1130176098, 1.5256808177), (10.3243705879, 1.2931925418))
                Line((10.3243705879, 1.2931925418), (10.6444130873, 0.9411457924))
                Line((10.6444130873, 0.9411457924), (11.5000001714, 0))
                Line((13.3000001982, 0), (11.5000001714, 0))
                Line((13.3000001982, 0), (10.2200957684, 3.4023966676))
                Line((9.2275182715, 2.5038994822), (10.2200957684, 3.4023966676))
            make_face()
            # Profile area: 31.8109874809, perimeter: 96.1387990852
            with BuildLine():
                CenterArc((9.522365525, 6), 1, 90, 55.1620297155)
                Line((7.857862876, 5.3590016517), (8.7015947117, 6.5712576232))
                Line((6.9270647434, 4.0216506752), (7.857862876, 5.3590016517))
                Line((6.0829201143, 2.8088016111), (6.9270647434, 4.0216506752))
                Line((5.5745228387, 2.0783472094), (6.0829201143, 2.8088016111))
                CenterArc((3.9329812122, 3.2208624559), 2, -101.4406964967, 66.6027262122)
                Line((-10, 4), (3.5362740818, 1.2606013884))
                Line((-10, 0), (-10, 4))
                Line((-10, 0), (-5, 0))
                Line((-5, 0), (4.7, 0))
                Line((4.7, 0), (5, 0))
                Line((5, 0), (6.3530893876, 0))
                CenterArc((6.3530893876, 0.38), 0.38, -90, 42.2736890061)
                Line((6.6087050493, 0.0988227721), (7.0543991015, 0.5039991831))
                Line((7.7885453268, 1.1943625382), (7.0543991015, 0.5039991831))
                Line((7.9864449442, 1.3804598566), (7.7885453268, 1.1943625382))
                Line((7.9864449442, 1.3804598566), (9.2275182715, 2.5038994822))
                Line((9.2275182715, 2.5038994822), (10.2200957684, 3.4023966676))
                Line((10.2200957684, 3.4023966676), (12.0831545299, 5.0888675566))
                Line((14, 7), (12.0831545299, 5.0888675566))
                Line((9.522365525, 7), (14, 7))
            make_face()
            with BuildLine():
                Line((-9.7, 0.3000000045), (-9.7, 3.633205928))
                Line((-9.7, 3.633205928), (1, 1.4388998961))
                Line((1, 0.3000000045), (1, 1.4388998961))
                Line((-9.7, 0.3000000045), (1, 0.3000000045))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((8.2398870856, 3.6760193208), 2.7860845563, 0.8489745322, 0, 360, -128.6448999574)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4440771513, perimeter: 3.8131554599
            with BuildLine():
                Line((7.7885453268, 1.1943625382), (8.8867861672, -0.0137023861))
                Line((8.8867861672, -0.0137023861), (9.0877660709, 0.1690066173))
                Line((8.8764130928, 0.4014948932), (9.0877660709, 0.1690066173))
                Line((7.9864449442, 1.3804598566), (8.8764130928, 0.4014948932))
                Line((7.9864449442, 1.3804598566), (7.7885453268, 1.1943625382))
            make_face()
            # Profile area: 13.0914187965, perimeter: 24.4266892332
            with BuildLine():
                Line((4, 9), (-7, 9))
                CenterArc((-7, 8.4), 0.6, 90, 127.4320084477)
                CenterArc((-7, 8.4), 0.6, -142.5679915523, 52.5679915523)
                Line((-7, 7.8), (2.526292838, 7.8))
                CenterArc((2.526292838, 6.8), 1, 72.6493424927, 17.3506575073)
                Line((2.8245117382, 7.7544975053), (4, 9))
            make_face()
            # Profile area: 16.6730810029, perimeter: 52.9372600085
            with BuildLine():
                Line((3.2126633686, 7.527252016), (6.9270647434, 4.0216506752))
                CenterArc((2.526292838, 6.8), 1, 46.6565128411, 25.9928296516)
                CenterArc((2.526292838, 6.8), 1, 72.6493424927, 17.3506575073)
                Line((-7, 7.8), (2.526292838, 7.8))
                CenterArc((-7, 8.4), 0.6, -142.5679915523, 52.5679915523)
                Line((-5, 4.8), (-7.4764451106, 8.0353082719))
                Line((2.4560147456, 5.7320018432), (-5, 4.8))
                CenterArc((2.5800494802, 4.7397239665), 1, 46.6565128411, 50.4685035078)
                Line((6.0829201143, 2.8088016111), (3.2664200107, 5.4669759825))
                Line((6.0829201143, 2.8088016111), (6.9270647434, 4.0216506752))
            make_face()
            with BuildLine():
                Line((-6.7000000998, 7.7500001155), (1.5000000224, 7.7500001155))
                Line((1.5000000224, 7.7500001155), (1.5000000224, 5.9148346684))
                Line((1.5000000224, 5.9148346684), (-5.3826679847, 5.9148346684))
                Line((-5.3826679847, 5.9148346684), (-6.7000000998, 7.7500001155))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 8.7569915337, perimeter: 14.2078192013
            with BuildLine():
                Line((6.3484134257, 6.783599449), (7.857862876, 5.3590016517))
                Line((4, 9), (6.3484134257, 6.783599449))
                Line((2.8245117382, 7.7544975053), (4, 9))
                CenterArc((2.526292838, 6.8), 1, 46.6565128411, 25.9928296516)
                Line((3.2126633686, 7.527252016), (6.9270647434, 4.0216506752))
                Line((6.9270647434, 4.0216506752), (7.857862876, 5.3590016517))
            make_face()
            # Profile area: 17.9919589035, perimeter: 20.25794246
            with BuildLine():
                Line((9.522365525, 7), (14, 7))
                Line((14, 7), (14, 9.5))
                Line((14, 9.5), (9.4312528017, 9.5))
                CenterArc((9.4312528017, 8.2962104951), 1.2037895049, 90, 46.6565128411)
                Line((8.5557944574, 9.1224561363), (6.3484134257, 6.783599449))
                Line((6.3484134257, 6.783599449), (7.857862876, 5.3590016517))
                Line((7.857862876, 5.3590016517), (8.7015947117, 6.5712576232))
                CenterArc((9.522365525, 6), 1, 90, 55.1620297155)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a rectangular connector housing or junction block with four dark cylindrical cavities arranged in a 2x2 grid pattern, featuring blue internal passages or channels visible through the translucent sections, designed to hold or connect multiple components or connectors.
def model_119907_90a6e5af_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 80 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.1557826502, perimeter: 21.9894566255
            with BuildLine():
                Line((-3, -5), (-3, -5.8))
                Line((-3, -5), (-9, -5))
                CenterArc((-9, -4), 1, 180, 90)
                Line((-10, -4), (-10, -2.0043865448))
                Line((-10.8, -2.0043865448), (-10, -2.0043865448))
                Line((-10.8, -4), (-10.8, -2.0043865448))
                CenterArc((-9, -4), 1.8, 180, 90)
                Line((-3, -5.8), (-9, -5.8))
            make_face()
            # Profile area: 10.3518079454, perimeter: 22.7036158908
            with BuildLine():
                Line((-10, -2.0043865448), (-10, -1.0043865448))
                Line((-10, -2.0043865448), (-4, -2.0043865448))
                CenterArc((-4, -3.0043865448), 1, 0, 90)
                Line((-3, -3.0043865448), (-3, -5))
                Line((-2, -5), (-3, -5))
                Line((-2, -3.0043865448), (-2, -5))
                CenterArc((-4, -3.0043865448), 2, 0, 90)
                Line((-10, -1.0043865448), (-4, -1.0043865448))
            make_face()
            # Profile area: 19.5305711562, perimeter: 41.0611423123
            with BuildLine():
                Line((-2, -5.8), (-3, -5.8))
                Line((-3, -5.8), (-3, -7))
                CenterArc((-4, -7), 1, -90, 90)
                Line((-4, -8), (-11.0331871152, -8))
                CenterArc((-11.0331871152, -7), 1, -180, 90)
                Line((-12.0331871152, -7), (-12.0331871152, -3.0043865448))
                CenterArc((-11.0331871152, -3.0043865448), 1, 90, 90)
                Line((-11.0331871152, -2.0043865448), (-10.8, -2.0043865448))
                Line((-10.8, -2.0043865448), (-10.8, -1.0043865448))
                Line((-11.0331871152, -1.0043865448), (-10.8, -1.0043865448))
                CenterArc((-11.0331871152, -3.0043865448), 2, 90, 90)
                Line((-13.0331871152, -7), (-13.0331871152, -3.0043865448))
                CenterArc((-11.0331871152, -7), 2, -180, 90)
                Line((-4, -9), (-11.0331871152, -9))
                CenterArc((-4, -7), 2, -90, 90)
                Line((-2, -5.8), (-2, -7))
            make_face()
            # Profile area: 5.759291886, perimeter: 15.998229715
            with BuildLine():
                Line((-10, 1), (-10.8, 1))
                Line((-10, 1), (-10, 3))
                CenterArc((-9, 3), 1, 90, 90)
                Line((-9, 4), (-6, 4))
                Line((-6, 4.8), (-6, 4))
                Line((-9, 4.8), (-6, 4.8))
                CenterArc((-9, 3), 1.8, 90, 90)
                Line((-10.8, 1), (-10.8, 3))
            make_face()
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((-10, 0), (-10.8, 0))
                Line((-10, 0), (-10, 1))
                Line((-10, 1), (-10.8, 1))
                Line((-10.8, 0), (-10.8, 1))
            make_face()
            # Profile area: 7.4801698614, perimeter: 16.9603397227
            with BuildLine():
                Line((6.9380123144, -0.9380123144), (10, -0.9380123144))
                CenterArc((6.9380123144, -2.9380123144), 2, 90, 90)
                Line((4.9380123144, -5), (4.9380123144, -2.9380123144))
                Line((5.9380123144, -5), (4.9380123144, -5))
                Line((5.9380123144, -5), (5.9380123144, -2.9380123144))
                CenterArc((6.9380123144, -2.9380123144), 1, 90, 90)
                Line((6.9380123144, -1.9380123144), (10, -1.9380123144))
                Line((10, -0.9380123144), (10, -1.9380123144))
            make_face()
            # Profile area: 16.4685834706, perimeter: 34.9371669412
            with BuildLine():
                Line((-10.8, 0), (-10.8, 1))
                Line((-10.8, 1), (-11, 1))
                CenterArc((-11, 2), 1, 180, 90)
                Line((-12, 2), (-12, 6))
                CenterArc((-11, 6), 1, 90, 90)
                Line((-11, 7), (-7, 7))
                CenterArc((-7, 6), 1, 0, 90)
                Line((-6, 6), (-6, 4.8))
                Line((-6, 4.8), (-5, 4.8))
                Line((-5, 6), (-5, 4.8))
                CenterArc((-7, 6), 2, 0, 90)
                Line((-11, 8), (-7, 8))
                CenterArc((-11, 6), 2, 90, 90)
                Line((-13, 2), (-13, 6))
                CenterArc((-11, 2), 2, 180, 90)
                Line((-10.8, 0), (-11, 0))
            make_face()
            # Profile area: 0.8035092358, perimeter: 3.6087730895
            with BuildLine():
                Line((-10.8, -1.0043865448), (-10, -1.0043865448))
                Line((-10, -1.0043865448), (-10, 0))
                Line((-10, 0), (-10.8, 0))
                Line((-10.8, -1.0043865448), (-10.8, 0))
            make_face()
            # Profile area: 5.8584721829, perimeter: 16.2461804573
            with BuildLine():
                Line((10, -1.9380123144), (10.8, -1.9380123144))
                Line((10, -1.9380123144), (10, -4))
                CenterArc((9, -4), 1, -90, 90)
                Line((9, -5), (5.9380123144, -5))
                Line((5.9380123144, -5.8), (5.9380123144, -5))
                Line((9, -5.8), (5.9380123144, -5.8))
                CenterArc((9, -4), 1.8, -90, 90)
                Line((10.8, -1.9380123144), (10.8, -4))
            make_face()
            # Profile area: 7.3561944902, perimeter: 16.7123889804
            with BuildLine():
                Line((-6, 4), (-5, 4))
                Line((-6, 4), (-6, 2))
                CenterArc((-7, 2), 1, -90, 90)
                Line((-7, 1), (-10, 1))
                Line((-10, 0), (-10, 1))
                Line((-7, 0), (-10, 0))
                CenterArc((-7, 2), 2, -90, 90)
                Line((-5, 4), (-5, 2))
            make_face()
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((-10.8, -2.0043865448), (-10.8, -1.0043865448))
                Line((-10.8, -2.0043865448), (-10, -2.0043865448))
                Line((-10, -2.0043865448), (-10, -1.0043865448))
                Line((-10.8, -1.0043865448), (-10, -1.0043865448))
            make_face()
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((-2, -5), (-2, -5.8))
                Line((-2, -5), (-3, -5))
                Line((-3, -5), (-3, -5.8))
                Line((-2, -5.8), (-3, -5.8))
            make_face()
            # Profile area: 16.5925588417, perimeter: 35.1851176835
            with BuildLine():
                Line((10.8, -0.9380123144), (10.8, -1.9380123144))
                Line((10.8, -1.9380123144), (11.0331871152, -1.9380123144))
                CenterArc((11.0331871152, -2.9380123144), 1, 0, 90)
                Line((12.0331871152, -2.9380123144), (12.0331871152, -6.9668128848))
                CenterArc((11.0331871152, -6.9668128848), 1, -90, 90)
                Line((11.0331871152, -7.9668128848), (6.9380123144, -7.9668128848))
                CenterArc((6.9380123144, -6.9668128848), 1, -180, 90)
                Line((5.9380123144, -6.9668128848), (5.9380123144, -5.8))
                Line((5.9380123144, -5.8), (4.9380123144, -5.8))
                Line((4.9380123144, -6.9668128848), (4.9380123144, -5.8))
                CenterArc((6.9380123144, -6.9668128848), 2, -180, 90)
                Line((11.0331871152, -8.9668128848), (6.9380123144, -8.9668128848))
                CenterArc((11.0331871152, -6.9668128848), 2, -90, 90)
                Line((13.0331871152, -2.9380123144), (13.0331871152, -6.9668128848))
                CenterArc((11.0331871152, -2.9380123144), 2, 0, 90)
                Line((10.8, -0.9380123144), (11.0331871152, -0.9380123144))
            make_face()
            # Profile area: 5.5504098515, perimeter: 15.4760246288
            with BuildLine():
                Line((4.9380123144, -5.8), (4.9380123144, -5))
                Line((4.9380123144, -5), (-2, -5))
                Line((-2, -5), (-2, -5.8))
                Line((4.9380123144, -5.8), (-2, -5.8))
            make_face()
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((-6, 4.8), (-5, 4.8))
                Line((-6, 4.8), (-6, 4))
                Line((-6, 4), (-5, 4))
                Line((-5, 4.8), (-5, 4))
            make_face()
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((5.9380123144, -5.8), (4.9380123144, -5.8))
                Line((5.9380123144, -5.8), (5.9380123144, -5))
                Line((5.9380123144, -5), (4.9380123144, -5))
                Line((4.9380123144, -5.8), (4.9380123144, -5))
            make_face()
            # Profile area: 5.6530993843, perimeter: 15.7327484607
            with BuildLine():
                Line((-5, 4.8), (2.0663742303, 4.8))
                Line((-5, 4.8), (-5, 4))
                Line((-5, 4), (2.0663742303, 4))
                Line((2.0663742303, 4), (2.0663742303, 4.8))
            make_face()
            # Profile area: 8.0761335738, perimeter: 21.7903339344
            with BuildLine():
                Line((3.0663742303, 4), (3.0663742303, 4.8))
                Line((3.0663742303, 4), (9, 4))
                CenterArc((9, 3), 1, 0, 90)
                Line((10, 3), (10, 1.0375736599))
                Line((10.8, 1.0375736599), (10, 1.0375736599))
                Line((10.8, 3), (10.8, 1.0375736599))
                CenterArc((9, 3), 1.8, 0, 90)
                Line((3.0663742303, 4.8), (9, 4.8))
            make_face()
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((10, -0.9380123144), (10.8, -0.9380123144))
                Line((10, -0.9380123144), (10, -1.9380123144))
                Line((10, -1.9380123144), (10.8, -1.9380123144))
                Line((10.8, -0.9380123144), (10.8, -1.9380123144))
            make_face()
            # Profile area: 19.497384041, perimeter: 40.994768082
            with BuildLine():
                Line((4.0663742303, 7), (11.0663742303, 7))
                CenterArc((11.0663742303, 6), 1, 0, 90)
                Line((12.0663742303, 6), (12.0663742303, 2.0375736599))
                CenterArc((11.0663742303, 2.0375736599), 1, -90, 90)
                Line((11.0663742303, 1.0375736599), (10.8, 1.0375736599))
                Line((10.8, 1.0375736599), (10.8, 0.0375736599))
                Line((11.0663742303, 0.0375736599), (10.8, 0.0375736599))
                CenterArc((11.0663742303, 2.0375736599), 2, -90, 90)
                Line((13.0663742303, 6), (13.0663742303, 2.0375736599))
                CenterArc((11.0663742303, 6), 2, 0, 90)
                Line((4.0663742303, 8), (11.0663742303, 8))
                CenterArc((4.0663742303, 6), 2, 90, 90)
                Line((2.0663742303, 4.8), (2.0663742303, 6))
                Line((2.0663742303, 4.8), (3.0663742303, 4.8))
                Line((3.0663742303, 4.8), (3.0663742303, 6))
                CenterArc((4.0663742303, 6), 1, 90, 90)
            make_face()
            # Profile area: 0.7804687795, perimeter: 3.5511719487
            with BuildLine():
                Line((10.8, 0.0375736599), (10, 0.0375736599))
                Line((10, 0.0375736599), (10, -0.9380123144))
                Line((10, -0.9380123144), (10.8, -0.9380123144))
                Line((10.8, 0.0375736599), (10.8, -0.9380123144))
            make_face()
            # Profile area: 10.2522465999, perimeter: 22.5044931998
            with BuildLine():
                Line((2.0663742303, 4), (3.0663742303, 4))
                Line((2.0663742303, 2.0375736599), (2.0663742303, 4))
                CenterArc((4.0663742303, 2.0375736599), 2, -180, 90)
                Line((10, 0.0375736599), (4.0663742303, 0.0375736599))
                Line((10, 1.0375736599), (10, 0.0375736599))
                Line((10, 1.0375736599), (4.0663742303, 1.0375736599))
                CenterArc((4.0663742303, 2.0375736599), 1, -180, 90)
                Line((3.0663742303, 2.0375736599), (3.0663742303, 4))
            make_face()
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((10.8, 1.0375736599), (10, 1.0375736599))
                Line((10, 1.0375736599), (10, 0.0375736599))
                Line((10.8, 0.0375736599), (10, 0.0375736599))
                Line((10.8, 1.0375736599), (10.8, 0.0375736599))
            make_face()
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((2.0663742303, 4.8), (3.0663742303, 4.8))
                Line((2.0663742303, 4), (2.0663742303, 4.8))
                Line((2.0663742303, 4), (3.0663742303, 4))
                Line((3.0663742303, 4), (3.0663742303, 4.8))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a circular disk or flange component with a central rectangular slot or opening, featuring radial fin-like ribs extending outward from the center to the outer edge, creating a lightweight spoke-pattern design.
def model_120048_0ced8cc6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9221234163, perimeter: 9.1792346858
            with BuildLine():
                Line((-0.9525, -6.0325), (-0.9525, -3.3601041651))
                Line((-0.9525, -6.0325), (0.9525, -6.0325))
                Line((0.9525, -6.0325), (0.9525, -3.3601041651))
                CenterArc((0, 0), 3.4925, -105.8266201319, 31.6532402637)
            make_face()
            # Profile area: 38.3197531067, perimeter: 21.9440246853
            with BuildLine():
                CenterArc((0, 0), 3.4925, -105.8266201319, 31.6532402637)
                CenterArc((0, 0), 3.4925, -74.1733798681, 328.3467597363)
            make_face()
        # OneSide extrude, distance=2.2225
        extrude(amount=2.2225)

        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 139.172815952, perimeter: 75.14224538
            with BuildLine():
                CenterArc((0, 0), 7.62, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4925, -74.1733798681, 328.3467597363)
                Line((0.9525, -6.0325), (0.9525, -3.3601041651))
                Line((-0.9525, -6.0325), (0.9525, -6.0325))
                Line((-0.9525, -6.0325), (-0.9525, -3.3601041651))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: This is a segmented robotic arm joint featuring two cubic end effectors connected by an articulated cylindrical shaft with internal structural bracing, designed for modular robotic manipulation with rotational flexibility at both the shoulder and wrist connections.
def model_121027_9ae27724_0002():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 27.7955123873, perimeter: 33.7029996865
            with BuildLine():
                Line((-2.535, 1.585), (-2.85, 1.585))
                Line((-2.85, 1.585), (-2.85, 2.065))
                Line((-2.85, 2.065), (-4.75, 2.065))
                Line((-4.75, 2.065), (-4.75, 0.8082903769))
                Line((-4.75, 0.8082903769), (-3.35, 0))
                Line((-3.35, 0), (-1.4, 0))
                Line((-1.4, 0), (0, 1.4))
                Line((0, 1.4), (0, 8.76))
                Line((0, 8.76), (-1.4, 10.16))
                Line((-1.4, 10.16), (-4.75, 10.16))
                Line((-4.75, 10.16), (-4.75, 8.26))
                Line((-4.75, 8.26), (-2.535, 8.26))
                CenterArc((-2.535, 7.625), 0.635, 0, 90)
                Line((-1.9, 7.625), (-1.9, 2.22))
                CenterArc((-2.535, 2.22), 0.635, -90, 90)
            make_face()
        # Symmetric extrude, full_length=True, total=1.9
        extrude(amount=0.95, both=True)
    return part.part


# Description: This is a flat, circular washer with a large central hole and a textured or knurled outer edge, designed to distribute load and prevent fastener loosening.
def model_121187_d1994db6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.907748562, perimeter: 10.084512418
            with BuildLine():
                CenterArc((0, 0), 1.19, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.415, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a curved duct or channel component with a tubular shape featuring a flat mounting flange on one end and a perforated or mesh-lined interior section on the other end, designed for air flow or fluid passage applications.
def model_121615_47659a4d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.8140676919, perimeter: 36.3977611447
            with BuildLine():
                Line((0, 0), (-4, 2))
                Line((-4, 2), (-0.9392077065, -3.4868021904))
                CenterArc((1.3389938025, -2.215915911), 2.6087073525, -150.8451986986, 109.4848380898)
                CenterArc((-2.1167048371, 0.826445826), 7.2128161725, -41.3603606087, 50.7242427133)
                CenterArc((-1.6319204927, 0.9063874147), 6.7214847993, 9.3638821046, 17.5278547513)
                CenterArc((3.6719173405, 3.5962162033), 0.7745633544, 26.8917368559, 152.8136669492)
                Line((2.8973642245, 3.6001987377), (2.8746237649, -0.8225361922))
                CenterArc((1.3219172649, -0.8145526119), 1.5527270245, 148.3590267468, 211.3463770583)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal or polygonal ring-shaped part with a large central hole and a complex internal cavity structure, featuring multiple angular faces and a toroidal or doughnut-like overall geometry.
def model_121944_dbb87fab_0002():
    """Model: nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.019631402, perimeter: 6.8561944902
            with BuildLine():
                Line((0.6495190528, 0.375), (0, 0.75))
                Line((0, 0.75), (-0.6495190528, 0.375))
                Line((-0.6495190528, 0.375), (-0.6495190528, -0.375))
                Line((-0.6495190528, -0.375), (0, -0.75))
                Line((0, -0.75), (0.6495190528, -0.375))
                Line((0.6495190528, -0.375), (0.6495190528, 0.375))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a helmet or head-mounted protective device with an overall rounded dome shape on top, featuring angular side flanges/guards, mesh or perforated ventilation panels on the crown, and a curved base or chin guard section.
def model_122423_9ab69fbb_0000():
    """Model: PT3 Bracket small"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.3052211349, perimeter: 14.8548667765
            with BuildLine():
                Line((1, 1.2), (1, 2))
                CenterArc((0, 2), 1, 0, 180)
                Line((-1, 1.2), (-1, 2))
                CenterArc((-1.2, 1.2), 0.2, -90, 90)
                Line((-2, 1), (-1.2, 1))
                Line((-2, 0), (-2, 1))
                Line((2, 0), (-2, 0))
                Line((2, 0), (2, 1))
                Line((2, 1), (1.2, 1))
                CenterArc((1.2, 1.2), 0.2, 180, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 2), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a complex organic-shaped component with an irregular, twisted form featuring multiple hollow cutouts and openings, curved surfaces with triangulated mesh patterns, and a non-symmetrical design resembling an abstract geometric or biomimetic structure.
def model_122747_290d163d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 66 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 183.1378262742, perimeter: 104.9781666923
            with BuildLine():
                CenterArc((1.7541825724, -3.5964612748), 0.3, -167.0448551323, 86.4445908534)
                CenterArc((0, 7), 11.040677262, -80.6002642789, 77.9162320928)
                CenterArc((10.1285536742, 6.5251785104), 0.901, -2.6840321861, 58.9939646601)
                Line((8.1410726114, 8.9330331187), (10.628338551, 7.2748558256))
                CenterArc((7.6412877346, 8.1833558035), 0.901, 56.309932474, 15.2551187031)
                Line((3.6267957706, 10.471257182), (7.9262089517, 9.038119455))
                CenterArc((3.3418745534, 9.6164935305), 0.901, 71.5650511771, 11.5064147897)
                Line((-0.4443615731, 10.9842198237), (3.4505632915, 10.5109138781))
                CenterArc((-0.5530503111, 10.0897994761), 0.901, 83.0714659668, 16.5217452726)
                Line((-3.4313144478, 10.5171067907), (-0.7032036898, 10.9781997028))
                CenterArc((-3.2811610692, 9.628706564), 0.901, 99.5932112393, 8.8417375836)
                Line((-7.8855303157, 9.0436542057), (-3.5660822864, 10.4834702155))
                CenterArc((-7.6006090986, 8.1888905542), 0.901, 108.4349488229, 15.2551187031)
                Line((-10.5878689439, 7.2802512237), (-8.1003939754, 8.9385678694))
                CenterArc((-10.0880840671, 6.5305739085), 0.901, 123.690067526, 58.9741396865)
                CenterArc((0, 7), 11, -177.3357927875, 77.9520701557)
                CenterArc((-1.7445887412, -3.5568181818), 0.3, -99.3837226319, 85.1302449956)
                CenterArc((0, -4), 1.5, 12.9551448677, 152.791377496)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 19.4712206345, 141.057558731)
                CenterArc((-1.4142135624, 0.5), 0.5, -90, 70.5287793655)
                Line((-6.5, 0), (-1.4142135624, 0))
                CenterArc((-6.5, 0.5), 0.5, 180, 90)
                Line((-7, 3.5), (-7, 0.5))
                CenterArc((-6.5, 3.5), 0.5, 90, 90)
                Line((6.5, 4), (-6.5, 4))
                CenterArc((6.5, 3.5), 0.5, 0, 90)
                Line((7, 0.5), (7, 3.5))
                CenterArc((6.5, 0.5), 0.5, -90, 90)
                Line((1.4142135624, 0), (6.5, 0))
                CenterArc((1.4142135624, 0.5), 0.5, -160.5287793655, 70.5287793655)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 7), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a hexagonal or wedge-shaped solid block with a tapered geometry, featuring flat faces and sharp edges, with no holes, slots, or curved surfaces—appearing to be a simple geometric form used as a structural component or reference part.
def model_123082_1fd91000_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 56.0519615344, perimeter: 29.9518009445
            with BuildLine():
                Line((0.5080000162, 7.6099002372), (0.5080000162, 0.2540000081))
                Line((0.5080000162, 0.2540000081), (8.1280002594, 0.2540000081))
                Line((8.1280002594, 0.2540000081), (8.1280002594, 7.6099002372))
                Line((8.1280002594, 7.6099002372), (0.5080000162, 7.6099002372))
            make_face()
        # OneSide extrude, distance=3.302
        extrude(amount=3.302)
    return part.part


# Description: This is a boat or small watercraft with an elongated rectangular hull, a pointed bow, and an open cabin area with a windshield frame at the stern.
def model_123411_90e032b4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 67.1998378195, perimeter: 41.073975339
            with BuildLine():
                Line((4.2, 3.5), (-10.2057158932, 1.4353330524))
                CenterArc((-10, 0), 1.45, -98.1562449329, 196.3124898659)
                Line((4.2, -3.5), (-10.2057158932, -1.4353330524))
                Line((4.2, 0), (4.2, -3.5))
                Line((4.2, 3.5), (4.2, 0))
            make_face()
            # Profile area: 4.8380526865, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((-10, 0), 1.45, 98.1562449329, 163.6875101341)
                CenterArc((-10, 0), 1.45, -98.1562449329, 196.3124898659)
            make_face()
            with BuildLine():
                CenterArc((-10, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)
    return part.part


# Description: This is a rectangular coffin or casket with a trapezoidal cross-section, featuring a hinged or removable lid with a beveled peak, and tapered side walls that narrow toward the top.
def model_123411_90e032b4_0001():
    """Model: 2002-2-D v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8380526865, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((-17.5, 0), 1.45, 95.7740705358, 168.4518589284)
                CenterArc((-17.5, 0), 1.45, -95.7740705358, 191.5481410716)
            make_face()
            with BuildLine():
                CenterArc((-17.5, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 96.8374862536, perimeter: 52.7468278169
            with BuildLine():
                Line((2.7, 3.5), (-17.6458787712, 1.4426431936))
                CenterArc((-17.5, 0), 1.45, -95.7740705358, 191.5481410716)
                Line((2.7, -3.5), (-17.6458787712, -1.4426431936))
                Line((2.7, 0), (2.7, -3.5))
                Line((2.7, 3.5), (2.7, 0))
            make_face()
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)
    return part.part


# Description: This is a rectangular storage box or container with a hinged transparent lid, featuring a dark blue/gray base body and a sloped, faceted transparent cover that opens upward for access to the interior.
def model_123411_90e032b4_0002():
    """Model: 2002-2-C v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 86.9537894481, perimeter: 48.8325055951
            with BuildLine():
                Line((3.2, 3.5), (-15.1615873039, 1.4409682659))
                CenterArc((-15, 0), 1.45, -96.3983042344, 192.7966084688)
                Line((3.2, -3.5), (-15.1615873039, -1.4409682659))
                Line((3.2, 0), (3.2, -3.5))
                Line((3.2, 3.5), (3.2, 0))
            make_face()
            # Profile area: 4.8380526865, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((-15, 0), 1.45, 96.3983042344, 167.2033915312)
                CenterArc((-15, 0), 1.45, -96.3983042344, 192.7966084688)
            make_face()
            with BuildLine():
                CenterArc((-15, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)
    return part.part


# Description: This is a boat hull or maritime vessel with an elongated rectangular base, a curved side profile, and an open cabin structure featuring a triangulated framework at the stern.
def model_123411_90e032b4_0003():
    """Model: 2002-2-B v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 77.0740360831, perimeter: 44.938777685
            with BuildLine():
                Line((3.7, 3.5), (-12.681036395, 1.438654171))
                CenterArc((-12.5, 0), 1.45, -97.172248677, 194.344497354)
                Line((3.7, -3.5), (-12.681036395, -1.438654171))
                Line((3.7, 0), (3.7, -3.5))
                Line((3.7, 3.5), (3.7, 0))
            make_face()
            # Profile area: 4.8380526865, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((-12.5, 0), 1.45, 97.172248677, 165.655502646)
                CenterArc((-12.5, 0), 1.45, -97.172248677, 194.344497354)
            make_face()
            with BuildLine():
                CenterArc((-12.5, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)
    return part.part


# Description: This is a hex head bolt with a long cylindrical shaft and a hexagonal head at one end, designed for fastening applications.
def model_123496_74cb10dc_0004():
    """Model: ??? v1"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.7054756887, perimeter: 44.8561944902
            with BuildLine():
                CenterArc((14.0353060459, 6.6170858674), 0.25, -129.8994636277, 180)
                Line((10.5073725722, 2.3976445056), (13.8749454334, 6.4252930782))
                Line((10.5073725722, 2.3976445056), (11.6581293073, 1.435480831))
                Line((11.6581293073, 1.435480831), (12.299571757, 2.2026519877))
                Line((12.299571757, 2.2026519877), (11.5324006003, 2.8440944374))
                Line((11.5324006003, 2.8440944374), (23.7198071456, 17.4203464145))
                Line((23.7198071456, 17.4203464145), (23.3362215673, 17.7410676394))
                Line((14.1956666583, 6.8088786566), (23.3362215673, 17.7410676394))
            make_face()
            with BuildLine():
                CenterArc((11.5952649538, 2.1397876342), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.9018252296, perimeter: 41.2853981634
            with BuildLine():
                Line((14.1956666583, 6.8088786566), (23.3362215673, 17.7410676394))
                Line((23.3362215673, 17.7410676394), (22.952635989, 18.0617888642))
                Line((22.952635989, 18.0617888642), (10.7652294436, 3.4855368872))
                Line((10.7652294436, 3.4855368872), (10.1237869939, 2.7183657305))
                Line((10.1237869939, 2.7183657305), (10.5073725722, 2.3976445056))
                Line((10.5073725722, 2.3976445056), (13.8749454334, 6.4252930782))
                CenterArc((14.0353060459, 6.6170858674), 0.25, 50.1005363723, 180)
            make_face()
            # Profile area: 1.3036504592, perimeter: 6.5707963268
            with BuildLine():
                Line((9.6144727086, 4.4477005618), (10.7652294436, 3.4855368872))
                Line((8.9730302588, 3.6805294051), (9.6144727086, 4.4477005618))
                Line((10.1237869939, 2.7183657305), (8.9730302588, 3.6805294051))
                Line((10.7652294436, 3.4855368872), (10.1237869939, 2.7183657305))
            make_face()
            with BuildLine():
                CenterArc((9.6773370621, 3.7433937586), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular mounting plate with a parallelogram shape, featuring a central rectangular cutout and two circular holes at opposite corners for fastening.
def model_124089_567171f0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.8073342317, perimeter: 29.2131524007
            with BuildLine():
                Line((1.27, -3.5), (1.27, 3.5))
                Line((1.27, 3.5), (-1.27, 3.5))
                Line((-1.27, 3.5), (-1.27, -3.5))
                Line((-1.27, -3.5), (1.27, -3.5))
            make_face()
            with BuildLine():
                CenterArc((0, 3.01625), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -3.01625), 0.23825, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.515, -1.27), (0.515, -1.27))
                Line((-0.515, 1.27), (-0.515, -1.27))
                Line((0.515, 1.27), (-0.515, 1.27))
                Line((0.515, -1.27), (0.515, 1.27))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a triangular pyramid or tetrahedron with a dark blue surface finish, featuring a diagonal internal edge or ridge that divides the visible face into two triangular sections.
def model_124431_9b241909_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 316.1284, perimeter: 71.12
            with BuildLine():
                Line((-17.78, 17.78), (0, 17.78))
                Line((-17.78, 0), (-17.78, 17.78))
                Line((0, 0), (-17.78, 0))
                Line((0, 17.78), (0, 0))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a polyhedron or geodesic dome-like structure featuring multiple triangular and rectangular faceted surfaces with an irregular, angular geometry and internal mesh or lattice framework visible through transparent sections.
def model_124497_5c00f42d_0000():
    """Model: Hinge 1/2-32 Hex Nut v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0078962097, perimeter: 11.6860226701
            with BuildLine():
                Line((1.2827, 0), (0.64135, 1.1108507854))
                Line((0.64135, 1.1108507854), (-0.64135, 1.1108507854))
                Line((-0.64135, 1.1108507854), (-1.2827, 0))
                Line((-1.2827, 0), (-0.64135, -1.1108507854))
                Line((-0.64135, -1.1108507854), (0.64135, -1.1108507854))
                Line((0.64135, -1.1108507854), (1.2827, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2303125
        extrude(amount=1.2303125)
    return part.part


# Description: This is a rectangular box or tray with a trapezoidal top surface featuring internal triangular subdivisions and a sloped or angled left end face.
def model_124497_5c00f42d_0006():
    """Model: Clamp Plate v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.177375, perimeter: 20.32
            with BuildLine():
                Line((0, 1.5875), (0, -1.5875))
                Line((0, -1.5875), (6.985, -1.5875))
                Line((6.985, -1.5875), (6.985, 1.5875))
                Line((6.985, 1.5875), (0, 1.5875))
            make_face()
        # OneSide extrude, distance=1.11125
        extrude(amount=1.11125)
    return part.part


# Description: This is a cylindrical roller or spacer with a smooth, rounded tubular body featuring a textured or knurled surface pattern along its length, and slightly tapered or rounded ends.
def model_124804_18e77ffd_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-10, 3)):
                Circle(0.75)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


# Description: This is a bicycle helmet with an oval shape featuring four large ventilation holes, a reinforced internal ribbed structure, and aerodynamic external venting panels along the sides.
def model_124886_437cfddd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0736504592, perimeter: 3.6796275023
            with BuildLine():
                Line((-0.2598076211, -0.15), (-0.2049038106, -0.2049038106))
                Line((-0.2049038106, -0.2049038106), (-0.2121320344, -0.2121320344))
                Line((-0.2121320344, -0.2121320344), (-0.1448888739, -0.2509548911))
                Line((-0.1448888739, -0.2509548911), (-0.15, -0.2598076211))
                Line((-0.15, -0.2598076211), (-0.075, -0.2799038106))
                Line((-0.075, -0.2799038106), (-0.0776457135, -0.2897777479))
                Line((-0.0776457135, -0.2897777479), (0, -0.2897777479))
                Line((0, -0.2897777479), (0, -0.3))
                Line((0, -0.3), (0.075, -0.2799038106))
                Line((0.075, -0.2799038106), (0.0776457135, -0.2897777479))
                Line((0.0776457135, -0.2897777479), (0.1448888739, -0.2509548911))
                Line((0.1448888739, -0.2509548911), (0.15, -0.2598076211))
                Line((0.15, -0.2598076211), (0.2049038106, -0.2049038106))
                Line((0.2049038106, -0.2049038106), (0.2121320344, -0.2121320344))
                Line((0.2121320344, -0.2121320344), (0.2509548911, -0.1448888739))
                Line((0.2509548911, -0.1448888739), (0.2598076211, -0.15))
                Line((0.2598076211, -0.15), (0.2799038106, -0.075))
                Line((0.2799038106, -0.075), (0.2897777479, -0.0776457135))
                Line((0.2897777479, -0.0776457135), (0.2897777479, 0))
                Line((0.2897777479, 0), (0.3, 0))
                Line((0.3, 0), (0.2799038106, 0.075))
                Line((0.2799038106, 0.075), (0.2897777479, 0.0776457135))
                Line((0.2897777479, 0.0776457135), (0.2509548911, 0.1448888739))
                Line((0.2509548911, 0.1448888739), (0.2598076211, 0.15))
                Line((0.2598076211, 0.15), (0.2049038106, 0.2049038106))
                Line((0.2049038106, 0.2049038106), (0.2121320344, 0.2121320344))
                Line((0.2121320344, 0.2121320344), (0.1448888739, 0.2509548911))
                Line((0.1448888739, 0.2509548911), (0.15, 0.2598076211))
                Line((0.15, 0.2598076211), (0.075, 0.2799038106))
                Line((0.075, 0.2799038106), (0.0776457135, 0.2897777479))
                Line((0.0776457135, 0.2897777479), (0, 0.2897777479))
                Line((0, 0.2897777479), (0, 0.3))
                Line((0, 0.3), (-0.075, 0.2799038106))
                Line((-0.075, 0.2799038106), (-0.0776457135, 0.2897777479))
                Line((-0.0776457135, 0.2897777479), (-0.1448888739, 0.2509548911))
                Line((-0.1448888739, 0.2509548911), (-0.15, 0.2598076211))
                Line((-0.15, 0.2598076211), (-0.2049038106, 0.2049038106))
                Line((-0.2049038106, 0.2049038106), (-0.2121320344, 0.2121320344))
                Line((-0.2121320344, 0.2121320344), (-0.2509548911, 0.1448888739))
                Line((-0.2509548911, 0.1448888739), (-0.2598076211, 0.15))
                Line((-0.2598076211, 0.15), (-0.2799038106, 0.075))
                Line((-0.2799038106, 0.075), (-0.2897777479, 0.0776457135))
                Line((-0.2897777479, 0.0776457135), (-0.2897777479, 0))
                Line((-0.2897777479, 0), (-0.3, 0))
                Line((-0.3, 0), (-0.2799038106, -0.075))
                Line((-0.2799038106, -0.075), (-0.2897777479, -0.0776457135))
                Line((-0.2897777479, -0.0776457135), (-0.2509548911, -0.1448888739))
                Line((-0.2598076211, -0.15), (-0.2509548911, -0.1448888739))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0129564059, perimeter: 0.7302095567
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face()
            with BuildLine():
                Line((0.0095, 0.047), (0.0095, 0.0367933418))
                CenterArc((0, 0), 0.038, 104.4775121859, 331.0449756281)
                Line((-0.0095, 0.047), (-0.0095, 0.0367933418))
                Line((0, 0.047), (-0.0095, 0.047))
                Line((0.0095, 0.047), (0, 0.047))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1472621556, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.1625), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.1625), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.1407291281, -0.08125), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.1407291281, 0.08125), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal punch or bit tool consisting of two components—a longer shaft with a hexagonal cross-section and a smaller detached hexagonal piece—featuring flat faces along their length and pointed or chamfered ends for striking or fastening applications.
def model_125428_e6d291da_0000():
    """Model: Arms v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 45 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 48.8380310101, perimeter: 58.2969020013
            with BuildLine():
                CenterArc((-5.6, -12.1), 0.4, 180, 90)
                Line((-5.6, -12.5), (-4.4, -12.5))
                CenterArc((-4.4, -12.1), 0.4, -90, 90)
                Line((-4, -12.1), (-4, 0))
                Line((-4, 0), (-4, 12.1))
                CenterArc((-4.4, 12.1), 0.4, 0, 90)
                Line((-4.4, 12.5), (-5.5, 12.5))
                CenterArc((-5.5, 12), 0.5, 90, 90)
                Line((-6, 12), (-6, -12.1))
            make_face()
            with BuildLine():
                CenterArc((-5, 11.2), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5, -11.2), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 45 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.8573451754, perimeter: 21.3398223686
            with BuildLine():
                CenterArc((4.4, 2.3146446067), 0.4, 90, 90)
                Line((4, 2.3146446067), (4, -3.3853553933))
                CenterArc((4.4, -3.3853553933), 0.4, -180, 90)
                Line((4.4, -3.7853553933), (5.6, -3.7853553933))
                CenterArc((5.6, -3.3853553933), 0.4, -90, 90)
                Line((6, -3.3853553933), (6, 0))
                Line((6, 0), (6, 2.3146446067))
                CenterArc((5.6, 2.3146446067), 0.4, 0, 90)
                Line((5.6, 2.7146446067), (4.4, 2.7146446067))
            make_face()
            with BuildLine():
                CenterArc((5, -1.75), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 1.75), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a rectangular prism or box-shaped part with a pyramidal or peaked roof-like top surface, featuring two diagonal ridge lines running across the upper face.
def model_126254_7d086401_0003():
    """Model: Punch Guide"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.2298133329, 0.1928362829, 0), x_dir=(0, 0, 1), z_dir=(-0.7660444431, 0.6427876097, 0))):
            # Profile area: 0.9, perimeter: 3.8
            with BuildLine():
                Line((0, -1.5), (0, -2.5))
                Line((-0.9, -1.5), (0, -1.5))
                Line((-0.9, -2.5), (-0.9, -1.5))
                Line((0, -2.5), (-0.9, -2.5))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a flat, parallelogram-shaped plate or panel with a thin profile, featuring a beveled or angled edge along one side and a slightly trapezoidal top surface.
def model_126330_445510fe_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 900, perimeter: 120
            with BuildLine():
                Line((15, -15), (15, 15))
                Line((15, 15), (-15, 15))
                Line((-15, 15), (-15, -15))
                Line((-15, -15), (15, -15))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)
    return part.part


# Description: This is a spherical-headed lollipop maker or candy tool featuring a round bulbous head connected to a long cylindrical handle, used for shaping and forming hard candies or lollipops.
def model_126659_bfbf0231_0001():
    """Model: Piston v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=11
        extrude(amount=11)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8119021395, perimeter: 8.1210170095
            with BuildLine():
                CenterArc((0, 0), 0.9925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or connector with an elongated, rounded rectangular shape featuring a central longitudinal slot or channel running along its top surface and circular openings at both ends.
def model_127202_42451722_0000():
    """Model: Pieza4_SCARA v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743337891, perimeter: 18.8495558905
            with BuildLine():
                CenterArc((-20, 0), 3, 90, 180)
                CenterArc((-20, 0), 3, -90, 179.9999994065)
            make_face()
            # Profile area: 91.7256662109, perimeter: 58.8495558905
            with BuildLine():
                CenterArc((-20, 0), 3, -90, 179.9999994065)
                Line((-20, -3), (0, -3))
                CenterArc((0, 0), 3, 90, 180)
                Line((-20, 3), (0, 3))
            make_face()
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 3, 90, 180)
                CenterArc((0, 0), 3, -90, 180)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a tapered flat metal bar with a gradual thickness reduction from one end to the other, featuring a slightly curved or beveled leading edge, commonly used as a shim, spacer, or alignment tool in mechanical assemblies.
def model_127274_6484a80b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.01155, perimeter: 2.2901666796
            with BuildLine():
                CenterArc((0.825, 0.6002083333), 0.6602083333, -114.6160316349, 49.2320632697)
                Line((1.1, 0.0105), (1.1, 0))
                CenterArc((0.825, 0.6107083333), 0.6602083333, -114.6160316349, 49.2320632697)
                CenterArc((0.275, -0.5897083333), 0.6602083333, 65.3839683651, 24.6160316349)
                CenterArc((0.275, -0.5897083333), 0.6602083333, 90, 24.6160316349)
                Line((0, 0.0105), (0, 0))
                CenterArc((0.275, -0.6002083333), 0.6602083333, 90, 24.6160316349)
                CenterArc((0.275, -0.6002083333), 0.6602083333, 65.3839683651, 24.6160316349)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a streamlined aerodynamic housing or duct component with a tapered, wedge-like shape featuring a curved internal cavity or channel, flat upper surfaces, and angled side panels that converge toward the rear.
def model_127646_b88ed13f_0019():
    """Model: 4x4 base (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=-0.3937
        extrude(amount=-0.3937)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.1349078256, perimeter: 12.154911335
            with BuildLine():
                Line((1.27, -1.27), (-1.27, -1.27))
                Line((1.27, -1.27), (1.27, 1.27))
                Line((-1.27, 1.27), (1.27, 1.27))
                Line((-1.27, -1.27), (-1.27, 1.27))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is an angled elbow connector or pipe fitting with a cylindrical upper section and a flared base, featuring internal channels or slots visible through the translucent blue sections, designed to join two perpendicular pipe segments at approximately 90 degrees.
def model_128043_d4650350_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4056194478, perimeter: 8.5767070038
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 180)
                Line((-0.4, 0), (-0.4941176582, -1.2235294838))
                Line((-0.4941176582, -1.2235294838), (-0.5, -1.3000000199))
                CenterArc((0, -1.3), 0.5, -179.9999977145, 179.999995429)
                Line((0.4941176582, -1.2235294838), (0.5, -1.3000000199))
                Line((0.4, 0), (0.4941176582, -1.2235294838))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -1.3), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.25
        extrude(amount=1.25, mode=Mode.ADD)
    return part.part


# Description: This is a satellite or antenna component featuring a blue trapezoidal base platform with geometric surface paneling and a dark mechanical assembly mounted on top, likely a receiver, transmitter, or positioning mechanism.
def model_128814_4cb0ca05_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6402298604, perimeter: 6.8823573292
            with BuildLine():
                CenterArc((0, 0), 0.85, -103.6089606308, 27.2179212616)
                CenterArc((0, 0), 0.85, -76.3910393692, 104.4635263051)
                Line((0.5123475383, 0.4), (0.75, 0.4))
                CenterArc((0, 0), 0.65, 142.0201275551, 255.9597448897)
                Line((-0.75, 0.4), (-0.5123475383, 0.4))
                CenterArc((0, 0), 0.85, 151.9275130641, 104.4635263051)
            make_face()
            # Profile area: 0.2631638377, perimeter: 2.1515148261
            with BuildLine():
                Line((-0.2, -0.8261355821), (-0.2, -1.5))
                Line((-0.2, -1.5), (0.2, -1.5))
                Line((0.2, -0.8261355821), (0.2, -1.5))
                CenterArc((0, 0), 0.85, -103.6089606308, 27.2179212616)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5, perimeter: 10.6
            with BuildLine():
                Line((-0.2, -1.5), (0.2, -1.5))
                Line((-0.2, -1.5), (-2.5, -1.5))
                Line((-2.5, -1.5), (-2.5, -1.8))
                Line((-2.5, -1.8), (0, -1.8))
                Line((2.5, -1.8), (0, -1.8))
                Line((2.5, -1.5), (2.5, -1.8))
                Line((0.2, -1.5), (2.5, -1.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shell or sleeve with a uniformly curved sidewall and open ends, featuring a slightly tapered or angled top opening and a flat or recessed bottom surface.
def model_128996_2033836a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is an elliptical dish or membrane component with a shallow, curved bowl shape featuring radial ribbing or support structure extending from a central point to the outer perimeter.
def model_128996_ac67f969_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a flat parallelogram plate or panel with a rectangular shape, featuring a slightly beveled or angled edge on one side and diagonal surface lines that suggest internal structure or reinforcement.
def model_129409_0664bc6f_0001():
    """Model: Untitled v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10, perimeter: 14
            with BuildLine():
                Line((5, -2), (0, -2))
                Line((5, 0), (5, -2))
                Line((0, 0), (5, 0))
                Line((0, -2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a lightweight watercraft hull featuring an elongated, tapered design with a curved top surface, dark gunwales (side rails) along the edges, and a streamlined profile optimized for water displacement and paddling performance.
def model_129422_621d0a90_0001():
    """Model: body work v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 236.1975873344, perimeter: 63.7478173408
            with BuildLine():
                CenterArc((-0.5942603759, -6.7300682155), 6.7562536645, 26.7694241036, 58.1844853752)
                CenterArc((0.5942603759, -6.7300682155), 6.7562536645, 95.0460905212, 58.1844853752)
                Line((-5.4379006, -3.6870438086), (-5.4379006, -16.0937580808))
                Line((-5.4379006, -16.0937580808), (-2.1507207134, -25.0324362146))
                CenterArc((1.0373810715, -23.8600185588), 3.396845029, -159.80910862, 51.253430881)
                Line((-0.0435835022, -27.0802781355), (0.0435835022, -27.0802781355))
                CenterArc((-1.0373810715, -23.8600185588), 3.396845029, -71.444322261, 51.253430881)
                Line((5.4379006, -16.0937580808), (2.1507207134, -25.0324362146))
                Line((5.4379006, -3.6870438086), (5.4379006, -16.0937580808))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an open top, featuring a uniform hollow cylindrical body with vertical ribbing or fluting on its exterior surface.
def model_129699_881b4b3a_0000():
    """Model: Inner Race"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.395865218, perimeter: 4.9872783376
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a cylindrical ring or band with an elliptical cross-section, featuring a dark outer surface and a light blue textured inner surface, with a slightly tapered or curved profile.
def model_130577_4425dd52_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.9777126301, perimeter: 24.0369086388
            Circle(3.8255928265)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a hexagonal or polygonal 3D solid with an irregular, faceted geometric form featuring multiple planar surfaces at varying angles, a darker recessed or concave section on the left side, and lighter raised surfaces on the upper right, creating a complex multi-faced structural component.
def model_130668_ef3fc7df_0000():
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
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (3, 0))
                Line((3, 0), (3, 3))
                Line((3, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is an elongated hexagonal prism or column with a tapered top end, featuring a hollow interior channel running along its length and a slightly angled upper face.
def model_130719_e4764a36_0002():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9454345152, perimeter: 3.8893383932
            with BuildLine():
                Line((10, -4), (9.0279018648, -4))
                Line((10, -3.0274289386), (10, -4))
                Line((9.0279018648, -3.0274289386), (10, -3.0274289386))
                Line((9.0279018648, -4), (9.0279018648, -3.0274289386))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is an elongated hexagonal or octagonal prism with a tapered top end, featuring a predominantly dark blue finish and straight parallel sides along its length.
def model_130719_e4764a36_0003():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0168951258, perimeter: 4.0342993813
            with BuildLine():
                Line((1.9904615127, -2.026688178), (1, -2.026688178))
                Line((1.9904615127, -1), (1.9904615127, -2.026688178))
                Line((1, -1), (1.9904615127, -1))
                Line((1, -2.026688178), (1, -1))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a hexagonal prism or column with a tall, slender elongated shape, featuring a six-sided cross-section and tapered or beveled edges at the top.
def model_130719_e4764a36_0005():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.9846471849, perimeter: 3.9691756119
            with BuildLine():
                Line((-1, 4), (-1, 3.0077766621))
                Line((-1, 4), (-1.992364468, 4))
                Line((-1.992364468, 3.0077766621), (-1.992364468, 4))
                Line((-1, 3.0077766621), (-1.992364468, 3.0077766621))
            make_face()
        # TwoSides extrude, along=3.5, against=-1
        extrude(amount=3.5)
        extrude(sk.sketch, amount=-1)
    return part.part


# Description: This is a bent or folded sheet metal bracket with three rectangular flanges connected at angular offsets, featuring triangulated internal geometry and light blue-shaded faces indicating the primary structural surfaces.
def model_130728_525bafa8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.9140145609, perimeter: 41.8280291219
            with BuildLine():
                Line((-1.1265962764, 9.382144626), (-0.9634666722, 5))
                Line((-0.9634666722, 5), (4.5932766095, 5))
                Line((4.5932766095, 5), (4.9160549026, 1))
                Line((4.9160549026, 1), (0, 1))
                Line((0, 1), (0, 0.1000000015))
                Line((0, 0), (0, 0.1000000015))
                Line((6, 0), (0, 0))
                Line((5.5158325604, 6), (6, 0))
                Line((0, 6), (5.5158325604, 6))
                Line((-0.1272884437, 9.4193448339), (0, 6))
                Line((-1.1265962764, 9.382144626), (-0.1272884437, 9.4193448339))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a truncated sphere or dome-shaped component with a flat base, featuring a polygonal upper surface with triangular facets and vertical ribbed or fluted details along its curved sides.
def model_130757_2772bec8_0000():
    """Model: Sensor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1556567093, perimeter: 1.4287091025
            with BuildLine():
                CenterArc((0, 0), 0.2325, -55.8894398212, 111.7788796424)
                Line((0.1303840481, 0.1925), (-0.1303840481, 0.1925))
                CenterArc((0, 0), 0.2325, 124.1105601788, 111.7788796424)
                Line((0.1303840481, -0.1925), (-0.1303840481, -0.1925))
            make_face()
        # OneSide extrude, distance=0.18
        extrude(amount=0.18)
    return part.part


# Description: This is a cylindrical duct or manifold component with a rounded, pod-like shape featuring a large circular opening on one end, internal ribbing or reinforcement structures, and smooth curved surfaces that taper toward a narrower outlet section.
def model_130757_3a6352fd_0002():
    """Model: Round Silver Thing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.165), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.318461275, perimeter: 2.3695574288
            with BuildLine():
                CenterArc((1.7119338607, -0.3144913182), 0.175, -90, 180)
                Line((1.7119338607, -0.1394913182), (1.0769338607, -0.1394913182))
                CenterArc((1.0769338607, -0.3144913182), 0.175, 90, 180)
                Line((1.0769338607, -0.4894913182), (1.7119338607, -0.4894913182))
            make_face()
        # OneSide extrude, distance=0.32
        extrude(amount=0.32)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.165), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1263318531, perimeter: 5.0532741229
            with BuildLine():
                CenterArc((1.7119338607, -0.3144913182), 0.225, -90, 180)
                Line((1.7119338607, -0.0894913182), (1.0769338607, -0.0894913182))
                CenterArc((1.0769338607, -0.3144913182), 0.225, 90, 180)
                Line((1.0769338607, -0.5394913182), (1.7119338607, -0.5394913182))
            make_face()
            with BuildLine():
                Line((1.0769338607, -0.4894913182), (1.7119338607, -0.4894913182))
                CenterArc((1.0769338607, -0.3144913182), 0.175, 90, 180)
                Line((1.7119338607, -0.1394913182), (1.0769338607, -0.1394913182))
                CenterArc((1.7119338607, -0.3144913182), 0.175, -90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.06
        extrude(amount=0.06, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or manifold component with a rounded rectangular base, featuring a protruding cylindrical barrel on one end with mesh/perforated sections and internal passages or channels visible through transparent areas.
def model_130757_a899408f_0001():
    """Model: Silver Box"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.327853685, perimeter: 2.4046957103
            with BuildLine():
                CenterArc((0.3223575796, -0.735), 0.1775, -90, 180)
                Line((0.3223575796, -0.5575), (-0.3223575796, -0.5575))
                CenterArc((-0.3223575796, -0.735), 0.1775, 90, 180)
                Line((-0.3223575796, -0.9125), (0.3223575796, -0.9125))
            make_face()
        # OneSide extrude, distance=0.355
        extrude(amount=0.355)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1012143767, perimeter: 5.0607188329
            with BuildLine():
                CenterArc((0.3223575796, -0.735), 0.2175, -90, 180)
                Line((0.3223575796, -0.5175), (-0.3223575796, -0.5175))
                CenterArc((-0.3223575796, -0.735), 0.2175, 90, 180)
                Line((-0.3223575796, -0.9525), (0.3223575796, -0.9525))
            make_face()
            with BuildLine():
                Line((-0.3223575796, -0.9125), (0.3223575796, -0.9125))
                CenterArc((-0.3223575796, -0.735), 0.1775, 90, 180)
                Line((0.3223575796, -0.5575), (-0.3223575796, -0.5575))
                CenterArc((0.3223575796, -0.735), 0.1775, -90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a closed domed top and open bottom, featuring a fine grid or perforated pattern across its curved surface.
def model_130757_a899408f_0003():
    """Model: Speaker/Microphone"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6582422007, perimeter: 9.0792027689
            with BuildLine():
                CenterArc((1.3250355288, -0.0075159477), 0.795, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.3250355288, -0.0075159477), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with Locations((1.3250355288, -0.0075159477)):
                Circle(0.65)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


# Description: A parallelogram-shaped flat panel or plate with a dark frame border, blue center area, and four corner mounting holes.
def model_130757_b2c47f8d_0001():
    """Model: PCB Board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 36 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 46.3151151228, perimeter: 35.4761053731
            with BuildLine():
                CenterArc((-3.95, -2.5), 0.3, 180, 90)
                Line((3.95, -2.8), (-3.95, -2.8))
                CenterArc((3.95, -2.5), 0.3, -90, 90)
                Line((4.25, 2.5), (4.25, -2.5))
                CenterArc((3.95, 2.5), 0.3, 0, 90)
                Line((-3.95, 2.8), (3.95, 2.8))
                CenterArc((-3.95, 2.5), 0.3, 90, 90)
                Line((-4.25, -2.5), (-4.25, 2.5))
            make_face()
            with BuildLine():
                CenterArc((-3.9, -2.45), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.9, -2.45), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.9, 2.45), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.9, 2.45), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.135
        extrude(amount=0.135)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 36 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2425113179, perimeter: 2.811725425
            with BuildLine():
                CenterArc((-3.9, 2.45), 0.31, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.9, 2.45), 0.1375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2425113179, perimeter: 2.811725425
            with BuildLine():
                CenterArc((1.9, 2.45), 0.31, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.9, 2.45), 0.1375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2425113179, perimeter: 2.811725425
            with BuildLine():
                CenterArc((1.9, -2.45), 0.31, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.9, -2.45), 0.1375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2425113179, perimeter: 2.811725425
            with BuildLine():
                CenterArc((-3.9, -2.45), 0.31, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.9, -2.45), 0.1375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.134
        extrude(amount=0.134, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_101190_cfdcb477_0001": {"func": model_101190_cfdcb477_0001, "volume": 1.1908929627, "area": 8.999625339},
    "model_102314_91648bfc_0000": {"func": model_102314_91648bfc_0000, "volume": 31.227127864, "area": 138.0726114979},
    "model_102416_eba35f73_0016": {"func": model_102416_eba35f73_0016, "volume": 6.8895, "area": 51.1203657993},
    "model_103284_e25015aa_0003": {"func": model_103284_e25015aa_0003, "volume": 18.0185179567, "area": 54.7244077425},
    "model_104453_aba0f2d1_0008": {"func": model_104453_aba0f2d1_0008, "volume": 7066.5292234282, "area": 2928.7549903077},
    "model_104892_5fcd41a9_0000": {"func": model_104892_5fcd41a9_0000, "volume": 7448.5732678773, "area": 3841.1113065477},
    "model_106059_5d7ef4ef_0000": {"func": model_106059_5d7ef4ef_0000, "volume": 4.1146616596, "area": 83.9380702322},
    "model_106325_dce63a49_0000": {"func": model_106325_dce63a49_0000, "volume": 2.1059324471, "area": 12.0613064279},
    "model_106726_19e9c7f3_0000": {"func": model_106726_19e9c7f3_0000, "volume": 0.057396738, "area": 1.188098},
    "model_107247_b9ff3971_0000": {"func": model_107247_b9ff3971_0000, "volume": 0.3453503717, "area": 5.5059454672},
    "model_108856_09f25b7b_0010": {"func": model_108856_09f25b7b_0010, "volume": 3.058723863, "area": 14.5741738675},
    "model_109880_aebcec75_0002": {"func": model_109880_aebcec75_0002, "volume": 31.9939795842, "area": 113.4743266477},
    "model_109946_242843a6_0000": {"func": model_109946_242843a6_0000, "volume": 90, "area": 138},
    "model_110324_300f25b9_0000": {"func": model_110324_300f25b9_0000, "volume": 108.6990966724, "area": 201.7743296621},
    "model_110344_a5d1ecce_0003": {"func": model_110344_a5d1ecce_0003, "volume": 32.7545, "area": 83.96},
    "model_110440_85dae82d_0000": {"func": model_110440_85dae82d_0000, "volume": 3.0421889241, "area": 15.8933641157},
    "model_110506_6f8424d2_0000": {"func": model_110506_6f8424d2_0000, "volume": 30.6305283725, "area": 168.4679060488},
    "model_110783_5d025c90_0002": {"func": model_110783_5d025c90_0002, "volume": 0.677845637, "area": 8.1590712124},
    "model_111313_a904bb4b_0000": {"func": model_111313_a904bb4b_0000, "volume": 2.1111502632, "area": 15.8336269741},
    "model_111493_9c64d90b_0000": {"func": model_111493_9c64d90b_0000, "volume": 3.0574309968, "area": 12.3133143031},
    "model_111872_8817499c_0001": {"func": model_111872_8817499c_0001, "volume": 2.8979516574, "area": 29.9379553},
    "model_112099_2c7f567f_0000": {"func": model_112099_2c7f567f_0000, "volume": 19.4468571429, "area": 82.8937785998},
    "model_112738_1107ad1c_0002": {"func": model_112738_1107ad1c_0002, "volume": 5.0893800988, "area": 23.8918121306},
    "model_113001_c1b164a3_0001": {"func": model_113001_c1b164a3_0001, "volume": 0.0883572934, "area": 2.3915374075},
    "model_113191_87565693_0001": {"func": model_113191_87565693_0001, "volume": 0.5060163287, "area": 9.2306275348},
    "model_113935_329e18e4_0000": {"func": model_113935_329e18e4_0000, "volume": 2.9782298356, "area": 64.5283131047},
    "model_114110_e6175b0c_0000": {"func": model_114110_e6175b0c_0000, "volume": 22.3926990817, "area": 103.1415926536},
    "model_114111_59282658_0003": {"func": model_114111_59282658_0003, "volume": 1011.393203016, "area": 1751.673916},
    "model_114345_228b4786_0001": {"func": model_114345_228b4786_0001, "volume": 0.0225373705, "area": 2.4260755639},
    "model_115330_1c326f55_0001": {"func": model_115330_1c326f55_0001, "volume": 2.7332079328, "area": 19.3154029395},
    "model_115430_bb9dd4dc_0000": {"func": model_115430_bb9dd4dc_0000, "volume": 0.0170000005, "area": 0.6828318686},
    "model_115518_3e1d2cc3_0000": {"func": model_115518_3e1d2cc3_0000, "volume": 4.468616674, "area": 35.5230038083},
    "model_115518_a1bf907b_0000": {"func": model_115518_a1bf907b_0000, "volume": 1.7277455426, "area": 14.8368430221},
    "model_115518_ce8600fe_0000": {"func": model_115518_ce8600fe_0000, "volume": 4.0503359252, "area": 32.6679685294},
    "model_115524_4490925e_0000": {"func": model_115524_4490925e_0000, "volume": 338.5800055361, "area": 750.9600116712},
    "model_115617_418b75dd_0000": {"func": model_115617_418b75dd_0000, "volume": 1910.6436127515, "area": 1271.7636225113},
    "model_115637_5c72f933_0000": {"func": model_115637_5c72f933_0000, "volume": 0.0319999998, "area": 0.7199999961},
    "model_116416_b2565d0a_0007": {"func": model_116416_b2565d0a_0007, "volume": 50.106192983, "area": 201.5309649149},
    "model_117699_6deeac69_0000": {"func": model_117699_6deeac69_0000, "volume": 0.6962938287, "area": 5.6346329925},
    "model_117852_77bf0ad1_0000": {"func": model_117852_77bf0ad1_0000, "volume": 1.7878512783, "area": 13.153804169},
    "model_118022_d715d1fb_0000": {"func": model_118022_d715d1fb_0000, "volume": 477.7108804235, "area": 510.7181446864},
    "model_118360_4167ef76_0000": {"func": model_118360_4167ef76_0000, "volume": 36.1737551088, "area": 131.800734698},
    "model_118459_55a06bd6_0000": {"func": model_118459_55a06bd6_0000, "volume": 30.1592894745, "area": 158.3362697409},
    "model_118700_df55782f_0000": {"func": model_118700_df55782f_0000, "volume": 48762.771069952, "area": 22092.889340143},
    "model_119790_1ed376f0_0003": {"func": model_119790_1ed376f0_0003, "volume": 0.4397979424, "area": 3.5981043829},
    "model_119880_14a41c0d_0000": {"func": model_119880_14a41c0d_0000, "volume": 20.526323186, "area": 99.6814950237},
    "model_119881_f122be32_0000": {"func": model_119881_f122be32_0000, "volume": 2.6703537556, "area": 37.3849525777},
    "model_119886_382e5a3f_0000": {"func": model_119886_382e5a3f_0000, "volume": 35.2798637088, "area": 106.8183275929},
    "model_119902_a18122ad_0000": {"func": model_119902_a18122ad_0000, "volume": 470.4856489414, "area": 989.0121286303},
    "model_119907_90a6e5af_0000": {"func": model_119907_90a6e5af_0000, "volume": 772.8334197518, "area": 1892.3931262645},
    "model_120048_0ced8cc6_0000": {"func": model_120048_0ced8cc6_0000, "volume": 123.9396337629, "area": 440.4529037729},
    "model_121027_9ae27724_0002": {"func": model_121027_9ae27724_0002, "volume": 52.8114735359, "area": 119.6267241791},
    "model_121187_d1994db6_0000": {"func": model_121187_d1994db6_0000, "volume": 1.1723245686, "area": 10.8408508494},
    "model_121615_47659a4d_0000": {"func": model_121615_47659a4d_0000, "volume": 31.8140676919, "area": 100.0258965284},
    "model_121944_dbb87fab_0002": {"func": model_121944_dbb87fab_0002, "volume": 0.509815701, "area": 5.467360049},
    "model_122423_9ab69fbb_0000": {"func": model_122423_9ab69fbb_0000, "volume": 7.3052211349, "area": 29.4653090463},
    "model_122747_290d163d_0000": {"func": model_122747_290d163d_0000, "volume": 366.2756525485, "area": 576.2319859332},
    "model_123082_1fd91000_0000": {"func": model_123082_1fd91000_0000, "volume": 185.0835769867, "area": 211.0047697877},
    "model_123411_90e032b4_0000": {"func": model_123411_90e032b4_0000, "volume": 302.5591401253, "area": 332.9107840669},
    "model_123411_90e032b4_0001": {"func": model_123411_90e032b4_0001, "volume": 427.0372635483, "area": 442.2248718632},
    "model_123411_90e032b4_0002": {"func": model_123411_90e032b4_0002, "volume": 385.5257369654, "area": 405.7519243448},
    "model_123411_90e032b4_0003": {"func": model_123411_90e032b4_0003, "volume": 344.0307728325, "area": 369.3097084659},
    "model_123496_74cb10dc_0004": {"func": model_123496_74cb10dc_0004, "volume": 10.9554756887, "area": 69.6780972451},
    "model_124089_567171f0_0000": {"func": model_124089_567171f0_0000, "volume": 2.9614668463, "area": 35.4572989436},
    "model_124431_9b241909_0000": {"func": model_124431_9b241909_0000, "volume": 200.741534, "area": 677.418},
    "model_124497_5c00f42d_0000": {"func": model_124497_5c00f42d_0000, "volume": 3.7006523055, "area": 20.3932521856},
    "model_124497_5c00f42d_0006": {"func": model_124497_5c00f42d_0006, "volume": 24.6446079687, "area": 66.93535},
    "model_124804_18e77ffd_0000": {"func": model_124804_18e77ffd_0000, "volume": 9.719302272, "area": 29.4524311274},
    "model_124886_437cfddd_0000": {"func": model_124886_437cfddd_0000, "volume": 0.0123422404, "area": 0.8890867932},
    "model_125428_e6d291da_0000": {"func": model_125428_e6d291da_0000, "volume": 54.625838567, "area": 193.063804304},
    "model_126254_7d086401_0003": {"func": model_126254_7d086401_0003, "volume": 0.09, "area": 2.18},
    "model_126330_445510fe_0000": {"func": model_126330_445510fe_0000, "volume": 1800, "area": 2040},
    "model_126659_bfbf0231_0001": {"func": model_126659_bfbf0231_0001, "volume": 6.4844592945, "area": 32.1451294607},
    "model_127202_42451722_0000": {"func": model_127202_42451722_0000, "volume": 296.5486677646, "area": 414.2477796077},
    "model_127274_6484a80b_0000": {"func": model_127274_6484a80b_0000, "volume": 0.05775, "area": 11.4739333979},
    "model_127646_b88ed13f_0019": {"func": model_127646_b88ed13f_0019, "volume": 4.2214477091, "area": 20.1401965926},
    "model_128043_d4650350_0000": {"func": model_128043_d4650350_0000, "volume": 0.5787654695, "area": 6.452392499},
    "model_128814_4cb0ca05_0000": {"func": model_128814_4cb0ca05_0000, "volume": 8.4033936981, "area": 65.2330875709},
    "model_128996_2033836a_0000": {"func": model_128996_2033836a_0000, "volume": 1.8472564803, "area": 8.3566364585},
    "model_128996_ac67f969_0000": {"func": model_128996_ac67f969_0000, "volume": 1.0602875206, "area": 15.5508836353},
    "model_129409_0664bc6f_0001": {"func": model_129409_0664bc6f_0001, "volume": 2, "area": 22.8},
    "model_129422_621d0a90_0001": {"func": model_129422_621d0a90_0001, "volume": 236.1975873344, "area": 536.1429920096},
    "model_129699_881b4b3a_0000": {"func": model_129699_881b4b3a_0000, "volume": 0.2513744135, "area": 3.9586521804},
    "model_130577_4425dd52_0000": {"func": model_130577_4425dd52_0000, "volume": 137.9331378902, "area": 164.0661511765},
    "model_130668_ef3fc7df_0000": {"func": model_130668_ef3fc7df_0000, "volume": 22.5, "area": 48},
    "model_130719_e4764a36_0002": {"func": model_130719_e4764a36_0002, "volume": 4.2544553182, "area": 19.3928917999},
    "model_130719_e4764a36_0003": {"func": model_130719_e4764a36_0003, "volume": 4.5760280661, "area": 20.1881374674},
    "model_130719_e4764a36_0005": {"func": model_130719_e4764a36_0005, "volume": 4.430912332, "area": 19.8305846233},
    "model_130728_525bafa8_0000": {"func": model_130728_525bafa8_0000, "volume": 119.4840873657, "area": 290.7962038532},
    "model_130757_2772bec8_0000": {"func": model_130757_2772bec8_0000, "volume": 0.0280182077, "area": 0.5684810571},
    "model_130757_3a6352fd_0002": {"func": model_130757_3a6352fd_0002, "volume": 0.1094875192, "area": 1.6666941893},
    "model_130757_a899408f_0001": {"func": model_130757_a899408f_0001, "volume": 0.1244852083, "area": 1.7319092935},
    "model_130757_a899408f_0003": {"func": model_130757_a899408f_0003, "volume": 0.8031638699, "area": 14.8253328119},
    "model_130757_b2c47f8d_0001": {"func": model_130757_b2c47f8d_0001, "volume": 6.382526608, "area": 98.7786517007},
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
