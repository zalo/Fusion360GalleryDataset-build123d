"""Batch 015 - passing/03_4to5ops
104 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_68956_2805fb2a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3600, perimeter: 240
            with BuildLine():
                Line((30, -30), (30, 30))
                Line((30, 30), (-30, 30))
                Line((-30, 30), (-30, -30))
                Line((-30, -30), (30, -30))
            make_face()
        # OneSide extrude, distance=66
        extrude(amount=66)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-25, 25)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((25, 25)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-25, -25)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((25, -25)):
                Circle(2.5)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_69058_b038ab52_0000():
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
            # Profile area: 35.263082575, perimeter: 34.9030833713
            with BuildLine():
                Line((-3, 0), (0, 0))
                _nurbs_edge([(0, 0), (0.0735319839, 0.0702710005), (0.2222604768, 0.2062837454), (0.4503467814, 0.3967151217), (0.7646133749, 0.6230008266), (1.1754905492, 0.856759513), (1.6059311848, 1.0372850407), (2.0573878757, 1.1606248285), (2.5303849379, 1.2253521865), (3.0237823367, 1.2345692059), (3.5359165048, 1.1928025371), (3.9593226694, 1.1221139985), (4.2840838256, 1.0494882576), (4.5037416134, 0.9924988361), (4.6143581367, 0.9618609462)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((4.6143581367, 0.9618609462), (4.6143581367, 3.1613485007))
                _nurbs_edge([(4.6143581367, 3.1613485007), (4.5019876132, 3.1310249232), (4.2805224621, 3.0742268364), (3.9581518936, 3.000576288), (3.548306695, 2.9258540038), (3.0717676943, 2.874476761), (2.6348321476, 2.8696322514), (2.2419403271, 2.916537646), (1.8971407939, 3.0199498688), (1.6019555988, 3.1816572783), (1.3542494853, 3.3991510198), (1.1916766176, 3.614965449), (1.08861757, 3.798998598), (1.0281638491, 3.9313835531), (1, 4)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((1, 4), (-4, 4))
                _nurbs_edge([(-4, 4), (-4.1174014747, 3.9972788594), (-4.3524466365, 3.9846333036), (-4.7057410421, 3.9440543753), (-5.1782772615, 3.8460235265), (-5.7715602601, 3.6457838372), (-6.3676341707, 3.3625437992), (-6.9666306213, 2.9923888617), (-7.5684695313, 2.5377005853), (-8.1729159462, 2.0054664014), (-8.7797100064, 1.4034144025), (-9.2668425389, 0.8712964039), (-9.6330811431, 0.4457633919), (-9.8776289253, 0.1505145933), (-10, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-10, 0), (-9.7513073308, 0.1080100478), (-9.262243845, 0.3157605542), (-8.5536138966, 0.6025778228), (-7.6595281935, 0.9345653708), (-6.6332874621, 1.2587572158), (-5.7095599794, 1.481079625), (-4.9027947075, 1.58717438), (-4.2280428139, 1.5620848391), (-3.6979796027, 1.3932153025), (-3.3153071171, 1.077880697), (-3.1221815942, 0.713310298), (-3.0379265079, 0.3796739597), (-3.0082292658, 0.1309431757), (-3, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(4.6143581367, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.0285406999, perimeter: 19.846072044
            with BuildLine():
                CenterArc((2.0616047234, 1), 1.8218620613, 0, 360)
            make_face()
            with BuildLine():
                Line((3.1613485007, 2), (0.9618609462, 2))
                Line((3.1613485007, 0), (3.1613485007, 2))
                Line((0.9618609462, 0), (3.1613485007, 0))
                Line((0.9618609462, 2), (0.9618609462, 0))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.3989751089, perimeter: 8.3989751089
            with BuildLine():
                Line((0.9618609462, 2), (0.9618609462, 0))
                Line((0.9618609462, 0), (3.1613485007, 0))
                Line((3.1613485007, 0), (3.1613485007, 2))
                Line((3.1613485007, 2), (0.9618609462, 2))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_69488_f2085c68_0002():
    """Model: Practica 15 - Ventanal v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2285.5936, perimeter: 1799.68
            with BuildLine():
                Line((150, -77.5), (150, 77.5))
                Line((150, 77.5), (-150, 77.5))
                Line((-150, 77.5), (-150, -77.5))
                Line((-150, -77.5), (150, -77.5))
            make_face()
            with BuildLine():
                Line((147.46, 74.96), (-147.46, 74.96))
                Line((147.46, -74.96), (147.46, 74.96))
                Line((-147.46, -74.96), (147.46, -74.96))
                Line((-147.46, 74.96), (-147.46, -74.96))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.62), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11993.6, perimeter: 459.84
            with BuildLine():
                Line((-67.46, 74.96), (-147.46, 74.96))
                Line((-147.46, 74.96), (-147.46, -74.96))
                Line((-147.46, -74.96), (-67.46, -74.96))
                Line((-67.46, -74.96), (-67.46, 74.96))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)
    return part.part


def model_69816_c51ea7d9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.3531739743, perimeter: 84.7087502478
            with BuildLine():
                CenterArc((5.7000000849, 3.7500000261), 0.7499999739, -90, 180)
                Line((5.7000000849, 4.5), (1.9642670538, 4.5))
                CenterArc((1.9642670538, 5.0773254954), 0.5773254954, -156.3811101865, 66.3811101865)
                Line((1.4353037175, 4.8460193856), (0.6266157223, 8.4851153639))
                CenterArc((0.3830156941, 8.3984320543), 0.2585632803, 19.5877339608, 153.2192887429)
                Line((0.1264872924, 8.430807184), (0.9560999912, 4.6975500396))
                CenterArc((1.9642670538, 5.0773254954), 1.0773254954, -159.3586618772, 69.3586618772)
                Line((5.7000000849, 4), (1.9642670538, 4))
                CenterArc((5.7000000849, 3.7500000261), 0.2499999739, -90, 180)
                Line((5.7000000849, 3.5000000522), (1.8366935833, 3.5000000522))
                CenterArc((1.9183468066, 2.8743145537), 0.6309909602, 97.4351960747, 59.3662134117)
                Line((1.3383746015, 3.1228740701), (0, 0))
                Line((0, 0), (0.5439837933, 0))
                Line((1.6606378709, 2.605526181), (0.5439837933, 0))
                CenterArc((2.3692072875, 2.1841012261), 0.824420773, 98.2453177054, 51.0124199127)
                Line((4.0976749682, 3.0000000522), (2.2509756652, 3.0000000522))
                CenterArc((4.1054017831, 2.4350433154), 0.5650095735, 26.0971288576, 64.6864466817)
                Line((4.6128084161, 2.6835877318), (5.9304128344, -0.0063186886))
                Line((6.4871749427, -0.0063186886), (5.9304128344, -0.0063186886))
                Line((5.0145813886, 3.0000000522), (6.4871749427, -0.0063186886))
                Line((5.7000000849, 3.0000000522), (5.0145813886, 3.0000000522))
            make_face()
            with BuildLine():
                Line((5.7000000849, 3.3500000522), (1.8471034887, 3.3500000522))
                CenterArc((5.7000000849, 3.7500000261), 0.3999999739, -90, 180)
                Line((5.7000000849, 4.15), (1.9642670538, 4.15))
                CenterArc((1.9642670538, 5.0773254954), 0.9273254954, -158.7259363649, 68.7259363649)
                Line((0.2798371691, 8.4321985732), (1.1001336287, 4.7408645052))
                CenterArc((0.3830156941, 8.3984320543), 0.1085632803, 23.4321941115, 138.4464464004)
                Line((1.2918509473, 4.8000910172), (0.4826259046, 8.4416037091))
                CenterArc((1.9642670538, 5.0773254954), 0.7273254954, -157.5938414234, 67.5938414234)
                Line((5.7000000849, 4.35), (1.9642670538, 4.35))
                CenterArc((5.7000000849, 3.7500000261), 0.5999999739, -90, 180)
                Line((5.7000000849, 3.1500000522), (4.7740778348, 3.1500000522))
                Line((4.7740778348, 3.1500000522), (6.2466713889, 0.1436813114))
                Line((6.2466713889, 0.1436813114), (6.0239665456, 0.1436813114))
                Line((4.7475158591, 2.749571857), (6.0239665456, 0.1436813114))
                CenterArc((4.1054017831, 2.4350433154), 0.7150095735, 26.0971288576, 64.5994208835)
                Line((4.0967095641, 3.1500000522), (2.2406176279, 3.1500000522))
                CenterArc((2.3692072875, 2.1841012261), 0.974420773, 97.5831701292, 52.280218107)
                Line((1.5264982097, 2.6733222936), (0.4450743696, 0.15))
                Line((0.2274808523, 0.15), (0.4450743696, 0.15))
                Line((1.476246356, 3.0637861753), (0.2274808523, 0.15))
                CenterArc((1.9183468066, 2.8743145537), 0.4809909602, 98.5178654402, 58.2835440462)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2522784952, perimeter: 41.7819772128
            with BuildLine():
                CenterArc((1.9183468066, 2.8743145537), 0.4809909602, 98.5178654402, 58.2835440462)
                Line((1.476246356, 3.0637861753), (0.2274808523, 0.15))
                Line((0.2274808523, 0.15), (0.4450743696, 0.15))
                Line((1.5264982097, 2.6733222936), (0.4450743696, 0.15))
                CenterArc((2.3692072875, 2.1841012261), 0.974420773, 97.5831701292, 52.280218107)
                Line((4.0967095641, 3.1500000522), (2.2406176279, 3.1500000522))
                CenterArc((4.1054017831, 2.4350433154), 0.7150095735, 26.0971288576, 64.5994208835)
                Line((4.7475158591, 2.749571857), (6.0239665456, 0.1436813114))
                Line((6.2466713889, 0.1436813114), (6.0239665456, 0.1436813114))
                Line((4.7740778348, 3.1500000522), (6.2466713889, 0.1436813114))
                Line((5.7000000849, 3.1500000522), (4.7740778348, 3.1500000522))
                CenterArc((5.7000000849, 3.7500000261), 0.5999999739, -90, 180)
                Line((5.7000000849, 4.35), (1.9642670538, 4.35))
                CenterArc((1.9642670538, 5.0773254954), 0.7273254954, -157.5938414234, 67.5938414234)
                Line((1.2918509473, 4.8000910172), (0.4826259046, 8.4416037091))
                CenterArc((0.3830156941, 8.3984320543), 0.1085632803, 23.4321941115, 138.4464464004)
                Line((0.2798371691, 8.4321985732), (1.1001336287, 4.7408645052))
                CenterArc((1.9642670538, 5.0773254954), 0.9273254954, -158.7259363649, 68.7259363649)
                Line((5.7000000849, 4.15), (1.9642670538, 4.15))
                CenterArc((5.7000000849, 3.7500000261), 0.3999999739, -90, 180)
                Line((5.7000000849, 3.3500000522), (1.8471034887, 3.3500000522))
            make_face()
        # OneSide extrude, distance=5.25
        extrude(amount=5.25, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2522784952, perimeter: 41.7819772128
            with BuildLine():
                CenterArc((1.9183468066, 2.8743145537), 0.4809909602, 98.5178654402, 58.2835440462)
                Line((1.476246356, 3.0637861753), (0.2274808523, 0.15))
                Line((0.2274808523, 0.15), (0.4450743696, 0.15))
                Line((1.5264982097, 2.6733222936), (0.4450743696, 0.15))
                CenterArc((2.3692072875, 2.1841012261), 0.974420773, 97.5831701292, 52.280218107)
                Line((4.0967095641, 3.1500000522), (2.2406176279, 3.1500000522))
                CenterArc((4.1054017831, 2.4350433154), 0.7150095735, 26.0971288576, 64.5994208835)
                Line((4.7475158591, 2.749571857), (6.0239665456, 0.1436813114))
                Line((6.2466713889, 0.1436813114), (6.0239665456, 0.1436813114))
                Line((4.7740778348, 3.1500000522), (6.2466713889, 0.1436813114))
                Line((5.7000000849, 3.1500000522), (4.7740778348, 3.1500000522))
                CenterArc((5.7000000849, 3.7500000261), 0.5999999739, -90, 180)
                Line((5.7000000849, 4.35), (1.9642670538, 4.35))
                CenterArc((1.9642670538, 5.0773254954), 0.7273254954, -157.5938414234, 67.5938414234)
                Line((1.2918509473, 4.8000910172), (0.4826259046, 8.4416037091))
                CenterArc((0.3830156941, 8.3984320543), 0.1085632803, 23.4321941115, 138.4464464004)
                Line((0.2798371691, 8.4321985732), (1.1001336287, 4.7408645052))
                CenterArc((1.9642670538, 5.0773254954), 0.9273254954, -158.7259363649, 68.7259363649)
                Line((5.7000000849, 4.15), (1.9642670538, 4.15))
                CenterArc((5.7000000849, 3.7500000261), 0.3999999739, -90, 180)
                Line((5.7000000849, 3.3500000522), (1.8471034887, 3.3500000522))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)
    return part.part


def model_70169_914780d4_0011():
    """Model: 1st gear carrier v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7953502442, perimeter: 7.3130354359
            with BuildLine():
                Line((-0.1275168659, 0.2404449986), (-0.1502459209, 0.4998856392))
                Line((-0.1502459209, 0.4998856392), (-1.6071049026, -0.7374466466))
                Line((-1.6071049026, -0.7374466466), (-0.2999232136, -2.014692877))
                Line((-0.2999232136, -2.014692877), (-0.1275168659, -1.8382457556))
                Line((-0.1275168659, -1.8382457556), (-1.2541159541, -0.7374466466))
                Line((-1.2541159541, -0.7374466466), (-0.1275168659, 0.2404449986))
            make_face()
            # Profile area: 0.7953502442, perimeter: 7.3130354359
            with BuildLine():
                Line((1.6059676547, -0.7374466466), (0.2987859657, -2.014692877))
                Line((0.1491086731, 0.4998856392), (1.6059676547, -0.7374466466))
                Line((0.1263796181, 0.2404449986), (0.1491086731, 0.4998856392))
                Line((1.2529787062, -0.7374466466), (0.1263796181, 0.2404449986))
                Line((0.1263796181, -1.8382457556), (1.2529787062, -0.7374466466))
                Line((0.2987859657, -2.014692877), (0.1263796181, -1.8382457556))
            make_face()
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True, mode=Mode.ADD)
    return part.part


def model_70188_002060a2_0001():
    """Model: 1st gear carrier v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7953502442, perimeter: 7.3130354359
            with BuildLine():
                Line((-0.1275168659, 0.2404449986), (-0.1502459209, 0.4998856392))
                Line((-0.1502459209, 0.4998856392), (-1.6071049026, -0.7374466466))
                Line((-1.6071049026, -0.7374466466), (-0.2999232136, -2.014692877))
                Line((-0.2999232136, -2.014692877), (-0.1275168659, -1.8382457556))
                Line((-0.1275168659, -1.8382457556), (-1.2541159541, -0.7374466466))
                Line((-1.2541159541, -0.7374466466), (-0.1275168659, 0.2404449986))
            make_face()
            # Profile area: 0.7953502442, perimeter: 7.3130354359
            with BuildLine():
                Line((1.6059676547, -0.7374466466), (0.2987859657, -2.014692877))
                Line((0.1491086731, 0.4998856392), (1.6059676547, -0.7374466466))
                Line((0.1263796181, 0.2404449986), (0.1491086731, 0.4998856392))
                Line((1.2529787062, -0.7374466466), (0.1263796181, 0.2404449986))
                Line((0.1263796181, -1.8382457556), (1.2529787062, -0.7374466466))
                Line((0.2987859657, -2.014692877), (0.1263796181, -1.8382457556))
            make_face()
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True, mode=Mode.ADD)
    return part.part


