"""Batch 002 - passing/03_4to5ops
86 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_122019_6e847ad7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.8626548246, perimeter: 29.3132741229
            with BuildLine():
                CenterArc((-0.6, 3.6), 0.4, 90, 90)
                Line((-1, -5.6), (-1, 3.6))
                CenterArc((-0.6, -5.6), 0.4, 180, 90)
                Line((3.6, -6), (-0.6, -6))
                CenterArc((3.6, -5.6), 0.4, -90, 90)
                Line((4, 3.6), (4, -5.6))
                CenterArc((3.6, 3.6), 0.4, 0, 90)
                Line((-0.6, 4), (3.6, 4))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.103284511, perimeter: 4.2313871076
            with BuildLine():
                Line((2.5000000373, 5.5500000827), (0.4343064008, 5.5500000827))
                Line((2.5000000373, 5.6), (2.5000000373, 5.5500000827))
                Line((0.4343064008, 5.6), (2.5000000373, 5.6))
                Line((0.4343064008, 5.5500000827), (0.4343064008, 5.6))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_122311_477d4e3b_0000():
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
        # Sketch1 -> Extrude28 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1605524909, perimeter: 2.3352588092
            with BuildLine():
                _nurbs_edge([(-2.6020000179, 0.7999999821), (-2.5963114472, 0.7779199834), (-2.5854310859, 0.7337599858), (-2.5706008389, 0.6675199894), (-2.553857197, 0.5791999937), (-2.5383204135, 0.4687999985), (-2.5286583455, 0.3584000026), (-2.5253504144, 0.248000006), (-2.5286583457, 0.1376000086), (-2.5383204138, 0.0272000104), (-2.5538571973, -0.0831999884), (-2.5706008391, -0.171519988), (-2.585431086, -0.2377599879), (-2.5963114472, -0.281919988), (-2.6020000179, -0.3039999881)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-2.6020000179, 0.7000000119), 0.1, 90, 90)
                Line((-2.7020000179, -0.2039999881), (-2.7020000179, 0.7000000119))
                CenterArc((-2.6020000179, -0.2039999881), 0.1, 180, 90)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude29 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4192062739, perimeter: 4.9336913508
            with BuildLine():
                Line((-1.9693199428, -0.3113199821), (-1.7693199524, -0.3113199821))
                Line((-1.6248503214, -0.1730140685), (-1.7693199524, -0.3113199821))
                Line((-1.3021110953, -0.1729777024), (-1.6248503214, -0.1730140685))
                CenterArc((-1.3000000179, -0.0729999881), 0.1, -91.2096481246, 91.2096481246)
                Line((-1.2000000179, -0.0729999881), (-1.2000000179, 0.7000000119))
                CenterArc((-1.3000000179, 0.7000000119), 0.1, 0, 90)
                Line((-2.6020000179, 0.7999999821), (-1.3000000179, 0.8000000119))
                _nurbs_edge([(-2.6020000179, 0.7999999821), (-2.5963114472, 0.7779199834), (-2.5854310859, 0.7337599858), (-2.5706008389, 0.6675199894), (-2.553857197, 0.5791999937), (-2.5383204135, 0.4687999985), (-2.5286583455, 0.3584000026), (-2.5253504144, 0.248000006), (-2.5286583457, 0.1376000086), (-2.5383204138, 0.0272000104), (-2.5538571973, -0.0831999884), (-2.5706008391, -0.171519988), (-2.585431086, -0.2377599879), (-2.5963114472, -0.281919988), (-2.6020000179, -0.3039999881)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-2.6020000179, -0.3039999881), (-2.14513272, -0.3039999881))
                Line((-2.1093199428, -0.2613199821), (-2.14513272, -0.3039999881))
                Line((-1.9693199428, -0.2613199821), (-2.1093199428, -0.2613199821))
                Line((-1.9693199428, -0.3113199821), (-1.9693199428, -0.2613199821))
            make_face()
        # OneSide extrude, distance=0.07
        extrude(amount=0.07, mode=Mode.ADD)
    return part.part


def model_122410_506a2f72_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8190937298, perimeter: 7.0984895497
            with BuildLine():
                Line((1.4501029262, -2.2986310637), (3.1112698372, -3.9597979746))
                Line((3.1112698372, -3.9597979746), (3.5355339059, -3.5355339059))
                Line((3.5355339059, -3.5355339059), (3.9597979746, -3.1112698372))
                Line((3.9597979746, -3.1112698372), (2.2986310637, -1.4501029262))
                Line((2.2986310637, -1.4501029262), (1.4501029262, -2.2986310637))
            make_face()
        # OneSide extrude, distance=0.7007
        extrude(amount=0.7007)
    return part.part


def model_122425_248c57e8_0000():
    """Model: PT1 Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.64, perimeter: 25.8
            with BuildLine():
                Line((-5.6, -9.2), (-3.4, -9.2))
                Line((-3.4, -9.2), (-3.4, -8.9))
                Line((-3.4, -8.9), (3.4, -8.9))
                Line((3.4, -8.9), (3.4, -9.2))
                Line((3.4, -9.2), (5.6, -9.2))
                Line((5.6, -9.2), (5.6, -7.8))
                Line((-5.6, -7.8), (5.6, -7.8))
                Line((-5.6, -9.2), (-5.6, -7.8))
            make_face()
        # OneSide extrude, distance=5.6
        extrude(amount=5.6)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.7213478829, perimeter: 25.4469004941
            with BuildLine():
                CenterArc((0, 0), 2.8, 161.2775649214, 217.4448701572)
                CenterArc((0, 0), 2.8, 18.7224350786, 142.5551298428)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


def model_122425_248c57e8_0002():
    """Model: PT2 Pulley Arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 33 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24.5986468844, perimeter: 34.5509625958
            with BuildLine():
                CenterArc((0, 0), 2.6, -91.3022889352, 182.6045778704)
                Line((-0.0590909091, -2.5993284257), (8.638961757, -2.7970625151))
                Line((8.638961757, -2.7970625151), (8.7363636364, -2.7992767661))
                CenterArc((8.8, 0), 2.8, 180, 88.6977110648)
                CenterArc((8.8, 0), 2.8, 91.3022889352, 88.6977110648)
                Line((-0.0590909091, 2.5993284257), (8.7363636364, 2.7992767661))
            make_face()
        # Symmetric extrude, full_length=True, total=1.4
        extrude(amount=0.7, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 33 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.328427817, perimeter: 24.1902634326
            with BuildLine():
                CenterArc((0, 0), 2.6, 91.3022889352, 177.3954221296)
                CenterArc((0, 0), 2.6, -91.3022889352, 182.6045778704)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=2.6
        extrude(amount=1.3, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 33 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 25.5841630797, perimeter: 34.1809218958
            with BuildLine():
                CenterArc((8.8, 0), 2.8, 91.3022889352, 88.6977110648)
                CenterArc((8.8, 0), 2.8, 180, 88.6977110648)
                CenterArc((8.8, 0), 2.8, -91.3022889352, 1.3022889352)
                Line((8.8, -2.8), (10, -2.8))
                Line((10, -2.4), (10, -2.8))
                Line((12.6, -2.4), (10, -2.4))
                Line((12.6, -2.4), (12.6, -0.2))
                Line((10.0338962679, -0.2), (12.6, -0.2))
                CenterArc((8.8, 0), 1.25, -180, 170.7931037787)
                CenterArc((8.8, 0), 1.25, 9.2068962213, 170.7931037787)
                Line((10.0338962679, 0.2), (12.6, 0.2))
                Line((12.6, 2.4), (12.6, 0.2))
                Line((12.6, 2.4), (10, 2.4))
                Line((10, 2.4), (10, 2.8))
                Line((8.8, 2.8), (10, 2.8))
                CenterArc((8.8, 0), 2.8, 90, 1.3022889352)
            make_face()
        # TwoSides extrude, along=1.3, against=-2.5
        extrude(amount=1.3, mode=Mode.ADD)
        extrude(sk.sketch, amount=-2.5, mode=Mode.ADD)
    return part.part


def model_122511_ab7ee8b4_0001():
    """Model: Phone case v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.9063, perimeter: 17.862
            with BuildLine():
                Line((7.3, 12.779), (0, 12.779))
                Line((7.3, 14.11), (7.3, 12.779))
                Line((7.3, 14.41), (7.3, 14.11))
                Line((7.3, 14.41), (0, 14.41))
                Line((0, 14.41), (0, 12.779))
            make_face()
            # Profile area: 11.9063, perimeter: 17.862
            with BuildLine():
                Line((0, 0), (7.3, 0))
                Line((7.3, 0), (7.3, 0.3))
                Line((7.3, 0.3), (7.3, 1.631))
                Line((7.3, 1.631), (0, 1.631))
                Line((0, 1.631), (0, 0))
            make_face()
            # Profile area: 81.3804, perimeter: 36.896
            with BuildLine():
                Line((7.3, 1.631), (0, 1.631))
                Line((7.3, 1.631), (7.3, 12.779))
                Line((7.3, 12.779), (0, 12.779))
                Line((0, 12.779), (0, 1.631))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_122752_229f274c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7, perimeter: 11
            with BuildLine():
                Line((-1, 1), (-4.5, 1))
                Line((-1, 3), (-1, 1))
                Line((-4.5, 3), (-1, 3))
                Line((-4.5, 1), (-4.5, 3))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6466851118, perimeter: 6.6859234963
            with BuildLine():
                Line((-3.3942491699, -0.7459442389), (-4.6821114827, -0.7459442389))
                Line((-3.3942491699, 1.3091551964), (-3.3942491699, -0.7459442389))
                Line((-4.6821114827, 1.3091551964), (-3.3942491699, 1.3091551964))
                Line((-4.6821114827, -0.7459442389), (-4.6821114827, 1.3091551964))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_123336_d21b9492_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 69.4706791927, perimeter: 39.7805826621
            with BuildLine():
                Line((5.5, 17), (2.5, 17))
                Line((2.5, 12), (2.5, 17))
                Line((1.5, 7.5), (2.5, 12))
                Line((0, 5), (1.5, 7.5))
                Line((0, 3.5), (0, 5))
                CenterArc((4, 8.0833333333), 6.0833333333, -131.1120904392, 82.2241808783)
                Line((8, 3.5), (8, 5))
                Line((6.5, 7.5), (8, 5))
                Line((5.5, 12), (6.5, 7.5))
                Line((5.5, 17), (5.5, 12))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 21.4601726198
            with BuildLine():
                CenterArc((4, 8.0833333333), 6.0833333333, -131.1120904392, 82.2241808783)
                Line((0, 1.5), (0, 3.5))
                CenterArc((4, 6.0833333333), 6.0833333333, -131.1120904392, 82.2241808783)
                Line((8, 1.5), (8, 3.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 21.4601726198
            with BuildLine():
                CenterArc((4, 8.0833333333), 6.0833333333, -131.1120904392, 82.2241808783)
                Line((0, 1.5), (0, 3.5))
                CenterArc((4, 6.0833333333), 6.0833333333, -131.1120904392, 82.2241808783)
                Line((8, 1.5), (8, 3.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_123496_74cb10dc_0002():
    """Model: ??? v2"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.0749481154, perimeter: 41.5205670506
            with BuildLine():
                Line((1.086709455, -3.0500000343), (10.086709455, -3.0500000343))
                Line((10.086709455, -3.0500000343), (10.4368132241, -3.5500000343))
                Line((10.4368132241, -3.5500000343), (15.586709455, -3.5500000343))
                Line((15.586709455, -3.5500000343), (15.586709455, -3.0500000343))
                Line((15.586709455, -3.0500000343), (10.586709455, -3.0500000343))
                Line((10.586709455, -3.0500000343), (10.586709455, -2.5500000343))
                Line((10.586709455, -2.5500000343), (15.586709455, -2.5500000343))
                Line((15.586709455, -2.5500000343), (15.586709455, -2.0500000343))
                Line((15.586709455, -2.0500000343), (10.4368132241, -2.0500000343))
                Line((10.4368132241, -2.0500000343), (10.086709455, -2.5500000343))
                Line((10.086709455, -2.5500000343), (1.086709455, -2.5500000343))
                Line((1.086709455, -2.5500000343), (1.086709455, -3.0500000343))
            make_face()
            # Profile area: 5.5749481154, perimeter: 23.5205670506
            with BuildLine():
                Line((1.086709455, -2.5500000343), (1.086709455, -3.0500000343))
                Line((0.7366056859, -2.0500000343), (1.086709455, -2.5500000343))
                Line((-4.413290545, -2.0500000343), (0.7366056859, -2.0500000343))
                Line((-4.413290545, -2.0500000343), (-4.413290545, -2.5500000343))
                Line((-4.413290545, -2.5500000343), (0.586709455, -2.5500000343))
                Line((0.586709455, -2.5500000343), (0.586709455, -2.8000000343))
                Line((0.586709455, -2.8000000343), (0.586709455, -3.0500000343))
                Line((0.586709455, -3.0500000343), (-4.413290545, -3.0500000343))
                Line((-4.413290545, -3.0500000343), (-4.413290545, -3.5500000343))
                Line((0.7366056859, -3.5500000343), (-4.413290545, -3.5500000343))
                Line((1.086709455, -3.0500000343), (0.7366056859, -3.5500000343))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> 押し出し7 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5500000343), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((15.086709455, 0.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-3.913290545, 0.5)):
                Circle(0.25)
        # OneSide extrude, distance=-3.1
        extrude(amount=-3.1, mode=Mode.SUBTRACT)
    return part.part


def model_124497_5c00f42d_0004():
    """Model: Hinge Bolt v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.26170669, perimeter: 3.9818430247
            Circle(0.63373)
        # OneSide extrude, distance=11.43
        extrude(amount=11.43)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9729973138, perimeter: 4.9792986922
            Circle(0.79248)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)
    return part.part


def model_124497_5c00f42d_0010():
    """Model: Collar v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0877487008, perimeter: 12.9669236777
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.79375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.555625
        extrude(amount=0.555625, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1237078806, perimeter: 1.2468195844
            Circle(0.1984375)
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_124497_5c00f42d_0013():
    """Model: Secondary Base v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.3594385743, perimeter: 30.2818882344
            with BuildLine():
                Line((0, 0), (11.90625, 0))
                Line((11.90625, 0), (11.90625, 1.905))
                CenterArc((10.16, 1.905), 1.74625, 0, 190.4756816964)
                Line((1.77165, 1.5875), (8.4428562051, 1.5875))
                Line((1.77165, 1.905), (1.77165, 1.5875))
                Line((0, 1.905), (1.77165, 1.905))
                Line((0, 0), (0, 1.905))
            make_face()
        # Symmetric extrude, each_side=4.1275
        extrude(amount=4.1275, both=True)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.1275), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7774366423, perimeter: 5.6286892465
            with BuildLine():
                Line((5.3859445061, 0), (6.8146945061, 0))
                CenterArc((10.16, 1.905), 3.8496875, -175.269201366, 24.9287551392)
                Line((5.3859445061, 1.5875), (6.3234276238, 1.5875))
                Line((5.3859445061, 1.5875), (5.3859445061, 0))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)
    return part.part


def model_124889_a069569f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 45.6036731188, perimeter: 23.9389360204
            Circle(3.81)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 130 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5414343991, perimeter: 7.1948301139
            with BuildLine():
                Line((3.0749862767, -1.7346383957), (3.1931125922, -1.7281655945))
                Line((3.1931125922, -1.7281655945), (3.1931125922, 0.0453819247))
                Line((3.1931125922, 0.0453819247), (3.0312925631, 0.0453819247))
                Line((3.0312925631, 0.0453819247), (3.0312925631, -0.5889525895))
                Line((3.0312925631, -0.5889525895), (2.7853261188, 0.0453819247))
                Line((2.7853261188, 0.0453819247), (2.6105604873, 0.0453819247))
                Line((2.6105604873, 0.0453819247), (2.9546641588, -0.8420433334))
                Line((2.9546641588, -0.8420433334), (2.6105604873, -1.7346383957))
                Line((2.6105604873, -1.7346383957), (2.7826123231, -1.7346383957))
                Line((2.7826123231, -1.7346383957), (3.0749862767, -0.976228739))
                Line((3.0749862767, -0.976228739), (3.0749862767, -1.7346383957))
            make_face()
            # Profile area: 0.6375011922, perimeter: 6.3161100992
            with BuildLine():
                Line((2.2358120992, -0.2264122166), (2.1963012128, -0.4077141569))
                Line((2.1963012128, -0.4077141569), (1.6008035056, -0.4077141569))
                Line((1.6008035056, -0.4077141569), (1.7302595289, -0.8439623771))
                Line((1.7302595289, -0.8439623771), (2.0159543901, -1.0761802369))
                Line((2.0159543901, -1.0761802369), (2.2278200614, -1.0133094079))
                Line((2.2278200614, -1.0133094079), (2.4163764524, -0.625838267))
                Line((2.4163764524, -0.625838267), (2.4163764524, -0.2264757242))
                Line((2.4163764524, -0.2264757242), (2.3220982569, 0.0912282647))
                Line((2.3220982569, 0.0912282647), (2.1218872258, 0.2589843631))
                Line((2.1218872258, 0.2589843631), (1.7367323301, 0.2589843631))
                Line((1.7367323301, 0.2589843631), (1.5037114881, 0.0912282647))
                Line((1.5037114881, 0.0912282647), (1.5037114881, -0.1293837068))
                Line((1.5037114881, -0.1293837068), (1.5735641421, -0.2264122166))
                Line((1.5735641421, -0.2264122166), (1.7561507335, -0.2264122166))
                Line((1.7561507335, -0.2264122166), (1.6648574378, -0.019077721))
                Line((1.6648574378, -0.019077721), (1.8711443947, 0.0717543236))
                Line((1.8711443947, 0.0717543236), (2.1445188035, -0.019077721))
                Line((2.1445188035, -0.019077721), (2.2358120992, -0.2264122166))
            make_face()
            with BuildLine():
                Line((2.0789433356, -0.8264951031), (2.1234054876, -0.8090278291))
                Line((2.0344811836, -0.8439623771), (2.0789433356, -0.8264951031))
                Line((1.9438619673, -0.8090278291), (2.0344811836, -0.8439623771))
                Line((1.8726611545, -0.6277893965), (1.9438619673, -0.8090278291))
                Line((2.1963012128, -0.6277893965), (1.8726611545, -0.6277893965))
                Line((2.1234054876, -0.8090278291), (2.1963012128, -0.6277893965))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3909004554, perimeter: 5.0099481018
            with BuildLine():
                Line((1.1153434182, -1.8058392085), (1.2771634473, -1.8058392085))
                Line((1.2771634473, -1.8058392085), (1.2771634473, -1.0549942734))
                Line((1.2771634473, -1.0549942734), (1.45840188, -1.0549942734))
                Line((1.45840188, -1.0549942734), (1.45840188, -0.8543374372))
                Line((1.45840188, -0.8543374372), (1.2771634473, -0.8543374372))
                Line((1.2771634473, -0.8543374372), (1.2771634473, 0.174837948))
                Line((1.2771634473, 0.174837948), (1.1153434182, 0.174837948))
                Line((1.1153434182, 0.174837948), (1.1153434182, -0.8543374372))
                Line((1.1153434182, -0.8543374372), (0.9341049856, -0.8543374372))
                Line((0.9341049856, -0.8543374372), (0.9341049856, -1.042048671))
                Line((0.9341049856, -1.042048671), (1.1153434182, -1.042048671))
                Line((1.1153434182, -1.042048671), (1.1153434182, -1.8058392085))
            make_face()
            # Profile area: 0.3355124166, perimeter: 4.7540410479
            with BuildLine():
                Line((0.636356132, -1.7799480039), (0.7463937518, -1.8058392085))
                Line((0.7463937518, -1.8058392085), (0.7463937518, -1.042048671))
                Line((0.7463937518, -1.042048671), (0.8564313716, -1.042048671))
                Line((0.8564313716, -1.042048671), (0.8564313716, -0.8737558407))
                Line((0.8564313716, -0.8737558407), (0.7463937518, -0.8737558407))
                Line((0.7463937518, -0.8737558407), (0.7463937518, 0.1618923457))
                Line((0.7463937518, 0.1618923457), (0.5781009215, 0.1618923457))
                Line((0.5781009215, 0.1618923457), (0.5781009215, -0.8737558407))
                Line((0.5781009215, -0.8737558407), (0.4356992959, -0.8737558407))
                Line((0.4356992959, -0.8737558407), (0.4356992959, -1.080885478))
                Line((0.4356992959, -1.080885478), (0.636356132, -1.080885478))
                Line((0.636356132, -1.080885478), (0.636356132, -1.7799480039))
            make_face()
            # Profile area: 0.8256653551, perimeter: 6.6635861869
            with BuildLine():
                Line((0.2091512551, -0.1156497542), (0.1379504423, -0.2782581336))
                Line((0.1379504423, -0.2782581336), (-0.4446016626, -0.2782581336))
                Line((-0.4446016626, -0.2782581336), (-0.4446016626, -0.7491544183))
                Line((-0.4446016626, -0.7491544183), (-0.2504176276, -0.9514294547))
                Line((-0.2504176276, -0.9514294547), (0.12500484, -1.0744126769))
                Line((0.12500484, -1.0744126769), (0.3069007928, -0.8997925622))
                Line((0.3069007928, -0.8997925622), (0.4273211388, -0.5321936111))
                Line((0.4273211388, -0.5321936111), (0.3671109658, -0.1229109056))
                Line((0.3671109658, -0.1229109056), (0.3069007928, 0.2863717999))
                Line((0.3069007928, 0.2863717999), (-0.108016002, 0.3560763806))
                Line((-0.108016002, 0.3560763806), (-0.4542986366, 0.4142506608))
                Line((-0.4542986366, 0.4142506608), (-0.5250619254, -0.0069680979))
                Line((-0.5250619254, -0.0069680979), (-0.3798736509, -0.1229109056))
                Line((-0.3798736509, -0.1229109056), (-0.2811573193, -0.1083886027))
                Line((-0.2811573193, -0.1083886027), (-0.1500652309, 0.0557702138))
                Line((-0.1500652309, 0.0557702138), (0.0994423954, 0.0924756429))
                Line((0.0994423954, 0.0924756429), (0.2091512551, -0.1156497542))
            make_face()
            with BuildLine():
                Line((0.1897328516, -0.8478646361), (0.1897328516, -0.6504442005))
                Line((0.0214400213, -0.8478646361), (0.1897328516, -0.8478646361))
                Line((-0.0950703997, -0.7701910221), (0.0214400213, -0.8478646361))
                Line((-0.0950703997, -0.530697379), (-0.0950703997, -0.7701910221))
                Line((0.1379504423, -0.530697379), (-0.0950703997, -0.530697379))
                Line((0.1897328516, -0.6504442005), (0.1379504423, -0.530697379))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3504954578, perimeter: 4.9699753749
            with BuildLine():
                Line((-0.799817162, -1.011590363), (-0.7017083258, -1.0584565008))
                Line((-0.7017083258, -1.0584565008), (-0.6911327182, -0.9955051545))
                Line((-0.6911327182, -0.9955051545), (-0.6911327182, 0.3754947841))
                Line((-0.6911327182, 0.3754947841), (-0.7941329255, 0.3754947841))
                Line((-0.7941329255, 0.3754947841), (-0.7941329255, -0.7831366244))
                Line((-0.7941329255, -0.7831366244), (-0.891224943, -0.8672830396))
                Line((-0.891224943, -0.8672830396), (-0.9883169604, -0.8672830396))
                Line((-0.9883169604, -0.8672830396), (-1.3313754222, -0.8672830396))
                Line((-1.3313754222, -0.8672830396), (-1.4351702388, -0.7475197896))
                Line((-1.4351702388, -0.7475197896), (-1.4351702388, -0.6407349988))
                Line((-1.4351702388, -0.6407349988), (-1.5277170575, -0.6407349988))
                Line((-1.5277170575, -0.6407349988), (-1.5277170575, -1.1132494838))
                Line((-1.5277170575, -1.1132494838), (-0.9171161476, -1.1132494838))
                Line((-0.9171161476, -1.1132494838), (-0.799817162, -1.011590363))
            make_face()
            # Profile area: 0.3755788512, perimeter: 3.262122887
            with BuildLine():
                Line((-1.952764334, -1.0350234319), (-1.7132706909, -1.0584565008))
                Line((-1.7132706909, -1.0584565008), (-1.7132706909, 0.3042939713))
                Line((-1.7132706909, 0.3042939713), (-2.030437948, 0.3042939713))
                Line((-2.030437948, 0.3042939713), (-1.952764334, -1.0350234319))
            make_face()
            # Profile area: 0.0245806828, perimeter: 0.6404742899
            with BuildLine():
                Line((-1.8506610334, -1.3971368685), (-1.7132706909, -1.4174711386))
                Line((-1.7132706909, -1.4174711386), (-1.7132706909, -1.2168143025))
                Line((-1.7132706909, -1.2168143025), (-1.8330175125, -1.2168143025))
                Line((-1.8330175125, -1.2168143025), (-1.8506610334, -1.3971368685))
            make_face()
            # Profile area: 0.649140667, perimeter: 6.0784542807
            with BuildLine():
                Line((-2.3031861259, -1.0105070549), (-2.1793123748, -1.0350234319))
                Line((-2.1793123748, -1.0350234319), (-2.1793123748, -0.9449566536))
                Line((-2.1793123748, -0.9449566536), (-2.1793123748, 0.2848755678))
                Line((-2.1793123748, 0.2848755678), (-2.4268485302, 0.30909555))
                Line((-2.4268485302, 0.30909555), (-2.4268485302, -0.5177517767))
                Line((-2.4268485302, -0.5177517767), (-2.5482620412, -0.7248814139))
                Line((-2.5482620412, -0.7248814139), (-2.6712452634, -0.7248814139))
                Line((-2.6712452634, -0.7248814139), (-2.735973275, -0.5177517767))
                Line((-2.735973275, -0.5177517767), (-2.7036092692, -0.0646556951))
                Line((-2.7036092692, -0.0646556951), (-2.735973275, 0.330185176))
                Line((-2.735973275, 0.330185176), (-2.9943356832, 0.3090079294))
                Line((-2.9943356832, 0.3090079294), (-2.9031013261, -0.8040512266))
                Line((-2.9031013261, -0.8040512266), (-2.6319868431, -0.9384492939))
                Line((-2.6319868431, -0.9384492939), (-2.3346596028, -0.8712502603))
                Line((-2.3346596028, -0.8712502603), (-2.3031861259, -1.0105070549))
            make_face()
            # Profile area: 0.5210822618, perimeter: 5.5906328014
            with BuildLine():
                Line((-3.0887409385, -0.7831366244), (-3.3024418048, -0.8774164184))
                Line((-2.9741076767, -0.5380935269), (-3.0887409385, -0.7831366244))
                Line((-3.0401949298, -0.3882957534), (-2.9741076767, -0.5380935269))
                Line((-3.1372869472, -0.1682205137), (-3.0401949298, -0.3882957534))
                Line((-3.2424699662, -0.2912037359), (-3.1372869472, -0.1682205137))
                Line((-3.4479814032, -0.2912037359), (-3.2424699662, -0.2912037359))
                Line((-3.4479814032, -0.0452372916), (-3.4479814032, -0.2912037359))
                Line((-3.4479814032, 0.2007291527), (-3.4479814032, -0.0452372916))
                Line((-3.324998181, 0.2719299655), (-3.4479814032, 0.2007291527))
                Line((-3.1599417513, 0.2007291527), (-3.324998181, 0.2719299655))
                Line((-3.1599417513, 0.0648003282), (-3.1599417513, 0.2007291527))
                Line((-3.0725589356, 0.0648003282), (-3.1599417513, 0.0648003282))
                Line((-3.0725589356, 0.3366579771), (-3.0725589356, 0.0648003282))
                Line((-3.2473245671, 0.5243692109), (-3.0725589356, 0.3366579771))
                Line((-3.6162742335, 0.3366579771), (-3.2473245671, 0.5243692109))
                Line((-3.6162742335, 0.136001141), (-3.6162742335, 0.3366579771))
                Line((-3.6162742335, -0.9048497771), (-3.6162742335, 0.136001141))
                Line((-3.441508602, -0.9048497771), (-3.6162742335, -0.9048497771))
                Line((-3.3024418048, -0.8774164184), (-3.441508602, -0.9048497771))
            make_face()
            with BuildLine():
                Line((-3.1955421577, -0.4789149697), (-3.441508602, -0.6213165953))
                Line((-3.441508602, -0.6213165953), (-3.441508602, -0.5565885837))
                Line((-3.441508602, -0.5565885837), (-3.441508602, -0.4012413557))
                Line((-3.441508602, -0.4012413557), (-3.2926341752, -0.4012413557))
                Line((-3.2926341752, -0.4012413557), (-3.1955421577, -0.4789149697))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4478890913, perimeter: 4.2211920732
            with BuildLine():
                Line((-0.8147336374, 0.4913131778), (-0.6128944949, 0.5761516671))
                Line((-0.6128944949, 0.5761516671), (-0.8667518011, 1.0098293451))
                Line((-0.8667518011, 1.0098293451), (-0.6968214221, 1.1092996901))
                Line((-0.6968214221, 1.1092996901), (-0.7817866116, 1.2544501554))
                Line((-0.7817866116, 1.2544501554), (-1.0099428923, 1.2544501554))
                Line((-1.0099428923, 1.2544501554), (-1.4117869197, 1.9409412687))
                Line((-1.4117869197, 1.9409412687), (-1.5991037696, 1.8312935895))
                Line((-1.5991037696, 1.8312935895), (-1.210864906, 1.1680448872))
                Line((-1.210864906, 1.1680448872), (-1.4049843378, 1.0544152528))
                Line((-1.4049843378, 1.0544152528), (-1.3079246219, 0.8886030772))
                Line((-1.3079246219, 0.8886030772), (-1.0738489581, 0.8886030772))
                Line((-1.0738489581, 0.8886030772), (-0.8147336374, 0.4913131778))
            make_face()
            # Profile area: 0.2903234982, perimeter: 3.4352366426
            with BuildLine():
                Line((-0.3570074517, 0.6797164857), (-0.1403800099, 0.6797164857))
                Line((-0.1403800099, 0.6797164857), (-0.8667518011, 2.0644699007))
                Line((-0.8667518011, 2.0644699007), (-1.0366353925, 1.975357538))
                Line((-1.0366353925, 1.975357538), (-0.3570074517, 0.6797164857))
            make_face()
            # Profile area: 0.2449516897, perimeter: 2.6924314722
            with BuildLine():
                Line((0.0473312239, 1.003356544), (0.1962056507, 1.1198669649))
                Line((0.1962056507, 1.1198669649), (-0.3193819135, 2.1027818426))
                Line((-0.3193819135, 2.1027818426), (-0.5388466644, 1.9876617046))
                Line((-0.5388466644, 1.9876617046), (0.0473312239, 1.003356544))
            make_face()
            # Profile area: 0.0354825191, perimeter: 0.7863021652
            with BuildLine():
                Line((0.1217684373, 0.798092209), (0.3496101953, 0.8274169146))
                Line((0.3496101953, 0.8274169146), (0.2573211405, 1.003356544))
                Line((0.2573211405, 1.003356544), (0.0473312239, 0.8932064261))
                Line((0.0473312239, 0.8932064261), (0.1217684373, 0.798092209))
            make_face()
            # Profile area: 0.5811193597, perimeter: 5.2295001423
            with BuildLine():
                Line((1.0938215363, 1.4035668386), (1.2189082348, 1.59238145))
                Line((1.2189082348, 1.59238145), (0.8564313696, 2.3173351805))
                Line((0.8564313696, 2.3173351805), (0.6759794107, 2.5488729354))
                Line((0.6759794107, 2.5488729354), (0.5055909087, 2.4904990968))
                Line((0.5055909087, 2.4904990968), (0.338059444, 2.4331040579))
                Line((0.338059444, 2.4331040579), (0.1314776391, 2.181406356))
                Line((0.1314776391, 2.181406356), (0.2347685415, 1.7542014791))
                Line((0.2347685415, 1.7542014791), (0.3496101953, 1.4189880033))
                Line((0.3496101953, 1.4189880033), (0.5345300901, 1.2672143266))
                Line((0.5345300901, 1.2672143266), (0.6631922006, 1.3112930126))
                Line((0.6631922006, 1.3112930126), (0.4420701427, 1.9567303709))
                Line((0.4420701427, 1.9567303709), (0.5345300901, 2.2655527711))
                Line((0.5345300901, 2.2655527711), (0.7226635235, 2.111141571))
                Line((0.7226635235, 2.111141571), (0.9729417905, 1.6340116918))
                Line((0.9729417905, 1.6340116918), (1.0938215363, 1.4035668386))
            make_face()
            # Profile area: 1.5485764076, perimeter: 8.9138797663
            with BuildLine():
                Line((2.2092468131, 0.8739005207), (2.9083093389, 1.1133941638))
                Line((2.9083093389, 1.1133941638), (2.4099036492, 2.4791552096))
                Line((2.4099036492, 2.4791552096), (1.5878579012, 2.6862848469))
                Line((1.5878579012, 2.6862848469), (1.3095274511, 2.0972599409))
                Line((1.3095274511, 2.0972599409), (1.5878579012, 1.670055064))
                Line((1.5878579012, 1.670055064), (2.2092468131, 1.7962746867))
                Line((2.2092468131, 1.7962746867), (1.5878579012, 1.514707836))
                Line((1.5878579012, 1.514707836), (1.7915000661, 1.0652906445))
                Line((1.7915000661, 1.0652906445), (2.2092468131, 0.8739005207))
            make_face()
            with BuildLine():
                Line((2.1088253766, 1.2899992402), (2.3715575295, 1.2363773859))
                Line((2.0380262312, 1.4966562052), (2.1088253766, 1.2899992402))
                Line((2.3267386086, 1.6274790012), (2.0380262312, 1.4966562052))
                Line((2.4163764503, 1.3658334092), (2.3267386086, 1.6274790012))
                Line((2.3715575295, 1.2363773859), (2.4163764503, 1.3658334092))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.8234339195, 1.9548583152), (2.0326197496, 2.0265238311))
                Line((1.7056470772, 2.1059905123), (1.8234339195, 1.9548583152))
                Line((1.6655315152, 2.2903150243), (1.7056470772, 2.1059905123))
                Line((1.8234339195, 2.3246801971), (1.6655315152, 2.2903150243))
                Line((1.9918136953, 2.2903150243), (1.8234339195, 2.3246801971))
                Line((2.0734258039, 2.1102055432), (1.9918136953, 2.2903150243))
                Line((2.0326197496, 2.0265238311), (2.0734258039, 2.1102055432))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)
    return part.part


