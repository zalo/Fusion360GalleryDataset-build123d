"""Batch 010 - passing/01_2ops
218 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a cylindrical tube or barrel with rounded ends featuring a central longitudinal slot or channel running along its length and a circular hole through one end.
def model_31962_e5291336_0055():
    """Model: goma"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-25, -8), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-25, -8), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.45
        extrude(amount=1.45)
    return part.part


# Description: This is an elongated, boat-shaped or pod-like component with a curved, streamlined profile featuring a mesh or perforated pattern on the upper surface and a solid bottom, resembling an aerodynamic duct or air intake housing.
def model_32074_105fccde_0013():
    """Model: Component20"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0589048623, perimeter: 1.096477507
            with Locations((0.5500000082, 0.1000000015)):
                Ellipse(0.25, 0.075, rotation=26.8781397521)
        # OneSide extrude, distance=0.11
        extrude(amount=0.11)
    return part.part


# Description: This is an elongated, aerodynamic composite structure with a streamlined oval cross-section, featuring a mesh-textured upper surface and a solid lower surface, resembling a fuselage or aerodynamic fairing component.
def model_32074_105fccde_0014():
    """Model: Component19"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.7156844547
            with Locations((-1.0000000149, 0.7000000104)):
                Ellipse(0.4, 0.1, rotation=20.9443804191)
        # OneSide extrude, distance=0.11
        extrude(amount=0.11)
    return part.part


# Description: This is an elongated, capsule-shaped component with a curved, rounded rectangular profile, featuring a textured or patterned top surface and smooth, tapered ends.
def model_32074_105fccde_0015():
    """Model: Component21"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0235619449, perimeter: 0.6682446518
            with Locations((0.5169157161, -0.1073127124)):
                Ellipse(0.15, 0.05, rotation=36.9775963527)
        # OneSide extrude, distance=0.11
        extrude(amount=0.11)
    return part.part


# Description: This is an elongated, streamlined fuselage or body component with a tapered, aerodynamic shape featuring a triangulated lattice structure on its upper surface and smooth curved sides, designed for lightweight aerospace or marine applications.
def model_32074_105fccde_0016():
    """Model: Component22"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0785398163, perimeter: 2.0319834125
            with Locations((-2.2000000328, 0.7000000104)):
                Ellipse(0.5, 0.05, rotation=22.8635561975)
        # OneSide extrude, distance=0.09
        extrude(amount=0.09)
    return part.part


# Description: This is a streamlined, elongated spindle or shaft component with a pointed nose cone at one end and a tapered body that curves smoothly along its length, featuring a slightly textured or ribbed surface detail on one side.
def model_32074_105fccde_0017():
    """Model: Component23"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0471238898, perimeter: 1.2450041531
            with Locations((-0.0773927977, -0.316225525)):
                Ellipse(0.3, 0.05, rotation=-38.0073259054)
        # OneSide extrude, distance=0.09
        extrude(amount=0.09)
    return part.part


# Description: This is a capsule-shaped or obround cylindrical component featuring a flat circular end face and a hemispherical or rounded end, with a mesh or lattice pattern visible on the curved upper surface suggesting internal structure or a textured exterior finish.
def model_32074_105fccde_0018():
    """Model: Component24"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0157079633, perimeter: 0.4844224113
            with Locations((-0.5002279149, -0.4304829543)):
                Ellipse(0.1, 0.05, rotation=-25.8870262663)
        # OneSide extrude, distance=0.09
        extrude(amount=0.09)
    return part.part


# Description: This is a rectangular prism or box-shaped structural component with a slanted top face and an internal rectangular slot or cutout running along one of its longer sides.
def model_32219_e5edc7ce_0010():
    """Model: CIECZ1 v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 188.16, perimeter: 58.4
            with BuildLine():
                Line((0, 19.6), (0, 0))
                Line((0, 0), (9.6, 0))
                Line((9.6, 0), (9.6, 19.6))
                Line((9.6, 19.6), (0, 19.6))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


# Description: This is a cylindrical housing or enclosure with a rounded rectangular cross-section, featuring a domed or curved top with triangulated panel sections and vertical ribbed/finned sides for structural reinforcement.
def model_32219_e5edc7ce_0036():
    """Model: niewiem v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 88.8533360549, perimeter: 34.3626464545
            with BuildLine():
                CenterArc((3.5089080313, -1.1993084813), 2, -54.8698976458, 72)
                Line((5.4201848282, -0.610223593), (4.1361991564, 3.5556480342))
                CenterArc((2.2249223595, 2.966563146), 2, 17.1301023542, 72)
                Line((2.2552863491, 4.9663326398), (-2.1034664012, 5.032514829))
                CenterArc((-2.1338303908, 3.0327453353), 2, 89.1301023542, 72)
                Line((-4.0263412101, 3.6795859638), (-5.4362128865, -0.445382821))
                CenterArc((-3.5437020672, -1.0922234496), 2, 161.1301023542, 72)
                Line((-4.7437020672, -2.6922234496), (-1.2562979328, -5.3077765504))
                CenterArc((-0.0562979328, -3.7077765504), 2, -126.8698976458, 72)
                Line((1.0945721, -5.343471561), (4.6597780641, -2.8350034918))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a cylindrical mesh or perforated tube with a closed bottom end and an open top end, featuring a textured or mesh surface pattern along its length.
def model_32219_e5edc7ce_0041():
    """Model: kolo - kolo v4 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)
    return part.part


# Description: This is a cylindrical or elliptical bowl-shaped container featuring a curved, tapered sidewall with a wire-frame mesh top opening and a solid base, resembling a strainer, basket, or ventilation duct component.
def model_32220_1fd19c5e_0000():
    """Model: soczewka v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a cylindrical mesh or perforated container with an open top and closed bottom, featuring a curved, tapered body with a textured surface pattern and a distinctive blue-highlighted rim or flange at the top edge.
def model_32220_1fd19c5e_0008():
    """Model: Przycik dobry  v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: These are two curved protective shroud or guard components with mesh/perforated upper sections and solid lower flanges, designed to cover or protect cylindrical machinery or equipment while allowing airflow or visibility through the textured top surfaces.
def model_32220_1fd19c5e_0009():
    """Model: okragle przyciski v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6891868884, perimeter: 3.4205750412
            with BuildLine():
                Line((0.7071067812, -0.7071067812), (0.2474873734, -0.2474873734))
                CenterArc((0, 0), 0.35, -135, 90)
                Line((-0.7071067812, -0.7071067812), (-0.2474873734, -0.2474873734))
                CenterArc((0, 0), 1, -135, 90)
            make_face()
            # Profile area: 0.6891868884, perimeter: 3.4205750412
            with BuildLine():
                CenterArc((0, 0), 1, 45, 90)
                Line((-0.2474873734, 0.2474873734), (-0.7071067812, 0.7071067812))
                CenterArc((0, 0), 0.35, 45, 90)
                Line((0.7071067812, 0.7071067812), (0.2474873734, 0.2474873734))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical mesh container or strainer with an open top, featuring a solid dark base and a blue perforated mesh upper section that allows for filtering or drainage.
def model_32220_1fd19c5e_0010():
    """Model: PRZYCSIK duzy v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is an elongated channel or tray with a rectangular base, curved sides, and a flanged rim at the top, featuring a tapered end and designed for containment or guidance purposes.
def model_32220_1fd19c5e_0016():
    """Model: szkielko blysk v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9656637061, perimeter: 4.6566370614
            with BuildLine():
                CenterArc((0.3, -0.2), 0.2, 0, 90)
                Line((0.2, 0), (0.3, 0))
                CenterArc((0.2, -0.2), 0.2, 90, 90)
                Line((0, -1.8), (0, -0.2))
                CenterArc((0.2, -1.8), 0.2, 180, 90)
                Line((0.3, -2), (0.2, -2))
                CenterArc((0.3, -1.8), 0.2, -90, 90)
                Line((0.5, -0.2), (0.5, -1.8))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a flat quadrilateral plate or panel with a trapezoidal shape and uniform thickness, featuring a diagonal internal edge or ridge that divides the surface into two triangular sections.
def model_32220_1fd19c5e_0017():
    """Model: ekran v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1047127294, perimeter: 18.3792959769
            with BuildLine():
                Line((0, 0), (0, -4.6244959769))
                Line((6.1, 0), (0, -4.6244959769))
                Line((0, 0), (6.1, 0))
            make_face()
            # Profile area: 14.1221793138, perimeter: 18.385025414
            with BuildLine():
                Line((6.1, 0), (0, -4.6244959769))
                Line((0, -4.6244959769), (6.1, -4.6302227258))
                Line((6.1, 0), (6.1, -4.6302227258))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a solar panel mounting bracket with an angular, L-shaped design featuring a flat base plate and an angled support arm, designed to secure and position solar panels at an optimal angle.
def model_32667_426cf6b5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7203687007, perimeter: 17.5650031085
            with BuildLine():
                Line((0, 0), (2.0000000298, 0))
                CenterArc((1.9000000283, 0.5000000075), 0.509901959, -78.690067526, 157.380135052)
                Line((2.0000000298, 1.0000000149), (-3.5000000522, 1.0000000149))
                Line((-3.5000000522, 1.0000000149), (-3.5000000522, 0.8000000119))
                Line((-3.5000000522, 0.8000000119), (2.0000000298, 0.8000000119))
                CenterArc((1.8750000279, 0.5000000075), 0.3250000048, -67.380135052, 134.7602701039)
                Line((0, 0.200000003), (2.0000000298, 0.200000003))
                Line((0, 0), (0, 0.200000003))
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)
    return part.part


# Description: This is a curved bracket or clamp assembly with a C-shaped or U-shaped profile, featuring ribbed reinforcement sections on the inner surfaces and what appears to be mounting flanges or attachment points at both ends.
def model_32775_a79b406b_0005():
    """Model: Rodfij"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0974124099, perimeter: 2.1784778856
            with BuildLine():
                CenterArc((-0.1587946785, -0.0799999982), 0.1345913617, 105.0086741426, 87.8705658151)
                CenterArc((-0.1074999976, -0.0674999985), 0.1873832928, -166.8907918018, 63.7815836037)
                CenterArc((-0.1749999961, -0.3249999927), 0.0790569397, 18.4349488229, 53.1301023542)
                Line((0.0999999978, -0.2999999933), (-0.0999999978, -0.2999999933))
                CenterArc((0.1749999961, -0.3249999927), 0.0790569397, 108.4349488229, 53.1301023542)
                CenterArc((0.1074999976, -0.0674999985), 0.1873832928, -76.8907918018, 63.7815836037)
                CenterArc((0.1587946785, -0.0799999982), 0.1345913617, -12.8792399576, 87.8705658151)
                Line((0.1936491676, 0.0499999989), (0.1499999966, 0.0499999989))
                Line((0.1499999966, 0.0499999989), (0.1499999966, 0.0249999994))
                Line((0.1499999966, 0.0249999994), (0.1249999972, 0.0249999994))
                Line((0.1249999972, 0.0249999994), (0.1249999972, -0.0249999994))
                Line((0.1249999972, -0.0249999994), (0.1499999966, -0.0249999994))
                Line((0.1499999966, -0.0249999994), (0.1499999966, -0.0499999989))
                Line((0.1499999966, -0.0499999989), (0.1936491676, -0.0499999989))
                CenterArc((0, 0), 0.2, -165.5224881447, 151.0449762895)
                Line((-0.1499999966, -0.0499999989), (-0.1936491676, -0.0499999989))
                Line((-0.1499999966, -0.0249999994), (-0.1499999966, -0.0499999989))
                Line((-0.1249999972, -0.0249999994), (-0.1499999966, -0.0249999994))
                Line((-0.1249999972, 0.0249999994), (-0.1249999972, -0.0249999994))
                Line((-0.1499999966, 0.0249999994), (-0.1249999972, 0.0249999994))
                Line((-0.1499999966, 0.0499999989), (-0.1499999966, 0.0249999994))
                Line((-0.1936491676, 0.0499999989), (-0.1499999966, 0.0499999989))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical capsule or rounded-end barrel featuring a flat circular base on one end and a hemispherical or domed cap on the opposite end, with a smooth curved transition between them.
def model_32839_feb1aa29_0001():
    """Model: Handle Spacer - Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2026829916, perimeter: 1.595929068
            Circle(0.254)
        # OneSide extrude, distance=0.381
        extrude(amount=0.381)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slight 3D depth, featuring a beveled or angled edge on one side and two diagonal slot or rib features running across its surface.
def model_32841_954e8c1a_0000():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6649.2941091053, perimeter: 340.9781997157
            with BuildLine():
                Line((170, 10), (59.9091388061, 10))
                Line((170, 70.3982386639), (170, 10))
                Line((59.9091388061, 70.3982386639), (170, 70.3982386639))
                Line((59.9091388061, 10), (59.9091388061, 70.3982386639))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a coffin-shaped enclosure or housing with a tapered hexagonal profile, featuring a transparent or translucent top panel, ventilation slots on the sides, and internal structural ribbing for reinforcement.
def model_32871_04ff3d41_0004():
    """Model: CT003"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.7956899307, perimeter: 26.6307516557
            with BuildLine():
                CenterArc((2.6, -4.8), 1.3, -156.1017195384, 156.1017195384)
                Line((3.9, 0), (3.9, -4.8))
                Line((0, 0), (3.9, 0))
                Line((0, 0), (0, -4.5000098182))
                CenterArc((0.1315, -5.8938), 1.3999797573, 23.8982804616, 71.4914534274)
            make_face()
            with BuildLine():
                CenterArc((0.8, -0.8), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.9, -0.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8, -2.6), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.6, -5.45), 0.29585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


# Description: This is a hexagonal or elongated polyhedron-shaped part with a faceted surface design, featuring multiple triangular faces and sharp edges, with darker shaded regions indicating depth and recessed areas along its bottom and left side.
def model_32871_04ff3d41_0014():
    """Model: CT008 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0478907386, perimeter: 3.8105117767
            with BuildLine():
                Line((0.3175426481, 0.55), (-0.3175426481, 0.55))
                Line((-0.3175426481, 0.55), (-0.6350852961, 0))
                Line((-0.6350852961, 0), (-0.3175426481, -0.55))
                Line((-0.3175426481, -0.55), (0.3175426481, -0.55))
                Line((0.3175426481, -0.55), (0.6350852961, 0))
                Line((0.6350852961, 0), (0.3175426481, 0.55))
            make_face()
        # OneSide extrude, distance=0.225
        extrude(amount=0.225)
    return part.part


# Description: This is a torus (donut-shaped ring) with a smooth, curved geometry featuring a central circular hole and uniform cross-section throughout its circumference.
def model_32879_49552f2f_0017():
    """Model: Pieza 13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3929200659, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical roller or shaft with hemispherical end caps, featuring a blue ribbed or grooved surface pattern along its length and dark circular end faces.
def model_32895_6140d821_0001():
    """Model: Component25"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0001767146, perimeter: 0.0471238898
            with Locations((-2.5, -1)):
                Circle(0.0075)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered, rounded end, featuring a smooth, uniform hollow body with no visible holes, slots, or flanges.
def model_32898_565835ed_0000():
    """Model: Component24"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((1.4711365502, -4.2000000387), (1.6711365502, -4.2000000387))
                CenterArc((1.5711365502, -4.2000000387), 0.1, -179.9999999999, 179.9999999998)
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((1.5711365502, -4.2000000387), 0.1, 0, 180)
                Line((1.4711365502, -4.2000000387), (1.6711365502, -4.2000000387))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a long, thin rectangular bar or shaft with pointed/beveled ends on both sides, featuring a simple elongated hexagonal or prismatic cross-section.
def model_32898_565835ed_0002():
    """Model: Component20"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1052251316, perimeter: 4.6112941403
            with BuildLine():
                Line((10.4940988978, -5.0056978256), (8.2350308276, -5.0056978256))
                Line((10.4940988978, -5.0056978256), (10.4940988978, -4.9591188256))
                Line((10.4940988978, -4.9591188256), (8.2350308276, -4.9591188256))
                Line((8.2350308276, -4.9591188256), (8.2350308276, -5.0056978256))
            make_face()
            # Profile area: 0.1052251316, perimeter: 4.6112941403
            with BuildLine():
                Line((10.4940988978, -5.0522768255), (10.4940988978, -5.0056978256))
                Line((10.4940988978, -5.0056978256), (8.2350308276, -5.0056978256))
                Line((8.2350308276, -5.0056978256), (8.2350308276, -5.0522768255))
                Line((8.2350308276, -5.0522768255), (10.4940988978, -5.0522768255))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a polyhedron or geodesic dome-like structure featuring a cubic base with a pyramidal top composed of multiple triangular facets in varying shades of blue and dark gray, creating a complex geometric form with no apparent holes or slots.
def model_33041_8c6b7740_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8819096024, perimeter: 10
            with BuildLine():
                Line((7.4021130326, 1.6180339887), (5.5, 1))
                Line((5.5, 1), (5.5, -1))
                Line((5.5, -1), (7.4021130326, -1.6180339887))
                Line((7.4021130326, -1.6180339887), (8.5776835372, 0))
                Line((8.5776835372, 0), (7.4021130326, 1.6180339887))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a bicycle handlebar grip featuring a curved, ergonomic tubular shape with textured surface detailing and a hook-shaped upper end for secure handlebar attachment.
def model_33088_7def8eac_0001():
    """Model: Decoration"""
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
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(15.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.8698652712, perimeter: 30.8889878501
            with BuildLine():
                _nurbs_edge([(2.5035152458, 20.0095992759), (2.6192465861, 20.3096967713), (2.7474050943, 20.5214198011), (2.8661967072, 20.6464650591), (2.962754266, 20.7481057774), (3.0477298658, 20.7931004594), (3.1260815011, 20.8101299057), (3.2024266076, 20.8267232402), (3.2810264538, 20.8195347705), (3.3751512906, 20.7774951666), (3.5129335333, 20.7159565641), (3.6754872509, 20.5712664725), (3.8044894218, 20.3374728683), (3.9433353863, 20.0858391303), (4.0408704635, 19.7332727527), (4.0602435964, 19.30440436), (4.08128265, 18.8386570198), (4.0101230877, 18.2847951821), (3.8586080722, 17.6948135053), (3.6849530186, 17.0186211199), (3.4072449717, 16.2975429643), (3.1049654078, 15.5956656608), (2.7619652188, 14.7992372), (2.3911286794, 14.029094433), (2.1407348772, 13.3126075016), (1.9535587576, 12.7770141986), (1.8350209361, 12.2672172919), (1.8310846469, 11.7945287816), (1.827829749, 11.4036650049), (1.9050323722, 11.0386214769), (2.0540825202, 10.730355598), (2.2100658317, 10.4077505338), (2.4390682487, 10.1477656989), (2.709020357, 9.9854944288), (2.9030664212, 9.8688511416), (3.1227824773, 9.8024126191), (3.3464851891, 9.816390296), (3.5354812933, 9.8281993905), (3.7214816044, 9.9005983473), (3.8782360896, 10.0198388961), (4.0842742931, 10.1765687557), (4.2438361293, 10.4053329329), (4.3762645792, 10.6920211894), (4.4230525973, 10.7933104164), (4.4664651161, 10.9022932691), (4.5070304848, 11.019198533)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0626056069, 0.0626056069, 0.0626056069, 0.113493413, 0.113493413, 0.113493413, 0.1630780192, 0.1630780192, 0.1630780192, 0.2356611808, 0.2356611808, 0.2356611808, 0.3137829597, 0.3137829597, 0.3137829597, 0.3986225314, 0.3986225314, 0.3986225314, 0.4958592332, 0.4958592332, 0.4958592332, 0.6061948665, 0.6061948665, 0.6061948665, 0.6886737278, 0.6886737278, 0.6886737278, 0.7568750877, 0.7568750877, 0.7568750877, 0.8282488777, 0.8282488777, 0.8282488777, 0.8795535448, 0.8795535448, 0.8795535448, 0.9228984918, 0.9228984918, 0.9228984918, 0.9798711201, 0.9798711201, 0.9798711201, 1, 1, 1, 1], 3)
                Line((4.5, 11), (4.5070304848, 11.019198533))
                _nurbs_edge([(2.5035152458, 20.0095992759), (2.6372955668, 20.3564987342), (2.7929638835, 20.6349501758), (2.9900091793, 20.8427693187), (3.1424912927, 21.0035886979), (3.324344831, 21.1214962381), (3.5255402652, 21.1727793899), (3.7292677702, 21.2247079468), (3.9456814079, 21.2046505396), (4.1411102725, 21.1258216747), (4.4724263835, 20.9921808587), (4.7510098524, 20.702393237), (4.941098357, 20.3122516506), (5.1343007243, 19.9157191077), (5.2314432964, 19.4126533153), (5.2233335903, 18.8515787921), (5.2138128083, 18.1928781975), (5.0599418144, 17.4537017664), (4.8177658599, 16.7063128673), (4.5489811038, 15.8768054811), (4.1730760719, 15.0399137119), (3.8322614349, 14.2721863441), (3.5516140817, 13.6399932679), (3.2995817893, 13.0525940307), (3.1499868402, 12.533871952), (3.0198343513, 12.0825668115), (2.9686470755, 11.6840766755), (3.0001337489, 11.3492365522), (3.0295565439, 11.036344421), (3.1302520365, 10.7755126217), (3.2700851823, 10.578781107), (3.3803807832, 10.4236060196), (3.5142384591, 10.3114467905), (3.6351906519, 10.2527572377), (3.7315193321, 10.2060157358), (3.8153151745, 10.1924731599), (3.8876389842, 10.2010234712), (3.9624181478, 10.2098640609), (4.0337210051, 10.2398035326), (4.1190180201, 10.3187600995), (4.2276314348, 10.4192998704), (4.3500136949, 10.6061744215), (4.4588229426, 10.8875432803), (4.4727446443, 10.9235432841), (4.4864789792, 10.9610337942), (4.5, 11)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0625, 0.0625, 0.0625, 0.1108651845, 0.1108651845, 0.1108651845, 0.1598390512, 0.1598390512, 0.1598390512, 0.2428658399, 0.2428658399, 0.2428658399, 0.3272527004, 0.3272527004, 0.3272527004, 0.42632274, 0.42632274, 0.42632274, 0.536277985, 0.536277985, 0.536277985, 0.6268217738, 0.6268217738, 0.6268217738, 0.7055978255, 0.7055978255, 0.7055978255, 0.7792102901, 0.7792102901, 0.7792102901, 0.8372732835, 0.8372732835, 0.8372732835, 0.8835157814, 0.8835157814, 0.8835157814, 0.9313281868, 0.9313281868, 0.9313281868, 0.9922103715, 0.9922103715, 0.9922103715, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 13.8698652712, perimeter: 30.8889878501
            with BuildLine():
                _nurbs_edge([(12.4964847542, 20.0095992759), (12.3627044332, 20.3564987342), (12.2070361165, 20.6349501758), (12.0099908207, 20.8427693187), (11.8575087073, 21.0035886979), (11.675655169, 21.1214962381), (11.4744597348, 21.1727793899), (11.2707322298, 21.2247079468), (11.0543185921, 21.2046505396), (10.8588897275, 21.1258216747), (10.5275736165, 20.9921808587), (10.2489901476, 20.702393237), (10.058901643, 20.3122516506), (9.8656992757, 19.9157191077), (9.7685567036, 19.4126533153), (9.7766664097, 18.8515787921), (9.7861871917, 18.1928781975), (9.9400581856, 17.4537017664), (10.1822341401, 16.7063128673), (10.4510188962, 15.8768054811), (10.8269239281, 15.0399137119), (11.1677385651, 14.2721863441), (11.4483859183, 13.6399932679), (11.7004182107, 13.0525940307), (11.8500131598, 12.533871952), (11.9801656487, 12.0825668115), (12.0313529245, 11.6840766755), (11.9998662511, 11.3492365522), (11.9704434561, 11.036344421), (11.8697479635, 10.7755126217), (11.7299148177, 10.578781107), (11.6196192168, 10.4236060196), (11.4857615409, 10.3114467905), (11.3648093481, 10.2527572377), (11.2684806679, 10.2060157358), (11.1846848255, 10.1924731599), (11.1123610158, 10.2010234712), (11.0375818522, 10.2098640609), (10.9662789949, 10.2398035326), (10.8809819799, 10.3187600995), (10.7723685652, 10.4192998704), (10.6499863051, 10.6061744215), (10.5411770574, 10.8875432803), (10.5272553557, 10.9235432841), (10.5135210208, 10.9610337942), (10.5, 11)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0625, 0.0625, 0.0625, 0.1108651845, 0.1108651845, 0.1108651845, 0.1598390512, 0.1598390512, 0.1598390512, 0.2428658399, 0.2428658399, 0.2428658399, 0.3272527004, 0.3272527004, 0.3272527004, 0.42632274, 0.42632274, 0.42632274, 0.536277985, 0.536277985, 0.536277985, 0.6268217738, 0.6268217738, 0.6268217738, 0.7055978255, 0.7055978255, 0.7055978255, 0.7792102901, 0.7792102901, 0.7792102901, 0.8372732835, 0.8372732835, 0.8372732835, 0.8835157814, 0.8835157814, 0.8835157814, 0.9313281868, 0.9313281868, 0.9313281868, 0.9922103715, 0.9922103715, 0.9922103715, 1, 1, 1, 1], 3)
                Line((10.4929695152, 11.019198533), (10.5, 11))
                _nurbs_edge([(12.4964847542, 20.0095992759), (12.3807534139, 20.3096967713), (12.2525949057, 20.5214198011), (12.1338032928, 20.6464650591), (12.037245734, 20.7481057774), (11.9522701342, 20.7931004594), (11.8739184989, 20.8101299057), (11.7975733924, 20.8267232402), (11.7189735462, 20.8195347705), (11.6248487094, 20.7774951666), (11.4870664667, 20.7159565641), (11.3245127491, 20.5712664725), (11.1955105782, 20.3374728683), (11.0566646137, 20.0858391303), (10.9591295365, 19.7332727527), (10.9397564036, 19.30440436), (10.91871735, 18.8386570198), (10.9898769123, 18.2847951821), (11.1413919278, 17.6948135053), (11.3150469814, 17.0186211199), (11.5927550283, 16.2975429643), (11.8950345922, 15.5956656608), (12.2380347812, 14.7992372), (12.6088713206, 14.029094433), (12.8592651228, 13.3126075016), (13.0464412424, 12.7770141986), (13.1649790639, 12.2672172919), (13.1689153531, 11.7945287816), (13.172170251, 11.4036650049), (13.0949676278, 11.0386214769), (12.9459174798, 10.730355598), (12.7899341683, 10.4077505338), (12.5609317513, 10.1477656989), (12.290979643, 9.9854944288), (12.0969335788, 9.8688511416), (11.8772175227, 9.8024126191), (11.6535148109, 9.816390296), (11.4645187067, 9.8281993905), (11.2785183956, 9.9005983473), (11.1217639104, 10.0198388961), (10.9157257069, 10.1765687557), (10.7561638707, 10.4053329329), (10.6237354208, 10.6920211894), (10.5769474027, 10.7933104164), (10.5335348839, 10.9022932691), (10.4929695152, 11.019198533)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0626056069, 0.0626056069, 0.0626056069, 0.113493413, 0.113493413, 0.113493413, 0.1630780192, 0.1630780192, 0.1630780192, 0.2356611808, 0.2356611808, 0.2356611808, 0.3137829597, 0.3137829597, 0.3137829597, 0.3986225314, 0.3986225314, 0.3986225314, 0.4958592332, 0.4958592332, 0.4958592332, 0.6061948665, 0.6061948665, 0.6061948665, 0.6886737278, 0.6886737278, 0.6886737278, 0.7568750877, 0.7568750877, 0.7568750877, 0.8282488777, 0.8282488777, 0.8282488777, 0.8795535448, 0.8795535448, 0.8795535448, 0.9228984918, 0.9228984918, 0.9228984918, 0.9798711201, 0.9798711201, 0.9798711201, 1, 1, 1, 1], 3)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a curved pipe or hose clamp with an open C-shaped design, featuring a textured outer surface and an inner grip surface, designed to secure cylindrical components.
def model_33147_d7173b68_0000():
    """Model: Pierscien fi v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5830272366, perimeter: 8.0736964884
            with BuildLine():
                CenterArc((0, 0), 0.73, 90, 340)
                Line((0.2496747046, 0.6859756132), (0.1983716831, 0.5450217201))
                CenterArc((0, 0), 0.58, 90, 340)
                Line((0, 0.58), (0, 0.73))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a curved clip or retaining ring with an open C-shaped design, featuring a textured or mesh-patterned surface and a slot or gap on one side for insertion or elastic retention purposes.