def model_70214_7e7a1219_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 73.3560257175, perimeter: 30.3614723945
            with Locations((2, -1)):
                Circle(4.8321784111)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_70355_e5f58cd5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20700, perimeter: 2790
            with BuildLine():
                Line((0, 15), (0, 0))
                Line((0, 0), (300, 0))
                Line((300, 0), (300, -450))
                Line((300, -450), (-300, -450))
                Line((-300, -465), (-300, -450))
                Line((315, -465), (-300, -465))
                Line((315, 15), (315, -465))
                Line((0, 15), (315, 15))
            make_face()
        # OneSide extrude, distance=250
        extrude(amount=250)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(300, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 27000, perimeter: 740
            with BuildLine():
                Line((390, 125), (120, 125))
                Line((390, 225), (390, 125))
                Line((120, 225), (390, 225))
                Line((120, 125), (120, 225))
            make_face()
        # OneSide extrude, distance=-120
        extrude(amount=-120, mode=Mode.SUBTRACT)
    return part.part


def model_71444_50b4c168_0001():
    """Model: Spur Gear (24 teeth) (1)"""
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
            # Profile area: 90.1697938148, perimeter: 37.8871047475
            with BuildLine():
                CenterArc((0, 0), 5.39492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.8352546687, perimeter: 3.5676306031
            with BuildLine():
                _nurbs_edge([(5.6199632879, -0.4525622818), (5.6521556147, -0.4519273633), (5.7171054252, -0.4506463799), (5.8142222789, -0.4348720957), (5.9117817233, -0.4137950667), (6.0095732206, -0.3865880246), (6.1074837957, -0.3542949712), (6.2054152409, -0.3171691795), (6.3032304317, -0.2754339161), (6.4009922023, -0.2295636824), (6.4651963757, -0.1958486317), (6.4975385572, -0.1788650272)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0964818268, 0.194657454, 0.2944688774, 0.3959106457, 0.4989809965, 0.6036791367, 0.7100046413, 0.8179572559, 0.9275368163, 0.9275368163, 0.9275368163, 0.9275368163], 3)
                CenterArc((0, 0), 6.5, -1.576846918, 3.1536938361)
                _nurbs_edge([(5.6199632879, 0.4525622818), (5.6521556147, 0.4519273633), (5.7171054252, 0.4506463799), (5.8142222789, 0.4348720957), (5.9117817233, 0.4137950667), (6.0095732206, 0.3865880246), (6.1074837957, 0.3542949712), (6.2054152409, 0.3171691795), (6.3032304317, 0.2754339161), (6.4009922023, 0.2295636824), (6.4651963757, 0.1958486317), (6.4975385572, 0.1788650272)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0964818268, 0.194657454, 0.2944688774, 0.3959106457, 0.4989809965, 0.6036791367, 0.7100046413, 0.8179572559, 0.9275368163, 0.9275368163, 0.9275368163, 0.9275368163], 3)
                Line((5.3765156299, 0.4330382885), (5.6199632879, 0.4525622818))
                Line((5.3765156299, -0.4330382885), (5.3765156299, 0.4330382885))
                Line((5.3765156299, -0.4330382885), (5.6199632879, -0.4525622818))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_71444_50b4c168_0003():
    """Model: Component35"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.6495190528, perimeter: 3
            with BuildLine():
                Line((0.25, 0.4330127019), (0.5, 0))
                Line((-0.25, 0.4330127019), (0.25, 0.4330127019))
                Line((-0.5, 0), (-0.25, 0.4330127019))
                Line((-0.25, -0.4330127019), (-0.5, 0))
                Line((0.25, -0.4330127019), (-0.25, -0.4330127019))
                Line((0.5, 0), (0.25, -0.4330127019))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


def model_71833_9b2c8d39_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch16 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 34.7588171711, perimeter: 25.2244849356
            with BuildLine():
                Line((-209.3830142845, -54.6162374797), (-207.6954228329, -50.2656640699))
                Line((-207.6954228329, -50.2656640699), (-215.8144251889, -50.2656640699))
                Line((-215.8144251889, -50.2656640699), (-217.2429709747, -54.6162374797))
                Line((-217.2429709747, -54.6162374797), (-209.3830142845, -54.6162374797))
            make_face()
        # OneSide extrude, distance=9.767
        extrude(amount=9.767)

        # Sketch16 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 19.3578780271, perimeter: 18.9074643753
            with BuildLine():
                Line((-215.9989949877, -53.9803115152), (-214.7936101978, -50.744804974))
                Line((-209.9392752866, -53.9803115152), (-215.9989949877, -53.9803115152))
                Line((-208.764431671, -50.8267839157), (-209.9392752866, -53.9803115152))
                Line((-214.7936101978, -50.744804974), (-208.764431671, -50.8267839157))
            make_face()
        # OneSide extrude, distance=28.1375
        extrude(amount=28.1375, mode=Mode.SUBTRACT)
    return part.part


def model_72966_11b78e5e_0001():
    """Model: Internal Gear (48)"""
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
        # Gear (144.000 mm pitch dia) -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 45.3803058811, perimeter: 100.8451241802
            with BuildLine():
                CenterArc((0, 0), 8.475, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 7.575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Gear Tooth (3.000 mm module; 20.000 pressure angle) -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.359173948, perimeter: 2.576315462
            with BuildLine():
                CenterArc((0, 0), 7.585, -3.1352319204, 6.2704638407)
                Line((7.5736469827, 0.4148450087), (7.5635969076, 0.4154838377))
                _nurbs_edge([(7.5635969076, 0.4154838377), (7.5393469936, 0.401783814), (7.4910885161, 0.3745201181), (7.4177802801, 0.3361672065), (7.3442824028, 0.3000387777), (7.2705279702, 0.2663842152), (7.1965624299, 0.2352849689), (7.1224085401, 0.2068705627), (7.0480656269, 0.1814396779), (6.9736417228, 0.1588780281), (6.9234970242, 0.1469161106), (6.8985598636, 0.1409674009)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0835523803, 0.166273194, 0.2481623974, 0.3292199283, 0.4094456954, 0.4888395546, 0.567401261, 0.6451303434, 0.7220256998, 0.7220256998, 0.7220256998, 0.7220256998], 3)
                CenterArc((0, 0), 6.9, -1.1706375488, 2.3412750975)
                _nurbs_edge([(7.5635969076, -0.4154838377), (7.5393469936, -0.401783814), (7.4910885161, -0.3745201181), (7.4177802801, -0.3361672065), (7.3442824028, -0.3000387777), (7.2705279702, -0.2663842152), (7.1965624299, -0.2352849689), (7.1224085401, -0.2068705627), (7.0480656269, -0.1814396779), (6.9736417228, -0.1588780281), (6.9234970242, -0.1469161106), (6.8985598636, -0.1409674009)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0835523803, 0.166273194, 0.2481623974, 0.3292199283, 0.4094456954, 0.4888395546, 0.567401261, 0.6451303434, 0.7220256998, 0.7220256998, 0.7220256998, 0.7220256998], 3)
                Line((7.5736469827, -0.4148450087), (7.5635969076, -0.4154838377))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_73081_906f09d5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56, perimeter: 30
            with BuildLine():
                Line((0, 7), (0, 0))
                Line((0, 0), (8, 0))
                Line((8, 0), (8, 7))
                Line((8, 7), (0, 7))
            make_face()
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)
    return part.part


def model_73388_10a40b49_0027():
    """Model: Frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 32 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6174578771, perimeter: 6.3882160012
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, -118.3576384467, 261.4877412721)
                CenterArc((-1.8294160246, 5.6053280711), 6.2514182343, -77.7294409422, 2.4823401832)
                CenterArc((0, 0), 0.71, -134.8594391478, 48.4537766516)
                CenterArc((0, 0), 0.71, -86.4056624963, 176.4056624963)
                CenterArc((0, 0), 0.71, 90, 65.0052501456)
                Line((-0.6435060212, 0.3000000011), (-0.4000000084, 0.3000000012))
            make_face()
            # Profile area: 1.8023078199, perimeter: 12.2150142471
            with BuildLine():
                CenterArc((-1.8294160246, 5.6053280711), 6.2514182343, -91.1501309808, 13.4206900385)
                CenterArc((-1.8931034624, 0.915735559), 1.5617891576, -127.7499025681, 35.4823942569)
                CenterArc((-3.2778068273, -0.8726399006), 0.7, 52.2500974319, 37.9619810806)
                Line((-5.4133374904, -0.1805397404), (-3.2803978492, -0.1726446959))
                CenterArc((-6.1, 0), 0.71, -65.5194664751, 50.7884620358)
                CenterArc((-4.4567581438, -5.9015813572), 5.4257904475, 67.2281983948, 37.1684214732)
                CenterArc((-1.9336816944, 0.108859042), 1.0927453208, -112.7718016052, 23.3211364885)
                CenterArc((-1.9970254064, 6.7154232002), 7.6996131416, -89.4506651167, 14.8264093448)
                CenterArc((0, 0), 0.71, -134.8594391478, 48.4537766516)
            make_face()
            # Profile area: 2.1221222996, perimeter: 12.5240569753
            with BuildLine():
                CenterArc((0, 0), 0.71, 90, 65.0052501456)
                Line((-6.1, 0.71), (0, 0.71))
                CenterArc((-6.1, 0), 0.71, 24.9947498279, 65.0052501721)
                Line((-5.4564939787, 0.3000000008), (-0.6435060212, 0.3000000011))
            make_face()
            # Profile area: 0.1808207927, perimeter: 2.2431357998
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 143.1301028288, 98.5122587245)
                Line((-0.6435060212, 0.3000000011), (-0.4000000084, 0.3000000012))
                CenterArc((0, 0), 0.71, 155.0052501456, 70.1353107066)
                CenterArc((-1.8294160246, 5.6053280711), 6.2514182343, -77.7294409422, 2.4823401832)
            make_face()
            # Profile area: 0.104694405, perimeter: 1.464035371
            with BuildLine():
                Line((-5.7001024446, 0.3000000008), (-5.4564939787, 0.3000000008))
                CenterArc((-6.1, 0), 0.4999180486, -21.2706252691, 58.147567719)
                Line((-5.6341376992, -0.1813570292), (-5.4133374904, -0.1805397404))
                CenterArc((-6.1, 0), 0.71, -14.7310044393, 39.7257542673)
            make_face()
            # Profile area: 0.6938417252, perimeter: 7.0669243096
            with BuildLine():
                CenterArc((-6.1, 0), 0.71, 24.9947498279, 65.0052501721)
                CenterArc((-6.1, 0), 0.71, 90, 204.4805335249)
                CenterArc((-6.1, 0), 0.71, -65.5194664751, 50.7884620358)
                Line((-5.6341376992, -0.1813570292), (-5.4133374904, -0.1805397404))
                CenterArc((-6.1, 0), 0.4999180486, 36.8769424499, 301.852432281)
                Line((-5.7001024446, 0.3000000008), (-5.4564939787, 0.3000000008))
            make_face()
            # Profile area: 3.1676214618, perimeter: 11.2026101537
            with BuildLine():
                Line((-5.4564939787, 0.3000000008), (-0.6435060212, 0.3000000011))
                CenterArc((-6.1, 0), 0.71, -14.7310044393, 39.7257542673)
                Line((-5.4133374904, -0.1805397404), (-3.2803978492, -0.1726446959))
                CenterArc((-3.2778068273, -0.8726399006), 0.7, 52.2500974319, 37.9619810806)
                CenterArc((-1.8931034624, 0.915735559), 1.5617891576, -127.7499025681, 35.4823942569)
                CenterArc((-1.8294160246, 5.6053280711), 6.2514182343, -91.1501309808, 13.4206900385)
                CenterArc((0, 0), 0.71, 155.0052501456, 70.1353107066)
            make_face()
        # OneSide extrude, distance=0.71
        extrude(amount=0.71)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 32 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.502654848, perimeter: 5.0265482925
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 143.1301028288, 98.5122587245)
                CenterArc((0, 0), 0.5000000075, -118.3576384467, 261.4877412721)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5023973877, perimeter: 5.0260333298
            with BuildLine():
                CenterArc((-6.1, 0), 0.4999180486, 36.8769424499, 301.852432281)
                CenterArc((-6.1, 0), 0.4999180486, -21.2706252691, 58.147567719)
            make_face()
            with BuildLine():
                CenterArc((-6.1, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.21
        extrude(amount=0.21, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.71), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.4531366595, perimeter: 12.1870203534
            with BuildLine():
                Line((-0.4000000084, 0.3000000012), (-5.7001024446, 0.3000000008))
                CenterArc((-6.1, 0), 0.4999180486, -21.2706252691, 58.147567719)
                Line((-5.6341376992, -0.1813570292), (-3.2803978492, -0.1726446959))
                CenterArc((-3.2778068273, -0.8726399006), 0.7, 52.2500974319, 37.9619810806)
                CenterArc((-1.8931034624, 0.915735559), 1.5617891576, -127.7499025681, 35.4823942569)
                CenterArc((-1.8294160246, 5.6053280711), 6.2514182343, -91.1501309808, 15.9030302217)
                CenterArc((0, 0), 0.5000000075, 143.1301028288, 98.5122587245)
            make_face()
        # OneSide extrude, distance=-0.37
        extrude(amount=-0.37, mode=Mode.SUBTRACT)
    return part.part


def model_73806_a694a87d_0001():
    """Model: Leg 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 766.8424773061, perimeter: 207.5179192236
            with BuildLine():
                Line((-6.2956687525, 0), (6.35, 0))
                Line((-6.2956687525, 0), (-12.6456687525, 0))
                Line((-12.6456687525, 0), (-17.7256687525, -43.2))
                Line((-17.7256687525, -43.2), (-10.1056687525, -43.2))
                Line((-10.1056687525, -43.2), (-6.1604777281, -9.6503440449))
                Line((-6.1604777281, -9.6503440449), (6.2148089757, -9.6503440449))
                Line((10.16, -43.2), (6.2148089757, -9.6503440449))
                Line((17.78, -43.2), (10.16, -43.2))
                Line((12.7, 0), (17.78, -43.2))
                Line((6.35, 0), (12.7, 0))
            make_face()
            # Profile area: 22.7622037545, perimeter: 28.891337505
            with BuildLine():
                Line((6.35, 1.8), (6.35, 0))
                Line((6.35, 1.8), (-6.2956687525, 1.8))
                Line((-6.2956687525, 1.8), (-6.2956687525, 0))
                Line((-6.2956687525, 0), (6.35, 0))
            make_face()
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.9594028589, perimeter: 18.4389208589
            with BuildLine():
                Line((-0.322564591, -6.72), (-0.322564591, 1.8))
                Line((0.3768958385, -6.72), (-0.322564591, -6.72))
                Line((0.3768958385, -6.72), (0.3768958385, 1.8))
                Line((0.3768958385, 1.8), (-0.322564591, 1.8))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


def model_73906_ca7def41_0001():
    """Model: Sofa Set v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.1384912454, perimeter: 22.3701947787
            with BuildLine():
                Line((-0.3432882756, -7.7520102701), (-0.3432882756, -7.1843707185))
                Line((-0.3432882756, -7.1843707185), (-0.579736362, -7.1843707185))
                Line((-0.579736362, -7.1843707185), (-2.6164221351, -7.1843707185))
                Line((-2.6164221351, -7.1843707185), (-2.6164221351, -3.7949608126))
                Line((-0.579736362, -3.7949608126), (-2.6164221351, -3.7949608126))
                Line((-0.3432882756, -3.7949608126), (-0.579736362, -3.7949608126))
                Line((-0.3432882756, -3.1833350158), (-0.3432882756, -3.7949608126))
                Line((-4.6865765511, -3.1833350158), (-0.3432882756, -3.1833350158))
                Line((-4.6865765511, -7.7520102701), (-4.6865765511, -3.1833350158))
                Line((-0.3432882756, -7.7520102701), (-4.6865765511, -7.7520102701))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.567967363, perimeter: 20.4230958734
            with BuildLine():
                Line((-0.579736362, -3.7949608126), (-2.6164221351, -3.7949608126))
                Line((-2.6164221351, -7.1843707185), (-2.6164221351, -3.7949608126))
                Line((-0.579736362, -7.1843707185), (-2.6164221351, -7.1843707185))
                Line((-0.579736362, -3.7949608126), (-0.579736362, -7.1843707185))
            make_face()
            with BuildLine():
                Line((-2.5, -7.0171800954), (-2.5, -4))
                Line((-2.5, -4), (-0.7317278376, -4))
                Line((-0.7317278376, -4), (-0.7317278376, -7.0171800954))
                Line((-0.7317278376, -7.0171800954), (-2.5, -7.0171800954))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.3351955714, perimeter: 9.5709045154
            with BuildLine():
                Line((-0.7317278376, -7.0171800954), (-2.5, -7.0171800954))
                Line((-0.7317278376, -4), (-0.7317278376, -7.0171800954))
                Line((-2.5, -4), (-0.7317278376, -4))
                Line((-2.5, -7.0171800954), (-2.5, -4))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3351955714, perimeter: 9.5709045154
            with BuildLine():
                Line((-0.7317278376, -7.0171800954), (-2.5, -7.0171800954))
                Line((-0.7317278376, -4), (-0.7317278376, -7.0171800954))
                Line((-2.5, -4), (-0.7317278376, -4))
                Line((-2.5, -7.0171800954), (-2.5, -4))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)
    return part.part


def model_74281_623219a4_0000():
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
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((-10, 5), (-20, 5))
                Line((-10, 15), (-10, 5))
                Line((-20, 15), (-10, 15))
                Line((-20, 5), (-20, 15))
            make_face()
        # OneSide extrude, distance=2.0832
        extrude(amount=2.0832)
    return part.part


def model_75646_4baf69b2_0002():
    """Model: ?? v1"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 71.0728631773, perimeter: 76.6314955146
            with BuildLine():
                Line((1.4400787953, -2), (11.4716812474, 28))
                Line((11.4716812474, 28), (9.4716812474, 28))
                Line((9.4716812474, 28), (0, 0))
                Line((0, 0), (-5, 0))
                Line((-5, 0), (-5, -2))
                Line((-5, -2), (1.4400787953, -2))
            make_face()
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_75966_08c4ab3e_0001():
    """Model: 4 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 244.7661573733, perimeter: 123.6024214187
            with BuildLine():
                CenterArc((1, -24), 2.5, 53.1301023542, 253.7397952917)
                Line((2.5, -26), (15.5, -26))
                CenterArc((15.5, -24), 2, -90, 90)
                Line((17.5, 2.5), (17.5, -24))
                CenterArc((15.5, 2.5), 2, 0, 90)
                Line((2.5, 4.5), (15.5, 4.5))
                CenterArc((1, 2.5), 2.5, 53.1301023542, 253.7397952917)
                Line((2.5, 0.5), (11.4336376326, 0.5))
                CenterArc((11.4336376326, -1.5), 2, 0.1551777142, 89.8448222858)
                Line((13.4336302973, -1.4945832825), (13.4836692001, -19.9702448393))
                CenterArc((11.4836765353, -19.9756615568), 2, -89.8448222858, 90)
                Line((2.5, -22), (11.4890932528, -21.9756542215))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_76298_af8ea172_0004():
    """Model: M3 Grub Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0346410162, perimeter: 0.692820323
            with BuildLine():
                Line((0.1, -0.0577350269), (0.1, 0.0577350269))
                Line((0.1, 0.0577350269), (0, 0.1154700538))
                Line((0, 0.1154700538), (-0.1, 0.0577350269))
                Line((-0.1, 0.0577350269), (-0.1, -0.0577350269))
                Line((-0.1, -0.0577350269), (0, -0.1154700538))
                Line((0, -0.1154700538), (0.1, -0.0577350269))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_76298_af8ea172_0011():
    """Model: M6 GrubScrew v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0779422863, perimeter: 1.0392304845
            with BuildLine():
                Line((-0.15, 0.0866025404), (-0.15, -0.0866025404))
                Line((-0.15, -0.0866025404), (0, -0.1732050808))
                Line((0, -0.1732050808), (0.15, -0.0866025404))
                Line((0.15, -0.0866025404), (0.15, 0.0866025404))
                Line((0.15, 0.0866025404), (0, 0.1732050808))
                Line((0, 0.1732050808), (-0.15, 0.0866025404))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_76880_9bb28e72_0003():
    """Model: casing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_76969_10fcc619_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 283.06395, perimeter: 72.39
            with BuildLine():
                Line((-12.3825, 5.715), (12.3825, 5.715))
                Line((-12.3825, -5.715), (-12.3825, 5.715))
                Line((12.3825, -5.715), (-12.3825, -5.715))
                Line((12.3825, 5.715), (12.3825, -5.715))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 26 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.905), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 32.8943233298, perimeter: 27.6522452512
            with BuildLine():
                Line((12.3825, -5.715), (12.3825, 5.715))
                Line((6.6267128907, 0), (12.3825, 5.715))
                Line((12.3825, -5.715), (6.6267128907, 0))
            make_face()
            # Profile area: 16.8587161019, perimeter: 19.8546142825
            with BuildLine():
                Line((1.8302236329, -4.7625), (5.9507860052, -0.6711370794))
                Line((10.0713483775, -4.7625), (1.8302236329, -4.7625))
                Line((5.9507860052, -0.6711370794), (10.0713483775, -4.7625))
            make_face()
            # Profile area: 16.8587161019, perimeter: 19.8546142825
            with BuildLine():
                Line((5.9507860052, 0.6711370794), (10.0713483775, 4.7625))
                Line((10.0713483775, 4.7625), (1.8302236329, 4.7625))
                Line((1.8302236329, 4.7625), (5.9507860052, 0.6711370794))
            make_face()
            # Profile area: 22.8310986318, perimeter: 23.1053531539
            with BuildLine():
                Line((-4.795210194, -0.47625), (0, -5.23748))
                Line((0, -5.23748), (4.795210194, -0.47625))
                Line((4.795210194, -0.47625), (-4.795210194, -0.47625))
            make_face()
            # Profile area: 22.8310986318, perimeter: 23.1053531539
            with BuildLine():
                Line((-4.795210194, 0.47625), (0, 5.23748))
                Line((4.795210194, 0.47625), (-4.795210194, 0.47625))
                Line((0, 5.23748), (4.795210194, 0.47625))
            make_face()
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)
    return part.part


def model_77001_aa7c50ef_0003():
    """Model: 02_Biela v1 (2)"""
    with BuildPart() as part:
        # Base de Biela -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5993993413, perimeter: 8.7179751777
            with BuildLine():
                CenterArc((0, 0), 0.7625088433, 40.7663787891, 98.4672424219)
                CenterArc((0, 0), 0.7625088433, 139.2336212109, 261.5327575781)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0315369562, perimeter: 15.0041739091
            with BuildLine():
                CenterArc((0, 5.8745211043), 1.2627442223, -136.3395181948, 92.6790363895)
                CenterArc((0, 5.8745211043), 1.2627442223, -43.6604818052, 267.3209636105)
            make_face()
            with BuildLine():
                CenterArc((0, 5.8745211043), 1.1252442223, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Base de Biela -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7297393758, perimeter: 20.5334819975
            with BuildLine():
                Line((-0.4462232366, 3.836193748), (-0.4462232366, 0.8512307266))
                CenterArc((-0.9873309942, 0.8512307266), 0.5411077576, -40.7663787891, 40.7663787891)
                CenterArc((0, 0), 0.7625088433, 40.7663787891, 98.4672424219)
                CenterArc((0.9873309942, 0.8512307266), 0.5411077576, -180, 40.7663787891)
                Line((0.4462232366, 3.836193748), (0.4462232366, 0.8512307266))
                CenterArc((2.1359352376, 3.836193748), 1.689712001, 136.3395181948, 43.6604818052)
                CenterArc((0, 5.8745211043), 1.2627442223, -136.3395181948, 92.6790363895)
                CenterArc((-2.1359352376, 3.836193748), 1.689712001, 0, 43.6604818052)
            make_face()
            with BuildLine():
                Line((0.2798603189, 4.163188745), (0.2798603189, 1.1097070536))
                CenterArc((0, 1.1097070536), 0.2798603189, 179.9991418664, 180.0008581343)
                Line((-0.2798603189, 1.1097112452), (-0.2798603189, 4.163188745))
                CenterArc((0, 4.163188745), 0.2798603189, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0460154239, perimeter: 14.8454439947
            with BuildLine():
                CenterArc((0, 4.163188745), 0.2798603189, 0, 180)
                Line((-0.2798603189, 1.1097112452), (-0.2798603189, 4.163188745))
                CenterArc((0, 1.1097070536), 0.2798603189, 179.9991418664, 180.0008581343)
                Line((0.2798603189, 4.163188745), (0.2798603189, 1.1097070536))
            make_face()
            with BuildLine():
                Line((0.1389584782, 4.163188745), (0.1389584782, 1.1097070536))
                CenterArc((0, 1.1097070536), 0.1389584782, 179.9982717316, 180.0017282686)
                Line((-0.1388665256, 4.158134367), (-0.1389584782, 1.1097112452))
                CenterArc((0, 4.163188745), 0.1389584782, 0, 182.0844962272)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9091364816, perimeter: 6.980066368
            with BuildLine():
                CenterArc((0, 4.163188745), 0.1389584782, 0, 182.0844962272)
                Line((-0.1388665256, 4.158134367), (-0.1389584782, 1.1097112452))
                CenterArc((0, 1.1097070536), 0.1389584782, 179.9982717316, 180.0017282686)
                Line((0.1389584782, 4.163188745), (0.1389584782, 1.1097070536))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)

        # Base de Biela -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 1.0460154239, perimeter: 14.8454439947
            with BuildLine():
                CenterArc((0, 4.163188745), 0.2798603189, 0, 180)
                Line((-0.2798603189, 1.1097112452), (-0.2798603189, 4.163188745))
                CenterArc((0, 1.1097070536), 0.2798603189, 179.9991418664, 180.0008581343)
                Line((0.2798603189, 4.163188745), (0.2798603189, 1.1097070536))
            make_face()
            with BuildLine():
                Line((0.1389584782, 4.163188745), (0.1389584782, 1.1097070536))
                CenterArc((0, 1.1097070536), 0.1389584782, 179.9982717316, 180.0017282686)
                Line((-0.1388665256, 4.158134367), (-0.1389584782, 1.1097112452))
                CenterArc((0, 4.163188745), 0.1389584782, 0, 182.0844962272)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9091364816, perimeter: 6.980066368
            with BuildLine():
                CenterArc((0, 4.163188745), 0.1389584782, 0, 182.0844962272)
                Line((-0.1388665256, 4.158134367), (-0.1389584782, 1.1097112452))
                CenterArc((0, 1.1097070536), 0.1389584782, 179.9982717316, 180.0017282686)
                Line((0.1389584782, 4.163188745), (0.1389584782, 1.1097070536))
            make_face()
        # TwoSides offset extrude, full=2.4, trim=0.15
        extrude(amount=2.4, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=0.15, mode=Mode.ADD)

        # Base de Biela -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 1.0460154239, perimeter: 14.8454439947
            with BuildLine():
                CenterArc((0, 4.163188745), 0.2798603189, 0, 180)
                Line((-0.2798603189, 1.1097112452), (-0.2798603189, 4.163188745))
                CenterArc((0, 1.1097070536), 0.2798603189, 179.9991418664, 180.0008581343)
                Line((0.2798603189, 4.163188745), (0.2798603189, 1.1097070536))
            make_face()
            with BuildLine():
                Line((0.1389584782, 4.163188745), (0.1389584782, 1.1097070536))
                CenterArc((0, 1.1097070536), 0.1389584782, 179.9982717316, 180.0017282686)
                Line((-0.1388665256, 4.158134367), (-0.1389584782, 1.1097112452))
                CenterArc((0, 4.163188745), 0.1389584782, 0, 182.0844962272)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9091364816, perimeter: 6.980066368
            with BuildLine():
                CenterArc((0, 4.163188745), 0.1389584782, 0, 182.0844962272)
                Line((-0.1388665256, 4.158134367), (-0.1389584782, 1.1097112452))
                CenterArc((0, 1.1097070536), 0.1389584782, 179.9982717316, 180.0017282686)
                Line((0.1389584782, 4.163188745), (0.1389584782, 1.1097070536))
            make_face()
        # TwoSides offset extrude, full=-2.5, trim=-0.15
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.15, mode=Mode.ADD)
    return part.part


def model_77665_e2629513_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.785321467, perimeter: 3.1415528305
            with BuildLine():
                CenterArc((0, 5.5), 0.5, -90, 96.1082489887)
                CenterArc((1.5133082809, 5.7665681281), 1.0383058641, -171.8781084595, 3.7364646962)
                CenterArc((0, 5.5), 0.5, 13.8719987884, 160.0197522229)
                CenterArc((0, 5.5), 0.5, 173.8917510113, 96.1082489887)
            make_face()
            # Profile area: 0.9557802014, perimeter: 6.4965231656
            with BuildLine():
                CenterArc((0, 5.5), 0.5, 13.8719987884, 160.0197522229)
                CenterArc((1.5133082809, 5.7665681281), 1.0383058641, 76.2977545365, 111.824137004)
                CenterArc((0, 0), 7, 75.4442089275, 6.4863663141)
                CenterArc((0.858981034, 5.579931073), 1.3564057042, 84.7705334485, 96.3585312095)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_77666_ba753255_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2453475574, perimeter: 2.9594940363
            with BuildLine():
                CenterArc((0.8600539368, 4.8813617896), 1.1856762568, 111.4600466275, 45.0622196589)
                CenterArc((0, 5.25), 0.25, 7.3342744218, 148.1523294109)
                CenterArc((1.0894424562, 5.1104657832), 0.8587761818, 105.4924234451, 62.9914898451)
                CenterArc((0, 0), 6, 81.7587014626, 4.167273393)
            make_face()
            # Profile area: 0.1954685781, perimeter: 1.5695268162
            with BuildLine():
                CenterArc((0, 5.25), 0.25, 7.3342744218, 148.1523294109)
                CenterArc((0, 5.25), 0.25, 155.4866038326, 114.5133961674)
                CenterArc((0, 5.25), 0.25, -90, 68.0684762823)
                CenterArc((1.0894424562, 5.1104657832), 0.8587761818, 168.4839132901, 8.4349241238)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_77976_300b479c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.5, perimeter: 71
            with BuildLine():
                Line((25, 0), (17.5, 0))
                Line((17.5, 0), (17.5, -5))
                Line((7.5, -5), (17.5, -5))
                Line((7.5, 0), (7.5, -5))
                Line((0, 0), (7.5, 0))
                Line((0, 0), (0, -0.5))
                Line((0, -0.5), (7, -0.5))
                Line((7, -0.5), (7, -5.5))
                Line((18, -5.5), (7, -5.5))
                Line((18, -0.5), (18, -5.5))
                Line((25, -0.5), (18, -0.5))
                Line((25, 0), (25, -0.5))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0401814742, perimeter: 29.1017641285
            with BuildLine():
                CenterArc((-3.5, -12.5), 2.523398598, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.5, -12.5), 2.1082910157, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_78075_e8f2196e_0002():
    """Model: Spur Gear (38 teeth)"""
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
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.3846523132, perimeter: 6.5340100646
            with BuildLine():
                CenterArc((0, 0), 0.88492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.155, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> 押し出し2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.009241708, perimeter: 0.382368311
            with BuildLine():
                _nurbs_edge([(0.8912965153, -0.0501804417), (0.8952954483, -0.0500508693), (0.9033486008, -0.0497899331), (0.9153763894, -0.0478802012), (0.9274410373, -0.0453960968), (0.9395220693, -0.042251621), (0.9516116058, -0.038563693), (0.963701942, -0.034362627), (0.9757817018, -0.0296748119), (0.9878587698, -0.0245535451), (0.995817568, -0.0208060557), (0.9998209818, -0.0189210033)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0119919738, 0.0241497403, 0.0364676233, 0.048945089, 0.0615819649, 0.0743781736, 0.0873336733, 0.1004484391, 0.113722455, 0.113722455, 0.113722455, 0.113722455], 3)
                CenterArc((0, 0), 1, -1.0841583316, 2.1683166631)
                _nurbs_edge([(0.8912965153, 0.0501804417), (0.8952954483, 0.0500508693), (0.9033486008, 0.0497899331), (0.9153763894, 0.0478802012), (0.9274410373, 0.0453960968), (0.9395220693, 0.042251621), (0.9516116058, 0.038563693), (0.963701942, 0.034362627), (0.9757817018, 0.0296748119), (0.9878587698, 0.0245535451), (0.995817568, 0.0208060557), (0.9998209818, 0.0189210033)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0119919738, 0.0241497403, 0.0364676233, 0.048945089, 0.0615819649, 0.0743781736, 0.0873336733, 0.1004484391, 0.113722455, 0.113722455, 0.113722455, 0.113722455], 3)
                Line((0.8825224204, 0.0497426673), (0.8912965153, 0.0501804417))
                Line((0.8825224204, -0.0497426673), (0.8825224204, 0.0497426673))
                Line((0.8825224204, -0.0497426673), (0.8912965153, -0.0501804417))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


def model_78091_0b1734e4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 105, perimeter: 52
            with BuildLine():
                Line((-5, 0), (-5, -5))
                Line((-5, -5), (-10, -5))
                Line((-10, -5), (-10, -16))
                Line((-10, -16), (-5, -16))
                Line((-5, -16), (-5, -10))
                Line((-5, -10), (0, -10))
                Line((0, -10), (0, 0))
                Line((-5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((-10, -10), (-5, -10))
                Line((-5, -5), (-5, -10))
                Line((-5, -5), (-10, -5))
                Line((-10, -5), (-10, -10))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_78098_0810099f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.3358398303, perimeter: 27.3362817987
            with BuildLine():
                Line((1.5, -6), (3, -6))
                Line((-1.5, -6), (1.5, -6))
                Line((-3, -6), (-1.5, -6))
                Line((-3, -8.5), (-3, -6))
                CenterArc((0, -8.5), 3, 180, 180)
                Line((3, -6), (3, -8.5))
            make_face()
            with BuildLine():
                CenterArc((0, -8.3), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8, perimeter: 9.4
            with BuildLine():
                Line((1.5, -1.3), (3, -1.3))
                Line((1.5, -1.3), (1.5, -4.5))
                Line((1.5, -4.5), (3, -4.5))
                Line((3, -1.3), (3, -4.5))
            make_face()
            # Profile area: 9.6, perimeter: 12.4
            with BuildLine():
                Line((-1.5, -4.5), (-1.5, -1.3))
                Line((-1.5, -4.5), (1.5, -4.5))
                Line((1.5, -1.3), (1.5, -4.5))
                Line((-1.5, -1.3), (1.5, -1.3))
            make_face()
            # Profile area: 4.8, perimeter: 9.4
            with BuildLine():
                Line((-3, -4.5), (-3, -1.3))
                Line((-3, -4.5), (-1.5, -4.5))
                Line((-1.5, -4.5), (-1.5, -1.3))
                Line((-3, -1.3), (-1.5, -1.3))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.95, perimeter: 5.6
            with BuildLine():
                Line((1.5, 0), (1.5, -1.3))
                Line((1.5, -1.3), (3, -1.3))
                Line((3, 0), (3, -1.3))
                Line((1.5, 0), (3, 0))
            make_face()
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((-3, -6), (-1.5, -6))
                Line((-1.5, -6), (-1.5, -4.5))
                Line((-3, -4.5), (-1.5, -4.5))
                Line((-3, -6), (-3, -4.5))
            make_face()
            # Profile area: 1.95, perimeter: 5.6
            with BuildLine():
                Line((-3, -1.3), (-3, 0))
                Line((-3, -1.3), (-1.5, -1.3))
                Line((-1.5, -1.3), (-1.5, 0))
                Line((-3, 0), (-1.5, 0))
            make_face()
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((1.5, -4.5), (3, -4.5))
                Line((1.5, -4.5), (1.5, -6))
                Line((1.5, -6), (3, -6))
                Line((3, -4.5), (3, -6))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.9, perimeter: 8.6
            with BuildLine():
                Line((-1.5, -1.3), (1.5, -1.3))
                Line((1.5, 0), (1.5, -1.3))
                Line((-1.5, 0), (1.5, 0))
                Line((-1.5, -1.3), (-1.5, 0))
            make_face()
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((-1.5, -6), (-1.5, -4.5))
                Line((-1.5, -6), (1.5, -6))
                Line((1.5, -4.5), (1.5, -6))
                Line((-1.5, -4.5), (1.5, -4.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_78422_3d6c0e4e_0005():
    """Model: Wall bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10, perimeter: 13
            with BuildLine():
                Line((0, 4), (0, 0))
                Line((0, 0), (2.5, 0))
                Line((2.5, 0), (2.5, 4))
                Line((2.5, 4), (0, 4))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 64, perimeter: 40
            with BuildLine():
                Line((-0.75, 8), (3.25, 8))
                Line((-0.75, -8), (-0.75, 8))
                Line((3.25, -8), (-0.75, -8))
                Line((3.25, 8), (3.25, -8))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)
    return part.part


