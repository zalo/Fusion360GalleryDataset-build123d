"""Batch 002 - passing/06_11to15ops
51 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_143263_b168ae22_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 157.0796326795, perimeter: 51.4159265359
            with BuildLine():
                Line((0, 15), (20, 15))
                CenterArc((10, 15), 10, -180, 180)
            make_face()
            # Profile area: 157.0796326795, perimeter: 51.4159265359
            with BuildLine():
                CenterArc((10, 15), 10, 0, 180)
                Line((0, 15), (20, 15))
            make_face()
            # Profile area: 157.0796326795, perimeter: 51.4159265359
            with BuildLine():
                Line((0, -15), (20, -15))
                CenterArc((10, -15), 10, -180, 180)
            make_face()
            # Profile area: 142.9203673205, perimeter: 81.4159265359
            with BuildLine():
                Line((20, 0), (0, 0))
                Line((0, 0), (0, -15))
                CenterArc((10, -15), 10, 0, 180)
                Line((20, -15), (20, 0))
            make_face()
            # Profile area: 142.9203673205, perimeter: 81.4159265359
            with BuildLine():
                CenterArc((10, 15), 10, -180, 180)
                Line((0, 0), (0, 15))
                Line((20, 0), (0, 0))
                Line((20, 15), (20, 0))
            make_face()
            # Profile area: 157.0796326795, perimeter: 51.4159265359
            with BuildLine():
                CenterArc((10, -15), 10, 0, 180)
                Line((0, -15), (20, -15))
            make_face()
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 90, perimeter: 66
            with BuildLine():
                Line((15, 2), (-15, 2))
                Line((15, 5), (15, 2))
                Line((-15, 5), (15, 5))
                Line((-15, 2), (-15, 5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -15, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))) as sk:
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((0, 2), (-3, 2))
                Line((0, 5), (0, 2))
                Line((-3, 5), (0, 5))
                Line((-3, 2), (-3, 5))
            make_face()
        # TwoSides extrude, along=15, against=-45
        extrude(amount=15, mode=Mode.ADD)
        extrude(sk.sketch, amount=-45, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 90, perimeter: 66
            with BuildLine():
                Line((15, 2), (-15, 2))
                Line((15, 5), (15, 2))
                Line((-15, 5), (15, 5))
                Line((-15, 2), (-15, 5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -15, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))) as sk:
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((23, 2), (20, 2))
                Line((23, 5), (23, 2))
                Line((20, 5), (23, 5))
                Line((20, 2), (20, 5))
            make_face()
        # TwoSides extrude, along=15, against=-45
        extrude(amount=15, mode=Mode.ADD)
        extrude(sk.sketch, amount=-45, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 8.6095032974, perimeter: 11.3377450763
            with BuildLine():
                CenterArc((1.5, -30), 3, 60, 60)
                Line((0, -27.4019237886), (0, -30))
                Line((0, -30), (3, -30))
                Line((3, -30), (3, -27.4019237886))
            make_face()
            # Profile area: 19.6648305849, perimeter: 23.9041156907
            with BuildLine():
                Line((3, -30), (3, -27.4019237886))
                Line((0, -30), (3, -30))
                Line((0, -27.4019237886), (0, -30))
                CenterArc((1.5, -30), 3, 120, 300)
            make_face()
            # Profile area: 8.6095032974, perimeter: 11.3377450763
            with BuildLine():
                CenterArc((-21.5, -30), 3, 60, 60)
                Line((-23, -27.4019237886), (-23, -30))
                Line((-23, -30), (-20, -30))
                Line((-20, -30), (-20, -27.4019237886))
            make_face()
            # Profile area: 19.6648305849, perimeter: 23.9041156907
            with BuildLine():
                Line((-20, -30), (-20, -27.4019237886))
                Line((-23, -30), (-20, -30))
                Line((-23, -27.4019237886), (-23, -30))
                CenterArc((-21.5, -30), 3, 120, 300)
            make_face()
            # Profile area: 19.6648305849, perimeter: 23.9041156907
            with BuildLine():
                Line((-23, 30), (-23, 27.4019237886))
                Line((-20, 30), (-23, 30))
                Line((-20, 27.4019237886), (-20, 30))
                CenterArc((-21.5, 30), 3, -60, 300)
            make_face()
            # Profile area: 8.6095032974, perimeter: 11.3377450763
            with BuildLine():
                CenterArc((-21.5, 30), 3, -120, 60)
                Line((-20, 27.4019237886), (-20, 30))
                Line((-20, 30), (-23, 30))
                Line((-23, 30), (-23, 27.4019237886))
            make_face()
            # Profile area: 19.6648305849, perimeter: 23.9041156907
            with BuildLine():
                CenterArc((1.5, 30), 3, -60, 300)
                Line((0, 30), (0, 27.4019237886))
                Line((3, 30), (0, 30))
                Line((3, 27.4019237886), (3, 30))
            make_face()
            # Profile area: 8.6095032974, perimeter: 11.3377450763
            with BuildLine():
                Line((3, 27.4019237886), (3, 30))
                Line((3, 30), (0, 30))
                Line((0, 30), (0, 27.4019237886))
                CenterArc((1.5, 30), 3, -120, 60)
            make_face()
        # TwoSides extrude, along=2, against=-5
        extrude(amount=2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-5, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-10, -3)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((10, -3)):
                Circle(1)
        # TwoSides extrude, along=2, against=-22
        extrude(amount=2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-22, mode=Mode.ADD)
    return part.part


def model_143346_695aab70_0000():
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
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((-15, 0)):
                Circle(4)
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            Circle(7.5)
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((15, 0)):
                Circle(4)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((15, 0)):
                Circle(2.5)
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-15, 0)):
                Circle(2.5)
        # OneSide extrude, distance=-5.6463
        extrude(amount=-5.6463, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10, perimeter: 14
            with BuildLine():
                Line((16, 1), (21, 1))
                Line((16, -1), (16, 1))
                Line((21, -1), (16, -1))
                Line((21, 1), (21, -1))
            make_face()
            # Profile area: 9.1100055053, perimeter: 13.1100055053
            with BuildLine():
                Line((-21, 1), (-16.4449972474, 1))
                Line((-21, -1), (-21, 1))
                Line((-16.4449972474, -1), (-21, -1))
                Line((-16.4449972474, 1), (-16.4449972474, -1))
            make_face()
        # OneSide extrude, distance=-3.9931
        extrude(amount=-3.9931, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 65.8741713975, perimeter: 74.0159229186
            with BuildLine():
                CenterArc((0, 0), 6.78, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.7768614339, perimeter: 46.9209905302
            with BuildLine():
                CenterArc((0, 0), 7.5, 127.0873024076, 106.3571092126)
                _nurbs_edge([(-15, 4), (-14.7937358045, 3.9662893002), (-14.3809158172, 3.9053882118), (-13.760811047, 3.833597522), (-12.932226328, 3.7776420282), (-11.8933348209, 3.7783712244), (-10.8510179432, 3.8556942635), (-9.8050235406, 4.0152495064), (-8.7552650879, 4.2589717199), (-7.7019456938, 4.58231924), (-6.6453575481, 4.9787584864), (-5.7976980319, 5.3493296975), (-5.160696754, 5.6553575334), (-4.7354798956, 5.871659737), (-4.522734124, 5.9828819179)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-15, -4), (-14.7272875404, -3.8414350638), (-14.2056979957, -3.5241797653), (-13.494817708, -3.0479205499), (-12.6923562332, -2.4121432519), (-11.9480047995, -1.6160601679), (-11.4854345762, -0.8184942987), (-11.3275373514, -0.0193251834), (-11.4866208794, 0.7815119438), (-11.9499147476, 1.5839498826), (-12.6943706419, 2.3878673483), (-13.4963639683, 3.0320875868), (-14.2065882343, 3.5158249193), (-14.7276065751, 3.838566615), (-15, 4)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-15, -4), (-14.79355945, -3.9657157102), (-14.3803029048, -3.9038012633), (-13.7592917477, -3.8308920462), (-12.9289871602, -3.7742610098), (-11.8870374518, -3.775587884), (-10.8406796543, -3.8550406679), (-9.7895919882, -4.0183223558), (-8.7336696638, -4.2672901697), (-7.6731783116, -4.5972362579), (-6.6084950711, -5.0014764641), (-5.753685837, -5.3791487613), (-5.1109680982, -5.6909519189), (-4.6817854437, -5.9113007694), (-4.4670180661, -6.0245953887)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 45.5847775829, perimeter: 45.9521648752
            with BuildLine():
                _nurbs_edge([(14.3055087555, 3.9011030441), (14.2378353477, 3.8929249663), (13.9633832928, 3.8612041031), (13.481688425, 3.8158401555), (12.7917992175, 3.777127244), (11.8921784057, 3.777852072), (10.8491221728, 3.8555660937), (9.8021965101, 4.0158071233), (8.751311353, 4.2604960547), (7.6966810762, 4.585060717), (6.6386133186, 4.9829398013), (5.7896469531, 5.3548222802), (5.1516007804, 5.6619168621), (4.7256590175, 5.8789666293), (4.5125437161, 5.9905716931)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0672618648, 0.0672618648, 0.0672618648, 0.0672618648, 0.0672618648, 0.0672618648, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 7.5, -53.3950865446, 106.4053110903)
                _nurbs_edge([(15, -4), (14.7935755922, -3.9657683789), (14.3803591671, -3.9039469304), (13.7594316976, -3.83114019), (12.9292864795, -3.7745705666), (11.8876208612, -3.7758412565), (10.8416389486, -3.8550966747), (9.7910254162, -4.0180339657), (8.7356770619, -4.2665177399), (7.675853603, -4.5958555471), (6.6119242242, -4.9993771371), (5.7577807951, -5.3763956276), (5.1155953801, -5.6876672053), (4.6867820206, -5.907643654), (4.4722028938, -6.020747568)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(15, -4), (14.7659380898, -3.9312547879), (14.3166003135, -3.7861813596), (13.6989509978, -3.5458226726), (12.9889594316, -3.1795124756), (12.2949999011, -2.6444386731), (11.7988925974, -2.0332323056), (11.5020957065, -1.3510018829), (11.4002199396, -0.6090449388), (11.478343415, 0.1718983456), (11.7089140324, 0.9605112203), (12.0581358248, 1.7203516097), (12.4901473222, 2.4138874927), (12.9715726199, 3.0071452924), (13.4380339938, 3.4394769916), (13.8080307385, 3.6872117366), (14.0759568371, 3.8177806022), (14.2416464286, 3.8799192916), (14.3055087555, 3.9011030441)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9085334278, 0.9085334278, 0.9085334278, 0.9085334278, 0.9085334278, 0.9085334278], 5)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


def model_143718_b25c8fd0_0004():
    """Model: Screw Spindle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # OneSide extrude, distance=15.7
        extrude(amount=15.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.8419229241, perimeter: 32.358404332
            with BuildLine():
                CenterArc((0, 0), 3.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 22.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0.0203018006, 19.2)):
                Circle(0.6)
        # Symmetric extrude, each_side=3.5
        extrude(amount=3.5, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_145702_e28c737e_0022():
    """Model: ????_L50x50x6txL988 v3"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((5, -5), (0, -5))
                Line((5, 0), (5, -5))
                Line((0, 0), (5, 0))
                Line((0, -5), (0, 0))
            make_face()
        # OneSide extrude, distance=98.8
        extrude(amount=98.8)

        # Sketch2 -> 押し出し2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 19.36, perimeter: 17.6
            with BuildLine():
                Line((0.6, 5), (0.6, 0.6))
                Line((0.6, 0.6), (5, 0.6))
                Line((5, 0.6), (5, 5))
                Line((5, 5), (0.6, 5))
            make_face()
        # OneSide extrude, distance=-1000
        extrude(amount=-1000, mode=Mode.SUBTRACT)

        # Sketch7 -> 押し出し4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3, perimeter: 11.2
            with BuildLine():
                Line((5, 0.6), (0.6, 0.6))
                Line((0.6, 0.6), (0, 0.6))
                Line((0, 0.6), (0, 0))
                Line((0, 0), (5, 0))
                Line((5, 0), (5, 0.6))
            make_face()
            # Profile area: 19.36, perimeter: 17.6
            with BuildLine():
                Line((0.6, 0.6), (0.6, 5))
                Line((5, 0.6), (0.6, 0.6))
                Line((5, 5), (5, 0.6))
                Line((0.6, 5), (5, 5))
            make_face()
        # OneSide extrude, distance=-4.4
        extrude(amount=-4.4, mode=Mode.SUBTRACT)

        # Sketch8 -> 押し出し5 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 98.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3, perimeter: 11.2
            with BuildLine():
                Line((-5, 0.6), (-0.6, 0.6))
                Line((-5, 0), (-5, 0.6))
                Line((0, 0), (-5, 0))
                Line((0, 0.6), (0, 0))
                Line((-0.6, 0.6), (0, 0.6))
            make_face()
            # Profile area: 19.36, perimeter: 17.6
            with BuildLine():
                Line((-0.6, 0.6), (-0.6, 5))
                Line((-0.6, 5), (-5, 5))
                Line((-5, 5), (-5, 0.6))
                Line((-5, 0.6), (-0.6, 0.6))
            make_face()
        # OneSide extrude, distance=-4.4
        extrude(amount=-4.4, mode=Mode.SUBTRACT)
    return part.part


def model_146159_f3f80701_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11, perimeter: 45
            with BuildLine():
                Line((-0.5, -9.5), (-0.5, 0))
                Line((12.5, -9.5), (-0.5, -9.5))
                Line((12.5, -9), (12.5, -9.5))
                Line((12, -9), (12.5, -9))
                Line((12, -9), (0, -9))
                Line((0, -9), (0, 0))
                Line((0, 0), (-0.5, 0))
            make_face()
            # Profile area: 11, perimeter: 45
            with BuildLine():
                Line((0, 0), (-0.5, 0))
                Line((0, 0), (12, 0))
                Line((12, 0), (12, -9))
                Line((12, -9), (12.5, -9))
                Line((12.5, 0.5), (12.5, -9))
                Line((-0.5, 0.5), (12.5, 0.5))
                Line((-0.5, 0), (-0.5, 0.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.825, perimeter: 20.9401219467
            with BuildLine():
                Line((0.15, 0), (0, 0))
                Line((0, 0), (0, 9))
                Line((0, 9), (0.15, 9))
                Line((0.15, 9), (-0.5, 9.5))
                Line((-0.5, 9.5), (-0.5, -0.5))
                Line((0.15, 0), (-0.5, -0.5))
            make_face()
            # Profile area: 6.175, perimeter: 26.3401219467
            with BuildLine():
                Line((0.15, 9), (11.85, 9))
                Line((12.5, 9.5), (11.85, 9))
                Line((12.5, 9.5), (-0.5, 9.5))
                Line((0.15, 9), (-0.5, 9.5))
            make_face()
            # Profile area: 4.825, perimeter: 20.9401219467
            with BuildLine():
                Line((12.5, -0.5), (11.85, 0))
                Line((12.5, -0.5), (12.5, 9.5))
                Line((12.5, 9.5), (11.85, 9))
                Line((11.85, 9), (12, 9))
                Line((12, 9), (12, 0))
                Line((12, 0), (11.85, 0))
            make_face()
            # Profile area: 6.175, perimeter: 26.3401219467
            with BuildLine():
                Line((0.15, 0), (-0.5, -0.5))
                Line((-0.5, -0.5), (12.5, -0.5))
                Line((12.5, -0.5), (11.85, 0))
                Line((11.85, 0), (0.15, 0))
            make_face()
            # Profile area: 27.675, perimeter: 24.0610975202
            with BuildLine():
                Line((6, 4.5), (0.15, 0))
                Line((6, 4.5), (0.15, 9))
                Line((0, 9), (0.15, 9))
                Line((0, 0), (0, 9))
                Line((0.15, 0), (0, 0))
            make_face()
            # Profile area: 26.325, perimeter: 26.4610975202
            with BuildLine():
                Line((11.85, 0), (0.15, 0))
                Line((11.85, 0), (6, 4.5))
                Line((6, 4.5), (0.15, 0))
            make_face()
            # Profile area: 27.675, perimeter: 24.0610975202
            with BuildLine():
                Line((11.85, 0), (6, 4.5))
                Line((12, 0), (11.85, 0))
                Line((12, 9), (12, 0))
                Line((11.85, 9), (12, 9))
                Line((11.85, 9), (6, 4.5))
            make_face()
            # Profile area: 26.325, perimeter: 26.4610975202
            with BuildLine():
                Line((11.85, 9), (6, 4.5))
                Line((0.15, 9), (11.85, 9))
                Line((6, 4.5), (0.15, 9))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-4.3, 2), (-4.3, 2.5))
                Line((-4.3, 2.5), (-4.3, 3))
                Line((-4.3, 3), (-5.3, 3))
                Line((-5.3, 3), (-5.3, 2))
                Line((-5.3, 2), (-4.3, 2))
            make_face()
        # OneSide extrude, distance=3.9
        extrude(amount=3.9, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(12, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((4.3, 2.5), (4.3, 3))
                Line((4.3, 2), (4.3, 2.5))
                Line((5.3, 2), (4.3, 2))
                Line((5.3, 3), (5.3, 2))
                Line((4.3, 3), (5.3, 3))
            make_face()
        # OneSide extrude, distance=3.9
        extrude(amount=3.9, mode=Mode.ADD)
    return part.part


def model_146284_12cd9232_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.8, perimeter: 23.2
            with BuildLine():
                Line((0, 3.6), (0, 0))
                Line((0, 0), (8, 0))
                Line((8, 0), (8, 3.6))
                Line((8, 3.6), (0, 3.6))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                Line((-7.88, -3.33), (-7.73, -3.33))
                Line((-7.73, -3.48), (-7.73, -3.33))
                CenterArc((-7.73, -3.33), 0.15, -90, 270)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                CenterArc((-7.73, -3.33), 0.15, 180, 90)
                Line((-7.73, -3.48), (-7.73, -3.33))
                Line((-7.88, -3.33), (-7.73, -3.33))
            make_face()
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.27, -3.33)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.27, -0.27)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-7.73, -0.27)):
                Circle(0.15)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 17.4685, perimeter: 19.16
            with BuildLine():
                Line((-7.6, -3), (-7.6, -0.55))
                Line((-0.47, -3), (-7.6, -3))
                Line((-0.47, -0.55), (-0.47, -3))
                Line((-7.6, -0.55), (-0.47, -0.55))
            make_face()
        # OneSide extrude, distance=0.71
        extrude(amount=0.71, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.301, perimeter: 2.7981465578
            with BuildLine():
                Line((-7.95, -1.8), (-7.95, -2.025))
                Line((-7.95, -2.025), (-7.6, -2.435))
                Line((-7.6, -2.435), (-7.6, -1.8))
                Line((-7.6, -1.165), (-7.6, -1.8))
                Line((-7.95, -1.575), (-7.6, -1.165))
                Line((-7.95, -1.8), (-7.95, -1.575))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0006097561, perimeter: 0.1186341634
            with BuildLine():
                Line((0.763125, -3.4493902439), (0.788125, -3.425))
                Line((0.788125, -3.425), (0.763125, -3.4006097561))
                Line((0.763125, -3.4493902439), (0.763125, -3.4006097561))
            make_face()
            # Profile area: 0.0006402439, perimeter: 0.1210731878
            with BuildLine():
                Line((0.763125, -3.45), (0.763125, -3.4493902439))
                Line((0.813125, -3.45), (0.763125, -3.45))
                Line((0.813125, -3.4493902439), (0.813125, -3.45))
                Line((0.813125, -3.4493902439), (0.788125, -3.425))
                Line((0.763125, -3.4493902439), (0.788125, -3.425))
            make_face()
            # Profile area: 0.0006402439, perimeter: 0.1210731878
            with BuildLine():
                Line((0.788125, -3.425), (0.763125, -3.4006097561))
                Line((0.788125, -3.425), (0.813125, -3.4006097561))
                Line((0.813125, -3.4), (0.813125, -3.4006097561))
                Line((0.763125, -3.4), (0.813125, -3.4))
                Line((0.763125, -3.4006097561), (0.763125, -3.4))
            make_face()
            # Profile area: 0.0006097561, perimeter: 0.1186341634
            with BuildLine():
                Line((0.813125, -3.4006097561), (0.813125, -3.4493902439))
                Line((0.788125, -3.425), (0.813125, -3.4006097561))
                Line((0.813125, -3.4493902439), (0.788125, -3.425))
            make_face()
        # OneSide extrude, distance=0.84
        extrude(amount=0.84, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0154058689, perimeter: 0.5869268995
            with BuildLine():
                Line((0.66, -3.55), (0.763125, -3.4493902439))
                Line((0.763125, -3.4493902439), (0.763125, -3.4006097561))
                Line((0.763125, -3.4006097561), (0.66, -3.3))
                Line((0.66, -3.3), (0.66, -3.55))
            make_face()
            # Profile area: 0.0154058689, perimeter: 0.5869268995
            with BuildLine():
                Line((0.813125, -3.4006097561), (0.91625, -3.3))
                Line((0.813125, -3.4006097561), (0.813125, -3.4493902439))
                Line((0.91625, -3.55), (0.813125, -3.4493902439))
                Line((0.91625, -3.55), (0.91625, -3.3))
            make_face()
            # Profile area: 0.0153753811, perimeter: 0.5956159239
            with BuildLine():
                Line((0.66, -3.55), (0.91625, -3.55))
                Line((0.91625, -3.55), (0.813125, -3.4493902439))
                Line((0.813125, -3.4493902439), (0.813125, -3.45))
                Line((0.813125, -3.45), (0.763125, -3.45))
                Line((0.763125, -3.45), (0.763125, -3.4493902439))
                Line((0.66, -3.55), (0.763125, -3.4493902439))
            make_face()
            # Profile area: 0.0153753811, perimeter: 0.5956159239
            with BuildLine():
                Line((0.763125, -3.4006097561), (0.66, -3.3))
                Line((0.763125, -3.4006097561), (0.763125, -3.4))
                Line((0.763125, -3.4), (0.813125, -3.4))
                Line((0.813125, -3.4), (0.813125, -3.4006097561))
                Line((0.813125, -3.4006097561), (0.91625, -3.3))
                Line((0.91625, -3.3), (0.66, -3.3))
            make_face()
        # OneSide extrude, distance=0.24
        extrude(amount=0.24, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.86), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.3525, perimeter: 15.8
            with BuildLine():
                Line((-0.81, -2.5), (-7.26, -2.5))
                Line((-0.81, -1.05), (-0.81, -2.5))
                Line((-7.26, -1.05), (-0.81, -1.05))
                Line((-7.26, -2.5), (-7.26, -1.05))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_20535_f2420e23_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch11 -> Extrude9 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6974097914, perimeter: 4.8497422612
            with BuildLine():
                Line((-4.5958548116, 0.7), (-5.4041451884, 0.7))
                Line((-5.4041451884, 0.7), (-5.8082903769, 0))
                Line((-5.8082903769, 0), (-5.4041451884, -0.7))
                Line((-5.4041451884, -0.7), (-4.5958548116, -0.7))
                Line((-4.5958548116, -0.7), (-4.1917096231, 0))
                Line((-4.1917096231, 0), (-4.5958548116, 0.7))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch13 -> Extrude10 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4243524479, perimeter: 2.4248711306
            with BuildLine():
                Line((-2.2979274058, 0.35), (-2.7020725942, 0.35))
                Line((-2.7020725942, 0.35), (-2.9041451884, 0))
                Line((-2.9041451884, 0), (-2.7020725942, -0.35))
                Line((-2.7020725942, -0.35), (-2.2979274058, -0.35))
                Line((-2.2979274058, -0.35), (-2.0958548116, 0))
                Line((-2.0958548116, 0), (-2.2979274058, 0.35))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch14 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5, 0)):
                Circle(0.25)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch15 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.45), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.086393798, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((-2.5, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5, 0)):
                Circle(0.25)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch16 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.5, 0)):
                Circle(0.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch17 -> Extrude14 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((2.5, 0)):
                Circle(0.02)
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.SUBTRACT)
    return part.part


def model_21237_7887a24b_0014():
    """Model: Line Guide Drive Shaft v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=4.42
        extrude(amount=4.42)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.42), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.132555575, perimeter: 2.4661502331
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.54
        extrude(amount=-0.54, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.88
        extrude(amount=-0.88, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0215984495, perimeter: 1.7278759595
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.22
        extrude(amount=-0.22, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0136331717, perimeter: 0.6718651465
            with BuildLine():
                CenterArc((0, 0), 0.125, 28.3576365763, 123.2847268473)
                Line((0.11, 0.1424780685), (0.11, 0.0593717104))
                CenterArc((0, 0), 0.18, 52.3301130357, 75.3397739287)
                Line((-0.11, 0.0593717104), (-0.11, 0.1424780685))
            make_face()
            # Profile area: 0.0466824701, perimeter: 0.775417942
            with BuildLine():
                Line((-0.11, -0.0593717104), (-0.11, 0.0593717104))
                CenterArc((0, 0), 0.125, -151.6423634237, 123.2847268473)
                Line((0.11, 0.0593717104), (0.11, -0.0593717104))
                CenterArc((0, 0), 0.125, 28.3576365763, 123.2847268473)
            make_face()
            # Profile area: 0.0012024576, perimeter: 0.2424769525
            with BuildLine():
                CenterArc((0, 0), 0.125, 151.6423634237, 56.7152731527)
                Line((-0.11, -0.0593717104), (-0.11, 0.0593717104))
            make_face()
            # Profile area: 0.0012024576, perimeter: 0.2424769525
            with BuildLine():
                CenterArc((0, 0), 0.125, -28.3576365763, 56.7152731527)
                Line((0.11, 0.0593717104), (0.11, -0.0593717104))
            make_face()
            # Profile area: 0.0136331717, perimeter: 0.6718651465
            with BuildLine():
                Line((-0.11, -0.1424780685), (-0.11, -0.0593717104))
                CenterArc((0, 0), 0.18, -127.6698869643, 75.3397739287)
                Line((0.11, -0.0593717104), (0.11, -0.1424780685))
                CenterArc((0, 0), 0.125, -151.6423634237, 123.2847268473)
            make_face()
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0136331717, perimeter: 0.6718651465
            with BuildLine():
                CenterArc((0, 0), 0.125, 28.3576365763, 123.2847268473)
                Line((0.11, 0.1424780685), (0.11, 0.0593717104))
                CenterArc((0, 0), 0.18, 52.3301130357, 75.3397739287)
                Line((-0.11, 0.0593717104), (-0.11, 0.1424780685))
            make_face()
            # Profile area: 0.0466824701, perimeter: 0.775417942
            with BuildLine():
                Line((-0.11, -0.0593717104), (-0.11, 0.0593717104))
                CenterArc((0, 0), 0.125, -151.6423634237, 123.2847268473)
                Line((0.11, 0.0593717104), (0.11, -0.0593717104))
                CenterArc((0, 0), 0.125, 28.3576365763, 123.2847268473)
            make_face()
            # Profile area: 0.0136331717, perimeter: 0.6718651465
            with BuildLine():
                Line((-0.11, -0.1424780685), (-0.11, -0.0593717104))
                CenterArc((0, 0), 0.18, -127.6698869643, 75.3397739287)
                Line((0.11, -0.0593717104), (0.11, -0.1424780685))
                CenterArc((0, 0), 0.125, -151.6423634237, 123.2847268473)
            make_face()
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17, mode=Mode.ADD)
    return part.part


def model_21337_062b39fa_0001():
    """Model: kapaki_plaketas v15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5519269846, perimeter: 4.189390575
            with BuildLine():
                Line((-0.8564850654, -0.3210931355), (0.8535149346, -0.3210931355))
                Line((0.8535149346, -0.3210931355), (0.8535149346, 0.3289068645))
                Line((0, 0), (0.8535149346, 0.3289068645))
                Line((-0.8564850654, -0.3210931355), (0, 0))
            make_face()
            # Profile area: 0.5595730154, perimeter: 4.189390575
            with BuildLine():
                Line((-0.8564850654, -0.3210931355), (0, 0))
                Line((0, 0), (0.8535149346, 0.3289068645))
                Line((0.8535149346, 0.3289068645), (-0.8564850654, 0.3289068645))
                Line((-0.8564850654, 0.3289068645), (-0.8564850654, -0.3210931355))
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                Line((-0.8535149346, 0.1087817131), (-0.8535149346, 0.083404558))
                CenterArc((-0.8455149346, 0.0960931355), 0.015, -122.2309526355, 244.461905271)
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                CenterArc((-0.6385149346, 0.3130931355), 0.015, 147.7690473645, 244.461905271)
                Line((-0.625826357, 0.3210931355), (-0.6512035121, 0.3210931355))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                CenterArc((-0.210826357, 0.3130931355), 0.015, 147.7690473645, 244.461905271)
                Line((-0.1981377795, 0.3210931355), (-0.2235149346, 0.3210931355))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                CenterArc((0.8644850654, 0.0960931355), 0.015, -122.2309526355, 244.461905271)
                Line((0.8564850654, 0.083404558), (0.8564850654, 0.1087817131))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                CenterArc((-0.6385149346, -0.3369068645), 0.015, 147.7690473645, 244.461905271)
                Line((-0.6512035121, -0.3289068645), (-0.625826357, -0.3289068645))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.ADD)
    return part.part


def model_21385_601444ba_0022():
    """Model: CrankShaft v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.175, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.0800252556, perimeter: 14.9698146581
            with BuildLine():
                CenterArc((0, 0), 2.06502, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.2408178737, perimeter: 6.3554592828
            with BuildLine():
                CenterArc((0, 0), 2.06502, 112.6051835413, 82.8948157428)
                Line((-0.79375, -0.2201263462), (-1.9899161654, -0.5518525665))
                Line((-0.79375, -0.2201263462), (-0.79375, 1.9063757599))
            make_face()
            # Profile area: 2.2408178737, perimeter: 6.3554592828
            with BuildLine():
                Line((0.79375, -0.2201263462), (1.9899161654, -0.5518525665))
                CenterArc((0, 0), 2.06502, -15.4999992841, 82.8948157428)
                Line((0.79375, -0.2201263462), (0.79375, 1.9063757599))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.9500765233, perimeter: 5.9847340051
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08128
        extrude(amount=0.08128, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.175, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((0, 1.2700000405)):
                Circle(0.3175)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 4.1275, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.5983895083, perimeter: 15.7301529987
            with BuildLine():
                CenterArc((0, 0), 2.06502, -164.5000007159, 149.0000014319)
                Line((1.9899161654, -0.5518525665), (0.79375, -0.2201263462))
                Line((0.79375, -0.2201263462), (0.79375, 1.9063757599))
                CenterArc((0, 0), 2.06502, 67.3948164587, 45.2103670826)
                Line((-0.79375, 1.9063757599), (-0.79375, -0.2201263462))
                Line((-0.79375, -0.2201263462), (-1.9899161654, -0.5518525665))
            make_face()
            with BuildLine():
                CenterArc((0, 1.2700000405), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((0, 1.2700000405)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_21638_0a984848_0011():
    """Model: Crankshaft counterweight v3 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.9486336379, perimeter: 21.9056755435
            with BuildLine():
                Line((-1.2964723969, -0.3473887317), (-3.0667194256, -0.8217249935))
                CenterArc((-2.9631918075, -1.208095324), 0.4, 105, 97.1807557815)
                CenterArc((0, 0), 3.6, -157.8192442185, 135.6384884371)
                CenterArc((2.9631918075, -1.208095324), 0.4, -22.1807557815, 97.1807557815)
                Line((1.2964723671, -0.3473887238), (3.0667194256, -0.8217249935))
                CenterArc((1.3999999851, 0.0389816068), 0.4, -180, 75)
                Line((0.9999999851, 0.0389816068), (0.9999999851, 2.4392304931))
                CenterArc((0.5999999851, 2.4392304931), 0.4, 0, 60.0000008215)
                CenterArc((-0.0000000149, 1.4), 1.6000000075, 60.0000003594, 60)
                CenterArc((-0.6000000149, 2.4392304759), 0.4, 120.0000008215, 59.9999991785)
                Line((-1.0000000149, 0.0389815988), (-1.0000000149, 2.4392304759))
                CenterArc((-1.4000000149, 0.0389815988), 0.4, -75, 75)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 1.8)):
                Circle(0.6)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.0000000149, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.5081862979, 1.8)):
                Circle(0.15)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.0000000149, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0469043967, perimeter: 0.8397999382
            with BuildLine():
                Line((0.3551537541, 0.0389815988), (0.6448462459, 0.0389815988))
                CenterArc((0.5, 0), 0.15, 164.9372168216, 210.1255663567)
            make_face()
            # Profile area: 0.023781438, perimeter: 0.6820628416
            with BuildLine():
                CenterArc((0.5, 0), 0.15, 15.0627831784, 149.8744336433)
                Line((0.3551537541, 0.0389815988), (0.6448462459, 0.0389815988))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4398229715, perimeter: 4.798229715
            with BuildLine():
                Line((0.6, 1.8), (0.8, 1.8))
                CenterArc((0, 1.8), 0.6, 180, 180)
                Line((-0.8, 1.8), (-0.6, 1.8))
                CenterArc((0, 1.8), 0.8, 180, 180)
            make_face()
            # Profile area: 0.4398229715, perimeter: 4.798229715
            with BuildLine():
                CenterArc((0, 1.8), 0.8, 0, 180)
                Line((-0.8, 1.8), (-0.6, 1.8))
                CenterArc((0, 1.8), 0.6, 0, 180)
                Line((0.6, 1.8), (0.8, 1.8))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11.7346184878, perimeter: 14.0817470824
            with BuildLine():
                Line((-1.2188266833, -0.6371664796), (-2.6407105175, -1.0181591047))
                CenterArc((-2.5371828995, -1.4045294353), 0.4, 105, 103.9679626747)
                CenterArc((0, 0), 3.3, -151.0320373253, 122.0640746507)
                CenterArc((2.5371828995, -1.4045294353), 0.4, -28.9679626747, 103.9679626747)
                Line((2.6407105175, -1.0181591047), (1.2188266535, -0.6371664716))
                CenterArc((1.3999999851, 0.0389816068), 0.7, -119.885447394, 14.885447394)
                CenterArc((0.8519056913, -0.9147440588), 0.4, 60.114552606, 72.8483395644)
                CenterArc((0, 0), 0.85, -132.9628925506, 85.925784721)
                CenterArc((-0.8519056974, -0.9147440531), 0.4, 47.0371074494, 72.8483413704)
                CenterArc((-1.4000000149, 0.0389815988), 0.7, -75, 14.8854488197)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_21732_adaf1650_0010():
    """Model: Crankshaft Counterweight v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.8193213448, perimeter: 30.8887389049
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
                Line((0, -0.6), (0, -3.3))
                CenterArc((0, 0), 3.3, -90, 74.651965068)
                CenterArc((2.9631918075, -1.208095324), 0.4, 56.784381497, 18.2155600662)
                Line((1.296472382, -0.3473887278), (3.0667198196, -0.8217250991))
                CenterArc((1.4, 0.0389816028), 0.4, -180, 75)
                Line((1, 2.3291868154), (1, 0.0389816028))
                CenterArc((0.6, 2.3291868154), 0.4, 0, 68.1985905136)
                Line((0.5942246756, 2.7623101298), (0.7485562705, 2.7005774918))
                CenterArc((-0.0000004066, 1.2767474244), 1.6, 68.1985905136, 43.6027919351)
                Line((-0.7485567418, 2.700577713), (-0.5942247877, 2.7623104102))
                CenterArc((-0.6, 2.3291872252), 0.4, 111.8014821854, 68.1985178146)
                Line((-1, 2.3291872252), (-1, 0.0389816213))
                CenterArc((-1.4, 0.0389816028), 0.4, -75.0000019109, 75.0000045637)
                Line((-1.2964723948, -0.3473887312), (-3.066719423, -0.8217249928))
                CenterArc((-2.9631918075, -1.208095324), 0.4, 104.9999996242, 18.2156188788)
                CenterArc((0, 0), 3.3, -164.651965068, 74.651965068)
            make_face()
            with BuildLine():
                CenterArc((0, 1.8), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.3141854588, perimeter: 9.4121339697
            with BuildLine():
                Line((0, -3.3), (0, -3.6))
                CenterArc((0, 0), 3.6, -90, 67.8192515162)
                CenterArc((2.9631918075, -1.208095324), 0.4, -22.1806901024, 78.9650715995)
                CenterArc((0, 0), 3.3, -90, 74.651965068)
            make_face()
            # Profile area: 1.3141854588, perimeter: 9.4121339697
            with BuildLine():
                CenterArc((0, 0), 3.3, -164.651965068, 74.651965068)
                CenterArc((-2.9631918075, -1.208095324), 0.4, 123.215618503, 78.9651439885)
                CenterArc((0, 0), 3.6, -157.819243473, 67.819243473)
                Line((0, -3.3), (0, -3.6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11.3220276252, perimeter: 14.5376280553
            with BuildLine():
                Line((-2.8775190686, -1.0816117648), (-0.944594095, -0.5636860791))
                CenterArc((-2.8257552596, -1.27479693), 0.2, 105, 99.2817990867)
                CenterArc((0, 0), 3.3, -155.7182009133, 131.4363943795)
                CenterArc((2.8257552596, -1.27479693), 0.2, -24.2819219643, 99.2820432284)
                Line((2.8775186598, -1.0816116552), (0.944594095, -0.5636860791))
                CenterArc((0, 0), 1.1, -149.1733798681, 118.3467597363)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.879645943, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.879645943, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((0, 1.8), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 1.8), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((-0.5, 1.8), 0.15, 180, 180)
                Line((-0.35, 1.8), (-0.65, 1.8))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.35, 1.8), (-0.65, 1.8))
                CenterArc((-0.5, 1.8), 0.15, 0, 180)
            make_face()
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.0237814368, perimeter: 0.6820628312
            with BuildLine():
                Line((-0.6448462448, 0.0389816028), (-0.3551537552, 0.0389816028))
                CenterArc((-0.5, 0), 0.15, 15.0627847578, 149.8744304845)
            make_face()
            # Profile area: 0.0115614805, perimeter: 0.6685610463
            with BuildLine():
                CenterArc((-0.5, 0), 0.15, 0, 15.0627847578)
                Line((-0.6448462448, 0.0389816028), (-0.3551537552, 0.0389816028))
                CenterArc((-0.5, 0), 0.15, 164.9372152422, 15.0627847578)
                Line((-0.35, 0), (-0.65, 0))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.35, 0), (-0.65, 0))
                CenterArc((-0.5, 0), 0.15, -180, 180)
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((-0.5, 1.8), 0.15, 180, 180)
                Line((-0.35, 1.8), (-0.65, 1.8))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.35, 1.8), (-0.65, 1.8))
                CenterArc((-0.5, 1.8), 0.15, 0, 180)
            make_face()
        # TwoSides extrude, along=-2.9, against=0.4
        extrude(amount=-2.9, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=0.4, mode=Mode.SUBTRACT)
    return part.part


def model_21734_7cf58bd0_0008():
    """Model: TOP SUPPORT BRACKET v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 33.0370526732, perimeter: 26.4685536327
            with BuildLine():
                CenterArc((-8.1101842557, 3.5710936297), 1.2, 90, 180)
                Line((-6.0533554756, 2.3710936297), (-8.1101842557, 2.3710936297))
                CenterArc((-3.8601842557, 3.5710936297), 2.5, -151.3145979859, 122.6291959718)
                Line((0.3898157443, 2.3710936297), (-1.6670130357, 2.3710936297))
                CenterArc((0.3898157443, 3.5710936297), 1.2, -90, 180)
                Line((-1.6670130357, 4.7710936297), (0.3898157443, 4.7710936297))
                CenterArc((-3.8601842557, 3.5710936297), 2.5, 28.6854020141, 122.6291959718)
                Line((-8.1101842557, 4.7710936297), (-6.0533554756, 4.7710936297))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-3.8601842557, 3.5710936297)):
                Circle(1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-8.1101842557, 3.5710936297)):
                Circle(0.6)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0.3898157443, 3.5710936297)):
                Circle(0.6)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-8.1101842557, 3.5710936297)):
                Circle(0.3)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.3898157443, 3.5710936297)):
                Circle(0.3)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 38 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with BuildLine():
                CenterArc((-5.239042479, 4.949951853), 0.225, -131.6926378203, 173.3852756407)
                CenterArc((-5.239042479, 4.949951853), 0.225, 41.6926378203, 186.6147243593)
            make_face()
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with BuildLine():
                CenterArc((-2.4813260323, 4.949951853), 0.225, 138.3073621797, 173.3852756407)
                CenterArc((-2.4813260323, 4.949951853), 0.225, -48.3073621797, 186.6147243593)
            make_face()
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with BuildLine():
                CenterArc((-2.4813260323, 2.1922354064), 0.225, 48.3073621797, 173.3852756407)
                CenterArc((-2.4813260323, 2.1922354064), 0.225, -138.3073621797, 186.6147243593)
            make_face()
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with BuildLine():
                CenterArc((-5.239042479, 2.1922354064), 0.225, -41.6926378203, 173.3852756407)
                CenterArc((-5.239042479, 2.1922354064), 0.225, 131.6926378203, 186.6147243593)
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_21734_7cf58bd0_0009():
    """Model: Part 28 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.15
        extrude(amount=1.15)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0450155561, perimeter: 1.3661476102
            with BuildLine():
                CenterArc((0, 0), 0.6, 146.4426902381, 67.1146195238)
                Line((-0.5, 0.331662479), (-0.5, -0.331662479))
            make_face()
            # Profile area: 0.0450155561, perimeter: 1.3661476102
            with BuildLine():
                CenterArc((0, 0), 0.6, -33.5573097619, 67.1146195238)
                Line((0.5, 0.331662479), (0.5, -0.331662479))
            make_face()
        # OneSide extrude, distance=-2.35
        extrude(amount=-2.35, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.4, 0)):
                Circle(0.2)
        # OneSide extrude, distance=-1.75
        extrude(amount=-1.75, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.35, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0009371318, perimeter: 0.2818970546
            with BuildLine():
                Line((-0.07, 0.24), (0.07, 0.24))
                CenterArc((0, 0), 0.25, 73.7397952917, 32.5204094166)
            make_face()
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)
    return part.part


def model_21803_8a36dcda_0013():
    """Model: Cylinder v7 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.5, perimeter: 19
            with BuildLine():
                Line((5, -4.5), (0, -4.5))
                Line((5, 0), (5, -4.5))
                Line((0, 0), (5, 0))
                Line((0, -4.5), (0, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            with Locations((2.8, 2.25)):
                Circle(1.8)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((-2.8, 2.25)):
                Circle(1.6)
        # OneSide extrude, distance=-6.2
        extrude(amount=-6.2, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.4, 2.25)):
                Circle(0.2)
        # OneSide extrude, distance=-6.2
        extrude(amount=-6.2, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-4.4263455967, 3.8763455967)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-4.4263455967, 0.6236544033)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-1.1736544033, 0.6236544033)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-1.1736544033, 3.8763455967)):
                Circle(0.35)
        # OneSide extrude, distance=-6.2
        extrude(amount=-6.2, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2587566188, perimeter: 2.6364458097
            with BuildLine():
                CenterArc((-0.4, 2.25), 0.2, 91.4262547814, 177.4351614524)
                Line((-0.4049780542, 2.4499380378), (-1.2125414081, 2.4499380378))
                CenterArc((-2.8, 2.25), 1.6, -7.179330528, 14.357849918)
                Line((-0.4039741455, 2.0500394885), (-1.2125442388, 2.0500394885))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_21822_7d3db422_0014():
    """Model: Crosshead Container Flange Crank"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8502938495, perimeter: 34.2057448061
            with BuildLine():
                Line((1.65, -13.8), (1.7464249197, -13.8))
                CenterArc((0, -11), 3.3, -58.0472535997, 296.0945071995)
                Line((-1.65, -13.8), (-1.7464249197, -13.8))
                CenterArc((0, -11), 3.25, -59.4897625939, 298.9795251878)
            make_face()
            # Profile area: 32.1784978652, perimeter: 20.2590756094
            with BuildLine():
                Line((-1.65, -13.8), (1.65, -13.8))
                CenterArc((0, -11), 3.25, -59.4897625939, 298.9795251878)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33.0287917148, perimeter: 20.5466691967
            with BuildLine():
                CenterArc((0, 11), 3.3, 121.9527464003, 296.0945071995)
                Line((1.7464249197, 13.8), (-1.7464249197, 13.8))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33.0287917148, perimeter: 20.5466691967
            with BuildLine():
                Line((1.7464249197, 13.8), (-1.7464249197, 13.8))
                CenterArc((0, 11), 3.3, 121.9527464003, 296.0945071995)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7426548246, perimeter: 8.1132741229
            with BuildLine():
                CenterArc((0, 8.8), 0.4, 180, 180)
                Line((0.4, 11.6), (0.4, 8.8))
                CenterArc((0, 11.6), 0.4, 0, 180)
                Line((-0.4, 8.8), (-0.4, 11.6))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-2.349231552, 10.1449496417)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-2.349231552, 11.8550503583)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-1.25, 13.1650635095)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((1.25, 13.1650635095)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((2.349231552, 11.8550503583)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((2.349231552, 10.1449496417)):
                Circle(0.225)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.8502938495, perimeter: 34.2057448061
            with BuildLine():
                Line((-1.65, 13.8), (-1.7464249197, 13.8))
                CenterArc((0, 11), 3.3, 121.9527464003, 296.0945071995)
                Line((1.7464249197, 13.8), (1.65, 13.8))
                CenterArc((0, 11), 3.25, 120.5102374061, 298.9795251878)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_21852_6cf9a734_0008():
    """Model: Bearing Support v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            Circle(0.275)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0648843512, perimeter: 1.0595137184
            with BuildLine():
                CenterArc((-1.3, 0), 0.2, 85.5882742142, 188.8234515715)
                CenterArc((0, 0), 1.3, 171.1765484285, 17.6469031431)
            make_face()
            # Profile area: 0.0607793549, perimeter: 0.9979144059
            with BuildLine():
                CenterArc((0, 0), 1.3, 171.1765484285, 17.6469031431)
                CenterArc((-1.3, 0), 0.2, -85.5882742142, 171.1765484285)
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


def model_21852_6cf9a734_0021():
    """Model: Heat Exchange Piston Exhaust v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.3482016398, perimeter: 10.8384946549
            Circle(1.725)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            Circle(1.7)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-2.9
        extrude(amount=-2.9, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0, 0.6000000089)):
                Circle(0.125)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


def model_21886_bfcc600c_0003():
    """Model: Hook Anchor v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.16, perimeter: 18.4
            with BuildLine():
                Line((2.3, -2.3), (2.3, 2.3))
                Line((2.3, 2.3), (-2.3, 2.3))
                Line((-2.3, 2.3), (-2.3, -2.3))
                Line((-2.3, -2.3), (2.3, -2.3))
            make_face()
        # OneSide extrude, distance=3.1
        extrude(amount=3.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 1.071238898
            with BuildLine():
                Line((2.3, 3.1), (2, 3.1))
                CenterArc((2.3, 3.1), 0.3, 180, 90)
                Line((2.3, 2.8), (2.3, 3.1))
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 1.071238898
            with BuildLine():
                Line((2, 0), (2.3, 0))
                Line((2.3, 0), (2.3, 0.3))
                CenterArc((2.3, 0), 0.3, 90, 90)
            make_face()
        # OneSide extrude, distance=-5.8
        extrude(amount=-5.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 1.071238898
            with BuildLine():
                Line((-2.3, 0.3), (-2.3, 0))
                Line((-2.3, 0), (-2, 0))
                CenterArc((-2.3, 0), 0.3, 0, 90)
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 1.071238898
            with BuildLine():
                Line((-2, 3.1), (-2.3, 3.1))
                Line((-2.3, 3.1), (-2.3, 2.8))
                CenterArc((-2.3, 3.1), 0.3, -90, 90)
            make_face()
        # OneSide extrude, distance=-5.3
        extrude(amount=-5.3, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)
    return part.part


def model_22093_f92b7e00_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.2053084434, perimeter: 13.8230076758
            Circle(2.2)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3470411741, perimeter: 12.2107145275
            with BuildLine():
                CenterArc((0, 3), 0.75, 0, 360)
                Line((0, 2.2), (0, 2.25))
                CenterArc((0, 0), 2.2, 69.9500242758, 20.0499757242)
                CenterArc((0, 3), 1.2, -51.057558731, 69.3390677173)
                Line((1.1227436416, 3.4236115145), (1.1394321152, 3.3764232389))
                CenterArc((0, 3), 1.2, 20.6715062946, 138.6569874108)
                Line((-1.1227436416, 3.4236115145), (-1.1394321152, 3.3764232389))
                CenterArc((0, 3), 1.2, 161.7184910137, 69.3390677173)
                CenterArc((0, 0), 2.2, 90, 20.0499757242)
            make_face()
            # Profile area: 0.000008709, perimeter: 0.1001083442
            with BuildLine():
                CenterArc((0, 3), 1.2, 18.2815089863, 2.3899973083)
                Line((1.1227436416, 3.4236115145), (1.1394321152, 3.3764232389))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3470411741, perimeter: 12.2107145275
            with BuildLine():
                CenterArc((0, 3), 0.75, 0, 360)
                Line((0, 2.2), (0, 2.25))
                CenterArc((0, 0), 2.2, 69.9500242758, 20.0499757242)
                CenterArc((0, 3), 1.2, -51.057558731, 69.3390677173)
                Line((1.1227436416, 3.4236115145), (1.1394321152, 3.3764232389))
                CenterArc((0, 3), 1.2, 20.6715062946, 138.6569874108)
                Line((-1.1227436416, 3.4236115145), (-1.1394321152, 3.3764232389))
                CenterArc((0, 3), 1.2, 161.7184910137, 69.3390677173)
                CenterArc((0, 0), 2.2, 90, 20.0499757242)
            make_face()
            # Profile area: 0.000008709, perimeter: 0.1001083442
            with BuildLine():
                CenterArc((0, 3), 1.2, 18.2815089863, 2.3899973083)
                Line((1.1227436416, 3.4236115145), (1.1394321152, 3.3764232389))
            make_face()
            # Profile area: 0.000008709, perimeter: 0.1001083442
            with BuildLine():
                CenterArc((0, 3), 1.2, 159.3284937054, 2.3899973083)
                Line((-1.1227436416, 3.4236115145), (-1.1394321152, 3.3764232389))
            make_face()
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, 3)):
                Circle(0.75)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6582281222, perimeter: 6.1935866073
            with BuildLine():
                Line((-1.1394321152, 3.3764232389), (-2.0741122138, 0.7335247265))
                CenterArc((0, 0), 2.2, 110.0499757242, 50.4735166354)
                CenterArc((0, 3), 1.2, 161.7184910137, 69.3390677173)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6582281222, perimeter: 6.1935866073
            with BuildLine():
                CenterArc((0, 0), 2.2, 19.4765076404, 50.4735166354)
                Line((1.1394321152, 3.3764232389), (2.0741122138, 0.7335247265))
                CenterArc((0, 3), 1.2, -51.057558731, 69.3390677173)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, 3)):
                Circle(0.75)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5737309739, perimeter: 15.1962321315
            with BuildLine():
                Line((2.6625502269, -3.9355658388), (-2.5, -3.9355658388))
                Line((2.6625502269, -1.5), (2.6625502269, -3.9355658388))
                Line((-2.5, -1.5), (2.6625502269, -1.5))
                Line((-2.5, -3.9355658388), (-2.5, -1.5))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude8 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)
    return part.part


def model_22173_3dff5b17_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.7168146928, perimeter: 17.2831853072
            with BuildLine():
                Line((0, 2), (3.5, 2))
                CenterArc((0, 0), 2, -90, 180)
                Line((3.5, -2), (0, -2))
                Line((3.5, 2), (3.5, -2))
            make_face()
            # Profile area: 3.8288160466, perimeter: 11.7101761242
            with BuildLine():
                Line((0, 1.25), (0, 2))
                CenterArc((0, 0), 1.25, -90, 180)
                Line((0, -2), (0, -1.25))
                CenterArc((0, 0), 2, -90, 180)
            make_face()
            # Profile area: 3.8288160466, perimeter: 11.7101761242
            with BuildLine():
                CenterArc((0, 0), 2, 90, 180)
                Line((0, -2), (0, -1.25))
                CenterArc((0, 0), 1.25, 90, 180)
                Line((0, 1.25), (0, 2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((0, -3.5), (1, -3.5))
                CenterArc((-0.5, -3.5), 0.5, -90, 90)
                Line((-0.5, -4), (-0.5, -5))
                CenterArc((-0.5, -3.5), 1.5, -90, 90)
            make_face()
            # Profile area: 2.4687240461, perimeter: 8.4322255636
            with BuildLine():
                CenterArc((-0.5, -3.5), 1.5, -160.5287793655, 70.5287793655)
                Line((-4, -4), (-1.9142135624, -4))
                Line((-4, -5), (-4, -4))
                Line((-0.5, -5), (-4, -5))
            make_face()
            # Profile area: 1.0312759539, perimeter: 4.2606526884
            with BuildLine():
                Line((-0.5, -4), (-0.5, -5))
                Line((-1.9142135624, -4), (-0.5, -4))
                CenterArc((-0.5, -3.5), 1.5, -160.5287793655, 70.5287793655)
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)

        # Sketch7 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.8288160466, perimeter: 11.7101761242
            with BuildLine():
                Line((-4, -1.25), (-4, -2))
                CenterArc((-4, 0), 1.25, 90, 180)
                Line((-4, 2), (-4, 1.25))
                CenterArc((-4, 0), 2, 90, 180)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch8 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                Line((-4, 1.25), (-4, -1.25))
                CenterArc((-4, 0), 1.25, 90, 180)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((-4, 0), 1.25, -90, 180)
                Line((-4, 1.25), (-4, -1.25))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_22175_cfad1a59_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.6807451779, perimeter: 14.4941415593
            with BuildLine():
                CenterArc((0, 0), 2.5, -180, 90)
                CenterArc((0, 0), 2.5, -90, 90)
                CenterArc((0, 0), 2.5, 0, 23.5781784782)
                Line((-2.2912878475, 1), (2.2912878475, 1))
                CenterArc((0, 0), 2.5, 156.4218215218, 23.5781784782)
            make_face()
            # Profile area: 0.0683659323, perimeter: 2.2375042677
            with BuildLine():
                Line((2.5, 0), (2.5, 1))
                Line((2.2912878475, 1), (2.5, 1))
                CenterArc((0, 0), 2.5, 0, 23.5781784782)
            make_face()
            # Profile area: 0.0683659323, perimeter: 2.2375042677
            with BuildLine():
                CenterArc((0, 0), 2.5, 156.4218215218, 23.5781784782)
                Line((-2.5, 1), (-2.2912878475, 1))
                Line((-2.5, 0), (-2.5, 1))
            make_face()
            # Profile area: 1.3412614788, perimeter: 8.926990817
            with BuildLine():
                Line((-2.5, -2.5), (-2.5, 0))
                Line((0, -2.5), (-2.5, -2.5))
                CenterArc((0, 0), 2.5, -180, 90)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((1.5, 0), (2.5, 0))
                Line((2.5, 2.5), (2.5, 0))
                Line((1.5, 2.5), (2.5, 2.5))
                Line((1.5, 0), (1.5, 2.5))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((2.5, -1), (1.5, -1))
                Line((2.5, 0), (2.5, -1))
                Line((1.5, 0), (2.5, 0))
                Line((1.5, -1), (1.5, 0))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((1.5, -1), (-2.5, -1))
                Line((1.5, -1), (1.5, 0))
                Line((-2.5, 0), (1.5, 0))
                Line((-2.5, -1), (-2.5, 0))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane.XY):
            # Profile area: 7, perimeter: 12.8150729064
            with BuildLine():
                Line((2.5, 4.5), (-1.5, 4.5))
                Line((-1.5, 4.5), (2.5, 1))
                Line((2.5, 1), (2.5, 4.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4206195997, perimeter: 4.9991148575
            with BuildLine():
                Line((-0.1, 1), (-1.5, 1))
                CenterArc((-0.1, 2.4), 1.4, 180, 90)
                Line((-1.5, 1), (-1.5, 2.4))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.2345133224, perimeter: 6.0849555922
            with BuildLine():
                Line((2, 4.5), (0.8, 4.5))
                Line((0.8, 3), (0.8, 4.5))
                CenterArc((1.4, 3), 0.6, 0, 180)
                Line((2, 4.5), (2, 3))
            make_face()
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((1.4, 3), 0.6, 0, 180)
                CenterArc((1.4, 3), 0.6, 180, 180)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_22176_272891b8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch7 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.819425444, perimeter: 25.015779669
            with BuildLine():
                CenterArc((0.0072984823, 4.6773403203), 1, 0, 180)
                Line((-0.9927015177, 4.6773403203), (-1.9468614264, 1.1279319955))
                CenterArc((0, 0), 2.25, 149.9137494825, 60.8069129282)
                Line((-1.9342532252, -1.1494191842), (-0.9900564091, -4.5874280145))
                CenterArc((-0.025761033, -4.3225989611), 1, -164.64320463, 148.6904618021)
                Line((1.9099256651, -1.1894048738), (0.9357276798, -4.5974433811))
                CenterArc((0, 0), 2.25, -31.9125573266, 61.6650139257)
                Line((1.0072984823, 4.6773403203), (1.9533994606, 1.1165708877))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch8 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch9 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, -4.5)):
                Circle(0.5)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0.025761033, 4.3225989611)):
                Circle(0.5)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_22198_327974c6_0009():
    """Model: Centrifugal Pump Shaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=5.4
        extrude(amount=5.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0288593018, perimeter: 0.6793159277
            with BuildLine():
                Line((-0.3, 0), (-0.5, 0))
                Line((-0.3, 0.15), (-0.3, 0))
                Line((-0.4769696007, 0.15), (-0.3, 0.15))
                CenterArc((0, 0), 0.5, 162.5423968763, 17.4576031237)
            make_face()
            # Profile area: 0.0311406998, perimeter: 0.7253767472
            with BuildLine():
                Line((-0.7000000104, 0.15), (-0.4769696007, 0.15))
                Line((-0.7000000104, 0), (-0.7000000104, 0.15))
                Line((-0.5, 0), (-0.7000000104, 0))
                CenterArc((0, 0), 0.5, 162.5423968763, 17.4576031237)
            make_face()
            # Profile area: 0.0311406998, perimeter: 0.7253767472
            with BuildLine():
                Line((-0.5, 0), (-0.7000000104, 0))
                Line((-0.7000000104, 0), (-0.7000000104, -0.15))
                Line((-0.7000000104, -0.15), (-0.4769696007, -0.15))
                CenterArc((0, 0), 0.5, -180, 17.4576031237)
            make_face()
            # Profile area: 0.0288593018, perimeter: 0.6793159277
            with BuildLine():
                Line((-0.3, 0), (-0.5, 0))
                CenterArc((0, 0), 0.5, -180, 17.4576031237)
                Line((-0.4769696007, -0.15), (-0.3, -0.15))
                Line((-0.3, -0.15), (-0.3, 0))
            make_face()
        # OneSide extrude, distance=-2.55
        extrude(amount=-2.55, mode=Mode.SUBTRACT)
    return part.part


def model_22202_c9c16395_0000():
    """Model: Cylinder v3 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0193488, perimeter: 6.97992
            with BuildLine():
                Line((0.79248, -0.9525), (0.79248, 0.9525))
                Line((0.79248, 0.9525), (-0.79248, 0.9525))
                Line((-0.79248, 0.9525), (-0.79248, -0.9525))
                Line((-0.79248, -0.9525), (0.79248, -0.9525))
            make_face()
        # Symmetric extrude, each_side=1.82499
        extrude(amount=1.82499, both=True)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.82499), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, -0.16002)):
                Circle(0.635)
        # OneSide extrude, distance=-6.604
        extrude(amount=-6.604, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.82499), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1558701317, perimeter: 1.6775810943
            with BuildLine():
                CenterArc((0, -0.16002), 0.635, 68.1609845516, 43.6780308968)
                Line((0.23622, 0.4294077832), (0.23622, 0.78994))
                Line((0.23622, 0.78994), (-0.23622, 0.78994))
                Line((-0.23622, 0.78994), (-0.23622, 0.4294077832))
            make_face()
            # Profile area: 1.1160919461, perimeter: 4.5548393107
            with BuildLine():
                CenterArc((0, -0.16002), 0.635, 111.8390154484, 316.3219691032)
                Line((0.23622, 0.1410811325), (0.23622, 0.4294077832))
                Line((-0.23622, 0.1410811325), (0.23622, 0.1410811325))
                Line((-0.23622, 0.4294077832), (-0.23622, 0.1410811325))
            make_face()
            # Profile area: 0.1506767517, perimeter: 1.5331699621
            with BuildLine():
                Line((-0.23622, 0.4294077832), (-0.23622, 0.1410811325))
                Line((-0.23622, 0.1410811325), (0.23622, 0.1410811325))
                Line((0.23622, 0.1410811325), (0.23622, 0.4294077832))
                CenterArc((0, -0.16002), 0.635, 68.1609845516, 43.6780308968)
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -1.82499), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1558701317, perimeter: 1.6775810943
            with BuildLine():
                Line((0.23622, 0.78994), (-0.23622, 0.78994))
                Line((-0.23622, 0.78994), (-0.23622, 0.4294077832))
                CenterArc((0, -0.16002), 0.635, 68.1609845516, 43.6780308968)
                Line((0.23622, 0.4294077832), (0.23622, 0.78994))
            make_face()
            # Profile area: 0.0144597088, perimeter: 0.9565166607
            with BuildLine():
                CenterArc((0, -0.16002), 0.635, 68.1609845516, 43.6780308968)
                Line((-0.23622, 0.4294077832), (0.23622, 0.4294077832))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)
    return part.part


def model_22305_5b45cdb3_0002():
    """Model: 28-FIRE-BOX-REAR-COVER v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.4228758088, perimeter: 17.1549710866
            with BuildLine():
                CenterArc((1.6, 3.1), 1.6, 0, 180)
                Line((0, 3.1), (0, 0))
                Line((0, 0), (3.2, 0))
                Line((3.2, 0), (3.2, 3.1))
            make_face()
            with BuildLine():
                EllipticalCenterArc((1.6, 1.7), 0.55, 0.3, 0, 360, 0)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.05), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((1.6, 4.1000000611)):
                Circle(0.1)
            # Profile area: 0.015, perimeter: 0.5
            with BuildLine():
                Line((2.2, 1.625), (2.2, 1.475))
                Line((2.2, 1.475), (2.3, 1.475))
                Line((2.3, 1.475), (2.3, 1.625))
                Line((2.3, 1.625), (2.2, 1.625))
            make_face()
            # Profile area: 0.015, perimeter: 0.5
            with BuildLine():
                Line((2.2, 1.925), (2.2, 1.775))
                Line((2.2, 1.775), (2.3, 1.775))
                Line((2.3, 1.775), (2.3, 1.925))
                Line((2.3, 1.925), (2.2, 1.925))
            make_face()
            # Profile area: 0.015, perimeter: 0.5
            with BuildLine():
                Line((0.9, 1.775), (0.9, 1.625))
                Line((0.9, 1.625), (1, 1.625))
                Line((1, 1.625), (1, 1.775))
                Line((1, 1.775), (0.9, 1.775))
            make_face()
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((1.0180261078, 3.2), (1.0180261078, 3.1))
                Line((1.0180261078, 3.1), (1.1180261078, 3.1))
                Line((1.1180261078, 3.1), (1.1180261078, 3.2))
                Line((1.1180261078, 3.2), (1.0180261078, 3.2))
            make_face()
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((1.0180261078, 4.2), (1.0180261078, 4.1))
                Line((1.0180261078, 4.1), (1.1180261078, 4.1))
                Line((1.1180261078, 4.1), (1.1180261078, 4.2))
                Line((1.1180261078, 4.2), (1.0180261078, 4.2))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.075, 1.55)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with BuildLine():
                CenterArc((0.075, 1.85), 0.025, 0, 180)
                CenterArc((0.075, 1.85), 0.025, 180, 180)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch3 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with BuildLine():
                CenterArc((-0.075, 1.7), 0.025, 0, 180)
                CenterArc((-0.075, 1.7), 0.025, 180, 180)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with BuildLine():
                CenterArc((-1.0680261078, 0.075), 0.025, 90, 180)
                CenterArc((-1.0680261078, 0.075), 0.025, -90, 180)
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


