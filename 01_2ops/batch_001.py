"""Batch 001 - passing/01_2ops
166 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a flat parallelogram-shaped plate or panel with a slightly curved or warped surface, featuring a grid pattern of lines across its face, commonly used as a structural component or solar panel.
def model_100221_4d7b66c4_0003():
    """Model: Gause Wrap"""
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
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0444353391, perimeter: 6.2737408767
            with BuildLine():
                _nurbs_edge([(11.6153257646, -0.4138680513), (12.0434893042, -0.383129591), (12.4612420994, -0.3639475502), (12.8713666281, -0.356527213), (13.4926850075, -0.3452857691), (14.1025007446, -0.3634862309), (14.7362203781, -0.3878515475)], [1, 1, 1, 1, 1, 1, 1], [0.1244516483, 0.1244516483, 0.1244516483, 0.1244516483, 0.3057498555, 0.3057498555, 0.3057498555, 0.5804076737, 0.5804076737, 0.5804076737, 0.5804076737], 3)
                Line((14.7362203781, -0.3738507672), (14.7362203781, -0.3878515475))
                _nurbs_edge([(11.6153257646, -0.3998211385), (11.651526887, -0.3972195219), (11.758474496, -0.3897240846), (11.9352863093, -0.3782732309), (12.1803700322, -0.3646176769), (12.4916209952, -0.3513386139), (12.8327430274, -0.3419902249), (13.1710873878, -0.337887177), (13.5080823232, -0.3387592248), (13.8452684956, -0.3441508887), (14.1574793555, -0.3526541135), (14.4038344992, -0.3611748728), (14.583153592, -0.3679269969), (14.6942095389, -0.3722176053), (14.7362203781, -0.3738507672)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1244846991, 0.1244846991, 0.1244846991, 0.1244846991, 0.1244846991, 0.1244846991, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.5803321898, 0.5803321898, 0.5803321898, 0.5803321898, 0.5803321898, 0.5803321898], 5)
                Line((11.6153257646, -0.3998211385), (11.6153257646, -0.4138680513))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a hexagonal aluminum extrusion or structural profile with a long, slender prism shape featuring parallel longitudinal grooves or channels running along its length, commonly used as a modular framing component in industrial construction systems.
def model_100243_9fb796fe_0005():
    """Model: Drone Leg Left"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.61, perimeter: 7.6
            with BuildLine():
                Line((-58.2782013783, -12.0401457697), (-58.2782013783, -13.9401457697))
                Line((-58.2782013783, -13.9401457697), (-56.3782013783, -13.9401457697))
                Line((-56.3782013783, -13.9401457697), (-56.3782013783, -12.0401457697))
                Line((-56.3782013783, -12.0401457697), (-58.2782013783, -12.0401457697))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is an elongated rectangular prism or box beam with a long, narrow profile, featuring a recessed slot or channel running along its length and beveled edges at the top end.