def model_78603_4720dcb8_0000():
    """Model: Tyre"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)
    return part.part


def model_78603_4720dcb8_0002():
    """Model: Dia Adjuster"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4890275602, perimeter: 4.4122295645
            with BuildLine():
                Line((-0.7499909099, 0.0036925614), (-0.4999863648, 0.0036925614))
                CenterArc((0, 0), 0.5, 0.4231402183, 179.1537195633)
                Line((0.4999863648, 0.0036925614), (0.7499909099, 0.0036925614))
                CenterArc((0, 0), 0.75, 0.2820920543, 89.7179079457)
                CenterArc((0, 0), 0.75, 90, 89.7179079457)
            make_face()
            # Profile area: 0.1207067379, perimeter: 2.6707030172
            with BuildLine():
                CenterArc((0, 0), 0.75, 0.2820920543, 89.7179079457)
                Line((0.7499909099, 0.75), (0.7499909099, 0.0036925614))
                Line((0, 0.75), (0.7499909099, 0.75))
            make_face()
            # Profile area: 0.1207067379, perimeter: 2.6707030172
            with BuildLine():
                CenterArc((0, 0), 0.75, 90, 89.7179079457)
                Line((-0.7499909099, 0.75), (0, 0.75))
                Line((-0.7499909099, 0.0036925614), (-0.7499909099, 0.75))
            make_face()
        # OneSide extrude, distance=0.049
        extrude(amount=0.049)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0652683852, perimeter: 2.0249752627
            with BuildLine():
                Line((-0.5000000075, 0.099), (0.4999909099, 0.099))
                CenterArc((-0.0000045488, -1.1387514743), 1.3349247809, 68.0035257822, 43.9929484355)
            make_face()
            # Profile area: 0.0499995459, perimeter: 2.0999818348
            with BuildLine():
                Line((0.4999909099, 0.049), (-0.5000000075, 0.049))
                Line((0.4999909099, 0.099), (0.4999909099, 0.049))
                Line((-0.5000000075, 0.099), (0.4999909099, 0.099))
                Line((-0.5000000075, 0.049), (-0.5000000075, 0.099))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_78603_4720dcb8_0004():
    """Model: Bolt 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.05), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_78608_6fed6de8_0000():
    """Model: Spur Gear (25 teeth)"""
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
            # Profile area: 3.9440968091, perimeter: 7.6963993465
            with BuildLine():
                CenterArc((0, 0), 1.12492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0343966747, perimeter: 0.7250133221
            with BuildLine():
                _nurbs_edge([(1.1710685068, -0.0912182746), (1.1776180977, -0.091079682), (1.190829613, -0.0908001198), (1.2105812312, -0.0875967824), (1.230419514, -0.0833290831), (1.2503026498, -0.0778316977), (1.2702088508, -0.0713149333), (1.2901190049, -0.0638301939), (1.3100062973, -0.0554227243), (1.3298835868, -0.046188132), (1.3429428183, -0.0394037486), (1.3495202692, -0.0359867062)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0196305306, 0.0395977486, 0.0598901243, 0.0805065742, 0.1014467479, 0.1227104877, 0.1442977093, 0.166208362, 0.1884424131, 0.1884424131, 0.1884424131, 0.1884424131], 3)
                CenterArc((0, 0), 1.35, -1.5275041859, 3.0550083717)
                _nurbs_edge([(1.1710685068, 0.0912182746), (1.1776180977, 0.091079682), (1.190829613, 0.0908001198), (1.2105812312, 0.0875967824), (1.230419514, 0.0833290831), (1.2503026498, 0.0778316977), (1.2702088508, 0.0713149333), (1.2901190049, 0.0638301939), (1.3100062973, 0.0554227243), (1.3298835868, 0.046188132), (1.3429428183, 0.0394037486), (1.3495202692, 0.0359867062)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0196305306, 0.0395977486, 0.0598901243, 0.0805065742, 0.1014467479, 0.1227104877, 0.1442977093, 0.166208362, 0.1884424131, 0.1884424131, 0.1884424131, 0.1884424131], 3)
                Line((1.120525829, 0.0873590016), (1.1710685068, 0.0912182746))
                Line((1.120525829, -0.0873590016), (1.120525829, 0.0873590016))
                Line((1.120525829, -0.0873590016), (1.1710685068, -0.0912182746))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_78608_6fed6de8_0001():
    """Model: Spur Gear (10 teeth) (1)"""
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
            # Profile area: 0.4101820649, perimeter: 2.9840103661
            with BuildLine():
                CenterArc((0, 0), 0.37492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0309319357, perimeter: 0.6752194143
            with BuildLine():
                _nurbs_edge([(0.4629147461, -0.0804082907), (0.4678081612, -0.0805877505), (0.4777497371, -0.0809523453), (0.4927515832, -0.0786110327), (0.5079250033, -0.0751196517), (0.5232099047, -0.0702715862), (0.5385469226, -0.0642666627), (0.5538908837, -0.0571399814), (0.569183917, -0.0489254548), (0.5844269369, -0.0397144237), (0.5942887334, -0.0328490082), (0.5992805473, -0.0293738931)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0146586006, 0.0297807544, 0.0453505758, 0.0613665727, 0.0778282624, 0.0947354281, 0.1120879532, 0.1298857681, 0.1481288279, 0.1481288279, 0.1481288279, 0.1481288279], 3)
                CenterArc((0, 0), 0.6, -2.806121858, 5.6122437161)
                _nurbs_edge([(0.4629147461, 0.0804082907), (0.4678081612, 0.0805877505), (0.4777497371, 0.0809523453), (0.4927515832, 0.0786110327), (0.5079250033, 0.0751196517), (0.5232099047, 0.0702715862), (0.5385469226, 0.0642666627), (0.5538908837, 0.0571399814), (0.569183917, 0.0489254548), (0.5844269369, 0.0397144237), (0.5942887334, 0.0328490082), (0.5992805473, 0.0293738931)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0146586006, 0.0297807544, 0.0453505758, 0.0613665727, 0.0778282624, 0.0947354281, 0.1120879532, 0.1298857681, 0.1481288279, 0.1481288279, 0.1481288279, 0.1481288279], 3)
                Line((0.3684036206, 0.0641628457), (0.4629147461, 0.0804082907))
                Line((0.3684036206, -0.0641628457), (0.3684036206, 0.0641628457))
                Line((0.3684036206, -0.0641628457), (0.4629147461, -0.0804082907))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_78608_6fed6de8_0002():
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
            # Profile area: 0.036396879, perimeter: 1.551444116
            with BuildLine():
                CenterArc((0, 0), 0.14692, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.005135361, perimeter: 0.2763059248
            with BuildLine():
                _nurbs_edge([(0.1851658985, -0.0321633163), (0.1871232645, -0.0322351002), (0.1910998948, -0.0323809381), (0.1971006333, -0.0314444131), (0.2031700013, -0.0300478607), (0.2092839619, -0.0281086345), (0.215418769, -0.0257066651), (0.2215563535, -0.0228559925), (0.2276735668, -0.0195701819), (0.2337707748, -0.0158857695), (0.2377154933, -0.0131396033), (0.2397122189, -0.0117495572)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0058634403, 0.0119123018, 0.0181402303, 0.0245466291, 0.031131305, 0.0378941712, 0.0448351813, 0.0519543072, 0.0592515312, 0.0592515312, 0.0592515312, 0.0592515312], 3)
                CenterArc((0, 0), 0.24, -2.806121858, 5.6122437161)
                _nurbs_edge([(0.1851658985, 0.0321633163), (0.1871232645, 0.0322351002), (0.1910998948, 0.0323809381), (0.1971006333, 0.0314444131), (0.2031700013, 0.0300478607), (0.2092839619, 0.0281086345), (0.215418769, 0.0257066651), (0.2215563535, 0.0228559925), (0.2276735668, 0.0195701819), (0.2337707748, 0.0158857695), (0.2377154933, 0.0131396033), (0.2397122189, 0.0117495572)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0058634403, 0.0119123018, 0.0181402303, 0.0245466291, 0.031131305, 0.0378941712, 0.0448351813, 0.0519543072, 0.0592515312, 0.0592515312, 0.0592515312, 0.0592515312], 3)
                Line((0.1437672666, 0.0251435114), (0.1851658985, 0.0321633163))
                Line((0.1437672666, -0.0251435114), (0.1437672666, 0.0251435114))
                Line((0.1437672666, -0.0251435114), (0.1851658985, -0.0321633163))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_78608_6fed6de8_0003():
    """Model: Spur Gear (10 teeth) (2)"""
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
            # Profile area: 0.4101820649, perimeter: 2.9840103661
            with BuildLine():
                CenterArc((0, 0), 0.37492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0309319357, perimeter: 0.6752194143
            with BuildLine():
                _nurbs_edge([(0.4629147461, -0.0804082907), (0.4678081612, -0.0805877505), (0.4777497371, -0.0809523453), (0.4927515832, -0.0786110327), (0.5079250033, -0.0751196517), (0.5232099047, -0.0702715862), (0.5385469226, -0.0642666627), (0.5538908837, -0.0571399814), (0.569183917, -0.0489254548), (0.5844269369, -0.0397144237), (0.5942887334, -0.0328490082), (0.5992805473, -0.0293738931)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0146586006, 0.0297807544, 0.0453505758, 0.0613665727, 0.0778282624, 0.0947354281, 0.1120879532, 0.1298857681, 0.1481288279, 0.1481288279, 0.1481288279, 0.1481288279], 3)
                CenterArc((0, 0), 0.6, -2.806121858, 5.6122437161)
                _nurbs_edge([(0.4629147461, 0.0804082907), (0.4678081612, 0.0805877505), (0.4777497371, 0.0809523453), (0.4927515832, 0.0786110327), (0.5079250033, 0.0751196517), (0.5232099047, 0.0702715862), (0.5385469226, 0.0642666627), (0.5538908837, 0.0571399814), (0.569183917, 0.0489254548), (0.5844269369, 0.0397144237), (0.5942887334, 0.0328490082), (0.5992805473, 0.0293738931)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0146586006, 0.0297807544, 0.0453505758, 0.0613665727, 0.0778282624, 0.0947354281, 0.1120879532, 0.1298857681, 0.1481288279, 0.1481288279, 0.1481288279, 0.1481288279], 3)
                Line((0.3684036206, 0.0641628457), (0.4629147461, 0.0804082907))
                Line((0.3684036206, -0.0641628457), (0.3684036206, 0.0641628457))
                Line((0.3684036206, -0.0641628457), (0.4629147461, -0.0804082907))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_78608_6fed6de8_0004():
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
            # Profile area: 5.9074665539, perimeter: 9.2671956733
            with BuildLine():
                CenterArc((0, 0), 1.37492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0350267924, perimeter: 0.7364322098
            with BuildLine():
                _nurbs_edge([(1.4063514173, -0.0947401158), (1.4134573765, -0.094549883), (1.4277796653, -0.0941664629), (1.4491802742, -0.0907241057), (1.4706606483, -0.0861911154), (1.4921798275, -0.0804010599), (1.5137191007, -0.0735725741), (1.535261319, -0.0657606863), (1.5567818879, -0.0570135556), (1.5782949245, -0.0474306898), (1.592450146, -0.0404037568), (1.5995752073, -0.0368667349)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213032918, 0.042937468, 0.0648911988, 0.0871634192, 0.1097537849, 0.1326621411, 0.1558884047, 0.1794325261, 0.203294473, 0.203294473, 0.203294473, 0.203294473], 3)
                CenterArc((0, 0), 1.6, -1.320309544, 2.6406190879)
                _nurbs_edge([(1.4063514173, 0.0947401158), (1.4134573765, 0.094549883), (1.4277796653, 0.0941664629), (1.4491802742, 0.0907241057), (1.4706606483, 0.0861911154), (1.4921798275, 0.0804010599), (1.5137191007, 0.0735725741), (1.535261319, 0.0657606863), (1.5567818879, 0.0570135556), (1.5782949245, 0.0474306898), (1.592450146, 0.0404037568), (1.5995752073, 0.0368667349)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213032918, 0.042937468, 0.0648911988, 0.0871634192, 0.1097537849, 0.1326621411, 0.1558884047, 0.1794325261, 0.203294473, 0.203294473, 0.203294473, 0.203294473], 3)
                Line((1.3708130343, 0.0924132545), (1.4063514173, 0.0947401158))
                Line((1.3708130343, -0.0924132545), (1.3708130343, 0.0924132545))
                Line((1.3708130343, -0.0924132545), (1.4063514173, -0.0947401158))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_78687_f22479b6_0005():
    """Model: Houten kaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 585.9, perimeter: 97.8
            with BuildLine():
                Line((0, 13.95), (0, -13.95))
                Line((0, -13.95), (21, -13.95))
                Line((21, -13.95), (21, 13.95))
                Line((21, 13.95), (0, 13.95))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.32, perimeter: 24.1
            with BuildLine():
                Line((0, 3.1), (0, 11.95))
                Line((0, 11.95), (-3.2, 11.95))
                Line((-3.2, 11.95), (-3.2, 3.1))
                Line((-3.2, 3.1), (0, 3.1))
            make_face()
            # Profile area: 28.32, perimeter: 24.1
            with BuildLine():
                Line((0, -11.95), (-3.2, -11.95))
                Line((0, -3.1), (0, -11.95))
                Line((-3.2, -3.1), (0, -3.1))
                Line((-3.2, -11.95), (-3.2, -3.1))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


