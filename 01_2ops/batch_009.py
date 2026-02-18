"""Batch 009 - passing/01_2ops
204 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a curved channel or duct component with a U-shaped cross-section, featuring cylindrical end flanges on both sides, a slotted or ribbed interior surface, and a smooth exterior bend that curves upward in the middle.
def model_25399_5e678d71_0000():
    """Model: ROCKER"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2619467106, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((15.8508863735, -31.8236702889), 1.1, -62.4413742137, 316.0271914288)
                CenterArc((15.8508863735, -31.8236702889), 1.1, -106.4141827849, 43.9728085712)
            make_face()
            with BuildLine():
                CenterArc((15.8508863735, -31.8236702889), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7907085705, perimeter: 11.9380511362
            with BuildLine():
                CenterArc((22.8481936243, -28.1719978858), 1.1, -62.4413742137, 180)
                CenterArc((22.8481936243, -28.1719978858), 1.1, 117.5586257863, 180)
            make_face()
            with BuildLine():
                EllipticalCenterArc((22.8481936243, -28.1719978858), 0.8, 0.7999996984, 0, 360, -51.9400001579)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.0421664939, perimeter: 42.1265325748
            with BuildLine():
                CenterArc((15.8508863735, -31.8236702889), 1.1, -62.4413742137, 316.0271914288)
                Line((23.3571151939, -29.1471895777), (16.3598079431, -32.7988619808))
                CenterArc((22.8481936243, -28.1719978858), 1.1, 117.5586257863, 180)
                Line((22.3392720547, -27.1968061939), (19.0860411299, -28.8945640832))
                CenterArc((15.8474493233, -22.688798771), 7, -117.5155100263, 55.0741358127)
                Line((10.4271284804, -27.7580793206), (12.6135283459, -28.896999405))
                CenterArc((9.618648236, -29.3101294791), 1.75, -106.4141827849, 168.8986727585)
                Line((9.1241351379, -30.988806576), (15.540049569, -32.8788387499))
            make_face()
            # Profile area: 8.7050390838, perimeter: 14.3884943534
            with BuildLine():
                CenterArc((9.618648236, -29.3101294791), 1.75, 62.4844899737, 191.1013272415)
                CenterArc((9.618648236, -29.3101294791), 1.75, -106.4141827849, 168.8986727585)
            make_face()
            with BuildLine():
                CenterArc((9.618648236, -29.3101294791), 0.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((15.8508863735, -31.8236702889)):
                Circle(0.7)
            # Profile area: 2.0106185404, perimeter: 5.0265472983
            with Locations((22.8481936243, -28.1719978858)):
                Ellipse(0.8, 0.7999996984, rotation=-51.9400001579)
            # Profile area: 0.9160884178, perimeter: 3.3929200659
            with Locations((9.618648236, -29.3101294791)):
                Circle(0.54)
        # Symmetric extrude, each_side=2.4125
        extrude(amount=2.4125, both=True)
    return part.part


# Description: This is an oval or elliptical dome-shaped component with a smooth, curved surface and radiating ridge or rib patterns running from the center toward the edges, featuring a wireframe mesh overlay indicating its 3D geometry.
def model_25416_93d169f7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            Circle(2.4)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a blue and dark gray polymer or composite blade/fin component with a streamlined, curved aerodynamic profile featuring a tapered pointed end and a broader rectangular base section.
def model_25432_1e61aab2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.4938115151, perimeter: 32.913470425
            with BuildLine():
                Line((7.46125, 0), (8.0549623068, 2.38125))
                Line((8.0549623068, 2.38125), (7.5787123068, 2.38125))
                Line((7.5787123068, 2.38125), (7.2577132125, 2.8571507281))
                Line((7.2577132125, 2.8571507281), (0, 2.8571507281))
                Line((0, 2.8571507281), (-0.2944646062, 2.4205889963))
                Line((-5.3975, 2.06375), (-0.2944646062, 2.4205889963))
                CenterArc((-5.3975, 1.42875), 0.635, 90, 180)
                Line((-5.3975, 0.79375), (-0.2944646062, 0.4369110037))
                Line((0.0002355868, 0), (-0.2944646062, 0.4369110037))
                Line((0.0002355868, 0), (7.46125, 0))
            make_face()
            with BuildLine():
                CenterArc((-5.3975, 1.42875), 0.224536, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a simple straight rod or cylindrical shaft with a uniform diameter, tapered slightly at the ends, oriented diagonally in 3D space.
def model_25436_61a7f978_0000():
    """Model: Wire v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            Circle(0.025)
        # OneSide extrude, distance=7.6
        extrude(amount=7.6)
    return part.part


# Description: This is a parallelogram-shaped structural frame or bracket with a hollow center, featuring four corner posts connected by flat sides and internal diagonal bracing for rigidity.
def model_25436_61a7f978_0002():
    """Model: Gate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5328, perimeter: 14.8799027765
            with BuildLine():
                Line((1.775, -0.08), (1.92, -0.08))
                Line((1.92, -0.08), (1.92, 0))
                Line((-0.145, 0), (1.92, 0))
                Line((-0.145, -0.08), (-0.145, 0))
                Line((0, -0.08), (-0.145, -0.08))
                Line((0, -1.1), (0, -0.08))
                Line((1.775, -1.1), (0, -1.1))
                Line((1.775, -0.08), (1.775, -1.1))
            make_face()
            with BuildLine():
                Line((0.08, -1.02), (0.08, -0.08))
                Line((1.615, -1.02), (0.08, -0.08))
                Line((1.615, -1.02), (0.08, -1.02))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.695, -0.08), (1.695, -1.02))
                Line((0.16, -0.08), (1.695, -1.02))
                Line((0.16, -0.08), (1.695, -0.08))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.07
        extrude(amount=0.07)
    return part.part


# Description: This is a hexahedral (box-like) polyhedron with an irregular, trapezoidal footprint, featuring a tapered or wedge-shaped profile with multiple faceted surfaces and what appears to be internal geometry or voids on the left side.
def model_25474_5422a377_0009():
    """Model: WPUST_2 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.84, perimeter: 4
            with BuildLine():
                Line((0.7, -0.3), (-0.7, -0.3))
                Line((0.7, 0.3), (0.7, -0.3))
                Line((-0.7, 0.3), (0.7, 0.3))
                Line((-0.7, -0.3), (-0.7, 0.3))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a hexagonal or wedge-shaped block with a complex faceted geometry featuring multiple angled surfaces, an internal cavity or depression on the left side, and a tapered profile that transitions from a narrower left end to a wider right end.
def model_25474_5422a377_0018():
    """Model: WPUST_1 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.44, perimeter: 5.2
            with BuildLine():
                Line((0.9, -0.4), (-0.9, -0.4))
                Line((0.9, 0.4), (0.9, -0.4))
                Line((-0.9, 0.4), (0.9, 0.4))
                Line((-0.9, -0.4), (-0.9, 0.4))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a cylindrical container or drum with a curved body and a flat or slightly angled top surface featuring a grid-like pattern or panel design.
def model_25484_9b17990a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4305.5250165173, perimeter: 250.1540680424
            with BuildLine():
                CenterArc((-27.7332231903, 0), 40.8612681343, 127.3093823481, 105.3812353039)
                Line((2.5, -32.5), (-52.5, -32.5))
                Line((2.5, 32.5), (2.5, -32.5))
                Line((2.5, 32.5), (-52.5, 32.5))
            make_face()
        # OneSide extrude, distance=70
        extrude(amount=70)
    return part.part


# Description: This is a cylindrical component with a hollow bore and internal spiral or helical groove features running along its length, featuring a flat circular base on one end.
def model_26245_4aac38e1_0000():
    """Model: Hilt-C"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on Plane3 construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=3.1
        extrude(amount=3.1)
    return part.part


# Description: This is a cylindrical mesh or perforated drum component with a solid circular end plate and an open latticed side structure, featuring a grid-pattern surface design typical of filtering, ventilation, or containment applications.
def model_26245_4aac38e1_0001():
    """Model: Hilt-A"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.4273222933, perimeter: 11.6238928183
            with BuildLine():
                CenterArc((0, 0), 1.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a long, slender conical shape that gradually decreases in diameter from one end to the other.
def model_26245_4aac38e1_0003():
    """Model: CurrentToMotor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.0549778714, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=9.8, against=-0.4
        extrude(amount=9.8)
        extrude(sk.sketch, amount=-0.4)
    return part.part


# Description: This is a curved deflector or trim panel with a wavy, concave profile featuring raised flanges on both ends and a central scalloped cutout, designed for aerodynamic or aesthetic purposes in an automotive application.
def model_26261_5deaf75a_0001():
    """Model: stretcher"""
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
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 173.3958760582, perimeter: 81.1800659298
            with BuildLine():
                Line((0, 0), (2.54, 0))
                _nurbs_edge([(2.54, 0), (2.7477745996, 0.2527782594), (3.1707622028, 0.7217295541), (3.827558883, 1.3153353395), (4.7480999046, 1.8863184541), (5.9742330089, 2.2360201138), (7.276237427, 2.2423215952), (8.6534866613, 1.9524263325), (10.1034389009, 1.4563827825), (11.621140796, 0.8796196956), (13.1990207704, 0.3567927839), (14.8264750128, 0.0110707251), (16.4894527665, -0.0683395482), (18.1698487044, 0.1500799834), (19.845090818, 0.6198275282), (21.4903633628, 1.2421708893), (23.0805385076, 1.8868536521), (24.592334959, 2.414714683), (26.0062140783, 2.6973605484), (27.3091086617, 2.6426544864), (28.4948834443, 2.2026227365), (29.3482237322, 1.525861529), (29.9348050621, 0.834231552), (30.3022098495, 0.2916577693), (30.48, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((33.02, 0), (30.48, 0))
                Line((33.02, 6.35), (33.02, 0))
                Line((0, 6.35), (33.02, 6.35))
                Line((0, 0), (0, 6.35))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a solid base and an open, textured top end, featuring a uniform hollow tube structure with vertical ribbing or corrugation patterns along its sides.
def model_26384_83eddf22_0009():
    """Model: Crankpin v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1233123321, perimeter: 1.2448246731
            Circle(0.19812)
        # OneSide extrude, distance=1.0414
        extrude(amount=1.0414)
    return part.part


# Description: This is a cylindrical mesh or perforated filter tube with rounded ends and a slightly tapered top opening, designed for fluid filtration or straining applications.
def model_26384_83eddf22_0011():
    """Model: Gudgeon Pin v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1248983265, perimeter: 1.2528043184
            Circle(0.19939)
        # OneSide extrude, distance=1.1684
        extrude(amount=1.1684)
    return part.part


# Description: This is a cylindrical rod or tube with a long, slender shape and rounded ends, featuring a uniform diameter throughout its length.
def model_26384_83eddf22_0015():
    """Model: Tommy Bar v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=2.8575
        extrude(amount=2.8575)
    return part.part


# Description: This is a cylindrical tube or pipe with a hollow circular cross-section, featuring a straight elongated body with slightly rounded ends and a uniform diameter throughout its length.
def model_26384_83eddf22_0020():
    """Model: Stud v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            Circle(0.2413)
        # OneSide extrude, distance=3.4925
        extrude(amount=3.4925)
    return part.part


# Description: This is a hexagonal or octagonal box-shaped enclosure with a flat base, angled side walls, and a faceted top structure featuring multiple triangular and trapezoidal surfaces, designed as a protective housing or container component.
def model_26384_83eddf22_0024():
    """Model: 6-32 Nut v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1969806291, perimeter: 3.2794918715
            with BuildLine():
                Line((0.1732050833, 0.3000000045), (-0.1732050833, 0.3000000045))
                Line((-0.1732050833, 0.3000000045), (-0.3464101667, 0))
                Line((-0.3464101667, 0), (-0.1732050833, -0.3000000045))
                Line((-0.1732050833, -0.3000000045), (0.1732050833, -0.3000000045))
                Line((0.1732050833, -0.3000000045), (0.3464101667, 0))
                Line((0.3464101667, 0), (0.1732050833, 0.3000000045))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.19115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a hexagonal or octagonal geometric housing/enclosure with a central rectangular cavity or slot running through its length, featuring triangular faceted faces on the ends and a structured mesh-like internal geometry.
def model_26384_83eddf22_0028():
    """Model: 10-32 Machine Nut v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3798747605, perimeter: 4.2515997918
            with BuildLine():
                Line((0.2309401111, 0.400000006), (-0.2309401111, 0.400000006))
                Line((-0.2309401111, 0.400000006), (-0.4618802222, 0))
                Line((-0.4618802222, 0), (-0.2309401111, -0.400000006))
                Line((-0.2309401111, -0.400000006), (0.2309401111, -0.400000006))
                Line((0.2309401111, -0.400000006), (0.4618802222, 0))
                Line((0.4618802222, 0), (0.2309401111, 0.400000006))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2356, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.27
        extrude(amount=0.27)
    return part.part


# Description: This is a flat rectangular plate or sheet metal component with a parallelogram-like 3D perspective, featuring a long, narrow slot or cutout running diagonally across its surface.
def model_26388_a3367cba_0001():
    """Model: chrome stainless steel blade.SLDPRT"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9200000107, perimeter: 16.600000003
            with BuildLine():
                Line((0, 0), (0, -1.1000000015))
                Line((0, -1.1000000015), (7.2, -1.1000000015))
                Line((7.2, -1.1000000015), (7.2, 0))
                Line((0, 0), (7.2, 0))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


# Description: This is a solar panel or photovoltaic module with an elongated parallelogram shape, featuring a segmented surface divided into multiple rectangular sections by internal grid lines, representing individual solar cells arranged in rows.
def model_26388_a3367cba_0007():
    """Model: chrome stainless steel blade 2.SLDPRT"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.1845000022, perimeter: 26.3999997914
            with BuildLine():
                Line((0, -1.5), (0.9795, -1.5))
                Line((0.9795, -1.5), (0.9795, -0.4000000209))
                Line((0.9795, -0.4000000209), (1.0005, -0.4000000209))
                Line((1.0005, -0.4000000209), (1.0005, -1.5))
                Line((1.0005, -1.5), (2.0295, -1.5))
                Line((2.0295, -1.5), (2.0295, -0.4000000209))
                Line((2.0295, -0.4000000209), (2.0505, -0.4000000209))
                Line((2.0505, -0.4000000209), (2.0505, -1.5))
                Line((2.0505, -1.5), (3.0795, -1.5))
                Line((3.0795, -1.5), (3.0795, -0.4000000209))
                Line((3.0795, -0.4000000209), (3.1005, -0.4000000209))
                Line((3.1005, -1.5), (3.1005, -0.4000000209))
                Line((3.1005, -1.5), (4.1295, -1.5))
                Line((4.1295, -1.5), (4.1295, -0.4000000209))
                Line((4.1295, -0.4000000209), (4.1505, -0.4000000209))
                Line((4.1505, -0.4000000209), (4.1505, -1.5))
                Line((4.1505, -1.5), (5.1795, -1.5))
                Line((5.1795, -1.5), (5.1795, -0.4000000209))
                Line((5.1795, -0.4000000209), (5.2005, -0.4000000209))
                Line((5.2005, -1.5), (5.2005, -0.4000000209))
                Line((6.2, -1.5), (5.2005, -1.5))
                Line((6.2, 0), (6.2, -1.5))
                Line((0, 0), (6.2, 0))
                Line((0, -1.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


# Description: This is a flat, rectangular plate with a parallelogram or trapezoidal shape featuring a central oval or slot-shaped hole and corner mounting holes, designed as a mounting bracket or connector component.
def model_26403_1f4a2618_0000():
    """Model: 03_Plaque 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.0438940241, perimeter: 28.1964594301
            with BuildLine():
                Line((-5.8, 3.9), (0, 3.9))
                Line((-5.8, 0), (-5.8, 3.9))
                Line((0, 0), (-5.8, 0))
                Line((0, 3.9), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-4.9, 1.9), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.9, 1.9), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9, 1.9), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular cutting tool insert or lathe tool holder with a long, flat prismatic body featuring multiple parallel slots or grooves running along its top surface and angled chamfered edges on both ends.
def model_26403_1f4a2618_0008():
    """Model: 08_Plaque"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.8745133224, perimeter: 18.9699111843
            with BuildLine():
                Line((2.9, -0.9), (2.9, 0.9))
                Line((2.9, 0.9), (-2.9, 0.9))
                Line((-2.9, 0.9), (-2.9, -0.9))
                Line((-2.9, -0.9), (2.9, -0.9))
            make_face()
            with BuildLine():
                CenterArc((-2.0000000432, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0000000432, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular cutting insert or tool holder with an elongated flat body, featuring two parallel recessed slots or grooves running lengthwise across the top surface and angled/beveled edges on both ends for chip clearance and mounting.
def model_26403_1f4a2618_0009():
    """Model: 09_Plaque"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.2945133224, perimeter: 18.7699111843
            with BuildLine():
                Line((2.9, -0.85), (2.9, 0.85))
                Line((2.9, 0.85), (-2.9, 0.85))
                Line((-2.9, 0.85), (-2.9, -0.85))
                Line((-2.9, -0.85), (2.9, -0.85))
            make_face()
            with BuildLine():
                CenterArc((-2.0000000432, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0000000432, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a vertical stand or support bracket with a cylindrical upper body, a wide rectangular base flange for stability, and vertical ribbing or fluting along the sides for structural reinforcement.
def model_26404_7be5b2e3_0003():
    """Model: Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.562792303, perimeter: 51.8547667519
            with BuildLine():
                Line((-0.7725121358, -0.635), (-0.7725121358, -9.2432))
                CenterArc((0, 0), 1, -140.5800155329, 101.1600310659)
                Line((0.7725121358, -0.635), (0.7725121358, -9.2432))
                Line((0.7725121358, -9.2432), (2.5, -9.2432))
                Line((2.5, -9.2432), (2.5, -9.0432))
                Line((2.5, -9.0432), (1, -9.0432))
                Line((1, 0), (1, -9.0432))
                CenterArc((0, 0), 1, 0, 180)
                Line((-1, 0), (-1, -9.0432))
                Line((-1, -9.0432), (-2.9000000432, -9.0432))
                Line((-2.9000000432, -9.2432), (-2.9000000432, -9.0432))
                Line((-0.7725121358, -9.2432), (-2.9000000432, -9.2432))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical tube or sleeve with a smooth, uniform circular cross-section and rounded ends, featuring a hollow interior core.
def model_26404_7be5b2e3_0007():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8748239558, perimeter: 10.2730079772
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a blue and dark gray plastic or composite bracket with a curved, angular boomerang or chevron shape, featuring hollow sections and reinforced edges designed for structural support or mounting applications.
def model_26764_ab35159a_0000():
    """Model: Trapezoidal joint"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 40 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.3405899945, perimeter: 37.9297927634
            with BuildLine():
                Line((1.25, 0), (-1.25, 0))
                CenterArc((1.25, 0.4), 0.4, -90, 67.380135052)
                Line((1.6192307692, 0.2461538462), (3.3692307692, 4.4461538462))
                CenterArc((3, 4.6), 0.4, -22.619864948, 112.619864948)
                Line((-3, 5), (3, 5))
                CenterArc((-3, 4.6), 0.4, 90, 112.619864948)
                Line((-1.6192307692, 0.2461538462), (-3.3692307692, 4.4461538462))
                CenterArc((-1.25, 0.4), 0.4, -157.380135052, 67.380135052)
            make_face()
            with BuildLine():
                CenterArc((-3, 4.6), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3, 4.6), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.25, 0.4), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.25, 0.4), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.95, 4.3), (-1.95, 4.3))
                CenterArc((1.95, 3.9), 0.4, -22.619864948, 112.619864948)
                Line((2.3192307692, 3.7461538462), (1.1525641026, 0.9461538462))
                CenterArc((0.7833333333, 1.1), 0.4, -90, 67.380135052)
                Line((-0.7833333333, 0.7), (0.7833333333, 0.7))
                CenterArc((-0.7833333333, 1.1), 0.4, -157.380135052, 67.380135052)
                Line((-2.3192307692, 3.7461538462), (-1.1525641026, 0.9461538462))
                CenterArc((-1.95, 3.9), 0.4, 90, 112.619864948)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a triangular bracket or frame component with three hollow sides forming a right-angled triangle, featuring a reinforced corner joint and smooth curved edges along the perimeter.