def model_100243_9fb796fe_0006():
    """Model: Drone Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.61, perimeter: 7.6
            with BuildLine():
                Line((-58.2782013783, -12.0401457697), (-58.2782013783, -13.9401457697))
                Line((-58.2782013783, -13.9401457697), (-56.3782013783, -13.9401457697))
                Line((-56.3782013783, -13.9401457697), (-56.3782013783, -12.0401457697))
                Line((-56.3782013783, -12.0401457697), (-58.2782013783, -12.0401457697))
            make_face()
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


# Description: This is a curved pipe or tube elbow connector with a segmented, polygonal surface design featuring two cylindrical sections joined at approximately a 90-degree angle, with faceted surfaces and visible geometric wireframe construction typical of CAD modeling.
def model_100797_b7eaa569_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.152, perimeter: 5.76
            with BuildLine():
                Line((2.4, 0.48), (0, 0.48))
                Line((0, 0.48), (0, 0))
                Line((0, 0), (2.4, 0))
                Line((2.4, 0), (2.4, 0.48))
            make_face()
            # Profile area: 30.6830104845, perimeter: 36.1018658931
            with BuildLine():
                Line((0, 0), (2.4, 0))
                Line((0, 0), (0, -0.665))
                Line((0, -0.665), (1.4, -2.065))
                Line((1.4, -2.065), (4.13, -2.065))
                Line((4.13, -2.065), (5.53, -0.665))
                Line((5.53, -0.665), (5.53, 6.695))
                Line((5.53, 6.695), (4.13, 8.095))
                Line((4.13, 8.095), (0.0389155344, 8.095))
                Line((0.0389155344, 8.095), (0.0389155344, 6.195))
                Line((0.0389155344, 6.195), (3.63, 6.195))
                Line((3.63, 6.195), (3.63, 0))
                Line((2.4, 0), (3.63, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=1.9
        extrude(amount=0.95, both=True)
    return part.part


# Description: This is a structural bracket or support component featuring a curved, elongated body with an angular upper section, internal ribbing for reinforcement, and a flange-like base designed for mounting or attachment purposes.
def model_100798_1efa7e4b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 8.3200259482, perimeter: 16.0987588171
            with BuildLine():
                Line((0, 0), (0.5, 0))
                CenterArc((0.5, 1), 1, -90, 60.9217865104)
                CenterArc((2.5974970091, -0.1664074318), 1.4, 75, 75.9217865104)
                Line((4.4, 0.8), (2.9598436722, 1.185888725))
                Line((5.942536496, 0.8), (4.4, 0.8))
                Line((5.942536496, 0.8), (6.5, 1.357463504))
                Line((6.5, 1.7), (6.5, 1.357463504))
                Line((6.5, 1.7), (5, 1.7))
                CenterArc((5, 3.2), 1.5, -141.2049952636, 51.2049952636)
                CenterArc((3.2826101009, 1.4239151513), 1, 56.7494668313, 20.6947578575)
                Line((1, 2.4), (3.5, 2.4))
                Line((0, 1.4), (1, 2.4))
                Line((0, 0), (0, 1.4))
            make_face()
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a curved, hollow plastic or composite shoe sole/footbed with an ergonomic bent shape, featuring multiple internal ribs for structural reinforcement and several small circular mounting holes or attachment points distributed across its surface.
def model_100799_98b904e9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0082464765, perimeter: 0.573335017
            with BuildLine():
                Line((0.0915676286, -0.0361361711), (0.1153618261, -0.0599303686))
                CenterArc((0, 0), 0.13, -27.4518375838, 19.9834952803)
                Line((0.08, 0.032), (0.1288971879, -0.0168971879))
                Line((0, 0.032), (0.08, 0.032))
                CenterArc((0, 0), 0.032, 90, 180)
                Line((0, -0.032), (0.052, -0.032))
                CenterArc((0.072, -0.032), 0.02, -11.9353906282, 191.9353906282)
            make_face()
            with BuildLine():
                CenterArc((0.015, 0), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.045, 0), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.03, 0.02), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.03, -0.02), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a flat, dark gray parallelogram or skewed rectangular plate with no holes, slots, or other features—a simple geometric flat part.
def model_100877_ac1e5a17_0001():
    """Model: Backing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 603.2246, perimeter: 99.06
            with BuildLine():
                Line((0, 21.59), (0, 0))
                Line((0, 0), (27.94, 0))
                Line((27.94, 0), (27.94, 21.59))
                Line((27.94, 21.59), (0, 21.59))
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a flat, dark gray parallelogram or skewed rectangular plate with no holes, slots, or other features—a simple planar geometric shape.
def model_100877_ac1e5a17_0017():
    """Model: Image 1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 483.87, perimeter: 88.9
            with BuildLine():
                Line((0, 19.05), (0, 0))
                Line((0, 0), (25.4, 0))
                Line((25.4, 0), (25.4, 19.05))
                Line((25.4, 19.05), (0, 19.05))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a long, tapered rectangular prism or wedge-shaped beam with a pointed end, featuring a flat top surface and dark edges, commonly used as a structural support or guide rail component.
def model_101269_f084ba14_0023():
    """Model: basic slat v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 544.35375, perimeter: 133.35
            with BuildLine():
                Line((9.525, 57.15), (9.525, 0))
                Line((0, 57.15), (9.525, 57.15))
                Line((0, 0), (0, 57.15))
                Line((9.525, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a flat, rectangular parallelogram-shaped plate with a simple geometric form, featuring two parallel long edges and two angled short edges, with no holes, slots, or other features.
def model_101427_a9bcb09c_0001():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1265, perimeter: 1012
            with BuildLine():
                Line((-2.5, 57.5), (-2.5, -2.5))
                Line((-2.5, -2.5), (195.5, -2.5))
                Line((195.5, -2.5), (195.5, 57.5))
                Line((195.5, 57.5), (-2.5, 57.5))
            make_face()
            with BuildLine():
                Line((193, 55), (0, 55))
                Line((193, 0), (193, 55))
                Line((0, 0), (193, 0))
                Line((0, 55), (0, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: A thin, elongated parallelogram-shaped plate or blade with a beveled or chamfered edge on the left side and a slight 3D depth, featuring a trapezoidal profile when viewed from the side.
def model_101427_a9bcb09c_0002():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10615, perimeter: 496
            with BuildLine():
                Line((0, 55), (0, 0))
                Line((0, 0), (193, 0))
                Line((193, 0), (193, 55))
                Line((193, 55), (0, 55))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cylindrical tube or rod with a long, slender hexagonal or polygonal cross-section, featuring a tapered end and a smooth, uniform body suitable for structural or mechanical applications.
def model_101817_b02acd9f_0000():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8624, perimeter: 31.04
            with BuildLine():
                Line((10, -7), (6, -7))
                Line((10, -3), (10, -7))
                Line((6, -3), (10, -3))
                Line((6, -7), (6, -3))
            make_face()
            with BuildLine():
                Line((6.12, -6.88), (6.12, -3.12))
                Line((6.12, -3.12), (9.88, -3.12))
                Line((9.88, -3.12), (9.88, -6.88))
                Line((9.88, -6.88), (6.12, -6.88))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=78
        extrude(amount=78)
    return part.part


# Description: This is a hexagonal bar or rod with a tapered/pointed end, featuring a uniform cross-section along its length and a sharp tip at one end.
def model_101817_b02acd9f_0001():
    """Model: horizontal leg 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8624, perimeter: 31.04
            with BuildLine():
                Line((-4, 4), (0, 4))
                Line((-4, 0), (-4, 4))
                Line((0, 0), (-4, 0))
                Line((0, 4), (0, 0))
            make_face()
            with BuildLine():
                Line((-0.12, 3.88), (-0.12, 0.12))
                Line((-0.12, 0.12), (-3.88, 0.12))
                Line((-3.88, 0.12), (-3.88, 3.88))
                Line((-3.88, 3.88), (-0.12, 3.88))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=52
        extrude(amount=52)
    return part.part


# Description: A long, flat rectangular bar or rail with chamfered or beveled ends and shallow surface grooves or slots running along its length.
def model_101817_b02acd9f_0002():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9776, perimeter: 32.96
            with BuildLine():
                Line((-1.88, 10.88), (-1.88, 15.12))
                Line((-1.88, 15.12), (-6.12, 15.12))
                Line((-6.12, 15.12), (-6.12, 10.88))
                Line((-6.12, 10.88), (-1.88, 10.88))
            make_face()
            with BuildLine():
                Line((-6, 11), (-2, 11))
                Line((-6, 15), (-6, 11))
                Line((-2, 15), (-6, 15))
                Line((-2, 11), (-2, 15))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-112
        extrude(amount=-112)
    return part.part


# Description: This is a flat parallelogram or trapezoidal plate with a thin, sheet-like rectangular profile and beveled or chamfered edges, featuring diagonal reinforcing ribs or creases across its surface for structural stiffness.
def model_101817_b02acd9f_0003():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7136, perimeter: 360
            with BuildLine():
                Line((19.6878517604, -0.3344121013), (23.6878517604, -0.3344121013))
                Line((19.6878517604, -52.3344121013), (19.6878517604, -0.3344121013))
                Line((23.6878517604, -52.3344121013), (19.6878517604, -52.3344121013))
                Line((23.6878517604, -56.3344121013), (23.6878517604, -52.3344121013))
                Line((135.6878517604, -56.3344121013), (23.6878517604, -56.3344121013))
                Line((135.6878517604, -52.3344121013), (135.6878517604, -56.3344121013))
                Line((139.6878517604, -52.3344121013), (135.6878517604, -52.3344121013))
                Line((139.6878517604, -0.3344121013), (139.6878517604, -52.3344121013))
                Line((135.6878517604, -0.3344121013), (139.6878517604, -0.3344121013))
                Line((135.6878517604, 3.6655878987), (135.6878517604, -0.3344121013))
                Line((23.6878517604, 3.6655878987), (135.6878517604, 3.6655878987))
                Line((23.6878517604, -0.3344121013), (23.6878517604, 3.6655878987))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat parallelogram or trapezoidal plate with a diagonal internal line suggesting a reinforcing rib or division, featuring a slightly curved or beveled left edge and a 3D perspective appearance.
def model_101817_b02acd9f_0004():
    """Model: surface"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7200, perimeter: 360
            with BuildLine():
                Line((127.8297613154, -66.3440229494), (7.8297613154, -66.3440229494))
                Line((127.8297613154, -6.3440229494), (127.8297613154, -66.3440229494))
                Line((7.8297613154, -6.3440229494), (127.8297613154, -6.3440229494))
                Line((7.8297613154, -66.3440229494), (7.8297613154, -6.3440229494))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a parallelogram cross-section, featuring flat faces and sharp edges, likely used as a structural component, spacer, or mounting bracket in an assembly.
def model_102175_699d5e7c_0003():
    """Model: FLIP (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.52, perimeter: 21.4
            with BuildLine():
                Line((-3.9, 6.8), (0, 6.8))
                Line((-3.9, 0), (-3.9, 6.8))
                Line((0, 0), (-3.9, 0))
                Line((0, 6.8), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular mounting bracket or enclosure component with a trapezoidal overall shape, featuring a large open face with internal ribbing/bracing, a solid mounting flange on one side, and a notched cutout on the edge for attachment or assembly purposes.
def model_102293_5d04e48d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 42 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1023993066, perimeter: 1.8324141889
            with BuildLine():
                Line((0.075, -1.8), (0.075, -1.6565449972))
                Line((-0.0348076211, -1.8), (0.075, -1.8))
                CenterArc((0.225, -1.65), 0.3, -150, 60)
                Line((0.675, -1.95), (0.225, -1.95))
                Line((0.675, -1.8), (0.675, -1.95))
                Line((0.2668402025, -1.8), (0.675, -1.8))
                CenterArc((0.2668402025, -1.6), 0.2, -163.5770920723, 73.5770920723)
            make_face()
            # Profile area: 1.1915873328, perimeter: 16.0376835806
            with BuildLine():
                Line((0.275, 1.8), (3.475, 1.8))
                CenterArc((3.475, 1.6), 0.2, 0, 90)
                Line((3.675, 1.2), (3.675, 1.6))
                Line((3.825, 1.2), (3.675, 1.2))
                Line((3.825, 1.65), (3.825, 1.2))
                CenterArc((3.525, 1.65), 0.3, 0, 60)
                CenterArc((3.525, 1.65), 0.3, 60, 30)
                Line((3.525, 1.95), (0.225, 1.95))
                CenterArc((0.225, 1.65), 0.3, 90, 60)
                CenterArc((0.225, 1.65), 0.3, 150, 30)
                Line((-0.075, 1.65), (-0.075, -1.65))
                CenterArc((0.225, -1.65), 0.3, 180, 30)
                Line((-0.0348076211, -1.8), (0.075, -1.8))
                Line((0.075, -1.8), (0.075, -1.6565449972))
                Line((0.075, -1.6565449972), (0.075, 1.6))
                CenterArc((0.275, 1.6), 0.2, 90, 90)
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)
    return part.part


# Description: This is a boat or canoe hull featuring an elongated, curved elliptical shape with an open top, structural ribs or frames running longitudinally, and a flat or slightly rounded bottom keel.
def model_102295_86f842dd_0000():
    """Model: FBL"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.7415926536, perimeter: 11.8831853072
            with BuildLine():
                CenterArc((1, 0), 1, 90, 180)
                Line((1, -1), (3.8, -1))
                CenterArc((3.8, 0), 1, -90, 180)
                Line((3.8, 1), (1, 1))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a cylindrical roller or shaft with rounded ends featuring a central longitudinal slot or groove running along its top surface and small holes or indentations near each end.
def model_102369_65e5a7e6_0001():
    """Model: K"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.8935566306, perimeter: 17.2849021219
            with BuildLine():
                CenterArc((8.5010000671, -1.999), 0.499, 0, 90)
                Line((2.9990000671, -1.5), (8.5010000671, -1.5))
                CenterArc((2.9990000671, -1.999), 0.499, 90, 90)
                Line((2.5000000671, -2.001), (2.5000000671, -1.999))
                CenterArc((2.9990000671, -2.001), 0.499, 180, 90)
                Line((8.5010000671, -2.5), (2.9990000671, -2.5))
                CenterArc((8.5010000671, -2.001), 0.499, -90, 90)
                Line((9.0000000671, -1.999), (9.0000000671, -2.001))
            make_face()
            with BuildLine():
                CenterArc((3.0000000671, -2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.5000000671, -2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is an elongated connector or mounting bracket with a rounded rectangular (stadium) shape, featuring two symmetrical circular holes at each end for fastening or assembly purposes.
def model_102369_65e5a7e6_0002():
    """Model: C"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.3235566306, perimeter: 14.1449021219
            with BuildLine():
                CenterArc((8.5010000671, -1.999), 0.499, 0, 90)
                Line((4.5690000671, -1.5), (8.5010000671, -1.5))
                CenterArc((4.5690000671, -1.999), 0.499, 90, 90)
                Line((4.0700000671, -2.001), (4.0700000671, -1.999))
                CenterArc((4.5690000671, -2.001), 0.499, 180, 90)
                Line((8.5010000671, -2.5), (4.5690000671, -2.5))
                CenterArc((8.5010000671, -2.001), 0.499, -90, 90)
                Line((9.0000000671, -1.999), (9.0000000671, -2.001))
            make_face()
            with BuildLine():
                CenterArc((4.5700000671, -2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.5000000671, -2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a triangular wedge or prism-shaped component with a dark blue/gray finish, featuring a pointed apex and a flat right-angled base, with subtle surface details and edge markings visible on its faces.
def model_102369_65e5a7e6_0003():
    """Model: Lower Triangle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.6650970964, perimeter: 20.1890819795
            with BuildLine():
                Line((-2.2426952676, -4.7641899597), (-4.3160110524, -9.1756932926))
                CenterArc((-2.6952107032, -4.551517017), 0.5, -25.172558791, 86.7604336679)
                Line((-5.6852463199, -2.3655190731), (-2.4573055269, -4.111743067))
                CenterArc((-5.9231514961, -2.8052930231), 0.5, 61.5878748769, 136.9360160923)
                Line((-4.3160110524, -9.1756932926), (-6.3972471283, -2.9641430516))
            make_face()
            with BuildLine():
                CenterArc((-2.6952107032, -4.551517017), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.9231514961, -2.8052930231), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a connector or bracket component with an elongated oval body featuring two circular holes on either side and a central slot or opening on top, designed for fastening or pivoting applications.
def model_102369_65e5a7e6_0004():
    """Model: M"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8935566306, perimeter: 9.2849021219
            with BuildLine():
                CenterArc((8.5010000671, -1.999), 0.499, 0, 90)
                Line((6.9990000671, -1.5), (8.5010000671, -1.5))
                CenterArc((6.9990000671, -1.999), 0.499, 90, 90)
                Line((6.5000000671, -2.001), (6.5000000671, -1.999))
                CenterArc((6.9990000671, -2.001), 0.499, 180, 90)
                Line((8.5010000671, -2.5), (6.9990000671, -2.5))
                CenterArc((8.5010000671, -2.001), 0.499, -90, 90)
                Line((9.0000000671, -1.999), (9.0000000671, -2.001))
            make_face()
            with BuildLine():
                CenterArc((7.0000000671, -2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.5000000671, -2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a triangular bracket or corner reinforcement with three rounded corner holes for fastening, featuring a blue top flange and dark gray structural body in a wedge-like shape.
def model_102369_65e5a7e6_0005():
    """Model: Upper Triangle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.3694576432, perimeter: 21.593981634
            with BuildLine():
                CenterArc((-3.8, -0.78), 0.5, -113.4273099504, 93.7316921202)
                Line((-3.3292518379, -0.9485116253), (-1.9306053476, 2.9586981201))
                CenterArc((-2.4013535097, 3.1272097455), 0.5, -19.6956178302, 134.1832559662)
                Line((-2.6086019618, 3.5822351065), (-7.6866849901, 1.2693423816))
                CenterArc((-7.4794365381, 0.8143170206), 0.5, 114.4876381359, 132.0850519137)
                Line((-7.6782291841, 0.3555344099), (-3.998792646, -1.2387826107))
            make_face()
            with BuildLine():
                CenterArc((-2.4013535097, 3.1272097455), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.4794365381, 0.8143170206), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.8, -0.78), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical roller or shaft with rounded ends, featuring a central longitudinal slot or groove running along its top surface and small circular holes near each end.
def model_102369_65e5a7e6_0006():
    """Model: J"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3935566306, perimeter: 16.2849021219
            with BuildLine():
                CenterArc((8.5010000671, -1.999), 0.499, 0, 90)
                Line((3.4990000671, -1.5), (8.5010000671, -1.5))
                CenterArc((3.4990000671, -1.999), 0.499, 90, 90)
                Line((3.0000000671, -2.001), (3.0000000671, -1.999))
                CenterArc((3.4990000671, -2.001), 0.499, 180, 90)
                Line((8.5010000671, -2.5), (3.4990000671, -2.5))
                CenterArc((8.5010000671, -2.001), 0.499, -90, 90)
                Line((9.0000000671, -1.999), (9.0000000671, -2.001))
            make_face()
            with BuildLine():
                CenterArc((3.5000000671, -2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.5000000671, -2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a curved, slightly tapered hollow body featuring an elliptical opening at the top and reinforced mesh or ribbed texturing along its outer surface for structural support.
def model_102410_f9877a7b_0000():
    """Model: ??????3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5635231822, perimeter: 6.4402649399
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.15
        extrude(amount=1.15)
    return part.part


# Description: This is a long, narrow rectangular extrusion or beam with a dark gray finish, featuring multiple circular holes or ports distributed along its length and rounded end caps on both sides.
def model_102410_f9877a7b_0003():
    """Model: ?????2 v1"""
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
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1436670362, perimeter: 42.8226703192
            with BuildLine():
                CenterArc((0, 0), 0.6, 85.3831396711, 189.2337206578)
                _nurbs_edge([(0.0482953447, -0.5980531412), (0.3812749529, -0.5769643249), (1.047507213, -0.5366039418), (2.0476747127, -0.4815149686), (3.3828967406, -0.4191468548), (5.0548877292, -0.3609100438), (6.7301049697, -0.3241456229), (8.408808557, -0.3105846595), (10.0911346357, -0.3211332663), (11.7769328639, -0.3547908406), (13.4659383426, -0.4097943403), (14.8194965576, -0.469463121), (15.835904883, -0.5224653183), (16.5140523986, -0.5614071783), (16.8532616523, -0.5817799045)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((17, 0), 0.6, -104.1560638023, 208.3121276045)
                _nurbs_edge([(0.0482953447, 0.5980531412), (0.3812749529, 0.5769643249), (1.047507213, 0.5366039418), (2.0476747127, 0.4815149686), (3.3828967406, 0.4191468548), (5.0548877292, 0.3609100438), (6.7301049697, 0.3241456229), (8.408808557, 0.3105846595), (10.0911346357, 0.3211332663), (11.7769328639, 0.3547908406), (13.4659383426, 0.4097943403), (14.8194965576, 0.469463121), (15.835904883, 0.5224653183), (16.5140523986, 0.5614071783), (16.8532616523, 0.5817799045)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((17, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical sleeve or tube with a curved, tapered upper edge and vertical ribbing or fluting running along its sidewalls.
def model_102410_f9877a7b_0012():
    """Model: ??????2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5635231822, perimeter: 6.4402649399
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is a flat diamond-shaped or rhombus-shaped plate with an internal lattice framework of triangular bracing elements that provide structural reinforcement while reducing weight.
def model_102416_eba35f73_0005():
    """Model: table v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 574.0365045915, perimeter: 111.7079632679
            with BuildLine():
                Line((12, -12), (-12, -12))
                Line((12, 12), (12, -12))
                Line((-12, 12), (12, 12))
                Line((-12, -12), (-12, 12))
            make_face()
            with BuildLine():
                CenterArc((-10.85, -3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.15, -3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.15, 3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.85, 3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.15, 3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.85, 3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.15, -3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.85, -3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.9), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.9), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a pentahedron or wedge-shaped solid featuring a rectangular base with an angled top surface, creating a sloped geometric form with triangular and quadrilateral facets.
def model_102525_06a3094b_0000():
    """Model: SOIC-8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1911, perimeter: 1.76
            with BuildLine():
                Line((0.195, -0.245), (0.195, 0.245))
                Line((0.195, 0.245), (-0.195, 0.245))
                Line((-0.195, 0.245), (-0.195, -0.245))
                Line((-0.195, -0.245), (0.195, -0.245))
            make_face()
        # OneSide extrude, distance=0.155
        extrude(amount=0.155)
    return part.part


# Description: This is an elongated hexagonal prism or wedge-shaped part with a tapered profile, featuring a flat base, angled top surfaces, and what appears to be internal geometric divisions or structural ribs visible through transparent surfaces.
def model_102525_06a3094b_0004():
    """Model: SOP-28 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.53, perimeter: 5.3
            with BuildLine():
                Line((0.425, -0.9), (0.425, 0.9))
                Line((0.425, 0.9), (-0.425, 0.9))
                Line((-0.425, 0.9), (-0.425, -0.9))
                Line((-0.425, -0.9), (0.425, -0.9))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is an elongated hexagonal prism or wedge-shaped component with a tapered top surface featuring multiple triangular facets and internal geometric divisions, appearing to be a structural or aerodynamic part with a beveled or chamfered upper face.
def model_102525_06a3094b_0006():
    """Model: SOP-28"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.373, perimeter: 6.46
            with BuildLine():
                Line((0.565, -1.05), (0.565, 1.05))
                Line((0.565, 1.05), (-0.565, 1.05))
                Line((-0.565, 1.05), (-0.565, -1.05))
                Line((-0.565, -1.05), (0.565, -1.05))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical mesh or perforated filter tube with a solid dark body and an open mesh/grid top end, designed for filtering or ventilation applications.
def model_102760_26430589_0037():
    """Model: Винт с плоской г v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.020106193, perimeter: 0.5026548246
            Circle(0.08)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4)
    return part.part


# Description: This is a cylindrical housing or barrel component with a rounded/domed top cap and a mesh-patterned cylindrical body, featuring a flat circular base.
def model_103284_e25015aa_0004():
    """Model: Tail Stock Lever"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.4772672853, perimeter: 7.5008666197
            with Locations((0.8077681284, 0.828433872)):
                Circle(1.1938)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a parallelepiped or wedge-shaped solid block with a trapezoidal profile, featuring slanted faces and angular edges, appearing to be a geometric structural component with no holes or slots.
def model_103481_b27a1cdf_0010():
    """Model: CAM Tolerance test"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((5.08, -5.08), (5.08, 5.08))
                Line((5.08, 5.08), (-5.08, 5.08))
                Line((-5.08, 5.08), (-5.08, -5.08))
                Line((-5.08, -5.08), (5.08, -5.08))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a horizontal rail or beam with a streamlined, elongated rectangular body featuring rounded end caps and a central blue-tinted channel or slot running along its length.
def model_103552_c3a389ed_0003():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.6467918106, perimeter: 55.3938040026
            with BuildLine():
                CenterArc((-10, 0), 1.25, 90, 180)
                Line((-10, -1.25), (10, -1.25))
                CenterArc((10, 0), 1.25, -90, 180)
                Line((10, 1.25), (-10, 1.25))
            make_face()
            with BuildLine():
                CenterArc((-10, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a cylindrical tube or barrel with hemispherical end caps, featuring internal ribbed or reinforcement patterns along its length for structural support.
def model_104283_e5646f96_0000():
    """Model: SHAFT[ v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-1.5, 1)):
                Circle(1.25)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


# Description: This is a curved duct or pipe fitting with an oval or circular cross-section, featuring a twisted or helical geometry with an open slot or channel running along its length, and a flat mounting flange or base at the bottom.
def model_104283_e5646f96_0001():
    """Model: Untitled v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8161681746, perimeter: 10.5164675131
            with BuildLine():
                Line((0.9188335454, 1.7044497562), (0.9188335454, 0))
                Line((0.9188335454, 0), (3.7174115709, 0))
                Line((3.7174115709, 1.7044497562), (3.7174115709, 0))
                CenterArc((2.3181225581, 1.7490620725), 1.4, -178.1739069798, 176.3478139596)
            make_face()
            # Profile area: 1.2486984921, perimeter: 16.6504108495
            with BuildLine():
                CenterArc((2.3181225581, 1.7490620725), 1.4, -178.1739069798, 176.3478139596)
                Line((3.7174115709, 1.7936743888), (3.7174115709, 1.7044497562))
                CenterArc((2.3181225581, 1.7490620725), 1.4, 1.8260930202, 176.3478139596)
                Line((0.9188335454, 1.7936743888), (0.9188335454, 1.7044497562))
            make_face()
            with BuildLine():
                CenterArc((2.3181225581, 1.7490620725), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


# Description: This is a elongated cylindrical housing or duct component with a rounded capsule shape, featuring mesh or perforated sections at both ends and a smooth curved body with subtle surface details and recessed areas along its length.
def model_104453_aba0f2d1_0002():
    """Model: ArmRest v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 578.5398163397, perimeter: 131.4159265359
            with BuildLine():
                CenterArc((0, 0), 5, 90, 180)
                Line((0, -5), (50, -5))
                CenterArc((50, 0), 5, -90, 180)
                Line((50, 5), (0, 5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a hollow rectangular box or duct with an open top and bottom, featuring a trapezoidal or wedge-like profile with angled side walls and internal triangulated structural geometry.
def model_104453_aba0f2d1_0006():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 700, perimeter: 280
            with BuildLine():
                Line((0, 30), (0, 0))
                Line((0, 0), (50, 0))
                Line((50, 0), (50, 30))
                Line((50, 30), (0, 30))
            make_face()
            with BuildLine():
                Line((5, 5), (5, 25))
                Line((5, 25), (45, 25))
                Line((45, 25), (45, 5))
                Line((45, 5), (5, 5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a cylindrical sleeve or tube with an open top and bottom, featuring a slightly tapered or curved profile and mesh or perforated surfaces visible at both ends.
def model_104524_f829aab2_0001():
    """Model: screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a polyhedron or geometric solid with an irregular, faceted structure featuring multiple planar faces, sharp edges, and angular surfaces, resembling a truncated or distorted pyramid with no apparent holes, slots, or curves.
def model_105278_909f3813_0000():
    """Model: Untitled v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.2, perimeter: 14.4
            with BuildLine():
                Line((-0.6, 3), (0.6, 3))
                Line((-0.6, -3), (-0.6, 3))
                Line((0.6, -3), (-0.6, -3))
                Line((0.6, 3), (0.6, -3))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a trapezoidal profile, featuring internal diagonal cross-bracing or reinforcement ribs visible on its surface.
def model_105831_359a0be0_0000():
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
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.2621055755, perimeter: 73.8679702639
            with BuildLine():
                Line((0, 0), (-16, 0))
                _nurbs_edge([(-17.5000002608, 1.0000000149), (-17.4859989347, 0.9644171275), (-17.4566624413, 0.894458952), (-17.4086561749, 0.7931444691), (-17.3365131398, 0.6654233832), (-17.2318144007, 0.5189880426), (-17.1111944067, 0.3872542709), (-16.9731107863, 0.272055842), (-16.8165044685, 0.1751111227), (-16.6412761329, 0.0976376761), (-16.4475444232, 0.0408321304), (-16.2778119947, 0.0129119771), (-16.1421684878, 0.0023477042), (-16.0480109529, 0), (-16, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-17.5000002608, -0.5), (-17.5000002608, 1.0000000149))
                Line((17.5000002608, -0.5), (-17.5000002608, -0.5))
                Line((17.5000002608, 1.0000000149), (17.5000002608, -0.5))
                _nurbs_edge([(17.5000002608, 1.0000000149), (17.4848982782, 0.9644171275), (17.4535916151, 0.894458952), (17.4033235547, 0.7931444691), (17.3295742803, 0.6654233832), (17.2252769013, 0.5189880426), (17.1073801861, 0.3872542709), (16.9739433495, 0.272055842), (16.8229348416, 0.1751111227), (16.6525562817, 0.0976376761), (16.4609210015, 0.0408321304), (16.2890700085, 0.0129119771), (16.148989393, 0.0023477042), (16.0505116268, 0), (16, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (16, 0))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a solid toroidal (doughnut-shaped) ring with a smooth, continuous curved surface featuring a large central hole and uniform wall thickness throughout.
def model_106323_77f22d29_0004():
    """Model: bearing 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.7123889804, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a cylindrical container or barrel with a curved, tilted body featuring a flat or slightly recessed top circular opening and a rounded bottom, designed as an open-top vessel or cup-like component.
def model_106817_bb28b7aa_0002():
    """Model: thumb screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7452260904, perimeter: 3.0601939879
            with Locations((11.4300003648, 0)):
                Circle(0.487045)
        # OneSide extrude, distance=0.68707
        extrude(amount=0.68707)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with a solid curved sidewall, open mesh top and bottom surfaces, and a slightly tapered design.
def model_106817_bb28b7aa_0003():
    """Model: ruler holder w/screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6974372413, perimeter: 2.9604484212
            with Locations((5.0800001621, 6.3500002027)):
                Circle(0.47117)
        # OneSide extrude, distance=1.2192
        extrude(amount=1.2192)
    return part.part


# Description: This is a toroidal (donut-shaped) mechanical component featuring a smooth curved surface with a central hollow opening and a textured mesh pattern on the outer surface, likely representing a composite or reinforced material structure.
def model_106817_bb28b7aa_0004():
    """Model: washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8399183174, perimeter: 4.7239500413
            with BuildLine():
                CenterArc((-2.5400000811, 1.2700000405), 0.55372, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5400000811, 1.2700000405), 0.19812, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.13208
        extrude(amount=0.13208)
    return part.part


# Description: This is a rectangular mounting bracket or panel with a parallelogram shape, featuring three horizontal slots or grooves across its surface and rounded edges, designed for securing or mounting components.
def model_107055_0500fdd1_0009():
    """Model: Section 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 165.7911082105, perimeter: 62.1378456705
            with BuildLine():
                Line((-6, -6.0967662351), (-4.9817662351, -7.115))
                Line((4.9817662351, -7.115), (-4.9817662351, -7.115))
                Line((4.9817662351, -7.115), (6, -6.0967662351))
                Line((6, 6.0967662351), (6, -6.0967662351))
                Line((4.9817662351, 7.115), (6, 6.0967662351))
                Line((-4.9817662351, 7.115), (4.9817662351, 7.115))
                Line((-6, 6.0967662351), (-4.9817662351, 7.115))
                Line((-6, -6.0967662351), (-6, 6.0967662351))
            make_face()
            with BuildLine():
                CenterArc((5.25, -3.465), 0.48, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.25, 3.722), 0.48, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.25, -3.465), 0.48, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.25, 3.722), 0.48, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.95
        extrude(amount=-0.95)
    return part.part


# Description: This is a flat washer or ring with a circular toroidal (donut-like) shape, featuring a large central hole and uniform thickness around its perimeter.
def model_107055_0500fdd1_0027():
    """Model: Washer (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2569854207, perimeter: 3.4494687336
            with BuildLine():
                CenterArc((0, 0), 0.349, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.036
        extrude(amount=0.036)
    return part.part


# Description: This is an oval or elliptical wheel/pulley with a ribbed or grooved rim around its perimeter and internal radial spokes or support structures connecting to a central hub.
def model_107075_beb19139_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 370.3550245909, perimeter: 68.4198949733
            with BuildLine():
                CenterArc((-6.6040002108, 3.6789694397), 0.3769693344, 175.9816141148, 94.0183858852)
                Line((-6.6040002108, 3.3020001054), (-6.3500002027, 3.3020001054))
                Line((-6.3500002027, 3.3020001054), (-3.8100001216, 3.5560001135))
                CenterArc((-4.8897273854, 14.3532727512), 10.8511247057, -84.2894068625, 343.1827584668)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a square/diamond-shaped mounting bracket or spacer with a large central oval hole and flanged edges, designed for mechanical fastening or alignment purposes.
def model_107250_aeb9e6d4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 77.8902260451, perimeter: 72.5585813605
            with BuildLine():
                Line((-10.16, 10.16), (0, 10.16))
                Line((-10.16, 0), (-10.16, 10.16))
                Line((0, 0), (-10.16, 0))
                Line((0, 10.16), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-8.8900002837, 8.8900002837), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.8900002837, 1.2700000405), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2700000405, 8.8900002837), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2700000405, 1.2700000405), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.0800001621, 5.0800001621), 2.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a dark blue/navy curved bracket or clamp component with an organic, asymmetrical shape featuring a large central cutout or opening, rounded edges, and what appears to be mounting surfaces or flanges on the sides.
def model_107278_ff1ba47b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.2867651417, perimeter: 14.8079026419
            with BuildLine():
                Line((0, 0.8128), (2.032, 0.8128))
                CenterArc((0, 0), 0.8128, 90, 180)
                Line((0, -0.8128), (1.3208, -0.8128))
                CenterArc((1.8288, -0.8128), 0.508, -11.9353906282, 191.9353906282)
                Line((2.3258177663, -0.9178587456), (2.9301903829, -1.5222313622))
                CenterArc((0, 0), 3.302, -27.4518375838, 19.9834952803)
                Line((2.032, 0.8128), (3.273988572, -0.429188572))
            make_face()
            with BuildLine():
                CenterArc((0.381, 0), 0.1465118516, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.762, -0.508), 0.1465118516, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.143, 0), 0.1270000041, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.762, 0.5080000162), 0.1270000041, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.127
        extrude(amount=0.127, both=True)
    return part.part


# Description: This is a cylindrical roller or drum with a solid dark gray body featuring a textured or mesh-patterned surface band around its middle section, suggesting it may be a bearing component, conveyor roller, or mechanical shaft element.
def model_107467_a8afc51d_0000():
    """Model: Pivot:2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a cylindrical roller or shaft with a smooth, rounded surface and subtle textured markings or grip patterns along its length.
def model_107467_a8afc51d_0002():
    """Model: Pivot"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a dark gray polymer hook or pull handle with an elongated teardrop shape, featuring a curved upper arm, a large oval aperture for gripping, and textured surface detailing.
def model_107656_3b6f2b9c_0000():
    """Model: connecting rod (1)"""
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
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 34.3610896508, perimeter: 54.9778649224
            with BuildLine():
                CenterArc((-12.0218573437, -15.26703717), 5, 149.299855308, 241.400289384)
                _nurbs_edge([(-7.7885559892, -12.6063681485), (-7.7754260566, -12.6279713086), (-7.7622657322, -12.6495672456), (-7.7490750193, -12.6711559602), (-7.7358539193, -12.6927374528), (-7.7226024322, -12.7143117233)], [1, 1, 1, 1, 1, 1], [0.992035597, 0.992035597, 0.992035597, 0.992035597, 0.992035597, 0.992035597, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-12.0218573437, -15.26703717), 5, 32.1497410768, 115.7005178463)
                _nurbs_edge([(-16.2551586982, -12.6063681485), (-16.2682886308, -12.6279713086), (-16.2814489551, -12.6495672456), (-16.2946396681, -12.6711559602), (-16.3078607681, -12.6927374528), (-16.3211122551, -12.7143117233)], [1, 1, 1, 1, 1, 1], [0.992035597, 0.992035597, 0.992035597, 0.992035597, 0.992035597, 0.992035597, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((-12.0218573437, -15.26703717), 3.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 38.6823019734, perimeter: 44.7129455489
            with BuildLine():
                CenterArc((-12.0218573437, -15.26703717), 5, 32.1497410768, 115.7005178463)
                _nurbs_edge([(-10.5758276043, 2.1289579305), (-10.6275254244, 1.8062432651), (-10.7214567828, 1.1630632867), (-10.8339620085, 0.2050411308), (-10.926242216, -1.0586019675), (-10.9388221389, -2.6137306687), (-10.8393334048, -4.1422242895), (-10.6184508384, -5.6418665386), (-10.2707598541, -7.1113705447), (-9.8008672397, -8.5518311918), (-9.2271118838, -9.9428833193), (-8.6900647492, -11.0322320265), (-8.2484011578, -11.8338225321), (-7.9402837702, -12.356724861), (-7.7885559892, -12.6063681484)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.992035597, 0.992035597, 0.992035597, 0.992035597, 0.992035597, 0.992035597], 5)
                CenterArc((-12.0218573437, 2.5277034543), 1.5, -164.5837018869, 149.1674037739)
                _nurbs_edge([(-13.4678870831, 2.1289579305), (-13.416189263, 1.8062432651), (-13.3222579046, 1.1630632867), (-13.2097526789, 0.2050411308), (-13.1174724713, -1.0586019675), (-13.1048925485, -2.6137306687), (-13.2043812825, -4.1422242895), (-13.4252638489, -5.6418665386), (-13.7729548332, -7.1113705447), (-14.2428474477, -8.5518311918), (-14.8166028035, -9.9428833193), (-15.3536499382, -11.0322320265), (-15.7953135295, -11.8338225321), (-16.1034309171, -12.356724861), (-16.2551586981, -12.6063681484)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.992035597, 0.992035597, 0.992035597, 0.992035597, 0.992035597, 0.992035597], 5)
            make_face()
            # Profile area: 5.5292030703, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((-12.0218573437, 2.5277034543), 1.5, -164.5837018869, 149.1674037739)
                CenterArc((-12.0218573437, 2.5277034543), 1.5, -15.4162981131, 210.8325962261)
            make_face()
            with BuildLine():
                CenterArc((-12.0218573437, 2.5277034543), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is a toroidal (donut-shaped) component featuring a smooth, rounded outer surface with a large central hole and a mesh-textured surface finish, commonly used as a bushing, spacer, or bearing component in mechanical assemblies.
def model_107668_cf76b132_0001():
    """Model: Wheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 374.8312734814, perimeter: 130.376095124
            with BuildLine():
                CenterArc((0, 0), 13.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 7.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or blade with a slightly tapered profile and subtle depth, featuring clean edges and a simple geometric form typical of a structural component or mounting bracket.
def model_108244_329b1876_0000():
    """Model: WOOD"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31587.0335999988, perimeter: 762
            with BuildLine():
                Line((121.1735612903, 31.2995511481), (-0.7464387097, 31.2995511481))
                Line((121.1735612903, 290.3795511481), (121.1735612903, 31.2995511481))
                Line((-0.7464387097, 290.3795511481), (121.1735612903, 290.3795511481))
                Line((-0.7464387097, 31.2995511481), (-0.7464387097, 290.3795511481))
            make_face()
        # OneSide extrude, distance=4.445
        extrude(amount=4.445)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a slight conical shape that gradually narrows from one end to the other, commonly used as a drift pin, alignment pin, or taper pin in mechanical assemblies.
def model_108244_329b1876_0002():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.9559109976, perimeter: 58.5109797196
            with BuildLine():
                Line((-3.81, 3.81), (3.81, 3.81))
                Line((-3.81, -3.81), (-3.81, 3.81))
                Line((3.81, -3.81), (-3.81, -3.81))
                Line((3.81, 3.81), (3.81, -3.81))
            make_face()
            with BuildLine():
                Line((-3.5038724649, 3.5038724649), (3.5038724649, 3.5038724649))
                Line((3.5038724649, 3.5038724649), (3.5038724649, -3.5038724649))
                Line((3.5038724649, -3.5038724649), (-3.5038724649, -3.5038724649))
                Line((-3.5038724649, -3.5038724649), (-3.5038724649, 3.5038724649))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-243.84
        extrude(amount=-243.84)
    return part.part


# Description: This is a rectangular steel rod or bar stock with a uniform hexagonal or multi-sided cross-section, featuring a tapered or chamfered point at one end, commonly used as a punch, chisel, or structural fastener.
def model_108244_329b1876_0004():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.9559109976, perimeter: 58.5109797196
            with BuildLine():
                Line((-3.81, 3.81), (3.81, 3.81))
                Line((-3.81, -3.81), (-3.81, 3.81))
                Line((3.81, -3.81), (-3.81, -3.81))
                Line((3.81, 3.81), (3.81, -3.81))
            make_face()
            with BuildLine():
                Line((-3.5038724649, 3.5038724649), (3.5038724649, 3.5038724649))
                Line((3.5038724649, 3.5038724649), (3.5038724649, -3.5038724649))
                Line((3.5038724649, -3.5038724649), (-3.5038724649, -3.5038724649))
                Line((-3.5038724649, -3.5038724649), (-3.5038724649, 3.5038724649))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-121.92
        extrude(amount=-121.92)
    return part.part


# Description: This is a hexagonal shaft or tool holder with a long, slender prismatic body featuring a six-sided cross-section and tapered or beveled ends.
def model_108244_329b1876_0011():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.9559109976, perimeter: 58.5109797196
            with BuildLine():
                Line((-3.81, 3.81), (3.81, 3.81))
                Line((-3.81, -3.81), (-3.81, 3.81))
                Line((3.81, -3.81), (-3.81, -3.81))
                Line((3.81, 3.81), (3.81, -3.81))
            make_face()
            with BuildLine():
                Line((-3.5038724649, 3.5038724649), (3.5038724649, 3.5038724649))
                Line((3.5038724649, 3.5038724649), (3.5038724649, -3.5038724649))
                Line((3.5038724649, -3.5038724649), (-3.5038724649, -3.5038724649))
                Line((-3.5038724649, -3.5038724649), (-3.5038724649, 3.5038724649))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=106.68
        extrude(amount=106.68)
    return part.part


# Description: This is a hexagonal steel shaft or tool holder with a long, slender prismatic form featuring a six-sided cross-section and tapered or chamfered ends, commonly used as a drive shaft, drill bit holder, or lathe tool.
def model_108244_329b1876_0018():
    """Model: Component12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.9559109976, perimeter: 58.5109797196
            with BuildLine():
                Line((-3.81, 3.81), (3.81, 3.81))
                Line((-3.81, -3.81), (-3.81, 3.81))
                Line((3.81, -3.81), (-3.81, -3.81))
                Line((3.81, 3.81), (3.81, -3.81))
            make_face()
            with BuildLine():
                Line((-3.5038724649, 3.5038724649), (3.5038724649, 3.5038724649))
                Line((3.5038724649, 3.5038724649), (3.5038724649, -3.5038724649))
                Line((3.5038724649, -3.5038724649), (-3.5038724649, -3.5038724649))
                Line((-3.5038724649, -3.5038724649), (-3.5038724649, 3.5038724649))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=118.11
        extrude(amount=118.11)
    return part.part


# Description: This is a hexagonal shaft or bar stock with a long, straight prismatic body featuring six equally-spaced flat faces along its length and tapered or beveled ends.
def model_108244_329b1876_0019():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.9559109976, perimeter: 58.5109797196
            with BuildLine():
                Line((-3.81, 3.81), (3.81, 3.81))
                Line((-3.81, -3.81), (-3.81, 3.81))
                Line((3.81, -3.81), (-3.81, -3.81))
                Line((3.81, 3.81), (3.81, -3.81))
            make_face()
            with BuildLine():
                Line((-3.5038724649, 3.5038724649), (3.5038724649, 3.5038724649))
                Line((3.5038724649, 3.5038724649), (3.5038724649, -3.5038724649))
                Line((3.5038724649, -3.5038724649), (-3.5038724649, -3.5038724649))
                Line((-3.5038724649, -3.5038724649), (-3.5038724649, 3.5038724649))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=91.44
        extrude(amount=91.44)
    return part.part


# Description: This is a flat parallelogram plate or panel with a dark blue-gray color, featuring a simple rectangular shape with angled sides and no holes or additional features.
def model_108412_8de2f9c3_0000():
    """Model: Stock"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 29728.9728, perimeter: 731.52
            with BuildLine():
                Line((121.92, -60.96), (121.92, 60.96))
                Line((121.92, 60.96), (-121.92, 60.96))
                Line((-121.92, 60.96), (-121.92, -60.96))
                Line((-121.92, -60.96), (121.92, -60.96))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is an elongated hexagonal or octagonal tubular component with a tapered profile, featuring triangulated faceted surfaces along its length and appearing to have internal structural ribbing or segmentation.
def model_108689_b235b790_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.016125, perimeter: 8.1460512242
            with BuildLine():
                Line((1.9050000405, -8.8900000405), (4.4450000405, -8.8900000405))
                Line((5.0800000405, -8.2550000405), (4.4450000405, -8.8900000405))
                Line((1.2700000405, -8.2550000405), (5.0800000405, -8.2550000405))
                Line((1.2700000405, -8.2550000405), (1.9050000405, -8.8900000405))
            make_face()
            # Profile area: 26.61285, perimeter: 21.59
            with BuildLine():
                Line((1.2700000405, -8.2550000405), (5.0800000405, -8.2550000405))
                Line((5.0800000405, -8.2550000405), (5.0800000405, -1.2700000405))
                Line((5.0800000405, -1.2700000405), (1.2700000405, -1.2700000405))
                Line((1.2700000405, -1.2700000405), (1.2700000405, -8.2550000405))
            make_face()
            # Profile area: 6.4516, perimeter: 10.16
            with BuildLine():
                Line((1.9050000405, -11.4300000405), (4.4450000405, -11.4300000405))
                Line((4.4450000405, -11.4300000405), (4.4450000405, -8.8900000405))
                Line((1.9050000405, -8.8900000405), (4.4450000405, -8.8900000405))
                Line((1.9050000405, -8.8900000405), (1.9050000405, -11.4300000405))
            make_face()
        # OneSide extrude, distance=1.778
        extrude(amount=1.778)
    return part.part


# Description: This is a rectangular flat plate or tray with a slightly tapered parallelogram shape, featuring a shallow depth and smooth surfaces with minimal features.
def model_108850_0dcd5ef1_0002():
    """Model: MPPF_FrameBottom1 4x6 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 65.32245, perimeter: 41.91
            with BuildLine():
                Line((0, 3.81), (0, 0))
                Line((0, 0), (17.145, 0))
                Line((17.145, 0), (17.145, 3.81))
                Line((17.145, 3.81), (0, 3.81))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a flat parallelogram plate or panel with a simple planar top surface and beveled or chamfered edges, featuring two diagonal lines scored or embossed across its face, commonly used as a structural component or cover panel in assemblies.
def model_108850_0dcd5ef1_0004():
    """Model: MPPF_FrameBack1 4x6 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 190.306071, perimeter: 56.4896
            with BuildLine():
                Line((0, 11.0998), (0, 0))
                Line((0, 0), (17.145, 0))
                Line((17.145, 0), (17.145, 11.0998))
                Line((17.145, 11.0998), (0, 11.0998))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a long, slender hexagonal or chamfered bar with a uniform rectangular cross-section and beveled or angled end faces, appearing to be a structural support beam or mounting rail.
def model_108851_4d515b10_0005():
    """Model: SoapCutterBedBack1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 58.645044, perimeter: 65.3796
            with BuildLine():
                Line((0, 1.905), (0, 0))
                Line((0, 0), (30.7848, 0))
                Line((30.7848, 0), (30.7848, 1.905))
                Line((30.7848, 1.905), (0, 1.905))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is an elongated hexagonal prism or channel-like structural component with tapered ends, featuring a recessed central slot or cavity running along its length.
def model_108851_4d515b10_0006():
    """Model: SoapCutterBedBack2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.145125, perimeter: 22.86
            with BuildLine():
                Line((0, 1.905), (0, 0))
                Line((0, 0), (9.525, 0))
                Line((9.525, 0), (9.525, 1.905))
                Line((9.525, 1.905), (0, 1.905))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a rectangular tray or shallow pan with a long, elongated flat base, slightly angled side walls, and an open top, featuring a clean, minimalist design with no holes or special features.
def model_108851_4d515b10_0007():
    """Model: SoapCutterBackBar1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 141.9352, perimeter: 66.04
            with BuildLine():
                Line((0, 5.08), (0, 0))
                Line((0, 0), (27.94, 0))
                Line((27.94, 0), (27.94, 5.08))
                Line((27.94, 5.08), (0, 5.08))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a elongated rectangular tray or shallow box with a flat bottom, sloped side walls, and an open top, featuring a tapered wedge-like profile that narrows toward one end.
def model_108851_4d515b10_0009():
    """Model: SoapCutterLeg1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 121.354596, perimeter: 53.4924
            with BuildLine():
                Line((0, 5.7912), (0, 0))
                Line((0, 0), (20.955, 0))
                Line((20.955, 0), (20.955, 5.7912))
                Line((20.955, 5.7912), (0, 5.7912))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform circular cross-section and a slight diagonal orientation.
def model_108852_fed54702_0004():
    """Model: ThreadedRod v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4948315226, perimeter: 2.4936391688
            Circle(0.396875)
        # OneSide extrude, distance=13.97
        extrude(amount=13.97)
    return part.part


# Description: This is a long, slender hexagonal or octagonal bar stock with tapered ends, featuring a beveled or chamfered tip at one end, commonly used as a cutting tool, punch, or structural component.
def model_108855_86bf65d0_0007():
    """Model: Riser1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 425.8056, perimeter: 127
            with BuildLine():
                Line((0, 55.88), (0, 0))
                Line((0, 0), (7.62, 0))
                Line((7.62, 0), (7.62, 55.88))
                Line((7.62, 55.88), (0, 55.88))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a slightly tapered form, featuring a smooth top surface and darker shaded edges that give it a three-dimensional appearance.
def model_108855_86bf65d0_0015():
    """Model: SeatSlat1 v1 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 496.7732, perimeter: 129.54
            with BuildLine():
                Line((0, 8.89), (0, 0))
                Line((0, 0), (55.88, 0))
                Line((55.88, 0), (55.88, 8.89))
                Line((55.88, 8.89), (0, 8.89))
            make_face()
        # OneSide extrude, distance=1.5875
        extrude(amount=1.5875)
    return part.part


# Description: This is a blue elongated flat bar or plate with a parallelogram shape, featuring beveled or chamfered edges at both ends and a slightly curved or textured top surface.
def model_108855_86bf65d0_0016():
    """Model: BackSlat1 v1 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 745.1598, perimeter: 185.42
            with BuildLine():
                Line((0, 8.89), (0, 0))
                Line((0, 0), (83.82, 0))
                Line((83.82, 0), (83.82, 8.89))
                Line((83.82, 8.89), (0, 8.89))
            make_face()
        # OneSide extrude, distance=1.5875
        extrude(amount=1.5875)
    return part.part


# Description: This is an elongated wedge or tapered box-shaped part with a trapezoidal cross-section, featuring a sloped top surface that angles downward from left to right and a flat bottom base.
def model_108855_86bf65d0_0020():
    """Model: ArmTruss1 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 74.1934, perimeter: 36.1763073453
            with BuildLine():
                Line((0, 0), (10.16, 0))
                Line((10.16, 0), (10.16, 2.54))
                Line((2.54, 10.16), (10.16, 2.54))
                Line((0, 10.16), (2.54, 10.16))
                Line((0, 0), (0, 10.16))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a cylindrical pipe or tube with a textured knurled end cap at the top and a smooth tapered body, featuring a diagonal orientation.
def model_109096_01748cff_0001():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a cylindrical filter or strainer component with a dark gray body and a blue perforated mesh top surface, designed for fluid filtration or air flow applications.
def model_109096_01748cff_0002():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((12.2039472976, 0.3462558145)):
                Circle(2.5)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a round knob or dial with a mesh-textured back section and a small protruding tab or pointer on the side, featuring a predominantly flat circular face with a ribbed or latticed rear portion.
def model_109225_9f3d5432_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.030083207, perimeter: 0.7223782095
            with BuildLine():
                CenterArc((0, 0), 1, -5.7391704773, 11.4783409545)
                Line((0.9949874371, -0.1), (1.2, -0.05))
                Line((1.2, 0.05), (1.2, -0.05))
                Line((0.9949874371, 0.1), (1.2, 0.05))
            make_face()
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 1, 5.7391704773, 348.5216590455)
                CenterArc((0, 0), 1, -5.7391704773, 11.4783409545)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a wedge-shaped or trapezoidal prism component with a rectangular base that tapers to a narrower top edge, featuring multiple flat faces and internal geometric subdivisions visible through its semi-transparent rendering.
def model_109232_04340d62_0003():
    """Model: Power supply 12 V v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((0, 3), (3, 3))
                Line((0, 0), (0, 3))
                Line((3, 0), (0, 0))
                Line((3, 3), (3, 0))
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((-3, 3), (0, 3))
                Line((-3, 0), (-3, 3))
                Line((0, 0), (-3, 0))
                Line((0, 0), (0, 3))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a modular storage or containment system consisting of three interlocking hexagonal/trapezoidal boxes with open tops and geometric faceted sides, designed to nest or stack together for compact storage or organization.
def model_109307_a5919b9f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0161250386, perimeter: 8.1460514318
            with BuildLine():
                Line((0.7620000243, 3.9370003486), (4.5720001459, 3.9370003486))
                Line((0.7620000243, 3.9370003486), (1.3970000243, 3.3020003486))
                Line((1.3970000243, 3.3020003486), (3.9370000243, 3.3020003486))
                Line((4.5720001459, 3.9370003486), (3.9370000243, 3.3020003486))
            make_face()
            # Profile area: 26.6128508493, perimeter: 21.5900002432
            with BuildLine():
                Line((0.7620000243, 10.9220003486), (0.7620000243, 3.9370003486))
                Line((0.7620000243, 3.9370003486), (4.5720001459, 3.9370003486))
                Line((4.5720001459, 3.9370003486), (4.5720001459, 10.9220003486))
                Line((0.7620000243, 10.9220003486), (4.5720001459, 10.9220003486))
            make_face()
            # Profile area: 5.9354723789, perimeter: 14.2240004539
            with BuildLine():
                Line((1.3970000243, 3.3020003486), (3.9370000243, 3.3020003486))
                Line((1.3970000243, 3.3020003486), (1.3970000243, 0.7620003486))
                Line((3.9370000243, 0.7620000243), (1.3970000243, 0.7620003486))
                Line((3.9370000243, 3.3020003486), (3.9370000243, 0.7620000243))
            make_face()
            with BuildLine():
                Line((1.7780000567, 1.7780000567), (2.286000073, 1.7780000567))
                Line((1.7780000567, 2.286000073), (1.7780000567, 1.7780000567))
                Line((2.286000073, 2.286000073), (1.7780000567, 2.286000073))
                Line((2.286000073, 1.7780000567), (2.286000073, 2.286000073))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.0480000973, 1.7780000567), (3.0480000973, 2.286000073))
                Line((3.0480000973, 2.286000073), (3.5560001135, 2.286000073))
                Line((3.5560001135, 2.286000073), (3.5560001135, 1.7780000567))
                Line((3.5560001135, 1.7780000567), (3.0480000973, 1.7780000567))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.4112710051, perimeter: 7.9000958761
            with BuildLine():
                Line((1.394650079, -3.3306706918), (3.934650079, -3.330670706))
                Line((0.7596500669, -3.7751707144), (1.394650079, -3.3306706918))
                Line((0.7596500669, -3.7751707144), (4.5695748894, -3.7751708177))
                Line((3.934650079, -3.330670706), (4.5695748894, -3.7751708177))
            make_face()
            # Profile area: 1.4084852582, perimeter: 7.8773300614
            with BuildLine():
                Line((0.7596501041, -1.9971707144), (4.5570422431, -1.9971708772))
                Line((1.3946500473, -2.4416707955), (0.7596501041, -1.9971707144))
                Line((1.3946500473, -2.4416707955), (3.9346500473, -2.441670705))
                Line((3.9346500473, -2.441670705), (4.5570422431, -1.9971708772))
            make_face()
            # Profile area: 0.8383161027, perimeter: 4.2069646666
            with BuildLine():
                Line((4.5570422431, -1.9971708772), (4.5570422431, -2.4416708772))
                Line((3.9346500473, -2.441670705), (4.5570422431, -1.9971708772))
                Line((3.934650079, -3.330670706), (3.9346500473, -2.441670705))
                Line((3.934650079, -3.330670706), (4.5695748894, -3.7751708177))
                Line((4.5695748894, -3.7751708177), (4.5695749015, -3.3306708177))
                Line((4.5570422431, -2.4416708772), (4.5695749015, -3.3306708177))
            make_face()
            # Profile area: 0.8467724671, perimeter: 4.2172324824
            with BuildLine():
                Line((0.7596500669, -3.7751707144), (1.394650079, -3.3306706918))
                Line((1.3946500473, -2.4416707955), (1.394650079, -3.3306706918))
                Line((1.3946500473, -2.4416707955), (0.7596501041, -1.9971707144))
                Line((0.7596501041, -1.9971707144), (0.7596500473, -2.4416707144))
                Line((0.7596500473, -2.4416707144), (0.759650079, -3.3306707144))
                Line((0.759650079, -3.3306707144), (0.7596500669, -3.7751707144))
            make_face()
            # Profile area: 12.4193305765, perimeter: 17.5260006485
            with BuildLine():
                Line((10.7950002432, -3.8100001216), (10.7950002432, -2.0320001216))
                Line((10.7950002432, -3.8100001216), (16.764000535, -3.8100001216))
                Line((16.764000535, -3.8100001216), (17.7800005674, -3.8100001216))
                Line((17.7800005674, -3.8100001216), (17.7800005674, -2.0320001216))
                Line((16.764000535, -2.0320001216), (17.7800005674, -2.0320001216))
                Line((10.7950002432, -2.0320001216), (16.764000535, -2.0320001216))
            make_face()
            # Profile area: 2.2580599237, perimeter: 6.8579999926
            with BuildLine():
                Line((8.1037814356, -2.4416707502), (7.6200002432, -2.4416707502))
                Line((7.6200002432, -3.330670706), (7.6200002432, -2.4416707502))
                Line((8.1280002594, -3.330670706), (7.6200002432, -3.330670706))
                Line((8.1280002594, -3.330670706), (10.1600003242, -3.330670706))
                Line((10.1600003242, -3.330670706), (10.1600002432, -2.4416707502))
                Line((8.1037814356, -2.4416707502), (10.1600002432, -2.4416707502))
            make_face()
            # Profile area: 0.8467724305, perimeter: 4.2182831817
            with BuildLine():
                Line((10.1600003242, -3.330670706), (10.1600002432, -2.4416707502))
                Line((10.7950002432, -3.8100001216), (10.1600003242, -3.330670706))
                Line((10.7950002432, -3.8100001216), (10.7950002432, -2.0320001216))
                Line((10.1600002432, -2.4416707502), (10.7950002432, -2.0320001216))
            make_face()
            # Profile area: 2.2580598696, perimeter: 6.8579998973
            with BuildLine():
                Line((1.3946500473, -2.4416707955), (3.9346500473, -2.441670705))
                Line((1.3946500473, -2.4416707955), (1.394650079, -3.3306706918))
                Line((1.394650079, -3.3306706918), (3.934650079, -3.330670706))
                Line((3.934650079, -3.330670706), (3.9346500473, -2.441670705))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a long, flat rectangular bar or beam with a slightly tapered parallelogram shape, featuring small flanged or beveled edges on both ends and a smooth, plain upper surface.
def model_109382_30283521_0001():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 104.6065257292, perimeter: 72.5119416366
            with BuildLine():
                Line((34.4805173046, 42.3575696543), (34.4805173046, 45.5183465974))
                Line((34.4805173046, 45.5183465974), (1.3853234295, 45.5183465974))
                Line((1.3853234295, 45.5183465974), (1.3853234295, 42.3575696543))
                Line((1.3853234295, 42.3575696543), (34.4805173046, 42.3575696543))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a robotic arm or manipulator joint assembly featuring a curved, hook-like shape with two hexagonal end segments connected by a cylindrical shaft, designed with internal structural ribbing and triangulated geometry for lightweight strength.
def model_109862_ea256f3b_0000():
    """Model: 01-MayaraGualberto-CentroUniversitário Jorge Amado-Body v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 32.4910656512, perimeter: 36.7089228721
            with BuildLine():
                Line((-2.535, 2.065), (-3, 2.065))
                Line((-3, 2.065), (-3, 2.545))
                Line((-3, 2.545), (-5.5, 2.545))
                Line((-5.5, 2.545), (-5.5, 1))
                Line((-5.5, 1), (-4.5, 0))
                Line((-4.5, 0), (-1.4, 0))
                Line((-1.4, 0), (0, 1.4))
                Line((0, 1.4), (0, 8.76))
                Line((0, 8.76), (-1.4, 10.16))
                Line((-1.4, 10.16), (-5.5, 10.16))
                Line((-5.5, 10.16), (-5.5, 8.26))
                Line((-5.5, 8.26), (-2.535, 8.26))
                CenterArc((-2.535, 7.625), 0.635, 0, 90)
                Line((-1.9, 7.625), (-1.9, 2.7))
                CenterArc((-2.535, 2.7), 0.635, -90, 90)
            make_face()
        # Symmetric extrude, full_length=True, total=1.9
        extrude(amount=0.95, both=True)
    return part.part


# Description: This is a elongated cylindrical bar or rod with rounded ends and blue accent lines or grooves running along its length, featuring a dark gray/charcoal finish.
def model_109863_7d9015ee_0001():
    """Model: big link"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0545851724, perimeter: 12.5553093477
            with BuildLine():
                CenterArc((0, 0), 0.25, 90, 180)
                Line((4, -0.25), (0, -0.25))
                CenterArc((4, 0), 0.25, -90, 180)
                Line((0, 0.25), (4, 0.25))
            make_face()
            with BuildLine():
                CenterArc((1.0000000149, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0000000447, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a ski or snowboard with an elongated, pointed oval shape featuring a dark gray/charcoal base with blue striped graphics running lengthwise down the center.
def model_109863_7d9015ee_0002():
    """Model: small link"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1112909198, perimeter: 7.3615041393
            with BuildLine():
                CenterArc((0, 0), 0.25, 90, 180)
                Line((0, -0.25), (2, -0.25))
                CenterArc((2, 0), 0.25, -90, 180)
                Line((0, 0.25), (2, 0.25))
            make_face()
            with BuildLine():
                CenterArc((1.0000000149, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with a solid dark base and perforated mesh sides, featuring an open top and a slightly tapered upper section.
def model_109863_7d9015ee_0003():
    """Model: nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1168672467, perimeter: 1.9477874452
            with BuildLine():
                CenterArc((0, 0), 0.215, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered or rounded end, featuring a smooth, uniform hollow body with no visible holes, slots, or flanges.
def model_109863_7d9015ee_0004():
    """Model: rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0283528737, perimeter: 0.5969026042
            Circle(0.095)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a parallelogram-like overall form, featuring angular faces and what appears to be internal geometric divisions or faceted surfaces on the darker left side.
def model_109880_aebcec75_0001():
    """Model: URS75CCmotor v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.52, perimeter: 23.6
            with BuildLine():
                Line((-4.1, 1.7999999925), (-4.1, -1.8000000075))
                Line((-4.1, -1.8000000075), (4.1, -1.8000000075))
                Line((4.1, -1.8000000075), (4.1, 1.7999999925))
                Line((4.1, 1.7999999925), (-4.1, 1.7999999925))
            make_face()
        # OneSide extrude, distance=9.5
        extrude(amount=9.5)
    return part.part


# Description: This is a cylindrical bucket or container with a curved, tapered design featuring an open top with a rolled rim edge and smooth, slightly sloped side walls.
def model_110043_b73b8beb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a horizontal bar or beam with a rounded rectangular profile featuring symmetrical grooved or ribbed ends on both sides, likely designed for gripping, alignment, or mechanical engagement.
def model_110138_19df5c5e_0010():
    """Model: Rod (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 283.5287369865, perimeter: 59.6902604182
            Circle(9.5)
        # Symmetric extrude, full_length=True, total=150
        extrude(amount=75, both=True)
    return part.part


# Description: This is a toroidal (doughnut-shaped) magnetic core or ferrite component with a central cylindrical void and a rounded, symmetrical outer profile, featuring a smooth curved surface characteristic of electromagnetic transformer or inductor applications.
def model_110138_19df5c5e_0012():
    """Model: Nut (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1168.6724671354, perimeter: 194.7787445226
            with BuildLine():
                CenterArc((0, 0), 21.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 9.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=30
        extrude(amount=15, both=True)
    return part.part


# Description: This is a cylindrical roller or shaft with a textured knurled surface pattern along its length, featuring rounded ends and a smooth, uniform dark finish.
def model_110222_5055efca_0002():
    """Model: w v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical component with a tapered or conical top section that transitions to a flat circular base, featuring a mesh or lattice pattern on the upper portion.
def model_110222_5055efca_0003():
    """Model: y v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: A rounded rectangular bar or beam with a horizontal slot or groove running along its top surface.
def model_110222_5055efca_0004():
    """Model: r v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.8926990817, perimeter: 23.2831853072
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((8.5, -0.5), (0, -0.5))
                CenterArc((8.5, 0), 0.5, -90, 180)
                Line((0, 0.5), (8.5, 0.5))
            make_face()
            with BuildLine():
                CenterArc((8.5, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a dark blue/navy metal bracket or support arm with an elongated, curved trapezoidal shape, featuring internal ribbing or reinforcement patterns and a small hole at the upper end.
def model_110317_4eaf60f5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 41.1097737236, perimeter: 34.1733024437
            with BuildLine():
                Line((0, 2.286), (0, 0))
                Line((0, 0), (5.715, 0))
                Line((5.715, 0), (13.208, 3.4059090909))
                Line((13.208, 3.4059090909), (13.208, 5.461))
                Line((9.144, 5.461), (13.208, 5.461))
                Line((9.144, 5.461), (2.284218031, 2.3429172868))
                CenterArc((2.0214531614, 2.921), 0.635, -90, 24.4439547804)
                Line((2.0214531614, 2.286), (0, 2.286))
            make_face()
            with BuildLine():
                CenterArc((12.2555, 4.699), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a flat, disk-shaped washer with a large central hole and a smooth, slightly curved outer edge, designed to distribute loads and prevent fastener penetration.
def model_110344_a5d1ecce_0002():
    """Model: Washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.0530964915, perimeter: 20.106192983
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is an elongated oval or boat-shaped housing or container with a ribbed/finned top surface and a solid base, featuring internal structural ribs or support elements visible through the transparent top section.
def model_110697_4b2725f1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a dual-wing or double-fin aerodynamic component featuring two parallel trapezoidal wings with angled surfaces, a streamlined tapered profile, and internal structural ribbing, resembling a stabilizer or control surface used in aerospace applications.
def model_110871_4b62f82f_0006():
    """Model: Corner guard"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.62, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.51209375, perimeter: 10.16
            with BuildLine():
                Line((-27.94, 0), (-27.94, -2.54))
                Line((-27.94, -2.54), (-27.6225, -2.54))
                Line((-27.6225, -0.3175), (-27.6225, -2.54))
                Line((-25.4, -0.3175), (-27.6225, -0.3175))
                Line((-25.4, -0.3175), (-25.4, 0))
                Line((-27.94, 0), (-25.4, 0))
            make_face()
            # Profile area: 3.32660625, perimeter: 8.89
            with BuildLine():
                Line((-25.4, -0.3175), (-27.6225, -0.3175))
                Line((-27.6225, -0.3175), (-27.6225, -2.54))
                Line((-27.6225, -2.54), (-26.67, -2.54))
                Line((-26.67, -2.54), (-26.67, -1.27))
                Line((-26.67, -1.27), (-25.4, -1.27))
                Line((-25.4, -1.27), (-25.4, -0.3175))
            make_face()
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175)
    return part.part


# Description: This is a dual-wing or split-body aerodynamic component with two parallel, angled blade-like sections featuring triangulated internal structure and dark leading edges, resembling aircraft wings or fins with a streamlined, tapered design.
def model_110871_4b62f82f_0007():
    """Model: Corner guard (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.62, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8387, perimeter: 10.16
            with BuildLine():
                Line((-25.4, -0.3175), (-25.4, 0))
                Line((-27.94, 0), (-25.4, 0))
                Line((-27.94, 0), (-27.94, -2.54))
                Line((-27.94, -2.54), (-27.6225, -2.54))
                Line((-26.67, -2.54), (-27.6225, -2.54))
                Line((-26.67, -1.27), (-26.67, -2.54))
                Line((-25.4, -1.27), (-26.67, -1.27))
                Line((-25.4, -0.3175), (-25.4, -1.27))
            make_face()
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175)
    return part.part


# Description: This is a rectangular box or enclosure with a complex internal cross-shaped structural framework, featuring four vertical supports and horizontal bracing that create a symmetrical cross-pattern when viewed from the front, likely designed for structural reinforcement or as a component assembly housing.
def model_110956_df981ed9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 22.4475929218, perimeter: 23.3096870058
            with BuildLine():
                Line((2.8229321879, 7.489411927), (2.8229321879, 3.3222263163))
                Line((2.8229321879, 3.3222263163), (8.4687965636, 3.3222263163))
                Line((8.4687965636, 3.3222263163), (8.4687965636, 7.489411927))
                Line((8.4687965636, 7.489411927), (2.8229321879, 7.489411927))
            make_face()
            with BuildLine():
                CenterArc((5.6458643757, 5.3194028302), 0.5862610846, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a rectangular prism or box beam with a longitudinal slot or channel running along its length, featuring a hollow or recessed interior cavity.
def model_111151_7c7f89f6_0001():
    """Model: leg1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.25, perimeter: 10
            with BuildLine():
                Line((2.5, 0), (0, 0))
                Line((0, 0), (0, -2.5))
                Line((0, -2.5), (2.5, -2.5))
                Line((2.5, -2.5), (2.5, 0))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a parallelogram prism or wedge-shaped block with a slanted rectangular form, featuring flat faces and sharp edges, commonly used as a structural component or support bracket in assemblies.
def model_111225_c58b9e26_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 45, perimeter: 28
            with BuildLine():
                Line((2.5, -4.5), (2.5, 4.5))
                Line((2.5, 4.5), (-2.5, 4.5))
                Line((-2.5, 4.5), (-2.5, -4.5))
                Line((-2.5, -4.5), (2.5, -4.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


# Description: This is a magnetic bar or linear magnetic strip with an elongated rectangular prism shape, featuring parallel grooved channels running along its length and a flat mounting surface at one end.
def model_111387_c4243097_0000():
    """Model: crank (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1039269908, perimeter: 2.6283185307
            with BuildLine():
                CenterArc((3.7961702337, -1.3035979929), 0.05, 118.9200440376, 180)
                Line((3.8203496648, -1.3473627631), (4.6956450694, -0.8637741418))
                CenterArc((4.6714656383, -0.8200093716), 0.05, -61.0799559624, 180)
                Line((4.6472862072, -0.7762446013), (3.7719908026, -1.2598332227))
            make_face()
            with BuildLine():
                CenterArc((3.7961702337, -1.3035979929), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.6714656383, -0.8200093716), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a long, narrow rectangular channel or extrusion with a open top profile, featuring angled end caps on both sides and a recessed interior groove running lengthwise along the bottom.
def model_111411_47094743_0001():
    """Model: Gantry Support Angle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.75, perimeter: 12
            with BuildLine():
                Line((3, 0.5), (3, 0))
                Line((0.5, 0.5), (3, 0.5))
                Line((0.5, 3), (0.5, 0.5))
                Line((0, 3), (0.5, 3))
                Line((0, 0), (0, 3))
                Line((3, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=31.2
        extrude(amount=31.2)
    return part.part


# Description: This is a flat parallelogram-shaped plate or bar with a slightly beveled edge, featuring a simple rectangular form with no holes or additional features.
def model_111411_47094743_0002():
    """Model: Connecting Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 187.2, perimeter: 74.4
            with BuildLine():
                Line((-15.6, 3), (15.6, 3))
                Line((-15.6, -3), (-15.6, 3))
                Line((15.6, -3), (-15.6, -3))
                Line((15.6, 3), (15.6, -3))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a straight cylindrical rod or pin with a tapered or pointed end, featuring a simple linear geometry with no holes, slots, or flanges.
def model_111411_47094743_0007():
    """Model: Y-Axis Drive-screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=130
        extrude(amount=130)
    return part.part


# Description: This is a stepped rectangular plate or spacer featuring three parallel horizontal surfaces at progressively offset heights, creating a tiered or stacked appearance with distinct level changes between each plane.
def model_112017_a8394d4b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 72.3822947387, perimeter: 30.1592894745
            with Locations((90.75, 696.6503658489)):
                Circle(4.8)
            # Profile area: 72.3822947387, perimeter: 30.1592894745
            with Locations((-90.75, 696.6503658489)):
                Circle(4.8)
            # Profile area: 72.3822947387, perimeter: 30.1592894745
            with Locations((0, 550)):
                Circle(4.8)
        # Symmetric extrude, full_length=True, total=1600
        extrude(amount=800, both=True)
    return part.part


# Description: This is a tapered rectangular box or tray with a sloped top surface, featuring a elongated hexagonal cross-section that narrows toward one end, with a flat bottom and angled side walls.
def model_112095_1fbe1a75_0000():
    """Model: base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 66, perimeter: 34
            with BuildLine():
                Line((-1.5, -3.5), (-7.5, -3.5))
                Line((-1.5, 7.5), (-1.5, -3.5))
                Line((-7.5, 7.5), (-1.5, 7.5))
                Line((-7.5, -3.5), (-7.5, 7.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical container or housing with a mesh/perforated top opening and vertical ribbed reinforcement features running along its sides.
def model_112375_114c01e5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3570726055, perimeter: 3.9767708012
            with BuildLine():
                Line((0.0479400018, -0.1941694009), (0.0479400018, -0.3971168043))
                CenterArc((0, 0), 0.4, -83.1165540054, 345.7717617812)
                Line((-0.0511360019, -0.3967179216), (-0.0511360019, -0.1933522933))
                CenterArc((0, 0), 0.2, -76.1311646675, 331.3172820284)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a conveyor or chute component featuring an elongated trapezoidal body with a central diagonal ridge, flanged ends, and internal ribbing for structural reinforcement.
def model_112724_2292d43f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8195, perimeter: 11.12
            with BuildLine():
                Line((0, 0.6), (-1.515, 0.6))
                Line((-1.515, 0.6), (-1.515, 1.05))
                Line((-1.215, 1.05), (-1.515, 1.05))
                Line((-1.215, 1.15), (-1.215, 1.05))
                Line((-1.415, 1.15), (-1.215, 1.15))
                Line((-1.415, 1.38), (-1.415, 1.15))
                Line((-1.215, 1.38), (-1.415, 1.38))
                Line((-1.215, 1.38), (-1.215, 1.48))
                Line((-1.665, 1.48), (-1.215, 1.48))
                Line((-1.665, 1.48), (-1.665, -1.2))
                Line((-0.8, -1.2), (-1.665, -1.2))
                Line((-0.8, -1.05), (-0.8, -1.2))
                Line((-1.515, -1.05), (-0.8, -1.05))
                Line((-1.515, 0.45), (-1.515, -1.05))
                Line((0, 0.45), (-1.515, 0.45))
                Line((0, 0.6), (0, 0.45))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular duct or channel component with a tapered, angular design featuring two vertical fins or baffles on the upper section and a sloped internal geometry that appears designed for fluid or air flow direction and control.
def model_112724_d334de09_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7025, perimeter: 9.56
            with BuildLine():
                Line((0, 0.75), (-1.125, 0.75))
                Line((-1.125, 0.75), (-1.125, 1.05))
                Line((-0.825, 1.05), (-1.125, 1.05))
                Line((-0.825, 1.15), (-0.825, 1.05))
                Line((-1.025, 1.15), (-0.825, 1.15))
                Line((-1.025, 1.38), (-1.025, 1.15))
                Line((-0.825, 1.38), (-1.025, 1.38))
                Line((-0.825, 1.38), (-0.825, 1.48))
                Line((-1.275, 1.48), (-0.825, 1.48))
                Line((-1.275, 1.48), (-1.275, -1.2))
                Line((-0.8, -1.2), (-1.275, -1.2))
                Line((-0.8, -1.05), (-0.8, -1.2))
                Line((-1.125, -1.05), (-0.8, -1.05))
                Line((-1.125, 0.6), (-1.125, -1.05))
                Line((0, 0.6), (-1.125, 0.6))
                Line((0, 0.75), (0, 0.6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: A horizontal rectangular bar with rounded ends, featuring two symmetrical recessed slots or vents on opposite sides near each end.
def model_112928_03f271d6_0000():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # TwoSides extrude (symmetric), distance=1.7
        extrude(amount=1.7, both=True)
    return part.part


# Description: This is a simple cylindrical rod or shaft with a straight, elongated rectangular profile and rounded ends, appearing to be a basic mechanical connector or support beam.
def model_113001_c1b164a3_0010():
    """Model: Axle v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0237787148, perimeter: 0.5466371217
            Circle(0.087)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a waist bag or fanny pack featuring a curved, cylindrical main pouch body with a flat rectangular top flange and an angled shoulder strap attachment point, designed for carrying small items at the waist.
def model_113175_b6232bdc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 430.5101803444, perimeter: 211.3327351998
            with BuildLine():
                Line((65, -3.2), (65, 0))
                Line((0, 0), (65, 0))
                Line((0, -3.2), (0, 0))
                Line((0, -3.2), (16.9, -3.2))
                CenterArc((16.9, -8.2), 5, 0, 90)
                Line((21.9, -13.2), (21.9, -8.2))
                CenterArc((32.5, -13.2), 10.6, 180, 180)
                Line((43.1, -13.2), (43.1, -8.2))
                CenterArc((48.1, -8.2), 5, 90, 90)
                Line((48.1, -3.2), (65, -3.2))
            make_face()
            with BuildLine():
                CenterArc((32.5, -13.2), 7.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a polyhedron or truncated geometric solid featuring multiple faceted surfaces with a combination of flat planes and angular edges, primarily composed of dark navy and slate blue faces arranged in an irregular, crystalline-like structure.
def model_113343_e692c488_0002():
    """Model: box v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1600, perimeter: 160
            with BuildLine():
                Line((-20, 20), (20, 20))
                Line((-20, -20), (-20, 20))
                Line((20, -20), (-20, -20))
                Line((20, 20), (20, -20))
            make_face()
        # OneSide extrude, distance=-40
        extrude(amount=-40)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a hollow tubular body, open top and bottom ends, and a fine mesh or grid pattern covering its curved surface.
def model_113356_bc60a46d_0001():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            with Locations((1.8000000268, 1.6000000238)):
                Circle(0.5000000075)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a stepped or bent flat plate with two rectangular parallelogram-shaped sections connected at an angle, featuring a diagonal slot or cutout across each section and dark edges indicating thickness and depth.
def model_113364_10837c89_0001():
    """Model: ashilok3 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.5, perimeter: 32.1803398875
            with BuildLine():
                Line((5, -0.5), (0, -0.5))
                Line((10, -3), (5, -0.5))
                Line((15, -3), (10, -3))
                Line((15, -2.5), (15, -3))
                Line((10, -2.5), (15, -2.5))
                Line((5, 0), (10, -2.5))
                Line((0, 0), (5, 0))
                Line((0, -0.5), (0, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slight trapezoidal profile, featuring clean edges and a uniform thickness, commonly used as a structural component or mounting bracket.
def model_113447_92e93a1b_0000():
    """Model: achter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 629.8051020408, perimeter: 121.3296262849
            with BuildLine():
                Line((0, 37.5), (0, 0))
                Line((0, 0), (17, 0))
                Line((17, 0), (15.4, 11.7))
                Line((15.4, 11.7), (13.3, 24.9))
                Line((13.3, 24.9), (12.4317518638, 29.6564897895))
                Line((12.4317518638, 29.6564897895), (11, 37.5))
                Line((8.5510204082, 47.5), (11, 37.5))
                Line((0, 47.5), (8.5510204082, 47.5))
                Line((0, 37.5), (0, 47.5))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a composite aerospace or industrial structural component featuring an elongated, horizontally-oriented body with a tapered nose section on the left, a central ribbed or segmented mid-section, and a rectangular solar panel or heat sink array on the right side, designed for modular assembly.
def model_113447_92e93a1b_0001():
    """Model: plank 1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 72 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 67.3206195997, perimeter: 67.798229715
            with BuildLine():
                Line((0, -0.7), (0.4, -0.7))
                Line((0.4, -0.7), (0.4, -2.2))
                Line((0.4, -2.2), (0, -2.2))
                Line((0, -2.8), (0, -2.2))
                Line((0.4, -2.8), (0, -2.8))
                Line((0.4, -4.3), (0.4, -2.8))
                Line((0, -4.3), (0.4, -4.3))
                Line((0, -5), (0, -4.3))
                Line((1, -5), (0, -5))
                Line((1, -4.6), (1, -5))
                Line((3, -4.6), (1, -4.6))
                Line((3, -5), (3, -4.6))
                Line((5.5, -5), (3, -5))
                Line((5.5, -4.6), (5.5, -5))
                Line((7.5, -4.6), (5.5, -4.6))
                Line((7.5, -5), (7.5, -4.6))
                Line((9.5, -5), (7.5, -5))
                Line((9.5, -5), (9.5, -4.6))
                Line((9.5, -4.6), (11.5, -4.6))
                Line((11.5, -4.6), (11.5, -5))
                Line((14, -5), (11.5, -5))
                Line((14, -5), (14, -4.6))
                Line((14, -4.6), (16, -4.6))
                Line((16, -4.6), (16, -5))
                Line((17, -5), (16, -5))
                Line((17, 0), (17, -5))
                Line((16, 0), (17, 0))
                Line((16, -0.4), (16, 0))
                Line((14, -0.4), (16, -0.4))
                Line((14, 0), (14, -0.4))
                Line((11.5, 0), (14, 0))
                Line((11.5, -0.4), (11.5, 0))
                Line((9.5, -0.4), (11.5, -0.4))
                Line((9.5, 0), (9.5, -0.4))
                Line((7.5, 0), (9.5, 0))
                Line((7.5, 0), (7.5, -0.4))
                Line((7.5, -0.4), (5.5, -0.4))
                Line((5.5, -0.4), (5.5, 0))
                Line((3, 0), (5.5, 0))
                Line((3, 0), (3, -0.4))
                Line((3, -0.4), (1, -0.4))
                Line((1, -0.4), (1, 0))
                Line((0, 0), (1, 0))
                Line((0, -0.7), (0, 0))
            make_face()
            with BuildLine():
                Line((1.6000000238, -2.7000000283), (1.6000000238, -2.6000000283))
                CenterArc((2.3000000238, -2.6000000283), 0.7, 90, 90)
                Line((2.3000000238, -1.9000000283), (7.9000000238, -1.9000000283))
                CenterArc((7.9000000238, -2.6000000283), 0.7, 0, 90)
                Line((8.6000000238, -2.6000000283), (8.6000000238, -2.7000000283))
                CenterArc((7.9000000238, -2.7000000283), 0.7, -90, 90)
                Line((7.9000000238, -3.4000000283), (2.3000000238, -3.4000000283))
                CenterArc((2.3000000238, -2.7000000283), 0.7, -180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a flat, parallelogram-shaped mounting bracket or frame with a large rectangular cutout in the center and small notches on the left side for fastening or alignment purposes.
def model_113447_92e93a1b_0003():
    """Model: wand"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4, perimeter: 2.8
            with BuildLine():
                Line((1, 0), (1, 0.4))
                Line((1, 0.4), (0, 0.4))
                Line((0, 0.4), (0, 0))
                Line((0, 0), (1, 0))
            make_face()
            # Profile area: 62.8862076595, perimeter: 78.211287171
            with BuildLine():
                Line((1, 0), (17, 0))
                Line((17, 0), (16.1870534848, 5.9446713924))
                Line((16.1870534848, 5.9446713924), (0, 5.9446713924))
                Line((0, 5.9446713924), (0, 5.5))
                Line((0, 5.5), (0.4, 5.5))
                Line((0.4, 5.5), (0.4, 4))
                Line((0.4, 4), (0, 4))
                Line((0, 4), (0, 2.7469418932))
                Line((0, 2.7469418932), (0.4, 2.7469418932))
                Line((0.4, 2.7469418932), (0.4, 1.2469418932))
                Line((0.4, 1.2469418932), (0, 1.2469418932))
                Line((0, 1.2469418932), (0, 0.4))
                Line((1, 0.4), (0, 0.4))
                Line((1, 0), (1, 0.4))
            make_face()
            with BuildLine():
                Line((1.7148825429, 1.6465924513), (1.7148825429, 4.2459686691))
                Line((1.7148825429, 4.2459686691), (14.855287472, 4.2459686691))
                Line((14.855287472, 4.2459686691), (14.855287472, 1.6465924513))
                Line((14.855287472, 1.6465924513), (1.7148825429, 1.6465924513))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4)
    return part.part


# Description: This is a roof rack or carrier bar featuring an elongated rectangular body with rounded end caps, dual longitudinal slots or channels along the top surface, and black rubber grip pads on both ends for secure mounting.
def model_113545_54cc71a3_0002():
    """Model: Link_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5340707511, perimeter: 11.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, -0.5), (3, -0.5))
                CenterArc((3, 0), 0.5, -90, 180)
                Line((3, 0.5), (0, 0.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.1
        extrude(amount=0.05, both=True)
    return part.part


# Description: This is an insect wing (likely a dragonfly or similar flying insect) featuring an elongated elliptical shape with a network of radiating veins and cross-bracing ribs that create a structural framework across the translucent surface.
def model_113554_8fdfcd6c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.570686039, perimeter: 16.0778998802
            Circle(2.5588772405)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform circular cross-section and slightly rounded ends, featuring no holes, slots, or flanges.
def model_113698_dcf18f66_0020():
    """Model: ALU_ROD29.3 V2 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=2.93
        extrude(amount=2.93)
    return part.part


# Description: This is a carabiner or climbing hook with an elongated oval body, curved ends with hook-like openings at both the top and bottom, and a streamlined profile designed for connecting or securing objects.
def model_113844_4abc5651_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 106 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9134784974, perimeter: 19.618860733
            with BuildLine():
                CenterArc((3.2000000473, -112.5000016854), 116.8072485197, 88.7282408102, 1.9087621566)
                CenterArc((1.6185185427, -7.0833334391), 11.3868753459, 88.5765320619, 10.1583198997)
                CenterArc((1.6185185427, -7.0833334391), 11.3868753459, 98.7348519617, 1.9602737348)
                CenterArc((1.6185185427, -7.0833334391), 11.3868753459, 100.6951256964, 4.5610018586)
                CenterArc((-1.1543712054, 3.6184016983), 0.3612168556, 128.2018669445, 45.8038441616)
                CenterArc((1.6185185427, -7.0833334391), 11.1868753459, 91.4622578575, 14.7969144311)
                CenterArc((1.6185185427, -7.0833334391), 11.1868753459, 90.6778016114, 0.784456246)
                CenterArc((1.6185185427, -7.0833334391), 11.1868753459, 88.5581851141, 2.1196164974)
                CenterArc((3.2000000473, -112.5000016854), 116.6072485197, 89.0943966076, 1.5443806419)
                CenterArc((3.2000000473, -112.5000016854), 116.6072485197, 87.5772021124, 1.5171944953)
                CenterArc((7.4843888896, 3.643385538), 0.7384576412, 29.1432255976, 21.0068400888)
                CenterArc((3.2000000473, -112.5000016854), 116.8072485197, 87.6656884593, 0.7665469431)
                CenterArc((3.2000000473, -112.5000016854), 116.8072485197, 88.4322354023, 0.2960054078)
            make_face()
            # Profile area: 10.2198760361, perimeter: 102.8497619471
            with BuildLine():
                CenterArc((7.4843888896, 3.643385538), 0.7384576412, 29.1432255976, 21.0068400888)
                CenterArc((3.2000000473, -112.5000016854), 116.6072485197, 87.5500159657, 0.0271861466)
                CenterArc((8.2060138632, 4.500201227), 0.5000000001, -92.449984034, 3.3701793423)
                CenterArc((8.2535715516, 1.5392857372), 2.4612973966, 74.3436733634, 16.5765219452)
                CenterArc((8.7828601359, 3.4278145488), 0.5, 66.3518415101, 7.9918318533)
                CenterArc((8.3583334579, 2.45833337), 1.558355638, 37.1762892681, 29.175552242)
                CenterArc((-0.9841186852, -6.4367656547), 14.4494128224, 37.0869944364, 5.8170592503)
                CenterArc((-0.9841186852, -6.4367656547), 14.4494128224, 36.7929384781, 0.2940559583)
                CenterArc((10.1866435369, 1.9178851141), 0.5, 31.6200810304, 5.1728574478)
                CenterArc((8.2698622577, 0.737747152), 2.7509500398, -6.6109363121, 38.2310173425)
                CenterArc((10.5058453006, 0.4786025713), 0.5, -10.5689484517, 3.9580121396)
                CenterArc((11.4630684871, 0.3000000045), 0.4737428334, 169.4310515483, 45.1934095903)
                CenterArc((8.9698619114, -0.9648945643), 2.3271444764, 4.8210310791, 20.5114541591)
                CenterArc((10.7905420918, -0.811334743), 0.5, -10.7324453482, 15.5534764274)
                CenterArc((8.8085196074, -0.4356651341), 2.5173102844, -43.8194346963, 33.0869893481)
                CenterArc((10.2640602415, -1.8324264759), 0.5, -80.537677792, 36.7182430957)
                Line((10.3462597352, -2.3256234378), (9.9000001475, -2.4000000358))
                CenterArc((5.2342066049, -3.081580084), 4.7153134302, 8.3109942821, 13.8882488418)
                CenterArc((7.450000111, -2.2500000335), 2.3505318897, 23.8387401832, 34.4810889862)
                CenterArc((8.4218572068, -0.6752105046), 0.5, 58.3198291694, 21.5031902443)
                CenterArc((7.5766440638, -5.3835605715), 5.2836121926, 79.8230194137, 20.8661167972)
                CenterArc((6.6893782395, -0.6829536993), 0.5, 100.6891362109, 10.6440512943)
                CenterArc((7.1992575561, -1.9884916078), 1.9015727408, 111.3331875052, 52.9012917652)
                CenterArc((16.233458696, -4.4969024565), 11.27753338, 164.4405167117, 6.3912012426)
                Line((5.100000076, -2.7000000402), (0.822181974, -2.8270639263))
                Line((0.822181974, -2.8270639263), (0.6718483706, -2.8315292802))
                Line((0.6718483706, -2.8315292802), (-5, -3))
                CenterArc((-8.9408042111, -2.7242339482), 3.9504410824, -4.0028672847, 17.5330253698)
                CenterArc((-7.5194445565, -2.4194444805), 2.4974833384, 14.3608181911, 37.7753897297)
                CenterArc((-6.2934164136, -0.8424870683), 0.5, 52.1362079208, 17.8049424466)
                CenterArc((-7.2931276295, -3.5804178242), 3.4147362383, 69.9411503675, 43.6619106611)
                CenterArc((-8.4601821568, -0.909524515), 0.5, 113.6030610285, 15.7153384453)
                CenterArc((-7.4391092124, -2.1562148444), 2.1114672617, 129.3183994738, 42.7078346089)
                CenterArc((-7.9358308496, -2.2769467119), 1.647114237, 165.4558217115, 48.628084945)
                CenterArc((-9.1935584192, -1.1941717969), 2.008650495, 177.3128106788, 89.6495681902)
                CenterArc((-10.7000001594, -1.1000000164), 0.5000000075, 126.8698976458, 53.1301023542)
                CenterArc((-8.4794438437, -0.9051390841), 2.5288903106, 145.4224019247, 29.9247542903)
                CenterArc((-9.7731895269, -0.0657748853), 0.988258157, 100.2662195131, 42.6547752908)
                CenterArc((-3.2149245314, -26.7892313681), 28.5028867404, 97.9813904915, 5.6851422412)
                CenterArc((-9.0840086265, 21.4774160279), 20.1308116421, -84.5515689424, 3.3269113813)
                CenterArc((-5.9365610168, 1.088106021), 0.5, 74.0632430332, 24.7120994058)
                CenterArc((-5.123630866, 3.9349864833), 2.4606728622, -105.9367569668, 5.8645356604)
                CenterArc((-5.4687254378, 3.0181091663), 1.5082830707, -93.2401922655, 11.3936468003)
                CenterArc((-5.3257258722, 2.0200180508), 0.5, -81.8465454652, 27.3376955548)
                CenterArc((16.72652666, -28.9062028885), 37.4833250694, 124.5719032546, 0.919246835)
                CenterArc((16.72652666, -28.9062028885), 37.4833250694, 123.6526564196, 0.919246835)
                CenterArc((6.9933078515, -14.7866157149), 20.3381720236, 115.4072176176, 7.4634118656)
                CenterArc((-1.5182385138, 3.1328331525), 0.5, 107.0685051081, 8.3387125094)
                CenterArc((1.6185185427, -7.0833334391), 11.1868753459, 106.2591722886, 0.8093328196)
                CenterArc((-1.1543712054, 3.6184016983), 0.3612168556, 128.2018669445, 45.8038441616)
                CenterArc((1.6185185427, -7.0833334391), 11.3868753459, 105.2561275551, 1.812377553)
                CenterArc((-1.5182385138, 3.1328331525), 0.7, 107.0685051081, 8.3387125094)
                CenterArc((6.9933078515, -14.7866157149), 20.5381720236, 115.4072176176, 7.4672238491)
                CenterArc((16.72652666, -28.9062028885), 37.6833250694, 123.6505834439, 1.8405666457)
                CenterArc((-5.3257258722, 2.0200180508), 0.3, -81.8465454652, 27.3376955548)
                CenterArc((-5.4687254378, 3.0181091663), 1.3082830707, -92.724757125, 10.8782116598)
                CenterArc((-5.123630866, 3.9349864833), 2.2606728622, -105.9367569668, 5.5575489553)
                CenterArc((-5.9365610168, 1.088106021), 0.7, 74.0632430332, 24.7120994058)
                CenterArc((-9.0840086265, 21.4774160279), 19.9308116421, -84.5642258316, 3.3395682705)
                CenterArc((-3.2149245314, -26.7892313681), 28.7028867404, 97.9725268353, 5.6826812157)
                CenterArc((-9.7731895269, -0.0657748853), 1.188258157, 100.5651313415, 42.572094364)
                CenterArc((-8.4794438437, -0.9051390841), 2.7288903106, 145.3332049519, 28.2775286968)
                CenterArc((-10.7000001594, -1.1000000164), 0.7000000075, 134.5858766441, 45.0070306727)
                CenterArc((-9.1935584192, -1.1941717969), 2.208650495, 177.4271539984, 100.9136709382)
                CenterArc((-7.9358308496, -2.2769467119), 1.447114237, 165.0045962443, 64.6247995658)
                CenterArc((-7.4391092124, -2.1562148444), 1.9114672617, 129.3183994738, 43.0545960542)
                CenterArc((-8.4601821568, -0.909524515), 0.3, 113.6030610285, 15.7153384453)
                CenterArc((-7.2931276295, -3.5804178242), 3.2147362383, 69.9411503675, 43.6619106611)
                CenterArc((-6.2934164136, -0.8424870683), 0.3, 52.1362079208, 17.8049424466)
                CenterArc((-7.5194445565, -2.4194444805), 2.2974833384, 14.3966892489, 37.739518672)
                CenterArc((-8.9408042111, -2.7242339482), 3.7504410824, -7.3906613677, 20.8984961888)
                Line((5.2723659912, -2.8949684685), (-5.2215212622, -3.2066680457))
                CenterArc((16.233458696, -4.4969024565), 11.07753338, 164.4424200171, 7.2428220422)
                CenterArc((7.1992575561, -1.9884916078), 1.7015727408, 111.3331875052, 52.8894652897)
                CenterArc((6.6893782395, -0.6829536993), 0.3, 100.6891362109, 10.6440512943)
                CenterArc((7.5766440638, -5.3835605715), 5.0836121926, 79.8230194137, 20.8661167972)
                CenterArc((8.4218572068, -0.6752105046), 0.3, 58.3198291694, 21.5031902443)
                CenterArc((7.450000111, -2.2500000335), 2.1505318897, 23.9141138953, 34.4057152741)
                CenterArc((5.2342066049, -3.081580084), 4.5153134302, 5.719574525, 16.4429423424)
                Line((10.3791395326, -2.5229022226), (9.7270409097, -2.6315853264))
                CenterArc((10.2640602415, -1.8324264759), 0.7, -80.537677792, 36.7182430957)
                CenterArc((8.8085196074, -0.4356651341), 2.7173102844, -43.8194346963, 33.0869893481)
                CenterArc((10.7905420918, -0.811334743), 0.7, -10.7324453482, 15.5534764274)
                CenterArc((8.9698619114, -0.9648945643), 2.5271444764, 4.8210310791, 20.9379456784)
                CenterArc((11.4630684871, 0.3000000045), 0.2737428334, 169.4310515483, 48.0657696525)
                CenterArc((10.5058453006, 0.4786025713), 0.7, -10.5689484517, 3.9580121396)
                CenterArc((8.2698622577, 0.737747152), 2.9509500398, -6.6109363121, 38.2310173425)
                CenterArc((10.1866435369, 1.9178851141), 0.7, 31.6200810304, 5.1728574478)
                CenterArc((-0.9841186852, -6.4367656547), 14.6494128224, 36.7929384781, 6.0730332913)
                CenterArc((8.3583334579, 2.45833337), 1.758355638, 37.5109987194, 28.8408427907)
                CenterArc((8.7828601359, 3.4278145488), 0.7, 66.3518415101, 7.9918318533)
                CenterArc((8.2535715516, 1.5392857372), 2.6612973966, 74.3436733634, 16.5765219452)
                CenterArc((8.2060138632, 4.500201227), 0.3000000001, -92.449984034, 3.370179342)
                CenterArc((3.2000000473, -112.5000016854), 116.8072485197, 87.5500159657, 0.1156724935)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular box-shaped connector or bracket with a cylindrical opening on the left end, featuring internal ribbing/webbing for structural support and internal geometry visible through transparent sections.
def model_114345_228b4786_0004():
    """Model: Leva v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3006814114, perimeter: 2.5826548131
            with BuildLine():
                Line((0.4799999893, 0), (0.95, 0))
                CenterArc((0.95, 0.05), 0.05, -90, 90)
                Line((1, 0.05), (1, 0.25))
                CenterArc((0.95, 0.25), 0.05, 0, 90)
                Line((0.95, 0.3), (0.4799999893, 0.2999999933))
                CenterArc((0.45, 0.3), 0.0299999893, -0.0000128066, 180.0000256132)
                Line((0.4199999906, 0.2999999933), (0.0500000137, 0.3))
                CenterArc((0.0500000128, 0.2499999743), 0.0500000257, 89.9999989616, 90.0000010384)
                Line((-0.0000000128, 0.2499999743), (0, 0.05))
                CenterArc((0.05, 0.05), 0.05, -180, 90)
                Line((0.05, 0), (0.4199999906, 0))
                CenterArc((0.4499999955, 0.0000000056), 0.0300000049, -179.9999893278, 179.9999786557)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a long, flat rectangular plate or bar with a slight trapezoidal profile, featuring a dark blue-gray finish and angled edges along its length.
def model_115093_424371f6_0001():
    """Model: Slice"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on Plane1 construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5759722041, 0, 0.4222804794), x_dir=(0.9659258263, 0, 0.2588190451), z_dir=(-0.2588190451, 0, 0.9659258263))):
            # Profile area: 141.9352, perimeter: 66.04
            with BuildLine():
                Line((-15.6015664839, 2.54), (12.3384335161, 2.54))
                Line((-15.6015664839, -2.54), (-15.6015664839, 2.54))
                Line((12.3384335161, -2.54), (-15.6015664839, -2.54))
                Line((12.3384335161, 2.54), (12.3384335161, -2.54))
            make_face()
        # Symmetric extrude, each_side=0.3175
        extrude(amount=0.3175, both=True)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a solid body, rounded top edge, and a mesh or perforated pattern visible on the upper portions, featuring what appears to be a central hollow core.
def model_115406_3e093a37_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2023185669, perimeter: 2.8902652413
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a hexagonal shaft or tool holder with a long, slender body featuring internal grooves or flutes running along its length and beveled/chamfered ends.
def model_115406_f90aa3dd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.1195752281, perimeter: 14.4053096491
            with BuildLine():
                Line((0, 0.7), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 0.7))
                Line((6, 0.7), (0, 0.7))
            make_face()
            with BuildLine():
                CenterArc((3, 0.35), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a cylindrical pressure vessel or tank with a curved hemispherical or domed end cap, featuring a fine mesh/grid surface pattern that suggests internal structural ribbing or reinforcement.
def model_115421_1876edbd_0008():
    """Model: Pin Center v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1809557368, perimeter: 1.5079644737
            Circle(0.24)
        # Symmetric extrude, full_length=True, total=0.4
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform diameter and tapered or rounded ends, featuring a smooth, elongated design.
def model_115421_1876edbd_0010():
    """Model: Pin Long v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1809557368, perimeter: 1.5079644737
            Circle(0.24)
        # Symmetric extrude, full_length=True, total=5.4
        extrude(amount=2.7, both=True)
    return part.part


# Description: This is a rod or shaft assembly with a cylindrical blue steel body featuring three black rubber or elastomer end caps/bumpers - one at each end and one in the middle - designed to provide cushioning and grip points.
def model_115421_1876edbd_0011():
    """Model: Link Arm v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4898124625, perimeter: 26.2739164744
            with BuildLine():
                CenterArc((-4.5398, 0), 0.44, 30, 300)
                Line((-4.1587488223, -0.22), (-0.3810511777, -0.22))
                CenterArc((0, 0), 0.44, -150, 120)
                Line((0.3810511777, -0.22), (4.1587488223, -0.22))
                CenterArc((4.5398, 0), 0.44, -150, 300)
                Line((0.3810511777, 0.22), (4.1587488223, 0.22))
                CenterArc((0, 0), 0.44, 30, 120)
                Line((-4.1587488223, 0.22), (-0.3810511777, 0.22))
            make_face()
            with BuildLine():
                CenterArc((-4.5398, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5398, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.2
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a claw hammer featuring a flat, textured striking head with a curved claw on one end and a cylindrical handle extending downward at an angle.
def model_115430_67c93e4d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.4882946435, perimeter: 36.7905301854
            with BuildLine():
                CenterArc((2.2093980381, 6.9585154448), 0.2, -128.4531787923, 73.2337489317)
                CenterArc((3.3111223864, 5.3721942374), 1.7313755493, 61.1416328558, 63.6389372836)
                CenterArc((4.1950286833, 6.9761412631), 0.1, -118.8583671442, 144.0819633317)
                CenterArc((0, 5), 4.7371758588, 25.2235961876, 61.2206570549)
                CenterArc((0.300000003, 9.8278639466), 0.1, 180, 86.4442532424)
                Line((0.200000003, 9.8278639466), (0.200000003, 9.900000149))
                CenterArc((0.100000003, 9.900000149), 0.1, 0, 90)
                Line((0.100000003, 10.000000149), (-0.100000003, 10.000000149))
                CenterArc((-0.100000003, 9.900000149), 0.1, 90, 90)
                Line((-0.200000003, 9.900000149), (-0.200000003, 9.8278639466))
                CenterArc((-0.300000003, 9.8278639466), 0.1, -86.4442532424, 86.4442532424)
                CenterArc((0, 5), 4.7371758588, 93.5557467576, 61.2206570549)
                CenterArc((-4.1950286833, 6.9761412631), 0.1, 154.7764038124, 144.0819633317)
                CenterArc((-3.3111223864, 5.3721942374), 1.7313755493, 52.8476351539, 66.0107319903)
                CenterArc((-2.2050875195, 6.8318597046), 0.1, -127.1523648461, 78.4425549306)
                CenterArc((-1.2000000179, 5.6873974785), 1.4231528725, 54.0964428549, 77.1937472296)
                CenterArc((-0.600000003, 6.516156661), 0.4, 0, 54.0964428549)
                Line((-0.200000003, 6.516156661), (-0.200000003, 1.0000000149))
                CenterArc((-0.8000000119, 1.0000000149), 0.6000000089, -171.7867894039, 171.7867894039)
                CenterArc((-1.492820344, 0.9000000149), 0.1, 8.2132105961, 81.7867894039)
                Line((-1.6944272179, 1.0000000149), (-1.492820344, 1.0000000149))
                CenterArc((-1.6944272179, 0.9000000149), 0.1, 90, 96.3793701024)
                CenterArc((-0.8000000119, 1.0000000149), 1.0000000149, -173.6206298976, 173.6206298976)
                Line((0.200000003, 1.0000000149), (0.200000003, 6.516156661))
                CenterArc((0.600000003, 6.516156661), 0.4, 125.9035571451, 54.0964428549)
                CenterArc((1.2000000179, 5.6873974785), 1.4231528725, 51.5468212077, 74.3567359374)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a bracket or mounting component with an overall angular, bent configuration featuring a wider flanged base on the left connected to a narrower vertical arm on the right, with internal ribs and reinforcing members visible throughout for structural stiffness.
def model_115518_278ce3a6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5, perimeter: 17
            with BuildLine():
                Line((-4, 6.5), (-4, 5.5))
                Line((-4, 5.5), (-4, 3.5))
                Line((-4, 3.5), (-3.5, 3.5))
                Line((-3.5, 3.5), (-3, 3.5))
                Line((-3, 3.5), (-3, 11))
                Line((-3, 11), (-4, 11))
                Line((-4, 11), (-4, 6.5))
            make_face()
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((-6, 5.5), (-4, 5.5))
                Line((-4, 6.5), (-4, 5.5))
                Line((-4, 6.5), (-6, 6.5))
                Line((-6, 5.5), (-6, 6.5))
            make_face()
            # Profile area: 22, perimeter: 18.8284271247
            with BuildLine():
                Line((-10, 3.5), (-6, 3.5))
                Line((-6, 3.5), (-6, 5.5))
                Line((-6, 5.5), (-6, 6.5))
                Line((-6, 6.5), (-6, 9.5))
                Line((-6, 9.5), (-8, 9.5))
                Line((-10, 7.5), (-8, 9.5))
                Line((-10, 3.5), (-10, 7.5))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a conveyor or chute assembly with a long, tapered blue channel/trough featuring two dark mounting boxes or hoppers positioned along its length, connected by structural framework with diagonal bracing elements.
def model_115527_ae156ba0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 39 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 75, perimeter: 56
            with BuildLine():
                Line((-103, 17), (-103, 20))
                Line((-103, 20), (-128, 20))
                Line((-128, 20), (-128, 17))
                Line((-128, 17), (-103, 17))
            make_face()
            # Profile area: 45, perimeter: 36
            with BuildLine():
                Line((-100, 27), (-100, 30))
                Line((-85, 27), (-100, 27))
                Line((-85, 30), (-85, 27))
                Line((-100, 30), (-85, 30))
            make_face()
            # Profile area: 1680, perimeter: 1126
            with BuildLine():
                Line((-50, 27), (-50, 30))
                Line((-50, 0), (-50, 27))
                Line((0, 0), (-50, 0))
                Line((0, 3), (0, 0))
                Line((0, 3), (-47, 3))
                Line((-47, 3), (-47, 17))
                Line((-47, 17), (-47, 20))
                Line((-47, 20), (-47, 37))
                Line((-47, 37), (28, 37))
                Line((28, 37), (28, 58))
                Line((28, 58), (-75, 58))
                Line((-178, 58), (-75, 58))
                Line((-178, 37), (-178, 58))
                Line((-103, 37), (-178, 37))
                Line((-103, 20), (-103, 37))
                Line((-103, 17), (-103, 20))
                Line((-103, 3), (-103, 17))
                Line((-150, 3), (-103, 3))
                Line((-150, 3), (-150, 0))
                Line((-150, 0), (-100, 0))
                Line((-100, 0), (-100, 27))
                Line((-100, 27), (-100, 30))
                Line((-100, 30), (-100, 40))
                Line((-100, 40), (-175, 40))
                Line((-175, 40), (-175, 55))
                Line((-175, 55), (-75, 55))
                Line((25, 55), (-75, 55))
                Line((25, 40), (25, 55))
                Line((-50, 40), (25, 40))
                Line((-50, 30), (-50, 40))
            make_face()
            # Profile area: 45, perimeter: 36
            with BuildLine():
                Line((-65, 30), (-65, 27))
                Line((-65, 27), (-50, 27))
                Line((-50, 27), (-50, 30))
                Line((-50, 30), (-65, 30))
            make_face()
            # Profile area: 75, perimeter: 56
            with BuildLine():
                Line((-47, 17), (-47, 20))
                Line((-22, 17), (-47, 17))
                Line((-22, 20), (-22, 17))
                Line((-47, 20), (-22, 20))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform circular cross-section and slightly tapered or rounded ends, appearing to be a simple mechanical component used for structural support or as part of an assembly.
def model_115533_04a1bec1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=22
        extrude(amount=22)
    return part.part


# Description: This is a curved enclosure or housing component with an irregular polygonal shape, featuring a rounded cylindrical side, flat and angled panels, and what appears to be a ventilation slot or opening on the curved surface.
def model_115533_96d86c9a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.7099380499, perimeter: 22.246901784
            with BuildLine():
                Line((0, 1.5000000224), (4, 1.5000000224))
                CenterArc((0, 0), 1.5000000224, 90, 180)
                Line((4, -1.5), (0, -1.5000000224))
                Line((4, 1.5000000224), (4, -1.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.8, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.95), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.95), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a turning tool holder or boring bar with a long, slender cylindrical shaft and a cutting tool insert mounted at the angled head, designed for lathe machining operations.
def model_115535_a171c715_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.3165575598, perimeter: 22.6267623112
            with BuildLine():
                Line((2.7725730896, 3.38119328), (3.7729141602, 3.38119328))
                Line((2.7725730896, 3.38119328), (2.7725730896, 1.7573096156))
                Line((2.7725730896, 1.7573096156), (2.7725730896, 1.2844290676))
                Line((2.7725730896, 1.2844290676), (2.7725730896, -6.9318468051))
                Line((3.7729141602, -6.9318468051), (2.7725730896, -6.9318468051))
                Line((3.7729141602, 3.38119328), (3.7729141602, -6.9318468051))
            make_face()
            # Profile area: 0.5431573569, perimeter: 3.0234836905
            with BuildLine():
                Line((2.0104084644, 2.0104006131), (2.7725730896, 1.7573096156))
                Line((2.0104084644, 1.0579792278), (2.0104084644, 2.0104006131))
                Line((2.7725730896, 1.2844290676), (2.0104084644, 1.0579792278))
                Line((2.7725730896, 1.7573096156), (2.7725730896, 1.2844290676))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a modular bracket or connector assembly with an overall angular, L-shaped form consisting of a long rectangular base section with perpendicular box-like extensions at each end, featuring internal cavities, slots, and mounting surfaces designed for assembly or attachment purposes.
def model_115535_be2c18b0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8391436293, perimeter: 8.7914360605
            with BuildLine():
                Line((0.7957180034, 1.1), (0.7957180034, 0.9000000104))
                Line((0.7957180034, 1.1), (0, 1.1))
                Line((0, 1.1), (0, 0.4))
                Line((1.1, 0.4), (0, 0.4))
                Line((1.1, 0.4), (1.8, 0.4))
                Line((1.8, 0.4), (1.8, 0.2))
                Line((1.8, 0.2), (1.1, 0.2))
                Line((1.1, 0.2), (1.1, 0))
                Line((1.1, 0), (1.9, 0))
                Line((2.0000000298, 0), (1.9, 0))
                Line((2.0000000298, 0.6000000089), (2.0000000298, 0))
                Line((0.200000003, 0.6000000089), (2.0000000298, 0.6000000089))
                Line((0.200000003, 0.9000000104), (0.200000003, 0.6000000089))
                Line((0.7957180034, 0.9000000104), (0.200000003, 0.9000000104))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a curved plastic or composite bracket/housing component with an organic, asymmetrical shape featuring a prominent cutout on one side, a textured or mesh-patterned surface on the upper section, and a curved body designed to fit or mount around another part.
def model_115637_38d9f69a_0000():
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
        # Sketch has 19 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0845486651, perimeter: 9.6710044366
            with BuildLine():
                Line((0, -3.3000000492), (-0.5000000075, -3.3000000492))
                Line((0.5000000075, -3.3000000492), (0, -3.3000000492))
                _nurbs_edge([(0.0175013527, -0.400000006), (0.048630475, -0.4030925538), (0.1097791075, -0.4111608492), (0.1981732922, -0.4289129073), (0.3093468857, -0.4639275112), (0.436882899, -0.5268247827), (0.5523889083, -0.6090325337), (0.6549012511, -0.7105462386), (0.74296776, -0.8309804496), (0.8148742453, -0.9694964322), (0.8690507604, -1.1247808575), (0.9044396811, -1.2949815328), (0.9209027752, -1.4776346575), (0.9196537877, -1.6695640726), (0.9028529179, -1.8671842923), (0.8732206191, -2.0667899512), (0.8336642648, -2.2648491147), (0.7869386795, -2.4582721269), (0.7352575683, -2.6447479963), (0.68007599, -2.8229047303), (0.6222941557, -2.9920180761), (0.5743584601, -3.1198639407), (0.5375219694, -3.2115557292), (0.5125726081, -3.2708278957), (0.5000000075, -3.3000000492)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.4596821995, -0.5863101357), (-0.4587399543, -0.5792872434), (-0.4564978992, -0.5654524149), (-0.4520620652, -0.5453329549), (-0.4439938556, -0.5197784787), (-0.4303670798, -0.4900211831), (-0.413443985, -0.4626106663), (-0.3937725703, -0.4378043385), (-0.3723800917, -0.4160503512), (-0.3507320546, -0.3977349724), (-0.3304443755, -0.3823843154), (-0.3130514196, -0.3681849665), (-0.2997764175, -0.3509224165), (-0.291216282, -0.3245054594), (-0.2869348804, -0.284296353), (-0.2849308958, -0.2304111079), (-0.2814017416, -0.1699545714), (-0.2695856243, -0.1230034803), (-0.2452719944, -0.1020677295), (-0.2058003458, -0.1152161382), (-0.1498172411, -0.1666733845), (-0.0914068834, -0.2398854031), (-0.0399251772, -0.3129212499), (-0.0022069886, -0.3696363647), (0.0175013527, -0.400000006)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.8771835581, -1.4863101492), (-0.8838816445, -1.4906007874), (-0.8971742842, -1.4970337577), (-0.9168022698, -1.5002395491), (-0.9423497311, -1.4915219669), (-0.972797737, -1.4594619568), (-1.0005166228, -1.4085189309), (-1.0229121204, -1.3445127504), (-1.036426935, -1.2755584434), (-1.0373159158, -1.2096380685), (-1.0222801578, -1.1526831916), (-0.9892792696, -1.1061897324), (-0.9381406733, -1.0655079184), (-0.869873619, -1.0219961606), (-0.7862166671, -0.9646001629), (-0.6891800182, -0.8815708139), (-0.6023628978, -0.7860132032), (-0.5327171968, -0.6943377182), (-0.4843499896, -0.6238766929), (-0.4596821995, -0.5863101357)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.1000000015, -1.4000000209), (-0.1151325118, -1.3939331285), (-0.1451518704, -1.3828346765), (-0.1894439271, -1.3692929615), (-0.2470152841, -1.3574947361), (-0.3164204507, -1.3533242202), (-0.3831253132, -1.3597006898), (-0.4469380686, -1.3761642526), (-0.5076276736, -1.4015561655), (-0.5649427264, -1.4336698284), (-0.6186341087, -1.4689694618), (-0.6684579567, -1.5032169469), (-0.7141895292, -1.5319827933), (-0.755647811, -1.5512046421), (-0.7927274852, -1.5577153999), (-0.8254536722, -1.5499190063), (-0.8482254064, -1.5318364704), (-0.8634285827, -1.5116360234), (-0.8727364919, -1.4952402551), (-0.8771835581, -1.4863101492)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.5000000075, -3.3000000492), (-0.5202033702, -3.2829180194), (-0.5589668341, -3.248290381), (-0.6121822666, -3.1949582184), (-0.6732362368, -3.1210556308), (-0.7328588011, -3.0240819671), (-0.7756142316, -2.9228054603), (-0.8014886465, -2.8179158776), (-0.8107650859, -2.7106423238), (-0.8042098055, -2.60298207), (-0.783024578, -2.4973100471), (-0.7487704845, -2.3958798848), (-0.7033238965, -2.3003589313), (-0.648838825, -2.2113429134), (-0.5877268705, -2.1278417293), (-0.5224745829, -2.0477885663), (-0.4554603831, -1.9685615678), (-0.3887829759, -1.8874695667), (-0.3240670189, -1.8022834209), (-0.2623213122, -1.7116476374), (-0.2041086719, -1.6148176254), (-0.1605568288, -1.5321576179), (-0.1296124708, -1.4672188692), (-0.1097439764, -1.4226234593), (-0.1000000015, -1.4000000209)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a thin-walled, elongated diamond or parallelogram-shaped plate with a shallow depth, featuring a tapered geometry and clean planar surfaces with subtle edge details.
def model_115637_b6adbb54_0001():
    """Model: quarter 21 v2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.0000004768, perimeter: 16.0000001788
            with BuildLine():
                Line((4.0000000596, -4), (0, -4.0000000596))
                Line((4.0000000596, -4), (4.0000000596, 0))
                Line((0, 0), (4.0000000596, 0))
                Line((0, -4.0000000596), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a uniform thickness, featuring straight edges and a slanted geometric form.
def model_115698_acf503fb_0004():
    """Model: PCB"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.18), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((9.7179826537, -3.1287182655), (8.7179826537, -3.1287182655))
                Line((9.7179826537, -1.6287182655), (9.7179826537, -3.1287182655))
                Line((9.7179826537, -1.6287182655), (8.7179826537, -1.6287182655))
                Line((8.7179826537, -1.6287182655), (8.7179826537, -3.1287182655))
            make_face()
            # Profile area: 248.9512373391, perimeter: 65.5265411258
            with BuildLine():
                Line((-2.4320173463, 17.4845522974), (9.7179826537, 17.4845522974))
                Line((-2.4320173463, -3.1287182655), (-2.4320173463, 17.4845522974))
                Line((8.7179826537, -3.1287182655), (-2.4320173463, -3.1287182655))
                Line((8.7179826537, -1.6287182655), (8.7179826537, -3.1287182655))
                Line((9.7179826537, -1.6287182655), (8.7179826537, -1.6287182655))
                Line((9.7179826537, 17.4845522974), (9.7179826537, -1.6287182655))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or blade with a tapered form, featuring a slightly curved or beveled edge along one side and a uniform thickness throughout.
def model_115717_cf5498c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9929.4, perimeter: 430.4
            with BuildLine():
                Line((67, -148.2), (0, -148.2))
                Line((67, 0), (67, -148.2))
                Line((0, 0), (67, 0))
                Line((0, -148.2), (0, 0))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a boat hull or watercraft structure featuring a streamlined, tapered triangular profile with a flat base, internal ribbed framework for structural reinforcement, and a pointed bow that extends upward.
def model_116247_2d150add_0004():
    """Model: Base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.9069824666, perimeter: 18.6742761358
            with BuildLine():
                Line((2, 2), (2, -2))
                Line((1.1207055948, 1.4954827977), (2, 2))
                Line((0.0277464532, 1.3556949321), (1.1207055948, 1.4954827977))
                Line((-1.7931650634, 1.1228030292), (0.0277464532, 1.3556949321))
                Line((-2, 1.1228030292), (-1.7931650634, 1.1228030292))
                Line((-3, 1.1228030292), (-2, 1.1228030292))
                Line((-4, 1.1228030292), (-3, 1.1228030292))
                Line((-4, -1.3255356373), (-4, 1.1228030292))
                Line((-4, -1.3255356373), (-2, -1.3255356373))
                Line((-2, -1.3255356373), (0.0493990877, -1.6031822902))
                Line((0.0493990877, -1.6031822902), (1.3865457598, -1.7843350487))
                Line((1.3865457598, -1.7843350487), (2, -2))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a simple geometric form, featuring four straight edges and no holes, slots, or other features.
def model_116416_b2565d0a_0001():
    """Model: 3DP Bed Mid"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1600, perimeter: 160
            with BuildLine():
                Line((77.5, -40), (37.5, -40))
                Line((77.5, 0), (77.5, -40))
                Line((37.5, 0), (77.5, 0))
                Line((37.5, -40), (37.5, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical rod or shaft with a straight, tapered design and a smooth, uniform surface, featuring a slight conical taper from one end to the other.
def model_116416_b2565d0a_0005():
    """Model: 16mm Copper Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-10, -10)):
                Circle(0.8)
        # OneSide extrude, distance=60
        extrude(amount=60)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow tubular body featuring a hexagonal cross-section at the ends and internal ribbed or textured surfaces throughout.
def model_116416_b2565d0a_0008():
    """Model: 16mm Bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5340707511, perimeter: 10.6814150222
            with BuildLine():
                CenterArc((-15, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-15, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a polyhedron-shaped mechanical part with an irregular, faceted geometry featuring multiple angular faces, internal cavities, and cutout sections that appears designed for structural support or geometric fitting applications.
def model_116416_b2565d0a_0012():
    """Model: 5mm Nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1458205162, perimeter: 2.6745286036
            with BuildLine():
                Line((-16.5, -5.6443375673), (-16.5, -5.3556624327))
                Line((-16.5, -5.3556624327), (-16.75, -5.2113248654))
                Line((-16.75, -5.2113248654), (-17, -5.3556624327))
                Line((-17, -5.3556624327), (-17, -5.6443375673))
                Line((-17, -5.6443375673), (-16.75, -5.7886751346))
                Line((-16.75, -5.7886751346), (-16.5, -5.6443375673))
            make_face()
            with BuildLine():
                CenterArc((-16.75, -5.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical tube or pipe with a closed rounded end at the top and an open end at the bottom, featuring a smooth, uniform diameter throughout its length.
def model_116416_b2565d0a_0015():
    """Model: 3DP Bed Adjusting Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((20, 0)):
                Circle(0.35)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a dual-channel linear bearing block or rail guide featuring two parallel rectangular channels with internal grooves, mounting flanges on the sides, and precision slots designed for smooth linear motion along a shaft or rail system.
def model_116556_dfebf7ea_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 235 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0733462165, perimeter: 31.2580647934
            with BuildLine():
                Line((-1.4249999687, -0.5099999886), (-1.475, -0.5099999886))
                CenterArc((-1.475, -0.5349999886), 0.025, 90, 90)
                Line((-1.5, -0.5349999886), (-1.5, -1.25))
                CenterArc((-1.25, -1.25), 0.25, 180, 45)
                CenterArc((-1.25, -1.25), 0.25, -135, 45)
                Line((-0.5349999886, -1.5), (-1.25, -1.5))
                CenterArc((-0.5349999886, -1.475), 0.025, -90, 90)
                Line((-0.5099999886, -1.4249999687), (-0.5099999886, -1.475))
                CenterArc((-0.4849999886, -1.4249999687), 0.025, 90, 90)
                Line((-0.435, -1.4), (-0.4849999886, -1.3999999687))
                CenterArc((-0.435, -1.375), 0.025, -90, 90)
                Line((-0.41, -1.3250000182), (-0.41, -1.375))
                CenterArc((-0.435, -1.3250000182), 0.025, 0, 89.9999973255)
                Line((-0.8000000012, -1.3000000012), (-0.4349999988, -1.3000000182))
                CenterArc((-0.8, -1.2750000012), 0.025, 180, 89.9999973255)
                Line((-0.825, -1.2750000012), (-0.825, -0.9664213562))
                Line((-0.825, -0.9664213562), (-0.4385786438, -0.58))
                Line((-0.0774019823, -0.58), (-0.4385786438, -0.58))
                Line((-0.0774019823, -0.58), (0, -0.5399999879))
                Line((0.0774019823, -0.58), (0, -0.5399999879))
                Line((0.0774019823, -0.58), (0.4385786438, -0.58))
                Line((0.825, -0.9664213562), (0.4385786438, -0.58))
                Line((0.825, -1.2750000012), (0.825, -0.9664213562))
                CenterArc((0.8, -1.2750000012), 0.025, -89.9999973255, 89.9999973255)
                Line((0.8000000012, -1.3000000012), (0.4349999988, -1.3000000182))
                CenterArc((0.435, -1.3250000182), 0.025, 90.0000026745, 89.9999973255)
                Line((0.41, -1.3250000182), (0.41, -1.375))
                CenterArc((0.435, -1.375), 0.025, 180, 90)
                Line((0.435, -1.4), (0.4849999886, -1.3999999687))
                CenterArc((0.4849999886, -1.4249999687), 0.025, 0, 90)
                Line((0.5099999886, -1.4249999687), (0.5099999886, -1.475))
                CenterArc((0.5349999886, -1.475), 0.025, -180, 90)
                Line((0.5349999886, -1.5), (1.25, -1.5))
                CenterArc((1.25, -1.25), 0.25, -90, 45)
                CenterArc((1.25, -1.25), 0.25, -45, 45)
                Line((1.5, -0.5349999886), (1.5, -1.25))
                CenterArc((1.475, -0.5349999886), 0.025, 0, 90)
                Line((1.4249999687, -0.5099999886), (1.475, -0.5099999886))
                CenterArc((1.4249999687, -0.4849999886), 0.025, 180, 90)
                Line((1.4, -0.435), (1.3999999687, -0.4849999886))
                CenterArc((1.375, -0.435), 0.025, 0, 90)
                Line((1.3250000182, -0.41), (1.375, -0.41))
                CenterArc((1.3250000182, -0.435), 0.025, 90, 89.9999973255)
                Line((1.3000000012, -0.8000000012), (1.3000000182, -0.4349999988))
                CenterArc((1.2750000012, -0.8), 0.025, -90, 89.9999973255)
                Line((1.2750000012, -0.825), (0.9664213562, -0.825))
                Line((0.9664213562, -0.825), (0.58, -0.4385786438))
                Line((0.58, -0.0774019823), (0.58, -0.4385786438))
                Line((0.58, -0.0774019823), (0.5399999879, 0))
                Line((0.58, 0.0774019823), (0.5399999879, 0))
                Line((0.58, 0.0774019823), (0.58, 0.4385786438))
                Line((0.9664213562, 0.825), (0.58, 0.4385786438))
                Line((1.2750000012, 0.825), (0.9664213562, 0.825))
                CenterArc((1.2750000012, 0.8), 0.025, 0.0000026745, 89.9999973255)
                Line((1.3000000012, 0.8000000012), (1.3000000182, 0.4349999988))
                CenterArc((1.3250000182, 0.435), 0.025, -179.9999973255, 89.9999973255)
                Line((1.3250000182, 0.41), (1.375, 0.41))
                CenterArc((1.375, 0.435), 0.025, -90, 90)
                Line((1.4, 0.435), (1.3999999687, 0.4849999886))
                CenterArc((1.4249999687, 0.4849999886), 0.025, 90, 90)
                Line((1.4249999687, 0.5099999886), (1.475, 0.5099999886))
                CenterArc((1.475, 0.5349999886), 0.025, -90, 90)
                Line((1.5, 0.5349999886), (1.5, 1.25))
                CenterArc((1.25, 1.25), 0.25, 0, 45)
                CenterArc((1.25, 1.25), 0.25, 45, 45)
                Line((0.5349999886, 1.5), (1.25, 1.5))
                CenterArc((0.5349999886, 1.475), 0.025, 90, 90)
                Line((0.5099999886, 1.4249999687), (0.5099999886, 1.475))
                CenterArc((0.4849999886, 1.4249999687), 0.025, -90, 90)
                Line((0.435, 1.4), (0.4849999886, 1.3999999687))
                CenterArc((0.435, 1.375), 0.025, 90, 90)
                Line((0.41, 1.3250000182), (0.41, 1.375))
                CenterArc((0.435, 1.3250000182), 0.025, -180, 89.9999973255)
                Line((0.8000000012, 1.3000000012), (0.4349999988, 1.3000000182))
                CenterArc((0.8, 1.2750000012), 0.025, 0, 89.9999973255)
                Line((0.825, 1.2750000012), (0.825, 0.9664213562))
                Line((0.825, 0.9664213562), (0.4385786438, 0.58))
                Line((0.0774019823, 0.58), (0.4385786438, 0.58))
                Line((0.0774019823, 0.58), (0, 0.5399999879))
                Line((-0.0774019823, 0.58), (0, 0.5399999879))
                Line((-0.0774019823, 0.58), (-0.4385786438, 0.58))
                Line((-0.825, 0.9664213562), (-0.4385786438, 0.58))
                Line((-0.825, 1.2750000012), (-0.825, 0.9664213562))
                CenterArc((-0.8, 1.2750000012), 0.025, 90.0000026745, 89.9999973255)
                Line((-0.8000000012, 1.3000000012), (-0.4349999988, 1.3000000182))
                CenterArc((-0.435, 1.3250000182), 0.025, -89.9999973255, 89.9999973255)
                Line((-0.41, 1.3250000182), (-0.41, 1.375))
                CenterArc((-0.435, 1.375), 0.025, 0, 90)
                Line((-0.435, 1.4), (-0.4849999886, 1.3999999687))
                CenterArc((-0.4849999886, 1.4249999687), 0.025, 180, 90)
                Line((-0.5099999886, 1.4249999687), (-0.5099999886, 1.475))
                CenterArc((-0.5349999886, 1.475), 0.025, 0, 90)
                Line((-0.5349999886, 1.5), (-1.25, 1.5))
                CenterArc((-1.25, 1.25), 0.25, 90, 45)
                CenterArc((-1.25, 1.25), 0.25, 135, 45)
                Line((-1.5, 0.5349999886), (-1.5, 1.25))
                CenterArc((-1.475, 0.5349999886), 0.025, -180, 90)
                Line((-1.4249999687, 0.5099999886), (-1.475, 0.5099999886))
                CenterArc((-1.4249999687, 0.4849999886), 0.025, 0, 90)
                Line((-1.4, 0.435), (-1.3999999687, 0.4849999886))
                CenterArc((-1.375, 0.435), 0.025, 180, 90)
                Line((-1.3250000182, 0.41), (-1.375, 0.41))
                CenterArc((-1.3250000182, 0.435), 0.025, -90, 89.9999973255)
                Line((-1.3000000012, 0.8000000012), (-1.3000000182, 0.4349999988))
                CenterArc((-1.2750000012, 0.8), 0.025, 90, 89.9999973255)
                Line((-1.2750000012, 0.825), (-0.9664213562, 0.825))
                Line((-0.58, 0.4385786438), (-0.9664213562, 0.825))
                Line((-0.58, 0.0774019823), (-0.58, 0.4385786438))
                Line((-0.58, 0.0774019823), (-0.5399999879, 0))
                Line((-0.58, -0.0774019823), (-0.5399999879, 0))
                Line((-0.58, -0.0774019823), (-0.58, -0.4385786438))
                Line((-0.58, -0.4385786438), (-0.9664213562, -0.825))
                Line((-1.2750000012, -0.825), (-0.9664213562, -0.825))
                CenterArc((-1.2750000012, -0.8), 0.025, -179.9999973255, 89.9999973255)
                Line((-1.3000000012, -0.8000000012), (-1.3000000182, -0.4349999988))
                CenterArc((-1.3250000182, -0.435), 0.025, 0.0000026745, 89.9999973255)
                Line((-1.3250000182, -0.41), (-1.375, -0.41))
                CenterArc((-1.375, -0.435), 0.025, 90, 90)
                Line((-1.4, -0.435), (-1.3999999687, -0.4849999886))
                CenterArc((-1.4249999687, -0.4849999886), 0.025, -90, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.975, 1.275), (0.975, 1.075))
                CenterArc((1.075, 1.275), 0.1, 90, 90)
                Line((1.275, 1.375), (1.075, 1.375))
                CenterArc((1.275, 1.275), 0.1, 0, 90)
                Line((1.375, 1.075), (1.375, 1.275))
                CenterArc((1.275, 1.075), 0.1, -90, 90)
                Line((1.075, 0.975), (1.275, 0.975))
                CenterArc((1.075, 1.075), 0.1, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.975, 1.275), (-0.975, 1.075))
                CenterArc((-1.075, 1.075), 0.1, -90, 90)
                Line((-1.075, 0.975), (-1.275, 0.975))
                CenterArc((-1.275, 1.075), 0.1, 180, 90)
                Line((-1.375, 1.075), (-1.375, 1.275))
                CenterArc((-1.275, 1.275), 0.1, 90, 90)
                Line((-1.275, 1.375), (-1.075, 1.375))
                CenterArc((-1.075, 1.275), 0.1, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.075, -1.275), 0.1, -90, 90)
                Line((-1.275, -1.375), (-1.075, -1.375))
                CenterArc((-1.275, -1.275), 0.1, -180, 90)
                Line((-1.375, -1.075), (-1.375, -1.275))
                CenterArc((-1.275, -1.075), 0.1, 90, 90)
                Line((-1.075, -0.975), (-1.275, -0.975))
                CenterArc((-1.075, -1.075), 0.1, 0, 90)
                Line((-0.975, -1.275), (-0.975, -1.075))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.275, -1.375), (1.075, -1.375))
                CenterArc((1.075, -1.275), 0.1, 180, 90)
                Line((0.975, -1.275), (0.975, -1.075))
                CenterArc((1.075, -1.075), 0.1, 90, 90)
                Line((1.075, -0.975), (1.275, -0.975))
                CenterArc((1.275, -1.075), 0.1, 0, 90)
                Line((1.375, -1.075), (1.375, -1.275))
                CenterArc((1.275, -1.275), 0.1, -90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender tubular shape and rounded ends, featuring a uniform diameter throughout its length.
def model_116566_96702ebb_0001():
    """Model: Pin Long"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # Symmetric extrude, full_length=True, total=5.4
        extrude(amount=2.7, both=True)
    return part.part


# Description: This is a flat, rectangular parallelogram-shaped panel or plate with a dark blue finish, featuring two vertical slots or ribs running across its surface and slightly beveled or chamfered edges, appearing to be a mounting bracket or structural component.
def model_116566_96702ebb_0003():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.3573009183, perimeter: 30.5415926536
            with BuildLine():
                Line((-5, 0.6), (5, 0.6))
                Line((-5, -0.6), (-5, 0.6))
                Line((5, -0.6), (-5, -0.6))
                Line((5, 0.6), (5, -0.6))
            make_face()
            with BuildLine():
                CenterArc((4.5, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2, 0.25), (-4.5, 0.25))
                CenterArc((-2, 0), 0.25, -90, 180)
                Line((-4.5, -0.25), (-2, -0.25))
                CenterArc((-4.5, 0), 0.25, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=4.5
        extrude(amount=2.25, both=True)
    return part.part


# Description: This is a flat, organically-shaped plate or gasket with smooth, flowing curved edges and no holes or protrusions, resembling an abstract blob or amoeba form.
def model_116576_30739502_0000():
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
        # Sketch has 45 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.4324365999, perimeter: 96.2061208562
            with BuildLine():
                CenterArc((3.9501981941, 5.5593524614), 3.2, -48.7059858113, 143.615773282)
                CenterArc((3.9501981941, 5.5593524614), 3.2, 94.9097874707, 0.5198006565)
                CenterArc((3.9501981941, 5.5593524614), 3.2, 95.4295881272, 28.8006012483)
                _nurbs_edge([(2.1501371002, 8.205062207), (2.0958007709, 8.1770788964), (1.99044242, 8.1233792733), (1.8423454382, 8.0496244956), (1.6624794329, 7.963406773), (1.4551081978, 7.8691260411), (1.2521623484, 7.7839146301), (1.0434623635, 7.7082276832), (0.8272773516, 7.6559960724), (0.6132448144, 7.6506906332), (0.4035222332, 7.6756439648), (0.2399489268, 7.6988351435), (0.1192572274, 7.7052769025), (0.0396163719, 7.7028771895), (-0.0000000001, 7.700000116)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-2.1501371002, 8.205062207), (-2.0958007709, 8.1770788964), (-1.99044242, 8.1233792733), (-1.8423454382, 8.0496244956), (-1.6624794329, 7.9634067731), (-1.4551081976, 7.8691260411), (-1.2521623483, 7.7839146301), (-1.0434623634, 7.7082276832), (-0.8272773519, 7.6559960724), (-0.6132448151, 7.6506906335), (-0.4035222343, 7.6756439654), (-0.239948928, 7.6988351442), (-0.1192572282, 7.7052769029), (-0.0396163724, 7.7028771896), (-0.0000000001, 7.700000116)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-3.9501981941, 5.5593524614), 3.2, 55.7698106245, 172.9361751868)
                CenterArc((-6.3919139535, 2.7794200611), 0.5, -48.701872516, 97.4078583273)
                CenterArc((-3.9499562676, -0.0002998277), 3.2, 131.2991370308, 115.6225506009)
                _nurbs_edge([(-5.2043208025, -2.9442036328), (-5.1842361379, -2.9552910496), (-5.1430408409, -2.9767870485), (-5.0781700946, -3.0069945595), (-4.9855129983, -3.0431939703), (-4.8597694461, -3.0816841582), (-4.7251986576, -3.11356361), (-4.5840711765, -3.1391660698), (-4.4401593047, -3.1590673254), (-4.299341734, -3.1741878501), (-4.1681999615, -3.185566271), (-4.0522443397, -3.1940730296), (-3.954182589, -3.2001298216), (-3.8723459358, -3.2034585978), (-3.7985432587, -3.202728437), (-3.7213345917, -3.196163299), (-3.6296628488, -3.1822067791), (-3.5170725338, -3.1603080368), (-3.3830710987, -3.1311441497), (-3.2309963405, -3.0961554643), (-3.0668340638, -3.0572694458), (-2.8976249866, -3.0165398649), (-2.7301425987, -2.975848456), (-2.5692318452, -2.9365158265), (-2.417584722, -2.8993197383), (-2.2760472842, -2.8646683453), (-2.1437531563, -2.8327200001), (-2.018307844, -2.8035274889), (-1.8959745904, -2.7771626072), (-1.7717717167, -2.753870934), (-1.6403786017, -2.73399964), (-1.4971620198, -2.717889535), (-1.3391984633, -2.7057765811), (-1.1662237836, -2.6976952426), (-0.9818190731, -2.6933647591), (-0.7939199006, -2.6921278618), (-0.6125274304, -2.693110527), (-0.4478305453, -2.6953484944), (-0.3081926013, -2.6979250148), (-0.1981384344, -2.7001061498), (-0.1164463117, -2.7014719978), (-0.0663621764, -2.7019475418), (-0.0324469494, -2.7020690661), (-0.0106758986, -2.7020686707), (0, -2.7020481271)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(5.2043208025, -2.9442036328), (5.1842361379, -2.9552910496), (5.1430408409, -2.9767870485), (5.0781700946, -3.0069945595), (4.9855129983, -3.0431939703), (4.8597694461, -3.0816841582), (4.7251986576, -3.11356361), (4.5840711765, -3.1391660698), (4.4401593047, -3.1590673254), (4.299341734, -3.1741878501), (4.1681999615, -3.185566271), (4.0522443397, -3.1940730296), (3.954182589, -3.2001298216), (3.8723459358, -3.2034585978), (3.7985432587, -3.202728437), (3.7213345917, -3.196163299), (3.6296628488, -3.1822067791), (3.5170725338, -3.1603080368), (3.3830710987, -3.1311441497), (3.2309963405, -3.0961554643), (3.0668340638, -3.0572694458), (2.8976249866, -3.0165398649), (2.7301425987, -2.975848456), (2.5692318452, -2.9365158265), (2.417584722, -2.8993197383), (2.2760472842, -2.8646683453), (2.1437531563, -2.8327200001), (2.018307844, -2.8035274889), (1.8959745904, -2.7771626072), (1.7717717167, -2.753870934), (1.6403786017, -2.73399964), (1.4971620198, -2.717889535), (1.3391984633, -2.7057765811), (1.1662237836, -2.6976952426), (0.9818190731, -2.6933647591), (0.7939199006, -2.6921278618), (0.6125274304, -2.693110527), (0.4478305453, -2.6953484944), (0.3081926013, -2.6979250148), (0.1981384344, -2.7001061498), (0.1164463117, -2.7014719978), (0.0663621764, -2.7019475418), (0.0324469494, -2.7020690661), (0.0106758986, -2.7020686707), (0, -2.7020481271)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((3.9499562676, -0.0002998277), 3.2, -66.9216876317, 115.6225506009)
                CenterArc((6.3919139535, 2.7794200611), 0.5, 131.2940141887, 97.4078583273)
            make_face()
            with BuildLine():
                _nurbs_edge([(5.0730196951, -2.6740104585), (5.068458204, -2.6765285566), (5.0638967128, -2.6790466546), (5.0593352216, -2.6815647526), (4.9566601732, -2.7382448661), (4.8193659009, -2.7861906635), (4.6521353694, -2.8204236726), (4.468188849, -2.8580785365), (4.2473830349, -2.8787408532), (4.0820618663, -2.8909033955), (3.9892065792, -2.8977346825), (3.9159541865, -2.9020284005), (3.8640306632, -2.9025460117), (3.8117573396, -2.90306711), (3.7761234932, -2.9008025623), (3.707708981, -2.8899843284), (3.6224615472, -2.8765043422), (3.4888684649, -2.8477346567), (3.3277153102, -2.8103720134), (3.1430134955, -2.7675497179), (2.9286444546, -2.7154626829), (2.7345205889, -2.6680601462), (2.5397887685, -2.6205091549), (2.3662322128, -2.577294158), (2.2069191329, -2.5396703634), (2.0151531522, -2.4943824067), (1.834992384, -2.4550280256), (1.6102955077, -2.4293989257), (1.4483204708, -2.4109239274), (1.2620291087, -2.4001481394), (1.0630873991, -2.3956390077), (0.7980623139, -2.3896320571), (0.5199470358, -2.3940325546), (0.3361002374, -2.3973969547), (0.2202056221, -2.3995178285), (0.1431724299, -2.401088821), (0.0872498435, -2.4016687721), (0.0544609013, -2.4020088133), (0.0270179918, -2.4020995624), (0.0005772883, -2.4020486826), (0.0003848602, -2.4020483123), (0.0001924321, -2.402047942), (0.000000004, -2.4020475717)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [-0.0034066971, -0.0034066971, -0.0034066971, -0.0034066971, 0, 0, 0, 0.1020443352, 0.1020443352, 0.1020443352, 0.2142887933, 0.2142887933, 0.2142887933, 0.2773326943, 0.2773326943, 0.2773326943, 0.3408013117, 0.3408013117, 0.3408013117, 0.4198859471, 0.4198859471, 0.4198859471, 0.5105269011, 0.5105269011, 0.5105269011, 0.6014517232, 0.6014517232, 0.6014517232, 0.7108984032, 0.7108984032, 0.7108984032, 0.7897941598, 0.7897941598, 0.7897941598, 0.8948970799, 0.8948970799, 0.8948970799, 0.961152585, 0.961152585, 0.961152585, 1, 1, 1, 1.000270368, 1.000270368, 1.000270368, 1.000270368], 3)
                _nurbs_edge([(-5.0730196951, -2.6740104585), (-5.068458204, -2.6765285566), (-5.0638967128, -2.6790466546), (-5.0593352216, -2.6815647526), (-4.9566601732, -2.7382448661), (-4.8193659009, -2.7861906635), (-4.6521353694, -2.8204236726), (-4.468188849, -2.8580785365), (-4.2473830349, -2.8787408532), (-4.0820618663, -2.8909033955), (-3.9892065792, -2.8977346825), (-3.9159541865, -2.9020284005), (-3.8640306632, -2.9025460117), (-3.8117573396, -2.90306711), (-3.7761234932, -2.9008025623), (-3.707708981, -2.8899843284), (-3.6224615472, -2.8765043422), (-3.4888684649, -2.8477346567), (-3.3277153102, -2.8103720134), (-3.1430134955, -2.7675497179), (-2.9286444546, -2.7154626829), (-2.7345205889, -2.6680601462), (-2.5397887685, -2.6205091549), (-2.3662322128, -2.577294158), (-2.2069191328, -2.5396703634), (-2.0151531522, -2.4943824067), (-1.834992384, -2.4550280256), (-1.6102955077, -2.4293989257), (-1.4483204708, -2.4109239274), (-1.2620291087, -2.4001481394), (-1.0630873991, -2.3956390077), (-0.7980623139, -2.3896320571), (-0.5199470358, -2.3940325546), (-0.3361002374, -2.3973969547), (-0.2202056221, -2.3995178285), (-0.1431724299, -2.401088821), (-0.0872498435, -2.4016687721), (-0.0544609013, -2.4020088133), (-0.0270179918, -2.4020995624), (-0.0005772883, -2.4020486826), (-0.0003848575, -2.4020483123), (-0.0001924267, -2.402047942), (0.000000004, -2.4020475717)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [-0.0034066971, -0.0034066971, -0.0034066971, -0.0034066971, 0, 0, 0, 0.1020443352, 0.1020443352, 0.1020443352, 0.2142887933, 0.2142887933, 0.2142887933, 0.2773326943, 0.2773326943, 0.2773326943, 0.3408013117, 0.3408013117, 0.3408013117, 0.4198859471, 0.4198859471, 0.4198859471, 0.5105269011, 0.5105269011, 0.5105269011, 0.6014517232, 0.6014517232, 0.6014517232, 0.7108984032, 0.7108984032, 0.7108984032, 0.7897941598, 0.7897941598, 0.7897941598, 0.8948970799, 0.8948970799, 0.8948970799, 0.961152585, 0.961152585, 0.961152585, 1, 1, 1, 1.0002703718, 1.0002703718, 1.0002703718, 1.0002703718], 3)
                CenterArc((-3.9499562676, -0.0002998277), 2.9, 131.299105263, 115.9165770346)
                CenterArc((-6.3919139535, 2.7794200611), 0.8, -48.7013787777, 97.407364589)
                CenterArc((-3.9501981941, 5.5593524614), 2.9, 55.4171066385, 173.2888791728)
                _nurbs_edge([(-2.3041641152, 7.9469394883), (-2.298606921, 7.944077523), (-2.2930497269, 7.9412155576), (-2.2874925327, 7.9383535923), (-2.0395233484, 7.8106490013), (-1.8355788715, 7.7120437348), (-1.6417914356, 7.6254335279), (-1.502178733, 7.5630358549), (-1.3661176521, 7.5049848614), (-1.2136857052, 7.4539016164), (-1.0903935547, 7.412583748), (-0.9524633848, 7.3769277084), (-0.8113896128, 7.3636736031), (-0.6410328059, 7.3476683102), (-0.479336614, 7.3654525803), (-0.3474566212, 7.3813683727), (-0.2238207742, 7.3962892294), (-0.1269920493, 7.4064864911), (-0.0392290812, 7.4018820945), (-0.0333769701, 7.4015750693), (-0.0275479433, 7.4012106577), (-0.0217297768, 7.400788123), (-0.0144865181, 7.4002620933), (-0.0072432594, 7.3997360636), (-0.0000000007, 7.3992100339)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [-0.0061364405, -0.0061364405, -0.0061364405, -0.0061364405, 0, 0, 0, 0.2695047028, 0.2695047028, 0.2695047028, 0.4636673416, 0.4636673416, 0.4636673416, 0.620712697, 0.620712697, 0.620712697, 0.8103563485, 0.8103563485, 0.8103563485, 0.9881449043, 0.9881449043, 0.9881449043, 1, 1, 1, 1.0109700989, 1.0109700989, 1.0109700989, 1.0109700989], 3)
                _nurbs_edge([(2.3041641152, 7.9469394883), (2.298606921, 7.944077523), (2.2930497269, 7.9412155576), (2.2874925327, 7.9383535923), (2.0395233482, 7.8106490012), (1.8355788712, 7.7120437346), (1.6417914352, 7.6254335277), (1.5021787325, 7.5630358546), (1.3661176513, 7.504984861), (1.2136857041, 7.453901616), (1.0903935532, 7.4125837475), (0.9524633826, 7.3769277079), (0.8113896101, 7.3636736028), (0.6410328036, 7.3476683101), (0.4793366121, 7.3654525799), (0.3474566193, 7.3813683722), (0.2238207722, 7.3962892288), (0.126992047, 7.4064864906), (0.0392290793, 7.4018820943), (0.0333769684, 7.4015750692), (0.0275479418, 7.4012106576), (0.0217297755, 7.4007881229), (0.0144865167, 7.4002620932), (0.007243258, 7.3997360635), (-0.0000000007, 7.3992100339)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [-0.0061364405, -0.0061364405, -0.0061364405, -0.0061364405, 0, 0, 0, 0.2695047031, 0.2695047031, 0.2695047031, 0.4636673421, 0.4636673421, 0.4636673421, 0.6207126979, 0.6207126979, 0.6207126979, 0.810356349, 0.810356349, 0.810356349, 0.9881449047, 0.9881449047, 0.9881449047, 1, 1, 1, 1.010970099, 1.010970099, 1.010970099, 1.010970099], 3)
                CenterArc((3.9501981941, 5.5593524614), 2.9, -48.7059858113, 173.2888791728)
                CenterArc((6.3919139535, 2.7794200611), 0.8, 131.2940141887, 97.4066056528)
                CenterArc((3.9499562676, -0.0002998277), 2.9, -67.2156822976, 115.9167863963)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a stepped prismatic bracket or connector block featuring a rectangular base with a progressively offset upper section, characterized by multiple flat faces, sharp edges, and internal geometric complexity suggesting reinforcing ribs or internal structure.
def model_116581_d405b783_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9064486407, perimeter: 12.4998076489
            with BuildLine():
                Line((1.1596870557, -0.8151904685), (1.1596870557, -4.3046248764))
                Line((1.1596870557, -4.3046248764), (3, -4.3046248764))
                Line((3, -4.3046248764), (3, -3.2652188826))
                Line((3, -3.2652188826), (3, -2.5599076724))
                Line((3, -2.5599076724), (2.0798435278, -2.5599076724))
                Line((2.0798435278, -2.5599076724), (2.0798435278, -2))
                Line((2.0798435278, -2), (3, -2))
                Line((3, -2), (3, -1))
                Line((3, -0.8151904685), (3, -1))
                Line((1.1596870557, -0.8151904685), (3, -0.8151904685))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical filter or strainer component with a hollow tubular body featuring a perforated or mesh surface pattern on its curved walls, likely designed to allow fluid or air passage while filtering out larger particles.
def model_116646_96f3ebb8_0001():
    """Model: pistone"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -7.5)):
                Circle(1)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a elongated mounting bracket or strap with a dark gray finish, featuring two oval mounting holes at each end and a slightly curved, channel-like body for structural support or cable management.
def model_116656_fdc76689_0005():
    """Model: Untitled v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5549778714, perimeter: 9.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.25, 180, 180)
                Line((0.25, 0), (0.25, 3))
                CenterArc((0, 3), 0.25, 0, 180)
                Line((-0.25, 0), (-0.25, 3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 3), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is an L-shaped steel angle bracket or corner brace with two perpendicular flanges, each featuring four evenly-spaced holes for fastening and structural support.
def model_116762_7f2aee8d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 46.8400934463, perimeter: 55.5624885624
            with BuildLine():
                Line((7.5681477897, 3.6), (7.5681477897, 0))
                Line((3.6, 3.6), (7.5681477897, 3.6))
                Line((3.6, 10.16), (3.6, 3.6))
                Line((0, 10.16), (3.6, 10.16))
                Line((0, 0), (0, 10.16))
                Line((7.5681477897, 0), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((2.4, 6.66), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2, 6.66), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2, 9.16), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4, 9.16), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 1.2), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 2.4), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 1.2), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 2.4), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a metal C-shaped channel or U-channel bracket with a hollow rectangular cross-section, featuring two parallel horizontal flanges connected by a vertical web, commonly used for structural support or mounting applications.
def model_116842_501e9f74_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.5227433388, perimeter: 25.5415926536
            with BuildLine():
                Line((2.3, 3), (6.9, 3))
                CenterArc((6.9, 3.1), 0.1, -90, 90)
                Line((7, 3.1), (7, 3.5))
                CenterArc((6.9, 3.5), 0.1, 0, 90)
                Line((6.9, 3.6), (1.5, 3.6))
                CenterArc((1.5, 3.1), 0.5, 90, 90)
                Line((1, 3.1), (1, 0.9))
                CenterArc((1.5, 0.9), 0.5, 180, 90)
                Line((1.5, 0.4), (5.9, 0.4))
                CenterArc((5.9, 0.5), 0.1, -90, 90)
                Line((6, 0.5), (6, 0.9))
                CenterArc((5.9, 0.9), 0.1, 0, 90)
                Line((5.9, 1), (2.3, 1))
                CenterArc((2.3, 1.3), 0.3, 180, 90)
                Line((2, 1.3), (2, 2.7))
                CenterArc((2.3, 2.7), 0.3, 90, 90)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a dark blue-gray finish and a slight 3D perspective, featuring clean straight edges and no holes or additional features.
def model_117211_d14ca1c3_0003():
    """Model: drawer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 326.61225, perimeter: 80.01
            with BuildLine():
                Line((-29.5275, -1.27), (-0.9525, -1.27))
                Line((-29.5275, -1.27), (-29.5275, -12.7))
                Line((-0.9525, -12.7), (-29.5275, -12.7))
                Line((-0.9525, -12.7), (-0.9525, -1.27))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a curved elbow or connector fitting with a rounded, tubular body that bends at approximately 90 degrees, featuring textured grip surfaces on the outer edges and what appears to be internal reinforcement or mesh detailing visible through cut-away sections.
def model_117227_c7eb2b91_0003():
    """Model: Pata_Drch v1 (1)"""
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
        # Hoppeltier_Känguru -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 13.4694742271, perimeter: 20.3001450734
            with BuildLine():
                _nurbs_edge([(4.4024506631, 4.2085309491), (3.8143140409, 4.6439807236), (3.0608394766, 5.4417296389), (2.5893011157, 5.771301998), (2.1177627549, 6.1008743571), (1.1884377828, 6.5434349972), (0.4763830397, 5.4811931911), (-0.2356717033, 4.418951385), (0.7098706679, 3.6642305703), (1.0792620937, 3.4964766875), (1.4486535195, 3.3287228046), (2.9305024098, 3.1698400916), (3.5203670656, 3.1815582663), (4.1102317213, 3.193276441), (4.189221743, 2.6179769649), (4.0011579517, 2.3576973479), (3.8130941604, 2.097417731), (3.4031336367, 1.3963696522), (3.3559683407, 1.2353646059), (3.3088030447, 1.0743595596), (3.5206972206, 0.5013223754), (3.9772383274, 0.7078785375), (4.4337794341, 0.9144346996), (5.1111878061, 1.6468754296), (5.360982073, 2.0008882458), (5.6107763399, 2.354901062), (6.1516610287, 3.0252426793), (5.9786808645, 3.2846327491), (5.6498838961, 3.7776758039), (4.9184979928, 3.8264552801), (4.4024506631, 4.2085309491)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(3.9502946617, 3.8112369076), (3.9002287257, 3.7452345057), (3.913147784, 3.6511425269), (3.9791501859, 3.6010765909), (4.0451525878, 3.551010655), (4.1392445666, 3.5639297132), (4.1893105026, 3.6299321152), (4.2393764385, 3.6959345171), (4.2264573803, 3.7900264959), (4.1604549783, 3.8400924318), (4.0944525764, 3.8901583678), (4.0003605976, 3.8772393095), (3.9502946617, 3.8112369076)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(1.51346027, 4.9100445112), (1.463394334, 4.8440421092), (1.4763133923, 4.7499501305), (1.5423157942, 4.6998841945), (1.6083181962, 4.6498182586), (1.7024101749, 4.6627373168), (1.7524761109, 4.7287397187), (1.8025420469, 4.7947421207), (1.7896229886, 4.8888340994), (1.7236205867, 4.9389000354), (1.6576181847, 4.9889659714), (1.563526206, 4.9760469131), (1.51346027, 4.9100445112)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is an elliptical or oval-shaped structural panel or cover featuring a reinforced rim with radial internal ribbing or support structure, designed with a shallow curved surface and flanged edges for assembly or mounting.
def model_117540_ba397889_0000():
    """Model: sea_7_2 v1"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 113097335.5292325467, perimeter: 37699.1118430775
            Circle(6000)
        # OneSide extrude, distance=-800
        extrude(amount=-800)
    return part.part


# Description: This is a chain link or connector bar with a horizontal rectangular bar body and three circular holes (eyes) at each end and middle for attaching pins or fasteners.
def model_117693_ebadc189_0003():
    """Model: Link Arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.5654247369, perimeter: 26.2509974233
            with BuildLine():
                CenterArc((0, 0), 0.44, 30.754703633, 118.4905927339)
                Line((-4.1616796488, 0.225), (-0.3781203512, 0.225))
                CenterArc((-4.5398, 0), 0.44, 30.754703633, 298.4905927339)
                Line((-4.1616796488, -0.225), (-0.3781203512, -0.225))
                CenterArc((0, 0), 0.44, -149.245296367, 118.4905927339)
                Line((0.3781203512, -0.225), (4.1616796488, -0.225))
                CenterArc((4.5398, 0), 0.44, -149.245296367, 298.4905927339)
                Line((0.3781203512, 0.225), (4.1616796488, 0.225))
            make_face()
            with BuildLine():
                CenterArc((4.5398, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.5398, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is an L-shaped bracket or mounting arm featuring a vertical flange with multiple mounting holes and a horizontal extension, with cutouts and slots for fastening and assembly purposes.
def model_118105_8adbe5cd_0005():
    """Model: Left Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 43 constraints, 25 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 434.7631803505, perimeter: 176.8878523586
            with BuildLine():
                Line((-41.0086028878, 7.3), (-45.3189884587, 15.6244402781))
                CenterArc((-47.9830351022, 14.245), 3, 27.3750688823, 125.2498622354)
                Line((-52.0086028878, 12.995), (-50.6470817458, 15.6244402781))
                Line((-52.0086028878, 11.995), (-52.0086028878, 12.995))
                Line((-50.5943893254, 11.995), (-52.0086028878, 11.995))
                Line((-52.0086028878, 10.5807864376), (-50.5943893254, 11.995))
                Line((-52.0086028878, 10.5807864376), (-52.0086028878, -1.6857864376))
                Line((-50.5943893254, -3.1), (-52.0086028878, -1.6857864376))
                Line((-50.5943893254, -3.1), (-41.0086028878, -3.1))
                Line((-41.0086028878, -3.1), (-41.0086028878, 0))
                Line((0, 0), (-41.0086028878, 0))
                CenterArc((-4.5086028878, 3.15), 5.5, -34.9406265836, 69.8812531672)
                Line((-41.0086028878, 6.3), (0, 6.3))
                Line((-41.0086028878, 7.3), (-41.0086028878, 6.3))
            make_face()
            with BuildLine():
                Line((-47.0086028878, -0.85), (-49.0086028878, -0.85))
                CenterArc((-47.0086028878, -1.6), 0.75, -90, 180)
                Line((-49.0086028878, -2.35), (-47.0086028878, -2.35))
                CenterArc((-49.0086028878, -1.6), 0.75, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-47.0086028878, 9.15), (-49.0086028878, 9.15))
                CenterArc((-47.0086028878, 8.4), 0.75, -90, 180)
                Line((-49.0086028878, 7.65), (-47.0086028878, 7.65))
                CenterArc((-49.0086028878, 8.4), 0.75, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-27.0086028878, 3.15), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-34.0086028878, 3.15), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.0086028878, 3.15), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-47.9430005027, 14.245), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.203125
        extrude(amount=0.203125)
    return part.part


# Description: This is a flat, elongated mounting bracket or spacer with rounded ends, featuring two circular mounting holes at each end for fastening purposes.
def model_118116_bcc4d1ef_0001():
    """Model: link"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.5340707511, perimeter: 11.6548667765
            with BuildLine():
                CenterArc((-1.5, 0), 0.5, 90, 180)
                Line((-1.5, -0.5), (1.5, -0.5))
                CenterArc((1.5, 0), 0.5, -90, 180)
                Line((1.5, 0.5), (-1.5, 0.5))
            make_face()
            with BuildLine():
                CenterArc((-1.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.2
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a roller chain link consisting of three circular pins connected by two parallel flat side plates, forming an open rectangular frame with the characteristic segmented structure of a drive chain.
def model_118124_46a97d36_0003():
    """Model: link arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1114398863, perimeter: 1.6737515905
            with BuildLine():
                CenterArc((0, 0), 0.25, -115.8419327632, 51.6838655263)
                Line((-0.3781203512, -0.225), (-0.1089724736, -0.225))
                CenterArc((0, 0), 0.44, -149.245296367, 118.4905927339)
                Line((0.1089724736, -0.225), (0.3781203512, -0.225))
            make_face()
            # Profile area: 0.0944915122, perimeter: 1.570538851
            with BuildLine():
                CenterArc((0, 0), 0.25, 115.8419327632, 128.3161344737)
                Line((-0.3781203512, 0.225), (-0.1089724736, 0.225))
                CenterArc((0, 0), 0.44, 149.245296367, 61.5094072661)
                Line((-0.3781203512, -0.225), (-0.1089724736, -0.225))
            make_face()
            # Profile area: 0.0944915122, perimeter: 1.570538851
            with BuildLine():
                Line((0.1089724736, -0.225), (0.3781203512, -0.225))
                CenterArc((0, 0), 0.44, -30.754703633, 61.5094072661)
                Line((0.1089724736, 0.225), (0.3781203512, 0.225))
                CenterArc((0, 0), 0.25, -64.1580672368, 128.3161344737)
            make_face()
            # Profile area: 1.6649181731, perimeter: 8.5118352716
            with BuildLine():
                Line((0.3781203512, -0.225), (4.1616796488, -0.225))
                CenterArc((4.5398, 0), 0.44, 149.245296367, 61.5094072661)
                Line((0.3781203512, 0.225), (4.1616796488, 0.225))
                CenterArc((0, 0), 0.44, -30.754703633, 61.5094072661)
            make_face()
            # Profile area: 0.4118627969, perimeter: 4.335397862
            with BuildLine():
                CenterArc((4.5398, 0), 0.44, 149.245296367, 61.5094072661)
                CenterArc((4.5398, 0), 0.44, -149.245296367, 298.4905927339)
            make_face()
            with BuildLine():
                CenterArc((4.5398, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4118627969, perimeter: 4.335397862
            with BuildLine():
                CenterArc((-4.5398, 0), 0.44, -30.754703633, 61.5094072661)
                CenterArc((-4.5398, 0), 0.44, 30.754703633, 298.4905927339)
            make_face()
            with BuildLine():
                CenterArc((-4.5398, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6649181731, perimeter: 8.5118352716
            with BuildLine():
                CenterArc((0, 0), 0.44, 149.245296367, 61.5094072661)
                Line((-4.1616796488, 0.225), (-0.3781203512, 0.225))
                CenterArc((-4.5398, 0), 0.44, -30.754703633, 61.5094072661)
                Line((-4.1616796488, -0.225), (-0.3781203512, -0.225))
            make_face()
            # Profile area: 0.1114398863, perimeter: 1.6737515905
            with BuildLine():
                Line((0.1089724736, 0.225), (0.3781203512, 0.225))
                CenterArc((0, 0), 0.44, 30.754703633, 118.4905927339)
                Line((-0.3781203512, 0.225), (-0.1089724736, 0.225))
                CenterArc((0, 0), 0.25, 64.1580672368, 51.6838655263)
            make_face()
        # Symmetric extrude, full_length=True, total=0.2
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a precision cutting tool or utility knife blade holder featuring an elongated flat body with two rectangular slots along its length, a mounting hole at the upper end, and a sharp pointed tip at the lower end for cutting or scraping applications.
def model_118127_40704f5d_0001():
    """Model: arm v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 34 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2375775219, perimeter: 2.1315512641
            with BuildLine():
                Line((9.8425003445, -0.9525), (9.5250003242, -0.9525))
                CenterArc((10.1600003242, -0.9525), 0.3174999797, 89.9778784644, 90.0221215356)
                Line((10.1602454937, -0.3175000473), (10.160122909, -0.6350000439))
                CenterArc((10.1600003242, -0.9525), 0.635, 89.9778784644, 90.0221215356)
            make_face()
            # Profile area: 0.23746076, perimeter: 2.1308157558
            with BuildLine():
                CenterArc((10.1600003242, -0.9525), 0.635, -180, 89.9778784644)
                Line((10.1598777395, -1.2699999561), (10.1597551548, -1.5874999527))
                CenterArc((10.1600003242, -0.9525), 0.3174999797, 180, 89.9778784644)
                Line((9.8425003445, -0.9525), (9.5250003242, -0.9525))
            make_face()
            # Profile area: 3.225416046, perimeter: 19.248890368
            with BuildLine():
                Line((6.9850003242, -1.2700000167), (9.2075003266, -1.27))
                Line((6.0325002096, -1.2700000238), (6.9850003242, -1.2700000167))
                Line((3.8100001216, -1.2700000405), (6.0325002096, -1.2700000238))
                CenterArc((3.8100002027, -0.9525), 0.3175, 180, 89.9999853716)
                Line((3.4925002027, -0.9525), (2.8575001216, -0.9525))
                Line((2.8575001216, -0.9525), (2.3546431071, -0.9525))
                CenterArc((0, 0), 2.5400000811, -38.5910420594, 16.566729962)
                CenterArc((0, 0), 2.5400000811, -60.2976680525, 21.7066259931)
                Line((1.2691329792, -2.2356436796), (1.2585548547, -2.2062728955))
                Line((1.2691329792, -2.2356436796), (2.4497873905, -1.810421482))
                CenterArc((3.7408101169, -5.3950219227), 3.81, 89.9778784644, 19.8290144335)
                Line((10.1597551548, -1.5874999527), (3.7422811336, -1.5850222067))
                CenterArc((10.1600003242, -0.9525), 0.635, -180, 89.9778784644)
                CenterArc((9.2075003242, -0.9525), 0.3175, -89.9999995698, 89.9999995698)
            make_face()
            # Profile area: 2.7170824298, perimeter: 16.8313195577
            with BuildLine():
                CenterArc((10.1600003242, -0.9525), 0.635, 89.9778784644, 90.0221215356)
                Line((10.1602454937, -0.3175000473), (2.5204480706, -0.31455037))
                CenterArc((0, 0), 2.5400000811, -22.0243120974, 14.9106135633)
                Line((2.8575001216, -0.9525), (2.3546431071, -0.9525))
                Line((3.4925002027, -0.9525), (2.8575001216, -0.9525))
                CenterArc((3.8100002027, -0.9525), 0.3175, 90.0000146284, 89.9999853716)
                Line((6.0325656973, -0.6350000203), (3.8100001216, -0.6350000203))
                Line((6.9850658189, -0.6350000203), (6.0325656973, -0.6350000203))
                Line((9.2073868842, -0.6350000203), (6.9850658189, -0.6350000203))
                CenterArc((9.2075003242, -0.9525), 0.3175, 0, 90.0204712933)
            make_face()
            # Profile area: 0.1440727207, perimeter: 2.2674558968
            with BuildLine():
                CenterArc((6.9850003242, -0.9525), 0.3175, 180, 90)
                Line((6.6675003242, -0.9525), (6.3500002027, -0.9525))
                CenterArc((6.0325002027, -0.9525), 0.3175, -89.9999987492, 89.9999987492)
                Line((6.0325002096, -1.2700000238), (6.9850003242, -1.2700000167))
            make_face()
            # Profile area: 0.4750382819, perimeter: 3.6273669794
            with BuildLine():
                CenterArc((10.1600003242, -0.9525), 0.635, -90.0221215356, 180)
                Line((10.1602454937, -0.3175000473), (10.160122909, -0.6350000439))
                CenterArc((10.1600003242, -0.9525), 0.3174999797, -90.0221215356, 180)
                Line((10.1598777395, -1.2699999561), (10.1597551548, -1.5874999527))
            make_face()
            # Profile area: 0.1440726821, perimeter: 2.2674559107
            with BuildLine():
                Line((6.9850658189, -0.6350000203), (6.0325656973, -0.6350000203))
                CenterArc((6.0325002027, -0.9525), 0.3175, 0, 89.988180893)
                Line((6.6675003242, -0.9525), (6.3500002027, -0.9525))
                CenterArc((6.9850003242, -0.9525), 0.3175, 89.9881808935, 90.0118191065)
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a curved, elongated metal plate or beam with a pronounced longitudinal bow, featuring multiple parallel horizontal slots or grooves running across its surface, and a flange-like edge along its bottom perimeter.
def model_118127_40704f5d_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6003923582, perimeter: 8.4083942765
            with BuildLine():
                Line((2.5368230941, -0.1270000041), (2.3778609214, -0.1270000041))
                CenterArc((0, 0), 2.38125, -80.5597479476, 77.5025224215)
                Line((0.0027921192, -2.4134773366), (0.3905702896, -2.3490011518))
                Line((-0.3793827452, -2.5115073451), (0.0027921192, -2.4134773366))
                Line((-0.3793827452, -2.5115073451), (0.3793827452, -2.5115073451))
                CenterArc((0, 0), 2.5400000811, -81.4099704415, 78.5439864589)
            make_face()
        # OneSide extrude, distance=13.97
        extrude(amount=13.97)
    return part.part


# Description: This is an electric motor assembly with a circular fan-cooled stator body featuring radial cooling fins, a central shaft opening, and mounting flanges on the side for mechanical attachment.
def model_118269_fa4b08d7_0001():
    """Model: Gear11 v1"""
    with BuildPart() as part:
        # Gear_13.995_14x20_250 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1065922376, perimeter: 6.1765994812
            with BuildLine():
                CenterArc((0, 0), 0.55, 3.9917427108, 197.9012646498)
                CenterArc((-0.6031231493, -0.2423684526), 0.1, -26.0952364742, 47.9882438348)
                Line((-0.5310647661, -0.3225907684), (-0.5133167344, -0.2863549033))
                Line((-0.532316821, -0.3254638948), (-0.5310647661, -0.3225907684))
                Line((-0.5337688553, -0.328000955), (-0.532316821, -0.3254638948))
                Line((-0.5353558597, -0.3303149615), (-0.5337688553, -0.328000955))
                Line((-0.5388128721, -0.3344739768), (-0.5353558597, -0.3303149615))
                Line((-0.5425418994, -0.3381880042), (-0.5388128721, -0.3344739768))
                Line((-0.546475918, -0.3415710204), (-0.5425418994, -0.3381880042))
                Line((-0.5505749192, -0.3446890215), (-0.546475918, -0.3415710204))
                Line((-0.559170926, -0.3502880262), (-0.5505749192, -0.3446890215))
                Line((-0.5682030282, -0.3551890819), (-0.559170926, -0.3502880262))
                Line((-0.576535046, -0.361210095), (-0.5682030282, -0.3551890819))
                Line((-0.5836079913, -0.3692260332), (-0.576535046, -0.361210095))
                Line((-0.5903599875, -0.3777210286), (-0.5836079913, -0.3692260332))
                Line((-0.5968149848, -0.386642025), (-0.5903599875, -0.3777210286))
                Line((-0.6029869827, -0.395954022), (-0.5968149848, -0.386642025))
                Line((-0.6088839809, -0.4056300193), (-0.6029869827, -0.395954022))
                Line((-0.6145119794, -0.415649017), (-0.6088839809, -0.4056300193))
                Line((-0.6198719781, -0.4259950147), (-0.6145119794, -0.415649017))
                Line((-0.6249659769, -0.4366520125), (-0.6198719781, -0.4259950147))
                Line((-0.6286119795, -0.4448410186), (-0.6249659769, -0.4366520125))
                Line((-0.5735669953, -0.5138649989), (-0.6286119795, -0.4448410186))
                Line((-0.564772, -0.5121329999), (-0.5735669953, -0.5138649989))
                Line((-0.553249, -0.5095379999), (-0.564772, -0.5121329999))
                Line((-0.54197, -0.5066139999), (-0.553249, -0.5095379999))
                Line((-0.530949, -0.5033569999), (-0.54197, -0.5066139999))
                Line((-0.520204, -0.4997609999), (-0.530949, -0.5033569999))
                Line((-0.509752, -0.4958159999), (-0.520204, -0.4997609999))
                Line((-0.499618, -0.4915079999), (-0.509752, -0.4958159999))
                Line((-0.489834, -0.4868149999), (-0.499618, -0.4915079999))
                Line((-0.4804439999, -0.4817029998), (-0.489834, -0.4868149999))
                Line((-0.472721, -0.4749199999), (-0.4804439999, -0.4817029998))
                Line((-0.4659320001, -0.467205), (-0.472721, -0.4749199999))
                Line((-0.4585620001, -0.46007), (-0.4659320001, -0.467205))
                Line((-0.454609, -0.456768), (-0.4585620001, -0.46007))
                Line((-0.450436, -0.453686), (-0.454609, -0.456768))
                Line((-0.445985, -0.450876), (-0.450436, -0.453686))
                Line((-0.441161, -0.448432), (-0.445985, -0.450876))
                Line((-0.438553, -0.447399), (-0.441161, -0.448432))
                Line((-0.435755, -0.446548), (-0.438553, -0.447399))
                Line((-0.432676, -0.445967), (-0.435755, -0.446548))
                Line((-0.42908, -0.445876), (-0.432676, -0.445967))
                Line((-0.42255, -0.448552), (-0.42908, -0.445876))
                Line((-0.34328, -0.511768), (-0.42255, -0.448552))
                Line((-0.339218, -0.517538), (-0.34328, -0.511768))
                Line((-0.338506, -0.521065), (-0.339218, -0.517538))
                Line((-0.338388, -0.524196), (-0.338506, -0.521065))
                Line((-0.338595, -0.527113), (-0.338388, -0.524196))
                Line((-0.339021, -0.529885), (-0.338595, -0.527113))
                Line((-0.340331, -0.535133), (-0.339021, -0.529885))
                Line((-0.34208, -0.540097), (-0.340331, -0.535133))
                Line((-0.344156, -0.544852), (-0.34208, -0.540097))
                Line((-0.346496, -0.54944), (-0.344156, -0.544852))
                Line((-0.351811, -0.558213), (-0.346496, -0.54944))
                Line((-0.357822, -0.566548), (-0.351811, -0.558213))
                Line((-0.362717, -0.575588), (-0.357822, -0.566548))
                Line((-0.365611, -0.585879), (-0.362717, -0.575588))
                Line((-0.368009, -0.596462), (-0.365611, -0.585879))
                Line((-0.369954, -0.607301), (-0.368009, -0.596462))
                Line((-0.371475, -0.618368), (-0.369954, -0.607301))
                Line((-0.37259, -0.629645), (-0.371475, -0.618368))
                Line((-0.373313, -0.641114), (-0.37259, -0.629645))
                Line((-0.373653, -0.65276), (-0.373313, -0.641114))
                Line((-0.373619, -0.664572), (-0.373653, -0.65276))
                Line((-0.373351, -0.673532), (-0.373619, -0.664572))
                Line((-0.293809, -0.711837), (-0.373351, -0.673532))
                Line((-0.286636, -0.706461), (-0.293809, -0.711837))
                Line((-0.27738, -0.699123), (-0.286636, -0.706461))
                Line((-0.268486, -0.691595), (-0.27738, -0.699123))
                Line((-0.25997, -0.683879), (-0.268486, -0.691595))
                Line((-0.251849, -0.675977), (-0.25997, -0.683879))
                Line((-0.244144, -0.667887), (-0.251849, -0.675977))
                Line((-0.236883, -0.659609), (-0.244144, -0.667887))
                Line((-0.230104, -0.651136), (-0.236883, -0.659609))
                Line((-0.223862, -0.642456), (-0.230104, -0.651136))
                Line((-0.219847, -0.632994), (-0.223862, -0.642456))
                Line((-0.217078, -0.623097), (-0.219847, -0.632994))
                Line((-0.213533, -0.613471), (-0.217078, -0.623097))
                Line((-0.211405, -0.608781), (-0.213533, -0.613471))
                Line((-0.208982, -0.604194), (-0.211405, -0.608781))
                Line((-0.206191, -0.599731), (-0.208982, -0.604194))
                Line((-0.202905, -0.595435), (-0.206191, -0.599731))
                Line((-0.201003, -0.593374), (-0.202905, -0.595435))
                Line((-0.198852, -0.591393), (-0.201003, -0.593374))
                Line((-0.19633, -0.589533), (-0.198852, -0.591393))
                Line((-0.193129, -0.587891), (-0.19633, -0.589533))
                Line((-0.186085, -0.587469), (-0.193129, -0.587891))
                Line((-0.087237, -0.610031), (-0.186085, -0.587469))
                Line((-0.081074, -0.613467), (-0.087237, -0.610031))
                Line((-0.078902, -0.616335), (-0.081074, -0.613467))
                Line((-0.077437, -0.619105), (-0.078902, -0.616335))
                Line((-0.076358, -0.621823), (-0.077437, -0.619105))
                Line((-0.075539, -0.624506), (-0.076358, -0.621823))
                Line((-0.074442, -0.629802), (-0.075539, -0.624506))
                Line((-0.073864, -0.635033), (-0.074442, -0.629802))
                Line((-0.073672, -0.640218), (-0.073864, -0.635033))
                Line((-0.073789, -0.645367), (-0.073672, -0.640218))
                Line((-0.074772, -0.655578), (-0.073789, -0.645367))
                Line((-0.076571, -0.665696), (-0.074772, -0.655578))
                Line((-0.077059, -0.675963), (-0.076571, -0.665696))
                Line((-0.075201, -0.686492), (-0.077059, -0.675963))
                Line((-0.07277, -0.697067), (-0.075201, -0.686492))
                Line((-0.06982, -0.707676), (-0.07277, -0.697067))
                Line((-0.066388, -0.718307), (-0.06982, -0.707676))
                Line((-0.0625, -0.728951), (-0.066388, -0.718307))
                Line((-0.058175, -0.739598), (-0.0625, -0.728951))
                Line((-0.053428, -0.750239), (-0.058175, -0.739598))
                Line((-0.048272, -0.760866), (-0.053428, -0.750239))
                Line((-0.044143, -0.768822), (-0.048272, -0.760866))
                Line((0.044142, -0.768822), (-0.044143, -0.768822))
                Line((0.048272, -0.760866), (0.044142, -0.768822))
                Line((0.053427, -0.750239), (0.048272, -0.760866))
                Line((0.058174, -0.739598), (0.053427, -0.750239))
                Line((0.062499, -0.728951), (0.058174, -0.739598))
                Line((0.066387, -0.718307), (0.062499, -0.728951))
                Line((0.069819, -0.707676), (0.066387, -0.718307))
                Line((0.072769, -0.697067), (0.069819, -0.707676))
                Line((0.0752, -0.686492), (0.072769, -0.697067))
                Line((0.077058, -0.675963), (0.0752, -0.686492))
                Line((0.07657, -0.665696), (0.077058, -0.675963))
                Line((0.074771, -0.655578), (0.07657, -0.665696))
                Line((0.073788, -0.645367), (0.074771, -0.655578))
                Line((0.073671, -0.640218), (0.073788, -0.645367))
                Line((0.073864, -0.635033), (0.073671, -0.640218))
                Line((0.074442, -0.629802), (0.073864, -0.635033))
                Line((0.075538, -0.624506), (0.074442, -0.629802))
                Line((0.076357, -0.621823), (0.075538, -0.624506))
                Line((0.077436, -0.619105), (0.076357, -0.621823))
                Line((0.078901, -0.616335), (0.077436, -0.619105))
                Line((0.081073, -0.613467), (0.078901, -0.616335))
                Line((0.087236, -0.610031), (0.081073, -0.613467))
                Line((0.186084, -0.587469), (0.087236, -0.610031))
                Line((0.193128, -0.587891), (0.186084, -0.587469))
                Line((0.19633, -0.589533), (0.193128, -0.587891))
                Line((0.198851, -0.591393), (0.19633, -0.589533))
                Line((0.201002, -0.593374), (0.198851, -0.591393))
                Line((0.202904, -0.595435), (0.201002, -0.593374))
                Line((0.20619, -0.599731), (0.202904, -0.595435))
                Line((0.208981, -0.604194), (0.20619, -0.599731))
                Line((0.211404, -0.608781), (0.208981, -0.604194))
                Line((0.213532, -0.613471), (0.211404, -0.608781))
                Line((0.217077, -0.623097), (0.213532, -0.613471))
                Line((0.219847, -0.632994), (0.217077, -0.623097))
                Line((0.223862, -0.642456), (0.219847, -0.632994))
                Line((0.230104, -0.651136), (0.223862, -0.642456))
                Line((0.236883, -0.659609), (0.230104, -0.651136))
                Line((0.244144, -0.667887), (0.236883, -0.659609))
                Line((0.251848, -0.675977), (0.244144, -0.667887))
                Line((0.25997, -0.683879), (0.251848, -0.675977))
                Line((0.268486, -0.691595), (0.25997, -0.683879))
                Line((0.277379, -0.699123), (0.268486, -0.691595))
                Line((0.286635, -0.706461), (0.277379, -0.699123))
                Line((0.293808, -0.711837), (0.286635, -0.706461))
                Line((0.37335, -0.673532), (0.293808, -0.711837))
                Line((0.373618, -0.664572), (0.37335, -0.673532))
                Line((0.373653, -0.65276), (0.373618, -0.664572))
                Line((0.373312, -0.641114), (0.373653, -0.65276))
                Line((0.372589, -0.629645), (0.373312, -0.641114))
                Line((0.371474, -0.618368), (0.372589, -0.629645))
                Line((0.369954, -0.607301), (0.371474, -0.618368))
                Line((0.368008, -0.596462), (0.369954, -0.607301))
                Line((0.365611, -0.585879), (0.368008, -0.596462))
                Line((0.362716, -0.575588), (0.365611, -0.585879))
                Line((0.357821, -0.566548), (0.362716, -0.575588))
                Line((0.351811, -0.558213), (0.357821, -0.566548))
                Line((0.346495, -0.54944), (0.351811, -0.558213))
                Line((0.344155, -0.544852), (0.346495, -0.54944))
                Line((0.342079, -0.540097), (0.344155, -0.544852))
                Line((0.34033, -0.535133), (0.342079, -0.540097))
                Line((0.33902, -0.529885), (0.34033, -0.535133))
                Line((0.338594, -0.527113), (0.33902, -0.529885))
                Line((0.338387, -0.524196), (0.338594, -0.527113))
                Line((0.338505, -0.521065), (0.338387, -0.524196))
                Line((0.339217, -0.517538), (0.338505, -0.521065))
                Line((0.343279, -0.511768), (0.339217, -0.517538))
                Line((0.42255, -0.448552), (0.343279, -0.511768))
                Line((0.429079, -0.445876), (0.42255, -0.448552))
                Line((0.432675, -0.445967), (0.429079, -0.445876))
                Line((0.435754, -0.446548), (0.432675, -0.445967))
                Line((0.438552, -0.447399), (0.435754, -0.446548))
                Line((0.44116, -0.448432), (0.438552, -0.447399))
                Line((0.445985, -0.450876), (0.44116, -0.448432))
                Line((0.450435, -0.453686), (0.445985, -0.450876))
                Line((0.454609, -0.456768), (0.450435, -0.453686))
                Line((0.458561, -0.46007), (0.454609, -0.456768))
                Line((0.465932, -0.467205), (0.458561, -0.46007))
                Line((0.47272, -0.47492), (0.465932, -0.467205))
                Line((0.480444, -0.481703), (0.47272, -0.47492))
                Line((0.489833, -0.486815), (0.480444, -0.481703))
                Line((0.499617, -0.491508), (0.489833, -0.486815))
                Line((0.509751, -0.495816), (0.499617, -0.491508))
                Line((0.520203, -0.499761), (0.509751, -0.495816))
                Line((0.530949, -0.503357), (0.520203, -0.499761))
                Line((0.541969, -0.506614), (0.530949, -0.503357))
                Line((0.553248, -0.509538), (0.541969, -0.506614))
                Line((0.564771, -0.512133), (0.553248, -0.509538))
                Line((0.573566, -0.513865), (0.564771, -0.512133))
                Line((0.628611, -0.444841), (0.573566, -0.513865))
                Line((0.624965, -0.436652), (0.628611, -0.444841))
                Line((0.619871, -0.425995), (0.624965, -0.436652))
                Line((0.614511, -0.415649), (0.619871, -0.425995))
                Line((0.608884, -0.40563), (0.614511, -0.415649))
                Line((0.602986, -0.395954), (0.608884, -0.40563))
                Line((0.596814, -0.386642), (0.602986, -0.395954))
                Line((0.590359, -0.377721), (0.596814, -0.386642))
                Line((0.583607, -0.369226), (0.590359, -0.377721))
                Line((0.576534, -0.36121), (0.583607, -0.369226))
                Line((0.568202, -0.355189), (0.576534, -0.36121))
                Line((0.55917, -0.350288), (0.568202, -0.355189))
                Line((0.550574, -0.344689), (0.55917, -0.350288))
                Line((0.546475, -0.341571), (0.550574, -0.344689))
                Line((0.542542, -0.338188), (0.546475, -0.341571))
                Line((0.538812, -0.334474), (0.542542, -0.338188))
                Line((0.535355, -0.330315), (0.538812, -0.334474))
                Line((0.533768, -0.328001), (0.535355, -0.330315))
                Line((0.532316, -0.325464), (0.533768, -0.328001))
                Line((0.531064, -0.322591), (0.532316, -0.325464))
                Line((0.530176, -0.319105), (0.531064, -0.322591))
                Line((0.531332, -0.312144), (0.530176, -0.319105))
                Line((0.575323, -0.220794), (0.531332, -0.312144))
                Line((0.580045, -0.21555), (0.575323, -0.220794))
                Line((0.583325, -0.214071), (0.580045, -0.21555))
                Line((0.586351, -0.213259), (0.583325, -0.214071))
                Line((0.589241, -0.212812), (0.586351, -0.213259))
                Line((0.592039, -0.212611), (0.589241, -0.212812))
                Line((0.597446, -0.21272), (0.592039, -0.212611))
                Line((0.602675, -0.21332), (0.597446, -0.21272))
                Line((0.607772, -0.214287), (0.602675, -0.21332))
                Line((0.612766, -0.215546), (0.607772, -0.214287))
                Line((0.622502, -0.218777), (0.612766, -0.215546))
                Line((0.631966, -0.222782), (0.622502, -0.218777))
                Line((0.641868, -0.225543), (0.631966, -0.222782))
                Line((0.652545, -0.226074), (0.641868, -0.225543))
                Line((0.663397, -0.226057), (0.652545, -0.226074))
                Line((0.674396, -0.225542), (0.663397, -0.226057))
                Line((0.685524, -0.224561), (0.674396, -0.225542))
                Line((0.696766, -0.223139), (0.685524, -0.224561))
                Line((0.708109, -0.221292), (0.696766, -0.223139))
                Line((0.719539, -0.219032), (0.708109, -0.221292))
                Line((0.731047, -0.21637), (0.719539, -0.219032))
                Line((0.739723, -0.214115), (0.731047, -0.21637))
                Line((0.759368, -0.128044), (0.739723, -0.214115))
                Line((0.75253, -0.122247), (0.759368, -0.128044))
                Line((0.743317, -0.114856), (0.75253, -0.122247))
                Line((0.733999, -0.10786), (0.743317, -0.114856))
                Line((0.724581, -0.101275), (0.733999, -0.10786))
                Line((0.71507, -0.095116), (0.724581, -0.101275))
                Line((0.705469, -0.089404), (0.71507, -0.095116))
                Line((0.695782, -0.084168), (0.705469, -0.089404))
                Line((0.686013, -0.079444), (0.695782, -0.084168))
                Line((0.676162, -0.07529), (0.686013, -0.079444))
                Line((0.666043, -0.073481), (0.676162, -0.07529))
                Line((0.655779, -0.072983), (0.666043, -0.073481))
                Line((0.645605, -0.071669), (0.655779, -0.072983))
                Line((0.640559, -0.070638), (0.645605, -0.071669))
                Line((0.635547, -0.069296), (0.640559, -0.070638))
                Line((0.630576, -0.067569), (0.635547, -0.069296))
                Line((0.625656, -0.065321), (0.630576, -0.067569))
                Line((0.623223, -0.063925), (0.625656, -0.065321))
                Line((0.620814, -0.062269), (0.623223, -0.063925))
                Line((0.618439, -0.060224), (0.620814, -0.062269))
                Line((0.5840252583, -0.0312560553), (0.618439, -0.060224))
                CenterArc((0.6484231604, 0.0452482597), 0.1, -176.0082572892, 45.91908821)
            make_face()
            with BuildLine():
                Line((-0.12489996, 0.1), (0.12489996, 0.1))
                CenterArc((0, 0), 0.16, 141.3178125465, 257.364374907)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


MODELS = {
    "model_100221_4d7b66c4_0003": {"func": model_100221_4d7b66c4_0003, "volume": 0.3385867195, "area": 47.8953652286},
    "model_100243_9fb796fe_0005": {"func": model_100243_9fb796fe_0005, "volume": 72.2, "area": 159.22},
    "model_100243_9fb796fe_0006": {"func": model_100243_9fb796fe_0006, "volume": 46.93, "area": 106.02},
    "model_100797_b7eaa569_0000": {"func": model_100797_b7eaa569_0000, "volume": 60.4865199206, "area": 134.0875661659},
    "model_100798_1efa7e4b_0000": {"func": model_100798_1efa7e4b_0000, "volume": 8.3200259482, "area": 32.7388107136},
    "model_100799_98b904e9_0000": {"func": model_100799_98b904e9_0000, "volume": 0.0000824648, "area": 0.0222263031},
    "model_100877_ac1e5a17_0001": {"func": model_100877_ac1e5a17_0001, "volume": 95.76190525, "area": 1222.174975},
    "model_100877_ac1e5a17_0017": {"func": model_100877_ac1e5a17_0017, "volume": 153.628725, "area": 995.96575},
    "model_101269_f084ba14_0023": {"func": model_101269_f084ba14_0023, "volume": 1036.99389375, "area": 1342.73925},
    "model_101427_a9bcb09c_0001": {"func": model_101427_a9bcb09c_0001, "volume": 3162.5, "area": 5060},
    "model_101427_a9bcb09c_0002": {"func": model_101427_a9bcb09c_0002, "volume": 53075, "area": 23710},
    "model_101817_b02acd9f_0000": {"func": model_101817_b02acd9f_0000, "volume": 145.2672, "area": 2424.8448},
    "model_101817_b02acd9f_0001": {"func": model_101817_b02acd9f_0001, "volume": 96.8448, "area": 1617.8048},
    "model_101817_b02acd9f_0002": {"func": model_101817_b02acd9f_0002, "volume": 221.4912, "area": 3695.4752},
    "model_101817_b02acd9f_0003": {"func": model_101817_b02acd9f_0003, "volume": 14272, "area": 14992},
    "model_101817_b02acd9f_0004": {"func": model_101817_b02acd9f_0004, "volume": 14400, "area": 15120},
    "model_102175_699d5e7c_0003": {"func": model_102175_699d5e7c_0003, "volume": 26.52, "area": 74.44},
    "model_102293_5d04e48d_0000": {"func": model_102293_5d04e48d_0000, "volume": 3.4937639266, "area": 49.4696190875},
    "model_102295_86f842dd_0000": {"func": model_102295_86f842dd_0000, "volume": 3.4966370614, "area": 22.2364594301},
    "model_102369_65e5a7e6_0001": {"func": model_102369_65e5a7e6_0001, "volume": 1.7680669892, "area": 16.9725838978},
    "model_102369_65e5a7e6_0002": {"func": model_102369_65e5a7e6_0002, "volume": 1.2970669892, "area": 12.8905838978},
    "model_102369_65e5a7e6_0003": {"func": model_102369_65e5a7e6_0003, "volume": 4.0995291289, "area": 33.3869187867},
    "model_102369_65e5a7e6_0004": {"func": model_102369_65e5a7e6_0004, "volume": 0.5680669892, "area": 6.5725838978},
    "model_102369_65e5a7e6_0005": {"func": model_102369_65e5a7e6_0005, "volume": 4.610837293, "area": 37.2171097767},
    "model_102369_65e5a7e6_0006": {"func": model_102369_65e5a7e6_0006, "volume": 1.6180669892, "area": 15.6725838978},
    "model_102410_f9877a7b_0000": {"func": model_102410_f9877a7b_0000, "volume": 0.6480516596, "area": 8.5333510453},
    "model_102410_f9877a7b_0003": {"func": model_102410_f9877a7b_0003, "volume": 7.0718342888, "area": 49.698669239},
    "model_102410_f9877a7b_0012": {"func": model_102410_f9877a7b_0012, "volume": 0.6762278187, "area": 8.8553642923},
    "model_102416_eba35f73_0005": {"func": model_102416_eba35f73_0005, "volume": 574.0365045915, "area": 1259.780972451},
    "model_102525_06a3094b_0000": {"func": model_102525_06a3094b_0000, "volume": 0.0296205, "area": 0.655},
    "model_102525_06a3094b_0004": {"func": model_102525_06a3094b_0004, "volume": 0.3825, "area": 4.385},
    "model_102525_06a3094b_0006": {"func": model_102525_06a3094b_0006, "volume": 0.7119, "area": 6.684},
    "model_102760_26430589_0037": {"func": model_102760_26430589_0037, "volume": 0.0080424772, "area": 0.2412743158},
    "model_103284_e25015aa_0004": {"func": model_103284_e25015aa_0004, "volume": 5.6861294523, "area": 18.4806351776},
    "model_103481_b27a1cdf_0010": {"func": model_103481_b27a1cdf_0010, "volume": 393.289536, "area": 361.2896},
    "model_103552_c3a389ed_0003": {"func": model_103552_c3a389ed_0003, "volume": 34.2204146769, "area": 141.299556223},
    "model_104283_e5646f96_0000": {"func": model_104283_e5646f96_0000, "volume": 36.8155389093, "area": 68.7223392973},
    "model_104283_e5646f96_0001": {"func": model_104283_e5646f96_0001, "volume": 5.5167600001, "area": 39.5177504754},
    "model_104453_aba0f2d1_0002": {"func": model_104453_aba0f2d1_0002, "volume": 5785.3981633974, "area": 2471.2388980385},
    "model_104453_aba0f2d1_0006": {"func": model_104453_aba0f2d1_0006, "volume": 35000.0000000001, "area": 15400},
    "model_104524_f829aab2_0001": {"func": model_104524_f829aab2_0001, "volume": 3.5342917353, "area": 12.9590696961},
    "model_105278_909f3813_0000": {"func": model_105278_909f3813_0000, "volume": 28.8, "area": 72},
    "model_105831_359a0be0_0000": {"func": model_105831_359a0be0_0000, "volume": 913.1052773198, "area": 3729.9227278385},
    "model_106323_77f22d29_0004": {"func": model_106323_77f22d29_0004, "volume": 4.7123889804, "area": 28.2743338823},
    "model_106817_bb28b7aa_0002": {"func": model_106817_bb28b7aa_0002, "volume": 0.5120224899, "area": 3.5930196641},
    "model_106817_bb28b7aa_0003": {"func": model_106817_bb28b7aa_0003, "volume": 0.8503154846, "area": 5.0042531977},
    "model_106817_bb28b7aa_0004": {"func": model_106817_bb28b7aa_0004, "volume": 0.1109364114, "area": 2.3037759562},
    "model_107055_0500fdd1_0009": {"func": model_107055_0500fdd1_0009, "volume": 157.5015527999, "area": 390.6131698079},
    "model_107055_0500fdd1_0027": {"func": model_107055_0500fdd1_0027, "volume": 0.0092514751, "area": 0.6381517157},
    "model_107075_beb19139_0000": {"func": model_107075_beb19139_0000, "volume": 940.7017624609, "area": 914.4965824139},
    "model_107250_aeb9e6d4_0000": {"func": model_107250_aeb9e6d4_0000, "volume": 98.9205870773, "area": 247.929850418},
    "model_107278_ff1ba47b_0000": {"func": model_107278_ff1ba47b_0000, "volume": 1.342838346, "area": 14.3347375544},
    "model_107467_a8afc51d_0000": {"func": model_107467_a8afc51d_0000, "volume": 0.3958406744, "area": 3.2044245067},
    "model_107467_a8afc51d_0002": {"func": model_107467_a8afc51d_0002, "volume": 0.7068583471, "area": 5.277875658},
    "model_107656_3b6f2b9c_0000": {"func": model_107656_3b6f2b9c_0000, "volume": 235.7177659961, "area": 413.6748301087},
    "model_107668_cf76b132_0001": {"func": model_107668_cf76b132_0001, "volume": 3748.3127348143, "area": 2053.4234982026},
    "model_108244_329b1876_0000": {"func": model_108244_329b1876_0000, "volume": 140404.3643519948, "area": 66561.1571999975},
    "model_108244_329b1876_0002": {"func": model_108244_329b1876_0002, "volume": 2183.8093376458, "area": 14285.2291168153},
    "model_108244_329b1876_0004": {"func": model_108244_329b1876_0004, "volume": 1091.9046688229, "area": 7151.5704694052},
    "model_108244_329b1876_0011": {"func": model_108244_329b1876_0011, "volume": 955.41658522, "area": 6259.8631384789},
    "model_108244_329b1876_0018": {"func": model_108244_329b1876_0018, "volume": 1057.7826479222, "area": 6928.6436366736},
    "model_108244_329b1876_0019": {"func": model_108244_329b1876_0019, "volume": 818.9285016172, "area": 5368.1558075527},
    "model_108412_8de2f9c3_0000": {"func": model_108412_8de2f9c3_0000, "volume": 37755.795456, "area": 60386.976},
    "model_108689_b235b790_0000": {"func": model_108689_b235b790_0000, "volume": 62.37326235, "area": 118.5157290767},
    "model_108850_0dcd5ef1_0002": {"func": model_108850_0dcd5ef1_0002, "volume": 41.47975575, "area": 157.25775},
    "model_108850_0dcd5ef1_0004": {"func": model_108850_0dcd5ef1_0004, "volume": 120.844355085, "area": 416.483038},
    "model_108851_4d515b10_0005": {"func": model_108851_4d515b10_0005, "volume": 74.47920588, "area": 200.32218},
    "model_108851_4d515b10_0006": {"func": model_108851_4d515b10_0006, "volume": 23.04430875, "area": 65.32245},
    "model_108851_4d515b10_0007": {"func": model_108851_4d515b10_0007, "volume": 270.386556, "area": 409.6766},
    "model_108851_4d515b10_0009": {"func": model_108851_4d515b10_0009, "volume": 231.18050538, "area": 344.612214},
    "model_108852_fed54702_0004": {"func": model_108852_fed54702_0004, "volume": 6.9127963701, "area": 35.8258022331},
    "model_108855_86bf65d0_0007": {"func": model_108855_86bf65d0_0007, "volume": 1081.546224, "area": 1174.1912},
    "model_108855_86bf65d0_0015": {"func": model_108855_86bf65d0_0015, "volume": 788.627455, "area": 1199.19115},
    "model_108855_86bf65d0_0016": {"func": model_108855_86bf65d0_0016, "volume": 1182.9411825, "area": 1784.67385},
    "model_108855_86bf65d0_0020": {"func": model_108855_86bf65d0_0020, "volume": 188.451236, "area": 240.274620657},
    "model_109096_01748cff_0001": {"func": model_109096_01748cff_0001, "volume": 589.0486225481, "area": 510.5088062083},
    "model_109096_01748cff_0002": {"func": model_109096_01748cff_0002, "volume": 196.3495408494, "area": 196.3495408494},
    "model_109225_9f3d5432_0000": {"func": model_109225_9f3d5432_0000, "volume": 1.5858379303, "area": 9.6457986372},
    "model_109232_04340d62_0003": {"func": model_109232_04340d62_0003, "volume": 54, "area": 90},
    "model_109307_a5919b9f_0000": {"func": model_109307_a5919b9f_0000, "volume": 144.4028503865, "area": 280.5600540271},
    "model_109382_30283521_0001": {"func": model_109382_30283521_0001, "volume": 104.6065257292, "area": 281.7249930951},
    "model_109862_ea256f3b_0000": {"func": model_109862_ea256f3b_0000, "volume": 61.7330247372, "area": 134.7290847592},
    "model_109863_7d9015ee_0001": {"func": model_109863_7d9015ee_0001, "volume": 0.2054585172, "area": 5.3647012795},
    "model_109863_7d9015ee_0002": {"func": model_109863_7d9015ee_0002, "volume": 0.111129092, "area": 2.9587322534},
    "model_109863_7d9015ee_0003": {"func": model_109863_7d9015ee_0003, "volume": 0.035060174, "area": 0.818070727},
    "model_109863_7d9015ee_0004": {"func": model_109863_7d9015ee_0004, "volume": 0.0425293105, "area": 0.9520596537},
    "model_109880_aebcec75_0001": {"func": model_109880_aebcec75_0001, "volume": 280.44, "area": 283.24},
    "model_110043_b73b8beb_0000": {"func": model_110043_b73b8beb_0000, "volume": 20.3575203953, "area": 42.9769875011},
    "model_110138_19df5c5e_0010": {"func": model_110138_19df5c5e_0010, "volume": 42529.3105479718, "area": 9520.5965367039},
    "model_110138_19df5c5e_0012": {"func": model_110138_19df5c5e_0012, "volume": 35060.1740140621, "area": 8180.7072699478},
    "model_110222_5055efca_0002": {"func": model_110222_5055efca_0002, "volume": 0.3926990817, "area": 3.5342917353},
    "model_110222_5055efca_0003": {"func": model_110222_5055efca_0003, "volume": 0.9424777961, "area": 5.3407075111},
    "model_110222_5055efca_0004": {"func": model_110222_5055efca_0004, "volume": 3.5570796327, "area": 27.0986722863},
    "model_110317_4eaf60f5_0000": {"func": model_110317_4eaf60f5_0000, "volume": 13.0523531572, "area": 93.069570973},
    "model_110344_a5d1ecce_0002": {"func": model_110344_a5d1ecce_0002, "volume": 2.0106192983, "area": 24.1274315796},
    "model_110697_4b2725f1_0000": {"func": model_110697_4b2725f1_0000, "volume": 28.2743338823, "area": 75.3982236862},
    "model_110871_4b62f82f_0006": {"func": model_110871_4b62f82f_0006, "volume": 1.53628725, "area": 12.9032},
    "model_110871_4b62f82f_0007": {"func": model_110871_4b62f82f_0007, "volume": 1.53628725, "area": 12.9032},
    "model_110956_df981ed9_0000": {"func": model_110956_df981ed9_0000, "volume": 28.5084430107, "area": 74.4984883411},
    "model_111151_7c7f89f6_0001": {"func": model_111151_7c7f89f6_0001, "volume": 62.5, "area": 112.5},
    "model_111225_c58b9e26_0000": {"func": model_111225_c58b9e26_0000, "volume": 45, "area": 118},
    "model_111387_c4243097_0000": {"func": model_111387_c4243097_0000, "volume": 0.0103926991, "area": 0.4706858347},
    "model_111411_47094743_0001": {"func": model_111411_47094743_0001, "volume": 85.8, "area": 379.9},
    "model_111411_47094743_0002": {"func": model_111411_47094743_0002, "volume": 93.6, "area": 411.6},
    "model_111411_47094743_0007": {"func": model_111411_47094743_0007, "volume": 408.4070449667, "area": 823.0972752405},
    "model_112017_a8394d4b_0000": {"func": model_112017_a8394d4b_0000, "volume": 347435.0147458026, "area": 145198.8832458499},
    "model_112095_1fbe1a75_0000": {"func": model_112095_1fbe1a75_0000, "volume": 66, "area": 166},
    "model_112375_114c01e5_0000": {"func": model_112375_114c01e5_0000, "volume": 0.2856580844, "area": 3.8955618518},
    "model_112724_2292d43f_0000": {"func": model_112724_2292d43f_0000, "volume": 0.40975, "area": 7.199},
    "model_112724_d334de09_0000": {"func": model_112724_d334de09_0000, "volume": 0.7025, "area": 10.965},
    "model_112928_03f271d6_0000": {"func": model_112928_03f271d6_0000, "volume": 0.6675884389, "area": 5.7334065928},
    "model_113001_c1b164a3_0010": {"func": model_113001_c1b164a3_0010, "volume": 0.1426722888, "area": 3.3273801599},
    "model_113175_b6232bdc_0000": {"func": model_113175_b6232bdc_0000, "volume": 10762.7545086094, "area": 6144.3387406849},
    "model_113343_e692c488_0002": {"func": model_113343_e692c488_0002, "volume": 64000, "area": 9600},
    "model_113356_bc60a46d_0001": {"func": model_113356_bc60a46d_0001, "volume": 1.1780972802, "area": 6.2831854242},
    "model_113364_10837c89_0001": {"func": model_113364_10837c89_0001, "volume": 22.5, "area": 111.5410196625},
    "model_113447_92e93a1b_0000": {"func": model_113447_92e93a1b_0000, "volume": 251.9220408163, "area": 1308.1420545956},
    "model_113447_92e93a1b_0001": {"func": model_113447_92e93a1b_0001, "volume": 26.9282478399, "area": 161.7605310855},
    "model_113447_92e93a1b_0003": {"func": model_113447_92e93a1b_0003, "volume": 25.3144830638, "area": 157.8569301875},
    "model_113545_54cc71a3_0002": {"func": model_113545_54cc71a3_0002, "volume": 0.3534070751, "area": 8.2336281799},
    "model_113554_8fdfcd6c_0000": {"func": model_113554_8fdfcd6c_0000, "volume": 2.0570686039, "area": 42.7491620659},
    "model_113698_dcf18f66_0020": {"func": model_113698_dcf18f66_0020, "volume": 0.0920486648, "area": 1.9038051481},
    "model_113844_4abc5651_0000": {"func": model_113844_4abc5651_0000, "volume": 6.0666772668, "area": 84.9415065577},
    "model_114345_228b4786_0004": {"func": model_114345_228b4786_0004, "volume": 0.1202725632, "area": 1.6344247479},
    "model_115093_424371f6_0001": {"func": model_115093_424371f6_0001, "volume": 90.128852, "area": 325.8058},
    "model_115406_3e093a37_0000": {"func": model_115406_3e093a37_0000, "volume": 0.1416229968, "area": 2.4278228027},
    "model_115406_f90aa3dd_0000": {"func": model_115406_f90aa3dd_0000, "volume": 2.8837026596, "area": 18.3228672105},
    "model_115421_1876edbd_0008": {"func": model_115421_1876edbd_0008, "volume": 0.0723822947, "area": 0.9650972632},
    "model_115421_1876edbd_0010": {"func": model_115421_1876edbd_0010, "volume": 0.977160979, "area": 8.5049196318},
    "model_115421_1876edbd_0011": {"func": model_115421_1876edbd_0011, "volume": 0.8979624925, "area": 14.2344082199},
    "model_115430_67c93e4d_0000": {"func": model_115430_67c93e4d_0000, "volume": 10.2441473217, "area": 59.3718543796},
    "model_115518_278ce3a6_0000": {"func": model_115518_278ce3a6_0000, "volume": 7.875, "area": 72.4571067812},
    "model_115527_ae156ba0_0000": {"func": model_115527_ae156ba0_0000, "volume": 96000, "area": 68140},
    "model_115533_04a1bec1_0000": {"func": model_115533_04a1bec1_0000, "volume": 24.8814138164, "area": 85.1999927654},
    "model_115533_96d86c9a_0000": {"func": model_115533_96d86c9a_0000, "volume": 44.1298141873, "area": 96.1605814518},
    "model_115535_a171c715_0000": {"func": model_115535_a171c715_0000, "volume": 7.6018004417, "area": 39.0125692675},
    "model_115535_be2c18b0_0000": {"func": model_115535_be2c18b0_0000, "volume": 0.6713149035, "area": 8.7114361071},
    "model_115637_38d9f69a_0000": {"func": model_115637_38d9f69a_0000, "volume": 4.0845472359, "area": 17.84008375},
    "model_115637_b6adbb54_0001": {"func": model_115637_b6adbb54_0001, "volume": 6.4000001907, "area": 38.400000906},
    "model_115698_acf503fb_0004": {"func": model_115698_acf503fb_0004, "volume": 40.0721979743, "area": 511.3867212584},
    "model_115717_cf5498c9_0000": {"func": model_115717_cf5498c9_0000, "volume": 34752.9, "area": 21365.2},
    "model_116247_2d150add_0004": {"func": model_116247_2d150add_0004, "volume": 13.5255859732, "area": 48.7533858417},
    "model_116416_b2565d0a_0001": {"func": model_116416_b2565d0a_0001, "volume": 800, "area": 3280},
    "model_116416_b2565d0a_0005": {"func": model_116416_b2565d0a_0005, "volume": 120.6371578978, "area": 305.6141333412},
    "model_116416_b2565d0a_0008": {"func": model_116416_b2565d0a_0008, "volume": 0.8011061267, "area": 17.0902640355},
    "model_116416_b2565d0a_0012": {"func": model_116416_b2565d0a_0012, "volume": 0.0437461549, "area": 1.0939996136},
    "model_116416_b2565d0a_0015": {"func": model_116416_b2565d0a_0015, "volume": 1.9242255003, "area": 11.7652644877},
    "model_116556_dfebf7ea_0000": {"func": model_116556_dfebf7ea_0000, "volume": 15.3667310827, "area": 162.4370163999},
    "model_116566_96702ebb_0001": {"func": model_116566_96702ebb_0001, "volume": 0.8588328917, "area": 7.9521564044},
    "model_116566_96702ebb_0003": {"func": model_116566_96702ebb_0003, "volume": 46.6078541324, "area": 158.1517687778},
    "model_116576_30739502_0000": {"func": model_116576_30739502_0000, "volume": 3.6079898883, "area": 52.9147919735},
    "model_116581_d405b783_0000": {"func": model_116581_d405b783_0000, "volume": 11.8128972815, "area": 36.8125125792},
    "model_116646_96f3ebb8_0001": {"func": model_116646_96f3ebb8_0001, "volume": 14.1371669412, "area": 34.5575191895},
    "model_116656_fdc76689_0005": {"func": model_116656_fdc76689_0005, "volume": 0.3109955743, "area": 5.0011061267},
    "model_116762_7f2aee8d_0000": {"func": model_116762_7f2aee8d_0000, "volume": 14.8717296692, "area": 111.3212770112},
    "model_116842_501e9f74_0000": {"func": model_116842_501e9f74_0000, "volume": 6.8181946711, "area": 37.4787608005},
    "model_117211_d14ca1c3_0003": {"func": model_117211_d14ca1c3_0003, "volume": 207.39877875, "area": 704.03085},
    "model_117227_c7eb2b91_0003": {"func": model_117227_c7eb2b91_0003, "volume": 13.4690826721, "area": 47.2383093657},
    "model_117540_ba397889_0000": {"func": model_117540_ba397889_0000, "volume": 90477868423.3860473633, "area": 256353960.5329270959},
    "model_117693_ebadc189_0003": {"func": model_117693_ebadc189_0003, "volume": 0.9130849474, "area": 14.3810489586},
    "model_118105_8adbe5cd_0005": {"func": model_118105_8adbe5cd_0005, "volume": 88.3112710087, "area": 905.4567057114},
    "model_118116_bcc4d1ef_0001": {"func": model_118116_bcc4d1ef_0001, "volume": 0.7068141502, "area": 9.3991148575},
    "model_118124_46a97d36_0003": {"func": model_118124_46a97d36_0003, "volume": 0.9130849474, "area": 14.3810489586},
    "model_118127_40704f5d_0001": {"func": model_118127_40704f5d_0001, "volume": 1.1399393769, "area": 20.0588701226},
    "model_118127_40704f5d_0002": {"func": model_118127_40704f5d_0002, "volume": 8.3874812447, "area": 118.6660527591},
    "model_118269_fa4b08d7_0001": {"func": model_118269_fa4b08d7_0001, "volume": 0.3319776713, "area": 4.0661643195},
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