def model_124890_897c868e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 45.6036731188, perimeter: 23.9389360204
            Circle(3.81)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 58 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.056018059, perimeter: 14.490809434
            with BuildLine():
                Line((2.2918833832, -1.817670877), (2.8019853309, -1.6034413369))
                Line((2.8019853309, -1.6034413369), (1.5074250979, 0.8977768911))
                Line((1.5074250979, 0.8977768911), (1.0542324575, 0.6632171219))
                Line((1.0542324575, 0.6632171219), (1.6454781566, -0.4791279633))
                Line((1.6454781566, -0.4791279633), (-0.002895174, 0.2744701122))
                Line((-0.002895174, 0.2744701122), (-0.5704230055, -0.0192663373))
                Line((-0.5704230055, -0.0192663373), (1.349855307, -0.7244189565))
                Line((1.349855307, -0.7244189565), (0.7238066347, -2.4292806493))
                Line((0.7238066347, -2.4292806493), (1.2393825427, -2.1624330548))
                Line((1.2393825427, -2.1624330548), (1.814323533, -0.8949780801))
                Line((1.814323533, -0.8949780801), (2.2918833832, -1.817670877))
            make_face()
            # Profile area: 4.0725938075, perimeter: 14.1734776135
            with BuildLine():
                Line((-2.9755890424, -0.7883478569), (-1.0114288537, 0.1446258928))
                Line((-1.7143749794, -3.2660487039), (-2.9755890424, -0.7883478569))
                Line((-1.2338502351, -3.0378000229), (-1.7143749794, -3.2660487039))
                Line((-2.0996967176, -1.214960751), (-1.2338502351, -3.0378000229))
                Line((-1.2015620564, -0.7883478569), (-2.0996967176, -1.214960751))
                Line((-0.2866590897, -2.7144641965), (-1.2015620564, -0.7883478569))
                Line((0.2847848778, -2.4744726048), (-0.2866590897, -2.7144641965))
                Line((-1.0114288537, 0.1446258928), (0.2847848778, -2.4744726048))
            make_face()
            # Profile area: 0.9744184734, perimeter: 7.6343794254
            with BuildLine():
                Line((1.4820892085, 1.4137517555), (2.0268474136, 1.6809059209))
                Line((2.0268474136, 1.6809059209), (1.3119579733, 3.1253944443))
                Line((1.3119579733, 3.1253944443), (0.5629203537, 2.7546894674))
                Line((0.5629203537, 2.7546894674), (0.9374391635, 2.2083193492))
                Line((0.9374391635, 2.2083193492), (1.3311096908, 2.4031501826))
                Line((1.3311096908, 2.4031501826), (1.3793213945, 2.3057347659))
                Line((1.3793213945, 2.3057347659), (1.0332643103, 2.068523976))
                Line((1.0332643103, 2.068523976), (1.4820892085, 1.4137517555))
            make_face()
            with BuildLine():
                Line((1.3555939594, 2.068523976), (1.418841584, 1.9395547632))
                Line((1.4820892085, 2.278619794), (1.3555939594, 2.068523976))
                Line((1.6694026934, 1.8966659598), (1.4820892085, 2.278619794))
                Line((1.418841584, 1.9395547632), (1.6694026934, 1.8966659598))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.8696092309, 2.6994121686), (1.0333010915, 2.5199727386))
                Line((1.1969929521, 2.8599639951), (0.8696092309, 2.6994121686))
                Line((1.2757289654, 2.6994121686), (1.1969929521, 2.8599639951))
                Line((1.0333010915, 2.5199727386), (1.2757289654, 2.6994121686))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3636341876, perimeter: 3.6016386679
            with BuildLine():
                Line((0.7100615691, 1.9099448564), (0.6284027174, 2.104434886))
                Line((0.6284027174, 2.104434886), (0.3327315531, 2.5759105265))
                Line((0.3327315531, 2.5759105265), (-0.1946818752, 2.3401727063))
                Line((-0.1946818752, 2.3401727063), (0.069024839, 1.6888970335))
                Line((0.069024839, 1.6888970335), (0.2384644351, 1.7951557633))
                Line((0.2384644351, 1.7951557633), (0.069024839, 2.1742409614))
                Line((0.069024839, 2.1742409614), (0.2384644351, 2.2499753263))
                Line((0.2384644351, 2.2499753263), (0.5325093668, 1.7951557633))
                Line((0.5325093668, 1.7951557633), (0.7100615691, 1.9099448564))
            make_face()
            # Profile area: 0.2247939378, perimeter: 3.0057551964
            with BuildLine():
                Line((0.0063474204, 1.0181101654), (0.153744637, 1.1055458174))
                Line((0.153744637, 1.1055458174), (-0.3065574509, 2.3401727063))
                Line((-0.3065574509, 2.3401727063), (-0.4645869474, 2.2812550625))
                Line((-0.4645869474, 2.2812550625), (0.0063474204, 1.0181101654))
            make_face()
            # Profile area: 0.3181329644, perimeter: 3.2635197895
            with BuildLine():
                Line((-0.2291197635, 0.878431634), (-0.0764064069, 1.0181101654))
                Line((-0.0764064069, 1.0181101654), (-0.5583238153, 2.3107138844))
                Line((-0.5583238153, 2.3107138844), (-0.7866123954, 2.1752936825))
                Line((-0.7866123954, 2.1752936825), (-0.2291197635, 0.878431634))
            make_face()
            # Profile area: 0.5421932977, perimeter: 4.8096933184
            with BuildLine():
                Line((-0.9989767341, 0.878431634), (-0.4645869474, 0.878431634))
                Line((-0.4645869474, 0.878431634), (-0.9989767341, 2.1215509037))
                Line((-0.9989767341, 2.1215509037), (-1.4940727812, 1.6687137041))
                Line((-1.4940727812, 1.6687137041), (-0.9989767341, 0.878431634))
            make_face()
            with BuildLine():
                Line((-1.2465247577, 1.5540803699), (-0.9989767341, 1.2334036182))
                Line((-0.9798600306, 1.6687137041), (-1.2465247577, 1.5540803699))
                Line((-0.8099975415, 1.273572669), (-0.9798600306, 1.6687137041))
                Line((-0.9989767341, 1.2334036182), (-0.8099975415, 1.273572669))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1967764883, perimeter: 2.5807189532
            with BuildLine():
                Line((-1.7164228487, 0.9457235664), (-1.4231350928, 1.1432453396))
                Line((-1.4231350928, 1.1432453396), (-1.7164228487, 1.611397037))
                Line((-1.7164228487, 1.611397037), (-2.0900593327, 1.3773211883))
                Line((-2.0900593327, 1.3773211883), (-1.7164228487, 0.9457235664))
            make_face()
            with BuildLine():
                Line((-1.8035998413, 1.2973712907), (-1.6622511477, 1.1432453396))
                Line((-1.7164228487, 1.3773211883), (-1.8035998413, 1.2973712907))
                Line((-1.5697789707, 1.2174213931), (-1.7164228487, 1.3773211883))
                Line((-1.6622511477, 1.1432453396), (-1.5697789707, 1.2174213931))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5041117009, perimeter: 5.2901236221
            with BuildLine():
                Line((-2.3650185811, 0.5861235016), (-1.9032410907, 0.9499365682))
                Line((-1.9032410907, 0.9499365682), (-2.2139996502, 1.3373462395))
                Line((-2.2139996502, 1.3373462395), (-2.5124307246, 1.0979613772))
                Line((-2.5124307246, 1.0979613772), (-2.59201564, 1.3373462395))
                Line((-2.59201564, 1.3373462395), (-2.4671564343, 1.6529461915))
                Line((-2.4671564343, 1.6529461915), (-2.2004511251, 1.6529461915))
                Line((-2.2004511251, 1.6529461915), (-2.2004511251, 1.8487192845))
                Line((-2.2004511251, 1.8487192845), (-2.5295860371, 1.8487192845))
                Line((-2.5295860371, 1.8487192845), (-2.8317490165, 1.537065895))
                Line((-2.8317490165, 1.537065895), (-2.8317490165, 1.1614836052))
                Line((-2.8317490165, 1.1614836052), (-2.3650185811, 0.5861235016))
            make_face()
            with BuildLine():
                Line((-2.4818903876, 0.9499365682), (-2.3611485377, 0.7994127647))
                Line((-2.2404066878, 1.1436414038), (-2.4818903876, 0.9499365682))
                Line((-2.2404066878, 0.9499365682), (-2.2404066878, 1.1436414038))
                Line((-2.3611485377, 0.7994127647), (-2.2404066878, 0.9499365682))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6154778729, perimeter: 5.9486733604
            with BuildLine():
                Line((-2.901713124, 0.3943368005), (-3.2872424318, 0.4263012507))
                Line((-3.2872424318, 0.4263012507), (-3.2872424318, 0.2105412118))
                Line((-3.2872424318, 0.2105412118), (-3.0155446051, 0.2105412118))
                Line((-3.0155446051, 0.2105412118), (-2.5600511898, 0.3184212312))
                Line((-2.5600511898, 0.3184212312), (-2.5600511898, 0.6340701769))
                Line((-2.5600511898, 0.6340701769), (-2.8876868043, 0.7699190903))
                Line((-2.8876868043, 0.7699190903), (-3.1513935185, 0.7699190903))
                Line((-3.1513935185, 0.7699190903), (-3.3543596644, 0.9634175932))
                Line((-3.3543596644, 0.9634175932), (-3.2528765915, 1.2653680684))
                Line((-3.2528765915, 1.2653680684), (-3.0195401614, 1.186945612))
                Line((-3.0195401614, 1.186945612), (-2.901713124, 1.0416947963))
                Line((-2.901713124, 1.0416947963), (-2.901713124, 1.4891192197))
                Line((-2.901713124, 1.4891192197), (-3.1362083764, 1.5679311468))
                Line((-3.1362083764, 1.5679311468), (-3.2333634687, 1.4891192197))
                Line((-3.2333634687, 1.4891192197), (-3.5091438154, 1.265407008))
                Line((-3.5091438154, 1.265407008), (-3.5909047087, 0.8738035534))
                Line((-3.5909047087, 0.8738035534), (-3.5091438154, 0.6420612895))
                Line((-3.5091438154, 0.6420612895), (-2.8317490165, 0.5006314752))
                Line((-2.8317490165, 0.5006314752), (-2.901713124, 0.3943368005))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)
    return part.part


def model_125002_7287b175_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 120 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 3.66135805, perimeter: 35.4838025582
            with BuildLine():
                Line((3, 2.8999999887), (3, 2.405))
                CenterArc((2.9, 2.8999999887), 0.1, 0, 90.0000064571)
                Line((2.405, 2.9999999329), (2.8999999887, 2.9999999887))
                Line((2.405, 2.9799999334), (2.405, 2.9999999329))
                Line((2.205, 2.9799999334), (2.405, 2.9799999334))
                Line((2.205, 3), (2.205, 2.9799999334))
                Line((1.905, 3), (2.205, 3))
                Line((1.905, 2.8), (1.905, 3))
                Line((2.4, 2.8000000231), (1.905, 2.8))
                Line((2.4, 2.8000000231), (2.4, 2.5414213562))
                Line((2.4, 2.5414213562), (2.1485786438, 2.29))
                Line((0.8514213562, 2.29), (2.1485786438, 2.29))
                Line((0.6, 2.5414213562), (0.8514213562, 2.29))
                Line((0.6, 2.8), (0.6, 2.5414213562))
                Line((1.095, 2.8), (0.6, 2.8))
                Line((1.095, 3), (1.095, 2.8))
                Line((1.095, 3), (0.795, 2.9999999329))
                Line((0.795, 2.98), (0.795, 2.9999999329))
                Line((0.595, 2.98), (0.795, 2.98))
                Line((0.595, 3), (0.595, 2.98))
                Line((0.595, 3), (0.1, 3))
                CenterArc((0.1, 2.9), 0.1, 90, 90)
                Line((0, 2.9), (0, 2.405))
                Line((0.02, 2.405), (0, 2.405))
                Line((0.02, 2.205), (0.02, 2.405))
                Line((0, 2.205), (0.02, 2.205))
                Line((0, 2.205), (0, 1.905))
                Line((0, 1.905), (0.2, 1.905))
                Line((0.2000000016, 2.4), (0.2, 1.905))
                Line((0.2000000016, 2.4), (0.4585786438, 2.4))
                Line((0.4585786438, 2.4), (0.71, 2.1485786438))
                Line((0.71, 0.8514213562), (0.71, 2.1485786438))
                Line((0.4585786438, 0.6), (0.71, 0.8514213562))
                Line((0.2, 0.6), (0.4585786438, 0.6))
                Line((0.2, 1.095), (0.2, 0.6))
                Line((0.2, 1.095), (0, 1.095))
                Line((0, 1.095), (0, 0.795))
                Line((0, 0.795), (0.0199999996, 0.795))
                Line((0.0199999996, 0.795), (0.0199999996, 0.595))
                Line((0.0199999996, 0.595), (0, 0.595))
                Line((0, 0.595), (0, 0.1))
                CenterArc((0.1, 0.1), 0.1, 180, 90)
                Line((0.595, 0), (0.1, 0))
                Line((0.595, 0.02), (0.595, 0))
                Line((0.795, 0.02), (0.595, 0.02))
                Line((0.795, 0), (0.795, 0.02))
                Line((1.095, 0), (0.795, 0))
                Line((1.095, 0.2), (1.095, 0))
                Line((0.6, 0.2000000016), (1.095, 0.2))
                Line((0.6, 0.2000000016), (0.6, 0.4585786438))
                Line((0.6, 0.4585786438), (0.8514213562, 0.71))
                Line((2.1485786438, 0.71), (0.8514213562, 0.71))
                Line((2.4, 0.4585786438), (2.1485786438, 0.71))
                Line((2.4, 0.2), (2.4, 0.4585786438))
                Line((1.905, 0.2), (2.4, 0.2))
                Line((1.905, 0.2), (1.905, 0))
                Line((1.905, 0), (2.205, 0))
                Line((2.205, 0), (2.205, 0.02))
                Line((2.205, 0.02), (2.405, 0.02))
                Line((2.405, 0.02), (2.405, 0))
                Line((2.405, 0), (2.8999999887, 0))
                CenterArc((2.8999999887, 0.1), 0.1, -90, 90.0000064571)
                Line((2.9999999887, 0.1000000113), (2.9999999329, 0.595))
                Line((2.98, 0.595), (2.9999999329, 0.595))
                Line((2.9799999334, 0.795), (2.98, 0.595))
                Line((3, 0.795), (2.9799999334, 0.795))
                Line((3, 0.795), (3, 1.095))
                Line((2.8, 1.095), (3, 1.095))
                Line((2.8000000231, 0.6), (2.8, 1.095))
                Line((2.8000000231, 0.6), (2.5414213562, 0.6))
                Line((2.5414213562, 0.6), (2.29, 0.8514213562))
                Line((2.29, 2.1485786438), (2.29, 0.8514213562))
                Line((2.5414213562, 2.4), (2.29, 2.1485786438))
                Line((2.8, 2.4), (2.5414213562, 2.4))
                Line((2.8, 1.905), (2.8, 2.4))
                Line((2.8, 1.905), (3, 1.905))
                Line((3.0000000447, 2.205), (3, 1.905))
                Line((2.98, 2.205), (3.0000000447, 2.205))
                Line((2.98, 2.405), (2.98, 2.205))
                Line((3, 2.405), (2.98, 2.405))
            make_face()
            with BuildLine():
                Line((0.91, 1.21), (1.21, 1.3225176065))
                CenterArc((1.5, 1.5), 0.34, 180, 31.4669762933)
                CenterArc((1.5, 1.5), 0.34, 148.5330237067, 31.4669762933)
                Line((0.91, 1.79), (1.21, 1.6774823935))
                Line((0.91, 2.0400000373), (0.91, 1.79))
                CenterArc((0.96, 2.0400000373), 0.05, 89.9999914623, 90.0000085377)
                Line((0.9600000075, 2.0900000373), (1.21, 2.09))
                Line((1.21, 2.09), (1.3225176065, 1.79))
                CenterArc((1.5, 1.5), 0.34, 58.5330237067, 62.9339525865)
                Line((1.79, 2.09), (1.6774823935, 1.79))
                Line((1.79, 2.09), (2.04, 2.09))
                CenterArc((2.04, 2.04), 0.05, 0, 90)
                Line((2.09, 2.04), (2.09, 1.79))
                Line((2.09, 1.79), (1.79, 1.6774823935))
                CenterArc((1.5, 1.5), 0.34, -31.4669762933, 62.9339525865)
                Line((2.09, 1.209999973), (1.79, 1.3225176065))
                Line((2.09, 0.9600000373), (2.09, 1.209999973))
                CenterArc((2.04, 0.9600000373), 0.05, -89.9999914623, 89.9999914623)
                Line((1.79, 0.91), (2.0400000075, 0.9100000373))
                Line((1.79, 0.91), (1.6774823935, 1.21))
                CenterArc((1.5, 1.5), 0.34, -121.4669762933, 62.9339525865)
                Line((1.209999973, 0.91), (1.3225176065, 1.21))
                Line((0.96, 0.91), (1.209999973, 0.91))
                CenterArc((0.96, 0.96), 0.05, 180, 90)
                Line((0.91, 1.21), (0.91, 0.96))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.250000003, 0.200000003), (0.4500000075, 0.200000003))
                CenterArc((0.250000003, 0.250000003), 0.05, 180, 90)
                Line((0.200000003, 0.4500000075), (0.200000003, 0.250000003))
                CenterArc((0.250000003, 0.4500000075), 0.05, 90, 90)
                Line((0.5000000075, 0.5000000075), (0.250000003, 0.5000000075))
                Line((0.5000000075, 0.250000003), (0.5000000075, 0.5000000075))
                CenterArc((0.4500000075, 0.250000003), 0.05, -90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.5000000075, 2.5000000373), (0.25, 2.5000000373))
                CenterArc((0.25, 2.5500000373), 0.05, 180, 90)
                Line((0.2, 2.5500000373), (0.2, 2.75))
                CenterArc((0.25, 2.75), 0.05, 90, 90)
                Line((0.25, 2.8), (0.4500000075, 2.8))
                CenterArc((0.4500000075, 2.75), 0.05, 0, 90)
                Line((0.5000000075, 2.75), (0.5000000075, 2.5000000373))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.5000000373, 2.5000000373), (2.75, 2.5000000373))
                Line((2.5000000373, 2.75), (2.5000000373, 2.5000000373))
                CenterArc((2.5500000373, 2.75), 0.05, 90, 90)
                Line((2.75, 2.8), (2.5500000373, 2.8))
                CenterArc((2.75, 2.75), 0.05, 0, 90)
                Line((2.8, 2.5500000373), (2.8, 2.75))
                CenterArc((2.75, 2.5500000373), 0.05, -90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.5000000373, 0.394999997), (2.75, 0.394999997))
                CenterArc((2.75, 0.344999997), 0.05, 0, 90)
                Line((2.8, 0.344999997), (2.8, 0.1449999896))
                CenterArc((2.75, 0.1449999896), 0.05, -90, 90)
                Line((2.75, 0.0949999896), (2.5500000373, 0.0949999896))
                CenterArc((2.5500000373, 0.1449999896), 0.05, 180, 90)
                Line((2.5000000373, 0.1449999896), (2.5000000373, 0.394999997))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_125152_65ed33fd_0000():
    """Model: mag glass v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4818581963, perimeter: 49.6371639267
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.2
        extrude(amount=0.6, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.7836242611, perimeter: 24.504422698
            Circle(3.9)
        # Symmetric extrude, full_length=True, total=0.6
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_125220_dd31e7cf_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 121 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9771510275, perimeter: 16.004343758
            with BuildLine():
                Line((0.4148674316, -0.5239524017), (0.4148674316, 2.2737454836))
                CenterArc((0.3148674316, 2.2737454836), 0.1, 0, 90)
                Line((-2.0851325684, 2.3737454836), (0.3148674316, 2.3737454836))
                Line((-2.0851325684, -0.6262545164), (-2.0851325684, 2.3737454836))
                Line((-1.3454046689, -0.6262545164), (-2.0851325684, -0.6262545164))
                Line((-1.3454046689, -0.6262545164), (-1.3454046689, 0.4086358076))
                Line((-1.3454046689, 0.4086358076), (-0.4248604684, 0.4086358076))
                Line((-0.4248604684, 0.4086358076), (-0.4248604684, -0.6262545164))
                Line((0.3148674311, -0.6262545164), (-0.4248604684, -0.6262545164))
                CenterArc((0.3148674311, -0.5262545159), 0.1000000005, -90, 90)
                Line((0.4148674316, -0.5262545159), (0.4148674316, -0.5239524017))
            make_face()
            with BuildLine():
                Line((-1.2954046468, 1.0463617625), (-1.2954046468, 1.7360195288))
                Line((-1.2954046468, 1.7360195288), (-0.4748604906, 1.7360195288))
                Line((-0.4748604906, 1.7360195288), (-0.4748604906, 1.0463617625))
                Line((-0.4748604906, 1.0463617625), (-1.2954046468, 1.0463617625))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 121 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0192416193, perimeter: 16.14420864
            with BuildLine():
                Line((2.9148674316, 0.7074257195), (2.9148674316, 2.2737454836))
                CenterArc((2.8148674316, 2.2737454836), 0.1, 0, 90)
                Line((0.5148674316, 2.3737454836), (2.8148674316, 2.3737454836))
                CenterArc((0.5148674316, 2.2737454836), 0.1, 90, 90)
                Line((0.4148674316, -0.5239524017), (0.4148674316, 2.2737454836))
                CenterArc((0.5148674316, -0.5239524017), 0.1, 180, 90)
                Line((1.2545953311, -0.6239524017), (0.5148674316, -0.6239524017))
                Line((1.2545953311, -0.6239524017), (1.2545953311, 0.4086358076))
                Line((1.2545953311, 0.4086358076), (1.5130283652, 0.4086358076))
                Line((1.5130283652, 0.4086358076), (2.0173257118, -0.6239524017))
                Line((2.7570536113, -0.6239524017), (2.0173257118, -0.6239524017))
                CenterArc((2.7570536113, -0.5239524017), 0.1, -90, 116.0300438665)
                Line((2.846910017, -0.4800681635), (2.3157977355, 0.6074257195))
                Line((2.3157977355, 0.6074257195), (2.8148674316, 0.6074257195))
                CenterArc((2.8148674316, 0.7074257195), 0.1, -90, 90)
            make_face()
            with BuildLine():
                Line((2.0751395141, 1.7360195288), (1.2545953311, 1.7360195288))
                Line((2.0751395141, 1.0463617625), (2.0751395141, 1.7360195288))
                Line((1.2545953311, 1.0463617625), (2.0751395141, 1.0463617625))
                Line((1.2545953311, 1.7360195288), (1.2545953311, 1.0463617625))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 121 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8000040037, perimeter: 14.3059423644
            with BuildLine():
                CenterArc((5.3148674316, 2.2737454836), 0.1, 0, 90)
                Line((3.0148674316, 2.3737454836), (5.3148674316, 2.3737454836))
                CenterArc((3.0148674316, 2.2737454836), 0.1, 90, 90)
                Line((2.9148674316, 0.7074257195), (2.9148674316, 2.2737454836))
                Line((2.9148674316, -0.6262545164), (2.9148674316, 0.7074257195))
                Line((5.3148674316, -0.6262545164), (2.9148674316, -0.6262545164))
                CenterArc((5.3148674316, -0.5262545164), 0.1, -90, 90)
                Line((5.4148674316, -0.5262545164), (5.4148674316, -0.3063905666))
                Line((5.4148674316, 0.0134733831), (5.4148674316, -0.3063905666))
                CenterArc((5.3148674316, 0.0134733831), 0.1, 0, 90)
                Line((5.3148674316, 0.1134733831), (3.6545953311, 0.1134733831))
                Line((3.6545953311, 0.1134733831), (3.6545953311, 1.6412291794))
                Line((3.6545953311, 1.6412291794), (5.3148674316, 1.6412291794))
                CenterArc((5.3148674316, 1.7412291794), 0.1, -90, 90)
                Line((5.4148674316, 2.0074873315), (5.4148674316, 1.7412291794))
                Line((5.4148674316, 2.2737454836), (5.4148674316, 2.0074873315))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 121 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9618762415, perimeter: 16.3340808965
            with BuildLine():
                CenterArc((5.5148674316, 2.2737454836), 0.1, 90, 90)
                Line((5.4148674316, 2.2737454836), (5.4148674316, 2.0074873315))
                Line((5.4148674316, 2.0074873315), (5.4148674316, 1.7412291794))
                Line((5.4148674316, 1.7412291794), (5.4148674316, 1.6340175622))
                Line((5.4148674316, 1.6340175622), (5.4148674316, 0.1668393502))
                Line((5.4148674316, 0.1668393502), (5.4148674316, 0.0134733831))
                Line((5.4148674316, 0.0134733831), (5.4148674316, -0.3063905666))
                Line((5.4148674316, -0.5262545164), (5.4148674316, -0.3063905666))
                CenterArc((5.5148674316, -0.5262545164), 0.1, 180, 90)
                Line((6.2871508805, -0.6262545164), (5.5148674316, -0.6262545164))
                Line((6.2871508805, -0.6262545164), (6.2871508805, 0.4133196111))
                Line((6.2871508805, 0.4133196111), (6.6365031584, 0.4133196111))
                Line((6.6365031584, 0.4133196111), (7.1425839826, -0.6262545164))
                Line((7.9148674316, -0.6262545164), (7.1425839826, -0.6262545164))
                Line((7.9148674316, -0.5761123704), (7.9148674316, -0.6262545164))
                Line((7.9148674316, -0.5761123704), (7.3381912209, 0.6084764145))
                Line((7.3381912209, 0.6084764145), (7.9148674286, 0.6085505966))
                Line((7.9148674316, 2.3737454836), (7.9148674286, 0.6085505966))
                Line((5.5148674316, 2.3737454836), (7.9148674316, 2.3737454836))
            make_face()
            with BuildLine():
                Line((7.0751395096, 1.0448781048), (7.0751395096, 1.7346842369))
                Line((6.2545953535, 1.0448781048), (7.0751395096, 1.0448781048))
                Line((6.2545953535, 1.7346842369), (6.2545953535, 1.0448781048))
                Line((7.0751395096, 1.7346842369), (6.2545953535, 1.7346842369))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_125226_291284e7_0000():
    """Model: piston v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8168141026, perimeter: 16.336281808
            with BuildLine():
                CenterArc((0, 0), 1.3500000015, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # TwoSides offset extrude, full=7.1233747679, trim=0.3
        extrude(amount=7.1233747679, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=0.3, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)
    return part.part


def model_125991_52824da3_0003():
    """Model: Bass Sadle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=0.95
        extrude(amount=0.95, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.32, 0.0001006785)):
                Circle(0.15)
        # Symmetric extrude, each_side=0.55
        extrude(amount=0.55, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_126491_c931419a_0003():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3653544672, perimeter: 2.25
            with BuildLine():
                Line((0.1875, 0.3247595264), (0.375, 0))
                Line((-0.1875, 0.3247595264), (0.1875, 0.3247595264))
                Line((-0.375, 0), (-0.1875, 0.3247595264))
                Line((-0.1875, -0.3247595264), (-0.375, 0))
                Line((0.1875, -0.3247595264), (-0.1875, -0.3247595264))
                Line((0.375, 0), (0.1875, -0.3247595264))
            make_face()
        # OneSide extrude, distance=0.313
        extrude(amount=0.313)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_127646_b88ed13f_0008():
    """Model: Corner 2 .25" v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2745746192, perimeter: 7.2111834824
            with BuildLine():
                Line((0.3175, -1.27), (-0.3175, -1.27))
                Line((0.3175, -0.0000000094), (0.3175, -1.27))
                CenterArc((0, 0), 0.3175, 90, 269.9999983008)
                Line((-1.27, 0.3175), (0, 0.3175))
                Line((-1.27, -0.3175), (-1.27, 0.3175))
                Line((-1.27, -0.3175), (-0.3175, -0.3175))
                Line((-0.3175, -0.3175), (-0.3175, -1.27))
            make_face()
            # Profile area: 0.0216332064, perimeter: 1.1337278526
            with BuildLine():
                Line((0.3175, 0.3175), (0.3175, -0.0000000094))
                Line((0, 0.3175), (0.3175, 0.3175))
                CenterArc((0, 0), 0.3175, -0.0000016992, 90.0000016992)
            make_face()
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with BuildLine():
                CenterArc((0, 0), 0.3175, -0.0000016992, 90.0000016992)
                CenterArc((0, 0), 0.3175, 90, 269.9999983008)
            make_face()
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)

        # Sketch1 -> Extrude1 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with BuildLine():
                CenterArc((0, 0), 0.3175, -0.0000016992, 90.0000016992)
                CenterArc((0, 0), 0.3175, 90, 269.9999983008)
            make_face()
        # OneSide extrude, distance=-0.3937
        extrude(amount=-0.3937, mode=Mode.ADD)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.90725625, perimeter: 3.81
            with BuildLine():
                Line((-0.3175, -1.27), (-1.27, -1.27))
                Line((-0.3175, -0.3175), (-0.3175, -1.27))
                Line((-1.27, -0.3175), (-0.3175, -0.3175))
                Line((-1.27, -1.27), (-1.27, -0.3175))
            make_face()
            # Profile area: 1.2745746192, perimeter: 7.2111834824
            with BuildLine():
                Line((0.3175, -1.27), (-0.3175, -1.27))
                Line((0.3175, -0.0000000094), (0.3175, -1.27))
                CenterArc((0, 0), 0.3175, 90, 269.9999983008)
                Line((-1.27, 0.3175), (0, 0.3175))
                Line((-1.27, -0.3175), (-1.27, 0.3175))
                Line((-1.27, -0.3175), (-0.3175, -0.3175))
                Line((-0.3175, -0.3175), (-0.3175, -1.27))
            make_face()
            # Profile area: 3.93144375, perimeter: 10.16
            with BuildLine():
                Line((-1.27, 0.3175), (0, 0.3175))
                Line((0, 0.3175), (0.3175, 0.3175))
                Line((0.3175, 0.3175), (0.3175, -0.0000000094))
                Line((0.3175, -0.0000000094), (0.3175, -1.27))
                Line((1.27, -1.27), (0.3175, -1.27))
                Line((1.27, 1.27), (1.27, -1.27))
                Line((-1.27, 1.27), (1.27, 1.27))
                Line((-1.27, 0.3175), (-1.27, 1.27))
            make_face()
            # Profile area: 0.0216332064, perimeter: 1.1337278526
            with BuildLine():
                Line((0.3175, 0.3175), (0.3175, -0.0000000094))
                Line((0, 0.3175), (0.3175, 0.3175))
                CenterArc((0, 0), 0.3175, -0.0000016992, 90.0000016992)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_127646_b88ed13f_0014():
    """Model: Corner 2 v1 (9)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-1.27, -0.635), (-0.635, -0.635))
                Line((-0.635, -0.635), (-0.635, 0.635))
                Line((-1.27, 0.635), (-0.635, 0.635))
                Line((-1.27, -0.635), (-1.27, 0.635))
            make_face()
            # Profile area: 1.2962078256, perimeter: 7.074911335
            with BuildLine():
                Line((0.635, 0.635), (0.635, -0.635))
                Line((-0.635, 0.635), (0.635, 0.635))
                Line((-0.635, -0.635), (-0.635, 0.635))
                Line((-0.635, -0.635), (0.635, -0.635))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-0.635, -0.635), (0.635, -0.635))
                Line((-0.635, -0.635), (-0.635, -1.27))
                Line((0.635, -1.27), (-0.635, -1.27))
                Line((0.635, -0.635), (0.635, -1.27))
            make_face()
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)

        # Sketch1 -> Extrude1 (Join)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=-0.3937
        extrude(amount=-0.3937, mode=Mode.ADD)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.403225, perimeter: 2.54
            with BuildLine():
                Line((-1.27, 0.635), (-0.635, 0.635))
                Line((-0.635, 0.635), (-0.635, 1.27))
                Line((-1.27, 1.27), (-0.635, 1.27))
                Line((-1.27, 0.635), (-1.27, 1.27))
            make_face()
            # Profile area: 0.403225, perimeter: 2.54
            with BuildLine():
                Line((0.635, 0.635), (0.635, 1.27))
                Line((0.635, 0.635), (1.27, 0.635))
                Line((1.27, 1.27), (1.27, 0.635))
                Line((0.635, 1.27), (1.27, 1.27))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-1.27, -0.635), (-0.635, -0.635))
                Line((-0.635, -0.635), (-0.635, 0.635))
                Line((-1.27, 0.635), (-0.635, 0.635))
                Line((-1.27, -0.635), (-1.27, 0.635))
            make_face()
            # Profile area: 0.403225, perimeter: 2.54
            with BuildLine():
                Line((-0.635, -0.635), (-0.635, -1.27))
                Line((-1.27, -0.635), (-0.635, -0.635))
                Line((-1.27, -1.27), (-1.27, -0.635))
                Line((-0.635, -1.27), (-1.27, -1.27))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-0.635, 0.635), (-0.635, 1.27))
                Line((-0.635, 0.635), (0.635, 0.635))
                Line((0.635, 0.635), (0.635, 1.27))
                Line((-0.635, 1.27), (0.635, 1.27))
            make_face()
            # Profile area: 1.2962078256, perimeter: 7.074911335
            with BuildLine():
                Line((0.635, 0.635), (0.635, -0.635))
                Line((-0.635, 0.635), (0.635, 0.635))
                Line((-0.635, -0.635), (-0.635, 0.635))
                Line((-0.635, -0.635), (0.635, -0.635))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.403225, perimeter: 2.54
            with BuildLine():
                Line((1.27, -0.635), (1.27, -1.27))
                Line((0.635, -0.635), (1.27, -0.635))
                Line((0.635, -0.635), (0.635, -1.27))
                Line((1.27, -1.27), (0.635, -1.27))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-0.635, -0.635), (0.635, -0.635))
                Line((-0.635, -0.635), (-0.635, -1.27))
                Line((0.635, -1.27), (-0.635, -1.27))
                Line((0.635, -0.635), (0.635, -1.27))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((1.27, 0.635), (1.27, -0.635))
                Line((0.635, 0.635), (1.27, 0.635))
                Line((0.635, 0.635), (0.635, -0.635))
                Line((0.635, -0.635), (1.27, -0.635))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_127646_b88ed13f_0015():
    """Model: 4" wall .25" v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with BuildLine():
                CenterArc((1.27, 0), 0.3175, -90, 180)
                CenterArc((1.27, 0), 0.3175, 90, 180)
            make_face()
        # OneSide extrude, distance=-0.3937
        extrude(amount=-0.3937)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.41935, perimeter: 6.985
            with BuildLine():
                Line((2.54, -0.3175), (2.54, -0.635))
                Line((2.54, -0.3175), (1.27, -0.3175))
                Line((1.27, -0.3175), (0, -0.3175))
                Line((0, -0.635), (0, -0.3175))
                Line((0, -1.27), (0, -0.635))
                Line((2.54, -1.27), (0, -1.27))
                Line((2.54, -0.635), (2.54, -1.27))
            make_face()
            # Profile area: 0.6481039128, perimeter: 4.1724556675
            with BuildLine():
                Line((2.54, 0), (2.54, -0.3175))
                Line((2.54, 0.3175), (2.54, 0))
                Line((1.27, 0.3175), (2.54, 0.3175))
                CenterArc((1.27, 0), 0.3175, -90, 180)
                Line((2.54, -0.3175), (1.27, -0.3175))
            make_face()
            # Profile area: 0.6481039128, perimeter: 4.1724556675
            with BuildLine():
                CenterArc((1.27, 0), 0.3175, 90, 180)
                Line((0, 0.3175), (1.27, 0.3175))
                Line((0, 0), (0, 0.3175))
                Line((0, -0.3175), (0, 0))
                Line((1.27, -0.3175), (0, -0.3175))
            make_face()
            # Profile area: 2.41935, perimeter: 6.985
            with BuildLine():
                Line((0, 0.3175), (1.27, 0.3175))
                Line((1.27, 0.3175), (2.54, 0.3175))
                Line((2.54, 1.27), (2.54, 0.3175))
                Line((0, 1.27), (2.54, 1.27))
                Line((0, 0.3175), (0, 1.27))
            make_face()
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with BuildLine():
                CenterArc((1.27, 0), 0.3175, -90, 180)
                CenterArc((1.27, 0), 0.3175, 90, 180)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6481039128, perimeter: 4.1724556675
            with BuildLine():
                Line((2.54, 0), (2.54, -0.3175))
                Line((2.54, 0.3175), (2.54, 0))
                Line((1.27, 0.3175), (2.54, 0.3175))
                CenterArc((1.27, 0), 0.3175, -90, 180)
                Line((2.54, -0.3175), (1.27, -0.3175))
            make_face()
            # Profile area: 0.6481039128, perimeter: 4.1724556675
            with BuildLine():
                CenterArc((1.27, 0), 0.3175, 90, 180)
                Line((0, 0.3175), (1.27, 0.3175))
                Line((0, 0), (0, 0.3175))
                Line((0, -0.3175), (0, 0))
                Line((1.27, -0.3175), (0, -0.3175))
            make_face()
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with BuildLine():
                CenterArc((1.27, 0), 0.3175, -90, 180)
                CenterArc((1.27, 0), 0.3175, 90, 180)
            make_face()
        # OneSide extrude, distance=3.175
        extrude(amount=3.175, mode=Mode.ADD)
    return part.part