def model_33147_d7173b68_0004():
    """Model: Pierscien fi6,25 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.423340082, perimeter: 5.2139779546
            with BuildLine():
                CenterArc((0, 0), 0.497, 90, 340)
                Line((0.1104725063, 0.3035207165), (0.1699840112, 0.4670272325))
                CenterArc((0, 0), 0.323, 90, 340)
                Line((0, 0.323), (0, 0.497))
            make_face()
        # OneSide extrude, distance=0.058
        extrude(amount=0.058)
    return part.part


# Description: This is a retaining ring or snap ring with a C-shaped circular form featuring a textured surface and an open gap, designed to secure components on a shaft or in a groove.
def model_33147_d7173b68_0005():
    """Model: Pierscien fi10 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5893322386, perimeter: 7.0852255834
            with BuildLine():
                CenterArc((0, 0), 0.655, 90, 340)
                Line((0.1641696688, 0.451052458), (0.2240231939, 0.6154986666))
                CenterArc((0, 0), 0.48, 90, 340)
                Line((0, 0.48), (0, 0.655))
            make_face()
        # OneSide extrude, distance=0.045
        extrude(amount=0.045)
    return part.part


# Description: This is a toroidal (donut-shaped) ring with a smooth, curved profile and a central void, featuring a textured or mesh-like surface finish across its entire geometry.
def model_33147_d7173b68_0007():
    """Model: Podkladka v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a rubber belt or O-ring with an elliptical/oval closed-loop shape, featuring a uniform circular cross-section and textured surface for grip and friction.
def model_33147_d7173b68_0014():
    """Model: Obudowa v4"""
    with BuildPart() as part:
        # Sketch10 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3929200659, perimeter: 33.9292006588
            with BuildLine():
                CenterArc((0, 0), 2.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a flat, elongated rectangular plate or bar with a slight parallelogram shape, featuring beveled or angled edges on the ends and a uniform dark gray finish.
def model_33197_0f08d771_0001():
    """Model: Component19"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0469715087, perimeter: 1.1394602773
            with BuildLine():
                Line((-0.3681576256, 4.3299835289), (-0.4681576256, 4.3299835289))
                Line((-0.4681576256, 4.3299835289), (-0.4681576256, 3.8614953654))
                Line((-0.4681576256, 3.8614953654), (-0.3681576256, 3.8590415175))
                Line((-0.3681576256, 3.8590415175), (-0.3681576256, 4.3299835289))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)
    return part.part


