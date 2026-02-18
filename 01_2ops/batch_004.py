"""Batch 004 - passing/01_2ops
145 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a hexagonal or elongated prismatic part with a tapered wedge-shaped top surface featuring multiple triangulated facets, dark recessed side surfaces, and a rectangular base.
def model_135230_c38e50b2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36.0611451754, perimeter: 29.4065482457
            with BuildLine():
                Line((-5.33, 6.86), (0, 6.86))
                Line((-5.33, 0), (-5.33, 6.86))
                Line((0, 0), (-5.33, 0))
                Line((0, 6.86), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-0.76, 6.61), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.25, 1.4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.07, 1.53), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.55, 6.61), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0640884901, perimeter: 2.1362830044
            with BuildLine():
                CenterArc((-0.76, 6.61), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.76, 6.61), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((-0.76, 6.61)):
                Circle(0.14)
            # Profile area: 0.0640884901, perimeter: 2.1362830044
            with BuildLine():
                CenterArc((-0.25, 1.4), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.25, 1.4), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((-0.25, 1.4)):
                Circle(0.14)
            # Profile area: 0.0640884901, perimeter: 2.1362830044
            with BuildLine():
                CenterArc((-5.07, 1.53), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.07, 1.53), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((-5.07, 1.53)):
                Circle(0.14)
            # Profile area: 0.0640884901, perimeter: 2.1362830044
            with BuildLine():
                CenterArc((-3.55, 6.61), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.55, 6.61), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((-3.55, 6.61)):
                Circle(0.14)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


# Description: This is a flat rectangular plate or panel with a parallelogram shape, featuring a simple planar geometry with beveled or chamfered edges along its perimeter.
def model_135445_77b4ac77_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.34, perimeter: 9
            with BuildLine():
                Line((-1.55, 0.7), (1.55, 0.7))
                Line((-1.55, -0.7), (-1.55, 0.7))
                Line((1.55, -0.7), (-1.55, -0.7))
                Line((1.55, 0.7), (1.55, -0.7))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a tapered cone or wedge-shaped rod with a long, slender body that gradually narrows to a sharp point at one end, commonly used as a drift punch, alignment tool, or tapered pin in mechanical applications.
def model_135514_12de81ba_0001():
    """Model: joist"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7800, perimeter: 821.1521443122
            with BuildLine():
                Line((-390, 260), (0, 290))
                Line((0, 290), (0, 295))
                Line((0, 295), (-390, 295))
                Line((-390, 295), (-390, 260))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a structural bracket or support component with a streamlined, wing-like shape featuring dual mounting flanges on the sides, internal truss-like reinforcement webbing, and a tapered profile designed for lightweight strength and aerodynamic efficiency.
def model_135518_26ac8077_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 91.0190024171, perimeter: 48.7081142364
            with BuildLine():
                Line((-5.4693974959, -0.1526359913), (-5.9000000879, 0.1000000015))
                Line((-3.6000000536, -0.5000000075), (-5.4693974959, -0.1526359913))
                Line((-1.9000000283, -2.3000000343), (-3.6000000536, -0.5000000075))
                Line((-1.4000000209, -4.5000000671), (-1.9000000283, -2.3000000343))
                Line((-1.4000000209, -5.6000000834), (-1.4000000209, -4.5000000671))
                Line((-1.6000000238, -5.9000000879), (-1.4000000209, -5.6000000834))
                Line((-0.200000003, -6.3000000939), (-1.6000000238, -5.9000000879))
                Line((1.179005522, -6.3000000939), (-0.200000003, -6.3000000939))
                Line((1.3116075481, -6.1500000916), (1.179005522, -6.3000000939))
                Line((3.5000000522, -6.3000000939), (1.3116075481, -6.1500000916))
                Line((4.0000000596, -6.0000000894), (3.5000000522, -6.3000000939))
                Line((3.7968243099, -5.3216765041), (4.0000000596, -6.0000000894))
                Line((4.70000007, -4.3000000641), (3.7968243099, -5.3216765041))
                Line((7.0000001043, -4.4000000656), (4.70000007, -4.3000000641))
                Line((8.1253907446, -3.1269531641), (7.0000001043, -4.4000000656))
                Line((8.0000001192, -2.5000000373), (8.1253907446, -3.1269531641))
                Line((7.5000001118, -2.6000000387), (8.0000001192, -2.5000000373))
                Line((7.2000001073, -2.2000000328), (7.5000001118, -2.6000000387))
                Line((7.1000001058, -1.7000000253), (7.2000001073, -2.2000000328))
                Line((6.6672288859, -1.5462870077), (7.1000001058, -1.7000000253))
                Line((6.9000001028, -1.2000000179), (6.6672288859, -1.5462870077))
                Line((5.9417022081, 0.0950331939), (6.9000001028, -1.2000000179))
                Line((5.244314201, 0.0950331939), (5.9417022081, 0.0950331939))
                Line((4.8039325897, 0.6030097035), (5.244314201, 0.0950331939))
                Line((6.3000000939, 1.9000000283), (4.8039325897, 0.6030097035))
                Line((6.0650038644, 2.9139985338), (6.3000000939, 1.9000000283))
                Line((6.1632637933, 3.9626754891), (6.0650038644, 2.9139985338))
                Line((4.6000000685, 3.8000000566), (6.1632637933, 3.9626754891))
                Line((4.2698134776, 4.1253509217), (4.6000000685, 3.8000000566))
                Line((3.6000000536, 3.9000000581), (4.2698134776, 4.1253509217))
                Line((3.1000000462, 4.1000000611), (3.6000000536, 3.9000000581))
                Line((2.6296675519, 4.1507017822), (3.1000000462, 4.1000000611))
                Line((2.5000000373, 4.4000000656), (2.6296675519, 4.1507017822))
                Line((1.8792053686, 4.2797573653), (2.5000000373, 4.4000000656))
                Line((1.8318624735, 4.7531863155), (1.8792053686, 4.2797573653))
                Line((1.3000000194, 4.70000007), (1.8318624735, 4.7531863155))
                Line((0.5079242408, 4.8240074255), (1.3000000194, 4.70000007))
                Line((0.0264136649, 5.4125203516), (0.5079242408, 4.8240074255))
                Line((-0.6000000089, 4.900000073), (0.0264136649, 5.4125203516))
                Line((-0.5000000075, 3.9000000581), (-0.6000000089, 4.900000073))
                Line((-1.6000000238, 3.0000000447), (-0.5000000075, 3.9000000581))
                Line((-1.7287975631, 2.7165973064), (-1.6000000238, 3.0000000447))
                Line((-2.6639303789, 2.2683640357), (-1.7287975631, 2.7165973064))
                Line((-3.1684971296, 2.7165973064), (-2.6639303789, 2.2683640357))
                Line((-3.6827304343, 2.5182501746), (-3.1684971296, 2.7165973064))
                Line((-3.1684971296, 1.5832805297), (-3.6827304343, 2.5182501746))
                Line((-4.1969637389, 1.0176238945), (-3.1684971296, 1.5832805297))
                Line((-4.3705477679, 1.3332312199), (-4.1969637389, 1.0176238945))
                Line((-6.0070301956, 0.7020165692), (-4.3705477679, 1.3332312199))
                Line((-5.7498686713, 0.2344501612), (-6.0070301956, 0.7020165692))
                Line((-5.9000000879, 0.1000000015), (-5.7498686713, 0.2344501612))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a rectangular frame or channel assembly composed of four connected trapezoidal box sections arranged in an open rectangular loop configuration, featuring hollow interior passages and angled side walls.
def model_135538_9913818f_0003():
    """Model: Seat Stretcher"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on Plane3 construction plane
        # Sketch has 24 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 25.4, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100.80625, perimeter: 69.85
            with BuildLine():
                Line((38.735, -30.7975), (6.985, -30.7975))
                Line((38.735, -27.6225), (38.735, -30.7975))
                Line((6.985, -27.6225), (38.735, -27.6225))
                Line((6.985, -30.7975), (6.985, -27.6225))
            make_face()
            # Profile area: 100.80625, perimeter: 69.85
            with BuildLine():
                Line((38.735, -4.1275), (6.985, -4.1275))
                Line((38.735, -0.9525), (38.735, -4.1275))
                Line((6.985, -0.9525), (38.735, -0.9525))
                Line((6.985, -4.1275), (6.985, -0.9525))
            make_face()
            # Profile area: 68.54825, perimeter: 49.53
            with BuildLine():
                Line((42.8625, -26.67), (39.6875, -26.67))
                Line((42.8625, -5.08), (42.8625, -26.67))
                Line((39.6875, -5.08), (42.8625, -5.08))
                Line((39.6875, -26.67), (39.6875, -5.08))
            make_face()
            # Profile area: 68.54825, perimeter: 49.53
            with BuildLine():
                Line((6.0325, -26.67), (2.8575, -26.67))
                Line((6.0325, -5.08), (6.0325, -26.67))
                Line((2.8575, -5.08), (6.0325, -5.08))
                Line((2.8575, -26.67), (2.8575, -5.08))
            make_face()
        # OneSide extrude, distance=5.715
        extrude(amount=5.715)
    return part.part


# Description: This is a flat, trapezoidal base plate or platform with a triangulated surface pattern and a beveled or sloped edge on one side, featuring a wedge-like or tapered profile.
def model_135538_9913818f_0005():
    """Model: Seat Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1625.8032, perimeter: 162.56
            with BuildLine():
                Line((45.72, -35.56), (0, -35.56))
                Line((45.72, 0), (45.72, -35.56))
                Line((0, 0), (45.72, 0))
                Line((0, -35.56), (0, 0))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a elongated hexagonal prism or channel-like structural component with a tapered design, featuring a hollow rectangular cross-section and angled end faces that narrow toward one end.
def model_135538_9913818f_0012():
    """Model: Long Apron"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 33.655), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 184.3087369244, perimeter: 75.9736561672
            with BuildLine():
                Line((6.4850022879, 55.245), (6.985, 60.96))
                Line((6.4850022879, 55.245), (39.2349977121, 55.245))
                Line((38.735, 60.96), (39.2349977121, 55.245))
                Line((6.985, 60.96), (38.735, 60.96))
            make_face()
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)
    return part.part


# Description: This is a hexagonal prism or bar stock with a long, slender elongated body featuring faceted sides and tapered or beveled edges at both ends.
def model_135538_9913818f_0013():
    """Model: Short Apron"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 123.38685, perimeter: 54.61
            with BuildLine():
                Line((-28.575, 0), (-6.985, 0))
                Line((-6.985, 0), (-6.985, 5.715))
                Line((-6.985, 5.715), (-28.575, 5.715))
                Line((-28.575, 5.715), (-28.575, 0))
            make_face()
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)
    return part.part


# Description: This is a hexagonal or multi-sided extruded tube or shaft with a long, slender cylindrical body and a slightly tapered or beveled top end, appearing to be a structural component or connector element.
def model_135538_9913818f_0018():
    """Model: Leg 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.8064, perimeter: 20.32
            with BuildLine():
                Line((5.08, -5.08), (0, -5.08))
                Line((5.08, 0), (5.08, -5.08))
                Line((0, 0), (5.08, 0))
                Line((0, -5.08), (0, 0))
            make_face()
        # OneSide extrude, distance=60.96
        extrude(amount=60.96)
    return part.part


# Description: This is a wedge-shaped or tapered hexagonal prism component with a sloped top surface featuring parallel linear grooves or ribs running across its face, and a dark underside, commonly used as a structural support or connector element.
def model_135538_9913818f_0021():
    """Model: Tabletop2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4615.9181875, perimeter: 268.7184843744
            with BuildLine():
                Line((15.24, 0), (0, -15.24))
                Line((0, -15.24), (0, -76.2))
                Line((0, -76.2), (29.845, -76.2))
                Line((29.845, -76.2), (76.2, -29.845))
                Line((76.2, 0), (76.2, -29.845))
                Line((15.24, 0), (76.2, 0))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a dual-chamber rocket or missile component with an elongated cylindrical body featuring two vertical tubular sections (likely nozzles or thruster chambers) extending upward from a central flat base platform.
def model_135630_863a2309_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.8880255218, perimeter: 55.6940752765
            with BuildLine():
                CenterArc((-15.1493903346, 2.2), 2.2, -135, 45)
                Line((0, 0), (-15.1493903346, 0))
                Line((0, 0), (0, 1.5))
                Line((0, 1.5), (-4, 1.5))
                CenterArc((-4, 2), 0.5, 180, 90)
                Line((-4.5, 2), (-4.5, 6))
                CenterArc((-6.5, 6), 2, 0, 180)
                Line((-8.5, 6), (-8.5, 2))
                CenterArc((-9, 2), 0.5, -90, 90)
                Line((-14.6109127035, 1.5), (-9, 1.5))
                CenterArc((-14.6109127035, 3.5), 2, -135, 45)
                Line((-18.9393398282, 5), (-16.0251262658, 2.0857864376))
                Line((-20, 3.9393398282), (-18.9393398282, 5))
                Line((-16.7050252532, 0.6443650814), (-20, 3.9393398282))
            make_face()
        # Symmetric extrude, full_length=True, total=2.5
        extrude(amount=1.25, both=True)
    return part.part