def model_127646_b88ed13f_0017():
    """Model: 3" Wall .5" v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((1.27, -0.635)):
                Circle(0.3175)
        # OneSide extrude, distance=-0.3937
        extrude(amount=-0.3937)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9091078256, perimeter: 9.614911335
            with BuildLine():
                Line((2.54, 0), (2.54, -1.27))
                Line((0, 0), (2.54, 0))
                Line((0, -1.27), (0, 0))
                Line((2.54, -1.27), (0, -1.27))
            make_face()
            with BuildLine():
                CenterArc((1.27, -0.635), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((1.27, -0.635)):
                Circle(0.3175)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6129, perimeter: 6.35
            with BuildLine():
                Line((2.54, 0.635), (2.54, 0))
                Line((0, 0.635), (2.54, 0.635))
                Line((0, 0), (0, 0.635))
                Line((0, 0), (2.54, 0))
            make_face()
            # Profile area: 1.6129, perimeter: 6.35
            with BuildLine():
                Line((2.54, -1.27), (0, -1.27))
                Line((0, -1.905), (0, -1.27))
                Line((2.54, -1.905), (0, -1.905))
                Line((2.54, -1.27), (2.54, -1.905))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_127902_e55aaac6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3101.0497720767, perimeter: 271.307941564
            with BuildLine():
                CenterArc((0, 0), 33.02, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 10.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 324.2927866224, perimeter: 63.8371627209
            Circle(10.16)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


def model_128043_0017e0c6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3117691454, perimeter: 2.0784609691
            with BuildLine():
                Line((0.0896575472, -0.3346065215), (0.3346065215, -0.0896575472))
                Line((0.3346065215, -0.0896575472), (0.2449489743, 0.2449489743))
                Line((0.2449489743, 0.2449489743), (-0.0896575472, 0.3346065215))
                Line((-0.0896575472, 0.3346065215), (-0.3346065215, 0.0896575472))
                Line((-0.3346065215, 0.0896575472), (-0.2449489743, -0.2449489743))
                Line((-0.2449489743, -0.2449489743), (0.0896575472, -0.3346065215))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_128043_13b28efa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=-4.1
        extrude(amount=-4.1, mode=Mode.SUBTRACT)
    return part.part


def model_128043_30303218_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3117691454, perimeter: 2.0784609691
            with BuildLine():
                Line((0.0896575472, -0.3346065215), (0.3346065215, -0.0896575472))
                Line((0.3346065215, -0.0896575472), (0.2449489743, 0.2449489743))
                Line((0.2449489743, 0.2449489743), (-0.0896575472, 0.3346065215))
                Line((-0.0896575472, 0.3346065215), (-0.3346065215, 0.0896575472))
                Line((-0.3346065215, 0.0896575472), (-0.2449489743, -0.2449489743))
                Line((-0.2449489743, -0.2449489743), (0.0896575472, -0.3346065215))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_128043_464a2744_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_128043_726cf3be_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=6.8
        extrude(amount=6.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0053096491, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.ADD)
    return part.part


def model_128043_76778a7f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1385640646, perimeter: 1.3856406461
            with BuildLine():
                Line((-0.0138368368, -0.2305252161), (0.192722275, -0.1272456603))
                Line((0.192722275, -0.1272456603), (0.2065591118, 0.1032795559))
                Line((0.2065591118, 0.1032795559), (0.0138368368, 0.2305252161))
                Line((0.0138368368, 0.2305252161), (-0.192722275, 0.1272456603))
                Line((-0.192722275, 0.1272456603), (-0.2065591118, -0.1032795559))
                Line((-0.2065591118, -0.1032795559), (-0.0138368368, -0.2305252161))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_128043_a1b3b620_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.4207942167, perimeter: 18.2212373908
            Circle(2.9)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.4, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 23.7582944428, perimeter: 17.2787595947
            Circle(2.75)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_128281_be786720_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 30 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 283.6067882977, perimeter: 113.5357968334
            with BuildLine():
                Line((5, 30), (2, 30))
                Line((2, 30), (2, 28.5))
                Line((1, 28.5), (2, 28.5))
                Line((1, 30), (1, 28.5))
                Line((1, 30), (0, 30))
                Line((0, 30), (0, 25.5))
                Line((0, 25.5), (0.8, 24.1143593539))
                Line((0.8, 24.1143593539), (0.8, 3.8))
                Line((0.8, 3.8), (0.8, 0))
                Line((0.8, 0), (4.1, 0))
                Line((4.1, 3.8), (4.1, 0))
                CenterArc((6, 3.8), 1.9, 90, 90)
                CenterArc((6, 3.8), 1.9, 0, 90)
                Line((7.9, 3.8), (7.9, 0))
                Line((7.9, 0), (11.2, 0))
                Line((11.2, 24.1143593539), (11.2, 0))
                Line((12, 25.5), (11.2, 24.1143593539))
                Line((12, 30), (12, 25.5))
                Line((12, 30), (11, 30))
                Line((11, 30), (11, 28.5))
                Line((10, 28.5), (11, 28.5))
                Line((10, 30), (10, 28.5))
                Line((10, 30), (6.5, 30))
                Line((6.5, 28.5), (6.5, 30))
                Line((5, 28.5), (6.5, 28.5))
                Line((5, 30), (5, 28.5))
            make_face()
            with BuildLine():
                CenterArc((6, 21), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6627687753, perimeter: 6.5569219382
            with BuildLine():
                Line((-2.4, 0), (0, 1.3856406461))
                Line((-2.4, 0), (0, 0))
                Line((0, 0), (0, 1.3856406461))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


def model_128355_739c5ce0_0001():
    """Model: Back Wall"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3800, perimeter: 780
            with BuildLine():
                Line((-100, 10), (-100, 0))
                Line((-100, 0), (280, 0))
                Line((280, 0), (280, 10))
                Line((280, 10), (-100, 10))
            make_face()
        # OneSide extrude, distance=270
        extrude(amount=270)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3800, perimeter: 780
            with BuildLine():
                Line((280, 260), (-100, 260))
                Line((280, 270), (280, 260))
                Line((-100, 270), (280, 270))
                Line((-100, 260), (-100, 270))
            make_face()
        # OneSide extrude, distance=130
        extrude(amount=130, mode=Mode.ADD)
    return part.part


def model_128646_ed76c192_0002():
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
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 92.4078826424, perimeter: 40.9344496215
            with BuildLine():
                CenterArc((0, 0), 5.51492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> 押し出し2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5019680533, perimeter: 2.8122642169
            with BuildLine():
                _nurbs_edge([(5.626935835, -0.3555180511), (5.6291713069, -0.3556581546), (5.6336427392, -0.3558857881), (5.6403513531, -0.3560695192), (5.6492990354, -0.356014496), (5.6604879621, -0.3555353181), (5.6716805398, -0.3547597658), (5.682875928, -0.3538005365), (5.6940731742, -0.3527414651), (5.7052712702, -0.3516149176), (5.7164692095, -0.3504188273), (5.727666045, -0.3491303234), (5.7388609441, -0.3477200538), (5.7500532528, -0.3461675516), (5.7612425322, -0.3444720175), (5.7724284909, -0.3426445187), (5.7836109314, -0.3407029146), (5.7947896946, -0.3386660489), (5.8059645977, -0.3365474955), (5.8171353987, -0.3343519578), (5.8283018253, -0.3320787757), (5.8394635927, -0.3297241095), (5.8506204245, -0.3272834818), (5.8617720751, -0.3247545571), (5.8729183408, -0.3221384893), (5.8840590452, -0.3194384226), (5.8951940299, -0.3166585969), (5.9063231447, -0.3138032884), (5.9174462358, -0.3108756388), (5.928563141, -0.3078771774), (5.9396736949, -0.3048084707), (5.9507777321, -0.3016695147), (5.9618750907, -0.2984601978), (5.972965617, -0.2951808151), (5.9840491661, -0.2918322626), (5.9951256002, -0.2884157649), (6.0061947861, -0.2849327134), (6.0172565937, -0.2813844753), (6.0283108943, -0.2777721806), (6.0393575589, -0.2740966474), (6.0503964597, -0.2703585002), (6.0614274698, -0.2665582426), (6.0724504642, -0.2626963425), (6.0834653198, -0.2587733276), (6.0944719162, -0.2547898216), (6.1054701352, -0.2507464941), (6.1164598609, -0.2466440315), (6.1274409796, -0.2424831019), (6.1384133801, -0.2382643177), (6.1493769532, -0.2339882202), (6.160331591, -0.229655303), (6.1712771855, -0.2252660269), (6.1822136287, -0.2208208371), (6.1931408111, -0.2163201827), (6.2040586219, -0.2117645263), (6.2149669515, -0.2071543301), (6.2258656926, -0.2024900493), (6.2367547426, -0.1977721222), (6.2476340061, -0.1930009612), (6.2585033946, -0.188176949), (6.2693628217, -0.1833004504), (6.2802121982, -0.1783718216), (6.2910514276, -0.1733914204), (6.3018804016, -0.1683596181), (6.3126989971, -0.1632768057), (6.3235070881, -0.1581433745), (6.334304555, -0.1529597019), (6.3450912948, -0.1477261347), (6.355867231, -0.1424429743), (6.3666323229, -0.1371104622), (6.3773865544, -0.1317287828), (6.3859812515, -0.1273842086), (6.3924223905, -0.1241037449), (6.3967143134, -0.1219069797), (6.3988597323, -0.1208061499)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 6.4, -1.0815771293, 2.1631542586)
                _nurbs_edge([(5.626935835, 0.3555180511), (5.6291713069, 0.3556581546), (5.6336427392, 0.3558857881), (5.6403513531, 0.3560695192), (5.6492990354, 0.356014496), (5.6604879621, 0.3555353181), (5.6716805398, 0.3547597658), (5.682875928, 0.3538005365), (5.6940731742, 0.3527414651), (5.7052712702, 0.3516149176), (5.7164692095, 0.3504188273), (5.727666045, 0.3491303234), (5.7388609441, 0.3477200538), (5.7500532528, 0.3461675516), (5.7612425322, 0.3444720175), (5.7724284909, 0.3426445187), (5.7836109314, 0.3407029146), (5.7947896946, 0.3386660489), (5.8059645977, 0.3365474955), (5.8171353987, 0.3343519578), (5.8283018253, 0.3320787757), (5.8394635927, 0.3297241095), (5.8506204245, 0.3272834818), (5.8617720751, 0.3247545571), (5.8729183408, 0.3221384893), (5.8840590452, 0.3194384226), (5.8951940299, 0.3166585969), (5.9063231447, 0.3138032884), (5.9174462358, 0.3108756388), (5.928563141, 0.3078771774), (5.9396736949, 0.3048084707), (5.9507777321, 0.3016695147), (5.9618750907, 0.2984601978), (5.972965617, 0.2951808151), (5.9840491661, 0.2918322626), (5.9951256002, 0.2884157649), (6.0061947861, 0.2849327134), (6.0172565937, 0.2813844753), (6.0283108943, 0.2777721806), (6.0393575589, 0.2740966474), (6.0503964597, 0.2703585002), (6.0614274698, 0.2665582426), (6.0724504642, 0.2626963425), (6.0834653198, 0.2587733276), (6.0944719162, 0.2547898216), (6.1054701352, 0.2507464941), (6.1164598609, 0.2466440315), (6.1274409796, 0.2424831019), (6.1384133801, 0.2382643177), (6.1493769532, 0.2339882202), (6.160331591, 0.229655303), (6.1712771855, 0.2252660269), (6.1822136287, 0.2208208371), (6.1931408111, 0.2163201827), (6.2040586219, 0.2117645263), (6.2149669515, 0.2071543301), (6.2258656926, 0.2024900493), (6.2367547426, 0.1977721222), (6.2476340061, 0.1930009612), (6.2585033946, 0.188176949), (6.2693628217, 0.1833004504), (6.2802121982, 0.1783718216), (6.2910514276, 0.1733914204), (6.3018804016, 0.1683596181), (6.3126989971, 0.1632768057), (6.3235070881, 0.1581433745), (6.334304555, 0.1529597019), (6.3450912948, 0.1477261347), (6.355867231, 0.1424429743), (6.3666323229, 0.1371104622), (6.3773865544, 0.1317287828), (6.3859812515, 0.1273842086), (6.3924223905, 0.1241037449), (6.3967143134, 0.1219069797), (6.3988597323, 0.1208061499)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((5.5029473385, 0.347747332), (5.626935835, 0.3555180511))
                Line((5.5029473385, -0.347747332), (5.5029473385, 0.347747332))
                Line((5.5029473385, -0.347747332), (5.626935835, -0.3555180511))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_128656_22e204c6_0000():
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
            # Profile area: 119.4233682921, perimeter: 61.4804689599
            with BuildLine():
                CenterArc((0, 0), 6.8349205386, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.7819936143, perimeter: 11.9786924549
            with BuildLine():
                _nurbs_edge([(8.3324660864, -1.4473493459), (8.339509338, -1.448572005), (8.3536182837, -1.4507689724), (8.3748490276, -1.4533193915), (8.4032845002, -1.4553073147), (8.4390020301, -1.4558839804), (8.4748420036, -1.455111784), (8.5107538034, -1.4535336293), (8.5466997575, -1.4515244963), (8.5826626319, -1.4492050949), (8.6186380809, -1.4465392294), (8.6546296077, -1.443400782), (8.6906429802, -1.4396466628), (8.7266798304, -1.4352014602), (8.7627357104, -1.4300814004), (8.7988030057, -1.4243525963), (8.834872602, -1.4181060856), (8.8709358954, -1.4114284231), (8.906987065, -1.4043682316), (8.9430230702, -1.3969359615), (8.9790425048, -1.3891202495), (9.0150447979, -1.3808992521), (9.0510293227, -1.3722533191), (9.0869944123, -1.3631790075), (9.1229375155, -1.3536867161), (9.1588556136, -1.3437945641), (9.1947455512, -1.3335235204), (9.2306043911, -1.3228921811), (9.2664297903, -1.3119112565), (9.3022198758, -1.3005853045), (9.3379730733, -1.2889151549), (9.373687953, -1.2769000906), (9.4093630706, -1.2645401042), (9.4449968055, -1.2518381968), (9.4805874183, -1.2387995252), (9.5161331147, -1.2254304546), (9.551632107, -1.2117376485), (9.5870826777, -1.1977271509), (9.6224832423, -1.1834034608), (9.6578323198, -1.1687699232), (9.6931285007, -1.1538291368), (9.7283704169, -1.1385833599), (9.7635567114, -1.1230349124), (9.7986860076, -1.107186597), (9.8337569215, -1.0910415466), (9.8687680759, -1.0746030548), (9.9037181148, -1.0578744122), (9.9386057171, -1.0408587487), (9.9734296134, -1.0235588594), (10.0081885731, -1.0059772658), (10.0428813889, -0.9881163012), (10.0775068633, -0.9699781914), (10.1120637948, -0.9515651335), (10.1465509618, -0.9328793929), (10.1809671371, -0.9139232783), (10.2153111098, -0.8946990899), (10.2495817072, -0.8752090767), (10.2837778128, -0.8554553968), (10.317898397, -0.8354400656), (10.3519424916, -0.8151649765), (10.3859091391, -0.7946319588), (10.4197973462, -0.7738428289), (10.4536060438, -0.7527994376), (10.4873340265, -0.7315037416), (10.5209799733, -0.7099577913), (10.5545425585, -0.6881636296), (10.5880205424, -0.6661232138), (10.6214128645, -0.6438383329), (10.6547187511, -0.6213105214), (10.6879377719, -0.5985409992), (10.7210697352, -0.575530693), (10.7475056368, -0.5569303352), (10.7672933957, -0.5428721718), (10.780467833, -0.5334521254), (10.7870507012, -0.5287301178)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 10.8000008504, -2.806121858, 5.6122437161)
                _nurbs_edge([(8.3324660864, 1.4473493459), (8.339509338, 1.448572005), (8.3536182837, 1.4507689724), (8.3748490276, 1.4533193915), (8.4032845002, 1.4553073147), (8.4390020301, 1.4558839804), (8.4748420036, 1.455111784), (8.5107538034, 1.4535336293), (8.5466997575, 1.4515244963), (8.5826626319, 1.4492050949), (8.6186380809, 1.4465392294), (8.6546296077, 1.443400782), (8.6906429802, 1.4396466628), (8.7266798304, 1.4352014602), (8.7627357104, 1.4300814004), (8.7988030057, 1.4243525963), (8.834872602, 1.4181060856), (8.8709358954, 1.4114284231), (8.906987065, 1.4043682316), (8.9430230702, 1.3969359615), (8.9790425048, 1.3891202495), (9.0150447979, 1.3808992521), (9.0510293227, 1.3722533191), (9.0869944123, 1.3631790075), (9.1229375155, 1.3536867161), (9.1588556136, 1.3437945641), (9.1947455512, 1.3335235204), (9.2306043911, 1.3228921811), (9.2664297903, 1.3119112565), (9.3022198758, 1.3005853045), (9.3379730733, 1.2889151549), (9.373687953, 1.2769000906), (9.4093630706, 1.2645401042), (9.4449968055, 1.2518381968), (9.4805874183, 1.2387995252), (9.5161331147, 1.2254304546), (9.551632107, 1.2117376485), (9.5870826777, 1.1977271509), (9.6224832423, 1.1834034608), (9.6578323198, 1.1687699232), (9.6931285007, 1.1538291368), (9.7283704169, 1.1385833599), (9.7635567114, 1.1230349124), (9.7986860076, 1.107186597), (9.8337569215, 1.0910415466), (9.8687680759, 1.0746030548), (9.9037181148, 1.0578744122), (9.9386057171, 1.0408587487), (9.9734296134, 1.0235588594), (10.0081885731, 1.0059772658), (10.0428813889, 0.9881163012), (10.0775068633, 0.9699781914), (10.1120637948, 0.9515651335), (10.1465509618, 0.9328793929), (10.1809671371, 0.9139232783), (10.2153111098, 0.8946990899), (10.2495817072, 0.8752090767), (10.2837778128, 0.8554553968), (10.317898397, 0.8354400656), (10.3519424916, 0.8151649765), (10.3859091391, 0.7946319588), (10.4197973462, 0.7738428289), (10.4536060438, 0.7527994376), (10.4873340265, 0.7315037416), (10.5209799733, 0.7099577913), (10.5545425585, 0.6881636296), (10.5880205424, 0.6661232138), (10.6214128645, 0.6438383329), (10.6547187511, 0.6213105214), (10.6879377719, 0.5985409992), (10.7210697352, 0.575530693), (10.7475056368, 0.5569303352), (10.7672933957, 0.5428721718), (10.780467833, 0.5334521254), (10.7870507012, 0.5287301178)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((6.7331008485, 1.1697107441), (8.3324660864, 1.4473493459))
                Line((6.7331008485, -1.1697107441), (6.7331008485, 1.1697107441))
                Line((6.7331008485, -1.1697107441), (8.3324660864, -1.4473493459))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)
    return part.part


def model_128656_22e204c6_0002():
    """Model: Spur Gear (60 teeth)"""
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
            # Profile area: 5923.0180209163, perimeter: 276.8391552536
            with BuildLine():
                CenterArc((0, 0), 43.42532, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 11.1815111815, perimeter: 13.5715942241
            with BuildLine():
                Line((42.475821008, 1.7460728569), (42.475821008, -1.7460728569))
                _nurbs_edge([(42.475821008, -1.7460728569), (42.4882213174, -1.7460601628), (42.513021288, -1.7459387334), (42.5502192985, -1.7454684645), (42.5998127541, -1.7442650036), (42.6617978999, -1.7418035435), (42.7237758202, -1.7383977451), (42.7857454264, -1.7340744916), (42.8477048985, -1.7288802774), (42.9096515511, -1.7228850429), (42.9715822342, -1.7161709627), (43.0334936961, -1.708822301), (43.0953829446, -1.7009153289), (43.1572476471, -1.6925071407), (43.2190864009, -1.6836281669), (43.2808984242, -1.674291091), (43.3426833248, -1.6644975924), (43.4044408514, -1.6542455642), (43.4661706244, -1.6435369699), (43.5278719666, -1.6323827493), (43.5895440382, -1.6207988319), (43.6511859186, -1.6088036959), (43.712796704, -1.5964154975), (43.7743756126, -1.5836489699), (43.8359220387, -1.5705138038), (43.8974354903, -1.5570164881), (43.9589155485, -1.5431614647), (44.0203618221, -1.5289524703), (44.0817738973, -1.5143940059), (44.1431513138, -1.4994920484), (44.2044935894, -1.4842533012), (44.2658002338, -1.468684761), (44.3270707672, -1.4527931977), (44.3883047386, -1.4365845848), (44.449501735, -1.4200638633), (44.5106613685, -1.4032352819), (44.5717832695, -1.3861026112), (44.6328670784, -1.3686693929), (44.6939124363, -1.3509392169), (44.7549189814, -1.3329158448), (44.8158863519, -1.3146030759), (44.8768141882, -1.2960046746), (44.9377021355, -1.2771242812), (44.9985498463, -1.2579653161), (45.0593569828, -1.2385309411), (45.1201232148, -1.2188241193), (45.1808482194, -1.1988476538), (45.2415316809, -1.1786042339), (45.3021732901, -1.1580964873), (45.3627727439, -1.1373270084), (45.4233297422, -1.1162983423), (45.4838439853, -1.0950129799), (45.5443151723, -1.0734733503), (45.604742998, -1.0516818164), (45.6651271538, -1.02964067), (45.7254673336, -1.0073521232), (45.7857632394, -0.9848183024), (45.8460145869, -0.9620412444), (45.9062211132, -0.9390228894), (45.9663825781, -0.9157650871), (46.026498747, -0.8922696336), (46.0865693773, -0.8685383052), (46.1465942041, -0.8445728931), (46.2065729246, -0.8203752453), (46.266505191, -0.7959472869), (46.3263906453, -0.7712909329), (46.3862289493, -0.7464080158), (46.4460198153, -0.7213002111), (46.5057630395, -0.6959689623), (46.5654585286, -0.670415415), (46.6251062645, -0.644640435), (46.6727862724, -0.6238437835), (46.7085248199, -0.6081470751), (46.7323409843, -0.5976385199), (46.7442466831, -0.5923732216)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 46.748, -0.7260501811, 1.4521003622)
                _nurbs_edge([(42.475821008, 1.7460728569), (42.4882213174, 1.7460601628), (42.513021288, 1.7459387334), (42.5502192985, 1.7454684645), (42.5998127541, 1.7442650036), (42.6617978999, 1.7418035435), (42.7237758202, 1.7383977451), (42.7857454264, 1.7340744916), (42.8477048985, 1.7288802774), (42.9096515511, 1.7228850429), (42.9715822342, 1.7161709627), (43.0334936961, 1.708822301), (43.0953829446, 1.7009153289), (43.1572476471, 1.6925071407), (43.2190864009, 1.6836281669), (43.2808984242, 1.674291091), (43.3426833248, 1.6644975924), (43.4044408514, 1.6542455642), (43.4661706244, 1.6435369699), (43.5278719666, 1.6323827493), (43.5895440382, 1.6207988319), (43.6511859186, 1.6088036959), (43.712796704, 1.5964154975), (43.7743756126, 1.5836489699), (43.8359220387, 1.5705138038), (43.8974354903, 1.5570164881), (43.9589155485, 1.5431614647), (44.0203618221, 1.5289524703), (44.0817738973, 1.5143940059), (44.1431513138, 1.4994920484), (44.2044935894, 1.4842533012), (44.2658002338, 1.468684761), (44.3270707672, 1.4527931977), (44.3883047386, 1.4365845848), (44.449501735, 1.4200638633), (44.5106613685, 1.4032352819), (44.5717832695, 1.3861026112), (44.6328670784, 1.3686693929), (44.6939124363, 1.3509392169), (44.7549189814, 1.3329158448), (44.8158863519, 1.3146030759), (44.8768141882, 1.2960046746), (44.9377021355, 1.2771242812), (44.9985498463, 1.2579653161), (45.0593569828, 1.2385309411), (45.1201232148, 1.2188241193), (45.1808482194, 1.1988476538), (45.2415316809, 1.1786042339), (45.3021732901, 1.1580964873), (45.3627727439, 1.1373270084), (45.4233297422, 1.1162983423), (45.4838439853, 1.0950129799), (45.5443151723, 1.0734733503), (45.604742998, 1.0516818164), (45.6651271538, 1.02964067), (45.7254673336, 1.0073521232), (45.7857632394, 0.9848183024), (45.8460145869, 0.9620412444), (45.9062211132, 0.9390228894), (45.9663825781, 0.9157650871), (46.026498747, 0.8922696336), (46.0865693773, 0.8685383052), (46.1465942041, 0.8445728931), (46.2065729246, 0.8203752453), (46.266505191, 0.7959472869), (46.3263906453, 0.7712909329), (46.3862289493, 0.7464080158), (46.4460198153, 0.7213002111), (46.5057630395, 0.6959689623), (46.5654585286, 0.670415415), (46.6251062645, 0.644640435), (46.6727862724, 0.6238437835), (46.7085248199, 0.6081470751), (46.7323409843, 0.5976385199), (46.7442466831, 0.5923732216)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)
    return part.part


def model_128656_22e204c6_0005():
    """Model: Spur Gear (36 teeth)"""
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
            # Profile area: 1992.9659628608, perimeter: 162.2941738296
            with BuildLine():
                CenterArc((0, 0), 25.19492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.7620079682, perimeter: 11.0751694121
            with BuildLine():
                _nurbs_edge([(25.3282431733, -1.4843507906), (25.3374452713, -1.4848870421), (25.3558502692, -1.4857519857), (25.3834601717, -1.4864267298), (25.4202780337, -1.4861424034), (25.4663070301, -1.4841695622), (25.5123409316, -1.4810317205), (25.5583773558, -1.4771755008), (25.604413339, -1.4729315452), (25.6504454078, -1.4684260493), (25.6964698912, -1.4636493441), (25.742483217, -1.458509914), (25.7884821973, -1.4528913589), (25.8344643594, -1.4467139604), (25.8804281339, -1.4399759755), (25.9263725569, -1.4327221792), (25.9722970459, -1.4250238269), (26.0182011611, -1.4169555609), (26.0640843405, -1.4085703327), (26.109945756, -1.3998860699), (26.1557844427, -1.3908997306), (26.2015993755, -1.3815959423), (26.247389559, -1.3719570887), (26.2931541293, -1.3619744536), (26.3388923937, -1.3516530351), (26.3846037704, -1.341005579), (26.4302877498, -1.3300490302), (26.4759438506, -1.3188003365), (26.5215715709, -1.3072717607), (26.5671703695, -1.2954692422), (26.6127396893, -1.2833949681), (26.6582789709, -1.2710489342), (26.7037876682, -1.2584307727), (26.7492652675, -1.245541813), (26.7947112923, -1.2323857299), (26.8401252924, -1.2189674697), (26.8855068361, -1.2052926084), (26.930855503, -1.1913665967), (26.9761708747, -1.1771939084), (27.021452532, -1.1627777955), (27.0667000578, -1.148120755), (27.1119130389, -1.1332248176), (27.1570910678, -1.1180918841), (27.2022337462, -1.1027241068), (27.2473406853, -1.0871240108), (27.2924115052, -1.0712942968), (27.3374458343, -1.055237725), (27.3824433088, -1.0389569785), (27.4274035731, -1.0224545108), (27.4723262786, -1.0057324965), (27.5172110803, -0.9887929223), (27.562057634, -0.9716376465), (27.6068655949, -0.9542684677), (27.6516346136, -0.9366872035), (27.6963643377, -0.9188957219), (27.7410544182, -0.9008958896), (27.7857045157, -0.8826895409), (27.8303143062, -0.8642784421), (27.8748834893, -0.8456642522), (27.9194117886, -0.8268485104), (27.9638989335, -0.807832685), (28.0083446441, -0.7886182122), (28.0527486172, -0.7692065371), (28.097110508, -0.7495991631), (28.1414299251, -0.7297976743), (28.1857064679, -0.7098036565), (28.2299397577, -0.6896186354), (28.2741294711, -0.6692440107), (28.3182753748, -0.6486809899), (28.3623773532, -0.6279305323), (28.4064353717, -0.606993364), (28.4416466312, -0.5900946627), (28.4680353166, -0.5773369742), (28.4856189946, -0.5687946774), (28.4944086388, -0.5645142363)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 28.5, -1.1349613534, 2.2699227067)
                _nurbs_edge([(25.3282431733, 1.4843507906), (25.3374452713, 1.4848870421), (25.3558502692, 1.4857519857), (25.3834601717, 1.4864267298), (25.4202780337, 1.4861424034), (25.4663070301, 1.4841695622), (25.5123409316, 1.4810317205), (25.5583773558, 1.4771755008), (25.604413339, 1.4729315452), (25.6504454078, 1.4684260493), (25.6964698912, 1.4636493441), (25.742483217, 1.458509914), (25.7884821973, 1.4528913589), (25.8344643594, 1.4467139604), (25.8804281339, 1.4399759755), (25.9263725569, 1.4327221792), (25.9722970459, 1.4250238269), (26.0182011611, 1.4169555609), (26.0640843405, 1.4085703327), (26.109945756, 1.3998860699), (26.1557844427, 1.3908997306), (26.2015993755, 1.3815959423), (26.247389559, 1.3719570887), (26.2931541293, 1.3619744536), (26.3388923937, 1.3516530351), (26.3846037704, 1.341005579), (26.4302877498, 1.3300490302), (26.4759438506, 1.3188003365), (26.5215715709, 1.3072717607), (26.5671703695, 1.2954692422), (26.6127396893, 1.2833949681), (26.6582789709, 1.2710489342), (26.7037876682, 1.2584307727), (26.7492652675, 1.245541813), (26.7947112923, 1.2323857299), (26.8401252924, 1.2189674697), (26.8855068361, 1.2052926084), (26.930855503, 1.1913665967), (26.9761708747, 1.1771939084), (27.021452532, 1.1627777955), (27.0667000578, 1.148120755), (27.1119130389, 1.1332248176), (27.1570910678, 1.1180918841), (27.2022337462, 1.1027241068), (27.2473406853, 1.0871240108), (27.2924115052, 1.0712942968), (27.3374458343, 1.055237725), (27.3824433088, 1.0389569785), (27.4274035731, 1.0224545108), (27.4723262786, 1.0057324965), (27.5172110803, 0.9887929223), (27.562057634, 0.9716376465), (27.6068655949, 0.9542684677), (27.6516346136, 0.9366872035), (27.6963643377, 0.9188957219), (27.7410544182, 0.9008958896), (27.7857045157, 0.8826895409), (27.8303143062, 0.8642784421), (27.8748834893, 0.8456642522), (27.9194117886, 0.8268485104), (27.9638989335, 0.807832685), (28.0083446441, 0.7886182122), (28.0527486172, 0.7692065371), (28.097110508, 0.7495991631), (28.1414299251, 0.7297976743), (28.1857064679, 0.7098036565), (28.2299397577, 0.6896186354), (28.2741294711, 0.6692440107), (28.3182753748, 0.6486809899), (28.3623773532, 0.6279305323), (28.4064353717, 0.606993364), (28.4416466312, 0.5900946627), (28.4680353166, 0.5773369742), (28.4856189946, 0.5687946774), (28.4944086388, 0.5645142363)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((25.1507669216, 1.4740083754), (25.3282431733, 1.4843507906))
                Line((25.1507669216, -1.4740083754), (25.1507669216, 1.4740083754))
                Line((25.1507669216, -1.4740083754), (25.3282431733, -1.4843507906))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)
    return part.part


def model_128996_5047840e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0225, perimeter: 0.6
            with BuildLine():
                Line((0.075, -0.075), (-0.075, -0.075))
                Line((0.075, 0.075), (0.075, -0.075))
                Line((-0.075, 0.075), (0.075, 0.075))
                Line((-0.075, -0.075), (-0.075, 0.075))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_128996_53a64f7e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1021017612, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_128996_69e2b8a9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433622, perimeter: 5.6548668233
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_128996_94d0d065_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.8920355263, perimeter: 40.2796447372
            with BuildLine():
                Line((4, 0), (4, -8.6))
                Line((0, 0), (4, 0))
                Line((0, -8.6), (0, 0))
                Line((4, -8.6), (0, -8.6))
            make_face()
            with BuildLine():
                CenterArc((1, -0.55), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3, -0.55), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3, -8.05), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, -8.05), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6, -2.05), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6, -3.55), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6, -5.05), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6, -6.55), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, -6.55), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, -5.05), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, -2.05), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, -3.55), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((-2.0483772618, 2.05), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.0483772618, 2.05), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_128996_94eea973_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1354811832, perimeter: 3.6128315516
            with BuildLine():
                CenterArc((0, 0), 0.325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


def model_128996_c40385f3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 256.8, perimeter: 256.8
            with BuildLine():
                Line((-6.5, -2.5), (40.6, -2.5))
                Line((40.6, -2.5), (40.6, -1))
                Line((40.6, -1), (40.6, 18.6))
                Line((40.6, 18.6), (10.6, 18.6))
                Line((10.6, 18.6), (10.6, 17.5))
                Line((10.6, 17.5), (10.6, 8.9))
                Line((-6.5, 8.9), (10.6, 8.9))
                Line((-6.5, -2.5), (-6.5, 8.9))
            make_face()
            with BuildLine():
                Line((-4.5, 6.9), (12.6, 6.9))
                Line((12.6, 16.6), (12.6, 6.9))
                Line((38.6, 16.6), (12.6, 16.6))
                Line((38.6, -0.5), (38.6, 16.6))
                Line((-4.5, -0.5), (38.6, -0.5))
                Line((-4.5, -0.5), (-4.5, 6.9))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((5.3, -7.7)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-11.8, -7.7)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-11.8, 1.3)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((5.3, 1.3)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-25.6, 1.3)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-11.8, -17.4)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-25.6, -17.4)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-39.4, 1.3)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-39.4, -17.4)):
                Circle(0.3)
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)
    return part.part