def model_22323_aa6edb8b_0002():
    """Model: Spindle v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1074114104, perimeter: 14.7654854719
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=17.8
        extrude(amount=17.8, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -23.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.44, perimeter: 4.8
            with BuildLine():
                Line((-0.6, 0.6), (0.6, 0.6))
                Line((-0.6, -0.6), (-0.6, 0.6))
                Line((0.6, -0.6), (-0.6, -0.6))
                Line((0.6, 0.6), (0.6, -0.6))
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -25.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)
    return part.part


def model_22369_481ab478_0017():
    """Model: piston rod detail v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.1248983265, perimeter: 1.2528043184
            Circle(0.19939)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-5.08, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.0635613862, perimeter: 0.8937202781
            Circle(0.14224)
        # OneSide extrude, distance=0.79248
        extrude(amount=0.79248, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2783266735, perimeter: 3.7928043184
            with BuildLine():
                Line((-0.3175, 0.3175), (0.3175, 0.3175))
                Line((-0.3175, -0.3175), (-0.3175, 0.3175))
                Line((0.3175, -0.3175), (-0.3175, -0.3175))
                Line((0.3175, 0.3175), (0.3175, -0.3175))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.19939, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1248983265, perimeter: 1.2528043184
            Circle(0.19939)
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.3175, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1583460872, perimeter: 1.6324556675
            with BuildLine():
                Line((0.47498, -0.3175), (0.47498, 0.3175))
                CenterArc((0.47498, 0), 0.3175, -90, 180)
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.3175, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((0.47498, 0)):
                Circle(0.15875)
        # OneSide extrude, distance=-1.778
        extrude(amount=-1.778, mode=Mode.SUBTRACT)
    return part.part


def model_22369_985c13a1_0021():
    """Model: eccentric rod clevis v1"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2256060004, perimeter: 1.89992
            with BuildLine():
                Line((0.23749, -0.23749), (0.23749, 0.23749))
                Line((0.23749, 0.23749), (-0.23749, 0.23749))
                Line((-0.23749, 0.23749), (-0.23749, -0.23749))
                Line((-0.23749, -0.23749), (0.23749, -0.23749))
            make_face()
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0885952692, perimeter: 1.2210768393
            with BuildLine():
                CenterArc((0.23749, 0), 0.23749, -90, 180)
                Line((0.23749, -0.23749), (0.23749, 0.23749))
            make_face()
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0401362994, perimeter: 0.7101884353
            with Locations((0.23749, 0)):
                Circle(0.11303)
        # OneSide extrude, distance=-0.7366
        extrude(amount=-0.7366, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.23749, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-0.23749, 0)):
                Circle(0.15875)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.87249, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.0410433058, perimeter: 0.7181680806
            with Locations((-0.23749, 0)):
                Circle(0.1143)
        # OneSide extrude, distance=-0.7112
        extrude(amount=-0.7112, mode=Mode.SUBTRACT)
    return part.part


def model_22432_e4a51ee9_0006():
    """Model: Crank Case"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 16.7617484852, perimeter: 15.24
            with BuildLine():
                Line((1.2699916648, 2.1997093379), (-1.2700083352, 2.1996997132))
                Line((-1.2700083352, 2.1996997132), (-2.54, -0.0000096247))
                Line((-2.54, -0.0000096247), (-1.2699916648, -2.1997093379))
                Line((-1.2699916648, -2.1997093379), (1.2700083352, -2.1996997132))
                Line((1.2700083352, -2.1996997132), (2.54, 0.0000096247))
                Line((2.54, 0.0000096247), (1.2699916648, 2.1997093379))
            make_face()
        # TwoSides extrude, along=1.588, against=-1.905
        extrude(amount=1.588)
        extrude(sk.sketch, amount=-1.905)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.905), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.9173043609, perimeter: 9.9745566751
            Circle(1.5875)
        # OneSide extrude, distance=-0.39
        extrude(amount=-0.39, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.588), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7028653828, perimeter: 2.9719466503
            Circle(0.473)
        # OneSide extrude, distance=-0.64
        extrude(amount=-0.64, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.9050041676, 1.0998450443, 0), x_dir=(0, 0, 1), z_dir=(-0.8660272984, 0.4999967184, 0))):
            # Profile area: 0.4659649985, perimeter: 2.4198117414
            with Locations((-0.1585, 0)):
                Circle(0.385125)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000083352, 2.1997045256, 0), x_dir=(0, 0, 1), z_dir=(-0.0000037893, 1, 0))):
            # Profile area: 2.8472379883, perimeter: 5.9815924124
            with Locations((-0.317, 0)):
                Circle(0.952)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000083352, 2.1997045256, 0), x_dir=(0, 0, 1), z_dir=(-0.0000037893, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.271, -0.953)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.271, 0.953)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.587, 0.953)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.587, -0.953)):
                Circle(0.15)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000083352, 2.1997045256, 0), x_dir=(0, 0, 1), z_dir=(-0.0000037893, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.191, -0.238)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.191, 0.238)):
                Circle(0.15)
        # OneSide extrude, distance=-1.35
        extrude(amount=-1.35, mode=Mode.SUBTRACT)
    return part.part