def model_26764_ab35159a_0002():
    """Model: Traingular joint"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6950221286, perimeter: 28.8121041037
            with BuildLine():
                CenterArc((4.2518613312, 0.3063553777), 0.3, -90, 120)
                Line((4.5116689524, 0.4563553777), (2.2616689524, 4.3534696948))
                CenterArc((2.0018613312, 4.2034696948), 0.3, 30, 120)
                Line((1.7420537101, 4.3534696948), (-0.5079462899, 0.4563553777))
                CenterArc((-0.2481386688, 0.3063553777), 0.3, 150, 120)
                Line((-0.2481386688, 0.0063553777), (4.2518613312, 0.0063553777))
            make_face()
            with BuildLine():
                Line((0.2714765735, 0.8063553777), (1.8286562505, 3.5034696948))
                CenterArc((2.0018613312, 3.4034696948), 0.2, 30, 120)
                Line((2.175066412, 3.5034696948), (3.732246089, 0.8063553777))
                CenterArc((3.5590410082, 0.7063553777), 0.2, -90, 120)
                Line((3.5590410082, 0.5063553777), (0.4446816543, 0.5063553777))
                CenterArc((0.4446816543, 0.7063553777), 0.2, 150, 120)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2518613312, 0.3063553777), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.2481386688, 0.3063553777), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0018613312, 4.2034696948), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a blue mesh or perforated rectangular enclosure or duct component with open sides and a curved, wave-like top edge, featuring ventilation holes throughout its walls.
def model_26764_ab35159a_0004():
    """Model: Nut 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6836393724, perimeter: 3.5127961262
            with BuildLine():
                CenterArc((0, 0), 1, 119.2946008376, 61.4107983248)
                CenterArc((-1.1258330249, -0.65), 0.65, 30, 48.8308663768)
                Line((-0.3031088913, -0.175), (-0.5629165125, -0.325))
                CenterArc((0, 0), 0.35, 90, 120)
                Line((0, 0.35), (0, 0.65))
                CenterArc((0, 1.3), 0.65, -138.8308663768, 48.8308663768)
            make_face()
            # Profile area: 0.6836393724, perimeter: 3.5127961262
            with BuildLine():
                CenterArc((0, 1.3), 0.65, -90, 48.8308663768)
                Line((0, 0.35), (0, 0.65))
                CenterArc((0, 0), 0.35, -30, 120)
                Line((0.3031088913, -0.175), (0.5629165125, -0.325))
                CenterArc((1.1258330249, -0.65), 0.65, 101.1691336232, 48.8308663768)
                CenterArc((0, 0), 1, -0.7053991624, 61.4107983248)
            make_face()
            # Profile area: 0.6836393724, perimeter: 3.5127961262
            with BuildLine():
                CenterArc((1.1258330249, -0.65), 0.65, 150, 48.8308663768)
                Line((0.3031088913, -0.175), (0.5629165125, -0.325))
                CenterArc((0, 0), 0.35, -150, 120)
                Line((-0.3031088913, -0.175), (-0.5629165125, -0.325))
                CenterArc((-1.1258330249, -0.65), 0.65, -18.8308663768, 48.8308663768)
                CenterArc((0, 0), 1, -120.7053991624, 61.4107983248)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a hexagonal prism or bar stock with chamfered edges, featuring an elongated rectangular slot or depression running along its top surface.
def model_26768_c4df841f_0010():
    """Model: Conexion"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5028365831, perimeter: 5.889
            with BuildLine():
                Line((-0.49075, 0.8500039338), (-0.9815, 0))
                Line((-0.9815, 0), (-0.49075, -0.8500039338))
                Line((-0.49075, -0.8500039338), (0.49075, -0.8500039338))
                Line((0.49075, -0.8500039338), (0.9815, 0))
                Line((0.9815, 0), (0.49075, 0.8500039338))
                Line((0.49075, 0.8500039338), (-0.49075, 0.8500039338))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)
    return part.part


# Description: This is a flexible corrugated hose or conduit assembly with a curved, loop-like shape featuring two rigid connector fittings (one at the top right and one at the bottom) for attachment to other components.
def model_26768_c4df841f_0014():
    """Model: Tope"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0746474927, perimeter: 13.619481198
            with BuildLine():
                CenterArc((0.06, 0), 1.3580443398, -165.6551875384, 12.1487890096)
                CenterArc((-1.1106789979, -0.5835157915), 0.05, -153.5063985288, 93.5063985288)
                Line((-1.0711653103, -0.6184375803), (-1.0856789979, -0.6268170617))
                CenterArc((-0.9711653103, -0.791642661), 0.2, 37.5140454689, 82.4859545311)
                CenterArc((0.06, 0), 1.1, -142.4859545311, 284.9719090622)
                CenterArc((-0.9711653103, 0.791642661), 0.2, -120, 82.4859545311)
                Line((-1.0711653103, 0.6184375803), (-1.0856789979, 0.6268170617))
                CenterArc((-1.1106789979, 0.5835157915), 0.05, 60, 93.5063985288)
                CenterArc((0.06, 0), 1.3580443398, 153.5063985288, 12.1487890096)
                Line((-0.917629535, 0.2458780928), (-1.2557035742, 0.3364647586))
                CenterArc((0, 0), 0.95, -165, 330)
                Line((-0.917629535, -0.2458780928), (-1.2557035742, -0.3364647586))
            make_face()
            with BuildLine():
                CenterArc((-1.1000000171, 0.4000000067), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.1000000171, -0.4000000067), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)
    return part.part


# Description: This is a torus or ring-shaped washer with a circular cross-section, featuring a smooth outer curved surface and a central hollow opening, commonly used as a spacer, seal, or fastener component.
def model_26773_35d26b3c_0002():
    """Model: Lock washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5245969806, perimeter: 5.4676562054
            with BuildLine():
                Line((-0.0031818281, 0.2999831261), (0.0518826854, 0.5053436325))
                CenterArc((0, 0), 0.508, 84.1380882268, 358.1744481023)
                Line((0.0133273755, 0.2997038222), (0.0679548323, 0.503434346))
                CenterArc((0, 0), 0.3, 90.6076957948, 356.8461250058)
            make_face()
        # OneSide extrude, distance=0.1016
        extrude(amount=0.1016)
    return part.part


# Description: This is a flat, annular (ring-shaped) washer with a large central hole and a slightly beveled or rounded outer edge, used for distributing loads under bolt heads or nuts.
def model_26773_35d26b3c_0010():
    """Model: Washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0611715726, perimeter: 5.9944729423
            with BuildLine():
                CenterArc((0, 0), 0.65405, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0635
        extrude(amount=0.0635)
    return part.part


# Description: This is an oval or elliptical ring/band with an open top, featuring a dark base structure and a lighter blue mesh or perforated upper surface with internal ribbing and structural elements.
def model_26861_21e598d0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2)
    return part.part