def model_128996_d4b68e98_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9886725877, perimeter: 9.7132741229
            with BuildLine():
                Line((2.0496673071, -3.8888414147), (1.2496673071, -3.8888414147))
                Line((2.0496673071, -1.0888414147), (2.0496673071, -3.8888414147))
                Line((1.2496673071, -1.0888414147), (2.0496673071, -1.0888414147))
                Line((1.2496673071, -3.8888414147), (1.2496673071, -1.0888414147))
            make_face()
            with BuildLine():
                CenterArc((1.6496673071, -3.4388414147), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6496673071, -1.5388414147), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.6496673071, 2.4888414147)):
                Circle(0.3)
        # OneSide extrude, distance=31.25
        extrude(amount=31.25, mode=Mode.ADD)
    return part.part


def model_128996_dab9e8bf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=13.6
        extrude(amount=13.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_128996_ef7e7c3d_0000():
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

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0053096491, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_128996_f46b97ad_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)
    return part.part


def model_129006_3364d0a7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.7211495699, perimeter: 44.2274680102
            with BuildLine():
                Line((2.286, -0.635), (2.286, 0.635))
                Line((2.286, 0.635), (8.255, 0.635))
                Line((8.255, 0.635), (8.255, 1.905))
                Line((0, 1.905), (8.255, 1.905))
                CenterArc((0, 0), 1.905, 90, 180)
                Line((0, -1.905), (8.255, -1.905))
                Line((8.255, -1.905), (8.255, -0.635))
                Line((2.286, -0.635), (8.255, -0.635))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=3.81
        extrude(amount=1.905, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.905), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-6.35, 0)):
                Circle(0.635)
            # Profile area: 0.7787954301, perimeter: 6.802366615
            with BuildLine():
                Line((-8.255, -1.905), (-6.3500002007, -1.905))
                CenterArc((-6.35, 0), 1.905, 179.9999997907, 89.9999941722)
                Line((-8.255, 0.000000007), (-8.255, -1.905))
            make_face()
            # Profile area: 0.7787954301, perimeter: 6.8023669886
            with BuildLine():
                CenterArc((-6.35, 0), 1.905, 90, 89.9999997907)
                Line((-6.35, 1.905), (-8.255, 1.905))
                Line((-8.255, 1.905), (-8.255, 0.000000007))
            make_face()
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81, mode=Mode.SUBTRACT)
    return part.part