# Description: This is a rectangular panel or frame assembly with a flat face featuring a geometric lattice or truss pattern, internal rectangular cutouts/windows, and triangulated structural bracing elements visible on its surface.
def model_135872_a6ca0e40_0000():
    """Model: Slider Plate v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 220.9380532894, perimeter: 75.8796447372
            with BuildLine():
                Line((1.4715000874, 16.4445184732), (1.4715000874, 4.0445184732))
                Line((1.4715000874, 4.0445184732), (19.4715000874, 4.0445184732))
                Line((19.4715000874, 4.0445184732), (19.4715000874, 16.4445184732))
                Line((1.4715000874, 16.4445184732), (19.4715000874, 16.4445184732))
            make_face()
            with BuildLine():
                CenterArc((2.4715000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2115000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7315000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7315000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2115000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4715000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical rod or shaft with a slight taper, featuring a simple elongated tubular form with rounded ends and a uniform dark gray surface finish.
def model_135872_a6ca0e40_0001():
    """Model: X-axis_1 Beam_160*80*2000 v1"""
    with BuildPart() as part:
        # 80X160 ITM26526 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.3087970362, perimeter: 168.0793754218
            with BuildLine():
                CenterArc((-2.4999999999, 7.65), 0.1, -90, 90)
                Line((-2.3999999999, 7.85), (-2.3999999999, 7.65))
                CenterArc((-2.5499999999, 7.85), 0.15, 0, 90)
                Line((-3.6, 8), (-2.5499999999, 8))
                CenterArc((-3.6, 7.6), 0.4, 90, 90)
                Line((-3.9999999999, 6.55), (-3.9999999999, 7.6))
                CenterArc((-3.85, 6.55), 0.15, 180, 90)
                Line((-3.6499999999, 6.4), (-3.85, 6.4))
                CenterArc((-3.6499999999, 6.5), 0.1, -90, 90)
                Line((-3.55, 6.891611505), (-3.55, 6.5))
                CenterArc((-3.441611505, 6.891611505), 0.108388495, 53.6249663649, 126.3750336351)
                CenterArc((-4.86, 4.966), 2.5, 36.6419281385, 16.9830382287)
                CenterArc((-3.175, 6.219305629), 0.4000000001, 0, 36.6419281384)
                Line((-2.7749999999, 5.780694371), (-2.7749999999, 6.219305629))
                CenterArc((-3.1749999999, 5.780694371), 0.4, -36.6419281384, 36.6419281384)
                CenterArc((-4.86, 7.034), 2.5, -53.6249663673, 16.9830382289)
                CenterArc((-3.441611505, 5.108388495), 0.108388495, 180, 126.3750336328)
                Line((-3.55, 5.5), (-3.55, 5.108388495))
                CenterArc((-3.65, 5.5), 0.1, 0, 90)
                Line((-3.85, 5.6), (-3.65, 5.6))
                CenterArc((-3.85, 5.45), 0.15, 90, 90)
                Line((-4, 2.55), (-4, 5.45))
                CenterArc((-3.85, 2.55), 0.15, 180, 90)
                Line((-3.65, 2.4), (-3.85, 2.4))
                CenterArc((-3.65, 2.5), 0.1, -90, 90)
                Line((-3.55, 2.891611505), (-3.55, 2.5))
                CenterArc((-3.441611505, 2.891611505), 0.108388495, 53.6249663672, 126.3750336328)
                CenterArc((-4.86, 0.966), 2.5, 36.6419281384, 16.9830382287)
                CenterArc((-3.175, 2.219305629), 0.4000000001, 0, 36.6419281384)
                Line((-2.7749999999, 1.780694371), (-2.7749999999, 2.219305629))
                CenterArc((-3.1749999999, 1.780694371), 0.4, -36.6419281378, 36.6419281378)
                CenterArc((-4.86, 3.034), 2.5, -53.6249663672, 16.9830382288)
                CenterArc((-3.441611505, 1.108388495), 0.108388495, 180, 126.3750336309)
                Line((-3.55, 1.5), (-3.55, 1.108388495))
                CenterArc((-3.65, 1.5), 0.1, 0, 90)
                Line((-3.85, 1.6), (-3.65, 1.6))
                CenterArc((-3.85, 1.45), 0.15, 90, 89.9999999914)
                Line((-4, -1.45), (-4, 1.45))
                CenterArc((-3.85, -1.45), 0.15, 180, 90)
                Line((-3.65, -1.6), (-3.85, -1.6))
                CenterArc((-3.65, -1.5), 0.1, -90, 90)
                Line((-3.55, -1.108388495), (-3.55, -1.5))
                CenterArc((-3.441611505, -1.108388495), 0.108388495, 53.6249663672, 126.3750336328)
                CenterArc((-4.86, -3.034), 2.5, 36.6419281384, 16.9830382287)
                CenterArc((-3.175, -1.780694371), 0.4000000001, 0, 36.6419281384)
                Line((-2.7749999999, -2.219305629), (-2.7749999999, -1.780694371))
                CenterArc((-3.1749999999, -2.219305629), 0.4, -36.6419281384, 36.6419281384)
                CenterArc((-4.86, -0.966), 2.5, -53.6249663673, 16.9830382288)
                CenterArc((-3.441611505, -2.891611505), 0.108388495, 180, 126.3750336328)
                Line((-3.55, -2.5), (-3.55, -2.891611505))
                CenterArc((-3.65, -2.5), 0.1, 0, 90)
                Line((-3.85, -2.4), (-3.65, -2.4))
                CenterArc((-3.85, -2.55), 0.15, 90, 90)
                Line((-4, -5.45), (-4, -2.55))
                CenterArc((-3.85, -5.45), 0.15, 180, 90)
                Line((-3.65, -5.6), (-3.85, -5.6))
                CenterArc((-3.65, -5.5), 0.1, -90, 90)
                Line((-3.55, -5.108388495), (-3.55, -5.5))
                CenterArc((-3.441611505, -5.108388495), 0.108388495, 53.6249663672, 126.3750336328)
                CenterArc((-4.86, -7.034), 2.5, 36.6419281386, 16.9830382285)
                CenterArc((-3.175, -5.780694371), 0.4000000001, 0, 36.6419281384)
                Line((-2.7749999999, -6.219305629), (-2.7749999999, -5.780694371))
                CenterArc((-3.175, -6.219305629), 0.4, -36.641928139, 36.641928139)
                CenterArc((-4.86, -4.966), 2.5, -53.6249663672, 16.9830382288)
                CenterArc((-3.441611505, -6.891611505), 0.108388495, 180, 126.3750336309)
                Line((-3.55, -6.5), (-3.55, -6.891611505))
                CenterArc((-3.65, -6.5), 0.1, 0, 90)
                Line((-3.85, -6.4), (-3.65, -6.4))
                CenterArc((-3.85, -6.55), 0.15, 90, 90)
                Line((-4, -7.6), (-4, -6.55))
                CenterArc((-3.6, -7.6), 0.4, 180, 90)
                Line((-2.55, -8), (-3.6, -8))
                CenterArc((-2.55, -7.85), 0.15, -90, 90)
                Line((-2.4, -7.65), (-2.4, -7.85))
                CenterArc((-2.5, -7.65), 0.1, 0, 90)
                Line((-2.891611505, -7.55), (-2.5, -7.55))
                CenterArc((-2.891611505, -7.441611505), 0.108388495, 143.6249663691, 126.3750336309)
                CenterArc((-0.966, -8.86), 2.5, 126.6419281384, 16.9830382288)
                CenterArc((-2.219305629, -7.175), 0.4000000001, 90, 36.6419281385)
                Line((-1.780694371, -6.7749999999), (-2.219305629, -6.7749999999))
                CenterArc((-1.780694371, -7.175), 0.4, 53.3580718622, 36.6419281378)
                CenterArc((-3.034, -8.86), 2.5, 36.3750336328, 16.9830382288)
                CenterArc((-1.108388495, -7.441611505), 0.108388495, -90, 126.3750336309)
                Line((-1.5, -7.55), (-1.108388495, -7.55))
                CenterArc((-1.5, -7.65), 0.1, 90, 90)
                Line((-1.6, -7.85), (-1.6, -7.65))
                CenterArc((-1.45, -7.85), 0.15, 180, 90)
                Line((1.45, -8), (-1.45, -8))
                CenterArc((1.45, -7.85), 0.15, -89.9999999957, 89.9999999957)
                Line((1.6, -7.65), (1.6, -7.85))
                CenterArc((1.5, -7.65), 0.1, 0, 90)
                Line((1.108388495, -7.55), (1.5, -7.55))
                CenterArc((1.108388495, -7.441611505), 0.108388495, 143.6249663691, 126.3750336309)
                CenterArc((3.034, -8.86), 2.5, 126.6419281384, 16.9830382288)
                CenterArc((1.780694371, -7.175), 0.4000000001, 90, 36.6419281384)
                Line((2.219305629, -6.7749999999), (1.780694371, -6.7749999999))
                CenterArc((2.219305629, -7.175), 0.4, 53.358071861, 36.641928139)
                CenterArc((0.966, -8.86), 2.5, 36.3750336328, 16.9830382288)
                CenterArc((2.891611505, -7.441611505), 0.108388495, -90, 126.3750336309)
                Line((2.5, -7.55), (2.891611505, -7.55))
                CenterArc((2.5, -7.65), 0.1, 90, 90)
                Line((2.4, -7.85), (2.4, -7.65))
                CenterArc((2.55, -7.85), 0.15, 180, 90)
                Line((3.6, -8), (2.55, -8))
                CenterArc((3.6, -7.6), 0.4, -90, 90)
                Line((4, -6.55), (4, -7.6))
                CenterArc((3.85, -6.55), 0.15, 0, 90)
                Line((3.65, -6.4), (3.85, -6.4))
                CenterArc((3.65, -6.5), 0.1, 90, 90)
                Line((3.55, -6.891611505), (3.55, -6.5))
                CenterArc((3.441611505, -6.891611505), 0.108388495, -126.3750336328, 126.3750336328)
                CenterArc((4.86, -4.966), 2.5, -143.3580718616, 16.9830382287)
                CenterArc((3.175, -6.219305629), 0.4000000001, 180, 36.6419281385)
                Line((2.7749999999, -5.780694371), (2.7749999999, -6.219305629))
                CenterArc((3.175, -5.780694371), 0.4, 143.3580718616, 36.6419281384)
                CenterArc((4.86, -7.034), 2.5, 126.3750336329, 16.9830382286)
                CenterArc((3.441611505, -5.108388495), 0.108388495, 0, 126.3750336328)
                Line((3.55, -5.5), (3.55, -5.108388495))
                CenterArc((3.65, -5.5), 0.1, 180, 90)
                Line((3.85, -5.6), (3.65, -5.6))
                CenterArc((3.85, -5.45), 0.15, -90, 90)
                Line((4, -2.55), (4, -5.45))
                CenterArc((3.85, -2.55), 0.15, 0, 90)
                Line((3.65, -2.4), (3.85, -2.4))
                CenterArc((3.65, -2.5), 0.1, 90, 90)
                Line((3.55, -2.891611505), (3.55, -2.5))
                CenterArc((3.441611505, -2.891611505), 0.108388495, -126.3750336309, 126.3750336309)
                CenterArc((4.86, -0.966), 2.5, -143.3580718616, 16.9830382288)
                CenterArc((3.175, -2.219305629), 0.4000000001, 180, 36.6419281384)
                Line((2.7749999999, -1.780694371), (2.7749999999, -2.219305629))
                CenterArc((3.175, -1.780694371), 0.4, 143.3580718622, 36.6419281378)
                CenterArc((4.86, -3.0340000001), 2.5, 126.3750336328, 16.9830382288)
                CenterArc((3.441611505, -1.108388495), 0.108388495, 0, 126.375033634)
                Line((3.55, -1.5), (3.55, -1.108388495))
                CenterArc((3.65, -1.5), 0.1, 180, 90)
                Line((3.85, -1.6), (3.65, -1.6))
                CenterArc((3.85, -1.45), 0.15, -90, 90)
                Line((4, 1.45), (4, -1.45))
                CenterArc((3.85, 1.45), 0.15, 0, 90)
                Line((3.65, 1.6), (3.85, 1.6))
                CenterArc((3.65, 1.5), 0.1, 90, 90)
                Line((3.55, 1.108388495), (3.55, 1.5))
                CenterArc((3.441611505, 1.108388495), 0.108388495, -126.3750336328, 126.3750336328)
                CenterArc((4.86, 3.034), 2.5, -143.3580718614, 16.9830382285)
                CenterArc((3.175, 1.780694371), 0.4000000001, 180, 36.6419281384)
                Line((2.7749999999, 2.219305629), (2.7749999999, 1.780694371))
                CenterArc((3.175, 2.219305629), 0.4, 143.3580718616, 36.6419281384)
                CenterArc((4.86, 0.966), 2.5, 126.3750336328, 16.9830382289)
                CenterArc((3.441611505, 2.891611505), 0.108388495, 0, 126.3750336309)
                Line((3.55, 2.5), (3.55, 2.891611505))
                CenterArc((3.65, 2.5), 0.1, 180, 90)
                Line((3.85, 2.4), (3.65, 2.4))
                CenterArc((3.85, 2.55), 0.15, -90, 90)
                Line((4, 5.45), (4, 2.55))
                CenterArc((3.85, 5.45), 0.15, 0, 90)
                Line((3.65, 5.6), (3.85, 5.6))
                CenterArc((3.65, 5.5), 0.1, 90, 90)
                Line((3.55, 5.108388495), (3.55, 5.5))
                CenterArc((3.441611505, 5.108388495), 0.108388495, -126.3750336328, 126.3750336328)
                CenterArc((4.86, 7.034), 2.5, -143.3580718616, 16.9830382289)
                CenterArc((3.1750000001, 5.780694371), 0.4000000001, 180, 36.6419281384)
                Line((2.7749999999, 6.219305629), (2.7749999999, 5.780694371))
                CenterArc((3.175, 6.219305629), 0.4, 143.3580718622, 36.6419281378)
                CenterArc((4.86, 4.9659999999), 2.5, 126.3750336328, 16.9830382288)
                CenterArc((3.441611505, 6.8916115049), 0.108388495, 0, 126.3750336309)
                Line((3.55, 6.4999999999), (3.55, 6.8916115049))
                CenterArc((3.65, 6.4999999999), 0.1, 180, 90)
                Line((3.85, 6.4), (3.65, 6.4))
                CenterArc((3.85, 6.5499999999), 0.15, -90, 90)
                Line((4, 7.5999999999), (4, 6.5499999999))
                CenterArc((3.6, 7.5999999999), 0.4, 0, 90)
                Line((2.55, 7.9999999999), (3.6, 8))
                CenterArc((2.55, 7.8499999999), 0.15, 90, 90)
                Line((2.4, 7.6499999999), (2.4, 7.8499999999))
                CenterArc((2.5, 7.6499999999), 0.1, 180, 90)
                Line((2.891611505, 7.55), (2.5, 7.5499999999))
                CenterArc((2.891611505, 7.441611505), 0.108388495, -36.3750336328, 126.3750336328)
                CenterArc((0.966, 8.86), 2.5, -53.3580718616, 16.9830382289)
                CenterArc((2.219305629, 7.175), 0.4000000001, -90, 36.6419281364)
                Line((1.780694371, 6.7749999999), (2.219305629, 6.7749999999))
                CenterArc((1.780694371, 7.1749999999), 0.4, -126.6419281381, 36.6419281381)
                CenterArc((3.0340000001, 8.86), 2.5, -143.6249663672, 16.9830382288)
                CenterArc((1.108388495, 7.441611505), 0.108388495, 90, 126.3750336351)
                Line((1.5, 7.55), (1.108388495, 7.55))
                CenterArc((1.5, 7.65), 0.1, -90, 90)
                Line((1.6, 7.85), (1.6, 7.65))
                CenterArc((1.45, 7.85), 0.15, 0, 90.0000000306)
                Line((-1.45, 8), (1.45, 8))
                CenterArc((-1.45, 7.85), 0.15, 90, 90)
                Line((-1.6, 7.65), (-1.6, 7.85))
                CenterArc((-1.5, 7.65), 0.1, 180, 90)
                Line((-1.108388495, 7.55), (-1.5, 7.55))
                CenterArc((-1.108388495, 7.441611505), 0.108388495, -36.3750336309, 126.3750336309)
                CenterArc((-3.034, 8.86), 2.5, -53.3580718616, 16.9830382288)
                CenterArc((-1.780694371, 7.175), 0.4000000001, -90, 36.6419281384)
                Line((-2.219305629, 6.7749999999), (-1.780694371, 6.7749999999))
                CenterArc((-2.219305629, 7.1749999999), 0.4, -126.6419281384, 36.6419281384)
                CenterArc((-0.9659999999, 8.86), 2.5, -143.6249663672, 16.9830382287)
                CenterArc((-2.8916115049, 7.441611505), 0.108388495, 90, 126.3750336309)
                Line((-2.4999999999, 7.55), (-2.8916115049, 7.55))
            make_face()
            with BuildLine():
                CenterArc((-2, -6), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 2), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, 6), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 6), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -6), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, -2), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -2), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, 2), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.0460759069, -4.5656854261), (2.4306953149, -5.1810660181))
                CenterArc((2.3246292978, -5.075000001), 0.1499999999, -90, 45)
                Line((2.3246292978, -5.2250000009), (1.6034271238, -5.2250000009))
                Line((1.6034271238, -5.2250000009), (1.2249999998, -5.6034271249))
                Line((1.2249999998, -5.6034271249), (1.2249999998, -6.3246292989))
                CenterArc((1.0749999999, -6.3246292989), 0.1499999999, -45, 45)
                Line((1.181066017, -6.430695316), (0.565685425, -7.046075908))
                CenterArc((0, -6.480390483), 0.8000000001, -135, 90)
                Line((-0.565685425, -7.046075908), (-1.181066017, -6.430695316))
                CenterArc((-1.0749999999, -6.3246292989), 0.1499999999, 180, 45)
                Line((-1.2249999998, -6.3246292989), (-1.2249999998, -5.6034271249))
                Line((-1.2249999998, -5.6034271249), (-1.6034271238, -5.2250000009))
                Line((-1.6034271238, -5.2250000009), (-2.3246292978, -5.2250000009))
                CenterArc((-2.3246292978, -5.075000001), 0.1499999999, -134.9999999973, 44.9999999973)
                Line((-2.4306953149, -5.1810660181), (-3.0460759044, -4.5656854286))
                CenterArc((-2.4803904794, -4.0000000036), 0.8000000001, 135, 90)
                Line((-3.0460759044, -3.4343145786), (-2.4306953099, -2.8189339841))
                CenterArc((-2.3246292928, -2.9250000012), 0.1499999999, 90, 45)
                Line((-2.3246292928, -2.7750000013), (-1.6034271188, -2.7750000013))
                Line((-1.6034271188, -2.7750000013), (-1.2249999948, -2.3965728773))
                Line((-1.2249999948, -2.3965728773), (-1.2249999948, -1.6753707033))
                CenterArc((-1.0749999949, -1.6753707033), 0.1499999999, 135, 45)
                Line((-1.181066012, -1.5693046862), (-0.5656854225, -0.9539240967))
                CenterArc((0.0000000025, -1.5196095217), 0.8000000001, 45, 90)
                Line((0.5656854275, -0.9539240967), (1.181066017, -1.5693046862))
                CenterArc((1.0749999999, -1.6753707033), 0.1499999999, 0, 45)
                Line((1.2249999998, -1.6753707033), (1.2249999998, -2.3965728773))
                Line((1.2249999998, -2.3965728773), (1.6034271238, -2.7750000013))
                Line((1.6034271238, -2.7750000013), (2.3246292978, -2.7750000013))
                CenterArc((2.3246292978, -2.9250000012), 0.1499999999, 45, 45)
                Line((2.4306953149, -2.8189339841), (3.0460759069, -3.4343145761))
                CenterArc((2.4803904819, -4.0000000011), 0.8000000001, -45, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.2249999998, 6.3246292967), (1.2249999998, 5.6034271227))
                Line((1.2249999998, 5.6034271227), (1.6034271238, 5.2249999987))
                Line((1.6034271238, 5.2249999987), (2.3246292978, 5.2249999987))
                CenterArc((2.3246292978, 5.0749999988), 0.1499999999, 45, 45)
                Line((2.4306953149, 5.1810660159), (3.0460759069, 4.5656854239))
                CenterArc((2.4803904819, 3.9999999989), 0.8000000001, -45, 90)
                Line((3.0460759069, 3.4343145739), (2.4306953149, 2.8189339819))
                CenterArc((2.3246292978, 2.924999999), 0.1499999999, -90, 45)
                Line((2.3246292978, 2.7749999991), (1.6034271238, 2.7749999991))
                Line((1.6034271238, 2.7749999991), (1.2249999998, 2.3965728751))
                Line((1.2249999998, 2.3965728751), (1.2249999998, 1.6753707011))
                CenterArc((1.0749999999, 1.6753707011), 0.1499999999, -45, 45)
                Line((1.181066017, 1.569304684), (0.565685425, 0.953924092))
                CenterArc((0, 1.519609517), 0.8000000001, -135, 90)
                Line((-0.565685425, 0.953924092), (-1.181066017, 1.569304684))
                CenterArc((-1.0749999999, 1.6753707011), 0.1499999999, 180, 45)
                Line((-1.2249999998, 1.6753707011), (-1.2249999998, 2.3965728751))
                Line((-1.2249999998, 2.3965728751), (-1.6034271238, 2.7749999991))
                Line((-1.6034271238, 2.7749999991), (-2.3246292978, 2.7749999991))
                CenterArc((-2.3246292978, 2.924999999), 0.1499999999, -135, 45)
                Line((-2.4306953149, 2.8189339819), (-3.0460759044, 3.4343145714))
                CenterArc((-2.4803904794, 3.9999999964), 0.8000000001, 135, 90)
                Line((-3.0460759044, 4.5656854214), (-2.4306953099, 5.1810660159))
                CenterArc((-2.3246292928, 5.0749999988), 0.1499999999, 90, 45)
                Line((-2.3246292928, 5.2249999987), (-1.6034271188, 5.2249999987))
                Line((-1.6034271188, 5.2249999987), (-1.2249999948, 5.6034271227))
                Line((-1.2249999948, 5.6034271227), (-1.2249999948, 6.3246292967))
                CenterArc((-1.0749999949, 6.3246292967), 0.1499999999, 135, 45)
                Line((-1.181066012, 6.4306953138), (-0.5656854225, 7.0460759033))
                CenterArc((0.0000000025, 6.4803904783), 0.8000000001, 45, 90)
                Line((0.5656854275, 7.0460759033), (1.181066017, 6.4306953138))
                CenterArc((1.0749999999, 6.3246292967), 0.1499999999, 0, 45)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.4943046839, -0.1060660172), (-1.5693046839, -1.1810660172))
                CenterArc((-1.675370701, -1.0750000001), 0.1499999999, -90, 45.0000000027)
                Line((-1.675370701, -1.225), (-2.324629299, -1.225))
                CenterArc((-2.324629299, -1.0750000001), 0.1499999999, -135.0000000027, 45.0000000027)
                Line((-2.4306953161, -1.1810660172), (-3.5056953161, -0.1060660172))
                CenterArc((-3.3996292991, -0.0000000002), 0.1499999997, 135, 90)
                Line((-3.5056953161, 0.1060660168), (-2.4306953161, 1.1810660168))
                CenterArc((-2.324629299, 1.0749999997), 0.1499999999, 90, 45)
                Line((-2.324629299, 1.2249999996), (-1.675370701, 1.2249999996))
                CenterArc((-1.675370701, 1.0749999996), 0.1499999999, 45, 45)
                Line((-1.5693046839, 1.1810660168), (-0.4943046839, 0.1060660168))
                CenterArc((-0.6003707009, -0.0000000002), 0.1499999997, -45, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.4943046839, 0.1060660168), (1.5693046839, 1.1810660168))
                CenterArc((1.675370701, 1.0749999997), 0.1499999999, 90, 45)
                Line((1.675370701, 1.2249999996), (2.324629299, 1.2249999996))
                CenterArc((2.324629299, 1.0749999996), 0.1499999999, 45, 45)
                Line((2.4306953161, 1.1810660168), (3.5056953161, 0.1060660168))
                CenterArc((3.3996292991, -0.0000000002), 0.1499999997, -45, 90)
                Line((3.5056953161, -0.1060660172), (2.4306953161, -1.1810660172))
                CenterArc((2.324629299, -1.0750000001), 0.1499999999, -90, 45)
                Line((2.324629299, -1.225), (1.675370701, -1.225))
                CenterArc((1.675370701, -1.0750000001), 0.1499999999, -135.0000000027, 45.0000000027)
                Line((1.5693046839, -1.1810660172), (0.4943046839, -0.1060660172))
                CenterArc((0.6003707009, -0.0000000002), 0.1499999997, 135, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=200
        extrude(amount=200)
    return part.part


# Description: A rectangular box or enclosure with a tilted, wireframe-patterned face panel featuring an internal geometric truss or lattice structure.
def model_135872_a6ca0e40_0002():
    """Model: Slider Plate v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 39 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 561.3451332235, perimeter: 136.6991118431
            with BuildLine():
                Line((1.4715000874, 23.7945184732), (1.4715000874, -7.7054815268))
                Line((1.4715000874, -7.7054815268), (19.4715000874, -7.7054815268))
                Line((19.4715000874, -7.7054815268), (19.4715000874, 23.7945184732))
                Line((1.4715000874, 23.7945184732), (19.4715000874, 23.7945184732))
            make_face()
            with BuildLine():
                CenterArc((2.5398895515, 17.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2127706684, 17.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7302295064, 17.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4031106233, 17.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.6631106233, 14.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.6715000874, 6.0709184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5398895515, -1.7054815268), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2798895515, 14.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7302295064, -1.7054815268), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.2715000874, 6.0709184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5398895515, 14.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.6715000874, 10.0181184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.6631106233, 1.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4031106233, 14.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4031106233, 1.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2127706684, -1.7054815268), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5398895515, 1.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2798895515, 1.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4031106233, -1.7054815268), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.2715000874, 10.0181184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat, square panel with a geometric lattice or web-like pattern of rectangular openings and internal bracing ribs, creating a lightweight, structurally-reinforced sheet with a raised perimeter frame.