# Description: This is a curved sheet metal or composite panel with an elongated hexagonal shape, featuring internal diagonal reinforcement ribs and a gently curved longitudinal surface.
def model_33266_2a15d3f5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1993.75, perimeter: 167.7817459305
            with BuildLine():
                Line((0, -22.5), (0, -10))
                Line((0, -22.5), (17.5, -40))
                Line((42.5, -40), (17.5, -40))
                Line((60, -22.5), (42.5, -40))
                Line((60, -10), (60, -22.5))
                Line((50, 0), (60, -10))
                Line((10, 0), (50, 0))
                Line((0, -10), (10, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a tapered metal wedge or shim with a long, narrow rectangular profile that gradually decreases in thickness from one end to the other, featuring a flat top surface and angled side surfaces.
def model_33271_94293b74_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.450696143, perimeter: 6.0618935081
            with BuildLine():
                Line((0.8825836557, 0.14945292), (0.0115443227, 0.0513008594))
                CenterArc((0.013, 0.0383826164), 0.013, 96.4291883736, 83.5708116264)
                Line((0, 0.0383826164), (0, 0))
                Line((0, 0), (2.485, 0))
                CenterArc((2.485, 0.015), 0.015, -90, 90)
                Line((2.5, 0.015), (2.5, 0.085))
                CenterArc((2.515, 0.085), 0.015, 90, 90)
                Line((2.515, 0.1), (2.885, 0.1))
                CenterArc((2.885, 0.115), 0.015, -90, 90)
                Line((2.9, 0.115), (2.9, 0.185))
                CenterArc((2.885, 0.185), 0.015, 0, 90)
                Line((2.885, 0.2), (0.9094536097, 0.2))
                CenterArc((0.9094536097, 0.189), 0.011, 90, 81.3527834563)
                Line((0.8985786487, 0.1906538512), (0.893980205, 0.1604166116))
                CenterArc((0.8811279784, 0.1623711631), 0.013, -83.5708116264, 74.9235950828)
            make_face()
        # OneSide extrude, distance=31
        extrude(amount=31)
    return part.part


# Description: This is a curved aerodynamic duct or air intake component with a tapered, swept design featuring two opposing blue surfaces connected by a central dark ribbed or finned section, likely designed for directional airflow.
def model_33274_28b853dd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16127.4645792283, perimeter: 534.1848827355
            with BuildLine():
                CenterArc((-5, 5), 5, -90, 90)
                Line((0, 78), (0, 5))
                CenterArc((-12, 78), 12, 0, 90)
                Line((-59.8960135188, 90), (-12, 90))
                CenterArc((-90, 50), 50.0624610068, 53.0348934632, 73.9302130423)
                Line((-168, 90), (-120.1039864593, 90.0000000164))
                CenterArc((-168, 78), 12, 90, 90)
                Line((-180, 5), (-180, 78))
                CenterArc((-175, 5), 5, 180, 90)
                Line((-120.1039864593, 0.0000000164), (-175, 0))
                CenterArc((-90, -40), 50.0624610068, 53.0348934632, 73.9302130423)
                Line((-5, 0), (-59.8960135188, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a hinged box or enclosure with a rectangular lid attached via a central hinge mechanism, featuring a trapezoidal/parallelogram body shape with an open-top design and internal reinforcement ribs or bracing elements.
def model_33529_756075a0_0001():
    """Model: Seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 110, perimeter: 100
            with BuildLine():
                Line((100, 10), (95, 10))
                Line((100, 40), (100, 10))
                Line((97.5, 40), (100, 40))
                Line((97.5, 12), (97.5, 40))
                Line((80, 12), (97.5, 12))
                Line((80, 10), (80, 12))
                Line((85, 10), (80, 10))
                Line((95, 10), (85, 10))
            make_face()
            # Profile area: 225, perimeter: 61.6227766017
            with BuildLine():
                Line((95, 10), (85, 10))
                Line((80, -5), (85, 10))
                Line((100, -5), (80, -5))
                Line((95, 10), (100, -5))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a rounded, pill-shaped profile featuring a central axial slot or keyway running along its length.
def model_33539_0e7a4748_0002():
    """Model: podwozie"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 306.7025099893, perimeter: 62.0816994684
            with Locations((-177.0681874629, -62.1468752105)):
                Circle(9.8806093459)
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)
    return part.part


# Description: This is a curved duct or pipe component with a horizontal flange at the top and a smooth, serpentine bend that curves downward, featuring a hollow interior channel with textured mesh-like surfaces along its length.
def model_33539_0e7a4748_0003():
    """Model: zawias b"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.5982323724, perimeter: 17.8433189772
            with BuildLine():
                Line((-423.3496545177, -29.8204749909), (-423.9616698174, -32.7573844674))
                CenterArc((-418.7826185668, -7.9044033347), 22.3868714701, -114.7811285195, 13.0098637719)
                Line((-428.1661443708, -28.2297928194), (-430.2187696698, -30.5695239165))
                CenterArc((-418.7826185668, -7.9044033347), 25.3868714701, -116.7741639896, 15.002899242)
            make_face()
            # Profile area: 117.165993857, perimeter: 94.6664993678
            with BuildLine():
                Line((-396.6176159794, -11.048393557), (-401.2846543469, -7.7841802889))
                CenterArc((-418.7826185668, -7.9044033347), 22.3868714701, -101.7712647476, 93.6980136922)
                Line((-423.3496545177, -29.8204749909), (-423.9616698174, -32.7573844674))
                CenterArc((-418.7826185668, -7.9044033347), 25.3868714701, -101.7712647476, 91.5398421586)
                Line((-401.2846543469, -7.7841802889), (-393.7994404497, -12.4137330193))
            make_face()
            # Profile area: 30.6378689489, perimeter: 34.9738108599
            with BuildLine():
                Line((-401.2846543469, -7.7841802889), (-399.2061814953, -6.7180774719))
                Line((-401.2846543469, -7.7841802889), (-393.7994404497, -12.4137330193))
                Line((-393.7994404497, -12.4137330193), (-387.743042911, -16.1595727703))
                Line((-386.6910157297, -14.4586204459), (-387.743042911, -16.1595727703))
                Line((-399.2061814953, -6.7180774719), (-386.6910157297, -14.4586204459))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered top end and textured surface, appearing to be a hollow tubular component, possibly a shrink-fit tubing, protective sleeve, or connector part.
def model_33607_c6f31fa6_0006():
    """Model: slider - part 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1288631902, perimeter: 3.7663926005
            Circle(0.59944)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered top end and vertical ribbed or fluted surface texture running along its length.
def model_33607_c6f31fa6_0009():
    """Model: simple pump tube"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.4508417564, perimeter: 65.832074056
            with BuildLine():
                CenterArc((0, 0), 5.3975, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=18.288
        extrude(amount=18.288)
    return part.part


# Description: This is an elliptical or oval-shaped disc with a central elongated slot or opening running through its middle, featuring a curved, slightly domed profile with a flat base and radiating surface texture pattern.
def model_33607_c6f31fa6_0010():
    """Model: flywheel 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1290.8775153064, perimeter: 146.5751162893
            with BuildLine():
                CenterArc((0, 0), 20.32, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
                Line((1.27, 0), (8.26516, 0))
                CenterArc((8.89, 0), 0.62484, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a cylindrical tube or pipe with a long, slender shape and rounded ends, appearing to be a simple hollow or solid cylinder without any holes, slots, or flanges.
def model_33607_c6f31fa6_0024():
    """Model: bottom cylindrical rod (6.2'' length)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.547122223, perimeter: 5.6575685461
            Circle(0.90043)
        # OneSide extrude, distance=15.748
        extrude(amount=15.748)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve with a slightly tapered, open top end and vertical ribbed or corrugated surface texture, designed as a tubular container or filter component.
def model_33607_c6f31fa6_0025():
    """Model: 1-inch bushing for axle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2239391258, perimeter: 18.4329807357
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3462, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.1275
        extrude(amount=4.1275)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a truncated, slightly tapered open-ended design featuring vertical ribbing or fluting patterns on its outer surface.
def model_33607_c6f31fa6_0034():
    """Model: small bushing for link (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.097693202, perimeter: 7.6923781079
            with BuildLine():
                CenterArc((0, 0), 0.62484, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.59944, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a turning insert tool with a dark circular head on the left and a blue rectangular cutting blade extending to the right, featuring a flat top surface and angled cutting edges.
def model_33607_c6f31fa6_0037():
    """Model: bushing and link (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.5967272413, perimeter: 27.8327801109
            with BuildLine():
                Line((0, 0), (0, 1.905))
                Line((0, 1.905), (-10.16, 1.905))
                CenterArc((-10.16, 0), 1.905, 90, 90)
                Line((-12.065, 0), (-10.7823, 0))
                CenterArc((-10.16, 0), 0.6223, 0, 180)
                Line((-9.5377, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: A pry bar or tire lever with a long, slender shaft featuring a curved claw end on one side and a flat hook or lever end on the opposite side for leverage applications.
def model_33615_7bab1106_0010():
    """Model: Drive_Rod_Long"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6260115819, perimeter: 12.8622546116
            with BuildLine():
                CenterArc((0.0304884309, -0.2128272905), 0.215, 98.1524031279, 234.0984904378)
                CenterArc((0.192, -0.2977994216), 0.0325, -27.7491064343, 180)
                CenterArc((0.0304884309, -0.2128272905), 0.15, 58.8859160295, 273.3649775362)
                Line((0.108, -0.0844062772), (0.108, 4.4951000906))
                CenterArc((0.0360360551, 4.6817044599), 0.2, 31.2156300471, 259.8734950516)
                CenterArc((0.243, 4.8071234597), 0.042, -148.7843699516, 180.0000008538)
                CenterArc((0.0360360551, 4.6817044599), 0.284, 31.2156301737, 231.4945991678)
                Line((0, 0), (0, 4.4))
            make_face()
        # OneSide extrude, distance=0.098
        extrude(amount=0.098)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered, rounded top edge and vertical ribbed or fluted detailing along its exterior surface.
def model_33615_7bab1106_0011():
    """Model: Piston_Seal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5654866776, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.1
        extrude(amount=3.1)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a tapered, rounded end cap, featuring a smooth tubular body designed to attach to a firearm barrel.
def model_33615_7bab1106_0013():
    """Model: Axle_Mid"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.67
        extrude(amount=1.67)
    return part.part


# Description: This is an oval-shaped disc or pad with a shallow central depression, featuring a fine mesh or textured surface pattern and a solid outer rim, likely designed as a cushioning element, filter base, or structural component.
def model_33615_7bab1106_0014():
    """Model: Heat_Exchange_Cylinder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 57.908129939, perimeter: 27.6114578324
            with BuildLine():
                CenterArc((0, 0), 4.2945, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.83
        extrude(amount=0.83)
    return part.part


# Description: This is a sheet metal bracket or channel shaped like the number "7" featuring a horizontal top flange with a mesh/grid pattern, a vertical stem with vertical ribbing or corrugations for reinforcement, and small mounting pads or feet at both ends.
def model_33625_c9ff9be8_0008():
    """Model: Wheel2 v6 (1)"""
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
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.6974698709, perimeter: 41.5912125664
            with BuildLine():
                CenterArc((0, 0), 1.5, 89.5557142506, 30)
                Line((0.0116312572, 1.4999549039), (0.1163125716, 14.9995490394))
                CenterArc((0, 0), 15, 89.5557142506, 30)
                Line((-6.6591403901, 11.7433321193), (-7.3990448779, 13.0481467992))
                CenterArc((0, 0), 13.5, 99.4170266076, 20.1386876429)
                _nurbs_edge([(-0.4813936157, 2.9611248178), (-0.4752957101, 3.1877462658), (-0.4649521606, 3.6343910831), (-0.4549936037, 4.2845641107), (-0.4529099948, 5.1115849907), (-0.4695032854, 6.0772012938), (-0.5060639683, 6.9726028569), (-0.5634466864, 7.7961252572), (-0.6423826711, 8.5475083791), (-0.7432560184, 9.2289199273), (-0.8657259946, 9.8466838918), (-1.0085681491, 10.4118033052), (-1.1701464276, 10.9371820665), (-1.3486906897, 11.435683423), (-1.5425754262, 11.9180796824), (-1.7505471933, 12.3909560462), (-1.9275088614, 12.7643005195), (-2.0659682253, 13.0420550742), (-2.1608063149, 13.22622975), (-2.208858323, 13.3180683625)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 3, 99.2338607196, 20.321853531)
                Line((-0.7399044878, 1.3048146799), (-1.4798089756, 2.6096293598))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a slightly tapered profile along its length.
def model_33625_c9ff9be8_0010():
    """Model: Axis saver v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.9452431127, perimeter: 23.5619449019
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=63
        extrude(amount=63)
    return part.part


# Description: This is a long, slender rectangular prism or beam with a uniform cross-section, tilted at an angle, featuring clean edges and a simple extruded profile with no visible holes, slots, or special features.
def model_33628_296ae2b8_0000():
    """Model: Component12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((2, 2.5), (3, 2.5))
                Line((2, 2), (2, 2.5))
                Line((3, 2), (2, 2))
                Line((3, 2.5), (3, 2))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a reinforced oval ring or band with a solid dark base material and a mesh or lattice reinforcement pattern on the outer surface, featuring a hollow elliptical center opening.
def model_33655_f8991a06_0007():
    """Model: pieza 13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)
    return part.part


# Description: This is a reinforced elastic band or belt with an oval/elliptical toroidal shape, featuring a solid inner core wrapped with a blue mesh or fabric reinforcement layer on the outer surface.
def model_33655_f8991a06_0010():
    """Model: pieza 12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)
    return part.part


# Description: This is a cylindrical container or sleeve with an open top and bottom, featuring a curved, slightly tapered body with a mesh or perforated surface pattern throughout.
def model_33655_f8991a06_0011():
    """Model: pieza 9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a cylindrical sleeve or tube with a dark gray finish, featuring a slightly tapered or beveled top end and what appears to be ribbed or textured surface detailing along its length.
def model_33655_f8991a06_0012():
    """Model: pieza 8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a dark gray cylindrical rod or shaft with a tapered or slightly beveled end, featuring a longitudinal slot or groove running along its length, commonly used as a mechanical fastener, alignment pin, or support component.
def model_33740_f9566689_0003():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.3000000492), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0087709378, perimeter: 0.8800003198
            with BuildLine():
                Line((3.615279494, 4.2199999057), (3.615279494, 4.4246365878))
                Line((3.715279494, 4.2199999057), (3.615279494, 4.2199999057))
                Line((3.715279494, 4.2700000656), (3.715279494, 4.2199999057))
                Line((3.695279494, 4.2700000656), (3.715279494, 4.2700000656))
                Line((3.695279494, 4.2400000656), (3.695279494, 4.2700000656))
                Line((3.635279494, 4.2400000656), (3.695279494, 4.2400000656))
                Line((3.635279494, 4.4000000656), (3.635279494, 4.2400000656))
                Line((3.695279494, 4.4000000656), (3.635279494, 4.4000000656))
                Line((3.695279494, 4.3746365878), (3.695279494, 4.4000000656))
                Line((3.715279494, 4.3746365878), (3.695279494, 4.3746365878))
                Line((3.715279494, 4.4246365878), (3.715279494, 4.3746365878))
                Line((3.615279494, 4.4246365878), (3.715279494, 4.4246365878))
            make_face()
        # OneSide extrude, distance=-3.3
        extrude(amount=-3.3)
    return part.part


# Description: This is a long, slender rectangular beam or rail with a shallow channel or groove running along its top surface and beveled or tapered ends.
def model_33762_23d5c1d9_0004():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0798281977, perimeter: 1.2006493731
            with BuildLine():
                CenterArc((-6, -22.5), 24.2538656713, 75.7232827696, 0.9449451772)
                Line((-0.0188700682, 1.0048098214), (0.0288906013, 1.1988580429))
                Line((-0.36030013, 1.2946470467), (0.0288906013, 1.1988580429))
                Line((-0.4073167419, 1.1002519896), (-0.36030013, 1.2946470467))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8)
    return part.part


# Description: This is a flat parallelogram or trapezoid-shaped plate with a diagonal internal edge dividing it into two triangular sections, featuring a simple planar geometry with no holes, slots, or curves.
def model_33765_4d6288b9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 264, perimeter: 68
            with BuildLine():
                Line((11, -6), (11, 6))
                Line((11, 6), (-11, 6))
                Line((-11, 6), (-11, -6))
                Line((-11, -6), (11, -6))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved composite bracket or duct component with an angled tubular body, featuring a blue reinforcement pattern on its upper surface and a solid flange or mounting base at the lower end.
def model_33991_aaf84876_0019():
    """Model: pokretlo"""
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
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.587712578, perimeter: 12.0256863085
            with BuildLine():
                _nurbs_edge([(1.0307447711, 82.2608028968), (1.0435854001, 82.2045045583), (1.0648152353, 82.0962229787), (1.083305853, 81.9467457974), (1.0812021961, 81.7733810694), (1.0353645345, 81.5989230096), (0.950961829, 81.4632997825), (0.8377189139, 81.3592729688), (0.7121686681, 81.2744612174), (0.5997638446, 81.1897228603), (0.5275029611, 81.0849758589), (0.5166437872, 80.9449653234), (0.5745906698, 80.7656400639), (0.6892400254, 80.5587168063), (0.8377865429, 80.3456747358), (0.993451746, 80.1532011462), (1.1334246553, 80.007947314), (1.2452413019, 79.9319970958), (1.3365086444, 79.9369832583), (1.4328247249, 80.0227497609), (1.5640397971, 80.1802701144), (1.7543217496, 80.3933844255), (2.0093792482, 80.6408052077), (2.3085025533, 80.8983354835), (2.6161827994, 81.1423761772), (2.8917406875, 81.3539239164), (3.0982962574, 81.5209902465), (3.2151420503, 81.6449751077), (3.2415528192, 81.7379546503), (3.2212677001, 81.8414465571), (3.2173223061, 81.9933363783), (3.2245972423, 82.1220244865), (3.2296445008, 82.2016246607), (3.2307447935, 82.2430128659), (3.2307447935, 82.2608036344)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(1.0307447711, 82.2608028968), (1.0435853623, 82.3171012439), (1.0648151249, 82.4253828377), (1.0833056424, 82.5748600313), (1.0812018693, 82.7482247579), (1.0353640907, 82.922682787), (0.9509612942, 83.0583059575), (0.8377183094, 83.1623326954), (0.7121680067, 83.2471443627), (0.5997631264, 83.3318826444), (0.5275021726, 83.4366295973), (0.5166429048, 83.5766401255), (0.5745896672, 83.7559654238), (0.6892388841, 83.9628887583), (0.8377852587, 84.1759309284), (0.9934503328, 84.3684046224), (1.1334231447, 84.5136585485), (1.2452397403, 84.5896088416), (1.3365070862, 84.5846227403), (1.4328232242, 84.4988563023), (1.564038402, 84.3413360369), (1.7543204974, 84.1282218533), (2.0093781619, 83.8808012422), (2.3085016397, 83.623271167), (2.6161820495, 83.3792306796), (2.8917400794, 83.1676831251), (3.0982957613, 83.0006169335), (3.2151416373, 82.8766321507), (3.2415524686, 82.7836526258), (3.2212674189, 82.6801607053), (3.2173221268, 82.5282708815), (3.2245971492, 82.3995827783), (3.2296444611, 82.3199826074), (3.2307447815, 82.2785944029), (3.2307447935, 82.2608036344)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a cylindrical tube or shaft with rounded hemispherical end caps, featuring internal longitudinal slots or grooves running along its length and circular openings at each end.
def model_33997_f6998a7d_0005():
    """Model: center piece"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23.7582944428, perimeter: 17.2787595947
            with Locations((-7, 2)):
                Circle(2.75)
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a hexagonal or wedge-shaped solid component with a trapezoidal profile, featuring a triangulated upper surface and a darker recessed or chamfered section on the left side, suggesting it may be a structural bracket, connector, or geometric base element.
def model_33997_f6998a7d_0006():
    """Model: Armrest"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 15.24), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.3197576339, perimeter: 9.4942300139
            with BuildLine():
                Line((-22.677041528, 51.6965159755), (-19.1571779622, 51.6965159755))
                Line((-22.677041528, 50.4692645343), (-22.677041528, 51.6965159755))
                Line((-19.1571779622, 50.4692645343), (-22.677041528, 50.4692645343))
                Line((-19.1571779622, 51.6965159755), (-19.1571779622, 50.4692645343))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a tapered wedge or shim with an elongated triangular profile, featuring a flat top surface, angled sides that converge toward a sharp point, and a small notch or slot on the left end.
def model_33997_f6998a7d_0007():
    """Model: chair legs"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 195.5762547871, perimeter: 94.660607036
            with BuildLine():
                CenterArc((39.401742725, 3.3632792433), 3.3702477991, 15.9905011491, 62.2611904951)
                Line((0, 15), (40.0879684676, 6.6629253542))
                Line((0.1420816133, 7.5749319034), (0, 15))
                Line((42.6415868053, 4.2917083263), (0.1420816133, 7.5749319034))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


# Description: This is a hexagonal or octagonal container/housing with a flat bottom, angled side walls, and an open top featuring internal ribbed reinforcement structures and mounting surfaces.
def model_34063_0ca1585e_0006():
    """Model: Feathering Hub"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4226548246, perimeter: 5.7132741229
            with BuildLine():
                CenterArc((-0.4, -0.4), 0.4, 180, 90)
                Line((-0.4, -0.8), (0.4, -0.8))
                CenterArc((0.4, -0.4), 0.4, -90, 90)
                Line((0.8, -0.4), (0.8, 0.4))
                CenterArc((0.4, 0.4), 0.4, 0, 90)
                Line((0.4, 0.8), (-0.4, 0.8))
                CenterArc((-0.4, 0.4), 0.4, 90, 90)
                Line((-0.8, 0.4), (-0.8, -0.4))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a long tubular body, rounded end caps, and a slightly textured surface featuring perforations or venting patterns along its length.
def model_34063_0ca1585e_0008():
    """Model: Alignment Arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1134114948, perimeter: 1.1938052084
            with Locations((-0.9054679244, -1.5041706831)):
                Circle(0.19)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2)
    return part.part


# Description: This is a curved cylindrical filter or strainer component with an elongated oval shape, featuring a mesh or perforated surface on the top and solid walls on the sides and bottom.
def model_34225_638d4d19_0000():
    """Model: Luz caliente/frio"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2831853072, perimeter: 9.6884482251
            with Locations((17.5, 0)):
                Ellipse(2, 1, rotation=90)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a thin, flat parallelogram-shaped plate or panel with a slightly warped or twisted surface, featuring four vertices and no holes or additional features.
def model_34225_69ae4861_0005():
    """Model: Base antideslizante"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 287.5, perimeter: 71
            with BuildLine():
                Line((6.25, -11.5), (6.25, 11.5))
                Line((-6.25, 11.5), (6.25, 11.5))
                Line((-6.25, -11.5), (-6.25, 11.5))
                Line((6.25, -11.5), (-6.25, -11.5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a gradually narrowing diameter from one end to the other, featuring a smooth conical shape without any holes, slots, or additional features.
def model_34225_69ae4861_0006():
    """Model: Eje"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-8, 2.5)):
                Circle(0.25)
        # Symmetric extrude, each_side=9.5
        extrude(amount=9.5, both=True)
    return part.part


# Description: This is a curved cylindrical sleeve or band with an asymmetrical design, featuring a flange on one end, smooth curved surfaces, and a hollow tubular structure with varying wall thicknesses.
def model_34225_69ae4861_0011():
    """Model: cubre luz"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.1415926536, perimeter: 10.2831853072
            with BuildLine():
                Line((17, -1), (17, 1))
                CenterArc((16, 1), 1, 0, 180)
                Line((15, 1), (15, -1))
                CenterArc((16, -1), 1, 180, 180)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a curved structural beam or channel with hexagonal end flanges on both sides and a central longitudinal slot or depression running along its length.
def model_34227_48203345_0009():
    """Model: part2"""
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
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 190, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 832.8895165411, perimeter: 278.6349412959
            with BuildLine():
                Line((-155, 185), (-220, 185))
                _nurbs_edge([(-220, 185), (-220.9394317378, 183.8205455142), (-222.7198290568, 181.5331750436), (-225.0950407257, 178.3167245529), (-227.6613792742, 174.4644846252), (-229.79934542, 170.4265393457), (-230.7679308716, 167.2381828471), (-230.4656041745, 164.9731806576), (-228.8262342927, 163.6795788808), (-225.8881610261, 163.3295225469), (-221.7434501969, 163.8561231826), (-217.5385257352, 164.9234010076), (-213.9160276235, 166.0644595514), (-211.2960523023, 166.9740866408), (-209.9348199834, 167.4661309068)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-205, 175), (-209.9348199834, 167.4661309068))
                Line((-215, 170), (-205, 175))
                Line((-215, 180), (-215, 170))
                Line((-155, 180), (-215, 180))
                Line((-155, 170), (-155, 180))
                Line((-170, 170), (-155, 170))
                Line((-170, 165), (-170, 170))
                _nurbs_edge([(-155, 185), (-153.9755291446, 183.8127877883), (-152.0437627867, 181.5080076823), (-149.4976365923, 178.2597688614), (-146.817438151, 174.3535349534), (-144.737757948, 170.2259170006), (-144.0369500717, 166.9178453063), (-144.8194226543, 164.4913758654), (-147.127047239, 162.9713954393), (-150.8828626267, 162.3121613862), (-155.9704910907, 162.4445034656), (-161.0151275772, 163.1296007778), (-165.3114080627, 163.948213314), (-168.3997714403, 164.6271964339), (-170, 165)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a curved plastic or composite bracket with a U-shaped or horseshoe-like profile, featuring two rounded end flanges connected by a central channel, and includes a central rectangular slot or cutout along its length.
def model_34227_48203345_0010():
    """Model: part3"""
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
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 60, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1281.5762382034, perimeter: 450.2374199054
            with BuildLine():
                Line((-150, 190), (-195, 190))
                Line((-195, 190), (-211.8448174786, 182.8323391959))
                Line((-211.8448174786, 182.8323391959), (-220, 170))
                _nurbs_edge([(-220, 170), (-220.7156911088, 170.5592309444), (-222.1393032329, 171.5192478336), (-224.2513346629, 172.4840113927), (-227.0210785752, 172.8153227104), (-230.3358592797, 171.6872626517), (-233.3061034307, 169.1946500606), (-235.5135109161, 165.7485937337), (-236.3399777208, 161.9916753436), (-235.1943493366, 158.6067016764), (-231.6783295996, 156.1812487154), (-225.8166865157, 155.0225172308), (-218.0069345622, 155.1816481727), (-208.9081974867, 156.5227895299), (-199.3573888199, 158.7725048681), (-190.2788519339, 161.5735479869), (-182.6000943936, 164.5336818839), (-177.1639683117, 167.2756062703), (-174.6429686454, 169.4847474255), (-175.4401719233, 170.9625781059), (-179.7538203177, 171.6016126324), (-186.0688007297, 171.4059357695), (-192.4120041967, 170.8582525925), (-197.3521165728, 170.3156621186), (-200, 170)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-186.166620297, 166.1230077022), (-200, 170))
                Line((-223.1481887831, 159.3990861593), (-186.166620297, 166.1230077022))
                Line((-228.5541489722, 166.1230077022), (-223.1481887831, 159.3990861593))
                Line((-217.742228594, 168.0888114074), (-228.5541489722, 166.1230077022))
                Line((-196.708128949, 185), (-217.742228594, 168.0888114074))
                Line((-155, 185), (-196.708128949, 185))
                Line((-140, 170), (-155, 185))
                Line((-151.887804472, 167.6956506663), (-140, 170))
                Line((-157.1954744758, 175.3622851163), (-151.887804472, 167.6956506663))
                _nurbs_edge([(-135.091957588, 180.5256707252), (-134.3454816415, 179.8132731273), (-132.9855551482, 178.4075129758), (-131.3447527302, 176.3559754271), (-129.9608975632, 173.735648331), (-129.5860485544, 170.6640231415), (-130.5480102428, 167.8240069889), (-132.7633345645, 165.2639762007), (-136.0319803071, 163.0597491519), (-140.0288003547, 161.3138344088), (-144.3659113955, 160.1423020277), (-148.6330908757, 159.6640492159), (-152.4464182521, 159.9865428421), (-155.4890061918, 161.1925125596), (-157.5697529873, 163.3177634332), (-158.6021916396, 166.362465119), (-158.570261729, 169.5210220223), (-158.0676763881, 172.2879746151), (-157.5214094382, 174.3082429528), (-157.1954744758, 175.3622851163)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-150, 190), (-135.091957588, 180.5256707252))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a cylindrical bowl or container with an elliptical/oval cross-section, featuring a curved, tapered sidewall and an open top with a distinctive ribbed or fluted rim pattern on the upper surface.
def model_34227_48203345_0012():
    """Model: 1 axis"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7853.9816339745, perimeter: 314.159265359
            Circle(50)
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a curved headlight or trim bezel component with a blue upper surface and black lower flanges, featuring two rectangular cutouts and a contoured aerodynamic shape.
def model_34234_04351713_0000():
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
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 114.4297586942, perimeter: 164.0471224895
            with BuildLine():
                Line((-17.5489160715, -1.6500001407), (-17.5489161028, 0))
                _nurbs_edge([(-5.0350872121, -7.5771667299), (-5.0880169897, -7.5326639581), (-5.1977339298, -7.4503118052), (-5.3738810592, -7.3467433766), (-5.6319330321, -7.2486472653), (-5.9927312507, -7.1920481106), (-6.3901594773, -7.1988789266), (-6.820529108, -7.2632588391), (-7.2789206082, -7.3759881002), (-7.7604432777, -7.5246706851), (-8.2612030966, -7.6938927962), (-8.7797455403, -7.8649962994), (-9.3163191675, -8.0179456751), (-9.8713312321, -8.1339569063), (-10.4439792959, -8.1980482468), (-11.030988557, -8.2012913469), (-11.6248028622, -8.144164111), (-12.2147735818, -8.0341549419), (-12.789436177, -7.8813106003), (-13.3385405066, -7.6942566086), (-13.8549270049, -7.4765535498), (-14.3371405787, -7.2216011498), (-14.7892792861, -6.9130576584), (-15.217862253, -6.5311915295), (-15.6294447671, -6.0577910925), (-16.0280973986, -5.4813348011), (-16.4125583166, -4.8029259364), (-16.7746807726, -4.0394249585), (-17.0931858132, -3.2397917274), (-17.3091285371, -2.585209378), (-17.442851981, -2.1024696239), (-17.5172579645, -1.7925311075), (-17.5489160715, -1.6500001407)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9288309288, 0.9288309288, 0.9288309288, 0.9288309288, 0.9288309288, 0.9288309288], 5)
                _nurbs_edge([(3.4643315895, -8.8797613281), (3.4802240997, -8.835876693), (3.5103361263, -8.7469668197), (3.5504854163, -8.610180108), (3.5939680835, -8.4209478561), (3.6308656919, -8.1733127076), (3.6482525856, -7.9156344272), (3.6421577007, -7.650046132), (3.6058517645, -7.3802262453), (3.5313430156, -7.1109369303), (3.4113265906, -6.8473967921), (3.2408764694, -6.5947329718), (3.019492903, -6.3573561515), (2.7522961939, -6.138498799), (2.4478392917, -5.9403647569), (2.1164676714, -5.7641865875), (1.7684158125, -5.6103082173), (1.4121618396, -5.4782630794), (1.0523236961, -5.3668205796), (0.6888907135, -5.2741365318), (0.3191012285, -5.1981214698), (-0.06124636, -5.1367618283), (-0.4562757105, -5.0884550661), (-0.8685757544, -5.0523475438), (-1.2977784911, -5.0286532394), (-1.738930866, -5.0190374013), (-2.1836221998, -5.0261764409), (-2.6213740419, -5.0532393897), (-3.0409250199, -5.1033990777), (-3.4315558379, -5.1793299744), (-3.7843972805, -5.2827089866), (-4.0937569541, -5.4137088792), (-4.3584441614, -5.5704889128), (-4.5803855375, -5.7496417509), (-4.7632315194, -5.946634146), (-4.9110283013, -6.1562400972), (-5.0267507905, -6.3729793652), (-5.1112515959, -6.5915316215), (-5.1641578925, -6.8070990754), (-5.1844537674, -7.0157383012), (-5.1712747331, -7.2147919885), (-5.1337080877, -7.3653641089), (-5.0903107141, -7.473231234), (-5.0546213726, -7.5428960337), (-5.0350872121, -7.5771667299)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(17.75, 0), (17.75, -0.2471562043), (17.7443800388, -0.7311876185), (17.719090231, -1.4263917613), (17.6522917053, -2.2918765662), (17.5177346358, -3.273007783), (17.3379348044, -4.1562000494), (17.1197366378, -4.9453016275), (16.8702963405, -5.6452095981), (16.5963827576, -6.2618566931), (16.3036449114, -6.8022227183), (15.9959557089, -7.2743134457), (15.6745638458, -7.687241432), (15.3377981671, -8.0510295963), (14.9826016133, -8.3754912725), (14.6057661268, -8.6692586518), (14.205262349, -8.938768809), (13.7815848425, -9.1872224074), (13.3389559243, -9.4136554977), (12.8834242004, -9.6143735354), (12.4211497126, -9.7842493553), (11.9565774448, -9.9180858207), (11.4907560361, -10.0119070501), (11.0193086645, -10.0644040055), (10.5350695857, -10.0763420344), (10.0310035705, -10.0498359186), (9.5031906248, -9.9876347449), (8.9534099475, -9.8925155908), (8.3928995183, -9.7663619542), (7.8398830421, -9.6109734565), (7.3147444922, -9.4295281824), (6.8359407627, -9.2278614681), (6.4156951087, -9.015781329), (6.0555389989, -8.8085084307), (5.7425291362, -8.6277058264), (5.4569785328, -8.4947134364), (5.1788118254, -8.4250378213), (4.8956709655, -8.4207857604), (4.6063007562, -8.4689261903), (4.3146978772, -8.550859071), (4.0257509216, -8.6504982822), (3.798405638, -8.7384168889), (3.6304006836, -8.8077581989), (3.5195033973, -8.8555071333), (3.4643315895, -8.8797613281)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                Line((-17.5489161028, 0), (17.75, 0))
            make_face()
            with BuildLine():
                _nurbs_edge([(16.5986722569, -1.6500000884), (16.5738848148, -1.8534481241), (16.5466199702, -2.0579996588), (16.5168011645, -2.2632750746), (16.4158241931, -2.9584098815), (16.2858350342, -3.6652210879), (16.1194289489, -4.3293168748), (15.9744547207, -4.9078820998), (15.8008318764, -5.4490410587), (15.5974145959, -5.9090278213), (15.4219045147, -6.3059081347), (15.2262790559, -6.6399952983), (15.0057927076, -6.9258465839), (14.7728543216, -7.227841413), (14.5086614863, -7.4829652908), (14.1992489123, -7.7209123671), (13.8686312726, -7.9751667424), (13.4852376276, -8.2099552759), (13.0876988537, -8.4120182952), (12.7098245053, -8.6040861809), (12.3241738756, -8.7630709121), (11.9554483254, -8.87257012), (11.5409530598, -8.995661409), (11.1501692758, -9.0579979961), (10.7121523473, -9.0655440791), (10.3931745371, -9.0710393758), (10.0441891504, -9.0465823566), (9.6651326184, -8.9929363193), (9.0510506251, -8.9060282654), (8.3640191864, -8.7403317876), (7.7924163084, -8.5321660263), (7.5031612068, -8.4268253943), (7.2455795003, -8.3122506629), (7.0160654469, -8.1947527935), (6.772983474, -8.0703089371), (6.5598797949, -7.9401396539), (6.3141231534, -7.8068345053), (6.1467260929, -7.7160337445), (5.9606470657, -7.6231556167), (5.7464115124, -7.5517430617), (5.531888318, -7.4802346254), (5.2914569191, -7.4365762963), (5.0642072386, -7.4307069761), (4.9080144676, -7.4266728873), (4.7591613727, -7.4383655888), (4.6205861075, -7.458584832)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0685261824, 0.0685261824, 0.0685261824, 0.0685261824, 0.0925528782, 0.0925528782, 0.0925528782, 0.1739157266, 0.1739157266, 0.1739157266, 0.2447996497, 0.2447996497, 0.2447996497, 0.305958874, 0.305958874, 0.305958874, 0.3705720853, 0.3705720853, 0.3705720853, 0.4396134534, 0.4396134534, 0.4396134534, 0.5052396607, 0.5052396607, 0.5052396607, 0.5790120157, 0.5790120157, 0.5790120157, 0.6327353829, 0.6327353829, 0.6327353829, 0.7197687133, 0.7197687133, 0.7197687133, 0.7638112397, 0.7638112397, 0.7638112397, 0.8104573777, 0.8104573777, 0.8104573777, 0.8422303802, 0.8422303802, 0.8422303802, 0.8740460424, 0.8740460424, 0.8740460424, 0.8959135162, 0.8959135162, 0.8959135162, 0.8959135162], 3)
                _nurbs_edge([(4.6205861075, -7.458584832), (4.6171544949, -7.4286825431), (4.6132686627, -7.3984680002), (4.6089082128, -7.3680784177), (4.5655960849, -7.0662202311), (4.4717770659, -6.7391525373), (4.3073014208, -6.4275951821), (4.1522465682, -6.1338831268), (3.9362899151, -5.8604309459), (3.6887042941, -5.629350701), (3.3232736713, -5.2882816296), (2.8949029839, -5.0310282437), (2.4601249256, -4.8277608247), (2.0026151475, -4.613865873), (1.5387519996, -4.459149406), (1.0744379046, -4.3429117814), (0.5575615637, -4.2135155845), (0.0364005976, -4.1319748403), (-0.5203884152, -4.0808564754), (-0.9772907325, -4.0389086302), (-1.4620402728, -4.0167415086), (-1.9604593464, -4.0247477935), (-2.6272055372, -4.0354579773), (-3.3106901397, -4.0996426034), (-3.9285098425, -4.2881081124), (-4.3120972295, -4.4051212018), (-4.6710003868, -4.5749374238), (-4.9732631498, -4.7936348732), (-5.2707050842, -5.0088442881), (-5.5092055878, -5.266379469), (-5.6890221794, -5.5324530056), (-5.835895845, -5.7497810912), (-5.9471873215, -5.9735513754), (-6.0287150776, -6.2052186081)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1321302643, 0.1321302643, 0.1321302643, 0.1321302643, 0.1379460228, 0.1379460228, 0.1379460228, 0.1957136588, 0.1957136588, 0.1957136588, 0.2501724954, 0.2501724954, 0.2501724954, 0.3305524727, 0.3305524727, 0.3305524727, 0.4151349966, 0.4151349966, 0.4151349966, 0.5092926067, 0.5092926067, 0.5092926067, 0.5865585535, 0.5865585535, 0.5865585535, 0.6899189151, 0.6899189151, 0.6899189151, 0.7540925419, 0.7540925419, 0.7540925419, 0.8172426551, 0.8172426551, 0.8172426551, 0.8688234827, 0.8688234827, 0.8688234827, 0.8688234827], 3)
                _nurbs_edge([(-6.0287150776, -6.2052186081), (-6.1865573948, -6.1992206666), (-6.3433914041, -6.2044311819), (-6.4991784298, -6.218225991), (-7.1314512578, -6.2742132145), (-7.7465976079, -6.4693285301), (-8.3388866872, -6.6651417059), (-8.7998225894, -6.8175289877), (-9.2424521641, -6.9673505093), (-9.673174243, -7.0642641697), (-10.0750399188, -7.1546850594), (-10.4681233484, -7.2003403755), (-10.8795037829, -7.1909507254), (-11.2875171882, -7.1816379268), (-11.7170677483, -7.1175793034), (-12.1407452614, -7.0125391033), (-12.5263429363, -6.9169398429), (-12.9037990862, -6.7896869752), (-13.2387942345, -6.6448112924), (-13.5193042562, -6.5234988461), (-13.7672992112, -6.3912254458), (-13.9926396006, -6.2358296837), (-14.2536310691, -6.0558487746), (-14.4916380605, -5.8418515593), (-14.7404446382, -5.5393227277), (-14.9541891915, -5.2794265041), (-15.1746405103, -4.9514795369), (-15.3924952376, -4.5580719046), (-15.7092934617, -3.985989578), (-16.0180798017, -3.2777893117), (-16.2581922316, -2.5576975142), (-16.359827502, -2.2528956156), (-16.448784281, -1.9470378388), (-16.5217853153, -1.6500001407)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1056564566, 0.1056564566, 0.1056564566, 0.1056564566, 0.1343469161, 0.1343469161, 0.1343469161, 0.2507892061, 0.2507892061, 0.2507892061, 0.341407848, 0.341407848, 0.341407848, 0.4259554566, 0.4259554566, 0.4259554566, 0.5098110677, 0.5098110677, 0.5098110677, 0.5861297951, 0.5861297951, 0.5861297951, 0.6500356995, 0.6500356995, 0.6500356995, 0.7240521501, 0.7240521501, 0.7240521501, 0.7876381426, 0.7876381426, 0.7876381426, 0.8801031064, 0.8801031064, 0.8801031064, 0.9192418616, 0.9192418616, 0.9192418616, 0.9192418616], 3)
                Line((0, -2.25), (-16.5217853153, -1.6500001407))
                Line((16.5986722569, -1.6500000884), (0, -2.25))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a long, slender cylindrical rod or tube with a hexagonal cross-section, featuring a smooth tapered end at the top and a uniform ribbed or fluted surface along its length.
def model_34317_e9c65aa6_0000():
    """Model: Beam3 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.16, perimeter: 21.6
            with BuildLine():
                Line((6.9096404851, -11.0704449915), (2.5096404851, -11.0704449915))
                Line((6.9096404851, -4.6704449915), (6.9096404851, -11.0704449915))
                Line((2.5096404851, -4.6704449915), (6.9096404851, -4.6704449915))
                Line((2.5096404851, -11.0704449915), (2.5096404851, -4.6704449915))
            make_face()
        # OneSide extrude, distance=83.1096
        extrude(amount=83.1096)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or bearing component with a smooth, uniform cross-section and a central void, featuring a textured or ribbed surface pattern across its curved geometry.
def model_34317_e9c65aa6_0006():
    """Model: Ring v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36.3246650571, perimeter: 58.1194640914
            with BuildLine():
                CenterArc((-1.5, 2), 5.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5, 2), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical shaft or tube with two circular flanged ends and longitudinal slot features running along its length, designed for mechanical transmission or alignment purposes.
def model_34317_e9c65aa6_0009():
    """Model: Handle v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.0138265833, perimeter: 26.7035375555
            with BuildLine():
                CenterArc((-4, 1.5), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4, 1.5), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=11.8
        extrude(amount=11.8)
    return part.part


# Description: This is a curved structural bracket or connector with a complex saddle-like shape featuring two opposing curved surfaces, multiple internal ribs for reinforcement, and a distinctive twisted or swept geometry that transitions between a narrower left section and a wider right section.
def model_34317_e9c65aa6_0010():
    """Model: Holdfast v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 201.7604908082, perimeter: 80.8765937179
            with BuildLine():
                Line((11.955616396, 5.7498048757), (11.955616396, 16.2498048757))
                Line((-15.5300010253, 16.2498048757), (11.955616396, 16.2498048757))
                Line((-15.5300010253, 5.7498048757), (-15.5300010253, 16.2498048757))
                Line((-11.5300010253, 5.7498048757), (-15.5300010253, 5.7498048757))
                CenterArc((-1.7871923146, 1.2066585619), 10.75, 25, 130)
                Line((7.955616396, 5.7498048757), (11.955616396, 5.7498048757))
            make_face()
        # OneSide extrude, distance=22
        extrude(amount=22)
    return part.part


# Description: This is a cylindrical capsule-shaped component with hemispherical ends, featuring ribbed or corrugated surfaces on both circular end caps and a smooth tapered central body with internal geometric divisions or partitions.
def model_34317_e9c65aa6_0011():
    """Model: Groove v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.3193733277, perimeter: 9.7982297102
            with BuildLine():
                Line((-5.0019147675, -0.1999973812), (-4.9980865894, -0.1999973849))
                Line((-4.9980865894, -0.1999973849), (-2.3000006785, -0.2))
                CenterArc((-2.3, 0.5), 0.7, -90.0000555336, 180.0001110628)
                Line((-4.9980865894, 1.1999973849), (-2.3000006784, 1.2))
                Line((-5.0019147675, 1.1999973812), (-4.9980865894, 1.1999973849))
                CenterArc((-5, 0.5), 0.7, 90.1567260478, 179.6865479045)
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a curved sheet metal or composite panel with a distinctive aerodynamic shape, featuring a horizontal flange on the left side and a smoothly curved surface that transitions from a flat upper section to a rounded lower edge, with horizontal ribbing or corrugation patterns visible across the blue-tinted surface.
def model_34317_e9c65aa6_0014():
    """Model: Lining2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.0268400733, perimeter: 48.7147205863
            with BuildLine():
                Line((5.8061484006, 6.4876092805), (6.0327253474, 6.5932638459))
                CenterArc((-3.7100833633, 2.0501175322), 10.75, 25, 130)
                Line((-13.2263151272, 6.4876092805), (-13.4528920739, 6.5932638459))
                CenterArc((-3.7100833633, 2.0501175322), 10.5, 25, 130)
            make_face()
        # OneSide extrude, distance=22
        extrude(amount=22)
    return part.part


# Description: This is a long, narrow rectangular beam or rail with a slightly tapered hexagonal cross-section, featuring a small slot or opening in the center and angled end caps on both sides.
def model_34317_e9c65aa6_0016():
    """Model: Beam2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24, perimeter: 20
            with BuildLine():
                Line((1.5, -4), (-2.5, -4))
                Line((1.5, 2), (1.5, -4))
                Line((-2.5, 2), (1.5, 2))
                Line((-2.5, -4), (-2.5, 2))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)
    return part.part


# Description: This is a cylindrical sleeve or tube with a ribbed or grooved texture covering its outer surface, featuring slightly tapered ends and a hollow interior design.
def model_34317_e9c65aa6_0019():
    """Model: Lining v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.2013246993, perimeter: 128.8052987972
            with BuildLine():
                CenterArc((0, 0), 10.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 10, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=33.0027
        extrude(amount=33.0027)
    return part.part


# Description: This is a windsurfing boom or hydrofoil wing with an elongated oval footprint, featuring a hollow central cavity with internal ribbing for structural support, curved side flanges, and a streamlined aerodynamic profile.
def model_34327_81dcda78_0000():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 281.9911485751, perimeter: 83.9822971503
            with BuildLine():
                CenterArc((5, -5), 4, -90, 90)
                Line((9, 5), (9, -5))
                CenterArc((5, 5), 4, 0, 90)
                Line((-5, 9), (5, 9))
                CenterArc((-5, 5), 4, 90, 90)
                Line((-9, -5), (-9, 5))
                CenterArc((-5, -5), 4, 180, 90)
                Line((5, -9), (-5, -9))
            make_face()
            with BuildLine():
                CenterArc((5, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a trapezoidal profile, featuring angled side faces and internal geometric divisions that suggest structural reinforcement or internal cavities.
def model_34327_81dcda78_0003():
    """Model: Ayuda pra sujeccion"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((1.5, -1), (-1.5, -1))
                Line((1.5, 1), (1.5, -1))
                Line((-1.5, 1), (1.5, 1))
                Line((-1.5, -1), (-1.5, 1))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a long, thin blue metallic bar or strip with a elongated parallelogram shape, featuring beveled or chamfered edges at both ends and a slightly tapered profile that gives it a three-dimensional appearance.
def model_34327_81dcda78_0005():
    """Model: LEDs"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 75, perimeter: 56
            with BuildLine():
                Line((12.5, -1.5), (-12.5, -1.5))
                Line((12.5, 1.5), (12.5, -1.5))
                Line((-12.5, 1.5), (12.5, 1.5))
                Line((-12.5, -1.5), (-12.5, 1.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved dish or bowl-shaped component with a flattened, elliptical rim featuring a recessed center cavity and a slightly dished profile, likely designed for containing or supporting materials.
def model_34327_81dcda78_0009():
    """Model: ONOFF"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-10.5, -4)):
                Circle(0.5)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is an L-shaped bracket or corner connector with a curved top surface featuring a fan or radial rib pattern, two cylindrical holes at each end, and reinforcing ribs along the inner corner for structural support.
def model_34330_5eff1ee1_0001():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0084610579, perimeter: 0.6425089657
            with BuildLine():
                Line((0, -0.045), (0.0633557647, -0.0776910581))
                CenterArc((0.075, -0.0555684049), 0.025, -117.76002835, 186.8344379548)
                Line((0, 0), (0.0839288803, -0.0322172787))
                Line((0, 0), (-0.0839288803, -0.0322172787))
                CenterArc((-0.075, -0.0555684049), 0.025, 110.9255903952, 186.8344379548)
                Line((0, -0.045), (-0.0633557647, -0.0776910581))
            make_face()
            with BuildLine():
                CenterArc((-0.075, -0.0555684049), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.075, -0.0555684049), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


# Description: This is a curved composite or fabric sleeve with an elongated, tapered tubular shape featuring a textured or ribbed surface pattern, designed to fit over or protect an object.
def model_34343_6d3253e1_0007():
    """Model: Longboard Press .75" Lower v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 96.8946988797, perimeter: 65.0865143995
            with BuildLine():
                Line((0, 0), (-1.905, 0))
                Line((0, 30.48), (0, 0))
                Line((0, 30.48), (-1.905, 30.48))
                CenterArc((58.1025, 15.24), 61.9125, 165.7499673022, 14.2500326978)
                CenterArc((58.1025, 15.24), 61.9125, -180, 14.2500326978)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a curved, elongated duct or channel component with a tapered, crescent-like cross-section that features longitudinal ribbing or fluting along its length for structural reinforcement.
def model_34343_6d3253e1_0013():
    """Model: Longboard Press .50" Lower v2 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 169.2818889315, perimeter: 67.7409911174
            with BuildLine():
                CenterArc((21.3567239019, 15.24), 28.3427418088, 147.4725369901, 65.0549260199)
                Line((0, 0), (-2.54, 0))
                Line((0, 30.48), (0, 0))
                Line((-2.54, 30.48), (0, 30.48))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a long, tapered dark blue composite or plastic structural component with a streamlined, aerodynamic shape that features internal ribbing or lattice reinforcement visible through semi-transparent sections, tapering from a wider rectangular cross-section at one end to a pointed nose cone at the other.
def model_34343_6d3253e1_0018():
    """Model: Longboard Press .70" Lower v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 99.5010790839, perimeter: 65.1299697103
            with BuildLine():
                Line((-1.905, 30.48), (0, 30.48))
                CenterArc((54.229, 15.24), 58.166, 164.8107132628, 15.1892867372)
                CenterArc((54.229, 15.24), 58.166, -180, 15.1892867372)
                Line((0, 0), (-1.905, 0))
                Line((0, 30.48), (0, 0))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a curved composite or metal channel/duct component with an elongated, tapered tubular shape featuring internal ribbing or reinforcement patterns and a streamlined aerodynamic profile.
def model_34343_6d3253e1_0023():
    """Model: Longboard Press .55" Lower v2 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 112.3244707383, perimeter: 66.1016416859
            with BuildLine():
                Line((0, 0), (-2.413, 0))
                Line((0, 30.48), (0, 0))
                Line((-2.413, 30.48), (0, 30.48))
                CenterArc((57.6802948386, 15.24), 61.9956585944, 165.7694850252, 28.4610299496)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a tapered punch or chisel tool with an elongated, slightly curved prismatic body that narrows to a sharp point at one end and has a flat or slightly rounded striking end at the other.
def model_34343_6d3253e1_0025():
    """Model: Longboard Press Joint Alignment v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1083.8688, perimeter: 261.62
            with BuildLine():
                Line((-8.89, 121.92), (0, 121.92))
                Line((-8.89, 0), (-8.89, 121.92))
                Line((0, 0), (-8.89, 0))
                Line((0, 121.92), (0, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is an elongated structural beam or channel with a tapered hexagonal cross-section, featuring a hollow interior with internal ribbing/bracing and open slots along its length for lightweighting.
def model_34343_6d3253e1_0029():
    """Model: Longboard Press .75" Upper v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 174.0725011203, perimeter: 75.2465143995
            with BuildLine():
                Line((-8.89, 30.48), (-1.905, 30.48))
                Line((-8.89, 0), (-8.89, 30.48))
                Line((-1.905, 0), (-8.89, 0))
                CenterArc((58.1025, 15.24), 61.9125, 165.7499673022, 28.5000653956)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a long, tapered rectangular duct or channel with a hexagonal cross-section that gradually narrows from left to right, featuring internal ribbing or lattice reinforcement structures along its length.
def model_34343_6d3253e1_0031():
    """Model: Longboard Press .65” Upper v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 166.3305811203, perimeter: 74.7385143995
            with BuildLine():
                Line((-8.89, 30.48), (-2.159, 30.48))
                Line((-8.89, 0), (-8.89, 30.48))
                Line((-2.159, 0), (-8.89, 0))
                CenterArc((57.8485, 15.24), 61.9125, 165.7499673022, 28.5000653956)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a long, tapered rectangular duct or channel with a hexagonal cross-section that gradually narrows from a larger opening at one end to a smaller opening at the other, featuring internal ribbing or reinforcement structure throughout its length.
def model_34343_6d3253e1_0035():
    """Model: Longboard Press .50" Upper v3 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 101.6853110685, perimeter: 75.3609911174
            with BuildLine():
                Line((-8.89, 30.48), (-2.54, 30.48))
                Line((-8.89, 0), (-8.89, 30.48))
                Line((-2.54, 0), (-8.89, 0))
                CenterArc((21.3567239019, 15.24), 28.3427418088, 147.4725369901, 65.0549260199)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a long, tapered triangular duct or channel with a hexagonal cross-section that narrows from a wider end to a pointed end, featuring internal ribbing or bracing structure along its length.
def model_34343_6d3253e1_0036():
    """Model: Longboard Press .55" Upper v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 158.6427292617, perimeter: 74.2296416859
            with BuildLine():
                Line((-2.413, 0), (-8.89, 0))
                CenterArc((57.6802948386, 15.24), 61.9956585944, 165.7694850252, 28.4610299496)
                Line((-8.89, 30.48), (-2.413, 30.48))
                Line((-8.89, 0), (-8.89, 30.48))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a flat, elongated rectangular box or tray with a shallow depth, featuring an angled or beveled left end and internal ribbing or reinforcement patterns across its top surface.
def model_34343_6d3253e1_0039():
    """Model: Longboard Press End Aligner v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.1612, perimeter: 27.94
            with BuildLine():
                Line((-8.89, 5.08), (0, 5.08))
                Line((-8.89, 0), (-8.89, 5.08))
                Line((0, 0), (-8.89, 0))
                Line((0, 5.08), (0, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: A cylindrical rod or pipe with rounded ends, displayed at an angle, featuring a uniform diameter throughout its length.
def model_34347_841c5375_0009():
    """Model: Carbon Fiber Paddle Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.425114785, perimeter: 17.9542020153
            with BuildLine():
                CenterArc((0, 0), 1.508125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.349375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-33.02
        extrude(amount=-33.02)
    return part.part


# Description: This is a flat, ring-shaped washer or thrust bearing with a circular central hole and a smooth, slightly curved outer profile, commonly used for spacing, load distribution, or rotational support in mechanical assemblies.
def model_34436_ffc43a58_0002():
    """Model: anilla"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5500000037), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1476668687, perimeter: 2.2442802117
            with BuildLine():
                CenterArc((-0.7500000112, 1.5000000224), 0.25, 126.8699061836, 53.1202026458)
                CenterArc((-0.7500000112, 1.5000000224), 0.25, 179.9901088293, 180.0098911707)
                CenterArc((-0.7500000112, 1.5000000224), 0.25, 0, 53.1300938164)
                Line((-0.5999999814, 1.7), (-0.900000041, 1.7))
            make_face()
            with BuildLine():
                CenterArc((-0.7500000112, 1.5000000224), 0.11065, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.010218826, perimeter: 0.6217506885
            with BuildLine():
                Line((-0.5999999814, 1.7), (-0.900000041, 1.7))
                CenterArc((-0.7500000112, 1.5000000224), 0.25, 53.1300938164, 73.7398123672)
            make_face()
        # OneSide extrude, distance=0.046
        extrude(amount=0.046)
    return part.part


# Description: This is a turning tool holder or lathe tool bit holder with an elongated hexagonal/parallelogram cross-section, featuring a tapered left end for clamping or mounting and a flat top surface for tool bit attachment.
def model_34440_af990c77_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 70, perimeter: 74
            with BuildLine():
                Line((35, 2), (0, 2))
                Line((35, 4), (35, 2))
                Line((0, 4), (35, 4))
                Line((0, 2), (0, 4))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical threaded fastener or bolt with a rounded/tapered head and external helical threading along its shaft, designed for mechanical assembly and fastening applications.
def model_34440_af990c77_0009():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2002412853, perimeter: 1.7120654344
            with BuildLine():
                CenterArc((29.5000004396, 2.1000000313), 0.3000000045, -19.4712266716, 218.9424533432)
                Line((29.2171577334, 2), (29.7828431457, 2))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a timing belt featuring a continuous loop with parallel ribs on the inner surface for grip and drive transmission, characterized by its oval-elliptical shape and uniform width.
def model_34520_035b5e9a_0000():
    """Model: Speaker_Magnet"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6182343759, perimeter: 19.0380514808
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.43, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a cylindrical shell or cup-shaped container with a curved, tapered design featuring an open top with a blue-highlighted rim edge and darker body walls.
def model_34520_035b5e9a_0006():
    """Model: Potentiometer_Knob_Sized"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.317132355, perimeter: 4.0683624864
            Circle(0.6475)
        # OneSide extrude, distance=0.73
        extrude(amount=0.73)
    return part.part


# Description: This is a spheroidal or egg-shaped shell structure with a smooth, curved surface featuring a series of parallel vertical ribs or flutes running along its length, creating a ribbed texture across the ellipsoidal form.
def model_34522_ed4af450_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8156646796, perimeter: 4.7766426782
            with Locations((-3.2833420926, 1.584558673)):
                Circle(0.7602262936)
        # Symmetric extrude, each_side=-0.2
        extrude(amount=-0.2, both=True)
    return part.part


# Description: This is an oval or elliptical shell/pod structure with a smooth, symmetrical form featuring vertical ribbing or fluting patterns across its surface and internal curved geometry visible through transparent sections.
def model_34525_13455627_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.7422761614, perimeter: 5.8703031073
            with Locations((3.7070883603, 2.0128986572)):
                Circle(0.934287757)
        # Symmetric extrude, each_side=0.19
        extrude(amount=0.19, both=True)
    return part.part


# Description: This is an ellipsoidal or ovoid shell structure with a smooth, curved exterior surface defined by vertical ribbing or linear surface patterns that create a streamlined, organic form without any holes, slots, or flanges.
def model_34526_3ea355a5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.6351375424, perimeter: 5.7544865086
            with Locations((-3.6891053576, 3.3598617633)):
                Circle(0.9158549728)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a cylindrical or oval-shaped component with a hollow interior core, featuring a ribbed or corrugated surface texture on its outer walls and internal curved surfaces that suggest a complex internal geometry or compartmentalized structure.
def model_34535_2e59cac1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21.1381483349, perimeter: 16.2981534561
            with Locations((7, 5)):
                Circle(2.5939316858)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a cylindrical roller or bearing component with a rounded rectangular profile, featuring a smooth curved outer surface and what appears to be a central hollow or bore running through its length.
def model_34538_4d9a3cdd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.6779125327, perimeter: 9.1606290077
            with Locations((-5, 0)):
                Circle(1.4579593884)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a cylindrical wheel or pulley with a rounded, barrel-like profile featuring radial spokes or fins extending from a central dark hub to the outer rim.
def model_34540_86189f81_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 54.8067540649, perimeter: 26.2435131747
            with Locations((-15.0155775949, 9.1492033014)):
                Circle(4.1767848458)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a cylindrical or drum-shaped container with an open top, featuring a curved, slightly tapered body with vertical ribbing or fluting on the exterior sides and a mesh or perforated pattern on the upper rim surface.
def model_34568_fbe47bf9_0000():
    """Model: pieza 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0010995574, perimeter: 0.2199114858
            with BuildLine():
                CenterArc((0, 0), 0.0225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0225
        extrude(amount=0.0225)
    return part.part


# Description: This is an elongated elliptical boat hull or shell structure featuring a streamlined, symmetrical oval shape with internal ribbing/stiffening elements running lengthwise and a raised flange or rim around the perimeter.
def model_34587_ed155e93_0010():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal or octagonal prism-based container or enclosure with tapered pyramidal top sections and open cutouts or slots on the upper edges, designed as a box-like structure with angular faceted surfaces.
def model_34678_f709cdcc_0000():
    """Model: Tuerca semifija"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0721284585, perimeter: 2.0813981634
            with BuildLine():
                Line((2.1521348153, -2.524459106), (2.2601348153, -2.3373976187))
                Line((2.2601348153, -2.3373976187), (2.1521348153, -2.1503361315))
                Line((2.1521348153, -2.1503361315), (1.9361348153, -2.1503361315))
                Line((1.9361348153, -2.1503361315), (1.8281348153, -2.3373976187))
                Line((1.8281348153, -2.3373976187), (1.9361348153, -2.524459106))
                Line((1.9361348153, -2.524459106), (2.1521348153, -2.524459106))
            make_face()
            with BuildLine():
                CenterArc((2.0441348153, -2.3373976187), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2135
        extrude(amount=0.2135)
    return part.part


# Description: This is a triangular bracket or gusset plate with three mounting holes at each corner and internal reinforcing ribs, designed to provide structural support and rigidity between perpendicular surfaces.
def model_34678_f709cdcc_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1504774376, perimeter: 9.5429525528
            with BuildLine():
                CenterArc((-2.4072360072, 3.5542325389), 0.35, -28.451429185, 118.451429185)
                Line((-2.4072360072, 3.9042325389), (-4.0072360072, 3.9042325389))
                CenterArc((-4.0072360072, 3.5542325389), 0.35, 90, 118.451429185)
                Line((-4.3149634602, 3.3874877797), (-3.5149634602, 1.9110877797))
                CenterArc((-3.2072360072, 2.0778325389), 0.35, -151.548570815, 123.0971416299)
                Line((-2.8995085543, 1.9110877797), (-2.0995085543, 3.3874877797))
            make_face()
            with BuildLine():
                CenterArc((-4.0072360072, 3.5542325389), 0.12655, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.4072360072, 3.5542325389), 0.12655, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.2072360072, 2.0778325389), 0.12655, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.125
        extrude(amount=0.125)
    return part.part


# Description: This is a cylindrical tube or pipe with hemispherical end caps, featuring longitudinal slots or grooves running along its length and mesh or perforated sections at both ends.
def model_34678_f709cdcc_0003():
    """Model: Pasador (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-5.6000000834, 1.0000000149)):
                Circle(0.05)
        # OneSide extrude, distance=0.525
        extrude(amount=0.525)
    return part.part


# Description: This is a cylindrical shaft or rod with a hexagonal or polygonal cross-section, featuring a slightly tapered or rounded end on one side and a flat or recessed end on the opposite side.
def model_34678_f709cdcc_0008():
    """Model: Pasador de horquilla"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0001227185, perimeter: 0.0392699082
            with Locations((3.6000000536, 0.1000000015)):
                Circle(0.00625)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a streamlined, elongated pod or fairing with a tapered, aerodynamic shape featuring a curved upper surface with triangulated faceting and a darker flat or recessed bottom surface, designed for minimal drag in fluid dynamics applications.
def model_34689_969a9743_0002():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 314.1857711781, 7.7878336871), x_dir=(1, 0, 0), z_dir=(0, 0.9996929351, 0.0247797419))):
            # Profile area: 4896.3976215535, perimeter: 296.1010224539
            with BuildLine():
                Line((-10, 50.7089513286), (-42.9055466999, 17.8135087687))
                Line((-42.9055466999, 17.8135087687), (-42.9055466999, -2.1803499324))
                Line((-42.9055466999, -2.1803499324), (-10, -35.0757924923))
                Line((-10, -35.0757924923), (10, -35.0757924923))
                Line((10, -35.0757924923), (42.9055466999, -2.1803499324))
                Line((42.9055466999, -2.1803499324), (42.9055466999, 17.8135087687))
                Line((42.9055466999, 17.8135087687), (10, 50.7089513286))
                Line((10, 35.7089513286), (10, 50.7089513286))
                Line((-10, 35.7089513286), (10, 35.7089513286))
                Line((-10, 50.7089513286), (-10, 35.7089513286))
            make_face()
            # Profile area: 300, perimeter: 70
            with BuildLine():
                Line((-10, 50.7089513286), (-10, 35.7089513286))
                Line((-10, 35.7089513286), (10, 35.7089513286))
                Line((10, 35.7089513286), (10, 50.7089513286))
                Line((10, 50.7089513286), (-10, 50.7089513286))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a long, slender rectangular prism or bar stock with a uniform cross-section and slight angular orientation, featuring a smooth, minimalist design with no visible holes, slots, or flanges.
def model_34689_969a9743_0003():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4446.8383499744, perimeter: 629.6835039415
            with BuildLine():
                Line((-42.9055466999, 315.4423259037), (-27.9101526741, 315.0706297753))
                Line((-95, 20), (-42.9055466999, 315.4423259037))
                Line((-79.9390659182, 20), (-95, 20))
                Line((-27.9101526741, 315.0706297753), (-79.9390659182, 20))
            make_face()
        # TwoSides extrude (symmetric), distance=10
        extrude(amount=10, both=True)
    return part.part


# Description: This is a quadrilateral plate or panel with a flat, slightly tapered trapezoidal shape and internal triangulated reinforcement ribs that provide structural stiffening across the surface.
def model_34689_969a9743_0004():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3900, perimeter: 431.2310562562
            with BuildLine():
                Line((100, 0), (95, 20))
                Line((-95, 20), (95, 20))
                Line((-100, 0), (-95, 20))
                Line((100, 0), (-100, 0))
            make_face()
        # TwoSides extrude (symmetric), distance=100
        extrude(amount=100, both=True)
    return part.part


# Description: This is a rectangular duct or channel connector with a tapered/curved profile, featuring a long, narrow box-like shape with angled edges and a slight longitudinal curve or bend.
def model_34708_7559c801_0004():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -258.9760954935), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5300.6481574763, perimeter: 482.717317856
            with BuildLine():
                Line((430, 180), (414.768895531, 126.6911343585))
                Line((430, 180), (228.1878657859, 180))
                Line((414.768895531, 126.6911343585), (228.1878657859, 180))
            make_face()
            with BuildLine():
                CenterArc((400, 150), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 21683.0955824158, perimeter: 855.5505083472
            with BuildLine():
                Line((434.3084504453, 195.0795765584), (430, 180))
                Line((68.4593938415, 299.6078784452), (434.3084504453, 195.0795765584))
                Line((48.9198389272, 231.2194362453), (68.4593938415, 299.6078784452))
                Line((228.1878657859, 180), (48.9198389272, 231.2194362453))
                Line((430, 180), (228.1878657859, 180))
            make_face()
        # OneSide extrude, distance=70
        extrude(amount=70)
    return part.part


# Description: This is a cylindrical rod or pin with a uniform diameter throughout its length, featuring slightly rounded ends and a smooth, tapered appearance typical of a dowel pin or support shaft.
def model_34769_44655d03_0000():
    """Model: Barras 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-1.795791425, 0.8585712609)):
                Circle(0.125)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a rounded end cap, featuring a hollow bore through its length and smooth cylindrical geometry typical of a tubular component or connector.
def model_34769_44655d03_0001():
    """Model: tubo 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((-1.5000000224, 0.6000000089), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5000000224, 0.6000000089), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


# Description: This is a simple cylindrical rod or shaft with rounded ends, featuring a straight, elongated body with minimal features.
def model_34769_44655d03_0005():
    """Model: EJE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-6.1000000909, 0.7000000104)):
                Circle(0.15)
        # OneSide extrude, distance=6.3
        extrude(amount=6.3)
    return part.part


# Description: This is a tall, hexagonal prism or elongated hexagonal column with a tapered top section, featuring clean edges and a uniform dark blue finish.
def model_34770_6bba5bd4_0002():
    """Model: Sear Lock"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6129, perimeter: 6.35
            with BuildLine():
                Line((3.1750001216, 2.7940000081), (3.8100001216, 2.7940000081))
                Line((3.1750001216, 0.2540000081), (3.1750001216, 2.7940000081))
                Line((3.8100001216, 0.2540000081), (3.1750001216, 0.2540000081))
                Line((3.8100001216, 2.7940000081), (3.8100001216, 0.2540000081))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: These are two identical trapezoidal bin or tray components with open tops, angled side walls, and a dark navy blue finish, featuring a slightly curved or contoured interior surface.
def model_34770_6bba5bd4_0006():
    """Model: body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8845307064, perimeter: 8.1094556675
            with BuildLine():
                Line((-3.4925, 0), (-5.715, 0))
                Line((-3.4925, 1.3335), (-3.4925, 0))
                Line((-5.715, 1.3335), (-3.4925, 1.3335))
                Line((-5.715, 0), (-5.715, 1.3335))
            make_face()
            with BuildLine():
                CenterArc((-4.60375, 0.66675), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.8845307064, perimeter: 8.1094556675
            with BuildLine():
                Line((-2.2225, 0), (-2.2225, 1.3335))
                Line((0, 0), (-2.2225, 0))
                Line((0, 1.3335), (0, 0))
                Line((-2.2225, 1.3335), (0, 1.3335))
            make_face()
            with BuildLine():
                CenterArc((-1.11125, 0.66675), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a flat, parallelogram-shaped frame or bezel with a hollow rectangular opening in the center and flanged edges on all sides, featuring a skewed rhombus geometry in a blue anodized aluminum finish.
def model_34770_6bba5bd4_0007():
    """Model: Mounting Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 88.897285215, perimeter: 89.8047340051
            with BuildLine():
                Line((-10.856945939, 7.9932743497), (-10.856945939, -2.1667256503))
                Line((-10.856945939, -2.1667256503), (4.383054061, -2.1667256503))
                Line((4.383054061, -2.1667256503), (4.383054061, 7.9932743497))
                Line((4.383054061, 7.9932743497), (-10.856945939, 7.9932743497))
            make_face()
            with BuildLine():
                Line((1.843054061, 6.0882743497), (-8.316945939, 6.0882743497))
                Line((1.843054061, -0.2617256503), (1.843054061, 6.0882743497))
                Line((-8.316945939, -0.2617256503), (1.843054061, -0.2617256503))
                Line((-8.316945939, 6.0882743497), (-8.316945939, -0.2617256503))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.113054061, 2.9132743497), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.586945939, 2.9132743497), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a dual-chamber aerospace or industrial component with an overall elongated hexagonal/polygonal shape featuring two distinct pyramidal or wedge-shaped ends connected by a central body, with multiple angled faceted surfaces and internal geometric subdivisions visible through transparent sections.
def model_34770_6bba5bd4_0010():
    """Model: Sear"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2812097841, perimeter: 2.1637328873
            with BuildLine():
                Line((4.9403010147, 7.18583272), (5.5880001783, 7.18583272))
                Line((4.9403010147, 6.75166544), (4.9403010147, 7.18583272))
                Line((5.5880001783, 6.75166544), (4.9403010147, 6.75166544))
                Line((5.5880001783, 7.18583272), (5.5880001783, 6.75166544))
            make_face()
            # Profile area: 0.2812097841, perimeter: 2.1637328873
            with BuildLine():
                Line((4.9403010147, 7.18583272), (4.9403010147, 7.62))
                Line((4.9403010147, 7.18583272), (5.5880001783, 7.18583272))
                Line((5.5880001783, 7.62), (5.5880001783, 7.18583272))
                Line((4.9403010147, 7.62), (5.5880001783, 7.62))
            make_face()
            # Profile area: 0.7966976447, perimeter: 4.5613796769
            with BuildLine():
                Line((3.9878010147, 7.02708272), (3.9878010147, 6.75166544))
                CenterArc((3.9878010147, 7.18583272), 0.15875, 180, 90)
                Line((2.1072104147, 7.18583272), (3.8290510147, 7.18583272))
                Line((2.1072104147, 6.75166544), (2.1072104147, 7.18583272))
                Line((3.9878010147, 6.75166544), (2.1072104147, 6.75166544))
            make_face()
            # Profile area: 0.3937510733, perimeter: 2.7051984769
            with BuildLine():
                Line((3.9878010147, 7.62), (3.9878010147, 7.34458272))
                CenterArc((3.9878010147, 7.18583272), 0.15875, 0, 90)
                Line((4.1465510147, 7.18583272), (4.9403010147, 7.18583272))
                Line((4.9403010147, 7.18583272), (4.9403010147, 7.62))
                Line((3.9878010147, 7.62), (4.9403010147, 7.62))
            make_face()
            # Profile area: 0.3937510733, perimeter: 2.7051984769
            with BuildLine():
                Line((4.9403010147, 6.75166544), (4.9403010147, 7.18583272))
                Line((4.1465510147, 7.18583272), (4.9403010147, 7.18583272))
                CenterArc((3.9878010147, 7.18583272), 0.15875, -90, 90)
                Line((3.9878010147, 7.02708272), (3.9878010147, 6.75166544))
                Line((4.9403010147, 6.75166544), (3.9878010147, 6.75166544))
            make_face()
            # Profile area: 0.3399851416, perimeter: 2.3408193435
            with BuildLine():
                Line((2.7422104147, 7.62), (2.7422104147, 8.1554096718))
                Line((2.7422104147, 8.1554096718), (2.1072104147, 8.1554096718))
                Line((2.1072104147, 8.1554096718), (2.1072104147, 7.62))
                Line((2.1072104147, 7.62), (2.7422104147, 7.62))
            make_face()
            # Profile area: 0.7966976447, perimeter: 4.5613796769
            with BuildLine():
                Line((2.1072104147, 7.62), (2.7422104147, 7.62))
                Line((2.1072104147, 7.18583272), (2.1072104147, 7.62))
                Line((2.1072104147, 7.18583272), (3.8290510147, 7.18583272))
                CenterArc((3.9878010147, 7.18583272), 0.15875, 90, 90)
                Line((3.9878010147, 7.62), (3.9878010147, 7.34458272))
                Line((2.7422104147, 7.62), (3.9878010147, 7.62))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a dark gray, smooth, elongated dome or lens-shaped component with a curved upper surface and a flat or slightly curved base, featuring a pointed end on the right side and a rounded end on the left.
def model_34781_4f8a4759_0007():
    """Model: Mastil v14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 24 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.2955801577, perimeter: 12.4247427441
            with BuildLine():
                CenterArc((2.8, 1.4), 3.5, -142.571994457, 105.1439889139)
                CenterArc((5.5, -0.666397832), 0.1, -37.428005543, 103.7329261309)
                CenterArc((2.7999999556, -6.8186051166), 6.8186051166, 66.3049205879, 47.3901580779)
                CenterArc((0.1, -0.666397832), 0.1, 113.6950794121, 103.7329261309)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a hollow cylindrical tube or sleeve with an open top end featuring a blue-highlighted circular rim or flange, and a closed or tapered bottom end.
def model_34782_b461066c_0015():
    """Model: Union 25 v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a cylindrical mesh or perforated tube with an open top end and a solid dark exterior body, commonly used as a filter, strainer, or protective cage component.
def model_34782_b461066c_0016():
    """Model: Union v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)
    return part.part


# Description: This is a cylindrical tube or pipe with a closed bottom end and an open top end that appears to have a textured or mesh-like surface feature.
def model_34782_b461066c_0018():
    """Model: Table2 support v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            Circle(2.25)
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a simple elongated rectangular bar or beam with a flat, linear profile and no additional features.
def model_34785_dc3b83fa_0001():
    """Model: kratka v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 900, perimeter: 606
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (300, 0))
                Line((300, 0), (300, 3))
                Line((300, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a torus or ring-shaped bearing/washer with a circular cross-section, featuring a hollow center and a uniformly thick toroidal body with textured or knurled surfaces on the outer edges.
def model_34785_dc3b83fa_0031():
    """Model: podkladka pod sworzen2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 35.3429173529, perimeter: 47.1238898038
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a toroidal ring or washer with a donut-like shape, featuring a smooth outer curved surface and a hollow center, with cross-hatched texture patterns visible on portions of the inner and outer edges suggesting material or grip characteristics.
def model_34785_dc3b83fa_0032():
    """Model: podkladka pod sworzen1 v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.2654824574, perimeter: 50.2654824574
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore and a mesh-textured or perforated upper rim section, featuring a smooth cylindrical body with what appears to be internal ribbing or surface detailing.
def model_34913_d23e2a24_0001():
    """Model: Component26"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8748239558, perimeter: 10.2730079772
            with BuildLine():
                CenterArc((3, -52.5), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3, -52.5), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a rectangular enclosure or structural frame with a trapezoidal top section, featuring dark exterior panels, internal cross-bracing support members, and transparent or semi-transparent window panels on the sides and roof for visibility into the interior cavity.
def model_34913_d23e2a24_0002():
    """Model: Component24"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.3405322206, perimeter: 27.1314153236
            with BuildLine():
                Line((-2, -49.5), (2, -49.5))
                Line((-2, -55.5), (-2, -49.5))
                Line((2, -55.5), (-2, -55.5))
                Line((2, -49.5), (2, -55.5))
            make_face()
            with BuildLine():
                CenterArc((0, -54.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -50.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -52.5), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a cylindrical rod or tube with a simple, uniform circular cross-section and a slight taper or chamfer at the top end.
def model_34913_d23e2a24_0003():
    """Model: Component28"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((5, -52.5)):
                Circle(0.635)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a dual-cavity mounting bracket with a diamond or rotated-square overall shape, featuring two large circular holes for fastener passage and internal ribbed reinforcement for structural support.
def model_34913_d23e2a24_0004():
    """Model: Component19"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 99.6920447165, perimeter: 73.904865662
            with BuildLine():
                CenterArc((-13.5432968249, 10.6844359055), 1.8, -166.9385623072, 332.1155868337)
                Line((-15.2967277503, 10.2776435877), (-18.1432968249, 10.2776435877))
                Line((-18.1432968249, 10.2776435877), (-18.1432968249, 4.6844359055))
                Line((-18.1432968249, 4.6844359055), (-6.1432968249, 4.6844359055))
                Line((-6.1432968249, 4.6844359055), (-6.1432968249, 14.6844359055))
                Line((-6.1432968249, 14.6844359055), (-18.1432968249, 14.6844359055))
                Line((-18.1432968249, 14.6844359055), (-18.1432968249, 11.1449360819))
                Line((-15.2833944048, 11.1449360819), (-18.1432968249, 11.1449360819))
            make_face()
            with BuildLine():
                CenterArc((-16, 6.5894359055), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.1432968249, 6.5894359055), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.1432968249, 10.6844359055), 1.42875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a streamlined aerodynamic fairing or shroud with an elongated hexagonal cross-section, featuring a curved top surface, internal structural ribs for reinforcement, and tapered ends designed to reduce drag or direct airflow.
def model_34913_d23e2a24_0005():
    """Model: Component23"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 194.7725633272, perimeter: 70.35634437
            with BuildLine():
                Line((-10, -60), (10, -60))
                Line((-10, -66), (-10, -60))
                Line((-3, -72), (-10, -66))
                Line((3, -72), (-3, -72))
                Line((10, -66), (3, -72))
                Line((10, -60), (10, -66))
            make_face()
            with BuildLine():
                CenterArc((8.095, -65), 0.395, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.095, -61), 0.395, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.095, -65), 0.395, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.095, -61), 0.395, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -69), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a rounded rectangular bar or rod with a simple cylindrical shape, featuring rounded ends and a uniform diameter throughout its length.
def model_34913_d23e2a24_0006():
    """Model: Component32"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            with Locations((-12, 3)):
                Circle(0.47625)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a long, rectangular metal channel or beam with a trapezoidal cross-section, featuring a slotted top surface and angled side flanges.
def model_34913_d23e2a24_0007():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 94.7332313023, perimeter: 73.9898226701
            with BuildLine():
                Line((16, -39), (16, -36))
                Line((16, -36), (-16, -36))
                Line((-16, -36), (-16, -39))
                Line((-16, -39), (16, -39))
            make_face()
            with BuildLine():
                CenterArc((0, -37.5), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a flat parallelogram or trapezoidal plate with a triangular internal diagonal partition or reinforcement rib running from one corner to an opposite edge, creating a triangulated structure for added rigidity.
def model_34913_d23e2a24_0008():
    """Model: Component33"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5.3202489279, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 419.5364878493, perimeter: 82.7778396684
            with BuildLine():
                Line((6.2973705339, 52.44), (6.2973705339, 28.791867215))
                Line((6.2973705339, 52.44), (-11.4434165152, 52.44))
                Line((-11.4434165152, 52.44), (-11.4434165152, 28.791867215))
                Line((-11.4434165152, 28.791867215), (6.2973705339, 28.791867215))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical rod or shaft with a simple, elongated tubular shape and slightly rounded ends, featuring no holes, slots, or flanges.
def model_34917_61633e20_0010():
    """Model: internal pipe v2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8482300165, perimeter: 16.9646003294
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube featuring two hemispherical end caps connected by a central cylindrical body with a recessed or hollowed interior section running along its length.
def model_35132_35c342c8_0004():
    """Model: limitador"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a cylindrical roller or spacer with a rounded hemispherical end on one side and a flat end on the other, featuring a knurled or textured surface along its body for grip.
def model_35143_6bdef095_0000():
    """Model: Eje rueda"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a mounting bracket or clamp with an elongated vertical body featuring a rectangular slot at the top and a circular hole at the bottom for fastening or attachment purposes.
def model_35143_6bdef095_0001():
    """Model: parte lateral"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.7817378309, perimeter: 12.4537655053
            with BuildLine():
                CenterArc((0, 0), 1, -170, 160)
                Line((0.984807753, -0.1736481777), (1.1789523177, 0.9274003626))
                CenterArc((0, 0), 1.5, 38.1896851042, 103.6206297916)
                Line((-0.984807753, -0.1736481777), (-1.1789523177, 0.9274003626))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 8.3465507238, perimeter: 12.6547262043
            with BuildLine():
                CenterArc((0, 0), 1.5, 38.1896851042, 103.6206297916)
                Line((1.1789523177, 0.9274003626), (1.7400040537, 4.1092828724))
                Line((-1.7400040537, 4.1092828724), (1.7400040537, 4.1092828724))
                Line((-1.1789523177, 0.9274003626), (-1.7400040537, 4.1092828724))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a ring or cylindrical band with a uniform circular cross-section, featuring a textured or knurled surface across its outer perimeter and a hollow center, commonly used as a spacer, bearing race, or cylindrical sleeve component.
def model_35143_6bdef095_0004():
    """Model: rueda"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.0424771932, perimeter: 40.2123859659
            with BuildLine():
                CenterArc((0, 0), 3.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)
    return part.part


# Description: This is a thin, flat parallelogram-shaped plate or panel with a tapered wedge-like profile, featuring a beveled or sloped edge that gradually reduces in thickness from one end to the other.
def model_35143_6bdef095_0005():
    """Model: parte para ensamblar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.1092828724, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.2599959463, perimeter: 25.9600162146
            with BuildLine():
                Line((-2, 2.5), (2, 2.5))
                Line((-2, -2.5), (-2, 2.5))
                Line((2, -2.5), (-2, -2.5))
                Line((2, 2.5), (2, -2.5))
            make_face()
            with BuildLine():
                Line((1.7400040537, -1), (-1.7400040537, -1))
                Line((1.7400040537, -1.5), (1.7400040537, -1))
                Line((-1.7400040537, -1.5), (1.7400040537, -1.5))
                Line((-1.7400040537, -1), (-1.7400040537, -1.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7400040537, perimeter: 7.9600162146
            with BuildLine():
                Line((-1.7400040537, -1), (-1.7400040537, -1.5))
                Line((-1.7400040537, -1.5), (1.7400040537, -1.5))
                Line((1.7400040537, -1.5), (1.7400040537, -1))
                Line((1.7400040537, -1), (-1.7400040537, -1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform diameter, tapered or rounded ends, and a slight 3D perspective showing its cylindrical geometry.
def model_35145_a3d7363c_0004():
    """Model: knee block"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, each_side=16.5
        extrude(amount=16.5, both=True)
    return part.part


# Description: This is a cylindrical pipe or tube with a uniform diameter, closed at one end and open at the other, featuring a slightly textured or ribbed surface finish along its length.
def model_35149_f50fea8a_0005():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a curved pipe or duct connector with an angular bend, featuring a streamlined blue finish with dark reinforced ends and internal ribbed or corrugated structural supports running along its length.
def model_35149_f50fea8a_0008():
    """Model: Component13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0307123393, perimeter: 1.1947841001
            with BuildLine():
                CenterArc((0.1812934785, -0.0475139854), 0.0125, -4.7801960008, 9.5603920016)
                Line((0.19375, -0.048555653), (0.19375, -0.1375))
                CenterArc((0.225, -0.1375), 0.03125, 180, 180)
                Line((0.25625, 0), (0.25625, -0.1375))
                CenterArc((0.225, 0), 0.03125, 0, 85.2198090673)
                Line((0.0041855178, 0.0498245064), (0.2276041662, 0.0311413041))
                CenterArc((0, 0), 0.05, 85.198130649, 189.5820653518)
                Line((0.1792173897, -0.0351875968), (0.0041666703, -0.0498260861))
                CenterArc((0.1812934785, -0.0475139854), 0.0125, 90, 9.5603920016)
                CenterArc((0.1812934785, -0.0475139854), 0.0125, 4.7801960008, 85.2198039992)
            make_face()
            with BuildLine():
                CenterArc((0.225, -0.1375), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.225, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0125
        extrude(amount=0.0125)
    return part.part


# Description: This is a parallelogram-shaped flat plate or base with a trapezoidal profile, featuring a uniform thickness and beveled or angled edges along one side, designed as a thin structural component or mounting base.
def model_35154_61b67282_0000():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -15.4416573868, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 107.03450463, perimeter: 133.91508926
            with BuildLine():
                Line((7.6566, -16.2827861575), (-7.6566, -16.2827861575))
                Line((7.6566, 5.2827861575), (7.6566, -16.2827861575))
                Line((-7.6566, 5.2827861575), (7.6566, 5.2827861575))
                Line((-7.6566, -16.2827861575), (-7.6566, 5.2827861575))
            make_face()
            with BuildLine():
                Line((6.6566, 2.8827861575), (-6.6566, 2.8827861575))
                Line((6.6566, -13.8827861575), (6.6566, 2.8827861575))
                Line((-6.6566, -13.8827861575), (6.6566, -13.8827861575))
                Line((-6.6566, 2.8827861575), (-6.6566, -13.8827861575))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 223.2034173442, perimeter: 60.15754463
            with BuildLine():
                Line((-6.6566, 2.8827861575), (-6.6566, -13.8827861575))
                Line((-6.6566, -13.8827861575), (6.6566, -13.8827861575))
                Line((6.6566, -13.8827861575), (6.6566, 2.8827861575))
                Line((6.6566, 2.8827861575), (-6.6566, 2.8827861575))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a hollow cylindrical cup or container with an open top and closed bottom, featuring a slightly tapered or curved sidewall that widens toward the upper rim.
def model_35166_562b126c_0002():
    """Model: Tail Cap Button Extension"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3631681108, perimeter: 2.1362830044
            Circle(0.34)
        # OneSide extrude, distance=0.575
        extrude(amount=0.575)
    return part.part


# Description: This is a cylindrical tube or sleeve with a hollow interior, featuring rounded ends and a uniform smooth cylindrical body with slight beveled or curved edges at the top.
def model_35166_562b126c_0007():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0224874499, perimeter: 13.8764147509
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.222
        extrude(amount=8.222)
    return part.part


# Description: This is a shallow, elongated elliptical dish or bowl with a curved bottom, featuring radial reinforcing ribs that extend from the center to the perimeter, and a raised rim flange around the outer edge.
def model_35166_562b126c_0012():
    """Model: Lens"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: These are two parallel elongated metal bars or rails with hexagonal end caps and a central groove or channel running along their length, appearing to be guide rails or linear motion components.
def model_35415_31c21951_0002():
    """Model: 7os"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 27 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 259.8, perimeter: 128.6
            with BuildLine():
                Line((-40, 83.8), (-31, 83.8))
                Line((-31, 87.3), (-31, 83.8))
                Line((-55, 87.3), (-31, 87.3))
                Line((-55, 83.8), (-55, 87.3))
                Line((-46, 83.8), (-55, 83.8))
                Line((-46, 68.5), (-46, 83.8))
                Line((-46, 68.5), (-55, 68.5))
                Line((-55, 65), (-55, 68.5))
                Line((-31, 65), (-55, 65))
                Line((-31, 68.5), (-31, 65))
                Line((-40, 68.5), (-31, 68.5))
                Line((-40, 83.8), (-40, 68.5))
            make_face()
            # Profile area: 259.8, perimeter: 128.6
            with BuildLine():
                Line((40, 83.8), (40, 68.5))
                Line((40, 68.5), (31, 68.5))
                Line((31, 68.5), (31, 65))
                Line((31, 65), (55, 65))
                Line((55, 65), (55, 68.5))
                Line((46, 68.5), (55, 68.5))
                Line((46, 68.5), (46, 83.8))
                Line((46, 83.8), (55, 83.8))
                Line((55, 83.8), (55, 87.3))
                Line((55, 87.3), (31, 87.3))
                Line((31, 87.3), (31, 83.8))
                Line((40, 83.8), (31, 83.8))
            make_face()
        # OneSide extrude, distance=500
        extrude(amount=500)
    return part.part


# Description: This is a cylindrical tube or sleeve with a smooth, hollow tubular body and rounded ends, featuring a simple geometric design with no visible holes, slots, or flanges.
def model_35580_2ab34839_0003():
    """Model: Smokestack_4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 549.7787143782, perimeter: 219.9114857513
            with BuildLine():
                CenterArc((-200, 500), 20, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-200, 500), 15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=140
        extrude(amount=140)
    return part.part


# Description: This is a segmented cylindrical housing or shroud with a ribbed/finned upper surface and vertical slot-like openings along its lower section, featuring a curved, fan-like or turbine-type geometry.
def model_35962_dbbd6e18_0003():
    """Model: toothed wheel v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 101 constraints, 48 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34.7053442814, perimeter: 36.0397539123
            with BuildLine():
                Line((-2.9945923214, -2.093506426), (-2.6676622505, -1.664361107))
                Line((-2.9945923214, -2.093506426), (-2.8770352692, -2.2553098273))
                Line((-2.8770352692, -2.2553098273), (-2.3676766551, -2.0769274347))
                Line((-2.3676766551, -2.0769274347), (-2.3547014482, -2.0768081862))
                Line((-2.2194530441, -2.2241440921), (-2.3547014482, -2.0768081862))
                Line((-2.4414672265, -2.7158337085), (-2.2194530441, -2.2241440921))
                Line((-2.4414672265, -2.7158337085), (-2.2905253082, -2.8470455163))
                Line((-2.2905253082, -2.8470455163), (-1.8343488297, -2.5586542956))
                Line((-1.8343488297, -2.5586542956), (-1.8353594185, -2.5572108581))
                Line((-1.6704340547, -2.6703462831), (-1.8353594185, -2.5572108581))
                Line((-1.7761519304, -3.1993762509), (-1.6704340547, -2.6703462831))
                Line((-1.7761519304, -3.1993762509), (-1.5995624092, -3.2932705649))
                Line((-1.5995624092, -3.2932705649), (-1.2199516135, -2.9096534127))
                Line((-1.1932383506, -2.8748733868), (-1.2199516135, -2.9096534127))
                Line((-1.0070900802, -2.9480090238), (-1.1932383506, -2.8748733868))
                Line((-0.9910925645, -3.4872613354), (-1.0070900802, -2.9480090238))
                Line((-0.9910925645, -3.4872613354), (-0.7979073964, -3.5390251452))
                Line((-0.7979073964, -3.5390251452), (-0.5143210836, -3.079846227))
                Line((-0.5158621561, -3.0789918869), (-0.5143210836, -3.079846227))
                Line((-0.3180329151, -3.1083788126), (-0.5158621561, -3.0789918869))
                Line((-0.1811400387, -3.6302114643), (-0.3180329151, -3.1083788126))
                Line((-0.1811400387, -3.6302114643), (0.0187381297, -3.6371913638))
                Line((0.0187381297, -3.6371913638), (0.1917633619, -3.1259881314))
                Line((0.1917633619, -3.1259881314), (0.1996577278, -3.1156901122))
                Line((0.3990272381, -3.0998219565), (0.1996577278, -3.1156901122))
                Line((0.6497983642, -3.5774858743), (0.3990272381, -3.0998219565))
                Line((0.6497983642, -3.5774858743), (0.8461238038, -3.5393240747))
                Line((0.8461238038, -3.5393240747), (0.8997187044, -3.0023007397))
                Line((0.8997187044, -3.0023007397), (0.8979590796, -3.0022084256))
                Line((1.0886492039, -2.9418985882), (0.8979590796, -3.0022084256))
                Line((1.4404440842, -3.3509087816), (1.0886492039, -2.9418985882))
                Line((1.4404440842, -3.3509087816), (1.6231531784, -3.2695614517))
                Line((1.6231531784, -3.2695614517), (1.5545704798, -2.7342457606))
                Line((1.5545704798, -2.7342457606), (1.5454847686, -2.7273530014))
                Line((1.7177207558, -2.6256929566), (1.5454847686, -2.7273530014))
                Line((2.1525064304, -2.945083616), (1.7177207558, -2.6256929566))
                Line((2.1525064304, -2.945083616), (2.3122335347, -2.8247206096))
                Line((2.3122335347, -2.8247206096), (2.1249887771, -2.3185527753))
                Line((2.1249887771, -2.3185527753), (2.123366769, -2.3192411728))
                Line((2.2683198248, -2.1814420015), (2.123366769, -2.3192411728))
                Line((2.7638092362, -2.394841203), (2.2683198248, -2.1814420015))
                Line((2.7638092362, -2.394841203), (2.8923667601, -2.2416323121))
                Line((2.8923667601, -2.2416323121), (2.5960580854, -1.7905584323))
                Line((2.5960580854, -1.7905584323), (2.5928033925, -1.7779974933))
                Line((2.703043242, -1.6111227631), (2.5928033925, -1.7779974933))
                Line((3.2338376673, -1.7075916915), (2.703043242, -1.6111227631))
                Line((3.2338376673, -1.7075916915), (3.3246357686, -1.529390384))
                Line((3.3246357686, -1.529390384), (2.9344519213, -1.1565324472))
                Line((2.9344519213, -1.1565324472), (2.9332958436, -1.1578622163))
                Line((3.0031716064, -0.9704659043), (2.9332958436, -1.1578622163))
                Line((3.5420625921, -0.9450595746), (3.0031716064, -0.9704659043))
                Line((3.5420625921, -0.9450595746), (3.590446972, -0.7510004265))
                Line((3.590446972, -0.7510004265), (3.1263887253, -0.4754710823))
                Line((3.1263887253, -0.4754710823), (3.1169038644, -0.471286951))
                Line((3.1428337179, -0.2729749678), (3.1169038644, -0.471286951))
                Line((3.6621977819, -0.1269957053), (3.1428337179, -0.2729749678))
                Line((3.6621977819, -0.1269957053), (3.6656882633, 0.0729738367))
                Line((3.6656882633, 0.0729738367), (3.151543183, 0.2370509898))
                Line((3.151543183, 0.2370509898), (3.1510870397, 0.2353490101))
                Line((3.1317418231, 0.434411218), (3.1510870397, 0.2353490101))
                Line((3.6049564308, 0.6934805352), (3.1317418231, 0.434411218))
                Line((3.6049564308, 0.6934805352), (3.563374092, 0.8891100583))
                Line((3.563374092, 0.8891100583), (3.0254971882, 0.9333244466))
                Line((3.0254971882, 0.9333244466), (3.0135952442, 0.9384929998))
                Line((2.9499665907, 1.1281015292), (3.0135952442, 0.9384929998))
                Line((3.3527748226, 1.4869810416), (2.9499665907, 1.1281015292))
                Line((3.3527748226, 1.4869810416), (3.268251169, 1.6682426017))
                Line((3.268251169, 1.6682426017), (2.7342139421, 1.5903278015))
                Line((2.7342139421, 1.5903278015), (2.734550062, 1.5885981123))
                Line((2.6298995681, 1.7590336547), (2.734550062, 1.5885981123))
                Line((2.9416535265, 2.1993272449), (2.6298995681, 1.7590336547))
                Line((2.9416535265, 2.1993272449), (2.8185212296, 2.356929398))
                Line((2.8185212296, 2.356929398), (2.3156983587, 2.1608793119))
                Line((2.3156983587, 2.1608793119), (2.3112083764, 2.1503959757))
                Line((2.1709004129, 2.2929220273), (2.3112083764, 2.1503959757))
                Line((2.3756196301, 2.7920603029), (2.1709004129, 2.2929220273))
                Line((2.3756196301, 2.7920603029), (2.2201904355, 2.917924383))
                Line((2.2201904355, 2.917924383), (1.7743565558, 2.613788513))
                Line((1.7743565558, 2.613788513), (1.7754169042, 2.6123812238))
                Line((1.6066436392, 2.7196919176), (1.7754169042, 2.6123812238))
                Line((1.6938342348, 3.2520891153), (1.6066436392, 2.7196919176))
                Line((1.6938342348, 3.2520891153), (1.5140754229, 3.339763346))
                Line((1.5140754229, 3.339763346), (1.1480839213, 2.9431316573))
                Line((1.1480839213, 2.9431316573), (1.1366834774, 2.9369348765))
                Line((0.9480962065, 3.0035294803), (1.1366834774, 2.9369348765))
                Line((0.9132888018, 3.5418949887), (0.9480962065, 3.0035294803))
                Line((0.9132888018, 3.5418949887), (0.718414786, 3.5868852002))
                Line((0.718414786, 3.5868852002), (0.4510263394, 3.1180889818))
                Line((0.4510263394, 3.1180889818), (0.4525962892, 3.1172889449))
                Line((0.2538619715, 3.1397538278), (0.4525962892, 3.1172889449))
                Line((0.0988407896, 3.6564911008), (0.2538619715, 3.1397538278))
                Line((0.0988407896, 3.6564911008), (-0.1011592134, 3.6564911008))
                Line((-0.1011592134, 3.6564911008), (-0.2748492232, 3.0775244014))
                CenterArc((-0.0048741024, -0.0400765668), 3.1292686626, 94.9492997975, 90.4726576245)
                Line((-3.6021096007, -0.5781571937), (-3.1201418738, -0.3357606462))
                Line((-3.6021096007, -0.5781571937), (-3.5673799647, -0.7751187473))
                Line((-3.5673799647, -0.7751187473), (-3.0313737809, -0.8380778346))
                Line((-3.0313737809, -0.8380778346), (-3.0224877336, -0.8309295173))
                Line((-2.9655150832, -1.0226431503), (-3.0224877336, -0.8309295173))
                Line((-3.3806026496, -1.3672462384), (-2.9655150832, -1.0226431503))
                Line((-3.3806026496, -1.3672462384), (-3.3024564227, -1.5513472119))
                Line((-3.3024564227, -1.5513472119), (-2.7660253296, -1.4921175057))
                Line((-2.7663008794, -1.4903771397), (-2.7660253296, -1.4921175057))
                Line((-2.6676622505, -1.664361107), (-2.7663008794, -1.4903771397))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or washer with a thick, rounded cross-section and a large central hole, featuring radial grooves or ridges running across its entire outer surface.
def model_35968_5488b3e5_0005():
    """Model: podkladka (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.243915399, perimeter: 16.650441064
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is an oval or egg-shaped container with a rounded body, featuring a small rectangular spout or nozzle protruding from the top, and displaying a textured ribbed or lined surface pattern across its exterior.
def model_36088_1ea9c8a9_0005():
    """Model: Driven Gearwheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0724483104, perimeter: 9.7341573331
            with BuildLine():
                CenterArc((0.9291949692, 1.3212388484), 1.045, 158.1892661923, 12.3195462738)
                CenterArc((0, 0), 1.497, 93.8877666439, 352.2244667122)
                CenterArc((-0.9291949692, 1.3212388484), 1.045, 9.491187534, 12.3195462738)
                Line((-0.041, 1.7095), (0.041, 1.7095))
            make_face()
        # Symmetric extrude, each_side=0.175
        extrude(amount=0.175, both=True)
    return part.part


# Description: This is a rounded, bulbous container or vessel with an overall egg-like shape, featuring a cylindrical neck or spout protruding from the top, and characterized by smooth curved surfaces with subtle ribbed or linear surface detailing throughout.
def model_36088_1ea9c8a9_0010():
    """Model: Driving Gearwheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5830682078, perimeter: 4.7491245918
            with BuildLine():
                CenterArc((0.6281554956, 0.6081726507), 0.73, 155.1024915844, 17.9601323071)
                CenterArc((0, 0), 0.703, 97.8898369029, 344.2203261943)
                CenterArc((-0.6281554956, 0.6081726507), 0.73, 6.9373761085, 17.9601323071)
                Line((-0.034, 0.9155), (0.034, 0.9155))
            make_face()
        # Symmetric extrude, each_side=0.225
        extrude(amount=0.225, both=True)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or washer with a hollow circular center and radial ribbing or fin patterns covering its outer surface for structural reinforcement or aesthetic purposes.
def model_36088_1ea9c8a9_0014():
    """Model: Spring Shim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3744467859, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a rubber or elastomer O-ring with a circular/toroidal shape, featuring a uniform cross-section and smooth surface texture, commonly used as a sealing gasket in mechanical applications.
def model_36088_1ea9c8a9_0015():
    """Model: Shim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2120575041, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a mounting bracket or clamp assembly with a vertical rectangular post extending upward from a wider base, featuring internal channels or slots in the base for securing or aligning components.
def model_36088_1ea9c8a9_0016():
    """Model: Blocking Element"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7474687701, perimeter: 6.6075999254
            with BuildLine():
                Line((-0.3, -0.3), (0.3, -0.3))
                Line((0.3, -0.3), (0.3, 0.45))
                Line((0.3, 0.45), (0.1500000022, 0.45))
                Line((0.1500000022, 0.45), (0.1500000022, 1.8))
                Line((-0.1500000022, 1.8), (0.1500000022, 1.8))
                Line((-0.1500000022, 0.45), (-0.1500000022, 1.8))
                Line((-0.3, 0.45), (-0.1500000022, 0.45))
                Line((-0.3, -0.3), (-0.3, 0.45))
            make_face()
            with BuildLine():
                Line((0.15, 0.1322875656), (0.15, -0.1322875656))
                CenterArc((0, 0), 0.2, -138.5903778907, 97.1807557815)
                Line((-0.15, 0.1322875656), (-0.15, -0.1322875656))
                CenterArc((0, 0), 0.2, 41.4096221093, 97.1807557815)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a toroidal or ring-shaped component with a large central oval hole and radial fins or grooves extending outward across its entire surface, likely designed for heat dissipation or structural reinforcement.
def model_36088_1ea9c8a9_0018():
    """Model: Component50"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3253594007, perimeter: 7.0685834706
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a mummy-style sleeping bag with a tapered, elongated oval shape that narrows toward the feet, featuring a hood at the head end and a quilted/segmented insulation pattern throughout its body.
def model_36194_c9cfd107_0001():
    """Model: Component11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.001483837, perimeter: 0.1671247689
            with BuildLine():
                Line((-0.00565, 0), (-0.03125, 0))
                CenterArc((0, 0), 0.03125, 180, 180)
                Line((0.00565, 0), (0.03125, 0))
                CenterArc((0, 0), 0.00565, -180, 180)
            make_face()
            # Profile area: 0.0105579746, perimeter: 0.5736247599
            with BuildLine():
                CenterArc((0, 0), 0.00565, 0, 180)
                Line((0.00565, 0), (0.03125, 0))
                Line((0.03125, 0), (0.03125, 0.15))
                CenterArc((0, 0.15), 0.03125, 0, 180)
                Line((-0.03125, 0), (-0.03125, 0.15))
                Line((-0.00565, 0), (-0.03125, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0.15), 0.00565, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.1094), 0.00565, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.0406), 0.00565, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0125
        extrude(amount=0.0125)
    return part.part


# Description: This is a cylindrical rod or tube with a uniform diameter and smooth surface, featuring a slightly tapered or rounded end at the top and a clean, straight body extending downward at an angle.
def model_36194_c9cfd107_0002():
    """Model: Component13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0000357196, perimeter: 0.0723343943
            with BuildLine():
                CenterArc((0, 0), 0.00625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0052623764, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical sleeve or tube with a polygonal (multi-faceted) top end cap and vertical slot or groove running along its length.
def model_36194_c9cfd107_0005():
    """Model: Component16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0001227185, perimeter: 0.0392699082
            Circle(0.00625)
        # OneSide extrude, distance=0.0375
        extrude(amount=0.0375)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform hollow circular cross-section, featuring a simple straight tubular shape with no additional features, holes, or flanges.
def model_36194_c9cfd107_0011():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0002775911, perimeter: 0.0590619419
            Circle(0.0094)
        # OneSide extrude, distance=0.2375
        extrude(amount=0.2375)
    return part.part


# Description: This is a tie rod or control arm featuring a long cylindrical shaft with textured spherical ball joint ends on both sides for articulated suspension connections.
def model_36194_c9cfd107_0012():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0023952476, perimeter: 0.4989086089
            with BuildLine():
                CenterArc((0, 0), 0.0125, -150, 300)
                Line((-0.0108253175, 0.00625), (-0.1356521779, 0.00625))
                CenterArc((-0.15, 0), 0.01565, 23.5382389781, 312.9235220439)
                Line((-0.0108253175, -0.00625), (-0.1356521779, -0.00625))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.00625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.15, 0), 0.0094, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.006
        extrude(amount=0.006)
    return part.part


# Description: This is a toggle clamp handle featuring an elongated oval loop with a textured grip surface and a solid cylindrical shaft extending from the base, designed for manual operation and secure gripping.
def model_36194_c9cfd107_0013():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0031316344, perimeter: 0.523068405
            with BuildLine():
                CenterArc((0, 0), 0.0094, 131.6741644997, 276.6516710006)
                Line((0.00625, 0.0070212178), (0.00625, 0.0443245014))
                CenterArc((0, 0.0813), 0.0375, -80.4059317731, 340.8118635463)
                Line((-0.00625, 0.0070212178), (-0.00625, 0.0443245014))
            make_face()
            with BuildLine():
                CenterArc((0, 0.0813), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.00365, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.006
        extrude(amount=0.006)
    return part.part


# Description: This is a flat parallelogram plate with a small elliptical or oval hole near its center and diagonal cross-bracing or reinforcement lines visible on its surface.
def model_36268_3c96c142_0003():
    """Model: rear grille v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 105.1846313023, perimeter: 47.1698226701
            with BuildLine():
                Line((6.985, -3.81), (6.985, 3.81))
                Line((6.985, 3.81), (-6.985, 3.81))
                Line((-6.985, 3.81), (-6.985, -3.81))
                Line((-6.985, -3.81), (6.985, -3.81))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.041275
        extrude(amount=0.041275)
    return part.part


# Description: This is a long, thin rectangular bar or plate with a parallelogram profile, featuring a beveled or angled edge on one end and a flat, elongated body with subtle surface details.
def model_36268_3c96c142_0004():
    """Model: top panel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.3548, perimeter: 33.02
            with BuildLine():
                Line((-7.62, 0.635), (7.62, 0.635))
                Line((-7.62, -0.635), (-7.62, 0.635))
                Line((7.62, -0.635), (-7.62, -0.635))
                Line((7.62, 0.635), (7.62, -0.635))
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a rectangular extrusion or channel with a long, slender profile featuring a central slot or groove running along its length, typical of an aluminum structural beam or rail component.
def model_36268_3c96c142_0006():
    """Model: side panel v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.2903, perimeter: 20.32
            with BuildLine():
                Line((0.635, -4.445), (0.635, 4.445))
                Line((0.635, 4.445), (-0.635, 4.445))
                Line((-0.635, 4.445), (-0.635, -4.445))
                Line((-0.635, -4.445), (0.635, -4.445))
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a dark blue/gray finish and a slight 3D beveled edge, featuring a slanted rectangular form typical of a trim piece, deflector, or structural flange.
def model_36268_3c96c142_0007():
    """Model: digital display v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.4516, perimeter: 12.7
            with BuildLine():
                Line((2.54, -0.635), (2.54, 0.635))
                Line((2.54, 0.635), (-2.54, 0.635))
                Line((-2.54, 0.635), (-2.54, -0.635))
                Line((-2.54, -0.635), (2.54, -0.635))
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped panel or plate with a slight 3D depth, featuring clean edges and a uniform dark blue color with subtle shading that suggests a beveled or chamfered edge detail along one side.
def model_36268_3c96c142_0008():
    """Model: display glass v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.903216, perimeter: 11.684
            with BuildLine():
                Line((2.413, -0.508), (2.413, 0.508))
                Line((2.413, 0.508), (-2.413, 0.508))
                Line((-2.413, 0.508), (-2.413, -0.508))
                Line((-2.413, -0.508), (2.413, -0.508))
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a cylindrical filter or strainer component with a solid circular base and end cap, featuring a perforated or mesh-textured curved side surface that tapers slightly toward the top, designed to allow fluid or air passage while filtering out particles.
def model_36268_3c96c142_0010():
    """Model: light element v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a thin, flat rectangular plate or tray with a slightly tapered or wedge-shaped profile, featuring diagonal surface divisions or scoring lines on the top face.
def model_36283_ee4931a7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 132, perimeter: 56
            with BuildLine():
                Line((11, -3), (11, 3))
                Line((11, 3), (-11, 3))
                Line((-11, 3), (-11, -3))
                Line((-11, -3), (11, -3))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a long, slender rectangular beam or rail with a uniform cross-section, featuring chamfered or beveled edges at both ends and a slightly curved or crowned top surface.
def model_36303_82ed629e_0001():
    """Model: gorny slupek oscieznicy wrot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.9999992624, perimeter: 41.9999999404
            with BuildLine():
                Line((-19, -3.5), (-19, -2.5000000373))
                Line((1, -3.5), (-19, -3.5))
                Line((1.0000000149, -2.5000000373), (1, -3.5))
                Line((-19, -2.5000000373), (1.0000000149, -2.5000000373))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a flat rectangular panel or plate with a parallelogram shape, featuring a simple planar geometry with subtle beveled or flanged edges on the sides, designed as a basic structural or mounting component.
def model_36409_3adb6194_0001():
    """Model: BT Indicator"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.6000000417, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0235999999, perimeter: 1.2599999933
            with BuildLine():
                Line((-0.295, -2.6200000522), (-0.295, -2.6600000522))
                Line((-0.295, -2.6600000522), (0.2949999993, -2.6600000522))
                Line((0.2949999993, -2.6600000522), (0.294999994, -2.6200000522))
                Line((0.294999994, -2.6200000522), (-0.295, -2.6200000522))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a bracket or connector component with an angular, bent shape featuring two circular mounting holes at each end and a curved, tapered body with ribbed reinforcement sections along its length.
def model_36413_fb06800c_0004():
    """Model: Clamp Elbow Bow Left v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 26 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.2092848166, perimeter: 20.2966620017
            with BuildLine():
                Line((-0.8, -2.2), (0.8, -2.2))
                Line((0.8, -1.5305028665), (0.8, -2.2))
                CenterArc((1.4, -1.5305028665), 0.6, 84.9003110858, 95.0996889142)
                Line((1.4533333333, -0.9328779377), (4.3933333333, -1.1952498577))
                CenterArc((4.5, 0), 1.2, 95.0996889142, 169.8006221716)
                Line((-0.0711111111, 0.7968332384), (4.3933333333, 1.1952498577))
                CenterArc((0, 0), 0.8, -180, 275.0996889142)
                Line((-0.8, 0), (-0.8, -2.2))
            make_face()
            # Profile area: 1.5079644737, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.8, -180, 275.0996889142)
                CenterArc((0, 0), 0.8, 95.0996889142, 84.9003110858)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.0212385966, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((4.5, 0), 1.2, 95.0996889142, 169.8006221716)
                CenterArc((4.5, 0), 1.2, -95.0996889142, 190.1993778284)
            make_face()
            with BuildLine():
                CenterArc((4.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25)
    return part.part


# Description: This is a cylindrical housing or chamber with a domed/curved top and a flat circular base, featuring internal ribbed or latticed structural elements visible through the transparent mesh rendering.
def model_36413_fb06800c_0006():
    """Model: Clamp Hinge v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)
    return part.part


# Description: This is a polygonal geometric solid with an irregular polyhedral shape featuring multiple faceted surfaces in varying shades of blue and dark gray, creating a complex angular form with no obvious functional features like holes, slots, or flanges—appearing to be an abstract geometric study or decorative object.
def model_36413_fb06800c_0009():
    """Model: Clamp Tee v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.1316, perimeter: 5.84
            with BuildLine():
                Line((-0.73, 0.73), (0.73, 0.73))
                Line((-0.73, -0.73), (-0.73, 0.73))
                Line((0.73, -0.73), (-0.73, -0.73))
                Line((0.73, 0.73), (0.73, -0.73))
            make_face()
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)
    return part.part


# Description: This is a toroidal (donut-shaped) spacer or bushing with a large central hole, featuring a curved outer surface and mesh-like surface texture, commonly used as a cylindrical component for alignment, spacing, or bearing applications.
def model_36436_362a4413_0024():
    """Model: Connector Wingscrew v3 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4064435496, perimeter: 3.6128315516
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a shoe insole or footbed with an elongated, curved anatomical shape featuring blue mesh ventilation panels and textured grip surfaces on the dark gray upper and lower layers.
def model_36436_362a4413_0028():
    """Model: Connector Plate v2 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2998484086, perimeter: 11.2853975489
            with BuildLine():
                CenterArc((0.8499076198, -0.0125314741), 0.55, -90.8447371627, 179.9999987926)
                Line((0.8580162322, 0.5374087503), (-0.8417990189, 0.5624716986))
                CenterArc((-0.8499076198, 0.0125314741), 0.55, 89.1552628373, 180)
                Line((-0.8580162207, -0.5374087505), (0.8417990189, -0.5624716986))
            make_face()
            with BuildLine():
                CenterArc((-0.8499076198, 0.0125314741), 0.235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8499076198, -0.0125314741), 0.235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve with an open top, featuring a tilted, elliptical opening and vertical ribbed or corrugated surface texture throughout its body.
def model_36445_67816b83_0000():
    """Model: plastic washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a cylindrical sleeve or barrel with a curved, tapered shape, featuring vertical ribbing or fluting along its exterior surface and an open top.
def model_36445_67816b83_0002():
    """Model: wire housing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.149225651, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered, curved profile and ribbed or fluted surface texture running vertically along its walls.
def model_36445_67816b83_0005():
    """Model: metal washer 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0687223393, perimeter: 5.4977871438
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a tapered end cap, featuring longitudinal venting slots or cooling fins along its body for heat dissipation.
def model_36451_1a7f9437_0000():
    """Model: Crankshaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)
    return part.part


# Description: This is a cylindrical rod or shaft with spherical end caps (or ball joints) at both ends, featuring a dark blue cylindrical body with gray rounded terminal nodes, commonly used as a connector, linkage, or suspension component.
def model_36451_1a7f9437_0004():
    """Model: Displacement Piston Connecting Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.3495470802, perimeter: 16.3682571712
            with BuildLine():
                Line((-0.3, 3.9390227771), (-0.3, 0.4609772229))
                CenterArc((0, 0), 0.55, 123.0557311509, 293.8885376983)
                Line((0.3, 3.9390227771), (0.3, 0.4609772229))
                CenterArc((0, 4.4), 0.55, -56.9442688491, 293.8885376983)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 4.4), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a hollow center bore and multiple rectangular slots or windows cut through the walls along its length.
def model_36451_1a7f9437_0009():
    """Model: Small Bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5079644737, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.1
        extrude(amount=3.1)
    return part.part


# Description: This is a cylindrical sleeve or barrel component with a hollow tubular body featuring longitudinal ridges or grooves running along its length and two through-holes positioned on opposite sides near the ends.
def model_36451_1a7f9437_0011():
    """Model: Large Bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2672563597, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.6
        extrude(amount=4.6)
    return part.part


# Description: A flat rectangular plate or bar with a slightly tapered parallelogram shape, featuring a blue surface finish and dark beveled edges on the left side.
def model_36733_b0605a21_0000():
    """Model: Tail Wing 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.861348626, perimeter: 31.861348626
            with BuildLine():
                Line((6.9708625165, 23.5), (6.9708625165, 25.5))
                Line((6.9708625165, 25.5), (-6.9598117966, 25.5))
                Line((-6.9598117966, 25.5), (-6.9598117966, 23.5))
                Line((-6.9598117966, 23.5), (6.9708625165, 23.5))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a long tubular body, featuring a tapered rounded end cap at one end and a threaded connection point at the other end for firearm attachment.
def model_36816_5ba90dc9_0000():
    """Model: Untitled v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a hollow rectangular frame or box-like structural component with an open top surface, featuring parallel flanged sides and a closed bottom, resembling a tray or mounting bracket with a rectangular cutout.
def model_36918_2dee90be_0005():
    """Model: Base Box v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.96, perimeter: 179.2
            with BuildLine():
                Line((0, 0), (30, 0))
                Line((30, 0), (30, 15))
                Line((30, 15), (0, 15))
                Line((0, 15), (0, 0))
            make_face()
            with BuildLine():
                Line((0.1, 0.1), (29.9, 0.1))
                Line((0.1, 14.9), (0.1, 0.1))
                Line((29.9, 14.9), (0.1, 14.9))
                Line((29.9, 0.1), (29.9, 14.9))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a 3D rectangular frame or border with a hollow center, featuring a uniform dark gray extruded profile with beveled or angled edges that give it a three-dimensional appearance.
def model_36918_2dee90be_0007():
    """Model: Top Box v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.99, perimeter: 119.6
            with BuildLine():
                Line((-7.5, 7.5), (7.5, 7.5))
                Line((-7.5, -7.5), (-7.5, 7.5))
                Line((7.5, -7.5), (-7.5, -7.5))
                Line((7.5, 7.5), (7.5, -7.5))
            make_face()
            with BuildLine():
                Line((7.45, 7.45), (7.45, -7.45))
                Line((7.45, -7.45), (-7.45, -7.45))
                Line((-7.45, -7.45), (-7.45, 7.45))
                Line((-7.45, 7.45), (7.45, 7.45))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a flat metal bar or spacer with a elongated rectangular body and two circular holes near each end, commonly used as a connector, bracket, or mounting plate in mechanical assemblies.
def model_36918_2dee90be_0008():
    """Model: Support Arms v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.240259851, perimeter: 27.853232674
            with BuildLine():
                CenterArc((0, 0), 0.6000000089, 90, 180)
                Line((8.888, -0.6000000089), (0, -0.6000000089))
                CenterArc((8.899882483, 0), 0.6001176586, -91.1345452165, 182.2690904331)
                Line((0, 0.6000000089), (8.888, 0.6000000089))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.888, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a horizontal pipe or tube connector with two circular holes at each end for fastening or alignment purposes.
def model_36918_2dee90be_0010():
    """Model: Secondary Arm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.280909383, perimeter: 21.2543609559
            with BuildLine():
                Line((0, -0.6000000089), (5.636, -0.6000000089))
                CenterArc((5.5988511528, 0), 0.6011489396, -86.4570690353, 172.9141380706)
                Line((5.636, 0.6000000089), (0, 0.6000000089))
                CenterArc((0, 0), 0.6000000089, 90, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.636, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a circular disk or wheel with a dark rim and multiple triangular cutouts or apertures arranged around its face, featuring a textured or mesh-patterned outer edge that suggests a flanged or ribbed design for structural support.
def model_36953_bdaf025b_0005():
    """Model: kolo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 89.5893364009, perimeter: 77.7424222331
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                Line((3.7903384691, 1.8665157804), (1.8535533906, 3.8033008589))
                CenterArc((3.4367850785, 1.5129623898), 0.5, -90, 135)
                Line((3.4367850785, 1.0129623898), (2, 1.0129623898))
                CenterArc((2, 2.0129623898), 1, 180, 90)
                Line((1, 3.4497474683), (1, 2.0129623898))
                CenterArc((1.5, 3.4497474683), 0.5, 45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.8535533906, -3.8033008589), (3.7903384691, -1.8665157804))
                CenterArc((1.5, -3.4497474683), 0.5, -180, 135)
                Line((1, -3.4497474683), (1, -2.0129623898))
                CenterArc((2, -2.0129623898), 1, 90, 90)
                Line((3.4367850785, -1.0129623898), (2, -1.0129623898))
                CenterArc((3.4367850785, -1.5129623898), 0.5, -45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.7903384691, -1.8665157804), (-1.8535533906, -3.8033008589))
                CenterArc((-3.4367850785, -1.5129623898), 0.5, 90, 135)
                Line((-3.4367850785, -1.0129623898), (-2, -1.0129623898))
                CenterArc((-2, -2.0129623898), 1, 0, 90)
                Line((-1, -3.4497474683), (-1, -2.0129623898))
                CenterArc((-1.5, -3.4497474683), 0.5, -135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.7903384691, 1.8665157804), (-1.8535533906, 3.8033008589))
                CenterArc((-1.5, 3.4497474683), 0.5, 0, 135)
                Line((-1, 3.4497474683), (-1, 2.0129623898))
                CenterArc((-2, 2.0129623898), 1, -90, 90)
                Line((-3.4367850785, 1.0129623898), (-2, 1.0129623898))
                CenterArc((-3.4367850785, 1.5129623898), 0.5, 135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a hexagonal or octagonal geometric container or junction box with a faceted exterior design, featuring a hollow interior cavity accessible from the top and reinforced internal ribbing or structural supports.
def model_36953_bdaf025b_0007():
    """Model: nakretka 2mm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2410833199, perimeter: 3.0209387961
            with BuildLine():
                Line((0.6267949286, 0.200000003), (0.9732050953, 0.200000003))
                Line((0.9732050953, 0.200000003), (1.1464101786, 0.5000000075))
                Line((1.1464101786, 0.5000000075), (0.9732050953, 0.8000000119))
                Line((0.9732050953, 0.8000000119), (0.6267949286, 0.8000000119))
                Line((0.6267949286, 0.8000000119), (0.4535898452, 0.5000000075))
                Line((0.4535898452, 0.5000000075), (0.6267949286, 0.200000003))
            make_face()
            with BuildLine():
                CenterArc((0.8000000119, 0.5000000075), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a parallelogram-shaped flat plate or shim with a trapezoidal appearance, featuring a simple rectangular form with no holes or additional features, likely used as a spacer, wedge, or structural component.
def model_37040_ecbcd25e_0011():
    """Model: szyba drzwi v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 422.65, perimeter: 100.4
            with BuildLine():
                Line((10.7, -39.5), (0, -39.5))
                Line((10.7, 0), (10.7, -39.5))
                Line((0, 0), (10.7, 0))
                Line((0, -39.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a flat, rectangular plate with a parallelogram shape, characterized by slanted sides and no additional features such as holes, slots, or curves.
def model_37040_ecbcd25e_0027():
    """Model: szyba v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 495.36, perimeter: 102.6
            with BuildLine():
                Line((0, 38.4), (0, 0))
                Line((0, 0), (12.9, 0))
                Line((12.9, 0), (12.9, 38.4))
                Line((12.9, 38.4), (0, 38.4))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a wedge-shaped or trapezoidal prism component with a tapered form that narrows from a wider rectangular face on one end to a narrower edge on the other, featuring a clean geometric design with flat surfaces and angular edges.
def model_37040_ecbcd25e_0037():
    """Model: pomocnicze v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.501850447, perimeter: 15.0085
            with BuildLine():
                Line((1.1663342335, -1.1906840471), (0.265987194, 1.6728064974))
                Line((0.265987194, 1.6728064974), (-2.7355766837, 1.7013928201))
                Line((-2.7355766837, 1.7013928201), (-3.6902981401, -1.1444304054))
                Line((-3.6902981401, -1.1444304054), (-1.2787845721, -2.9318322074))
                Line((-1.2787845721, -2.9318322074), (1.1663342335, -1.1906840471))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: A straight cylindrical rod or pin with a tapered or pointed end, rendered in dark gray/black.
def model_37040_ecbcd25e_0038():
    """Model: coś v4 (7)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5309, perimeter: 80.1287003555
            with BuildLine():
                Line((0, -38), (0, -37))
                Line((12.5309, -1), (0, -38))
                Line((12.5309, 0), (12.5309, -1))
                Line((0, -37), (12.5309, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with a hollow central bore, featuring a smooth curved body with flat ends and what appears to be internal ribbing or reinforcement structures visible through the semi-transparent rendering.
def model_37267_b2be4b50_0000():
    """Model: o (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((-37.5, -37.5), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-37.5, -37.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform diameter, featuring a straight, elongated design with slightly tapered or rounded ends.
def model_37267_b2be4b50_0001():
    """Model: pivot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((70, -20)):
                Circle(1.5)
        # OneSide extrude, distance=90
        extrude(amount=90)
    return part.part


# Description: This is a long, rectangular extrusion or beam with a hexagonal cross-section, featuring a flat top surface with two longitudinal slots or grooves running along its length.
def model_37267_b2be4b50_0008():
    """Model: beam (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 342.9314165294, perimeter: 159.4247779608
            with BuildLine():
                Line((70, -85), (0, -85))
                Line((70, -80), (70, -85))
                Line((0, -80), (70, -80))
                Line((0, -85), (0, -80))
            make_face()
            with BuildLine():
                CenterArc((35, -82.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a long, slender extruded structural member with a tapered diamond or rhombus cross-section, featuring a hollow core and pointed ends, commonly used as a reinforcing beam or trim component in engineering applications.
def model_37267_b2be4b50_0009():
    """Model: beam (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 468.75, perimeter: 146.2132034356
            with BuildLine():
                Line((-35, 115), (35, 115))
                Line((35, 115), (27.5, 122.5))
                Line((27.5, 122.5), (-27.5, 122.5))
                Line((-35, 115), (-27.5, 122.5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a long, slender tapered tube or shaft with a pointed conical tip at one end and a gradually narrowing profile along its length, resembling a lance, spear, or aerodynamic probe.
def model_37267_b2be4b50_0012():
    """Model: beam 45 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 454.5859044853, perimeter: 139.3491534303
            with BuildLine():
                Line((-45.5006076587, 115.1059940591), (0.0196257263, 160.6262274441))
                Line((-45.5006076587, 115.1059940591), (-40.1973067998, 109.8026932002))
                Line((-40.1973067998, 109.8026932002), (0, 150))
                Line((0.0196257263, 160.6262274441), (0, 150))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a hollow interior, featuring a solid dark sidewall and an open top with fine mesh screening, likely designed for filtering or ventilation applications.
def model_37267_b2be4b50_0016():
    """Model: millstone"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 71.4712328692, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((-100, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-100, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


# Description: This is a tapered blade or wedge-shaped metal part with a parallelogram profile, featuring a gradual taper from a wider section at one end to a pointed tip at the other, with a flat top surface and angled side edges.
def model_37267_b2be4b50_0026():
    """Model: Component60"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 675, perimeter: 142.9669331122
            with BuildLine():
                Line((100, 25), (115, 25))
                Line((100, -35), (100, 25))
                Line((107.5, -35), (100, -35))
                Line((115, 25), (107.5, -35))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a hexagonal shaft or tool bit with a long, slender prismatic body featuring a six-sided cross-section and tapered or beveled ends, commonly used as a cutting tool, drive shaft, or fastener component.
def model_37267_b2be4b50_0033():
    """Model: pillar III (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 825, perimeter: 235
            with BuildLine():
                Line((-10, 60), (-10, -50))
                Line((-10, -50), (-2.5, -50))
                Line((-2.5, -50), (-2.5, 60))
                Line((-2.5, 60), (-10, 60))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


# Description: This is a cylindrical ring or collar component with a large central hole and a mesh or perforated upper surface, featuring an asymmetrical cutout or opening on one side.
def model_37267_b2be4b50_0035():
    """Model: millstone I"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 687.2233929728, perimeter: 109.9557428756
            with BuildLine():
                CenterArc((-100, 0), 15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-100, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a slanted rectangular geometry and no additional features such as holes, slots, or curves.
def model_37267_b2be4b50_0036():
    """Model: wall"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5500, perimeter: 310
            with BuildLine():
                Line((-30, 65), (25, 65))
                Line((-30, -35), (-30, 65))
                Line((25, -35), (-30, -35))
                Line((25, 65), (25, -35))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a flat rectangular parallelogram plate or bar with a slight 3D perspective, featuring parallel edges and a uniform thickness with no holes, slots, or additional features.
def model_37267_b2be4b50_0038():
    """Model: wall (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2250, perimeter: 245
            with BuildLine():
                Line((27.5, 60), (50, 60))
                Line((27.5, -40), (27.5, 60))
                Line((50, -40), (27.5, -40))
                Line((50, 60), (50, -40))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a torus or ring-shaped component with a circular cross-section, featuring a uniform hollow center and smooth curved geometry throughout, commonly used as a seal, washer, or structural ring element.
def model_37375_1260516b_0001():
    """Model: 10"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6832964022, perimeter: 9.1106186954
            with BuildLine():
                CenterArc((0, 16.4500002317), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 16.4500002317), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is an L-shaped structural bracket or corner brace with a flat base, vertical flanges on two perpendicular sides, and a reinforced top featuring radial ribs or gussets that converge toward a central peak, providing strength and rigidity at the corner joint.
def model_37517_f894f8bd_0009():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.008245292, perimeter: 0.6354002576
            with BuildLine():
                Line((0, -0.045), (0.0616604653, -0.0762109042))
                Line((0.0616604653, -0.0762109042), (0.0639716752, -0.0773807778))
                CenterArc((0.0739502778, -0.0547990282), 0.0246882142, -113.8400567291, 180)
                Line((0.0816448707, -0.0313405295), (0.0839288803, -0.0322172787))
                Line((0, 0), (0.0816448707, -0.0313405295))
                Line((0, 0), (-0.0816448707, -0.0313405295))
                Line((-0.0816448707, -0.0313405295), (-0.0839288803, -0.0322172787))
                CenterArc((-0.0739502778, -0.0547990282), 0.0246882142, 113.8400567291, 180)
                Line((-0.0616604653, -0.0762109042), (-0.0639716752, -0.0773807778))
                Line((0, -0.045), (-0.0616604653, -0.0762109042))
            make_face()
            with BuildLine():
                CenterArc((-0.0739502778, -0.0547990282), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0739502778, -0.0547990282), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform diameter and slightly tapered or rounded ends, featuring a textured surface finish.
def model_37517_f894f8bd_0014():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


MODELS = {
    "model_31962_e5291336_0055": {"func": model_31962_e5291336_0055, "volume": 0.5466371217, "area": 6.2203534541},
    "model_32074_105fccde_0013": {"func": model_32074_105fccde_0013, "volume": 0.0064795348, "area": 0.2384222503},
    "model_32074_105fccde_0014": {"func": model_32074_105fccde_0014, "volume": 0.0138230077, "area": 0.4400527023},
    "model_32074_105fccde_0015": {"func": model_32074_105fccde_0015, "volume": 0.0025918139, "area": 0.1206308015},
    "model_32074_105fccde_0016": {"func": model_32074_105fccde_0016, "volume": 0.0070685835, "area": 0.3399583957},
    "model_32074_105fccde_0017": {"func": model_32074_105fccde_0017, "volume": 0.0042411501, "area": 0.2062981534},
    "model_32074_105fccde_0018": {"func": model_32074_105fccde_0018, "volume": 0.0014137167, "area": 0.0750139435},
    "model_32219_e5edc7ce_0010": {"func": model_32219_e5edc7ce_0010, "volume": 489.216, "area": 528.16},
    "model_32219_e5edc7ce_0036": {"func": model_32219_e5edc7ce_0036, "volume": 533.1200163295, "area": 383.882550837},
    "model_32219_e5edc7ce_0041": {"func": model_32219_e5edc7ce_0041, "volume": 2.8274333882, "area": 12.8805298797},
    "model_32220_1fd19c5e_0000": {"func": model_32220_1fd19c5e_0000, "volume": 6.3617251235, "area": 22.6194671058},
    "model_32220_1fd19c5e_0008": {"func": model_32220_1fd19c5e_0008, "volume": 0.0589048623, "area": 0.8639379797},
    "model_32220_1fd19c5e_0009": {"func": model_32220_1fd19c5e_0009, "volume": 0.413512133, "area": 4.8090925782},
    "model_32220_1fd19c5e_0010": {"func": model_32220_1fd19c5e_0010, "volume": 0.11545353, "area": 1.4294246574},
    "model_32220_1fd19c5e_0016": {"func": model_32220_1fd19c5e_0016, "volume": 0.0965663706, "area": 2.3969911184},
    "model_32220_1fd19c5e_0017": {"func": model_32220_1fd19c5e_0017, "volume": 5.6453784086, "area": 60.7447283646},
    "model_32667_426cf6b5_0000": {"func": model_32667_426cf6b5_0000, "volume": 4.1288848816, "area": 45.5967448617},
    "model_32775_a79b406b_0005": {"func": model_32775_a79b406b_0005, "volume": 0.009741241, "area": 0.4126726083},
    "model_32839_feb1aa29_0001": {"func": model_32839_feb1aa29_0001, "volume": 0.0772222198, "area": 1.0134149582},
    "model_32841_954e8c1a_0000": {"func": model_32841_954e8c1a_0000, "volume": 33246.4705455266, "area": 15003.479216789},
    "model_32871_04ff3d41_0004": {"func": model_32871_04ff3d41_0004, "volume": 31.6731038891, "area": 82.2005825105},
    "model_32871_04ff3d41_0014": {"func": model_32871_04ff3d41_0014, "volume": 0.2357754162, "area": 2.9531466269},
    "model_32879_49552f2f_0017": {"func": model_32879_49552f2f_0017, "volume": 0.6785840132, "area": 9.0477868423},
    "model_32895_6140d821_0001": {"func": model_32895_6140d821_0001, "volume": 0.0000176715, "area": 0.0050658182},
    "model_32898_565835ed_0000": {"func": model_32898_565835ed_0000, "volume": 0.0408407045, "area": 0.879645943},
    "model_32898_565835ed_0002": {"func": model_32898_565835ed_0002, "volume": 0.0210450263, "area": 0.8913457403},
    "model_33041_8c6b7740_0000": {"func": model_33041_8c6b7740_0000, "volume": 13.7638192047, "area": 33.7638192047},
    "model_33088_7def8eac_0001": {"func": model_33088_7def8eac_0001, "volume": 5.5474848315, "area": 67.8337653718},
    "model_33147_d7173b68_0000": {"func": model_33147_d7173b68_0000, "volume": 0.0583027237, "area": 1.9734241221},
    "model_33147_d7173b68_0004": {"func": model_33147_d7173b68_0004, "volume": 0.0245537248, "area": 1.1490908855},
    "model_33147_d7173b68_0005": {"func": model_33147_d7173b68_0005, "volume": 0.0265199507, "area": 1.4974996284},
    "model_33147_d7173b68_0007": {"func": model_33147_d7173b68_0007, "volume": 0.0490873852, "area": 2.3561944902},
    "model_33147_d7173b68_0014": {"func": model_33147_d7173b68_0014, "volume": 0.3392920066, "area": 10.1787601976},
    "model_33197_0f08d771_0001": {"func": model_33197_0f08d771_0001, "volume": 0.4227435787, "area": 10.3490855129},
    "model_33266_2a15d3f5_0000": {"func": model_33266_2a15d3f5_0000, "volume": 1993.75, "area": 4155.2817459305},
    "model_33271_94293b74_0000": {"func": model_33271_94293b74_0000, "volume": 13.9715804332, "area": 188.8200910359},
    "model_33274_28b853dd_0000": {"func": model_33274_28b853dd_0000, "volume": 40318.6614480708, "area": 33590.3913652953},
    "model_33529_756075a0_0001": {"func": model_33529_756075a0_0001, "volume": 10050, "area": 4918.6832980505},
    "model_33539_0e7a4748_0002": {"func": model_33539_0e7a4748_0002, "volume": 3067.0250998928, "area": 1234.2220146621},
    "model_33539_0e7a4748_0003": {"func": model_33539_0e7a4748_0003, "volume": 827.010475892, "area": 950.2102999487},
    "model_33607_c6f31fa6_0006": {"func": model_33607_c6f31fa6_0006, "volume": 5.7346250064, "area": 21.3910007912},
    "model_33607_c6f31fa6_0009": {"func": model_33607_c6f31fa6_0009, "volume": 191.1249940408, "area": 1224.8386538484},
    "model_33607_c6f31fa6_0010": {"func": model_33607_c6f31fa6_0010, "volume": 3278.8288888783, "area": 2936.2881195878},
    "model_33607_c6f31fa6_0024": {"func": model_33607_c6f31fa6_0024, "volume": 40.1120807678, "area": 94.1896339107},
    "model_33607_c6f31fa6_0025": {"func": model_33607_c6f31fa6_0025, "volume": 9.1793087416, "area": 80.530006238},
    "model_33607_c6f31fa6_0034": {"func": model_33607_c6f31fa6_0034, "volume": 0.0620351833, "area": 5.0800465024},
    "model_33607_c6f31fa6_0037": {"func": model_33607_c6f31fa6_0037, "volume": 13.7139217982, "area": 60.8672698529},
    "model_33615_7bab1106_0010": {"func": model_33615_7bab1106_0010, "volume": 0.061349135, "area": 2.5125241158},
    "model_33615_7bab1106_0011": {"func": model_33615_7bab1106_0011, "volume": 1.7530087007, "area": 36.1911473694},
    "model_33615_7bab1106_0013": {"func": model_33615_7bab1106_0013, "volume": 0.118045344, "area": 1.7153095889},
    "model_33615_7bab1106_0014": {"func": model_33615_7bab1106_0014, "volume": 48.0637478494, "area": 138.7337698789},
    "model_33625_c9ff9be8_0008": {"func": model_33625_c9ff9be8_0008, "volume": 68.0924149967, "area": 170.1686071501},
    "model_33625_c9ff9be8_0010": {"func": model_33625_c9ff9be8_0010, "volume": 185.5503161026, "area": 1490.2930150467},
    "model_33628_296ae2b8_0000": {"func": model_33628_296ae2b8_0000, "volume": 4, "area": 25},
    "model_33655_f8991a06_0007": {"func": model_33655_f8991a06_0007, "volume": 0.0263893783, "area": 0.9676105373},
    "model_33655_f8991a06_0010": {"func": model_33655_f8991a06_0010, "volume": 0.0125663706, "area": 0.5654866776},
    "model_33655_f8991a06_0011": {"func": model_33655_f8991a06_0011, "volume": 0.0439822972, "area": 0.6911503838},
    "model_33655_f8991a06_0012": {"func": model_33655_f8991a06_0012, "volume": 0.1759291886, "area": 2.0106192983},
    "model_33740_f9566689_0003": {"func": model_33740_f9566689_0003, "volume": 0.0289440946, "area": 2.9215429308},
    "model_33762_23d5c1d9_0004": {"func": model_33762_23d5c1d9_0004, "volume": 0.6386255815, "area": 9.7648513804},
    "model_33765_4d6288b9_0000": {"func": model_33765_4d6288b9_0000, "volume": 132, "area": 562},
    "model_33991_aaf84876_0019": {"func": model_33991_aaf84876_0019, "volume": 3.7938594326, "area": 21.1882524306},
    "model_33997_f6998a7d_0005": {"func": model_33997_f6998a7d_0005, "volume": 427.6492999699, "area": 358.5342615909},
    "model_33997_f6998a7d_0006": {"func": model_33997_f6998a7d_0006, "volume": 8.6395152679, "area": 27.6279752957},
    "model_33997_f6998a7d_0007": {"func": model_33997_f6998a7d_0007, "volume": 1173.4575287227, "area": 959.1161517903},
    "model_34063_0ca1585e_0006": {"func": model_34063_0ca1585e_0006, "volume": 1.4535928947, "area": 8.2732741229},
    "model_34063_0ca1585e_0008": {"func": model_34063_0ca1585e_0008, "volume": 0.2495052885, "area": 2.853194448},
    "model_34225_638d4d19_0000": {"func": model_34225_638d4d19_0000, "volume": 6.2831853072, "area": 22.2548188395},
    "model_34225_69ae4861_0005": {"func": model_34225_69ae4861_0005, "volume": 86.25, "area": 596.3},
    "model_34225_69ae4861_0006": {"func": model_34225_69ae4861_0006, "volume": 3.7306412761, "area": 30.2378292908},
    "model_34225_69ae4861_0011": {"func": model_34225_69ae4861_0011, "volume": 7.1415926536, "area": 24.5663706144},
    "model_34227_48203345_0009": {"func": model_34227_48203345_0009, "volume": 4164.4480206434, "area": 3058.9545783659},
    "model_34227_48203345_0010": {"func": model_34227_48203345_0010, "volume": 12815.7602860926, "area": 7065.5254894524},
    "model_34227_48203345_0012": {"func": model_34227_48203345_0012, "volume": 235619.4490192345, "area": 25132.7412287183},
    "model_34234_04351713_0000": {"func": model_34234_04351713_0000, "volume": 228.8586264432, "area": 556.9748225801},
    "model_34317_e9c65aa6_0000": {"func": model_34317_e9c65aa6_0000, "volume": 2340.366336, "area": 1851.48736},
    "model_34317_e9c65aa6_0006": {"func": model_34317_e9c65aa6_0006, "volume": 36.3246650571, "area": 130.7687942057},
    "model_34317_e9c65aa6_0009": {"func": model_34317_e9c65aa6_0009, "volume": 118.1631536831, "area": 335.1293963217},
    "model_34317_e9c65aa6_0010": {"func": model_34317_e9c65aa6_0010, "volume": 4438.7307977794, "area": 2182.8060434103},
    "model_34317_e9c65aa6_0011": {"func": model_34317_e9c65aa6_0011, "volume": 4.787435995, "area": 19.4571533947},
    "model_34317_e9c65aa6_0014": {"func": model_34317_e9c65aa6_0014, "volume": 132.5904816124, "area": 1083.7775330461},
    "model_34317_e9c65aa6_0016": {"func": model_34317_e9c65aa6_0016, "volume": 2400, "area": 2048},
    "model_34317_e9c65aa6_0019": {"func": model_34317_e9c65aa6_0019, "volume": 1062.7306586534, "area": 4315.3252840123},
    "model_34327_81dcda78_0000": {"func": model_34327_81dcda78_0000, "volume": 281.9911485751, "area": 647.9645943005},
    "model_34327_81dcda78_0003": {"func": model_34327_81dcda78_0003, "volume": 27, "area": 57},
    "model_34327_81dcda78_0005": {"func": model_34327_81dcda78_0005, "volume": 37.5, "area": 178},
    "model_34327_81dcda78_0009": {"func": model_34327_81dcda78_0009, "volume": 0.1963495408, "area": 2.3561944902},
    "model_34330_5eff1ee1_0001": {"func": model_34330_5eff1ee1_0001, "volume": 0.0002115264, "area": 0.03298484},
    "model_34343_6d3253e1_0007": {"func": model_34343_6d3253e1_0007, "volume": 369.1688027316, "area": 441.7690176215},
    "model_34343_6d3253e1_0013": {"func": model_34343_6d3253e1_0013, "volume": 644.9639968289, "area": 596.6569540201},
    "model_34343_6d3253e1_0018": {"func": model_34343_6d3253e1_0018, "volume": 379.0991113096, "area": 447.1473427639},
    "model_34343_6d3253e1_0023": {"func": model_34343_6d3253e1_0023, "volume": 427.9562335131, "area": 476.4961963},
    "model_34343_6d3253e1_0025": {"func": model_34343_6d3253e1_0025, "volume": 1376.513376, "area": 2499.995},
    "model_34343_6d3253e1_0029": {"func": model_34343_6d3253e1_0029, "volume": 663.2162292684, "area": 634.8342221027},
    "model_34343_6d3253e1_0031": {"func": model_34343_6d3253e1_0031, "volume": 633.7195140684, "area": 617.4149021027},
    "model_34343_6d3253e1_0035": {"func": model_34343_6d3253e1_0035, "volume": 387.4210351711, "area": 490.4959982942},
    "model_34343_6d3253e1_0036": {"func": model_34343_6d3253e1_0036, "volume": 604.4287984869, "area": 600.1003933467},
    "model_34343_6d3253e1_0039": {"func": model_34343_6d3253e1_0039, "volume": 57.354724, "area": 125.8062},
    "model_34347_841c5375_0009": {"func": model_34347_841c5375_0009, "volume": 47.0572901994, "area": 595.697980114},
    "model_34436_ffc43a58_0002": {"func": model_34436_ffc43a58_0002, "volume": 0.007262742, "area": 0.4200088053},
    "model_34440_af990c77_0001": {"func": model_34440_af990c77_0001, "volume": 140, "area": 288},
    "model_34440_af990c77_0009": {"func": model_34440_af990c77_0009, "volume": 0.2603136709, "area": 2.6261676353},
    "model_34520_035b5e9a_0000": {"func": model_34520_035b5e9a_0000, "volume": 1.1327640631, "area": 16.5631047883},
    "model_34520_035b5e9a_0006": {"func": model_34520_035b5e9a_0006, "volume": 0.9615066191, "area": 5.604169325},
    "model_34522_ed4af450_0000": {"func": model_34522_ed4af450_0000, "volume": 0.7262658718, "area": 5.5419864304},
    "model_34525_13455627_0000": {"func": model_34525_13455627_0000, "volume": 1.0420649413, "area": 7.7152675036},
    "model_34526_3ea355a5_0000": {"func": model_34526_3ea355a5_0000, "volume": 1.0540550169, "area": 7.5720696882},
    "model_34535_2e59cac1_0000": {"func": model_34535_2e59cac1_0000, "volume": 25.3657780019, "area": 61.8340808171},
    "model_34538_4d9a3cdd_0000": {"func": model_34538_4d9a3cdd_0000, "volume": 13.3558250654, "area": 31.6770830808},
    "model_34540_86189f81_0000": {"func": model_34540_86189f81_0000, "volume": 109.6135081297, "area": 162.1005344791},
    "model_34568_fbe47bf9_0000": {"func": model_34568_fbe47bf9_0000, "volume": 0.00002474, "area": 0.0071471233},
    "model_34587_ed155e93_0010": {"func": model_34587_ed155e93_0010, "volume": 314.159265359, "area": 691.1503837898},
    "model_34678_f709cdcc_0000": {"func": model_34678_f709cdcc_0000, "volume": 0.0153994259, "area": 0.5886354249},
    "model_34678_f709cdcc_0002": {"func": model_34678_f709cdcc_0002, "volume": 0.3938096797, "area": 7.4938239444},
    "model_34678_f709cdcc_0003": {"func": model_34678_f709cdcc_0003, "volume": 0.0041233404, "area": 0.1806415776},
    "model_34678_f709cdcc_0008": {"func": model_34678_f709cdcc_0008, "volume": 0.0000122718, "area": 0.0041724277},
    "model_34689_969a9743_0002": {"func": model_34689_969a9743_0002, "volume": 51963.9762155346, "area": 13053.8054676463},
    "model_34689_969a9743_0003": {"func": model_34689_969a9743_0003, "volume": 88936.7669994871, "area": 21487.3467787791},
    "model_34689_969a9743_0004": {"func": model_34689_969a9743_0004, "volume": 780000, "area": 94046.2112512353},
    "model_34708_7559c801_0004": {"func": model_34708_7559c801_0004, "volume": 1888862.0617924472, "area": 119392.536524033},
    "model_34769_44655d03_0000": {"func": model_34769_44655d03_0000, "volume": 0.122718463, "area": 2.0616701789},
    "model_34769_44655d03_0001": {"func": model_34769_44655d03_0001, "volume": 0.235619449, "area": 4.0644354956},
    "model_34769_44655d03_0005": {"func": model_34769_44655d03_0005, "volume": 0.4453207586, "area": 6.0789817847},
    "model_34770_6bba5bd4_0002": {"func": model_34770_6bba5bd4_0002, "volume": 1.0241915, "area": 7.25805},
    "model_34770_6bba5bd4_0006": {"func": model_34770_6bba5bd4_0006, "volume": 3.6633539971, "area": 21.8371315233},
    "model_34770_6bba5bd4_0007": {"func": model_34770_6bba5bd4_0007, "volume": 56.4497761115, "area": 234.8205765233},
    "model_34770_6bba5bd4_0010": {"func": model_34770_6bba5bd4_0010, "volume": 2.0848968626, "area": 13.4033468147},
    "model_34781_4f8a4759_0007": {"func": model_34781_4f8a4759_0007, "volume": 0.8295580056, "area": 17.8336345898},
    "model_34782_b461066c_0015": {"func": model_34782_b461066c_0015, "volume": 29.4524311274, "area": 56.9413668463},
    "model_34782_b461066c_0016": {"func": model_34782_b461066c_0016, "volume": 6.715154297, "area": 21.4413698608},
    "model_34782_b461066c_0018": {"func": model_34782_b461066c_0018, "volume": 286.2776305584, "area": 286.2776305584},
    "model_34785_dc3b83fa_0001": {"func": model_34785_dc3b83fa_0001, "volume": 1350, "area": 2709},
    "model_34785_dc3b83fa_0031": {"func": model_34785_dc3b83fa_0031, "volume": 35.3429173529, "area": 117.8097245096},
    "model_34785_dc3b83fa_0032": {"func": model_34785_dc3b83fa_0032, "volume": 75.3982236862, "area": 175.929188601},
    "model_34913_d23e2a24_0001": {"func": model_34913_d23e2a24_0001, "volume": 2.8122359338, "area": 19.1591598776},
    "model_34913_d23e2a24_0002": {"func": model_34913_d23e2a24_0002, "volume": 67.0215966617, "area": 126.0753104121},
    "model_34913_d23e2a24_0003": {"func": model_34913_d23e2a24_0003, "volume": 25.3353739549, "area": 82.3299907967},
    "model_34913_d23e2a24_0004": {"func": model_34913_d23e2a24_0004, "volume": 63.304448395, "area": 246.3136791284},
    "model_34913_d23e2a24_0005": {"func": model_34913_d23e2a24_0005, "volume": 116.8635379963, "area": 431.7589332763},
    "model_34913_d23e2a24_0006": {"func": model_34913_d23e2a24_0006, "volume": 10.6883608872, "area": 46.3106198231},
    "model_34913_d23e2a24_0007": {"func": model_34913_d23e2a24_0007, "volume": 284.1996939068, "area": 411.4359306147},
    "model_34913_d23e2a24_0008": {"func": model_34913_d23e2a24_0008, "volume": 125.8609463548, "area": 863.9063275991},
    "model_34917_61633e20_0010": {"func": model_34917_61633e20_0010, "volume": 21.2057504117, "area": 425.8114682676},
    "model_35132_35c342c8_0004": {"func": model_35132_35c342c8_0004, "volume": 0.1033780333, "area": 1.2370021074},
    "model_35143_6bdef095_0000": {"func": model_35143_6bdef095_0000, "volume": 7.0685834706, "area": 22.3838476568},
    "model_35143_6bdef095_0001": {"func": model_35143_6bdef095_0001, "volume": 5.5641442773, "area": 32.09804122},
    "model_35143_6bdef095_0004": {"func": model_35143_6bdef095_0004, "volume": 12.8679635091, "area": 80.4247719319},
    "model_35143_6bdef095_0005": {"func": model_35143_6bdef095_0005, "volume": 10, "area": 49},
    "model_35145_a3d7363c_0004": {"func": model_35145_a3d7363c_0004, "volume": 103.6725575685, "area": 213.6283004441},
    "model_35149_f50fea8a_0005": {"func": model_35149_f50fea8a_0005, "volume": 0.0001472622, "area": 0.0245436926},
    "model_35149_f50fea8a_0008": {"func": model_35149_f50fea8a_0008, "volume": 0.0003839042, "area": 0.0763594799},
    "model_35154_61b67282_0000": {"func": model_35154_61b67282_0000, "volume": 495.3568829613, "area": 771.1121608935},
    "model_35166_562b126c_0002": {"func": model_35166_562b126c_0002, "volume": 0.2088216637, "area": 1.9546989491},
    "model_35166_562b126c_0007": {"func": model_35166_562b126c_0007, "volume": 16.6288918134, "area": 118.1368569818},
    "model_35166_562b126c_0012": {"func": model_35166_562b126c_0012, "volume": 1.2315043202, "area": 14.0743350881},
    "model_35415_31c21951_0002": {"func": model_35415_31c21951_0002, "volume": 259799.9999999996, "area": 129639.2},
    "model_35580_2ab34839_0003": {"func": model_35580_2ab34839_0003, "volume": 76969.0200129503, "area": 31887.1654339364},
    "model_35962_dbbd6e18_0003": {"func": model_35962_dbbd6e18_0003, "volume": 58.9990852784, "area": 130.6782702137},
    "model_35968_5488b3e5_0005": {"func": model_35968_5488b3e5_0005, "volume": 1.8731746197, "area": 17.4829631172},
    "model_36088_1ea9c8a9_0005": {"func": model_36088_1ea9c8a9_0005, "volume": 2.4753569086, "area": 17.5518516874},
    "model_36088_1ea9c8a9_0010": {"func": model_36088_1ea9c8a9_0010, "volume": 0.7123806935, "area": 5.303242482},
    "model_36088_1ea9c8a9_0014": {"func": model_36088_1ea9c8a9_0014, "volume": 0.1374446786, "area": 3.5342917353},
    "model_36088_1ea9c8a9_0015": {"func": model_36088_1ea9c8a9_0015, "volume": 0.0212057504, "area": 1.2723450247},
    "model_36088_1ea9c8a9_0016": {"func": model_36088_1ea9c8a9_0016, "volume": 0.149493754, "area": 2.8164575252},
    "model_36088_1ea9c8a9_0018": {"func": model_36088_1ea9c8a9_0018, "volume": 0.06626797, "area": 3.004147975},
    "model_36194_c9cfd107_0001": {"func": model_36194_c9cfd107_0001, "volume": 0.0001505226, "area": 0.0320629923},
    "model_36194_c9cfd107_0002": {"func": model_36194_c9cfd107_0002, "volume": 0.0000071439, "area": 0.014538318},
    "model_36194_c9cfd107_0005": {"func": model_36194_c9cfd107_0005, "volume": 0.0000046019, "area": 0.0017180585},
    "model_36194_c9cfd107_0011": {"func": model_36194_c9cfd107_0011, "volume": 0.0000659279, "area": 0.0145823935},
    "model_36194_c9cfd107_0012": {"func": model_36194_c9cfd107_0012, "volume": 0.0000143715, "area": 0.0077839468},
    "model_36194_c9cfd107_0013": {"func": model_36194_c9cfd107_0013, "volume": 0.0000187898, "area": 0.0094016793},
    "model_36268_3c96c142_0003": {"func": model_36268_3c96c142_0003, "volume": 4.341495657, "area": 212.3161970352},
    "model_36268_3c96c142_0004": {"func": model_36268_3c96c142_0004, "volume": 3.0725745, "area": 43.951525},
    "model_36268_3c96c142_0006": {"func": model_36268_3c96c142_0006, "volume": 1.792335125, "area": 25.8064},
    "model_36268_3c96c142_0007": {"func": model_36268_3c96c142_0007, "volume": 1.0241915, "area": 14.919325},
    "model_36268_3c96c142_0008": {"func": model_36268_3c96c142_0008, "volume": 0.77838554, "area": 11.661267},
    "model_36268_3c96c142_0010": {"func": model_36268_3c96c142_0010, "volume": 2.4131943692, "area": 10.1341495819},
    "model_36283_ee4931a7_0000": {"func": model_36283_ee4931a7_0000, "volume": 198, "area": 348},
    "model_36303_82ed629e_0001": {"func": model_36303_82ed629e_0001, "volume": 19.9999992624, "area": 81.9999984577},
    "model_36409_3adb6194_0001": {"func": model_36409_3adb6194_0001, "volume": 0.00472, "area": 0.2991999984},
    "model_36413_fb06800c_0004": {"func": model_36413_fb06800c_0004, "volume": 3.4346219717, "area": 33.2506648949},
    "model_36413_fb06800c_0006": {"func": model_36413_fb06800c_0006, "volume": 3.8170350741, "area": 13.5716802635},
    "model_36413_fb06800c_0009": {"func": model_36413_fb06800c_0009, "volume": 3.1974, "area": 13.0232},
    "model_36436_362a4413_0024": {"func": model_36436_362a4413_0024, "volume": 0.1422552423, "area": 2.0773781422},
    "model_36436_362a4413_0028": {"func": model_36436_362a4413_0028, "volume": 0.4599696829, "area": 6.856776327},
    "model_36445_67816b83_0000": {"func": model_36445_67816b83_0000, "volume": 0.081681409, "area": 3.518583772},
    "model_36445_67816b83_0002": {"func": model_36445_67816b83_0002, "volume": 0.0969966732, "area": 4.1783182293},
    "model_36445_67816b83_0005": {"func": model_36445_67816b83_0005, "volume": 0.0446695205, "area": 3.7110063221},
    "model_36451_1a7f9437_0000": {"func": model_36451_1a7f9437_0000, "volume": 0.7634070148, "area": 5.6548667765},
    "model_36451_1a7f9437_0004": {"func": model_36451_1a7f9437_0004, "volume": 1.3398188321, "area": 13.2463970289},
    "model_36451_1a7f9437_0009": {"func": model_36451_1a7f9437_0009, "volume": 4.6746898685, "area": 26.3893782902},
    "model_36451_1a7f9437_0011": {"func": model_36451_1a7f9437_0011, "volume": 15.0293792548, "area": 81.6814089933},
    "model_36733_b0605a21_0000": {"func": model_36733_b0605a21_0000, "volume": 11.1445394504, "area": 68.4672367025},
    "model_36816_5ba90dc9_0000": {"func": model_36816_5ba90dc9_0000, "volume": 73.6310778185, "area": 127.6272015521},
    "model_36918_2dee90be_0005": {"func": model_36918_2dee90be_0005, "volume": 44.8, "area": 913.92},
    "model_36918_2dee90be_0007": {"func": model_36918_2dee90be_0007, "volume": 7.475, "area": 304.98},
    "model_36918_2dee90be_0008": {"func": model_36918_2dee90be_0008, "volume": 1.0240259851, "area": 23.2658429694},
    "model_36918_2dee90be_0010": {"func": model_36918_2dee90be_0010, "volume": 0.6280909383, "area": 14.6872548616},
    "model_36953_bdaf025b_0005": {"func": model_36953_bdaf025b_0005, "volume": 179.1786728018, "area": 334.663517268},
    "model_36953_bdaf025b_0007": {"func": model_36953_bdaf025b_0007, "volume": 0.048216664, "area": 1.0863543991},
    "model_37040_ecbcd25e_0011": {"func": model_37040_ecbcd25e_0011, "volume": 84.53, "area": 865.38},
    "model_37040_ecbcd25e_0027": {"func": model_37040_ecbcd25e_0027, "volume": 99.072, "area": 1011.24},
    "model_37040_ecbcd25e_0037": {"func": model_37040_ecbcd25e_0037, "volume": 1.5501850447, "area": 32.5045508939},
    "model_37040_ecbcd25e_0038": {"func": model_37040_ecbcd25e_0038, "volume": 6.26545, "area": 65.1261501778},
    "model_37267_b2be4b50_0000": {"func": model_37267_b2be4b50_0000, "volume": 41.2334035784, "area": 175.929188601},
    "model_37267_b2be4b50_0001": {"func": model_37267_b2be4b50_0001, "volume": 636.1725123519, "area": 862.3671834104},
    "model_37267_b2be4b50_0008": {"func": model_37267_b2be4b50_0008, "volume": 1714.6570826471, "area": 1482.9867228627},
    "model_37267_b2be4b50_0009": {"func": model_37267_b2be4b50_0009, "volume": 4687.4999999999, "area": 2399.632034356},
    "model_37267_b2be4b50_0012": {"func": model_37267_b2be4b50_0012, "volume": 3409.3942836395, "area": 1954.2904596981},
    "model_37267_b2be4b50_0016": {"func": model_37267_b2be4b50_0016, "volume": 500.2986300842, "area": 428.827397215},
    "model_37267_b2be4b50_0026": {"func": model_37267_b2be4b50_0026, "volume": 337.5, "area": 1421.4834665561},
    "model_37267_b2be4b50_0033": {"func": model_37267_b2be4b50_0033, "volume": 6187.5, "area": 3412.5},
    "model_37267_b2be4b50_0035": {"func": model_37267_b2be4b50_0035, "volume": 5154.1754472957, "area": 2199.1148575129},
    "model_37267_b2be4b50_0036": {"func": model_37267_b2be4b50_0036, "volume": 16500, "area": 11930},
    "model_37267_b2be4b50_0038": {"func": model_37267_b2be4b50_0038, "volume": 4500, "area": 4990},
    "model_37375_1260516b_0001": {"func": model_37375_1260516b_0001, "volume": 0.2733185609, "area": 5.0108402825},
    "model_37517_f894f8bd_0009": {"func": model_37517_f894f8bd_0009, "volume": 0.0002061323, "area": 0.0323755905},
    "model_37517_f894f8bd_0014": {"func": model_37517_f894f8bd_0014, "volume": 0.0002454369, "area": 0.0402516559},
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