def model_129012_576921da_0000():
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
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 57.3915035088, perimeter: 28.2
            with BuildLine():
                Line((4.7, 0), (2.35, 4.0703193978))
                Line((2.35, 4.0703193978), (-2.35, 4.0703193978))
                Line((-2.35, 4.0703193978), (-4.7, 0))
                Line((-4.7, 0), (-2.35, -4.0703193978))
                Line((-2.35, -4.0703193978), (2.35, -4.0703193978))
                Line((2.35, -4.0703193978), (4.7, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_129092_5eb5a5c6_0000():
    """Model: Spur Gear (50 teeth)"""
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
            # Profile area: 6.2645755377, perimeter: 10.040027466
            with BuildLine():
                CenterArc((0, 0), 1.42292, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.475
        extrude(amount=0.475)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0239203023, perimeter: 0.6324082513
            with BuildLine():
                Line((1.3569006555, 0.0834066666), (1.3569006555, -0.0834066666))
                _nurbs_edge([(1.3569006555, -0.0834066666), (1.3574844496, -0.083412695), (1.3586522086, -0.083419245), (1.3604043592, -0.0834125489), (1.3627415843, -0.0833705683), (1.365664808, -0.0832632018), (1.368589675, -0.0831016492), (1.3715160855, -0.0828873968), (1.3744438696, -0.0826230122), (1.3773727726, -0.082312377), (1.3803024934, -0.081960073), (1.3832327194, -0.0815708172), (1.3861631614, -0.0811488971), (1.3890935913, -0.080697562), (1.3920238714, -0.080218562), (1.3949539245, -0.0797126286), (1.397883712, -0.0791798561), (1.4008132095, -0.0786201056), (1.4037423808, -0.0780334342), (1.4066711597, -0.0774204068), (1.4095994624, -0.0767818822), (1.412527196, -0.0761188735), (1.4154542683, -0.0754323876), (1.4183805974, -0.0747232553), (1.4213061188, -0.0739920215), (1.4242307792, -0.0732390446), (1.4271545325, -0.0724645628), (1.4300773356, -0.0716687689), (1.4329991431, -0.070851891), (1.4359199049, -0.0700142425), (1.4388395683, -0.0691561812), (1.4417580793, -0.0682780843), (1.4446753849, -0.067380319), (1.4475914342, -0.0664632118), (1.4505061803, -0.0655270302), (1.4534195784, -0.0645720019), (1.4563315858, -0.0635983264), (1.4592421605, -0.0626061897), (1.4621512606, -0.0615957792), (1.4650588437, -0.0605672925), (1.4679648675, -0.0595209305), (1.4708692896, -0.0584568926), (1.4737720681, -0.0573753722), (1.4766731616, -0.056276551), (1.4795725296, -0.0551605962), (1.4824701322, -0.0540276638), (1.4853659303, -0.0528779009), (1.4882598854, -0.0517114481), (1.4911519597, -0.0505284429), (1.4940421158, -0.049329021), (1.4969303167, -0.048113316), (1.4998165255, -0.0468814582), (1.5027007049, -0.045633575), (1.5055828172, -0.0443697899), (1.5084628241, -0.0430902222), (1.5113406877, -0.0417949871), (1.5142163705, -0.0404841956), (1.5170898367, -0.0391579535), (1.5199610525, -0.0378163626), (1.5228299866, -0.0364595198), (1.5256966084, -0.0350875194), (1.5285608864, -0.0337004543), (1.5314227867, -0.0322984178), (1.5342822716, -0.0308815052), (1.5371392982, -0.029449815), (1.5399938223, -0.0280034453), (1.5428458017, -0.0265424903), (1.5456951993, -0.025067037), (1.548541987, -0.0235771617), (1.5513861485, -0.0220729276), (1.5542276759, -0.0205543838), (1.5564987891, -0.0193281293), (1.5582009383, -0.0184020246), (1.5593351777, -0.0177817718), (1.5599021657, -0.0174709329)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 1.56, -0.641686954, 1.2833739081)
                _nurbs_edge([(1.3569006555, 0.0834066666), (1.3574844496, 0.083412695), (1.3586522086, 0.083419245), (1.3604043592, 0.0834125489), (1.3627415843, 0.0833705683), (1.365664808, 0.0832632018), (1.368589675, 0.0831016492), (1.3715160855, 0.0828873968), (1.3744438696, 0.0826230122), (1.3773727726, 0.082312377), (1.3803024934, 0.081960073), (1.3832327194, 0.0815708172), (1.3861631614, 0.0811488971), (1.3890935913, 0.080697562), (1.3920238714, 0.080218562), (1.3949539245, 0.0797126286), (1.397883712, 0.0791798561), (1.4008132095, 0.0786201056), (1.4037423808, 0.0780334342), (1.4066711597, 0.0774204068), (1.4095994624, 0.0767818822), (1.412527196, 0.0761188735), (1.4154542683, 0.0754323876), (1.4183805974, 0.0747232553), (1.4213061188, 0.0739920215), (1.4242307792, 0.0732390446), (1.4271545325, 0.0724645628), (1.4300773356, 0.0716687689), (1.4329991431, 0.070851891), (1.4359199049, 0.0700142425), (1.4388395683, 0.0691561812), (1.4417580793, 0.0682780843), (1.4446753849, 0.067380319), (1.4475914342, 0.0664632118), (1.4505061803, 0.0655270302), (1.4534195784, 0.0645720019), (1.4563315858, 0.0635983264), (1.4592421605, 0.0626061897), (1.4621512606, 0.0615957792), (1.4650588437, 0.0605672925), (1.4679648675, 0.0595209305), (1.4708692896, 0.0584568926), (1.4737720681, 0.0573753722), (1.4766731616, 0.056276551), (1.4795725296, 0.0551605962), (1.4824701322, 0.0540276638), (1.4853659303, 0.0528779009), (1.4882598854, 0.0517114481), (1.4911519597, 0.0505284429), (1.4940421158, 0.049329021), (1.4969303167, 0.048113316), (1.4998165255, 0.0468814582), (1.5027007049, 0.045633575), (1.5055828172, 0.0443697899), (1.5084628241, 0.0430902222), (1.5113406877, 0.0417949871), (1.5142163705, 0.0404841956), (1.5170898367, 0.0391579535), (1.5199610525, 0.0378163626), (1.5228299866, 0.0364595198), (1.5256966084, 0.0350875194), (1.5285608864, 0.0337004543), (1.5314227867, 0.0322984178), (1.5342822716, 0.0308815052), (1.5371392982, 0.029449815), (1.5399938223, 0.0280034453), (1.5428458017, 0.0265424903), (1.5456951993, 0.025067037), (1.548541987, 0.0235771617), (1.5513861485, 0.0220729276), (1.5542276759, 0.0205543838), (1.5564987891, 0.0193281293), (1.5582009383, 0.0184020246), (1.5593351777, 0.0177817718), (1.5599021657, 0.0174709329)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.475
        extrude(amount=0.475, mode=Mode.ADD)
    return part.part


def model_129092_5eb5a5c6_0001():
    """Model: Spur Gear (50 teeth) (1)"""
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
            # Profile area: 6.4791382483, perimeter: 10.1895672764
            with BuildLine():
                CenterArc((0, 0), 1.44672, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.475
        extrude(amount=0.475)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0247242902, perimeter: 0.6429483885
            with BuildLine():
                Line((1.3795156664, 0.0847967777), (1.3795156664, -0.0847967777))
                _nurbs_edge([(1.3795156664, -0.0847967777), (1.3801092782, -0.0848029067), (1.3812966739, -0.0848095647), (1.383078284, -0.0848027511), (1.3854547977, -0.0847600547), (1.388427147, -0.0846508648), (1.3914011537, -0.0844865727), (1.3943767162, -0.0842686905), (1.3973536616, -0.0839998308), (1.4003317314, -0.0836839425), (1.4033106191, -0.0833256865), (1.4062900072, -0.0829298605), (1.4092696016, -0.0825008251), (1.4122491708, -0.0820418837), (1.4152285746, -0.0815548147), (1.4182077348, -0.0810403613), (1.4211866123, -0.0804986191), (1.4241651819, -0.0799294467), (1.4271434071, -0.0793329032), (1.4301212204, -0.0787095639), (1.4330985366, -0.0780603031), (1.4360752615, -0.0773861516), (1.4390513011, -0.0766881332), (1.4420265724, -0.0759670928), (1.4450010099, -0.0752235841), (1.4479745594, -0.0744579717), (1.450947174, -0.0736704975), (1.45391881, -0.072861358), (1.4568894214, -0.0720307854), (1.459858957, -0.0711790989), (1.4628273635, -0.0703066624), (1.4657945859, -0.0694138598), (1.4687605704, -0.0685010648), (1.4717252655, -0.0675686093), (1.4746886232, -0.0666167655), (1.4776505984, -0.0656457649), (1.4806111474, -0.0646558107), (1.4835702276, -0.063647092), (1.4865277966, -0.0626197995), (1.4894838114, -0.0615741346), (1.4924382288, -0.0605103015), (1.4953910059, -0.0594285034), (1.4983421001, -0.0583289368), (1.5012914693, -0.0572117867), (1.5042390725, -0.0560772232), (1.5071848692, -0.0549254052), (1.5101288196, -0.0537564822), (1.5130708847, -0.0525705975), (1.5160110261, -0.051367891), (1.5189492058, -0.0501485009), (1.5218853864, -0.0489125629), (1.5248195301, -0.04766021), (1.5277515994, -0.0463915716), (1.5306815558, -0.0451067735), (1.5336093605, -0.0438059371), (1.536534975, -0.0424891799), (1.5394583613, -0.0411566145), (1.5423794831, -0.0398083489), (1.5452983059, -0.0384444866), (1.5482147982, -0.0370651263), (1.5511289287, -0.035670364), (1.5540406656, -0.0342602942), (1.5569499746, -0.0328350119), (1.5598568171, -0.0313946142), (1.5627611498, -0.0299392013), (1.5656629278, -0.0284688733), (1.5685621082, -0.0269837259), (1.5714586534, -0.0254838478), (1.574352535, -0.0239693167), (1.5772437363, -0.0224401967), (1.5801322495, -0.020896538), (1.5824409081, -0.0196500088), (1.584171192, -0.0187085953), (1.585324177, -0.0180780911), (1.5859005351, -0.0177621152)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 1.586, -0.641686954, 1.2833739081)
                _nurbs_edge([(1.3795156664, 0.0847967777), (1.3801092782, 0.0848029067), (1.3812966739, 0.0848095647), (1.383078284, 0.0848027511), (1.3854547977, 0.0847600547), (1.388427147, 0.0846508648), (1.3914011537, 0.0844865727), (1.3943767162, 0.0842686905), (1.3973536616, 0.0839998308), (1.4003317314, 0.0836839425), (1.4033106191, 0.0833256865), (1.4062900072, 0.0829298605), (1.4092696016, 0.0825008251), (1.4122491708, 0.0820418837), (1.4152285746, 0.0815548147), (1.4182077348, 0.0810403613), (1.4211866123, 0.0804986191), (1.4241651819, 0.0799294467), (1.4271434071, 0.0793329032), (1.4301212204, 0.0787095639), (1.4330985366, 0.0780603031), (1.4360752615, 0.0773861516), (1.4390513011, 0.0766881332), (1.4420265724, 0.0759670928), (1.4450010099, 0.0752235841), (1.4479745594, 0.0744579717), (1.450947174, 0.0736704975), (1.45391881, 0.072861358), (1.4568894214, 0.0720307854), (1.459858957, 0.0711790989), (1.4628273635, 0.0703066624), (1.4657945859, 0.0694138598), (1.4687605704, 0.0685010648), (1.4717252655, 0.0675686093), (1.4746886232, 0.0666167655), (1.4776505984, 0.0656457649), (1.4806111474, 0.0646558107), (1.4835702276, 0.063647092), (1.4865277966, 0.0626197995), (1.4894838114, 0.0615741346), (1.4924382288, 0.0605103015), (1.4953910059, 0.0594285034), (1.4983421001, 0.0583289368), (1.5012914693, 0.0572117867), (1.5042390725, 0.0560772232), (1.5071848692, 0.0549254052), (1.5101288196, 0.0537564822), (1.5130708847, 0.0525705975), (1.5160110261, 0.051367891), (1.5189492058, 0.0501485009), (1.5218853864, 0.0489125629), (1.5248195301, 0.04766021), (1.5277515994, 0.0463915716), (1.5306815558, 0.0451067735), (1.5336093605, 0.0438059371), (1.536534975, 0.0424891799), (1.5394583613, 0.0411566145), (1.5423794831, 0.0398083489), (1.5452983059, 0.0384444866), (1.5482147982, 0.0370651263), (1.5511289287, 0.035670364), (1.5540406656, 0.0342602942), (1.5569499746, 0.0328350119), (1.5598568171, 0.0313946142), (1.5627611498, 0.0299392013), (1.5656629278, 0.0284688733), (1.5685621082, 0.0269837259), (1.5714586534, 0.0254838478), (1.574352535, 0.0239693167), (1.5772437363, 0.0224401967), (1.5801322495, 0.020896538), (1.5824409081, 0.0196500088), (1.584171192, 0.0187085953), (1.585324177, 0.0180780911), (1.5859005351, 0.0177621152)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.475
        extrude(amount=0.475, mode=Mode.ADD)
    return part.part


def model_129092_5eb5a5c6_0003():
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
            # Profile area: 0.2604068865, perimeter: 3.2164882225
            with BuildLine():
                CenterArc((0, 0), 0.33692, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0255410309, perimeter: 0.6129501364
            with BuildLine():
                _nurbs_edge([(0.4007242384, -0.0758441181), (0.4011092631, -0.0759159775), (0.4018809525, -0.0760456914), (0.4030434063, -0.0761982479), (0.4046027936, -0.0763216988), (0.4065654812, -0.0763663509), (0.4085386555, -0.0763313193), (0.4105193012, -0.0762461616), (0.4125050259, -0.07613267), (0.4144945981, -0.0759990547), (0.4164875716, -0.0758445359), (0.4184840007, -0.0756629278), (0.4204841339, -0.075446425), (0.4224880858, -0.0751897138), (0.4244956177, -0.0748926515), (0.42650629, -0.0745581604), (0.428519553, -0.0741909025), (0.4305348548, -0.0737957462), (0.4325517587, -0.0733760919), (0.4345700013, -0.0729330281), (0.4365894256, -0.0724662674), (0.4386099386, -0.0719747192), (0.4406314629, -0.0714571578), (0.442653883, -0.0709129666), (0.4446770232, -0.0703424347), (0.4467006753, -0.0697463614), (0.4487246154, -0.0691258204), (0.4507486232, -0.0684818818), (0.4527725038, -0.0678152997), (0.4547960947, -0.0671264138), (0.4568192532, -0.0664153198), (0.4588418488, -0.0656819726), (0.4608637547, -0.0649263074), (0.4628848374, -0.064148377), (0.4649049542, -0.0633483895), (0.4669239577, -0.0625266379), (0.4689416997, -0.0616834571), (0.4709580338, -0.060819174), (0.4729728199, -0.0599340508), (0.4749859253, -0.0590282709), (0.4769972216, -0.0581019695), (0.4790065837, -0.0571552528), (0.481013888, -0.0561882201), (0.4830190098, -0.0552009894), (0.4850218235, -0.0541937041), (0.4870222035, -0.0531665205), (0.4890200252, -0.0521195996), (0.4910151658, -0.0510530985), (0.4930075056, -0.04996716), (0.4949969281, -0.0488619097), (0.4969833183, -0.0477374623), (0.4989665618, -0.0465939247), (0.5009465438, -0.0454314009), (0.5029231472, -0.0442499975), (0.5048962533, -0.0430498247), (0.5068657438, -0.0418309941), (0.5088315028, -0.0405936157), (0.5107934187, -0.0393377965), (0.5127513869, -0.0380636378), (0.5147053098, -0.0367712344), (0.5166550913, -0.0354606775), (0.5186006326, -0.0341320568), (0.5205418281, -0.0327854628), (0.5224785598, -0.0314209897), (0.5244106958, -0.0300387369), (0.5263381014, -0.0286388044), (0.5282606484, -0.0272212896), (0.5301782243, -0.0257862835), (0.5320907425, -0.0243338679), (0.5339981506, -0.0228641114), (0.5359004209, -0.0213770693), (0.5374181191, -0.0201736396), (0.5385540765, -0.0192633182), (0.5393103522, -0.0186529944), (0.5396882328, -0.0183469718)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.54, -1.9470488929, 3.8940977857)
                _nurbs_edge([(0.4007242384, 0.0758441181), (0.4011092631, 0.0759159775), (0.4018809525, 0.0760456914), (0.4030434063, 0.0761982479), (0.4046027936, 0.0763216988), (0.4065654812, 0.0763663509), (0.4085386555, 0.0763313193), (0.4105193012, 0.0762461616), (0.4125050259, 0.07613267), (0.4144945981, 0.0759990547), (0.4164875716, 0.0758445359), (0.4184840007, 0.0756629278), (0.4204841339, 0.075446425), (0.4224880858, 0.0751897138), (0.4244956177, 0.0748926515), (0.42650629, 0.0745581604), (0.428519553, 0.0741909025), (0.4305348548, 0.0737957462), (0.4325517587, 0.0733760919), (0.4345700013, 0.0729330281), (0.4365894256, 0.0724662674), (0.4386099386, 0.0719747192), (0.4406314629, 0.0714571578), (0.442653883, 0.0709129666), (0.4446770232, 0.0703424347), (0.4467006753, 0.0697463614), (0.4487246154, 0.0691258204), (0.4507486232, 0.0684818818), (0.4527725038, 0.0678152997), (0.4547960947, 0.0671264138), (0.4568192532, 0.0664153198), (0.4588418488, 0.0656819726), (0.4608637547, 0.0649263074), (0.4628848374, 0.064148377), (0.4649049542, 0.0633483895), (0.4669239577, 0.0625266379), (0.4689416997, 0.0616834571), (0.4709580338, 0.060819174), (0.4729728199, 0.0599340508), (0.4749859253, 0.0590282709), (0.4769972216, 0.0581019695), (0.4790065837, 0.0571552528), (0.481013888, 0.0561882201), (0.4830190098, 0.0552009894), (0.4850218235, 0.0541937041), (0.4870222035, 0.0531665205), (0.4890200252, 0.0521195996), (0.4910151658, 0.0510530985), (0.4930075056, 0.04996716), (0.4949969281, 0.0488619097), (0.4969833183, 0.0477374623), (0.4989665618, 0.0465939247), (0.5009465438, 0.0454314009), (0.5029231472, 0.0442499975), (0.5048962533, 0.0430498247), (0.5068657438, 0.0418309941), (0.5088315028, 0.0405936157), (0.5107934187, 0.0393377965), (0.5127513869, 0.0380636378), (0.5147053098, 0.0367712344), (0.5166550913, 0.0354606775), (0.5186006326, 0.0341320568), (0.5205418281, 0.0327854628), (0.5224785598, 0.0314209897), (0.5244106958, 0.0300387369), (0.5263381014, 0.0286388044), (0.5282606484, 0.0272212896), (0.5301782243, 0.0257862835), (0.5320907425, 0.0243338679), (0.5339981506, 0.0228641114), (0.5359004209, 0.0213770693), (0.5374181191, 0.0201736396), (0.5385540765, 0.0192633182), (0.5393103522, 0.0186529944), (0.5396882328, 0.0183469718)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.3300602684, 0.0626556836), (0.4007242384, 0.0758441181))
                Line((0.3300602684, -0.0626556836), (0.3300602684, 0.0626556836))
                Line((0.3300602684, -0.0626556836), (0.4007242384, -0.0758441181))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


def model_129401_7686af57_0001():
    """Model: Spur Gear (24 teeth)"""
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
            # Profile area: 589.3191207328, perimeter: 90.138073762
            with BuildLine():
                CenterArc((0, 0), 13.71092, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3689851757, perimeter: 9.0447675342
            with BuildLine():
                _nurbs_edge([(14.2747067512, -1.1495081959), (14.281176463, -1.1500283337), (14.2941191705, -1.1509045973), (14.3135430839, -1.1517269639), (14.339460457, -1.1518883985), (14.3718832413, -1.150815655), (14.4043250313, -1.148828396), (14.4367782935, -1.1462809582), (14.4692364132, -1.1434326116), (14.5016947987, -1.1403794607), (14.534150309, -1.1371107601), (14.566600868, -1.133551871), (14.5990450265, -1.1296098723), (14.6314815052, -1.1252236685), (14.6639088835, -1.1203940693), (14.6963257205, -1.115157973), (14.7287305965, -1.1095725211), (14.7611221808, -1.1036966236), (14.7934993009, -1.0975705272), (14.825860968, -1.0912069795), (14.8582063226, -1.0846025675), (14.8905345976, -1.0777445901), (14.9228450767, -1.0706190912), (14.9551370493, -1.0632199174), (14.9874097924, -1.0555515693), (15.0196625887, -1.0476244734), (15.0518947352, -1.0394521371), (15.0841055553, -1.0310478206), (15.1162944117, -1.0224207387), (15.1484607079, -1.0135752304), (15.1806038781, -1.0045127663), (15.2127233801, -0.9952332067), (15.2448186879, -0.9857362457), (15.2768892826, -0.9760230754), (15.308934651, -0.9660966816), (15.3409542876, -0.9559610162), (15.3729476967, -0.9456204767), (15.4049143942, -0.9350793122), (15.4368539102, -0.9243409375), (15.468765789, -0.9134078313), (15.5006495856, -0.9022818961), (15.5325048641, -0.8909646907), (15.5643311953, -0.8794576953), (15.5961281547, -0.867762618), (15.6278953223, -0.8558814506), (15.6596322838, -0.8438163177), (15.6913386323, -0.8315693826), (15.7230139694, -0.8191427402), (15.7546579074, -0.8065382947), (15.7862700685, -0.7937577358), (15.8178500804, -0.7808026097), (15.8493975729, -0.7676743661), (15.8809121749, -0.7543744126), (15.9123935105, -0.7409041776), (15.9438412, -0.7272651278), (15.9752548674, -0.7134587283), (16.0066341469, -0.6994864172), (16.0379786891, -0.6853495787), (16.0692881701, -0.6710495112), (16.1005622902, -0.6565874216), (16.1318007552, -0.6419644632), (16.1630032616, -0.6271817665), (16.1941694813, -0.6122404707), (16.2252990433, -0.5971417633), (16.2563915303, -0.5818868936), (16.2874465168, -0.5664771106), (16.3184636013, -0.5509136156), (16.3494424392, -0.5351975103), (16.3803827792, -0.5193297461), (16.4112844895, -0.5033110813), (16.4421475214, -0.487142092), (16.4668070082, -0.4740869614), (16.4852842325, -0.4642282525), (16.4975946554, -0.4576258516), (16.5037479352, -0.4543171691)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 16.51, -1.576846918, 3.1536938361)
                _nurbs_edge([(14.2747067512, 1.1495081959), (14.281176463, 1.1500283337), (14.2941191705, 1.1509045973), (14.3135430839, 1.1517269639), (14.339460457, 1.1518883985), (14.3718832413, 1.150815655), (14.4043250313, 1.148828396), (14.4367782935, 1.1462809582), (14.4692364132, 1.1434326116), (14.5016947987, 1.1403794607), (14.534150309, 1.1371107601), (14.566600868, 1.133551871), (14.5990450265, 1.1296098723), (14.6314815052, 1.1252236685), (14.6639088835, 1.1203940693), (14.6963257205, 1.115157973), (14.7287305965, 1.1095725211), (14.7611221808, 1.1036966236), (14.7934993009, 1.0975705272), (14.825860968, 1.0912069795), (14.8582063226, 1.0846025675), (14.8905345976, 1.0777445901), (14.9228450767, 1.0706190912), (14.9551370493, 1.0632199174), (14.9874097924, 1.0555515693), (15.0196625887, 1.0476244734), (15.0518947352, 1.0394521371), (15.0841055553, 1.0310478206), (15.1162944117, 1.0224207387), (15.1484607079, 1.0135752304), (15.1806038781, 1.0045127663), (15.2127233801, 0.9952332067), (15.2448186879, 0.9857362457), (15.2768892826, 0.9760230754), (15.308934651, 0.9660966816), (15.3409542876, 0.9559610162), (15.3729476967, 0.9456204767), (15.4049143942, 0.9350793122), (15.4368539102, 0.9243409375), (15.468765789, 0.9134078313), (15.5006495856, 0.9022818961), (15.5325048641, 0.8909646907), (15.5643311953, 0.8794576953), (15.5961281547, 0.867762618), (15.6278953223, 0.8558814506), (15.6596322838, 0.8438163177), (15.6913386323, 0.8315693826), (15.7230139694, 0.8191427402), (15.7546579074, 0.8065382947), (15.7862700685, 0.7937577358), (15.8178500804, 0.7808026097), (15.8493975729, 0.7676743661), (15.8809121749, 0.7543744126), (15.9123935105, 0.7409041776), (15.9438412, 0.7272651278), (15.9752548674, 0.7134587283), (16.0066341469, 0.6994864172), (16.0379786891, 0.6853495787), (16.0692881701, 0.6710495112), (16.1005622902, 0.6565874216), (16.1318007552, 0.6419644632), (16.1630032616, 0.6271817665), (16.1941694813, 0.6122404707), (16.2252990433, 0.5971417633), (16.2563915303, 0.5818868936), (16.2874465168, 0.5664771106), (16.3184636013, 0.5509136156), (16.3494424392, 0.5351975103), (16.3803827792, 0.5193297461), (16.4112844895, 0.5033110813), (16.4421475214, 0.487142092), (16.4668070082, 0.4740869614), (16.4852842325, 0.4642282525), (16.4975946554, 0.4576258516), (16.5037479352, 0.4543171691)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((13.6656826881, 1.1005452038), (14.2747067512, 1.1495081959))
                Line((13.6656826881, -1.1005452038), (13.6656826881, 1.1005452038))
                Line((13.6656826881, -1.1005452038), (14.2747067512, -1.1495081959))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_129409_0664bc6f_0000():
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
        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.2651600979, perimeter: 18.0342453874
            with BuildLine():
                Line((0, 0), (6, 0))
                Line((0, -2.5), (0, 0))
                Line((6, -2.5), (0, -2.5))
                _nurbs_edge([(6, 0), (6.1107648633, -0.0158235499), (6.3160425108, -0.0518963501), (6.5752031711, -0.119282924), (6.8263910354, -0.2330995849), (7.0018129442, -0.4008303611), (7.0639359878, -0.5760061469), (7.0406855927, -0.7417333363), (6.959365462, -0.8862281921), (6.8428830271, -1.0085737636), (6.7088321965, -1.1180451646), (6.5705561254, -1.2286585143), (6.4375949744, -1.3556733825), (6.3162476684, -1.5105859293), (6.2101571002, -1.6995839842), (6.1211032769, -1.9256360648), (6.0639287629, -2.1366930321), (6.0289237939, -2.3118403561), (6.0090620989, -2.4360408073), (6, -2.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_129418_723e4053_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.7853982379, perimeter: 11.1415926983
            with BuildLine():
                CenterArc((-0.5000000149, 0.0000000075), 0.5, 90, 90)
                Line((-1.0000000149, 0.0000000075), (-1.0000000149, -3))
                CenterArc((-0.5000000149, -3), 0.5, 180, 90)
                Line((0.5, -3.5), (-0.5000000149, -3.5))
                CenterArc((0.5, -3), 0.5, -90, 90)
                Line((1, 0.0000000075), (1, -3))
                CenterArc((0.5, 0.0000000075), 0.5, 0, 90)
                Line((-0.5000000149, 0.5000000075), (0.5, 0.5000000075))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_129618_2962c248_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 26 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.34116577, perimeter: 19.6095089772
            with BuildLine():
                Line((1.1928097986, -3.9411780519), (0.9160785465, -4.563823369))
                CenterArc((1.0120287591, -4.606467908), 0.105, 156.0375110254, 41.3165136108)
                Line((0.9118083614, -4.6377867822), (0.9250958345, -4.680306696))
                CenterArc((1.0253162322, -4.6489878217), 0.105, -162.6459753637, 90)
                Line((1.0566351065, -4.7492082194), (3.6937921577, -3.9250966409))
                CenterArc((3.6192234094, -3.6864766463), 0.25, -72.6459753637, 93.0115861221)
                Line((3.8535961683, -3.5994742907), (3.4037781064, -2.3877243407))
                CenterArc((-4.0961501776, -5.1717997229), 8, 20.3656107584, 16.5042868875)
                Line((2.3038498224, -0.3717997229), (2.2300000313, -0.2733333348))
                CenterArc((2.7500000313, 0.1166666652), 0.65, 180, 36.8698976458)
                Line((2.1000000313, 0.1166666652), (2.1000000313, 0.2500000134))
                CenterArc((2.7500000313, 0.2500000134), 0.65, 90, 90)
                Line((2.7500000313, 0.9000000134), (2.8000000417, 0.9000000134))
                Line((2.8000000417, 0.9000000134), (2.8000000417, 1.5000000224))
                Line((2.8000000417, 1.5000000224), (2.7000000402, 1.5000000224))
                Line((2.7000000402, 1.5000000224), (-0.5000000075, 1.5000000224))
                Line((-0.5000000075, 1.5000000224), (-0.5000000075, -0.5000000075))
                Line((-0.5000000075, -0.5000000075), (-0.2881527262, -0.5000000075))
                CenterArc((-0.2881527262, -1.3000000075), 0.8, 17.3540246363, 72.6459753637)
                Line((0.4754312562, -1.0613800129), (1.2212776992, -3.4480886305))
                CenterArc((0.5531417145, -3.6568811257), 0.7, -23.9624889746, 41.3165136108)
            make_face()
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True)
    return part.part


def model_129935_8a7613e5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.9486725877, perimeter: 34.9132741229
            with BuildLine():
                Line((10.2, -6), (0, -6))
                Line((10.2, 0), (10.2, -6))
                Line((0, 0), (10.2, 0))
                Line((0, -6), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((9.7, -5), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, -0.25), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-2.5, 0.7)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-7.7, 2.2)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-7.7, 4.95)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-2.5, 5.5)):
                Circle(0.2)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_130109_be1c92dd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5223645744, perimeter: 12.3684505318
            with BuildLine():
                CenterArc((-3.048, 0), 1.2700000405, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.048, -0.8890000284), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.6830000203, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.048, 0.7620000243), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.205672345, perimeter: 13.5653975111
            with BuildLine():
                CenterArc((0, 0), 1.2700000405, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -0.8890000284), 0.2540000081, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.7620000243), 0.2540000081, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.6350000203, 0), 0.3810000122, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4560367603, perimeter: 2.3938936784
            with Locations((-0.6350000203, 0)):
                Circle(0.3810000122)
            # Profile area: 0.2026830046, perimeter: 1.595929119
            with Locations((0, 0.7620000243)):
                Circle(0.2540000081)
            # Profile area: 0.2026830046, perimeter: 1.595929119
            with Locations((0, -0.8890000284)):
                Circle(0.2540000081)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-3.6830000203, 0)):
                Circle(0.3175)
            # Profile area: 0.1140091828, perimeter: 1.196946801
            with Locations((-3.048, 0.7620000243)):
                Circle(0.1905)
            # Profile area: 0.1140091828, perimeter: 1.196946801
            with Locations((-3.048, -0.8890000284)):
                Circle(0.1905)
        # OneSide extrude, distance=1.4605
        extrude(amount=1.4605, mode=Mode.ADD)
    return part.part


def model_130569_ef78205f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 37.5, perimeter: 25
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 5))
                Line((7.5, 5), (0, 5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((4.5, 5), (4.5, 0))
                Line((3, 5), (4.5, 5))
                Line((3, 0), (3, 5))
                Line((4.5, 0), (3, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_130656_cd404fec_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=17
        extrude(amount=17)
    return part.part


def model_130724_ac486cd1_0000():
    """Model: Front Left"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 24 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 499.6820622719, perimeter: 238.7041598634
            with BuildLine():
                Line((-26, 39.5035845403), (-26, 0))
                Line((-3.1305883671, 0), (-26, 0))
                Line((-3.1305883671, 0), (0, 0))
                Line((0, 39.5035845403), (0, 0))
                Line((-3.1305594424, 39.5035845403), (0, 39.5035845403))
                Line((-26, 39.5035845403), (-3.1305594424, 39.5035845403))
            make_face()
            with BuildLine():
                Line((-4.0329814237, 24.6082109577), (-4.0329814237, 30.5556129181))
                Line((-4.0329814237, 24.6082109577), (-4.0329814237, 22.192268066))
                Line((-4.0329814237, 4.6842335658), (-4.0329814237, 22.192268066))
                CenterArc((-6.4079814237, 4.6842335658), 2.375, -110.6028568661, 110.6028568661)
                Line((-7.2437161872, 2.4611338368), (-19.0996138117, 6.9181474692))
                CenterArc((-18.596413512, 8.2566875166), 1.43, -171.1789505037, 60.5760936376)
                Line((-21.4654838065, 17.4196837414), (-20.0094996298, 8.0373986121))
                Line((-21.4654838065, 17.4196837414), (-22.1086423349, 22.1154780441))
                Line((-22.1086423349, 22.1154780441), (-23.9609446689, 36.2975644654))
                CenterArc((-22.54298771, 36.4827618269), 1.43, 39.0700802862, 148.3711193981)
                Line((-21.4327705469, 37.3840486017), (-17.0261523271, 31.955917051))
                Line((-17.0261523271, 31.955917051), (-13.1991649752, 30.6072772209))
                Line((-14.1743206945, 35.8326162327), (-13.1991649752, 30.6072772209))
                CenterArc((-12.7685900503, 36.09495448), 1.43, 40.8884976473, 149.6824732665)
                Line((-8.5411059222, 33.3972098096), (-11.6875316495, 37.0310168357))
                Line((-7.1525389939, 31.9856129181), (-8.5411059222, 33.3972098096))
                Line((-5.4629814237, 31.9856129181), (-7.1525389939, 31.9856129181))
                CenterArc((-5.4629814237, 30.5556129181), 1.43, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 42.686754139, perimeter: 213.3525168677
            with BuildLine():
                CenterArc((-5.4629814237, 30.5556129181), 1.43, 0, 90)
                Line((-5.4629814237, 31.9856129181), (-7.1525389939, 31.9856129181))
                Line((-7.1525389939, 31.9856129181), (-8.5411059222, 33.3972098096))
                Line((-8.5411059222, 33.3972098096), (-11.6875316495, 37.0310168357))
                CenterArc((-12.7685900503, 36.09495448), 1.43, 40.8884976473, 149.6824732665)
                Line((-14.1743206945, 35.8326162327), (-13.1991649752, 30.6072772209))
                Line((-17.0261523271, 31.955917051), (-13.1991649752, 30.6072772209))
                Line((-21.4327705469, 37.3840486017), (-17.0261523271, 31.955917051))
                CenterArc((-22.54298771, 36.4827618269), 1.43, 39.0700802862, 148.3711193981)
                Line((-22.1086423349, 22.1154780441), (-23.9609446689, 36.2975644654))
                Line((-21.4654838065, 17.4196837414), (-22.1086423349, 22.1154780441))
                Line((-21.4654838065, 17.4196837414), (-20.0094996298, 8.0373986121))
                CenterArc((-18.596413512, 8.2566875166), 1.43, -171.1789505037, 60.5760936376)
                Line((-7.2437161872, 2.4611338368), (-19.0996138117, 6.9181474692))
                CenterArc((-6.4079814237, 4.6842335658), 2.375, -110.6028568661, 110.6028568661)
                Line((-4.0329814237, 4.6842335658), (-4.0329814237, 22.192268066))
                Line((-4.0329814237, 24.6082109577), (-4.0329814237, 22.192268066))
                Line((-4.0329814237, 24.6082109577), (-4.0329814237, 30.5556129181))
            make_face()
            with BuildLine():
                Line((-7.1029608586, 2.8355506333), (-18.9588584831, 7.2925642657))
                CenterArc((-18.596413512, 8.2566875166), 1.03, -171.1789505037, 60.5760936376)
                Line((-21.069667845, 17.4774976996), (-19.6142307857, 8.0987381658))
                Line((-21.069667845, 17.4774976996), (-21.7121727596, 22.1685198723))
                Line((-21.7121727596, 22.1685198723), (-23.5643133518, 36.3493679232))
                CenterArc((-22.54298771, 36.4827618269), 1.03, 39.0700802862, 148.3711193981)
                Line((-21.7433208023, 37.131940413), (-17.2655595448, 31.6161739121))
                Line((-17.2655595448, 31.6161739121), (-12.7972910688, 30.0415450241))
                CenterArc((-12.7731943681, 30.1099233761), 0.0725, -109.4125840017, 119.9835549156)
                Line((-13.7811093255, 35.9059975606), (-12.7019248074, 30.1232237418))
                CenterArc((-12.7685900503, 36.09495448), 1.03, 40.8884976473, 149.6824732665)
                Line((-8.8351792269, 33.1257646629), (-11.9899256078, 36.7691812117))
                Line((-7.3201547959, 31.5856129181), (-8.8351792269, 33.1257646629))
                Line((-5.4629814237, 31.5856129181), (-7.3201547959, 31.5856129181))
                CenterArc((-5.4629814237, 30.5556129181), 1.03, 0, 90)
                Line((-4.4329814237, 24.6082109577), (-4.4329814237, 30.5556129181))
                Line((-4.4329814237, 24.6082109577), (-4.4329814237, 22.192268066))
                Line((-4.4329814237, 4.6842335658), (-4.4329814237, 22.192268066))
                CenterArc((-6.4079814237, 4.6842335658), 1.975, -110.6028568661, 110.6028568661)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 274.0936122798, perimeter: 308.0887204069
            with BuildLine():
                CenterArc((-6.4079814237, 4.6842335658), 1.975, -110.6028568661, 110.6028568661)
                Line((-4.4329814237, 4.6842335658), (-4.4329814237, 22.192268066))
                Line((-4.4329814237, 24.6082109577), (-4.4329814237, 22.192268066))
                Line((-4.4329814237, 24.6082109577), (-4.4329814237, 30.5556129181))
                CenterArc((-5.4629814237, 30.5556129181), 1.03, 0, 90)
                Line((-5.4629814237, 31.5856129181), (-7.3201547959, 31.5856129181))
                Line((-7.3201547959, 31.5856129181), (-8.8351792269, 33.1257646629))
                Line((-8.8351792269, 33.1257646629), (-11.9899256078, 36.7691812117))
                CenterArc((-12.7685900503, 36.09495448), 1.03, 40.8884976473, 149.6824732665)
                Line((-13.7811093255, 35.9059975606), (-12.7019248074, 30.1232237418))
                CenterArc((-12.7731943681, 30.1099233761), 0.0725, -109.4125840017, 119.9835549156)
                Line((-17.2655595448, 31.6161739121), (-12.7972910688, 30.0415450241))
                Line((-21.7433208023, 37.131940413), (-17.2655595448, 31.6161739121))
                CenterArc((-22.54298771, 36.4827618269), 1.03, 39.0700802862, 148.3711193981)
                Line((-21.7121727596, 22.1685198723), (-23.5643133518, 36.3493679232))
                Line((-21.069667845, 17.4774976996), (-21.7121727596, 22.1685198723))
                Line((-21.069667845, 17.4774976996), (-19.6142307857, 8.0987381658))
                CenterArc((-18.596413512, 8.2566875166), 1.03, -171.1789505037, 60.5760936376)
                Line((-7.1029608586, 2.8355506333), (-18.9588584831, 7.2925642657))
            make_face()
            with BuildLine():
                Line((-6.0929814237, 5.3366467223), (-18.932185854, 21.0040675133))
                Line((-18.932185854, 21.0040675133), (-20.414713146, 31.8282156869))
                Line((-20.7936445967, 32.2949885409), (-20.414713146, 31.8282156869))
                Line((-18.6691156075, 16.7834922579), (-20.7936445967, 32.2949885409))
                Line((-9.5321788716, 5.5221966096), (-18.6691156075, 16.7834922579))
                Line((-18.0302922558, 8.716911038), (-9.5321788716, 5.5221966096))
                Line((-19.4270316047, 17.7174256265), (-18.0302922558, 8.716911038))
                Line((-19.4270316047, 17.7174256265), (-20.0668240219, 22.3886434593))
                Line((-20.0668240219, 22.3886434593), (-21.6302359863, 34.3588511219))
                Line((-21.6302359863, 34.3588511219), (-18.259099498, 30.2062398855))
                Line((-18.259099498, 30.2062398855), (-13.1289907589, 28.3983768481))
                Line((-13.1289907589, 28.3983768481), (-12.6109707815, 25.5785549204))
                Line((-12.6109707815, 25.5785549204), (-18.4792192186, 27.5093838104))
                Line((-18.4792192186, 27.5093838104), (-18.1491288368, 25.712549446))
                Line((-12.2808803997, 23.781720556), (-18.1491288368, 25.712549446))
                Line((-12.2808803997, 23.781720556), (-11.8678763922, 21.5335490427))
                Line((-11.8678763922, 21.5335490427), (-17.7361248293, 23.4643779327))
                Line((-17.7361248293, 23.4643779327), (-17.3231208218, 21.2162064194))
                Line((-9.98549724, 18.8019092492), (-17.3231208218, 21.2162064194))
                Line((-9.98549724, 18.8019092492), (-6.7229814237, 15.1737269447))
                Line((-6.7229814237, 18.6333452812), (-6.7229814237, 15.1737269447))
                Line((-9.5262684531, 22.1551997318), (-6.7229814237, 18.6333452812))
                Line((-11.7226800513, 33.9245971544), (-9.5262684531, 22.1551997318))
                Line((-10.0555834413, 31.9992673041), (-11.7226800513, 33.9245971544))
                Line((-8.0157603741, 29.9256129181), (-10.0555834413, 31.9992673041))
                Line((-6.0929814237, 29.9256129181), (-8.0157603741, 29.9256129181))
                Line((-6.0929814237, 25.8682109577), (-6.0929814237, 29.9256129181))
                Line((-8.0598574409, 25.8682109577), (-6.0929814237, 25.8682109577))
                Line((-6.0929814237, 21.897314577), (-8.0598574409, 25.8682109577))
                Line((-6.0929814237, 5.3366467223), (-6.0929814237, 21.897314577))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 199.0386334269, perimeter: 219.9607830613
            with BuildLine():
                Line((-6.0929814237, 5.3366467223), (-6.0929814237, 21.897314577))
                Line((-6.0929814237, 21.897314577), (-8.0598574409, 25.8682109577))
                Line((-8.0598574409, 25.8682109577), (-6.0929814237, 25.8682109577))
                Line((-6.0929814237, 25.8682109577), (-6.0929814237, 29.9256129181))
                Line((-6.0929814237, 29.9256129181), (-8.0157603741, 29.9256129181))
                Line((-8.0157603741, 29.9256129181), (-10.0555834413, 31.9992673041))
                Line((-10.0555834413, 31.9992673041), (-11.7226800513, 33.9245971544))
                Line((-11.7226800513, 33.9245971544), (-9.5262684531, 22.1551997318))
                Line((-9.5262684531, 22.1551997318), (-6.7229814237, 18.6333452812))
                Line((-6.7229814237, 18.6333452812), (-6.7229814237, 15.1737269447))
                Line((-9.98549724, 18.8019092492), (-6.7229814237, 15.1737269447))
                Line((-9.98549724, 18.8019092492), (-17.3231208218, 21.2162064194))
                Line((-17.7361248293, 23.4643779327), (-17.3231208218, 21.2162064194))
                Line((-11.8678763922, 21.5335490427), (-17.7361248293, 23.4643779327))
                Line((-12.2808803997, 23.781720556), (-11.8678763922, 21.5335490427))
                Line((-12.2808803997, 23.781720556), (-18.1491288368, 25.712549446))
                Line((-18.4792192186, 27.5093838104), (-18.1491288368, 25.712549446))
                Line((-12.6109707815, 25.5785549204), (-18.4792192186, 27.5093838104))
                Line((-13.1289907589, 28.3983768481), (-12.6109707815, 25.5785549204))
                Line((-18.259099498, 30.2062398855), (-13.1289907589, 28.3983768481))
                Line((-21.6302359863, 34.3588511219), (-18.259099498, 30.2062398855))
                Line((-20.0668240219, 22.3886434593), (-21.6302359863, 34.3588511219))
                Line((-19.4270316047, 17.7174256265), (-20.0668240219, 22.3886434593))
                Line((-19.4270316047, 17.7174256265), (-18.0302922558, 8.716911038))
                Line((-18.0302922558, 8.716911038), (-9.5321788716, 5.5221966096))
                Line((-9.5321788716, 5.5221966096), (-18.6691156075, 16.7834922579))
                Line((-18.6691156075, 16.7834922579), (-20.7936445967, 32.2949885409))
                Line((-20.7936445967, 32.2949885409), (-20.414713146, 31.8282156869))
                Line((-18.932185854, 21.0040675133), (-20.414713146, 31.8282156869))
                Line((-6.0929814237, 5.3366467223), (-18.932185854, 21.0040675133))
            make_face()
            with BuildLine():
                Line((-8.8436518974, 11.8515697898), (-7.5089563417, 15.1722842649))
                Line((-13.4677887687, 17.7172022806), (-8.8436518974, 11.8515697898))
                Line((-7.5089563417, 15.1722842649), (-13.4677887687, 17.7172022806))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.5921359299, perimeter: 17.5275887393
            with BuildLine():
                Line((-7.5089563417, 15.1722842649), (-13.4677887687, 17.7172022806))
                Line((-13.4677887687, 17.7172022806), (-8.8436518974, 11.8515697898))
                Line((-8.8436518974, 11.8515697898), (-7.5089563417, 15.1722842649))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 24 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 499.6820622719, perimeter: 238.7041598634
            with BuildLine():
                Line((-26, 39.5035845403), (-26, 0))
                Line((-3.1305883671, 0), (-26, 0))
                Line((-3.1305883671, 0), (0, 0))
                Line((0, 39.5035845403), (0, 0))
                Line((-3.1305594424, 39.5035845403), (0, 39.5035845403))
                Line((-26, 39.5035845403), (-3.1305594424, 39.5035845403))
            make_face()
            with BuildLine():
                Line((-4.0329814237, 24.6082109577), (-4.0329814237, 30.5556129181))
                Line((-4.0329814237, 24.6082109577), (-4.0329814237, 22.192268066))
                Line((-4.0329814237, 4.6842335658), (-4.0329814237, 22.192268066))
                CenterArc((-6.4079814237, 4.6842335658), 2.375, -110.6028568661, 110.6028568661)
                Line((-7.2437161872, 2.4611338368), (-19.0996138117, 6.9181474692))
                CenterArc((-18.596413512, 8.2566875166), 1.43, -171.1789505037, 60.5760936376)
                Line((-21.4654838065, 17.4196837414), (-20.0094996298, 8.0373986121))
                Line((-21.4654838065, 17.4196837414), (-22.1086423349, 22.1154780441))
                Line((-22.1086423349, 22.1154780441), (-23.9609446689, 36.2975644654))
                CenterArc((-22.54298771, 36.4827618269), 1.43, 39.0700802862, 148.3711193981)
                Line((-21.4327705469, 37.3840486017), (-17.0261523271, 31.955917051))
                Line((-17.0261523271, 31.955917051), (-13.1991649752, 30.6072772209))
                Line((-14.1743206945, 35.8326162327), (-13.1991649752, 30.6072772209))
                CenterArc((-12.7685900503, 36.09495448), 1.43, 40.8884976473, 149.6824732665)
                Line((-8.5411059222, 33.3972098096), (-11.6875316495, 37.0310168357))
                Line((-7.1525389939, 31.9856129181), (-8.5411059222, 33.3972098096))
                Line((-5.4629814237, 31.9856129181), (-7.1525389939, 31.9856129181))
                CenterArc((-5.4629814237, 30.5556129181), 1.43, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 24 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 42.686754139, perimeter: 213.3525168677
            with BuildLine():
                CenterArc((-5.4629814237, 30.5556129181), 1.43, 0, 90)
                Line((-5.4629814237, 31.9856129181), (-7.1525389939, 31.9856129181))
                Line((-7.1525389939, 31.9856129181), (-8.5411059222, 33.3972098096))
                Line((-8.5411059222, 33.3972098096), (-11.6875316495, 37.0310168357))
                CenterArc((-12.7685900503, 36.09495448), 1.43, 40.8884976473, 149.6824732665)
                Line((-14.1743206945, 35.8326162327), (-13.1991649752, 30.6072772209))
                Line((-17.0261523271, 31.955917051), (-13.1991649752, 30.6072772209))
                Line((-21.4327705469, 37.3840486017), (-17.0261523271, 31.955917051))
                CenterArc((-22.54298771, 36.4827618269), 1.43, 39.0700802862, 148.3711193981)
                Line((-22.1086423349, 22.1154780441), (-23.9609446689, 36.2975644654))
                Line((-21.4654838065, 17.4196837414), (-22.1086423349, 22.1154780441))
                Line((-21.4654838065, 17.4196837414), (-20.0094996298, 8.0373986121))
                CenterArc((-18.596413512, 8.2566875166), 1.43, -171.1789505037, 60.5760936376)
                Line((-7.2437161872, 2.4611338368), (-19.0996138117, 6.9181474692))
                CenterArc((-6.4079814237, 4.6842335658), 2.375, -110.6028568661, 110.6028568661)
                Line((-4.0329814237, 4.6842335658), (-4.0329814237, 22.192268066))
                Line((-4.0329814237, 24.6082109577), (-4.0329814237, 22.192268066))
                Line((-4.0329814237, 24.6082109577), (-4.0329814237, 30.5556129181))
            make_face()
            with BuildLine():
                Line((-7.1029608586, 2.8355506333), (-18.9588584831, 7.2925642657))
                CenterArc((-18.596413512, 8.2566875166), 1.03, -171.1789505037, 60.5760936376)
                Line((-21.069667845, 17.4774976996), (-19.6142307857, 8.0987381658))
                Line((-21.069667845, 17.4774976996), (-21.7121727596, 22.1685198723))
                Line((-21.7121727596, 22.1685198723), (-23.5643133518, 36.3493679232))
                CenterArc((-22.54298771, 36.4827618269), 1.03, 39.0700802862, 148.3711193981)
                Line((-21.7433208023, 37.131940413), (-17.2655595448, 31.6161739121))
                Line((-17.2655595448, 31.6161739121), (-12.7972910688, 30.0415450241))
                CenterArc((-12.7731943681, 30.1099233761), 0.0725, -109.4125840017, 119.9835549156)
                Line((-13.7811093255, 35.9059975606), (-12.7019248074, 30.1232237418))
                CenterArc((-12.7685900503, 36.09495448), 1.03, 40.8884976473, 149.6824732665)
                Line((-8.8351792269, 33.1257646629), (-11.9899256078, 36.7691812117))
                Line((-7.3201547959, 31.5856129181), (-8.8351792269, 33.1257646629))
                Line((-5.4629814237, 31.5856129181), (-7.3201547959, 31.5856129181))
                CenterArc((-5.4629814237, 30.5556129181), 1.03, 0, 90)
                Line((-4.4329814237, 24.6082109577), (-4.4329814237, 30.5556129181))
                Line((-4.4329814237, 24.6082109577), (-4.4329814237, 22.192268066))
                Line((-4.4329814237, 4.6842335658), (-4.4329814237, 22.192268066))
                CenterArc((-6.4079814237, 4.6842335658), 1.975, -110.6028568661, 110.6028568661)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 24 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 274.0936122798, perimeter: 308.0887204069
            with BuildLine():
                CenterArc((-6.4079814237, 4.6842335658), 1.975, -110.6028568661, 110.6028568661)
                Line((-4.4329814237, 4.6842335658), (-4.4329814237, 22.192268066))
                Line((-4.4329814237, 24.6082109577), (-4.4329814237, 22.192268066))
                Line((-4.4329814237, 24.6082109577), (-4.4329814237, 30.5556129181))
                CenterArc((-5.4629814237, 30.5556129181), 1.03, 0, 90)
                Line((-5.4629814237, 31.5856129181), (-7.3201547959, 31.5856129181))
                Line((-7.3201547959, 31.5856129181), (-8.8351792269, 33.1257646629))
                Line((-8.8351792269, 33.1257646629), (-11.9899256078, 36.7691812117))
                CenterArc((-12.7685900503, 36.09495448), 1.03, 40.8884976473, 149.6824732665)
                Line((-13.7811093255, 35.9059975606), (-12.7019248074, 30.1232237418))
                CenterArc((-12.7731943681, 30.1099233761), 0.0725, -109.4125840017, 119.9835549156)
                Line((-17.2655595448, 31.6161739121), (-12.7972910688, 30.0415450241))
                Line((-21.7433208023, 37.131940413), (-17.2655595448, 31.6161739121))
                CenterArc((-22.54298771, 36.4827618269), 1.03, 39.0700802862, 148.3711193981)
                Line((-21.7121727596, 22.1685198723), (-23.5643133518, 36.3493679232))
                Line((-21.069667845, 17.4774976996), (-21.7121727596, 22.1685198723))
                Line((-21.069667845, 17.4774976996), (-19.6142307857, 8.0987381658))
                CenterArc((-18.596413512, 8.2566875166), 1.03, -171.1789505037, 60.5760936376)
                Line((-7.1029608586, 2.8355506333), (-18.9588584831, 7.2925642657))
            make_face()
            with BuildLine():
                Line((-6.0929814237, 5.3366467223), (-18.932185854, 21.0040675133))
                Line((-18.932185854, 21.0040675133), (-20.414713146, 31.8282156869))
                Line((-20.7936445967, 32.2949885409), (-20.414713146, 31.8282156869))
                Line((-18.6691156075, 16.7834922579), (-20.7936445967, 32.2949885409))
                Line((-9.5321788716, 5.5221966096), (-18.6691156075, 16.7834922579))
                Line((-18.0302922558, 8.716911038), (-9.5321788716, 5.5221966096))
                Line((-19.4270316047, 17.7174256265), (-18.0302922558, 8.716911038))
                Line((-19.4270316047, 17.7174256265), (-20.0668240219, 22.3886434593))
                Line((-20.0668240219, 22.3886434593), (-21.6302359863, 34.3588511219))
                Line((-21.6302359863, 34.3588511219), (-18.259099498, 30.2062398855))
                Line((-18.259099498, 30.2062398855), (-13.1289907589, 28.3983768481))
                Line((-13.1289907589, 28.3983768481), (-12.6109707815, 25.5785549204))
                Line((-12.6109707815, 25.5785549204), (-18.4792192186, 27.5093838104))
                Line((-18.4792192186, 27.5093838104), (-18.1491288368, 25.712549446))
                Line((-12.2808803997, 23.781720556), (-18.1491288368, 25.712549446))
                Line((-12.2808803997, 23.781720556), (-11.8678763922, 21.5335490427))
                Line((-11.8678763922, 21.5335490427), (-17.7361248293, 23.4643779327))
                Line((-17.7361248293, 23.4643779327), (-17.3231208218, 21.2162064194))
                Line((-9.98549724, 18.8019092492), (-17.3231208218, 21.2162064194))
                Line((-9.98549724, 18.8019092492), (-6.7229814237, 15.1737269447))
                Line((-6.7229814237, 18.6333452812), (-6.7229814237, 15.1737269447))
                Line((-9.5262684531, 22.1551997318), (-6.7229814237, 18.6333452812))
                Line((-11.7226800513, 33.9245971544), (-9.5262684531, 22.1551997318))
                Line((-10.0555834413, 31.9992673041), (-11.7226800513, 33.9245971544))
                Line((-8.0157603741, 29.9256129181), (-10.0555834413, 31.9992673041))
                Line((-6.0929814237, 29.9256129181), (-8.0157603741, 29.9256129181))
                Line((-6.0929814237, 25.8682109577), (-6.0929814237, 29.9256129181))
                Line((-8.0598574409, 25.8682109577), (-6.0929814237, 25.8682109577))
                Line((-6.0929814237, 21.897314577), (-8.0598574409, 25.8682109577))
                Line((-6.0929814237, 5.3366467223), (-6.0929814237, 21.897314577))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.5921359299, perimeter: 17.5275887393
            with BuildLine():
                Line((-7.5089563417, 15.1722842649), (-13.4677887687, 17.7172022806))
                Line((-13.4677887687, 17.7172022806), (-8.8436518974, 11.8515697898))
                Line((-8.8436518974, 11.8515697898), (-7.5089563417, 15.1722842649))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_130757_46123542_0000():
    """Model: Body"""
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1698227179, perimeter: 1.4608405839
            Circle(0.2325)
        # Symmetric extrude, full_length=True, total=0.25
        extrude(amount=0.125, both=True)
    return part.part


def model_130849_deb0581b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 875.9240338093, perimeter: 195.3778593941
            with BuildLine():
                Line((0, 0), (0, -5.08))
                Line((0, -5.08), (80.9859909073, -5.08))
                Line((80.9859909073, -5.08), (91.44, 0))
                Line((91.44, 0), (80.9859909073, 5.08))
                Line((0, 5.08), (80.9859909073, 5.08))
                Line((0, 0), (0, 5.08))
            make_face()
        # TwoSides extrude (symmetric), distance=0.3175
        extrude(amount=0.3175, both=True)
    return part.part


def model_130966_95aacf5a_0002():
    """Model: Main Driven Gear"""
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
            # Profile area: 1.9488730301, perimeter: 7.1805498328
            with BuildLine():
                CenterArc((0, 0), 0.84282, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.268
        extrude(amount=0.268)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0044315674, perimeter: 0.2698229485
            with BuildLine():
                Line((0.8304255543, 0.0348876637), (0.8304255543, -0.0348876637))
                _nurbs_edge([(0.8304255543, -0.0348876637), (0.8306670009, -0.0348876023), (0.8311499446, -0.034885618), (0.8318745119, -0.0348770565), (0.8328409055, -0.0348544678), (0.8340494004, -0.0348076741), (0.8352583873, -0.034742555), (0.8364678437, -0.0346596024), (0.8376777313, -0.0345596638), (0.838887992, -0.0344440295), (0.8400985567, -0.0343142366), (0.841309353, -0.0341718796), (0.8425203138, -0.0340184211), (0.8437313851, -0.033854997), (0.8449425341, -0.0336822395), (0.8461537427, -0.0335004237), (0.8473650022, -0.033309599), (0.848576308, -0.0331097231), (0.8497876532, -0.0329008004), (0.8509990241, -0.0326830046), (0.8522104024, -0.0324566175), (0.8534217674, -0.0322219786), (0.8546330982, -0.0319794317), (0.8558443762, -0.0317292713), (0.8570555864, -0.0314716945), (0.858266717, -0.0312068314), (0.859477758, -0.0309347677), (0.8606886999, -0.0306555705), (0.8618995331, -0.0303693136), (0.863110247, -0.0300760997), (0.86432083, -0.0297760485), (0.8655312704, -0.0294692878), (0.8667415563, -0.0291559433), (0.8679516765, -0.0288361293), (0.8691616207, -0.0285099396), (0.8703713791, -0.0281774537), (0.8715809423, -0.0278387406), (0.8727903011, -0.0274938642), (0.8739994465, -0.0271428874), (0.8752083693, -0.0267858769), (0.8764170603, -0.0264229007), (0.8776255101, -0.0260540267), (0.8788337097, -0.0256793209), (0.88004165, -0.0252988454), (0.881249322, -0.0249126578), (0.8824567171, -0.0245208113), (0.8836638267, -0.0241233559), (0.8848706425, -0.0237203396), (0.886077156, -0.0233118088), (0.8872833592, -0.0228978092), (0.8884892439, -0.0224783861), (0.889694802, -0.0220535835), (0.8909000254, -0.0216234443), (0.8921049059, -0.0211880101), (0.893309435, -0.0207473212), (0.8945136045, -0.0203014163), (0.895717406, -0.0198503328), (0.8969208317, -0.0193941061), (0.8981238741, -0.0189327704), (0.8993265261, -0.0184663581), (0.9005287811, -0.0179949009), (0.9017306321, -0.0175184296), (0.9029320717, -0.0170369751), (0.9041330916, -0.0165505689), (0.9053336825, -0.0160592435), (0.9065338347, -0.0155630313), (0.9077335388, -0.0150619634), (0.9089327864, -0.0145560685), (0.9101315713, -0.0140453721), (0.9113298896, -0.0135298949), (0.9125277392, -0.0130096534), (0.9134856436, -0.0125896581), (0.9142038607, -0.0122725262), (0.9146825784, -0.0120601561), (0.9149219137, -0.0119537338)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.915, -0.7485442433, 1.4970884865)
                _nurbs_edge([(0.8304255543, 0.0348876637), (0.8306670009, 0.0348876023), (0.8311499446, 0.034885618), (0.8318745119, 0.0348770565), (0.8328409055, 0.0348544678), (0.8340494004, 0.0348076741), (0.8352583873, 0.034742555), (0.8364678437, 0.0346596024), (0.8376777313, 0.0345596638), (0.838887992, 0.0344440295), (0.8400985567, 0.0343142366), (0.841309353, 0.0341718796), (0.8425203138, 0.0340184211), (0.8437313851, 0.033854997), (0.8449425341, 0.0336822395), (0.8461537427, 0.0335004237), (0.8473650022, 0.033309599), (0.848576308, 0.0331097231), (0.8497876532, 0.0329008004), (0.8509990241, 0.0326830046), (0.8522104024, 0.0324566175), (0.8534217674, 0.0322219786), (0.8546330982, 0.0319794317), (0.8558443762, 0.0317292713), (0.8570555864, 0.0314716945), (0.858266717, 0.0312068314), (0.859477758, 0.0309347677), (0.8606886999, 0.0306555705), (0.8618995331, 0.0303693136), (0.863110247, 0.0300760997), (0.86432083, 0.0297760485), (0.8655312704, 0.0294692878), (0.8667415563, 0.0291559433), (0.8679516765, 0.0288361293), (0.8691616207, 0.0285099396), (0.8703713791, 0.0281774537), (0.8715809423, 0.0278387406), (0.8727903011, 0.0274938642), (0.8739994465, 0.0271428874), (0.8752083693, 0.0267858769), (0.8764170603, 0.0264229007), (0.8776255101, 0.0260540267), (0.8788337097, 0.0256793209), (0.88004165, 0.0252988454), (0.881249322, 0.0249126578), (0.8824567171, 0.0245208113), (0.8836638267, 0.0241233559), (0.8848706425, 0.0237203396), (0.886077156, 0.0233118088), (0.8872833592, 0.0228978092), (0.8884892439, 0.0224783861), (0.889694802, 0.0220535835), (0.8909000254, 0.0216234443), (0.8921049059, 0.0211880101), (0.893309435, 0.0207473212), (0.8945136045, 0.0203014163), (0.895717406, 0.0198503328), (0.8969208317, 0.0193941061), (0.8981238741, 0.0189327704), (0.8993265261, 0.0184663581), (0.9005287811, 0.0179949009), (0.9017306321, 0.0175184296), (0.9029320717, 0.0170369751), (0.9041330916, 0.0165505689), (0.9053336825, 0.0160592435), (0.9065338347, 0.0155630313), (0.9077335388, 0.0150619634), (0.9089327864, 0.0145560685), (0.9101315713, 0.0140453721), (0.9113298896, 0.0135298949), (0.9125277392, 0.0130096534), (0.9134856436, 0.0125896581), (0.9142038607, 0.0122725262), (0.9146825784, 0.0120601561), (0.9149219137, 0.0119537338)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.268
        extrude(amount=0.268, mode=Mode.ADD)
    return part.part


def model_130996_b842b511_0010():
    """Model: 20mm Ball Nut Carrier v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.6612398024, perimeter: 31.1038461026
            with BuildLine():
                Line((3.1, 2.2), (-3.1, 2.2))
                Line((-3.1, 2.2), (-3.1, -1))
                Line((-3.1, -1), (-1.9, -2.2))
                Line((-1.9, -2.2), (1.9, -2.2))
                Line((1.9, -2.2), (3.1, -1))
                Line((3.1, -1), (3.1, 2.2))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_131068_085c0ed9_0002():
    """Model: Spur Gear (24 teeth)"""
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
            # Profile area: 130.4432121295, perimeter: 44.6729448792
            with BuildLine():
                CenterArc((0, 0), 6.47492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2016958531, perimeter: 4.2790962025
            with BuildLine():
                _nurbs_edge([(6.7439559455, -0.5430747382), (6.7470033057, -0.5433192941), (6.7530997154, -0.5437315002), (6.7622493974, -0.5441190955), (6.7744586984, -0.5441972859), (6.7897340657, -0.5436963271), (6.8050198815, -0.5427646805), (6.8203126236, -0.5415679577), (6.8356091796, -0.5402280882), (6.8509073666, -0.5387909464), (6.8662056749, -0.53725221), (6.8815030923, -0.5355774199), (6.8967989047, -0.533723203), (6.9120924902, -0.5316603845), (6.9273831717, -0.5293887428), (6.9426702682, -0.5269251407), (6.9579531116, -0.5242961059), (6.973231075, -0.5215292292), (6.9885036017, -0.5186437418), (7.0037702166, -0.5156459374), (7.0190305034, -0.5125344352), (7.0342840879, -0.5093033862), (7.0495306205, -0.5059462227), (7.0647697562, -0.5024598411), (7.0800011461, -0.4988461827), (7.0952244447, -0.4951100156), (7.1104393137, -0.4912576138), (7.1256454269, -0.4872952003), (7.1408424754, -0.4832271889), (7.156030169, -0.479055677), (7.1712082317, -0.4747813947), (7.186376398, -0.470404287), (7.2015344105, -0.4659241912), (7.2166820154, -0.461341608), (7.2318189619, -0.4566578956), (7.2469450029, -0.4518748751), (7.2620598959, -0.4469945903), (7.277163404, -0.4420190288), (7.2922552965, -0.4369498034), (7.3073353494, -0.4317880809), (7.3224033437, -0.4265347538), (7.3374590647, -0.4211905476), (7.3525023008, -0.4157561453), (7.3675328425, -0.41023233), (7.3825504827, -0.4046200213), (7.3975550167, -0.3989202027), (7.4125462435, -0.3931338785), (7.4275239658, -0.3872620236), (7.4424879918, -0.3813055262), (7.4574381341, -0.375265173), (7.472374208, -0.3691416827), (7.4872960297, -0.3629357277), (7.5022034152, -0.3566479598), (7.517096178, -0.3502790391), (7.5319741293, -0.3438296445), (7.5468370823, -0.3373004543), (7.5616848547, -0.3306921353), (7.5765172722, -0.3240053295), (7.5913341727, -0.3172406401), (7.6061354061, -0.3103986273), (7.6209208252, -0.303479826), (7.6356902783, -0.29648476), (7.650443602, -0.2894139559), (7.6651806117, -0.2822679619), (7.6799011001, -0.2750473545), (7.6946048551, -0.2677527106), (7.7092916763, -0.2603845855), (7.7239613906, -0.2529434895), (7.7386138705, -0.2454298651), (7.7532490468, -0.2378440663), (7.7678668918, -0.2301863638), (7.7795473022, -0.2240028301), (7.7882998155, -0.2193329579), (7.7941313614, -0.2162053937), (7.7970462686, -0.2146380327)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 7.8, -1.576846918, 3.1536938361)
                _nurbs_edge([(6.7439559455, 0.5430747382), (6.7470033057, 0.5433192941), (6.7530997154, 0.5437315002), (6.7622493974, 0.5441190955), (6.7744586984, 0.5441972859), (6.7897340657, 0.5436963271), (6.8050198815, 0.5427646805), (6.8203126236, 0.5415679577), (6.8356091796, 0.5402280882), (6.8509073666, 0.5387909464), (6.8662056749, 0.53725221), (6.8815030923, 0.5355774199), (6.8967989047, 0.533723203), (6.9120924902, 0.5316603845), (6.9273831717, 0.5293887428), (6.9426702682, 0.5269251407), (6.9579531116, 0.5242961059), (6.973231075, 0.5215292292), (6.9885036017, 0.5186437418), (7.0037702166, 0.5156459374), (7.0190305034, 0.5125344352), (7.0342840879, 0.5093033862), (7.0495306205, 0.5059462227), (7.0647697562, 0.5024598411), (7.0800011461, 0.4988461827), (7.0952244447, 0.4951100156), (7.1104393137, 0.4912576138), (7.1256454269, 0.4872952003), (7.1408424754, 0.4832271889), (7.156030169, 0.479055677), (7.1712082317, 0.4747813947), (7.186376398, 0.470404287), (7.2015344105, 0.4659241912), (7.2166820154, 0.461341608), (7.2318189619, 0.4566578956), (7.2469450029, 0.4518748751), (7.2620598959, 0.4469945903), (7.277163404, 0.4420190288), (7.2922552965, 0.4369498034), (7.3073353494, 0.4317880809), (7.3224033437, 0.4265347538), (7.3374590647, 0.4211905476), (7.3525023008, 0.4157561453), (7.3675328425, 0.41023233), (7.3825504827, 0.4046200213), (7.3975550167, 0.3989202027), (7.4125462435, 0.3931338785), (7.4275239658, 0.3872620236), (7.4424879918, 0.3813055262), (7.4574381341, 0.375265173), (7.472374208, 0.3691416827), (7.4872960297, 0.3629357277), (7.5022034152, 0.3566479598), (7.517096178, 0.3502790391), (7.5319741293, 0.3438296445), (7.5468370823, 0.3373004543), (7.5616848547, 0.3306921353), (7.5765172722, 0.3240053295), (7.5913341727, 0.3172406401), (7.6061354061, 0.3103986273), (7.6209208252, 0.303479826), (7.6356902783, 0.29648476), (7.650443602, 0.2894139559), (7.6651806117, 0.2822679619), (7.6799011001, 0.2750473545), (7.6946048551, 0.2677527106), (7.7092916763, 0.2603845855), (7.7239613906, 0.2529434895), (7.7386138705, 0.2454298651), (7.7532490468, 0.2378440663), (7.7678668918, 0.2301863638), (7.7795473022, 0.2240028301), (7.7882998155, 0.2193329579), (7.7941313614, 0.2162053937), (7.7970462686, 0.2146380327)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((6.4530308323, 0.5197274983), (6.7439559455, 0.5430747382))
                Line((6.4530308323, -0.5197274983), (6.4530308323, 0.5197274983))
                Line((6.4530308323, -0.5197274983), (6.7439559455, -0.5430747382))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_131068_085c0ed9_0003():
    """Model: Spur Gear (12 teeth)"""
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
            # Profile area: 24.6990129671, perimeter: 22.0534777734
            with BuildLine():
                CenterArc((0, 0), 2.87492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1148756887, perimeter: 4.0574976262
            with BuildLine():
                _nurbs_edge([(3.3469989154, -0.4914938979), (3.3494293312, -0.4918500939), (3.3542959241, -0.4924838577), (3.3616130966, -0.4931986237), (3.3714022801, -0.4937037842), (3.3836842328, -0.493726906), (3.3959995091, -0.4933159263), (3.4083358348, -0.492641233), (3.4206836978, -0.4918243315), (3.4330383347, -0.4909074861), (3.4453980837, -0.4898825466), (3.4577632353, -0.4887117436), (3.4701347743, -0.4873500445), (3.4825129738, -0.4857704769), (3.4948967286, -0.4839755749), (3.5072842021, -0.4819844207), (3.5196731857, -0.4798249897), (3.5320615369, -0.4775251247), (3.5444476723, -0.4751022716), (3.5568306777, -0.4725611249), (3.5692100363, -0.4698990578), (3.5815854576, -0.467109508), (3.5939566813, -0.4641858737), (3.6063232525, -0.461125996), (3.6186845003, -0.4579325223), (3.6310396433, -0.4546107464), (3.6433878576, -0.4511671785), (3.6557283541, -0.447607941), (3.6680604679, -0.4439369214), (3.6803836535, -0.4401558437), (3.6926974401, -0.4362651526), (3.7050013991, -0.4322646537), (3.7172951093, -0.4281542055), (3.7295781167, -0.4239345167), (3.7418499372, -0.4196070774), (3.7541100739, -0.4151738037), (3.7663580299, -0.4106367708), (3.7785933218, -0.405997931), (3.790815496, -0.4012587864), (3.8030241255, -0.3964204302), (3.8152188018, -0.3914836996), (3.8273991282, -0.3864492952), (3.8395647127, -0.3813179057), (3.8517151603, -0.3760903547), (3.8638500742, -0.3707675886), (3.8759690594, -0.3653506121), (3.8880717259, -0.3598404406), (3.9001576923, -0.3542380499), (3.91222659, -0.3485443175), (3.9242780614, -0.3427600264), (3.9363117552, -0.3368858963), (3.9483273227, -0.3309226071), (3.9603244142, -0.3248708242), (3.9723026746, -0.3187312295), (3.9842617456, -0.3125045218), (3.9962012722, -0.3061913992), (4.0081209097, -0.2997925464), (4.020020328, -0.2933086223), (4.0318992215, -0.2867402441), (4.043757304, -0.2800879891), (4.0555942939, -0.2733524118), (4.0674099, -0.2665340594), (4.0792038096, -0.259633486), (4.0909756711, -0.2526512726), (4.1027250952, -0.2455880294), (4.1144516883, -0.2384443659), (4.1261550794, -0.2312208683), (4.1378349486, -0.2239180752), (4.1494910583, -0.2165364534), (4.1611232734, -0.2090763784), (4.1727315314, -0.2015381388), (4.1819989618, -0.1954451775), (4.1889387532, -0.1908404272), (4.1935604908, -0.1877550304), (4.195870162, -0.1862084411)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 4.2, -2.5410609694, 5.0821219387)
                _nurbs_edge([(3.3469989154, 0.4914938979), (3.3494293312, 0.4918500939), (3.3542959241, 0.4924838577), (3.3616130966, 0.4931986237), (3.3714022801, 0.4937037842), (3.3836842328, 0.493726906), (3.3959995091, 0.4933159263), (3.4083358348, 0.492641233), (3.4206836978, 0.4918243315), (3.4330383347, 0.4909074861), (3.4453980837, 0.4898825466), (3.4577632353, 0.4887117436), (3.4701347743, 0.4873500445), (3.4825129738, 0.4857704769), (3.4948967286, 0.4839755749), (3.5072842021, 0.4819844207), (3.5196731857, 0.4798249897), (3.5320615369, 0.4775251247), (3.5444476723, 0.4751022716), (3.5568306777, 0.4725611249), (3.5692100363, 0.4698990578), (3.5815854576, 0.467109508), (3.5939566813, 0.4641858737), (3.6063232525, 0.461125996), (3.6186845003, 0.4579325223), (3.6310396433, 0.4546107464), (3.6433878576, 0.4511671785), (3.6557283541, 0.447607941), (3.6680604679, 0.4439369214), (3.6803836535, 0.4401558437), (3.6926974401, 0.4362651526), (3.7050013991, 0.4322646537), (3.7172951093, 0.4281542055), (3.7295781167, 0.4239345167), (3.7418499372, 0.4196070774), (3.7541100739, 0.4151738037), (3.7663580299, 0.4106367708), (3.7785933218, 0.405997931), (3.790815496, 0.4012587864), (3.8030241255, 0.3964204302), (3.8152188018, 0.3914836996), (3.8273991282, 0.3864492952), (3.8395647127, 0.3813179057), (3.8517151603, 0.3760903547), (3.8638500742, 0.3707675886), (3.8759690594, 0.3653506121), (3.8880717259, 0.3598404406), (3.9001576923, 0.3542380499), (3.91222659, 0.3485443175), (3.9242780614, 0.3427600264), (3.9363117552, 0.3368858963), (3.9483273227, 0.3309226071), (3.9603244142, 0.3248708242), (3.9723026746, 0.3187312295), (3.9842617456, 0.3125045218), (3.9962012722, 0.3061913992), (4.0081209097, 0.2997925464), (4.020020328, 0.2933086223), (4.0318992215, 0.2867402441), (4.043757304, 0.2800879891), (4.0555942939, 0.2733524118), (4.0674099, 0.2665340594), (4.0792038096, 0.259633486), (4.0909756711, 0.2526512726), (4.1027250952, 0.2455880294), (4.1144516883, 0.2384443659), (4.1261550794, 0.2312208683), (4.1378349486, 0.2239180752), (4.1494910583, 0.2165364534), (4.1611232734, 0.2090763784), (4.1727315314, 0.2015381388), (4.1819989618, 0.1954451775), (4.1889387532, 0.1908404272), (4.1935604908, 0.1877550304), (4.195870162, 0.1862084411)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((2.8434259927, 0.417691442), (3.3469989154, 0.4914938979))
                Line((2.8434259927, -0.417691442), (2.8434259927, 0.417691442))
                Line((2.8434259927, -0.417691442), (3.3469989154, -0.4914938979))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_131335_b4d05d31_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Block Shape -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 154.8384, perimeter: 55.88
            with BuildLine():
                Line((10.16, -3.81), (-10.16, -3.81))
                Line((10.16, 3.81), (10.16, -3.81))
                Line((-10.16, 3.81), (10.16, 3.81))
                Line((-10.16, -3.81), (-10.16, 3.81))
            make_face()
        # OneSide extrude, distance=-3.175
        extrude(amount=-3.175)

        # Radius -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.2059198621, perimeter: 15.2596749796
            with BuildLine():
                Line((-3.81, 0), (0, 0))
                CenterArc((0, 30.48), 30.717202021, -97.1250163489, 14.2500326978)
                Line((0, 0), (3.81, 0))
            make_face()
        # Symmetric extrude, each_side=10.16
        extrude(amount=10.16, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_131466_90a4c082_0000():
    """Model: Spur Gear (15 teeth)"""
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
            # Profile area: 4.7203370817, perimeter: 7.7819956632
            with BuildLine():
                CenterArc((0, 0), 1.2258430769, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1224892412, perimeter: 1.3511555215
            with BuildLine():
                _nurbs_edge([(1.3671703836, -0.164331185), (1.3680022444, -0.1644305159), (1.3696673924, -0.1646049041), (1.3721693939, -0.1647936664), (1.3755136189, -0.1649068431), (1.3797056214, -0.1648588397), (1.3839067601, -0.1646739421), (1.3881143746, -0.1644040343), (1.3923262923, -0.1640874815), (1.3965412865, -0.1637388543), (1.4007587823, -0.1633569208), (1.4049786322, -0.1629309339), (1.4092008765, -0.1624472629), (1.4134254868, -0.1618965663), (1.4176521893, -0.161278583), (1.4218805746, -0.1605984656), (1.4261101616, -0.1598644481), (1.4303404747, -0.1590851563), (1.4345711264, -0.1582666864), (1.4388018609, -0.1574110612), (1.4430325043, -0.1565178677), (1.4472629345, -0.1555852626), (1.4514930447, -0.1546111461), (1.4557227044, -0.1535944604), (1.4599517421, -0.1525357448), (1.4641799653, -0.1514364408), (1.468407172, -0.1502984789), (1.4726331644, -0.1491237903), (1.4768577651, -0.1479137603), (1.4810808216, -0.1466690401), (1.4853021973, -0.1453898465), (1.4895217663, -0.1440761429), (1.4937394064, -0.1427278522), (1.4979549922, -0.141345097), (1.5021683923, -0.1399282737), (1.5063794732, -0.1384779275), (1.5105881014, -0.1369946777), (1.5147941457, -0.1354791296), (1.5189974802, -0.1339317756), (1.5231979851, -0.1323529671), (1.5273955447, -0.1307429687), (1.531590046, -0.1291019914), (1.5357813777, -0.1274302323), (1.5399694286, -0.1257279188), (1.544154087, -0.1239953221), (1.5483352418, -0.1222327349), (1.552512783, -0.1204404573), (1.5566866026, -0.1186187815), (1.5608565956, -0.1167679737), (1.5650226594, -0.1148882685), (1.5691846935, -0.1129798794), (1.5733425978, -0.1110430055), (1.5774962717, -0.1090778395), (1.5816456136, -0.1070845766), (1.5857905201, -0.1050634183), (1.5899308884, -0.1030145666), (1.594066618, -0.1009382202), (1.5981976126, -0.0988345714), (1.6023237817, -0.0967038009), (1.6064450412, -0.0945460771), (1.6105613088, -0.0923615607), (1.6146724997, -0.090150409), (1.6187785231, -0.0879127797), (1.6228792778, -0.0856488361), (1.62697465, -0.0833587497), (1.6310645236, -0.0810426923), (1.6351487882, -0.0787008299), (1.6392273473, -0.0763333164), (1.6433001275, -0.073940287), (1.6473670855, -0.0715218532), (1.6514281996, -0.0690781021), (1.654672411, -0.0671028974), (1.6571029378, -0.0656101462), (1.6587221198, -0.064609937), (1.6595314185, -0.0641085719)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 1.6607692308, -2.2122660809, 4.4245321618)
                _nurbs_edge([(1.3671703836, 0.164331185), (1.3680022444, 0.1644305159), (1.3696673924, 0.1646049041), (1.3721693939, 0.1647936664), (1.3755136189, 0.1649068431), (1.3797056214, 0.1648588397), (1.3839067601, 0.1646739421), (1.3881143746, 0.1644040343), (1.3923262923, 0.1640874815), (1.3965412865, 0.1637388543), (1.4007587823, 0.1633569208), (1.4049786322, 0.1629309339), (1.4092008765, 0.1624472629), (1.4134254868, 0.1618965663), (1.4176521893, 0.161278583), (1.4218805746, 0.1605984656), (1.4261101616, 0.1598644481), (1.4303404747, 0.1590851563), (1.4345711264, 0.1582666864), (1.4388018609, 0.1574110612), (1.4430325043, 0.1565178677), (1.4472629345, 0.1555852626), (1.4514930447, 0.1546111461), (1.4557227044, 0.1535944604), (1.4599517421, 0.1525357448), (1.4641799653, 0.1514364408), (1.468407172, 0.1502984789), (1.4726331644, 0.1491237903), (1.4768577651, 0.1479137603), (1.4810808216, 0.1466690401), (1.4853021973, 0.1453898465), (1.4895217663, 0.1440761429), (1.4937394064, 0.1427278522), (1.4979549922, 0.141345097), (1.5021683923, 0.1399282737), (1.5063794732, 0.1384779275), (1.5105881014, 0.1369946777), (1.5147941457, 0.1354791296), (1.5189974802, 0.1339317756), (1.5231979851, 0.1323529671), (1.5273955447, 0.1307429687), (1.531590046, 0.1291019914), (1.5357813777, 0.1274302323), (1.5399694286, 0.1257279188), (1.544154087, 0.1239953221), (1.5483352418, 0.1222327349), (1.552512783, 0.1204404573), (1.5566866026, 0.1186187815), (1.5608565956, 0.1167679737), (1.5650226594, 0.1148882685), (1.5691846935, 0.1129798794), (1.5733425978, 0.1110430055), (1.5774962717, 0.1090778395), (1.5816456136, 0.1070845766), (1.5857905201, 0.1050634183), (1.5899308884, 0.1030145666), (1.594066618, 0.1009382202), (1.5981976126, 0.0988345714), (1.6023237817, 0.0967038009), (1.6064450412, 0.0945460771), (1.6105613088, 0.0923615607), (1.6146724997, 0.090150409), (1.6187785231, 0.0879127797), (1.6228792778, 0.0856488361), (1.62697465, 0.0833587497), (1.6310645236, 0.0810426923), (1.6351487882, 0.0787008299), (1.6392273473, 0.0763333164), (1.6433001275, 0.073940287), (1.6473670855, 0.0715218532), (1.6514281996, 0.0690781021), (1.654672411, 0.0671028974), (1.6571029378, 0.0656101462), (1.6587221198, 0.064609937), (1.6595314185, 0.0641085719)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((1.2160898104, 0.1462909369), (1.3671703836, 0.164331185))
                Line((1.2160898104, -0.1462909369), (1.2160898104, 0.1462909369))
                Line((1.2160898104, -0.1462909369), (1.3671703836, -0.164331185))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


def model_131568_0e01803b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4425908705, perimeter: 7.829455742
            with BuildLine():
                Line((-0.5244806194, 0.3119000034), (-0.2585120892, 0.104672989))
                CenterArc((-0.5814720604, 0.3586264816), 0.0736979519, -39.3478429713, 324.0352369316)
                Line((-0.4507248733, -0.1585874556), (-0.5627863041, 0.2873367163))
                Line((-0.4507248733, -0.1585874556), (-0.3222484146, -0.1585874556))
                Line((-0.3222484146, -0.1585874556), (-0.3920711785, 0.1038788376))
                Line((-0.3920711785, 0.1038788376), (-0.2220012757, -0.0286296143))
                Line((-0.2220012757, -0.0286296143), (-0.1231030339, 0.0983027748))
                Line((-0.1231030339, 0.0983027748), (-0.0434692653, -0.2010434397))
                Line((-0.4535919721, -0.2049187763), (-0.0434692653, -0.2010434397))
                Line((-0.4535919721, -0.2049187763), (-0.4873921341, -0.332071767))
                Line((-0.4873921341, -0.332071767), (0.4884571176, -0.332071767))
                Line((0.4884571176, -0.332071767), (0.4534266317, -0.2019585334))
                Line((0.0614188126, -0.2011244742), (0.4534266317, -0.2019585334))
                Line((0.1391565334, 0.0999708932), (0.0614188126, -0.2011244742))
                Line((0.234903124, -0.0251379852), (0.1391565334, 0.0999708932))
                Line((0.4011758795, 0.1021115726), (0.234903124, -0.0251379852))
                Line((0.4011758795, 0.1021115726), (0.3249815165, -0.1602555739))
                Line((0.3249815165, -0.1602555739), (0.45509475, -0.1602555739))
                Line((0.45509475, -0.1602555739), (0.5751992733, 0.2851320333))
                CenterArc((0.5980730017, 0.3571433206), 0.0755568194, -107.6219754337, 327.1806667833)
                Line((0.2665973732, 0.1016390116), (0.5398207637, 0.3090235771))
                Line((0.074119641, 0.3552230643), (0.2665973732, 0.1016390116))
                Line((0, 0.1000000015), (0.074119641, 0.3552230643))
                Line((-0.0620219475, 0.3568611236), (0, 0.1000000015))
                Line((-0.2585120892, 0.104672989), (-0.0620219475, 0.3568611236))
            make_face()
        # OneSide extrude, distance=0.001
        extrude(amount=0.001)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.002500977, perimeter: 0.2222701166
            with BuildLine():
                Line((0.225432239, -0.1000000015), (0.1988613409, -0.0530592841))
                Line((0.1988613409, -0.0530592841), (0.1748612166, -0.1000000015))
                Line((0.1748612166, -0.1000000015), (0.1988613409, -0.1519687746))
                Line((0.1988613409, -0.1519687746), (0.225432239, -0.1000000015))
            make_face()
        # OneSide extrude, distance=0.001
        extrude(amount=0.001)

        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.002500977, perimeter: 0.2222701166
            with BuildLine():
                Line((-0.1747016087, -0.0977520585), (-0.2012725068, -0.0508113411))
                Line((-0.2012725068, -0.0508113411), (-0.2252726311, -0.0977520585))
                Line((-0.2252726311, -0.0977520585), (-0.2012725068, -0.1497208316))
                Line((-0.2012725068, -0.1497208316), (-0.1747016087, -0.0977520585))
            make_face()
        # OneSide extrude, distance=0.001
        extrude(amount=0.001)
    return part.part


def model_131816_9dc8a682_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 88.8, perimeter: 38.8
            with BuildLine():
                Line((-6, 3.7), (6, 3.7))
                Line((-6, -3.7), (-6, 3.7))
                Line((6, -3.7), (-6, -3.7))
                Line((6, 3.7), (6, -3.7))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0053096491, perimeter: 4.1132741229
            with BuildLine():
                CenterArc((4.5, 0), 0.8, -180, 180)
                Line((5.3, 0), (3.7, 0))
            make_face()
            # Profile area: 1.0053096491, perimeter: 4.1132741229
            with BuildLine():
                Line((5.3, 0), (3.7, 0))
                CenterArc((4.5, 0), 0.8, 0, 180)
            make_face()
            # Profile area: 0.138544236, perimeter: 1.3194689145
            with Locations((4.5, 1.45)):
                Circle(0.21)
            # Profile area: 0.2123716634, perimeter: 1.6336281799
            with Locations((2.3, 2.8)):
                Circle(0.26)
            # Profile area: 0.2123716634, perimeter: 1.6336281799
            with Locations((-2.3, 2.8)):
                Circle(0.26)
            # Profile area: 1.0053096491, perimeter: 4.1132741229
            with BuildLine():
                CenterArc((-4.5, 0), 0.8, 0, 180)
                Line((-3.7, 0), (-5.3, 0))
            make_face()
            # Profile area: 1.0053096491, perimeter: 4.1132741229
            with BuildLine():
                Line((-3.7, 0), (-5.3, 0))
                CenterArc((-4.5, 0), 0.8, -180, 180)
            make_face()
            # Profile area: 0.138544236, perimeter: 1.3194689145
            with Locations((-4.5, -1.45)):
                Circle(0.21)
            # Profile area: 0.2123716634, perimeter: 1.6336281799
            with Locations((-2.3, -2.8)):
                Circle(0.26)
            # Profile area: 0.2123716634, perimeter: 1.6336281799
            with Locations((2.3, -2.8)):
                Circle(0.26)
            # Profile area: 0.138544236, perimeter: 1.3194689145
            with Locations((4.5, -1.45)):
                Circle(0.21)
            # Profile area: 0.138544236, perimeter: 1.3194689145
            with Locations((-4.5, 1.45)):
                Circle(0.21)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


def model_132156_cd3f1428_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6022210641, perimeter: 8.2462166244
            with BuildLine():
                Line((-7.2819083778, 1.591661643), (-4.7496122666, 2.8401824055))
                Line((-4.7561066431, 0.3463428615), (-7.2819083778, 1.591661643))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, 150.4500549912, 58.80147505)
            make_face()
            # Profile area: 2.6538492311, perimeter: 8.3423484986
            with BuildLine():
                Line((-2.5399999619, 6.3499999046), (-1.2789884109, 3.792369513))
                Line((-3.8010115128, 3.792369513), (-2.5399999619, 6.3499999046))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, 60.2338470791, 59.5323058417)
            make_face()
            # Profile area: 20.263760498, perimeter: 16.0499932223
            with BuildLine():
                Line((-3.8160173283, -0.608719386), (-3.756811202, -0.5926163814))
                Line((-3.7236681677, -0.6598383127), (-3.756811202, -0.5926163814))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, -117.7756791038, 56.9858506278)
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, -60.789828476, 30.2489313345)
                Line((-0.3523826649, 0.2967907261), (-0.3627918347, 0.3336940144))
                Line((-0.3188743553, 0.3553470449), (-0.3627918347, 0.3336940144))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, -29.0189972523, 56.9011530197)
                Line((-0.3259061686, 2.7900623665), (-0.2948652439, 2.775342518))
                Line((-0.3259061686, 2.7900623665), (-0.3187501326, 2.8194289523))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, 29.0132203042, 31.2206267749)
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, 60.2338470791, 59.5323058417)
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, 119.7661529209, 29.807166479)
                Line((-4.7242779862, 2.852673194), (-4.7301858809, 2.8738457486))
                Line((-4.7496122666, 2.8401824055), (-4.7242779862, 2.852673194))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, 150.4500549912, 58.80147505)
                Line((-4.7242779862, 0.330650092), (-4.7561066431, 0.3463428615))
                Line((-4.7242779862, 0.330650092), (-4.7317267058, 0.3037812819))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, -149.6420202105, 29.4851609967)
            make_face()
            # Profile area: 2.5254752866, perimeter: 8.0805948317
            with BuildLine():
                Line((2.194838557, 1.5947055654), (-0.3188743553, 0.3553470449))
                Line((-0.2948652439, 2.775342518), (2.194838557, 1.5947055654))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, -29.0189972523, 56.9011530197)
            make_face()
            # Profile area: 2.5326337221, perimeter: 8.0927207929
            with BuildLine():
                Line((-2.4957996511, -3.150246773), (-3.7236681677, -0.6598383127))
                Line((-1.3004428499, -0.6295020474), (-2.4957996511, -3.150246773))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, -117.7756791038, 56.9858506278)
            make_face()
        # OneSide extrude, distance=2.032
        extrude(amount=2.032)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6684084006, perimeter: 3.9451033422
            with BuildLine():
                Line((-5.0799999237, 4.127499938), (-3.8010115128, 3.792369513))
                Line((-4.7301858809, 2.8738457486), (-5.0799999237, 4.127499938))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, 119.7661529209, 29.807166479)
            make_face()
            # Profile area: 0.6617877061, perimeter: 3.9206798711
            with BuildLine():
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, -149.6420202105, 29.4851609967)
                Line((-4.7317267058, 0.3037812819), (-5.0799999237, -0.9524999857))
                Line((-5.0799999237, -0.9524999857), (-3.8160173283, -0.608719386))
            make_face()
            # Profile area: 0.6973899094, perimeter: 4.0525666409
            with BuildLine():
                Line((-0.3187501326, 2.8194289523), (0, 4.127499938))
                Line((0, 4.127499938), (-1.2789884109, 3.792369513))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, 29.0132203042, 31.2206267749)
            make_face()
            # Profile area: 0.6773883014, perimeter: 3.9789685847
            with BuildLine():
                Line((-1.3004428499, -0.6295020474), (0, -0.9524999857))
                Line((0, -0.9524999857), (-0.3523826649, 0.2967907261))
                CenterArc((-2.5399999619, 1.5874999762), 2.5399999619, -60.789828476, 30.2489313345)
            make_face()
        # OneSide extrude, distance=1.778
        extrude(amount=1.778, mode=Mode.ADD)
    return part.part


def model_132529_38b4798b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 38 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.005, perimeter: 0.3
            with BuildLine():
                Line((0.2, 0.3), (0.2, 0.4))
                Line((0.2, 0.4), (0.15, 0.4))
                Line((0.15, 0.4), (0.15, 0.3))
                Line((0.15, 0.3), (0.2, 0.3))
            make_face()
            # Profile area: 0.005, perimeter: 0.3
            with BuildLine():
                Line((0.825, 1.745), (0.825, 1.795))
                Line((0.825, 1.795), (0.725, 1.795))
                Line((0.725, 1.795), (0.725, 1.745))
                Line((0.725, 1.745), (0.825, 1.745))
            make_face()
            # Profile area: 0.0036, perimeter: 0.24
            with BuildLine():
                Line((0.145, 1.6), (0.205, 1.6))
                Line((0.145, 1.54), (0.145, 1.6))
                Line((0.205, 1.54), (0.145, 1.54))
                Line((0.205, 1.6), (0.205, 1.54))
            make_face()
            # Profile area: 0.0036, perimeter: 0.24
            with BuildLine():
                Line((1.345, 1.6), (1.345, 1.54))
                Line((1.345, 1.54), (1.405, 1.54))
                Line((1.405, 1.54), (1.405, 1.6))
                Line((1.405, 1.6), (1.345, 1.6))
            make_face()
            # Profile area: 0.005, perimeter: 0.3
            with BuildLine():
                Line((1.35, 0.4), (1.35, 0.3))
                Line((1.35, 0.3), (1.4, 0.3))
                Line((1.4, 0.3), (1.4, 0.4))
                Line((1.4, 0.4), (1.35, 0.4))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 38 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9383, perimeter: 8.3
            with BuildLine():
                Line((0, 1.91), (0, 0))
                Line((0, 0), (1.55, 0))
                Line((1.55, 0), (1.55, 1.91))
                Line((1.55, 1.91), (0, 1.91))
            make_face()
            with BuildLine():
                Line((0.205, 1.6), (0.205, 1.54))
                Line((0.205, 1.54), (0.145, 1.54))
                Line((0.145, 1.54), (0.145, 1.6))
                Line((0.145, 1.6), (0.205, 1.6))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.725, 1.745), (0.825, 1.745))
                Line((0.725, 1.795), (0.725, 1.745))
                Line((0.825, 1.795), (0.725, 1.795))
                Line((0.825, 1.745), (0.825, 1.795))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.15, 0.3), (0.2, 0.3))
                Line((0.15, 0.4), (0.15, 0.3))
                Line((0.2, 0.4), (0.15, 0.4))
                Line((0.2, 0.3), (0.2, 0.4))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.4, 0.4), (1.35, 0.4))
                Line((1.4, 0.3), (1.4, 0.4))
                Line((1.35, 0.3), (1.4, 0.3))
                Line((1.35, 0.4), (1.35, 0.3))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.405, 1.6), (1.345, 1.6))
                Line((1.405, 1.54), (1.405, 1.6))
                Line((1.345, 1.54), (1.405, 1.54))
                Line((1.345, 1.6), (1.345, 1.54))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0036, perimeter: 0.24
            with BuildLine():
                Line((0.145, 1.6), (0.205, 1.6))
                Line((0.145, 1.54), (0.145, 1.6))
                Line((0.205, 1.54), (0.145, 1.54))
                Line((0.205, 1.6), (0.205, 1.54))
            make_face()
            # Profile area: 0.005, perimeter: 0.3
            with BuildLine():
                Line((0.825, 1.745), (0.825, 1.795))
                Line((0.825, 1.795), (0.725, 1.795))
                Line((0.725, 1.795), (0.725, 1.745))
                Line((0.725, 1.745), (0.825, 1.745))
            make_face()
            # Profile area: 0.005, perimeter: 0.3
            with BuildLine():
                Line((0.2, 0.3), (0.2, 0.4))
                Line((0.2, 0.4), (0.15, 0.4))
                Line((0.15, 0.4), (0.15, 0.3))
                Line((0.15, 0.3), (0.2, 0.3))
            make_face()
            # Profile area: 0.005, perimeter: 0.3
            with BuildLine():
                Line((1.35, 0.4), (1.35, 0.3))
                Line((1.35, 0.3), (1.4, 0.3))
                Line((1.4, 0.3), (1.4, 0.4))
                Line((1.4, 0.4), (1.35, 0.4))
            make_face()
            # Profile area: 0.0036, perimeter: 0.24
            with BuildLine():
                Line((1.345, 1.6), (1.345, 1.54))
                Line((1.345, 1.54), (1.405, 1.54))
                Line((1.405, 1.54), (1.405, 1.6))
                Line((1.405, 1.6), (1.345, 1.6))
            make_face()
        # OneSide extrude, distance=1.53
        extrude(amount=1.53)
    return part.part


def model_132626_f1f9e3a7_0000():
    """Model: cylinder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0609287715, perimeter: 1.0000851773
            with BuildLine():
                CenterArc((0, 0), 1.4, 171.8666597067, 16.3845381424)
                CenterArc((-1.3999992595, -0.0014399014), 0.2000044249, -85.8449366866, 171.8077309288)
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)
    return part.part


def model_132642_26b12db4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((10.5, -10.5), (0.5, -10.5))
                Line((10.5, -0.5), (10.5, -10.5))
                Line((0.5, -0.5), (10.5, -0.5))
                Line((0.5, -10.5), (0.5, -0.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-8.5740316717, 2.4225529355)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-2.4246231735, 2.4239046597)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-2.4211541121, 8.5726486061)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-8.5754142498, 8.5760578569)):
                Circle(0.6)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)
    return part.part


def model_132685_6ff62835_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 191.1870399846, perimeter: 52.781923012
            with BuildLine():
                CenterArc((0, 3.5), 4, 20.0000050378, 140)
                Line((-3.7587706034, 4.8680802428), (-7.5, -5.4108658574))
                Line((-7.5, -5.4108658574), (-7.5, -8.1222971704))
                CenterArc((0.0000008971, 4.8680833685), 15, -120.0000039567, 60)
                Line((7.5, -8.1222982062), (7.5, -5.4108602331))
                Line((7.5, -5.4108602331), (3.7587703629, 4.8680809038))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_132687_d1a27238_0001():
    """Model: Cloud Saving USB v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((1, -0.5), (0, -0.5))
                Line((1, 0), (1, -0.5))
                Line((0, 0), (1, 0))
                Line((0, -0.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.340000025, perimeter: 6.8000000566
            with BuildLine():
                Line((0.1000000015, -0.1000000015), (0.1000000015, 0.6000000089))
                Line((0.1000000015, 0.6000000089), (-1.1000000164, 0.6000000089))
                Line((-1.1000000164, 0.6000000089), (-1.1000000164, -0.1000000015))
                Line((-1.1000000164, -0.1000000015), (0.1000000015, -0.1000000015))
            make_face()
            with BuildLine():
                Line((-1, 0), (0, 0))
                Line((-1, 0.5), (-1, 0))
                Line((0, 0.5), (-1, 0.5))
                Line((0, 0), (0, 0.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((0, 0), (0, 0.5))
                Line((0, 0.5), (-1, 0.5))
                Line((-1, 0.5), (-1, 0))
                Line((-1, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_132796_53ed101d_0001():
    """Model: stopper2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-42.1153718959, -1.1667238268)):
                Circle(0.5)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-42.1153718959, -1.1667238268)):
                Circle(0.25)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_132863_90d729e2_0000():
    """Model: Behuizing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.0793380069, perimeter: 54.8422217591
            with BuildLine():
                CenterArc((0.3, -5.949627094), 0.3, -180, 79.6951535312)
                Line((0.2463343685, -6.244788067), (1.5321114562, -6.4785657193))
                CenterArc((1.55, -6.3801787283), 0.1, -100.3048464688, 100.3048464688)
                Line((1.65, -6.3801787283), (1.65, -6.2))
                Line((1.65, -6.2), (4.85, -6.2))
                Line((4.85, -6.2), (4.85, -6.3801787283))
                CenterArc((4.95, -6.3801787283), 0.1, 180, 100.3048464688)
                Line((6.2536656315, -6.244788067), (4.9678885438, -6.4785657193))
                CenterArc((6.2, -5.949627094), 0.3, -79.6951535312, 79.6951535312)
                Line((6.5, -0.3), (6.5, -5.949627094))
                CenterArc((6.2, -0.3), 0.3, 0, 90)
                Line((0.3, 0), (6.2, 0))
                CenterArc((0.3, -0.3), 0.3, 90, 90)
                Line((0, -5.949627094), (0, -0.3))
            make_face()
            with BuildLine():
                Line((0.6184852767, -1.1902215883), (5.9039002661, -1.1902215883))
                CenterArc((0.6184852767, -0.9902215883), 0.2, 180, 90)
                Line((0.4184852767, -0.6378982438), (0.4184852767, -0.9902215883))
                CenterArc((0.6184852767, -0.6378982438), 0.2, 90, 90)
                Line((5.9039002661, -0.4378982438), (0.6184852767, -0.4378982438))
                CenterArc((5.9039002661, -0.6378982438), 0.2, 0, 90)
                Line((6.1039002661, -0.9902215883), (6.1039002661, -0.6378982438))
                CenterArc((5.9039002661, -0.9902215883), 0.2, -90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((5.9039002661, -1.3944236389), (0.6184852767, -1.3944236389))
                CenterArc((5.9039002661, -1.5944236389), 0.2, 0, 90)
                Line((6.1039002661, -4.0854947772), (6.1039002661, -1.5944236389))
                CenterArc((5.9039002661, -4.0854947772), 0.2, -90, 90)
                Line((0.6184852767, -4.2854947772), (5.9039002661, -4.2854947772))
                CenterArc((0.6184852767, -4.0854947772), 0.2, -180, 90)
                Line((0.4184852767, -1.5944236389), (0.4184852767, -4.0854947772))
                CenterArc((0.6184852767, -1.5944236389), 0.2, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.3893431132, perimeter: 23.635908928
            with BuildLine():
                CenterArc((5.9039002661, -0.9902215883), 0.2, -90, 90)
                Line((6.1039002661, -0.9902215883), (6.1039002661, -0.6378982438))
                CenterArc((5.9039002661, -0.6378982438), 0.2, 0, 90)
                Line((5.9039002661, -0.4378982438), (0.6184852767, -0.4378982438))
                CenterArc((0.6184852767, -0.6378982438), 0.2, 90, 90)
                Line((0.4184852767, -0.6378982438), (0.4184852767, -0.9902215883))
                CenterArc((0.6184852767, -0.9902215883), 0.2, 180, 90)
                Line((0.6184852767, -1.1902215883), (5.9039002661, -1.1902215883))
            make_face()
            with BuildLine():
                Line((5.8039002661, -0.6378982438), (0.7184852767, -0.6378982438))
                CenterArc((5.8039002661, -0.7378982438), 0.1, 0, 90)
                Line((5.9039002661, -0.8902215883), (5.9039002661, -0.7378982438))
                CenterArc((5.8039002661, -0.8902215883), 0.1, -90, 90)
                Line((0.7184852767, -0.9902215883), (5.8039002661, -0.9902215883))
                CenterArc((0.7184852767, -0.8902215883), 0.1, -180, 90)
                Line((0.6184852767, -0.7378982438), (0.6184852767, -0.8902215883))
                CenterArc((0.7184852767, -0.7378982438), 0.1, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.8535910129, perimeter: 11.1037951986
            with BuildLine():
                CenterArc((0.7184852767, -0.7378982438), 0.1, 90, 90)
                Line((0.6184852767, -0.7378982438), (0.6184852767, -0.8902215883))
                CenterArc((0.7184852767, -0.8902215883), 0.1, -180, 90)
                Line((0.7184852767, -0.9902215883), (5.8039002661, -0.9902215883))
                CenterArc((5.8039002661, -0.8902215883), 0.1, -90, 90)
                Line((5.9039002661, -0.8902215883), (5.9039002661, -0.7378982438))
                CenterArc((5.8039002661, -0.7378982438), 0.1, 0, 90)
                Line((5.8039002661, -0.6378982438), (0.7184852767, -0.6378982438))
            make_face()
            # Profile area: 3.2448422307, perimeter: 32.1909001029
            with BuildLine():
                CenterArc((0.6184852767, -1.5944236389), 0.2, 90, 90)
                Line((0.4184852767, -1.5944236389), (0.4184852767, -4.0854947772))
                CenterArc((0.6184852767, -4.0854947772), 0.2, -180, 90)
                Line((0.6184852767, -4.2854947772), (5.9039002661, -4.2854947772))
                CenterArc((5.9039002661, -4.0854947772), 0.2, -90, 90)
                Line((6.1039002661, -4.0854947772), (6.1039002661, -1.5944236389))
                CenterArc((5.9039002661, -1.5944236389), 0.2, 0, 90)
                Line((5.9039002661, -1.3944236389), (0.6184852767, -1.3944236389))
            make_face()
            with BuildLine():
                Line((5.9039002661, -3.9854947772), (5.9039002661, -1.6944236389))
                CenterArc((5.8039002661, -3.9854947772), 0.1, -90, 90)
                Line((0.7184852767, -4.0854947772), (5.8039002661, -4.0854947772))
                CenterArc((0.7184852767, -3.9854947772), 0.1, 180, 90)
                Line((0.6184852767, -1.6944236389), (0.6184852767, -3.9854947772))
                CenterArc((0.7184852767, -1.6944236389), 0.1, 90, 90)
                Line((5.8039002661, -1.5944236389), (0.7184852767, -1.5944236389))
                CenterArc((5.8039002661, -1.6944236389), 0.1, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 13.1577606605, perimeter: 15.3812907861
            with BuildLine():
                CenterArc((5.8039002661, -1.6944236389), 0.1, 0, 90)
                Line((5.8039002661, -1.5944236389), (0.7184852767, -1.5944236389))
                CenterArc((0.7184852767, -1.6944236389), 0.1, 90, 90)
                Line((0.6184852767, -1.6944236389), (0.6184852767, -3.9854947772))
                CenterArc((0.7184852767, -3.9854947772), 0.1, 180, 90)
                Line((0.7184852767, -4.0854947772), (5.8039002661, -4.0854947772))
                CenterArc((5.8039002661, -3.9854947772), 0.1, -90, 90)
                Line((5.9039002661, -3.9854947772), (5.9039002661, -1.6944236389))
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2448422307, perimeter: 32.1909001029
            with BuildLine():
                CenterArc((0.6184852767, -1.5944236389), 0.2, 90, 90)
                Line((0.4184852767, -1.5944236389), (0.4184852767, -4.0854947772))
                CenterArc((0.6184852767, -4.0854947772), 0.2, -180, 90)
                Line((0.6184852767, -4.2854947772), (5.9039002661, -4.2854947772))
                CenterArc((5.9039002661, -4.0854947772), 0.2, -90, 90)
                Line((6.1039002661, -4.0854947772), (6.1039002661, -1.5944236389))
                CenterArc((5.9039002661, -1.5944236389), 0.2, 0, 90)
                Line((5.9039002661, -1.3944236389), (0.6184852767, -1.3944236389))
            make_face()
            with BuildLine():
                Line((5.9039002661, -3.9854947772), (5.9039002661, -1.6944236389))
                CenterArc((5.8039002661, -3.9854947772), 0.1, -90, 90)
                Line((0.7184852767, -4.0854947772), (5.8039002661, -4.0854947772))
                CenterArc((0.7184852767, -3.9854947772), 0.1, 180, 90)
                Line((0.6184852767, -1.6944236389), (0.6184852767, -3.9854947772))
                CenterArc((0.7184852767, -1.6944236389), 0.1, 90, 90)
                Line((5.8039002661, -1.5944236389), (0.7184852767, -1.5944236389))
                CenterArc((5.8039002661, -1.6944236389), 0.1, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.3893431132, perimeter: 23.635908928
            with BuildLine():
                CenterArc((5.9039002661, -0.9902215883), 0.2, -90, 90)
                Line((6.1039002661, -0.9902215883), (6.1039002661, -0.6378982438))
                CenterArc((5.9039002661, -0.6378982438), 0.2, 0, 90)
                Line((5.9039002661, -0.4378982438), (0.6184852767, -0.4378982438))
                CenterArc((0.6184852767, -0.6378982438), 0.2, 90, 90)
                Line((0.4184852767, -0.6378982438), (0.4184852767, -0.9902215883))
                CenterArc((0.6184852767, -0.9902215883), 0.2, 180, 90)
                Line((0.6184852767, -1.1902215883), (5.9039002661, -1.1902215883))
            make_face()
            with BuildLine():
                Line((5.8039002661, -0.6378982438), (0.7184852767, -0.6378982438))
                CenterArc((5.8039002661, -0.7378982438), 0.1, 0, 90)
                Line((5.9039002661, -0.8902215883), (5.9039002661, -0.7378982438))
                CenterArc((5.8039002661, -0.8902215883), 0.1, -90, 90)
                Line((0.7184852767, -0.9902215883), (5.8039002661, -0.9902215883))
                CenterArc((0.7184852767, -0.8902215883), 0.1, -180, 90)
                Line((0.6184852767, -0.7378982438), (0.6184852767, -0.8902215883))
                CenterArc((0.7184852767, -0.7378982438), 0.1, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.467858986, perimeter: 9.6632712466
            with BuildLine():
                Line((-4.7606763357, -0.2441950049), (-1.7379675016, -0.2441950049))
                Line((-4.7606763357, -2.0531217942), (-4.7606763357, -0.2441950049))
                Line((-1.7379675016, -2.0531217942), (-4.7606763357, -2.0531217942))
                Line((-1.7379675016, -0.2441950049), (-1.7379675016, -2.0531217942))
            make_face()
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)
    return part.part


def model_133109_dbf8891f_0004():
    """Model: DeltiQ"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 625.2703415324, perimeter: 114
            with BuildLine():
                Line((-235, -55.1720612173), (-197, -55.1720612173))
                Line((-197, -55.1720612173), (-216, -22.2630958735))
                Line((-216, -22.2630958735), (-235, -55.1720612173))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 80, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((-218, -25.7271974887), (-218, -29.7271974887))
                Line((-218, -29.7271974887), (-214, -29.7271974887))
                Line((-214, -29.7271974887), (-214, -25.7271974887))
                Line((-214, -25.7271974887), (-218, -25.7271974887))
            make_face()
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((-231, -55.1720612173), (-227.5358983849, -53.1720612173))
                Line((-227.5358983849, -53.1720612173), (-229.5358983849, -49.7079596022))
                Line((-229.5358983849, -49.7079596022), (-233, -51.7079596022))
                Line((-231, -55.1720612173), (-233, -51.7079596022))
            make_face()
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((-201, -55.1720612173), (-199, -51.7079596022))
                Line((-202.4641016151, -49.7079596022), (-199, -51.7079596022))
                Line((-204.4641016151, -53.1720612173), (-202.4641016151, -49.7079596022))
                Line((-201, -55.1720612173), (-204.4641016151, -53.1720612173))
            make_face()
        # OneSide extrude, distance=70
        extrude(amount=70, mode=Mode.ADD)
    return part.part


def model_133439_0ddc18c5_0000():
    """Model: lbyj v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.4446399139, perimeter: 24.6602140935
            with BuildLine():
                Line((1.3506063094, 0.5731447136), (0.4318650855, 0.2899412557))
                Line((0.4318650855, 0.2899412557), (0.3070922115, 0.2514798169))
                CenterArc((0.8602828361, -1.5431276199), 1.8779338964, 107.1319983055, 80.7298281172)
                Line((-1.0000000149, -1.8000000268), (-0.8114629172, -2.4209574299))
                CenterArc((0.0024631631, -2.1738305575), 0.8506158682, -163.1104909017, 59.3408116532)
                Line((-0.200000003, -3.0000000447), (0.6123816267, -3.0225388241))
                Line((0.6123816267, -3.0225388241), (1.8000000268, -3.0000000447))
                Line((1.8000000268, -3.0000000447), (2.5000000373, -2.5000000373))
                Line((2.5000000373, -2.5000000373), (2.8000000417, -2.5000000373))
                Line((2.8000000417, -2.5000000373), (3.4000000507, -2.5000000373))
                Line((3.4000000507, -2.5000000373), (3.5000000522, -2.5000000373))
                Line((3.5000000522, -2.5000000373), (3.8340952852, -2.550000038))
                Line((3.8340952852, -2.550000038), (4.2401456816, -2.6107686995))
                Line((4.2401456816, -2.6107686995), (4.5415193311, -2.6558716558))
                Line((4.5415193311, -2.6558716558), (4.9036692413, -2.7100702615))
                Line((4.9036692413, -2.7100702615), (5.2000000775, -2.7100702615))
                Line((5.2000000775, -2.7100702615), (5.500000082, -2.7100702615))
                Line((5.500000082, -2.7100702615), (5.7418365928, -2.7100702615))
                Line((5.7418365928, -2.7100702615), (6.0000000894, -2.7100702615))
                Line((6.0000000894, -2.7100702615), (6.1955916102, -2.6829709586))
                Line((6.1955916102, -2.6829709586), (6.4424961339, -2.6244663582))
                Line((6.4424961339, -2.6244663582), (6.6804548415, -2.5421648503))
                Line((6.6804548415, -2.5421648503), (6.9254784175, -2.457419854))
                Line((6.9254784175, -2.457419854), (7.1170106659, -2.3525135495))
                Line((7.1170106659, -2.3525135495), (7.2762461921, -2.2380071037))
                Line((7.2762461921, -2.2380071037), (7.4560470454, -2.1087121081))
                Line((7.4560470454, -2.1087121081), (7.5820759285, -2.0180845966))
                Line((7.5820759285, -2.0180845966), (7.6823862419, -1.8873311136))
                Line((7.6823862419, -1.8873311136), (7.7306936487, -1.7477763828))
                Line((7.7306936487, -1.7477763828), (7.7671103287, -1.6425726404))
                Line((7.7671103287, -1.6425726404), (7.7671103287, -1.5294984706))
                Line((7.7671103287, -1.5294984706), (7.7489019887, -1.4185703513))
                Line((7.7489019887, -1.4185703513), (7.6805970786, -1.2790156205))
                Line((7.6805970786, -1.2790156205), (7.6000001132, -1.1500000171))
                Line((7.6000001132, -1.1500000171), (7.5111879842, -1.0078339895))
                Line((7.5111879842, -1.0078339895), (7.3818068217, -0.9569662418))
                Line((7.3818068217, -0.9569662418), (7.3000001088, -0.9569662418))
                CenterArc((7.3000001088, -1.0475718994), 0.0906056576, 90, 63.9866286773)
                Line((7.2185735547, -1.0078339895), (7.1877712121, -1.070950762))
                Line((7.1877712121, -1.070950762), (7.0751507436, -1.3573988119))
                Line((7.0751507436, -1.3573988119), (7.0000001043, -1.4000000209))
                CenterArc((6.9203433837, -1.2594816268), 0.1615258871, -95.1339207965, 34.681847374)
                Line((6.9058894066, -1.4203595145), (6.7000000998, -1.4203595145))
                Line((6.7000000998, -1.4203595145), (6.5000000969, -1.4203595145))
                Line((6.5000000969, -1.4203595145), (6.1669649988, -1.3613171284))
                Line((6.1669649988, -1.3613171284), (5.9415304337, -1.2843831102))
                Line((5.9415304337, -1.2843831102), (5.5872761171, -1.1287259104))
                Line((5.5872761171, -1.1287259104), (5.2603105847, -0.9850592371))
                Line((5.2603105847, -0.9850592371), (4.7500000708, -0.7500000112))
                Line((4.7500000708, -0.7500000112), (4.4469325091, -0.6104010327))
                Line((4.4469325091, -0.6104010327), (4.1143847402, -0.4969125084))
                Line((4.1143847402, -0.4969125084), (3.9146004585, -0.4223964894))
                Line((3.9146004585, -0.4223964894), (3.6500000544, -0.4223964894))
                Line((3.6500000544, -0.4223964894), (3.4500000514, -0.4223964894))
                Line((3.4500000514, -0.4223964894), (3.2756772434, -0.4361982481))
                Line((3.2756772434, -0.4361982481), (3.1522249815, -0.4738921738))
                Line((3.1522249815, -0.4738921738), (3.0353868769, -0.4831426633))
                Line((3.0353868769, -0.4831426633), (2.9186895443, -0.4923820075))
                Line((2.9186895443, -0.4923820075), (2.7570395274, -0.4372157319))
                Line((2.7570395274, -0.4372157319), (2.6513312397, -0.3462866519))
                Line((2.6513312397, -0.3462866519), (2.4892302723, -0.2068492232))
                Line((2.4892302723, -0.2068492232), (2.2386766887, 0.008674151))
                Line((2.2386766887, 0.008674151), (1.7599556199, 0.4204646293))
                Line((1.7599556199, 0.4204646293), (1.5451547294, 0.5005815788))
                Line((1.5451547294, 0.5005815788), (1.3521399041, 0.5725727097))
                Line((1.3506063094, 0.5731447136), (1.3521399041, 0.5725727097))
            make_face()
            with BuildLine():
                CenterArc((0.9354698546, -2.3657423187), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.3995769189, perimeter: 27.2643932712
            with BuildLine():
                CenterArc((-3.6500000544, 4.2000000626), 2.0155644671, -43.9949139947, 20.6096929375)
                CenterArc((-3.1500000469, 3.5500000529), 1.358307791, -6.3401917459, 90)
                Line((-3.0000000447, 4.900000073), (-3.8000000566, 5.100000076))
                Line((-3.8000000566, 5.100000076), (-4.1000000611, 5.300000079))
                CenterArc((-4.2327769882, 5.1008346883), 0.2393670095, 56.309932474, 99.2159730456)
                Line((-4.4506365549, 5.2000000775), (-5.0000000745, 4.900000073))
                CenterArc((-4.7618994889, 4.4639874938), 0.4967885447, 118.638358262, 108.4732507782)
                CenterArc((-4.4341956345, 3.8000000566), 0.7302708792, 155.7444937308, 87.5924495402)
                Line((-4.7618994889, 3.1473855143), (-4.2000000626, 2.8000000417))
                Line((-4.2000000626, 2.8000000417), (-5.0000000745, 1.7000000253))
                CenterArc((-3.3340909588, 0.7477272839), 1.9188737728, 150.2467015179, 73.2945227396)
                CenterArc((-2.6348058181, -0.8219261615), 2.1048719606, 173.2394303382, 285.9130428592)
                CenterArc((-2.8477021577, 1.5729319272), 0.3394320939, 138.0127875042, 110.9387732493)
                Line((-2.2000000328, 2.8000000417), (-3.1000000462, 1.8000000268))
            make_face()
            with BuildLine():
                CenterArc((-2.9161382962, -2.0415787757), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_133466_609f225b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5687861353, perimeter: 2.6734953482
            with Locations((0.3500000052, -0.0500000007)):
                Circle(0.4255)
        # OneSide extrude, distance=0.66
        extrude(amount=0.66)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6983342755, perimeter: 3.0569189595
            with BuildLine():
                Line((1.5000000224, 0.4199999906), (1.4570000224, 0.4199999906))
                Line((1.4570000224, 0.4199999906), (1.4570000224, 0.3680288438))
                CenterArc((1.5000000224, -0.1000000015), 0.47, 95.2492947698, 349.5014104605)
                Line((1.5430000224, 0.4199999906), (1.5430000224, 0.3680288438))
                Line((1.5000000224, 0.4199999906), (1.5430000224, 0.4199999906))
            make_face()
        # OneSide extrude, distance=0.023
        extrude(amount=0.023)
    return part.part


def model_133564_b5340c41_0003():
    """Model: displacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.9157906816, perimeter: 7.0685834706
            with BuildLine():
                CenterArc((0, 0), 0.975, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=6.2
        extrude(amount=6.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_133710_00be7f31_0003():
    """Model: Respaldo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 47.2554087077, perimeter: 66.0072116103
            with BuildLine():
                Line((-1.9249306846, 90.9555535399), (-13.6560991456, 61.7176181603))
                Line((-3.3170539653, 91.5141166708), (-1.9249306846, 90.9555535399))
                Line((-15.0482224264, 62.2761812912), (-3.3170539653, 91.5141166708))
                Line((-13.6560991456, 61.7176181603), (-15.0482224264, 62.2761812912))
            make_face()
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((-13.6560991456, 61.7176181603), (-15.0482224264, 62.2761812912))
                Line((-16.9100995292, 57.6357703553), (-15.0482224264, 62.2761812912))
                Line((-15.5179762485, 57.0772072244), (-16.9100995292, 57.6357703553))
                Line((-13.6560991456, 61.7176181603), (-15.5179762485, 57.0772072244))
            make_face()
            # Profile area: 7.0561209281, perimeter: 12.5206974761
            with BuildLine():
                Line((-19.5269057127, 47.0856346879), (-20.9190289935, 47.6441978187))
                Line((-22.7809060963, 43.0037868829), (-20.9190289935, 47.6441978187))
                Line((-21.1683966074, 42.9944987652), (-22.7809060963, 43.0037868829))
                Line((-19.5269057127, 47.0856346879), (-21.1683966074, 42.9944987652))
            make_face()
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((-17.6650286099, 51.7260456238), (-19.0571518906, 52.2846087546))
                Line((-20.9190289935, 47.6441978187), (-19.0571518906, 52.2846087546))
                Line((-19.5269057127, 47.0856346879), (-20.9190289935, 47.6441978187))
                Line((-17.6650286099, 51.7260456238), (-19.5269057127, 47.0856346879))
            make_face()
            # Profile area: 8.6487409325, perimeter: 14.5316545766
            with BuildLine():
                Line((-15.5179762485, 57.0772072244), (-16.9100995292, 57.6357703553))
                Line((-19.0571518906, 52.2846087546), (-16.9100995292, 57.6357703553))
                Line((-17.6650286099, 51.7260456238), (-19.0571518906, 52.2846087546))
                Line((-15.5179762485, 57.0772072244), (-17.6650286099, 51.7260456238))
            make_face()
        # OneSide extrude, distance=-60
        extrude(amount=-60)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((-13.6560991456, 61.7176181603), (-15.0482224264, 62.2761812912))
                Line((-16.9100995292, 57.6357703553), (-15.0482224264, 62.2761812912))
                Line((-15.5179762485, 57.0772072244), (-16.9100995292, 57.6357703553))
                Line((-13.6560991456, 61.7176181603), (-15.5179762485, 57.0772072244))
            make_face()
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((-17.6650286099, 51.7260456238), (-19.0571518906, 52.2846087546))
                Line((-20.9190289935, 47.6441978187), (-19.0571518906, 52.2846087546))
                Line((-19.5269057127, 47.0856346879), (-20.9190289935, 47.6441978187))
                Line((-17.6650286099, 51.7260456238), (-19.5269057127, 47.0856346879))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-60, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((13.6560991456, 61.7176181603), (15.5179762485, 57.0772072244))
                Line((15.5179762485, 57.0772072244), (16.9100995292, 57.6357703553))
                Line((16.9100995292, 57.6357703553), (15.0482224264, 62.2761812912))
                Line((13.6560991456, 61.7176181603), (15.0482224264, 62.2761812912))
            make_face()
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((17.6650286099, 51.7260456238), (19.0571518906, 52.2846087546))
                Line((17.6650286099, 51.7260456238), (19.5269057127, 47.0856346879))
                Line((19.5269057127, 47.0856346879), (20.9190289935, 47.6441978187))
                Line((20.9190289935, 47.6441978187), (19.0571518906, 52.2846087546))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_133742_8d1f00a2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0176714579, perimeter: 0.4712388875
            with Locations((-0.0749999983, 0)):
                Circle(0.0749999983)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


MODELS = {
    "model_122019_6e847ad7_0000": {"func": model_122019_6e847ad7_0000, "volume": 14.9536322218, "area": 108.7308612414},
    "model_122311_477d4e3b_0000": {"func": model_122311_477d4e3b_0000, "volume": 0.1153996873, "area": 3.5820061528},
    "model_122410_506a2f72_0000": {"func": model_122410_506a2f72_0000, "volume": 1.9753389765, "area": 10.6120990872},
    "model_122425_248c57e8_0000": {"func": model_122425_248c57e8_0000, "volume": 127.6595044956, "area": 277.3646370504},
    "model_122425_248c57e8_0002": {"func": model_122425_248c57e8_0002, "volume": 174.1118376652, "area": 326.7005871403},
    "model_122511_ab7ee8b4_0001": {"func": model_122511_ab7ee8b4_0001, "volume": 105.193, "area": 253.806},
    "model_122752_229f274c_0000": {"func": model_122752_229f274c_0000, "volume": 27.2334255591, "area": 74.7229877049},
    "model_123336_d21b9492_0000": {"func": model_123336_d21b9492_0000, "volume": 288.412037578, "area": 345.2034516112},
    "model_123496_74cb10dc_0002": {"func": model_123496_74cb10dc_0002, "volume": 15.2571971492, "area": 96.9117228897},
    "model_124497_5c00f42d_0004": {"func": model_124497_5c00f42d_0004, "volume": 15.0988117862, "area": 50.4085369235},
    "model_124497_5c00f42d_0010": {"func": model_124497_5c00f42d_0010, "volume": 3.3128444327, "area": 21.287128952},
    "model_124497_5c00f42d_0013": {"func": model_124497_5c00f42d_0013, "volume": 209.9065015646, "area": 302.482973359},
    "model_124889_a069569f_0000": {"func": model_124889_a069569f_0000, "volume": 26.9770729171, "area": 125.6512848415},
    "model_124890_897c868e_0000": {"func": model_124890_897c868e_0000, "volume": 26.1978221299, "area": 122.8674631132},
    "model_125002_7287b175_0000": {"func": model_125002_7287b175_0000, "volume": 36.6135805, "area": 362.1607416818},
    "model_125152_65ed33fd_0000": {"func": model_125152_65ed33fd_0000, "volume": 31.6484043923, "area": 145.3929080081},
    "model_125220_dd31e7cf_0000": {"func": model_125220_dd31e7cf_0000, "volume": 17.9658257481, "area": 88.7902918484},
    "model_125226_291284e7_0000": {"func": model_125226_291284e7_0000, "volume": 5.8826323197, "area": 107.897999769},
    "model_125991_52824da3_0003": {"func": model_125991_52824da3_0003, "volume": 1.4223693546, "area": 8.3176340293},
    "model_126491_c931419a_0003": {"func": model_126491_c931419a_0003, "volume": 0.4455976237, "area": 4.0848923377},
    "model_127646_b88ed13f_0008": {"func": model_127646_b88ed13f_0008, "volume": 8.3182137091, "area": 36.2691965926},
    "model_127646_b88ed13f_0014": {"func": model_127646_b88ed13f_0014, "volume": 12.4149797091, "area": 39.4949965926},
    "model_127646_b88ed13f_0015": {"func": model_127646_b88ed13f_0015, "volume": 8.3182137091, "area": 36.2691965926},
    "model_127646_b88ed13f_0017": {"func": model_127646_b88ed13f_0017, "volume": 12.4149797091, "area": 39.4949965926},
    "model_127902_e55aaac6_0000": {"func": model_127902_e55aaac6_0000, "volume": 4350.1850495478, "area": 7114.1730065289},
    "model_128043_0017e0c6_0000": {"func": model_128043_0017e0c6_0000, "volume": 0.1047653299, "area": 1.6047171622},
    "model_128043_13b28efa_0000": {"func": model_128043_13b28efa_0000, "volume": 0.0604756586, "area": 4.8812495855},
    "model_128043_30303218_0000": {"func": model_128043_30303218_0000, "volume": 0.1330396638, "area": 1.9817082806},
    "model_128043_464a2744_0000": {"func": model_128043_464a2744_0000, "volume": 1.1026990214, "area": 6.8486719848},
    "model_128043_726cf3be_0000": {"func": model_128043_726cf3be_0000, "volume": 1.0053096491, "area": 11.1840698468},
    "model_128043_76778a7f_0000": {"func": model_128043_76778a7f_0000, "volume": 0.0459173509, "area": 0.9876290507},
    "model_128043_a1b3b620_0000": {"func": model_128043_a1b3b620_0000, "volume": 17.5728912069, "area": 70.0103922852},
    "model_128281_be786720_0000": {"func": model_128281_be786720_0000, "volume": 669.6820179976, "area": 826.3536421583},
    "model_128355_739c5ce0_0001": {"func": model_128355_739c5ce0_0001, "volume": 1520000, "area": 319600},
    "model_128646_ed76c192_0002": {"func": model_128646_ed76c192_0002, "volume": 371.6164282908, "area": 355.2207082289},
    "model_128656_22e204c6_0000": {"func": model_128656_22e204c6_0000, "volume": 1161.4123439737, "area": 876.9892295885},
    "model_128656_22e204c6_0002": {"func": model_128656_22e204c6_0002, "volume": 53378.8531515883, "area": 14397.79944538},
    "model_128656_22e204c6_0005": {"func": model_128656_22e204c6_0005, "volume": 18005.7682191212, "area": 5508.5059651951},
    "model_128996_5047840e_0000": {"func": model_128996_5047840e_0000, "volume": 0.1108473355, "area": 1.4423007676},
    "model_128996_53a64f7e_0000": {"func": model_128996_53a64f7e_0000, "volume": 0.3031636911, "area": 2.7174776454},
    "model_128996_69e2b8a9_0000": {"func": model_128996_69e2b8a9_0000, "volume": 1.4922565175, "area": 8.7964594909},
    "model_128996_94d0d065_0000": {"func": model_128996_94d0d065_0000, "volume": 10.4959291886, "area": 84.1511497809},
    "model_128996_94eea973_0000": {"func": model_128996_94eea973_0000, "volume": 0.2853940576, "area": 2.8549223239},
    "model_128996_c40385f3_0000": {"func": model_128996_c40385f3_0000, "volume": 2034.0424796047, "area": 2698.6274225363},
    "model_128996_d4b68e98_0000": {"func": model_128996_d4b68e98_0000, "volume": 9.6311983733, "area": 66.7675170794},
    "model_128996_dab9e8bf_0000": {"func": model_128996_dab9e8bf_0000, "volume": 7.0324551551, "area": 36.756634047},
    "model_128996_ef7e7c3d_0000": {"func": model_128996_ef7e7c3d_0000, "volume": 3.119601505, "area": 13.1946891451},
    "model_128996_f46b97ad_0000": {"func": model_128996_f46b97ad_0000, "volume": 3.0536280593, "area": 20.4203522483},
    "model_129006_3364d0a7_0000": {"func": model_129006_3364d0a7_0000, "volume": 94.6337046419, "area": 216.6320879819},
    "model_129012_576921da_0000": {"func": model_129012_576921da_0000, "volume": 229.5660140352, "area": 227.5830070176},
    "model_129092_5eb5a5c6_0000": {"func": model_129092_5eb5a5c6_0000, "volume": 2.9820691446, "area": 17.4141667201},
    "model_129092_5eb5a5c6_0001": {"func": model_129092_5eb5a5c6_0001, "volume": 3.0841953427, "area": 17.9166242146},
    "model_129092_5eb5a5c6_0003": {"func": model_129092_5eb5a5c6_0003, "volume": 0.3423993244, "area": 4.8616132139},
    "model_129401_7686af57_0001": {"func": model_129401_7686af57_0001, "volume": 755.1690403701, "area": 1309.60763766},
    "model_129409_0664bc6f_0000": {"func": model_129409_0664bc6f_0000, "volume": 8.1325807416, "area": 41.5474311989},
    "model_129418_723e4053_0000": {"func": model_129418_723e4053_0000, "volume": 1.5570796476, "area": 17.7991150155},
    "model_129618_2962c248_0000": {"func": model_129618_2962c248_0000, "volume": 21.477632078, "area": 58.135644108},
    "model_129935_8a7613e5_0000": {"func": model_129935_8a7613e5_0000, "volume": 18.1338053289, "area": 132.8739822369},
    "model_130109_be1c92dd_0000": {"func": model_130109_be1c92dd_0000, "volume": 8.4662907614, "area": 40.916630792},
    "model_130569_ef78205f_0000": {"func": model_130569_ef78205f_0000, "volume": 75, "area": 165},
    "model_130656_cd404fec_0000": {"func": model_130656_cd404fec_0000, "volume": 4.80663676, "area": 32.6097317443},
    "model_130724_ac486cd1_0000": {"func": model_130724_ac486cd1_0000, "volume": 927.5738813341, "area": 2295.1739567063},
    "model_130757_46123542_0000": {"func": model_130757_46123542_0000, "volume": 0.0424556795, "area": 0.7048555817},
    "model_130849_deb0581b_0000": {"func": model_130849_deb0581b_0000, "volume": 556.2117614689, "area": 1875.9130083338},
    "model_130966_95aacf5a_0002": {"func": model_130966_95aacf5a_0002, "volume": 0.5232601229, "area": 5.8583678211},
    "model_130996_b842b511_0010": {"func": model_130996_b842b511_0010, "volume": 62.6449592095, "area": 155.7378640152},
    "model_131068_085c0ed9_0002": {"func": model_131068_085c0ed9_0002, "volume": 197.444190109, "area": 333.5635709842},
    "model_131068_085c0ed9_0003": {"func": model_131068_085c0ed9_0003, "volume": 38.6941354487, "area": 88.2446011534},
    "model_131335_b4d05d31_0000": {"func": model_131335_b4d05d31_0000, "volume": 467.1076284018, "area": 485.0837558619},
    "model_131466_90a4c082_0000": {"func": model_131466_90a4c082_0000, "volume": 1.2295708892, "area": 11.8521018479},
    "model_131568_0e01803b_0000": {"func": model_131568_0e01803b_0000, "volume": 0.0004475928, "area": 0.9034596452},
    "model_131816_9dc8a682_0001": {"func": model_131816_9dc8a682_0001, "volume": 150.0751760504, "area": 275.9480683757},
    "model_132156_cd3f1428_0000": {"func": model_132156_cd3f1428_0000, "volume": 66.9438180142, "area": 133.1422905361},
    "model_132529_38b4798b_0000": {"func": model_132529_38b4798b_0000, "volume": 4.540665, "area": 17.243},
    "model_132626_f1f9e3a7_0000": {"func": model_132626_f1f9e3a7_0000, "volume": 61.1182502242, "area": 101.7750294556},
    "model_132642_26b12db4_0000": {"func": model_132642_26b12db4_0000, "volume": 181.6672539482, "area": 365.5575131606},
    "model_132685_6ff62835_0000": {"func": model_132685_6ff62835_0000, "volume": 382.3740799692, "area": 487.9379259931},
    "model_132687_d1a27238_0001": {"func": model_132687_d1a27238_0001, "volume": 0.4020000075, "area": 3.7200000671},
    "model_132796_53ed101d_0001": {"func": model_132796_53ed101d_0001, "volume": 1.0995574288, "area": 9.1106186954},
    "model_132863_90d729e2_0000": {"func": model_132863_90d729e2_0000, "volume": 84.0901430122, "area": 159.3197986588},
    "model_133109_dbf8891f_0004": {"func": model_133109_dbf8891f_0004, "volume": 6486.3517076618, "area": 5180.5406830647},
    "model_133439_0ddc18c5_0000": {"func": model_133439_0ddc18c5_0000, "volume": 12.7066912104, "area": 99.2055527011},
    "model_133466_609f225b_0000": {"func": model_133466_609f225b_0000, "volume": 0.3914605377, "area": 4.3690568875},
    "model_133564_b5340c41_0003": {"func": model_133564_b5340c41_0003, "volume": 18.5090858177, "area": 44.0490559941},
    "model_133710_00be7f31_0003": {"func": model_133710_00be7f31_0003, "volume": 4722.616234096, "area": 6657.4943609147},
    "model_133742_8d1f00a2_0000": {"func": model_133742_8d1f00a2_0000, "volume": 0.0008835729, "area": 0.0589048601},
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