def model_135872_a6ca0e40_0004():
    """Model: Slider Plate v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 41 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 296.7451332235, perimeter: 107.2991118431
            with BuildLine():
                Line((1.4715000874, 16.4445184732), (1.4715000874, -0.3554815268))
                Line((1.4715000874, -0.3554815268), (19.4715000874, -0.3554815268))
                Line((19.4715000874, -0.3554815268), (19.4715000874, 16.4445184732))
                Line((1.4715000874, 16.4445184732), (19.4715000874, 16.4445184732))
            make_face()
            with BuildLine():
                CenterArc((2.4715000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.1944096694, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7485905054, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7315000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.6715000874, 6.0709184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4715000874, 0.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2115000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7485905054, 0.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.2715000874, 6.0709184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4715000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.6715000874, 10.0181184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7315000874, 3.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 3.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.1944096694, 0.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4715000874, 3.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2115000874, 3.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 0.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.2715000874, 10.0181184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a dark blue rectangular wallet or clutch with a textured geometric pattern on the upper half and smooth surface on the lower half, featuring a slightly curved, elongated rectangular shape.
def model_135872_a6ca0e40_0006():
    """Model: Gantry_550 Side v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 44 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 954.1451332235, perimeter: 181.7652645553
            with BuildLine():
                Line((1.4715000874, 16.4445184732), (1.4715000874, -0.3554815268))
                Line((1.4715000874, -0.3554815268), (19.4715000874, -0.3554815268))
                Line((19.4715000874, -0.3554815268), (19.4715000874, 16.4445184732))
                Line((19.4715000874, 24.4445184732), (19.4715000874, 16.4445184732))
                Line((17.4715000874, 54.6445184732), (19.4715000874, 24.4445184732))
                Line((1.4715000874, 54.6445184732), (17.4715000874, 54.6445184732))
                Line((1.4715000874, 16.4445184732), (1.4715000874, 54.6445184732))
            make_face()
            with BuildLine():
                CenterArc((2.4715000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2115000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7315000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 15.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7315000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.6715000874, 6.0709184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4715000874, 0.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2115000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7315000874, 0.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.2715000874, 6.0709184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4715000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.6715000874, 10.0181184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.7315000874, 3.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 12.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 3.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2115000874, 0.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4715000874, 3.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2115000874, 3.7945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((18.4715000874, 0.2945184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.2715000874, 10.0181184732), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender rectangular profile, slightly tapered at the ends, featuring a smooth surface with no visible holes, slots, or flanges.
def model_135872_a6ca0e40_0014():
    """Model: Y-Axis_Undriven 1540 v1"""
    with BuildPart() as part:
        # 80X160 ITM26526 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.3087970362, perimeter: 168.0793754218
            with BuildLine():
                CenterArc((-2.4999999999, 7.65), 0.1, -90, 90)
                Line((-2.3999999999, 7.85), (-2.3999999999, 7.65))
                CenterArc((-2.5499999999, 7.85), 0.15, 0, 90)
                Line((-3.6, 8), (-2.5499999999, 8))
                CenterArc((-3.6, 7.6), 0.4, 90, 90)
                Line((-3.9999999999, 6.55), (-3.9999999999, 7.6))
                CenterArc((-3.85, 6.55), 0.15, 180, 90)
                Line((-3.6499999999, 6.4), (-3.85, 6.4))
                CenterArc((-3.6499999999, 6.5), 0.1, -90, 90)
                Line((-3.55, 6.891611505), (-3.55, 6.5))
                CenterArc((-3.441611505, 6.891611505), 0.108388495, 53.6249663649, 126.3750336351)
                CenterArc((-4.86, 4.966), 2.5, 36.6419281385, 16.9830382287)
                CenterArc((-3.175, 6.219305629), 0.4000000001, 0, 36.6419281384)
                Line((-2.7749999999, 5.780694371), (-2.7749999999, 6.219305629))
                CenterArc((-3.1749999999, 5.780694371), 0.4, -36.6419281384, 36.6419281384)
                CenterArc((-4.86, 7.034), 2.5, -53.6249663673, 16.9830382289)
                CenterArc((-3.441611505, 5.108388495), 0.108388495, 180, 126.3750336328)
                Line((-3.55, 5.5), (-3.55, 5.108388495))
                CenterArc((-3.65, 5.5), 0.1, 0, 90)
                Line((-3.85, 5.6), (-3.65, 5.6))
                CenterArc((-3.85, 5.45), 0.15, 90, 90)
                Line((-4, 2.55), (-4, 5.45))
                CenterArc((-3.85, 2.55), 0.15, 180, 90)
                Line((-3.65, 2.4), (-3.85, 2.4))
                CenterArc((-3.65, 2.5), 0.1, -90, 90)
                Line((-3.55, 2.891611505), (-3.55, 2.5))
                CenterArc((-3.441611505, 2.891611505), 0.108388495, 53.6249663672, 126.3750336328)
                CenterArc((-4.86, 0.966), 2.5, 36.6419281384, 16.9830382287)
                CenterArc((-3.175, 2.219305629), 0.4000000001, 0, 36.6419281384)
                Line((-2.7749999999, 1.780694371), (-2.7749999999, 2.219305629))
                CenterArc((-3.1749999999, 1.780694371), 0.4, -36.6419281378, 36.6419281378)
                CenterArc((-4.86, 3.034), 2.5, -53.6249663672, 16.9830382288)
                CenterArc((-3.441611505, 1.108388495), 0.108388495, 180, 126.3750336309)
                Line((-3.55, 1.5), (-3.55, 1.108388495))
                CenterArc((-3.65, 1.5), 0.1, 0, 90)
                Line((-3.85, 1.6), (-3.65, 1.6))
                CenterArc((-3.85, 1.45), 0.15, 90, 89.9999999914)
                Line((-4, -1.45), (-4, 1.45))
                CenterArc((-3.85, -1.45), 0.15, 180, 90)
                Line((-3.65, -1.6), (-3.85, -1.6))
                CenterArc((-3.65, -1.5), 0.1, -90, 90)
                Line((-3.55, -1.108388495), (-3.55, -1.5))
                CenterArc((-3.441611505, -1.108388495), 0.108388495, 53.6249663672, 126.3750336328)
                CenterArc((-4.86, -3.034), 2.5, 36.6419281384, 16.9830382287)
                CenterArc((-3.175, -1.780694371), 0.4000000001, 0, 36.6419281384)
                Line((-2.7749999999, -2.219305629), (-2.7749999999, -1.780694371))
                CenterArc((-3.1749999999, -2.219305629), 0.4, -36.6419281384, 36.6419281384)
                CenterArc((-4.86, -0.966), 2.5, -53.6249663673, 16.9830382288)
                CenterArc((-3.441611505, -2.891611505), 0.108388495, 180, 126.3750336328)
                Line((-3.55, -2.5), (-3.55, -2.891611505))
                CenterArc((-3.65, -2.5), 0.1, 0, 90)
                Line((-3.85, -2.4), (-3.65, -2.4))
                CenterArc((-3.85, -2.55), 0.15, 90, 90)
                Line((-4, -5.45), (-4, -2.55))
                CenterArc((-3.85, -5.45), 0.15, 180, 90)
                Line((-3.65, -5.6), (-3.85, -5.6))
                CenterArc((-3.65, -5.5), 0.1, -90, 90)
                Line((-3.55, -5.108388495), (-3.55, -5.5))
                CenterArc((-3.441611505, -5.108388495), 0.108388495, 53.6249663672, 126.3750336328)
                CenterArc((-4.86, -7.034), 2.5, 36.6419281386, 16.9830382285)
                CenterArc((-3.175, -5.780694371), 0.4000000001, 0, 36.6419281384)
                Line((-2.7749999999, -6.219305629), (-2.7749999999, -5.780694371))
                CenterArc((-3.175, -6.219305629), 0.4, -36.641928139, 36.641928139)
                CenterArc((-4.86, -4.966), 2.5, -53.6249663672, 16.9830382288)
                CenterArc((-3.441611505, -6.891611505), 0.108388495, 180, 126.3750336309)
                Line((-3.55, -6.5), (-3.55, -6.891611505))
                CenterArc((-3.65, -6.5), 0.1, 0, 90)
                Line((-3.85, -6.4), (-3.65, -6.4))
                CenterArc((-3.85, -6.55), 0.15, 90, 90)
                Line((-4, -7.6), (-4, -6.55))
                CenterArc((-3.6, -7.6), 0.4, 180, 90)
                Line((-2.55, -8), (-3.6, -8))
                CenterArc((-2.55, -7.85), 0.15, -90, 90)
                Line((-2.4, -7.65), (-2.4, -7.85))
                CenterArc((-2.5, -7.65), 0.1, 0, 90)
                Line((-2.891611505, -7.55), (-2.5, -7.55))
                CenterArc((-2.891611505, -7.441611505), 0.108388495, 143.6249663691, 126.3750336309)
                CenterArc((-0.966, -8.86), 2.5, 126.6419281384, 16.9830382288)
                CenterArc((-2.219305629, -7.175), 0.4000000001, 90, 36.6419281385)
                Line((-1.780694371, -6.7749999999), (-2.219305629, -6.7749999999))
                CenterArc((-1.780694371, -7.175), 0.4, 53.3580718622, 36.6419281378)
                CenterArc((-3.034, -8.86), 2.5, 36.3750336328, 16.9830382288)
                CenterArc((-1.108388495, -7.441611505), 0.108388495, -90, 126.3750336309)
                Line((-1.5, -7.55), (-1.108388495, -7.55))
                CenterArc((-1.5, -7.65), 0.1, 90, 90)
                Line((-1.6, -7.85), (-1.6, -7.65))
                CenterArc((-1.45, -7.85), 0.15, 180, 90)
                Line((1.45, -8), (-1.45, -8))
                CenterArc((1.45, -7.85), 0.15, -89.9999999957, 89.9999999957)
                Line((1.6, -7.65), (1.6, -7.85))
                CenterArc((1.5, -7.65), 0.1, 0, 90)
                Line((1.108388495, -7.55), (1.5, -7.55))
                CenterArc((1.108388495, -7.441611505), 0.108388495, 143.6249663691, 126.3750336309)
                CenterArc((3.034, -8.86), 2.5, 126.6419281384, 16.9830382288)
                CenterArc((1.780694371, -7.175), 0.4000000001, 90, 36.6419281384)
                Line((2.219305629, -6.7749999999), (1.780694371, -6.7749999999))
                CenterArc((2.219305629, -7.175), 0.4, 53.358071861, 36.641928139)
                CenterArc((0.966, -8.86), 2.5, 36.3750336328, 16.9830382288)
                CenterArc((2.891611505, -7.441611505), 0.108388495, -90, 126.3750336309)
                Line((2.5, -7.55), (2.891611505, -7.55))
                CenterArc((2.5, -7.65), 0.1, 90, 90)
                Line((2.4, -7.85), (2.4, -7.65))
                CenterArc((2.55, -7.85), 0.15, 180, 90)
                Line((3.6, -8), (2.55, -8))
                CenterArc((3.6, -7.6), 0.4, -90, 90)
                Line((4, -6.55), (4, -7.6))
                CenterArc((3.85, -6.55), 0.15, 0, 90)
                Line((3.65, -6.4), (3.85, -6.4))
                CenterArc((3.65, -6.5), 0.1, 90, 90)
                Line((3.55, -6.891611505), (3.55, -6.5))
                CenterArc((3.441611505, -6.891611505), 0.108388495, -126.3750336328, 126.3750336328)
                CenterArc((4.86, -4.966), 2.5, -143.3580718616, 16.9830382287)
                CenterArc((3.175, -6.219305629), 0.4000000001, 180, 36.6419281385)
                Line((2.7749999999, -5.780694371), (2.7749999999, -6.219305629))
                CenterArc((3.175, -5.780694371), 0.4, 143.3580718616, 36.6419281384)
                CenterArc((4.86, -7.034), 2.5, 126.3750336329, 16.9830382286)
                CenterArc((3.441611505, -5.108388495), 0.108388495, 0, 126.3750336328)
                Line((3.55, -5.5), (3.55, -5.108388495))
                CenterArc((3.65, -5.5), 0.1, 180, 90)
                Line((3.85, -5.6), (3.65, -5.6))
                CenterArc((3.85, -5.45), 0.15, -90, 90)
                Line((4, -2.55), (4, -5.45))
                CenterArc((3.85, -2.55), 0.15, 0, 90)
                Line((3.65, -2.4), (3.85, -2.4))
                CenterArc((3.65, -2.5), 0.1, 90, 90)
                Line((3.55, -2.891611505), (3.55, -2.5))
                CenterArc((3.441611505, -2.891611505), 0.108388495, -126.3750336309, 126.3750336309)
                CenterArc((4.86, -0.966), 2.5, -143.3580718616, 16.9830382288)
                CenterArc((3.175, -2.219305629), 0.4000000001, 180, 36.6419281384)
                Line((2.7749999999, -1.780694371), (2.7749999999, -2.219305629))
                CenterArc((3.175, -1.780694371), 0.4, 143.3580718622, 36.6419281378)
                CenterArc((4.86, -3.0340000001), 2.5, 126.3750336328, 16.9830382288)
                CenterArc((3.441611505, -1.108388495), 0.108388495, 0, 126.375033634)
                Line((3.55, -1.5), (3.55, -1.108388495))
                CenterArc((3.65, -1.5), 0.1, 180, 90)
                Line((3.85, -1.6), (3.65, -1.6))
                CenterArc((3.85, -1.45), 0.15, -90, 90)
                Line((4, 1.45), (4, -1.45))
                CenterArc((3.85, 1.45), 0.15, 0, 90)
                Line((3.65, 1.6), (3.85, 1.6))
                CenterArc((3.65, 1.5), 0.1, 90, 90)
                Line((3.55, 1.108388495), (3.55, 1.5))
                CenterArc((3.441611505, 1.108388495), 0.108388495, -126.3750336328, 126.3750336328)
                CenterArc((4.86, 3.034), 2.5, -143.3580718614, 16.9830382285)
                CenterArc((3.175, 1.780694371), 0.4000000001, 180, 36.6419281384)
                Line((2.7749999999, 2.219305629), (2.7749999999, 1.780694371))
                CenterArc((3.175, 2.219305629), 0.4, 143.3580718616, 36.6419281384)
                CenterArc((4.86, 0.966), 2.5, 126.3750336328, 16.9830382289)
                CenterArc((3.441611505, 2.891611505), 0.108388495, 0, 126.3750336309)
                Line((3.55, 2.5), (3.55, 2.891611505))
                CenterArc((3.65, 2.5), 0.1, 180, 90)
                Line((3.85, 2.4), (3.65, 2.4))
                CenterArc((3.85, 2.55), 0.15, -90, 90)
                Line((4, 5.45), (4, 2.55))
                CenterArc((3.85, 5.45), 0.15, 0, 90)
                Line((3.65, 5.6), (3.85, 5.6))
                CenterArc((3.65, 5.5), 0.1, 90, 90)
                Line((3.55, 5.108388495), (3.55, 5.5))
                CenterArc((3.441611505, 5.108388495), 0.108388495, -126.3750336328, 126.3750336328)
                CenterArc((4.86, 7.034), 2.5, -143.3580718616, 16.9830382289)
                CenterArc((3.1750000001, 5.780694371), 0.4000000001, 180, 36.6419281384)
                Line((2.7749999999, 6.219305629), (2.7749999999, 5.780694371))
                CenterArc((3.175, 6.219305629), 0.4, 143.3580718622, 36.6419281378)
                CenterArc((4.86, 4.9659999999), 2.5, 126.3750336328, 16.9830382288)
                CenterArc((3.441611505, 6.8916115049), 0.108388495, 0, 126.3750336309)
                Line((3.55, 6.4999999999), (3.55, 6.8916115049))
                CenterArc((3.65, 6.4999999999), 0.1, 180, 90)
                Line((3.85, 6.4), (3.65, 6.4))
                CenterArc((3.85, 6.5499999999), 0.15, -90, 90)
                Line((4, 7.5999999999), (4, 6.5499999999))
                CenterArc((3.6, 7.5999999999), 0.4, 0, 90)
                Line((2.55, 7.9999999999), (3.6, 8))
                CenterArc((2.55, 7.8499999999), 0.15, 90, 90)
                Line((2.4, 7.6499999999), (2.4, 7.8499999999))
                CenterArc((2.5, 7.6499999999), 0.1, 180, 90)
                Line((2.891611505, 7.55), (2.5, 7.5499999999))
                CenterArc((2.891611505, 7.441611505), 0.108388495, -36.3750336328, 126.3750336328)
                CenterArc((0.966, 8.86), 2.5, -53.3580718616, 16.9830382289)
                CenterArc((2.219305629, 7.175), 0.4000000001, -90, 36.6419281364)
                Line((1.780694371, 6.7749999999), (2.219305629, 6.7749999999))
                CenterArc((1.780694371, 7.1749999999), 0.4, -126.6419281381, 36.6419281381)
                CenterArc((3.0340000001, 8.86), 2.5, -143.6249663672, 16.9830382288)
                CenterArc((1.108388495, 7.441611505), 0.108388495, 90, 126.3750336351)
                Line((1.5, 7.55), (1.108388495, 7.55))
                CenterArc((1.5, 7.65), 0.1, -90, 90)
                Line((1.6, 7.85), (1.6, 7.65))
                CenterArc((1.45, 7.85), 0.15, 0, 90.0000000306)
                Line((-1.45, 8), (1.45, 8))
                CenterArc((-1.45, 7.85), 0.15, 90, 90)
                Line((-1.6, 7.65), (-1.6, 7.85))
                CenterArc((-1.5, 7.65), 0.1, 180, 90)
                Line((-1.108388495, 7.55), (-1.5, 7.55))
                CenterArc((-1.108388495, 7.441611505), 0.108388495, -36.3750336309, 126.3750336309)
                CenterArc((-3.034, 8.86), 2.5, -53.3580718616, 16.9830382288)
                CenterArc((-1.780694371, 7.175), 0.4000000001, -90, 36.6419281384)
                Line((-2.219305629, 6.7749999999), (-1.780694371, 6.7749999999))
                CenterArc((-2.219305629, 7.1749999999), 0.4, -126.6419281384, 36.6419281384)
                CenterArc((-0.9659999999, 8.86), 2.5, -143.6249663672, 16.9830382287)
                CenterArc((-2.8916115049, 7.441611505), 0.108388495, 90, 126.3750336309)
                Line((-2.4999999999, 7.55), (-2.8916115049, 7.55))
            make_face()
            with BuildLine():
                CenterArc((-2, -6), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 2), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, 6), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 6), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -6), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, -2), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -2), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, 2), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.0460759069, -4.5656854261), (2.4306953149, -5.1810660181))
                CenterArc((2.3246292978, -5.075000001), 0.1499999999, -90, 45)
                Line((2.3246292978, -5.2250000009), (1.6034271238, -5.2250000009))
                Line((1.6034271238, -5.2250000009), (1.2249999998, -5.6034271249))
                Line((1.2249999998, -5.6034271249), (1.2249999998, -6.3246292989))
                CenterArc((1.0749999999, -6.3246292989), 0.1499999999, -45, 45)
                Line((1.181066017, -6.430695316), (0.565685425, -7.046075908))
                CenterArc((0, -6.480390483), 0.8000000001, -135, 90)
                Line((-0.565685425, -7.046075908), (-1.181066017, -6.430695316))
                CenterArc((-1.0749999999, -6.3246292989), 0.1499999999, 180, 45)
                Line((-1.2249999998, -6.3246292989), (-1.2249999998, -5.6034271249))
                Line((-1.2249999998, -5.6034271249), (-1.6034271238, -5.2250000009))
                Line((-1.6034271238, -5.2250000009), (-2.3246292978, -5.2250000009))
                CenterArc((-2.3246292978, -5.075000001), 0.1499999999, -134.9999999973, 44.9999999973)
                Line((-2.4306953149, -5.1810660181), (-3.0460759044, -4.5656854286))
                CenterArc((-2.4803904794, -4.0000000036), 0.8000000001, 135, 90)
                Line((-3.0460759044, -3.4343145786), (-2.4306953099, -2.8189339841))
                CenterArc((-2.3246292928, -2.9250000012), 0.1499999999, 90, 45)
                Line((-2.3246292928, -2.7750000013), (-1.6034271188, -2.7750000013))
                Line((-1.6034271188, -2.7750000013), (-1.2249999948, -2.3965728773))
                Line((-1.2249999948, -2.3965728773), (-1.2249999948, -1.6753707033))
                CenterArc((-1.0749999949, -1.6753707033), 0.1499999999, 135, 45)
                Line((-1.181066012, -1.5693046862), (-0.5656854225, -0.9539240967))
                CenterArc((0.0000000025, -1.5196095217), 0.8000000001, 45, 90)
                Line((0.5656854275, -0.9539240967), (1.181066017, -1.5693046862))
                CenterArc((1.0749999999, -1.6753707033), 0.1499999999, 0, 45)
                Line((1.2249999998, -1.6753707033), (1.2249999998, -2.3965728773))
                Line((1.2249999998, -2.3965728773), (1.6034271238, -2.7750000013))
                Line((1.6034271238, -2.7750000013), (2.3246292978, -2.7750000013))
                CenterArc((2.3246292978, -2.9250000012), 0.1499999999, 45, 45)
                Line((2.4306953149, -2.8189339841), (3.0460759069, -3.4343145761))
                CenterArc((2.4803904819, -4.0000000011), 0.8000000001, -45, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.2249999998, 6.3246292967), (1.2249999998, 5.6034271227))
                Line((1.2249999998, 5.6034271227), (1.6034271238, 5.2249999987))
                Line((1.6034271238, 5.2249999987), (2.3246292978, 5.2249999987))
                CenterArc((2.3246292978, 5.0749999988), 0.1499999999, 45, 45)
                Line((2.4306953149, 5.1810660159), (3.0460759069, 4.5656854239))
                CenterArc((2.4803904819, 3.9999999989), 0.8000000001, -45, 90)
                Line((3.0460759069, 3.4343145739), (2.4306953149, 2.8189339819))
                CenterArc((2.3246292978, 2.924999999), 0.1499999999, -90, 45)
                Line((2.3246292978, 2.7749999991), (1.6034271238, 2.7749999991))
                Line((1.6034271238, 2.7749999991), (1.2249999998, 2.3965728751))
                Line((1.2249999998, 2.3965728751), (1.2249999998, 1.6753707011))
                CenterArc((1.0749999999, 1.6753707011), 0.1499999999, -45, 45)
                Line((1.181066017, 1.569304684), (0.565685425, 0.953924092))
                CenterArc((0, 1.519609517), 0.8000000001, -135, 90)
                Line((-0.565685425, 0.953924092), (-1.181066017, 1.569304684))
                CenterArc((-1.0749999999, 1.6753707011), 0.1499999999, 180, 45)
                Line((-1.2249999998, 1.6753707011), (-1.2249999998, 2.3965728751))
                Line((-1.2249999998, 2.3965728751), (-1.6034271238, 2.7749999991))
                Line((-1.6034271238, 2.7749999991), (-2.3246292978, 2.7749999991))
                CenterArc((-2.3246292978, 2.924999999), 0.1499999999, -135, 45)
                Line((-2.4306953149, 2.8189339819), (-3.0460759044, 3.4343145714))
                CenterArc((-2.4803904794, 3.9999999964), 0.8000000001, 135, 90)
                Line((-3.0460759044, 4.5656854214), (-2.4306953099, 5.1810660159))
                CenterArc((-2.3246292928, 5.0749999988), 0.1499999999, 90, 45)
                Line((-2.3246292928, 5.2249999987), (-1.6034271188, 5.2249999987))
                Line((-1.6034271188, 5.2249999987), (-1.2249999948, 5.6034271227))
                Line((-1.2249999948, 5.6034271227), (-1.2249999948, 6.3246292967))
                CenterArc((-1.0749999949, 6.3246292967), 0.1499999999, 135, 45)
                Line((-1.181066012, 6.4306953138), (-0.5656854225, 7.0460759033))
                CenterArc((0.0000000025, 6.4803904783), 0.8000000001, 45, 90)
                Line((0.5656854275, 7.0460759033), (1.181066017, 6.4306953138))
                CenterArc((1.0749999999, 6.3246292967), 0.1499999999, 0, 45)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.4943046839, -0.1060660172), (-1.5693046839, -1.1810660172))
                CenterArc((-1.675370701, -1.0750000001), 0.1499999999, -90, 45.0000000027)
                Line((-1.675370701, -1.225), (-2.324629299, -1.225))
                CenterArc((-2.324629299, -1.0750000001), 0.1499999999, -135.0000000027, 45.0000000027)
                Line((-2.4306953161, -1.1810660172), (-3.5056953161, -0.1060660172))
                CenterArc((-3.3996292991, -0.0000000002), 0.1499999997, 135, 90)
                Line((-3.5056953161, 0.1060660168), (-2.4306953161, 1.1810660168))
                CenterArc((-2.324629299, 1.0749999997), 0.1499999999, 90, 45)
                Line((-2.324629299, 1.2249999996), (-1.675370701, 1.2249999996))
                CenterArc((-1.675370701, 1.0749999996), 0.1499999999, 45, 45)
                Line((-1.5693046839, 1.1810660168), (-0.4943046839, 0.1060660168))
                CenterArc((-0.6003707009, -0.0000000002), 0.1499999997, -45, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.4943046839, 0.1060660168), (1.5693046839, 1.1810660168))
                CenterArc((1.675370701, 1.0749999997), 0.1499999999, 90, 45)
                Line((1.675370701, 1.2249999996), (2.324629299, 1.2249999996))
                CenterArc((2.324629299, 1.0749999996), 0.1499999999, 45, 45)
                Line((2.4306953161, 1.1810660168), (3.5056953161, 0.1060660168))
                CenterArc((3.3996292991, -0.0000000002), 0.1499999997, -45, 90)
                Line((3.5056953161, -0.1060660172), (2.4306953161, -1.1810660172))
                CenterArc((2.324629299, -1.0750000001), 0.1499999999, -90, 45)
                Line((2.324629299, -1.225), (1.675370701, -1.225))
                CenterArc((1.675370701, -1.0750000001), 0.1499999999, -135.0000000027, 45.0000000027)
                Line((1.5693046839, -1.1810660172), (0.4943046839, -0.1060660172))
                CenterArc((0.6003707009, -0.0000000002), 0.1499999997, 135, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=154
        extrude(amount=154)
    return part.part


# Description: This is a hexagonal prism or block with a diagonal planar cut through its interior, creating an asymmetrical wedge or chamfered geometry with contrasting light and dark faces.
def model_135872_a6ca0e40_0016():
    """Model: Slider (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.08, perimeter: 16.3
            with BuildLine():
                Line((1.15, -0.65), (-1.25, -0.65))
                Line((-1.25, -0.65), (-1.25, -4))
                Line((-1.25, -4), (1.15, -4))
                Line((3.55, -4), (1.15, -4))
                Line((3.55, -0.65), (3.55, -4))
                Line((1.15, -0.65), (3.55, -0.65))
            make_face()
        # OneSide extrude, distance=8.4
        extrude(amount=8.4)
    return part.part


# Description: This is a trapezoidal wedge or truncated prism with a rectangular base, slanted top surface, and triangulated internal geometry, featuring a tapered profile that transitions from a wider base to a narrower top edge.
def model_135896_ecae901d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.1830000376, perimeter: 25.2200000119
            with BuildLine():
                Line((-3.5300000015, 2.7750000015), (-3.5300000015, -2.7750000015))
                Line((-3.5300000015, -2.7750000015), (3.5300000015, -2.7750000015))
                Line((3.5300000015, -2.7750000015), (3.5300000015, 2.7750000015))
                Line((3.5300000015, 2.7750000015), (-3.5300000015, 2.7750000015))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


# Description: This is a circular disk or plate with an elliptical or slightly dished profile, featuring a smooth curved surface with a subtle mesh or textured pattern visible on the upper edge, suggesting it may be a thin-walled component or have internal ribbing.
def model_136015_20ead420_0001():
    """Model: pads"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 4.9969892127, perimeter: 7.9242676887
            with Locations((0, 4.69900015)):
                Circle(1.261186373)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a polyhedral geometric solid with a diamond-like or faceted crown shape, featuring multiple triangular and quadrilateral faces arranged symmetrically around a central structure with what appears to be horizontal slot features dividing the form.
def model_136128_831e37a6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.9684179638, perimeter: 7.9295991034
            with BuildLine():
                Line((-3.4637874588, 2.2813900947), (-4.9275749176, 0.2534877883))
                Line((-4.9275749176, 0.2534877883), (-2, 0.2534877883))
                Line((-2, 0.2534877883), (-3.4637874588, 2.2813900947))
            make_face()
            # Profile area: 5.8487841474, perimeter: 13.7186621014
            with BuildLine():
                Line((-4.9275749176, -0.0241416941), (0, -4))
                Line((-1.9909956092, -0.0196475848), (0, -4))
                Line((-4.9275749176, -0.0241416941), (-1.9909956092, -0.0196475848))
            make_face()
            # Profile area: 5.83737407, perimeter: 13.7873558002
            with BuildLine():
                Line((0, -4), (4.9973306836, -0.0361239717))
                Line((4.9973306836, -0.0361239717), (2.0520447926, -0.0361239717))
                Line((2.0520447926, -0.0361239717), (0, -4))
            make_face()
            # Profile area: 6.2817593534, perimeter: 11.4702979581
            with BuildLine():
                Line((-1.7806067826, -0.0018488113), (0, -3.5615967458))
                Line((1.7645801173, -0.0335531933), (0, -3.5615967458))
                Line((-1.7806067826, -0.0018488113), (1.7645801173, -0.0335531933))
            make_face()
            # Profile area: 3.5434217009, perimeter: 8.8483806321
            with BuildLine():
                Line((-0.0332732499, 2.2813900947), (-1.7806067826, 0.2534877883))
                Line((-1.7806067826, 0.2534877883), (1.7140602828, 0.2534877883))
                Line((1.7140602828, 0.2534877883), (-0.0332732499, 2.2813900947))
            make_face()
            # Profile area: 2.5629337951, perimeter: 7.5252523851
            with BuildLine():
                Line((3.5139511532, 1.9781510123), (2.0279023064, 0.2534877883))
                Line((2.0279023064, 0.2534877883), (5, 0.2534877883))
                Line((5, 0.2534877883), (3.5139511532, 1.9781510123))
            make_face()
            # Profile area: 2.5663258052, perimeter: 7.5302305262
            with BuildLine():
                Line((3.2637641394, 2.2813900947), (0.2897003295, 2.2813900947))
                Line((0.2897003295, 2.2813900947), (1.7767322344, 0.5555859632))
                Line((1.7767322344, 0.5555859632), (3.2637641394, 2.2813900947))
            make_face()
            # Profile area: 2.2439095636, perimeter: 7.0106963559
            with BuildLine():
                Line((-3.114278542, 2.2813900947), (-1.9268153641, 0.6363020031))
                Line((-1.9268153641, 0.6363020031), (-0.386267106, 2.2813900947))
                Line((-3.114278542, 2.2813900947), (-0.386267106, 2.2813900947))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a curved bracket or deflector component with an asymmetrical angular shape, featuring a central circular hole, blue surface panels, black ribbed reinforcement structures, and multiple angled flanges designed for structural support and assembly.
def model_136204_cd4e55ea_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 83.0081237521, perimeter: 52.9664110571
            with BuildLine():
                CenterArc((5, 0), 2.75, 90, 180)
                Line((5, 5), (5, 2.75))
                Line((-5, 5), (5, 5))
                Line((-5, -5), (-5, 5))
                Line((5, -5), (-5, -5))
                Line((5, -2.75), (5, -5))
            make_face()
            with BuildLine():
                EllipticalCenterArc((-3.0007960353, 2.8171456936), 2.2041182047, 0.7383597627, 0, 360, 45.8282991783)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with a solid dark gray body, an open mesh top end, and exposed mesh side panels, designed for fluid or air filtration applications.
def model_136206_3113969f_0001():
    """Model: Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, full_length=True, total=2
        extrude(amount=1, both=True)
    return part.part


# Description: This is a rectangular metal insert or cutting tool with an elongated prismatic body, featuring four equally-spaced rectangular cutting edges or flutes along its top surface and tapered end faces.
def model_136206_3113969f_0003():
    """Model: Plate (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.8584073464, perimeter: 42.5663706144
            with BuildLine():
                Line((-6, 1.5), (6, 1.5))
                Line((-6, -1.5), (-6, 1.5))
                Line((6, -1.5), (-6, -1.5))
                Line((6, 1.5), (6, -1.5))
            make_face()
            with BuildLine():
                CenterArc((4.5, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.5, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a kiteboarding kite with a curved, crescent-shaped profile featuring a blue ripstop fabric canopy with black struts and battens, a central bridle attachment point, and a control bar connection system.
def model_136206_911a4e4d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 175.469383848, perimeter: 109.430638586
            with BuildLine():
                CenterArc((0, 0), 11, -74.1733798681, 74.1733798681)
                Line((11, 0), (8, 2))
                Line((8, 2), (4, 3.5))
                Line((4, 3.5), (0, 4))
                Line((-4, 3.5), (0, 4))
                Line((-8, 2), (-4, 3.5))
                Line((-11, 0), (-8, 2))
                CenterArc((0, 0), 11, 180, 74.1733798681)
                CenterArc((0, -10.5830052443), 3, 90, 90)
                CenterArc((0, -10.5830052443), 3, 0, 90)
            make_face()
            with BuildLine():
                Line((0, -2.5830052443), (7, -2.5830052443))
                Line((7, -2.5830052443), (7, -6.5830052443))
                Line((7, -6.5830052443), (2, -6.5830052443))
                CenterArc((0, -6.5830052443), 2, 0, 90)
                CenterArc((0, -6.5830052443), 2, 90, 90)
                Line((-7, -6.5830052443), (-2, -6.5830052443))
                Line((-7, -2.5830052443), (-7, -6.5830052443))
                Line((0, -2.5830052443), (-7, -2.5830052443))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a blue plastic mounting bracket or support assembly featuring two angled upright wings with a curved base platform, designed to hold or secure a rectangular component between its vertical supports.
def model_136206_b333b31e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.7286076236, perimeter: 55.6381377126
            with BuildLine():
                CenterArc((-14.6109128802, 3.5000006033), 3.5000006033, -135, 45)
                Line((-14.6109128802, 0), (0, 0))
                Line((0, 0), (0, 1.5))
                Line((0, 1.5), (-4.0000009653, 1.5))
                CenterArc((-4.0000009653, 2), 0.5, 179.9999861736, 90.0000138264)
                Line((-4.5000009653, 2.0000001207), (-4.5, 5.9999995174))
                CenterArc((-6.5, 6), 2, -0.0000138264, 180.0000138195)
                Line((-8.5, 6), (-8.5, 2.0000006033))
                CenterArc((-9, 2.0000006033), 0.5, -90, 90)
                Line((-9, 1.5000006033), (-14.6109128802, 1.5000006033))
                CenterArc((-14.6109128802, 3.5000006033), 2, -135, 45)
                Line((-16.0251264425, 2.0857870409), (-18.9393394016, 5))
                Line((-20, 3.9393394016), (-18.9393394016, 5))
                Line((-17.0857870409, 1.0251264425), (-20, 3.9393394016))
            make_face()
        # Symmetric extrude, full_length=True, total=4
        extrude(amount=2, both=True)
    return part.part


# Description: This is a flat rectangular metal plate or bar with a slight trapezoidal shape, featuring a single small hole near the left end and angled edges at both ends, likely used as a mounting bracket or connector component.
def model_136288_6364ea63_0002():
    """Model: Flat piece"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.2379870669, perimeter: 33.0944687638
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (13, 0))
                Line((13, 0), (13, 2))
                Line((13, 2), (0, 2))
            make_face()
            with BuildLine():
                CenterArc((1.5, 1), 0.4925, 0, 180)
                CenterArc((1.5, 1), 0.4925, -180, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3810064665, perimeter: 2.5322343819
            with BuildLine():
                CenterArc((1.5, 1), 0.4925, -180, 180)
                Line((1.0075, 1), (1.9925, 1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved cylindrical duct or pipe component with a rectangular flanged section on the left side, featuring a smooth, rounded tubular body that transitions from a flat mounting surface to a curved, horizontal pipe section.
def model_136312_6a0f8b1b_0000():
    """Model: ?????? 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 37 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9734109472, perimeter: 21.8282203734
            with BuildLine():
                CenterArc((-0.150000003, 0.05), 0.05, 180, 90)
                Line((-0.05, 0), (-0.150000003, 0))
                CenterArc((-0.05, 0.05), 0.05, -90, 90)
                Line((0, 1.6715728753), (0, 0.05))
                CenterArc((-2, 1.6715728753), 2, 0, 45)
                Line((-1.0857864376, 3.5857864376), (-0.5857864376, 3.0857864376))
                CenterArc((-2.5, 2.1715728753), 2, 45, 90)
                Line((-4.4142135624, 3.0857864376), (-3.9142135624, 3.5857864376))
                CenterArc((-3, 1.6715728753), 2, 135, 45)
                Line((-5, 0.05), (-5, 1.6715728753))
                CenterArc((-4.95, 0.05), 0.05, 180, 90)
                Line((-4.8467584212, 0), (-4.95, 0))
                CenterArc((-4.8467584212, 0.05), 0.05, -90, 90)
                Line((-4.7967584212, 1.6715728753), (-4.7967584212, 0.05))
                CenterArc((-2.7967584212, 1.6715728753), 2, 135, 45)
                Line((-3.9125927745, 3.3841656467), (-4.2109719836, 3.0857864376))
                CenterArc((-2.4983792121, 1.9699520844), 2, 45, 90)
                Line((-0.7857864406, 3.0857864376), (-1.0841656497, 3.3841656467))
                CenterArc((-2.200000003, 1.6715728753), 2, 0, 45)
                Line((-0.200000003, 0.05), (-0.200000003, 1.6715728753))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a wing or aerodynamic fairing component with an elongated, streamlined shape featuring a curved upper surface, a flattened underside with radiating internal ribs or structural supports, and tapered ends for aerodynamic efficiency.
def model_136337_1351909b_0001():
    """Model: Light PCB Board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 1, 90, 180)
                CenterArc((0, 0), 1, -90, 90)
                CenterArc((0, 0), 1, 0, 90)
            make_face()
            # Profile area: 0.7351126494, perimeter: 5.295818364
            with BuildLine():
                CenterArc((0, 0), 1, 0, 90)
                Line((1, 0), (1.45, 0))
                Line((1.45, 0), (1.45, 0.25))
                Line((1.45, 0.25), (1.72, 0.61))
                CenterArc((1.6, 0.7), 0.15, 36.8698976458, 286.2602047083)
                Line((1.5639797387, 1), (1.72, 0.79))
                Line((1.5639797387, 1), (0, 1))
            make_face()
            # Profile area: 0.0392699082, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((1.6, 0.7), 0.15, 36.8698976458, 286.2602047083)
                CenterArc((1.6, 0.7), 0.15, -36.8698976458, 73.7397952917)
            make_face()
            with BuildLine():
                CenterArc((1.6, 0.7), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7351128586, perimeter: 5.2971740572
            with BuildLine():
                Line((1, 0), (1.45, 0))
                CenterArc((0, 0), 1, -90, 90)
                Line((1.5639797387, -1), (0, -1))
                Line((1.5639797387, -1), (1.7204054948, -0.7894567841))
                CenterArc((1.6000000099, -0.7), 0.1499999901, 36.8698973929, 286.5191306914)
                Line((1.45, -0.25), (1.7200000024, -0.6100000065))
                Line((1.45, 0), (1.45, -0.25))
            make_face()
            # Profile area: 0.0392698988, perimeter: 1.5707962644
            with BuildLine():
                CenterArc((1.6000000099, -0.7), 0.1499999901, 36.8698973929, 286.5191306914)
                CenterArc((1.6000000099, -0.7), 0.1499999901, -36.6109719158, 73.4808693086)
            make_face()
            with BuildLine():
                CenterArc((1.6000000099, -0.7), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical or toroidal bowl-shaped component with a flattened bottom, featuring a curved, mesh-textured upper surface that tapers toward the rim, resembling a strainer, filter, or acoustic deflector element.
def model_136337_1351909b_0005():
    """Model: Infrared Light"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.1, -0.7000000104)):
                Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a flat sheet metal parallelogram or trapezoidal bracket with a triangular internal reinforcement rib that connects two opposing corners, providing structural support and stiffness to the thin-walled component.
def model_136343_567984b9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 279.24, perimeter: 77
            with BuildLine():
                Line((0, 1.3), (0, 0))
                Line((0, 0), (24.1, 0))
                Line((24.1, 0), (24.1, 1.3))
                Line((24.1, 1.3), (23.1, 1.3))
                Line((23.1, 1.3), (23.1, 11.1))
                Line((23.1, 11.1), (24.1, 11.1))
                Line((24.1, 11.1), (24.1, 12.4))
                Line((24.1, 12.4), (0, 12.4))
                Line((0, 12.4), (0, 11.1))
                Line((0, 11.1), (1, 11.1))
                Line((1, 11.1), (1, 1.3))
                Line((1, 1.3), (0, 1.3))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a uniform thickness, featuring a slightly sloped/skewed geometry and clean edges with no holes, slots, or additional features.
def model_136355_b5fd1a59_0000():
    """Model: PCB Board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.505, perimeter: 12.3
            with BuildLine():
                Line((4.05, -2.1), (0, -2.1))
                Line((4.05, 0), (4.05, -2.1))
                Line((0, 0), (4.05, 0))
                Line((0, -2.1), (0, 0))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a polyhedron or truncated geometric solid with an irregular, faceted shape featuring multiple planar surfaces in dark navy and blue-gray tones, characterized by angular edges and triangulated face divisions.
def model_136355_b5fd1a59_0002():
    """Model: Pin Holder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0625, perimeter: 1
            with BuildLine():
                Line((0.25, -0.25), (0, -0.25))
                Line((0.25, 0), (0.25, -0.25))
                Line((0, 0), (0.25, 0))
                Line((0, -0.25), (0, 0))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a cylindrical rod or tube with a uniform circular cross-section, featuring a smooth, slightly tapered end at the top and a clean, finished appearance throughout its length.
def model_136355_b5fd1a59_0004():
    """Model: Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0025, perimeter: 0.2
            with BuildLine():
                Line((0.05, -0.05), (0, -0.05))
                Line((0.05, 0), (0.05, -0.05))
                Line((0, 0), (0.05, 0))
                Line((0, -0.05), (0, 0))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)
    return part.part


# Description: This is an elliptical or oval-shaped structural panel with a curved surface featuring multiple internal radial ribs or reinforcing struts that extend from the center to the perimeter edge.
def model_136485_5ef7e95a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a curved rectangular duct or channel component with a tapered, trapezoidal cross-section featuring a textured/ribbed surface on one side and smooth surfaces on the others, appearing to be an air intake or ventilation duct with an angled, aerodynamic design.
def model_136499_954c9245_0000():
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
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 24 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5425841335, perimeter: 2.8950999467
            with BuildLine():
                Line((0.3703398355, 0.9999999876), (0.2709924359, 1))
                _nurbs_edge([(0.2709924359, 1), (0.2685243834, 0.999841886), (0.2455657467, 0.9982807031), (0.2016729489, 0.9936965358), (0.137540737, 0.9821928805), (0.0632752453, 0.9572952331), (0.0174609368, 0.9209011508), (0.0028355411, 0.88731333), (0, 0.8626830593), (0, 0.849999981)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2939690685, 0.2939690685, 0.2939690685, 0.2939690685, 0.2939690685, 0.2939690685, 0.3, 0.35, 0.4, 0.45, 0.498901999, 0.498901999, 0.498901999, 0.498901999, 0.498901999, 0.498901999], 5)
                _nurbs_edge([(0, 0.849999981), (0, 0.8497152067), (0.0000328936, 0.8364507397), (0.0031130695, 0.8091197041), (0.0147561834, 0.765476563), (0.035248281, 0.7036137991), (0.0609047432, 0.6234125871), (0.0819676569, 0.542313138), (0.0984758057, 0.4619720246), (0.1117919586, 0.3835562223), (0.1231288753, 0.3077820861), (0.1331129458, 0.2350451575), (0.1403067752, 0.1794153164), (0.145306081, 0.1391452196), (0.1484644738, 0.1129412746), (0.1500000022, 0.1000000015)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.498901999, 0.498901999, 0.498901999, 0.498901999, 0.498901999, 0.498901999, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0.1500000022, 0.1000000015), (0.3703400226, 0))
                Line((0.590680043, 0.1000000015), (0.3703400226, 0))
                _nurbs_edge([(0.4696876093, 1), (0.4721556619, 0.999841886), (0.4951142985, 0.9982807031), (0.5390070963, 0.9936965358), (0.6031393082, 0.9821928805), (0.6778027038, 0.9571618351), (0.7352044822, 0.9113332473), (0.7481610204, 0.8512101155), (0.7309070269, 0.7805200383), (0.7054317642, 0.7036137991), (0.679775302, 0.6234125871), (0.6587123884, 0.542313138), (0.6422042396, 0.4619720246), (0.6288880867, 0.3835562223), (0.61755117, 0.3077820861), (0.6075670994, 0.2350451575), (0.60037327, 0.1794153164), (0.5953739642, 0.1391452196), (0.5922155715, 0.1129412746), (0.590680043, 0.1000000015)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2939690685, 0.2939690685, 0.2939690685, 0.2939690685, 0.2939690685, 0.2939690685, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0.4696876093, 1), (0.3703398355, 0.9999999876))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a long, flat rectangular structural truss panel with a parallelogram cross-bracing lattice pattern featuring multiple diagonal triangular openings throughout its length, designed for lightweight structural support or framing applications.
def model_136562_bdd2c987_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59.0102432946, perimeter: 201.5001641581
            with BuildLine():
                Line((20.5, 2.5), (25, 2.5))
                Line((20, 2.5), (20.5, 2.5))
                Line((16, 2.5), (20, 2.5))
                Line((15.5, 2.5), (16, 2.5))
                Line((11.5, 2.5), (15.5, 2.5))
                Line((11, 2.5), (11.5, 2.5))
                Line((7, 2.5), (11, 2.5))
                Line((6.5, 2.5), (7, 2.5))
                Line((2.5, 2.5), (6.5, 2.5))
                Line((-2.5, 2.5), (2.5, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
                Line((2, -2.5), (-2.5, -2.5))
                Line((2.5, -2.5), (2, -2.5))
                Line((6.5, -2.5), (2.5, -2.5))
                Line((7, -2.5), (6.5, -2.5))
                Line((11, -2.5), (7, -2.5))
                Line((11.5, -2.5), (11, -2.5))
                Line((15.5, -2.5), (11.5, -2.5))
                Line((16, -2.5), (15.5, -2.5))
                Line((20, -2.5), (16, -2.5))
                Line((20.5, -2.5), (20, -2.5))
                Line((25, -2.5), (20.5, -2.5))
                Line((25, 2.5), (25, -2.5))
            make_face()
            with BuildLine():
                Line((16.6949747468, -1.6585786438), (19.6585786438, 1.3050252532))
                CenterArc((19.8, 1.1636038969), 0.2, 0, 135)
                Line((20, -1.8), (20, 1.1636038969))
                CenterArc((19.8, -1.8), 0.2, -90, 90)
                Line((16.8363961031, -2), (19.8, -2))
                CenterArc((16.8363961031, -1.8), 0.2, 135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((20.7, 1.8), 0.2, 90, 90)
                Line((23.6636038969, 2), (20.7, 2))
                CenterArc((23.6636038969, 1.8), 0.2, -45, 135)
                Line((20.8414213562, -1.3050252532), (23.8050252532, 1.6585786438))
                CenterArc((20.7, -1.1636038969), 0.2, 180, 135)
                Line((20.5, 1.8), (20.5, -1.1636038969))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((12.1949747468, -1.6585786438), (15.1585786438, 1.3050252532))
                CenterArc((15.3, 1.1636038969), 0.2, 0, 135)
                Line((15.5, -1.8), (15.5, 1.1636038969))
                CenterArc((15.3, -1.8), 0.2, -90, 90)
                Line((12.3363961031, -2), (15.3, -2))
                CenterArc((12.3363961031, -1.8), 0.2, 135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((7.6949747468, -1.6585786438), (10.6585786438, 1.3050252532))
                CenterArc((10.8, 1.1636038969), 0.2, 0, 135)
                Line((11, -1.8), (11, 1.1636038969))
                CenterArc((10.8, -1.8), 0.2, -90, 90)
                Line((7.8363961031, -2), (10.8, -2))
                CenterArc((7.8363961031, -1.8), 0.2, 135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.1949747468, -1.6585786438), (6.1585786438, 1.3050252532))
                CenterArc((6.3, 1.1636038969), 0.2, 0, 135)
                Line((6.5, -1.8), (6.5, 1.1636038969))
                CenterArc((6.3, -1.8), 0.2, -90, 90)
                Line((3.3363961031, -2), (6.3, -2))
                CenterArc((3.3363961031, -1.8), 0.2, 135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((21.1949747468, -1.6585786438), (24.1585786438, 1.3050252532))
                CenterArc((24.3, 1.1636038969), 0.2, 0, 135)
                Line((24.5, -1.8), (24.5, 1.1636038969))
                CenterArc((24.3, -1.8), 0.2, -90, 90)
                Line((21.3363961031, -2), (24.3, -2))
                CenterArc((21.3363961031, -1.8), 0.2, 135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((16.2, -1.1636038969), 0.2, 180, 135)
                Line((16, 1.8), (16, -1.1636038969))
                CenterArc((16.2, 1.8), 0.2, 90, 90)
                Line((19.1636038969, 2), (16.2, 2))
                CenterArc((19.1636038969, 1.8), 0.2, -45, 135)
                Line((16.3414213562, -1.3050252532), (19.3050252532, 1.6585786438))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.7, -1.1636038969), 0.2, 180, 135)
                Line((11.5, 1.8), (11.5, -1.1636038969))
                CenterArc((11.7, 1.8), 0.2, 90, 90)
                Line((14.6636038969, 2), (11.7, 2))
                CenterArc((14.6636038969, 1.8), 0.2, -45, 135)
                Line((11.8414213562, -1.3050252532), (14.8050252532, 1.6585786438))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.2, -1.1636038969), 0.2, 180, 135)
                Line((7, 1.8), (7, -1.1636038969))
                CenterArc((7.2, 1.8), 0.2, 90, 90)
                Line((10.1636038969, 2), (7.2, 2))
                CenterArc((10.1636038969, 1.8), 0.2, -45, 135)
                Line((7.3414213562, -1.3050252532), (10.3050252532, 1.6585786438))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.3050252532, -1.6585786438), (1.6585786438, 1.3050252532))
                CenterArc((1.8, 1.1636038969), 0.2, 0, 135)
                Line((2, -1.8), (2, 1.1636038969))
                CenterArc((1.8, -1.8), 0.2, -90, 90)
                Line((-1.1636038969, -2), (1.8, -2))
                CenterArc((-1.1636038969, -1.8), 0.2, 135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.7, -1.1636038969), 0.2, 180, 135)
                Line((2.5, 1.8), (2.5, -1.1636038969))
                CenterArc((2.7, 1.8), 0.2, 90, 90)
                Line((5.6636038969, 2), (2.7, 2))
                CenterArc((5.6636038969, 1.8), 0.2, -45, 135)
                Line((2.8414213562, -1.3050252532), (5.8050252532, 1.6585786438))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.1636038969, 2), (-1.8, 2))
                CenterArc((1.1636038969, 1.8), 0.2, -45, 135)
                Line((-1.6585786438, -1.3050252532), (1.3050252532, 1.6585786438))
                CenterArc((-1.8, -1.1636038969), 0.2, 180, 135)
                Line((-2, 1.8), (-2, -1.1636038969))
                CenterArc((-1.8, 1.8), 0.2, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with an oval or elliptical cross-section, featuring a seamless curved body with a fine mesh or screen pattern covering its surface.
def model_136627_98da0c2f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.3107499284, perimeter: 41.8931380356
            with BuildLine():
                CenterArc((0, 0), 3.556, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.1115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a trapezoidal profile, featuring angled side faces and a beveled or chamfered edge on one end, commonly used as a structural support component or bracket.
def model_136640_16741d62_0000():
    """Model: leuning klein"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 32, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1500, perimeter: 170
            with BuildLine():
                Line((185, 232.5689900082), (125, 232.5689900082))
                Line((185, 232.5689900082), (185, 257.5689900082))
                Line((185, 257.5689900082), (125, 257.5689900082))
                Line((125, 257.5689900082), (125, 232.5689900082))
            make_face()
        # OneSide extrude, distance=22.5
        extrude(amount=22.5)
    return part.part


# Description: This is a trapezoidal or wedge-shaped structural component with an asymmetrical geometry, featuring a tapered profile, angular faces, and a hollowed or recessed underside, likely designed as a bracket, support, or connector part.
def model_136653_11d77223_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1260, perimeter: 144
            with BuildLine():
                Line((-23.5792192991, 34.5794578764), (18.4207807009, 34.5794578764))
                Line((-23.5792192991, 4.5794578764), (-23.5792192991, 34.5794578764))
                Line((18.4207807009, 4.5794578764), (-23.5792192991, 4.5794578764))
                Line((18.4207807009, 34.5794578764), (18.4207807009, 4.5794578764))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: A flat, elongated parallelogram-shaped plate or panel with a slight 3D depth, featuring a beveled or chamfered edge on the left side and a smooth, tapered profile.
def model_136716_076bbbb3_0006():
    """Model: Ribbon"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8, perimeter: 4.2
            with BuildLine():
                Line((1.6, -0.5), (0, -0.5))
                Line((1.6, 0), (1.6, -0.5))
                Line((0, 0), (1.6, 0))
                Line((0, -0.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a cylindrical barrel or cup-shaped container with a curved, tapered top rim and vertical ribbed or fluted surface detailing on the exterior walls.
def model_136800_c5e4d711_0000():
    """Model: Untitled v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a cylindrical tube or sleeve with a mesh or perforated grid panel on one end and a flanged base with fins or louvers at the opposite end, appearing to be an air intake or exhaust component.
def model_136821_0f4b88d0_0007():
    """Model: keep plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 189.7807844457, perimeter: 84.9390479769
            with BuildLine():
                CenterArc((0, 9.1333076528), 22, -100.4756816964, 20.9513633928)
                Line((4, -12.5), (4, 12.5))
                CenterArc((0, -9.1333076528), 22, 79.5243183036, 20.9513633928)
                Line((-4, 12.5), (-4, -12.5))
            make_face()
            with BuildLine():
                CenterArc((0, 7.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -7.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a hexagonal or rectangular prism-shaped mechanical component with a faceted, angular geometry featuring multiple triangular faces and internal geometric subdivisions, appearing to be a structural or connector part with a complex faceted surface design.
def model_136834_9ebedb8b_0006():
    """Model: battery 2.0 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 65.8, perimeter: 37.4
            with BuildLine():
                Line((-7, 0), (-7, -4.7))
                Line((-7, -4.7), (7, -4.7))
                Line((7, 0), (7, -4.7))
                Line((-7, 0), (7, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a heat sink or cooling fin assembly with an elongated rectangular body featuring multiple parallel cooling fins along its length and mounting flanges or tabs protruding from the sides at regular intervals.
def model_136886_3194fe8e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 114 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((36, 0), (40, 0))
                Line((40, 0), (40, 2))
                Line((40, 2), (36, 2))
                Line((36, 2), (36, 0))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((24, 0), (28, 0))
                Line((28, 0), (28, 2))
                Line((28, 2), (24, 2))
                Line((24, 2), (24, 0))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((40, -12), (40, -8))
                Line((42, -12), (40, -12))
                Line((42, -8), (42, -12))
                Line((40, -8), (42, -8))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((12, 0), (16, 0))
                Line((16, 0), (16, 2))
                Line((16, 2), (12, 2))
                Line((12, 2), (12, 0))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((0, 0), (4, 0))
                Line((4, 0), (4, 2))
                Line((4, 2), (0, 2))
                Line((0, 2), (0, 0))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((0, -1), (0, -5))
                Line((-2, -1), (0, -1))
                Line((-2, -5), (-2, -1))
                Line((0, -5), (-2, -5))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((0, -13), (0, -17))
                Line((-2, -13), (0, -13))
                Line((-2, -17), (-2, -13))
                Line((0, -17), (-2, -17))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((40, -20), (42, -20))
                Line((40, -24), (40, -20))
                Line((42, -24), (40, -24))
                Line((42, -20), (42, -24))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((4, -25), (0, -25))
                Line((0, -25), (0, -27))
                Line((0, -27), (4, -27))
                Line((4, -27), (4, -25))
            make_face()
            # Profile area: 920, perimeter: 170
            with BuildLine():
                Line((40, -18), (40, -20))
                Line((38, -18), (40, -18))
                Line((38, -14), (38, -18))
                Line((40, -14), (38, -14))
                Line((40, -12), (40, -14))
                Line((40, -12), (40, -8))
                Line((40, -6), (40, -8))
                Line((38, -6), (40, -6))
                Line((38, -2), (38, -6))
                Line((40, -2), (38, -2))
                Line((40, 0), (40, -2))
                Line((36, 0), (40, 0))
                Line((34, 0), (36, 0))
                Line((34, 0), (34, -2))
                Line((34, -2), (30, -2))
                Line((30, -2), (30, 0))
                Line((28, 0), (30, 0))
                Line((24, 0), (28, 0))
                Line((22, 0), (24, 0))
                Line((22, 0), (22, -2))
                Line((22, -2), (18, -2))
                Line((18, -2), (18, 0))
                Line((16, 0), (18, 0))
                Line((12, 0), (16, 0))
                Line((10, 0), (12, 0))
                Line((10, 0), (10, -2))
                Line((10, -2), (6, -2))
                Line((6, -2), (6, 0))
                Line((4, 0), (6, 0))
                Line((0, 0), (4, 0))
                Line((0, -1), (0, 0))
                Line((0, -1), (0, -5))
                Line((0, -7), (0, -5))
                Line((2, -7), (0, -7))
                Line((2, -11), (2, -7))
                Line((0, -11), (2, -11))
                Line((0, -13), (0, -11))
                Line((0, -13), (0, -17))
                Line((0, -19), (0, -17))
                Line((2, -19), (0, -19))
                Line((2, -23), (2, -19))
                Line((0, -23), (2, -23))
                Line((0, -25), (0, -23))
                Line((4, -25), (0, -25))
                Line((6, -25), (4, -25))
                Line((6, -25), (6, -23))
                Line((6, -23), (10, -23))
                Line((10, -23), (10, -25))
                Line((12, -25), (10, -25))
                Line((16, -25), (12, -25))
                Line((18, -25), (16, -25))
                Line((18, -25), (18, -23))
                Line((18, -23), (22, -23))
                Line((22, -23), (22, -25))
                Line((24, -25), (22, -25))
                Line((28, -25), (24, -25))
                Line((30, -25), (28, -25))
                Line((30, -25), (30, -23))
                Line((30, -23), (34, -23))
                Line((34, -23), (34, -25))
                Line((36, -25), (34, -25))
                Line((40, -25), (36, -25))
                Line((40, -24), (40, -25))
                Line((40, -24), (40, -20))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((16, -25), (12, -25))
                Line((12, -25), (12, -27))
                Line((12, -27), (16, -27))
                Line((16, -27), (16, -25))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((28, -25), (24, -25))
                Line((24, -25), (24, -27))
                Line((24, -27), (28, -27))
                Line((28, -27), (28, -25))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((40, -25), (36, -25))
                Line((36, -25), (36, -27))
                Line((36, -27), (40, -27))
                Line((40, -27), (40, -25))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped solid with an irregular pentagonal or trapezoidal cross-section, featuring multiple planar faces and internal triangulated geometry, appearing to be a structural component or mounting bracket with no obvious holes or slots.
def model_136886_3aa46890_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.09, perimeter: 1.2
            with BuildLine():
                Line((0.15, -0.15), (-0.15, -0.15))
                Line((0.15, 0.15), (0.15, -0.15))
                Line((-0.15, 0.15), (0.15, 0.15))
                Line((-0.15, -0.15), (-0.15, 0.15))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical rod or tube with a slightly tapered design, featuring rounded ends and a smooth, uniform diameter along its length.
def model_136900_4fe212e6_0001():
    """Model: ShortClosetRod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6950376144, perimeter: 18.4728789624
            with BuildLine():
                CenterArc((0, 0), 1.67005, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=30.48
        extrude(amount=30.48)
    return part.part


# Description: This is a flat parallelogram plate or shim with a skewed rectangular shape, featuring clean edges and a uniform thickness, commonly used as a spacer, shim, or structural component in assemblies.
def model_136900_4fe212e6_0002():
    """Model: FlatShelf v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3425.7996, perimeter: 241.3
            with BuildLine():
                Line((74.93, -45.72), (0, -45.72))
                Line((74.93, 0), (74.93, -45.72))
                Line((0, 0), (74.93, 0))
                Line((0, -45.72), (0, 0))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a straight cylindrical rod or shaft with a simple, uniform circular cross-section and tapered or slightly pointed ends.
def model_136900_4fe212e6_0005():
    """Model: LongClosetRod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6950376144, perimeter: 18.4728789624
            with BuildLine():
                CenterArc((0, 0), 1.67005, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=121.92
        extrude(amount=121.92)
    return part.part


# Description: This is a dark navy elongated rectangular prism or bar with a slightly curved or tapered profile, featuring a long, narrow form with rounded edges and a subtle 3D depth that gives it a sleek, blade-like appearance.
def model_136900_4fe212e6_0010():
    """Model: Vertical Panel v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9187.0784, perimeter: 490.0784506514
            with BuildLine():
                Line((0, 0), (0, 203.2))
                Line((0, 203.2), (-35.56, 203.2))
                Line((-45.72, 182.88), (-35.56, 203.2))
                Line((-45.72, 0), (-45.72, 182.88))
                Line((0, 0), (-45.72, 0))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a cylindrical mesh or perforated tube with a slightly tapered top end and a solid body, commonly used as a filter, screen, or strainer component.
def model_136913_72e7b367_0000():
    """Model: Handbroms bord skruv v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a toroidal elastomer O-ring seal with a circular cross-section, designed for static or dynamic sealing applications in fluid or gas systems.
def model_136963_ff9b11e8_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch3 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.002589496, perimeter: 57.5479137456
            with BuildLine():
                EllipticalCenterArc((0, 0), 5.6463758526, 3.7176720464, 0, 360, 0.2209171214)
            make_face()
            with BuildLine():
                EllipticalCenterArc((0, 0), 5.3608704003, 3.3811226685, 0, 360, 0.2209171214)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a composite bracket or mounting assembly featuring a large angled triangular plate on top with internal bracing, connected to a lower rectangular base structure with multiple protruding rectangular bosses or mounting feet.
def model_136964_8bb2b432_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3870960247, perimeter: 2.5400000811
            with BuildLine():
                Line((-0.2540000081, -1.5240000486), (0.2540000081, -1.5240000486))
                Line((-0.2540000081, -1.5240000486), (-0.2540000081, -2.286000073))
                Line((-0.2540000081, -2.286000073), (0.2540000081, -2.286000073))
                Line((0.2540000081, -2.286000073), (0.2540000081, -1.5240000486))
            make_face()
            # Profile area: 7.7419204942, perimeter: 13.2080004215
            with BuildLine():
                Line((-2.5400000811, 0), (-2.5400000811, -1.5240000486))
                Line((-2.5400000811, -1.5240000486), (-0.2540000081, -1.5240000486))
                Line((-0.2540000081, -1.5240000486), (0.2540000081, -1.5240000486))
                Line((0.2540000081, -1.5240000486), (2.5400000811, -1.5240000486))
                Line((2.5400000811, -1.5240000486), (2.5400000811, 0))
                Line((2.5400000811, 0), (-2.5400000811, 0))
            make_face()
            # Profile area: 25.8064016472, perimeter: 24.5284105765
            with BuildLine():
                Line((-2.5400000811, 0), (-5.0800001621, 0))
                Line((2.5400000811, 0), (-2.5400000811, 0))
                Line((5.0800001621, 0), (2.5400000811, 0))
                Line((0, 5.0800001621), (5.0800001621, 0))
                Line((-5.0800001621, 0), (0, 5.0800001621))
            make_face()
        # OneSide extrude, distance=1.524
        extrude(amount=1.524)
    return part.part


# Description: This is a torus or ring-shaped seal/gasket characterized by a circular cross-section with a smooth, curved toroidal geometry and a textured or patterned surface finish.
def model_136980_9660c50c_0001():
    """Model: outer ring 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 333.7942194439, perimeter: 267.0353755551
            with BuildLine():
                CenterArc((0, 0), 22.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 20, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a conveyor or drive belt featuring an elliptical/oval torus shape with a textured ribbed surface on the outer edge, designed to transmit power or move materials in machinery.
def model_136980_9660c50c_0002():
    """Model: glass ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 263.304734279, perimeter: 234.0486526924
            with BuildLine():
                CenterArc((0, 0), 19.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 17.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a rubber or elastomeric seal ring with a toroidal (doughnut-like) shape, featuring a smooth outer surface and a hollow center opening, commonly used as a gasket, O-ring, or vibration isolator in mechanical assemblies.
def model_136980_9660c50c_0003():
    """Model: large ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 706.8583470577, perimeter: 282.7433388231
            with BuildLine():
                CenterArc((0, 0), 25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 20, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a trapezoidal cross-section, featuring angled faces and a predominantly rectangular form with beveled or chamfered edges on one end.
def model_136994_22d5d740_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 600, perimeter: 100
            with BuildLine():
                Line((30, -20), (0, -20))
                Line((30, 0), (30, -20))
                Line((0, 0), (30, 0))
                Line((0, -20), (0, 0))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a trapezoidal prism or wedge-shaped structural component with a slanted top surface, featuring a rectangular body that tapers in one direction with clean planar faces and sharp edges.
def model_136994_22d5d740_0001():
    """Model: key_lock"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 15), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14.85, perimeter: 15.6
            with BuildLine():
                Line((-6.3, 11.5), (-3, 11.5))
                Line((-6.3, 7), (-6.3, 11.5))
                Line((-3, 7), (-6.3, 7))
                Line((-3, 11.5), (-3, 7))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a parallelogram-shaped flat plate or base with a triangular reinforcement rib, featuring a trapezoidal top surface and a beveled or angled edge on one side for structural support or aesthetic purposes.
def model_136994_a3a2f50f_0008():
    """Model: top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -12.15, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 192, perimeter: 183
            with BuildLine():
                Line((-2.9901163479, 20.5544688721), (27.0098836521, 20.5544688721))
                Line((-2.9901163479, 0.5544688721), (-2.9901163479, 20.5544688721))
                Line((27.0098836521, 0.5544688721), (-2.9901163479, 0.5544688721))
                Line((27.0098836521, 20.5544688721), (27.0098836521, 0.5544688721))
            make_face()
            with BuildLine():
                Line((24.75, 18), (-0.75, 18))
                Line((24.75, 2), (24.75, 18))
                Line((-0.75, 2), (24.75, 2))
                Line((-0.75, 18), (-0.75, 2))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 408, perimeter: 83
            with BuildLine():
                Line((-0.75, 18), (-0.75, 2))
                Line((-0.75, 2), (24.75, 2))
                Line((24.75, 2), (24.75, 18))
                Line((24.75, 18), (-0.75, 18))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


# Description: This is a curved belt or band-like component with a bilobed (figure-8) cross-section, featuring a mesh-textured upper surface and solid dark lower surface, designed for flexible wrapping or containment applications.
def model_137088_d7fc9a5b_0001():
    """Model: Untitled v1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3887.5216810819, perimeter: 247.327804441
            with BuildLine():
                CenterArc((-20, -50.8645293625), 64.0663010835, 71.8095484661, 36.3809030677)
                CenterArc((-1.8968160298, -10), 43.033157317, 152.305444857, 55.3891102861)
                CenterArc((-20, 13.3363842287), 47.7288403171, -114.7736057986, 49.5472115971)
                CenterArc((20, 13.5480246323), 47.9210856448, -114.6675720961, 49.3351441921)
                CenterArc((1.7063570189, -10), 43.2018876065, -27.5771604343, 55.1543208687)
                CenterArc((20, -41.7143820742), 55.447067671, 68.8565394781, 42.2869210437)
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a black and blue polymer connector or clip with three curved arms extending from a central hub, featuring elongated slots or windows along each arm and rounded end caps, designed for fastening or securing components together.
def model_137098_0a45d1c8_0004():
    """Model: Clip"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6295093379, perimeter: 24.1048423376
            with BuildLine():
                Line((1.2, -0.3), (1.7, -0.3))
                CenterArc((1.7, 0), 0.3, -90, 180)
                Line((1.2, 0.3), (1.7, 0.3))
                CenterArc((1.2, 1.2), 0.9, -180, 90)
                Line((0.3, 1.7), (0.3, 1.2))
                CenterArc((0, 1.7), 0.3, 0, 180)
                Line((-0.3, 1.2), (-0.3, 1.7))
                CenterArc((-1.2, 1.2), 0.9, -90, 90)
                Line((-1.7, 0.3), (-1.2, 0.3))
                CenterArc((-1.6993243205, 0), 0.3000007609, 90.129045068, 179.741909864)
                Line((-1.7, -0.3), (-1.2, -0.3))
                CenterArc((-1.2, -1.1999970644), 0.8999970644, 0.0003363911, 89.9996636089)
                Line((-0.3000029356, -1.1999917804), (-0.3, -1.7))
                CenterArc((0, -1.7), 0.3, 180, 180)
                Line((0.3, -1.2), (0.3, -1.7))
                CenterArc((1.2, -1.2), 0.9, 90, 90)
            make_face()
            with BuildLine():
                CenterArc((0, -1.7), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.7, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.8, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 1.7), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.7, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.15
        extrude(amount=0.075, both=True)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform hollow core, featuring rounded ends and a slight taper, commonly used as a structural component or connector in mechanical assemblies.
def model_137098_0a45d1c8_0013():
    """Model: BLDC Motor Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # Symmetric extrude, full_length=True, total=2.2
        extrude(amount=1.1, both=True)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, slightly tapered or rounded at one end, featuring a smooth, featureless design without holes, slots, or flanges.
def model_137098_0a45d1c8_0014():
    """Model: Screw Servo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0452389342, perimeter: 0.7539822369
            Circle(0.12)
        # Symmetric extrude, full_length=True, total=3.5
        extrude(amount=1.75, both=True)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a simple cylindrical or prismatic body, featuring uniformly rounded ends and smooth, flat surfaces along its length.
def model_137098_0a45d1c8_0017():
    """Model: Stand Pipe"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=10
        extrude(amount=5, both=True)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, tapered slightly at the ends, rendered in dark gray with a 3D perspective view.
def model_137098_0a45d1c8_0018():
    """Model: Stand Pipe2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=16
        extrude(amount=8, both=True)
    return part.part


# Description: This is a cylindrical tube or sleeve with a smooth exterior surface and a slightly tapered or beveled top end.
def model_137098_0a45d1c8_0019():
    """Model: Stepper Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, full_length=True, total=2.2
        extrude(amount=1.1, both=True)
    return part.part


# Description: This is a hexagonal steel shaft or rod with a tapered or chamfered end, featuring a long, slender prismatic form with six flat sides and a pointed tip.
def model_137141_748596d0_0006():
    """Model: pin (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.00403225, perimeter: 0.254
            with BuildLine():
                Line((0.03175, -0.03175), (0.03175, 0.03175))
                Line((0.03175, 0.03175), (-0.03175, 0.03175))
                Line((-0.03175, 0.03175), (-0.03175, -0.03175))
                Line((-0.03175, -0.03175), (0.03175, -0.03175))
            make_face()
        # TwoSides extrude, along=0.889, against=-0.254
        extrude(amount=0.889)
        extrude(sk.sketch, amount=-0.254)
    return part.part


# Description: This is a curved plastic or composite bracket or mounting clip with a dark gray finish, featuring a smooth curved body with a flat rectangular mounting surface and textured grip area on one end.
def model_137211_d47bba3f_0001():
    """Model: Component2"""
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
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.535365078, perimeter: 10.295860336
            with BuildLine():
                _nurbs_edge([(6.0054250043, -7.8323526748), (7.0858594807, -7.0577483436), (7.6793570546, -5.9689704939), (7.7182944065, -4.8500351683), (7.5102821939, -4.3953402202), (7.2528395373, -4.2264273371), (6.9605375928, -4.4301614478), (6.7867608027, -4.6518289726), (6.850963688, -5.0705625825), (7.0408751589, -5.7256780654), (6.9745846499, -6.0782903937), (6.8669377267, -6.5599479766), (6.6109268622, -7.1584323486), (6.1977286381, -7.5478153944), (6.0565557626, -7.7490186174), (6.0422244495, -7.7647872153)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0909090909, 0.1818181818, 0.2727272727, 0.3636363636, 0.4545454545, 0.5454545455, 0.6363636364, 0.7272727273, 0.8181818182, 0.9090909091, 0.9822761953, 0.9822761953, 0.9822761953, 0.9822761953, 0.9822761953, 0.9822761953], 5)
                Line((6.0054250043, -7.8323526748), (6.0422244495, -7.7647872153))
            make_face()
            with BuildLine():
                CenterArc((7.250042389, -4.8264447991), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.2934104441, -5.6818720954), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.016
        extrude(amount=1.016)
    return part.part


# Description: This is a 3D sheet metal part with an angular, zigzag or chevron-like shape, consisting of two rectangular flanges connected at an offset angle, resembling a bent bracket or corner support with sharp edges and flat surfaces.
def model_137403_81c69c1f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 122.42685, perimeter: 51.8984166942
            with BuildLine():
                Line((0, 0), (0, 6.1))
                Line((0, 0), (11.999, -0.1))
                Line((11.999, 13.9), (11.999, -0.1))
                Line((5.764, 13.9), (11.999, 13.9))
                Line((5.764, 6.1), (5.764, 13.9))
                Line((0, 6.1), (5.764, 6.1))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a hexagonal or polygonal prism-based component with an angular, faceted geometry featuring a hollow or recessed cavity on one face and internal structural ribbing or webbing.
def model_137426_1d583698_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 225, perimeter: 60
            with BuildLine():
                Line((-7.5, -7.5), (-22.5, -7.5))
                Line((-7.5, 7.5), (-7.5, -7.5))
                Line((-22.5, 7.5), (-7.5, 7.5))
                Line((-22.5, -7.5), (-22.5, 7.5))
            make_face()
        # TwoSides extrude, along=17, against=-8
        extrude(amount=17)
        extrude(sk.sketch, amount=-8)
    return part.part


# Description: This is a cross-shaped or plus-sign structural component with two perpendicular rectangular bars of equal width that intersect at their centers, featuring angled edges and a uniform thickness throughout.
def model_137445_368e129e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.5, perimeter: 25
            with BuildLine():
                Line((7.0402090963, -4.1336582091), (-2.4597909037, -4.1336582091))
                Line((7.0402090963, -4.1336582091), (7.0402090963, -1.1336582091))
                Line((-2.4597909037, -1.1336582091), (7.0402090963, -1.1336582091))
                Line((-2.4597909037, -4.1336582091), (-2.4597909037, -1.1336582091))
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((10.0402090963, -4.1336582091), (7.0402090963, -4.1336582091))
                Line((10.0402090963, -1.1336582091), (10.0402090963, -4.1336582091))
                Line((7.0402090963, -1.1336582091), (10.0402090963, -1.1336582091))
                Line((7.0402090963, -4.1336582091), (7.0402090963, -1.1336582091))
            make_face()
            # Profile area: 28.5, perimeter: 25
            with BuildLine():
                Line((10.0402090963, -1.1336582091), (10.0402090963, -4.1336582091))
                Line((19.5402090963, -4.1336582091), (10.0402090963, -4.1336582091))
                Line((19.5402090963, -1.1336582091), (19.5402090963, -4.1336582091))
                Line((10.0402090963, -1.1336582091), (19.5402090963, -1.1336582091))
            make_face()
            # Profile area: 28.5, perimeter: 25
            with BuildLine():
                Line((7.0402090963, -1.1336582091), (10.0402090963, -1.1336582091))
                Line((10.0402090963, 8.3663417909), (10.0402090963, -1.1336582091))
                Line((7.0402090963, 8.3663417909), (10.0402090963, 8.3663417909))
                Line((7.0402090963, -1.1336582091), (7.0402090963, 8.3663417909))
            make_face()
            # Profile area: 28.5, perimeter: 25
            with BuildLine():
                Line((7.0402090963, -13.6336582091), (7.0402090963, -4.1336582091))
                Line((10.0402090963, -13.6336582091), (7.0402090963, -13.6336582091))
                Line((10.0402090963, -4.1336582091), (10.0402090963, -13.6336582091))
                Line((10.0402090963, -4.1336582091), (7.0402090963, -4.1336582091))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical sleeve or tube with a rounded/domed end cap on one side and open or recessed features on the opposite end, designed as a connector or housing component.
def model_137445_4395e806_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2218788767, perimeter: 3.0988669935
            with BuildLine():
                CenterArc((0, 0), 0.3182, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a 3D cross or plus-shaped connector/joint featuring two perpendicular cylindrical bars with rounded ends that intersect at their centers, commonly used as a structural link, coupling, or mounting component.
def model_137448_0f2fd70e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 185 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2146018653, perimeter: 3.5707964098
            with BuildLine():
                Line((-1.0000000149, -2.0000000298), (-1, -1))
                Line((-1, -1), (-2.0000000298, -1.0000000149))
                CenterArc((-2.0000000298, -2.0000000298), 1.0000000149, 0, 90)
            make_face()
            # Profile area: 0.2146018653, perimeter: 3.5707964098
            with BuildLine():
                Line((2.0000000298, -1.0000000149), (1, -1))
                Line((1, -1), (1.0000000149, -2.0000000298))
                CenterArc((2.0000000298, -2.0000000298), 1.0000000149, 90, 90)
            make_face()
            # Profile area: 0.2146018653, perimeter: 3.5707964098
            with BuildLine():
                Line((1.0000000149, 2.0000000298), (1, 1))
                Line((1, 1), (2.0000000298, 1.0000000149))
                CenterArc((2.0000000298, 2.0000000298), 1.0000000149, 180, 90)
            make_face()
            # Profile area: 0.2146018653, perimeter: 3.5707964098
            with BuildLine():
                Line((-2.0000000298, 1.0000000149), (-1, 1))
                Line((-1, 1), (-1.0000000149, 2.0000000298))
                CenterArc((-2.0000000298, 2.0000000298), 1.0000000149, -90, 90)
            make_face()
            # Profile area: 19.2782355109, perimeter: 27.3827427359
            with BuildLine():
                Line((-1, 1), (-1.0000000149, 2.0000000298))
                Line((-1, 1), (1, 1))
                Line((1.0000000149, 2.0000000298), (1, 1))
                Line((1, 10), (1.0000000149, 2.0000000298))
                CenterArc((0, 10), 1, -0.0000000001, 90.0000000001)
                CenterArc((0, 10), 1, 90, 90.0000000001)
                Line((-1.0000000149, 2.0000000298), (-1, 10))
            make_face()
            with BuildLine():
                CenterArc((-0.4242635565, 9.5757354191), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4242656052, 9.5757374678), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4242635565, 10.4242645809), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.4242635565, 10.4242645809), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 4.5), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.2782355109, perimeter: 27.3827427359
            with BuildLine():
                Line((-1, -1), (-2.0000000298, -1.0000000149))
                Line((-1, -1), (-1, 1))
                Line((-2.0000000298, 1.0000000149), (-1, 1))
                Line((-10.0000000624, 1), (-2.0000000298, 1.0000000149))
                CenterArc((-10, 0), 1, 90.0000035748, 89.999991274)
                CenterArc((-10, 0), 1, 179.9999948489, 90.0000008084)
                Line((-2.0000000298, -1.0000000149), (-10.0000000758, -1))
            make_face()
            with BuildLine():
                CenterArc((-4.5, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.424264075, 0.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.424264075, -0.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.575735925, -0.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.575735925, 0.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.2782355109, perimeter: 27.3827427359
            with BuildLine():
                Line((1, -1), (1.0000000149, -2.0000000298))
                Line((1, -1), (-1, -1))
                Line((-1.0000000149, -2.0000000298), (-1, -1))
                Line((-1, -10.000000124), (-1.0000000149, -2.0000000298))
                CenterArc((0, -10), 1, -179.9999928977, 89.9999880681)
                CenterArc((0, -10), 1, -90.0000048296, 90.0000022726)
                Line((1.0000000149, -2.0000000298), (1, -10.0000000446))
            make_face()
            with BuildLine():
                CenterArc((0.424264075, -10.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.424264075, -10.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.424264075, -9.575735925), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.424264075, -9.575735925), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -4.5), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-1, 1), (1, 1))
                Line((-1, -1), (-1, 1))
                Line((1, -1), (-1, -1))
                Line((1, 1), (1, -1))
            make_face()
            # Profile area: 19.2782355109, perimeter: 27.3827427359
            with BuildLine():
                CenterArc((10, 0), 1, -89.9999995037, 89.9999995038)
                CenterArc((10, 0), 1, 0, 90.0000004962)
                Line((2.0000000298, 1.0000000149), (9.9999999913, 1))
                Line((1, 1), (2.0000000298, 1.0000000149))
                Line((1, 1), (1, -1))
                Line((2.0000000298, -1.0000000149), (1, -1))
                Line((10.0000000087, -1), (2.0000000298, -1.0000000149))
            make_face()
            with BuildLine():
                CenterArc((9.575735925, -0.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.424264075, -0.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.424264075, 0.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.575735925, 0.424264075), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a truncated polygonal solid with an irregular, roughly cubic or pentahedron-like shape featuring multiple flat faceted surfaces in varying shades of blue and dark gray, with some internal geometric divisions or edges visible across the faces.
def model_137605_b2c5f816_0000():
    """Model: Devil"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.25, perimeter: 10
            with BuildLine():
                Line((2.5, -2.5), (0, -2.5))
                Line((2.5, 0), (2.5, -2.5))
                Line((0, 0), (2.5, 0))
                Line((0, -2.5), (0, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a hollow rectangular box or container with an open top, featuring two internal vertical dividers or baffles that create three separate compartments within the structure.
def model_137724_20be6062_0002():
    """Model: test"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6082300165, perimeter: 44.0548667765
            with BuildLine():
                CenterArc((0.6, 0.6), 0.6, 180, 90)
                Line((2, 0), (0.6, 0))
                Line((7.4, 0), (2, 0))
                CenterArc((7.4, 0.6), 0.6, -90, 90)
                Line((8, 3.4), (8, 0.6))
                CenterArc((7.4, 3.4), 0.6, 0, 90)
                Line((0.6, 4), (7.4, 4))
                CenterArc((0.6, 3.4), 0.6, 90, 90)
                Line((0, 2), (0, 3.4))
                Line((0, 0.6), (0, 2))
            make_face()
            with BuildLine():
                Line((7.7, 3.4), (7.7, 0.6))
                CenterArc((7.4, 0.6), 0.3, -90, 90)
                Line((7.4, 0.3), (0.6, 0.3))
                CenterArc((0.6, 0.6), 0.3, 180, 90)
                Line((0.3, 0.6), (0.3, 3.4))
                CenterArc((0.6, 3.4), 0.3, 90, 90)
                Line((0.6, 3.7), (7.4, 3.7))
                CenterArc((7.4, 3.4), 0.3, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a rectangular aluminum extrusion or channel with a longitudinal slot running along its length, featuring a hollow core design typical of structural framing components.
def model_137724_20be6062_0003():
    """Model: back-foot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6082300165, perimeter: 44.0548667765
            with BuildLine():
                CenterArc((0.6, 0.6), 0.6, 180, 90)
                Line((2, 0), (0.6, 0))
                Line((7.4, 0), (2, 0))
                CenterArc((7.4, 0.6), 0.6, -90, 90)
                Line((8, 3.4), (8, 0.6))
                CenterArc((7.4, 3.4), 0.6, 0, 90)
                Line((0.6, 4), (7.4, 4))
                CenterArc((0.6, 3.4), 0.6, 90, 90)
                Line((0, 2), (0, 3.4))
                Line((0, 0.6), (0, 2))
            make_face()
            with BuildLine():
                Line((7.7, 3.4), (7.7, 0.6))
                CenterArc((7.4, 0.6), 0.3, -90, 90)
                Line((7.4, 0.3), (0.6, 0.3))
                CenterArc((0.6, 0.6), 0.3, 180, 90)
                Line((0.3, 0.6), (0.3, 3.4))
                CenterArc((0.6, 3.4), 0.3, 90, 90)
                Line((0.6, 3.7), (7.4, 3.7))
                CenterArc((7.4, 3.4), 0.3, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=41
        extrude(amount=41)
    return part.part


# Description: This is an extruded rectangular tube or channel with a longitudinal slot running along its length, featuring a hollow interior cavity and angled top edges, commonly used as a structural component or mounting rail.
def model_137837_9c9f163d_0000():
    """Model: TIE ROD"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 51.2, perimeter: 33.6
            with BuildLine():
                Line((4, 25.6), (0, 25.6))
                Line((0, 25.6), (0, 12.8))
                Line((0, 12.8), (4, 12.8))
                Line((4, 12.8), (4, 25.6))
            make_face()
            # Profile area: 51.2, perimeter: 33.6
            with BuildLine():
                Line((0, 12.8), (4, 12.8))
                Line((0, 12.8), (0, 0))
                Line((0, 0), (4, 0))
                Line((4, 0), (4, 12.8))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4)
    return part.part


# Description: This is a long hexagonal steel bar or shaft with a tapered end on one side and a flat end on the other, featuring a central longitudinal groove or slot running along its length.
def model_137837_9c9f163d_0002():
    """Model: PUSH BACK INSERTS"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((1.5, 10), (0, 10))
                Line((0, 10), (0, 5))
                Line((0, 5), (1.5, 5))
                Line((1.5, 5), (1.5, 10))
            make_face()
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((0, 5), (1.5, 5))
                Line((0, 5), (0, 0))
                Line((0, 0), (1.5, 0))
                Line((1.5, 0), (1.5, 5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


# Description: This is a thin, flat parallelogram-shaped plate or panel with a beveled or angled edge along one side, featuring a simple geometric form with no holes or complex features.
def model_137837_9c9f163d_0006():
    """Model: WEAR PLATE"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72, perimeter: 34
            with BuildLine():
                Line((8, -9), (0, -9))
                Line((8, 0), (8, -9))
                Line((8, 0), (0, 0))
                Line((0, -9), (0, 0))
            make_face()
            # Profile area: 216, perimeter: 68
            with BuildLine():
                Line((0, -9), (0, 0))
                Line((8, 0), (0, 0))
                Line((8, 9), (8, 0))
                Line((-8, 9), (8, 9))
                Line((-8, -9), (-8, 9))
                Line((0, -9), (-8, -9))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal shaft, featuring a long, tapered or uniform polygonal body with six sides and pointed ends, commonly used as a structural component or drive shaft in mechanical assemblies.
def model_137837_9c9f163d_0008():
    """Model: HEEL BLOCK"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 125, perimeter: 60
            with BuildLine():
                Line((-5, 25), (0, 25))
                Line((-5, 0), (-5, 25))
                Line((0, 0), (-5, 0))
                Line((0, 25), (0, 0))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a flat, elongated rectangular plate or panel with a tapered wedge-like shape, featuring a thin profile and angled edges that create a streamlined, aerodynamic form suitable for aerospace or industrial applications.
def model_137837_9c9f163d_0009():
    """Model: CORE BACK PLATE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 156.25, perimeter: 50
            with BuildLine():
                Line((12.5, -12.5), (0, -12.5))
                Line((12.5, 0), (12.5, -12.5))
                Line((0, 0), (12.5, 0))
                Line((0, -12.5), (0, 0))
            make_face()
            # Profile area: 468.75, perimeter: 100
            with BuildLine():
                Line((0, -12.5), (0, 0))
                Line((0, 0), (12.5, 0))
                Line((12.5, 12.5), (12.5, 0))
                Line((-12.5, 12.5), (12.5, 12.5))
                Line((-12.5, -12.5), (-12.5, 12.5))
                Line((0, -12.5), (-12.5, -12.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a boat hull or marine vessel component with an elongated pentagonal shape, featuring a tapered pointed bow, flat deck surface with internal ribbing/stringers for structural reinforcement, and a stepped stern section.
def model_137846_46d17568_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.75, perimeter: 22.8994949366
            with BuildLine():
                Line((0, 0), (0, -4))
                Line((0, -4), (3, -4))
                Line((3, -4), (4.5, -2.5))
                Line((4.5, -2.5), (6, -4))
                Line((6, -4), (8, -2))
                Line((8, -2), (6, 0))
                Line((0, 0), (6, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=0.4
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a rectangular prism or block with a parallelogram-like slant, featuring a trapezoidal cross-section and angled surfaces that give it a wedge or skewed box appearance.
def model_138071_f8d5a493_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 53.56, perimeter: 31
            with BuildLine():
                Line((0, 10.3), (0, 0))
                Line((0, 0), (5.2, 0))
                Line((5.2, 0), (5.2, 10.3))
                Line((5.2, 10.3), (0, 10.3))
            make_face()
        # OneSide extrude, distance=2.1
        extrude(amount=2.1)
    return part.part


# Description: This is a cylindrical container or sleeve with a tapered, slightly curved top opening and vertical ribbed or fluted surface detailing along its sides.
def model_138138_3d94bb12_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 427.2566008882, perimeter: 73.2739025451
            Circle(11.6619037897)
        # OneSide extrude, distance=27.5
        extrude(amount=27.5)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform circular cross-section, featuring slightly rounded ends and a smooth, tapered appearance suggesting a hollow or solid rod component.
def model_138143_48d4dcd5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9058887283, perimeter: 3.3739788819
            with Locations((0, 0.2317970817)):
                Circle(0.5369854169)
        # OneSide extrude, distance=8.5
        extrude(amount=8.5)
    return part.part


# Description: This is a hexagonal or wedge-shaped solid object with a trapezoidal profile, featuring angular faceted surfaces and what appears to be a tapered or chamfered geometry, with darker shaded faces indicating depth and dimensionality.
def model_138150_55b9f95f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((5, 0), (0, 0))
                Line((5, 2.5), (5, 0))
                Line((0, 2.5), (5, 2.5))
                Line((0, 0), (0, 2.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)
    return part.part


# Description: This is a flat rectangular panel or plate with a slightly curved or beveled edge design, featuring diagonal surface lines or reinforcing ribs that run across its face.
def model_138154_c30b80d3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 32.5274304144, perimeter: 23.6726314055
            with BuildLine():
                Line((6.9639035122, 0.2821368957), (2.6259867625, 0.2821368957))
                Line((6.9639035122, 7.7805358488), (6.9639035122, 0.2821368957))
                Line((2.6259867625, 7.7805358488), (6.9639035122, 7.7805358488))
                Line((2.6259867625, 0.2821368957), (2.6259867625, 7.7805358488))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a polyhedron or geometric solid with an irregular hexagonal-like base, featuring multiple faceted surfaces in varying shades that suggest a complex 3D form with angular planes and triangulated faces, likely representing a machine part or structural component with multiple intersecting geometric surfaces.
def model_138289_9b76f4fd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 77, perimeter: 36
            with BuildLine():
                Line((0, 7), (0, 0))
                Line((0, 0), (11, 0))
                Line((11, 0), (11, 7))
                Line((11, 7), (0, 7))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)
    return part.part


# Description: This is an elliptical bowl or basin with a shallow, curved interior surface and a flat outer rim, featuring longitudinal ribbing or fluting along its sides for structural reinforcement.
def model_138451_7b6845cd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an elliptical or oval-shaped central hole running through its length, featuring a solid lower section and a mesh or perforated upper section.
def model_138535_c0da19b3_0012():
    """Model: Шайба (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3561944902, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a pentagonal or irregular polyhedral solid featuring a pyramidal top section with a broader, faceted base, combining angular geometric surfaces with no apparent holes or slots.
def model_138559_520601c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 72.4675497244, perimeter: 33.6541376174
            with BuildLine():
                Line((-4, 11), (0, 6.1087748622))
                Line((-8.5, 6), (-4, 11))
                Line((-8.5, 0), (-8.5, 6))
                Line((0, 0), (-8.5, 0))
                Line((0, 6.1087748622), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a hexagonal or polygonal block with a complex internal geometric structure, featuring multiple triangulated facets and planes that create a faceted, crystalline appearance with both solid external faces and internal geometric divisions.
def model_138561_5abbe69a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 128.25, perimeter: 44.55238742
            with BuildLine():
                Line((-2.5, -5.5), (0, 0))
                Line((0, 0), (0, 6.5))
                Line((0, 6.5), (-11.5, 6))
                Line((-11.5, 6), (-11.5, -5.5))
                Line((-11.5, -5.5), (-2.5, -5.5))
            make_face()
        # OneSide extrude, distance=8.5
        extrude(amount=8.5)
    return part.part


# Description: This is a 3D wedge or trapezoidal prism with a pointed left end that tapers to a sharp edge, a wider right face, and a sloped top surface, resembling a streamlined or aerodynamic cutting wedge or deflector part.
def model_138562_03f863fb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24, perimeter: 24
            with BuildLine():
                Line((-8, 0), (-8, 6))
                Line((0, 0), (-8, 0))
                Line((-8, 6), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a pentagonal prism or wedge-shaped solid with a five-sided polygonal cross-section, featuring flat faces and sharp edges with no holes, slots, or curves.
def model_138598_71a570e5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 101.25, perimeter: 40.9327073429
            with BuildLine():
                Line((-12.5, -3), (0, 0))
                Line((0, 0), (-3, 7.5))
                Line((-3, 7.5), (-12.5, 7.5))
                Line((-12.5, 7.5), (-12.5, -3))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a hexagonal or polygonal prism-like geometric solid with a complex faceted structure featuring multiple planar surfaces in varying shades, displaying an angular, crystal-like or truncated polyhedron form without apparent holes or slots.
def model_138599_fe19d5c7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 51, perimeter: 29
            with BuildLine():
                Line((-8.5, 6), (0, 6))
                Line((-8.5, 0), (-8.5, 6))
                Line((0, 0), (-8.5, 0))
                Line((0, 6), (0, 0))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


# Description: This is a hexagonal prism or block with a rectangular body featuring a sloped or angled top surface and internal triangulated geometry visible through transparent faces.
def model_138633_a2a11904_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 74.75, perimeter: 36
            with BuildLine():
                Line((-11.5, 7), (0, 7))
                Line((-11.5, 0.5), (-11.5, 7))
                Line((0, 0.5), (-11.5, 0.5))
                Line((0, 7), (0, 0.5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped solid with a trapezoidal top face, featuring a tapered geometry that transitions from a wider base to a narrower top, with internal structural lines suggesting internal geometry or divisions.
def model_138636_c1153075_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 66, perimeter: 34
            with BuildLine():
                Line((-11, 6), (0, 6))
                Line((-11, 0), (-11, 6))
                Line((0, 0), (-11, 0))
                Line((0, 6), (0, 0))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


# Description: This is a hexagonal or polygonal solid block with an irregular, angular geometry featuring multiple faceted surfaces in varying shades, likely representing a complex geometric form with flat planes and potentially internal or recessed features suggested by the edge lines and shading variations.
def model_138675_8f140033_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 51, perimeter: 29
            with BuildLine():
                Line((-8.5, 6), (0, 6))
                Line((-8.5, 0), (-8.5, 6))
                Line((0, 0), (-8.5, 0))
                Line((0, 6), (0, 0))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)
    return part.part


# Description: This is a hexagonal or polygonal prismatic part with an irregular, faceted geometric shape featuring multiple planar surfaces at varying angles, internal geometric divisions, and a complex three-dimensional structure with no obvious holes or slots.
def model_138680_1a4395e8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 46.8714503857, perimeter: 27.4507542565
            with BuildLine():
                Line((0, 6.388300598), (0, 0))
                Line((0, 0), (7.3370765302, 0))
                Line((7.3370765302, 0), (7.3370765302, 6.388300598))
                Line((7.3370765302, 6.388300598), (0, 6.388300598))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a tapered top face, featuring a regular hexagonal base and internal geometric divisions visible through its translucent rendering.
def model_138682_b210e304_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 80.9706122001, perimeter: 37.7506153083
            with BuildLine():
                Line((-12.2834748966, 6.5918327576), (0, 6.5918327576))
                Line((-12.2834748966, 0), (-12.2834748966, 6.5918327576))
                Line((0, 0), (-12.2834748966, 0))
                Line((0, 6.5918327576), (0, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped solid with a trapezoidal profile, featuring flat faces and angular edges, appearing to be a structural component or connector block with no prominent holes or slots.
def model_138684_b2780d91_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 64.4884336074, perimeter: 33.4674509495
            with BuildLine():
                Line((-10.7154705077, 6.0182549671), (0, 6.0182549671))
                Line((-10.7154705077, 0), (-10.7154705077, 6.0182549671))
                Line((0, 0), (-10.7154705077, 0))
                Line((0, 6.0182549671), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped polyhedron with multiple planar faces, featuring a predominantly rectangular body with angled top surfaces and internal edge divisions that suggest structural ribbing or internal geometry.
def model_138685_fd9b79cd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 44.8061145748, perimeter: 27.7525996384
            with BuildLine():
                Line((-8.7634744269, 5.1128253923), (0, 5.1128253923))
                Line((-8.7634744269, 0), (-8.7634744269, 5.1128253923))
                Line((0, 0), (-8.7634744269, 0))
                Line((0, 5.1128253923), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a hexagonal prism or block with a trapezoidal or wedge-shaped top surface, featuring internal geometric subdivisions and edges that suggest a complex multi-faceted design.
def model_138688_840e870e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 45, perimeter: 28
            with BuildLine():
                Line((-9, 5), (0, 5))
                Line((-9, 0), (-9, 5))
                Line((0, 0), (-9, 0))
                Line((0, 5), (0, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a complex polyhedral bracket or connector featuring an irregular geometric shape with multiple angular faces, composed of darker and lighter blue faceted surfaces that form an asymmetrical structure with protruding sections and internal voids.
def model_138698_e190e3eb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 25.75, perimeter: 22.8994949366
            with BuildLine():
                Line((6, 4), (8, 2))
                Line((4.5, 2.5), (6, 4))
                Line((3, 4), (4.5, 2.5))
                Line((0, 4), (3, 4))
                Line((0, 0), (0, 4))
                Line((6, 0), (0, 0))
                Line((8, 2), (6, 0))
            make_face()
        # Symmetric extrude, each_side=1.1132
        extrude(amount=1.1132, both=True)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal block with a rectangular base and angled top face, featuring multiple planar surfaces and internal geometric subdivisions visible through its wireframe structure.
def model_138713_3ac3915b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 70, perimeter: 34
            with BuildLine():
                Line((-10, 7), (0, 7))
                Line((-10, 0), (-10, 7))
                Line((0, 0), (-10, 0))
                Line((0, 7), (0, 0))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped 3D part with a tapered or angled top surface, featuring internal geometric divisions and faceted surfaces in dark and light blue tones.
def model_138714_15a003f6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 49.5, perimeter: 29
            with BuildLine():
                Line((-9, 5.5), (0, 5.5))
                Line((-9, 0), (-9, 5.5))
                Line((0, 0), (-9, 0))
                Line((0, 5.5), (0, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a diagonal slot or cutout running through its left side, creating an angular cavity that intersects the front and back faces.
def model_138720_1ba95e19_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 49.5, perimeter: 31
            with BuildLine():
                Line((0, -4.5), (0, 0))
                Line((0, 0), (-11, 0))
                Line((-11, 0), (-11, -4.5))
                Line((-11, -4.5), (0, -4.5))
            make_face()
        # OneSide extrude, distance=-8.5
        extrude(amount=-8.5)
    return part.part


# Description: This is a polyhedral solid with an irregular geometric shape, featuring multiple triangular and rectangular facets in varying shades of blue and dark gray, with a complex angular structure and no apparent holes, slots, or curves.
def model_138723_787cbfa9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 38.5, perimeter: 25
            with BuildLine():
                Line((0, 5.5), (0, 0))
                Line((0, 0), (7, 0))
                Line((7, 0), (7, 5.5))
                Line((7, 5.5), (0, 5.5))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a hexagonal or pentagonal prism with internal triangular subdivisions, featuring a solid geometric structure with flat faces and internal geometric divisions that create a faceted, modular appearance.
def model_138724_99a5d09c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 44, perimeter: 27
            with BuildLine():
                Line((0, 5.5), (0, 0))
                Line((0, 0), (8, 0))
                Line((8, 0), (8, 5.5))
                Line((8, 5.5), (0, 5.5))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a trapezoidal prism or wedge-shaped structural component with a tapered profile that narrows toward the bottom, featuring a flat top surface and angled side faces that converge downward.
def model_138725_4382f988_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 76.6856758064, perimeter: 40.052193514
            with BuildLine():
                Line((-12.7347820002, -5.7860486611), (0, 0))
                Line((0, 0), (-10, 7.5))
                Line((-10, 7.5), (-12.7347820002, -5.7860486611))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)
    return part.part


# Description: This is a hexagonal or irregular polygonal prism with a triangulated surface structure, featuring a combination of flat faces and internal geometric divisions created by multiple planar sections radiating from a central point.
def model_138739_ef445038_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 51, perimeter: 29
            with BuildLine():
                Line((0, -6), (0, 0))
                Line((0, 0), (-8.5, 0))
                Line((-8.5, 0), (-8.5, -6))
                Line((-8.5, -6), (0, -6))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6)
    return part.part


# Description: This is a hexagonal prism or block with a pentagonal or wedge-shaped cut removed from one side, creating an asymmetrical polyhedron with flat faces and defined edges.
def model_138742_85e709ec_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 46.75, perimeter: 28
            with BuildLine():
                Line((-8.5, 5.5), (0, 5.5))
                Line((-8.5, 0), (-8.5, 5.5))
                Line((0, 0), (-8.5, 0))
                Line((0, 5.5), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a long, flat rectangular bar or plate with beveled or angled edges on both ends, featuring a blue metallic finish and subtle surface details or grooves along its length.
def model_138771_38afab8e_0000():
    """Model: 1?????? ????????? v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1200, perimeter: 224
            with BuildLine():
                Line((-100, 12), (0, 12))
                Line((-100, 0), (-100, 12))
                Line((0, 0), (-100, 0))
                Line((0, 12), (0, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a cylindrical rod or shaft with a tapered conical point at one end, featuring a uniform dark metallic finish and a slightly textured surface.
def model_138771_38afab8e_0011():
    """Model: ннннннннннннннннннннннннннннннннн v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 500, perimeter: 210
            with BuildLine():
                Line((-100, 5), (0, 5))
                Line((-100, 0), (-100, 5))
                Line((0, 0), (-100, 0))
                Line((0, 5), (0, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a sailboat hull or keel with an elliptical cross-section, featuring a streamlined, elongated oval shape with internal ribbing/stringers for structural support and a reinforced rim or flange around the perimeter.
def model_138771_38afab8e_0013():
    """Model: ????????! v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34.1382718561, perimeter: 20.7121745907
            Circle(3.2964449683)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a boat hull or ship bow section with a sleek, tapered wedge shape featuring a pointed prow, curved sides, and a flat upper deck area with what appears to be a small ventilation or access opening.
def model_138885_72845989_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5159723794, perimeter: 15.502973727
            with BuildLine():
                Line((1.5406014566, -3.5703619777), (0, 0))
                CenterArc((1.905, -3.413125), 0.396875, -156.6599339926, 133.3198679852)
                Line((2.2693985434, -3.5703619777), (3.81, 0))
                Line((0, 0), (3.81, 0))
            make_face()
            with BuildLine():
                CenterArc((1.905, -2.54), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a flat, elongated rectangular plate or bar with a parallelogram-like profile, featuring beveled or chamfered edges on the left end and a slight 3D depth, appearing to be a simple structural component or mounting bracket.
def model_138946_b45b2c50_0002():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 329.0316005814, perimeter: 101.6000001526
            with BuildLine():
                Line((48.26, 94.2975), (48.26, 101.9175))
                Line((48.26, 101.9175), (5.0799999237, 101.9175))
                Line((5.0799999237, 101.9175), (5.0799999237, 94.2975))
                Line((5.0799999237, 94.2975), (48.26, 94.2975))
            make_face()
        # OneSide extrude, distance=2.38125
        extrude(amount=2.38125)
    return part.part


# Description: Two identical dark rectangular prisms or panels with a slight trapezoidal profile, each featuring diagonal cross-bracing lines on their faces, positioned side-by-side at an angle.
def model_138946_b45b2c50_0005():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 194.1528375, perimeter: 207.645
            with BuildLine():
                Line((1.905, 0), (0, 0))
                Line((1.905, 101.9175), (1.905, 0))
                Line((0, 101.9175), (1.905, 101.9175))
                Line((0, 0), (0, 101.9175))
            make_face()
            # Profile area: 194.1528375, perimeter: 207.645
            with BuildLine():
                Line((53.34, 0), (53.34, 101.9175))
                Line((53.34, 101.9175), (51.435, 101.9175))
                Line((51.435, 101.9175), (51.435, 0))
                Line((51.435, 0), (53.34, 0))
            make_face()
        # OneSide extrude, distance=-38.1
        extrude(amount=-38.1)
    return part.part


# Description: This is a long, narrow rectangular extrusion or channel with a shallow U-shaped or trough-like cross-section, featuring angled end caps on both sides.
def model_138946_b45b2c50_0006():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 109.6772, perimeter: 91.44
            with BuildLine():
                Line((5.08, 2.54), (5.08, 0))
                Line((5.08, 0), (48.26, 0))
                Line((48.26, 0), (48.26, 2.54))
                Line((48.26, 2.54), (5.08, 2.54))
            make_face()
        # OneSide extrude, distance=2.38125
        extrude(amount=2.38125)
    return part.part


# Description: This is a flat, parallelogram-shaped plate with a beveled or chamfered edge on one side and internal diagonal reinforcement ribs that divide the surface into triangular sections.
def model_138946_b45b2c50_0007():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 94.35465, perimeter: 102.87
            with BuildLine():
                Line((51.435, 100.0125), (51.435, 101.9175))
                Line((51.435, 101.9175), (1.905, 101.9175))
                Line((1.905, 101.9175), (1.905, 100.0125))
                Line((1.905, 100.0125), (51.435, 100.0125))
            make_face()
        # OneSide extrude, distance=-36.195
        extrude(amount=-36.195)
    return part.part


# Description: This is a wedge-shaped or trapezoidal prism with a tapered profile, featuring a slanted top surface and a broader base, appearing to be a support bracket or angled structural component with clean planar faces.
def model_138947_0778db40_0000():
    """Model: right side cabs"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6141.9232, perimeter: 370.84
            with BuildLine():
                Line((142.24, -43.18), (0, -43.18))
                Line((142.24, 0), (142.24, -43.18))
                Line((0, 0), (142.24, 0))
                Line((0, -43.18), (0, 0))
            make_face()
        # OneSide extrude, distance=71.12
        extrude(amount=71.12)
    return part.part


# Description: This is a cylindrical dowel pin or shaft with a smooth, tapered rounded end and a slightly textured surface, designed for alignment or fastening applications.
def model_138947_0778db40_0001():
    """Model: duct"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 182.4146924751, perimeter: 47.8778720407
            with Locations((0, 177.8)):
                Circle(7.62)
        # OneSide extrude, distance=76.2
        extrude(amount=76.2)
    return part.part


# Description: This is a pair of parallel cylindrical rods or pins with a slight diagonal orientation, featuring a smooth, uniform round cross-section and tapered ends.
def model_138947_0778db40_0002():
    """Model: support beams"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33.8709, perimeter: 25.4
            with BuildLine():
                Line((10.16, -43.18), (10.16, -46.99))
                Line((10.16, -46.99), (19.05, -46.99))
                Line((19.05, -46.99), (19.05, -43.18))
                Line((19.05, -43.18), (10.16, -43.18))
            make_face()
            # Profile area: 33.8709, perimeter: 25.4
            with BuildLine():
                Line((133.35, -43.18), (133.35, -46.99))
                Line((133.35, -46.99), (142.24, -46.99))
                Line((142.24, -46.99), (142.24, -43.18))
                Line((142.24, -43.18), (133.35, -43.18))
            make_face()
        # OneSide extrude, distance=284.48
        extrude(amount=284.48)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped solid block with a trapezoidal profile, featuring flat faces and angular edges, with no apparent holes, slots, or curved surfaces.
def model_138947_0778db40_0004():
    """Model: left side cabs"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2961.2844, perimeter: 223.52
            with BuildLine():
                Line((0, -43.18), (0, 0))
                Line((0, 0), (-68.58, 0))
                Line((-68.58, 0), (-68.58, -43.18))
                Line((-68.58, -43.18), (0, -43.18))
            make_face()
        # OneSide extrude, distance=71.12
        extrude(amount=71.12)
    return part.part


# Description: This is a cylindrical sleeve or tube component with a long, hollow body and threaded or textured end caps on both ends, featuring a smooth main section with subtle surface details.
def model_139005_7b6aa20e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.29, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a long, flat rectangular bar or plate with a parallelogram-like skewed profile, featuring beveled or angled edges on the ends and a dark metallic finish.
def model_139093_f71ea5d2_0002():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((5, -11), (-10, -11))
                Line((5, -10), (5, -11))
                Line((-10, -10), (5, -10))
                Line((-10, -11), (-10, -10))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a multi-stage cylindrical gear or sprocket assembly with four stacked barrel-shaped sections of decreasing diameter, featuring axial holes through each stage and a stepped profile designed for power transmission or mechanical coupling.
def model_139116_5f441b87_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 271 constraints, 49 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.7249707276, perimeter: 83.8448043666
            with BuildLine():
                Line((1.0848201588, 0.6479865041), (1.2033201588, 0.5294865041))
                Line((1.0848201588, 0.6479865041), (0.0008201588, 0.6479865041))
                Line((0.0008201588, 0.6479865041), (-0.1176798412, 0.5294865041))
                Line((-0.1176798412, 0.5294865041), (-0.1176798412, 0.4679865041))
                Line((-0.1176798412, 0.4679865041), (0.0928201588, 0.4679865041))
                Line((0.0928201588, 0.4679865041), (0.0928201588, 0.3040525213))
                Line((0.0928201588, 0.3040525213), (-0.1732458584, 0.0379865041))
                Line((-0.741113824, 0.0379865041), (-0.1732458584, 0.0379865041))
                Line((-1.0071798412, 0.3040525213), (-0.741113824, 0.0379865041))
                Line((-1.0071798412, 0.4679865041), (-1.0071798412, 0.3040525213))
                Line((-0.7966798412, 0.4679865041), (-1.0071798412, 0.4679865041))
                Line((-0.7966798412, 0.5294865041), (-0.7966798412, 0.4679865041))
                Line((-0.9151798412, 0.6479865041), (-0.7966798412, 0.5294865041))
                Line((-1.4571798412, 0.6479865041), (-0.9151798412, 0.6479865041))
                Line((-1.4571798412, 1.1899865041), (-1.4571798412, 0.6479865041))
                Line((-1.4571798412, 1.1899865041), (-1.5756798412, 1.3084865041))
                Line((-1.5756798412, 1.3084865041), (-1.6371798412, 1.3084865041))
                Line((-1.6371798412, 1.3084865041), (-1.6371798412, 1.0979865041))
                Line((-1.6371798412, 1.0979865041), (-1.801113824, 1.0979865041))
                Line((-1.801113824, 1.0979865041), (-2.0671798412, 1.3640525213))
                Line((-2.0671798412, 1.3640525213), (-2.0671798412, 1.931920487))
                Line((-1.801113824, 2.1979865041), (-2.0671798412, 1.931920487))
                Line((-1.6371798412, 2.1979865041), (-1.801113824, 2.1979865041))
                Line((-1.6371798412, 1.9874865041), (-1.6371798412, 2.1979865041))
                Line((-1.5756798412, 1.9874865041), (-1.6371798412, 1.9874865041))
                Line((-1.4571798412, 2.1059865041), (-1.5756798412, 1.9874865041))
                Line((-1.4571798412, 2.1059865041), (-1.4571798412, 2.4979865041))
                CenterArc((-1.6071798412, 2.4979865041), 0.15, 0, 90)
                Line((-1.6071798412, 2.6479865041), (-1.9991798412, 2.6479865041))
                Line((-1.9991798412, 2.6479865041), (-2.1176798412, 2.5294865041))
                Line((-2.1176798412, 2.5294865041), (-2.1176798412, 2.4679865041))
                Line((-2.1176798412, 2.4679865041), (-1.9071798412, 2.4679865041))
                Line((-1.9071798412, 2.4679865041), (-1.9071798412, 2.3040525213))
                Line((-1.9071798412, 2.3040525213), (-2.1732458584, 2.0379865041))
                Line((-2.1732458584, 2.0379865041), (-2.741113824, 2.0379865041))
                Line((-3.0071798412, 2.3040525213), (-2.741113824, 2.0379865041))
                Line((-3.0071798412, 2.4679865041), (-3.0071798412, 2.3040525213))
                Line((-2.7966798412, 2.4679865041), (-3.0071798412, 2.4679865041))
                Line((-2.7966798412, 2.5294865041), (-2.7966798412, 2.4679865041))
                Line((-2.9151798412, 2.6479865041), (-2.7966798412, 2.5294865041))
                Line((-2.9151798412, 2.6479865041), (-3.3071798412, 2.6479865041))
                CenterArc((-3.3071798412, 2.4979865041), 0.15, 90, 90)
                Line((-3.4571798412, 2.1059865041), (-3.4571798412, 2.4979865041))
                Line((-3.4571798412, 2.1059865041), (-3.3386798412, 1.9874865041))
                Line((-3.3386798412, 1.9874865041), (-3.2771798412, 1.9874865041))
                Line((-3.2771798412, 1.9874865041), (-3.2771798412, 2.1979865041))
                Line((-3.2771798412, 2.1979865041), (-3.1132458584, 2.1979865041))
                Line((-3.1132458584, 2.1979865041), (-2.8471798412, 1.931920487))
                Line((-2.8471798412, 1.3640525213), (-2.8471798412, 1.931920487))
                Line((-3.1132458584, 1.0979865041), (-2.8471798412, 1.3640525213))
                Line((-3.2771798412, 1.0979865041), (-3.1132458584, 1.0979865041))
                Line((-3.2771798412, 1.3084865041), (-3.2771798412, 1.0979865041))
                Line((-3.3386798412, 1.3084865041), (-3.2771798412, 1.3084865041))
                Line((-3.4571798412, 1.1899865041), (-3.3386798412, 1.3084865041))
                Line((-3.4571798412, 1.1899865041), (-3.4571798412, 0.1059865041))
                Line((-3.4571798412, 0.1059865041), (-3.3386798412, -0.0125134959))
                Line((-3.3386798412, -0.0125134959), (-3.2771798412, -0.0125134959))
                Line((-3.2771798412, -0.0125134959), (-3.2771798412, 0.1979865041))
                Line((-3.2771798412, 0.1979865041), (-3.1132458584, 0.1979865041))
                Line((-3.1132458584, 0.1979865041), (-2.8471798412, -0.068079513))
                Line((-2.8471798412, -0.068079513), (-2.8471798412, -0.6359474787))
                Line((-3.1132458584, -0.9020134959), (-2.8471798412, -0.6359474787))
                Line((-3.2771798412, -0.9020134959), (-3.1132458584, -0.9020134959))
                Line((-3.2771798412, -0.6915134959), (-3.2771798412, -0.9020134959))
                Line((-3.3386798412, -0.6915134959), (-3.2771798412, -0.6915134959))
                Line((-3.4571798412, -0.8100134959), (-3.3386798412, -0.6915134959))
                Line((-3.4571798412, -0.8100134959), (-3.4571798412, -1.2020134959))
                CenterArc((-3.3071798412, -1.2020134959), 0.15, 180, 90)
                Line((-2.9151798412, -1.3520134959), (-3.3071798412, -1.3520134959))
                Line((-2.9151798412, -1.3520134959), (-2.7966798412, -1.2335134959))
                Line((-2.7966798412, -1.2335134959), (-2.7966798412, -1.1720134959))
                Line((-2.7966798412, -1.1720134959), (-3.0071798412, -1.1720134959))
                Line((-3.0071798412, -1.1720134959), (-3.0071798412, -1.008079513))
                Line((-3.0071798412, -1.008079513), (-2.741113824, -0.7420134959))
                Line((-2.1732458584, -0.7420134959), (-2.741113824, -0.7420134959))
                Line((-1.9071798412, -1.008079513), (-2.1732458584, -0.7420134959))
                Line((-1.9071798412, -1.1720134959), (-1.9071798412, -1.008079513))
                Line((-2.1176798412, -1.1720134959), (-1.9071798412, -1.1720134959))
                Line((-2.1176798412, -1.2335134959), (-2.1176798412, -1.1720134959))
                Line((-1.9991798412, -1.3520134959), (-2.1176798412, -1.2335134959))
                Line((-0.9151798412, -1.3520134959), (-1.9991798412, -1.3520134959))
                Line((-0.9151798412, -1.3520134959), (-0.7966798412, -1.2335134959))
                Line((-0.7966798412, -1.2335134959), (-0.7966798412, -1.1720134959))
                Line((-0.7966798412, -1.1720134959), (-1.0071798412, -1.1720134959))
                Line((-1.0071798412, -1.1720134959), (-1.0071798412, -1.008079513))
                Line((-1.0071798412, -1.008079513), (-0.741113824, -0.7420134959))
                Line((-0.741113824, -0.7420134959), (-0.1732458584, -0.7420134959))
                Line((0.0928201588, -1.008079513), (-0.1732458584, -0.7420134959))
                Line((0.0928201588, -1.1720134959), (0.0928201588, -1.008079513))
                Line((-0.1176798412, -1.1720134959), (0.0928201588, -1.1720134959))
                Line((-0.1176798412, -1.2335134959), (-0.1176798412, -1.1720134959))
                Line((0.0008201588, -1.3520134959), (-0.1176798412, -1.2335134959))
                Line((0.0008201588, -1.3520134959), (1.0848201588, -1.3520134959))
                Line((1.0848201588, -1.3520134959), (1.2033201588, -1.2335134959))
                Line((1.2033201588, -1.2335134959), (1.2033201588, -1.1720134959))
                Line((1.2033201588, -1.1720134959), (0.9928201588, -1.1720134959))
                Line((0.9928201588, -1.1720134959), (0.9928201588, -1.008079513))
                Line((0.9928201588, -1.008079513), (1.258886176, -0.7420134959))
                Line((1.8267541416, -0.7420134959), (1.258886176, -0.7420134959))
                Line((2.0928201588, -1.008079513), (1.8267541416, -0.7420134959))
                Line((2.0928201588, -1.1720134959), (2.0928201588, -1.008079513))
                Line((1.8823201588, -1.1720134959), (2.0928201588, -1.1720134959))
                Line((1.8823201588, -1.2335134959), (1.8823201588, -1.1720134959))
                Line((2.0008201588, -1.3520134959), (1.8823201588, -1.2335134959))
                Line((2.0008201588, -1.3520134959), (3.0848201588, -1.3520134959))
                Line((3.0848201588, -1.3520134959), (3.2033201588, -1.2335134959))
                Line((3.2033201588, -1.2335134959), (3.2033201588, -1.1720134959))
                Line((3.2033201588, -1.1720134959), (2.9928201588, -1.1720134959))
                Line((2.9928201588, -1.1720134959), (2.9928201588, -1.008079513))
                Line((2.9928201588, -1.008079513), (3.258886176, -0.7420134959))
                Line((3.258886176, -0.7420134959), (3.8267541416, -0.7420134959))
                Line((4.0928201588, -1.008079513), (3.8267541416, -0.7420134959))
                Line((4.0928201588, -1.1720134959), (4.0928201588, -1.008079513))
                Line((3.8823201588, -1.1720134959), (4.0928201588, -1.1720134959))
                Line((3.8823201588, -1.2335134959), (3.8823201588, -1.1720134959))
                Line((4.0008201588, -1.3520134959), (3.8823201588, -1.2335134959))
                Line((4.0008201588, -1.3520134959), (4.3928201588, -1.3520134959))
                CenterArc((4.3928201588, -1.2020134959), 0.15, -90, 90)
                Line((4.5428201588, -0.8100134959), (4.5428201588, -1.2020134959))
                Line((4.5428201588, -0.8100134959), (4.4243201588, -0.6915134959))
                Line((4.4243201588, -0.6915134959), (4.3628201588, -0.6915134959))
                Line((4.3628201588, -0.6915134959), (4.3628201588, -0.9020134959))
                Line((4.3628201588, -0.9020134959), (4.198886176, -0.9020134959))
                Line((4.198886176, -0.9020134959), (3.9328201588, -0.6359474787))
                Line((3.9328201588, -0.068079513), (3.9328201588, -0.6359474787))
                Line((4.198886176, 0.1979865041), (3.9328201588, -0.068079513))
                Line((4.3628201588, 0.1979865041), (4.198886176, 0.1979865041))
                Line((4.3628201588, -0.0125134959), (4.3628201588, 0.1979865041))
                Line((4.4243201588, -0.0125134959), (4.3628201588, -0.0125134959))
                Line((4.5428201588, 0.1059865041), (4.4243201588, -0.0125134959))
                Line((4.5428201588, 1.1899865041), (4.5428201588, 0.1059865041))
                Line((4.5428201588, 1.1899865041), (4.4243201588, 1.3084865041))
                Line((4.4243201588, 1.3084865041), (4.3628201588, 1.3084865041))
                Line((4.3628201588, 1.3084865041), (4.3628201588, 1.0979865041))
                Line((4.3628201588, 1.0979865041), (4.198886176, 1.0979865041))
                Line((4.198886176, 1.0979865041), (3.9328201588, 1.3640525213))
                Line((3.9328201588, 1.3640525213), (3.9328201588, 1.931920487))
                Line((4.198886176, 2.1979865041), (3.9328201588, 1.931920487))
                Line((4.3628201588, 2.1979865041), (4.198886176, 2.1979865041))
                Line((4.3628201588, 1.9874865041), (4.3628201588, 2.1979865041))
                Line((4.4243201588, 1.9874865041), (4.3628201588, 1.9874865041))
                Line((4.5428201588, 2.1059865041), (4.4243201588, 1.9874865041))
                Line((4.5428201588, 2.1059865041), (4.5428201588, 2.4979865041))
                CenterArc((4.3928201588, 2.4979865041), 0.15, 0, 90)
                Line((4.0008201588, 2.6479865041), (4.3928201588, 2.6479865041))
                Line((4.0008201588, 2.6479865041), (3.8823201588, 2.5294865041))
                Line((3.8823201588, 2.5294865041), (3.8823201588, 2.4679865041))
                Line((3.8823201588, 2.4679865041), (4.0928201588, 2.4679865041))
                Line((4.0928201588, 2.4679865041), (4.0928201588, 2.3040525213))
                Line((4.0928201588, 2.3040525213), (3.8267541416, 2.0379865041))
                Line((3.258886176, 2.0379865041), (3.8267541416, 2.0379865041))
                Line((2.9928201588, 2.3040525213), (3.258886176, 2.0379865041))
                Line((2.9928201588, 2.4679865041), (2.9928201588, 2.3040525213))
                Line((3.2033201588, 2.4679865041), (2.9928201588, 2.4679865041))
                Line((3.2033201588, 2.5294865041), (3.2033201588, 2.4679865041))
                Line((3.0848201588, 2.6479865041), (3.2033201588, 2.5294865041))
                Line((2.6928201588, 2.6479865041), (3.0848201588, 2.6479865041))
                CenterArc((2.6928201588, 2.4979865041), 0.15, 90, 90)
                Line((2.5428201588, 2.1059865041), (2.5428201588, 2.4979865041))
                Line((2.5428201588, 2.1059865041), (2.6613201588, 1.9874865041))
                Line((2.6613201588, 1.9874865041), (2.7228201588, 1.9874865041))
                Line((2.7228201588, 1.9874865041), (2.7228201588, 2.1979865041))
                Line((2.7228201588, 2.1979865041), (2.8867541416, 2.1979865041))
                Line((2.8867541416, 2.1979865041), (3.1528201588, 1.931920487))
                Line((3.1528201588, 1.3640525213), (3.1528201588, 1.931920487))
                Line((2.8867541416, 1.0979865041), (3.1528201588, 1.3640525213))
                Line((2.7228201588, 1.0979865041), (2.8867541416, 1.0979865041))
                Line((2.7228201588, 1.3084865041), (2.7228201588, 1.0979865041))
                Line((2.6613201588, 1.3084865041), (2.7228201588, 1.3084865041))
                Line((2.5428201588, 1.1899865041), (2.6613201588, 1.3084865041))
                Line((2.5428201588, 1.1899865041), (2.5428201588, 0.6479865041))
                Line((2.5428201588, 0.6479865041), (2.0008201588, 0.6479865041))
                Line((2.0008201588, 0.6479865041), (1.8823201588, 0.5294865041))
                Line((1.8823201588, 0.5294865041), (1.8823201588, 0.4679865041))
                Line((1.8823201588, 0.4679865041), (2.0928201588, 0.4679865041))
                Line((2.0928201588, 0.4679865041), (2.0928201588, 0.3040525213))
                Line((2.0928201588, 0.3040525213), (1.8267541416, 0.0379865041))
                Line((1.8267541416, 0.0379865041), (1.258886176, 0.0379865041))
                Line((0.9928201588, 0.3040525213), (1.258886176, 0.0379865041))
                Line((0.9928201588, 0.4679865041), (0.9928201588, 0.3040525213))
                Line((1.2033201588, 0.4679865041), (0.9928201588, 0.4679865041))
                Line((1.2033201588, 0.5294865041), (1.2033201588, 0.4679865041))
            make_face()
            with BuildLine():
                CenterArc((-2.4571798412, 1.6479865041), 0.23, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.4571798412, -0.3520134959), 0.23, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.4571798412, -0.3520134959), 0.23, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2.7509052159, 1.2481951122), (-3.051113824, 0.9479865041))
                Line((-2.1634544665, 1.2481951122), (-2.7509052159, 1.2481951122))
                Line((-1.8632458584, 0.9479865041), (-2.1634544665, 1.2481951122))
                Line((-1.6071798412, 0.9479865041), (-1.8632458584, 0.9479865041))
                Line((-1.6071798412, 0.6040525213), (-1.6071798412, 0.9479865041))
                Line((-2.1912658386, 0.0199665239), (-1.6071798412, 0.6040525213))
                Line((-2.7230938438, 0.0199665239), (-2.1912658386, 0.0199665239))
                Line((-3.051113824, 0.3479865041), (-2.7230938438, 0.0199665239))
                Line((-3.3071798412, 0.3479865041), (-3.051113824, 0.3479865041))
                Line((-3.3071798412, 0.9479865041), (-3.3071798412, 0.3479865041))
                Line((-3.051113824, 0.9479865041), (-3.3071798412, 0.9479865041))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2.0851998214, -0.6179274985), (-2.0851998214, -0.0860994932))
                Line((-2.0851998214, -0.0860994932), (-1.501113824, 0.4979865041))
                Line((-1.501113824, 0.4979865041), (-1.1571798412, 0.4979865041))
                Line((-1.1571798412, 0.4979865041), (-1.1571798412, 0.241920487))
                Line((-1.1571798412, 0.241920487), (-0.8569712331, -0.0582881211))
                Line((-0.8569712331, -0.0582881211), (-0.8569712331, -0.6457388706))
                Line((-0.8569712331, -0.6457388706), (-1.1571798412, -0.9459474787))
                Line((-1.1571798412, -0.9459474787), (-1.1571798412, -1.2020134959))
                Line((-1.1571798412, -1.2020134959), (-1.7571798412, -1.2020134959))
                Line((-1.7571798412, -1.2020134959), (-1.7571798412, -0.9459474787))
                Line((-1.7571798412, -0.9459474787), (-2.0851998214, -0.6179274985))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5428201588, -0.3520134959), 0.23, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5428201588, -0.3520134959), 0.23, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5428201588, 1.6479865041), 0.23, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.2428201588, -1.2020134959), (2.8428201588, -1.2020134959))
                Line((2.2428201588, -0.9459474787), (2.2428201588, -1.2020134959))
                Line((1.9426115507, -0.6457388706), (2.2428201588, -0.9459474787))
                Line((1.9426115507, -0.0582881211), (1.9426115507, -0.6457388706))
                Line((2.2428201588, 0.241920487), (1.9426115507, -0.0582881211))
                Line((2.2428201588, 0.4979865041), (2.2428201588, 0.241920487))
                Line((2.5867541416, 0.4979865041), (2.2428201588, 0.4979865041))
                Line((3.170840139, -0.0860994932), (2.5867541416, 0.4979865041))
                Line((3.170840139, -0.6179274985), (3.170840139, -0.0860994932))
                Line((2.8428201588, -0.9459474787), (3.170840139, -0.6179274985))
                Line((2.8428201588, -1.2020134959), (2.8428201588, -0.9459474787))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.8365455335, 1.2481951122), (4.1367541416, 0.9479865041))
                Line((4.1367541416, 0.9479865041), (4.3928201588, 0.9479865041))
                Line((4.3928201588, 0.9479865041), (4.3928201588, 0.3479865041))
                Line((4.3928201588, 0.3479865041), (4.1367541416, 0.3479865041))
                Line((4.1367541416, 0.3479865041), (3.8087341614, 0.0199665239))
                Line((3.8087341614, 0.0199665239), (3.2769061562, 0.0199665239))
                Line((3.2769061562, 0.0199665239), (2.6928201588, 0.6040525213))
                Line((2.6928201588, 0.6040525213), (2.6928201588, 0.9479865041))
                Line((2.6928201588, 0.9479865041), (2.948886176, 0.9479865041))
                Line((2.948886176, 0.9479865041), (3.2490947841, 1.2481951122))
                Line((3.2490947841, 1.2481951122), (3.8365455335, 1.2481951122))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.2428201588, 0.241920487), (0.2428201588, 0.4979865041))
                Line((0.2428201588, 0.4979865041), (0.8428201588, 0.4979865041))
                Line((0.8428201588, 0.4979865041), (0.8428201588, 0.241920487))
                Line((0.8428201588, 0.241920487), (1.1605624423, -0.0758217966))
                Line((1.1605624423, -0.0758217966), (1.1605624423, -0.6282051952))
                Line((1.1605624423, -0.6282051952), (0.8428201588, -0.9459474787))
                Line((0.8428201588, -0.9459474787), (0.8428201588, -1.2020134959))
                Line((0.8428201588, -1.2020134959), (0.2428201588, -1.2020134959))
                Line((0.2428201588, -1.2020134959), (0.2428201588, -0.9459474787))
                Line((0.2428201588, -0.9459474787), (-0.0649423526, -0.6381849673))
                Line((-0.0649423526, -0.6381849673), (-0.0649423526, -0.0658420244))
                Line((-0.0649423526, -0.0658420244), (0.2428201588, 0.241920487))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a curved black plastic or composite bracket or guard with a smooth upper arc and a textured lower section, featuring a rectangular attachment flange at one end.