def model_78773_06275eba_0000():
    """Model: arrow_1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2578249999, perimeter: 3.8662047908
            with BuildLine():
                Line((0.055, -0.243874968), (0.0994886434, -1.7))
                CenterArc((0, 0), 0.25, -102.7090329944, 25.4180659888)
                Line((-0.055, -0.243874968), (-0.0994886434, -1.7))
                CenterArc((-0.2913147817, -1.87), 0.2563147817, 0, 41.5479771522)
                Line((-0.035, -1.87), (-0.035, -2.05))
                CenterArc((0, -2.05), 0.035, 180, 180)
                Line((0.035, -2.05), (0.035, -1.87))
                CenterArc((0.2913147817, -1.87), 0.2563147817, 138.4520228478, 41.5479771522)
            make_face()
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.25, -77.2909670056, 334.5819340112)
                CenterArc((0, 0), 0.25, -102.7090329944, 25.4180659888)
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.02), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0291237332, perimeter: 0.9248292827
            with BuildLine():
                CenterArc((0, -0.3222543435), 0.030386498, 1.75, 176.5)
                Line((-0.0303723255, -0.321326385), (-0.0410558199, -0.6709999747))
                CenterArc((0, -0.6722543435), 0.0410749777, 178.25, 183.5)
                Line((0.0303723255, -0.321326385), (0.0410558199, -0.6709999747))
            make_face()
            # Profile area: 0.0433553684, perimeter: 1.0169312687
            with BuildLine():
                CenterArc((0, -0.8022543435), 0.0450449844, 1.75, 176.5)
                Line((-0.045023975, -0.8008787366), (-0.0557075064, -1.1505535362))
                CenterArc((0, -1.1522543435), 0.055733464, 178.2512443351, 183.4987556649)
                Line((0.045023975, -0.8008787366), (0.0557074694, -1.1505523263))
            make_face()
            # Profile area: 0.058238486, perimeter: 1.1145875255
            with BuildLine():
                CenterArc((0, -1.3122543435), 0.0606196261, 1.7499999998, 176.5011456498)
                Line((-0.0605913896, -1.3104043217), (-0.0707898211, -1.6442016756))
                Line((-0.0707898211, -1.6442016756), (-0.0216217615, -1.7345910119))
                CenterArc((0.0010576625, -1.7222543435), 0.0258176231, -151.4556383439, 124.4879690963)
                Line((0.0240679433, -1.7339623167), (0.0707303247, -1.6422543435))
                Line((0.0605913526, -1.3104031102), (0.0707303247, -1.6422543435))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


def model_78773_06275eba_0001():
    """Model: Spur Gear (70 teeth)"""
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
            # Profile area: 6.7754090841, perimeter: 10.5690716689
            with BuildLine():
                CenterArc((0, 0), 1.48212, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.011059665, perimeter: 0.4296410182
            with BuildLine():
                Line((1.4461176725, 0.0540294164), (1.4461176725, -0.0540294164))
                _nurbs_edge([(1.4461176725, -0.0540294164), (1.4512100905, -0.0538194491), (1.4614504012, -0.0533972273), (1.4767381743, -0.0510553165), (1.4920567469, -0.0480733976), (1.5073855694, -0.0443588053), (1.5227195358, -0.040045326), (1.5380525223, -0.0351693704), (1.5533748032, -0.0297623874), (1.5686957929, -0.0238855805), (1.5788181592, -0.0196018611), (1.5839038831, -0.017449616)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0152790937, 0.0307246323, 0.0463309178, 0.0620974145, 0.0780239494, 0.0941104444, 0.1103568579, 0.1267631647, 0.1433293489, 0.1433293489, 0.1433293489, 0.1433293489], 3)
                CenterArc((0, 0), 1.584, -0.6311929121, 1.2623858242)
                _nurbs_edge([(1.4461176725, 0.0540294164), (1.4512100905, 0.0538194491), (1.4614504012, 0.0533972273), (1.4767381743, 0.0510553165), (1.4920567469, 0.0480733976), (1.5073855694, 0.0443588053), (1.5227195358, 0.040045326), (1.5380525223, 0.0351693704), (1.5533748032, 0.0297623874), (1.5686957929, 0.0238855805), (1.5788181592, 0.0196018611), (1.5839038831, 0.017449616)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0152790937, 0.0307246323, 0.0463309178, 0.0620974145, 0.0780239494, 0.0941104444, 0.1103568579, 0.1267631647, 0.1433293489, 0.1433293489, 0.1433293489, 0.1433293489], 3)
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


def model_78773_06275eba_0003():
    """Model: Spur Gear (120 teeth)"""
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
            # Profile area: 2.6250266004, perimeter: 7.1359392171
            with BuildLine():
                CenterArc((0, 0), 0.93572, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0026803371, perimeter: 0.217344902
            with BuildLine():
                Line((0.9017514565, 0.0252505453), (0.9017514565, -0.0252505453))
                _nurbs_edge([(0.9017514565, -0.0252505453), (0.9044983118, -0.0251266489), (0.9100179535, -0.0248776866), (0.9182578729, -0.023648226), (0.9265104879, -0.0220997437), (0.9347661652, -0.0201868305), (0.9430232369, -0.017977068), (0.9512792376, -0.0154892764), (0.9595300323, -0.012739657), (0.9677804014, -0.009759194), (0.9732379726, -0.0075912372), (0.9759783376, -0.006502659)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0082437408, 0.0165653053, 0.0249620296, 0.0334336634, 0.0419801255, 0.0506013797, 0.0592974062, 0.0680681936, 0.0769137341, 0.0769137341, 0.0769137341, 0.0769137341], 3)
                CenterArc((0, 0), 0.976, -0.3817394208, 0.7634788416)
                _nurbs_edge([(0.9017514565, 0.0252505453), (0.9044983118, 0.0251266489), (0.9100179535, 0.0248776866), (0.9182578729, 0.023648226), (0.9265104879, 0.0220997437), (0.9347661652, 0.0201868305), (0.9430232369, 0.017977068), (0.9512792376, 0.0154892764), (0.9595300323, 0.012739657), (0.9677804014, 0.009759194), (0.9732379726, 0.0075912372), (0.9759783376, 0.006502659)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0082437408, 0.0165653053, 0.0249620296, 0.0334336634, 0.0419801255, 0.0506013797, 0.0592974062, 0.0680681936, 0.0769137341, 0.0769137341, 0.0769137341, 0.0769137341], 3)
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)
    return part.part


def model_78773_06275eba_0010():
    """Model: arrow_2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with BuildLine():
                CenterArc((0, 0), 0.175, -71.6823015888, 323.3646031776)
                CenterArc((0, 0), 0.175, -108.3176984112, 36.6353968224)
            make_face()
            # Profile area: 0.3270321401, perimeter: 4.5332381617
            with BuildLine():
                Line((0.055, -0.1661324773), (0.1095020822, -1.95))
                CenterArc((0, 0), 0.175, -108.3176984112, 36.6353968224)
                Line((-0.055, -0.1661324773), (-0.1095020822, -1.95))
                CenterArc((-0.2662053519, -2.12), 0.2312053519, 0, 47.3306356529)
                Line((-0.035, -2.12), (-0.035, -2.3))
                CenterArc((0, -2.3), 0.035, 180, 180)
                Line((0.035, -2.3), (0.035, -2.12))
                CenterArc((0.2662053519, -2.12), 0.2312053519, 132.6693643471, 47.3306356529)
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.02), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0258715893, perimeter: 1.0648961122
            with BuildLine():
                CenterArc((0, -0.22), 0.0193060681, 1.75, 176.5)
                Line((-0.0192970635, -0.2194104214), (-0.0330329849, -0.668990751))
                CenterArc((0, -0.67), 0.033048399, 178.25, 183.5)
                Line((0.0192970635, -0.2194104214), (0.0330329849, -0.668990751))
            make_face()
            # Profile area: 0.0457189909, perimeter: 1.1761860119
            with BuildLine():
                CenterArc((0, -0.8), 0.0370184057, 1.75, 176.5)
                Line((-0.03700114, -0.7988695129), (-0.0507370679, -1.2484500558))
                CenterArc((0, -1.25), 0.0507607367, 178.2502408153, 183.4997591847)
                Line((0.03700114, -0.7988695129), (0.0507370614, -1.2484498426))
            make_face()
            # Profile area: 0.0695108015, perimeter: 1.2970698685
            with BuildLine():
                CenterArc((0, -1.43), 0.0562576691, 1.75, 176.5002242495)
                Line((-0.0562314367, -1.4282821945), (-0.0699673514, -1.8778623041))
                CenterArc((0, -1.88), 0.07, 178.25, 183.5)
                Line((0.05623143, -1.4282819744), (0.0699673514, -1.8778623041))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