# Description: This is a torus-shaped ring or washer with a circular cross-section, featuring a smooth outer surface and a hollow center, with visible mesh texturing on the top and inner edges.
def model_27054_342fcf5c_0003():
    """Model: 20 - Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0579641723, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a toroidal (donut-shaped) rubber gasket or seal with a circular cross-section, featuring a smooth outer surface and a hollow center, commonly used for sealing applications in mechanical assemblies.
def model_27054_342fcf5c_0005():
    """Model: 19 - Seal v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.8618356156, perimeter: 24.1902634326
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a cylindrical sleeve or tube with a smooth exterior surface and slightly textured or knurled top end, appearing to be a simple hollow shaft or spacer component.
def model_27054_342fcf5c_0006():
    """Model: 36 - Pin v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)
    return part.part


# Description: This is a circular gasket or sealing ring with an oval/elliptical profile, featuring six evenly-spaced bolt holes around its perimeter for securing it between flanged connections.
def model_27054_342fcf5c_0016():
    """Model: 17 - Seal v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.0298630084, perimeter: 74.7699051554
            with BuildLine():
                CenterArc((0, 0), 5.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3301270189, 2.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3301270189, -2.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.3301270189, -2.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.3301270189, 2.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center, featuring a textured or ribbed surface pattern on its outer walls, designed for mechanical assembly or bearing applications.
def model_27054_342fcf5c_0024():
    """Model: 9 - Spacer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9738937226, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.1
        extrude(amount=2.1)
    return part.part


# Description: This is a torus or ring-shaped seal/gasket with a uniform circular cross-section and smooth curved surfaces, featuring a hollow center and textured outer edges.
def model_27054_342fcf5c_0038():
    """Model: 32 - Seal v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.0870567505, perimeter: 27.9601746169
            with BuildLine():
                CenterArc((0, 0), 2.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: A flat, circular ring gasket with an oval center opening and four evenly-spaced bolt holes around its perimeter for sealing connections between flanged pipes or equipment.
def model_27054_342fcf5c_0042():
    """Model: 12 - Seal v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 92.4413638319, perimeter: 87.9645943005
            with BuildLine():
                CenterArc((0, 0), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 6), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7063390978, 1.8541019662), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5267115138, -4.8541019662), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.5267115138, -4.8541019662), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.7063390978, 1.8541019662), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or washer with a smooth outer surface and a large central hole, featuring textured or knurled sections on portions of its inner and outer edges for grip or engagement purposes.
def model_27054_342fcf5c_0047():
    """Model: 33 - Washer v1 (16)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6675884389, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, tapered slightly at both ends, featuring a smooth, rounded finish suitable for mechanical assembly or bearing applications.
def model_27070_53448c4a_0008():
    """Model: Wal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -7.0915699103), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 22), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 22), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=19.25
        extrude(amount=19.25)
    return part.part


# Description: This is a long, rectangular hollow tube or channel with a square or rectangular cross-section, tilted at an angle, featuring clean edges and uniform wall thickness throughout its length.
def model_27070_53448c4a_0017():
    """Model: Chwytacz"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.8, perimeter: 13.6
            with BuildLine():
                Line((-34, 13), (-34, 7))
                Line((-34, 7), (-33.2, 7))
                Line((-33.2, 7), (-33.2, 13))
                Line((-33.2, 13), (-34, 13))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a triangular pyramidal or wedge-shaped 3D part with a pointed apex at the top, a broad triangular base, and an internal diagonal line or edge visible on one face, suggesting it may be a solid geometric form or a part with internal structure.
def model_27449_088a5bd0_0001():
    """Model: plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 120764.1172802494, perimeter: 1491.3443346436
            with BuildLine():
                Line((350.2446079372, -130), (350.2446079372, 245.2012509021))
                Line((350.2446079372, 245.2012509021), (-105, 25.3448123559))
                Line((-105, 25.3448123559), (-105, -130))
                Line((-105, -130), (350.2446079372, -130))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: A cylindrical rod or shaft with a uniform diameter, slightly tapered at one end, oriented at an angle.
def model_27452_f37cb86c_0003():
    """Model: Aufhaengung v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=3.6
        extrude(amount=3.6, both=True)
    return part.part


# Description: A long, flat rectangular bar or plate with a slight 3D parallelogram profile, featuring clean edges and a uniform thickness throughout its length.
def model_27577_8520e14a_0000():
    """Model: Ladder Horizontal Wood"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1122.5784, perimeter: 596.9
            with BuildLine():
                Line((-147.32, 1.905), (147.32, 1.905))
                Line((-147.32, -1.905), (-147.32, 1.905))
                Line((147.32, -1.905), (-147.32, -1.905))
                Line((147.32, 1.905), (147.32, -1.905))
            make_face()
        # OneSide extrude, distance=-8.89
        extrude(amount=-8.89)
    return part.part


# Description: This is a cylindrical tube or rod with a smooth, tapered design, featuring a hollow interior and a slightly beveled or rounded top edge.
def model_27577_8520e14a_0001():
    """Model: Ladder Vertical Wood Thick"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2632.2528, perimeter: 538.48
            with BuildLine():
                Line((-5.08, 129.54), (5.08, 129.54))
                Line((-5.08, -129.54), (-5.08, 129.54))
                Line((5.08, -129.54), (-5.08, -129.54))
                Line((5.08, 129.54), (5.08, -129.54))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


# Description: This is a long, slender rectangular prism or beam with a uniform cross-section, featuring a slight hexagonal or chamfered top end and appearing to be a structural support or mounting rod.
def model_27577_8520e14a_0002():
    """Model: Ladder Vertical Wood Thin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 774.192, perimeter: 172.72
            with BuildLine():
                Line((5.08, -38.1), (5.08, 38.1))
                Line((5.08, 38.1), (-5.08, 38.1))
                Line((-5.08, 38.1), (-5.08, -38.1))
                Line((-5.08, -38.1), (5.08, -38.1))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a slightly tapered design, featuring a smooth external surface and rounded ends, commonly used as a muzzle attachment for firearms.
def model_27577_8520e14a_0003():
    """Model: Ladder Bar Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 31.6692174436, perimeter: 19.9491133503
            Circle(3.175)
        # OneSide extrude, distance=50.8
        extrude(amount=50.8)
    return part.part


# Description: This is a flat, elongated rectangular plate or base with a slight trapezoidal profile, featuring a beveled or angled edge on one end and a thin, uniform thickness throughout.
def model_27577_8520e14a_0005():
    """Model: Swing Seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1238.7072, perimeter: 162.56
            with BuildLine():
                Line((-30.48, 10.16), (30.48, 10.16))
                Line((-30.48, -10.16), (-30.48, 10.16))
                Line((30.48, -10.16), (-30.48, -10.16))
                Line((30.48, 10.16), (30.48, -10.16))
            make_face()
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81)
    return part.part


# Description: This is a curved rod or tube with a smooth, elongated S-shaped bend, tapering slightly at both ends, commonly used as a structural support, guide rail, or decorative element.
def model_27577_8520e14a_0006():
    """Model: Slide"""
    with BuildPart() as part:
        # Sketch8 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 505.6395145108, perimeter: 211.1463532504
            with BuildLine():
                Line((-175.895, -151.765), (-175.895, -156.845))
                CenterArc((-184.4849481065, -70.7501612344), 86.5223004234, -84.3022794077, 69.1642849534)
                Line((-106.045, -93.345), (-100.965, -93.345))
                CenterArc((-184.7140023601, -70.2523884825), 81.9882957442, -83.8250808452, 67.4659314413)
            make_face()
            # Profile area: 309.9788629617, perimeter: 135.9677680978
            with BuildLine():
                CenterArc((-44.636994063, -113.2053065307), 59.7266776937, 103.9691703309, 56.6090373504)
                Line((-59.055, -50.165), (-59.055, -55.245))
                CenterArc((-44.9226460103, -112.7024146358), 64.1143639025, 102.7339464161, 59.6930887344)
                Line((-106.045, -93.345), (-100.965, -93.345))
            make_face()
            # Profile area: 77.4192, perimeter: 40.64
            with BuildLine():
                Line((15.875, 9.525), (15.875, 14.605))
                Line((31.115, 9.525), (15.875, 9.525))
                Line((31.115, 14.605), (31.115, 9.525))
                Line((15.875, 14.605), (31.115, 14.605))
            make_face()
            # Profile area: 312.7773412465, perimeter: 134.9060021309
            with BuildLine():
                Line((-59.055, -50.165), (-59.055, -55.245))
                CenterArc((-68.559149871, 5.0155529718), 61.0054350795, -81.0372759007, 62.2763668938)
                Line((-15.875, -14.605), (-10.795, -14.605))
                CenterArc((-69.2569020732, 6.2194525175), 57.2999589146, -79.7441629829, 58.4332456624)
            make_face()
            # Profile area: 184.8310470005, perimeter: 91.439134208
            with BuildLine():
                Line((-15.875, -14.605), (-10.795, -14.605))
                CenterArc((31.57140625, -34.62734375), 46.8594347787, 109.570585696, 45.1340181557)
                Line((15.875, 9.525), (15.875, 14.605))
                CenterArc((33.7427750657, -36.6769294192), 54.3055583781, 109.2094833214, 46.8091452964)
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: A horizontal rounded rectangular bar or rod with a slightly curved top surface and uniform cylindrical cross-section.
def model_27577_8520e14a_0007():
    """Model: Thick Horizontal Pole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.6692174436, perimeter: 19.9491133503
            Circle(3.175)
        # OneSide extrude, distance=96.52
        extrude(amount=96.52)
    return part.part


# Description: This is a simple rounded rectangular bar or rod with a uniform cylindrical profile and slightly rounded ends.
def model_27577_8520e14a_0008():
    """Model: Thin Horizontal Pole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=96.52
        extrude(amount=96.52)
    return part.part


# Description: This is a long, slender rectangular prism or bar stock with a hexagonal or slightly tapered cross-section, featuring grooved or ribbed surface details running along its length.
def model_27577_8520e14a_0009():
    """Model: Platform Leg"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((-5.08, 5.08), (5.08, 5.08))
                Line((-5.08, -5.08), (-5.08, 5.08))
                Line((5.08, -5.08), (-5.08, -5.08))
                Line((5.08, 5.08), (5.08, -5.08))
            make_face()
        # OneSide extrude, distance=-162.56
        extrude(amount=-162.56)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform hollow circular cross-section, featuring a slightly textured or threaded end at the top and a beveled or chamfered edge at the bottom.
def model_27577_8520e14a_0011():
    """Model: Vertical Pole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.6692174436, perimeter: 19.9491133503
            Circle(3.175)
        # OneSide extrude, distance=-45.72
        extrude(amount=-45.72)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve with a hollow center, featuring a solid base band at the bottom and an open mesh or latticed upper section that tapers slightly inward.
def model_27679_501db761_0002():
    """Model: rolament"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.7128309487, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a solid outer wall and a mesh/screen top surface, designed to allow fluid or air passage while filtering debris.
def model_27679_501db761_0003():
    """Model: rol_in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5079644737, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with an open top and curved, tapered sidewalls that widen toward the base.
def model_27679_501db761_0012():
    """Model: 19_23"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7559457323, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((0, 0), 0.775, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is a polyhedron or geometric solid featuring multiple angular faces in varying shades of blue and dark gray, with a predominantly cuboid-like structure that appears to have been sectioned or truncated to create multiple planar surfaces and internal geometric divisions.
def model_27679_501db761_0018():
    """Model: 11_14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.7980695053, perimeter: 20.0844676764
            with BuildLine():
                CenterArc((4.25, 4.497), 0.25, -90, 180)
                Line((4.25, 0), (4.25, 4.247))
                Line((4.25, 0), (8.7502988551, 0))
                Line((8.7502988551, 0), (8.7502988551, 4))
                Line((6.64475, 6), (8.7502988551, 4))
                Line((4.25, 6), (6.64475, 6))
                Line((4.25, 6), (4.25, 4.747))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a slightly tapered, curved top edge and vertical ribbed or fluted surface texture on its outer walls.
def model_27679_501db761_0022():
    """Model: 22_22"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7559457323, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((0, 0), 0.775, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)
    return part.part


# Description: This is a curved cylindrical duct or shroud component with a rectangular cross-section, featuring vertical ribs on the outer surface and a mesh or perforated panel on the top curved section, designed for airflow management or containment.
def model_27682_04277f62_0009():
    """Model: pasa eje"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4135407509, perimeter: 11.0307021718
            with BuildLine():
                CenterArc((0.975, 1.1399013115), 0.6, 0, 49.4583981265)
                CenterArc((0, 0), 2.1, 49.4583981265, 130.5416018735)
                Line((-0.8, 0), (-2.1, 0))
                CenterArc((0, 0), 0.8, 0, 180)
                Line((1.575, 0), (0.8, 0))
                Line((1.575, 1.1399013115), (1.575, 0))
            make_face()
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)
    return part.part


# Description: This is a cylindrical mesh or perforated filter basket with a solid base and mesh-sided walls, featuring an open top and designed for liquid filtration or containment applications.
def model_27682_04277f62_0010():
    """Model: tapon2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.6345121166, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a torus or ring gasket with a circular cross-section, featuring a uniform donut-shaped geometry with a hollow center and smooth, rounded outer and inner surfaces.
def model_27688_65b3c0dc_0002():
    """Model: Component45"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.0107805653), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.6576320931, perimeter: 20.4203522483
            with BuildLine():
                CenterArc((27.6908962602, 11.35179153), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((27.6908962602, 11.35179153), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical roller or shaft with a slightly tapered, rounded end and a smooth, elongated body featuring a subtle curved profile along its length.
def model_27688_65b3c0dc_0004():
    """Model: plaskownikK"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 109.9087385212, perimeter: 81.2699081699
            with BuildLine():
                CenterArc((2.5, -23.5), 2.5, 180, 180)
                Line((5, -2.5), (5, -23.5))
                CenterArc((2.5, -2.5), 2.5, 0, 180)
                Line((0, -23.5), (0, -2.5))
            make_face()
            with BuildLine():
                CenterArc((2.5, -22), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -13), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -4), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a stylus or pen-shaped tool with an elongated cylindrical body, tapered at both ends, featuring a smooth curved profile and what appears to be a metallic accent stripe running along its length.
def model_27688_65b3c0dc_0006():
    """Model: plaskownikD"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 150, perimeter: 107.1238898038
            with BuildLine():
                CenterArc((2.5, -32.5), 2.5, 180, 180)
                Line((5, -2.5), (5, -32.5))
                CenterArc((2.5, -2.5), 2.5, 0, 180)
                Line((0, -32.5), (0, -2.5))
            make_face()
            with BuildLine():
                CenterArc((2.5, -31), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -22), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -13), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -4), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hollow cylindrical tube or sleeve with rounded ends and a seam running along its length, appearing to be a simple tubular component suitable for containment, spacing, or protective covering applications.
def model_27694_7801dc67_0002():
    """Model: Bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((2.5, 2.5), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical connector or housing with a tapered end, featuring a central longitudinal slot or window cutout along its length and dark end caps on both sides.
def model_27694_7801dc67_0006():
    """Model: Large"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3926990817, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((1.5000000224, 3.5000000522), 0.5, 0, 180)
                Line((1.0000000224, 3.5000000522), (1.0000000224, 1.5000000522))
                CenterArc((1.5000000224, 1.5000000522), 0.5, 180, 180)
                Line((2.0000000224, 3.5000000522), (2.0000000224, 1.5000000522))
            make_face()
            with BuildLine():
                CenterArc((1.5000000224, 1.5000000522), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5000000224, 3.5000000522), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved cylindrical or band-shaped component with a hollow interior, featuring rectangular slots or openings along its sides and a ribbed or textured outer surface, designed to wrap around or encompass another object.
def model_27694_7801dc67_0007():
    """Model: Small"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3926433088, perimeter: 8.2831861031
            with BuildLine():
                CenterArc((2.5, 5), 0.5, 0, 181.2124413671)
                Line((2.0001119438, 4.9894202427), (2.0000000032, 4.000056572))
                CenterArc((2.5, 4), 0.5, 179.9935173245, 180.0064826755)
                Line((3, 5), (3, 4))
            make_face()
            with BuildLine():
                CenterArc((2.5, 4), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with a solid dark body and perforated blue mesh cap at the top, designed for fluid or air filtration applications.
def model_27694_7801dc67_0008():
    """Model: Small pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-5.5, 1)):
                Circle(0.125)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical sleeve or tube with an open top, featuring a curved rim edge and vertical ribbed or fluted surface texture on its sides.
def model_27694_7801dc67_0013():
    """Model: Small cylinder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7017696821, perimeter: 27.0176968209
            with BuildLine():
                CenterArc((2.5, 2.5), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 2.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered or curved profile, featuring vertical ribbing or fluting along its entire surface for structural reinforcement.
def model_27694_7801dc67_0016():
    """Model: Large cylinder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.6707957239, perimeter: 86.7079572391
            with BuildLine():
                CenterArc((7.3053731928, 7.175369261), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.3053731928, 7.175369261), 6.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-10
        extrude(amount=-10)
    return part.part


# Description: A cylindrical suppressor or silencer with a slightly tapered end cap and textured surface finish, designed for threaded attachment to a firearm barrel.
def model_27694_7801dc67_0020():
    """Model: I"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2.5, 2.5)):
                Circle(0.25)
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)
    return part.part


# Description: This is a cylindrical tube or sleeve with a closed bottom end and an open top end, featuring a textured or mesh-like surface pattern on the upper portion.
def model_27694_7801dc67_0024():
    """Model: II"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1.0000000149, 1.0000000149)):
                Circle(0.25)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


# Description: This is a curved rectangular housing or bracket with a distinctive organic, wave-like surface featuring parallel ribbing or fluting along its concave interior, solid flat external faces, and mounting flanges or tabs on the sides.
def model_27725_5cceaeb7_0009():
    """Model: Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.753964739, perimeter: 16.867374394
            with BuildLine():
                Line((1.66878, 1.2141817714), (1.66878, 2.464143588))
                Line((1.66878, 2.464143588), (-1.66878, 2.464143588))
                Line((-1.66878, 2.464143588), (-1.66878, 1.2141817714))
                CenterArc((0, 0), 2.06375, 143.9608705114, 72.0782589772)
                Line((-1.66878, -1.2141817714), (-1.66878, -2.464143588))
                Line((-1.66878, -2.464143588), (1.66878, -2.464143588))
                Line((1.66878, -2.464143588), (1.66878, -1.2141817714))
                CenterArc((0, 0), 2.06375, -36.0391294886, 72.0782589772)
            make_face()
        # Symmetric extrude, each_side=0.254
        extrude(amount=0.254, both=True)
    return part.part


# Description: This is a cylindrical rod or tube with a slightly tapered design, featuring rounded ends and a smooth, elongated shaft with a uniform diameter throughout its length.
def model_27725_5cceaeb7_0011():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5042878286, perimeter: 18.9516576828
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.42875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=41.91
        extrude(amount=41.91)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or washer with a thick circular cross-section, featuring a large central hole and textured surface details on the outer edges.
def model_27733_626709f1_0000():
    """Model: Prcision Shim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical capsule-shaped component with rounded ends, featuring two large circular holes on opposite sides and a central longitudinal slot running along the top surface.
def model_27839_4a077326_0004():
    """Model: Oslonka III stopnia"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.4131612192, perimeter: 33.6150413934
            with BuildLine():
                CenterArc((37.5686929363, 47.3585823641), 3.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((37.5686929363, 47.3585823641), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.3
        extrude(amount=15.3)
    return part.part


# Description: This is a torus or ring-shaped component with a circular cross-section, featuring a large central hole and a textured or ribbed surface pattern running radially across its outer geometry.
def model_27839_4a077326_0009():
    """Model: Podkladka sprezyny"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5079644737, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((-3, 23), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3, 23), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical shaft or tube with rounded end caps featuring two large circular holes or bores on opposite ends and a central longitudinal slot or cavity running along its length.
def model_27839_4a077326_0010():
    """Model: Oslonka II stopnia"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 41.4690230274, perimeter: 41.4690230274
            with BuildLine():
                CenterArc((-28.5666909708, 43.8361418825), 4.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-28.5666909708, 43.8361418825), 2.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.3
        extrude(amount=15.3)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a textured or ribbed surface finish, featuring a large central circular opening and uniform cross-sectional geometry throughout.
def model_27839_4a077326_0013():
    """Model: Podkladka rolki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.759291886, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((-3.0360671645, 9.4576047619), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.0360671645, 9.4576047619), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: A dark gray rounded rectangular bar or rod with a elongated pill-shaped profile, featuring uniformly rounded ends and a smooth cylindrical surface.
def model_27839_4a077326_0022():
    """Model: Oslonka przeciwwagi"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4476769531, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((-2.4598598782, 8.7770047813), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.4598598782, 8.7770047813), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=14
        extrude(amount=14)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, tapered slightly at both ends, featuring a smooth, elongated body with no holes, slots, or flanges.
def model_27872_07f8a3a0_0000():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((5.8000000864, -1.9000000283), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.8000000864, -1.9000000283), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a cylindrical rod or shaft with a tapered/rounded end, featuring a smooth, uniform circular cross-section throughout its length with a slight conical taper at one end.
def model_27872_07f8a3a0_0002():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((7.0334470413, -0.6291631471), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.0334470413, -0.6291631471), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a dark blue composite or plastic housing component with a trapezoidal profile, featuring a dual-chambered design with a central divider, angled side walls, and a flat base with a subtle curved underside detail.
def model_28282_97002185_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 336.6422056528, perimeter: 98.7323575667
            with BuildLine():
                Line((-0.5, 3.495), (-0.5, 13))
                CenterArc((-1.5, 13), 1, 0, 90)
                Line((-1.5, 14), (-5.6198006777, 14))
                CenterArc((-5.6198006777, 13), 1, 90, 41.6335393366)
                Line((-15, 6), (-6.2841645165, 13.7474093187))
                Line((-15, 0), (-15, 6))
                Line((15, 0), (-15, 0))
                Line((15, 0), (15, 6))
                Line((15, 6), (6.2841645165, 13.7474093187))
                CenterArc((5.6198006777, 13), 1, 48.3664606634, 41.6335393366)
                Line((5.6198006777, 14), (1.5, 14))
                CenterArc((1.5, 13), 1, 90, 90)
                Line((0.5, 13), (0.5, 3.495))
                CenterArc((0.005, 3.495), 0.495, -90, 90)
                Line((-0.005, 3), (0.005, 3))
                CenterArc((-0.005, 3.495), 0.495, 180, 90)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular box or enclosure with an angled lid and a cylindrical protruding connector or port on the left side, featuring a segmented geometric surface design with triangulated panels on the top and sides.
def model_28283_1a9ffb0b_0000():
    """Model: Arm 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5940927342, perimeter: 4.6495192749
            with BuildLine():
                Line((21, 1.5531228657), (21, -0.4271872516))
                Line((20.400000304, -0.4271872516), (21, 1.5531228657))
                Line((21, -0.4271872516), (20.400000304, -0.4271872516))
            make_face()
            # Profile area: 4.9863238933, perimeter: 13.9246961805
            with BuildLine():
                CenterArc((22.4661842282, 1.5531228657), 1.4661842282, 0, 180)
                CenterArc((22.4661842282, 1.5531228657), 1.4661842282, -180, 180)
            make_face()
            with BuildLine():
                CenterArc((22.4661842282, 1.5531228657), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.4302640413, perimeter: 11.499142291
            with BuildLine():
                CenterArc((22.4661842282, 1.5531228657), 1.4661842282, -180, 180)
                Line((21, 1.5531228657), (21, -0.4271872516))
                Line((21, -0.4271872516), (23.9323684563, -0.4271872516))
                Line((23.9323684563, -0.4271872516), (23.9323684563, 1.5531228657))
            make_face()
            # Profile area: 20.9536068077, perimeter: 18.8750993222
            with BuildLine():
                Line((21, -0.4271872516), (23.9323684563, -0.4271872516))
                Line((21, -0.4271872516), (21, -4))
                Line((21, -4), (26.8647369127, -4))
                Line((26.8647369127, -4), (26.8647369127, -0.4271872516))
                Line((26.8647369127, -0.4271872516), (23.9323684563, -0.4271872516))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)
    return part.part


# Description: This is a cylindrical container or barrel with an open top and a slightly tapered upper rim, featuring a flat circular base and vertical ribbed or fluted surface detailing along its sides.
def model_28456_69d04209_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.6172512352, perimeter: 28.2743338823
            Circle(4.5)
        # OneSide extrude, distance=9
        extrude(amount=9)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a uniform thickness and a slight angular/skewed geometry, featuring clean edges and a simple geometric form without holes, slots, or additional features.
def model_28888_da6e6e94_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((8.5000000075, -6.7999999821), (0.5000000075, -6.7999999821))
                Line((8.5000000075, 1.2000000179), (8.5000000075, -6.7999999821))
                Line((0.5000000075, 1.2000000179), (8.5000000075, 1.2000000179))
                Line((0.5000000075, -6.7999999821), (0.5000000075, 1.2000000179))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is an L-shaped bracket or corner joint with two perpendicular rectangular arms extending horizontally and vertically, featuring hollow/tubular construction with visible internal geometry and sharp edges typical of a metal structural component or connector.
def model_29114_80c15ce0_0004():
    """Model: SA-107"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 160.17, perimeter: 65.9
            with BuildLine():
                Line((5.1, 7.5), (0, 7.5))
                Line((0, 7.5), (0, 0))
                Line((-9.55, 0), (0, 0))
                Line((-9.55, -6.4), (-9.55, 0))
                Line((9.5, -6.4), (-9.55, -6.4))
                Line((9.5, 0), (9.5, -6.4))
                Line((5.1, 0), (9.5, 0))
                Line((5.1, 0), (5.1, 7.5))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)
    return part.part


# Description: This is a flat parallelogram-shaped plate or bracket with a diagonal line dividing it into two triangular sections, featuring a tapered left end and straight right edge with uniform thickness throughout.
def model_29115_cade8ac7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5000, perimeter: 300
            with BuildLine():
                Line((50, -25), (50, 25))
                Line((50, 25), (-50, 25))
                Line((-50, 25), (-50, -25))
                Line((-50, -25), (50, -25))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a slightly curved or warped surface, characterized by horizontal linear grooves or ribs running across its entire face.
def model_29442_365e23df_0008():
    """Model: SA-218-Canopy"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.9666041602, perimeter: 30.0857777437
            with BuildLine():
                Line((7.3, 22.8628519656), (7.3, 23.0727111541))
                CenterArc((0, 0), 24.2, 72.4430932397, 35.1138135207)
                Line((-7.3, 22.8628519656), (-7.3, 23.0727111541))
                CenterArc((0, 0), 24, 72.2919643897, 35.4160712206)
            make_face()
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped box with a tapered/angled left end, featuring a rectangular base and sloped upper surfaces, with a simple geometric design suitable for structural or assembly applications.
def model_30030_d4b0c535_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20, perimeter: 21
            with BuildLine():
                Line((8, -2.5), (0, -2.5))
                Line((8, 0), (8, -2.5))
                Line((0, 0), (8, 0))
                Line((0, -2.5), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular prism or flat bar stock part with a tapered or beveled edge along one of its long sides, creating an asymmetrical cross-section.
def model_30274_ca0d10b2_0004():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8694112025, perimeter: 4.2874370307
            with BuildLine():
                Line((1.0000000149, -1.0000000149), (1.6000000238, -1.0000000149))
                Line((1.6000000238, -1.0000000149), (1.5432762303, 0.5989941725))
                Line((1.0558392096, 0.5990253083), (1.5432762303, 0.5989941725))
                Line((1.0000000149, -1.0000000149), (1.0558392096, 0.5990253083))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a curved timing belt or drive belt with a smooth upper surface and evenly spaced teeth on the underside, designed to transmit power between pulleys in a mechanical system.
def model_30292_0b5e0265_0003():
    """Model: Headset"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.8400974061, perimeter: 51.160070759
            with BuildLine():
                CenterArc((0, 0), 8.255, -0.0299964655, 180.059992931)
                Line((-8.2549988687, -0.0043217985), (-7.6199987744, -0.0043217985))
                CenterArc((0, 0), 7.62, -0.0324961712, 180.0649923424)
                Line((7.6199987744, -0.0043217985), (8.2549988687, -0.0043217985))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: A flat, annular (ring-shaped) disk with a large central hole, commonly used as a spacer or fastener component in mechanical assemblies.
def model_30297_fd93a92a_0000():
    """Model: Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7869483843, perimeter: 5.0072274509
            with BuildLine():
                CenterArc((0, 0), 0.555625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05842
        extrude(amount=0.05842)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a closed bottom end and an open top with a mesh screen, typically used for fluid or air filtration applications.
def model_30297_fd93a92a_0003():
    """Model: Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            Circle(0.2413)
        # OneSide extrude, distance=1.143
        extrude(amount=1.143)
    return part.part


# Description: This is a cylindrical mesh or perforated filter/strainer component with a solid base section and an open latticed or mesh-patterned upper portion, designed for liquid or gas filtration applications.
def model_30297_fd93a92a_0004():
    """Model: Part 3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0838472978, perimeter: 5.5059552847
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: A hexagonal prism or bolt with a central cylindrical hole running through its length and triangular relief cutouts on the top surface.
def model_30297_fd93a92a_0007():
    """Model: Bolt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6831040296, perimeter: 4.9802342814
            with BuildLine():
                Line((0.2886751389, 0.5000000075), (-0.2886751389, 0.5000000075))
                Line((-0.2886751389, 0.5000000075), (-0.5773502778, 0))
                Line((-0.5773502778, 0), (-0.2886751389, -0.5000000075))
                Line((-0.2886751389, -0.5000000075), (0.2886751389, -0.5000000075))
                Line((0.2886751389, -0.5000000075), (0.5773502778, 0))
                Line((0.5773502778, 0), (0.2886751389, 0.5000000075))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a flexible rubber or elastomer boot/sleeve component with a tapered, curved tubular shape that widens at one end and narrows toward the other, featuring a textured surface and appearing designed to provide protective covering or sealing for mechanical components.
def model_30375_4ff65965_0008():
    """Model: Trigger"""
    with BuildPart() as part:
        # Sketch15 -> Extrude12 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8551806518, perimeter: 13.6199993352
            with BuildLine():
                CenterArc((-8.7185039296, 3), 1.083322632, -67.3187830496, 247.3187830496)
                Line((-9.8018265615, 3), (-9.8018265615, 1.9921217575))
                CenterArc((-10.8185072774, 0.3498457279), 1.9315046558, -58.2396711924, 116.4793423847)
                Line((-9.6491534761, -1.3534502626), (-9.8018265615, -1.2924303016))
                CenterArc((-11.4017062194, 1.2991353836), 3.1792533288, -56.5474196101, 69.2912883853)
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a paraglider wing or airfoil component featuring a streamlined, elongated pod-like shape with a curved upper surface, flat bottom panel, and a textured mesh or grid pattern on the leading edge for aerodynamic flow management.
def model_30376_e4495332_0000():
    """Model: Loop"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.5902133638, perimeter: 11.5960348203
            with BuildLine():
                CenterArc((0.4235635442, 0.5), 0.5, -170.537677792, 80.537677792)
                Line((0.4235635442, 0), (1.5764364558, 0))
                CenterArc((1.5764364558, 0.5), 0.5, -90, 80.537677792)
                Line((2.0696334177, 0.4178005063), (2.4739801194, 2.8438807165))
                CenterArc((1.9807831575, 2.9260802101), 0.5, -9.462322208, 38.7929844475)
                CenterArc((1, 2.375), 1.625, 29.3306622395, 121.3386755211)
                CenterArc((0.0192168425, 2.9260802101), 0.5, 150.6693377605, 38.7929844475)
                Line((-0.0696334177, 0.4178005063), (-0.4739801194, 2.8438807165))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is an elliptical composite structure featuring a shallow oval basin with radial internal ribs/reinforcements and a flat rim flange around the perimeter.
def model_30376_e4495332_0001():
    """Model: Canister Lid"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 216.4243179058, perimeter: 52.1504380496
            Circle(8.3)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


# Description: This is a parallelogram-shaped flat plate or wedge with a trapezoidal profile, featuring a thin beveled or angled edge on one side and a uniform thickness throughout, likely used as a structural component or spacer.
def model_30379_f1d5e193_0004():
    """Model: Motor Controller Housing Bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.16, perimeter: 6
            with BuildLine():
                Line((0.9, -0.6), (0.9, 0.6))
                Line((0.9, 0.6), (-0.9, 0.6))
                Line((-0.9, 0.6), (-0.9, -0.6))
                Line((-0.9, -0.6), (0.9, -0.6))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve with a hollow core, featuring a continuous pattern of parallel slots or perforations running along its length, and a curved or rounded outer surface.
def model_30379_f1d5e193_0009():
    """Model: Inner Race"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1178097245, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a cylindrical manifold or pressure vessel with a elongated horizontal body, rounded end caps, and internal passages or channels visible through the transparent sections, featuring what appears to be port connections or fittings on the ends.
def model_30379_f1d5e193_0015():
    """Model: Half Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0018397241, perimeter: 0.1723135674
            with BuildLine():
                Line((-0.0375, 0.2471714992), (-0.0375, 0.2))
                Line((-0.0375, 0.2), (0, 0.2))
                Line((0, 0.2), (0, 0.25))
                CenterArc((0, 0), 0.25, 90, 8.6269265587)
            make_face()
            # Profile area: 0.0018397241, perimeter: 0.1723135674
            with BuildLine():
                CenterArc((0, 0), 0.25, 81.3730734413, 8.6269265587)
                Line((0, 0.2), (0, 0.25))
                Line((0, 0.2), (0.0375, 0.2))
                Line((0.0375, 0.2), (0.0375, 0.2471714992))
            make_face()
            # Profile area: 0.1926700926, perimeter: 1.6648551887
            with BuildLine():
                CenterArc((0, 0), 0.25, 98.6269265587, 342.7461468826)
                Line((0.0375, 0.2), (0.0375, 0.2471714992))
                Line((0, 0.2), (0.0375, 0.2))
                Line((-0.0375, 0.2), (0, 0.2))
                Line((-0.0375, 0.2471714992), (-0.0375, 0.2))
            make_face()
            # Profile area: 0.0038205517, perimeter: 0.2559411381
            with BuildLine():
                CenterArc((0, 0), 0.25, 90, 8.6269265587)
                CenterArc((0, 0), 0.25, 81.3730734413, 8.6269265587)
                Line((0.0375, 0.2471714992), (0.0375, 0.3))
                Line((0.0375, 0.3), (-0.0375, 0.3))
                Line((-0.0375, 0.3), (-0.0375, 0.2471714992))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical sleeve or tube with an oval or elongated opening at the top and vertical ribbing or fluting along its outer surface.
def model_30380_4d422f95_0004():
    """Model: Master Rod Sleeve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.0089589025, perimeter: 28.5884931477
            with BuildLine():
                CenterArc((0, 0), 2.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or bushing with a uniform cross-section and a central circular hole, featuring a smooth curved outer surface and textured inner surfaces.
def model_30380_4d422f95_0005():
    """Model: Crank Case Bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.9070781255, perimeter: 35.8141562509
            with BuildLine():
                CenterArc((0, 0), 3.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a hollow cylindrical tube or sleeve with a slightly tapered, curved top end and vertical ribbing or fluting along its outer surface.
def model_30380_4d422f95_0011():
    """Model: Cylinder Lining"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5790922768, perimeter: 60.6327382143
            with BuildLine():
                CenterArc((0, 0), 4.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=17.5
        extrude(amount=17.5)
    return part.part


# Description: A claw hammer consisting of a long cylindrical shaft with a flat striking head on one end and a forked claw for nail removal on the opposite end.
def model_30389_3f514b04_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 21 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 270.6245860398, perimeter: 216.8074250476
            with BuildLine():
                Line((0, 0), (0, 76.2))
                Line((0, 0), (2.5, 0))
                Line((2.5, 76.2), (2.5, 0))
                Line((2.0164317902, 77.9525454746), (2.5, 76.2))
                Line((2.6795119063, 79.3597231629), (2.0164317902, 77.9525454746))
                Line((9.0136774708, 81.1074673139), (2.6795119063, 79.3597231629))
                Line((9.7520702455, 82.5978981348), (9.0136774708, 81.1074673139))
                Line((8.5000001267, 83.7000012472), (9.7520702455, 82.5978981348))
                Line((7.4730123355, 83.4637425915), (8.5000001267, 83.7000012472))
                Line((3.330603021, 81.6501908166), (7.4730123355, 83.4637425915))
                Line((1.5969179921, 81.2513563825), (3.330603021, 81.6501908166))
                Line((-4, 82.5986198757), (1.5969179921, 81.2513563825))
                Line((-7.8548182159, 82.5986198757), (-4, 82.5986198757))
                Line((-9.6499921426, 83.0307456097), (-7.8548182159, 82.5986198757))
                Line((-14.3095621697, 81.630661823), (-9.6499921426, 83.0307456097))
                Line((-14.6191243394, 79), (-14.3095621697, 81.630661823))
                Line((-14.6191243394, 77.0604861241), (-14.6191243394, 79))
                Line((-14, 75), (-14.6191243394, 77.0604861241))
                Line((-13.2104016144, 77.0604861241), (-14, 75))
                Line((-11.2678814626, 79.6359210055), (-13.2104016144, 77.0604861241))
                Line((-6, 80), (-11.2678814626, 79.6359210055))
                Line((-3.5221254048, 79.5969488709), (-6, 80))
                Line((-1.4884124526, 78.314825488), (-3.5221254048, 79.5969488709))
                Line((0, 76.2), (-1.4884124526, 78.314825488))
            make_face()
        # Symmetric extrude, each_side=1.25
        extrude(amount=1.25, both=True)
    return part.part


# Description: This is a rectangular frame or mounting bracket with a hollow center opening, featuring four corner reinforcement blocks and parallel slot or rib details running along the inner surfaces for structural rigidity.
def model_30400_8824ce97_0015():
    """Model: 18-03-001300-1_18-03-001302-1-solid1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180.6588505205, perimeter: 129.8761041673
            with BuildLine():
                Line((0, 0), (8.5, 0))
                Line((0, -16), (0, 0))
                Line((17, -16), (0, -16))
                Line((17, 0), (17, -16))
                Line((8.5, 0), (17, 0))
                Line((8.5, -4), (8.5, 0))
                Line((8.5, -4), (13.5, -4))
                Line((13.5, -4), (13.5, -12))
                Line((3.5, -12), (13.5, -12))
                Line((3.5, -4), (3.5, -12))
                Line((8.5, -4), (3.5, -4))
            make_face()
            with BuildLine():
                CenterArc((14.25, -13.5), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.75, -13.5), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.25, -2.5), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.75, -2.5), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a flat, elongated blue composite or plastic panel with a trapezoidal shape, featuring internal structural ribs, a central white cutout, and angular reinforcement patterns visible through its semi-transparent surface.
def model_30400_8824ce97_0032():
    """Model: 18-03-001200-1_18-03-001203-1-solid1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 203.2734535629, perimeter: 117.9557489045
            with BuildLine():
                Line((23.5, -10), (0, -10))
                Line((23.5, 0), (23.5, -10))
                Line((0, 0), (23.5, 0))
                Line((0, -10), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((5, -5), 2.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5251, -2.5251), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.4749, -2.5251), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.4749, -7.4749), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5251, -7.4749), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((12.55, -2.8), (12.55, -1.3))
                CenterArc((12.1, -2.8), 0.45, 180, 180)
                Line((11.65, -2.8), (11.65, -1.3))
                CenterArc((12.1, -1.3), 0.45, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((14.05, -2.8), (14.05, -1.3))
                CenterArc((13.6, -2.8), 0.45, 180, 180)
                Line((13.15, -1.3), (13.15, -2.8))
                CenterArc((13.6, -1.3), 0.45, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((14.05, -8.7), (14.05, -7.2))
                CenterArc((13.6, -8.7), 0.45, 180, 180)
                Line((13.15, -7.2), (13.15, -8.7))
                CenterArc((13.6, -7.2), 0.45, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((11.65, -7.2), (11.65, -8.7))
                CenterArc((12.1, -7.2), 0.45, 0, 180)
                Line((12.55, -8.7), (12.55, -7.2))
                CenterArc((12.1, -8.7), 0.45, 180, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a curved sheet metal duct or channel with a rectangular cross-section and a gentle longitudinal curve, featuring flanged edges along its length for structural rigidity and assembly purposes.
def model_30400_8824ce97_0033():
    """Model: 18-03-001200-1_18-03-001202-1-solid1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0346018366, perimeter: 17.5707963268
            with BuildLine():
                Line((0, 0), (0, -0.7))
                Line((0, -0.7), (3.6, -0.7))
                CenterArc((3.6, -1.7), 1, 0, 90)
                Line((4.6, -1.7), (4.6, -4))
                Line((5, -4), (4.6, -4))
                Line((5, 0), (5, -4))
                Line((0, 0), (5, 0))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


# Description: This is a complex aluminum or composite aerospace/defense component with an overall angular, wedge-like shape featuring multiple internal structural ribs, rectangular apertures or windows, and faceted exterior surfaces designed for lightweight structural efficiency.
def model_30400_8824ce97_0036():
    """Model: 18-03-001001-1-solid"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.9565952553, perimeter: 36.1283179278
            with BuildLine():
                Line((7.2, 0), (0, 0))
                Line((0, 0), (0, -4))
                Line((0, -4), (1, -4))
                Line((1, -4), (1, -7))
                Line((1, -7), (6.2, -7))
                Line((6.2, -4), (6.2, -7))
                Line((7.2, -4), (6.2, -4))
                Line((7.2, 0), (7.2, -4))
            make_face()
            with BuildLine():
                CenterArc((2.5, -1.5), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9, -1.5), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3, -1.5), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7, -1.5), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a cylindrical housing or barrel component with a rounded nose cone on one end, featuring symmetrical side flanges or mounting brackets and internal ribbed reinforcement structure visible through the semi-transparent rendering.
def model_30417_0010bc7c_0009():
    """Model: Shaft_3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0533812221, perimeter: 1.0147836558
            with BuildLine():
                CenterArc((-0.137330935, 0.6194598165), 0.2474728706, -14.3224351924, 60.9449416266)
                CenterArc((0, 0), 0.8, 87.6621175181, 4.6757649637)
                CenterArc((0.137330935, 0.6194598165), 0.2474728706, 133.3774935658, 60.9449416266)
                CenterArc((-0.1484738662, 0.5464898911), 0.0475, -74.8004052918, 89.1228404842)
                CenterArc((0, 0), 0.5188, 74.8004052918, 30.3991894165)
                CenterArc((0.1484738662, 0.5464898911), 0.0475, 165.6775648076, 89.1228404842)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is an oval or elliptical shell/cover with a smooth, curved surface and vertical ribbing or fluting pattern running across its face, featuring tapered edges that blend seamlessly into the rounded form.
def model_30417_0010bc7c_0010():
    """Model: Backing plate (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a long, flat rectangular bar or rail with a tapered/pointed left end, rounded right end with a circular hole or port, and linear slot details along its upper surface.
def model_30417_0010bc7c_0011():
    """Model: Motor pinion"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0071728409, perimeter: 0.3646859484
            with BuildLine():
                CenterArc((-0.0466337185, 0.2399096836), 0.0889252732, -14.7171065826, 56.6770459037)
                CenterArc((0, 0), 0.3, 86.2746347902, 7.4507304196)
                CenterArc((0.0466337185, 0.2399096836), 0.0889252732, 138.0400606789, 56.6770459037)
                CenterArc((-0.0540754071, 0.2134569988), 0.0152, -75.7842388173, 90.5013454)
                CenterArc((0, 0), 0.205, 75.7842388173, 28.4315223653)
                CenterArc((0.0540754071, 0.2134569988), 0.0152, 165.2828934174, 90.5013454)
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)
    return part.part


# Description: This is a cylindrical tube or barrel with a tapered, pointed nose cone on the left end and circular end caps on both sides, featuring a ribbed or corrugated surface texture throughout.
def model_30417_0010bc7c_0012():
    """Model: Shaft_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0126140461, perimeter: 0.4954940697
            with BuildLine():
                CenterArc((-0.0793467625, 0.3579101162), 0.1333879098, -10.465237929, 53.9251772501)
                CenterArc((0, 0), 0.45, 87.7746347902, 4.4507304196)
                CenterArc((0.0793467625, 0.3579101162), 0.1333879098, 136.5400606789, 53.9251772501)
                CenterArc((-0.0742430069, 0.32954031), 0.0228, -77.3036583248, 87.7688962538)
                CenterArc((0, 0), 0.315, 77.3036583248, 25.3926833505)
                CenterArc((0.0742430069, 0.32954031), 0.0228, 169.534762071, 87.7688962538)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a hemispherical bowl or dome with a flat rectangular top flange featuring triangular reinforcement ribs and mounting points.
def model_30417_0010bc7c_0015():
    """Model: Key"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.460482587, perimeter: 2.8675869348
            with BuildLine():
                Line((-0.575, -0.3031088913), (-0.575, -0.15))
                CenterArc((0, 0), 0.65, -152.204227504, 124.4084550079)
                Line((0.575, -0.15), (0.575, -0.3031088913))
                Line((-0.575, -0.15), (0.575, -0.15))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a toroidal (donut-shaped) mechanical component with a large central oval hole and radial ribbing or fin-like protrusions around its entire circumference, likely serving as a cooling element or structural reinforcement in an industrial application.
def model_30417_0010bc7c_0017():
    """Model: Washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.9015509452, perimeter: 12.1652091314
            with BuildLine():
                CenterArc((0, 0), 1.45, 0, 360)
            make_face()
            with BuildLine():
                Line((0.4, 0.3), (0.4, -0.3))
                CenterArc((0, 0), 0.5, -143.1301023542, 106.2602047083)
                Line((-0.4, 0.3), (-0.4, -0.3))
                CenterArc((0, 0), 0.5, 36.8698976458, 106.2602047083)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a regular hexagonal prism with chamfered or beveled edges along its top and bottom perimeters, creating an octagonal-like appearance when viewed from above, featuring flat faces and triangulated surface geometry.
def model_30417_0010bc7c_0018():
    """Model: Nut for Belleville"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((-2.3094010768, 0.0000000662), (-1.7320508219, 1.0000000083))
                Line((-1.7320507932, -0.9999999917), (-2.3094010768, 0.0000000662))
                Line((-0.5773502835, -0.9999999917), (-1.7320507932, -0.9999999917))
                Line((0, 0), (-0.5773502835, -0.9999999917))
                Line((-0.5773502549, 1.0000000083), (0, 0))
                Line((-1.7320508219, 1.0000000083), (-0.5773502549, 1.0000000083))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a rectangular flat panel or screen bezel with a dark surface and a gray border frame, featuring four corner mounting points and a diagonal cross-brace or support structure visible on the inner surface.
def model_30417_0010bc7c_0019():
    """Model: Motor cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 93.785, perimeter: 44.5247779608
            with BuildLine():
                CenterArc((-3.95, 4.825), 0.5, 90, 90)
                Line((-4.45, -4.825), (-4.45, 4.825))
                CenterArc((-3.95, -4.825), 0.5, 180, 90)
                Line((3.95, -5.325), (-3.95, -5.325))
                CenterArc((3.95, -4.825), 0.5, -90, 90)
                Line((4.45, 4.825), (4.45, -4.825))
                CenterArc((3.95, 4.825), 0.5, 0, 90)
                Line((-3.95, 5.325), (3.95, 5.325))
            make_face()
            with BuildLine():
                CenterArc((-3.95, -4.825), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.95, -4.825), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.95, 4.825), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.95, 4.825), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a ring-shaped washer or spacer with an oval/elliptical profile, featuring a textured or ribbed surface pattern across its outer and inner edges.
def model_30417_0010bc7c_0021():
    """Model: Washer (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.1526539202, perimeter: 22.3053078405
            with BuildLine():
                CenterArc((0, 0), 2.275, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a metal bracket or mounting arm with an angular, bent L-shaped design featuring two perpendicular sections connected by a curved transition, with slots or openings along the upper surface and reinforcing ribs on the dark gray/blue textured base.
def model_30418_de83ae84_0003():
    """Model: Part1 Base:1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0351640627, perimeter: 1.5265377381
            with BuildLine():
                Line((0.055, 0.075), (0.1867, 0.075))
                CenterArc((0.1867, 0), 0.075, 0, 90)
                Line((0.2617, 0), (0.4241, 0))
                Line((0.4241, 0.0375), (0.4241, 0))
                Line((0.3228, 0.0375), (0.4241, 0.0375))
                Line((0.3228, 0.0202), (0.3228, 0.0375))
                CenterArc((0.3168, 0.0202), 0.006, 180, 180)
                Line((0.3108, 0.0375), (0.3108, 0.0202))
                Line((0.3108, 0.0375), (0.2575962389, 0.1310400973))
                CenterArc((0.225, 0.1125), 0.0375, 29.6303645001, 60.3696354999)
                Line((0.025, 0.15), (0.225, 0.15))
                CenterArc((0.025, 0.1125), 0.0375, 90, 90)
                Line((-0.0125, 0.075), (-0.0125, 0.1125))
                Line((-0.0025, 0.075), (-0.0125, 0.075))
                CenterArc((-0.0025, 0.06875), 0.00625, -90, 180)
                Line((-0.025, 0.0625), (-0.0025, 0.0625))
                Line((-0.025, 0), (-0.025, 0.0625))
                Line((-0.025, 0), (0.0775, 0))
                Line((0.0775, 0.0625), (0.0775, 0))
                Line((0.055, 0.0625), (0.0775, 0.0625))
                CenterArc((0.055, 0.06875), 0.00625, 90, 180)
            make_face()
            with BuildLine():
                CenterArc((0.225, 0.1125), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.025, 0.1125), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0125
        extrude(amount=0.0125)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, tapered conical end, featuring a textured surface finish and uniform diameter along its length.
def model_30418_de83ae84_0004():
    """Model: giro"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            with Locations((-0.2254999911, 0.1294544379)):
                Circle(0.0125)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a flat, oval-shaped plate or pad with a textured, ribbed surface pattern and a slightly raised peripheral rim or flange around its edges.
def model_30419_d55a0a22_0000():
    """Model: lower platform"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 132.2286923118, perimeter: 44.5271909061
            Ellipse(9.21, 4.57)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is an oval or elliptical plate/base with a dark finish featuring two rectangular slots or cutouts on its upper surface, designed with a slightly domed or curved profile.
def model_30419_d55a0a22_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.6777508009, perimeter: 27.0627654757
            with BuildLine():
                EllipticalCenterArc((0, 0), 4.495, 3.05, 0, 360, 0)
            make_face()
            with BuildLine():
                CenterArc((-1.8503500353, -1.09), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0391337154, 1.11), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a cylindrical rod or pin with rounded ends, featuring a uniform diameter throughout its length and a slight surface texture or knurling pattern along its body.
def model_30421_211edb5e_0004():
    """Model: Pins"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-52, 32)):
                Circle(0.5)
        # TwoSides extrude, along=6, against=-2
        extrude(amount=6)
        extrude(sk.sketch, amount=-2)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with beveled edges on the corners, featuring a simple planar surface with no holes or slots, typical of a shim, spacer, or structural mounting plate.
def model_30426_2cde26de_0002():
    """Model: Tavola"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2363, perimeter: 213.3421356237
            with BuildLine():
                Line((39.8, 10), (34.8, 15))
                Line((-34.8, 15), (34.8, 15))
                Line((-39.8, 10), (-34.8, 15))
                Line((-39.8, -15), (-39.8, 10))
                Line((39.8, -15), (-39.8, -15))
                Line((39.8, 10), (39.8, -15))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is a square steel shaft or rod with a uniform cross-section and tapered or beveled ends, featuring a dark blue/gray metallic finish.
def model_30435_c97330d2_0012():
    """Model: CrossBraceShort1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -34.29), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.435475, perimeter: 27.94
            with BuildLine():
                Line((-72.39, -49.53), (-76.2, -49.53))
                Line((-76.2, -49.53), (-76.2, -53.34))
                Line((-76.2, -53.34), (-72.39, -53.34))
                Line((-72.39, -53.34), (-72.39, -49.53))
            make_face()
            with BuildLine():
                Line((-72.7075, -49.8475), (-75.8825, -49.8475))
                Line((-72.7075, -53.0225), (-72.7075, -49.8475))
                Line((-75.8825, -53.0225), (-72.7075, -53.0225))
                Line((-75.8825, -49.8475), (-75.8825, -53.0225))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=71.12
        extrude(amount=71.12)
    return part.part


# Description: This is a hexagonal rod or bar stock, characterized by its elongated prismatic shape with a uniform hexagonal cross-section and tapered or beveled ends.
def model_30435_c97330d2_0016():
    """Model: Leg2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.435475, perimeter: 27.94
            with BuildLine():
                Line((-72.39, 38.1), (-72.39, 34.29))
                Line((-76.2, 38.1), (-72.39, 38.1))
                Line((-76.2, 34.29), (-76.2, 38.1))
                Line((-72.39, 34.29), (-76.2, 34.29))
            make_face()
            with BuildLine():
                Line((-75.8825, 34.6075), (-75.8825, 37.7825))
                Line((-75.8825, 37.7825), (-72.7075, 37.7825))
                Line((-72.7075, 37.7825), (-72.7075, 34.6075))
                Line((-72.7075, 34.6075), (-75.8825, 34.6075))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=68.58
        extrude(amount=68.58)
    return part.part


# Description: This is a rounded rectangular bar or rail with two small rectangular slots or cutouts positioned symmetrically near each end on the top surface.
def model_30445_791b6800_0000():
    """Model: Component17"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-14.5682712752, 2.3659468695)):
                Circle(0.25)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a rounded rectangular bar or rod with a simple, elongated cylindrical shape featuring hemispherical or rounded ends, commonly used as a spacer, pin, or connector element in mechanical assemblies.
def model_30445_791b6800_0006():
    """Model: Component19"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-23.2447830126, 3.2211179593)):
                Circle(0.3)
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: A dark gray rounded rectangular bar or capsule-shaped solid with uniform width and length, featuring smoothly rounded ends and no visible holes or features.
def model_30445_791b6800_0007():
    """Model: Component20"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((-17.3049899588, 3.6353638602), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-17.3049899588, 3.6353638602), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)
    return part.part


# Description: This is a parallelogram-shaped structural frame or tray with a hollow interior, featuring a reinforced border/flange around the perimeter and internal cross-bracing or support ribs for structural rigidity.
def model_30445_791b6800_0010():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.6151548999, perimeter: 26.398229715
            with BuildLine():
                Line((4.6788521913, 0.871277209), (-1.3211478087, 0.871277209))
                Line((-1.3211478087, 0.871277209), (-1.3211478087, -4.128722791))
                Line((-1.3211478087, -4.128722791), (4.6788521913, -4.128722791))
                Line((4.6788521913, -4.128722791), (4.6788521913, 0.871277209))
            make_face()
            with BuildLine():
                CenterArc((-0.6211478087, 0.171277209), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.9788521913, 0.171277209), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.9788521913, -3.428722791), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.6211478087, -3.428722791), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a rectangular tray or shallow box with a flat bottom, four raised wall flanges around the perimeter, and an open top designed for holding or organizing contents.
def model_30445_791b6800_0013():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.6151548999, perimeter: 26.398229715
            with BuildLine():
                Line((5.0001702446, -10.8526522673), (-0.9998296486, -10.8537845642))
                Line((4.9992266638, -5.8526523563), (5.0001702446, -10.8526522673))
                Line((-1.0007732294, -5.8537846532), (4.9992266638, -5.8526523563))
                Line((-0.9998296486, -10.8537845642), (-1.0007732294, -5.8537846532))
            make_face()
            with BuildLine():
                CenterArc((4.3000381557, -10.152784381), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2993587775, -6.5527844451), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.3006411405, -6.5536525395), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.2999617624, -10.1536524754), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical rifle handguard with a ribbed exterior surface, featuring ventilation slots along its length and a cutout window, designed to protect the barrel while providing ergonomic grip and heat dissipation.
def model_30445_791b6800_0014():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 27 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.514884393, perimeter: 35.7409001574
            with BuildLine():
                Line((-5.6037483566, 0.8939675625), (-5.530489223, 11.3937119926))
                CenterArc((-6.5501956812, 8.5728049716), 2.9995529138, 70.1260006402, 38.9484800108)
                Line((-7.6036996767, 0.9079216831), (-7.5304405431, 11.4076661133))
                Line((-7.6036996767, 0.9079216831), (-7.2037094126, 0.905130859))
                Line((-7.2037094126, 0.905130859), (-7.2071979428, 0.405143029))
                Line((-7.2071979428, 0.405143029), (-6.0072271508, 0.3967705566))
                Line((-6.0037386206, 0.8967583866), (-6.0072271508, 0.3967705566))
                Line((-5.6037483566, 0.8939675625), (-6.0037386206, 0.8967583866))
            make_face()
            with BuildLine():
                CenterArc((-6.2432465801, 9.5677268374), 0.15115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.8432611845, 9.5677268374), 0.15115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.5520937701, 8.3007645069), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.9939123195, 2.305096783), 0.12295, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.1939415282, 2.305096783), 0.12295, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.9827484795, 3.9051357279), 0.12295, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.1939415282, 3.9051357279), 0.12295, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.5883744839, 3.1008910748), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a horizontal support beam or crossmember with a blue/gray rectangular tube body and black reinforced end flanges on both sides, designed for structural bracing or mounting applications.
def model_30447_4ed3b778_0001():
    """Model: Valve Link Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1623587763, perimeter: 4.1698145723
            with BuildLine():
                CenterArc((1.70688, 0), 0.11049, -180, 180)
                Line((0, 0), (1.59639, 0))
                Line((0, -0.08128), (0, 0))
                Line((0, -0.08128), (1.47066, -0.08128))
                Line((1.47066, -0.08128), (1.47066, -0.15748))
                Line((1.47066, -0.15748), (1.86436, -0.15748))
                Line((1.86436, -0.15748), (1.86436, 0))
                Line((1.81737, 0), (1.86436, 0))
            make_face()
            # Profile area: 0.3247175525, perimeter: 5.0528691446
            with BuildLine():
                Line((0, 0.08128), (0, 0))
                Line((0, 0.08128), (-1.47066, 0.08128))
                Line((-1.47066, 0.08128), (-1.47066, 0.15748))
                Line((-1.47066, 0.15748), (-1.86436, 0.15748))
                Line((-1.86436, -0.15748), (-1.86436, 0.15748))
                Line((-1.47066, -0.15748), (-1.86436, -0.15748))
                Line((-1.47066, -0.08128), (-1.47066, -0.15748))
                Line((0, -0.08128), (-1.47066, -0.08128))
                Line((0, -0.08128), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-1.70688, 0), 0.11049, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1623587763, perimeter: 4.1698145723
            with BuildLine():
                Line((1.81737, 0), (1.86436, 0))
                Line((1.86436, 0.15748), (1.86436, 0))
                Line((1.47066, 0.15748), (1.86436, 0.15748))
                Line((1.47066, 0.08128), (1.47066, 0.15748))
                Line((0, 0.08128), (1.47066, 0.08128))
                Line((0, 0.08128), (0, 0))
                Line((0, 0), (1.59639, 0))
                CenterArc((1.70688, 0), 0.11049, 0, 180)
            make_face()
        # Symmetric extrude, each_side=0.08128
        extrude(amount=0.08128, both=True)
    return part.part


# Description: This is a curved protective shroud or housing component with a streamlined, elongated shape featuring blue mesh or ventilation panels on the sides and dark gray end caps, designed to cover and protect internal components while allowing airflow.
def model_30447_4ed3b778_0003():
    """Model: Valve Link Bellcrank"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.088141766, perimeter: 1.9550131083
            with BuildLine():
                CenterArc((0.635, 0), 0.20066, 81.9521537528, 196.0956924945)
                CenterArc((0.635, 0), 0.20066, -81.9521537527, 163.9043075055)
            make_face()
            with BuildLine():
                CenterArc((0.635, 0), 0.11049, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1842337723, perimeter: 2.8168148051
            with BuildLine():
                CenterArc((0, 0), 0.28956, 174.6445993869, 103.4032468604)
                CenterArc((0, 0), 0.28956, -81.9521537527, 256.5967531396)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.088141766, perimeter: 1.9550131083
            with BuildLine():
                CenterArc((0, 0.9525), 0.20066, 174.6445993869, 190.7108012261)
                CenterArc((0, 0.9525), 0.20066, 5.3554006131, 169.2891987739)
            make_face()
            with BuildLine():
                CenterArc((0, 0.9525), 0.11049, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3880966281, perimeter: 5.2997801197
            with BuildLine():
                CenterArc((0, 0), 0.28956, -81.9521537527, 256.5967531396)
                Line((0.0405384, -0.2867082694), (0.6630924, -0.1986838007))
                CenterArc((0.635, 0), 0.20066, 81.9521537528, 196.0956924945)
                Line((0.4233395545, 0.2325830558), (0.6630924, 0.1986838007))
                CenterArc((0.4513395545, 0.4306133565), 0.2, -174.6445993869, 76.5967531396)
                Line((0.1997841025, 0.9712282667), (0.252212571, 0.4119466898))
                CenterArc((0, 0.9525), 0.20066, 174.6445993869, 190.7108012261)
                Line((-0.1997841025, 0.9712282667), (-0.2882960467, 0.0270256))
            make_face()
        # Symmetric extrude, each_side=0.079375
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a circular disc with a reinforced mesh or textured rim around its outer edge, featuring a flat front face and a perforated or latticed band running along the circumference, commonly used as a filter, strainer, or structural reinforcement component.
def model_30447_4ed3b778_0006():
    """Model: Flywheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 45.2869809443, perimeter: 25.9338473554
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.635
        extrude(amount=0.635, both=True)
    return part.part


# Description: This is a rectangular tray or sliding mechanism with a flat base platform, angled side walls, and two parallel slots or guide rails running along the top surface for linear motion or component alignment.
def model_30447_4ed3b778_0016():
    """Model: Steam Chest Cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2812082016, perimeter: 8.1868639169
            with BuildLine():
                Line((0.79375, 1.5875), (0.79375, -0.9525))
                Line((0.79375, 1.5875), (0.39751, 1.5875))
                Line((0.39751, 1.5875), (0.39751, 1.11125))
                CenterArc((0.23876, 1.11125), 0.15875, -90, 90)
                Line((-0.79375, 0.9525), (0.23876, 0.9525))
                Line((-0.79375, -0.9525), (-0.79375, 0.9525))
                Line((0.79375, -0.9525), (-0.79375, -0.9525))
            make_face()
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875)
    return part.part


# Description: This is a black plastic mounting bracket or clamp with an angular hook-shaped head on one end and a flat, elongated body with internal ribbing or reinforcement features for structural support.
def model_30637_f6324fc6_0009():
    """Model: Component12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 83.4890872221, perimeter: 65.9365019775
            with BuildLine():
                CenterArc((-9.8, 4.8), 0.2, 90, 90)
                Line((-10, 4.8), (-10, 1.7))
                CenterArc((-9.8, 1.7), 0.2, 180, 90)
                Line((-9.8, 1.5), (-5.533383448, 1.5))
                CenterArc((-5.533383448, 1.3), 0.2, 71.0474191873, 18.9525808127)
                Line((-5.4684263456, 1.4891575398), (9.4487141234, -3.6334202989))
                Line((9.4487141234, -3.6334202989), (17, -3.6334202989))
                Line((17, -3.6334202989), (17, -3.5000000298))
                CenterArc((16.5, -3.5000000298), 0.5, 0, 89.9999982925)
                Line((16.5000000149, -3.0000000298), (15.6040275241, -3.0000000031))
                CenterArc((18.8823281383, 5.1526837192), 8.7871216444, -128.3473753419, 16.4416716813)
                CenterArc((17.4633344787, 3.3589773859), 6.5, -157.5910952681, 29.2437199262)
                CenterArc((9.9796176939, 0.2730511399), 1.5949958438, 22.4089047319, 82.4827745507)
                CenterArc((9.6211142949, 1.6211938315), 0.2, 104.8916792826, 118.8384587268)
                Line((9.4765935676, 1.4829413112), (9.8086416392, 1.1358385699))
                CenterArc((9.9796176939, 0.2730511399), 0.8795652112, -124.260499662, 225.4694165337)
                Line((-5.4668613675, 4.9879385242), (9.4844608345, -0.4538977203))
                CenterArc((-5.5352653961, 4.8), 0.2, 70, 20)
                Line((-9.8, 5), (-5.5352653961, 5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical tube or barrel with rounded ends (capsule shape) featuring multiple longitudinal slots or grooves running along its length, with blue highlights indicating specific surface features or details.
def model_30690_3df2c9e2_0003():
    """Model: Pasador de Expansión"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1834895869, perimeter: 3.8705031424
            with BuildLine():
                CenterArc((-27.5, 25), 0.35, -85.9039562418, 351.8079124837)
                Line((-27.525, 24.7512531407), (-27.525, 24.6508939989))
                CenterArc((-27.5, 25), 0.25, -84.2608295227, 348.5216590455)
                Line((-27.475, 24.7512531407), (-27.475, 24.6508939989))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


# Description: This is a adjustable hose clamp (or worm-gear clamp) featuring a circular band with a textured surface and a tightening mechanism on one side, designed to secure hoses or tubes by compressing them with the adjustable screw mechanism.
def model_30690_3df2c9e2_0005():
    """Model: Anillo de retención"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.78915204, perimeter: 13.3855648294
            with BuildLine():
                Line((-11.3064272042, -14.5878386209), (-11.3064272042, -14.912900544))
                CenterArc((-11.3264272042, -13.7130672222), 1.2, -89.0450261262, 8.7698638753)
                Line((-11.1237272042, -14.6923081068), (-11.1237272042, -14.8958236257))
                CenterArc((-11.3264272042, -13.7130672222), 1, -78.3051077337, 336.6102154674)
                Line((-11.5291272042, -14.6923081068), (-11.5291272042, -14.8958236257))
                CenterArc((-11.3264272042, -13.7130672222), 1.2, -99.7248377491, 8.7698638753)
                Line((-11.3464272042, -14.5878386209), (-11.3464272042, -14.912900544))
                CenterArc((-11.3264272042, -13.7130672222), 0.875, -88.690268121, 357.380536242)
            make_face()
            with BuildLine():
                CenterArc((-11.2150772042, -14.7940658663), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.4377772042, -14.7940658663), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is an elongated rectangular bracket or connector with a cylindrical rounded profile at both ends, featuring two mounting holes at the top and bottom and a central slot or channel running along its length.
def model_30690_3df2c9e2_0007():
    """Model: Riostra"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.6448116878, perimeter: 23.6142627476
            with BuildLine():
                CenterArc((-33.9834, 18.9833), 1.0167, 0, 89.9943645343)
                CenterArc((-33.9833, 18.9833), 1.0167, 90, 90)
                Line((-35, 18.9833), (-35, 12.8834))
                CenterArc((-33.9833, 12.8834), 1.0167, 180, 90)
                CenterArc((-33.9834, 12.8834), 1.0167, -89.9943645343, 89.9943645343)
                Line((-32.9667, 18.9833), (-32.9667, 12.8834))
            make_face()
            with BuildLine():
                CenterArc((-33.9833, 18.9833), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-33.9833, 12.8834), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a horseshoe-shaped magnetic core or ferrite ring with a C-shaped cross-section, featuring a central open gap and internal cylindrical surfaces designed to guide magnetic flux or accommodate coil windings.
def model_30690_3df2c9e2_0015():
    """Model: Anillo de retención 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.242107191, perimeter: 5.0308801009
            with BuildLine():
                CenterArc((-29, 19), 0.5, -56.1551275083, 292.3102550166)
                CenterArc((-29.2506258121, 18.6262531575), 0.05, -123.8448724917, 93.0998086614)
                CenterArc((-29.2981755933, 18.6431858809), 0.1, -25.1466603841, 75.262476595)
                CenterArc((-29, 19), 0.365, -175.644227373, 45.7600435839)
                CenterArc((-29.3938591119, 18.97), 0.03, 4.355772627, 85.644227373)
                CenterArc((-29.3938591119, 19.03), 0.03, 175.644227373, 94.3557726269)
                CenterArc((-29, 19), 0.425, 112.2593873892, 63.3848399837)
                CenterArc((-29.1231100824, 19.3007804974), 0.1, 52.0080748931, 60.251312496)
                CenterArc((-29, 19.4584), 0.1, -127.9919251069, 75.9838502138)
                CenterArc((-28.8768899176, 19.3007804974), 0.1, 67.7406126109, 60.251312496)
                CenterArc((-29, 19), 0.425, 4.355772627, 63.3848399837)
                CenterArc((-28.6061408881, 19.03), 0.03, -89.9999999998, 94.3557726269)
                CenterArc((-28.6061408881, 18.97), 0.03, 90, 85.644227373)
                CenterArc((-29, 19), 0.365, -50.1158162109, 45.7600435839)
                CenterArc((-28.7018244067, 18.6431858809), 0.1, 129.8841837891, 75.2624765949)
                CenterArc((-28.7493741879, 18.6262531575), 0.05, -149.25493617, 93.0998086616)
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a cylindrical shaft or rod with a long, slender tubular body and rounded ends, featuring a slight taper or chamfer at both extremities.
def model_30690_3df2c9e2_0018():
    """Model: Soporte"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-24.1089471048, -7.8977585343)):
                Circle(0.7)
        # OneSide extrude, distance=13.55
        extrude(amount=13.55)
    return part.part


# Description: This is a cylindrical tube or pipe component with a hemispherical end cap on the left side and an open or recessed circular end on the right, featuring a hollow interior cavity running through its length.
def model_30690_3df2c9e2_0019():
    """Model: Pasador de resorte"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.214907135, perimeter: 4.4986619876
            with BuildLine():
                Line((-16.4647741705, 26.3181372148), (-16.4647741705, 26.2178757478))
                CenterArc((-16.4897741705, 26.6170937333), 0.4, -86.4166783015, 352.8333566031)
                Line((-16.5147741705, 26.3181372148), (-16.5147741705, 26.2178757478))
                CenterArc((-16.4897741705, 26.6170937333), 0.3, -85.2198081528, 350.4396163056)
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a tapered coffin or casket shape with a hexagonal cross-section, featuring a hinged or split lid design (shown in blue) and a darker base body with internal structural ribbing and a rectangular slot or opening at the foot end.
def model_30708_4282508b_0000():
    """Model: Component19"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-19.05, 1.2700001216, 30.48), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.4139806628, perimeter: 14.0749263284
            with BuildLine():
                CenterArc((21.2090705526, 3.5560238944), 0.2667232867, 72.2147800498, 16.7075210216)
                Line((21.59, 3.81), (21.290541096, 3.81))
                Line((21.59, 2.933674147), (21.59, 3.81))
                Line((21.59, 2.933674147), (22.2505340817, 2.933674147))
                Line((22.2505340817, 2.933674147), (22.2505340817, 4.838674147))
                Line((18.3894672153, 4.838674147), (22.2505340817, 4.838674147))
                Line((18.3894672153, 2.933674147), (18.3894672153, 4.838674147))
                Line((19.6594672153, 2.933674147), (18.3894672153, 2.933674147))
                CenterArc((19.6594659183, 2.946374147), 0.0127, -89.9941486253, 89.9881804004)
                Line((19.6722003138, 3.2765754686), (19.6721659182, 2.9463728241))
                CenterArc((19.6595003139, 3.2765767915), 0.0127, -0.0059682249, 89.9999985922)
                Line((19.4309016575, 3.2893006092), (19.6595016371, 3.2892767914))
                CenterArc((19.4309294474, 3.5560238944), 0.2667232867, 91.0776989286, 178.9163314386)
                Line((21.2140871604, 3.8227), (19.4259128396, 3.8227))
            make_face()
            # Profile area: 0.3084894745, perimeter: 3.1390645862
            with BuildLine():
                CenterArc((21.2090705526, 3.5560238944), 0.2667232867, -89.9940303673, 162.208810417)
                Line((20.9804983629, 3.2892767914), (21.2090983425, 3.2893006092))
                CenterArc((20.9804996861, 3.2765767915), 0.0127, 90.0059696327, 89.9999985922)
                Line((20.9678340818, 2.9463728241), (20.9677996862, 3.2765754686))
                CenterArc((20.9805340817, 2.946374147), 0.0127, -179.9940317751, 89.9940317751)
                Line((20.9805340817, 2.933674147), (21.59, 2.933674147))
                Line((21.59, 2.933674147), (21.59, 3.81))
                Line((21.59, 3.81), (21.290541096, 3.81))
            make_face()
        # OneSide extrude, distance=-10.16
        extrude(amount=-10.16)
    return part.part


# Description: This is a cylindrical sleeve or ring with a curved, tapered profile featuring vertical ribbing or fluting along its exterior surface and a smooth interior bore.
def model_30713_06b3d0ec_0002():
    """Model: Ruedabien"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 75.3982236862, perimeter: 150.7964473723
            with BuildLine():
                CenterArc((0, 0), 12.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 11.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=5.25
        extrude(amount=5.25, both=True)
    return part.part


# Description: This is an elliptical parabolic reflector or antenna dish featuring a wireframe skeletal structure with radial support ribs converging toward the center, a curved perimeter rim, and a dark reinforced edge band, commonly used in satellite communications or radio astronomy applications.
def model_30713_06b3d0ec_0014():
    """Model: TapaEmbellecedor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            Circle(1.7)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a bracket or mounting component with a curved, angular design featuring a main body with ribbed reinforcement sections, a protruding flange on one end, and internal hollow sections, likely designed to provide structural support while minimizing weight.
def model_30713_06b3d0ec_0016():
    """Model: FijaciónE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 61.5518657083, perimeter: 59.1412017448
            with BuildLine():
                CenterArc((3.2656977611, -6.9366435025), 0.9633564975, -159.4218360905, 69.4218360905)
                Line((3.2656977611, -7.9), (7.0299718927, -7.9))
                CenterArc((7.0299718927, -7.4756226185), 0.4243773815, -90, 131.8912309335)
                CenterArc((13.2618885853, 1.4895878378), 10.505881843, -168.9040759111, 44.6326813333)
                CenterArc((0, 0), 3, -10.2201352042, 200.4402704083)
                CenterArc((-13.2618885853, 1.4895878378), 10.505881843, -55.7286054222, 44.6326813333)
                CenterArc((-7.0299718927, -7.4756226185), 0.4243773815, 138.1087690665, 131.8912309335)
                Line((-7.0299718927, -7.9), (-3.2656977611, -7.9))
                CenterArc((-3.2656977611, -6.9366435025), 0.9633564975, -90, 69.4218360905)
                CenterArc((4.7271697032, -7.3886598777), 7.0918861916, 140.7440542188, 38.3396512914)
                CenterArc((0, 0), 3, -104.7591497578, 29.5182995155)
                CenterArc((-4.7271697032, -7.3886598777), 7.0918861916, 0.9162944898, 38.3396512914)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is a cylindrical roller or spacer with a dark gray body and blue mesh-textured end caps, featuring a hollow central axis and symmetrical design for alignment or support applications.
def model_30729_b4d83b07_0002():
    """Model: 16 Hand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1101767271, perimeter: 20.7345115137
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


# Description: This is a cylindrical rod or dowel pin with a uniform diameter and rounded ends, featuring a smooth, tapered finish at both extremities.
def model_30729_b4d83b07_0005():
    """Model: 11 Pin 2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # Symmetric extrude, each_side=19
        extrude(amount=19, both=True)
    return part.part


# Description: This is a cylindrical suppressor or silencer featuring a tubular body with a slightly tapered threaded end cap, designed to reduce firearm noise signature.
def model_30729_b4d83b07_0007():
    """Model: 9 Pin v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, each_side=7
        extrude(amount=7, both=True)
    return part.part


# Description: A long, slender tire lever with a curved hook at the top end and a small circular hole near the bottom end, designed for prying and removing tires from wheel rims.
def model_30729_b4d83b07_0012():
    """Model: 12 Bar support v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 127.1912642435, perimeter: 80.0639902413
            with BuildLine():
                Line((-2.5, -1.5), (-2.5, 2.9772373242))
                CenterArc((-1.5, -1.5), 1, 180, 90)
                Line((-1.5, -2.5), (1.5, -2.5))
                CenterArc((1.5, -1.5), 1, -90, 90)
                Line((2.5, -1.5), (2.5, 5.1273669299))
                CenterArc((-39.4301111869, 5.1273669299), 41.9301111869, 0, 28.1413504444)
                CenterArc((-5.3133899982, 23.3756536505), 3.2396649126, 28.1413504444, 141.7017443364)
                Line((-8.5022845771, 23.9469505184), (-8.5281173247, 23.8027559437))
                CenterArc((-8.0359530632, 23.7145837278), 0.5, 169.8430947808, 175.1145599949)
                CenterArc((-6.1044845056, 23.1955180179), 1.5, 11.8848312789, 153.0728234968)
                CenterArc((-102.173146, 2.9772373242), 99.673146, 0, 11.8848312789)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: A dark gray cylindrical tube or pipe with slightly rounded ends, tilted at an angle, featuring a smooth cylindrical body with no visible holes, slots, or flanges.
def model_30729_b4d83b07_0017():
    """Model: 10 Bar Support v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.5924768917, perimeter: 25.7610597594
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a hexagonal steel pin or rod with a long, slender cylindrical body and a tapered or chamfered end, commonly used as a fastener, alignment pin, or dowel in mechanical assemblies.
def model_30729_b4d83b07_0018():
    """Model: 3 Structure v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.5446900494, perimeter: 56.9646003294
            with BuildLine():
                CenterArc((-1.5, -3.5), 1.5, -180, 90)
                Line((-1.5, -5), (1.5, -5))
                CenterArc((1.5, -3.5), 1.5, -90, 90)
                Line((3, -3.5), (3, 3.5))
                CenterArc((1.5, 3.5), 1.5, 0, 90)
                Line((1.5, 5), (-1.5, 5))
                CenterArc((-1.5, 3.5), 1.5, 90, 90)
                Line((-3, 3.5), (-3, -3.5))
            make_face()
            with BuildLine():
                Line((1.5, 4.7), (-1.5, 4.7))
                CenterArc((1.5, 3.5), 1.2, 0, 90)
                Line((2.7, -3.5), (2.7, 3.5))
                CenterArc((1.5, -3.5), 1.2, -90, 90)
                Line((-1.5, -4.7), (1.5, -4.7))
                CenterArc((-1.5, -3.5), 1.2, -180, 90)
                Line((-2.7, 3.5), (-2.7, -3.5))
                CenterArc((-1.5, 3.5), 1.2, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=75
        extrude(amount=75, both=True)
    return part.part


# Description: This is a tapered cylindrical rod or shaft with a gradual conical reduction from a thicker end to a pointed tip, featuring a smooth, continuous surface.
def model_30904_54099e05_0008():
    """Model: Vertical de la pizarra v6 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0707963268, perimeter: 8.1415926536
            with BuildLine():
                CenterArc((0, -0.5), 1, 0, 180)
                Line((-1, -1.5), (-1, -0.5))
                Line((-0.5, -1.5), (-1, -1.5))
                Line((-0.5, -1), (-0.5, -1.5))
                Line((0.5, -1), (-0.5, -1))
                Line((0.5, -1.5), (0.5, -1))
                Line((1, -1.5), (0.5, -1.5))
                Line((1, -0.5), (1, -1.5))
            make_face()
        # Symmetric extrude, each_side=71
        extrude(amount=71, both=True)
    return part.part


# Description: This is a simple tapered rod or cone pin with a straight, elongated cylindrical shape that gradually decreases in diameter from one end to the other.
def model_30904_54099e05_0009():
    """Model: Horizontal de la pizarra v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0707963268, perimeter: 8.1415926536
            with BuildLine():
                CenterArc((0, -0.5), 1, 0, 180)
                Line((-1, -1.5), (-1, -0.5))
                Line((-0.5, -1.5), (-1, -1.5))
                Line((-0.5, -1), (-0.5, -1.5))
                Line((0.5, -1), (-0.5, -1))
                Line((0.5, -1.5), (0.5, -1))
                Line((1, -1.5), (0.5, -1.5))
                Line((1, -0.5), (1, -1.5))
            make_face()
        # Symmetric extrude, each_side=96
        extrude(amount=96, both=True)
    return part.part


# Description: This is an elongated rectangular bar or beam with a tapered hexagonal cross-section, featuring beveled edges on the ends and a slight curved top surface, designed as a structural or support component.
def model_30904_54099e05_0016():
    """Model: Pie de la pizarra v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 29 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.4106192983, perimeter: 82.0530964915
            with BuildLine():
                CenterArc((-3.1587093472, 8.3687808681), 1, 90, 90)
                Line((-4.1587093472, -1.6312191319), (-4.1587093472, 8.3687808681))
                CenterArc((-3.1587093472, -1.6312191319), 1, 180, 90)
                Line((4.8412906528, -2.6312191319), (-3.1587093472, -2.6312191319))
                CenterArc((4.8412906528, -1.6312191319), 1, -90, 90)
                Line((5.8412906528, 8.3687808681), (5.8412906528, -1.6312191319))
                CenterArc((4.8412906528, 8.3687808681), 1, 0, 90)
                Line((-3.1587093472, 9.3687808681), (4.8412906528, 9.3687808681))
            make_face()
            with BuildLine():
                Line((-3.1587093472, 8.9687808681), (4.8412906528, 8.9687808681))
                CenterArc((4.8412906528, 8.3687808681), 0.6, 0, 90)
                Line((5.4412906528, 8.3687808681), (5.4412906528, -1.6312191319))
                CenterArc((4.8412906528, -1.6312191319), 0.6, -90, 90)
                Line((4.8412906528, -2.2312191319), (-3.1587093472, -2.2312191319))
                CenterArc((-3.1587093472, -1.6312191319), 0.6, 179.9999881612, 90.0000118388)
                Line((-3.7587093472, -1.6312190079), (-3.7587093472, 8.3687808681))
                CenterArc((-3.1587093472, 8.3687808681), 0.6, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=50
        extrude(amount=50, both=True)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a smooth, curved cross-section and a central hollow opening, featuring textured surface detailing on portions of the outer and inner surfaces.
def model_31096_cf2a94f6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 62.8318530718, perimeter: 62.8318530718
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a triangular prism or wedge-shaped part with a pointed apex on the left and a rectangular face on the right, featuring a simple geometric form with flat surfaces and sharp edges.
def model_31106_7fcb831a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5500, perimeter: 341.6609194719
            with BuildLine():
                Line((-50, 0), (50, 0))
                Line((50, 0), (0, 110))
                Line((0, 110), (-50, 0))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a wedge-shaped or trapezoidal prism block with a slanted top surface and angled side faces, featuring a uniform thickness and sharp geometric edges characteristic of a basic structural or mounting component.
def model_31116_0b0aa2be_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 171.370625, perimeter: 53.34
            with BuildLine():
                Line((-7.9375, 5.3975), (7.9375, 5.3975))
                Line((-7.9375, -5.3975), (-7.9375, 5.3975))
                Line((7.9375, -5.3975), (-7.9375, -5.3975))
                Line((7.9375, 5.3975), (7.9375, -5.3975))
            make_face()
        # OneSide extrude, distance=4.445
        extrude(amount=4.445)
    return part.part


# Description: This is a cross-shaped or X-shaped bracket or connector featuring four cylindrical arms extending from a central junction, with black reinforced edges and blue structural webbing or ribbing between the arms for rigidity.
def model_31245_b2c86b4e_0000():
    """Model: base plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1818815433, perimeter: 8.9039645632
            with BuildLine():
                Line((2, -2), (4.582575695, -2))
                Line((2, -4.582575695), (2, -2))
                CenterArc((0, 0), 5, -66.4218215218, 42.8436430436)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((-2, -12.5), (2, -12.5))
                CenterArc((0, -12.5), 2, 180, 180)
            make_face()
            # Profile area: 4.1818815433, perimeter: 8.9039645632
            with BuildLine():
                Line((-2, -2), (-2, -4.582575695))
                Line((-4.582575695, -2), (-2, -2))
                CenterArc((0, 0), 5, -156.4218215218, 42.8436430436)
            make_face()
            # Profile area: 4.1818815433, perimeter: 8.9039645632
            with BuildLine():
                Line((2, 2), (2, 4.582575695))
                Line((4.582575695, 2), (2, 2))
                CenterArc((0, 0), 5, 23.5781784782, 42.8436430436)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((12.5, -2), (12.5, 2))
                CenterArc((12.5, 0), 2, -90, 180)
            make_face()
            # Profile area: 24.2637421512, perimeter: 26.2332023779
            with BuildLine():
                CenterArc((0, 0), 5, -113.5781784782, 47.1563569564)
                Line((-2, -4.582575695), (-2, -12.5))
                CenterArc((0, -12.5), 2, 0, 180)
                Line((2, -12.5), (2, -4.582575695))
            make_face()
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((-2, 2), (-2, -2))
                Line((-2, -2), (2, -2))
                Line((2, -2), (2, 2))
                Line((2, 2), (-2, 2))
            make_face()
            # Profile area: 4.1818815433, perimeter: 8.9039645632
            with BuildLine():
                Line((-2, 2), (-4.582575695, 2))
                Line((-2, 4.582575695), (-2, 2))
                CenterArc((0, 0), 5, 113.5781784782, 42.8436430436)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((2, 12.5), (-2, 12.5))
                CenterArc((0, 12.5), 2, 0, 180)
            make_face()
            # Profile area: 24.2637421512, perimeter: 26.2332023779
            with BuildLine():
                CenterArc((0, 0), 5, -23.5781784782, 47.1563569564)
                Line((4.582575695, -2), (12.5, -2))
                CenterArc((12.5, 0), 2, 90, 180)
                Line((12.5, 2), (4.582575695, 2))
            make_face()
            # Profile area: 11.4530725416, perimeter: 13.2803198506
            with BuildLine():
                CenterArc((0, 0), 5, 156.4218215218, 47.1563569564)
                Line((-4.582575695, -2), (-2, -2))
                Line((-2, 2), (-2, -2))
                Line((-2, 2), (-4.582575695, 2))
            make_face()
            # Profile area: 24.2637421512, perimeter: 26.2332023779
            with BuildLine():
                CenterArc((-12.5, 0), 2, -90, 180)
                Line((-12.5, -2), (-4.582575695, -2))
                CenterArc((0, 0), 5, 156.4218215218, 47.1563569564)
                Line((-4.582575695, 2), (-12.5, 2))
            make_face()
            # Profile area: 24.2637421512, perimeter: 26.2332023779
            with BuildLine():
                CenterArc((0, 0), 5, 66.4218215218, 47.1563569564)
                Line((2, 4.582575695), (2, 12.5))
                CenterArc((0, 12.5), 2, 180, 180)
                Line((-2, 12.5), (-2, 4.582575695))
            make_face()
            # Profile area: 11.4530725416, perimeter: 13.2803198506
            with BuildLine():
                Line((2, -4.582575695), (2, -2))
                Line((-2, -2), (2, -2))
                Line((-2, -2), (-2, -4.582575695))
                CenterArc((0, 0), 5, -113.5781784782, 47.1563569564)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((-12.5, 0), 2, 90, 180)
                Line((-12.5, 2), (-12.5, -2))
            make_face()
            # Profile area: 11.4530725416, perimeter: 13.2803198506
            with BuildLine():
                Line((4.582575695, 2), (2, 2))
                Line((2, -2), (2, 2))
                Line((2, -2), (4.582575695, -2))
                CenterArc((0, 0), 5, -23.5781784782, 47.1563569564)
            make_face()
            # Profile area: 11.4530725416, perimeter: 13.2803198506
            with BuildLine():
                Line((-2, 4.582575695), (-2, 2))
                Line((2, 2), (-2, 2))
                Line((2, 2), (2, 4.582575695))
                CenterArc((0, 0), 5, 66.4218215218, 47.1563569564)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((0, -12.5), 2, 0, 180)
                Line((-2, -12.5), (2, -12.5))
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((12.5, 0), 2, 90, 180)
                Line((12.5, -2), (12.5, 2))
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((0, 12.5), 2, 180, 180)
                Line((2, 12.5), (-2, 12.5))
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((-12.5, 2), (-12.5, -2))
                CenterArc((-12.5, 0), 2, -90, 180)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: A flat, elongated parallelogram-shaped plate or blade with a tapered profile and beveled edges, featuring a thin, wedge-like geometry.
def model_31245_b2c86b4e_0007():
    """Model: wing"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.855, perimeter: 28.5
            with BuildLine():
                Line((23.5, -14.95), (23.9, -14.95))
                Line((23.9, -14.95), (23.9, -15))
                Line((25.25, -15), (23.9, -15))
                Line((25.25, -2.5), (25.25, -15))
                Line((23.5, -2.5), (25.25, -2.5))
                Line((23.5, -14.95), (23.5, -2.5))
            make_face()
            # Profile area: 10.9375, perimeter: 26.8719055614
            with BuildLine():
                Line((21.75, -15), (21.75, -2.5))
                Line((20, -2.5), (21.75, -2.5))
                Line((21.75, -15), (20, -2.5))
            make_face()
            # Profile area: 21.855, perimeter: 28.5
            with BuildLine():
                Line((23.1, -15), (23.1, -14.95))
                Line((23.1, -14.95), (23.5, -14.95))
                Line((23.5, -14.95), (23.5, -2.5))
                Line((21.75, -2.5), (23.5, -2.5))
                Line((21.75, -15), (21.75, -2.5))
                Line((23.1, -15), (21.75, -15))
            make_face()
            # Profile area: 10.9375, perimeter: 26.8719055614
            with BuildLine():
                Line((25.25, -2.5), (25.25, -15))
                Line((25.25, -15), (27, -2.5))
                Line((27, -2.5), (25.25, -2.5))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a boat hull or marine vessel component with an elongated, tapered rectangular shape featuring a central keel or fin structure running lengthwise, designed to provide hydrodynamic stability and directional control.
def model_31277_b1263495_0005():
    """Model: KEEPER PLATE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.696484276, perimeter: 10.6375423295
            with BuildLine():
                Line((0, 0), (-2.2225, 0))
                Line((-2.2225, 0), (-2.2225, -2.2225))
                Line((-2.2225, -2.2225), (0, -2.2225))
                Line((0, -2.2225), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-1.5875, -1.43002), 0.27813, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a curved serpentine or C-shaped structural component with a hollow center, featuring a textured mesh or latticed surface on its outer edges and a solid dark core, designed to bend around obstacles or provide flexible support in an assembly.
def model_31277_b1263495_0007():
    """Model: WHEEL SNAP RING"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.7191786602, perimeter: 27.5975842783
            with BuildLine():
                CenterArc((0, 0), 1.79578, 15.0089136767, 344.9910863233)
                Line((1.7345179518, 0.4650519146), (2.45364, 0.65786))
                CenterArc((0, 0), 2.5403009722, 15.0089136767, 344.9910863233)
                Line((1.79578, 0), (2.5403009722, 0))
            make_face()
        # OneSide extrude, distance=0.39624
        extrude(amount=0.39624)
    return part.part


# Description: This is a stamped or molded metal bracket or strap with an elongated rectangular body, featuring a central slot or groove running lengthwise and black reinforced end caps or flanges on both terminals.
def model_31277_b1263495_0009():
    """Model: 5-32 x 1 1-2  COTTER PIN"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9791540673, perimeter: 13.7535917504
            with BuildLine():
                Line((-0.9398, -0.36068), (0, 0))
                Line((0, 0), (3.048, 0))
                Line((3.048, 0), (3.3361069539, -0.1503166716))
                Line((3.3361069539, -0.1503166716), (3.3401, -0.1524))
                CenterArc((3.52044, 0.19812), 0.3941913063, -117.2254920057, 234.4509840115)
                Line((3.3361069539, 0.5465566716), (3.3401, 0.54864))
                Line((3.048, 0.39624), (3.3361069539, 0.5465566716))
                Line((0, 0.39624), (3.048, 0.39624))
                Line((-0.7615450453, 0.688508639), (0, 0.39624))
                Line((-0.8278969014, 0.51562), (-0.7615450453, 0.688508639))
                Line((0.0001430986, 0.19812), (-0.8278969014, 0.51562))
                Line((-1.00584, -0.18796), (0.0001430986, 0.19812))
                Line((-0.9398, -0.36068), (-1.00584, -0.18796))
            make_face()
            with BuildLine():
                CenterArc((3.52044, 0.19812), 0.19558, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.39624
        extrude(amount=0.39624)
    return part.part


# Description: This is a curved headband or head-worn device featuring a padded dark gray inner band with a blue mesh or textured outer covering, designed to distribute pressure and provide comfort around the head.
def model_31277_b1263495_0010():
    """Model: AXLE SNAP RING"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1763998668, perimeter: 13.7736546584
            with BuildLine():
                Line((1.26492, 0.34036), (0.7848829148, 0.2111933948))
                CenterArc((0, 0), 1.3099112703, 15.0602358508, 344.9397641492)
                Line((0.8128, 0), (1.3099112703, 0))
                CenterArc((0, 0), 0.8128, 15.0602358508, 344.9397641492)
            make_face()
        # OneSide extrude, distance=0.23876
        extrude(amount=0.23876)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered design, featuring rounded ends and a uniform diameter along its length.
def model_31280_c8bd4b11_0002():
    """Model: Main Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


# Description: This is a flat trapezoidal or wedge-shaped plate with a tapered profile, featuring a sloped top surface and a thicker base, commonly used as a shim, spacer, or angled mounting bracket.
def model_31280_c8bd4b11_0003():
    """Model: Sponge"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.7217215589, perimeter: 17.7636579832
            with BuildLine():
                Line((-2.2204572479, -1.9704572479), (2.2204572479, -1.9704572479))
                Line((2.2204572479, -1.9704572479), (2.2204572479, 2.4704572479))
                Line((2.2204572479, 2.4704572479), (-2.2204572479, 2.4704572479))
                Line((-2.2204572479, 2.4704572479), (-2.2204572479, -1.9704572479))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: A long, slender cylindrical rod or shaft with a uniform diameter and slight taper at one end, featuring a smooth surface finish suitable for mechanical assembly or structural support applications.
def model_31280_c8bd4b11_0007():
    """Model: Left Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a cylindrical ring or sleeve with a hollow central bore, featuring a curved, dome-like top surface and a mesh or perforated pattern across its outer surfaces, suggesting it may be a filter, strainer, or ventilation component.
def model_31360_a1accb4b_0001():
    """Model: 21-Low Friction Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring a straight, tapered or slightly angled linear form with smooth surfaces and no holes or protrusions.
def model_31360_a1accb4b_0003():
    """Model: Threaded Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=13.76
        extrude(amount=13.76)
    return part.part


# Description: This is a long, slender cylindrical stylus or pen with a tapered pointed tip at one end and a small circular loop or hole at the opposite end for attachment or grip purposes.
def model_31360_a1accb4b_0004():
    """Model: 5-Connecting Rod"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 22 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8061665882, perimeter: 25.7773141887
            with BuildLine():
                CenterArc((-60.1811845596, 4.505), 60, 1.4135144654, 0.0190292721)
                CenterArc((-60.1811845596, 4.505), 60, -4.2644126545, 5.6779271199)
                CenterArc((-60.1811845596, 4.505), 60, -4.2976312127, 0.0332185582)
                CenterArc((0, 0), 0.35, 178.5674562624, 182.8650874751)
                CenterArc((60.1811845596, 4.505), 60, -175.7355873455, 0.0332185582)
                CenterArc((60.1811845596, 4.505), 60, 178.5864855346, 5.6779271199)
                CenterArc((60.1811845596, 4.505), 60, 178.5674562624, 0.0190292721)
                CenterArc((0, 6), 0.2, 1.4325437376, 177.1349125249)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 6), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-60.0794584432, 3.9402087887), 60, -3.233819742, 4.7331284841)
                CenterArc((0, 6), 0.5, -101.5369590328, 23.0739180656)
                CenterArc((60.0794584432, 3.9402087887), 60, 178.5006912579, 4.7331284841)
                CenterArc((0, 0), 0.5824689478, 72.5156551281, 34.9686897438)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a washer or ring-shaped spacer with a flat, disc-like form featuring a large central hole and a uniformly thick annular (donut-shaped) body.
def model_31360_a1accb4b_0005():
    """Model: Thrust Roller Bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1837831702, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.29, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.02
        extrude(amount=0.02, both=True)
    return part.part


# Description: This is a curved bracket or support clamp with an elongated, tapered body featuring a central oval slot and flared ends for mounting or attachment points.
def model_31360_a1accb4b_0007():
    """Model: 6-Rocker"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 54 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2868616396, perimeter: 13.7417084496
            with BuildLine():
                CenterArc((3.0882035641, 0.2701828025), 0.25, -78.5172989489, 167.0345978977)
                CenterArc((1.7108798362, 6.8785308514), 6.507267942, -78.731600051, 1.0094925123)
                CenterArc((1.7108798362, 6.8785308514), 6.507267942, -105.2365479704, 26.5049479194)
                CenterArc((0, 0), 0.6, 89.9294032868, 0.0705967132)
                Line((0, 0.6), (0, 0.45))
                CenterArc((0, 0), 0.45, -90, 180)
                Line((0, -0.45), (0, -0.6))
                CenterArc((0, 0), 0.6, -90, 11.4827010511)
                CenterArc((3.4660346938, -9.3261314142), 9.3570707919, 92.5002023181, 18.4559721839)
                CenterArc((3.4660346938, -9.3261314142), 9.3570707919, 92.0092276003, 0.4909747178)
            make_face()
            with BuildLine():
                CenterArc((3.0882035641, 0.2701828025), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0012080614, -7.6055399899), 7.7474049738, 92.145055149, 14.5264464938)
                CenterArc((0, 0), 0.8, -13.2819716132, 36.5639432265)
                CenterArc((1.650851695, 6.469020188), 6.2206253164, -98.4676678121, 18.1187788323)
                CenterArc((3.0882035641, 0.2701828025), 0.4, 170.4659710517, 29.0680578965)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.2868616396, perimeter: 13.7417084496
            with BuildLine():
                CenterArc((0, 0), 0.6, 90, 0.0705967132)
                CenterArc((-1.7108798362, 6.8785308514), 6.507267942, -101.268399949, 26.5049479194)
                CenterArc((-1.7108798362, 6.8785308514), 6.507267942, -102.2778924613, 1.0094925123)
                CenterArc((-3.0882035641, 0.2701828025), 0.25, 91.4827010511, 167.0345978977)
                CenterArc((-3.4660346938, -9.3261314142), 9.3570707919, 87.4997976819, 0.4909747178)
                CenterArc((-3.4660346938, -9.3261314142), 9.3570707919, 69.043825498, 18.4559721839)
                CenterArc((0, 0), 0.6, -101.4827010511, 11.4827010511)
                Line((0, -0.45), (0, -0.6))
                CenterArc((0, 0), 0.45, 90, 180)
                Line((0, 0.6), (0, 0.45))
            make_face()
            with BuildLine():
                CenterArc((-3.0882035641, 0.2701828025), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.0012080614, -7.6055399899), 7.7474049738, 73.3284983572, 14.5264464938)
                CenterArc((-3.0882035641, 0.2701828025), 0.4, -19.5340289483, 29.0680578965)
                CenterArc((-1.650851695, 6.469020188), 6.2206253164, -99.6511110202, 18.1187788323)
                CenterArc((0, 0), 0.8, 156.7180283868, 36.5639432265)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a torus or ring-shaped elastomeric seal/gasket featuring a smooth inner and outer diameter with a mesh-textured surface, designed for fluid containment or mechanical sealing applications.
def model_31360_a1accb4b_0009():
    """Model: 31-Low Friction Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0505796417, perimeter: 1.4451326207
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)
    return part.part


# Description: This is a cylindrical mesh filter or strainer component with an elliptical cross-section, featuring a solid outer wall and a perforated or mesh inner surface with a central longitudinal slot or opening along the top.
def model_31360_a1accb4b_0011():
    """Model: Oil conduit gasket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0122522113, perimeter: 0.8168140899
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)
    return part.part


# Description: A straight cylindrical rod or pin with a uniform circular cross-section and slight taper at the ends, displayed at an angle.
def model_31391_df3562f8_0001():
    """Model: Steel Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=17
        extrude(amount=17)
    return part.part


# Description: This is a thin-walled elliptical ring or oval washer with a smooth, curved perimeter and a large central opening.
def model_31391_df3562f8_0002():
    """Model: Circular Spring"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0838494655, perimeter: 43.3539786195
            with BuildLine():
                CenterArc((0, 0), 3.475, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.005
        extrude(amount=0.005, both=True)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a simple rectangular geometry, featuring a uniform thickness and clean edges with no holes, slots, or additional features.
def model_31391_df3562f8_0003():
    """Model: Table"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 400, perimeter: 80
            with BuildLine():
                Line((-10, 10), (10, 10))
                Line((-10, -10), (-10, 10))
                Line((10, -10), (-10, -10))
                Line((10, 10), (10, -10))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)
    return part.part


# Description: This is a parallelogram-shaped flat bar or plate with a simple rectangular profile, featuring a uniform cross-section and slight 3D depth, commonly used as a structural support or connector element.
def model_31391_df3562f8_0005():
    """Model: Steel support bands"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0966785929, perimeter: 2.1335718583
            with BuildLine():
                Line((-0.4776178513, -4.776178513), (-0.4875682232, -4.875682232))
                CenterArc((0, 0), 4.9, -95.7105931375, 11.421186275)
                Line((0.4776178513, -4.776178513), (0.4875682232, -4.875682232))
                CenterArc((0, 0), 4.8, -95.7105931375, 11.421186275)
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a horizontal roof rack cross bar with a streamlined blue/gray tubular body and black end caps, designed to mount transversely across a vehicle's roof for cargo carrying.
def model_31464_b2855e3a_0008():
    """Model: Linkage Arm (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.3477922622, perimeter: 22.9974888613
            with BuildLine():
                Line((0.3549757914, -0.3175), (8.5350242086, -0.3175))
                CenterArc((8.89, 0), 0.47625, -138.1896851042, 276.3793702084)
                Line((8.5350242086, 0.3175), (0.3549757914, 0.3175))
                CenterArc((0, 0), 0.47625, 41.8103148958, 276.3793702084)
            make_face()
            with BuildLine():
                CenterArc((8.89, 0), 0.16256, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.16256, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a cylindrical bushing or sleeve with a hollow bore through its center, featuring a rounded rectangular overall shape with smooth curved surfaces and a recessed or stepped inner diameter.
def model_31464_b2855e3a_0014():
    """Model: Hitch Magnet (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7093904707, perimeter: 5.5857517381
            with BuildLine():
                CenterArc((0, 0), 0.5715, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a cylindrical connector or coupling with two coaxial bores of different diameters, featuring rounded edges and a stepped design for joining or aligning components of varying sizes.
def model_31464_b2855e3a_0018():
    """Model: Brushing  (1) (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0805664892, perimeter: 4.2292120303
            with BuildLine():
                CenterArc((0, 0), 0.3556, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a wedge-shaped or tapered rectangular block with a sloped top surface, featuring a prismatic form that narrows from one end to the other, commonly used as a structural component or support element.
def model_31596_4acd1c1d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30, perimeter: 22
            with BuildLine():
                Line((2.5, -1), (-2.5, -1))
                Line((2.5, 5), (2.5, -1))
                Line((-2.5, 5), (2.5, 5))
                Line((-2.5, -1), (-2.5, 5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a cylindrical bearing or bushing with a hollow central bore, featuring a rounded/domed top surface and a mesh-textured exterior finish.
def model_31616_c013ae1f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 232.4784815426, perimeter: 94.8698149531
            with BuildLine():
                CenterArc((0, 0), 10, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.099, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a flat washer—a simple ring-shaped fastener with a circular outer diameter, a centered hole, and a flat profile, used to distribute load and prevent surface damage under bolt heads or nuts.
def model_31627_6b01242d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4825176332, perimeter: 7.6026542966
            with BuildLine():
                CenterArc((0, 0), 0.8000000119, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.41, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)
    return part.part


# Description: This is a toroidal (donut-shaped) washer or spacer ring featuring a smooth, rounded torus geometry with a central circular hole and uniform thickness throughout.
def model_31627_ec13313b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8290663013, perimeter: 5.7176986295
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)
    return part.part


# Description: This is a flat, parallelogram-shaped plate or bracket with a tapered wedge profile, featuring a thin body with sloped surfaces and dark edges that suggest beveled or chamfered corners.
def model_31652_96a3746c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.6302210426, perimeter: 21.7390271235
            with BuildLine():
                Line((4.0640001297, -3.0480000973), (-2.3227861805, -3.0480000973))
                Line((4.0640001297, 1.4347271543), (4.0640001297, -3.0480000973))
                Line((-2.3227861805, 1.4347271543), (4.0640001297, 1.4347271543))
                Line((-2.3227861805, -3.0480000973), (-2.3227861805, 1.4347271543))
            make_face()
        # OneSide extrude, distance=0.60452
        extrude(amount=0.60452)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a straight, elongated body that gradually decreases in diameter from one end to the other, featuring a simple conical taper along its length.
def model_31655_baca05af_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch10 -> Extrude10 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.3341581703, perimeter: 2.0491840844
            with Locations((-1.4346064664, 12.8493603633)):
                Circle(0.3261377763)
        # TwoSides extrude, along=12, against=-22.5
        extrude(amount=12)
        extrude(sk.sketch, amount=-22.5)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a trapezoidal profile, featuring a thin, wedge-like geometry with sloped edges and a beveled or angled side face.
def model_31740_86dab66b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1350, perimeter: 150
            with BuildLine():
                Line((15, -22.5), (15, 22.5))
                Line((15, 22.5), (-15, 22.5))
                Line((-15, 22.5), (-15, -22.5))
                Line((-15, -22.5), (15, -22.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical rod or tube with a slightly tapered design, featuring rounded ends and a uniform dark gray finish.
def model_31866_a5b1db64_0001():
    """Model: DIFFERENTIAL GEAR WHEEL"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((-1.5, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.275
        extrude(amount=2.275, both=True)
    return part.part


# Description: This is a toroidal or ring-shaped component with a circular cross-section, featuring a hollow center, radial ribbing or fins around its outer and inner surfaces, and a smooth, symmetrical doughnut-like geometry.
def model_31962_e5291336_0003():
    """Model: arandela"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4996673329, perimeter: 5.0205675696
            with BuildLine():
                CenterArc((33, 0), 0.4990481458, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((33, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a hexagonal or octagonal geometric solid with a large central elliptical or oval hole passing through its center, featuring alternating dark and light faceted surfaces that create a symmetrical, faceted appearance.
def model_31962_e5291336_0011():
    """Model: DIN Tuerca"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6761405616, perimeter: 5.0088227229
            with BuildLine():
                Line((14.6414484889, 2.1693360597), (14.3527733543, 1.6693360597))
                Line((14.3527733543, 1.6693360597), (14.6414484889, 1.1693360597))
                Line((14.6414484889, 1.1693360597), (15.2187987581, 1.1693360597))
                Line((15.2187987581, 1.1693360597), (15.5074738927, 1.6693360597))
                Line((15.5074738927, 1.6693360597), (15.2187987581, 2.1693360597))
                Line((15.2187987581, 2.1693360597), (14.6414484889, 2.1693360597))
            make_face()
            with BuildLine():
                CenterArc((14.9301236235, 1.6693360597), 0.24585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.32
        extrude(amount=0.32)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or torus with a smooth, rounded outer profile and a central circular hole, featuring a uniform cross-section throughout its circumference.
def model_31962_e5291336_0016():
    """Model: ten"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((5.0832323559, 0.8504404511), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.0832323559, 0.8504404511), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a simple, elongated tubular shape with hemispherical or rounded caps on both ends.
def model_31962_e5291336_0027():
    """Model: Eje (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.6272838859, 1.9719541822)):
                Circle(0.25)
        # OneSide extrude, distance=7.3
        extrude(amount=7.3)
    return part.part


# Description: This is an oval or elliptical disk with a central axial hole, featuring radial fins or ribs extending outward from the center, creating a cooling or impeller-like component commonly used in thermal management or fluid dynamics applications.
def model_31962_e5291336_0029():
    """Model: Rueda 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.470462439, perimeter: 21.6769893098
            with BuildLine():
                CenterArc((15.5, 1), 2.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((15.5, 1), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a C-shaped retaining ring (snap ring) with a circular overall form, featuring two opposing open ends with small holes for installation tool access and a textured surface for grip.
def model_31962_e5291336_0030():
    """Model: Anilla"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.037497608, perimeter: 12.9379935824
            with BuildLine():
                Line((4.9199446614, 1.6957261269), (4.8682665721, 1.9241091791))
                CenterArc((5.100000076, 0.9000000134), 1.05, 102.7500669732, 325.8316870314)
                Line((5.3979241711, 1.6595006609), (5.4834320022, 1.8774865647))
                CenterArc((5.5841120856, 1.5864660083), 0.2, 158.5817540047, 143.9445472235)
                CenterArc((5.745418097, 1.3335225943), 0.1, 33.888969995, 88.6373312331)
                CenterArc((5.100000076, 0.9000000134), 0.8775, 137.4428509829, 256.4461190122)
                CenterArc((4.5272911576, 1.4258429032), 0.1, 48.8055197498, 88.6373312331)
                CenterArc((4.7248762489, 1.6515864119), 0.2, -131.1944802502, 143.9445472235)
            make_face()
            with BuildLine():
                CenterArc((5.5841120856, 1.5864660083), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7248762489, 1.6515864119), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is an oval or elliptical dome/shell with a smooth curved surface featuring multiple vertical ribs or reinforcement lines running from top to bottom for structural support.
def model_31962_e5291336_0031():
    """Model: Tents"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with Locations((22.5, 0)):
                Circle(3.5)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a dark gray elongated rectangular bar with rounded ends and two symmetrical recessed slots or vents on opposite sides, featuring a smooth cylindrical profile suitable for structural or mechanical applications.
def model_31962_e5291336_0033():
    """Model: Eje"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((16.500214738, 0.357803289)):
                Circle(0.5)
        # OneSide extrude, distance=7.6
        extrude(amount=7.6)
    return part.part


# Description: This is a toroidal ring or washer with a smooth, rounded doughnut shape featuring a large central hole and textured radial surface patterns.
def model_31962_e5291336_0036():
    """Model: Arandela (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.547815219, perimeter: 4.8694686131
            with BuildLine():
                CenterArc((15.367506031, 1.4300991417), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((15.367506031, 1.4300991417), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a toroidal (donut-shaped) housing or connector component featuring a smooth, rounded outer surface with a central rectangular slot or opening and symmetrical curved geometry designed for fluid flow, cable routing, or assembly purposes.
def model_31962_e5291336_0037():
    """Model: Component43"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.565928646, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((14.8966128317, 1.6993207205), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((14.8966128317, 1.6993207205), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a simple, uniform circular cross-section and smooth, elongated geometry with no visible holes, slots, or flanges.
def model_31962_e5291336_0038():
    """Model: eje"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((21.3159243057, -1.3050565901)):
                Circle(0.325)
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


# Description: This is a C-shaped internal retaining ring (snap ring) with a circular band featuring two opposing hook ends with retention holes, designed to hold components in grooves or bores.
def model_31962_e5291336_0051():
    """Model: DIN"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2870102184, perimeter: 13.8548879666
            with BuildLine():
                CenterArc((9.3341796566, 0.8682353661), 0.2, 88.48685565, 155.1594213126)
                CenterArc((8.4000001252, 1.1000000164), 0.94, 56.307222833, 277.766681188)
                CenterArc((9.088683527, 1.7723997651), 0.2, 146.7348498915, 155.1594213126)
                Line((9.1943542163, 1.6025948611), (9.1968770277, 1.6041910661))
                Line((9.1968770277, 1.6041910661), (9.3718163005, 1.7148766881))
                CenterArc((8.4000001252, 1.1000000164), 1.15, 32.3218982626, 325.7373303288)
                Line((9.3424445726, 1.0680645211), (9.5493404505, 1.0610536863))
                Line((9.3394609128, 1.0681656248), (9.3424445726, 1.0680645211))
            make_face()
            with BuildLine():
                CenterArc((9.3341796566, 0.8682353661), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.088683527, 1.7723997651), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


MODELS = {
    "model_25399_5e678d71_0000": {"func": model_25399_5e678d71_0000, "volume": 218.4082001479, "area": 271.8631399217},
    "model_25416_93d169f7_0000": {"func": model_25416_93d169f7_0000, "volume": 3.6191147369, "area": 39.2070763168},
    "model_25432_1e61aab2_0000": {"func": model_25432_1e61aab2_0000, "volume": 9.999285156, "area": 73.4376498901},
    "model_25436_61a7f978_0000": {"func": model_25436_61a7f978_0000, "volume": 0.0149225651, "area": 1.1977321992},
    "model_25436_61a7f978_0002": {"func": model_25436_61a7f978_0002, "volume": 0.037296, "area": 2.1071931944},
    "model_25474_5422a377_0009": {"func": model_25474_5422a377_0009, "volume": 0.504, "area": 4.08},
    "model_25474_5422a377_0018": {"func": model_25474_5422a377_0018, "volume": 1.008, "area": 6.52},
    "model_25484_9b17990a_0000": {"func": model_25484_9b17990a_0000, "volume": 301386.751156214, "area": 26121.834796006},
    "model_26245_4aac38e1_0000": {"func": model_26245_4aac38e1_0000, "volume": 31.5541566127, "area": 55.4176944093},
    "model_26245_4aac38e1_0001": {"func": model_26245_4aac38e1_0001, "volume": 21.0683057331, "area": 45.9143766322},
    "model_26245_4aac38e1_0003": {"func": model_26245_4aac38e1_0003, "volume": 0.5607742887, "area": 22.5409272895},
    "model_26261_5deaf75a_0001": {"func": model_26261_5deaf75a_0001, "volume": 330.3191394045, "area": 501.4400623303},
    "model_26384_83eddf22_0009": {"func": model_26384_83eddf22_0009, "volume": 0.1284174627, "area": 1.5429850787},
    "model_26384_83eddf22_0011": {"func": model_26384_83eddf22_0011, "volume": 0.1459312047, "area": 1.7135732187},
    "model_26384_83eddf22_0015": {"func": model_26384_83eddf22_0015, "volume": 0.2262369721, "area": 3.0085756571},
    "model_26384_83eddf22_0020": {"func": model_26384_83eddf22_0020, "volume": 0.6388529893, "area": 5.6609359565},
    "model_26384_83eddf22_0024": {"func": model_26384_83eddf22_0024, "volume": 0.0492451573, "area": 1.2138342261},
    "model_26384_83eddf22_0028": {"func": model_26384_83eddf22_0028, "volume": 0.1025661853, "area": 1.9076814649},
    "model_26388_a3367cba_0001": {"func": model_26388_a3367cba_0001, "volume": 0.1584000002, "area": 16.1720000215},
    "model_26388_a3367cba_0007": {"func": model_26388_a3367cba_0007, "volume": 0.18369, "area": 18.8970000002},
    "model_26403_1f4a2618_0000": {"func": model_26403_1f4a2618_0000, "volume": 10.021947012, "area": 54.1860177631},
    "model_26403_1f4a2618_0008": {"func": model_26403_1f4a2618_0008, "volume": 4.9372566612, "area": 29.2339822369},
    "model_26403_1f4a2618_0009": {"func": model_26403_1f4a2618_0009, "volume": 4.6472566612, "area": 27.9739822369},
    "model_26404_7be5b2e3_0003": {"func": model_26404_7be5b2e3_0003, "volume": 13.1255846059, "area": 116.8351181098},
    "model_26404_7be5b2e3_0007": {"func": model_26404_7be5b2e3_0007, "volume": 14.2861585435, "area": 82.0299686983},
    "model_26764_ab35159a_0000": {"func": model_26764_ab35159a_0000, "volume": 1.2340589995, "area": 28.4741592654},
    "model_26764_ab35159a_0002": {"func": model_26764_ab35159a_0002, "volume": 0.6695022129, "area": 16.2712546675},
    "model_26764_ab35159a_0004": {"func": model_26764_ab35159a_0004, "volume": 1.6407344938, "area": 11.0925469374},
    "model_26768_c4df841f_0010": {"func": model_26768_c4df841f_0010, "volume": 22.525529248, "area": 58.0066731662},
    "model_26768_c4df841f_0014": {"func": model_26768_c4df841f_0014, "volume": 0.1289576991, "area": 3.7836327291},
    "model_26773_35d26b3c_0002": {"func": model_26773_35d26b3c_0002, "volume": 0.0532990532, "area": 1.6047078317},
    "model_26773_35d26b3c_0010": {"func": model_26773_35d26b3c_0010, "volume": 0.0673843949, "area": 2.5029921771},
    "model_26861_21e598d0_0000": {"func": model_26861_21e598d0_0000, "volume": 33.9292006588, "area": 79.1681348705},
    "model_27054_342fcf5c_0003": {"func": model_27054_342fcf5c_0003, "volume": 1.5173892517, "area": 14.4513262065},
    "model_27054_342fcf5c_0005": {"func": model_27054_342fcf5c_0005, "volume": 3.1447342462, "area": 25.3997766043},
    "model_27054_342fcf5c_0006": {"func": model_27054_342fcf5c_0006, "volume": 0.6785840132, "area": 5.0893800988},
    "model_27054_342fcf5c_0016": {"func": model_27054_342fcf5c_0016, "volume": 5.0029863008, "area": 107.5367165324},
    "model_27054_342fcf5c_0024": {"func": model_27054_342fcf5c_0024, "volume": 2.0451768175, "area": 42.851323795},
    "model_27054_342fcf5c_0038": {"func": model_27054_342fcf5c_0038, "volume": 3.6348227002, "area": 29.3581833478},
    "model_27054_342fcf5c_0042": {"func": model_27054_342fcf5c_0042, "volume": 9.2441363832, "area": 193.6791870938},
    "model_27054_342fcf5c_0047": {"func": model_27054_342fcf5c_0047, "volume": 0.1068141502, "area": 2.1896900796},
    "model_27070_53448c4a_0008": {"func": model_27070_53448c4a_0008, "volume": 18.8986433068, "area": 153.1526418625},
    "model_27070_53448c4a_0017": {"func": model_27070_53448c4a_0017, "volume": 4.8, "area": 23.2},
    "model_27449_088a5bd0_0001": {"func": model_27449_088a5bd0_0001, "volume": 603820.5864012471, "area": 248984.9562337168},
    "model_27452_f37cb86c_0003": {"func": model_27452_f37cb86c_0003, "volume": 0.9047786842, "area": 9.2991142546},
    "model_27577_8520e14a_0000": {"func": model_27577_8520e14a_0000, "volume": 9979.721976, "area": 7551.5978},
    "model_27577_8520e14a_0001": {"func": model_27577_8520e14a_0001, "volume": 26743.688448, "area": 10735.4624},
    "model_27577_8520e14a_0002": {"func": model_27577_8520e14a_0002, "volume": 4916.1192, "area": 2645.156},
    "model_27577_8520e14a_0003": {"func": model_27577_8520e14a_0003, "volume": 1608.7962461346, "area": 1076.7533930822},
    "model_27577_8520e14a_0005": {"func": model_27577_8520e14a_0005, "volume": 4719.474432, "area": 3096.768},
    "model_27577_8520e14a_0006": {"func": model_27577_8520e14a_0006, "volume": 7064.4815058557, "area": 5694.4649604893},
    "model_27577_8520e14a_0007": {"func": model_27577_8520e14a_0007, "volume": 3056.7128676557, "area": 1988.8268554577},
    "model_27577_8520e14a_0008": {"func": model_27577_8520e14a_0008, "volume": 1100.416632356, "area": 1178.0948889017},
    "model_27577_8520e14a_0009": {"func": model_27577_8520e14a_0009, "volume": 16780.353536, "area": 6812.8896},
    "model_27577_8520e14a_0011": {"func": model_27577_8520e14a_0011, "volume": 1447.9166215211, "area": 975.4118972627},
    "model_27679_501db761_0002": {"func": model_27679_501db761_0002, "volume": 12.8553971385, "area": 44.7991112402},
    "model_27679_501db761_0003": {"func": model_27679_501db761_0003, "volume": 4.2223005264, "area": 31.1645991236},
    "model_27679_501db761_0012": {"func": model_27679_501db761_0012, "volume": 0.9071348787, "area": 11.8791472214},
    "model_27679_501db761_0018": {"func": model_27679_501db761_0018, "volume": 99.1922780213, "area": 129.9340097164},
    "model_27679_501db761_0022": {"func": model_27679_501db761_0022, "volume": 0.7181484457, "area": 9.719302272},
    "model_27682_04277f62_0009": {"func": model_27682_04277f62_0009, "volume": 17.3233304029, "area": 46.1253284516},
    "model_27682_04277f62_0010": {"func": model_27682_04277f62_0010, "volume": 20.4517681749, "area": 56.4858359115},
    "model_27688_65b3c0dc_0002": {"func": model_27688_65b3c0dc_0002, "volume": 1.5315264186, "area": 19.3993346359},
    "model_27688_65b3c0dc_0004": {"func": model_27688_65b3c0dc_0004, "volume": 109.9087385212, "area": 301.0873852123},
    "model_27688_65b3c0dc_0006": {"func": model_27688_65b3c0dc_0006, "volume": 150, "area": 407.1238898038},
    "model_27694_7801dc67_0002": {"func": model_27694_7801dc67_0002, "volume": 0.3769911184, "area": 7.916813487},
    "model_27694_7801dc67_0006": {"func": model_27694_7801dc67_0006, "volume": 1.1963495408, "area": 9.926990817},
    "model_27694_7801dc67_0007": {"func": model_27694_7801dc67_0007, "volume": 0.6963216544, "area": 6.9268796692},
    "model_27694_7801dc67_0008": {"func": model_27694_7801dc67_0008, "volume": 0.0245436926, "area": 0.4908738521},
    "model_27694_7801dc67_0013": {"func": model_27694_7801dc67_0013, "volume": 8.1053090463, "area": 86.4566298268},
    "model_27694_7801dc67_0016": {"func": model_27694_7801dc67_0016, "volume": 86.7079572391, "area": 884.4211638386},
    "model_27694_7801dc67_0020": {"func": model_27694_7801dc67_0020, "volume": 0.5301437603, "area": 4.633849164},
    "model_27694_7801dc67_0024": {"func": model_27694_7801dc67_0024, "volume": 0.3534291735, "area": 3.2201324699},
    "model_27725_5cceaeb7_0009": {"func": model_27725_5cceaeb7_0009, "volume": 9.0190140874, "area": 44.0765556702},
    "model_27725_5cceaeb7_0011": {"func": model_27725_5cceaeb7_0011, "volume": 63.0447028954, "area": 797.2725491425},
    "model_27733_626709f1_0000": {"func": model_27733_626709f1_0000, "volume": 0.0589048623, "area": 1.6493361431},
    "model_27839_4a077326_0004": {"func": model_27839_4a077326_0004, "volume": 450.0213666543, "area": 573.1364557577},
    "model_27839_4a077326_0009": {"func": model_27839_4a077326_0009, "volume": 0.1507964474, "area": 3.7699111843},
    "model_27839_4a077326_0010": {"func": model_27839_4a077326_0010, "volume": 634.476052319, "area": 717.4140983738},
    "model_27839_4a077326_0013": {"func": model_27839_4a077326_0013, "volume": 0.3518583772, "area": 5.277875658},
    "model_27839_4a077326_0022": {"func": model_27839_4a077326_0022, "volume": 6.2674773439, "area": 84.4617184918},
    "model_27872_07f8a3a0_0000": {"func": model_27872_07f8a3a0_0000, "volume": 3.7699111843, "area": 38.4530940799},
    "model_27872_07f8a3a0_0002": {"func": model_27872_07f8a3a0_0002, "volume": 8.8357293382, "area": 71.8639319509},
    "model_28282_97002185_0000": {"func": model_28282_97002185_0000, "volume": 336.6422056528, "area": 772.0167688723},
    "model_28283_1a9ffb0b_0000": {"func": model_28283_1a9ffb0b_0000, "volume": 78.2035761867, "area": 138.6877153004},
    "model_28456_69d04209_0000": {"func": model_28456_69d04209_0000, "volume": 572.5552611167, "area": 381.7035074112},
    "model_28888_da6e6e94_0000": {"func": model_28888_da6e6e94_0000, "volume": 76.8, "area": 166.4},
    "model_29114_80c15ce0_0004": {"func": model_29114_80c15ce0_0004, "volume": 304.323, "area": 445.55},
    "model_29115_cade8ac7_0000": {"func": model_29115_cade8ac7_0000, "volume": 5000, "area": 10300},
    "model_29442_365e23df_0008": {"func": model_29442_365e23df_0008, "volume": 88.998124807, "area": 908.5065406315},
    "model_30030_d4b0c535_0000": {"func": model_30030_d4b0c535_0000, "volume": 20, "area": 61},
    "model_30274_ca0d10b2_0004": {"func": model_30274_ca0d10b2_0004, "volume": 0.0869411202, "area": 2.167566108},
    "model_30292_0b5e0265_0003": {"func": model_30292_0b5e0265_0003, "volume": 40.2338474115, "area": 161.62677454},
    "model_30297_fd93a92a_0000": {"func": model_30297_fd93a92a_0000, "volume": 0.0459735246, "area": 1.8664189962},
    "model_30297_fd93a92a_0003": {"func": model_30297_fd93a92a_0003, "volume": 0.2090791601, "area": 2.0987823784},
    "model_30297_fd93a92a_0004": {"func": model_30297_fd93a92a_0004, "volume": 0.6882430341, "area": 5.6639762014},
    "model_30297_fd93a92a_0007": {"func": model_30297_fd93a92a_0007, "volume": 0.2390864104, "area": 3.1092900578},
    "model_30375_4ff65965_0008": {"func": model_30375_4ff65965_0008, "volume": 2.9275903259, "area": 18.5203609711},
    "model_30376_e4495332_0000": {"func": model_30376_e4495332_0000, "volume": 2.8770640092, "area": 22.6592371738},
    "model_30376_e4495332_0001": {"func": model_30376_e4495332_0001, "volume": 389.5637722304, "area": 526.7194243009},
    "model_30379_f1d5e193_0004": {"func": model_30379_f1d5e193_0004, "volume": 0.216, "area": 4.92},
    "model_30379_f1d5e193_0009": {"func": model_30379_f1d5e193_0009, "volume": 0.0589048623, "area": 2.5918139392},
    "model_30379_f1d5e193_0015": {"func": model_30379_f1d5e193_0015, "volume": 0.4003401852, "area": 3.7526785693},
    "model_30380_4d422f95_0004": {"func": model_30380_4d422f95_0004, "volume": 75.0447945126, "area": 172.9603835434},
    "model_30380_4d422f95_0005": {"func": model_30380_4d422f95_0005, "volume": 26.8606171882, "area": 89.5353906273},
    "model_30380_4d422f95_0011": {"func": model_30380_4d422f95_0011, "volume": 132.6341148437, "area": 1076.2311033035},
    "model_30389_3f514b04_0000": {"func": model_30389_3f514b04_0000, "volume": 676.5614650995, "area": 1083.2677346987},
    "model_30400_8824ce97_0015": {"func": model_30400_8824ce97_0015, "volume": 180.6588505205, "area": 487.1938052084},
    "model_30400_8824ce97_0032": {"func": model_30400_8824ce97_0032, "volume": 203.2734535629, "area": 524.5026560303},
    "model_30400_8824ce97_0033": {"func": model_30400_8824ce97_0033, "volume": 60.4152220392, "area": 220.9187595947},
    "model_30400_8824ce97_0036": {"func": model_30400_8824ce97_0036, "volume": 64.434892883, "area": 140.1056674024},
    "model_30417_0010bc7c_0009": {"func": model_30417_0010bc7c_0009, "volume": 0.0533812221, "area": 1.1215461},
    "model_30417_0010bc7c_0010": {"func": model_30417_0010bc7c_0010, "volume": 0.3404701038, "area": 5.3407075111},
    "model_30417_0010bc7c_0011": {"func": model_30417_0010bc7c_0011, "volume": 0.007890125, "area": 0.4155002251},
    "model_30417_0010bc7c_0012": {"func": model_30417_0010bc7c_0012, "volume": 0.006307023, "area": 0.272975127},
    "model_30417_0010bc7c_0015": {"func": model_30417_0010bc7c_0015, "volume": 0.1841930348, "area": 2.0679999479},
    "model_30417_0010bc7c_0017": {"func": model_30417_0010bc7c_0017, "volume": 1.180310189, "area": 14.2361437166},
    "model_30417_0010bc7c_0018": {"func": model_30417_0010bc7c_0018, "volume": 2.7712812921, "area": 12.4707658145},
    "model_30417_0010bc7c_0019": {"func": model_30417_0010bc7c_0019, "volume": 37.514, "area": 205.3799111843},
    "model_30417_0010bc7c_0021": {"func": model_30417_0010bc7c_0021, "volume": 2.230530784, "area": 26.7663694086},
    "model_30418_de83ae84_0003": {"func": model_30418_de83ae84_0003, "volume": 0.0004395508, "area": 0.0894098471},
    "model_30418_de83ae84_0004": {"func": model_30418_de83ae84_0004, "volume": 0.0001227185, "area": 0.0206167018},
    "model_30419_d55a0a22_0000": {"func": model_30419_d55a0a22_0000, "volume": 132.2286923118, "area": 308.9845755297},
    "model_30419_d55a0a22_0002": {"func": model_30419_d55a0a22_0002, "volume": 25.6066504805, "area": 101.5931608871},
    "model_30421_211edb5e_0004": {"func": model_30421_211edb5e_0004, "volume": 6.2831853072, "area": 26.7035375555},
    "model_30426_2cde26de_0002": {"func": model_30426_2cde26de_0002, "volume": 7089, "area": 5366.0264068712},
    "model_30435_c97330d2_0012": {"func": model_30435_c97330d2_0012, "volume": 315.450982, "area": 1995.96375},
    "model_30435_c97330d2_0016": {"func": model_30435_c97330d2_0016, "volume": 304.1848755, "area": 1924.99615},
    "model_30445_791b6800_0000": {"func": model_30445_791b6800_0000, "volume": 0.8835729338, "area": 7.4612825523},
    "model_30445_791b6800_0006": {"func": model_30445_791b6800_0006, "volume": 2.2619467106, "area": 15.6451314149},
    "model_30445_791b6800_0007": {"func": model_30445_791b6800_0007, "volume": 0.3581415625, "area": 7.3513268094},
    "model_30445_791b6800_0010": {"func": model_30445_791b6800_0010, "volume": 8.88454647, "area": 67.1497787144},
    "model_30445_791b6800_0013": {"func": model_30445_791b6800_0013, "volume": 14.80757745, "area": 72.4294246574},
    "model_30445_791b6800_0014": {"func": model_30445_791b6800_0014, "volume": 10.2574421965, "area": 58.9002188646},
    "model_30447_4ed3b778_0001": {"func": model_30447_4ed3b778_0001, "volume": 0.1055721707, "area": 2.8888075191},
    "model_30447_4ed3b778_0003": {"func": model_30447_4ed3b778_0003, "volume": 0.1188424618, "area": 2.5646194145},
    "model_30447_4ed3b778_0006": {"func": model_30447_4ed3b778_0006, "volume": 57.5144657993, "area": 123.50994803},
    "model_30447_4ed3b778_0016": {"func": model_30447_4ed3b778_0016, "volume": 0.520891802, "area": 7.86208105},
    "model_30637_f6324fc6_0009": {"func": model_30637_f6324fc6_0009, "volume": 83.4890872221, "area": 232.9146764217},
    "model_30690_3df2c9e2_0003": {"func": model_30690_3df2c9e2_0003, "volume": 0.4036770911, "area": 8.8820860871},
    "model_30690_3df2c9e2_0005": {"func": model_30690_3df2c9e2_0005, "volume": 0.118372806, "area": 3.5861388044},
    "model_30690_3df2c9e2_0007": {"func": model_30690_3df2c9e2_0007, "volume": 8.7868870127, "area": 43.4581810242},
    "model_30690_3df2c9e2_0015": {"func": model_30690_3df2c9e2_0015, "volume": 0.0387371506, "area": 1.2891551982},
    "model_30690_3df2c9e2_0018": {"func": model_30690_3df2c9e2_0018, "volume": 20.8586044235, "area": 62.6747734391},
    "model_30690_3df2c9e2_0019": {"func": model_30690_3df2c9e2_0019, "volume": 0.2793792755, "area": 6.2780748538},
    "model_30708_4282508b_0000": {"func": model_30708_4282508b_0000, "volume": 58.1402965951, "area": 162.4471417039},
    "model_30713_06b3d0ec_0002": {"func": model_30713_06b3d0ec_0002, "volume": 791.6813487046, "area": 1734.1591447816},
    "model_30713_06b3d0ec_0014": {"func": model_30713_06b3d0ec_0014, "volume": 1.8158405538, "area": 20.2946885422},
    "model_30713_06b3d0ec_0016": {"func": model_30713_06b3d0ec_0016, "volume": 184.655597125, "area": 300.5273366512},
    "model_30729_b4d83b07_0002": {"func": model_30729_b4d83b07_0002, "volume": 40.4322974517, "area": 275.7690031321},
    "model_30729_b4d83b07_0005": {"func": model_30729_b4d83b07_0005, "volume": 268.6061718819, "area": 372.2787294504},
    "model_30729_b4d83b07_0007": {"func": model_30729_b4d83b07_0007, "volume": 43.9822971503, "area": 94.2477796077},
    "model_30729_b4d83b07_0012": {"func": model_30729_b4d83b07_0012, "volume": 127.1912642435, "area": 334.4465187282},
    "model_30729_b4d83b07_0017": {"func": model_30729_b4d83b07_0017, "volume": 289.8119222937, "area": 667.2114477694},
    "model_30729_b4d83b07_0018": {"func": model_30729_b4d83b07_0018, "volume": 1281.7035074112, "area": 8561.7794295065},
    "model_30904_54099e05_0008": {"func": model_30904_54099e05_0008, "volume": 436.0530784049, "area": 1162.2477494633},
    "model_30904_54099e05_0009": {"func": model_30904_54099e05_0009, "volume": 589.5928947446, "area": 1569.3273821428},
    "model_30904_54099e05_0016": {"func": model_30904_54099e05_0016, "volume": 1641.0619298297, "area": 8238.1308877453},
    "model_31096_cf2a94f6_0000": {"func": model_31096_cf2a94f6_0000, "volume": 94.2477796077, "area": 219.9114857513},
    "model_31106_7fcb831a_0000": {"func": model_31106_7fcb831a_0000, "volume": 110000, "area": 17833.2183894378},
    "model_31116_0b0aa2be_0000": {"func": model_31116_0b0aa2be_0000, "volume": 761.742428125, "area": 579.83755},
    "model_31245_b2c86b4e_0000": {"func": model_31245_b2c86b4e_0000, "volume": 271.0323208825, "area": 575.8334008389},
    "model_31245_b2c86b4e_0007": {"func": model_31245_b2c86b4e_0007, "volume": 10.4936, "area": 136.9050097796},
    "model_31277_b1263495_0005": {"func": model_31277_b1263495_0005, "volume": 1.4911337576, "area": 12.7703882415},
    "model_31277_b1263495_0007": {"func": model_31277_b1263495_0007, "volume": 3.8511273523, "area": 30.3736241148},
    "model_31277_b1263495_0009": {"func": model_31277_b1263495_0009, "volume": 0.7842200076, "area": 9.4080313298},
    "model_31277_b1263495_0010": {"func": model_31277_b1263495_0010, "volume": 0.7583972322, "area": 9.6413975198},
    "model_31280_c8bd4b11_0002": {"func": model_31280_c8bd4b11_0002, "volume": 6.0318578949, "area": 31.1645991236},
    "model_31280_c8bd4b11_0003": {"func": model_31280_c8bd4b11_0003, "volume": 9.8608607795, "area": 48.3252721094},
    "model_31280_c8bd4b11_0007": {"func": model_31280_c8bd4b11_0007, "volume": 0.7068583471, "area": 9.5661496302},
    "model_31360_a1accb4b_0001": {"func": model_31360_a1accb4b_0001, "volume": 0.0471238898, "area": 1.2566370614},
    "model_31360_a1accb4b_0003": {"func": model_31360_a1accb4b_0003, "volume": 0.9726370856, "area": 13.1098661434},
    "model_31360_a1accb4b_0004": {"func": model_31360_a1accb4b_0004, "volume": 0.1806166588, "area": 6.1900645953},
    "model_31360_a1accb4b_0005": {"func": model_31360_a1accb4b_0005, "volume": 0.0073513268, "area": 0.480663676},
    "model_31360_a1accb4b_0007": {"func": model_31360_a1accb4b_0007, "volume": 0.2573723279, "area": 7.8357882484},
    "model_31360_a1accb4b_0009": {"func": model_31360_a1accb4b_0009, "volume": 0.0020231857, "area": 0.1589645883},
    "model_31360_a1accb4b_0011": {"func": model_31360_a1accb4b_0011, "volume": 0.0004900885, "area": 0.0571769863},
    "model_31391_df3562f8_0001": {"func": model_31391_df3562f8_0001, "volume": 2.1362830044, "area": 21.6141574567},
    "model_31391_df3562f8_0002": {"func": model_31391_df3562f8_0002, "volume": 0.0108384947, "area": 2.6012387172},
    "model_31391_df3562f8_0003": {"func": model_31391_df3562f8_0003, "volume": 120, "area": 824},
    "model_31391_df3562f8_0005": {"func": model_31391_df3562f8_0005, "volume": 0.7734287433, "area": 17.2619320525},
    "model_31464_b2855e3a_0008": {"func": model_31464_b2855e3a_0008, "volume": 2.0154240432, "area": 19.9972872379},
    "model_31464_b2855e3a_0014": {"func": model_31464_b2855e3a_0014, "volume": 0.4504629489, "area": 4.9657332952},
    "model_31464_b2855e3a_0018": {"func": model_31464_b2855e3a_0018, "volume": 0.0511597206, "area": 2.8466826176},
    "model_31596_4acd1c1d_0000": {"func": model_31596_4acd1c1d_0000, "volume": 45, "area": 93},
    "model_31616_c013ae1f_0000": {"func": model_31616_c013ae1f_0000, "volume": 2324.7848154258, "area": 1413.6551126162},
    "model_31627_6b01242d_0000": {"func": model_31627_6b01242d_0000, "volume": 0.1482517633, "area": 3.725300696},
    "model_31627_ec13313b_0000": {"func": model_31627_ec13313b_0000, "volume": 0.0829066301, "area": 2.2299024655},
    "model_31652_96a3746c_0000": {"func": model_31652_96a3746c_0000, "volume": 17.3075412247, "area": 70.402118762},
    "model_31655_baca05af_0000": {"func": model_31655_baca05af_0000, "volume": 11.5284568751, "area": 71.365167252},
    "model_31740_86dab66b_0000": {"func": model_31740_86dab66b_0000, "volume": 2700, "area": 3000},
    "model_31866_a5b1db64_0001": {"func": model_31866_a5b1db64_0001, "volume": 0.7147123287, "area": 14.6084058392},
    "model_31962_e5291336_0003": {"func": model_31962_e5291336_0003, "volume": 0.0499667333, "area": 1.5013914227},
    "model_31962_e5291336_0011": {"func": model_31962_e5291336_0011, "volume": 0.2163649797, "area": 2.9551043946},
    "model_31962_e5291336_0016": {"func": model_31962_e5291336_0016, "volume": 0.1507964474, "area": 2.5132741229},
    "model_31962_e5291336_0027": {"func": model_31962_e5291336_0027, "volume": 1.4333516482, "area": 11.8595122673},
    "model_31962_e5291336_0029": {"func": model_31962_e5291336_0029, "volume": 25.470462439, "area": 72.6179141877},
    "model_31962_e5291336_0030": {"func": model_31962_e5291336_0030, "volume": 0.1037497608, "area": 3.3687945742},
    "model_31962_e5291336_0031": {"func": model_31962_e5291336_0031, "volume": 1.9242255003, "area": 78.0685774417},
    "model_31962_e5291336_0033": {"func": model_31962_e5291336_0033, "volume": 5.9690260418, "area": 25.4469004941},
    "model_31962_e5291336_0036": {"func": model_31962_e5291336_0036, "volume": 0.0547815219, "area": 1.5825772992},
    "model_31962_e5291336_0037": {"func": model_31962_e5291336_0037, "volume": 7.8791143752, "area": 27.4575197924},
    "model_31962_e5291336_0038": {"func": model_31962_e5291336_0038, "volume": 3.9819686884, "area": 25.1680841461},
    "model_31962_e5291336_0051": {"func": model_31962_e5291336_0051, "volume": 0.1287010218, "area": 3.9595092334},
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