def model_139155_1a724258_0000():
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
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.6539071518, perimeter: 120.5173566448
            with BuildLine():
                Line((-4.9463931058, -41.3764088756), (-4.9463931058, -27))
                _nurbs_edge([(-4.9463931058, -27), (-4.5, -22.5), (-3.5, -19.5), (-2.3085929666, -17.5209844491), (-1, -15), (-0.5, -13.5), (0, -12), (-0.2495271828, -10.5758816244), (-1.2468489354, -8.5703020001), (-3.1317833714, -6.774577529), (-5.4528347372, -5.0373396622), (-8.0085116815, -3.423227908), (-10.5193521881, -2.1678076546), (-13.5233935085, -1.181406027), (-16.5722712666, -0.598532338), (-20.4282049018, -0.8675509637), (-24.867012226, -2.481662718)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0833333333, 0.1666666667, 0.25, 0.3333333333, 0.4166666667, 0.5, 0.5833333333, 0.6666666667, 0.75, 0.8333333333, 0.9166666667, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-24.607690339, -2.6871494863), 0.3308665184, 141.6066806045, 147.3879600983)
                _nurbs_edge([(-5.5082937557, -27), (-5.3126691181, -24.0187261487), (-4.9463931058, -22.5061639109), (-4, -19.5), (-3, -17.5), (-1.4638244907, -14.9884650494), (-1, -13.5), (-0.5, -12), (-0.7234351871, -10.5088507294), (-1.8247637871, -8.6149100805), (-3.6032432219, -7.1169400044), (-5.870874065, -5.5084742775), (-8.3128565753, -4.0103947752), (-10.7975268027, -2.9095915099), (-13.753969858, -1.9660458539), (-16.5, -1.5), (-18.7733710414, -1.4143681359), (-20.4282049018, -1.6746068408), (-22.9941816844, -2.481662718), (-24.5, -3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-5.5082937557, -31.2034254137), (-5.5082937557, -27))
                _nurbs_edge([(-6, -32), (-5.6729166868, -31.7796056724), (-5.5082937557, -31.2034254137)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                Line((-6, -41.3764088756), (-6, -32))
                Line((-4.9463931058, -41.3764088756), (-6, -41.3764088756))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


# Description: This is a fan or impeller blade with a curved, streamlined aerodynamic shape featuring radial internal ribs for structural reinforcement and a tapered profile from a thicker root section to a thinner trailing edge.
def model_139222_2c10ca9a_0017():
    """Model: Untitled v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6435.0367746696, perimeter: 328.7008788924
            with BuildLine():
                CenterArc((100, 75), 100.0002, 0.1145914635, 36.7553061823)
                Line((180.00016, 135.00012), (100, 75))
                Line((100, 75), (180.00016, 14.99988))
                CenterArc((100, 75), 100.0002, -36.8698976458, 36.7553061823)
                Line((200, 74.7999999), (200, 75.2000001))
            make_face()
            # Profile area: 0.0000533334, perimeter: 0.8000006667
            with BuildLine():
                CenterArc((100, 75), 100.0002, 179.8854085365, 0.2291829271)
                Line((0, 75.2000001), (0, 74.7999999))
            make_face()
            # Profile area: 7006.4015925297, perimeter: 373.2003926009
            with BuildLine():
                CenterArc((100, 75), 100.0002, 131.4097520435, 11.7203503107)
                Line((19.99984, 135.00012), (100, 75))
                Line((180.00016, 135.00012), (100, 75))
                CenterArc((100, 75), 100.0002, 36.8698976458, 11.7203503107)
                Line((166.1440851478, 150), (33.8559148522, 150))
            make_face()
            # Profile area: 0.0000533334, perimeter: 0.8000006667
            with BuildLine():
                Line((200, 74.7999999), (200, 75.2000001))
                CenterArc((100, 75), 100.0002, -0.1145914635, 0.2291829271)
            make_face()
            # Profile area: 6435.0367746696, perimeter: 328.7008788924
            with BuildLine():
                Line((0, 75.2000001), (0, 74.7999999))
                CenterArc((100, 75), 100.0002, -179.8854085365, 36.7553061823)
                Line((100, 75), (19.99984, 14.99988))
                Line((19.99984, 135.00012), (100, 75))
                CenterArc((100, 75), 100.0002, 143.1301023542, 36.7553061823)
            make_face()
            # Profile area: 7006.4015925297, perimeter: 373.2003926009
            with BuildLine():
                CenterArc((100, 75), 100.0002, -48.5902479565, 11.7203503107)
                Line((100, 75), (180.00016, 14.99988))
                Line((100, 75), (19.99984, 14.99988))
                CenterArc((100, 75), 100.0002, -143.1301023542, 11.7203503107)
                Line((33.8559148522, 0), (166.1440851478, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a simple cylindrical form featuring chamfered or rounded ends for smooth edges.
def model_139222_2c10ca9a_0018():
    """Model: Untitled v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a thin-walled, flat trapezoidal or wedge-shaped plate with a tapered profile, featuring multiple parallel internal ribs or reinforcing fins running across its surface for structural stiffness.
def model_139258_43c33f60_0037():
    """Model: Stock v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2401, perimeter: 196
            with BuildLine():
                Line((-24.5, 24.5), (24.5, 24.5))
                Line((-24.5, -24.5), (-24.5, 24.5))
                Line((24.5, -24.5), (-24.5, -24.5))
                Line((24.5, 24.5), (24.5, -24.5))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a cymbal - a circular, flat-to-slightly-curved percussion instrument with radial grooves/ridges extending from a central raised dome, designed to produce sound when struck or clashed together.
def model_139379_fe5c3f64_0000():
    """Model: base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1253.4954687823, perimeter: 138.230076758
            with BuildLine():
                CenterArc((0, 0), 20, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 2), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.7320508076, -1), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.7320508076, -1), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a straight cylindrical rod or shaft with a uniform diameter, featuring a slightly tapered or pointed end, commonly used as a pin, dowel, or fastening component.
def model_139379_fe5c3f64_0001():
    """Model: tower"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981673, perimeter: 3.1415926613
            with Locations((0, 2.0000000298)):
                Circle(0.5000000012)
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block featuring a trapezoidal profile with angled side faces and a flat top surface, appearing to be a structural component or base part without any holes or complex features.
def model_139610_e43b543c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((10, -10), (0, -10))
                Line((10, 0), (10, -10))
                Line((0, 0), (10, 0))
                Line((0, -10), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a four-pointed star or cross-shaped structural component with two perpendicular planar wings that intersect at a central hub, featuring a triangulated mesh structure with both dark and light blue faceted surfaces.
def model_139674_8774f1a3_0019():
    """Model: pdtplf v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 200, perimeter: 89.4427191
            with BuildLine():
                Line((-5, 0), (-10, 10))
                Line((-10, -10), (-5, 0))
                Line((0, -5), (-10, -10))
                Line((10, -10), (0, -5))
                Line((5, 0), (10, -10))
                Line((10, 10), (5, 0))
                Line((0, 5), (10, 10))
                Line((-10, 10), (0, 5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a curved flexible conduit or hose sleeve with a ribbed/corrugated exterior surface, forming an open arc shape with no end caps, designed to protect or route cables or tubing.
def model_139674_8774f1a3_0027():
    """Model: ????-?????? v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13242.093594074, perimeter: 1076.6025316653
            with BuildLine():
                Line((150, 0), (177.7154898797, 0.0077188823))
                CenterArc((1.2863841413, -0.8803409899), 176.431340759, 0.2883971593, 179.4254510934)
                Line((-175.1427562646, 0.0008046543), (-149.9999999978, 0.0008046543))
                CenterArc((0, 0), 150, 0, 179.9996926439)
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a four-pointed star composed of triangular facets, featuring a central hub with four symmetrical tapered points extending outward, creating a sharp, geometric star geometry with visible wireframe edges.
def model_139674_8774f1a3_0041():
    """Model: ????????? v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8, perimeter: 17.88854382
            with BuildLine():
                Line((-1, 0), (-2, 2))
                Line((-2, -2), (-1, 0))
                Line((0, -1), (-2, -2))
                Line((2, -2), (0, -1))
                Line((1, 0), (2, -2))
                Line((2, 2), (1, 0))
                Line((0, 1), (2, 2))
                Line((-2, 2), (0, 1))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a rectangular prism or box-shaped component with a triangulated internal structure, featuring a light blue upper section divided by internal ribs or webs and a darker blue lower section, suggesting a hollow or partially hollow design optimized for structural rigidity while minimizing weight.
def model_139674_8774f1a3_0060():
    """Model: ???? v1 (11) (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1093060649, perimeter: 8.1086979998
            with BuildLine():
                Line((-0.0260085399, -2.8667851749), (-1.4464523976, -1.4365368069))
                Line((1.4204438577, -1.430248368), (-0.0260085399, -2.8667851749))
                Line((0, 0), (1.4204438577, -1.430248368))
                Line((-1.4464523976, -1.4365368069), (0, 0))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a carabiner or snap hook with an elongated oval loop shape, featuring a curved metal body with textured grip surfaces on the rounded ends and a smooth interior channel for securing ropes or cables.
def model_139674_8774f1a3_0072():
    """Model: ????? ???? v1 (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.9269910596, perimeter: 35.7079637049
            with BuildLine():
                CenterArc((1, 0), 1.5000000075, 180, 180)
                Line((2.5000000373, 5.0000000745), (2.5000000373, 0))
                CenterArc((1.0000000149, 5.0000000745), 1.5000000224, 0, 180)
                Line((-0.5000000075, 0), (-0.5000000075, 5.0000000745))
            make_face()
            with BuildLine():
                Line((0, 0), (0, 5.0000000015))
                CenterArc((1.0000000149, 5.0000000745), 1.0000000149, 0, 180.0000041826)
                Line((2.0000000298, 5.0000000745), (2, 0))
                CenterArc((1, 0), 1, 180, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a disc or wheel component with a flat circular face and a textured or ribbed cylindrical rim along its edge, suggesting it may be a pulley, gear, or similar rotational mechanical part.
def model_139787_fca785f0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal block with chamfered or angled edges along its top surface, creating a faceted, wedge-like appearance.
def model_139801_97e2ca6a_0003():
    """Model: 9V Battery v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.25, perimeter: 14
            with BuildLine():
                Line((0, 4.5), (0, 0))
                Line((0, 0), (2.5, 0))
                Line((2.5, 0), (2.5, 4.5))
                Line((2.5, 4.5), (0, 4.5))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


# Description: This is a cylindrical or curved container/vessel with an open top, featuring a rounded bottom and curved sidewalls that taper slightly, with a wireframe top surface visible showing internal structural details.
def model_139801_97e2ca6a_0007():
    """Model: 9V Battery Connector v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5709733553, perimeter: 6.1699111843
            with BuildLine():
                Line((1.5000000045, 0.06), (0.9000000045, 0.06))
                Line((0.3000000045, 0.06), (0.9000000045, 0.06))
                CenterArc((0.3000000045, -0.54), 0.6, 90, 180)
                Line((0.3000000045, -1.14), (0.9000000045, -1.14))
                Line((1.5000000045, -1.14), (0.9000000045, -1.14))
                CenterArc((1.5000000045, -0.54), 0.6, -90, 180)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is an angular, faceted bracket or support component with an L-shaped or bent configuration, featuring sharp geometric planes and edges typical of a stamped or cast metal part designed to provide structural support or mounting functionality.
def model_139852_e9b59447_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.75, perimeter: 22.8994949366
            with BuildLine():
                Line((0, 0), (6, 0))
                Line((6, 0), (8, 2))
                Line((6, 4), (8, 2))
                Line((4.5, 2.5), (6, 4))
                Line((3, 4), (4.5, 2.5))
                Line((0, 4), (3, 4))
                Line((0, 0), (0, 4))
            make_face()
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a wedge-shaped or trapezoidal prism block with a tapered profile, featuring a slanted top surface and a hollowed or recessed upper cavity, commonly used as a support bracket, angled spacer, or structural component in assemblies.
def model_139863_77335f61_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 71.5, perimeter: 35
            with BuildLine():
                Line((6, -1.5), (-5, -1.5))
                Line((6, 5), (6, -1.5))
                Line((-5, 5), (6, 5))
                Line((-5, -1.5), (-5, 5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a long, slender rectangular prism or beam with a hexagonal cross-section, featuring a central longitudinal slot or groove running along its length.
def model_139918_b1e05e80_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 180.9, perimeter: 77.8
            with BuildLine():
                Line((0, 5.4), (0, 0))
                Line((0, 0), (33.5, 0))
                Line((33.5, 0), (33.5, 5.4))
                Line((33.5, 5.4), (0, 5.4))
            make_face()
        # OneSide extrude, distance=5.4
        extrude(amount=5.4)
    return part.part


MODELS = {
    "model_135230_c38e50b2_0000": {"func": model_135230_c38e50b2_0000, "volume": 80.44036, "area": 126.7636},
    "model_135445_77b4ac77_0000": {"func": model_135445_77b4ac77_0000, "volume": 0.434, "area": 9.58},
    "model_135514_12de81ba_0001": {"func": model_135514_12de81ba_0001, "volume": 39000, "area": 19705.7607215608},
    "model_135518_26ac8077_0000": {"func": model_135518_26ac8077_0000, "volume": 72.8152019337, "area": 221.0044962233},
    "model_135538_9913818f_0003": {"func": model_135538_9913818f_0003, "volume": 1935.721935, "area": 2041.9314},
    "model_135538_9913818f_0005": {"func": model_135538_9913818f_0005, "volume": 8259.080256, "area": 4077.4112},
    "model_135538_9913818f_0012": {"func": model_135538_9913818f_0012, "volume": 585.1802397349, "area": 609.8338321797},
    "model_135538_9913818f_0013": {"func": model_135538_9913818f_0013, "volume": 391.75324875, "area": 420.16045},
    "model_135538_9913818f_0018": {"func": model_135538_9913818f_0018, "volume": 1573.158144, "area": 1290.32},
    "model_135538_9913818f_0021": {"func": model_135538_9913818f_0021, "volume": 23448.8643925, "area": 10596.9262756218},
    "model_135630_863a2309_0000": {"func": model_135630_863a2309_0000, "volume": 139.7200638046, "area": 251.0112392349},
    "model_135872_a6ca0e40_0000": {"func": model_135872_a6ca0e40_0000, "volume": 441.8761065788, "area": 593.6353960533},
    "model_135872_a6ca0e40_0001": {"func": model_135872_a6ca0e40_0001, "volume": 10061.7594072257, "area": 33716.4926784315},
    "model_135872_a6ca0e40_0002": {"func": model_135872_a6ca0e40_0002, "volume": 1122.6902664471, "area": 1396.0884901332},
    "model_135872_a6ca0e40_0004": {"func": model_135872_a6ca0e40_0004, "volume": 593.4902664471, "area": 808.0884901332},
    "model_135872_a6ca0e40_0006": {"func": model_135872_a6ca0e40_0006, "volume": 1908.2902664471, "area": 2271.8207955577},
    "model_135872_a6ca0e40_0014": {"func": model_135872_a6ca0e40_0014, "volume": 7747.5547435638, "area": 25984.8414090289},
    "model_135872_a6ca0e40_0016": {"func": model_135872_a6ca0e40_0016, "volume": 135.072, "area": 169.08},
    "model_135896_ecae901d_0000": {"func": model_135896_ecae901d_0000, "volume": 86.2026000827, "area": 133.8500001014},
    "model_136015_20ead420_0001": {"func": model_136015_20ead420_0001, "volume": 1.586544075, "area": 12.5099334165},
    "model_136128_831e37a6_0000": {"func": model_136128_831e37a6_0000, "volume": 79.6323159987, "area": 258.2570399551},
    "model_136204_cd4e55ea_0000": {"func": model_136204_cd4e55ea_0000, "volume": 41.504061876, "area": 192.4994530328},
    "model_136206_3113969f_0001": {"func": model_136206_3113969f_0001, "volume": 1.5707963268, "area": 7.853981634},
    "model_136206_3113969f_0003": {"func": model_136206_3113969f_0003, "volume": 32.8584073464, "area": 108.2831853072},
    "model_136206_911a4e4d_0000": {"func": model_136206_911a4e4d_0000, "volume": 175.469383848, "area": 460.369406282},
    "model_136206_b333b31e_0000": {"func": model_136206_b333b31e_0000, "volume": 222.9144304957, "area": 334.0097660976},
    "model_136288_6364ea63_0002": {"func": model_136288_6364ea63_0002, "volume": 12.8094967667, "area": 67.5041042579},
    "model_136312_6a0f8b1b_0000": {"func": model_136312_6a0f8b1b_0000, "volume": 15.7872875775, "area": 178.5725848815},
    "model_136337_1351909b_0001": {"func": model_136337_1351909b_0001, "volume": 0.4690357969, "area": 10.3642678897},
    "model_136337_1351909b_0005": {"func": model_136337_1351909b_0005, "volume": 0.0196349541, "area": 0.5497787144},
    "model_136343_567984b9_0000": {"func": model_136343_567984b9_0000, "volume": 55.848, "area": 573.88},
    "model_136355_b5fd1a59_0000": {"func": model_136355_b5fd1a59_0000, "volume": 1.27575, "area": 18.855},
    "model_136355_b5fd1a59_0002": {"func": model_136355_b5fd1a59_0002, "volume": 0.015625, "area": 0.375},
    "model_136355_b5fd1a59_0004": {"func": model_136355_b5fd1a59_0004, "volume": 0.00275, "area": 0.225},
    "model_136485_5ef7e95a_0000": {"func": model_136485_5ef7e95a_0000, "volume": 0.9621127502, "area": 20.341812432},
    "model_136499_954c9245_0000": {"func": model_136499_954c9245_0000, "volume": 0.1627752137, "area": 1.9536857473},
    "model_136562_bdd2c987_0000": {"func": model_136562_bdd2c987_0000, "volume": 35.4061459768, "area": 238.9205850841},
    "model_136627_98da0c2f_0000": {"func": model_136627_98da0c2f_0000, "volume": 23.6493048182, "area": 125.0300704673},
    "model_136640_16741d62_0000": {"func": model_136640_16741d62_0000, "volume": 33750, "area": 6825},
    "model_136653_11d77223_0000": {"func": model_136653_11d77223_0000, "volume": 18900, "area": 4680},
    "model_136716_076bbbb3_0006": {"func": model_136716_076bbbb3_0006, "volume": 0.04, "area": 1.81},
    "model_136800_c5e4d711_0000": {"func": model_136800_c5e4d711_0000, "volume": 31.4159265359, "area": 56.5486677646},
    "model_136821_0f4b88d0_0007": {"func": model_136821_0f4b88d0_0007, "volume": 664.23274556, "area": 676.8482368106},
    "model_136834_9ebedb8b_0006": {"func": model_136834_9ebedb8b_0006, "volume": 197.4, "area": 243.8},
    "model_136886_3194fe8e_0000": {"func": model_136886_3194fe8e_0000, "volume": 508, "area": 2141},
    "model_136886_3aa46890_0000": {"func": model_136886_3aa46890_0000, "volume": 0.045, "area": 0.78},
    "model_136900_4fe212e6_0001": {"func": model_136900_4fe212e6_0001, "volume": 112.6247464884, "area": 570.443426002},
    "model_136900_4fe212e6_0002": {"func": model_136900_4fe212e6_0002, "volume": 6526.148238, "area": 7311.2757},
    "model_136900_4fe212e6_0005": {"func": model_136900_4fe212e6_0005, "volume": 450.4989859536, "area": 2259.6034783215},
    "model_136900_4fe212e6_0010": {"func": model_136900_4fe212e6_0010, "volume": 17501.384352, "area": 19307.7562484909},
    "model_136913_72e7b367_0000": {"func": model_136913_72e7b367_0000, "volume": 10.6028752059, "area": 31.8086256176},
    "model_136963_ff9b11e8_0000": {"func": model_136963_ff9b11e8_0000, "volume": 4.501294748, "area": 46.7791358647},
    "model_136964_8bb2b432_0000": {"func": model_136964_8bb2b432_0000, "volume": 51.7175772851, "area": 112.2198622731},
    "model_136980_9660c50c_0001": {"func": model_136980_9660c50c_0001, "volume": 834.4855486098, "area": 1335.1768777757},
    "model_136980_9660c50c_0002": {"func": model_136980_9660c50c_0002, "volume": 658.2618356975, "area": 1111.7311002891},
    "model_136980_9660c50c_0003": {"func": model_136980_9660c50c_0003, "volume": 1767.1458676443, "area": 2120.5750411731},
    "model_136994_22d5d740_0000": {"func": model_136994_22d5d740_0000, "volume": 9000, "area": 2700},
    "model_136994_22d5d740_0001": {"func": model_136994_22d5d740_0001, "volume": 11.88, "area": 42.18},
    "model_136994_a3a2f50f_0008": {"func": model_136994_a3a2f50f_0008, "volume": 1020, "area": 1370},
    "model_137088_d7fc9a5b_0001": {"func": model_137088_d7fc9a5b_0001, "volume": 77750.4336216375, "area": 12721.5994509838},
    "model_137098_0a45d1c8_0004": {"func": model_137098_0a45d1c8_0004, "volume": 0.5444264007, "area": 10.8747450264},
    "model_137098_0a45d1c8_0013": {"func": model_137098_0a45d1c8_0013, "volume": 0.1555088364, "area": 2.2148228208},
    "model_137098_0a45d1c8_0014": {"func": model_137098_0a45d1c8_0014, "volume": 0.1583362697, "area": 2.7294156974},
    "model_137098_0a45d1c8_0017": {"func": model_137098_0a45d1c8_0017, "volume": 2.8274333882, "area": 57.1141544423},
    "model_137098_0a45d1c8_0018": {"func": model_137098_0a45d1c8_0018, "volume": 4.5238934212, "area": 91.043355101},
    "model_137098_0a45d1c8_0019": {"func": model_137098_0a45d1c8_0019, "volume": 0.4319689899, "area": 3.8484510006},
    "model_137141_748596d0_0006": {"func": model_137141_748596d0_0006, "volume": 0.0046088617, "area": 0.2983865},
    "model_137211_d47bba3f_0001": {"func": model_137211_d47bba3f_0001, "volume": 1.5599124689, "area": 13.5313383087},
    "model_137403_81c69c1f_0000": {"func": model_137403_81c69c1f_0000, "volume": 24.48537, "area": 255.2333833388},
    "model_137426_1d583698_0000": {"func": model_137426_1d583698_0000, "volume": 5625, "area": 1950},
    "model_137445_368e129e_0000": {"func": model_137445_368e129e_0000, "volume": 61.5, "area": 290},
    "model_137445_4395e806_0000": {"func": model_137445_4395e806_0000, "volume": 0.4437577535, "area": 6.6414917405},
    "model_137448_0f2fd70e_0000": {"func": model_137448_0f2fd70e_0000, "volume": 32.7885397663, "area": 203.8683612739},
    "model_137605_b2c5f816_0000": {"func": model_137605_b2c5f816_0000, "volume": 15.625, "area": 37.5},
    "model_137724_20be6062_0002": {"func": model_137724_20be6062_0002, "volume": 39.6493800988, "area": 277.5456606917},
    "model_137724_20be6062_0003": {"func": model_137724_20be6062_0003, "volume": 270.9374306752, "area": 1819.4659978679},
    "model_137837_9c9f163d_0000": {"func": model_137837_9c9f163d_0000, "volume": 409.6, "area": 441.6},
    "model_137837_9c9f163d_0002": {"func": model_137837_9c9f163d_0002, "volume": 15, "area": 53},
    "model_137837_9c9f163d_0006": {"func": model_137837_9c9f163d_0006, "volume": 288, "area": 644},
    "model_137837_9c9f163d_0008": {"func": model_137837_9c9f163d_0008, "volume": 625, "area": 550},
    "model_137837_9c9f163d_0009": {"func": model_137837_9c9f163d_0009, "volume": 1562.5, "area": 1500},
    "model_137846_46d17568_0000": {"func": model_137846_46d17568_0000, "volume": 10.3, "area": 60.6597979746},
    "model_138071_f8d5a493_0002": {"func": model_138071_f8d5a493_0002, "volume": 112.476, "area": 172.22},
    "model_138138_3d94bb12_0000": {"func": model_138138_3d94bb12_0000, "volume": 11749.5565244258, "area": 2869.5455217674},
    "model_138143_48d4dcd5_0000": {"func": model_138143_48d4dcd5_0000, "volume": 7.7000541905, "area": 30.4905979523},
    "model_138150_55b9f95f_0000": {"func": model_138150_55b9f95f_0000, "volume": 37.5, "area": 70},
    "model_138154_c30b80d3_0000": {"func": model_138154_c30b80d3_0000, "volume": 11.384600645, "area": 73.3402818208},
    "model_138289_9b76f4fd_0000": {"func": model_138289_9b76f4fd_0000, "volume": 693, "area": 478},
    "model_138451_7b6845cd_0000": {"func": model_138451_7b6845cd_0000, "volume": 50.2654824574, "area": 125.6637061436},
    "model_138535_c0da19b3_0012": {"func": model_138535_c0da19b3_0012, "volume": 0.9424777961, "area": 8.4823001647},
    "model_138559_520601c9_0000": {"func": model_138559_520601c9_0000, "volume": 362.337748622, "area": 313.2057875358},
    "model_138561_5abbe69a_0000": {"func": model_138561_5abbe69a_0000, "volume": 1090.125, "area": 635.1952930702},
    "model_138562_03f863fb_0000": {"func": model_138562_03f863fb_0000, "volume": 120, "area": 168},
    "model_138598_71a570e5_0000": {"func": model_138598_71a570e5_0000, "volume": 506.25, "area": 407.1635367144},
    "model_138599_fe19d5c7_0000": {"func": model_138599_fe19d5c7_0000, "volume": 357, "area": 305},
    "model_138633_a2a11904_0000": {"func": model_138633_a2a11904_0000, "volume": 448.5, "area": 365.5},
    "model_138636_c1153075_0000": {"func": model_138636_c1153075_0000, "volume": 462, "area": 370},
    "model_138675_8f140033_0000": {"func": model_138675_8f140033_0000, "volume": 331.5, "area": 290.5},
    "model_138680_1a4395e8_0000": {"func": model_138680_1a4395e8_0000, "volume": 421.8430534713, "area": 340.7996890796},
    "model_138682_b210e304_0000": {"func": model_138682_b210e304_0000, "volume": 485.8236732007, "area": 388.4449162502},
    "model_138684_b2780d91_0000": {"func": model_138684_b2780d91_0000, "volume": 322.442168037, "area": 296.3141219625},
    "model_138685_fd9b79cd_0000": {"func": model_138685_fd9b79cd_0000, "volume": 224.0305728742, "area": 228.3752273419},
    "model_138688_840e870e_0000": {"func": model_138688_840e870e_0000, "volume": 180, "area": 202},
    "model_138698_e190e3eb_0000": {"func": model_138698_e190e3eb_0000, "volume": 57.3298, "area": 102.4834355269},
    "model_138713_3ac3915b_0000": {"func": model_138713_3ac3915b_0000, "volume": 455, "area": 361},
    "model_138714_15a003f6_0000": {"func": model_138714_15a003f6_0000, "volume": 297, "area": 273},
    "model_138720_1ba95e19_0000": {"func": model_138720_1ba95e19_0000, "volume": 420.75, "area": 362.5},
    "model_138723_787cbfa9_0000": {"func": model_138723_787cbfa9_0000, "volume": 173.25, "area": 189.5},
    "model_138724_99a5d09c_0000": {"func": model_138724_99a5d09c_0000, "volume": 198, "area": 209.5},
    "model_138725_4382f988_0000": {"func": model_138725_4382f988_0000, "volume": 498.4568927413, "area": 413.7106094534},
    "model_138739_ef445038_0000": {"func": model_138739_ef445038_0000, "volume": 306, "area": 276},
    "model_138742_85e709ec_0000": {"func": model_138742_85e709ec_0000, "volume": 233.75, "area": 233.5},
    "model_138771_38afab8e_0000": {"func": model_138771_38afab8e_0000, "volume": 3000, "area": 2960},
    "model_138771_38afab8e_0011": {"func": model_138771_38afab8e_0011, "volume": 1250, "area": 1525},
    "model_138771_38afab8e_0013": {"func": model_138771_38afab8e_0013, "volume": 10.2414815568, "area": 74.4901960895},
    "model_138885_72845989_0000": {"func": model_138885_72845989_0000, "volume": 4.7726424609, "area": 24.8763330754},
    "model_138946_b45b2c50_0002": {"func": model_138946_b45b2c50_0002, "volume": 783.5064988844, "area": 899.9982015261},
    "model_138946_b45b2c50_0005": {"func": model_138946_b45b2c50_0005, "volume": 14794.4462175, "area": 16599.16035},
    "model_138946_b45b2c50_0006": {"func": model_138946_b45b2c50_0006, "volume": 261.1688325, "area": 437.0959},
    "model_138946_b45b2c50_0007": {"func": model_138946_b45b2c50_0007, "volume": 3415.16655675, "area": 3912.08895},
    "model_138947_0778db40_0000": {"func": model_138947_0778db40_0000, "volume": 436813.577984, "area": 38657.9872},
    "model_138947_0778db40_0001": {"func": model_138947_0778db40_0001, "volume": 13899.9995666026, "area": 4013.1232344522},
    "model_138947_0778db40_0002": {"func": model_138947_0778db40_0002, "volume": 19271.187264, "area": 14587.0676},
    "model_138947_0778db40_0004": {"func": model_138947_0778db40_0004, "volume": 210606.5465279999, "area": 21819.3112},
    "model_139005_7b6aa20e_0000": {"func": model_139005_7b6aa20e_0000, "volume": 0.2513274123, "area": 6.5345127195},
    "model_139093_f71ea5d2_0002": {"func": model_139093_f71ea5d2_0002, "volume": 3, "area": 36.4},
    "model_139116_5f441b87_0000": {"func": model_139116_5f441b87_0000, "volume": 30.8998829103, "area": 350.8291589214},
    "model_139155_1a724258_0000": {"func": model_139155_1a724258_0000, "volume": 277.5770475252, "area": 922.8792815102},
    "model_139222_2c10ca9a_0017": {"func": model_139222_2c10ca9a_0017, "volume": 26882.8768410653, "area": 54369.5546256505},
    "model_139222_2c10ca9a_0018": {"func": model_139222_2c10ca9a_0018, "volume": 212.0575041173, "area": 296.8805057642},
    "model_139258_43c33f60_0037": {"func": model_139258_43c33f60_0037, "volume": 15246.35, "area": 6046.6},
    "model_139379_fe5c3f64_0000": {"func": model_139379_fe5c3f64_0000, "volume": 1253.4954687823, "area": 2645.2210143226},
    "model_139379_fe5c3f64_0001": {"func": model_139379_fe5c3f64_0001, "volume": 39.2699083632, "area": 158.6504294006},
    "model_139610_e43b543c_0000": {"func": model_139610_e43b543c_0000, "volume": 500, "area": 400},
    "model_139674_8774f1a3_0019": {"func": model_139674_8774f1a3_0019, "volume": 1000, "area": 847.2135955},
    "model_139674_8774f1a3_0027": {"func": model_139674_8774f1a3_0027, "volume": 331052.3398600462, "area": 53399.2504797801},
    "model_139674_8774f1a3_0041": {"func": model_139674_8774f1a3_0041, "volume": 0.8, "area": 17.788854382},
    "model_139674_8774f1a3_0060": {"func": model_139674_8774f1a3_0060, "volume": 1.2327918195, "area": 10.6512215297},
    "model_139674_8774f1a3_0072": {"func": model_139674_8774f1a3_0072, "volume": 4.4634955678, "area": 35.7079639717},
    "model_139787_fca785f0_0000": {"func": model_139787_fca785f0_0000, "volume": 0.9424777961, "area": 8.1681408993},
    "model_139801_97e2ca6a_0003": {"func": model_139801_97e2ca6a_0003, "volume": 19.125, "area": 46.3},
    "model_139801_97e2ca6a_0007": {"func": model_139801_97e2ca6a_0007, "volume": 3.0851680264, "area": 12.5458401318},
    "model_139852_e9b59447_0000": {"func": model_139852_e9b59447_0000, "volume": 25.75, "area": 74.3994949366},
    "model_139863_77335f61_0000": {"func": model_139863_77335f61_0000, "volume": 178.75, "area": 230.5},
    "model_139918_b1e05e80_0000": {"func": model_139918_b1e05e80_0000, "volume": 976.86, "area": 781.92},
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
