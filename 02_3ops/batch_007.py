"""Batch 007 - passing/02_3ops
60 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a circular mesh or perforated filter plate with an elliptical/oval shape, featuring a flat rim around the edges and a fine mesh or perforated surface covering the central area.
def model_78513_7ad0bd6a_0001():
    """Model: fram"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.9225651046, perimeter: 59.6902604182
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.6340701482, perimeter: 16.9646003294
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 53.4384910376, perimeter: 39.5840674352
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a motorcycle or powersports seat cover featuring an ergonomic contoured shape with a dark gray base, blue mesh or ventilation pattern design, and curved surfaces that conform to a rider's seating position.
def model_78513_7ad0bd6a_0003():
    """Model: plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 58.517294468, perimeter: 86.0901969785
            with BuildLine():
                CenterArc((-5.1, -4.2), 1.2, 155.810485846, 116.1786959545)
                Line((-5.0583470425, -5.3992768784), (5.0999145777, -5.399999997))
                CenterArc((5.1, -4.2), 1.2, -90.0040786152, 114.1935927692)
                CenterArc((14.45, 0), 9.05, 155.810485846, 48.379028308)
                CenterArc((5.1, 4.2), 1.2, -24.189514154, 114.1935927692)
                Line((-5.0583470425, 5.3992768784), (5.0999145777, 5.399999997))
                CenterArc((-5.1, 4.2), 1.2, 88.0108181995, 116.1786959545)
                CenterArc((-14.45, 0), 9.05, -24.189514154, 48.379028308)
            make_face()
            with BuildLine():
                CenterArc((5.1, 4.2), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.1, -4.2), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.1, -4.2), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.1, 4.2), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.6340701482, perimeter: 16.9646003294
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 53.4384910376, perimeter: 39.5840674352
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.45
        extrude(amount=0.45, both=True, mode=Mode.ADD)
    return part.part


# Description: This is an elliptical or oval-shaped pad or cushion with a flat base and gently curved top surface, featuring a textured or mesh-like pattern across its upper face.
def model_78865_cb0167cd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.0788682782, perimeter: 25.4469004941
            with BuildLine():
                CenterArc((0, 0), 3.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 2.9), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a dual-loop pulley or cable guide with two circular openings at the top, a tapered body that narrows toward the bottom, and internal ribbing for structural reinforcement.
def model_79423_62db5fc6_0009():
    """Model: 2-33-TRACK ROD YOKE END"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.48, perimeter: 2.8
            with BuildLine():
                Line((6.4, 0.4), (6.4, -0.4))
                Line((6.4, 0.4), (5.8, 0.4))
                Line((5.8, 0.4), (5.8, -0.4))
                Line((5.8, -0.4), (6.4, -0.4))
            make_face()
            # Profile area: 0.6149778714, perimeter: 5.0274333882
            with BuildLine():
                CenterArc((7.1, 0), 0.4, -90, 180)
                Line((7.1, 0.4), (6.4, 0.4))
                Line((6.4, 0.4), (6.4, -0.4))
                Line((6.4, -0.4), (7.1, -0.4))
            make_face()
            with BuildLine():
                CenterArc((7.1, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.9
        extrude(amount=0.45, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.6149778714, perimeter: 5.0274333882
            with BuildLine():
                CenterArc((7.1, 0), 0.4, -90, 180)
                Line((7.1, 0.4), (6.4, 0.4))
                Line((6.4, 0.4), (6.4, -0.4))
                Line((6.4, -0.4), (7.1, -0.4))
            make_face()
            with BuildLine():
                CenterArc((7.1, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a U-shaped bracket or mounting block with a rectangular cross-section, featuring two large circular holes through the legs and internal diagonal reinforcement ribs, designed for structural support and fastening applications.
def model_79423_62db5fc6_0011():
    """Model: 2-35-STEERING PUSH ROD YOKE END"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6836504592, perimeter: 5.3707963268
            with BuildLine():
                Line((0.4, -0.6), (0.4, -1.7))
                Line((-0.4, -0.6), (0.4, -0.6))
                Line((-0.4, -1.7), (-0.4, -0.6))
                Line((0.4, -1.7), (-0.4, -1.7))
            make_face()
            with BuildLine():
                CenterArc((0, -1.3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.48, perimeter: 2.8
            with BuildLine():
                Line((0.4, 0), (0.4, -0.6))
                Line((-0.4, 0), (0.4, 0))
                Line((-0.4, -0.6), (-0.4, 0))
                Line((-0.4, -0.6), (0.4, -0.6))
            make_face()
        # Symmetric extrude, full_length=True, total=0.9
        extrude(amount=0.45, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6836504592, perimeter: 5.3707963268
            with BuildLine():
                Line((0.4, -0.6), (0.4, -1.7))
                Line((-0.4, -0.6), (0.4, -0.6))
                Line((-0.4, -1.7), (-0.4, -0.6))
                Line((0.4, -1.7), (-0.4, -1.7))
            make_face()
            with BuildLine():
                CenterArc((0, -1.3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a horizontal bar or shaft component with rounded cylindrical end caps on both sides, a blue accent stripe along the top surface, and an arrow or pointer extending from the left end, featuring a streamlined, modern design typical of a control slider or handle mechanism.
def model_79423_62db5fc6_0015():
    """Model: 1-30 FRONT WHEEL FIXED AXLE BEAM"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-5.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((5.4, 0)):
                Circle(0.2)
        # OneSide extrude, distance=2.25
        extrude(amount=2.25)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.1685840735, perimeter: 37.8247779608
            with BuildLine():
                CenterArc((-7.1, 0), 0.5, 90, 180)
                Line((-7.1, -0.5), (7.1, -0.5))
                CenterArc((7.1, 0), 0.5, -90, 180)
                Line((7.1, 0.5), (-7.1, 0.5))
            make_face()
            with BuildLine():
                CenterArc((7.1, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.1, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular mounting bracket or frame with rounded corners, featuring a central recessed rectangular cavity, four corner mounting holes, and curved flanges or edges that suggest a plastic or molded composite construction.
def model_79637_fac1d5d3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.0297591563, perimeter: 19.4446173983
            with BuildLine():
                CenterArc((-1.5, 1), 0.5, 90, 90)
                Line((-2, -1), (-2, 1))
                CenterArc((-1.5, -1), 0.5, 180, 90)
                Line((1.5099197188, -1.5), (-1.5, -1.5))
                CenterArc((1.5099197188, -1), 0.5, -90, 90)
                Line((2.0099197188, 1), (2.0099197188, -1))
                CenterArc((1.5099197188, 1), 0.5, 0, 90)
                Line((-1.5, 1.5), (1.5099197188, 1.5))
            make_face()
            with BuildLine():
                CenterArc((1.5099197188, -1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, -1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5099197188, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.4968409387, 0.9974838516), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)
    return part.part


# Description: This is a solar-powered outdoor wall sconce featuring a curved, rounded base (dark gray) that houses the battery and electronics, topped with an angled solar panel array (light blue) that tilts upward for optimal sun exposure, designed for mounting on vertical surfaces.
def model_80188_c67d0fb1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 513.7780263365, perimeter: 198.2401385897
            with BuildLine():
                Line((21.9287086715, -12.4203849365), (22.2128345772, -8.5677429545))
                CenterArc((32.5, -13.2), 10.6, 175.7821676542, 189.2041644064)
                Line((43.0598838844, -12.2786681667), (42.7419443308, -8.6345904874))
                CenterArc((47.7230216348, -8.2), 5, 90, 94.9863320606)
                Line((65, -3.2), (47.7230216348, -3.2))
                Line((65, 0), (65, -3.2))
                Line((0, 0), (65, 0))
                Line((0, 0), (0, -3.2))
                Line((0, -3.2), (17.2263764034, -3.2))
                CenterArc((17.2263764034, -8.2), 5, -4.2178323458, 94.2178323458)
            make_face()
            with BuildLine():
                CenterArc((32.5, -13.2), 5.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a structural support bracket or gusset plate with a complex geometric shape featuring triangular bracing elements, a vertical reinforced flange with ribbed detailing, and cable or wire attachment points, designed to provide rigid support and load distribution in a framework assembly.
def model_80497_abe71aa5_0001():
    """Model: 箱体"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 98.0685834706, perimeter: 37.4247779608
            with BuildLine():
                CenterArc((3.5, 3.5), 1.5, 0, 90)
                Line((3.5, 5), (-3.5, 5))
                CenterArc((-3.5, 3.5), 1.5, 90, 90)
                Line((-5, 3.5), (-5, -3.5))
                CenterArc((-3.5, -3.5), 1.5, -180, 90)
                Line((-3.5, -5), (3.5, -5))
                CenterArc((3.5, -3.5), 1.5, -90, 90)
                Line((5, -3.5), (5, 3.5))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9)
    return part.part


# Description: This is a 3D CAD part consisting of two triangular pyramidal (tetrahedral) sections joined together at a right angle, forming an L-shaped or corner bracket-like structure with faceted surfaces and internal edge definitions.
def model_80755_807d96f0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.8225176033, perimeter: 14.4712062973
            with BuildLine():
                Line((3.6585071726, 0.7263307286), (3.6585071726, 0))
                Line((0.7717242921, 0.7263307286), (3.6585071726, 0.7263307286))
                Line((0.7717242921, 3.5893832515), (0.7717242921, 0.7263307286))
                Line((0.024659255, 3.5893832515), (0.7717242921, 3.5893832515))
                Line((0, 0), (0.024659255, 3.5893832515))
                Line((3.6585071726, 0), (0, 0))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is a bracket or support stand with an L-shaped profile consisting of a vertical rectangular plate and a horizontal base plate joined at a right angle, featuring triangulated internal geometry for structural reinforcement.
def model_80756_6f2e842f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12, perimeter: 26
            with BuildLine():
                Line((-0.5, 5), (-1.5, 5))
                Line((-1.5, 5), (-1.5, -2.5))
                Line((-1.5, -2.5), (4, -2.5))
                Line((4, -2.5), (4, -1.5))
                Line((4, -1.5), (-0.5, -1.5))
                Line((-0.5, -1.5), (-0.5, 5))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a leaf spring or curved deflector component featuring an elongated oval top surface with fine mesh detailing, mounted on a rectangular base with two distinct support blocks underneath, designed to redirect or manage fluid or air flow.
def model_80763_97f05760_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 83.1445984574, perimeter: 43.0212373508
            with BuildLine():
                CenterArc((0, -1.8000000268), 0.8000000119, 0, 180)
                Line((0.8000000119, -1.8000000268), (0.8000000119, -5))
                Line((5, -5), (0.8000000119, -5))
                Line((5, 0), (5, -5))
                CenterArc((0, 0), 5, 0, 180)
                Line((-5, 0), (-5, -5))
                Line((-5, -5), (-0.8000000119, -5))
                Line((-0.8000000119, -1.8000000268), (-0.8000000119, -5))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a cylindrical container or sleeve with an open top, featuring a flat base and curved sidewalls with vertical ribbing or fluting for structural reinforcement.
def model_80765_1b57e0b1_0000():
    """Model: 耳机挂钩"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a cylindrical sleeve or tube with a textured grid pattern on the top circular end, featuring a smooth dark body and tapered or beveled edges at both ends.
def model_80765_1b57e0b1_0001():
    """Model: 耳机"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 38.4845111534, perimeter: 21.9911489028
            Circle(3.5000000522)
        # TwoSides extrude, along=17.5, against=-10
        extrude(amount=17.5)
        extrude(sk.sketch, amount=-10)
    return part.part


# Description: This is a torus (donut-shaped) component featuring a smooth, curved ring geometry with a central hole and fine radial surface texturing that suggests a functional or aesthetic finish.
def model_80767_2a27abc1_0000():
    """Model: 基座"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 71.4712328692, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)
    return part.part


# Description: This is an elongated rectangular box or tray with an open top, featuring an internal dividing wall or partition that runs lengthwise down the center, creating two separate compartments.
def model_81123_41bb9143_0008():
    """Model: 03-REAR PLATE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.2, perimeter: 26
            with BuildLine():
                Line((3.9, -5.5), (3.7, -5.5))
                Line((3.9, -7), (3.9, -5.5))
                Line((4.5, -7), (3.9, -7))
                Line((4.5, 0), (4.5, -7))
                Line((0, 0), (4.5, 0))
                Line((0, -7), (0, 0))
                Line((3.7, -7), (0, -7))
                Line((3.7, -5.5), (3.7, -7))
            make_face()
        # Symmetric extrude, full_length=True, total=0.8
        extrude(amount=0.4, both=True)
    return part.part


# Description: A dark blue rectangular block or plate with rounded corners and edges, featuring a slightly tapered or beveled top surface and a smooth, minimalist design with no visible holes or slots.
def model_81224_f2807572_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 118.970046553, perimeter: 44.9708393871
            with BuildLine():
                CenterArc((-3.0678169543, -6.8648605247), 0.8351394753, -166.534881596, 76.534881596)
                Line((3.0678169543, -7.7), (-3.0678169543, -7.7))
                CenterArc((3.0678169543, -6.8648605247), 0.8351394753, -90, 76.534881596)
                Line((3.88, 7.0593255435), (3.88, -7.0593255435))
                CenterArc((3.0678169543, 6.8648605247), 0.8351394753, 13.465118404, 76.534881596)
                Line((-3.0678169543, 7.7), (3.0678169543, 7.7))
                CenterArc((-3.0678169543, 6.8648605247), 0.8351394753, 90, 76.534881596)
                Line((-3.88, -7.0593255435), (-3.88, 7.0593255435))
            make_face()
        # Symmetric extrude, each_side=0.54
        extrude(amount=0.54, both=True)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a simple rectangular form and no distinctive features, holes, or slots.
def model_82041_6a8544dd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 41400, perimeter: 820
            with BuildLine():
                Line((114.9851844572, -96.5996772594), (-115.0148155428, -96.5996772594))
                Line((114.9851844572, 83.4003227406), (114.9851844572, -96.5996772594))
                Line((-115.0148155428, 83.4003227406), (114.9851844572, 83.4003227406))
                Line((-115.0148155428, -96.5996772594), (-115.0148155428, 83.4003227406))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a cylindrical capsule-shaped component with two hemispherical ends and a central rectangular slot or channel running through its length, featuring a dark gray body with blue highlight details on the curved end surfaces.
def model_82169_acef7d14_0001():
    """Model: Koleso v1"""
    with BuildPart() as part:
        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 75.3982236862, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=15
        extrude(amount=7.5, both=True)
    return part.part


# Description: This is a curved aerodynamic fairing or duct component with an elongated, streamlined shape featuring a textured mesh or perforated upper surface and a solid dark base, designed for airflow management or protective covering in a mechanical assembly.
def model_82177_11e98151_0000():
    """Model: serce v2 v1"""
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
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.0579898929, perimeter: 17.7551617687
            with BuildLine():
                _nurbs_edge([(-0.0563558443, -3.6770451626), (-0.0213523325, -3.6519967297), (0.0479972729, -3.601394134), (0.1500492738, -3.5239730948), (0.2821719493, -3.4177079301), (0.440960714, -3.2797224421), (0.5940817307, -3.1363236431), (0.742910627, -2.9870235574), (0.8898676235, -2.8309951997), (1.038128706, -2.6671498845), (1.1908361438, -2.4943585357), (1.3504262964, -2.3116386317), (1.5179666702, -2.1183405867), (1.6923310106, -1.9143755626), (1.8706481851, -1.7001138735), (2.0490523261, -1.476205505), (2.2233253322, -1.2434289161), (2.389582914, -1.0025289054), (2.5449418664, -0.7540598145), (2.6882003813, -0.4982257464), (2.8191796217, -0.2350735503), (2.9380615437, 0.0353129887), (3.0447400668, 0.3126209558), (3.1381447187, 0.596110229), (3.2156259161, 0.8844260789), (3.2721707242, 1.1753789864), (3.3014999648, 1.466075414), (3.2973814853, 1.7530875937), (3.2548655438, 2.0326075454), (3.1715597676, 2.3006063249), (3.04889101, 2.5529905569), (2.8933989523, 2.7857597818), (2.7146422267, 2.9951733988), (2.5231742144, 3.1779163141), (2.3283750089, 3.3312725912), (2.1366257153, 3.4532865409), (1.948624392, 3.5429630056), (1.760090581, 3.6003295835), (1.5652829814, 3.6264045342), (1.3594872646, 3.623175175), (1.1424143406, 3.593624231), (0.9196531797, 3.5415876806), (0.6999880406, 3.4712158955), (0.4934484237, 3.3864939512), (0.3092493497, 3.2907855553), (0.1533381905, 3.1862492798), (0.0534682219, 3.0964050221), (-0.0070364152, 3.025695161), (-0.0409813725, 2.9770772901), (-0.0563558443, 2.9523989002)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.0563558443, -3.6770451626), (-0.0563558443, 2.9523989002))
            make_face()
            # Profile area: 17.0579898929, perimeter: 17.7551617687
            with BuildLine():
                Line((-0.0563558443, -3.6770451626), (-0.0563558443, 2.9523989002))
                _nurbs_edge([(-0.0563558443, -3.6770451626), (-0.091359356, -3.6519967297), (-0.1607089614, -3.601394134), (-0.2627609623, -3.5239730948), (-0.3948836378, -3.4177079301), (-0.5536724025, -3.2797224421), (-0.7067934192, -3.1363236431), (-0.8556223155, -2.9870235574), (-1.002579312, -2.8309951997), (-1.1508403945, -2.6671498845), (-1.3035478323, -2.4943585357), (-1.4631379849, -2.3116386317), (-1.6306783587, -2.1183405867), (-1.8050426991, -1.9143755626), (-1.9833598736, -1.7001138735), (-2.1617640146, -1.476205505), (-2.3360370207, -1.2434289161), (-2.5022946025, -1.0025289054), (-2.6576535549, -0.7540598145), (-2.8009120698, -0.4982257464), (-2.9318913102, -0.2350735503), (-3.0507732322, 0.0353129887), (-3.1574517553, 0.3126209558), (-3.2508564072, 0.596110229), (-3.3283376046, 0.8844260789), (-3.3848824127, 1.1753789864), (-3.4142116533, 1.466075414), (-3.4100931738, 1.7530875937), (-3.3675772323, 2.0326075454), (-3.2842714561, 2.3006063249), (-3.1616026985, 2.5529905569), (-3.0061106408, 2.7857597818), (-2.8273539152, 2.9951733988), (-2.6358859029, 3.1779163141), (-2.4410866974, 3.3312725912), (-2.2493374038, 3.4532865409), (-2.0613360805, 3.5429630056), (-1.8728022695, 3.6003295835), (-1.6779946699, 3.6264045342), (-1.4721989531, 3.623175175), (-1.2551260292, 3.593624231), (-1.0323648682, 3.5415876806), (-0.8126997291, 3.4712158955), (-0.6061601122, 3.3864939512), (-0.4219610382, 3.2907855553), (-0.266049879, 3.1862492798), (-0.1661799104, 3.0964050221), (-0.1056752733, 3.025695161), (-0.071730316, 2.9770772901), (-0.0563558443, 2.9523989002)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a long, flat rectangular metal plate or beam with a slightly tapered parallelogram shape, featuring a central slot or channel running along its length and reinforcing ribs or flanges on the underside.
def model_83338_b9bb889f_0001():
    """Model: Top Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 30 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 117.7651731519, perimeter: 72.5248670025
            with BuildLine():
                Line((33.655, 3.81), (33.655, 0))
                Line((33.655, 3.81), (2.69875, 3.81))
                Line((2.69875, 3.81), (2.69875, 0))
                Line((2.69875, 0), (33.655, 0))
            make_face()
            with BuildLine():
                CenterArc((22.463125, 1.905), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((31.115, 1.905), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((13.890625, 1.905), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.23875, 1.905), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 30 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.2822375, perimeter: 13.0175
            with BuildLine():
                Line((36.35375, 0), (36.35375, 3.81))
                Line((36.35375, 3.81), (33.655, 3.81))
                Line((33.655, 3.81), (33.655, 0))
                Line((33.655, 0), (36.35375, 0))
            make_face()
            # Profile area: 10.2822375, perimeter: 13.0175
            with BuildLine():
                Line((2.69875, 3.81), (2.69875, 0))
                Line((2.69875, 3.81), (0, 3.81))
                Line((0, 3.81), (0, 0))
                Line((0, 0), (2.69875, 0))
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular enclosure or case with a dark blue finish, featuring reinforced corner guards, internal ribbing for structural support, and what appears to be a mounting hole or access port on the top surface.
def model_83380_ab6e9bd8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 53.6799860357, perimeter: 45.8743499531
            with BuildLine():
                CenterArc((1.5, 8.1901016864), 1, 0, 90)
                Line((-2.0988827716, 9.1901016864), (1.5, 9.1901016864))
                CenterArc((-2.0988827716, 8.1901016864), 1, 90, 90)
                Line((-3.0988827716, 0), (-3.0988827716, 8.1901016864))
                CenterArc((-2.0988827716, 0), 1, -180, 90)
                Line((1.5, -1), (-2.0988827716, -1))
                CenterArc((1.5, 0), 1, -90, 90)
                Line((2.5, 8.1901016864), (2.5, 0))
            make_face()
            with BuildLine():
                Line((0.8000000119, 7.6000001132), (0.8000000119, 7.7000001147))
                Line((0.8000000119, 7.7000001147), (2.0000000298, 7.7000001147))
                Line((2.0000000298, 7.7000001147), (2.0000000298, 7.6000001132))
                Line((2.0000000298, 7.6000001132), (0.8000000119, 7.6000001132))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.6000000089, 7.3000001088), (0.6000000089, 7.5000001118))
                Line((0.6000000089, 7.5000001118), (2.0000000298, 7.5000001118))
                Line((2.0000000298, 7.5000001118), (2.0000000298, 7.3000001088))
                Line((2.0000000298, 7.3000001088), (0.6000000089, 7.3000001088))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.5, 7.7716578758), (0.5, 8))
                Line((0.5, 8), (1.9773915108, 8))
                Line((1.9773915108, 8), (1.9773915108, 7.7716578758))
                Line((1.9773915108, 7.7716578758), (0.5, 7.7716578758))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2, 7.2789615814), (-2, 8))
                Line((-2, 8), (-1.3452035372, 8))
                Line((-1.3452035372, 8), (-1.3452035372, 7.2789615814))
                Line((-1.3452035372, 7.2789615814), (-2, 7.2789615814))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.2243884446, 7.6042698323), 0.6445868477, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is an elliptical reinforced shell or composite component with a curved, boat-like shape featuring internal ribbing and structural bracing elements running radially from the center.
def model_83386_f927e369_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a rectangular prism or box-shaped solid block with a trapezoidal or wedge-like profile, featuring flat faces and sharp edges with no holes, slots, or curved surfaces visible.
def model_83406_87f89dc9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 72.7802757991, perimeter: 34.3569522463
            with BuildLine():
                Line((-3.7959370983, 4.7933009633), (-3.7959370983, -4.7933009633))
                Line((-3.7959370983, -4.7933009633), (3.7959370983, -4.7933009633))
                Line((3.7959370983, -4.7933009633), (3.7959370983, 4.7933009633))
                Line((3.7959370983, 4.7933009633), (-3.7959370983, 4.7933009633))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a 3D-rendered numeral "4" with a bold, rounded sans-serif typeface featuring thick strokes, curved corners, and a modern geometric design.
def model_83562_851e465d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch10 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30.6801045401, perimeter: 43.1216566233
            with BuildLine():
                Line((5.2565131611, -3.5130962501), (1.28748121, 3.5911374103))
                CenterArc((0.1787778004, 2.9717209514), 1.27, 29.1914568154, 60.8089671384)
                Line((0.1787684032, 4.2417209514), (-0.3752437701, 4.241716852))
                CenterArc((-0.3752343729, 2.9717168521), 1.27, 90.0004239537, 60.4282659472)
                Line((-1.479806908, 3.598470005), (-4.3073024254, -1.3846304018))
                CenterArc((-3.2027298904, -2.0113835548), 1.27, 150.4286899009, 62.6774776192)
                CenterArc((-2.9375002354, -1.5239931773), 1.778, -138.3744157901, 48.3748707465)
                Line((-2.9374861172, -3.3019931772), (-0.9515331316, -3.3019774078))
                CenterArc((-0.9515482583, -1.3969774078), 1.905, -89.9995450436, 35.7792910157)
                Line((0.1622498592, -2.9424478066), (1.7780000567, -1.7780000567))
                Line((1.7780000567, -1.7780000567), (-1.9059463231, -1.7780273157))
                CenterArc((-1.905950082, -1.2700273157), 0.508, 150.4286899009, 119.5717340528)
                Line((-0.4828073053, 2.2674489844), (-2.347779096, -1.0193260545))
                CenterArc((0.2903934693, 1.8287217773), 0.889, 116.1043612387, 34.3243286622)
                CenterArc((-0.4919280953, 1.8287159886), 0.889, 29.1914568154, 34.7050298534)
                Line((3.5107983169, -3.5130962501), (0.2841642914, 2.2623075098))
                Line((5.2565131611, -3.5130962501), (3.5107983169, -3.5130962501))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


# Description: This is a rectangular frame or bracket with rounded corners and parallel side walls, featuring an open center void and what appears to be metal reinforcement bands or flanges along the top and bottom edges.
def model_84610_091c78e8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.7287078728, perimeter: 87.2870787283
            with BuildLine():
                CenterArc((-6.8128754596, 6.6323946625), 0.96, 90, 90)
                Line((-7.7728754596, -6.5676053375), (-7.7728754596, 6.6323946625))
                CenterArc((-6.8128754596, -6.5676053375), 0.96, 180, 90)
                Line((-0.8928754596, -7.5276053375), (-6.8128754596, -7.5276053375))
                CenterArc((-0.8928754596, -6.5676053375), 0.96, -90, 90)
                Line((0.0671245404, 6.6323946625), (0.0671245404, -6.5676053375))
                CenterArc((-0.8928754596, 6.6323946625), 0.96, 0, 90)
                Line((-6.8128754596, 7.5923946625), (-0.8928754596, 7.5923946625))
            make_face()
            with BuildLine():
                Line((-0.1328754596, 6.6323946625), (-0.1328754596, -6.5676053375))
                CenterArc((-0.8928754596, -6.5676053375), 0.76, -90, 90)
                Line((-0.8928754596, -7.3276053375), (-6.8128754596, -7.3276053375))
                CenterArc((-6.8128754596, -6.5676053375), 0.76, 180, 90)
                Line((-7.5728754596, -6.5676053375), (-7.5728754596, 6.6323946625))
                CenterArc((-6.8128754596, 6.6323946625), 0.76, 90, 90)
                Line((-6.8128754596, 7.3923946625), (-0.8928754596, 7.3923946625))
                CenterArc((-0.8928754596, 6.6323946625), 0.76, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)
    return part.part


# Description: This is a rectangular smartphone case or protective cover with rounded corners and a slightly tapered parallelogram shape, featuring smooth surfaces and beveled edges.
def model_85419_1e3af3b4_0001():
    """Model: iphone7+"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 21 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 121.4365419312, perimeter: 48.9453084327
            with BuildLine():
                CenterArc((8.8591033043, 12), 1, 180, 90)
                Line((8.8591033043, 11), (14.6491033043, 11))
                CenterArc((14.6491033043, 12), 1, -90, 90)
                Line((15.6491033043, 12), (15.6491033043, 25.82))
                CenterArc((14.6491033043, 25.82), 1, 0, 90)
                Line((14.6491033043, 26.82), (8.8591033043, 26.82))
                CenterArc((8.8591033043, 25.82), 1, 90, 90)
                Line((7.8591033043, 25.82), (7.8591033043, 12))
            make_face()
            with BuildLine():
                CenterArc((11.7676558477, 11.9214340718), 0.5478309102, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9428507224, perimeter: 3.4421231255
            with Locations((11.7676558477, 11.9214340718)):
                Circle(0.5478309102)
        # OneSide extrude, distance=-0.73
        extrude(amount=-0.73)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 21 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9428507224, perimeter: 3.4421231255
            with Locations((11.7676558477, 11.9214340718)):
                Circle(0.5478309102)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical capsule or barrel-shaped component with a hollow central chamber (shown in blue), featuring rounded hemispherical ends and a uniform cylindrical body with what appears to be internal ribbing or structural features along its length.
def model_85617_4879c1a8_0002():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.25, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.5229320315, -2.4274198511)):
                Circle(0.1)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a long, narrow rectangular channel or beam with a sloped top surface and vertical flanges on the sides, featuring a hollow interior cavity running along its length.
def model_85638_2ab1040c_0000():
    """Model: Arrière1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 255.8875061952, perimeter: 87.3266886222
            with BuildLine():
                Line((23.7439829487, 4.8157603257), (23.7439829487, -2.2922259575))
                Line((23.7439829487, -2.2922259575), (59.7439829487, 4.055545348))
                Line((59.7439829487, 4.055545348), (59.7439829487, 11.1635316312))
                Line((59.7439829487, 11.1635316312), (23.7439829487, 4.8157603257))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a polyhedron or irregular hexahedron with a blocky, geometric form featuring multiple flat faces in varying shades, angular edges, and a complex faceted surface structure with no obvious holes, slots, or curves.
def model_86296_8a6ed4d3_0008():
    """Model: REGIN"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0762, perimeter: 1.108
            with BuildLine():
                Line((-0.127, 0.3), (-0.127, 0))
                Line((-0.127, 0), (0.127, 0))
                Line((0.127, 0), (0.127, 0.3))
                Line((0.127, 0.3), (-0.127, 0.3))
            make_face()
        # Symmetric extrude, full_length=True, total=0.254
        extrude(amount=0.127, both=True)
    return part.part


# Description: This is a stacked array of rectangular solar panel mounting brackets or trays, featuring a trapezoidal profile with angled flanges, internal ribbing for structural reinforcement, and mounting slots along the sides.
def model_86381_dcef1ea4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2000000358, perimeter: 8.6000001281
            with BuildLine():
                Line((2.0000000298, 1.7000000253), (-2.0000000298, 1.7000000253))
                Line((2.0000000298, 2.0000000298), (2.0000000298, 1.7000000253))
                Line((-2.0000000298, 2.0000000298), (2.0000000298, 2.0000000298))
                Line((-2.0000000298, 1.7000000253), (-2.0000000298, 2.0000000298))
            make_face()
            # Profile area: 0.8000000238, perimeter: 8.4000001252
            with BuildLine():
                Line((2.0000000298, 1.1000000164), (-2.0000000298, 1.1000000164))
                Line((2.0000000298, 1.3000000194), (2.0000000298, 1.1000000164))
                Line((-2.0000000298, 1.3000000194), (2.0000000298, 1.3000000194))
                Line((-2.0000000298, 1.1000000164), (-2.0000000298, 1.3000000194))
            make_face()
            # Profile area: 0.8000000238, perimeter: 8.4000001252
            with BuildLine():
                Line((2.0000000298, 0.5000000075), (-2.0000000298, 0.5000000075))
                Line((2.0000000298, 0.7000000104), (2.0000000298, 0.5000000075))
                Line((-2.0000000298, 0.7000000104), (2.0000000298, 0.7000000104))
                Line((-2.0000000298, 0.5000000075), (-2.0000000298, 0.7000000104))
            make_face()
            # Profile area: 0.8000000238, perimeter: 8.4000001252
            with BuildLine():
                Line((2.0000000298, -0.1000000015), (-2.0000000298, -0.1000000015))
                Line((2.0000000298, 0.1000000015), (2.0000000298, -0.1000000015))
                Line((-2.0000000298, 0.1000000015), (2.0000000298, 0.1000000015))
                Line((-2.0000000298, -0.1000000015), (-2.0000000298, 0.1000000015))
            make_face()
            # Profile area: 0.8000000238, perimeter: 8.4000001252
            with BuildLine():
                Line((2.0000000298, -0.7000000104), (-2.0000000298, -0.7000000104))
                Line((2.0000000298, -0.5000000075), (2.0000000298, -0.7000000104))
                Line((-2.0000000298, -0.5000000075), (2.0000000298, -0.5000000075))
                Line((-2.0000000298, -0.7000000104), (-2.0000000298, -0.5000000075))
            make_face()
            # Profile area: 0.8000000238, perimeter: 8.4000001252
            with BuildLine():
                Line((2.0000000298, -1.3000000194), (-2.0000000298, -1.3000000194))
                Line((2.0000000298, -1.1000000164), (2.0000000298, -1.3000000194))
                Line((-2.0000000298, -1.1000000164), (2.0000000298, -1.1000000164))
                Line((-2.0000000298, -1.3000000194), (-2.0000000298, -1.1000000164))
            make_face()
            # Profile area: 1.2000000358, perimeter: 8.6000001281
            with BuildLine():
                Line((2.0000000298, -2.0000000298), (-2.0000000298, -2.0000000298))
                Line((2.0000000298, -1.7000000253), (2.0000000298, -2.0000000298))
                Line((-2.0000000298, -1.7000000253), (2.0000000298, -1.7000000253))
                Line((-2.0000000298, -2.0000000298), (-2.0000000298, -1.7000000253))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a straight cylindrical rod or shaft with a uniform circular cross-section and slightly rounded ends.
def model_86382_d80c0d30_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3, 0)):
                Circle(0.25)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a elongated rectangular prism or bar with a tapered or slightly beveled end, featuring a simple linear geometry with no holes, slots, or other features.
def model_86704_3f8f3bfe_0007():
    """Model: Horizontal 1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2258, perimeter: 11.43
            with BuildLine():
                Line((-2.54, 0.3175), (2.54, 0.3175))
                Line((-2.54, -0.3175), (-2.54, 0.3175))
                Line((2.54, -0.3175), (-2.54, -0.3175))
                Line((2.54, 0.3175), (2.54, -0.3175))
            make_face()
        # OneSide extrude, distance=91.44
        extrude(amount=91.44)
    return part.part


# Description: This is a wedge-shaped duct or deflector component with a tapered triangular profile and radiating internal ribs or fins running lengthwise along its curved surfaces for structural reinforcement.
def model_86898_b705167e_0000():
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
        # Sketch12 -> Extrude11 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4575956649, perimeter: 3.2104700011
            with BuildLine():
                Line((-3.2000000477, 8.1000001207), (-3.2000000477, 6.9000001028))
                Line((-3.2000000477, 6.9000001028), (-2.6000000387, 6.9000001028))
                _nurbs_edge([(-3.1000000462, 8.1000001207), (-3.0949128212, 8.0856001993), (-3.0846389491, 8.0571057121), (-3.0689298783, 8.0152800384), (-3.0473854605, 7.9613521455), (-3.0194563911, 7.8970239569), (-2.9905528413, 7.8357480555), (-2.9607439782, 7.7774019397), (-2.9301631601, 7.7217263052), (-2.8990360735, 7.6682574044), (-2.8676683642, 7.6163665362), (-2.8364201441, 7.5653341704), (-2.8056860927, 7.5144092807), (-2.7758739899, 7.4628724017), (-2.7473835934, 7.4100980839), (-2.7205903979, 7.3555560511), (-2.6958274683, 7.2988135117), (-2.6733673555, 7.2395389611), (-2.6533968876, 7.1775127641), (-2.6360034599, 7.1126290234), (-2.6212112873, 7.044855926), (-2.6114474943, 6.988336225), (-2.6052773335, 6.9446646176), (-2.6016741017, 6.9149828375), (-2.6000000387, 6.9000001028)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.2000000477, 8.1000001207), (-3.1000000462, 8.1000001207))
            make_face()
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)
    return part.part


# Description: A flat, elongated rectangular plate or bar with a slight downward slope and a small notch or cutout on the right end.
def model_87046_b31418fa_0000():
    """Model: Blade"""
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
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 126.92276401, perimeter: 110.0151754602
            with BuildLine():
                Line((13.7160004377, 0), (13.7160004377, -1.7780000567))
                Line((-39.8780012727, 0), (13.7160004377, 0))
                Line((-32.2580010295, -2.5400000811), (-39.8780012727, 0))
                Line((9.9060003161, -2.5400000811), (-32.2580010295, -2.5400000811))
                _nurbs_edge([(10.472005911, -2.9561612902), (10.4653256975, -2.9442020663), (10.4515535716, -2.9206062413), (10.4296602892, -2.8861803699), (10.3979583944, -2.842246806), (10.3538680026, -2.7908272451), (10.3049384163, -2.7431998597), (10.2508098144, -2.6996466194), (10.1913512689, -2.6602701243), (10.1268439481, -2.6248500404), (10.0576991341, -2.5930640713), (9.998992517, -2.5702924284), (9.953178744, -2.5546115571), (9.9218564318, -2.5447687213), (9.9060003161, -2.5400000811)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((12.377005911, -2.9561612902), (10.472005911, -2.9561612902))
                _nurbs_edge([(13.7160004377, -1.7780000567), (13.6930778142, -1.7823316506), (13.6468672617, -1.7928161847), (13.5764555063, -1.8140070761), (13.4803453387, -1.8533691383), (13.3562749202, -1.9221794873), (13.2280231547, -2.011837271), (13.0954408159, -2.1230865042), (12.9587147189, -2.2549957618), (12.8182174393, -2.4057074488), (12.6743461119, -2.5732415234), (12.5568172145, -2.7193934723), (12.4673982496, -2.8353508494), (12.4072293962, -2.9154289297), (12.377005911, -2.9561612902)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.8976195454, perimeter: 18.064008138
            with BuildLine():
                Line((13.7160004377, -1.7780000567), (20.97000445, -1.7780000567))
                Line((20.97000445, -1.7780000567), (20.97000445, 0))
                Line((13.7160004377, 0), (20.97000445, 0))
                Line((13.7160004377, 0), (13.7160004377, -1.7780000567))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a polyhedron or irregular geometric solid with a predominantly hexagonal or octagonal form, featuring multiple flat faces in varying shades of blue and dark gray, with a lighter blue triangular face visible at the top and darker faceted sides creating a complex angular structure.
def model_87358_854d47fe_0008():
    """Model: 15 М16х45,58 v1 v1 v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.8987381147, perimeter: 7.35
            with BuildLine():
                Line((1.0608811196, 0.6125), (0, 1.225))
                Line((0, 1.225), (-1.0608811196, 0.6125))
                Line((-1.0608811196, 0.6125), (-1.0608811196, -0.6125))
                Line((-1.0608811196, -0.6125), (0, -1.225))
                Line((0, -1.225), (1.0608811196, -0.6125))
                Line((1.0608811196, -0.6125), (1.0608811196, 0.6125))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a curved handle or lever with an elongated, slightly tapered design featuring a hook-like curved end at one end and a smaller curved feature at the opposite end, typical of a pull handle or tool grip.
def model_87564_c58c72e9_0002():
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
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 695.1643050717, perimeter: 256.0573250334
            with BuildLine():
                Line((-19, 0), (0, 0))
                _nurbs_edge([(0, 0), (0.0955111348, 0.5659360566), (0.3796255787, 1.6470119243), (1.0850616435, 3.1162475826), (2.5865564937, 4.7691363708), (5.398376148, 6.3281214642), (9.1237034362, 7.4003078623), (13.697059185, 8.0400432394), (19.0097145588, 8.331411656), (24.9232625926, 8.3722585251), (31.2779928673, 8.2623874458), (37.9022687754, 8.090558168), (44.6207518304, 7.9217834189), (51.2624715285, 7.7849445868), (57.6693234961, 7.6578673418), (63.6978247545, 7.4791384013), (69.220570445, 7.1624971821), (74.1282240676, 6.6095797889), (78.3325398367, 5.7238686043), (81.7689256879, 4.4227820693), (84.4028622451, 2.6548626624), (85.8615572923, 0.8517247139), (86.592492778, -0.7205951324), (86.9190881775, -1.8661438596), (87.042210949, -2.4632538298)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((87.042210949, -2.4632538298), (101, -2.5882791706))
                _nurbs_edge([(-19, 0), (-18.3906256785, 0.8448702007), (-17.1094606642, 2.4676041329), (-15.0004634753, 4.7006814774), (-11.8124445781, 7.2744660927), (-7.1942739147, 9.8166857582), (-1.9395371717, 11.6948303927), (3.9463977742, 12.9430275625), (10.4419822693, 13.6344970115), (17.5063938507, 13.8732497699), (25.0777849544, 13.7752892744), (33.0704270168, 13.4542811138), (41.3707852991, 13.0050165521), (49.8343783661, 12.4897046428), (58.2781733014, 11.9181293101), (66.4888810052, 11.2508355877), (74.2420910977, 10.4173640687), (81.3176209782, 9.3292330879), (87.5179253719, 7.8955262022), (92.6836992685, 6.0359936907), (96.7182403901, 3.6993729428), (99.013905941, 1.4333139348), (100.2103594305, -0.4906066735), (100.7755323171, -1.8725061574), (101, -2.5882791706)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


# Description: This is a flat, elongated parallelogram or wedge-shaped plate with a triangular internal division, featuring a dark navy blue color and a slightly tapered, tilted geometric form.
def model_87757_eb92dadf_0015():
    """Model: rearpart"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0210778025, perimeter: 4.253
            with BuildLine():
                Line((6.2390834869, -1.3529279839), (5.9005611163, -2.783418321))
                Line((5.9005611163, -2.783418321), (6.8408551629, -2.507289536))
                Line((6.9833915535, -1.4670091039), (6.8408551629, -2.507289536))
                Line((6.2390834869, -1.3529279839), (6.9833915535, -1.4670091039))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


# Description: This is a cylindrical sleeve or tube with a dark gray finish, featuring a slightly tapered or beveled top end and a smooth, elongated hollow body designed for shaft or rod insertion.
def model_89527_b3bf425d_0001():
    """Model: 8.1 v0"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a curved aerodynamic fairing or deflector with a streamlined, wedge-like shape featuring a smooth upper surface with internal ribbing or structural reinforcement lines, a tapered profile, and a darker undersurface, designed for reduced drag and structural efficiency.
def model_89527_b3bf425d_0011():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72, perimeter: 34
            with BuildLine():
                Line((0, 8), (0, 0))
                Line((0, 0), (9, 0))
                Line((9, 0), (9, 8))
                Line((9, 8), (0, 8))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a hexagonal prism or block with an angled/beveled cut on one side, featuring a triangulated geometric surface pattern that suggests internal structural geometry or a complex faceted design.
def model_90223_9e1de020_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 678.4581821296, perimeter: 104.7397047888
            with BuildLine():
                Line((11.7515512984, -14.4333748988), (-11.7515512984, -14.4333748988))
                Line((11.7515512984, 14.4333748988), (11.7515512984, -14.4333748988))
                Line((-11.7515512984, 14.4333748988), (11.7515512984, 14.4333748988))
                Line((-11.7515512984, -14.4333748988), (-11.7515512984, 14.4333748988))
            make_face()
        # OneSide extrude, distance=17.5
        extrude(amount=17.5)
    return part.part


# Description: This is a geometric polyhedron with a hexagonal cross-section, featuring a central hexagonal body with pyramidal top and bottom sections, characterized by flat faceted surfaces and sharp angular edges throughout.
def model_90482_87d35b1c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23.3826859022, perimeter: 18
            with BuildLine():
                Line((-3, 0), (0, 0))
                Line((0, 0), (1.5, 2.5980762114))
                Line((1.5, 2.5980762114), (0, 5.1961524227))
                Line((0, 5.1961524227), (-3, 5.1961524227))
                Line((-3, 5.1961524227), (-4.5, 2.5980762114))
                Line((-4.5, 2.5980762114), (-3, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a structural bracket or chassis component with an elongated rectangular frame featuring multiple parallel ribs/flanges running lengthwise, two large rectangular cutouts in the center, and reinforcing internal webbing for structural rigidity.
def model_90917_4d6ea65a_0000():
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
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.8104496299, perimeter: 81.9193352959
            with BuildLine():
                Line((-3.2, -1.3), (3.2, -1.3))
                Line((3.2, -1.3), (3.6, -1.3000000053))
                Line((3.6, -1.3000000053), (3.6, -0.5000000053))
                Line((3.6, -0.5000000053), (3.2000000159, -0.1000000212))
                Line((3.2000000159, -0.1000000212), (3.2000000477, 2.3000000343))
                Line((3.6, 2.7), (3.2000000477, 2.3000000343))
                Line((3.6, 3.5), (3.6, 2.7))
                Line((3.6, 3.5), (-3.6, 3.5))
                Line((-3.6, 3.5), (-3.6, 2.7))
                Line((-3.6, 2.7), (-3.2000000477, 2.3000000343))
                Line((-3.2000000477, 2.3000000343), (-3.2000000159, -0.1000000233))
                Line((-3.6, -0.5000000075), (-3.2000000159, -0.1000000233))
                Line((-3.6, -1.3000000053), (-3.6, -0.5000000075))
                Line((-3.2, -1.3), (-3.6, -1.3000000053))
            make_face()
            with BuildLine():
                Line((1.375, 0.75), (1.375, -0.75))
                Line((1.375, -0.75), (-1.375, -0.75))
                Line((-1.375, -0.75), (-1.375, 0.75))
                Line((-1.375, 0.75), (1.375, 0.75))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.1408349937, 1.0298436746), (-1.1408349937, 2.2618437872))
                Line((-1.1408349937, 2.2618437872), (-1.3768349355, 2.2618437872))
                Line((-1.3768349355, 2.2618437872), (-1.3768349355, 2.4538436994))
                Line((-1.3768349355, 2.4538436994), (-0.7008350557, 2.4538436994))
                Line((-0.7008350557, 2.4538436994), (-0.7008350557, 2.2618437872))
                Line((-0.7008350557, 2.2618437872), (-0.9368348783, 2.2618437872))
                Line((-0.9368348783, 2.2618437872), (-0.9368348783, 1.0298436746))
                Line((-0.9368348783, 1.0298436746), (-1.1408349937, 1.0298436746))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.7028351492, 1.0298436746), (-0.384835071, 2.4538436994))
                Line((-0.384835071, 2.4538436994), (-0.2148349947, 2.4538436994))
                Line((-0.2148349947, 2.4538436994), (0.1031648451, 1.0298436746))
                Line((0.1031648451, 1.0298436746), (-0.1008351511, 1.0298436746))
                Line((-0.1008351511, 1.0298436746), (-0.1608350938, 1.3358436689))
                Line((-0.1608350938, 1.3358436689), (-0.4388352102, 1.3358436689))
                Line((-0.4388352102, 1.3358436689), (-0.498835153, 1.0298436746))
                Line((-0.498835153, 1.0298436746), (-0.7028351492, 1.0298436746))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.3371650511, 1.0298436746), (0.3371650511, 2.2618437872))
                Line((0.3371650511, 2.2618437872), (0.1011649901, 2.2618437872))
                Line((0.1011649901, 2.2618437872), (0.1011649901, 2.4538436994))
                Line((0.1011649901, 2.4538436994), (0.7771651083, 2.4538436994))
                Line((0.7771651083, 2.4538436994), (0.7771651083, 2.2618437872))
                Line((0.7771651083, 2.2618437872), (0.5411650473, 2.2618437872))
                Line((0.5411650473, 2.2618437872), (0.5411650473, 1.0298436746))
                Line((0.5411650473, 1.0298436746), (0.3371650511, 1.0298436746))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.8731650645, 1.0298436746), (0.8731650645, 2.4538436994))
                Line((0.8731650645, 2.4538436994), (1.0771652991, 2.4538436994))
                Line((1.0771652991, 2.4538436994), (1.0771652991, 1.0298436746))
                Line((1.0771652991, 1.0298436746), (0.8731650645, 1.0298436746))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.2751652533, 1.0298436746), (1.2751652533, 2.4538436994))
                Line((1.2751652533, 2.4538436994), (1.4711653525, 2.4538436994))
                Line((1.4711653525, 2.4538436994), (1.7331654364, 1.6998436913))
                Line((1.7331654364, 1.6998436913), (1.7371651465, 1.6998436913))
                Line((1.7371651465, 1.6998436913), (1.9971653754, 2.4538436994))
                Line((1.9971653754, 2.4538436994), (2.1951653296, 2.4538436994))
                Line((2.1951653296, 2.4538436994), (2.1951653296, 1.0298436746))
                Line((2.1951653296, 1.0298436746), (1.9911653334, 1.0298436746))
                Line((1.9911653334, 1.0298436746), (1.9911653334, 1.8958437309))
                Line((1.9911653334, 1.8958437309), (1.9871651465, 1.8958437309))
                Line((1.9871651465, 1.8958437309), (1.7851654822, 1.2838436231))
                Line((1.7851654822, 1.2838436231), (1.6831652457, 1.2838436231))
                Line((1.6831652457, 1.2838436231), (1.4831654364, 1.8958437309))
                Line((1.4831654364, 1.8958437309), (1.4791652495, 1.8958437309))
                Line((1.4791652495, 1.8958437309), (1.4791652495, 1.0298436746))
                Line((1.4791652495, 1.0298436746), (1.2751652533, 1.0298436746))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.3871652418, 1.0298436746), (2.3871652418, 2.4538436994))
                Line((2.3871652418, 2.4538436994), (2.9951650435, 2.4538436994))
                Line((2.9951650435, 2.4538436994), (2.9951650435, 2.2618437872))
                Line((2.9951650435, 2.2618437872), (2.591165238, 2.2618437872))
                Line((2.591165238, 2.2618437872), (2.591165238, 1.8438436851))
                Line((2.591165238, 1.8438436851), (2.9431654745, 1.8438436851))
                Line((2.9431654745, 1.8438436851), (2.9431654745, 1.6518437133))
                Line((2.9431654745, 1.6518437133), (2.591165238, 1.6518437133))
                Line((2.591165238, 1.6518437133), (2.591165238, 1.2338436708))
                Line((2.591165238, 1.2338436708), (2.9951650435, 1.2338436708))
                Line((2.9951650435, 1.2338436708), (2.9951650435, 1.0298436746))
                Line((2.9951650435, 1.0298436746), (2.3871652418, 1.0298436746))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(-2.9608351207, 1.2118437156), (-2.9695791815, 1.2354277376), (-2.9879869624, 1.2850762386), (-2.9898546322, 1.3380391575), (-2.9908351219, 1.3658436403)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.074956603, 0.157796791, 0.157796791, 0.157796791, 0.157796791], 3)
                Line((-2.9908351219, 1.3658436403), (-2.9908351219, 2.1178437338))
                _nurbs_edge([(-2.9908351219, 2.1178437338), (-2.9898206818, 2.1451442585), (-2.9878774325, 2.1974408182), (-2.9695804678, 2.2464289628), (-2.9608351207, 2.2698436842)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0813464525, 0.1558262944, 0.1558262944, 0.1558262944, 0.1558262944], 3)
                _nurbs_edge([(-2.9608351207, 2.2698436842), (-2.9503662256, 2.2905939697), (-2.9300989868, 2.3307654482), (-2.8982383721, 2.3625009604), (-2.8828351265, 2.3778437242)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.069211628, 0.1339901288, 0.1339901288, 0.1339901288, 0.1339901288], 3)
                _nurbs_edge([(-2.8828351265, 2.3778437242), (-2.8658599921, 2.3915538138), (-2.8322659043, 2.4186863208), (-2.7925048542, 2.4355173967), (-2.7728351122, 2.443843709)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651037775, 0.1288415144, 0.1288415144, 0.1288415144, 0.1288415144], 3)
                _nurbs_edge([(-2.7728351122, 2.443843709), (-2.752329772, 2.4502599703), (-2.7119309938, 2.4629010245), (-2.669653612, 2.464872819), (-2.6488350993, 2.4658437833)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0641580286, 0.1264015103, 0.1264015103, 0.1264015103, 0.1264015103], 3)
                _nurbs_edge([(-2.6488350993, 2.4658437833), (-2.628175498, 2.4648990324), (-2.5865336613, 2.4629947766), (-2.5468371348, 2.4502602864), (-2.5268350905, 2.443843709)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.06174543, 0.1244551179, 0.1244551179, 0.1244551179, 0.1244551179], 3)
                _nurbs_edge([(-2.5268350905, 2.443843709), (-2.5067730521, 2.435613216), (-2.4667548691, 2.4191956731), (-2.4334456268, 2.3916033695), (-2.4168350762, 2.3778437242)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0646412996, 0.1289414018, 0.1289414018, 0.1289414018, 0.1289414018], 3)
                _nurbs_edge([(-2.4168350762, 2.3778437242), (-2.400874525, 2.362559795), (-2.3680638767, 2.3311401017), (-2.3474311489, 2.290641813), (-2.3368350929, 2.2698436842)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0657951755, 0.1352573807, 0.1352573807, 0.1352573807, 0.1352573807], 3)
                _nurbs_edge([(-2.3368350929, 2.2698436842), (-2.3280897218, 2.2464289644), (-2.3097927097, 2.19744083), (-2.3078495268, 2.1451442603), (-2.3068351215, 2.1178437338)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0744798555, 0.1558263011, 0.1558263011, 0.1558263011, 0.1558263011], 3)
                Line((-2.3068351215, 2.1178437338), (-2.3068351215, 1.3658436403))
                _nurbs_edge([(-2.3068351215, 1.3658436403), (-2.3078156436, 1.3380391604), (-2.309683375, 1.2850762575), (-2.3280910733, 1.2354277401), (-2.3368350929, 1.2118437156)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0828401934, 0.1577967695, 0.1577967695, 0.1577967695, 0.1577967695], 3)
                _nurbs_edge([(-2.3368350929, 1.2118437156), (-2.3475370706, 1.1914600656), (-2.3686177622, 1.1513084736), (-2.4009277918, 1.1195026988), (-2.4168350762, 1.1038436756)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.068600318, 0.1351284968, 0.1351284968, 0.1351284968, 0.1351284968], 3)
                _nurbs_edge([(-2.4168350762, 1.1038436756), (-2.4334993806, 1.0906483824), (-2.4670951891, 1.0640462191), (-2.506816484, 1.0479538459), (-2.5268350905, 1.0398436651)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0634133799, 0.1278435466, 0.1278435466, 0.1278435466, 0.1278435466], 3)
                _nurbs_edge([(-2.5268350905, 1.0398436651), (-2.5468371357, 1.0334271074), (-2.5865336672, 1.0206926555), (-2.6281754988, 1.0187884407), (-2.6488350993, 1.0178437099)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0627096722, 0.1244550969, 0.1244550969, 0.1244550969, 0.1244550969], 3)
                _nurbs_edge([(-2.6488350993, 1.0178437099), (-2.6696536112, 1.018814654), (-2.7119309882, 1.0207864072), (-2.7523297712, 1.0334274235), (-2.7728351122, 1.0398436651)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0622434763, 0.1264014897, 0.1264014897, 0.1264014897, 0.1264014897], 3)
                _nurbs_edge([(-2.7728351122, 1.0398436651), (-2.7924638681, 1.0480485911), (-2.8319390486, 1.0645494298), (-2.8658075162, 1.0906975329), (-2.8828351265, 1.1038436756)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0635236516, 0.1277517344, 0.1277517344, 0.1277517344, 0.1277517344], 3)
                _nurbs_edge([(-2.8828351265, 1.1038436756), (-2.8981855816, 1.1195601017), (-2.929548001, 1.1516702344), (-2.9502604555, 1.1915058123), (-2.9608351207, 1.2118437156)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0655229194, 0.13386947, 0.13386947, 0.13386947, 0.13386947], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(-1.7068350977, 1.2578437195), (-1.6963681921, 1.2726694271), (-1.672829889, 1.3060099399), (-1.6715473241, 1.3470520287), (-1.6708350843, 1.369843708)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0533385196, 0.1199493229, 0.1199493229, 0.1199493229, 0.1199493229], 3)
                Line((-1.6708350843, 1.369843708), (-1.6708350843, 2.4538436994))
                Line((-1.6708350843, 2.4538436994), (-1.4668350881, 2.4538436994))
                Line((-1.4668350881, 2.4538436994), (-1.4668350881, 1.3498437271))
                _nurbs_edge([(-1.4668350881, 1.3498437271), (-1.4678402751, 1.3271092338), (-1.4698159501, 1.282425037), (-1.4852524278, 1.2404584803), (-1.492835111, 1.2198437318)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0678122366, 0.1332836095, 0.1332836095, 0.1332836095, 0.1332836095], 3)
                _nurbs_edge([(-1.492835111, 1.2198437318), (-1.502324863, 1.2004372422), (-1.5212791965, 1.1616757364), (-1.5503292703, 1.1297735679), (-1.5648350185, 1.113843666)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0644457327, 0.12872053, 0.12872053, 0.12872053, 0.12872053], 3)
                _nurbs_edge([(-1.5648350185, 1.113843666), (-1.5802927284, 1.0998734276), (-1.6116070161, 1.0715724651), (-1.6495976963, 1.0531647999), (-1.6688349908, 1.0438437328)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0621630738, 0.1259301923, 0.1259301923, 0.1259301923, 0.1259301923], 3)
                _nurbs_edge([(-1.6688349908, 1.0438437328), (-1.6892804818, 1.0362606112), (-1.7305882797, 1.0209397732), (-1.7746047186, 1.0188826501), (-1.7968350118, 1.0178437099)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0649942702, 0.131313559, 0.131313559, 0.131313559, 0.131313559], 3)
                _nurbs_edge([(-1.7968350118, 1.0178437099), (-1.8190653051, 1.0188826501), (-1.863081744, 1.0209397732), (-1.9043895419, 1.0362606112), (-1.9248350328, 1.0438437328)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0663192887, 0.131313559, 0.131313559, 0.131313559, 0.131313559], 3)
                _nurbs_edge([(-1.9248350328, 1.0438437328), (-1.9441981504, 1.0532092449), (-1.982659532, 1.0718121652), (-2.0148504677, 1.0998976334), (-2.0308350986, 1.113843666)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0642067346, 0.1275352331, 0.1275352331, 0.1275352331, 0.1275352331], 3)
                _nurbs_edge([(-2.0308350986, 1.113843666), (-2.0447811248, 1.1298283411), (-2.0728665359, 1.1620193156), (-2.0914695081, 1.2004806618), (-2.1008350319, 1.2198437318)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0633285916, 0.1275352214, 0.1275352214, 0.1275352214, 0.1275352214], 3)
                _nurbs_edge([(-2.1008350319, 1.2198437318), (-2.1084177151, 1.2404584803), (-2.1238541928, 1.282425037), (-2.1258298678, 1.3271092338), (-2.1268350547, 1.3498437271)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0654713729, 0.1332836095, 0.1332836095, 0.1332836095, 0.1332836095], 3)
                Line((-2.1268350547, 1.3498437271), (-2.1268350547, 2.4538436994))
                Line((-2.1268350547, 2.4538436994), (-1.9228350586, 2.4538436994))
                Line((-1.9228350586, 2.4538436994), (-1.9228350586, 1.369843708))
                _nurbs_edge([(-1.9228350586, 1.369843708), (-1.9221228188, 1.3470520287), (-1.9208402539, 1.3060099399), (-1.8973019508, 1.2726694271), (-1.8868350452, 1.2578437195)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0666108033, 0.1199493229, 0.1199493229, 0.1199493229, 0.1199493229], 3)
                _nurbs_edge([(-1.8868350452, 1.2578437195), (-1.8739406625, 1.2473445518), (-1.8477183548, 1.2259932072), (-1.8139820508, 1.2232420352), (-1.7968350118, 1.2218437061)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.048674952, 0.0989864815, 0.0989864815, 0.0989864815, 0.0989864815], 3)
                _nurbs_edge([(-1.7968350118, 1.2218437061), (-1.7796879633, 1.2232419741), (-1.7459516446, 1.2259930257), (-1.7197294319, 1.2473444928), (-1.7068350977, 1.2578437195)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0503115082, 0.0989864271, 0.0989864271, 0.0989864271, 0.0989864271], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 3.1000000462), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.6, 3.1000000462), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6, 3.1000000462), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2, 3.1000000462), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.2, 3.1000000462), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.2000000053, -0.9), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2000000053, -0.9000000848), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2718375243, perimeter: 2.4045372769
            with BuildLine():
                _nurbs_edge([(-2.7468351191, 2.2258437738), (-2.7584728452, 2.2118249817), (-2.7842663125, 2.1807541993), (-2.7859248739, 2.1401356464), (-2.7868351108, 2.1178437338)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0532541329, 0.1180306808, 0.1180306808, 0.1180306808, 0.1180306808], 3)
                Line((-2.7868351108, 2.1178437338), (-2.7868351108, 1.3658436403))
                _nurbs_edge([(-2.7868351108, 1.3658436403), (-2.7858567931, 1.3434346924), (-2.7840615924, 1.3023145506), (-2.7584770414, 1.2703766691), (-2.7468351191, 1.2558437452)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0652704505, 0.1197704682, 0.1197704682, 0.1197704682, 0.1197704682], 3)
                _nurbs_edge([(-2.7468351191, 1.2558437452), (-2.7321625909, 1.2459273181), (-2.7025291386, 1.2258995516), (-2.6668488605, 1.2232043978), (-2.6488350993, 1.2218437061)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0521584504, 0.1053421007, 0.1053421007, 0.1053421007, 0.1053421007], 3)
                _nurbs_edge([(-2.6488350993, 1.2218437061), (-2.6309579208, 1.2231572212), (-2.5958261433, 1.2257385077), (-2.5669951495, 1.2459279267), (-2.5528351134, 1.2558437452)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0526901444, 0.1035453347, 0.1035453347, 0.1035453347, 0.1035453347], 3)
                _nurbs_edge([(-2.5528351134, 1.2558437452), (-2.5406073221, 1.2703133879), (-2.5139401727, 1.3018697102), (-2.5119258209, 1.343371712), (-2.5108351177, 1.3658436403)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0553399156, 0.1206888279, 0.1206888279, 0.1206888279, 0.1206888279], 3)
                Line((-2.5108351177, 1.3658436403), (-2.5108351177, 2.1178437338))
                _nurbs_edge([(-2.5108351177, 2.1178437338), (-2.5118589548, 2.140200614), (-2.5137370466, 2.1812113133), (-2.5406112946, 2.2118896539), (-2.5528351134, 2.2258437738)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0648556214, 0.118968942, 0.118968942, 0.118968942, 0.118968942], 3)
                _nurbs_edge([(-2.5528351134, 2.2258437738), (-2.5669358028, 2.2363433832), (-2.5954511567, 2.2575763931), (-2.630910308, 2.2604108399), (-2.6488350993, 2.261843668)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0516235963, 0.1043966773, 0.1043966773, 0.1043966773, 0.1043966773], 3)
                _nurbs_edge([(-2.6488350993, 2.261843668), (-2.6668946752, 2.2603640057), (-2.70289245, 2.2574146259), (-2.7322205254, 2.2363437089), (-2.7468351191, 2.2258437738)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.053265877, 0.1061737586, 0.1061737586, 0.1061737586, 0.1061737586], 3)
            make_face()
            # Profile area: 0.0536639891, perimeter: 1.2592012351
            with BuildLine():
                Line((-0.1988352007, 1.5278437004), (-0.2988351053, 2.0438437328))
                Line((-0.2988351053, 2.0438437328), (-0.3028350538, 2.0438437328))
                Line((-0.3028350538, 2.0438437328), (-0.4028351968, 1.5278437004))
                Line((-0.4028351968, 1.5278437004), (-0.1988352007, 1.5278437004))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6213291074, perimeter: 6.0912608652
            with BuildLine():
                _nurbs_edge([(-2.8828351265, 1.1038436756), (-2.8981855816, 1.1195601017), (-2.929548001, 1.1516702344), (-2.9502604555, 1.1915058123), (-2.9608351207, 1.2118437156)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0655229194, 0.13386947, 0.13386947, 0.13386947, 0.13386947], 3)
                _nurbs_edge([(-2.7728351122, 1.0398436651), (-2.7924638681, 1.0480485911), (-2.8319390486, 1.0645494298), (-2.8658075162, 1.0906975329), (-2.8828351265, 1.1038436756)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0635236516, 0.1277517344, 0.1277517344, 0.1277517344, 0.1277517344], 3)
                _nurbs_edge([(-2.6488350993, 1.0178437099), (-2.6696536112, 1.018814654), (-2.7119309882, 1.0207864072), (-2.7523297712, 1.0334274235), (-2.7728351122, 1.0398436651)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0622434763, 0.1264014897, 0.1264014897, 0.1264014897, 0.1264014897], 3)
                _nurbs_edge([(-2.5268350905, 1.0398436651), (-2.5468371357, 1.0334271074), (-2.5865336672, 1.0206926555), (-2.6281754988, 1.0187884407), (-2.6488350993, 1.0178437099)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0627096722, 0.1244550969, 0.1244550969, 0.1244550969, 0.1244550969], 3)
                _nurbs_edge([(-2.4168350762, 1.1038436756), (-2.4334993806, 1.0906483824), (-2.4670951891, 1.0640462191), (-2.506816484, 1.0479538459), (-2.5268350905, 1.0398436651)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0634133799, 0.1278435466, 0.1278435466, 0.1278435466, 0.1278435466], 3)
                _nurbs_edge([(-2.3368350929, 1.2118437156), (-2.3475370706, 1.1914600656), (-2.3686177622, 1.1513084736), (-2.4009277918, 1.1195026988), (-2.4168350762, 1.1038436756)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.068600318, 0.1351284968, 0.1351284968, 0.1351284968, 0.1351284968], 3)
                _nurbs_edge([(-2.3068351215, 1.3658436403), (-2.3078156436, 1.3380391604), (-2.309683375, 1.2850762575), (-2.3280910733, 1.2354277401), (-2.3368350929, 1.2118437156)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0828401934, 0.1577967695, 0.1577967695, 0.1577967695, 0.1577967695], 3)
                Line((-2.3068351215, 2.1178437338), (-2.3068351215, 1.3658436403))
                _nurbs_edge([(-2.3368350929, 2.2698436842), (-2.3280897218, 2.2464289644), (-2.3097927097, 2.19744083), (-2.3078495268, 2.1451442603), (-2.3068351215, 2.1178437338)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0744798555, 0.1558263011, 0.1558263011, 0.1558263011, 0.1558263011], 3)
                _nurbs_edge([(-2.4168350762, 2.3778437242), (-2.400874525, 2.362559795), (-2.3680638767, 2.3311401017), (-2.3474311489, 2.290641813), (-2.3368350929, 2.2698436842)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0657951755, 0.1352573807, 0.1352573807, 0.1352573807, 0.1352573807], 3)
                _nurbs_edge([(-2.5268350905, 2.443843709), (-2.5067730521, 2.435613216), (-2.4667548691, 2.4191956731), (-2.4334456268, 2.3916033695), (-2.4168350762, 2.3778437242)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0646412996, 0.1289414018, 0.1289414018, 0.1289414018, 0.1289414018], 3)
                _nurbs_edge([(-2.6488350993, 2.4658437833), (-2.628175498, 2.4648990324), (-2.5865336613, 2.4629947766), (-2.5468371348, 2.4502602864), (-2.5268350905, 2.443843709)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.06174543, 0.1244551179, 0.1244551179, 0.1244551179, 0.1244551179], 3)
                _nurbs_edge([(-2.7728351122, 2.443843709), (-2.752329772, 2.4502599703), (-2.7119309938, 2.4629010245), (-2.669653612, 2.464872819), (-2.6488350993, 2.4658437833)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0641580286, 0.1264015103, 0.1264015103, 0.1264015103, 0.1264015103], 3)
                _nurbs_edge([(-2.8828351265, 2.3778437242), (-2.8658599921, 2.3915538138), (-2.8322659043, 2.4186863208), (-2.7925048542, 2.4355173967), (-2.7728351122, 2.443843709)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651037775, 0.1288415144, 0.1288415144, 0.1288415144, 0.1288415144], 3)
                _nurbs_edge([(-2.9608351207, 2.2698436842), (-2.9503662256, 2.2905939697), (-2.9300989868, 2.3307654482), (-2.8982383721, 2.3625009604), (-2.8828351265, 2.3778437242)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.069211628, 0.1339901288, 0.1339901288, 0.1339901288, 0.1339901288], 3)
                _nurbs_edge([(-2.9908351219, 2.1178437338), (-2.9898206818, 2.1451442585), (-2.9878774325, 2.1974408182), (-2.9695804678, 2.2464289628), (-2.9608351207, 2.2698436842)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0813464525, 0.1558262944, 0.1558262944, 0.1558262944, 0.1558262944], 3)
                Line((-2.9908351219, 1.3658436403), (-2.9908351219, 2.1178437338))
                _nurbs_edge([(-2.9608351207, 1.2118437156), (-2.9695791815, 1.2354277376), (-2.9879869624, 1.2850762386), (-2.9898546322, 1.3380391575), (-2.9908351219, 1.3658436403)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.074956603, 0.157796791, 0.157796791, 0.157796791, 0.157796791], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-2.6488350993, 2.261843668), (-2.6668946752, 2.2603640057), (-2.70289245, 2.2574146259), (-2.7322205254, 2.2363437089), (-2.7468351191, 2.2258437738)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.053265877, 0.1061737586, 0.1061737586, 0.1061737586, 0.1061737586], 3)
                _nurbs_edge([(-2.5528351134, 2.2258437738), (-2.5669358028, 2.2363433832), (-2.5954511567, 2.2575763931), (-2.630910308, 2.2604108399), (-2.6488350993, 2.261843668)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0516235963, 0.1043966773, 0.1043966773, 0.1043966773, 0.1043966773], 3)
                _nurbs_edge([(-2.5108351177, 2.1178437338), (-2.5118589548, 2.140200614), (-2.5137370466, 2.1812113133), (-2.5406112946, 2.2118896539), (-2.5528351134, 2.2258437738)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0648556214, 0.118968942, 0.118968942, 0.118968942, 0.118968942], 3)
                Line((-2.5108351177, 1.3658436403), (-2.5108351177, 2.1178437338))
                _nurbs_edge([(-2.5528351134, 1.2558437452), (-2.5406073221, 1.2703133879), (-2.5139401727, 1.3018697102), (-2.5119258209, 1.343371712), (-2.5108351177, 1.3658436403)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0553399156, 0.1206888279, 0.1206888279, 0.1206888279, 0.1206888279], 3)
                _nurbs_edge([(-2.6488350993, 1.2218437061), (-2.6309579208, 1.2231572212), (-2.5958261433, 1.2257385077), (-2.5669951495, 1.2459279267), (-2.5528351134, 1.2558437452)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0526901444, 0.1035453347, 0.1035453347, 0.1035453347, 0.1035453347], 3)
                _nurbs_edge([(-2.7468351191, 1.2558437452), (-2.7321625909, 1.2459273181), (-2.7025291386, 1.2258995516), (-2.6668488605, 1.2232043978), (-2.6488350993, 1.2218437061)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0521584504, 0.1053421007, 0.1053421007, 0.1053421007, 0.1053421007], 3)
                _nurbs_edge([(-2.7868351108, 1.3658436403), (-2.7858567931, 1.3434346924), (-2.7840615924, 1.3023145506), (-2.7584770414, 1.2703766691), (-2.7468351191, 1.2558437452)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0652704505, 0.1197704682, 0.1197704682, 0.1197704682, 0.1197704682], 3)
                Line((-2.7868351108, 2.1178437338), (-2.7868351108, 1.3658436403))
                _nurbs_edge([(-2.7468351191, 2.2258437738), (-2.7584728452, 2.2118249817), (-2.7842663125, 2.1807541993), (-2.7859248739, 2.1401356464), (-2.7868351108, 2.1178437338)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0532541329, 0.1180306808, 0.1180306808, 0.1180306808, 0.1180306808], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5971366847, perimeter: 6.2634878325
            with BuildLine():
                _nurbs_edge([(-1.7968350118, 1.2218437061), (-1.7796879633, 1.2232419741), (-1.7459516446, 1.2259930257), (-1.7197294319, 1.2473444928), (-1.7068350977, 1.2578437195)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0503115082, 0.0989864271, 0.0989864271, 0.0989864271, 0.0989864271], 3)
                _nurbs_edge([(-1.8868350452, 1.2578437195), (-1.8739406625, 1.2473445518), (-1.8477183548, 1.2259932072), (-1.8139820508, 1.2232420352), (-1.7968350118, 1.2218437061)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.048674952, 0.0989864815, 0.0989864815, 0.0989864815, 0.0989864815], 3)
                _nurbs_edge([(-1.9228350586, 1.369843708), (-1.9221228188, 1.3470520287), (-1.9208402539, 1.3060099399), (-1.8973019508, 1.2726694271), (-1.8868350452, 1.2578437195)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0666108033, 0.1199493229, 0.1199493229, 0.1199493229, 0.1199493229], 3)
                Line((-1.9228350586, 2.4538436994), (-1.9228350586, 1.369843708))
                Line((-2.1268350547, 2.4538436994), (-1.9228350586, 2.4538436994))
                Line((-2.1268350547, 1.3498437271), (-2.1268350547, 2.4538436994))
                _nurbs_edge([(-2.1008350319, 1.2198437318), (-2.1084177151, 1.2404584803), (-2.1238541928, 1.282425037), (-2.1258298678, 1.3271092338), (-2.1268350547, 1.3498437271)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0654713729, 0.1332836095, 0.1332836095, 0.1332836095, 0.1332836095], 3)
                _nurbs_edge([(-2.0308350986, 1.113843666), (-2.0447811248, 1.1298283411), (-2.0728665359, 1.1620193156), (-2.0914695081, 1.2004806618), (-2.1008350319, 1.2198437318)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0633285916, 0.1275352214, 0.1275352214, 0.1275352214, 0.1275352214], 3)
                _nurbs_edge([(-1.9248350328, 1.0438437328), (-1.9441981504, 1.0532092449), (-1.982659532, 1.0718121652), (-2.0148504677, 1.0998976334), (-2.0308350986, 1.113843666)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0642067346, 0.1275352331, 0.1275352331, 0.1275352331, 0.1275352331], 3)
                _nurbs_edge([(-1.7968350118, 1.0178437099), (-1.8190653051, 1.0188826501), (-1.863081744, 1.0209397732), (-1.9043895419, 1.0362606112), (-1.9248350328, 1.0438437328)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0663192887, 0.131313559, 0.131313559, 0.131313559, 0.131313559], 3)
                _nurbs_edge([(-1.6688349908, 1.0438437328), (-1.6892804818, 1.0362606112), (-1.7305882797, 1.0209397732), (-1.7746047186, 1.0188826501), (-1.7968350118, 1.0178437099)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0649942702, 0.131313559, 0.131313559, 0.131313559, 0.131313559], 3)
                _nurbs_edge([(-1.5648350185, 1.113843666), (-1.5802927284, 1.0998734276), (-1.6116070161, 1.0715724651), (-1.6495976963, 1.0531647999), (-1.6688349908, 1.0438437328)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0621630738, 0.1259301923, 0.1259301923, 0.1259301923, 0.1259301923], 3)
                _nurbs_edge([(-1.492835111, 1.2198437318), (-1.502324863, 1.2004372422), (-1.5212791965, 1.1616757364), (-1.5503292703, 1.1297735679), (-1.5648350185, 1.113843666)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0644457327, 0.12872053, 0.12872053, 0.12872053, 0.12872053], 3)
                _nurbs_edge([(-1.4668350881, 1.3498437271), (-1.4678402751, 1.3271092338), (-1.4698159501, 1.282425037), (-1.4852524278, 1.2404584803), (-1.492835111, 1.2198437318)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0678122366, 0.1332836095, 0.1332836095, 0.1332836095, 0.1332836095], 3)
                Line((-1.4668350881, 2.4538436994), (-1.4668350881, 1.3498437271))
                Line((-1.6708350843, 2.4538436994), (-1.4668350881, 2.4538436994))
                Line((-1.6708350843, 1.369843708), (-1.6708350843, 2.4538436994))
                _nurbs_edge([(-1.7068350977, 1.2578437195), (-1.6963681921, 1.2726694271), (-1.672829889, 1.3060099399), (-1.6715473241, 1.3470520287), (-1.6708350843, 1.369843708)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0533385196, 0.1199493229, 0.1199493229, 0.1199493229, 0.1199493229], 3)
            make_face()
            # Profile area: 0.3811200827, perimeter: 4.1999998093
            with BuildLine():
                Line((-0.9368348783, 1.0298436746), (-1.1408349937, 1.0298436746))
                Line((-0.9368348783, 2.2618437872), (-0.9368348783, 1.0298436746))
                Line((-0.7008350557, 2.2618437872), (-0.9368348783, 2.2618437872))
                Line((-0.7008350557, 2.4538436994), (-0.7008350557, 2.2618437872))
                Line((-1.3768349355, 2.4538436994), (-0.7008350557, 2.4538436994))
                Line((-1.3768349355, 2.2618437872), (-1.3768349355, 2.4538436994))
                Line((-1.1408349937, 2.2618437872), (-1.3768349355, 2.2618437872))
                Line((-1.1408349937, 1.0298436746), (-1.1408349937, 2.2618437872))
            make_face()
            # Profile area: 0.5378200571, perimeter: 5.6570052664
            with BuildLine():
                Line((-0.498835153, 1.0298436746), (-0.7028351492, 1.0298436746))
                Line((-0.4388352102, 1.3358436689), (-0.498835153, 1.0298436746))
                Line((-0.1608350938, 1.3358436689), (-0.4388352102, 1.3358436689))
                Line((-0.1008351511, 1.0298436746), (-0.1608350938, 1.3358436689))
                Line((0.1031648451, 1.0298436746), (-0.1008351511, 1.0298436746))
                Line((-0.2148349947, 2.4538436994), (0.1031648451, 1.0298436746))
                Line((-0.384835071, 2.4538436994), (-0.2148349947, 2.4538436994))
                Line((-0.7028351492, 1.0298436746), (-0.384835071, 2.4538436994))
            make_face()
            with BuildLine():
                Line((-0.4028351968, 1.5278437004), (-0.1988352007, 1.5278437004))
                Line((-0.3028350538, 2.0438437328), (-0.4028351968, 1.5278437004))
                Line((-0.2988351053, 2.0438437328), (-0.3028350538, 2.0438437328))
                Line((-0.1988352007, 1.5278437004), (-0.2988351053, 2.0438437328))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3811199817, perimeter: 4.2000002861
            with BuildLine():
                Line((0.5411650473, 1.0298436746), (0.3371650511, 1.0298436746))
                Line((0.5411650473, 2.2618437872), (0.5411650473, 1.0298436746))
                Line((0.7771651083, 2.2618437872), (0.5411650473, 2.2618437872))
                Line((0.7771651083, 2.4538436994), (0.7771651083, 2.2618437872))
                Line((0.1011649901, 2.4538436994), (0.7771651083, 2.4538436994))
                Line((0.1011649901, 2.2618437872), (0.1011649901, 2.4538436994))
                Line((0.3371650511, 2.2618437872), (0.1011649901, 2.2618437872))
                Line((0.3371650511, 1.0298436746), (0.3371650511, 2.2618437872))
            make_face()
            # Profile area: 0.2904963391, perimeter: 3.2560005188
            with BuildLine():
                Line((1.0771652991, 1.0298436746), (0.8731650645, 1.0298436746))
                Line((1.0771652991, 2.4538436994), (1.0771652991, 1.0298436746))
                Line((0.8731650645, 2.4538436994), (1.0771652991, 2.4538436994))
                Line((0.8731650645, 1.0298436746), (0.8731650645, 2.4538436994))
            make_face()
            # Profile area: 0.8523141448, perimeter: 8.3801184129
            with BuildLine():
                Line((1.4791652495, 1.0298436746), (1.2751652533, 1.0298436746))
                Line((1.4791652495, 1.8958437309), (1.4791652495, 1.0298436746))
                Line((1.4831654364, 1.8958437309), (1.4791652495, 1.8958437309))
                Line((1.6831652457, 1.2838436231), (1.4831654364, 1.8958437309))
                Line((1.7851654822, 1.2838436231), (1.6831652457, 1.2838436231))
                Line((1.9871651465, 1.8958437309), (1.7851654822, 1.2838436231))
                Line((1.9911653334, 1.8958437309), (1.9871651465, 1.8958437309))
                Line((1.9911653334, 1.0298436746), (1.9911653334, 1.8958437309))
                Line((2.1951653296, 1.0298436746), (1.9911653334, 1.0298436746))
                Line((2.1951653296, 2.4538436994), (2.1951653296, 1.0298436746))
                Line((1.9971653754, 2.4538436994), (2.1951653296, 2.4538436994))
                Line((1.7371651465, 1.6998436913), (1.9971653754, 2.4538436994))
                Line((1.7331654364, 1.6998436913), (1.7371651465, 1.6998436913))
                Line((1.4711653525, 2.4538436994), (1.7331654364, 1.6998436913))
                Line((1.2751652533, 2.4538436994), (1.4711653525, 2.4538436994))
                Line((1.2751652533, 1.0298436746), (1.2751652533, 2.4538436994))
            make_face()
            # Profile area: 0.5180639211, perimeter: 5.5759997368
            with BuildLine():
                Line((2.9951650435, 1.0298436746), (2.3871652418, 1.0298436746))
                Line((2.9951650435, 1.2338436708), (2.9951650435, 1.0298436746))
                Line((2.591165238, 1.2338436708), (2.9951650435, 1.2338436708))
                Line((2.591165238, 1.6518437133), (2.591165238, 1.2338436708))
                Line((2.9431654745, 1.6518437133), (2.591165238, 1.6518437133))
                Line((2.9431654745, 1.8438436851), (2.9431654745, 1.6518437133))
                Line((2.591165238, 1.8438436851), (2.9431654745, 1.8438436851))
                Line((2.591165238, 2.2618437872), (2.591165238, 1.8438436851))
                Line((2.9951650435, 2.2618437872), (2.591165238, 2.2618437872))
                Line((2.9951650435, 2.4538436994), (2.9951650435, 2.2618437872))
                Line((2.3871652418, 2.4538436994), (2.9951650435, 2.4538436994))
                Line((2.3871652418, 1.0298436746), (2.3871652418, 2.4538436994))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a vertical rectangular duct or channel with two parallel elongated slots or grooves running along its length and a hexagonal or polygonal cross-section, featuring a dark blue metallic finish with subtle shading that suggests depth and structural edges.
def model_91419_b4303ed7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3578486039, perimeter: 7.0851199765
            with BuildLine():
                Line((0.25, 0), (-0.25, 0))
                Line((0.25, 0), (0.25, 1.6000000238))
                Line((0.25, 1.6000000238), (0.15, 1.6000000238))
                Line((0.15, 1.6000000238), (0.15, 0.200000003))
                CenterArc((0, 0.2594617882), 0.1613558301, -158.3760361333, 136.7520722667)
                Line((-0.15, 1.6000000238), (-0.15, 0.200000003))
                Line((-0.25, 1.6000000238), (-0.15, 1.6000000238))
                Line((-0.25, 0), (-0.25, 1.6000000238))
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a pentahedron or wedge-shaped connector featuring a rectangular body with a pointed pyramidal projection on one end, commonly used as a plug, adapter, or mechanical fastening component.
def model_91546_80acf346_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.6913429511, perimeter: 15.5884572681
            with BuildLine():
                Line((-4.5980762114, 0.5), (0.5980762114, 0.5))
                Line((0.5980762114, 0.5), (-2, 5))
                Line((-2, 5), (-4.5980762114, 0.5))
            make_face()
        # OneSide extrude, distance=10.5
        extrude(amount=10.5)
    return part.part


# Description: This is a multi-segmented extruded housing or bracket with a rectangular base featuring internal cross-bracing, protruding horizontal flanges or arms extending perpendicular to the main body, and a modular box-like construction with segmented sections stacked vertically.
def model_91561_f2ef3380_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 168.0919982788, perimeter: 88.7199257456
            with BuildLine():
                Line((-5.3361840361, -0.4034208433), (0, 6))
                Line((0, 6), (6, 0))
                Line((6, 0), (8.5, 2.5))
                Line((8.5, 2.5), (4.2979664918, 6.7020335082))
                Line((4.2979664918, 6.7020335082), (5.6045236289, 8.0085906454))
                Line((5.6045236289, 8.0085906454), (3.1661725527, 10.4469417216))
                Line((3.1661725527, 10.4469417216), (8.2605689397, 15.5413381086))
                Line((8.2605689397, 15.5413381086), (4.9512450603, 18.3179084368))
                Line((4.9512450603, 18.3179084368), (0.4845267062, 12.9941399151))
                Line((0.4845267062, 12.9941399151), (-6.6619840771, 20.1406506984))
                Line((-6.6619840771, 20.1406506984), (-9.8730115028, 16.9296232727))
                Line((-9.8730115028, 16.9296232727), (-3.0887286854, 10.1453404553))
                Line((-3.0887286854, 10.1453404553), (-6.4808700941, 6.7531990466))
                Line((-6.4808700941, 6.7531990466), (-4.7847993898, 5.0571283423))
                Line((-4.7847993898, 5.0571283423), (-7.3969977565, 1.543988722))
                Line((-7.3969977565, 1.543988722), (-5.3361840361, -0.4034208433))
            make_face()
        # OneSide extrude, distance=-27.5
        extrude(amount=-27.5)
    return part.part


# Description: This is an elliptical or lens-shaped structural component with a curved, aerodynamic profile featuring internal radial ribs or struts that extend from a central point to reinforce the thin shell walls.
def model_91877_00e41864_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 490.8738521234, perimeter: 78.5398163397
            Circle(12.5)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is an octagonal or elongated hexagonal enclosure or housing with angled faceted sides, featuring mesh or perforated panels on the upper portions and solid panels on the lower section, designed as a protective cage or ventilated container.
def model_92031_7b105c24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4534823168, perimeter: 11.954751476
            with BuildLine():
                Line((4.1071308878, -1.7538432036), (4.6112709332, -0.7150091707))
                Line((4.6112709332, -0.7150091707), (3.9636842931, 0.2410059322))
                Line((3.9636842931, 0.2410059322), (2.8119576076, 0.1581870021))
                Line((2.8119576076, 0.1581870021), (2.3078175622, -0.8806470309))
                Line((2.3078175622, -0.8806470309), (2.9554042023, -1.8366621337))
                Line((2.9554042023, -1.8366621337), (4.1071308878, -1.7538432036))
            make_face()
            with BuildLine():
                CenterArc((3.4595442477, -0.7978281008), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a hexagonal or polyhedron-shaped container or housing with an angular, faceted geometric form featuring multiple planar surfaces, some appearing as mesh or perforated panels, and what appears to be an open or recessed central area.
def model_92032_272677e5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3383124663, perimeter: 5.2539744581
            with BuildLine():
                Line((1.1688671351, -0.4186817348), (1.6336251366, -0.1863027341))
                Line((1.6336251366, -0.1863027341), (1.6647580194, 0.3323790023))
                Line((1.6647580194, 0.3323790023), (1.2311329007, 0.6186817378))
                Line((1.2311329007, 0.6186817378), (0.7663748991, 0.3863027371))
                Line((0.7663748991, 0.3863027371), (0.7352420163, -0.1323789993))
                Line((0.7352420163, -0.1323789993), (1.1688671351, -0.4186817348))
            make_face()
            with BuildLine():
                CenterArc((1.2000000179, 0.1000000015), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a phone mount bracket with an elongated, curved body featuring two large oval cutouts for structural lightness, textured grip surfaces on the sides, and a spherical ball joint at the top for adjustable device attachment.
def model_92552_38c9173a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.242478399, perimeter: 14.7964594301
            with BuildLine():
                CenterArc((0.6, 0), 1.4, 0, 180)
                Line((2, 3), (2, 0))
                CenterArc((0.6, 3), 1.4, 180, 180)
                Line((-0.8, 0), (-0.8, 3))
            make_face()
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                Line((-0.5025, 0), (-0.8, 0))
                CenterArc((0.6, 0), 1.4, -180, 180)
                Line((2, 0), (1.7025, 0))
                CenterArc((0.6, 0), 1.1025, -180, 180)
            make_face()
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                Line((1.7025, 3), (2, 3))
                CenterArc((0.6, 3), 1.1025, 180, 180)
                Line((-0.8, 3), (-0.5025, 3))
                CenterArc((0.6, 3), 1.4, 180, 180)
            make_face()
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                CenterArc((0.6, 0), 1.1025, 0, 180)
                Line((2, 0), (1.7025, 0))
                CenterArc((0.6, 0), 1.4, 0, 180)
                Line((-0.5025, 0), (-0.8, 0))
            make_face()
            # Profile area: 4.0183562586, perimeter: 13.9145657569
            with BuildLine():
                Line((3.2464222086, 4.9227432098), (2, 3))
                CenterArc((3.5184006291, 5.3422998076), 0.5, -122.9534065898, 320.7752392992)
                Line((0.587134272, 4.399940882), (3.0423942103, 5.1892707605))
                CenterArc((0.6, 3), 1.4, 90.5265444946, 89.4734555054)
                Line((-0.8, 3), (-0.5025, 3))
                CenterArc((0.6, 3), 1.1025, 0, 180)
                Line((1.7025, 3), (2, 3))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a right-angle triangular bracket or frame corner brace with three equal-length sides forming an isosceles right triangle, featuring a hollow interior and reinforced edges with rounded corner joints.
def model_92554_c930ff00_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.841006918, perimeter: 90.6241884517
            with BuildLine():
                Line((-11.8848865799, -16.0397587934), (-12.5848865799, -16.0397587934))
                Line((-12.5848865799, -16.0397587934), (-12.5848865799, -16.3397587934))
                Line((-12.5848865799, -16.3397587934), (-3.7848865799, -16.3397587934))
                Line((-3.7848865799, -16.3397587934), (-3.7848865799, 1.7602412066))
                Line((-3.7848865799, 1.7602412066), (-4.5848865799, 1.7602412066))
                Line((-4.5848865799, 1.7602412066), (-4.5848865799, 1.4602412066))
                Line((-4.0848865799, 1.4602412066), (-4.5848865799, 1.4602412066))
                Line((-4.0848865799, 0.6602873268), (-4.0848865799, 1.4602412066))
                Line((-11.8848865799, -16.0397587934), (-4.0848865799, 0.6602873268))
            make_face()
            with BuildLine():
                Line((-11.5848865799, -16.0397587934), (-4.0848865799, 0.3386873268))
                Line((-4.0848865799, -16.0397587934), (-4.0848865799, 0.3386873268))
                Line((-11.5848865799, -16.0397587934), (-4.0848865799, -16.0397587934))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a long, slender curved trim strip or deflector with a tapered profile, featuring a slight downward arc and what appears to be mounting holes or attachment points along its length.
def model_93963_e78f0c67_0000():
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
        # Sketch6 -> Extrude16 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.432545151, perimeter: 11.440908391
            with BuildLine():
                Line((-2.549999943, 0.0099999998), (-2.1000000313, 0.0099999998))
                _nurbs_edge([(-2.510461833, -0.2563434838), (-2.5121014177, -0.2563588991), (-2.5153248203, -0.2562068249), (-2.5199926255, -0.255430009), (-2.5258803905, -0.2532922887), (-2.5326683802, -0.2487439416), (-2.5388632049, -0.2422452607), (-2.5444332181, -0.2336860832), (-2.5493351085, -0.2229105977), (-2.5535207925, -0.2097656926), (-2.5569466106, -0.1941641448), (-2.5595830919, -0.1761501068), (-2.5614242077, -0.1559590992), (-2.5625013744, -0.1341093896), (-2.56287764, -0.1113506266), (-2.5626345638, -0.0885573799), (-2.5618627152, -0.0666461306), (-2.5606512414, -0.0464795584), (-2.559079269, -0.028785365), (-2.5572049408, -0.0140396407), (-2.5550648657, -0.0024798956), (-2.5531568417, 0.0041480372), (-2.5516195489, 0.0076449695), (-2.5505476512, 0.0093237402), (-2.549999943, 0.0099999998)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-2.3225653969, -0.2563434838), (-2.510461833, -0.2563434838))
                Line((-1.444688605, -0.244022406), (-2.3225653969, -0.2563434838))
                Line((-0.6961831297, -0.2655842922), (-1.444688605, -0.244022406))
                Line((0.3788309067, -0.3210291422), (-0.6961831297, -0.2655842922))
                Line((1.1119350347, -0.3733937227), (0.3788309067, -0.3210291422))
                Line((1.7506958983, -0.4476466154), (1.1119350347, -0.3733937227))
                Line((1.9635241202, -0.4750778085), (1.7506958983, -0.4476466154))
                Line((2.4874797947, -0.5584547204), (1.9635241202, -0.4750778085))
                Line((2.8797832003, -0.6270853487), (2.4874797947, -0.5584547204))
                _nurbs_edge([(2.915940392, -0.3946278775), (2.9175786139, -0.3970961985), (2.9206510748, -0.4021916526), (2.9246478244, -0.4103112636), (2.9287439871, -0.4220972552), (2.9317732909, -0.438438817), (2.932696725, -0.4563444412), (2.9315624434, -0.4756617493), (2.9285273663, -0.4960754686), (2.9239175845, -0.5170354541), (2.9181680282, -0.5378411839), (2.9117613495, -0.557729749), (2.9051707352, -0.5759647231), (2.8988096398, -0.5919163452), (2.8929648018, -0.6051792979), (2.88778315, -0.6155897867), (2.8842174816, -0.6216103239), (2.8818729898, -0.624843101), (2.8804555409, -0.6264322664), (2.8797832003, -0.6270853487)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-2.1000000313, 0.0099999998), (-2.088446021, 0.0103737102), (-2.0637184938, 0.0110933952), (-2.0217687224, 0.012089715), (-1.9561084994, 0.0132515557), (-1.8581011881, 0.0144235764), (-1.7450961579, 0.0153090913), (-1.6190520106, 0.0158969569), (-1.4832771731, 0.0161696593), (-1.3417967094, 0.0160987606), (-1.1987748493, 0.0156406509), (-1.0578995844, 0.0147317848), (-0.9218247058, 0.0132849121), (-0.7914814455, 0.0111828195), (-0.6657615704, 0.0082793757), (-0.5423299511, 0.0044230286), (-0.4182258529, -0.0005239983), (-0.2905611377, -0.0066639294), (-0.157136842, -0.0140443812), (-0.0172013074, -0.0226330671), (0.1287499503, -0.0323363651), (0.2793635941, -0.0430267632), (0.4327440184, -0.0545665231), (0.5868063766, -0.0668338487), (0.7395896658, -0.0797454777), (0.8896430154, -0.0932871006), (1.0361268905, -0.1075122961), (1.1787328785, -0.1225211214), (1.3176551927, -0.1384445896), (1.453553704, -0.1554275762), (1.5874987872, -0.1736106611), (1.7209858818, -0.1931167253), (1.8556813075, -0.2140176411), (1.9928887339, -0.2362792367), (2.1331107569, -0.2597144979), (2.2755255884, -0.2839267476), (2.4175943386, -0.3082700066), (2.5543560466, -0.3317663213), (2.6789702401, -0.3531958466), (2.7840477203, -0.3712954673), (2.8628077054, -0.3849350064), (2.9006954527, -0.3916115613), (2.9141294682, -0.3940977891), (2.9164440472, -0.3946375336), (2.915940392, -0.3946278775)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, each_side=0.062
        extrude(amount=0.062, both=True)
    return part.part


# Description: This is a structural bracket or support arm with an elongated tapered body, featuring a vertical reinforced hub on one end and multiple internal ribs/gussets for strength, designed to support or connect components while minimizing weight through hollow construction.
def model_94479_f401cd52_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 58.496828589, perimeter: 65.3903845026
            with BuildLine():
                Line((-2.1816740531, 2.3822239482), (-0.3958230971, 6.7843960283))
                Line((-4.0000000596, -2.1000000313), (-2.1816740531, 2.3822239482))
                Line((-4.3000000641, -2.2000000328), (-4.0000000596, -2.1000000313))
                Line((-5.1100444285, -3.9550961556), (-4.3000000641, -2.2000000328))
                Line((-6.7000000998, -7.4000001103), (-5.1100444285, -3.9550961556))
                Line((-3.2874252591, -5.8733218921), (-6.7000000998, -7.4000001103))
                Line((-2.9000000432, -5.7000000849), (-3.2874252591, -5.8733218921))
                Line((-2.7000000402, -4.3000000641), (-2.9000000432, -5.7000000849))
                Line((2.4000000358, -4.3000000641), (-2.7000000402, -4.3000000641))
                Line((2.8363451796, -5.8068105604), (2.4000000358, -4.3000000641))
                Line((3.3000000492, -6.0000000894), (2.8363451796, -5.8068105604))
                Line((6.9000001028, -7.5000001118), (3.3000000492, -6.0000000894))
                Line((5.1227331663, -4.0349942229), (6.9000001028, -7.5000001118))
                Line((4.1974236184, -2.2309866391), (5.1227331663, -4.0349942229))
                Line((3.7978453709, -2.0644957026), (4.1974236184, -2.2309866391))
                Line((1.6467823117, 2.4743762331), (3.7978453709, -2.0644957026))
                Line((-0.3958230971, 6.7843960283), (1.6467823117, 2.4743762331))
            make_face()
            with BuildLine():
                Line((-2.2701069759, -2.8464610528), (-1.1000000164, -2.8464610528))
                Line((-1.8579160651, -1.6357076434), (-2.2701069759, -2.8464610528))
                Line((-1.6819504973, -1.7345657803), (-1.8579160651, -1.6357076434))
                Line((-0.6866983977, 1.1888486891), (-1.6819504973, -1.7345657803))
                Line((-0.9099621966, 1.3142791553), (-0.6866983977, 1.1888486891))
                Line((-0.3000000045, 2.4000000358), (-0.9099621966, 1.3142791553))
                Line((0.4147545813, 1.3142791553), (-0.3000000045, 2.4000000358))
                Line((0.1635168152, 1.2066244716), (0.4147545813, 1.3142791553))
                Line((1.4386270034, -1.7691479156), (0.1635168152, 1.2066244716))
                Line((1.6000000238, -1.7000000253), (1.4386270034, -1.7691479156))
                Line((2.1000000313, -2.866868763), (1.6000000238, -1.7000000253))
                Line((0.8776005141, -2.866868763), (2.1000000313, -2.866868763))
                Line((0.8298325193, -2.6773719177), (0.8776005141, -2.866868763))
                Line((-1.041547833, -2.6773719177), (0.8298325193, -2.6773719177))
                Line((-1.1000000164, -2.8464610528), (-1.041547833, -2.6773719177))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4084419238, perimeter: 26.8070812597
            with BuildLine():
                Line((-1.1000000164, -2.8464610528), (-1.041547833, -2.6773719177))
                Line((-1.041547833, -2.6773719177), (0.8298325193, -2.6773719177))
                Line((0.8298325193, -2.6773719177), (0.8776005141, -2.866868763))
                Line((0.8776005141, -2.866868763), (2.1000000313, -2.866868763))
                Line((2.1000000313, -2.866868763), (1.6000000238, -1.7000000253))
                Line((1.6000000238, -1.7000000253), (1.4386270034, -1.7691479156))
                Line((1.4386270034, -1.7691479156), (0.1635168152, 1.2066244716))
                Line((0.1635168152, 1.2066244716), (0.4147545813, 1.3142791553))
                Line((0.4147545813, 1.3142791553), (-0.3000000045, 2.4000000358))
                Line((-0.3000000045, 2.4000000358), (-0.9099621966, 1.3142791553))
                Line((-0.9099621966, 1.3142791553), (-0.6866983977, 1.1888486891))
                Line((-0.6866983977, 1.1888486891), (-1.6819504973, -1.7345657803))
                Line((-1.6819504973, -1.7345657803), (-1.8579160651, -1.6357076434))
                Line((-1.8579160651, -1.6357076434), (-2.2701069759, -2.8464610528))
                Line((-2.2701069759, -2.8464610528), (-1.1000000164, -2.8464610528))
            make_face()
            with BuildLine():
                Line((-1.3599120823, -2.0563964676), (1.1539396392, -2.0563964676))
                Line((-0.2527418202, 1.3828587187), (-1.3599120823, -2.0563964676))
                Line((1.1539396392, -2.0563964676), (-0.2527418202, 1.3828587187))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.0257925275, perimeter: 21.557146028
            with BuildLine():
                Line((-0.3958230971, 6.7843960283), (1.6467823117, 2.4743762331))
                Line((1.8000000268, 2.9000000432), (1.6467823117, 2.4743762331))
                Line((1.4000000209, 3.4000000507), (1.8000000268, 2.9000000432))
                Line((1.5293699752, 4.3269092188), (1.4000000209, 3.4000000507))
                Line((-0.400000006, 7.9000001177), (1.5293699752, 4.3269092188))
                Line((-2.0830904967, 4.3269092188), (-0.400000006, 7.9000001177))
                Line((-1.9682694151, 3.4063062356), (-2.0830904967, 4.3269092188))
                Line((-2.1979115784, 2.8402319414), (-1.9682694151, 3.4063062356))
                Line((-2.1979115784, 2.8402319414), (-2.1979115784, 2.4743762331))
                Line((-2.1979115784, 2.4743762331), (-2.1816740531, 2.3822239482))
                Line((-2.1816740531, 2.3822239482), (-0.3958230971, 6.7843960283))
            make_face()
            # Profile area: 3.7687085419, perimeter: 17.3190303813
            with BuildLine():
                Line((-5.1100444285, -3.9550961556), (-6.0000000894, -4.5000000671))
                Line((-6.0000000894, -4.5000000671), (-7.4000001103, -8.0000001192))
                Line((-7.4000001103, -8.0000001192), (-3.4000000507, -6.6000000983))
                Line((-3.4000000507, -6.6000000983), (-3.2874252591, -5.8733218921))
                Line((-3.2874252591, -5.8733218921), (-6.7000000998, -7.4000001103))
                Line((-6.7000000998, -7.4000001103), (-5.1100444285, -3.9550961556))
            make_face()
            # Profile area: 3.0055654027, perimeter: 17.2624488254
            with BuildLine():
                Line((3.3000000492, -6.0000000894), (3.5923129227, -6.6534053361))
                Line((3.5923129227, -6.6534053361), (7.4000001103, -8.0000001192))
                Line((7.4000001103, -8.0000001192), (5.9000000879, -4.5000000671))
                Line((5.9000000879, -4.5000000671), (5.1227331663, -4.0349942229))
                Line((5.1227331663, -4.0349942229), (6.9000001028, -7.5000001118))
                Line((6.9000001028, -7.5000001118), (3.3000000492, -6.0000000894))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slightly beveled edge, featuring internal diagonal reinforcement ribs or creases that provide structural stiffness to the otherwise thin, flat component.
def model_95914_696a062f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 375, perimeter: 80
            with BuildLine():
                Line((1, 26), (1, 1))
                Line((1, 1), (16, 1))
                Line((16, 1), (16, 26))
                Line((16, 26), (1, 26))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slight 3D depth, featuring a beveled or chamfered edge on one side and internal diagonal reinforcement or support lines visible within the geometry.
def model_95918_12be82d7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 300, perimeter: 70
            with BuildLine():
                Line((3, 25), (3, 5))
                Line((3, 5), (18, 5))
                Line((18, 5), (18, 25))
                Line((18, 25), (3, 25))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved, box-like industrial component with a rounded cylindrical surface on one side, featuring multiple internal structural ribs or reinforcement elements visible through transparent sections, and what appears to be mounting flanges or attachment points.
def model_98397_d10953a3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7549678305, perimeter: 41.4064801568
            with BuildLine():
                CenterArc((-1.5, -1.5), 1.5, -180, 90)
                Line((-1.5, -3), (1.5, -3))
                CenterArc((1.5, -1.5), 1.5, -90, 90)
                Line((3, -1.5), (3, 1.5))
                CenterArc((1.5, 1.5), 1.5, 0, 90)
                Line((1.5, 3), (-1.5, 3))
                CenterArc((-1.5, 1.5), 1.5, 90, 90)
                Line((-3, 1.5), (-3, -1.5))
            make_face()
            with BuildLine():
                Line((2.7703273588, -1.5), (2.7703273588, 1.5))
                CenterArc((1.5, -1.5), 1.2703273588, -90, 90)
                Line((-1.5, -2.7703273588), (1.5, -2.7703273588))
                CenterArc((-1.5, -1.5), 1.2703273588, -180, 90)
                Line((-2.7703273588, 1.5), (-2.7703273588, -1.5))
                CenterArc((-1.5, 1.5), 1.2703273588, 90, 90)
                Line((1.5, 2.7703273588), (-1.5, 2.7703273588))
                CenterArc((1.5, 1.5), 1.2703273588, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.3136156401, perimeter: 19.981702196
            with BuildLine():
                CenterArc((1.5, 1.5), 1.2703273588, 0, 90)
                Line((1.5, 2.7703273588), (-1.5, 2.7703273588))
                CenterArc((-1.5, 1.5), 1.2703273588, 90, 90)
                Line((-2.7703273588, 1.5), (-2.7703273588, -1.5))
                CenterArc((-1.5, -1.5), 1.2703273588, -180, 90)
                Line((-1.5, -2.7703273588), (1.5, -2.7703273588))
                CenterArc((1.5, -1.5), 1.2703273588, -90, 90)
                Line((2.7703273588, -1.5), (2.7703273588, 1.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or arm assembly with an angular, bent tubular structure featuring hexagonal cross-sections and triangulated reinforcement panels, designed to support loads at two perpendicular endpoints.
def model_98960_f2639863_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.9120000161, perimeter: 4.760000017
            with BuildLine():
                Line((0.4494013592, -3.5519999678), (-1.4505986408, -3.5519999678))
                Line((0.4494013592, -3.0719999754), (0.4494013592, -3.5519999678))
                Line((-1.4505986408, -3.0719999432), (0.4494013592, -3.0719999754))
                Line((-1.4505986408, -3.5519999678), (-1.4505986408, -3.0719999432))
            make_face()
            # Profile area: 26.7210624139, perimeter: 32.7429997434
            with BuildLine():
                Line((-1.450598653, -4.2717095585), (-0.050598653, -5.079999967))
                Line((-0.050598653, -5.079999967), (1.8994013653, -5.08))
                Line((1.8994013653, -5.08), (3.2994012969, -3.6800000286))
                Line((3.2994012969, -3.6800000286), (3.2994014216, 3.6800000286))
                Line((3.2994014216, 3.6800000286), (1.8994014216, 5.08))
                Line((1.8994014216, 5.08), (-1.4505986408, 5.0800000567))
                Line((-1.4505986408, 3.1800000567), (-1.4505986408, 5.0800000567))
                Line((0.7644013592, 3.1800000567), (-1.4505986408, 3.1800000567))
                CenterArc((0.7644013592, 2.5450000567), 0.635, 0, 90)
                Line((1.3994013592, -2.9169999678), (1.3994013592, 2.5450000567))
                CenterArc((0.7644013592, -2.9169999678), 0.635, -90, 90)
                Line((0.7644013592, -3.5519999678), (0.4494013592, -3.5519999678))
                Line((0.4494013592, -3.5519999678), (-1.4505986408, -3.5519999678))
                Line((-1.4505986408, -3.5519999678), (-1.450598653, -4.2717095585))
            make_face()
        # Symmetric extrude, full_length=True, total=1.9
        extrude(amount=0.95, both=True)
    return part.part


# Description: This is an elongated rectangular tray or channel with a shallow, open-top box design, featuring a sloped end section on the left side and a flat bottom base.
def model_99059_8a1d187a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.28, perimeter: 8
            with BuildLine():
                Line((-3.2, -0.0125979881), (-1.6, -0.0125979881))
                Line((-1.6, -0.0125979881), (-1.6, 0.6874020119))
                Line((-1.6, 0.6874020119), (-0.8, 0.6874020119))
                Line((-0.8, 0.6874020119), (-0.8, 1.5874020119))
                Line((-3.2, 1.5874020119), (-0.8, 1.5874020119))
                Line((-3.2, -0.0125979881), (-3.2, 1.5874020119))
            make_face()
        # OneSide extrude, distance=-14.4
        extrude(amount=-14.4)
    return part.part


# Description: This is a boat hull with an elongated, tapered shape featuring a curved bottom, open top cabin area with structural frame elements, and dark hull sides contrasting with a light blue interior deck configuration.
def model_99449_a5ffa5ad_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 41.3924191087, perimeter: 86.390974469
            with BuildLine():
                CenterArc((5.5, -3), 2, -90, 90)
                Line((7.5, 3), (7.5, -3))
                CenterArc((5.5, 3), 2, 0, 90)
                Line((-5.5, 5), (5.5, 5))
                CenterArc((-5.5, 3), 2, 90, 90)
                Line((-7.5, -3), (-7.5, 3))
                CenterArc((-5.5, -3), 2, 180, 90)
                Line((5.5, -5), (-5.5, -5))
            make_face()
            with BuildLine():
                Line((6.8518457467, -1.1857264099), (6.8518457467, 2.7396987169))
                CenterArc((4.8518457467, -1.1857264099), 2, -90, 90)
                Line((-4.8518457467, -3.1857264099), (4.8518457467, -3.1857264099))
                CenterArc((-4.8518457467, -1.1857264099), 2, -180, 90)
                Line((-6.8518457467, 2.7396987169), (-6.8518457467, -1.1857264099))
                CenterArc((-4.8518457467, 2.7396987169), 2, 90, 90)
                Line((4.8518457467, 4.7396987169), (-4.8518457467, 4.7396987169))
                CenterArc((4.8518457467, 2.7396987169), 2, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 105.1739515056, perimeter: 39.8246038547
            with BuildLine():
                CenterArc((4.8518457467, 2.7396987169), 2, 0, 90)
                Line((4.8518457467, 4.7396987169), (-4.8518457467, 4.7396987169))
                CenterArc((-4.8518457467, 2.7396987169), 2, 90, 90)
                Line((-6.8518457467, 2.7396987169), (-6.8518457467, -1.1857264099))
                CenterArc((-4.8518457467, -1.1857264099), 2, -180, 90)
                Line((-4.8518457467, -3.1857264099), (4.8518457467, -3.1857264099))
                CenterArc((4.8518457467, -1.1857264099), 2, -90, 90)
                Line((6.8518457467, -1.1857264099), (6.8518457467, 2.7396987169))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical roller or drum with a smooth, uniform circular cross-section and flat circular end faces, featuring a wireframe mesh surface pattern typical of CAD visualization.
def model_99925_48150ea4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


MODELS = {
    "model_78513_7ad0bd6a_0001": {"func": model_78513_7ad0bd6a_0001, "volume": 97.9611421242, "area": 219.4716627798},
    "model_78513_7ad0bd6a_0003": {"func": model_78513_7ad0bd6a_0003, "volume": 147.3216888581, "area": 358.1362465776},
    "model_78865_cb0167cd_0000": {"func": model_78865_cb0167cd_0000, "volume": 40.0788682782, "area": 105.6046370504},
    "model_79423_62db5fc6_0009": {"func": model_79423_62db5fc6_0009, "volume": 0.6779911486, "area": 7.310884841},
    "model_79423_62db5fc6_0011": {"func": model_79423_62db5fc6_0011, "volume": 0.7054601837, "area": 7.7229203673},
    "model_79423_62db5fc6_0015": {"func": model_79423_62db5fc6_0015, "volume": 13.3172123438, "area": 64.0130964915},
    "model_79637_fac1d5d3_0000": {"func": model_79637_fac1d5d3_0000, "volume": 6.066367536, "area": 32.7540578817},
    "model_80188_c67d0fb1_0000": {"func": model_80188_c67d0fb1_0000, "volume": 12844.4506584121, "area": 5983.5595174147},
    "model_80497_abe71aa5_0001": {"func": model_80497_abe71aa5_0001, "volume": 882.6172512352, "area": 532.9601685881},
    "model_80755_807d96f0_0000": {"func": model_80755_807d96f0_0000, "volume": 14.4675528099, "area": 53.0586540985},
    "model_80756_6f2e842f_0000": {"func": model_80756_6f2e842f_0000, "volume": 48, "area": 128},
    "model_80763_97f05760_0000": {"func": model_80763_97f05760_0000, "volume": 66.5156787659, "area": 200.7061867954},
    "model_80765_1b57e0b1_0000": {"func": model_80765_1b57e0b1_0000, "volume": 502.6548245744, "area": 351.8583772021},
    "model_80765_1b57e0b1_0001": {"func": model_80765_1b57e0b1_0001, "volume": 1058.3240567186, "area": 681.7256171344},
    "model_80767_2a27abc1_0000": {"func": model_80767_2a27abc1_0000, "volume": 21.4413698608, "area": 155.1946770873},
    "model_81123_41bb9143_0008": {"func": model_81123_41bb9143_0008, "volume": 24.96, "area": 83.2},
    "model_81224_f2807572_0000": {"func": model_81224_f2807572_0000, "volume": 128.4876502772, "area": 286.5085996439},
    "model_82041_6a8544dd_0000": {"func": model_82041_6a8544dd_0000, "volume": 207000, "area": 86900},
    "model_82169_acef7d14_0001": {"func": model_82169_acef7d14_0001, "volume": 1130.9733552923, "area": 716.2831250185},
    "model_82177_11e98151_0000": {"func": model_82177_11e98151_0000, "volume": 34.1160125029, "area": 90.4834642278},
    "model_83338_b9bb889f_0001": {"func": model_83338_b9bb889f_0001, "volume": 243.9303172918, "area": 425.1014054436},
    "model_83380_ab6e9bd8_0000": {"func": model_83380_ab6e9bd8_0000, "volume": 53.6799860357, "area": 153.2343220245},
    "model_83386_f927e369_0000": {"func": model_83386_f927e369_0000, "volume": 5.0265482457, "area": 30.1592894745},
    "model_83406_87f89dc9_0000": {"func": model_83406_87f89dc9_0000, "volume": 145.5605515982, "area": 214.2744560908},
    "model_83562_851e465d_0000": {"func": model_83562_851e465d_0000, "volume": 15.5854931064, "area": 83.2660106449},
    "model_84610_091c78e8_0000": {"func": model_84610_091c78e8_0000, "volume": 8.2922724792, "area": 100.3801405376},
    "model_85419_1e3af3b4_0001": {"func": model_85419_1e3af3b4_0001, "volume": 89.289814101, "area": 278.1482167377},
    "model_85617_4879c1a8_0002": {"func": model_85617_4879c1a8_0002, "volume": 0.0157079633, "area": 0.3769911184},
    "model_85638_2ab1040c_0000": {"func": model_85638_2ab1040c_0000, "volume": 511.7750123904, "area": 686.4283896348},
    "model_86296_8a6ed4d3_0008": {"func": model_86296_8a6ed4d3_0008, "volume": 0.0193548, "area": 0.433832},
    "model_86381_dcef1ea4_0000": {"func": model_86381_dcef1ea4_0000, "volume": 8.960000267, "area": 95.6800016165},
    "model_86382_d80c0d30_0000": {"func": model_86382_d80c0d30_0000, "volume": 1.9634954085, "area": 16.1006623496},
    "model_86704_3f8f3bfe_0007": {"func": model_86704_3f8f3bfe_0007, "volume": 294.967152, "area": 1051.6108},
    "model_86898_b705167e_0000": {"func": model_86898_b705167e_0000, "volume": 0.0457595631, "area": 1.2362383262},
    "model_87046_b31418fa_0000": {"func": model_87046_b31418fa_0000, "volume": 88.7859405722, "area": 360.9710488022},
    "model_87358_854d47fe_0008": {"func": model_87358_854d47fe_0008, "volume": 3.5088643032, "area": 14.4124762293},
    "model_87564_c58c72e9_0002": {"func": model_87564_c58c72e9_0002, "volume": 4170.9853250414, "area": 2926.6733182592},
    "model_87757_eb92dadf_0015": {"func": model_87757_eb92dadf_0015, "volume": 0.0306323341, "area": 2.1697456051},
    "model_89527_b3bf425d_0001": {"func": model_89527_b3bf425d_0001, "volume": 0.0989601686, "area": 1.4608405839},
    "model_89527_b3bf425d_0011": {"func": model_89527_b3bf425d_0011, "volume": 93.6, "area": 188.2},
    "model_90223_9e1de020_0000": {"func": model_90223_9e1de020_0000, "volume": 11873.0181872674, "area": 3189.8611980633},
    "model_90482_87d35b1c_0000": {"func": model_90482_87d35b1c_0000, "volume": 46.7653718044, "area": 82.7653718044},
    "model_90917_4d6ea65a_0000": {"func": model_90917_4d6ea65a_0000, "volume": 10.0902607512, "area": 80.1391889676},
    "model_91419_b4303ed7_0000": {"func": model_91419_b4303ed7_0000, "volume": 0.178924302, "area": 4.2582571961},
    "model_91546_80acf346_0000": {"func": model_91546_80acf346_0000, "volume": 122.7591009864, "area": 187.0614872174},
    "model_91561_f2ef3380_0000": {"func": model_91561_f2ef3380_0000, "volume": 4622.5299526669, "area": 2775.981954563},
    "model_91877_00e41864_0000": {"func": model_91877_00e41864_0000, "volume": 171.8058482432, "area": 1009.2366399657},
    "model_92031_7b105c24_0000": {"func": model_92031_7b105c24_0000, "volume": 0.8720893901, "area": 10.0798155193},
    "model_92032_272677e5_0000": {"func": model_92032_272677e5_0000, "volume": 0.1353249865, "area": 2.7782147158},
    "model_92552_38c9173a_0000": {"func": model_92552_38c9173a_0000, "volume": 6.8384251607, "area": 43.4143868236},
    "model_92554_c930ff00_0000": {"func": model_92554_c930ff00_0000, "volume": 9.4728055344, "area": 96.1813645975},
    "model_93963_e78f0c67_0000": {"func": model_93963_e78f0c67_0000, "volume": 0.1776358996, "area": 4.2837595951},
    "model_94479_f401cd52_0000": {"func": model_94479_f401cd52_0000, "volume": 144.3064197718, "area": 283.1759623878},
    "model_95914_696a062f_0000": {"func": model_95914_696a062f_0000, "volume": 187.5, "area": 790},
    "model_95918_12be82d7_0000": {"func": model_95918_12be82d7_0000, "volume": 150, "area": 635},
    "model_98397_d10953a3_0000": {"func": model_98397_d10953a3_0000, "volume": 38.4316469727, "area": 265.1787166271},
    "model_98960_f2639863_0002": {"func": model_98960_f2639863_0002, "volume": 52.502818617, "area": 119.3018244048},
    "model_99059_8a1d187a_0000": {"func": model_99059_8a1d187a_0000, "volume": 47.232, "area": 121.76},
    "model_99449_a5ffa5ad_0000": {"func": model_99449_a5ffa5ad_0000, "volume": 251.4017413732, "area": 374.9296783067},
    "model_99925_48150ea4_0000": {"func": model_99925_48150ea4_0000, "volume": 384.8451000647, "area": 296.8805057642},
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