def model_22498_b8bdb105_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.9022104447, perimeter: 16.9646003294
            Circle(2.7)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            Circle(0.325)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 22.9022104447, perimeter: 16.9646003294
            Circle(2.7)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.25), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 20.9928289696, perimeter: 16.2420340191
            Circle(2.585)
        # OneSide extrude, distance=-1.65
        extrude(amount=-1.65, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7278759595, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, 0), 2.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_22543_684108ff_0001():
    """Model: 1_crankcase v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.4516, perimeter: 10.16
            with BuildLine():
                Line((1.27, -1.27), (1.27, 1.27))
                Line((1.27, 1.27), (-1.27, 1.27))
                Line((-1.27, 1.27), (-1.27, -1.27))
                Line((-1.27, -1.27), (1.27, -1.27))
            make_face()
        # Symmetric extrude, each_side=2.343
        extrude(amount=2.343, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.27, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.0136299419, perimeter: 7.1018843527
            with Locations((-1.073, 0)):
                Circle(1.1303)
        # OneSide extrude, distance=-4.6
        extrude(amount=-4.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.343), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0068439274, perimeter: 0.4062181211
            with BuildLine():
                Line((-1.27, 1.27), (-1.27, 1.1510412677))
                CenterArc((0, 0), 1.714, 132.1870136208, 5.6259727584)
                Line((-1.1510412677, 1.27), (-1.27, 1.27))
            make_face()
            # Profile area: 0.0068439274, perimeter: 0.4062181211
            with BuildLine():
                CenterArc((0, 0), 1.714, 42.1870136208, 5.6259727584)
                Line((1.27, 1.1510412677), (1.27, 1.27))
                Line((1.27, 1.27), (1.1510412677, 1.27))
            make_face()
            # Profile area: 0.0068439274, perimeter: 0.4062181211
            with BuildLine():
                CenterArc((0, 0), 1.714, -137.8129863792, 5.6259727584)
                Line((-1.27, -1.1510412677), (-1.27, -1.27))
                Line((-1.27, -1.27), (-1.1510412677, -1.27))
            make_face()
            # Profile area: 0.0068439274, perimeter: 0.4062181211
            with BuildLine():
                CenterArc((0, 0), 1.714, -47.8129863792, 5.6259727584)
                Line((1.1510412677, -1.27), (1.27, -1.27))
                Line((1.27, -1.27), (1.27, -1.1510412677))
            make_face()
        # OneSide extrude, distance=-1.111
        extrude(amount=-1.111, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.343), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            Circle(0.9525)
        # OneSide extrude, distance=-3.175
        extrude(amount=-3.175, mode=Mode.SUBTRACT)
    return part.part


def model_22586_ff3651b2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.7087168449, perimeter: 25.3699111841
            with BuildLine():
                CenterArc((12.6534978903, 2.1), 0.1, 0, 90)
                Line((12.6534978903, 2.2), (2.5534978903, 2.2))
                CenterArc((2.5534978903, 2.1), 0.1, 90, 90)
                Line((2.4534978903, 2.1), (2.4534978903, 1.6))
                CenterArc((2.5534978903, 1.6), 0.1, -180, 90)
                Line((2.5534978903, 1.5), (12.6534978903, 1.5))
                CenterArc((12.6534978903, 1.6), 0.1, -90, 90)
                Line((12.7534978903, 1.6), (12.7534978903, 2.1))
            make_face()
            with BuildLine():
                Line((2.8534978903, 1.6), (2.7534978903, 1.6))
                CenterArc((2.7534978903, 1.85), 0.25, 90, 180)
                Line((2.8034978903, 2.1), (2.7534978903, 2.1))
                Line((2.8534978903, 2.1), (2.8034978903, 2.1))
                CenterArc((2.8534978903, 1.85), 0.25, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((12.3534978903, 2.1), (12.4534978665, 2.1))
                CenterArc((12.4534978903, 1.85), 0.25, -90, 180.0000054668)
                Line((12.3534978903, 1.6), (12.4534978903, 1.6))
                CenterArc((12.3534978903, 1.85), 0.25, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.75, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.71, perimeter: 12
            with BuildLine():
                Line((10.2534978903, 2.2), (4.9534978903, 2.2))
                Line((4.9534978903, 1.5), (4.9534978903, 2.2))
                Line((4.9534978903, 1.5), (10.2534978903, 1.5))
                Line((10.2534978903, 2.2), (10.2534978903, 1.5))
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.565, perimeter: 8.5
            with BuildLine():
                Line((-1.9, -4.9534978903), (-1.9, -8.0534978903))
                Line((-3.05, -4.9534978903), (-1.9, -4.9534978903))
                Line((-3.05, -8.0534978903), (-3.05, -4.9534978903))
                Line((-1.9, -8.0534978903), (-3.05, -8.0534978903))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.49, perimeter: 2.8
            with BuildLine():
                Line((-3.05, -7.3534978903), (-3.05, -8.0534978903))
                Line((-3.75, -7.3534978903), (-3.05, -7.3534978903))
                Line((-3.75, -8.0534978903), (-3.75, -7.3534978903))
                Line((-3.05, -8.0534978903), (-3.75, -8.0534978903))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -7.3534978903), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.49, perimeter: 2.8
            with BuildLine():
                Line((3.05, 1.4), (3.75, 1.4))
                Line((3.05, 0.7), (3.05, 1.4))
                Line((3.75, 0.7), (3.05, 0.7))
                Line((3.75, 1.4), (3.75, 0.7))
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4, mode=Mode.ADD)
    return part.part


def model_22605_ddf43428_0004():
    """Model: A9 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9900000003, perimeter: 10.4259406627
            with BuildLine():
                Line((2.7000000402, 1.8), (2.3000000343, 1.5000000224))
                Line((2.3000000343, 1.5000000224), (2.3000000343, 1.4000000209))
                Line((2.3000000343, 1.4000000209), (2.1000000313, 1.4000000209))
                Line((2.1000000313, 1.4000000209), (0, 0.4))
                Line((0, 0), (0, 0.4))
                Line((0, 0), (3.9, 0))
                Line((3.9, 0), (3.9, 1.8))
                Line((3.9, 1.8), (2.7000000402, 1.8))
            make_face()
            # Profile area: 0.69, perimeter: 4.3317821063
            with BuildLine():
                Line((3.9, 0), (3.9, 1.8))
                Line((4.5, 0), (3.9, 0))
                Line((4.5, 0), (4.5, 0.5))
                Line((4.5, 0.5), (3.9, 1.8))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2381720338, perimeter: 6.1545884518
            with BuildLine():
                Line((-3.2000000477, -0.9000000134), (-3.1981038846, 0))
                Line((-4.0812623518, -1.4072649045), (-3.2000000477, -0.9000000134))
                Line((-3.9, -1.8), (-4.0812623518, -1.4072649045))
                Line((-2.7000000402, -1.8), (-3.9, -1.8))
                Line((-2.3000000343, -1.5000000224), (-2.7000000402, -1.8))
                Line((-2.3000000343, -1.5000000224), (-2.3000000343, -1.4000000209))
                Line((-2.3000000343, -1.4000000209), (-2.5000000373, -1.4000000209))
                Line((-2.5000000373, -1.4000000209), (-3.0000000447, -0.9000000134))
                Line((-3.0000000447, -0.9000000134), (-3.0000000447, 0))
                Line((-3.0000000447, 0), (-3.1981038846, 0))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.8231910155, perimeter: 6.0488702987
            with BuildLine():
                Line((2.5000000373, -1.4000000209), (3.0000000447, -0.9000000134))
                Line((2.3000000343, -1.4000000209), (2.5000000373, -1.4000000209))
                Line((2.3000000343, -1.5000000224), (2.3000000343, -1.4000000209))
                Line((2.7000000402, -1.8), (2.3000000343, -1.5000000224))
                Line((3.9, -1.8), (2.7000000402, -1.8))
                Line((3.9, -1.8), (3.2133231656, -1.4830722303))
                Line((3.2133231656, -1.4830722303), (3.2073832932, -0.9042498959))
                Line((3.2000000477, -0.9000000134), (3.2073832932, -0.9042498959))
                Line((3.1981038846, 0), (3.2000000477, -0.9000000134))
                Line((3.0000000447, 0), (3.1981038846, 0))
                Line((3.0000000447, -0.9000000134), (3.0000000447, 0))
            make_face()
            # Profile area: 0.5751366751, perimeter: 3.5073020727
            with BuildLine():
                Line((3.0000000447, -0.9000000134), (3.0000000447, 0))
                Line((2.4998048116, 0), (3.0000000447, 0))
                Line((2.5000000373, -1.4000000209), (2.4998048116, 0))
                Line((2.5000000373, -1.4000000209), (3.0000000447, -0.9000000134))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7782885078, perimeter: 3.7975314033
            with BuildLine():
                Line((0, 0), (1.3968829435, 0))
                Line((0, 0), (0, -0.4))
                Line((0.9367633914, -0.8460778081), (0, -0.4))
                Line((0.9367633914, -0.8460778081), (1.3968829435, 0))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3689568044, perimeter: 2.6236039856
            with BuildLine():
                Line((4.5, -0.5), (4.5, 0))
                Line((3.800770151, 0), (4.5, 0))
                Line((3.8000000566, -0.1000000015), (3.800770151, 0))
                Line((4.3340918235, -0.8594677158), (3.8000000566, -0.1000000015))
                Line((4.5, -0.5), (4.3340918235, -0.8594677158))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.8357235552, -1.2936133525)):
                Circle(0.2)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)

        # Sketch14 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-4.3447529057, -0.4666665973)):
                Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_22606_f1813fe7_0005():
    """Model: B4 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2613477007, perimeter: 6.2919244055
            with BuildLine():
                Line((0, 0), (-1.2864772787, -0.7713470111))
                Line((-1.2864772787, -0.7713470111), (-1.2864772787, -0.9713470111))
                Line((-1.5, -1.3), (-1.2864772787, -0.9713470111))
                Line((-1.5, -2), (-1.5, -1.3))
                Line((0, -2), (-1.5, -2))
                Line((0, 0), (0, -2))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.45, perimeter: 2.8
            with BuildLine():
                Line((-1.5, 1.2), (-0.6, 1.2))
                Line((-0.6, 1.2), (-0.6, 1.7))
                Line((-0.6, 1.7), (-1.5, 1.7))
                Line((-1.5, 1.7), (-1.5, 1.2))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.34, perimeter: 3.8464249197
            with BuildLine():
                Line((-0.4, 0), (0, 1.7))
                Line((-0.4, 0), (0, 0))
                Line((0, 0), (0, 1.7))
            make_face()
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.25, 1.75)):
                Circle(0.15)
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.3354813714, 0.4813635536)):
                Circle(0.15)
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7493326186, perimeter: 3.7662012239
            with BuildLine():
                Line((0.7, 1.9), (0.7, 0.5363039979))
                Line((0.7, 0.5363039979), (1.1864772787, 0.8279864093))
                Line((1.1864772787, 0.8279864093), (1.1864772787, 1.0009791815))
                Line((1.1864772787, 1.0009791815), (1.4, 1.3296321704))
                Line((1.4, 1.3296321704), (1.4, 1.9))
                Line((1.4, 1.9), (0.7, 1.9))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude7 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-1.1, 0.7)):
                Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch7 -> Extrude8 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((-1.1864772787, 0.8279864093), 0.1, -120.946090305, 300.946090305)
                CenterArc((-1.1864772787, 0.8279864093), 0.1, 180, 59.053909695)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_22734_f6bad9f7_0018():
    """Model: Cylinder v13 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7040291606, perimeter: 8.7486132919
            with BuildLine():
                Line((0.9525, -1.2700000405), (0.9525, 1.1993066054))
                Line((0.9525, 1.1993066054), (-0.9525, 1.1993066054))
                Line((-0.9525, 1.1993066054), (-0.9525, -1.2700000405))
                Line((-0.9525, -1.2700000405), (0.9525, -1.2700000405))
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            Circle(0.79375)
        # OneSide extrude, distance=2.86004
        extrude(amount=2.86004, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.81254, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=-2.8575
        extrude(amount=-2.8575, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.1993066054), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((0, 0.47625)):
                Circle(0.15875)
        # OneSide extrude, distance=-3.302
        extrude(amount=-3.302, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.1993066054), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1790906914, perimeter: 1.5001733239
            with Locations((0.0000000717, 0.47625)):
                Circle(0.23876)
        # OneSide extrude, distance=-2.1844
        extrude(amount=-2.1844, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.95504, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((0, 0.34036)):
                Circle(0.15875)
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


def model_23137_e55b73cb_0007():
    """Model: Stepper_Motor v11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 17.8929, perimeter: 16.92
            with BuildLine():
                Line((0, 4.23), (0, 0))
                Line((0, 0), (4.23, 0))
                Line((4.23, 0), (4.23, 4.23))
                Line((4.23, 4.23), (0, 4.23))
            make_face()
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.4, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((2.115, 2.115)):
                Circle(1.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.6, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2.115, 2.115)):
                Circle(0.25)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.115, 2.115)):
                Circle(0.05)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0431243563, perimeter: 0.9929594729
            with BuildLine():
                CenterArc((2.115, 2.115), 0.25, 117.182861889, 125.634276222)
                Line((2.0007920331, 2.3373882648), (2.0007920331, 1.8926117352))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_23599_db59334f_0000():
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
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663462837, perimeter: 45.1168380277
            with BuildLine():
                CenterArc((0, 0), 3.8688128612, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.3117549275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9793260902, perimeter: 13.1031958439
            with BuildLine():
                CenterArc((0, 0), 4.1275, 45, 90)
                Line((-2.6940768363, 2.6940768363), (-2.9185832393, 2.9185832393))
                CenterArc((0, 0), 3.81, 45, 90)
                Line((2.6940768363, 2.6940768363), (2.9185832393, 2.9185832393))
            make_face()
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((3.81, 0)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-3.81, 0)):
                Circle(0.635)
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1911932411, perimeter: 4.1258996073
            with BuildLine():
                _nurbs_edge([(0.2631088544, -1.014067171), (0.270732103, -1.0270521307), (0.2867560198, -1.0543462572), (0.2951638725, -1.0848774015), (0.2995717574, -1.1008836011)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0449694572, 0.0945249033, 0.0945249033, 0.0945249033, 0.0945249033], 3)
                _nurbs_edge([(0.19712842, -0.9478386621), (0.2101547956, -0.9578663435), (0.2350752647, -0.9770500775), (0.2540517283, -1.0021076436), (0.2631088544, -1.014067171)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0490612521, 0.0938579888, 0.0938579888, 0.0938579888, 0.0938579888], 3)
                _nurbs_edge([(0.0912123967, -0.898229299), (0.1110968497, -0.904762499), (0.1484304246, -0.9170287511), (0.181617368, -0.938025237), (0.19712842, -0.9478386621)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0625053824, 0.1173554726, 0.1173554726, 0.1173554726, 0.1173554726], 3)
                _nurbs_edge([(-0.0556313347, -0.8788816313), (-0.0294511377, -0.8794977176), (0.0202138893, -0.8806664615), (0.0684182595, -0.8925907336), (0.0912123967, -0.898229299)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0782842867, 0.1485088603, 0.1485088603, 0.1485088603, 0.1485088603], 3)
                _nurbs_edge([(-0.2285200309, -0.9074070434), (-0.201704051, -0.8990921937), (-0.1454199553, -0.8816401447), (-0.0864865328, -0.8798295741), (-0.0556313347, -0.8788816313)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0838253937, 0.1759412299, 0.1759412299, 0.1759412299, 0.1759412299], 3)
                _nurbs_edge([(-0.3527915429, -0.9934793095), (-0.33523315, -0.9754221054), (-0.2994527047, -0.9386251841), (-0.2524548293, -0.9179409746), (-0.2285200309, -0.9074070434)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0748049882, 0.1524374013, 0.1524374013, 0.1524374013, 0.1524374013], 3)
                _nurbs_edge([(-0.4048813533, -1.1001394371), (-0.3992849373, -1.0802708012), (-0.3883756157, -1.0415400603), (-0.3644456035, -1.0092195792), (-0.3527915429, -0.9934793095)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0613456237, 0.119583522, 0.119583522, 0.119583522, 0.119583522], 3)
                _nurbs_edge([(-0.4152993511, -1.2296199183), (-0.4151961271, -1.2046234468), (-0.4150166906, -1.1611715547), (-0.4079028366, -1.11833395), (-0.4048813533, -1.1001394371)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.074831465, 0.1300811091, 0.1300811091, 0.1300811091, 0.1300811091], 3)
                Line((-0.4152993511, -1.4801472778), (-0.4152993511, -1.2296199183))
                Line((0.3119741131, -1.4801472778), (-0.4152993511, -1.4801472778))
                Line((0.3119741131, -1.2177136819), (0.3119741131, -1.4801472778))
                _nurbs_edge([(0.2995717574, -1.1008836011), (0.3031858038, -1.119038073), (0.3108610296, -1.1575931044), (0.3115889499, -1.1969099989), (0.3119741131, -1.2177136819)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0554185462, 0.1176935254, 0.1176935254, 0.1176935254, 0.1176935254], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-0.2324888062, -1.015555499), (-0.2509790752, -1.0281138992), (-0.2858681723, -1.0518102143), (-0.3054080303, -1.0890737709), (-0.314592297, -1.1065886597)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0658664195, 0.1242826644, 0.1242826644, 0.1242826644, 0.1242826644], 3)
                _nurbs_edge([(-0.0571196627, -0.9781004171), (-0.0913187913, -0.9787578279), (-0.1523832514, -0.9799316717), (-0.2080140264, -1.0046712934), (-0.2324888062, -1.015555499)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1013266689, 0.1809244439, 0.1809244439, 0.1809244439, 0.1809244439], 3)
                _nurbs_edge([(0.0830268312, -0.9972000102), (0.0618275974, -0.9916379452), (0.0159209052, -0.9795933586), (-0.0315632158, -0.9786227882), (-0.0571196627, -0.9781004171)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.065519185, 0.1418810262, 0.1418810262, 0.1418810262, 0.1418810262], 3)
                _nurbs_edge([(0.1750522304, -1.0505300741), (0.1621459691, -1.0395867875), (0.1347044133, -1.0163189487), (0.1009211912, -1.0038203116), (0.0830268312, -0.9972000102)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0503666849, 0.107090671, 0.107090671, 0.107090671, 0.107090671], 3)
                _nurbs_edge([(0.2127553869, -1.1157664041), (0.2080985836, -1.1030874105), (0.1992991073, -1.0791292369), (0.1828134514, -1.0596844251), (0.1750522304, -1.0505300741)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.040152233, 0.0758714923, 0.0758714923, 0.0758714923, 0.0758714923], 3)
                _nurbs_edge([(0.2261498619, -1.2286277394), (0.2259397412, -1.2071172466), (0.2255671163, -1.168970873), (0.2166459607, -1.1319231544), (0.2127553869, -1.1157664041)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0642694265, 0.1139744022, 0.1139744022, 0.1139744022, 0.1139744022], 3)
                Line((0.2261498619, -1.383905081), (0.2261498619, -1.2286277394))
                Line((-0.3294751, -1.383905081), (0.2261498619, -1.383905081))
                Line((-0.3294751, -1.2311082165), (-0.3294751, -1.383905081))
                _nurbs_edge([(-0.314592297, -1.1065886597), (-0.3188996455, -1.1233354685), (-0.329383901, -1.164097859), (-0.3294412891, -1.2062650073), (-0.3294751, -1.2311082165)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.051696944, 0.1258323921, 0.1258323921, 0.1258323921, 0.1258323921], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.135953807, perimeter: 3.362902811
            with BuildLine():
                Line((0.3119741131, -0.3029167633), (0.3119741131, -0.3961824159))
                _nurbs_edge([(0.2487221409, -0.3254890422), (0.2596484761, -0.3230980763), (0.2816937401, -0.3182740001), (0.3018220399, -0.3080655701), (0.3119741131, -0.3029167633)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0334064085, 0.0674016564, 0.0674016564, 0.0674016564, 0.0674016564], 3)
                _nurbs_edge([(0.0912123967, -0.3311941604), (0.1251222681, -0.3313994296), (0.1777260076, -0.3317178598), (0.2301073178, -0.3271222063), (0.2487221409, -0.3254890422)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1016471908, 0.1576833566, 0.1576833566, 0.1576833566, 0.1576833566], 3)
                Line((-0.0278500866, -0.3311941604), (0.0912123967, -0.3311941604))
                _nurbs_edge([(-0.1102016818, -0.3356590251), (-0.0995464975, -0.3343716112), (-0.0722108302, -0.3310687759), (-0.0446611577, -0.3311466444), (-0.0278500866, -0.3311941604)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321728054, 0.0825387042, 0.0825387042, 0.0825387042, 0.0825387042], 3)
                _nurbs_edge([(-0.1709731769, -0.3634402732), (-0.162155015, -0.3572659477), (-0.1436226873, -0.3442899302), (-0.1216953983, -0.3386272535), (-0.1102016818, -0.3356590251)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0320249975, 0.06730402, 0.06730402, 0.06730402, 0.06730402], 3)
                _nurbs_edge([(-0.2109087061, -0.425451992), (-0.2057334634, -0.4127279266), (-0.1962860993, -0.3895002473), (-0.1788553877, -0.3715551091), (-0.1709731769, -0.3634402732)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0407404555, 0.0743713749, 0.0743713749, 0.0743713749, 0.0743713749], 3)
                _nurbs_edge([(-0.226783688, -0.5350886564), (-0.2264379508, -0.5145570084), (-0.2258104572, -0.4772932192), (-0.2155264283, -0.4415164385), (-0.2109087061, -0.425451992)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0612721851, 0.1112055784, 0.1112055784, 0.1112055784, 0.1112055784], 3)
                _nurbs_edge([(-0.2081801843, -0.6546472291), (-0.2136018137, -0.6362087401), (-0.2250715325, -0.5972012265), (-0.2261925598, -0.5565332556), (-0.226783688, -0.5350886564)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0574078285, 0.1214490325, 0.1214490325, 0.1214490325, 0.1214490325], 3)
                _nurbs_edge([(-0.155098195, -0.7335261683), (-0.1660861298, -0.7229657215), (-0.189422282, -0.7005374673), (-0.2016892007, -0.6705270848), (-0.2081801843, -0.6546472291)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0452093731, 0.0960155694, 0.0960155694, 0.0960155694, 0.0960155694], 3)
                _nurbs_edge([(-0.0645610642, -0.7727175931), (-0.0818875374, -0.7684589234), (-0.1143190129, -0.7604875987), (-0.1421403642, -0.7420933253), (-0.155098195, -0.7335261683)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0530555525, 0.0993087182, 0.0993087182, 0.0993087182, 0.0993087182], 3)
                Line((-0.0526547979, -0.6854050736), (-0.0645610642, -0.7727175931))
                _nurbs_edge([(-0.1307895731, -0.6410046796), (-0.1211098361, -0.650565123), (-0.0991601962, -0.6722442544), (-0.0693299688, -0.680686075), (-0.0526547979, -0.6854050736)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0402021032, 0.0911617424, 0.0911617424, 0.0911617424, 0.0911617424], 3)
                _nurbs_edge([(-0.1528657626, -0.5479871015), (-0.152575363, -0.5666421544), (-0.1520649757, -0.5994290417), (-0.137197686, -0.6284821725), (-0.1307895731, -0.6410046796)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0550338415, 0.0967238402, 0.0967238402, 0.0967238402, 0.0967238402], 3)
                _nurbs_edge([(-0.1226040374, -0.4462878684), (-0.1314047846, -0.460074024), (-0.1510916532, -0.4909130233), (-0.1522340557, -0.5276647402), (-0.1528657626, -0.5479871015)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0482159648, 0.1078569074, 0.1078569074, 0.1078569074, 0.1078569074], 3)
                _nurbs_edge([(-0.0457095455, -0.4209871273), (-0.0618455135, -0.4213434039), (-0.0902970534, -0.4219716042), (-0.1128442343, -0.438942028), (-0.1226040374, -0.4462878684)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0469369384, 0.0827609582, 0.0827609582, 0.0827609582, 0.0827609582], 3)
                _nurbs_edge([(-0.0223931026, -0.4214831571), (-0.0273950672, -0.421343251), (-0.035166182, -0.4211258912), (-0.0429395813, -0.4210235835), (-0.0457095455, -0.4209871273)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0150114515, 0.0233219791, 0.0233219791, 0.0233219791, 0.0233219791], 3)
                _nurbs_edge([(0.0083647419, -0.5807293038), (0.0045540395, -0.5492519006), (-0.0019634541, -0.4954156905), (-0.0163981887, -0.4431780566), (-0.0223931026, -0.4214831571)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0949443583, 0.1623845645, 0.1623845645, 0.1623845645, 0.1623845645], 3)
                _nurbs_edge([(0.0217592169, -0.6601042728), (0.0193394344, -0.6491329507), (0.0135545882, -0.6229043902), (0.0102734124, -0.5962400415), (0.0083647419, -0.5807293038)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0336880427, 0.0805362247, 0.0805362247, 0.0805362247, 0.0805362247], 3)
                _nurbs_edge([(0.0510287929, -0.7243484239), (0.0449429872, -0.7144335915), (0.0325411913, -0.6942289165), (0.0253974059, -0.6716190381), (0.0217592169, -0.6601042728)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0347595837, 0.0708338845, 0.0708338845, 0.0708338845, 0.0708338845], 3)
                _nurbs_edge([(0.1023744989, -0.7704851608), (0.0922860355, -0.7642337551), (0.0724092868, -0.7519169518), (0.0580835084, -0.7334449453), (0.0510287929, -0.7243484239)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0352872579, 0.0695245578, 0.0695245578, 0.0695245578, 0.0695245578], 3)
                _nurbs_edge([(0.1730678726, -0.7880964856), (0.1605317866, -0.7874081335), (0.1358334007, -0.7860519539), (0.1134143694, -0.7756214734), (0.1023744989, -0.7704851608)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0372819294, 0.0734522306, 0.0734522306, 0.0734522306, 0.0734522306], 3)
                _nurbs_edge([(0.2814643432, -0.7414636592), (0.2662042182, -0.7550642594), (0.2352820159, -0.7826237002), (0.1939848586, -0.7862564831), (0.1730678726, -0.7880964856)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0596389385, 0.1208487693, 0.1208487693, 0.1208487693, 0.1208487693], 3)
                _nurbs_edge([(0.3238803793, -0.6080144624), (0.322822867, -0.6344375152), (0.3208784558, -0.6830206677), (0.2938106891, -0.7231565772), (0.2814643432, -0.7414636592)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0774993635, 0.1424953968, 0.1424953968, 0.1424953968, 0.1424953968], 3)
                _nurbs_edge([(0.3065170694, -0.5095398406), (0.3115808904, -0.5252654664), (0.3218916138, -0.5572852746), (0.3232096562, -0.5909057403), (0.3238803793, -0.6080144624)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0493134703, 0.1004098589, 0.1004098589, 0.1004098589, 0.1004098589], 3)
                _nurbs_edge([(0.2469858576, -0.4140417556), (0.2597568438, -0.4297872649), (0.283587491, -0.459168369), (0.2992487655, -0.4935729023), (0.3065170694, -0.5095398406)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0605249955, 0.1129395795, 0.1129395795, 0.1129395795, 0.1129395795], 3)
                _nurbs_edge([(0.3119741131, -0.3961824159), (0.302051224, -0.4004260047), (0.2812148559, -0.4093368147), (0.2587515034, -0.4124245108), (0.2469858576, -0.4140417556)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0322252884, 0.0676675881, 0.0676675881, 0.0676675881, 0.0676675881], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(0.2313588906, -0.4949051122), (0.2232468936, -0.4824502974), (0.2072715434, -0.4579224249), (0.182022981, -0.4431440907), (0.1695951868, -0.4358699302)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0439192187, 0.0864922536, 0.0864922536, 0.0864922536, 0.0864922536], 3)
                _nurbs_edge([(0.25393111, -0.5866824369), (0.2531070201, -0.5701710825), (0.2515062146, -0.538097559), (0.2379408472, -0.5090157113), (0.2313588906, -0.4949051122)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0490668004, 0.0953129061, 0.0953129061, 0.0953129061, 0.0953129061], 3)
                _nurbs_edge([(0.2301186372, -0.665809391), (0.2370457934, -0.655022092), (0.2524445149, -0.6310424663), (0.2534035174, -0.6024258123), (0.25393111, -0.5866824369)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.037787097, 0.083998825, 0.083998825, 0.083998825, 0.083998825], 3)
                _nurbs_edge([(0.1705873657, -0.6928464751), (0.1820072809, -0.6917088278), (0.2049036934, -0.6894278967), (0.2216998202, -0.6736951859), (0.2301186372, -0.665809391)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0334326152, 0.0670308789, 0.0670308789, 0.0670308789, 0.0670308789], 3)
                _nurbs_edge([(0.1281713892, -0.6804441194), (0.1347377183, -0.6840614402), (0.1479532653, -0.6913417443), (0.1630111841, -0.6923428052), (0.1705873657, -0.6928464751)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0221968381, 0.0446738742, 0.0446738742, 0.0446738742, 0.0446738742], 3)
                _nurbs_edge([(0.0991498876, -0.6452214698), (0.1027612127, -0.6523425073), (0.1098172171, -0.6662559795), (0.1221504254, -0.6757897947), (0.1281713892, -0.6804441194)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0236203316, 0.0461506949, 0.0461506949, 0.0461506949, 0.0461506949], 3)
                _nurbs_edge([(0.0812905479, -0.5673347692), (0.0835541021, -0.5831352717), (0.0873480829, -0.6096187574), (0.0957576235, -0.6349879666), (0.0991498876, -0.6452214698)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0477554592, 0.0800437214, 0.0800437214, 0.0800437214, 0.0800437214], 3)
                _nurbs_edge([(0.0475561071, -0.4214831571), (0.054173023, -0.4416204503), (0.0698016316, -0.489183073), (0.0770887087, -0.5387523642), (0.0812905479, -0.5673347692)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0634831431, 0.1499419382, 0.1499419382, 0.1499419382, 0.1499419382], 3)
                Line((0.0802983094, -0.4214831571), (0.0475561071, -0.4214831571))
                _nurbs_edge([(0.1695951868, -0.4358699302), (0.1572122913, -0.4316951709), (0.1283203574, -0.4219545677), (0.0977604428, -0.4216545749), (0.0802983094, -0.4214831571)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0389783226, 0.0909447323, 0.0909447323, 0.0909447323, 0.0909447323], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1109780183, perimeter: 2.7738484327
            with BuildLine():
                _nurbs_edge([(-0.1493930768, 0.0364114066), (-0.1479452433, 0.0181159626), (-0.1450781754, -0.0181135328), (-0.1237406093, -0.0475110688), (-0.1131782483, -0.0620632152)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0539097829, 0.1067546782, 0.1067546782, 0.1067546782, 0.1067546782], 3)
                _nurbs_edge([(-0.1332700502, 0.0986711999), (-0.1379708285, 0.0892365931), (-0.1477329359, 0.0696437429), (-0.1488262366, 0.047758289), (-0.1493930768, 0.0364114066)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.031268259, 0.0649348012, 0.0649348012, 0.0649348012, 0.0649348012], 3)
                _nurbs_edge([(-0.0901098799, 0.1356301327), (-0.0987158009, 0.1314051605), (-0.1162571839, 0.1227934319), (-0.1275285119, 0.1068120221), (-0.1332700502, 0.0986711999)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0282785143, 0.05763988, 0.05763988, 0.05763988, 0.05763988], 3)
                _nurbs_edge([(-0.0085024189, 0.146048071), (-0.0245087407, 0.1459622885), (-0.0521813269, 0.1458139831), (-0.078861851, 0.1386502385), (-0.0901098799, 0.1356301327)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0477581242, 0.0825668026, 0.0825668026, 0.0825668026, 0.0825668026], 3)
                Line((0.3119741131, 0.146048071), (-0.0085024189, 0.146048071))
                Line((0.3119741131, 0.235345008), (0.3119741131, 0.146048071))
                Line((-0.0119751047, 0.235345008), (0.3119741131, 0.235345008))
                _nurbs_edge([(-0.0987915348, 0.2303839942), (-0.0874353748, 0.2318156796), (-0.0586275011, 0.2354475246), (-0.029575008, 0.235383683), (-0.0119751047, 0.235345008)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0343088461, 0.0870333726, 0.0870333726, 0.0870333726, 0.0870333726], 3)
                _nurbs_edge([(-0.164771999, 0.2026027461), (-0.1548720125, 0.2087626385), (-0.1343664395, 0.2215214562), (-0.1109187823, 0.2273628141), (-0.0987915348, 0.2303839942)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0347533866, 0.0719837454, 0.0719837454, 0.0719837454, 0.0719837454], 3)
                _nurbs_edge([(-0.2096684527, 0.1428234597), (-0.2038484324, 0.1550528937), (-0.192902364, 0.1780535394), (-0.1737439105, 0.1947730109), (-0.164771999, 0.2026027461)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0401273704, 0.0754700032, 0.0754700032, 0.0754700032, 0.0754700032], 3)
                _nurbs_edge([(-0.226783688, 0.0552629252), (-0.2261404469, 0.0706521443), (-0.224883679, 0.1007196824), (-0.2146596174, 0.129011842), (-0.2096684527, 0.1428234597)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0459024369, 0.089684425, 0.089684425, 0.089684425, 0.089684425], 3)
                _nurbs_edge([(-0.1399673175, -0.1124167423), (-0.1652872493, -0.0906596292), (-0.2166766455, -0.0465013389), (-0.2233820735, 0.0210132624), (-0.226783688, 0.0552629252)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0962926935, 0.1954358886, 0.1954358886, 0.1954358886, 0.1954358886], 3)
                Line((-0.2148774814, -0.1124167423), (-0.1399673175, -0.1124167423))
                Line((-0.2148774814, -0.1927839498), (-0.2148774814, -0.1124167423))
                Line((0.3119741131, -0.1927839498), (-0.2148774814, -0.1927839498))
                Line((0.3119741131, -0.1034870128), (0.3119741131, -0.1927839498))
                Line((0.0242397238, -0.1034870128), (0.3119741131, -0.1034870128))
                _nurbs_edge([(-0.1131782483, -0.0620632152), (-0.0962498777, -0.0740617883), (-0.0555591825, -0.1029027377), (-0.0051802711, -0.1032716042), (0.0242397238, -0.1034870128)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0609710134, 0.1465559192, 0.1465559192, 0.1465559192, 0.1465559192], 3)
            make_face()
            # Profile area: 0.0470461708, perimeter: 1.2322968245
            with BuildLine():
                Line((-0.2148774814, 0.4620597382), (0.3119741131, 0.4620597382))
                Line((-0.2148774814, 0.3727629204), (-0.2148774814, 0.4620597382))
                Line((0.3119741131, 0.3727629204), (-0.2148774814, 0.3727629204))
                Line((0.3119741131, 0.4620597382), (0.3119741131, 0.3727629204))
            make_face()
            # Profile area: 0.1329179283, perimeter: 3.288463467
            with BuildLine():
                _nurbs_edge([(0.2504584838, 0.8197433968), (0.2495384837, 0.8353015459), (0.2477593368, 0.8653887503), (0.2321832547, 0.8911454349), (0.2246615935, 0.9035832902)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.045971115, 0.0889014705, 0.0889014705, 0.0889014705, 0.0889014705], 3)
                _nurbs_edge([(0.2043217469, 0.7096107026), (0.2177779849, 0.7253374551), (0.2449414032, 0.7570842451), (0.2486081654, 0.798728772), (0.2504584838, 0.8197433968)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0604847905, 0.1220975487, 0.1220975487, 0.1220975487, 0.1220975487], 3)
                _nurbs_edge([(0.0713686396, 0.6604974289), (0.0978221486, 0.6630778713), (0.1466300469, 0.667838902), (0.1861989074, 0.6964888213), (0.2043217469, 0.7096107026)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0780545318, 0.1440140753, 0.1440140753, 0.1440140753, 0.1440140753], 3)
                Line((0.0713686396, 1.0534036179), (0.0713686396, 0.6604974289))
                _nurbs_edge([(0.0475561071, 1.053899767), (0.0508636033, 1.0538682857), (0.0588028784, 1.0537927184), (0.0667388108, 1.0535469812), (0.0713686396, 1.0534036179)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0099226829, 0.0238182919, 0.0238182919, 0.0238182919, 0.0238182919], 3)
                _nurbs_edge([(-0.1548501205, 0.9869270344), (-0.1269533938, 1.0064291765), (-0.0664337067, 1.0487374926), (0.0076314831, 1.0520916943), (0.0475561071, 1.053899767)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1000853511, 0.2171270555, 0.2171270555, 0.2171270555, 0.2171270555], 3)
                _nurbs_edge([(-0.226783688, 0.8142864724), (-0.2240406703, 0.8476564025), (-0.2186651361, 0.9130519711), (-0.1758282697, 0.9626418081), (-0.1548501205, 0.9869270344)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0976641942, 0.1913940328, 0.1913940328, 0.1913940328, 0.1913940328], 3)
                _nurbs_edge([(-0.1533618521, 0.6366848965), (-0.1747731933, 0.6616133402), (-0.2186360202, 0.7126812298), (-0.2240251998, 0.7798868298), (-0.226783688, 0.8142864724)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0959952635, 0.1966538943, 0.1966538943, 0.1966538943, 0.1966538943], 3)
                _nurbs_edge([(0.0530131508, 0.5682239552), (0.0123154703, 0.5700811884), (-0.0632271846, 0.5735285673), (-0.1249099304, 0.6167489609), (-0.1533618521, 0.6366848965)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1193044266, 0.221451764, 0.221451764, 0.221451764, 0.221451764], 3)
                _nurbs_edge([(0.2526909161, 0.6359407921), (0.2251789712, 0.6162189761), (0.1657421968, 0.5736119874), (0.0924044861, 0.5701067156), (0.0530131508, 0.5682239552)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0994588633, 0.2148708148, 0.2148708148, 0.2148708148, 0.2148708148], 3)
                _nurbs_edge([(0.3238803793, 0.8192474862), (0.3214974639, 0.7832883841), (0.3169405944, 0.7145234873), (0.273442589, 0.6613218123), (0.2526909161, 0.6359407921)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1051387531, 0.2010577321, 0.2010577321, 0.2010577321, 0.2010577321], 3)
                _nurbs_edge([(0.2792319108, 0.9700598736), (0.2922425604, 0.9482197373), (0.3198636943, 0.9018539256), (0.3224907637, 0.8478260758), (0.3238803793, 0.8192474862)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0750994112, 0.1594333068, 0.1594333068, 0.1594333068, 0.1594333068], 3)
                _nurbs_edge([(0.1537202049, 1.050923111), (0.1788956735, 1.0424455888), (0.2276148253, 1.0260400277), (0.2624147418, 0.9882985576), (0.2792319108, 0.9700598736)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0782667487, 0.1514605215, 0.1514605215, 0.1514605215, 0.1514605215], 3)
                Line((0.1423100282, 0.9586498757), (0.1537202049, 1.050923111))
                _nurbs_edge([(0.2246615935, 0.9035832902), (0.2140757936, 0.9147982796), (0.1908916859, 0.9393603838), (0.1594147056, 0.9518584126), (0.1423100282, 0.9586498757)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0457208868, 0.1001339499, 0.1001339499, 0.1001339499, 0.1001339499], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-0.1533618521, 0.8152787705), (-0.1517359842, 0.795682301), (-0.1485254544, 0.7569860153), (-0.1241951072, 0.7267613747), (-0.1121860694, 0.7118430157)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.057544989, 0.1136315564, 0.1136315564, 0.1136315564, 0.1136315564], 3)
                _nurbs_edge([(-0.1017680716, 0.9259076138), (-0.1168161763, 0.9105830665), (-0.1470441002, 0.8797998378), (-0.1512498261, 0.8368481785), (-0.1533618521, 0.8152787705)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0624281996, 0.1254028269, 0.1254028269, 0.1254028269, 0.1254028269], 3)
                _nurbs_edge([(-0.0020532559, 0.9596419354), (-0.021994626, 0.9573835937), (-0.0578034191, 0.953328281), (-0.0882685201, 0.9343272575), (-0.1017680716, 0.9259076138)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0592754483, 0.1064411452, 0.1064411452, 0.1064411452, 0.1064411452], 3)
                Line((-0.0020532559, 0.6654584427), (-0.0020532559, 0.9596419354))
                _nurbs_edge([(-0.1121860694, 0.7118430157), (-0.0968291846, 0.6994059266), (-0.0646786945, 0.6733681909), (-0.0235411777, 0.6681724205), (-0.0020532559, 0.6654584427)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0580993683, 0.1216342494, 0.1216342494, 0.1216342494, 0.1216342494], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.064943206, perimeter: 1.633140564
            with BuildLine():
                Line((-0.4152993511, 1.2503528615), (0.3119741131, 1.2503528615))
                Line((-0.4152993511, 1.1610560437), (-0.4152993511, 1.2503528615))
                Line((0.3119741131, 1.1610560437), (-0.4152993511, 1.1610560437))
                Line((0.3119741131, 1.2503528615), (0.3119741131, 1.1610560437))
            make_face()
        # OneSide extrude, distance=-3.556
        extrude(amount=-3.556, mode=Mode.SUBTRACT)
    return part.part


def model_23632_5c8e8093_0000():
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
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.1268109384, perimeter: 65.5404511767
            with BuildLine():
                CenterArc((0, 0), 5.4310867772, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0.0062892481, -5.3729868848)):
                Circle(1)
        # Symmetric extrude, each_side=9
        extrude(amount=9, both=True, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.863556222, perimeter: 5.9987089245
            with Locations((0.0302591559, 5.2697492192)):
                Circle(0.9547241775)
        # Symmetric extrude, each_side=19
        extrude(amount=19, both=True, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.110176565, perimeter: 3.7512404116
            with BuildLine():
                _nurbs_edge([(1.0413236838, 0.1847502712), (1.0389225491, 0.1606423668), (1.0341077276, 0.1123005311), (1.000879311, 0.0768486782), (0.9842217896, 0.0590765403)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0705756699, 0.1415202826, 0.1415202826, 0.1415202826, 0.1415202826], 3)
                _nurbs_edge([(1.0146550887, 0.2685232019), (1.0224316809, 0.255677217), (1.0380391162, 0.2298956313), (1.0402262937, 0.1998335561), (1.0413236838, 0.1847502712)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0443636266, 0.0890367418, 0.0890367418, 0.0890367418, 0.0890367418], 3)
                _nurbs_edge([(0.901166312, 0.3301965559), (0.9249482589, 0.325116619), (0.9690605098, 0.3156940327), (1.0002709345, 0.2834046313), (1.0146550887, 0.2685232019)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.071050723, 0.1317893501, 0.1317893501, 0.1317893501, 0.1317893501], 3)
                _nurbs_edge([(0.9361974246, 0.3492419569), (0.9307916481, 0.3459091446), (0.9194620387, 0.3389241239), (0.907448005, 0.3331930973), (0.901166312, 0.3301965559)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.019037367, 0.0398991581, 0.0398991581, 0.0398991581, 0.0398991581], 3)
                _nurbs_edge([(0.9628505327, 0.3713325366), (0.9589802751, 0.3673073577), (0.9509337594, 0.3589387508), (0.9412325122, 0.3525551421), (0.9361974246, 0.3492419569)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.016696854, 0.0347138385, 0.0347138385, 0.0347138385, 0.0347138385], 3)
                _nurbs_edge([(1.0001547579, 0.4688238895), (0.9987121793, 0.4504090805), (0.9958757666, 0.4142016971), (0.9737320955, 0.3854575982), (0.9628505327, 0.3713325366)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0541227495, 0.106416697, 0.106416697, 0.106416697, 0.106416697], 3)
                _nurbs_edge([(0.9475878889, 0.5754411623), (0.9629153366, 0.5614315533), (0.9942449392, 0.5327956386), (0.9981567372, 0.4904517752), (1.0001547579, 0.4688238895)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0600575543, 0.122758815, 0.122758815, 0.122758815, 0.122758815], 3)
                _nurbs_edge([(0.8257260856, 0.6066489806), (0.8492002874, 0.6058910306), (0.8922619871, 0.604500627), (0.9302900459, 0.5845267089), (0.9475878889, 0.5754411623)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0693662894, 0.1272473644, 0.1272473644, 0.1272473644, 0.1272473644], 3)
                Line((0.6208535988, 0.6066185481), (0.8257260856, 0.6066489806))
                Line((0.6209422943, 0.0095180584), (0.6208535988, 0.6066185481))
                Line((0.8509479137, 0.0095522242), (0.6209422943, 0.0095180584))
                _nurbs_edge([(0.9842217896, 0.0590765403), (0.9647511267, 0.0446359488), (0.9251522825, 0.0152671114), (0.8759550018, 0.0114781578), (0.8509479137, 0.0095522242)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0711873053, 0.1447785844, 0.1447785844, 0.1447785844, 0.1447785844], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(0.9361810205, 0.4596750871), (0.9351119037, 0.4719117068), (0.9329794297, 0.4963190236), (0.9178306042, 0.515570028), (0.9102766495, 0.5251695323)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0360016079, 0.0718092635, 0.0718092635, 0.0718092635, 0.0718092635], 3)
                _nurbs_edge([(0.8996357022, 0.3797008476), (0.9102965113, 0.3908728336), (0.9317027628, 0.4133054971), (0.9346843385, 0.4441778707), (0.9361810205, 0.4596750871)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0449384994, 0.0902337534, 0.0902337534, 0.0902337534, 0.0902337534], 3)
                _nurbs_edge([(0.7945384048, 0.3492209143), (0.8152928053, 0.3499105714), (0.853076188, 0.351166092), (0.885170697, 0.3708357339), (0.8996357022, 0.3797008476)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0610249467, 0.1110959058, 0.1110959058, 0.1110959058, 0.1110959058], 3)
                Line((0.681058911, 0.3492040577), (0.7945384048, 0.3492209143))
                Line((0.6810284785, 0.5540765742), (0.681058911, 0.3492040577))
                Line((0.8219258702, 0.5540975036), (0.6810284785, 0.5540765742))
                _nurbs_edge([(0.9102766495, 0.5251695323), (0.8981197355, 0.5335942728), (0.8716655036, 0.5519270533), (0.839376577, 0.5533360205), (0.8219258702, 0.5540975036)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0435018391, 0.0946628175, 0.0946628175, 0.0946628175, 0.0946628175], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(0.9750639366, 0.1839788602), (0.9734196883, 0.2010847716), (0.9701910011, 0.2346743671), (0.9448414776, 0.2568613596), (0.9324015082, 0.2677493555)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.049523535, 0.0972456524, 0.0972456524, 0.0972456524, 0.0972456524], 3)
                _nurbs_edge([(0.9331889365, 0.0948645295), (0.945404462, 0.1073119883), (0.9697664159, 0.132136497), (0.9733014385, 0.1667307786), (0.9750639366, 0.1839788602)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0507005017, 0.1011142169, 0.1011142169, 0.1011142169, 0.1011142169], 3)
                _nurbs_edge([(0.8258069749, 0.0620994022), (0.8462084573, 0.0631315983), (0.8848333313, 0.0650857918), (0.9176879688, 0.0853185989), (0.9331889365, 0.0948645295)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0601555811, 0.1138888681, 0.1138888681, 0.1138888681, 0.1138888681], 3)
                Line((0.6811015618, 0.0620779071), (0.8258069749, 0.0620994022))
                Line((0.6810667171, 0.2966531165), (0.6811015618, 0.0620779071))
                Line((0.8113015532, 0.2966724621), (0.6810667171, 0.2966531165))
                _nurbs_edge([(0.9324015082, 0.2677493555), (0.915630568, 0.2761588488), (0.8776798726, 0.2951885582), (0.8350774003, 0.2961409471), (0.8113015532, 0.2966724621)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0556275913, 0.1258787963, 0.1258787963, 0.1258787963, 0.1258787963], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0470854307, perimeter: 1.9085728634
            with BuildLine():
                _nurbs_edge([(0.1738167316, 0.4260510978), (0.1884130617, 0.4254683175), (0.2170605634, 0.4243245233), (0.2442565834, 0.4152716807), (0.2575958249, 0.4108313967)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0435783103, 0.0855290139, 0.0855290139, 0.0855290139, 0.0855290139], 3)
                _nurbs_edge([(0.0260740827, 0.3635773114), (0.0471805848, 0.3817953147), (0.0896904059, 0.4184875177), (0.1456443937, 0.4235181958), (0.1738167316, 0.4260510978)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0814547, 0.1640548822, 0.1640548822, 0.1640548822, 0.1640548822], 3)
                _nurbs_edge([(-0.0325473344, 0.2127702811), (-0.030150736, 0.2409039475), (-0.0253782605, 0.2969280312), (0.0089730179, 0.3414252851), (0.0260740827, 0.3635773114)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0828003358, 0.1648847637, 0.1648847637, 0.1648847637, 0.1648847637], 3)
                _nurbs_edge([(0.0268807374, 0.0604575301), (0.0095511023, 0.0827145414), (-0.0253691966, 0.127563812), (-0.0301427278, 0.1842269393), (-0.0325473344, 0.2127702811)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0827125439, 0.1666709516, 0.1666709516, 0.1666709516, 0.1666709516], 3)
                _nurbs_edge([(0.1731184574, -0.0004493907), (0.1456715761, 0.0021139072), (0.0906216253, 0.0072550896), (0.0481678501, 0.0426898713), (0.0268807374, 0.0604575301)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0806585143, 0.1617760207, 0.1617760207, 0.1617760207, 0.1617760207], 3)
                _nurbs_edge([(0.2393767338, 0.0102230074), (0.2284685781, 0.0071115185), (0.2068033948, 0.000931649), (0.1842944319, 0.0000088101), (0.1731184574, -0.0004493907)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.033896384, 0.0673231478, 0.0673231478, 0.0673231478, 0.0673231478], 3)
                _nurbs_edge([(0.3124858109, 0.0460294371), (0.2998723286, 0.0384302316), (0.276531497, 0.0243681534), (0.2510759825, 0.0146770145), (0.2393767338, 0.0102230074)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0440701513, 0.0815503562, 0.0815503562, 0.0815503562, 0.0815503562], 3)
                Line((0.3124750634, 0.1183821437), (0.3124858109, 0.0460294371))
                _nurbs_edge([(0.2462228961, 0.0665829584), (0.2574870096, 0.0734512126), (0.2815695711, 0.088135471), (0.3017393016, 0.1078752387), (0.3124750634, 0.1183821437)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0394481784, 0.0843398093, 0.0843398093, 0.0843398093, 0.0843398093], 3)
                _nurbs_edge([(0.1738726188, 0.0498168686), (0.1866788216, 0.0504616347), (0.2118080333, 0.0517268391), (0.2348992775, 0.0616948079), (0.2462228961, 0.0665829584)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0381207977, 0.0748032504, 0.0748032504, 0.0748032504, 0.0748032504], 3)
                _nurbs_edge([(0.0687637759, 0.0962593213), (0.0836485221, 0.0827112902), (0.1135073576, 0.0555339082), (0.1537107664, 0.0517263461), (0.1738726188, 0.0498168686)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0586837205, 0.1177196802, 0.1177196802, 0.1177196802, 0.1177196802], 3)
                _nurbs_edge([(0.0268579978, 0.213540674), (0.0284797372, 0.1916672594), (0.031666808, 0.1486812397), (0.0565448923, 0.1135258893), (0.0687637759, 0.0962593213)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0644506912, 0.1266596335, 0.1266596335, 0.1266596335, 0.1266596335], 3)
                _nurbs_edge([(0.0672060204, 0.329311078), (0.0554361978, 0.3121299632), (0.0315215594, 0.2772203335), (0.0284286843, 0.2349879686), (0.0268579978, 0.213540674)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0613085638, 0.1245704534, 0.1245704534, 0.1245704534, 0.1245704534], 3)
                _nurbs_edge([(0.1707776918, 0.3765461273), (0.1506929544, 0.3746154389), (0.1107239797, 0.3707733356), (0.0816634137, 0.3430855329), (0.0672060204, 0.329311078)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0587006893, 0.1168153862, 0.1168153862, 0.1168153862, 0.1168153862], 3)
                _nurbs_edge([(0.1981958099, 0.3742653752), (0.193633981, 0.37493111), (0.1845416629, 0.3762580061), (0.1753551274, 0.3764503078), (0.1707776918, 0.3765461273)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.013815637, 0.0275363613, 0.0275363613, 0.0275363613, 0.0275363613], 3)
                _nurbs_edge([(0.2248530978, 0.3674148902), (0.2205141289, 0.3690316847), (0.2118691049, 0.3722530094), (0.2027419918, 0.3735962914), (0.1981958099, 0.3742653752)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.013848353, 0.0275916572, 0.0275916572, 0.0275916572, 0.0275916572], 3)
                _nurbs_edge([(0.3124466672, 0.3095457112), (0.298550373, 0.3218786755), (0.2720924185, 0.345360116), (0.240060944, 0.3603147539), (0.2248530978, 0.3674148902)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0553977834, 0.1054750289, 0.1054750289, 0.1054750289, 0.1054750289], 3)
                Line((0.3124360328, 0.3811368195), (0.3124466672, 0.3095457112))
                _nurbs_edge([(0.2575958249, 0.4108313967), (0.2660838031, 0.4071669602), (0.2852333559, 0.3988997003), (0.3027073377, 0.3874894904), (0.3124360328, 0.3811368195)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0276869232, 0.062463898, 0.062463898, 0.062463898, 0.062463898], 3)
            make_face()
            # Profile area: 0.0641411922, perimeter: 2.5202389592
            with BuildLine():
                _nurbs_edge([(-0.2526836437, 0.4259877439), (-0.2270733595, 0.4237086158), (-0.1768017863, 0.4192348134), (-0.1408420214, 0.3839237851), (-0.1232015519, 0.3666015607)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0746074326, 0.1464502692, 0.1464502692, 0.1464502692, 0.1464502692], 3)
                _nurbs_edge([(-0.3935719313, 0.364276574), (-0.3734378267, 0.3822725505), (-0.3332100724, 0.4182283447), (-0.2795077848, 0.4234030121), (-0.2526836437, 0.4259877439)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0787983127, 0.1574382982, 0.1574382982, 0.1574382982, 0.1574382982], 3)
                _nurbs_edge([(-0.4499084105, 0.2127082848), (-0.4478023025, 0.2414195935), (-0.4436904701, 0.297473743), (-0.4100039779, 0.3423743547), (-0.3935719313, 0.364276574)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0843901653, 0.1647580397, 0.1647580397, 0.1647580397, 0.1647580397], 3)
                _nurbs_edge([(-0.3874333797, 0.0565879647), (-0.4056476337, 0.078566363), (-0.4431476205, 0.1238160694), (-0.4476122912, 0.1825184496), (-0.4499084105, 0.2127082848)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0834918266, 0.1718951763, 0.1718951763, 0.1718951763, 0.1718951763], 3)
                _nurbs_edge([(-0.2465274435, -0.0005117264), (-0.2730958546, 0.0018088483), (-0.3259273595, 0.0064233304), (-0.3670105138, 0.0399309677), (-0.3874333797, 0.0565879647)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.078049466, 0.1552020079, 0.1552020079, 0.1552020079, 0.1552020079], 3)
                _nurbs_edge([(-0.1505685343, 0.0246356013), (-0.1662918642, 0.0173049561), (-0.1967746218, 0.0030930631), (-0.2302965039, 0.0006642696), (-0.2465274435, -0.0005117264)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0515512129, 0.0999421332, 0.0999421332, 0.0999421332, 0.0999421332], 3)
                _nurbs_edge([(-0.1216299882, 0.0413953022), (-0.1265374785, 0.0382745461), (-0.1359523456, 0.032287473), (-0.1458364904, 0.0271129224), (-0.1505685343, 0.0246356013)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0174381434, 0.033454534, 0.033454534, 0.033454534, 0.033454534], 3)
                _nurbs_edge([(-0.0873612957, 0.065771838), (-0.0932326252, 0.0614122865), (-0.1044898725, 0.0530536088), (-0.1160832515, 0.045168063), (-0.1216299882, 0.0413953022)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0219358904, 0.0420582334, 0.0420582334, 0.0420582334, 0.0420582334], 3)
                Line((-0.0873711382, 0.1320316983), (-0.0873612957, 0.065771838))
                _nurbs_edge([(-0.1185926454, 0.1023243372), (-0.1135486099, 0.1069258162), (-0.1029335714, 0.1166095062), (-0.0927275041, 0.1267236014), (-0.0873711382, 0.1320316983)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0204804669, 0.0431005969, 0.0431005969, 0.0431005969, 0.0431005969], 3)
                _nurbs_edge([(-0.1460074887, 0.081756841), (-0.1415172254, 0.0848031753), (-0.1320534441, 0.0912236988), (-0.1232297679, 0.0985002685), (-0.1185926454, 0.1023243372)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0162690372, 0.0342889939, 0.0342889939, 0.0342889939, 0.0342889939], 3)
                _nurbs_edge([(-0.2427268887, 0.0497549853), (-0.225906394, 0.0512471681), (-0.191196066, 0.054326397), (-0.1613765693, 0.0724274766), (-0.1460074887, 0.081756841)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0499583252, 0.103092679, 0.103092679, 0.103092679, 0.103092679], 3)
                _nurbs_edge([(-0.3501203837, 0.0954354706), (-0.3351352204, 0.0821112781), (-0.3045105815, 0.0548811054), (-0.2636127215, 0.0514878582), (-0.2427268887, 0.0497549853)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0585005292, 0.1195554266, 0.1195554266, 0.1195554266, 0.1195554266], 3)
                _nurbs_edge([(-0.3905055136, 0.2294724514), (-0.3895677785, 0.2029265598), (-0.3878564738, 0.1544820572), (-0.3618680576, 0.1138173443), (-0.3501203837, 0.0954354706)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0779590579, 0.1422701425, 0.1422701425, 0.1422701425, 0.1422701425], 3)
                Line((-0.080531085, 0.2295184961), (-0.3905055136, 0.2294724514))
                _nurbs_edge([(-0.1232015519, 0.3666015607), (-0.1107676694, 0.346734061), (-0.0845740159, 0.3048804886), (-0.0819234514, 0.2554728109), (-0.080531085, 0.2295184961)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0691523612, 0.1456787921, 0.1456787921, 0.1456787921, 0.1456787921], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-0.2564847107, 0.3787674851), (-0.2715179643, 0.3776203127), (-0.3010466777, 0.3753670065), (-0.3247924549, 0.3577171278), (-0.3364491077, 0.3490529133)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0442297866, 0.0868773137, 0.0868773137, 0.0868773137, 0.0868773137], 3)
                _nurbs_edge([(-0.184128098, 0.352883591), (-0.1947183189, 0.3604336201), (-0.21637034, 0.3758698787), (-0.2429205003, 0.377787693), (-0.2564847107, 0.3787674851)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0382385759, 0.0781799041, 0.0781799041, 0.0781799041, 0.0781799041], 3)
                _nurbs_edge([(-0.1445130811, 0.2759670878), (-0.1479990604, 0.2917223088), (-0.1544665236, 0.320952635), (-0.1747688005, 0.3428082217), (-0.184128098, 0.352883591)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.047388692, 0.0879192317, 0.0879192317, 0.0879192317, 0.0879192317], 3)
                Line((-0.382896312, 0.2759316775), (-0.1445130811, 0.2759670878))
                _nurbs_edge([(-0.3364491077, 0.3490529133), (-0.3461036415, 0.33884383), (-0.366291864, 0.3174960103), (-0.3772031087, 0.290182931), (-0.382896312, 0.2759316775)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0417605913, 0.0873239592, 0.0873239592, 0.0873239592, 0.0873239592], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0327424812, perimeter: 1.3038725853
            with BuildLine():
                Line((-0.5108068463, 0.0093499442), (-0.5656426421, 0.0093417987))
                Line((-0.5108955418, 0.6064504339), (-0.5108068463, 0.0093499442))
                Line((-0.5657313376, 0.6064422884), (-0.5108955418, 0.6064504339))
                Line((-0.5656426421, 0.0093417987), (-0.5657313376, 0.6064422884))
            make_face()
            # Profile area: 0.0825765669, perimeter: 2.8949463285
            with BuildLine():
                Line((-1.0667805339, 0.0092673578), (-1.1330404035, 0.0092575154))
                Line((-0.9921732921, 0.2133893331), (-1.0667805339, 0.0092673578))
                Line((-0.7652142002, 0.2134230465), (-0.9921732921, 0.2133893331))
                Line((-0.6935927428, 0.0093227925), (-0.7652142002, 0.2134230465))
                Line((-0.6235248312, 0.0093332007), (-0.6935927428, 0.0093227925))
                Line((-0.8460029838, 0.6064006558), (-0.6235248312, 0.0093332007))
                Line((-0.9046467862, 0.6063919447), (-0.8460029838, 0.6064006558))
                Line((-1.1330404035, 0.0092575154), (-0.9046467862, 0.6063919447))
            make_face()
            with BuildLine():
                Line((-0.8741718456, 0.5348053319), (-0.9739025145, 0.2659429894))
                Line((-0.7819773784, 0.2659714987), (-0.8741718456, 0.5348053319))
                Line((-0.9739025145, 0.2659429894), (-0.7819773784, 0.2659714987))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)
    return part.part


def model_23724_f9f5a141_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.283920012, perimeter: 45.8829607057
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9793260902, perimeter: 13.1031958439
            with BuildLine():
                CenterArc((0, 0), 3.81, 45, 90)
                Line((2.6940768363, 2.6940768363), (2.9185832393, 2.9185832393))
                CenterArc((0, 0), 4.1275, 45, 90)
                Line((-2.6940768363, 2.6940768363), (-2.9185832393, 2.9185832393))
            make_face()
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, -3.81)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 3.81)):
                Circle(0.635)
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.8241470412, perimeter: 4.7877873569
            with Locations((0, -3.8100001216)):
                Circle(0.7620000243)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_23726_f87337ef_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.283920012, perimeter: 45.8829607057
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9793260902, perimeter: 13.1031958439
            with BuildLine():
                Line((2.6940768363, 2.6940768363), (2.9185832393, 2.9185832393))
                CenterArc((0, 0), 4.1275, 45, 90)
                Line((-2.6940768363, 2.6940768363), (-2.9185832393, 2.9185832393))
                CenterArc((0, 0), 3.81, 45, 90)
            make_face()
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.ADD)
    return part.part


def model_23956_ee17fe48_0012():
    """Model: shaft v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=18
        extrude(amount=18)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((-4, 2.5), (0, 2.5))
                CenterArc((-2, 2.5), 2, -180, 180)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((-2, 2.5), 2, 0, 180)
                Line((-4, 2.5), (0, 2.5))
            make_face()
            # Profile area: 7.4336293856, perimeter: 22.5663706144
            with BuildLine():
                CenterArc((-2, 2.5), 2, -180, 180)
                Line((-4, -2.5), (-4, 2.5))
                CenterArc((-2, -2.5), 2, 0, 180)
                Line((0, 2.5), (0, -2.5))
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((-2, -2.5), 2, 0, 180)
                Line((0, -2.5), (-4, -2.5))
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((0, -2.5), (-4, -2.5))
                CenterArc((-2, -2.5), 2, -180, 180)
            make_face()
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True, mode=Mode.ADD)

        # Sketch10 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3768, perimeter: 7.3768
            with BuildLine():
                Line((2, -2.4384), (0, -2.4384))
                Line((2, -2.4384), (2, -0.75))
                Line((0, -0.75), (2, -0.75))
                Line((0, -2.4384), (0, -0.75))
            make_face()
            # Profile area: 3.2630125779, perimeter: 7.7414470576
            with BuildLine():
                Line((4.6981, -2.4384), (2, -2.4384))
                CenterArc((2.0000070735, -3.75), 3, 25.9253661295, 64.0747689644)
                Line((2, -2.4384), (2, -0.75))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(18, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_24009_c40b0d48_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            Circle(1.7)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0995574288, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            Circle(1.7)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_24032_d6172503_0020():
    """Model: mounting bracket left v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.5396849313, perimeter: 34.0231624563
            with BuildLine():
                Line((-1.8750788263, 2.5370118457), (-1.8750788263, -6.5116881543))
                Line((-1.8750788263, 2.5370118457), (-2.3304788263, 2.5370118457))
                Line((-2.3304788263, 2.5370118457), (-2.3304788263, -6.5116881543))
                CenterArc((-1.3987788263, -6.5116881543), 0.9317, 180, 90)
                Line((-1.3987788263, -7.4433881543), (0.8490211737, -7.4433881543))
                CenterArc((0.8490211737, -6.5116881543), 0.9317, -90, 90)
                Line((1.7807211737, -6.5116881543), (1.7807211737, -3.4636881543))
                Line((1.7807211737, -3.4636881543), (1.3253211737, -3.4636881543))
                Line((1.3253211737, -6.5116881543), (1.3253211737, -3.4636881543))
                CenterArc((0.8490211737, -6.5116881543), 0.4763, -90, 90)
                Line((-1.3987788263, -6.9879881543), (0.8490211737, -6.9879881543))
                CenterArc((-1.3987788263, -6.5116881543), 0.4763, 180, 90)
            make_face()
        # OneSide extrude, distance=22.86
        extrude(amount=22.86)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.4636881543, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.209802, perimeter: 6.0326
            with BuildLine():
                Line((-0.8490211737, 20.32), (-1.3253211737, 20.32))
                Line((-0.8490211737, 20.32), (-0.8490211737, 22.86))
                Line((-1.3253211737, 22.86), (-0.8490211737, 22.86))
                Line((-1.3253211737, 20.32), (-1.3253211737, 22.86))
            make_face()
            # Profile area: 1.156716, perimeter: 5.9908
            with BuildLine():
                Line((-1.3253211737, 20.32), (-1.7807211737, 20.32))
                Line((-1.3253211737, 20.32), (-1.3253211737, 22.86))
                Line((-1.7807211737, 22.86), (-1.3253211737, 22.86))
                Line((-1.7807211737, 20.32), (-1.7807211737, 22.86))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.3304788263, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 43.1014219444, perimeter: 35.4131375373
            with BuildLine():
                Line((0, 2.5370118457), (0, -3.6333943457))
                Line((0, -3.6333943457), (0.7569, -3.2990881543))
                Line((0.7569, -3.2990881543), (13.9703677871, 2.5370118457))
                Line((0, 2.5370118457), (13.9703677871, 2.5370118457))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.3304788263, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.4948315226, perimeter: 2.8343195844
            with BuildLine():
                Line((1.72, -5.3414881543), (0.92625, -5.3414881543))
                CenterArc((1.72, -5.3414881543), 0.79375, 180, 90)
                Line((1.72, -5.3414881543), (1.72, -6.1352381543))
            make_face()
            # Profile area: 1.4844945677, perimeter: 5.3279587532
            with BuildLine():
                Line((1.72, -5.3414881543), (1.72, -6.1352381543))
                CenterArc((1.72, -5.3414881543), 0.79375, -90, 270)
                Line((1.72, -5.3414881543), (0.92625, -5.3414881543))
            make_face()
            # Profile area: 0.3372641792, perimeter: 2.3399428329
            with BuildLine():
                CenterArc((16.51, 1.2670118457), 0.6553, 0, 90)
                Line((16.51, 1.2670118457), (16.51, 1.9223118457))
                Line((16.51, 1.2670118457), (17.1653, 1.2670118457))
            make_face()
            # Profile area: 1.0117925376, perimeter: 4.3986284988
            with BuildLine():
                Line((16.51, 1.2670118457), (17.1653, 1.2670118457))
                Line((16.51, 1.2670118457), (16.51, 1.9223118457))
                CenterArc((16.51, 1.2670118457), 0.6553, 90, 270)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.7807211737, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1387752393, perimeter: 1.500984236
            with BuildLine():
                CenterArc((-1.72, -5.3414881543), 0.42035, -90, 90)
                Line((-1.72, -5.3414881543), (-1.29965, -5.3414881543))
                Line((-1.72, -5.3414881543), (-1.72, -5.7618381543))
            make_face()
            # Profile area: 0.4163257179, perimeter: 2.8215527079
            with BuildLine():
                Line((-1.72, -5.3414881543), (-1.72, -5.7618381543))
                Line((-1.72, -5.3414881543), (-1.29965, -5.3414881543))
                CenterArc((-1.72, -5.3414881543), 0.42035, 0, 270)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -7.4433881543, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.754912274, perimeter: 3.0800174376
            with Locations((-0.5416788263, 13.97)):
                Circle(0.4902)
            # Profile area: 0.1887280685, perimeter: 1.7504043594
            with BuildLine():
                Line((-0.5416788263, 21.59), (-0.5416788263, 22.0802))
                Line((-0.5416788263, 21.59), (-0.0514788263, 21.59))
                CenterArc((-0.5416788263, 21.59), 0.4902, 0, 90)
            make_face()
            # Profile area: 0.1887280685, perimeter: 1.7504043594
            with BuildLine():
                Line((-0.5416788263, 21.59), (-0.0514788263, 21.59))
                Line((-0.5416788263, 21.59), (-0.5416788263, 21.0998))
                CenterArc((-0.5416788263, 21.59), 0.4902, -90, 90)
            make_face()
            # Profile area: 0.377456137, perimeter: 2.5204087188
            with BuildLine():
                CenterArc((-0.5416788263, 21.59), 0.4902, 90, 180)
                Line((-0.5416788263, 21.59), (-0.5416788263, 21.0998))
                Line((-0.5416788263, 21.59), (-0.5416788263, 22.0802))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_24133_2ac9dc04_0005():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 668.0547023948, perimeter: 161.4457832067
            with BuildLine():
                Line((-33.5, -1), (-35, -1))
                Line((-35, -1), (-35, -4))
                Line((-35, -4), (-31.5, -6.5))
                Line((-31.5, -6.5), (-13.5, -6.5))
                Line((-7.5, -10), (-13.5, -6.5))
                Line((-7.5, -10), (-2.75, -10))
                CenterArc((-2.75, -10.75), 0.75, 0, 90)
                Line((-2, -10.75), (3.5, -10.75))
                Line((9.5, -6.5), (3.5, -10.75))
                Line((9.5, -6.5), (9.5, -1))
                Line((8, -1), (9.5, -1))
                CenterArc((8, 0), 1, 90, 180)
                Line((8, 1), (9.5, 1))
                Line((9.5, 6.5), (9.5, 1))
                Line((9.5, 6.5), (3.5, 10.75))
                Line((-2, 10.75), (3.5, 10.75))
                CenterArc((-2.75, 10.75), 0.75, -90, 90)
                Line((-7.5, 10), (-2.75, 10))
                Line((-7.5, 10), (-13.5, 6.5))
                Line((-31.5, 6.5), (-13.5, 6.5))
                Line((-35, 4), (-31.5, 6.5))
                Line((-35, 1), (-35, 4))
                Line((-33.5, 1), (-35, 1))
                CenterArc((-33.5, 0), 1, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((-5.125, 8.2), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.75, 7.25), (-1.25, 7.25))
                CenterArc((-1.25, 8.25), 1, 90, 180)
                Line((2.75, 9.25), (-1.25, 9.25))
                CenterArc((2.75, 8.25), 1, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.125, -8.2), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.75, -9.25), (-1.25, -9.25))
                CenterArc((-1.25, -8.25), 1, 90, 180)
                Line((2.75, -7.25), (-1.25, -7.25))
                CenterArc((2.75, -8.25), 1, -90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 359.5, perimeter: 107
            with BuildLine():
                Line((31.5, -4), (31.5, 4))
                Line((31.5, 4), (-2.5, 4))
                Line((-2.5, 6.25), (-2.5, 4))
                Line((-9.5, 6.25), (-2.5, 6.25))
                Line((-9.5, -6.25), (-9.5, 6.25))
                Line((-2.5, -6.25), (-9.5, -6.25))
                Line((-2.5, -4), (-2.5, -6.25))
                Line((-2.5, -4), (31.5, -4))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 426.34, perimeter: 107.5656854249
            with BuildLine():
                Line((-2.5, 6.25), (-9.5, 6.25))
                Line((-9.5, 6.25), (-9.5, -6.25))
                Line((-9.5, -6.25), (-2.5, -6.25))
                Line((-2.5, -6.25), (-2.5, -4.8))
                Line((-2.5, -4.8), (0.3, -4.8))
                Line((0.5, -5), (0.3, -4.8))
                Line((0.5, -5), (31.5, -5))
                Line((31.5, -5), (31.5, 5))
                Line((0.5, 5), (31.5, 5))
                Line((0.5, 5), (0.3, 4.8))
                Line((-2.5, 4.8), (0.3, 4.8))
                Line((-2.5, 6.25), (-2.5, 4.8))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 87.5, perimeter: 39
            with BuildLine():
                Line((-2.5, 6.25), (-9.5, 6.25))
                Line((-9.5, 6.25), (-9.5, -6.25))
                Line((-9.5, -6.25), (-2.5, -6.25))
                Line((-2.5, -6.25), (-2.5, -4.8))
                Line((-2.5, -4.8), (-2.5, 4.8))
                Line((-2.5, 4.8), (-2.5, 6.25))
            make_face()
        # OneSide extrude, distance=4.7
        extrude(amount=4.7, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.2, perimeter: 20.7
            with BuildLine():
                Line((-1.75, 4.8), (-1.75, 0.5))
                Line((-1.75, 4.8), (-2.5, 4.8))
                Line((-2.5, 4.8), (-2.5, -4.8))
                Line((-2.5, -4.8), (-1.75, -4.8))
                Line((-1.75, -0.5), (-1.75, -4.8))
                Line((-1.75, 0.5), (-1.75, -0.5))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 87.25, perimeter: 86.5
            with BuildLine():
                Line((20.25, 0.5), (20.25, 5))
                Line((20.25, 5), (14.25, 5))
                Line((14.25, 0.5), (14.25, 5))
                Line((-1.75, 0.5), (14.25, 0.5))
                Line((-1.75, 0.5), (-1.75, -0.5))
                Line((-1.75, -0.5), (14.25, -0.5))
                Line((14.25, -0.5), (14.25, -5))
                Line((14.25, -5), (20.25, -5))
                Line((20.25, -0.5), (20.25, -5))
                Line((31.5, -0.5), (20.25, -0.5))
                Line((31.5, -0.5), (31.5, 0.5))
                Line((31.5, 0.5), (20.25, 0.5))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_24233_960b6e9c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 484, perimeter: 88
            with BuildLine():
                Line((11, -11), (11, 11))
                Line((11, 11), (-11, 11))
                Line((-11, 11), (-11, -11))
                Line((-11, -11), (11, -11))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-8.8, 1.5)):
                Circle(0.25)
        # OneSide extrude, distance=-27
        extrude(amount=-27, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -11), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 24, perimeter: 35
            with BuildLine():
                Line((-8, 1.5), (8, 1.5))
                Line((-8, 1.5), (-8, 0))
                Line((8, 0), (-8, 0))
                Line((8, 1.5), (8, 0))
            make_face()
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((-11, 0), (-11, 1.5))
                Line((-8, 0), (-11, 0))
                Line((-8, 1.5), (-8, 0))
                Line((-11, 1.5), (-8, 1.5))
            make_face()
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((8, 1.5), (11, 1.5))
                Line((8, 1.5), (8, 0))
                Line((11, 0), (8, 0))
                Line((11, 1.5), (11, 0))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 28 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((11, 8), (8, 8))
                Line((11, 11), (11, 8))
                Line((8, 11), (11, 11))
                Line((8, 8), (8, 11))
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((11, -11), (8, -11))
                Line((11, -8), (11, -11))
                Line((8, -8), (11, -8))
                Line((8, -11), (8, -8))
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((-11, -8), (-11, -11))
                Line((-11, -11), (-8, -11))
                Line((-8, -11), (-8, -8))
                Line((-8, -8), (-11, -8))
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((-11, 11), (-8, 11))
                Line((-11, 8), (-11, 11))
                Line((-8, 8), (-11, 8))
                Line((-8, 11), (-8, 8))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch9 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 475, perimeter: 88
            with BuildLine():
                Line((8, 11), (-11, 11))
                Line((-11, 11), (-11, -11))
                Line((-11, -11), (11, -11))
                Line((11, -11), (11, 8))
                Line((8, 8), (11, 8))
                Line((8, 11), (8, 8))
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((8, 11), (8, 8))
                Line((8, 8), (11, 8))
                Line((11, 8), (11, 11))
                Line((11, 11), (8, 11))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 1.5)):
                Circle(1)
        # OneSide extrude, distance=-29
        extrude(amount=-29, mode=Mode.SUBTRACT)
    return part.part


def model_24372_03b260fe_0003():
    """Model: stick v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=80
        extrude(amount=80)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 80, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1371669412, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 81.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=23.5
        extrude(amount=23.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 14.1371669412, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=23.5
        extrude(amount=23.5, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 4234.1408834416, perimeter: 260.3801993565
            with BuildLine():
                Line((28.4106724158, -14.3167761623), (-34.8886519105, -14.3167761623))
                Line((28.4106724158, 52.5739991896), (28.4106724158, -14.3167761623))
                Line((-34.8886519105, 52.5739991896), (28.4106724158, 52.5739991896))
                Line((-34.8886519105, -14.3167761623), (-34.8886519105, 52.5739991896))
            make_face()
        # TwoSides extrude, along=-40, against=10
        extrude(amount=-40, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=10, mode=Mode.SUBTRACT)
    return part.part


def model_24407_2d357602_0000():
    """Model: Head v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 126.6768697744, perimeter: 39.8982267006
            Circle(6.35)
        # OneSide extrude, distance=8.125
        extrude(amount=8.125)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 102.6082645172, perimeter: 35.9084040305
            Circle(5.715)
        # OneSide extrude, distance=-6.225
        extrude(amount=-6.225, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.8442202306, perimeter: 24.2546891451
            with BuildLine():
                Line((3.615, 1.2), (3.615, 1.3))
                CenterArc((0.615, 1.3), 3, 0, 90)
                Line((0.615, 4.3), (-0.615, 4.3))
                CenterArc((-0.615, 1.3), 3, 90, 90)
                Line((-3.615, 1.2), (-3.615, 1.3))
                CenterArc((-4.815, 1.2), 1.2, -90, 90)
                Line((4.815, 0), (-4.815, 0))
                CenterArc((4.815, 1.2), 1.2, -180, 90)
            make_face()
        # TwoSides extrude (symmetric), distance=6.35
        extrude(amount=6.35, both=True, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.4986626045, perimeter: 29.7494680102
            with BuildLine():
                Line((2.54, 6.225), (-2.54, 6.225))
                Line((-2.54, 1.145), (-2.54, 6.225))
                CenterArc((-1.27, 1.145), 1.27, 180, 90)
                Line((1.27, -0.125), (-1.27, -0.125))
                CenterArc((1.27, 1.145), 1.27, -90, 90)
                Line((2.54, 6.225), (2.54, 1.145))
            make_face()
            with BuildLine():
                CenterArc((0, 2.415), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=3.488
        extrude(amount=3.488, both=True, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 31.5657373955, perimeter: 21.7698226701
            with BuildLine():
                Line((2.54, 6.225), (-2.54, 6.225))
                Line((-2.54, 6.225), (-2.54, 1.145))
                CenterArc((-1.27, 1.145), 1.27, -180, 90)
                Line((1.27, -0.125), (-1.27, -0.125))
                CenterArc((1.27, 1.145), 1.27, -90, 90)
                Line((2.54, 6.225), (2.54, 1.145))
            make_face()
        # TwoSides extrude (symmetric), distance=1.588
        extrude(amount=1.588, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_24407_2d357602_0001():
    """Model: Rod Camp v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.6676869774, perimeter: 22.4891133503
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 180)
                Line((-2.54, 0), (-3.81, 0))
                CenterArc((0, 0), 2.54, 0, 180)
                Line((2.54, 0), (3.81, 0))
            make_face()
        # TwoSides extrude (symmetric), distance=1.2
        extrude(amount=1.2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((-3.81, 0)):
                Circle(0.95)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((3.81, 0)):
                Circle(0.95)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5977044254, perimeter: 7.6969020013
            with BuildLine():
                CenterArc((-3.81, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.81, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.5977044254, perimeter: 7.6969020013
            with BuildLine():
                CenterArc((3.81, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.81, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.525
        extrude(amount=1.525, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.547815219, perimeter: 4.8694686131
            with BuildLine():
                CenterArc((3.81, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.81, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.547815219, perimeter: 4.8694686131
            with BuildLine():
                CenterArc((-3.81, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.81, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.33
        extrude(amount=-0.33, mode=Mode.SUBTRACT)
    return part.part


def model_24662_716a39d5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50, perimeter: 30
            with BuildLine():
                Line((-5, 2.5), (5, 2.5))
                Line((-5, -2.5), (-5, 2.5))
                Line((5, -2.5), (-5, -2.5))
                Line((5, 2.5), (5, -2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 32, perimeter: 24
            with BuildLine():
                Line((-4, 2), (4, 2))
                Line((-4, -2), (-4, 2))
                Line((4, -2), (-4, -2))
                Line((4, 2), (4, -2))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 21, perimeter: 20
            with BuildLine():
                Line((3.5, -1.5), (3.5, 1.5))
                Line((3.5, 1.5), (-3.5, 1.5))
                Line((-3.5, 1.5), (-3.5, -1.5))
                Line((-3.5, -1.5), (3.5, -1.5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch8 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 24, perimeter: 22
            with BuildLine():
                Line((-4, 1.5), (4, 1.5))
                Line((-4, -1.5), (-4, 1.5))
                Line((4, -1.5), (-4, -1.5))
                Line((4, 1.5), (4, -1.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on Profile plane
        # Sketch has 4 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1.7949033391, 1.0200377361)):
                Circle(0.25)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((2.3093042001, -0.9799622639)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.280502478, -0.9799622639)):
                Circle(0.15)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.5898066781, -0.4799622639)):
                Circle(0.2)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((1.7949033391, 0.4200377361)):
                Circle(0.175)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((1, -0.4799622639)):
                Circle(0.2)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_24705_f6618d4b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((0, 5), (5, 5))
                Line((0, 0), (0, 5))
                Line((5, 0), (0, 0))
                Line((5, 5), (5, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20, perimeter: 18
            with BuildLine():
                Line((0, -1), (5, -1))
                Line((0, -5), (0, -1))
                Line((5, -5), (0, -5))
                Line((5, -1), (5, -5))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.371410982, perimeter: 14.4646526177
            with BuildLine():
                Line((1, 5), (1, 0.8))
                Line((1, 0.8), (5, 0.8))
                CenterArc((5.625, 5.4), 4.6422650721, -175.0569892814, 77.3196165082)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4710109775, perimeter: 10.588404391
            with BuildLine():
                Line((-0.2, 5), (-5, 5))
                Line((0, 5), (-0.2, 5))
                Line((0, 5.2942021955), (0, 5))
                Line((-5, 5.2942021955), (0, 5.2942021955))
                Line((-5, 5), (-5, 5.2942021955))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.371410982, perimeter: 14.4646526177
            with BuildLine():
                CenterArc((-5.625, 5.4), 4.6422650721, -82.2626272268, 77.3196165082)
                Line((-1, 0.8), (-5, 0.8))
                Line((-1, 5), (-1, 0.8))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.8, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((1.8000000268, 1.5000000224)):
                Circle(0.45)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_143263_b168ae22_0000": {"func": model_143263_b168ae22_0000, "volume": 10935.0927039542, "area": 4771.95581346},
    "model_143346_695aab70_0000": {"func": model_143346_695aab70_0000, "volume": 407.2196552825, "area": 782.371475727},
    "model_143718_b25c8fd0_0004": {"func": model_143718_b25c8fd0_0004, "volume": 407.9592142589, "area": 427.7435342337},
    "model_145702_e28c737e_0022": {"func": model_145702_e28c737e_0022, "volume": 530.832, "area": 1899.28},
    "model_146159_f3f80701_0000": {"func": model_146159_f3f80701_0000, "volume": 182.8, "area": 754.2},
    "model_146284_12cd9232_0000": {"func": model_146284_12cd9232_0000, "volume": 16.3197734992, "area": 75.9140439673},
    "model_20535_f2420e23_0000": {"func": model_20535_f2420e23_0000, "volume": 0.8603200245, "area": 8.2605986058},
    "model_21237_7887a24b_0014": {"func": model_21237_7887a24b_0014, "volume": 0.6851756826, "area": 6.4817757378},
    "model_21337_062b39fa_0001": {"func": model_21337_062b39fa_0001, "volume": 0.0888851095, "area": 2.6145128804},
    "model_21385_601444ba_0022": {"func": model_21385_601444ba_0022, "volume": 12.5054233761, "area": 59.6000735258},
    "model_21638_0a984848_0011": {"func": model_21638_0a984848_0011, "volume": 18.3121648092, "area": 75.5130255567},
    "model_21732_adaf1650_0010": {"func": model_21732_adaf1650_0010, "volume": 18.2436511856, "area": 75.77480446},
    "model_21734_7cf58bd0_0008": {"func": model_21734_7cf58bd0_0008, "volume": 21.5956606569, "area": 98.9041298921},
    "model_21734_7cf58bd0_0009": {"func": model_21734_7cf58bd0_0009, "volume": 2.315802915, "area": 17.301371634},
    "model_21803_8a36dcda_0013": {"func": model_21803_8a36dcda_0013, "volume": 77.1303774796, "area": 264.6138455245},
    "model_21822_7d3db422_0014": {"func": model_21822_7d3db422_0014, "volume": 23.0403555726, "area": 88.2337542371},
    "model_21852_6cf9a734_0008": {"func": model_21852_6cf9a734_0008, "volume": 5.5769160087, "area": 38.3549193095},
    "model_21852_6cf9a734_0021": {"func": model_21852_6cf9a734_0021, "volume": 3.6424803323, "area": 28.2115020292},
    "model_21886_bfcc600c_0003": {"func": model_21886_bfcc600c_0003, "volume": 48.4303377408, "area": 111.4264139672},
    "model_22093_f92b7e00_0000": {"func": model_22093_f92b7e00_0000, "volume": 25.8527926499, "area": 90.5773963458},
    "model_22173_3dff5b17_0000": {"func": model_22173_3dff5b17_0000, "volume": 37.0320788791, "area": 119.480084294},
    "model_22175_cfad1a59_0000": {"func": model_22175_cfad1a59_0000, "volume": 34.0948008429, "area": 89.0113101465},
    "model_22176_272891b8_0000": {"func": model_22176_272891b8_0000, "volume": 54.2242704852, "area": 133.9501283966},
    "model_22198_327974c6_0009": {"func": model_22198_327974c6_0009, "volume": 4.9075167961, "area": 24.2019850853},
    "model_22202_c9c16395_0000": {"func": model_22202_c9c16395_0000, "volume": 6.3177002947, "area": 43.904890864},
    "model_22305_5b45cdb3_0002": {"func": model_22305_5b45cdb3_0002, "volume": 0.681855073, "area": 28.3368629597},
    "model_22323_aa6edb8b_0002": {"func": model_22323_aa6edb8b_0002, "volume": 105.9457479344, "area": 208.6392310495},
    "model_22369_481ab478_0017": {"func": model_22369_481ab478_0017, "volume": 0.9266533192, "area": 10.1072903684},
    "model_22369_985c13a1_0021": {"func": model_22369_985c13a1_0021, "volume": 0.1512602631, "area": 3.060799809},
    "model_22432_e4a51ee9_0006": {"func": model_22432_e4a51ee9_0006, "volume": 52.8832128661, "area": 100.2159968007},
    "model_22498_b8bdb105_0000": {"func": model_22498_b8bdb105_0000, "volume": 9.3286177366, "area": 116.9787732527},
    "model_22543_684108ff_0001": {"func": model_22543_684108ff_0001, "volume": 13.1724601686, "area": 79.2700956168},
    "model_22586_ff3651b2_0000": {"func": model_22586_ff3651b2_0000, "volume": 18.3275376336, "area": 73.2848670779},
    "model_22605_ddf43428_0004": {"func": model_22605_ddf43428_0004, "volume": 4.2495302489, "area": 25.7940608535},
    "model_22606_f1813fe7_0005": {"func": model_22606_f1813fe7_0005, "volume": 1.7519395585, "area": 18.2430938488},
    "model_22734_f6bad9f7_0018": {"func": model_22734_f6bad9f7_0018, "volume": 6.0878691411, "area": 46.9134419942},
    "model_23137_e55b73cb_0007": {"func": model_23137_e55b73cb_0007, "volume": 61.9661930424, "area": 98.8561017284},
    "model_23599_db59334f_0000": {"func": model_23599_db59334f_0000, "volume": 58.2819238373, "area": 258.1725404624},
    "model_23632_5c8e8093_0000": {"func": model_23632_5c8e8093_0000, "volume": 76.0142554424, "area": 396.9848995395},
    "model_23724_f9f5a141_0000": {"func": model_23724_f9f5a141_0000, "volume": 41.9059318489, "area": 241.7332441229},
    "model_23726_f87337ef_0000": {"func": model_23726_f87337ef_0000, "volume": 46.0517925456, "area": 256.7953362453},
    "model_23956_ee17fe48_0012": {"func": model_23956_ee17fe48_0012, "volume": 388.7852960522, "area": 458.2492822722},
    "model_24009_c40b0d48_0000": {"func": model_24009_c40b0d48_0000, "volume": 28.4565462562, "area": 160.0955616269},
    "model_24032_d6172503_0020": {"func": model_24032_d6172503_0020, "volume": 145.4678834707, "area": 680.6951297808},
    "model_24133_2ac9dc04_0005": {"func": model_24133_2ac9dc04_0005, "volume": 3381.5864047896, "area": 2477.9507976215},
    "model_24233_960b6e9c_0000": {"func": model_24233_960b6e9c_0000, "volume": 2035.0652717223, "area": 2755.6117115586},
    "model_24372_03b260fe_0003": {"func": model_24372_03b260fe_0003, "volume": 628.3876472791, "area": 770.1057896979},
    "model_24407_2d357602_0000": {"func": model_24407_2d357602_0000, "volume": 453.5085179916, "area": 870.4426781033},
    "model_24407_2d357602_0001": {"func": model_24407_2d357602_0001, "volume": 33.4634681803, "area": 96.931966864},
    "model_24662_716a39d5_0000": {"func": model_24662_716a39d5_0000, "volume": 87.7517920819, "area": 197.6548667765},
    "model_24705_f6618d4b_0000": {"func": model_24705_f6618d4b_0000, "volume": 43.5039364768, "area": 138.6997112175},
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