def model_78972_71d3bfef_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7563245274, perimeter: 12.25203732
            with BuildLine():
                CenterArc((-10, 0), 1.2, 52.7265610299, 216.8260340898)
                CenterArc((-3.8969175373, -89.642929871), 88.6539361491, 93.8360899605, 0.117438013)
                CenterArc((-10, 0), 1.2, -81.7629771857, 29.0364161558)
                CenterArc((-10, 0), 1.2, -52.7265610299, 105.4531220598)
            make_face()
            with BuildLine():
                CenterArc((-10, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0972340804, perimeter: 18.5353966562
            with BuildLine():
                CenterArc((7.8, 0), 1.75, 146.930215642, 66.1395687159)
                CenterArc((7.8, 0), 1.75, -146.930215642, 293.8604312841)
            make_face()
            with BuildLine():
                CenterArc((7.8, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.0221092971, perimeter: 64.5838057971
            with BuildLine():
                CenterArc((-10, 0), 1.2, -52.7265610299, 105.4531220598)
                Line((-9.2732565141, -0.9549051815), (6.3334884609, -0.9549051815))
                CenterArc((7.8, 0), 1.75, 146.930215642, 66.1395687159)
                Line((-9.2732565141, 0.9549051815), (6.3334884609, 0.9549051815))
            make_face()
            with BuildLine():
                Line((-8, 0.5), (5, 0.5))
                CenterArc((5, 0), 0.5, -90, 180)
                Line((-8, -0.5), (5, -0.5))
                CenterArc((-8, 0), 0.5, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_78973_5f3ba6bc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 374.6772306933, perimeter: 72.0533135949
            with BuildLine():
                Line((6.0042425962, -10.4001155849), (12.0088855969, -0.0002311737))
                Line((12.0088855969, -0.0002311737), (6.0046430008, 10.3998844112))
                Line((6.0046430008, 10.3998844112), (-6.0042425962, 10.4001155849))
                Line((-6.0042425962, 10.4001155849), (-12.0088855969, 0.0002311737))
                Line((-12.0088855969, 0.0002311737), (-6.0046430008, -10.3998844112))
                Line((-6.0046430008, -10.3998844112), (6.0042425962, -10.4001155849))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_78979_6c732414_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 374.6772306933, perimeter: 72.0533135949
            with BuildLine():
                Line((6.0044427996, 10.4), (-6.0044427996, 10.4))
                Line((-6.0044427996, 10.4), (-12.0088855991, 0))
                Line((-12.0088855991, 0), (-6.0044427996, -10.4))
                Line((-6.0044427996, -10.4), (6.0044427996, -10.4))
                Line((6.0044427996, -10.4), (12.0088855991, 0))
                Line((12.0088855991, 0), (6.0044427996, 10.4))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=44.5
        extrude(amount=44.5, mode=Mode.ADD)
    return part.part


def model_78981_9684a26f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 86.6025403784, perimeter: 34.6410161514
            with BuildLine():
                Line((2.2679491924, -5.3094010768), (5.7320508076, -0.6905989232))
                Line((5.7320508076, -0.6905989232), (3.4641016151, 4.6188021535))
                Line((3.4641016151, 4.6188021535), (-2.2679491924, 5.3094010768))
                Line((-2.2679491924, 5.3094010768), (-5.7320508076, 0.6905989232))
                Line((-5.7320508076, 0.6905989232), (-3.4641016151, -4.6188021535))
                Line((-3.4641016151, -4.6188021535), (2.2679491924, -5.3094010768))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 25.1327412287, perimeter: 17.7715317526
            Circle(2.8284271247)
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)
    return part.part


def model_78988_182be740_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.5070415552, perimeter: 22.1810730128
            with BuildLine():
                Line((0.556624327, -3.6547005384), (3.443375673, -1.3452994616))
                Line((3.443375673, -1.3452994616), (2.8867513459, 2.3094010768))
                Line((2.8867513459, 2.3094010768), (-0.556624327, 3.6547005384))
                Line((-0.556624327, 3.6547005384), (-3.443375673, 1.3452994616))
                Line((-3.443375673, 1.3452994616), (-2.8867513459, -2.3094010768))
                Line((-2.8867513459, -2.3094010768), (0.556624327, -3.6547005384))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.2101764285, perimeter: 11.3271735679
            Circle(1.8027756646)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_78991_64d81333_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 445.7063637762, perimeter: 212.6124454699
            with BuildLine():
                Line((-12.4834958613, 30.6504693151), (-4.983504909, 30.6388195991))
                Line((-4.983504909, 30.6388195991), (4.4124910397, 30.6242167092))
                CenterArc((4.4047202444, 25.6242227477), 5, 0, 89.910953209)
                Line((9.4047202444, 20.3163019126), (9.4047202444, 25.6242227477))
                CenterArc((20, 20), 10.6, 178.2900513979, 181.2894167478)
                Line((30.5997144866, 19.9222002446), (30.5997144866, 20.0777997554))
                Line((30.5997144866, 20.0777997554), (30.5997144866, 25.6000010268))
                CenterArc((35.5997144866, 25.6000010268), 5, 90.0000507916, 89.9999492084)
                Line((52.5164649319, 30.6000160231), (35.5997100542, 30.6000010268))
                Line((52.5214746842, 33.8504654547), (52.5164649319, 30.6000160231))
                Line((-12.4785253158, 33.8504654547), (52.5214746842, 33.8504654547))
                Line((-12.4834958613, 30.6504693151), (-12.4785253158, 33.8504654547))
            make_face()
            with BuildLine():
                CenterArc((20, 20), 7.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-25
        extrude(amount=-25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000271263, 30.5999694683, 0), x_dir=(0, 0, -1), z_dir=(0.0000008865, -1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((5, 45)):
                Circle(2.5)
        # OneSide extrude, distance=-25
        extrude(amount=-25, mode=Mode.SUBTRACT)
    return part.part


def model_79094_4872079c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64.9519052838, perimeter: 30
            with BuildLine():
                Line((9.4540131971, -0.9659194317), (4.4833903455, -0.424709244))
                Line((4.4833903455, -0.424709244), (1.5293771484, -4.4587898123))
                Line((1.5293771484, -4.4587898123), (3.5459868029, -9.0340805683))
                Line((3.5459868029, -9.0340805683), (8.5166096545, -9.575290756))
                Line((8.5166096545, -9.575290756), (11.4706228516, -5.5412101877))
                Line((11.4706228516, -5.5412101877), (9.4540131971, -0.9659194317))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.853981634, perimeter: 9.9345882658
            with Locations((-6.5, 5)):
                Circle(1.5811388301)
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)
    return part.part


def model_79097_9e06d5f8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.9711431703, perimeter: 23.2379000772
            with BuildLine():
                Line((2.1339745962, -3.2320508076), (3.8660254038, 0.2320508076))
                Line((3.8660254038, 0.2320508076), (1.7320508076, 3.4641016151))
                Line((1.7320508076, 3.4641016151), (-2.1339745962, 3.2320508076))
                Line((-2.1339745962, 3.2320508076), (-3.8660254038, -0.2320508076))
                Line((-3.8660254038, -0.2320508076), (-1.7320508076, -3.4641016151))
                Line((-1.7320508076, -3.4641016151), (2.1339745962, -3.2320508076))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2831853072, perimeter: 8.8857658763
            Circle(1.4142135624)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_79098_6d4d6157_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.2831853072, perimeter: 18.3519881302
            with BuildLine():
                CenterArc((0, 0), 1.8027756377, 47.3947763964, 265.2104472073)
                CenterArc((0, 0), 1.8027756377, -47.3947763964, 94.7895527927)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1180339887, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 28.9721605878
            with BuildLine():
                CenterArc((23.5, 0), 2.5495097568, 148.6371825191, 62.7256349618)
                CenterArc((23.5, 0), 2.5495097568, -148.6371825191, 297.2743650382)
            make_face()
            with BuildLine():
                CenterArc((23.5, 0), 2.0615528128, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 35.1102316124, perimeter: 80.9788692209
            with BuildLine():
                CenterArc((0, 0), 1.8027756377, -47.3947763964, 94.7895527927)
                Line((1.2203764858, -1.3269066406), (21.3230023502, -1.3269066406))
                CenterArc((23.5, 0), 2.5495097568, 148.6371825191, 62.7256349618)
                Line((1.2203764858, 1.3269066406), (21.3230023502, 1.3269066406))
            make_face()
            with BuildLine():
                Line((3, -0.5), (3, 0.5))
                Line((3, 0.5), (19.5, 0.5))
                Line((19.5, 0.5), (19.5, -0.5))
                Line((19.5, -0.5), (3, -0.5))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True, mode=Mode.ADD)
    return part.part


def model_79207_77757b86_0001():
    """Model: Spur Gear (40 teeth)"""
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
            # Profile area: 694.248997591, perimeter: 108.6043553798
            with BuildLine():
                CenterArc((0, 0), 15.03492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.2280266526, perimeter: 5.9759141111
            with BuildLine():
                _nurbs_edge([(15.0130244434, -0.8141165642), (15.0787929213, -0.8119184471), (15.2112180817, -0.8074925273), (15.4089881758, -0.7761855759), (15.6073405392, -0.7355566678), (15.8059463097, -0.684215084), (16.0046835489, -0.6240638822), (16.2034311988, -0.5555991761), (16.4020093818, -0.4792524303), (16.6005472899, -0.3958914401), (16.7314212453, -0.3349166542), (16.7972447874, -0.3042491592)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1972369683, 0.3971376259, 0.5996107737, 0.8046478394, 1.0122460514, 1.2224041628, 1.4351215051, 1.6503976783, 1.8682324241, 1.8682324241, 1.8682324241, 1.8682324241], 3)
                CenterArc((0, 0), 16.8, -1.037687248, 2.075374496)
                _nurbs_edge([(15.0130244434, 0.8141165642), (15.0787929213, 0.8119184471), (15.2112180817, 0.8074925273), (15.4089881758, 0.7761855759), (15.6073405392, 0.7355566678), (15.8059463097, 0.684215084), (16.0046835489, 0.6240638822), (16.2034311988, 0.5555991761), (16.4020093818, 0.4792524303), (16.6005472899, 0.3958914401), (16.7314212453, 0.3349166542), (16.7972447874, 0.3042491592)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1972369683, 0.3971376259, 0.5996107737, 0.8046478394, 1.0122460514, 1.2224041628, 1.4351215051, 1.6503976783, 1.8682324241, 1.8682324241, 1.8682324241, 1.8682324241], 3)
                Line((15.0118642155, 0.8141077959), (15.0130244434, 0.8141165642))
                Line((15.0118642155, -0.8141077959), (15.0118642155, 0.8141077959))
                Line((15.0118642155, -0.8141077959), (15.0130244434, -0.8141165642))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_79423_62db5fc6_0007():
    """Model: 2-32-TRACK ROD"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=5.8
        extrude(amount=5.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_79693_9396219b_0001():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((1.5, 1)):
                Circle(0.35)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.326721207, perimeter: 4.0831446692
            with Locations((1.5, 1)):
                Circle(0.6498526575)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_79998_13b5563b_0000():
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
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.8564598431, perimeter: 28.7009385813
            with BuildLine():
                CenterArc((0, 3.85), 3.85, 90.0317779082, 179.9682220918)
                _nurbs_edge([(-0.002135322, 7.6999994078), (-0.1472985471, 7.6218468892), (-0.4216108071, 7.465802137), (-0.7850367999, 7.2325158577), (-1.1731264088, 6.9230356123), (-1.4963952901, 6.5387736389), (-1.6587217226, 6.1569587837), (-1.665150066, 5.7772534118), (-1.527157169, 5.3990438035), (-1.2653615466, 5.0213423115), (-0.9072597466, 4.6429878946), (-0.4849020741, 4.2628565093), (-0.0327771137, 3.8800718209), (0.4142358329, 3.4942117158), (0.8229389723, 3.1055498829), (1.1627978752, 2.7148583684), (1.4068873091, 2.3231850715), (1.5329903233, 1.9316465652), (1.5247595409, 1.541221846), (1.3731966641, 1.1525344811), (1.074619842, 0.7659283964), (0.7178378477, 0.4584279204), (0.3844170425, 0.2288199209), (0.1329958012, 0.0761982522), (0, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((-0.8067555309, 1.5534868383), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.4266119576, perimeter: 28.7052092256
            with BuildLine():
                _nurbs_edge([(-0.002135322, 7.6999994078), (-0.1472985471, 7.6218468892), (-0.4216108071, 7.465802137), (-0.7850367999, 7.2325158577), (-1.1731264088, 6.9230356123), (-1.4963952901, 6.5387736389), (-1.6587217226, 6.1569587837), (-1.665150066, 5.7772534118), (-1.527157169, 5.3990438035), (-1.2653615466, 5.0213423115), (-0.9072597466, 4.6429878946), (-0.4849020741, 4.2628565093), (-0.0327771137, 3.8800718209), (0.4142358329, 3.4942117158), (0.8229389723, 3.1055498829), (1.1627978752, 2.7148583684), (1.4068873091, 2.3231850715), (1.5329903233, 1.9316465652), (1.5247595409, 1.541221846), (1.3731966641, 1.1525344811), (1.074619842, 0.7659283964), (0.7178378477, 0.4584279204), (0.3844170425, 0.2288199209), (0.1329958012, 0.0761982522), (0, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 3.85), 3.85, -90, 180.0317779082)
            make_face()
            with BuildLine():
                CenterArc((0.8651794111, 5.9627923284), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-0.8067555309, 1.5534868383)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0.8651794111, 5.9627923284)):
                Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_80189_5bbbf853_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.1769145362, perimeter: 20.7846096908
            with BuildLine():
                Line((3, -1.7320508076), (3, 1.7320508076))
                Line((3, 1.7320508076), (0, 3.4641016151))
                Line((0, 3.4641016151), (-3, 1.7320508076))
                Line((-3, 1.7320508076), (-3, -1.7320508076))
                Line((-3, -1.7320508076), (0, -3.4641016151))
                Line((0, -3.4641016151), (3, -1.7320508076))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.853981634, perimeter: 9.9345882658
            Circle(1.5811388301)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)
    return part.part


def model_80191_ac61cdc4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.8275496309, perimeter: 27.0554985169
            with BuildLine():
                Line((1.556624327, -4.2320508076), (4.443375673, -0.7679491924))
                Line((4.443375673, -0.7679491924), (2.8867513459, 3.4641016151))
                Line((2.8867513459, 3.4641016151), (-1.556624327, 4.2320508076))
                Line((-1.556624327, 4.2320508076), (-4.443375673, 0.7679491924))
                Line((-4.443375673, 0.7679491924), (-2.8867513459, -3.4641016151))
                Line((-2.8867513459, -3.4641016151), (1.556624327, -4.2320508076))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1371669412, perimeter: 13.3286488145
            Circle(2.1213203436)
        # OneSide extrude, distance=-8.5
        extrude(amount=-8.5, mode=Mode.SUBTRACT)
    return part.part


def model_80192_c2f08a97_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.6460227907, perimeter: 32.595316179
            with BuildLine():
                CenterArc((0, 0), 2.8284271247, 27.1115522864, 305.7768954272)
                CenterArc((0, 0), 2.8284271247, -27.1115522864, 54.2231045728)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.3592785668, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.1711218651, perimeter: 63.0993697331
            with BuildLine():
                CenterArc((33.4857364091, 0), 5.4202007129, 144.4496486614, 71.1007026773)
                CenterArc((33.4857364091, 0), 5.4202007129, -144.4496486614, 288.8992973227)
            make_face()
            with BuildLine():
                CenterArc((33.4857364091, 0), 4.6223758861, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 73.9155896446, perimeter: 104.9329087333
            with BuildLine():
                CenterArc((33.4857364091, 0), 5.4202007129, 144.4496486614, 71.1007026773)
                Line((2.5176422027, 1.2889832191), (29.0758346354, 3.1514031978))
                CenterArc((0, 0), 2.8284271247, -27.1115522864, 54.2231045728)
                Line((2.5176422027, -1.2889832191), (29.0758346354, -3.1514031978))
            make_face()
            with BuildLine():
                Line((7, 1), (25, 1))
                CenterArc((25, 0), 1, -90, 180)
                Line((7, -1), (25, -1))
                CenterArc((7, 0), 1, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True, mode=Mode.ADD)
    return part.part


def model_80760_3ac12cd8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 150, perimeter: 50
            with BuildLine():
                Line((5, -7.5), (5, 7.5))
                Line((5, 7.5), (-5, 7.5))
                Line((-5, 7.5), (-5, -7.5))
                Line((-5, -7.5), (5, -7.5))
            make_face()
        # TwoSides extrude (symmetric), distance=5
        extrude(amount=5, both=True)

        # Sketch2 -> 拉伸3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.3856949295, perimeter: 12.9686412661
            with BuildLine():
                Line((-5, 3.5016168363), (-1.5, 3.5016161148))
                Line((-0.5005387046, 3.5005392853), (-1.5, 3.5016161148))
                CenterArc((-0.5, 4.0005389951), 0.5, -90.0617310135, 90.0617310135)
                Line((0, 4.7000000906), (0, 4.0005389951))
                CenterArc((-0.5, 4.7000000906), 0.5, 0, 90.000000754)
                Line((-1.5000000224, 5.2000000775), (-0.5000000066, 5.2000000906))
                Line((-1.5000000224, 5.2000000775), (-5.0000000224, 5.2000000775))
                Line((-5.0000000224, 5.2000000775), (-5, 3.5016168363))
            make_face()
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)
    return part.part


def model_81029_104dff26_0000():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 27.7936657623, perimeter: 33.7059090786
            with BuildLine():
                Line((1.9, -6.195), (0, -6.195))
                Line((0, -6.195), (0, -7.4517096231))
                Line((0, -7.4517096231), (1.4, -8.26))
                Line((1.4, -8.26), (3.35, -8.26))
                Line((4.75, -6.86), (3.35, -8.26))
                Line((4.75, 0.5), (4.75, -6.86))
                Line((3.35, 1.9), (4.75, 0.5))
                Line((0, 1.9), (3.35, 1.9))
                Line((0, 0), (0, 1.9))
                Line((0, 0), (2.215, 0))
                CenterArc((2.215, -0.635), 0.635, 0, 90)
                Line((2.85, -0.635), (2.85, -6.0456998816))
                CenterArc((2.2199117886, -6.0456998816), 0.6300882114, -87.1340344673, 87.1340344673)
                CenterArc((2.2199117886, -6.0456998816), 0.6300882114, -92.8659655327, 5.7319310655)
                Line((1.9, -6.675), (2.1884075806, -6.675))
                Line((1.9, -6.195), (1.9, -6.675))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-0.95, -0.95)):
                Circle(0.5)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)
    return part.part


def model_81029_5cd05f84_0001():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 32.4150934568, perimeter: 37.4786321571
            with BuildLine():
                Line((3.0492777369, -6.195), (0.1142457938, -6.195))
                Line((0.1142457938, -6.195), (0.1142457938, -6.86))
                Line((0.1142457938, -6.86), (1.5142457938, -8.26))
                Line((1.5142457938, -8.26), (4.6, -8.26))
                Line((6, -6.86), (4.6, -8.26))
                Line((6, 0.5), (6, -6.86))
                Line((4.6, 1.9), (6, 0.5))
                Line((0, 1.9), (4.6, 1.9))
                Line((0, 0), (0, 1.9))
                Line((0, 0), (3.465, 0))
                CenterArc((3.465, -0.635), 0.635, 0, 90)
                Line((4.1, -0.635), (4.1, -5.715))
                CenterArc((3.465, -5.715), 0.635, -130.8954455861, 130.8954455861)
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-0.95, -0.95)):
                Circle(0.5)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)
    return part.part


def model_81975_26c061f9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16267.3634013826, perimeter: 541.4969644752
            with BuildLine():
                Line((-75, 43.2205377215), (-75, -46.7794622785))
                Line((-75, -46.7794622785), (105.7484822376, -46.7794622785))
                Line((105.7484822376, -46.7794622785), (105.7484822376, 43.2205377215))
                Line((105.7484822376, 43.2205377215), (-75, 43.2205377215))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 106.6913059301, perimeter: 47.7164855849
            with BuildLine():
                Line((-20, 34.038510576), (-20, 40))
                Line((-20, 40), (-37.8967533685, 40))
                Line((-37.8967533685, 40), (-37.8967533685, 34.038510576))
                Line((-37.8967533685, 34.038510576), (-20, 34.038510576))
            make_face()
            # Profile area: 136.033518152, perimeter: 59.0462020307
            with BuildLine():
                Line((13.8097467499, 44.2866457346), (-10, 44.2866457346))
                Line((13.8097467499, 50), (13.8097467499, 44.2866457346))
                Line((-10, 50), (13.8097467499, 50))
                Line((-10, 44.2866457346), (-10, 50))
            make_face()
            # Profile area: 107.5012237593, perimeter: 47.9882021885
            with BuildLine():
                Line((38.0326116702, 34.038510576), (20, 34.038510576))
                Line((38.0326116702, 40), (38.0326116702, 34.038510576))
                Line((20, 40), (38.0326116702, 40))
                Line((20, 34.038510576), (20, 40))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


def model_81996_b3752ed2_0000():
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
        # Sketch9 -> Extrude9 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1000, perimeter: 130
            with BuildLine():
                Line((20, -12.5), (-20, -12.5))
                Line((20, 12.5), (20, -12.5))
                Line((-20, 12.5), (20, 12.5))
                Line((-20, -12.5), (-20, 12.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_82012_c533307b_0002():
    """Model: rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=9.6
        extrude(amount=9.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=12.6
        extrude(amount=12.6, mode=Mode.SUBTRACT)
    return part.part


def model_82012_c533307b_0003():
    """Model: connecting rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.3929199862, perimeter: 12.5097332872
            with BuildLine():
                CenterArc((0.0000000664, 3.5), 2.1, -148.9972829641, 58.9972811517)
                Line((0, 2), (0, 1.4))
                CenterArc((0.0000000664, 3.5), 1.5, 90.0000025374, 179.9999949253)
                Line((0, 5.6), (0, 5))
                CenterArc((0.0000000664, 3.5), 2.1, 90.0000018124, 121.0027152235)
            make_face()
            # Profile area: 3.3929201456, perimeter: 12.5097338186
            with BuildLine():
                Line((0, 5.6), (0, 5))
                CenterArc((0.0000000664, 3.5), 1.5, -90.0000025374, 180.0000050747)
                Line((0, 2), (0, 1.4))
                CenterArc((0.0000000664, 3.5), 2.1, -90.0000018124, 58.9972805806)
                CenterArc((0.0000000664, 3.5), 2.1, -31.0027212318, 121.0027230442)
            make_face()
            # Profile area: 4.8765208062, perimeter: 12.6387215968
            with BuildLine():
                CenterArc((0.0000000664, -13.3), 3.0002, 90.0000012686, 0.9357155455)
                Line((0, -9.4), (0, -10.2998))
                CenterArc((0.0000000664, -13.3), 3.9, 90.0000009759, 90.0024098462)
                Line((-3.8999999301, -13.3001640995), (-3.0001999299, -13.3001488156))
                CenterArc((0.0000000664, -13.3), 3.0002, 90.9357168141, 89.067125166)
            make_face()
            # Profile area: 4.8763448261, perimeter: 12.6383304428
            with BuildLine():
                CenterArc((0.0000000664, -13.3), 3.9, -90.0000009759, 89.9995365809)
                Line((3.0002000661, -13.3000468942), (3.9000000663, -13.3000316104))
                CenterArc((0.0000000664, -13.3), 3.0002, -89.3384237023, 89.3375281494)
                CenterArc((0.0000000664, -13.3), 3.0002, -90.0000012686, 0.6615775663)
                Line((0, -16.3002), (0, -17.2))
            make_face()
            # Profile area: 4.8764154644, perimeter: 12.6384874519
            with BuildLine():
                CenterArc((0.0000000664, -13.3), 3.0002, 89.0642831859, 0.9357180827)
                CenterArc((0.0000000664, -13.3), 3.0002, -0.0008955529, 89.0651787389)
                Line((3.0002000661, -13.3000468942), (3.9000000663, -13.3000316104))
                CenterArc((0.0000000664, -13.3), 3.9, -0.000464395, 90.0004653709)
                Line((0, -9.4), (0, -10.2998))
            make_face()
            # Profile area: 4.8762392452, perimeter: 12.6380957666
            with BuildLine():
                Line((-3.8999999301, -13.3001640995), (-3.0001999299, -13.3001488156))
                CenterArc((0.0000000664, -13.3), 3.9, -179.9975891779, 89.997588202)
                Line((0, -16.3002), (0, -17.2))
                CenterArc((0.0000000664, -13.3), 3.0002, -90.6615762977, 0.6615750291)
                CenterArc((0.0000000664, -13.3), 3.0002, -179.99715802, 89.3355817223)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.9850462258, perimeter: 17.0656535408
            with BuildLine():
                Line((-1.2, -0.1), (-1.2, -4.9))
                CenterArc((0, -0.1), 1.2, 90, 90)
                Line((0, 1.4), (0, 1.1))
                CenterArc((0.0000000664, 3.5), 2.1, -148.9972829641, 58.9972811517)
                Line((-1.7999999732, 2.4183346833), (-1.7999999732, -4.9))
                Line((-1.7999999732, -4.9), (-1.2, -4.9))
            make_face()
            # Profile area: 2.0736930247, perimeter: 8.2024891286
            with BuildLine():
                CenterArc((0.0000000664, -13.3), 4.2, -45.5846914028, 45.5843296942)
                Line((4.4999921543, -16.3), (2.9393877578, -16.3))
                Line((4.5, -16.3002000867), (4.4999921543, -16.3))
                Line((4.5, -13.3000214189), (4.5, -16.3002000867))
                Line((4.2000000663, -13.3000265146), (4.5, -13.3000214189))
            make_face()
            # Profile area: 8.8492533164, perimeter: 22.5945943425
            with BuildLine():
                CenterArc((0.0000000664, -13.3), 3.9, -0.000464395, 90.0004653709)
                Line((3.9000000663, -13.3000316104), (4.2000000663, -13.3000265146))
                Line((4.2000000663, -13.3000265146), (4.5, -13.3000214189))
                Line((4.5, -10.3002000867), (4.5, -13.3000214189))
                Line((3.1099507467, -10.3002000867), (4.5, -10.3002000867))
                CenterArc((7.9982661098, -6.4893109501), 6.1982661366, 180, 37.9396762812)
                Line((1.7999999827, -4.9), (1.7999999732, -6.4893109501))
                Line((1.2, -4.9), (1.7999999827, -4.9))
                Line((1.2, -7.3), (1.2, -4.9))
                CenterArc((0, -7.3), 1.2, -90, 90)
                Line((0, -8.5), (0, -9.4))
            make_face()
            # Profile area: 8.849339236, perimeter: 22.5948795645
            with BuildLine():
                Line((0, -8.5), (0, -9.4))
                CenterArc((0, -7.3), 1.2, 180, 90)
                Line((-1.2, -4.9), (-1.2, -7.3))
                Line((-1.7999999732, -4.9), (-1.2, -4.9))
                Line((-1.7999999732, -4.9), (-1.7999999732, -6.4893109501))
                CenterArc((-7.9982661098, -6.4893109501), 6.1982661366, -37.9396762812, 37.9396762812)
                Line((-4.4999999336, -10.3002000867), (-3.1099507467, -10.3002000867))
                Line((-4.4999999336, -13.3001742909), (-4.4999999336, -10.3002000867))
                Line((-4.4999999336, -13.3001742909), (-4.1999999302, -13.3001691952))
                Line((-4.1999999302, -13.3001691952), (-3.8999999301, -13.3001640995))
                CenterArc((0.0000000664, -13.3), 3.9, 90.0000009759, 90.0024098462)
            make_face()
            # Profile area: 2.0736488903, perimeter: 8.2018012306
            with BuildLine():
                Line((-4.4999999336, -16.3), (-4.4999999336, -13.3001742909))
                Line((-2.9393876249, -16.3), (-4.4999999336, -16.3))
                CenterArc((0.0000000664, -13.3), 4.2, -179.9976918642, 45.5823832671)
                Line((-4.4999999336, -13.3001742909), (-4.1999999302, -13.3001691952))
            make_face()
            # Profile area: 4.9850463219, perimeter: 17.0656533976
            with BuildLine():
                Line((1.8000000268, 2.4183345515), (1.7999999827, -4.9))
                CenterArc((0.0000000664, 3.5), 2.1, -90.0000018124, 58.9972805806)
                Line((0, 1.4), (0, 1.1))
                CenterArc((0, -0.1), 1.2, 0, 90)
                Line((1.2, -4.9), (1.2, -0.1))
                Line((1.2, -4.9), (1.7999999827, -4.9))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.8909733553, perimeter: 13.8849555922
            with BuildLine():
                Line((-1.2, -4.9), (0, -4.9))
                Line((0, 1.1), (0, -4.9))
                CenterArc((0, -0.1), 1.2, 90, 90)
                Line((-1.2, -0.1), (-1.2, -4.9))
            make_face()
            # Profile area: 4.0109733553, perimeter: 9.0849555922
            with BuildLine():
                Line((0, -4.9), (0, -8.5))
                Line((-1.2, -4.9), (0, -4.9))
                Line((-1.2, -4.9), (-1.2, -7.3))
                CenterArc((0, -7.3), 1.2, 180, 90)
            make_face()
            # Profile area: 6.8909733553, perimeter: 13.8849555922
            with BuildLine():
                Line((1.2, -4.9), (1.2, -0.1))
                CenterArc((0, -0.1), 1.2, 0, 90)
                Line((0, 1.1), (0, -4.9))
                Line((0, -4.9), (1.2, -4.9))
            make_face()
            # Profile area: 4.0109733553, perimeter: 9.0849555922
            with BuildLine():
                Line((0, -4.9), (1.2, -4.9))
                Line((0, -4.9), (0, -8.5))
                CenterArc((0, -7.3), 1.2, -90, 90)
                Line((1.2, -7.3), (1.2, -4.9))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_82146_ba68ced6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 26 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 27.9904219024, perimeter: 18.7546798234
            with Locations((14.1923143507, 3.9977778893)):
                Circle(2.9849)
            # Profile area: 1.0732998968, perimeter: 7.4823665567
            with BuildLine():
                Line((11.5639644221, 5.6008117957), (10.1796171275, 4.8567175839))
                CenterArc((10.3216511783, 4.592470865), 0.3, 118.2582717647, 39.4355231803)
                Line((10.0441005928, 4.7063377719), (9.3179587727, 2.9363670856))
                CenterArc((9.3642172036, 2.9173892677), 0.05, 157.6937949451, 35.8119471055)
                CenterArc((9.3297006285, 2.9108276745), 0.015, -160.0599649044, 94.3284867715)
                Line((9.3358658321, 2.8971532361), (9.3365697672, 2.8974706095))
                CenterArc((9.3211567581, 2.9316567054), 0.0375, -65.731478133, 33.2869634672)
                Line((9.3528034346, 2.9115386074), (10.2889983562, 4.3842154829))
                CenterArc((10.5421717678, 4.2232706985), 0.3, 101.1862835729, 46.3692017614)
                Line((10.4839719154, 4.5175711864), (11.156542373, 4.6505764072))
                CenterArc((14.0593678781, 3.9684242651), 2.9818999746, 146.8089833447, 19.9666871478)
            make_face()
            # Profile area: 1.0735100971, perimeter: 7.4916240114
            with BuildLine():
                Line((18.1374483316, 2.7580948486), (16.6950178565, 2.1340051492))
                CenterArc((18.0183209595, 3.0334285901), 0.3, -66.6035366497, 39.4355231803)
                Line((18.2852223852, 2.8964481938), (19.1666422812, 4.613863482))
                CenterArc((19.1488488528, 4.6229955084), 0.02, -27.1680134694, 169.8616903891)
                Line((19.1329407208, 4.6351170321), (18.0685065179, 3.2381672545))
                CenterArc((17.8298845379, 3.4199901097), 0.3, -83.6755248416, 46.3692017614)
                Line((17.8629322059, 3.1218159129), (17.1815090883, 3.0462914536))
                CenterArc((14.3469422017, 3.9720117263), 2.9818999746, -38.0528250698, 19.9666871478)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_82203_8b9714ce_0000():
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
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0024350364, perimeter: 0.3167391018
            with BuildLine():
                CenterArc((0, 0.1999999955), 0.0817616559, 51.6311624008, 22.9021637736)
                _nurbs_edge([(0.0218040213, 0.2788007127), (0.0226764437, 0.2693008801), (0.0235488661, 0.2593605355), (0.0244212884, 0.248984978), (0.0252937108, 0.2381794513), (0.0261661332, 0.2269489942)], [1, 1, 1, 1, 1, 1], [0.7180402178, 0.7180402178, 0.7180402178, 0.7180402178, 0.7180402178, 0.7180402178, 0.761661338, 0.761661338, 0.761661338, 0.761661338, 0.761661338, 0.761661338], 5)
                Line((0.0261661332, 0.2269489942), (0.0696437163, 0.2269489942))
                Line((0.0696437163, 0.2269489942), (0.0696437163, 0.1571663504))
                CenterArc((0, 0.1999999955), 0.0817616559, -31.593162936, 83.2243253368)
            make_face()
            # Profile area: 0.002780834, perimeter: 0.2310765267
            with BuildLine():
                CenterArc((0.0696437163, 0.0715620572), 0.0462793999, 90, 49.1070218644)
                _nurbs_edge([(0.0346595581, 0.1018587819), (0.0354035155, 0.0895506597), (0.036147473, 0.0769525013), (0.0368914304, 0.0640666317), (0.0376353879, 0.0508951507), (0.0383793453, 0.0374398948)], [1, 1, 1, 1, 1, 1], [0.8465955885, 0.8465955885, 0.8465955885, 0.8465955885, 0.8465955885, 0.8465955885, 0.8837934619, 0.8837934619, 0.8837934619, 0.8837934619, 0.8837934619, 0.8837934619], 5)
                CenterArc((0.0696437163, 0.0715620572), 0.0462793999, -132.4974167377, 42.4974167377)
                Line((0.0696437163, 0.1178414571), (0.0696437163, 0.0252826573))
            make_face()
            # Profile area: 0.0035870249, perimeter: 0.2643057255
            with BuildLine():
                CenterArc((0, 0.1999999955), 0.0817616559, -148.406837064, 34.4364695557)
                _nurbs_edge([(-0.033216827, 0.1252898169), (-0.0325734614, 0.1355427495), (-0.0311633227, 0.1575352739), (-0.0297531839, 0.1784679437), (-0.0283430452, 0.1983225349), (-0.0269329064, 0.2170785301), (-0.0261661332, 0.2269489942)], [1, 1, 1, 1, 1, 1, 1], [0.167831723, 0.167831723, 0.167831723, 0.167831723, 0.167831723, 0.167831723, 0.2, 0.238338662, 0.238338662, 0.238338662, 0.238338662, 0.238338662, 0.238338662], 5)
                Line((-0.0696437163, 0.2269489942), (-0.0261661332, 0.2269489942))
                Line((-0.0696437163, 0.1571663504), (-0.0696437163, 0.2269489942))
            make_face()
            # Profile area: 0.0035870249, perimeter: 0.2643057255
            with BuildLine():
                Line((0.0696437163, 0.2269489942), (0.0696437163, 0.1571663504))
                Line((0.0261661332, 0.2269489942), (0.0696437163, 0.2269489942))
                _nurbs_edge([(0.0261661332, 0.2269489942), (0.0269329064, 0.2170785301), (0.0283430452, 0.1983225349), (0.0297531839, 0.1784679437), (0.0311633227, 0.1575352739), (0.0325734614, 0.1355427495), (0.033216827, 0.1252898169)], [1, 1, 1, 1, 1, 1, 1], [0.761661338, 0.761661338, 0.761661338, 0.761661338, 0.761661338, 0.761661338, 0.8, 0.832168277, 0.832168277, 0.832168277, 0.832168277, 0.832168277, 0.832168277], 5)
                CenterArc((0, 0.1999999955), 0.0817616559, -66.0296324917, 34.4364695557)
            make_face()
            # Profile area: 0.0062776275, perimeter: 0.575443258
            with BuildLine():
                CenterArc((0, -0.2099999953), 0.0504008672, 168.5560465394, 31.0945820439)
                Line((-0.0499999989, -0.1999999955), (-0.0493988605, -0.1999999955))
                _nurbs_edge([(-0.0499999989, -0.1999999955), (-0.0479999989, -0.154491431), (-0.0456680785, -0.1037471578), (-0.0433361581, -0.0557042193), (-0.0410042376, -0.010388733), (-0.0386723172, 0.0321461816), (-0.0383403967, 0.0381440106)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.1165960242, 0.1165960242, 0.1165960242, 0.1165960242, 0.1165960242, 0.1165960242], 5)
                CenterArc((-0.0703562837, 0.0715620572), 0.0462793999, -89.1177777766, 42.8901954954)
                Line((-0.0696437163, -0.2269489942), (-0.0696437163, 0.0252881433))
                Line((-0.0474655544, -0.2269489942), (-0.0696437163, -0.2269489942))
            make_face()
            # Profile area: 0.0027602582, perimeter: 0.2302073801
            with BuildLine():
                CenterArc((-0.0703562837, 0.0715620572), 0.0462793999, -89.1177777766, 42.8901954954)
                _nurbs_edge([(-0.0383403967, 0.0381440106), (-0.0376137192, 0.0512751307), (-0.0368870416, 0.0641354504), (-0.0361603641, 0.0767232528), (-0.0354336865, 0.089036582), (-0.034707009, 0.1010732766)], [1, 1, 1, 1, 1, 1], [0.1165960242, 0.1165960242, 0.1165960242, 0.1165960242, 0.1165960242, 0.1165960242, 0.1529299025, 0.1529299025, 0.1529299025, 0.1529299025, 0.1529299025, 0.1529299025], 5)
                CenterArc((-0.0703562837, 0.0715620572), 0.0462793999, 39.618672682, 49.4991050946)
                Line((-0.0696437163, 0.0252881433), (-0.0696437163, 0.1178359711))
            make_face()
            # Profile area: 0.0034302564, perimeter: 0.2393640416
            with BuildLine():
                Line((-0.0696437163, 0.0252881433), (-0.0696437163, 0.1178359711))
                CenterArc((-0.0703562837, 0.0715620572), 0.0462793999, 89.1177777766, 24.2157602023)
                CenterArc((-0.0703562837, 0.0715620572), 0.0462793999, 113.333537979, 77.7166657824)
                CenterArc((-0.0703562837, 0.0715620572), 0.0462793999, -168.9497962386, 79.832018462)
            make_face()
            # Profile area: 0.0090743851, perimeter: 0.5061144819
            with BuildLine():
                CenterArc((-0.0703562837, 0.0715620572), 0.0462793999, 113.333537979, 77.7166657824)
                _nurbs_edge([(-0.0886867693, 0.1140564822), (-0.0936503755, 0.1171300559), (-0.1037646218, 0.1232738058), (-0.1192036418, 0.1322910571), (-0.1402501924, 0.1438618077), (-0.1671950173, 0.1574729646), (-0.1945473583, 0.1700807833), (-0.221480096, 0.1812685627), (-0.2467933587, 0.1904746143), (-0.2686060902, 0.1968664118), (-0.2846708402, 0.1994719235), (-0.2927607422, 0.1973433694), (-0.291018772, 0.1897082639), (-0.2784254468, 0.1761772224), (-0.2546112032, 0.156651317), (-0.2197765691, 0.1313302307), (-0.183266115, 0.1065285906), (-0.1511856179, 0.085466361), (-0.1278131088, 0.0703932334), (-0.1157776457, 0.0626917288)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0015590217, 0.0015590217, 0.0015590217, 0.0015590217, 0.0015590217, 0.0015590217, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 0.99823208, 0.99823208, 0.99823208, 0.99823208, 0.99823208, 0.99823208], 5)
            make_face()
            # Profile area: 0.0024350364, perimeter: 0.3167391018
            with BuildLine():
                CenterArc((0, 0.1999999955), 0.0817616559, 128.3688375992, 83.2243253368)
                Line((-0.0696437163, 0.1571663504), (-0.0696437163, 0.2269489942))
                Line((-0.0696437163, 0.2269489942), (-0.0261661332, 0.2269489942))
                _nurbs_edge([(-0.0261661332, 0.2269489942), (-0.0252937108, 0.2381794513), (-0.0244212884, 0.248984978), (-0.0235488661, 0.2593605355), (-0.0226764437, 0.2693008801), (-0.0218040213, 0.2788007127)], [1, 1, 1, 1, 1, 1], [0.238338662, 0.238338662, 0.238338662, 0.238338662, 0.238338662, 0.238338662, 0.2819597822, 0.2819597822, 0.2819597822, 0.2819597822, 0.2819597822, 0.2819597822], 5)
                CenterArc((0, 0.1999999955), 0.0817616559, 105.4666738256, 22.9021637736)
            make_face()
            # Profile area: 0.0026770817, perimeter: 0.2484342168
            with BuildLine():
                CenterArc((0, -0.2099999953), 0.0504008672, -19.6506285833, 31.0945820439)
                Line((-0.0493988605, -0.1999999955), (0.0493988605, -0.1999999955))
                CenterArc((0, -0.2099999953), 0.0504008672, 168.5560465394, 31.0945820439)
                Line((0.0474655544, -0.2269489942), (-0.0474655544, -0.2269489942))
            make_face()
            # Profile area: 0.0104321451, perimeter: 0.7852051395
            with BuildLine():
                CenterArc((0, 0.1999999955), 0.0817616559, 105.4666738256, 22.9021637736)
                _nurbs_edge([(-0.0218040213, 0.2788007127), (-0.0214432169, 0.2827295217), (-0.0190824126, 0.3079434006), (-0.0147216084, 0.348529634), (-0.0083608042, 0.3910712468), (0, 0.4131968189), (0.0083608042, 0.3910712468), (0.0147216084, 0.348529634), (0.0190824126, 0.3079434006), (0.0214432169, 0.2827295217), (0.0218040213, 0.2788007127)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2819597822, 0.2819597822, 0.2819597822, 0.2819597822, 0.2819597822, 0.2819597822, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7180402178, 0.7180402178, 0.7180402178, 0.7180402178, 0.7180402178, 0.7180402178], 5)
                CenterArc((0, 0.1999999955), 0.0817616559, 51.6311624008, 22.9021637736)
                _nurbs_edge([(-0.0507512135, 0.2641036827), (-0.0487211649, 0.2812373775), (-0.0446610678, 0.3140084896), (-0.0385709222, 0.3586764632), (-0.0304507281, 0.4091074877), (-0.0203004854, 0.4559035144), (-0.0101502427, 0.4850051877), (0, 0.4949685136), (0.0101502427, 0.4850051877), (0.0203004854, 0.4559035144), (0.0304507281, 0.4091074877), (0.0385709222, 0.3586764632), (0.0446610678, 0.3140084896), (0.0487211649, 0.2812373775), (0.0507512135, 0.2641036827)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 0.0009104232, perimeter: 0.1516066101
            with BuildLine():
                CenterArc((0, 0.1999999955), 0.0817616559, -66.0296324917, 34.4364695557)
                _nurbs_edge([(0.033216827, 0.1252898169), (0.0335053732, 0.1206914279), (0.0337939194, 0.1160489868), (0.0340824656, 0.1113626391), (0.0343710118, 0.1066325256), (0.0346595581, 0.1018587819)], [1, 1, 1, 1, 1, 1], [0.832168277, 0.832168277, 0.832168277, 0.832168277, 0.832168277, 0.832168277, 0.8465955885, 0.8465955885, 0.8465955885, 0.8465955885, 0.8465955885, 0.8465955885], 5)
                CenterArc((0.0696437163, 0.0715620572), 0.0462793999, 90, 49.1070218644)
                Line((0.0696437163, 0.1571663504), (0.0696437163, 0.1178414571))
            make_face()
            # Profile area: 0.0009220885, perimeter: 0.15271573
            with BuildLine():
                CenterArc((-0.0703562837, 0.0715620572), 0.0462793999, 39.618672682, 49.4991050946)
                _nurbs_edge([(-0.034707009, 0.1010732766), (-0.0344089726, 0.1060099547), (-0.0341109362, 0.1109000998), (-0.0338128998, 0.1157435628), (-0.0335148634, 0.1205401886), (-0.033216827, 0.1252898169)], [1, 1, 1, 1, 1, 1], [0.1529299025, 0.1529299025, 0.1529299025, 0.1529299025, 0.1529299025, 0.1529299025, 0.167831723, 0.167831723, 0.167831723, 0.167831723, 0.167831723, 0.167831723], 5)
                CenterArc((0, 0.1999999955), 0.0817616559, -148.406837064, 34.4364695557)
                Line((-0.0696437163, 0.1178359711), (-0.0696437163, 0.1571663504))
            make_face()
            # Profile area: 0.0062687171, perimeter: 0.5744153214
            with BuildLine():
                CenterArc((0.0696437163, 0.0715620572), 0.0462793999, -132.4974167377, 42.4974167377)
                _nurbs_edge([(0.0383793453, 0.0374398948), (0.0387034761, 0.031577648), (0.0410276068, -0.0108429501), (0.0433517375, -0.056025222), (0.0456758682, -0.1039166678), (0.0479999989, -0.154491431), (0.0499999989, -0.1999999955)], [1, 1, 1, 1, 1, 1, 1], [0.8837934619, 0.8837934619, 0.8837934619, 0.8837934619, 0.8837934619, 0.8837934619, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0.0493988605, -0.1999999955), (0.0499999989, -0.1999999955))
                CenterArc((0, -0.2099999953), 0.0504008672, -19.6506285833, 31.0945820439)
                Line((0.0696437163, -0.2269489942), (0.0474655544, -0.2269489942))
                Line((0.0696437163, 0.0252826573), (0.0696437163, -0.2269489942))
            make_face()
            # Profile area: 0.0033643046, perimeter: 0.2379498227
            with BuildLine():
                Line((0.0696437163, 0.1178414571), (0.0696437163, 0.0252826573))
                CenterArc((0.0696437163, 0.0715620572), 0.0462793999, -90, 77.6209488401)
                CenterArc((0.0696437163, 0.0715620572), 0.0462793999, -12.3790511599, 77.9201545241)
                CenterArc((0.0696437163, 0.0715620572), 0.0462793999, 65.5411033641, 24.4588966359)
            make_face()
            # Profile area: 0.0091480693, perimeter: 0.5089281921
            with BuildLine():
                CenterArc((0.0696437163, 0.0715620572), 0.0462793999, -12.3790511599, 77.9201545241)
                _nurbs_edge([(0.0888052548, 0.1136882759), (0.0938844122, 0.1168391782), (0.1041133645, 0.1230612118), (0.1196686885, 0.1321549445), (0.1408361449, 0.1437978483), (0.1679075846, 0.1574729646), (0.1952599257, 0.1700807833), (0.2221926633, 0.1812685627), (0.247505926, 0.1904746143), (0.2693186576, 0.1968664117), (0.2853834076, 0.1994719235), (0.2934733095, 0.1973433694), (0.2917313393, 0.1897082639), (0.2791380142, 0.1761772224), (0.2553237705, 0.156651317), (0.2203033968, 0.1311952177), (0.1834909581, 0.1061973374), (0.1510387263, 0.0849022376), (0.1272671425, 0.0695818628), (0.1148471538, 0.061640762)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


def model_82377_8e929ad6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch9 -> Extrude9 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2054531843, perimeter: 1.606798325
            with Locations((0, -1.6917516196)):
                Circle(0.255729896)
        # OneSide extrude, distance=0.153
        extrude(amount=0.153)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.153), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.020006662, perimeter: 0.5014091442
            with Locations((0, -1.6917516196)):
                Circle(0.0798017438)
        # OneSide extrude, distance=0.4093
        extrude(amount=0.4093, mode=Mode.ADD)
    return part.part


def model_82614_a8ef3280_0001():
    """Model: led body v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0235619447, perimeter: 0.9424778008
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0333122229, perimeter: 1.5302042857
            with BuildLine():
                CenterArc((0, 0), 0.143539576, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0235619447, perimeter: 0.9424778008
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0078539819, perimeter: 0.31415927
            Circle(0.0500000007)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_82614_a8ef3280_0018():
    """Model: cap top v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7787067899, perimeter: 3.4992943309
            with BuildLine():
                CenterArc((-0.0052692485, 0.4822345586), 0.16, 30.4709029231, 119.5290970769)
                Line((-0.1438333131, 0.5622345586), (-0.5575203445, -0.1542923983))
                CenterArc((-0.4189562799, -0.2342923983), 0.16, 150, 120)
                Line((-0.4189562799, -0.3942923983), (0.416307393, -0.3942923983))
                CenterArc((0.416307393, -0.2342923983), 0.16, -90, 120.4709029231)
                Line((0.1326326391, 0.5633706751), (0.5542092806, -0.1531562818))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_82614_a8ef3280_0019():
    """Model: tip v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0028274334, perimeter: 0.5654866776
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.04, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0175929189, perimeter: 0.879645943
            with BuildLine():
                CenterArc((0, 0), 0.09, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_82760_61e37ad2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5)
    return part.part


def model_83101_df904768_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 378.5867228627, perimeter: 270.5911485751
            with BuildLine():
                CenterArc((5, 5), 5, 180, 90)
                Line((5, 0), (31.3, 0))
                CenterArc((31.3, 5), 5, -90, 90)
                Line((36.3, 52), (36.3, 5))
                Line((33.3, 52), (36.3, 52))
                Line((33.3, 4), (33.3, 52))
                CenterArc((31.3, 4), 2, -90, 90)
                Line((5.3, 2), (31.3, 2))
                CenterArc((5.3, 4), 2, 180, 90)
                Line((3.3, 52), (3.3, 4))
                Line((0, 52), (3.3, 52))
                Line((0, 5), (0, 52))
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 22.0893233456, perimeter: 19.280972451
            with BuildLine():
                Line((18.15, 17.75), (18.15, 10.25))
                CenterArc((18.15, 14), 3.75, -90, 180)
            make_face()
            # Profile area: 22.0893233456, perimeter: 19.280972451
            with BuildLine():
                CenterArc((18.15, 14), 3.75, 90, 180)
                Line((18.15, 17.75), (18.15, 10.25))
            make_face()
        # OneSide extrude, distance=32.5
        extrude(amount=32.5, mode=Mode.ADD)
    return part.part


def model_83106_8e9f36f3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.0836477965, perimeter: 17.4928556845
            with BuildLine():
                Line((-0.0490381057, -2.9150635095), (2.5, -1.5))
                Line((2.5, -1.5), (2.5490381057, 1.4150635095))
                Line((2.5490381057, 1.4150635095), (0.0490381057, 2.9150635095))
                Line((0.0490381057, 2.9150635095), (-2.5, 1.5))
                Line((-2.5, 1.5), (-2.5490381057, -1.4150635095))
                Line((-2.5490381057, -1.4150635095), (-0.0490381057, -2.9150635095))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 7.024814731
            Circle(1.1180339887)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)
    return part.part


def model_83110_487f8396_0000():
    """Model: Cable"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 2.6000000387)):
                Circle(0.5)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 2.6000000387)):
                Circle(0.3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_83220_c8e6b276_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 194.8557158515, perimeter: 51.9615242271
            with BuildLine():
                Line((7.5, -4.3301270189), (7.5, 4.3301270189))
                Line((7.5, 4.3301270189), (0, 8.6602540378))
                Line((0, 8.6602540378), (-7.5, 4.3301270189))
                Line((-7.5, 4.3301270189), (-7.5, -4.3301270189))
                Line((-7.5, -4.3301270189), (0, -8.6602540378))
                Line((0, -8.6602540378), (7.5, -4.3301270189))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 70.1894251052, perimeter: 29.6989280797
            Circle(4.7267312084)
        # OneSide extrude, distance=48
        extrude(amount=48, mode=Mode.ADD)
    return part.part


def model_83239_1a00d111_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7567475535, perimeter: 12.252211349
            with BuildLine():
                CenterArc((0, 0), 1.2, 48.5903778907, 262.8192442185)
                CenterArc((0, 0), 1.2, -48.5903778907, 97.1807557815)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.4
        extrude(amount=1.4, both=True)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0972340804, perimeter: 18.5353966562
            with BuildLine():
                CenterArc((17.8, 0), 1.75, 149.0502769211, 61.8994461577)
                CenterArc((17.8, 0), 1.75, -149.0502769211, 298.1005538423)
            make_face()
            with BuildLine():
                CenterArc((17.8, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.1
        extrude(amount=2.1, both=True)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.3228318691, perimeter: 64.0784593023
            with BuildLine():
                CenterArc((17.8, 0), 1.75, 149.0502769211, 61.8994461577)
                Line((16.299166898, 0.9), (0.7937253933, 0.9))
                CenterArc((0, 0), 1.2, -48.5903778907, 97.1807557815)
                Line((16.299166898, -0.9), (0.7937253933, -0.9))
            make_face()
            with BuildLine():
                Line((15.3739429534, -0.4993205687), (2.4000261845, -0.4999999993))
                CenterArc((2.4, 0), 0.5, 89.9969994792, 180.0060010415)
                Line((15.3739429534, 0.4993205687), (2.4000261845, 0.4999999993))
                CenterArc((15.4, 0), 0.5, -92.9872708136, 185.9745416271)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True, mode=Mode.ADD)
    return part.part


def model_83378_2dc861a1_0002():
    """Model: leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 827.5955414598, perimeter: 201.2336200486
            with BuildLine():
                Line((7.5091771091, -15.24), (10.8021011768, -43.1702306904))
                Line((17.7895184527, -43.1687526233), (10.8021011768, -43.1702306904))
                Line((17.7895184527, -43.1687526233), (12.7, 0))
                Line((12.7, 0), (6.2327833004, 0))
                Line((6.2327833004, 0), (6.2327833004, 1.8288))
                Line((-6.2327833004, 1.8288), (6.2327833004, 1.8288))
                Line((-6.2327833004, 0), (-6.2327833004, 1.8288))
                Line((-12.7, 0), (-6.2327833004, 0))
                Line((-17.7895184527, -43.1687526233), (-12.7, 0))
                Line((-17.7895184527, -43.1687526233), (-10.8021011768, -43.1702306904))
                Line((-7.5091771091, -15.24), (-10.8021011768, -43.1702306904))
                Line((-7.5091771091, -15.24), (7.5091771091, -15.24))
            make_face()
        # Symmetric extrude, each_side=0.9144
        extrude(amount=0.9144, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9144, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.60771072, perimeter: 20.7264
            with BuildLine():
                Line((-0.9144, 1.8288), (-0.9144, -6.7056))
                Line((-0.9144, -6.7056), (0.9144, -6.7056))
                Line((0.9144, 1.8288), (0.9144, -6.7056))
                Line((0.9144, 1.8288), (-0.9144, 1.8288))
            make_face()
        # OneSide extrude, distance=-1.8288
        extrude(amount=-1.8288, mode=Mode.SUBTRACT)
    return part.part


def model_83392_50368ba2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.75, perimeter: 12
            with BuildLine():
                Line((3.5, -4.5), (1, -4.5))
                Line((3.5, -1), (3.5, -4.5))
                Line((1, -1), (3.5, -1))
                Line((1, -4.5), (1, -1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_83395_4c74f86e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((4, -0.25)):
                Circle(3.75)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.4751091356, perimeter: 14.8188629093
            with Locations((4, -0.25)):
                Circle(2.358495283)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


def model_83396_fdb2987a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.0597320457, perimeter: 19.1095620787
            with Locations((1, -1)):
                Circle(3.0413812651)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.61946778, perimeter: 16.8595556057
            with Locations((1.1000000164, -1.1000000164)):
                Circle(2.683281613)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)
    return part.part


def model_83411_51aa29e1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 706.8583470577, perimeter: 94.2477796077
            Circle(15)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_83421_0bbb503e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((3, 3)):
                Circle(2)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            with Locations((3, 3)):
                Circle(1.9)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


def model_83432_a7f85698_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.0229152728, perimeter: 13.2746808026
            Circle(2.1127310677)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_83432_a7f85698_0002():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((5.500000082, 2.3000000343)):
                Circle(0.6)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_84608_204c01e6_0003():
    """Model: Zijkant R"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 110, perimeter: 42
            with BuildLine():
                Line((9, -5), (-2, -5))
                Line((9, 5), (9, -5))
                Line((9, 5), (-2, 5))
                Line((-2, -5), (-2, 5))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.15, 4.2)):
                Circle(0.1)
        # OneSide extrude, distance=-1.24
        extrude(amount=-1.24, mode=Mode.SUBTRACT)
    return part.part


def model_84608_204c01e6_0004():
    """Model: Spijker"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-4.9549576654, 4.0379159045)):
                Circle(0.075)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1079922475, perimeter: 1.7278759595
            with BuildLine():
                CenterArc((-4.9549576654, 4.0379159045), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.9549576654, 4.0379159045), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-4.9549576654, 4.0379159045)):
                Circle(0.075)
        # OneSide extrude, distance=0.12
        extrude(amount=0.12, mode=Mode.ADD)
    return part.part


def model_85195_c6ef0067_0001():
    """Model: Component16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.5980762114, perimeter: 6
            with BuildLine():
                Line((0.5, 0.8660254038), (1, 0))
                Line((-0.5, 0.8660254038), (0.5, 0.8660254038))
                Line((-1, 0), (-0.5, 0.8660254038))
                Line((-0.5, -0.8660254038), (-1, 0))
                Line((0.5, -0.8660254038), (-0.5, -0.8660254038))
                Line((1, 0), (0.5, -0.8660254038))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)
    return part.part


def model_85195_c6ef0067_0004():
    """Model: shaft 25 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # TwoSides extrude, along=1.5, against=-2.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_85552_3669d6cf_0001():
    """Model: Brazo Direccion"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0206858347, perimeter: 13.9424777961
            with BuildLine():
                CenterArc((-3.2, 2.7484970672), 0.15, 90, 180)
                Line((-3.2, 2.5984970672), (3.3, 2.5984970672))
                CenterArc((3.3, 2.7484970672), 0.15, -90, 180)
                Line((3.3, 2.8984970672), (-3.2, 2.8984970672))
            make_face()
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-3.2, -2.7484970672)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((3.3, -2.7484970672)):
                Circle(0.05)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_85617_4879c1a8_0001():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.25, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8335739468, perimeter: 7.311913156
            with BuildLine():
                Line((1.7799705827, 0.049773076), (1.7799705827, -3.006183502))
                Line((1.7799705827, -3.006183502), (2.3799705827, -3.006183502))
                Line((2.3799705827, -3.006183502), (2.3799705827, 0.049773076))
                Line((2.3799705827, 0.049773076), (1.7799705827, 0.049773076))
            make_face()
        # Symmetric extrude, each_side=0.18
        extrude(amount=0.18, both=True)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.07, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.0799705827, -2.7171419971)):
                Circle(0.1)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_86186_a116ac82_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 49.19345, perimeter: 30.834982348
            with BuildLine():
                Line((0, 0), (10.16, 0))
                Line((10.16, 0), (10.16, 2.54))
                Line((2.54, 5.969), (10.16, 2.54))
                Line((2.54, 6.604), (2.54, 5.969))
                Line((0, 6.604), (2.54, 6.604))
                Line((0, 0), (0, 6.604))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_86296_8a6ed4d3_0010():
    """Model: BODY (5)"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2398751121, perimeter: 2.04307619
            with BuildLine():
                Line((0.3375983, -0.17145), (0.36195, 0))
                Line((0.36195, 0), (0.3375983, 0.17145))
                Line((0.3375983, 0.17145), (-0.3375983, 0.17145))
                Line((-0.3375983, 0.17145), (-0.36195, 0))
                Line((-0.36195, 0), (-0.3375983, -0.17145))
                Line((-0.3375983, -0.17145), (0.3375983, -0.17145))
            make_face()
        # OneSide extrude, distance=3.4671
        extrude(amount=3.4671)

        # Sketch2 -> 押し出し2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.17145), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0127234502, perimeter: 0.4627433388
            with BuildLine():
                CenterArc((0, 0), 0.09, 90, 180)
                Line((0, -0.09), (0, 0.09))
            make_face()
            # Profile area: 0.0127234502, perimeter: 0.4627433388
            with BuildLine():
                Line((0, -0.09), (0, 0.09))
                CenterArc((0, 0), 0.09, -90, 180)
            make_face()
        # OneSide extrude, distance=-0.11
        extrude(amount=-0.11, mode=Mode.SUBTRACT)
    return part.part


def model_86384_a3b5cf5e_0001():
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
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 240.5281875405, perimeter: 54.9778714378
            Circle(8.75)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_86386_ce62c3a1_0004():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -33.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((33.1250136379, 70.2382225623)):
                Circle(1.5)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -31), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((33.1250136379, 70.2382225623), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((33.1250136379, 70.2382225623), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((33.1250136379, 70.2382225623)):
                Circle(1.5)
        # OneSide extrude, distance=62
        extrude(amount=62, mode=Mode.ADD)
    return part.part


def model_86497_3288c394_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 181.4269757448, perimeter: 103.6725575685
            with BuildLine():
                CenterArc((0, 0), 10, 43.9780084757, 272.0439830486)
                CenterArc((0, 0), 10, -43.9780084757, 87.9560169514)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 62.8318530718, perimeter: 62.8318530718
            with BuildLine():
                CenterArc((100, 0), 6, 134.2266642879, 91.5466714242)
                CenterArc((100, 0), 6, -134.2266642879, 268.4533285758)
            make_face()
            with BuildLine():
                CenterArc((100, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=7
        extrude(amount=7, both=True)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 529.1463918513, perimeter: 355.1538884079
            with BuildLine():
                CenterArc((0, 0), 10, -43.9780084757, 87.9560169514)
                Line((7.1960637425, -6.9438221905), (95.8150080224, -4.2995165016))
                CenterArc((100, 0), 6, 134.2266642879, 91.5466714242)
                Line((7.1960637425, 6.9438221905), (95.8150080224, 4.2995165016))
            make_face()
            with BuildLine():
                CenterArc((17.9756463649, -0.1260623091), 3, 94.9697407281, 170.0605185438)
                CenterArc((17.9756463649, -0.1260623091), 3, 85.2641737948, 9.7055669333)
                Line((18.2233313905, 2.8636955621), (84.9938761364, 2.9999937497))
                CenterArc((85, 0), 3, -89.9022596339, 180.0192168953)
                Line((18.2457305499, -3.1138799965), (85.0051176711, -2.9999956349))
                CenterArc((17.9756463649, -0.1260623091), 3, -94.9697407281, 10.1349621885)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True, mode=Mode.ADD)
    return part.part


def model_86503_9c214425_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.75, perimeter: 28
            with BuildLine():
                Line((-9, -8.5), (2.5, -8.5))
                Line((2.5, -8.5), (2.5, -6))
                Line((2.5, -6), (-9, -6))
                Line((-9, -6), (-9, -8.5))
            make_face()
            # Profile area: 51.9344535547, perimeter: 29.5641577581
            with BuildLine():
                Line((2.5, -6), (-9, -6))
                CenterArc((-3.25, -6), 5.75, 0, 180)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_86586_ee75152f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 79.4803711652, perimeter: 39.8303473774
            with BuildLine():
                Line((6.985, 5.5880001783), (0, 5.5880001783))
                Line((0, 5.5880001783), (0, -5.8420001864))
                Line((0, -5.8420001864), (6.985, -5.8420001864))
                Line((6.985, -5.8420001864), (6.985, 5.5880001783))
            make_face()
            with BuildLine():
                CenterArc((3.4925, 2.7940001783), 0.23876, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.4925, -3.8100001216), 0.23876, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on Profile plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.9806392, perimeter: 7.7216
            with BuildLine():
                Line((4.1148000892, -1.5239999595), (3.0480000892, -1.5239999595))
                Line((4.1148000892, 1.2700000405), (4.1148000892, -1.5239999595))
                Line((3.0480000892, 1.2700000405), (4.1148000892, 1.2700000405))
                Line((3.0480000892, -1.5239999595), (3.0480000892, 1.2700000405))
            make_face()
        # OneSide extrude, distance=-3.302
        extrude(amount=-3.302, mode=Mode.SUBTRACT)
    return part.part


def model_86801_40091568_0000():
    """Model: Cilinder zelfgemaakte reconstructie volledig v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.4528666144, perimeter: 52.3103706144
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                Line((0.514, 0.514), (0.1, 0.514))
                Line((0.514, 0.1), (0.514, 0.514))
                Line((0.1, 0.1), (0.514, 0.1))
                Line((0.1, 0.514), (0.1, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.514, 1.128), (0.1, 1.128))
                Line((0.514, 0.714), (0.514, 1.128))
                Line((0.1, 0.714), (0.514, 0.714))
                Line((0.1, 1.128), (0.1, 0.714))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.514, 1.742), (0.1, 1.742))
                Line((0.514, 1.328), (0.514, 1.742))
                Line((0.1, 1.328), (0.514, 1.328))
                Line((0.1, 1.742), (0.1, 1.328))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.128, 0.514), (0.714, 0.514))
                Line((1.128, 0.1), (1.128, 0.514))
                Line((0.714, 0.1), (1.128, 0.1))
                Line((0.714, 0.514), (0.714, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.742, 0.514), (1.328, 0.514))
                Line((1.742, 0.1), (1.742, 0.514))
                Line((1.328, 0.1), (1.742, 0.1))
                Line((1.328, 0.514), (1.328, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.128, 1.128), (0.714, 1.128))
                Line((1.128, 0.714), (1.128, 1.128))
                Line((0.714, 0.714), (1.128, 0.714))
                Line((0.714, 1.128), (0.714, 0.714))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.514, 1.742), (-0.1, 1.742))
                Line((-0.1, 1.742), (-0.1, 1.328))
                Line((-0.1, 1.328), (-0.514, 1.328))
                Line((-0.514, 1.328), (-0.514, 1.742))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.1, 0.1), (-0.514, 0.1))
                Line((-0.514, 0.1), (-0.514, 0.514))
                Line((-0.514, 0.514), (-0.1, 0.514))
                Line((-0.1, 0.514), (-0.1, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.328, 0.1), (-1.742, 0.1))
                Line((-1.742, 0.1), (-1.742, 0.514))
                Line((-1.742, 0.514), (-1.328, 0.514))
                Line((-1.328, 0.514), (-1.328, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.714, 0.714), (-1.128, 0.714))
                Line((-1.128, 0.714), (-1.128, 1.128))
                Line((-1.128, 1.128), (-0.714, 1.128))
                Line((-0.714, 1.128), (-0.714, 0.714))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.714, 0.514), (-0.714, 0.1))
                Line((-0.714, 0.1), (-1.128, 0.1))
                Line((-1.128, 0.1), (-1.128, 0.514))
                Line((-1.128, 0.514), (-0.714, 0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.514, 0.714), (-0.514, 1.128))
                Line((-0.514, 1.128), (-0.1, 1.128))
                Line((-0.1, 1.128), (-0.1, 0.714))
                Line((-0.1, 0.714), (-0.514, 0.714))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.128, -0.714), (1.128, -1.128))
                Line((1.128, -1.128), (0.714, -1.128))
                Line((0.714, -1.128), (0.714, -0.714))
                Line((0.714, -0.714), (1.128, -0.714))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.714, -0.514), (0.714, -0.1))
                Line((0.714, -0.1), (1.128, -0.1))
                Line((1.128, -0.1), (1.128, -0.514))
                Line((1.128, -0.514), (0.714, -0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.514, -0.1), (0.514, -0.514))
                Line((0.514, -0.514), (0.1, -0.514))
                Line((0.1, -0.514), (0.1, -0.1))
                Line((0.1, -0.1), (0.514, -0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.514, -1.128), (-0.1, -1.128))
                Line((-0.514, -0.714), (-0.514, -1.128))
                Line((-0.1, -0.714), (-0.514, -0.714))
                Line((-0.1, -1.128), (-0.1, -0.714))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.1, -1.742), (0.1, -1.328))
                Line((0.1, -1.328), (0.514, -1.328))
                Line((0.514, -1.328), (0.514, -1.742))
                Line((0.514, -1.742), (0.1, -1.742))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.514, -1.128), (0.1, -1.128))
                Line((0.1, -1.128), (0.1, -0.714))
                Line((0.1, -0.714), (0.514, -0.714))
                Line((0.514, -0.714), (0.514, -1.128))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.128, -0.714), (-1.128, -1.128))
                Line((-0.714, -0.714), (-1.128, -0.714))
                Line((-0.714, -1.128), (-0.714, -0.714))
                Line((-1.128, -1.128), (-0.714, -1.128))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.328, -0.1), (-1.742, -0.1))
                Line((-1.328, -0.514), (-1.328, -0.1))
                Line((-1.742, -0.514), (-1.328, -0.514))
                Line((-1.742, -0.1), (-1.742, -0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.514, -0.514), (-0.1, -0.514))
                Line((-0.514, -0.1), (-0.514, -0.514))
                Line((-0.1, -0.1), (-0.514, -0.1))
                Line((-0.1, -0.514), (-0.1, -0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.328, -0.514), (1.328, -0.1))
                Line((1.328, -0.1), (1.742, -0.1))
                Line((1.742, -0.1), (1.742, -0.514))
                Line((1.742, -0.514), (1.328, -0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.128, -0.1), (-1.128, -0.514))
                Line((-0.714, -0.1), (-1.128, -0.1))
                Line((-0.714, -0.514), (-0.714, -0.1))
                Line((-1.128, -0.514), (-0.714, -0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.1, -1.742), (-0.1, -1.328))
                Line((-0.514, -1.742), (-0.1, -1.742))
                Line((-0.514, -1.328), (-0.514, -1.742))
                Line((-0.1, -1.328), (-0.514, -1.328))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8.4528666144, perimeter: 52.3103706144
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                Line((1.128, -1.128), (0.714, -1.128))
                Line((0.714, -1.128), (0.714, -0.714))
                Line((0.714, -0.714), (1.128, -0.714))
                Line((1.128, -0.714), (1.128, -1.128))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.328, 0.1), (-1.742, 0.1))
                Line((-1.742, 0.1), (-1.742, 0.514))
                Line((-1.742, 0.514), (-1.328, 0.514))
                Line((-1.328, 0.514), (-1.328, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.1, 1.742), (-0.1, 1.328))
                Line((-0.1, 1.328), (-0.514, 1.328))
                Line((-0.514, 1.328), (-0.514, 1.742))
                Line((-0.514, 1.742), (-0.1, 1.742))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.128, 0.1), (-1.128, 0.514))
                Line((-1.128, 0.514), (-0.714, 0.514))
                Line((-0.714, 0.514), (-0.714, 0.1))
                Line((-0.714, 0.1), (-1.128, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.714, -0.1), (-0.714, -0.514))
                Line((-0.714, -0.514), (-1.128, -0.514))
                Line((-1.128, -0.514), (-1.128, -0.1))
                Line((-1.128, -0.1), (-0.714, -0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.128, 1.128), (1.128, 0.714))
                Line((1.128, 0.714), (0.714, 0.714))
                Line((0.714, 0.714), (0.714, 1.128))
                Line((0.714, 1.128), (1.128, 1.128))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.1, 1.128), (0.514, 1.128))
                Line((0.514, 1.128), (0.514, 0.714))
                Line((0.514, 0.714), (0.1, 0.714))
                Line((0.1, 0.714), (0.1, 1.128))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.714, 0.1), (0.714, 0.514))
                Line((0.714, 0.514), (1.128, 0.514))
                Line((1.128, 0.514), (1.128, 0.1))
                Line((1.128, 0.1), (0.714, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.514, -0.514), (0.1, -0.514))
                Line((0.1, -0.514), (0.1, -0.1))
                Line((0.1, -0.1), (0.514, -0.1))
                Line((0.514, -0.1), (0.514, -0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.128, -0.514), (0.714, -0.514))
                Line((0.714, -0.514), (0.714, -0.1))
                Line((0.714, -0.1), (1.128, -0.1))
                Line((1.128, -0.1), (1.128, -0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.514, 0.514), (-0.1, 0.514))
                Line((-0.1, 0.514), (-0.1, 0.1))
                Line((-0.1, 0.1), (-0.514, 0.1))
                Line((-0.514, 0.1), (-0.514, 0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.1, -1.742), (-0.514, -1.742))
                Line((-0.514, -1.742), (-0.514, -1.328))
                Line((-0.514, -1.328), (-0.1, -1.328))
                Line((-0.1, -1.328), (-0.1, -1.742))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.128, -0.714), (-0.714, -0.714))
                Line((-0.714, -0.714), (-0.714, -1.128))
                Line((-0.714, -1.128), (-1.128, -1.128))
                Line((-1.128, -1.128), (-1.128, -0.714))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.128, 0.714), (-1.128, 1.128))
                Line((-1.128, 1.128), (-0.714, 1.128))
                Line((-0.714, 1.128), (-0.714, 0.714))
                Line((-0.714, 0.714), (-1.128, 0.714))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.514, -1.128), (0.1, -1.128))
                Line((0.1, -1.128), (0.1, -0.714))
                Line((0.1, -0.714), (0.514, -0.714))
                Line((0.514, -0.714), (0.514, -1.128))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.742, -0.514), (1.328, -0.514))
                Line((1.328, -0.514), (1.328, -0.1))
                Line((1.328, -0.1), (1.742, -0.1))
                Line((1.742, -0.1), (1.742, -0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.514, -1.742), (0.1, -1.742))
                Line((0.1, -1.742), (0.1, -1.328))
                Line((0.1, -1.328), (0.514, -1.328))
                Line((0.514, -1.328), (0.514, -1.742))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.328, 0.1), (1.328, 0.514))
                Line((1.328, 0.514), (1.742, 0.514))
                Line((1.742, 0.514), (1.742, 0.1))
                Line((1.742, 0.1), (1.328, 0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.514, 1.128), (-0.1, 1.128))
                Line((-0.1, 1.128), (-0.1, 0.714))
                Line((-0.1, 0.714), (-0.514, 0.714))
                Line((-0.514, 0.714), (-0.514, 1.128))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.742, -0.1), (-1.328, -0.1))
                Line((-1.328, -0.1), (-1.328, -0.514))
                Line((-1.328, -0.514), (-1.742, -0.514))
                Line((-1.742, -0.514), (-1.742, -0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.514, -0.1), (-0.1, -0.1))
                Line((-0.1, -0.1), (-0.1, -0.514))
                Line((-0.1, -0.514), (-0.514, -0.514))
                Line((-0.514, -0.514), (-0.514, -0.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.514, -1.128), (-0.514, -0.714))
                Line((-0.514, -0.714), (-0.1, -0.714))
                Line((-0.1, -0.714), (-0.1, -1.128))
                Line((-0.1, -1.128), (-0.514, -1.128))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.514, 0.514), (0.514, 0.1))
                Line((0.514, 0.1), (0.1, 0.1))
                Line((0.1, 0.1), (0.1, 0.514))
                Line((0.1, 0.514), (0.514, 0.514))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.1, 1.328), (0.1, 1.742))
                Line((0.1, 1.742), (0.514, 1.742))
                Line((0.514, 1.742), (0.514, 1.328))
                Line((0.514, 1.328), (0.1, 1.328))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((1.128, -0.714), (1.128, -1.128))
                Line((0.714, -0.714), (1.128, -0.714))
                Line((0.714, -1.128), (0.714, -0.714))
                Line((1.128, -1.128), (0.714, -1.128))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-1.328, 0.514), (-1.328, 0.1))
                Line((-1.742, 0.514), (-1.328, 0.514))
                Line((-1.742, 0.1), (-1.742, 0.514))
                Line((-1.328, 0.1), (-1.742, 0.1))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-0.514, 1.742), (-0.1, 1.742))
                Line((-0.514, 1.328), (-0.514, 1.742))
                Line((-0.1, 1.328), (-0.514, 1.328))
                Line((-0.1, 1.742), (-0.1, 1.328))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-0.714, 0.1), (-1.128, 0.1))
                Line((-0.714, 0.514), (-0.714, 0.1))
                Line((-1.128, 0.514), (-0.714, 0.514))
                Line((-1.128, 0.1), (-1.128, 0.514))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-1.128, -0.1), (-0.714, -0.1))
                Line((-1.128, -0.514), (-1.128, -0.1))
                Line((-0.714, -0.514), (-1.128, -0.514))
                Line((-0.714, -0.1), (-0.714, -0.514))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((0.714, 1.128), (1.128, 1.128))
                Line((0.714, 0.714), (0.714, 1.128))
                Line((1.128, 0.714), (0.714, 0.714))
                Line((1.128, 1.128), (1.128, 0.714))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((0.1, 0.714), (0.1, 1.128))
                Line((0.514, 0.714), (0.1, 0.714))
                Line((0.514, 1.128), (0.514, 0.714))
                Line((0.1, 1.128), (0.514, 1.128))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((1.128, 0.1), (0.714, 0.1))
                Line((1.128, 0.514), (1.128, 0.1))
                Line((0.714, 0.514), (1.128, 0.514))
                Line((0.714, 0.1), (0.714, 0.514))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((0.514, -0.1), (0.514, -0.514))
                Line((0.1, -0.1), (0.514, -0.1))
                Line((0.1, -0.514), (0.1, -0.1))
                Line((0.514, -0.514), (0.1, -0.514))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((1.128, -0.1), (1.128, -0.514))
                Line((0.714, -0.1), (1.128, -0.1))
                Line((0.714, -0.514), (0.714, -0.1))
                Line((1.128, -0.514), (0.714, -0.514))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-0.514, 0.1), (-0.514, 0.514))
                Line((-0.1, 0.1), (-0.514, 0.1))
                Line((-0.1, 0.514), (-0.1, 0.1))
                Line((-0.514, 0.514), (-0.1, 0.514))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-0.1, -1.328), (-0.1, -1.742))
                Line((-0.514, -1.328), (-0.1, -1.328))
                Line((-0.514, -1.742), (-0.514, -1.328))
                Line((-0.1, -1.742), (-0.514, -1.742))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-1.128, -1.128), (-1.128, -0.714))
                Line((-0.714, -1.128), (-1.128, -1.128))
                Line((-0.714, -0.714), (-0.714, -1.128))
                Line((-1.128, -0.714), (-0.714, -0.714))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-0.714, 0.714), (-1.128, 0.714))
                Line((-0.714, 1.128), (-0.714, 0.714))
                Line((-1.128, 1.128), (-0.714, 1.128))
                Line((-1.128, 0.714), (-1.128, 1.128))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((0.514, -0.714), (0.514, -1.128))
                Line((0.1, -0.714), (0.514, -0.714))
                Line((0.1, -1.128), (0.1, -0.714))
                Line((0.514, -1.128), (0.1, -1.128))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((1.742, -0.1), (1.742, -0.514))
                Line((1.328, -0.1), (1.742, -0.1))
                Line((1.328, -0.514), (1.328, -0.1))
                Line((1.742, -0.514), (1.328, -0.514))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((0.514, -1.328), (0.514, -1.742))
                Line((0.1, -1.328), (0.514, -1.328))
                Line((0.1, -1.742), (0.1, -1.328))
                Line((0.514, -1.742), (0.1, -1.742))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((1.742, 0.1), (1.328, 0.1))
                Line((1.742, 0.514), (1.742, 0.1))
                Line((1.328, 0.514), (1.742, 0.514))
                Line((1.328, 0.1), (1.328, 0.514))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-0.514, 0.714), (-0.514, 1.128))
                Line((-0.1, 0.714), (-0.514, 0.714))
                Line((-0.1, 1.128), (-0.1, 0.714))
                Line((-0.514, 1.128), (-0.1, 1.128))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-1.742, -0.514), (-1.742, -0.1))
                Line((-1.328, -0.514), (-1.742, -0.514))
                Line((-1.328, -0.1), (-1.328, -0.514))
                Line((-1.742, -0.1), (-1.328, -0.1))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-0.514, -0.514), (-0.514, -0.1))
                Line((-0.1, -0.514), (-0.514, -0.514))
                Line((-0.1, -0.1), (-0.1, -0.514))
                Line((-0.514, -0.1), (-0.1, -0.1))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((-0.1, -1.128), (-0.514, -1.128))
                Line((-0.1, -0.714), (-0.1, -1.128))
                Line((-0.514, -0.714), (-0.1, -0.714))
                Line((-0.514, -1.128), (-0.514, -0.714))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((0.1, 0.514), (0.514, 0.514))
                Line((0.1, 0.1), (0.1, 0.514))
                Line((0.514, 0.1), (0.1, 0.1))
                Line((0.514, 0.514), (0.514, 0.1))
            make_face()
            # Profile area: 0.171396, perimeter: 1.656
            with BuildLine():
                Line((0.514, 1.328), (0.1, 1.328))
                Line((0.514, 1.742), (0.514, 1.328))
                Line((0.1, 1.742), (0.514, 1.742))
                Line((0.1, 1.328), (0.1, 1.742))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_87155_a31e9102_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.5345833766, perimeter: 127.4277783544
            with BuildLine():
                Line((-9.3396650957, -3.5369168833), (-8.8663899118, -2.9728894826))
                CenterArc((-9.7473410214, -2.2336837315), 1.15, -40, 52.9069511683)
                CenterArc((0, 0), 8.85, -10.2924023883, 203.1993535566)
                CenterArc((9.8390873905, -1.786717471), 1.15, 169.7075976117, 50.2924023883)
                Line((9.4558266454, -3.119047502), (8.958136281, -2.5259232222))
                CenterArc((8.8046888687, -3.6654169702), 0.85, -17, 57)
                Line((9.6175479113, -3.9139329192), (7.8758767141, -9.6106827151))
                CenterArc((7.3020938605, -9.4352596923), 0.6, 163, 180)
                Line((8.3906097624, -3.8227024325), (6.7283110069, -9.2598366695))
                Line((8.3906097624, -3.8227024325), (8.247164049, -3.7788466768))
                Line((8.247164049, -3.7788466768), (6.5848652935, -9.2159809138))
                CenterArc((7.3020938605, -9.4352596923), 0.75, 163, 180)
                Line((9.7609936247, -3.9577886749), (8.0193224275, -9.6545384708))
                CenterArc((8.8046888687, -3.6654169702), 1, -17, 57)
                Line((9.5707333118, -3.0226293605), (9.0730429474, -2.4295050807))
                CenterArc((9.8390873905, -1.786717471), 1, 169.7075976117, 50.2924023883)
                CenterArc((0, 0), 9, -10.2924023883, 203.1993535566)
                CenterArc((-9.7473410214, -2.2336837315), 1, -40, 52.9069511683)
                Line((-9.4545717621, -3.4404987418), (-8.9812965783, -2.8764713412))
                CenterArc((-8.688527319, -4.0832863515), 1, 140, 55.7471343256)
                Line((-9.6509961305, -4.3546786634), (-8.1549401054, -9.660308931))
                CenterArc((-7.4330884968, -9.4567646971), 0.75, -164.2528656744, 180)
                Line((-8.1355256295, -4.2021065148), (-6.7112368882, -9.2532204632))
                Line((-8.2798959512, -4.2428153616), (-8.1355256295, -4.2021065148))
                Line((-8.2798959512, -4.2428153616), (-6.8556072099, -9.29392931))
                CenterArc((-7.4330884968, -9.4567646971), 0.6, -164.2528656744, 180)
                Line((-9.5066258087, -4.3139698166), (-8.0105697836, -9.6196000843))
                CenterArc((-8.688527319, -4.0832863515), 0.85, 140, 55.7471343256)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_87244_538fdd2d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0526545231, perimeter: 27.0176968209
            with BuildLine():
                CenterArc((0, 0), 2.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_87260_5f2a8b18_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch11 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4899160125, perimeter: 6.8833893465
            with BuildLine():
                Line((-0.1500000022, 1.9500000313), (0.0120045563, 1.9500000313))
                CenterArc((-2.566457532, 3.5403823477), 3.0294855427, -31.6660746115, 63.7620205618)
                Line((-0.1500000022, 5.1500000313), (-0.0000000163, 5.1500650722))
                Line((-0.1500000022, 1.9500000313), (-0.1500000022, 5.1500000313))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


MODELS = {
    "model_68956_2805fb2a_0000": {"func": model_68956_2805fb2a_0000, "volume": 238385.3981633974, "area": 23825.3981633974},
    "model_69058_b038ab52_0000": {"func": model_69058_b038ab52_0000, "volume": 91.3812024032, "area": 175.2836126751},
    "model_69488_f2085c68_0002": {"func": model_69488_f2085c68_0002, "volume": 21014.3032319999, "area": 42409.9008},
    "model_69816_c51ea7d9_0000": {"func": model_69816_c51ea7d9_0000, "volume": 55.1534015951, "area": 256.7357587202},
    "model_70169_914780d4_0011": {"func": model_70169_914780d4_0011, "volume": 0.7837721819, "area": 10.2328992226},
    "model_70188_002060a2_0001": {"func": model_70188_002060a2_0001, "volume": 1.4399666289, "area": 12.6100677053},
    "model_70214_7e7a1219_0000": {"func": model_70214_7e7a1219_0000, "volume": 36.6780128588, "area": 161.8927876323},
    "model_70355_e5f58cd5_0000": {"func": model_70355_e5f58cd5_0000, "volume": 4770000, "area": 696000},
    "model_71444_50b4c168_0001": {"func": model_71444_50b4c168_0001, "volume": 115.563042441, "area": 232.432015859},
    "model_71444_50b4c168_0003": {"func": model_71444_50b4c168_0003, "volume": 1.9165254613, "area": 13.2777983033},
    "model_71833_9b2c8d39_0000": {"func": model_71833_9b2c8d39_0000, "volume": 150.420972619, "area": 461.838627208},
    "model_72966_11b78e5e_0001": {"func": model_72966_11b78e5e_0001, "volume": 45.7394780883, "area": 194.9003966014},
    "model_73081_906f09d5_0000": {"func": model_73081_906f09d5_0000, "volume": 42, "area": 134.5},
    "model_73388_10a40b49_0027": {"func": model_73388_10a40b49_0027, "volume": 5.1024955362, "area": 38.7300175578},
    "model_73806_a694a87d_0001": {"func": model_73806_a694a87d_0001, "volume": 1410.5615007629, "area": 1977.9748110058},
    "model_73906_ca7def41_0001": {"func": model_73906_ca7def41_0001, "volume": 48.120312685, "area": 109.7343352136},
    "model_74281_623219a4_0000": {"func": model_74281_623219a4_0000, "volume": 208.32, "area": 283.328},
    "model_75646_4baf69b2_0002": {"func": model_75646_4baf69b2_0002, "volume": 71.0728631773, "area": 218.7772218692},
    "model_75966_08c4ab3e_0001": {"func": model_75966_08c4ab3e_0001, "volume": 1223.8307868666, "area": 1107.5444218399},
    "model_76298_af8ea172_0004": {"func": model_76298_af8ea172_0004, "volume": 0.0354832976, "area": 0.8454224117},
    "model_76298_af8ea172_0011": {"func": model_76298_af8ea172_0011, "volume": 0.1384690888, "area": 2.1121522268},
    "model_76880_9bb28e72_0003": {"func": model_76880_9bb28e72_0003, "volume": 25.4688916427, "area": 59.8787559774},
    "model_76969_10fcc619_0000": {"func": model_76969_10fcc619_0000, "volume": 325.3549446715, "area": 652.289647542},
    "model_77001_aa7c50ef_0003": {"func": model_77001_aa7c50ef_0003, "volume": 3.2553254946, "area": 40.2906945613},
    "model_77665_e2629513_0001": {"func": model_77665_e2629513_0001, "volume": 3.4822033369, "area": 17.17261224},
    "model_77666_ba753255_0001": {"func": model_77666_ba753255_0001, "volume": 0.881632271, "area": 7.3539280332},
    "model_77976_300b479c_0000": {"func": model_77976_300b479c_0000, "volume": 140.6205444225, "area": 619.3052923855},
    "model_78075_e8f2196e_0002": {"func": model_78075_e8f2196e_0002, "volume": 0.3590565517, "area": 5.7946927646},
    "model_78091_0b1734e4_0000": {"func": model_78091_0b1734e4_0000, "volume": 650, "area": 570},
    "model_78098_0810099f_0000": {"func": model_78098_0810099f_0000, "volume": 153.4165917794, "area": 296.7688459989},
    "model_78422_3d6c0e4e_0005": {"func": model_78422_3d6c0e4e_0005, "volume": 316, "area": 528},
    "model_78603_4720dcb8_0000": {"func": model_78603_4720dcb8_0000, "volume": 0.4665265091, "area": 3.6285395149},
    "model_78603_4720dcb8_0002": {"func": model_78603_4720dcb8_0002, "volume": 0.0473184039, "area": 1.9516621063},
    "model_78603_4720dcb8_0004": {"func": model_78603_4720dcb8_0004, "volume": 0.009424778, "area": 0.408407045},
    "model_78608_6fed6de8_0000": {"func": model_78608_6fed6de8_0000, "volume": 2.3867641563, "area": 12.7976418569},
    "model_78608_6fed6de8_0001": {"func": model_78608_6fed6de8_0001, "volume": 0.2643078986, "area": 2.920827977},
    "model_78608_6fed6de8_0002": {"func": model_78608_6fed6de8_0002, "volume": 0.0525903954, "area": 2.2731332539},
    "model_78608_6fed6de8_0003": {"func": model_78608_6fed6de8_0003, "volume": 0.1321536235, "area": 1.9009275011},
    "model_78608_6fed6de8_0004": {"func": model_78608_6fed6de8_0004, "volume": 3.5651693184, "area": 17.6628782835},
    "model_78687_f22479b6_0005": {"func": model_78687_f22479b6_0005, "volume": 1157.64, "area": 1370.6},
    "model_78773_06275eba_0000": {"func": model_78773_06275eba_0000, "volume": 0.0077763149, "area": 1.0432162951},
    "model_78773_06275eba_0001": {"func": model_78773_06275eba_0001, "volume": 1.6956788972, "area": 16.2453154923},
    "model_78773_06275eba_0003": {"func": model_78773_06275eba_0003, "volume": 0.2100906343, "area": 5.827817982},
    "model_78773_06275eba_0010": {"func": model_78773_06275eba_0010, "volume": 0.0070538545, "area": 0.9900484039},
    "model_78972_71d3bfef_0000": {"func": model_78972_71d3bfef_0000, "volume": 23.0665880776, "area": 133.6507970162},
    "model_78973_5f3ba6bc_0000": {"func": model_78973_5f3ba6bc_0000, "volume": 2562.2226495188, "area": 1307.3380490994},
    "model_78979_6c732414_0000": {"func": model_78979_6c732414_0000, "volume": 2559.8029948995, "area": 1772.5987379872},
    "model_78981_9684a26f_0000": {"func": model_78981_9684a26f_0000, "volume": 245.8791965989, "area": 332.5897899155},
    "model_78988_182be740_0000": {"func": model_78988_182be740_0000, "volume": 173.1158473949, "area": 228.6479648152},
    "model_78991_64d81333_0000": {"func": model_78991_64d81333_0000, "volume": 11078.836538229, "area": 6218.5120010665},
    "model_79094_4872079c_0000": {"func": model_79094_4872079c_0000, "volume": 239.8595534433, "area": 328.9880462888},
    "model_79097_9e06d5f8_0000": {"func": model_79097_9e06d5f8_0000, "volume": 49.0319367947, "area": 113.5614146566},
    "model_79098_6d4d6157_0000": {"func": model_79098_6d4d6157_0000, "volume": 82.9729824316, "area": 332.834580476},
    "model_79207_77757b86_0001": {"func": model_79207_77757b86_0001, "volume": 2785.8114865742, "area": 1838.1869386141},
    "model_79423_62db5fc6_0007": {"func": model_79423_62db5fc6_0007, "volume": 1.1812388377, "area": 10.0688044548},
    "model_79693_9396219b_0001": {"func": model_79693_9396219b_0001, "volume": 1.3945662936, "area": 8.8733329779},
    "model_79998_13b5563b_0000": {"func": model_79998_13b5563b_0000, "volume": 35.0672274602, "area": 122.7218189089},
    "model_80189_5bbbf853_0000": {"func": model_80189_5bbbf853_0000, "volume": 117.4512065101, "area": 182.9420380009},
    "model_80191_ac61cdc4_0000": {"func": model_80191_ac61cdc4_0000, "volume": 174.1067221036, "area": 259.1094283707},
    "model_80192_c2f08a97_0000": {"func": model_80192_c2f08a97_0000, "volume": 219.4583585444, "area": 651.6315470758},
    "model_80760_3ac12cd8_0000": {"func": model_80760_3ac12cd8_0000, "volume": 1416.1430480564, "area": 878.9473580154},
    "model_81029_104dff26_0000": {"func": model_81029_104dff26_0000, "volume": 51.3157084378, "area": 124.0267884889},
    "model_81029_5cd05f84_0001": {"func": model_81029_5cd05f84_0001, "volume": 60.0964210575, "area": 140.4378177273},
    "model_81975_26c061f9_0000": {"func": model_81975_26c061f9_0000, "volume": 91843.598442158, "area": 40585.1904149457},
    "model_81996_b3752ed2_0000": {"func": model_81996_b3752ed2_0000, "volume": 2500, "area": 2325},
    "model_82012_c533307b_0002": {"func": model_82012_c533307b_0002, "volume": 39.7348638826, "area": 101.771894013},
    "model_82012_c533307b_0003": {"func": model_82012_c533307b_0003, "volume": 57.1804168039, "area": 266.3527404487},
    "model_82146_ba68ced6_0000": {"func": model_82146_ba68ced6_0000, "volume": 15.0686159482, "area": 77.1387989884},
    "model_82203_8b9714ce_0000": {"func": model_82203_8b9714ce_0000, "volume": 0.0021027233, "area": 0.254028722},
    "model_82377_8e929ad6_0000": {"func": model_82377_8e929ad6_0000, "volume": 0.039623064, "area": 0.861973275},
    "model_82614_a8ef3280_0001": {"func": model_82614_a8ef3280_0001, "volume": 0.3498948783, "area": 14.0429192306},
    "model_82614_a8ef3280_0018": {"func": model_82614_a8ef3280_0018, "volume": 0.233612037, "area": 2.6072018791},
    "model_82614_a8ef3280_0019": {"func": model_82614_a8ef3280_0019, "volume": 0.0010210176, "area": 0.1130973355},
    "model_82760_61e37ad2_0000": {"func": model_82760_61e37ad2_0000, "volume": 17.6714586764, "area": 37.6991118431},
    "model_83101_df904768_0000": {"func": model_83101_df904768_0000, "volume": 12036.2342576164, "area": 9099.4888151415},
    "model_83106_8e9f36f3_0000": {"func": model_83106_8e9f36f3_0000, "volume": 53.4995743324, "area": 117.8586691259},
    "model_83110_487f8396_0000": {"func": model_83110_487f8396_0000, "volume": 1.7121679962, "area": 8.7964594301},
    "model_83220_c8e6b276_0000": {"func": model_83220_c8e6b276_0000, "volume": 4538.2267001608, "area": 2127.0291248895},
    "model_83239_1a00d111_0000": {"func": model_83239_1a00d111_0000, "volume": 53.1083736521, "area": 255.7162555352},
    "model_83378_2dc861a1_0002": {"func": model_83378_2dc861a1_0002, "volume": 1484.963344857, "area": 2023.2071272644},
    "model_83392_50368ba2_0000": {"func": model_83392_50368ba2_0000, "volume": 4.375, "area": 23.5},
    "model_83395_4c74f86e_0000": {"func": model_83395_4c74f86e_0000, "volume": 335.9540643933, "area": 291.6717155069},
    "model_83396_fdb2987a_0000": {"func": model_83396_fdb2987a_0000, "volume": 15.4880513777, "area": 87.3447595336},
    "model_83411_51aa29e1_0000": {"func": model_83411_51aa29e1_0000, "volume": 1060.2875205866, "area": 1555.0883635269},
    "model_83421_0bbb503e_0000": {"func": model_83421_0bbb503e_0000, "volume": 0.9801769079, "area": 22.0539804282},
    "model_83432_a7f85698_0000": {"func": model_83432_a7f85698_0000, "volume": 9.6768169843, "area": 47.4226314742},
    "model_83432_a7f85698_0002": {"func": model_83432_a7f85698_0002, "volume": 2.8274333882, "area": 11.6867246714},
    "model_84608_204c01e6_0003": {"func": model_84608_204c01e6_0003, "volume": 43.9874336294, "area": 236.9884955592},
    "model_84608_204c01e6_0004": {"func": model_84608_204c01e6_0004, "volume": 0.0415868328, "area": 1.1089822067},
    "model_85195_c6ef0067_0001": {"func": model_85195_c6ef0067_0001, "volume": 14.3837715079, "area": 45.5811050004},
    "model_85195_c6ef0067_0004": {"func": model_85195_c6ef0067_0004, "volume": 291.6968778858, "area": 284.3141351499},
    "model_85552_3669d6cf_0001": {"func": model_85552_3669d6cf_0001, "volume": 0.1594054192, "area": 5.4012167695},
    "model_85617_4879c1a8_0001": {"func": model_85617_4879c1a8_0001, "volume": 0.6487768873, "area": 6.4627994478},
    "model_86186_a116ac82_0000": {"func": model_86186_a116ac82_0000, "volume": 312.3784075, "area": 294.1890379098},
    "model_86296_8a6ed4d3_0010": {"func": model_86296_8a6ed4d3_0010, "volume": 0.8302714215, "area": 7.5746014499},
    "model_86384_a3b5cf5e_0001": {"func": model_86384_a3b5cf5e_0001, "volume": 265.6609287692, "area": 548.6006171331},
    "model_86386_ce62c3a1_0004": {"func": model_86386_ce62c3a1_0004, "volume": 1235.0386119425, "area": 1036.7255756846},
    "model_86497_3288c394_0000": {"func": model_86497_3288c394_0000, "volume": 8741.3565927115, "area": 6942.1311879172},
    "model_86503_9c214425_0000": {"func": model_86503_9c214425_0000, "volume": 161.3689071093, "area": 230.4972226256},
    "model_86586_ee75152f_0000": {"func": model_86586_ee75152f_0000, "volume": 48.5773297979, "area": 183.194950515},
    "model_86801_40091568_0000": {"func": model_86801_40091568_0000, "volume": 69.6796849149, "area": 423.7437061436},
    "model_87155_a31e9102_0000": {"func": model_87155_a31e9102_0000, "volume": 28.6037501297, "area": 401.3525018162},
    "model_87244_538fdd2d_0000": {"func": model_87244_538fdd2d_0000, "volume": 2.0263272616, "area": 21.6141574567},
    "model_87260_5f2a8b18_0000": {"func": model_87260_5f2a8b18_0000, "volume": 0.7449580062, "area": 6.4215266982},
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
