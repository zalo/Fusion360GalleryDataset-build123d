"""Batch 008 - passing/01_2ops
199 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a hexagonal or elongated octagonal frame ring with a hollow center opening and textured surface, featuring uniform wall thickness throughout its perimeter.
def model_23554_a0845d54_0003():
    """Model: Bullone grande v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.9411158357, perimeter: 49.7039614962
            with BuildLine():
                Line((2.3094010768, 4), (-2.3094010768, 4))
                Line((-2.3094010768, 4), (-4.6188021535, 0))
                Line((-4.6188021535, 0), (-2.3094010768, -4))
                Line((-2.3094010768, -4), (2.3094010768, -4))
                Line((2.3094010768, -4), (4.6188021535, 0))
                Line((4.6188021535, 0), (2.3094010768, 4))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a hollow elliptical center opening and a textured or mesh-patterned outer surface, featuring a uniform curved cross-section throughout.
def model_23554_a0845d54_0006():
    """Model: guarnizione v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.3939428713, perimeter: 35.3429173529
            with BuildLine():
                CenterArc((0, 0), 3.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a cylindrical roller or shaft with a hexagonal flat end face, featuring a grooved or textured surface along its length and a tapered transition to the flat hexagonal end.
def model_23568_4de5a366_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 607055.5664551785, perimeter: 2960.3361612213
            with BuildLine():
                Line((0, 0), (914.4, 0))
                Line((914.4, 0), (914.4, 304.8))
                CenterArc((457.2, 304.8), 457.2, 0, 180)
                Line((0, 0), (0, 304.8))
            make_face()
        # OneSide extrude, distance=2743.2
        extrude(amount=2743.2)
    return part.part


# Description: This is a torus-shaped washer or ring with a smooth, curved donut geometry featuring a central hole and a textured or mesh-patterned surface finish on the outer portion.
def model_23602_5daaccf5_0001():
    """Model: Washer2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.7232168054, perimeter: 21.1939380234
            with BuildLine():
                CenterArc((0, 0), 2.38125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.99187, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2778125
        extrude(amount=0.2778125)
    return part.part


# Description: This is a curved shell or shroud component with an elongated, boat-like shape featuring a smooth outer surface (dark blue) and an open interior structure with radial ribs or support elements (light blue) that extend from a central spine.
def model_23602_5daaccf5_0003():
    """Model: Key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3873650778, perimeter: 4.8320687758
            with BuildLine():
                Line((0.9398, 0), (-0.9398, 0))
                CenterArc((0, 0), 0.9398, 180, 180)
            make_face()
        # OneSide extrude, distance=0.3302
        extrude(amount=0.3302)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender form and rounded ends, featuring a uniform circular cross-section throughout its length.
def model_23649_45d06d26_0000():
    """Model: Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: A flat, rectangular plate or panel with a slightly beveled or angled edge design, featuring diagonal surface details or reinforcement lines across its face.
def model_23649_45d06d26_0002():
    """Model: Switch (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6400000262, perimeter: 3.2000000656
            with BuildLine():
                Line((0.5000000075, -1.5000000224), (0.5000000075, -0.7000000104))
                Line((0.5000000075, -0.7000000104), (-0.3000000134, -0.7000000104))
                Line((-0.3000000134, -0.7000000104), (-0.3000000134, -1.5000000224))
                Line((-0.3000000134, -1.5000000224), (0.5000000075, -1.5000000224))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a timing belt or drive belt, characterized by its oval/elliptical loop shape with a ribbed or toothed inner surface for power transmission and grip.
def model_23649_45d06d26_0004():
    """Model: Interlocking Ring1 Top"""
    with BuildPart() as part:
        # Sketch14 -> Extrude10 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.3882733693, perimeter: 45.6755910946
            with BuildLine():
                EllipticalCenterArc((0, 0), 4.25, 3.5, 0, 360, 0)
            make_face()
            with BuildLine():
                EllipticalCenterArc((0, 0), 3.75, 3, 0, 360, 0)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cable management loop or strain relief guide featuring an oval-shaped loop with a textured grip surface and a flat mounting tab or slot at the base for attachment.
def model_23681_932e722e_0005():
    """Model: carbonpath m v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.276353257, perimeter: 3.1094489615
            with BuildLine():
                Line((0.175, -0.6519202405), (0.175, -1.5400892831))
                CenterArc((0, 0), 0.675, -105.0261137591, 30.0522275182)
                Line((-0.175, -0.6519202405), (-0.175, -1.5400892831))
                CenterArc((0, 0), 1.55, -96.4827010511, 12.9654021023)
            make_face()
            with BuildLine():
                CenterArc((0, -1.3), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.8639379797, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((0, 0), 0.675, -105.0261137591, 30.0522275182)
                CenterArc((0, 0), 0.675, -74.9738862409, 329.9477724818)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a U-shaped cable or wire management clip with textured grip surfaces and mounting flanges at each end featuring rectangular slots for fastening.
def model_23681_932e722e_0006():
    """Model: carbonpath v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1638409535, perimeter: 2.4511032121
            with BuildLine():
                CenterArc((0, 0), 1.55, -71.4827010511, 12.9654021023)
                Line((0.8094737185, -1.3218367142), (0.5747004626, -0.8183638422))
                CenterArc((0, 0), 1, -75.5224878141, 20.6011459219)
                Line((0.25, -0.9682458366), (0.492265993, -1.4697531058))
            make_face()
            with BuildLine():
                CenterArc((0.5494037403, -1.1782001231), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.2476400285, perimeter: 10.5027365238
            with BuildLine():
                Line((-0.25, -0.9682458366), (-0.25, -0.7071067812))
                CenterArc((0, 0), 0.75, -70.5287793655, 321.057558731)
                Line((0.25, -0.9682458366), (0.25, -0.7071067812))
                CenterArc((0, 0), 1, -75.5224878141, 20.6011459219)
                CenterArc((0, 0), 1, -54.9213418922, 289.8426837844)
                CenterArc((0, 0), 1, -125.0786581078, 20.6011459219)
            make_face()
            # Profile area: 0.1638409535, perimeter: 2.4511032121
            with BuildLine():
                Line((-0.25, -0.9682458366), (-0.492265993, -1.4697531058))
                CenterArc((0, 0), 1, -125.0786581078, 20.6011459219)
                Line((-0.8094737185, -1.3218367142), (-0.5747004626, -0.8183638422))
                CenterArc((0, 0), 1.55, -121.4827010511, 12.9654021023)
            make_face()
            with BuildLine():
                CenterArc((-0.5494037403, -1.1782001231), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a curved C-shaped or horseshoe-shaped bracket or clamp with a hollow center and textured surface, designed to grip or hold cylindrical objects or components.
def model_23681_932e722e_0012():
    """Model: carbon v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0690141668, perimeter: 9.0521133348
            with BuildLine():
                CenterArc((0, 0), 1, -50, 280)
                Line((-0.4820907073, -0.5745333323), (-0.6427876097, -0.7660444431))
                CenterArc((0, 0), 0.75, -50, 280)
                Line((0.4820907073, -0.5745333323), (0.6427876097, -0.7660444431))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


# Description: This is a coffin-shaped or hexagonal box-like container with a tapered, elongated form featuring a faceted top surface with triangulated panels and darker side flanges, resembling a streamlined capsule or pod structure.
def model_23681_932e722e_0015():
    """Model: nut v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0478907386, perimeter: 3.8105117767
            with BuildLine():
                Line((-0.55, -0.3175426481), (0, -0.6350852961))
                Line((0, -0.6350852961), (0.55, -0.3175426481))
                Line((0.55, -0.3175426481), (0.55, 0.3175426481))
                Line((0.55, 0.3175426481), (0, 0.6350852961))
                Line((0, 0.6350852961), (-0.55, 0.3175426481))
                Line((-0.55, 0.3175426481), (-0.55, -0.3175426481))
            make_face()
        # Symmetric extrude, each_side=0.075
        extrude(amount=0.075, both=True)
    return part.part


# Description: This is a retaining ring (or snap ring), a circular metal fastener with a C-shaped gap and a small lug or tab, designed to secure components on shafts or in grooves.
def model_23706_ef15ef9c_0003():
    """Model: Pierścień osadczy 35x1,5 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.5015692036, perimeter: 25.6670418861
            with BuildLine():
                Line((-0.4815361485, -1.9950898433), (-0.4666124496, -2.1084465905))
                CenterArc((-0.392254085, -2.0986571261), 0.075, -172.5000000011, 71.9131607689)
                CenterArc((0, 0), 2.21, -100.5868392324, 9.6145791191)
                Line((-0.0279977376, -1.6497624455), (-0.0375, -2.209681821))
                CenterArc((0, 0), 1.65, -89.0277398867, 358.0554797735)
                Line((0.0279977376, -1.6497624455), (0.0375, -2.209681821))
                CenterArc((0, 0), 2.21, -89.0277398867, 9.6145791191)
                CenterArc((0.392254085, -2.0986571261), 0.075, -79.4131607676, 71.9131607687)
                Line((0.4815361485, -1.9950898433), (0.4666124496, -2.1084465905))
                CenterArc((0.8434135229, -2.0427319034), 0.365, 112.435, 60.0650000011)
                CenterArc((0.8434135229, -2.0427319034), 0.365, 110.5151024069, 1.9198975931)
                CenterArc((0, 0.1011352019), 1.9388647981, -68.3442422822, 316.6884845643)
                CenterArc((-0.8434135229, -2.0427319034), 0.365, 67.565, 1.9198975931)
                CenterArc((-0.8434135229, -2.0427319034), 0.365, 7.4999999989, 60.0650000012)
            make_face()
            with BuildLine():
                CenterArc((-0.2, -1.9698730924), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.2, -1.9698730924), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a suspension hammock or sling with a curved, elongated rectangular body featuring dual attachment points at each end with radiating suspension lines, designed for hanging or supporting loads.
def model_23706_ef15ef9c_0005():
    """Model: Wpust 16x10x56 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.4106192983, perimeter: 13.0265482457
            with BuildLine():
                CenterArc((0.8, 0), 0.8, 90, 180)
                Line((0.8, -0.8), (4.8, -0.8))
                CenterArc((4.8, 0), 0.8, -90, 180)
                Line((4.8, 0.8), (0.8, 0.8))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a retaining ring (or snap ring) with an open C-shaped design featuring two small protruding tabs at the bottom ends for easy installation and removal.
def model_23706_ef15ef9c_0007():
    """Model: Pierścień osadczy wewnętrzny 68x2,5 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.2797526126, perimeter: 42.0174518644
            with BuildLine():
                CenterArc((-1.0298201519, -2.9080397959), 0.315, -16.5740906888, 2.9340906888)
                CenterArc((-1.0298201519, -2.9080397959), 0.315, -13.64, 154.155633416)
                CenterArc((-1.5159316258, -2.5075431395), 0.3148427874, -121.155, 81.670633416)
                CenterArc((-1.5159316258, -2.5075431395), 0.3148427874, -124.6609470393, 3.5059470393)
                CenterArc((0, -0.1649845007), 3.1049845007, -56.9143039011, 293.8286078021)
                CenterArc((1.5159316258, -2.5075431395), 0.3148427874, -58.845, 3.5059470393)
                CenterArc((1.5159316258, -2.5075431395), 0.3148427874, -140.515633416, 81.670633416)
                CenterArc((1.0298201519, -2.9080397959), 0.315, 39.484366584, 154.155633416)
                CenterArc((1.0298201519, -2.9080397959), 0.315, -166.36, 2.9340906888)
                CenterArc((0, 0), 3.085, -76.36, 0.0076692857)
                Line((0.7275065897, -2.997992522), (0.8371631745, -3.4498779427))
                CenterArc((0, 0), 3.55, -76.36, 332.72)
                Line((-0.7275065897, -2.997992522), (-0.8371631745, -3.4498779427))
                CenterArc((0, 0), 3.085, -103.6476692857, 0.0076692857)
            make_face()
            with BuildLine():
                CenterArc((-1.0298201519, -2.9080397959), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0298201519, -2.9080397959), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a retaining ring (or snap ring) with a circular band shape and a small gap/opening at the bottom for installation, designed to secure components onto a shaft or in a bore.
def model_23706_ef15ef9c_0008():
    """Model: Pierścień osadczy 45x1,75 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3461565916, perimeter: 32.3016235043
            with BuildLine():
                CenterArc((-0.8914912695, -2.649012706), 0.435, 71.4, 1.5137949372)
                CenterArc((-0.8914912695, -2.649012706), 0.435, 7.5, 63.9)
                Line((-0.4602127548, -2.5922338124), (-0.4441458237, -2.7142742699))
                CenterArc((-0.3697874591, -2.7044848055), 0.075, -172.5, 74.7141594834)
                CenterArc((0, 0), 2.8046484807, -97.7858405166, 6.8905255043)
                Line((-0.033370759, -2.1247379585), (-0.0438242, -2.804306071))
                CenterArc((0, 0), 2.125, -89.1001965907, 358.2003931814)
                Line((0.033370759, -2.1247379585), (0.0436758, -2.7946587313))
                CenterArc((0, 0), 2.795, -89.1046365433, 6.9460310643)
                CenterArc((0.3710931992, -2.6945667254), 0.075, -82.1586054791, 74.6586054791)
                Line((0.4454515638, -2.7043561898), (0.4602127548, -2.5922338124))
                CenterArc((0.8914912695, -2.649012706), 0.435, 108.6, 63.9)
                CenterArc((0.8914912695, -2.649012706), 0.435, 107.0862050628, 1.5137949372)
                CenterArc((0, 0.1204976446), 2.4745023554, -72.0238440012, 324.0476880025)
            make_face()
            with BuildLine():
                CenterArc((0.2125, -2.5135333696), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.2125, -2.5135333696), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.175
        extrude(amount=0.175)
    return part.part


# Description: This is a retaining ring (or snap ring) with a circular band shape and a small rectangular slot or gap at the bottom, designed to secure components on a shaft or in a bore.
def model_23706_ef15ef9c_0009():
    """Model: Pierścień osadczy 50x2 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.7551812675, perimeter: 35.4501237901
            with BuildLine():
                Line((0.0386513158, -2.3496821223), (0.0455592105, -2.7696253101))
                CenterArc((0, 0), 2.77, -89.0575927128, 1.130945985)
                CenterArc((0.225, -2.7608467904), 0.125, 98.5811133774, 84.7851244197)
                CenterArc((0.225, -2.7608467904), 0.125, 90.3893414784, 8.1917718991)
                CenterArc((0.225, -2.7608467904), 0.125, -176.6337622028, 267.0231036812)
                Line((0.0455592105, -2.7696253101), (0.05, -3.039588788))
                CenterArc((0, 0), 3.04, -89.0575927128, 7.999093505)
                CenterArc((0.4608379422, -2.9289679737), 0.075, -81.0584992077, 73.5584992077)
                Line((0.5351963068, -2.9387574381), (0.5479530671, -2.8418602232))
                CenterArc((0.9346165631, -2.8927654381), 0.39, 107.905, 64.595)
                CenterArc((0.9346165631, -2.8927654381), 0.39, 106.6997577971, 1.2052422029)
                CenterArc((0, 0.1075041225), 2.7524958775, -72.61223751, 325.22447502)
                CenterArc((-0.9346165631, -2.8927654381), 0.39, 72.095, 1.2052422029)
                CenterArc((-0.9346165631, -2.8927654381), 0.39, 7.5, 64.595)
                Line((-0.5351963068, -2.9387574381), (-0.5479530671, -2.8418602232))
                CenterArc((-0.4608379422, -2.9289679737), 0.075, -172.4999999999, 73.5584992077)
                CenterArc((0, 0), 3.04, -98.9415007923, 7.999093505)
                Line((-0.0386513158, -2.3496821223), (-0.05, -3.039588788))
                CenterArc((0, 0), 2.35, -89.0575927128, 358.1151854255)
            make_face()
            with BuildLine():
                CenterArc((-0.225, -2.7608467904), 0.125, 89.6106585217, 351.808228101)
                CenterArc((-0.225, -2.7608467904), 0.125, 81.4188866227, 8.191771899)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a rounded rectangular bar or spacer with a long, flat profile and uniformly rounded ends, featuring a simple cylindrical or pill-shaped geometry with no holes or additional features.
def model_23751_5e8bc03f_0008():
    """Model: Double Ended Screw v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2026829916, perimeter: 1.595929068
            Circle(0.254)
        # OneSide extrude, distance=5.0038
        extrude(amount=5.0038)
    return part.part


# Description: This is a long, rectangular trough or channel with pyramidal/angular end caps on both sides and a shallow central depression or slot running along its length, designed to guide or contain material flow.
def model_23770_f35c1c3b_0006():
    """Model: handle v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12, perimeter: 26
            with BuildLine():
                Line((0.5, 0), (0.5, -2))
                Line((0.5, -2), (10.5, -2))
                Line((10.5, -2), (10.5, 0))
                Line((10.5, 0), (9.5, 0))
                Line((9.5, 0), (9.5, -1))
                Line((9.5, -1), (1.5, -1))
                Line((1.5, -1), (1.5, 0))
                Line((1.5, 0), (0.5, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a triangular pyramidal or wedge-shaped 3D part with a pointed apex at the top, a slanted rectangular face on the right side, and a flat triangular base, featuring clean edges and a simple geometric form with no holes or slots.
def model_23770_f35c1c3b_0012():
    """Model: glass v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1459.2, perimeter: 152.8
            with BuildLine():
                Line((0, 38), (0, 0))
                Line((0, 0), (38.4, 0))
                Line((38.4, 0), (38.4, 38))
                Line((38.4, 38), (0, 38))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or bushing with a smooth outer surface and a central oval or oblong hole, featuring a subtle mesh or textured pattern on the upper surface.
def model_23774_716b8bc4_0003():
    """Model: Guarnizione v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.3256625004, perimeter: 23.8761041673
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved solar panel or photovoltaic module with a gently arched rectangular shape, featuring a blue solar cell surface with linear wire interconnects, bordered by a dark frame or housing on the edges.
def model_23790_2abde9b6_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.0223191027, perimeter: 20.885051633
            with BuildLine():
                CenterArc((4.75, 0), 0.25, -107.6989675258, 180.1952953653)
                CenterArc((0.0011403535, -14.6592913127), 15.6592913542, 72.0574514739, 35.8308161485)
                CenterArc((0.0011403535, -14.6592913127), 15.6592913542, 107.8882676225, 0.1389365795)
                CenterArc((-4.75, 0), 0.25, 112.3132252206, 180.406523536)
                CenterArc((-0.00143743, -14.6758165624), 15.1758166305, 72.0641069981, 35.7867775756)
                CenterArc((-0.00143743, -14.6758165624), 15.1758166305, 72.0561702543, 0.0079367438)
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


# Description: This is a dark navy blue elbow pipe fitting or connector with two cylindrical ends positioned at approximately 90 degrees to each other, featuring reinforced curved joints at both connection points.
def model_23792_5b4c1ce0_0001():
    """Model: WheelBracket v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 819.9379886613, perimeter: 183.62967497
            with BuildLine():
                Line((20.3199996948, 0), (-20.3199996948, 0))
                Line((20.3199996948, 0), (34.6884094885, 14.3684097937))
                CenterArc((31.0963070401, 17.9605122421), 5.08, -45, 180)
                Line((16.1115899011, 10.16), (27.5042045917, 21.5526146906))
                Line((16.1115899011, 10.16), (-16.1115899011, 10.16))
                Line((-16.1115899011, 10.16), (-27.5042045917, 21.5526146906))
                CenterArc((-31.0963070401, 17.9605122421), 5.08, 45, 180)
                Line((-20.3199996948, 0), (-34.6884094885, 14.3684097937))
            make_face()
            with BuildLine():
                CenterArc((31.0963070401, 17.9605122421), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-31.0963070401, 17.9605122421), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a cylindrical rod or tube with a long, slender tapered shape featuring a slightly beveled or angled top end, commonly used as a shaft, pin, or structural component.
def model_23792_5b4c1ce0_0002():
    """Model: Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4645007474, perimeter: 18.450403117
            with BuildLine():
                CenterArc((-2.2860000811, 2.2860000811), 0.254, 90, 90)
                Line((-2.5400000811, 0.254), (-2.5400000811, 2.2860000811))
                CenterArc((-2.2860000811, 0.254), 0.254, 180, 90)
                Line((-0.254, 0), (-2.2860000811, 0))
                CenterArc((-0.254, 0.254), 0.254, -90, 90)
                Line((0, 2.2860000811), (0, 0.254))
                CenterArc((-0.254, 2.2860000811), 0.254, 0, 90)
                Line((-2.2860000811, 2.5400000811), (-0.254, 2.5400000811))
            make_face()
            with BuildLine():
                Line((-2.3812500811, 0.254), (-2.3812500811, 2.2860000811))
                CenterArc((-2.2860000811, 2.2860000811), 0.09525, 90, 90)
                Line((-2.2860000811, 2.3812500811), (-0.254, 2.3812500811))
                CenterArc((-0.254, 2.2860000811), 0.09525, 0, 90)
                Line((-0.15875, 2.2860000811), (-0.15875, 0.254))
                CenterArc((-0.254, 0.254), 0.09525, -90, 90)
                Line((-0.254, 0.15875), (-2.2860000811, 0.15875))
                CenterArc((-2.2860000811, 0.254), 0.09525, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=60.96
        extrude(amount=60.96)
    return part.part


# Description: This is a long, slender rectangular bar or rail with rounded ends and a slightly beveled or chamfered edge profile, appearing to be a simple structural or guide component.
def model_23792_5b4c1ce0_0022():
    """Model: Base v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4645007474, perimeter: 18.450403117
            with BuildLine():
                CenterArc((-0.254, 2.2860000811), 0.254, 0, 90)
                Line((-2.2860000811, 2.5400000811), (-0.254, 2.5400000811))
                CenterArc((-2.2860000811, 2.2860000811), 0.254, 90, 90)
                Line((-2.5400000811, 0.254), (-2.5400000811, 2.2860000811))
                CenterArc((-2.2860000811, 0.254), 0.254, 180, 90)
                Line((-0.254, 0), (-2.2860000811, 0))
                CenterArc((-0.254, 0.254), 0.254, -90, 90)
                Line((0, 2.2860000811), (0, 0.254))
            make_face()
            with BuildLine():
                Line((-2.2860000811, 2.3812500811), (-0.254, 2.3812500811))
                CenterArc((-0.254, 2.2860000811), 0.09525, 0, 90)
                Line((-0.15875, 2.2860000811), (-0.15875, 0.254))
                CenterArc((-0.254, 0.254), 0.09525, -90, 90)
                Line((-0.254, 0.15875), (-2.2860000811, 0.15875))
                CenterArc((-2.2860000811, 0.254), 0.09525, 180, 90)
                Line((-2.3812500811, 0.254), (-2.3812500811, 2.2860000811))
                CenterArc((-2.2860000811, 2.2860000811), 0.09525, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=91.44
        extrude(amount=91.44)
    return part.part


# Description: This is a channel or U-shaped structural beam with a long, rectangular profile featuring a central longitudinal slot or channel running through its length, flanged edges on both sides, and stepped or tapered ends.
def model_23801_7ebe01f7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.0060670089, perimeter: 16.016877559
            with BuildLine():
                Line((0, 2.0000000298), (-0.0167655296, 0.7455511694))
                Line((3, 0.7455511694), (-0.0167655296, 0.7455511694))
                Line((3, 0), (3, 0.7455511694))
                Line((4.5, 0), (3, 0))
                Line((4.5, 0.5097616376), (4.5, 0))
                Line((4.5, 3.5), (4.5, 0.5097616376))
                Line((3.0118635483, 3.5), (4.5, 3.5))
                Line((3.0118635483, 2.0000000298), (3.0118635483, 3.5))
                Line((0, 2.0000000298), (3.0118635483, 2.0000000298))
            make_face()
            # Profile area: 0.7625533178, perimeter: 4.011326744
            with BuildLine():
                Line((4.5, 0.5097616376), (4.5, 0))
                Line((4.5, 0), (5.9959017344, 0))
                Line((5.9959017344, 0), (5.9959017344, 0.5097616376))
                Line((4.5, 0.5097616376), (5.9959017344, 0.5097616376))
            make_face()
        # Symmetric extrude, each_side=-7
        extrude(amount=-7, both=True)
    return part.part


# Description: A dark gray parallelogram-shaped flat plate or bracket with a rectangular notch cut out from the upper right corner.
def model_23862_7a684f76_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8613.5115567256, perimeter: 538.407818637
            with BuildLine():
                Line((0, 50), (0, 0.0790639244))
                Line((-190, 50), (0, 50))
                Line((-190, 0), (-190, 50))
                Line((-50, 0), (-190, 0))
                CenterArc((-50, 1.3), 1.3, -90, 45)
                Line((-46.1099241067, 3.3515982622), (-49.0807611845, 0.3807611845))
                CenterArc((-49.0090619096, 6.2507360651), 4.1, -45, 57.4)
                Line((-48.6832068031, 23.8619340021), (-45.0047055684, 7.1311509065))
                CenterArc((-44.678850462, 24.7423488435), 4.1, 99.5, 92.9)
                Line((-22.4681984702, 32.6161482011), (-45.355545646, 28.7861198098))
                CenterArc((-21.7915032861, 28.5723772348), 4.1, -11.1, 110.6)
                Line((-21.4534304845, 8.9992775628), (-17.7682033638, 27.7830371721))
                CenterArc((-17.4301305622, 8.2099375), 4.1, 168.9, 88.4)
                Line((0, 0.0790639244), (-18.3315, 4.2102458698))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


# Description: This is a C-clip or retaining ring, characterized by an open circular shape with a gap on one end and hooked terminals at both extremities, designed to secure components onto shafts or in grooves.
def model_23876_74957d38_0008():
    """Model: DIN 472 75x2.5 v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8989296458, perimeter: 23.7750345051
            with BuildLine():
                Line((0, 3.327), (0, 3.9))
                CenterArc((0, 0), 3.9, 90, 168.45)
                Line((-0.7808697157, -3.8210263657), (-0.7027229747, -3.4276023913))
                CenterArc((-0.9675458142, -3.375), 0.2699965701, -11.2345677261, 143.7345677261)
                Line((-1.149952853, -3.1759376479), (-1.2602229235, -3.276981551))
                CenterArc((0, 0), 3.51095, 177.0220801999, 71.9427634937)
                CenterArc((0, -0.2), 3.527, 90, 83.7757499038)
            make_face()
            with BuildLine():
                CenterArc((-0.9675458142, -3.375), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.8989296458, perimeter: 23.7750345051
            with BuildLine():
                CenterArc((0.9675458142, -3.375), 0.2699965701, 47.5, 143.7345677261)
                Line((0.7808697157, -3.8210263657), (0.7027229747, -3.4276023913))
                CenterArc((0, 0), 3.9, -78.45, 168.45)
                Line((0, 3.327), (0, 3.9))
                CenterArc((0, -0.2), 3.527, 6.2242500962, 83.7757499038)
                CenterArc((0, 0), 3.51095, -68.9648436936, 71.9427634937)
                Line((1.149952853, -3.1759376479), (1.2602229235, -3.276981551))
            make_face()
            with BuildLine():
                CenterArc((0.9675458142, -3.375), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a hollow cylindrical sleeve or tube with a uniform circular cross-section, featuring internal threading or grooved patterns visible on its inner and outer surfaces, likely designed for mechanical fastening or assembly purposes.
def model_23881_bec7f38c_0000():
    """Model: spacer center v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1101767271, perimeter: 20.7345115137
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.3
        extrude(amount=7.3)
    return part.part


# Description: This is a torus or ring-shaped washer featuring a smooth, curved circular band with a hollow center, commonly used as a spacer, seal, or fastener component in mechanical assemblies.
def model_23881_bec7f38c_0003():
    """Model: spacer small v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.7858401318, perimeter: 22.6194671058
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a ring or band-shaped component with a circular toroidal form featuring a uniform textured or ribbed surface pattern across its outer diameter, designed as a mechanical part with symmetrical geometry and no apparent holes or protrusions.
def model_23881_bec7f38c_0004():
    """Model: spacer drive side v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 20.106192983
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a 3D O-ring or circular seal featuring a toroidal (donut-shaped) cross-section, designed to create a watertight or airtight seal in mechanical assemblies.
def model_23881_bec7f38c_0010():
    """Model: crank bolt bushing v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7539822369, perimeter: 15.0796447372
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


# Description: This is a ring-shaped gear or friction ring with a circular band profile featuring diagonal linear ridges or teeth across its outer and inner surfaces for traction or engagement purposes.
def model_23881_bec7f38c_0012():
    """Model: spacer non-drive side v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.552544031, perimeter: 20.4203522483
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.85
        extrude(amount=0.85)
    return part.part


# Description: This is a rubber o-ring (seal) with a circular torus shape, featuring a uniform cross-section and smooth surface designed to create a watertight or airtight seal in mechanical assemblies.
def model_23881_bec7f38c_0015():
    """Model: bearing shield bushing v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1991148575, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 1.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a simple cylindrical rod or shaft with a straight, tapered or uniformly thin profile, featuring a clean, minimalist design with no visible holes, slots, or flanges.
def model_23910_316134bd_0011():
    """Model: outer blades v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.07351, perimeter: 3.0404
            with BuildLine():
                Line((1.4702, -0.05), (0, -0.05))
                Line((1.4702, 0), (1.4702, -0.05))
                Line((0, 0), (1.4702, 0))
                Line((0, -0.05), (0, 0))
            make_face()
        # OneSide extrude, distance=31.3
        extrude(amount=31.3)
    return part.part


# Description: This is a parallelogram-shaped flat plate or shim, characterized by its elongated rectangular form with slanted edges, featuring no holes, slots, or additional features—a simple geometric wedge or angled spacer component.
def model_23910_316134bd_0014():
    """Model: inner blades v1 (3)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1006665, perimeter: 3.7706
            with BuildLine():
                Line((1.8303, -0.055), (0, -0.055))
                Line((1.8303, 0), (1.8303, -0.055))
                Line((0, 0), (1.8303, 0))
                Line((0, -0.055), (0, 0))
            make_face()
        # OneSide extrude, distance=16.13
        extrude(amount=16.13)
    return part.part


# Description: This is a triangular fin or blade-shaped component with a pointed apex and a flat base, featuring a small rectangular slot or notch along its lower edge for mounting or assembly purposes.
def model_23913_b3ac2abf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 180.7402065417, perimeter: 65.8803462895
            with BuildLine():
                Line((22.5, 12.4063571016), (22.5, 0))
                Line((2.149423643, 4.1841905426), (22.5, 12.4063571016))
                Line((1.3907757819, 6.0619098901), (2.149423643, 4.1841905426))
                Line((0, 5.5), (1.3907757819, 6.0619098901))
                Line((0, 0), (0, 5.5))
                Line((22.5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a spheroidal or egg-shaped housing component with a smooth, rounded exterior featuring a central vertical slot or opening on one side and a ribbed or textured surface pattern across its cylindrical width.
def model_23956_ee17fe48_0003():
    """Model: Control Valve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a cylindrical sleeve or tube with a hollow center, featuring a closed rounded top end and an open bottom end, with a simple geometric form suitable for connector, bushing, or protective covering applications.
def model_24013_13d47495_0002():
    """Model: Bulon 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4005530633, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


# Description: This is a rectangular tray or container with an open top, featuring two vertical handle flanges on the opposing ends and a recessed rectangular slot running lengthwise through the center of the base.
def model_24032_d6172503_0005():
    """Model: catcher spacer stinger whe v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.7451085378, perimeter: 20.6067519129
            with BuildLine():
                Line((0, 2.54), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 2.54))
                Line((6, 2.54), (0, 2.54))
            make_face()
            with BuildLine():
                CenterArc((0.9, 1.27), 0.28065, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.1, 1.27), 0.28065, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)
    return part.part


# Description: This is a torus (donut-shaped ring) with a smooth, curved surface featuring a central hole and radial surface texturing or ribbing that creates a distinctive pattern across its upper and lower surfaces.
def model_24032_d6172503_0009():
    """Model: m8 washer v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.3412883482, perimeter: 10.5243353895
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a cylindrical sleeve or tube with a smooth, rounded body and slightly tapered or beveled edges at both ends, appearing to be a hollow tubular component, possibly used as a spacer, bushing, or protective cover.
def model_24032_d6172503_0014():
    """Model: slide spacer stinger whe v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7014527971, perimeter: 6.6551498774
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4242, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a thin, uniform thickness, featuring a simple geometric form without holes, slots, or other features—essentially a basic geometric solid used as a structural or mounting component.
def model_24032_d6172503_0028():
    """Model: plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((5.08, -5.08), (-5.08, -5.08))
                Line((5.08, 5.08), (5.08, -5.08))
                Line((-5.08, 5.08), (5.08, 5.08))
                Line((-5.08, -5.08), (-5.08, 5.08))
            make_face()
        # OneSide extrude, distance=0.4552
        extrude(amount=0.4552)
    return part.part


# Description: A cylindrical rubber puck with a flat top and bottom surface, tapered curved edges, and a textured surface pattern, commonly used in ice hockey.
def model_24032_d6172503_0031():
    """Model: left torion spring v3"""
    with BuildPart() as part:
        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1570796374, perimeter: 1.4049629671
            Circle(0.2236068011)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a rounded rectangular pad or cushion with a smooth, organic oblong shape featuring gently curved edges and a slightly domed top surface.
def model_24047_9eb475f0_0002():
    """Model: Case"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 19 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5.686391002, -1.5237568553, 4), x_dir=(0.984807753, -0.1736481777, 0), z_dir=(0, 0, 1))):
            # Profile area: 17.7263392592, perimeter: 56.5962330438
            with BuildLine():
                Line((-2.162801118, 8.035074615), (1.2278235892, 9.0676268391))
                CenterArc((0.167778672, 0.382075344), 8, -87.3758526764, 194.3129998683)
                Line((0.5340506763, -7.6095355586), (4.0746956466, -7.4472604998))
                CenterArc((0.167778672, 0.382075344), 8.75, -63.4803444902, 146.521983496)
            make_face()
            # Profile area: 27.4602057127, perimeter: 67.6841699227
            with BuildLine():
                CenterArc((25.8762651015, 4.8137599297), 12.25, 130.2485928735, 119.0641087687)
                Line((21.5487387074, -6.6463890793), (26.3913351076, -6.4244429021))
                CenterArc((25.8762651015, 4.8137599297), 11.25, 106.937147192, 165.6870001317)
                Line((17.96147597, 14.1635520666), (22.5988872718, 15.5757901546))
            make_face()
            # Profile area: 17.6144787275, perimeter: 51.9436584669
            with BuildLine():
                CenterArc((0.167778672, 0.382075344), 8.75, 83.0416390058, 24.4492335392)
                Line((1.2278235892, 9.0676268391), (17.96147597, 14.1635520666))
                CenterArc((25.8762651015, 4.8137599297), 12.25, 107.4908725449, 22.7577203285)
                Line((-2.4620676435, 8.7275177143), (22.1944802598, 16.4973792482))
            make_face()
            # Profile area: 21.7399184516, perimeter: 62.8245677302
            with BuildLine():
                CenterArc((0.167778672, 0.382075344), 8.75, 107.4908725449, 164.5795494257)
                CenterArc((0.167778672, 0.382075344), 8.75, -87.9295780294, 24.4492335392)
                Line((0.5340506763, -7.6095355586), (4.0746956466, -7.4472604998))
                CenterArc((0.167778672, 0.382075344), 8, 106.937147192, 165.6870001317)
                Line((-2.162801118, 8.035074615), (1.2278235892, 9.0676268391))
                CenterArc((0.167778672, 0.382075344), 8.75, 83.0416390058, 24.4492335392)
            make_face()
            # Profile area: 161.5681521919, perimeter: 82.8173128493
            with BuildLine():
                CenterArc((0.167778672, 0.382075344), 8.75, -63.4803444902, 146.521983496)
                Line((4.0746956466, -7.4472604998), (21.5487387074, -6.6463890793))
                CenterArc((25.8762651015, 4.8137599297), 12.25, 130.2485928735, 119.0641087687)
                Line((1.2278235892, 9.0676268391), (17.96147597, 14.1635520666))
            make_face()
            # Profile area: 46.3672216467, perimeter: 99.3614042257
            with BuildLine():
                Line((17.96147597, 14.1635520666), (22.5988872718, 15.5757901546))
                CenterArc((25.8762651015, 4.8137599297), 11.25, -87.3758526764, 194.3129998683)
                Line((21.5487387074, -6.6463890793), (26.3913351076, -6.4244429021))
                CenterArc((25.8762651015, 4.8137599297), 12.25, -110.6872983579, 22.7577203285)
                CenterArc((25.8762651015, 4.8137599297), 12.25, -87.9295780294, 195.4204505743)
                CenterArc((25.8762651015, 4.8137599297), 12.25, 107.4908725449, 22.7577203285)
            make_face()
            # Profile area: 17.6144787275, perimeter: 51.9436584669
            with BuildLine():
                Line((0.4838970669, -8.3622124578), (26.3188308543, -7.4282429928))
                CenterArc((25.8762651015, 4.8137599297), 12.25, -110.6872983579, 22.7577203285)
                Line((4.0746956466, -7.4472604998), (21.5487387074, -6.6463890793))
                CenterArc((0.167778672, 0.382075344), 8.75, -87.9295780294, 24.4492335392)
            make_face()
            # Profile area: 193.9933463592, perimeter: 59.6902604182
            with BuildLine():
                CenterArc((0.167778672, 0.382075344), 8, -87.3758526764, 194.3129998683)
                CenterArc((0.167778672, 0.382075344), 8, 106.937147192, 165.6870001317)
            make_face()
            with BuildLine():
                CenterArc((0.167778672, 0.382075344), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((0.167778672, 0.382075344)):
                Circle(1.5)
            # Profile area: 397.60782022, perimeter: 70.6858347058
            with BuildLine():
                CenterArc((25.8762651015, 4.8137599297), 11.25, 106.937147192, 165.6870001317)
                CenterArc((25.8762651015, 4.8137599297), 11.25, -87.3758526764, 194.3129998683)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a curved cylindrical sleeve or band with a split opening on one side, featuring a ribbed or corrugated exterior texture and a trapezoidal profile that tapers slightly toward one end.
def model_24047_9eb475f0_0008():
    """Model: Cams"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6598251405, perimeter: 8.8245351706
            with BuildLine():
                CenterArc((-0.9872307614, -5.9195920685), 1.5, -147.7837545798, 121.4017128369)
                Line((-1.3062586902, -8.2269483325), (-2.2562938251, -6.7192663399))
                CenterArc((-0.883237669, -7.960390242), 0.5, -26.3820417429, 238.5982871631)
                Line((-0.4353121297, -8.1825674489), (0.3565458564, -6.5861236892))
            make_face()
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((-0.883237669, -7.960390242), 0.5, -26.3820417429, 238.5982871631)
                CenterArc((-0.883237669, -7.960390242), 0.5, -147.7837545798, 121.4017128369)
            make_face()
            # Profile area: 2.1598449493, perimeter: 17.2787595947
            with BuildLine():
                CenterArc((-0.9872307614, -5.9195920685), 1.5, -26.3820417429, 238.5982871631)
                CenterArc((-0.9872307614, -5.9195920685), 1.5, -147.7837545798, 121.4017128369)
            make_face()
            with BuildLine():
                CenterArc((-0.9872307614, -5.9195920685), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a curved composite or layered structural component with a boat-shaped profile, featuring a ribbed or striped internal structure on the upper surface and a solid curved flange along the bottom edge.
def model_24051_4852a192_0003():
    """Model: Magnet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.4531865262, perimeter: 12.2193011838
            with BuildLine():
                CenterArc((0, 0), 4.9022, 58.008547412, 63.9829051761)
                Line((-2.59715, 4.1576888673), (-2.59715, 3.5316888673))
                Line((-2.59715, 3.5316888673), (-2.4041050381, 3.5316888673))
                CenterArc((0, 0), 4.2723, 55.7559453242, 68.4881093516)
                Line((2.4041050381, 3.5316888673), (2.59715, 3.5316888673))
                Line((2.59715, 4.1576888673), (2.59715, 3.5316888673))
            make_face()
        # Symmetric extrude, each_side=1.8669
        extrude(amount=1.8669, both=True)
    return part.part


# Description: This is a cylindrical rod or tube with a slightly tapered or rounded end, featuring a smooth, elongated shaft with no visible holes, slots, or flanges.
def model_24051_4852a192_0004():
    """Model: Rotor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4932742253, perimeter: 2.489712178
            Circle(0.39625)
        # Symmetric extrude, each_side=4.8641
        extrude(amount=4.8641, both=True)
    return part.part


# Description: This is a cylindrical sleeve or tube with a knurled (textured) end cap, featuring a smooth body and ridged grip pattern along its length.
def model_24070_485194e7_0004():
    """Model: Pivot v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0182414692, perimeter: 0.4787787204
            Circle(0.0762)
        # OneSide extrude, distance=0.6096
        extrude(amount=0.6096)
    return part.part


# Description: This is a cylindrical tube or pipe with a smooth, hollow interior and slightly tapered or rounded ends, oriented at a diagonal angle.
def model_24090_a2bf0d93_0001():
    """Model: Passador 2x12 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0324292787, perimeter: 0.6383716272
            Circle(0.1016)
        # OneSide extrude, distance=-1.1938
        extrude(amount=-1.1938)
    return part.part


# Description: This is a thin-walled, flat quadrilateral panel or plate with a trapezoidal shape, featuring a slight curved or bent edge along one side and subtle relief grooves or creases across its surface.
def model_24131_3ea7d5a8_0022():
    """Model: Forward Canard v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33.2257421208, perimeter: 23.9418900657
            with BuildLine():
                Line((-2.5400000811, 7.8740002513), (0, 7.8740002513))
                Line((-5.0800001621, 2.5400000811), (-2.5400000811, 7.8740002513))
                Line((-5.0800001621, 0), (-5.0800001621, 2.5400000811))
                Line((0, 0), (-5.0800001621, 0))
                Line((0, 7.8740002513), (0, 0))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a motorcycle or vehicle seat with an elongated, curved bean-like shape featuring a textured mesh side panel, a central longitudinal slot or depression running along the top surface, and integrated mounting points or attachment features on the underside.
def model_24146_08d7c016_0000():
    """Model: FLANGE SPRING v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.3795273174, perimeter: 22.6100518012
            with BuildLine():
                CenterArc((0, 0), 1.7275, 80.4829608629, 199.0340782743)
                Line((0.2856264205, -1.7037235098), (4.5653409091, -0.9862364746))
                CenterArc((4.4, 0), 1, -80.4829608629, 160.9659217257)
                Line((0.2856264205, 1.7037235098), (4.5653409091, 0.9862364746))
            make_face()
            with BuildLine():
                CenterArc((4.4, 0), 0.395, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.42, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a solid toroidal (doughnut-shaped) ring with a uniform cross-section, featuring a circular hole through its center and smooth, curved surfaces throughout.
def model_24195_9791f5d3_0003():
    """Model: Collar 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1206371579, perimeter: 3.0159289474
            with BuildLine():
                CenterArc((0, 0), 0.28, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a timing belt or drive belt with a cylindrical loop shape, featuring regularly spaced teeth or ribs on the inner surface for power transmission and grip.
def model_24195_9791f5d3_0004():
    """Model: Inner"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6597344573, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a flat, ring-shaped washer with a large central hole and a circular outer diameter, featuring a uniform thickness and slightly textured edges.
def model_24195_9791f5d3_0011():
    """Model: Washer 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.215120557, perimeter: 2.6075219025
            with BuildLine():
                CenterArc((0, 0), 0.29, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.06
        extrude(amount=0.06)
    return part.part


# Description: This is a hollow cylindrical bushing or spacer with a thick-walled tubular body featuring a centered through-hole and a curved, rounded top surface.
def model_24195_9791f5d3_0022():
    """Model: Damper 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2061670179, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 0), 0.325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a hexagonal hollow structural component with a central oval/elongated aperture and internal ribbed or latticed reinforcement structures, featuring faceted surfaces and geometric complexity throughout its body.
def model_24195_9791f5d3_0025():
    """Model: Bolt 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1071481381, perimeter: 2.0139591768
            with BuildLine():
                Line((0.2, -0.1154700538), (0.2, 0.1154700538))
                Line((0.2, 0.1154700538), (0, 0.2309401077))
                Line((0, 0.2309401077), (-0.2, 0.1154700538))
                Line((-0.2, 0.1154700538), (-0.2, -0.1154700538))
                Line((-0.2, -0.1154700538), (0, -0.2309401077))
                Line((0, -0.2309401077), (0.2, -0.1154700538))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a bicycle saddle featuring an elongated teardrop shape with a rounded nose, a curved seat surface with blue and gray coloring, textured grip areas at both ends, and integrated support rails running along the underside.
def model_24195_9791f5d3_0034():
    """Model: Servo Horn 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2973874848, perimeter: 5.8971284315
            with BuildLine():
                CenterArc((-1.6800002406, -0.0003102222), 0.2, 96.8477200801, 170.8026800877)
                Line((-1.6881995927, -0.2001420781), (-0.0476923763, -0.3971466193))
                CenterArc((0, 0), 0.4, -96.8477200801, 193.6954401601)
                Line((-1.7038464288, 0.1982630874), (-0.0476923763, 0.3971466193))
            make_face()
            with BuildLine():
                CenterArc((-1.28, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical connector or coupling component with a hexagonal or polygonal body on one end and a ribbed/finned circular flange on the opposite end, featuring angular faceted surfaces and horizontal linear grooves for structural reinforcement or aesthetic purposes.
def model_24195_9791f5d3_0035():
    """Model: Ball Link 5-2-2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.51670279, perimeter: 2.7025873712
            with BuildLine():
                Line((-0.175, -0.6), (0.175, -0.6))
                Line((0.175, -0.6), (0.333253516, -0.1069677245))
                CenterArc((0, 0), 0.35, -17.7955930343, 215.5911860685)
                Line((-0.175, -0.6), (-0.333253516, -0.1069677245))
            make_face()
        # Symmetric extrude, each_side=0.125
        extrude(amount=0.125, both=True)
    return part.part


# Description: This is a cylindrical sleeve or tube with a curved, slightly tapered body and an open top featuring a mesh or perforated rim, likely designed as a filter cartridge, air intake component, or similar cylindrical housing.
def model_24195_9791f5d3_0039():
    """Model: Inner (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a cylindrical barrel or sleeve component with a hexagonal or polygonal cross-section, featuring internal radial fins or blades, and flat end faces, likely designed for fluid flow, heat exchange, or mechanical containment purposes.
def model_24221_0b711dbf_0004():
    """Model: kabina"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 24.1415926536, perimeter: 18.2831853072
            with BuildLine():
                CenterArc((-1.5, -1.5), 1, 180, 90)
                Line((-1.5, -2.5), (1.5, -2.5))
                CenterArc((1.5, -1.5), 1, -90, 90)
                Line((2.5, -1.5), (2.5, 1.5))
                CenterArc((1.5, 1.5), 1, 0, 90)
                Line((1.5, 2.5), (-1.5, 2.5))
                CenterArc((-1.5, 1.5), 1, 90, 90)
                Line((-2.5, 1.5), (-2.5, -1.5))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


# Description: These are two complementary trapezoidal or wedge-shaped panels with light blue upper surfaces and dark gray sides, featuring angled edges and a geometric, faceted design that suggests they form part of an aerodynamic or structural assembly, possibly for a vehicle or industrial application.
def model_24221_0b711dbf_0005():
    """Model: skrzydla_t"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.7532095785, perimeter: 20.5319592008
            with BuildLine():
                CenterArc((8.5, -1.554921593), 0.5, 0, 90)
                Line((2.5, -1.054921593), (8.5, -1.054921593))
                Line((2.5, -1.054921593), (2.5, -5.8204907162))
                Line((7.4310976523, -4.7320115962), (2.5, -5.8204907162))
                CenterArc((7, -2.7790254688), 2, -77.5522722875, 77.5522722875)
                Line((9, -1.554921593), (9, -2.7790254688))
            make_face()
            # Profile area: 25.7532095785, perimeter: 20.5319592008
            with BuildLine():
                Line((-2.5, -1.054921593), (-8.5, -1.054921593))
                CenterArc((-8.5, -1.554921593), 0.5, 90, 90)
                Line((-9, -1.554921593), (-9, -2.7790254688))
                CenterArc((-7, -2.7790254688), 2, 180, 77.5522722875)
                Line((-7.4310976523, -4.7320115962), (-2.5, -5.8204907162))
                Line((-2.5, -1.054921593), (-2.5, -5.8204907162))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a bent metal bracket or angle piece with an L-shaped profile featuring two flat rectangular flanges connected at a 90-degree angle, with reinforcing ribs or webs along the inner bend for structural support.
def model_24230_636208ab_0005():
    """Model: fotel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6101846874, perimeter: 6.3097460355
            with BuildLine():
                CenterArc((1.5516486279, 2.3331380583), 0.05, 90, 74.123773602)
                Line((1.210932038, 1.3179319708), (1.5035558829, 2.3468160654))
                CenterArc((0.922375568, 1.4000000134), 0.3, -90, 74.123773602)
                Line((-0.350000006, 1.1000000134), (0.922375568, 1.1000000134))
                CenterArc((-0.350000006, 1.0500000134), 0.05, 90, 90)
                Line((-0.400000006, 1.0500000134), (-0.400000006, 0.9500000134))
                CenterArc((-0.350000006, 0.9500000134), 0.05, -180, 90)
                Line((-0.350000006, 0.9000000134), (1.0734253485, 0.9000000134))
                CenterArc((1.0734253485, 1.2000000134), 0.3, -90, 74.123773602)
                Line((1.3619818185, 1.1179319708), (1.7043499077, 2.3217199997))
                CenterArc((1.6562571627, 2.3353980068), 0.05, -15.876226398, 14.5812610328)
                CenterArc((1.6562571627, 2.3331380583), 0.05, 1.2949653652, 88.7050346348)
                Line((1.5516486279, 2.3831380583), (1.6562571627, 2.3831380583))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a cylindrical housing or connector body with a rounded, barrel-like shape featuring a rectangular mounting flange or base on one side and a hollow cylindrical bore running through its length.
def model_24230_636208ab_0009():
    """Model: lusterko"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2825162226, perimeter: 2.0801240775
            with BuildLine():
                Line((2.1000000328, 1.9000000283), (2.6000000417, 1.9000000283))
                CenterArc((2.6000000417, 2.1000000283), 0.2, -90, 90)
                Line((2.8000000417, 2.1000000283), (2.8000000417, 2.1795532519))
                CenterArc((2.6000000417, 2.1795532519), 0.2, 0, 90)
                Line((2.6000000417, 2.3795532519), (2.4000000328, 2.3795532519))
                CenterArc((2.4000000328, 2.1795532519), 0.2, 90, 90)
                Line((2.2000000328, 2.1795532519), (2.2000000328, 2.1500000283))
                CenterArc((2.1500000328, 2.1500000283), 0.05, -90, 90)
                Line((2.1000000328, 2.1000000283), (2.1500000328, 2.1000000283))
                Line((2.1000000328, 1.9000000283), (2.1000000328, 2.1000000283))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: A rounded rectangular bar or rod with a uniform cylindrical profile, featuring rounded ends and a smooth, elongated horizontal shape.
def model_24230_636208ab_0014():
    """Model: os"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-4.9368558505, 0.7)):
                Circle(0.15)
        # Symmetric extrude, each_side=2.6
        extrude(amount=2.6, both=True)
    return part.part


# Description: This is a rectangular prism or block with a flat top surface featuring two diagonal cross-braces or ribs that divide the face into four triangular sections, creating an X-pattern for structural reinforcement.
def model_24230_636208ab_0015():
    """Model: szyba_p"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1031632653, perimeter: 2.5861468101
            with BuildLine():
                Line((-1.3043763988, 2.5161844366), (-0.6412059058, 3.454427131))
                CenterArc((-0.6657040926, 3.4717429862), 0.03, -35.2535069321, 122.3573402801)
                CenterArc((-0.6614202605, 3.4017429862), 0.1, 91.5861775841, 53.1603154838)
                Line((-1.4168692936, 2.5061977546), (-0.7430808833, 3.4594625036))
                CenterArc((-1.2723356033, 1.5166978747), 1, 91.8361166131, 6.4741605544)
            make_face()
        # Symmetric extrude, each_side=1.6
        extrude(amount=1.6, both=True)
    return part.part


# Description: This is a ring or annular spacer with an oval/elliptical cross-section, featuring a hollow center opening and a textured or ribbed surface pattern on its outer band.
def model_24230_636208ab_0019():
    """Model: opony_t (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9738937226, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical foam roller with a hollow tubular body, rounded ends, and a textured surface pattern featuring linear grooves or ridges running along its length.
def model_24250_dd7e0408_0001():
    """Model: perno 6 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.97
        extrude(amount=0.97)
    return part.part


# Description: This is a cylindrical roller or shaft with a textured knurled surface pattern along its length, featuring rounded ends and a dark gray finish.
def model_24250_dd7e0408_0003():
    """Model: perno 7 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.89
        extrude(amount=0.89)
    return part.part


# Description: This is a cylindrical roller or shaft with a textured knurled surface running along its length, featuring rounded ends and a uniform diameter throughout.
def model_24250_dd7e0408_0007():
    """Model: perno 3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.85
        extrude(amount=0.85)
    return part.part


# Description: This is a cylindrical foam roller with a textured surface and rounded ends, featuring a hollow core design for exercise and muscle recovery applications.
def model_24250_dd7e0408_0009():
    """Model: perno 4 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=1.03
        extrude(amount=1.03)
    return part.part


# Description: This is a cylindrical foam roller with a textured, perforated surface featuring a hollow core design, typically used for muscle recovery and self-massage applications.
def model_24250_dd7e0408_0010():
    """Model: perno 5 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.93
        extrude(amount=0.93)
    return part.part


# Description: This is a cylindrical roller or shaft with a rounded hemispherical end on one side and a flat end on the other, featuring a textured or knurled surface pattern along its length.
def model_24250_dd7e0408_0011():
    """Model: perno 8 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.79
        extrude(amount=0.79)
    return part.part


# Description: This is a cylindrical roller or shaft with a knurled or textured surface along its length, featuring rounded ends and what appears to be technical specifications or markings embossed on its body.
def model_24250_dd7e0408_0017():
    """Model: perno 2 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a drone or aircraft chassis frame with an elongated diamond-shaped structure featuring four black motor mounting arms at the corners, a central blue structural body with geometric cutouts for weight reduction, and mounting points for electronics and components.
def model_24267_8a216138_0001():
    """Model: Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 72 constraints, 43 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.1789634221, perimeter: 76.9205617221
            with BuildLine():
                Line((0, -1.1115), (0, -2.762))
                CenterArc((0, -4.191), 1.429, -90, 180)
                Line((0, -5.62), (0, -6.001))
                CenterArc((0, -4.191), 1.81, -90, 58.0958180497)
                Line((1.5365689387, -5.1475855407), (2.4788916072, -5.5245146081))
                CenterArc((3.175, -5.461), 0.699, -174.7866303636, 236.5090225523)
                Line((3.5061471028, -4.8454168648), (3.5572777676, -2.5259439798))
                CenterArc((3.252, -1.968), 0.636, -61.3148272327, 46.2822770132)
                Line((3.8662352107, -2.1329578915), (6.3059726022, -1.4830893978))
                CenterArc((6.826, -1.016), 0.699, -138.0697696409, 267.09845157)
                Line((6.3858331665, -0.4729952498), (4.5649678032, 0.3360518114))
                CenterArc((3.252, 0.572), 1.334, -10.1876564274, 86.4187739067)
                Line((3.5695, 1.8676657555), (3.5695, 2.4892683162))
                CenterArc((3.252, 3.112), 0.699, -62.9852208772, 238.9300353713)
                CenterArc((0, 10.003), 7.303, -90, 20.476427812)
                Line((0, 2.7), (0, 1.1115))
                CenterArc((0, 0), 1.1115, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.492, 22.2623981436, 55.451017466)
                Line((0.3175, 1.4578263786), (0.3175, 2.0713521416))
                CenterArc((0, 10.003), 7.938, -87.7077016979, 18.3849465273)
                CenterArc((3.252, 3.112), 0.699, -129.974051709, 12.9592725862)
                Line((2.9345, 2.4892683162), (2.9345, 1.8676657555))
                CenterArc((3.252, 0.572), 1.334, 103.7688825207, 72.4380487117)
                Line((1.3807841524, 0.565242536), (1.9209221559, 0.6602483595))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.252, -1.968), 0.636, 119.9480014558, 64.4597017286)
                Line((1.2919023757, -2.9232901548), (2.6178810154, -2.016878557))
                CenterArc((0, -4.191), 1.81, 44.4584771042, 35.4387504319)
                Line((0.3175, -2.4090646055), (0.3175, -1.4578263786))
                CenterArc((0, 0), 1.492, -77.7134156096, 75.4026449723)
                Line((1.4907867554, -0.0601568782), (2.0309247589, 0.0348489453))
                CenterArc((3.252, 0.572), 1.334, -156.2553037261, 52.4864212053)
                Line((2.9345, -1.4169194705), (2.9345, -0.7236657555))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.252, -1.968), 0.636, 44.8634526921, 15.1885458521)
                Line((3.5695, -1.4169194705), (3.5695, -0.7236657555))
                CenterArc((3.252, 0.572), 1.334, -76.2311174793, 38.5056960103)
                Line((4.3071301383, -0.2442453009), (5.8748088699, -0.9407964552))
                Line((3.7027904072, -1.5193531358), (5.8748088699, -0.9407964552))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -4.191), 1.81, -11.6986370224, 35.9515691987)
                Line((1.6502512523, -3.4475144223), (2.9209564275, -2.5788866227))
                Line((2.8713013331, -4.8314222687), (2.9209564275, -2.5788866227))
                CenterArc((3.175, -5.461), 0.699, 115.7519504343, 15.4318609565)
                Line((1.7724020182, -4.558002842), (2.7147246867, -4.9349319094))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.175, -5.461), 0.2415, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.826, -1.016), 0.3162277707, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.252, -1.968), 0.2415, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.252, 0.572), 0.9525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.252, 3.112), 0.2415, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a conveyor belt or drive belt with an elliptical/oval toroidal shape, featuring a continuous loop design with ribbed or grooved texture on its outer surfaces and internal structural reinforcement ribs for strength and flexibility.
def model_24267_8a216138_0003():
    """Model: Small - Spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4275230366, perimeter: 10.4247340051
            with BuildLine():
                CenterArc((0, 0), 0.9525, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.74, 0), (-0.37, -0.6408587988))
                Line((-0.37, 0.6408587988), (-0.74, 0))
                Line((0.37, 0.6408587988), (-0.37, 0.6408587988))
                Line((0.74, 0), (0.37, 0.6408587988))
                Line((0.37, -0.6408587988), (0.74, 0))
                Line((-0.37, -0.6408587988), (0.37, -0.6408587988))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered or rounded end, featuring a smooth, uniform diameter along its length and a subtle conical tip at one end.
def model_24284_3710e946_0000():
    """Model: guide ++_D‚faut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.291863508, perimeter: 1.9151148816
            Circle(0.3048)
        # TwoSides extrude (symmetric), distance=5.0038
        extrude(amount=5.0038, both=True)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform diameter and rounded ends, featuring a slight diagonal orientation.
def model_24300_ed2686dc_0006():
    """Model: rurka_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.086393798, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


# Description: A hollow cylindrical vessel with an open top and closed bottom, featuring a slightly tapered or curved cylindrical sidewall and a flat or slightly curved base.
def model_24300_ed2686dc_0010():
    """Model: Lacznik"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a hollow rectangular box or duct component with a parallelogram profile, featuring open ends and thin walls, commonly used as a structural channel or air duct in assemblies.
def model_24300_ed2686dc_0011():
    """Model: obudowa_zarowki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1192274325, perimeter: 4.7484956009
            with BuildLine():
                CenterArc((0.03, -0.03), 0.03, 90, 90)
                Line((0, -0.03), (0, -0.2700000045))
                CenterArc((0.03, -0.2700000045), 0.03, 180, 90)
                Line((0.97, -0.3000000045), (0.03, -0.3000000045))
                CenterArc((0.97, -0.2700000045), 0.03, -90, 90)
                Line((1, -0.03), (1, -0.2700000045))
                CenterArc((0.97, -0.03), 0.03, 0, 90)
                Line((0.03, 0), (0.97, 0))
            make_face()
            with BuildLine():
                Line((0.0500000007, -0.2500000037), (0.0500000007, -0.0500000007))
                Line((0.0500000007, -0.0500000007), (0.9500000142, -0.0500000007))
                Line((0.9500000142, -0.0500000007), (0.9500000142, -0.2500000037))
                Line((0.9500000142, -0.2500000037), (0.0500000007, -0.2500000037))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a curved sheet metal or composite component with a dark gray U-shaped channel structure featuring two vertical flanges on either side and a blue central panel or membrane spanning between them.
def model_24300_ed2686dc_0014():
    """Model: lacznik_rurek"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1640081155, perimeter: 2.5816962484
            with BuildLine():
                Line((3.4928362829, -0.2298133329), (3.5892544244, -0.3447199994))
                CenterArc((3.3, 0), 0.45, -50, 179.4040185192)
                CenterArc((1.65, -8.7), 9.15, 79.6111421845, 1.813565438)
                CenterArc((3.3, 0), 0.3, -50, 140)
            make_face()
            # Profile area: 0.0380149465, perimeter: 0.9975641467
            with BuildLine():
                CenterArc((1.65, -8.7), 9.15, 79.6111421845, 1.813565438)
                CenterArc((3.3, 0), 0.45, 129.4040185192, 29.0998930531)
                CenterArc((1.65, -8.7), 8.95, 81.0927895264, 0.9996346868)
                CenterArc((3.3, 0), 0.3, 90, 61.7346977309)
            make_face()
            # Profile area: 0.0728662952, perimeter: 1.2774750334
            with BuildLine():
                CenterArc((1.65, -8.7), 8.95, 81.0927895264, 0.9996346868)
                CenterArc((3.3, 0), 0.45, 158.5039115723, 71.4960884277)
                Line((3.1071637171, -0.2298133329), (3.0107455756, -0.3447199994))
                CenterArc((3.3, 0), 0.3, 151.7346977309, 78.2653022691)
            make_face()
            # Profile area: 0.5165911306, perimeter: 5.6664446072
            with BuildLine():
                CenterArc((3.3, 0), 0.45, 129.4040185192, 29.0998930531)
                CenterArc((1.65, -8.7), 9.15, 81.4247076226, 17.1505847549)
                CenterArc((0, 0), 0.45, 21.4960884277, 29.0998930531)
                CenterArc((1.65, -8.7), 8.95, 82.0924242132, 15.8151515736)
            make_face()
            # Profile area: 0.0728662952, perimeter: 1.2774750334
            with BuildLine():
                CenterArc((1.65, -8.7), 8.95, 97.9075757868, 0.9996346868)
                CenterArc((0, 0), 0.3, -50, 78.2653022691)
                Line((0.1928362829, -0.2298133329), (0.2892544244, -0.3447199994))
                CenterArc((0, 0), 0.45, -50, 71.4960884277)
            make_face()
            # Profile area: 0.0380149465, perimeter: 0.9975641467
            with BuildLine():
                CenterArc((0, 0), 0.45, 21.4960884277, 29.0998930531)
                CenterArc((1.65, -8.7), 9.15, 98.5752923774, 1.813565438)
                CenterArc((0, 0), 0.3, 28.2653022691, 61.7346977309)
                CenterArc((1.65, -8.7), 8.95, 97.9075757868, 0.9996346868)
            make_face()
            # Profile area: 0.1640081155, perimeter: 2.5816962484
            with BuildLine():
                CenterArc((1.65, -8.7), 9.15, 98.5752923774, 1.813565438)
                CenterArc((0, 0), 0.45, 50.5959814808, 179.4040185192)
                Line((-0.1928362829, -0.2298133329), (-0.2892544244, -0.3447199994))
                CenterArc((0, 0), 0.3, 90, 140)
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


# Description: This is a bracket or connector part featuring a curved cylindrical opening on the left side and a vertical rectangular flange on the right, with a modern industrial design suitable for mechanical assembly or mounting applications.
def model_24315_6ffc3461_0002():
    """Model: seat clamp v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 79.059611834, perimeter: 73.1960249618
            with BuildLine():
                CenterArc((-10.0686775558, 0.3587934665), 5.0813605379, -4.0490085044, 4.0163178108)
                CenterArc((0, 0), 5, 180, 180)
                CenterArc((10.5046111119, 0.0972333329), 5.5054698087, -179.9513080682, 0.9632742501)
                CenterArc((10.5046111119, 0.0972333329), 5.5054698087, 117.0605207539, 62.9881711779)
                Line((8, 7), (8, 5))
                Line((-8, 7), (8, 7))
                Line((-8, 5), (-8, 7))
                CenterArc((-10.0686775558, 0.3587934665), 5.0813605379, -0.0326906936, 66.0092122621)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or washer with a smooth, curved elliptical cross-section and a large central void, featuring a textured or mesh-patterned surface finish on the outer edge.
def model_24330_a1e03326_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 329.8672286269, perimeter: 131.9468914508
            with BuildLine():
                CenterArc((0, 0), 13, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform hollow circular cross-section, featuring rounded ends and a slight taper or chamfer at the edges.
def model_24331_fb99e8e6_0003():
    """Model: Stop Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0481574788, perimeter: 1.5799697773
            with BuildLine():
                CenterArc((-0.1416717096, -0.8488034182), 0.15621, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.1416717096, -0.8488034182), 0.09525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: A horizontal cylindrical bar or rod with rounded ends and shallow parallel slot patterns or vents on both sides of its upper surface.
def model_24372_03b260fe_0014():
    """Model: pinA v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=-8.2
        extrude(amount=-8.2)
    return part.part


# Description: A rounded rectangular bar or rod with chamfered or rounded edges on both ends, appearing as a simple elongated cylindrical or prismatic element with a smooth, finished profile.
def model_24372_03b260fe_0016():
    """Model: pin v6"""
    with BuildPart() as part:
        # Sketch8 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-1, 2)):
                Circle(1)
        # OneSide extrude, distance=34
        extrude(amount=34)
    return part.part


# Description: This is a flat, trapezoidal or wedge-shaped panel with a tapered profile, featuring a thin raised flange or lip along one edge and a sloped upper surface, commonly used as a structural cover, baffle, or aerodynamic component.
def model_24372_03b260fe_0017():
    """Model: plate2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((4.5, -5), (1.5, -5))
                Line((4.5, -2), (4.5, -5))
                Line((1.5, -2), (4.5, -2))
                Line((1.5, -5), (1.5, -2))
            make_face()
        # OneSide extrude, distance=0.215
        extrude(amount=0.215)
    return part.part


# Description: This is a cylindrical capsule-shaped component with rounded ends, featuring a central longitudinal slot or channel running along its top surface and circular holes at each end.
def model_24372_03b260fe_0020():
    """Model: leather v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 62.0464549084, perimeter: 47.7460477568
            with BuildLine():
                CenterArc((-1, 2), 5.0990195136, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1, 2), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a teardrop-shaped or leaf-shaped hollow shell featuring a curved upper perimeter and a straight angled base, with uniform wall thickness throughout.
def model_24372_03b260fe_0025():
    """Model: pin ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.659205345, perimeter: 20.1544131098
            with BuildLine():
                CenterArc((0, 0), 1.75, -27.202894851, 234.4057897021)
                Line((1.5564382355, -0.8000000119), (-1.5564382355, -0.8000000119))
            make_face()
            with BuildLine():
                Line((-1.5491933338, -0.7000000104), (1.5491933338, -0.7000000104))
                CenterArc((0, 0), 1.7, -24.315739557, 228.6314791139)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical capsule-shaped housing or manifold block with rounded ends, featuring a central rectangular cavity or slot running along its length, and multiple small holes or ports distributed across its top and side surfaces for fluid/gas connections.
def model_24372_03b260fe_0029():
    """Model: leather2 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.0450550081, perimeter: 29.233788633
            with BuildLine():
                CenterArc((-4.5, 2), 3.3541019662, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.5, 2), 1.2986, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=14.9
        extrude(amount=14.9)
    return part.part


# Description: This is a blue and black aerodynamic fairing or body panel with a streamlined, elongated shape featuring curved surfaces and a tapered design typical of motorcycle or aircraft components.
def model_24405_b96b34b6_0000():
    """Model: Pieza 2.1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0378028691, perimeter: 10.3466997405
            with BuildLine():
                Line((1.4499979418, -1.7484521366), (1.4499979418, -2.2184521366))
                Line((0.8312949534, -2.1909467898), (1.4499979418, -2.2184521366))
                Line((0.8099979418, -2.19), (0.8312949534, -2.1909467898))
                CenterArc((0.8099979418, -2.43), 0.24, 90, 180)
                Line((2.7699979418, -2.77), (0.8099979418, -2.67))
                Line((2.7799979418, -2.57), (2.7699979418, -2.77))
                Line((2.7799979418, -2.57), (2.4803722402, -2.5550187149))
                CenterArc((2.5799979418, -2.24), 0.3303968389, 70.5531083201, 181.8971621586)
                Line((3.4499979418, -2.1184521366), (2.6899979418, -1.9284521366))
                Line((3.4499979418, -2.1184521366), (3.9499979418, -2.1384521366))
                Line((3.9599979418, -1.8484521366), (3.9499979418, -2.1384521366))
                Line((3.2099979418, -1.4884521366), (3.9599979418, -1.8484521366))
                Line((1.4499979418, -1.7484521366), (3.2099979418, -1.4884521366))
            make_face()
            with BuildLine():
                CenterArc((0.8099979418, -2.43), 0.1249979418, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a curved stapler with a distinctive hook-shaped design, featuring a dark gray/blue body with an arched upper arm, a flattened base platform, and a central slot mechanism for staple insertion and actuation.
def model_24405_b96b34b6_0001():
    """Model: Pieza 2.2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1204278033, perimeter: 11.5473592474
            with BuildLine():
                CenterArc((5.6999994246, -3.4197915522), 1.96, 45.5247719747, 42.9953211438)
                CenterArc((5.6399994246, -2.5397915522), 1.085, 84.1483192619, 84.83356972)
                Line((4.5749994246, -2.3324271386), (5.2749994246, -2.0897915522))
                CenterArc((5.4799994246, -2.0897915522), 0.205, 90, 90)
                Line((5.4799994246, -1.8847915522), (5.9741907049, -1.8755863137))
                CenterArc((5.9899994246, -2.2997915522), 0.4244997055, -105.0183606312, 197.1525963078)
                Line((5.6599994246, -2.4797915522), (5.8799994246, -2.7097915522))
                Line((5.5499994246, -2.5597915522), (5.6599994246, -2.4797915522))
                Line((5.6799994246, -2.9097915522), (5.5499994246, -2.5597915522))
                Line((5.6799994246, -2.9097915522), (7.6355436484, -3.0095642166))
                Line((7.6355436484, -3.0095642166), (7.6399994246, -3.0097915522))
                CenterArc((7.65, -2.77), 0.24, -92.3881529491, 184.7763058983)
                Line((7.0199994246, -2.5002084478), (7.6399994246, -2.5302084478))
                Line((7.073177038, -2.0212268443), (7.0199994246, -2.5002084478))
            make_face()
            with BuildLine():
                CenterArc((7.65, -2.77), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a slender, cylindrical ballpoint pen with a pointed tip at one end and a slightly wider grip section, featuring a smooth tapered design typical of a standard writing instrument.
def model_24405_b96b34b6_0002():
    """Model: Pieza 2.3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5044865074, perimeter: 10.4152936495
            with BuildLine():
                CenterArc((4.25, -3.4), 0.25, 0, 180)
                Line((4, -3.4), (4, -4.15))
                Line((4, -4.15), (4.15, -4.15))
                Line((4.15, -4.15), (4.15, -7.72))
                CenterArc((1.1819487613, -6.2363324596), 3.3182220429, -26.559520975, 25.9781731797)
                Line((4.5, -3.4), (4.5, -6.27))
            make_face()
            with BuildLine():
                CenterArc((4.25, -3.4), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a kayak or canoe hull featuring a symmetrical elongated design with a tapered profile, curved sides, and rounded ends, with blue fabric or material stretched across a dark frame structure.
def model_24405_b96b34b6_0007():
    """Model: Pieza 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.5426813534, perimeter: 22.4440980702
            with BuildLine():
                Line((3.8, -3.6), (7.7792230649, -3.6))
                CenterArc((7.7999992357, -2.8502878214), 0.75, -91.5873855963, 181.5873272084)
                Line((0.81, -1.7502878214), (7.8, -2.1002878214))
                CenterArc((0.8934, -2.6917), 0.9450991747, 95.0626344095, 103.976212764)
                Line((0, -3), (3.6, -3))
                Line((3.8, -3.6), (3.6, -3))
            make_face()
            with BuildLine():
                CenterArc((0.81, -2.43), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.35, -3.4), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.25, -3.4), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.65, -2.77), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is an elongated flat blade or strip with a tapered design, featuring a pointed left end and a slightly curved or angled right end, with a subtle groove or channel running along its length.
def model_24405_b96b34b6_0008():
    """Model: Pieza 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0748972614, perimeter: 18.2828395103
            with BuildLine():
                Line((0.2, -3.1), (0.2, -2.66))
                Line((0.2, -3.1), (4.25, -3.1))
                CenterArc((4.25, -3.4), 0.3, 0, 90)
                Line((4.55, -3.4), (4.55, -3.7))
                Line((4.55, -3.7), (7.8, -3.7))
                CenterArc((7.7999992357, -2.8502878214), 0.8497121786, -89.9999484638, 26.5648371845)
                Line((8.2299994246, -3.0602945309), (8.1799999193, -3.6102945759))
                Line((0.2, -2.66), (8.2299994246, -3.0602945309))
            make_face()
            with BuildLine():
                CenterArc((5.35, -3.4), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a tapered needle or pin tool with a long, slender cylindrical shaft that gradually tapers to a sharp point, featuring a slightly enlarged grip or mounting section near the left end.
def model_24405_b96b34b6_0009():
    """Model: Pieza 4.2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4541457104, perimeter: 12.1023257605
            with BuildLine():
                Line((12.8446026234, -3.6397100025), (12.9946026234, -3.3697100025))
                Line((10.0446026234, -1.7397100025), (12.9946026234, -3.3697100025))
                CenterArc((10.1146026234, -1.8497100025), 0.1303840481, 122.4711922908, 115.0576154183)
                Line((10.0446026234, -1.9597100025), (10.0588374575, -1.9675668914))
                Line((10.0588374575, -1.9675668914), (11.5564217578, -2.7941556286))
                CenterArc((9.9046026234, -4.4797100025), 2.36, 29.2949107631, 16.2842335885)
                CenterArc((15.2546026234, 0.0802899975), 4.7362115662, -134.0296888651, 36.0193446097)
                Line((12.8446026234, -3.6397100025), (14.5946026234, -4.6097100025))
            make_face()
            with BuildLine():
                CenterArc((12.4946026234, -3.4497100025), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a tapered cylindrical stylus pen with a rounded tip at one end and a slightly flattened grip section, designed for precision touch input on digital devices.
def model_24405_b96b34b6_0012():
    """Model: Pieza 6.2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.082305023, perimeter: 11.3484620586
            with BuildLine():
                CenterArc((4.15, -7.37), 0.3500000618, -106.7119588255, 106.7460182794)
                Line((4.5, -3.4), (4.5, -7.3697919426))
                CenterArc((4.25, -3.4), 0.25, 0, 180)
                Line((4, -3.4), (4, -7.21))
                CenterArc((3.8, -7.48), 0.3360059523, -42.088417768, 95.559562401)
            make_face()
            with BuildLine():
                CenterArc((4.25, -3.4), 0.1250001149, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3200000618, -7.22), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a curved bracket or support arm with a horizontal S-shaped profile, featuring mounting holes at each end and a central reinforcing web, designed to provide structural support or cable routing.
def model_24405_b96b34b6_0013():
    """Model: Pieza 4.1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8347847959, perimeter: 18.537408203
            with BuildLine():
                Line((8.1882053095, -3.7597100025), (10.2282053095, -3.7597100025))
                CenterArc((11.0614039665, -2.2202710915), 1.7504548444, -118.4238155989, 56.8476311978)
                Line((11.8946026234, -3.7597100025), (12.8946026234, -3.7597100025))
                Line((12.8946026234, -3.7597100025), (12.8946026234, -3.4497100025))
                Line((12.8946026234, -3.4497100025), (14.6237090728, -3.4497100025))
                CenterArc((13.1007641936, -7.9402710915), 4.7417823653, 71.2659638506, 20.3050455626)
                Line((12.0507641936, -3.2002710915), (12.9707641936, -3.2002710915))
                CenterArc((11.1914039665, -2.3202710915), 1.23, -90, 44.320142915)
                Line((9.2914039665, -3.5502710915), (11.1914039665, -3.5502710915))
                Line((9.2914039665, -3.3002710915), (9.2914039665, -3.5502710915))
                Line((8.7514039665, -3.3002710915), (9.2914039665, -3.3002710915))
                Line((8.7514039665, -2.5802710915), (8.7514039665, -3.3002710915))
                Line((8.7514039665, -2.5802710915), (7.6614039665, -2.5302710915))
                CenterArc((7.65, -2.77), 0.24, 87.2764780258, 179.9999991462)
                Line((8.2582053095, -3.0397100025), (7.63859603, -3.0097289083))
                Line((8.1882053095, -3.7597100025), (8.2582053095, -3.0397100025))
            make_face()
            with BuildLine():
                CenterArc((12.4946026234, -3.4497100025), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.65, -2.77), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a ski or snowboard with a tapered, elongated design, featuring a curved profile with black binding areas at both ends and a blue central core, designed for winter sports performance.
def model_24405_b96b34b6_0014():
    """Model: Pieza 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.8458395623, perimeter: 23.9344290395
            with BuildLine():
                Line((3.73, -3.7), (7.8, -3.7))
                CenterArc((7.8, -2.85), 0.85, -90, 180)
                Line((7.8, -2), (7.1363794895, -1.9702856488))
                CenterArc((5.9, -1.68), 1.27, -96.1466650221, 82.9336876974)
                Line((5.7640161689, -2.9426988547), (2.92, -2.79))
                CenterArc((2.92, -0.17), 2.62, -145.4961798628, 55.4961798628)
                CenterArc((0.89, -2.69), 1.0438869671, 97.1047399401, 106.0217804486)
                Line((3.53, -3.1), (-0.07, -3.1))
                Line((3.73, -3.7), (3.53, -3.1))
            make_face()
            with BuildLine():
                CenterArc((7.65, -2.77), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.35, -3.4), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.25, -3.4), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.81, -2.43), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.035
        extrude(amount=0.035)
    return part.part


# Description: A tapered cylindrical pen with a rounded tip at one end and a slightly textured grip section, designed for touch-screen input on digital devices.
def model_24405_b96b34b6_0015():
    """Model: Pieza 4.3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5632499299, perimeter: 11.2288701142
            with BuildLine():
                Line((4.3200000618, -7.72), (4.5000000618, -7.37))
                Line((4.5, -3.4), (4.5000000618, -7.37))
                CenterArc((4.25, -3.4), 0.25, 0, 180)
                Line((4, -3.4), (4, -4.15))
                Line((4, -4.15), (4.15, -4.15))
                Line((4.1500000618, -7.37), (4.15, -4.15))
                Line((4.3200000618, -7.72), (4.1500000618, -7.37))
            make_face()
            with BuildLine():
                CenterArc((4.3200000618, -7.22), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.25, -3.4), 0.1250001149, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a long, slender metal pry bar or lever tool with an angled blade at one end and a flat, tapered shaft that curves slightly upward, designed for prying, lifting, or separating materials.
def model_24405_b96b34b6_0016():
    """Model: Pieza 6 = Pieza 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.528883219, perimeter: 19.7386757784
            with BuildLine():
                Line((4.55, -3.4), (4.55, -3.7))
                Line((4.55, -3.7), (7.8, -3.7))
                CenterArc((7.7999992357, -2.8502878214), 0.8497121786, -89.9999484638, 26.5648371845)
                Line((8.2299994246, -3.0602945309), (8.1799999193, -3.6102945759))
                Line((8.2299994246, -3.0602945309), (0.77, -2.6932327327))
                CenterArc((2.41, -0.65), 2.62, -149.9545471771, 21.2022897728)
                CenterArc((0.89, -2.69), 1.0438869671, 135.7663913183, 67.3601290704)
                Line((-0.07, -3.1), (4.25, -3.1))
                CenterArc((4.25, -3.4), 0.3, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((5.35, -3.4), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a ribbonfish or elongated marine creature, characterized by an extremely thin, flat, blade-like body with a dark blue-gray coloration, tapering to a pointed tail end and featuring subtle curved fins along its length.
def model_24405_b96b34b6_0017():
    """Model: Pieza 6.1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2637253988, perimeter: 16.5980790095
            with BuildLine():
                CenterArc((12.0430430562, 4.8296453185), 8.6058806517, -85.50031629, 13.6145912824)
                CenterArc((11.4655341856, -11.6096908757), 8.8775268326, 68.5030062968, 16.9364785215)
                Line((12.1714039665, -2.7602710915), (11.663586697, -2.7343735368))
                Line((11.663586697, -2.7343735368), (7.6630430562, -2.5303546815))
                Line((7.6630430562, -2.5303546815), (7.6614039665, -2.5302710915))
                CenterArc((7.65, -2.77), 0.24, 87.2764780258, 179.9999991462)
                Line((7.63859603, -3.0097289083), (8.2582053095, -3.0397100025))
                Line((8.2582053095, -3.0397100025), (8.1882053095, -3.7597100025))
                Line((12.7182053095, -3.7497100025), (8.1882053095, -3.7597100025))
            make_face()
            with BuildLine():
                CenterArc((7.65, -2.77), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a smooth, curved surface and a central circular hole, featuring a uniform cross-section throughout its circumference.
def model_24412_a8e106be_0004():
    """Model: Abstandsscheibe2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5105088062, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)
    return part.part


# Description: This is a curved, ring-like composite structure featuring a textured mesh or lattice upper section with blue faceted surfaces, transitioning into a smooth, solid dark cylindrical base, resembling an aerodynamic or ergonomic component with integrated ribbed reinforcement.
def model_24412_a8e106be_0005():
    """Model: Kurbel"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3888650188, perimeter: 9.6695333988
            with BuildLine():
                CenterArc((0, -0.4059443787), 1.5, 179.7729408662, 180.4541182676)
                Line((1.4999882214, -0.4), (0.55, 0))
                Line((0.55, 0), (0.3937070517, 0.870673598))
                CenterArc((0, 0.8), 0.4, 10.1766711305, 159.646657739)
                Line((-0.55, 0), (-0.3937070517, 0.870673598))
                Line((-1.4999882214, -0.4), (-0.55, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a snowboard with a symmetrical elongated shape featuring a blue mountain graphic design on the top surface, dark base, and curved upturned edges (rocker) at both ends for maneuverability and pop.
def model_24412_a8e106be_0006():
    """Model: Pleuel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.048087659, perimeter: 11.5302841343
            with BuildLine():
                Line((2.9, -0.3), (3.5, -0.3))
                CenterArc((3.5, 0), 0.3, -90, 180)
                Line((2.9, 0.3), (3.5, 0.3))
                CenterArc((2.5127016654, 1), 0.8, -90, 28.9550243719)
                Line((1.1291502622, 0.2), (2.5127016654, 0.2))
                CenterArc((1.1291502622, 1), 0.8, -131.4096221093, 41.4096221093)
                Line((0, 0.4), (0.6, 0.4))
                CenterArc((0, 0), 0.4, 90, 180)
                Line((0, -0.4), (0.6, -0.4))
                CenterArc((1.1291502622, -1), 0.8, 90, 41.4096221093)
                Line((1.1291502622, -0.2), (2.5127016654, -0.2))
                CenterArc((2.5127016654, -1), 0.8, 61.0449756281, 28.9550243719)
            make_face()
            with BuildLine():
                CenterArc((3.5, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a curved, box-like composite part with a saddle or boat-shaped profile, featuring a hollow underside, angled side walls, and a ribbed or faceted top surface with multiple triangulated panels.
def model_24412_a8e106be_0009():
    """Model: Grundplatte"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 41, perimeter: 26.4
            with BuildLine():
                Line((4.1, -2.5), (-4.1, -2.5))
                Line((4.1, 2.5), (4.1, -2.5))
                Line((-4.1, 2.5), (4.1, 2.5))
                Line((-4.1, -2.5), (-4.1, 2.5))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a tapered wedge profile, featuring a dark beveled or chamfered edge on one side and a slightly curved or faceted upper surface.
def model_24412_a8e106be_0010():
    """Model: Zylinderkopf"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.6, perimeter: 9.6
            with BuildLine():
                Line((1.4, -1), (-1.4, -1))
                Line((1.4, 1), (1.4, -1))
                Line((-1.4, 1), (1.4, 1))
                Line((-1.4, -1), (-1.4, 1))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a truncated octahedron or cuboctahedron-like polyhedron with a symmetrical geometric structure featuring multiple flat rectangular and square faces arranged in a regular pattern with internal edge divisions visible throughout.
def model_24415_217d80f6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch28 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0221831038, perimeter: 0.5544169034
            with BuildLine():
                Line((0.607603505, -0.1010800113), (0.6547370737, -0.1805577273))
                Line((0.6547370737, -0.1805577273), (0.7471335791, -0.1794777175))
                Line((0.7471335791, -0.1794777175), (0.7923965158, -0.0989199916))
                Line((0.7923965158, -0.0989199916), (0.7452629472, -0.0194422757))
                Line((0.7452629472, -0.0194422757), (0.6528664417, -0.0205222855))
                Line((0.6528664417, -0.0205222855), (0.607603505, -0.1010800113))
            make_face()
        # OneSide extrude, distance=0.09
        extrude(amount=0.09)
    return part.part


# Description: This is a black and blue polymer or composite arm guard/gaiter with a curved, anatomical shape designed to wrap around a limb, featuring tapered ends with elastic or strap attachment points and textured surface patterns for grip or durability.
def model_24430_90535b35_0000():
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
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1670.3411041469, perimeter: 298.4808388984
            with BuildLine():
                Line((15.0004706632, 4.9985880103), (16, 2))
                _nurbs_edge([(-4.8167242799, -14.8228635665), (-4.8083877842, -14.9672895748), (-4.7817691126, -15.2490650569), (-4.71200787, -15.6504976378), (-4.55918531, -16.1432119413), (-4.2712705245, -16.6868114412), (-3.8953445796, -17.1548267216), (-3.4511847687, -17.540945258), (-2.9689561704, -17.8361707066), (-2.4764454853, -18.0324543246), (-1.9883885988, -18.1258806325), (-1.4957345797, -18.1196113399), (-0.9764805225, -18.0158930134), (-0.4056571106, -17.8082264614), (0.2349742983, -17.4742405379), (0.9575891651, -16.9831339706), (1.7682966939, -16.3021174355), (2.667303968, -15.4035004641), (3.6490085907, -14.2709687482), (4.7018940845, -12.9078457354), (5.809312297, -11.3366434642), (6.9506824343, -9.5946126866), (8.1025158217, -7.7307130563), (9.2394787038, -5.8021322986), (10.3354208627, -3.8710933745), (11.3644055486, -2.0016189142), (12.3017600542, -0.2563011002), (13.1251038063, 1.3068529546), (13.8154990402, 2.6378705542), (14.3584113291, 3.6977324352), (14.7378932686, 4.4482846917), (14.9184239272, 4.8134947962), (14.9851908305, 4.9556529528), (14.999983095, 4.9932651689), (15.0004706632, 4.9985880103)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 0.9968185115, 0.9968185115, 0.9968185115, 0.9968185115, 0.9968185115, 0.9968185115], 5)
                Line((-4.8167242799, -18.1653768318), (-4.8167242799, -14.8228635665))
                Line((-12.3314127464, -18.1653768318), (-4.8167242799, -18.1653768318))
                Line((-12.3314127464, -10.6331344593), (-12.3314127464, -18.1653768318))
                _nurbs_edge([(-12.3314127464, -10.6331344593), (-12.4004182606, -10.7289179211), (-12.538201796, -10.9163318151), (-12.7441957976, -11.1849940888), (-13.017478052, -11.518223786), (-13.3584431298, -11.8929010142), (-13.7035976351, -12.2256524751), (-14.0630111432, -12.517014724), (-14.4525002247, -12.7678854002), (-14.8861563854, -12.9754329412), (-15.370682033, -13.1300800969), (-15.89730544, -13.2107588808), (-16.446299112, -13.1899005995), (-16.9946591268, -13.0409574622), (-17.5226014404, -12.7450384504), (-18.0207050881, -12.2981982555), (-18.4875713202, -11.7078157285), (-18.9275061049, -10.9890312936), (-19.3482052643, -10.161218247), (-19.758642816, -9.2447787071), (-20.166540559, -8.2573293453), (-20.5775497835, -7.2124788816), (-20.9958210793, -6.1207086761), (-21.4241608061, -4.9896445162), (-21.8643394693, -3.8245690318), (-22.3173182353, -2.6288222689), (-22.6902602893, -1.6491595596), (-22.975933934, -0.9017801641), (-23.1690282028, -0.3979275292), (-23.2662366286, -0.1446012813)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((-23.2662366286, -0.1446012813), (-24.3936537552, -2.6479240158))
                Line((-24.3936537552, -2.6479240158), (-19.272966041, -32.4384579462))
                _nurbs_edge([(-19.272966041, -32.4384579462), (-19.2539381027, -32.5185333092), (-19.2174051109, -32.688123203), (-19.1673438887, -32.9709815171), (-19.1085848564, -33.403901964), (-19.099188901, -34.0855967799), (-19.2559980596, -35.0024863006), (-19.6672129541, -36.2352797917), (-20.3679369838, -37.8140647143), (-21.3549248318, -39.732476323), (-22.5954795135, -41.9562368593), (-24.0375963716, -44.4328386414), (-25.61905401, -47.10016772), (-27.2761387183, -49.8947483901), (-28.9531258786, -52.7606273688), (-30.6087667427, -55.6554704663), (-32.2128701102, -58.5475348029), (-33.7447373134, -61.414308981), (-35.1910814763, -64.240651522), (-36.5443791213, -67.0173008369), (-37.8012350676, -69.7393748058), (-38.7289856513, -71.8718837843), (-39.3813288359, -73.4458034358), (-39.7969831451, -74.4838128729), (-40, -75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-40, -75), (-40, -80))
                _nurbs_edge([(-40, -80), (-39.578310782, -79.5104550081), (-38.7354713565, -78.5399621512), (-37.4728291848, -77.110014238), (-35.7925466376, -75.2550932332), (-33.6977859772, -73.0232886283), (-31.6091455832, -70.8795440802), (-29.5276198526, -68.8255644029), (-27.4548686155, -66.8635310665), (-25.3932650629, -64.9960795874), (-23.3463170745, -63.2262569009), (-21.3178499622, -61.5574928282), (-19.3090958727, -59.9935915559), (-17.3164020403, -58.5387130386), (-15.3283395741, -57.1973147645), (-13.3237389952, -55.9741446538), (-11.2673799993, -54.8740470906), (-9.1192201036, -53.9027569134), (-6.8469380193, -53.0678820696), (-4.43841028, -52.3799604555), (-1.912135655, -51.8531357587), (0.6657530517, -51.5068248797), (3.1878649259, -51.3637864305), (5.5365290932, -51.4445024208), (7.6096214397, -51.7621369117), (9.3453775581, -52.3179346507), (10.755691784, -53.0944455872), (11.9289618672, -54.0560553683), (12.9833725254, -55.1613733403), (14.0332342223, -56.3724410008), (15.1475228705, -57.6659246909), (16.1173931809, -58.7571859151), (16.8938241276, -59.605503534), (17.4331894668, -60.184302741), (17.708308669, -60.4770157732)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                Line((17.708308669, -60.4770157732), (18.573606529, -55.2234306657))
                Line((18.573606529, -55.2234306657), (8.6155125438, -32.6446012813))
                _nurbs_edge([(16, 2), (15.7972042393, 1.1424611314), (15.3985126975, -0.5431851905), (14.8211753077, -2.9833604974), (14.0929001084, -6.0598779489), (13.2524183785, -9.6075433747), (12.482745816, -12.8532233117), (11.7849261183, -15.7925358866), (11.1599100377, -18.4215428582), (10.608342098, -20.7376719021), (10.1303211098, -22.7407507018), (9.7251341481, -24.4341554644), (9.3909578357, -25.8260974924), (9.124534285, -26.9310225998), (8.9207978315, -27.7712108726), (8.7725016405, -28.3784004956), (8.6697245897, -28.7958686986), (8.5995326971, -29.0799793084), (8.5451311754, -29.3035941422), (8.4866098326, -29.5537996106), (8.417037455, -29.8756449474), (8.3492654658, -30.2481030705), (8.3019057166, -30.6315217882), (8.286818752, -31.0102849873), (8.3086969648, -31.3912426504), (8.3689659875, -31.7864071235), (8.4482216301, -32.1186911697), (8.5251035954, -32.3778035459), (8.5840878978, -32.5549368798), (8.6155125438, -32.6446012813)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a parallelogram-shaped plate or panel with a uniform thickness, featuring a trapezoidal profile when viewed from the side, with clean flat surfaces and sharp edges typical of a stamped or extruded metal component.
def model_24443_996411f9_0002():
    """Model: Frame & Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 129, perimeter: 47.2
            with BuildLine():
                Line((-7.5, 4.3), (7.5, 4.3))
                Line((-7.5, -4.3), (-7.5, 4.3))
                Line((7.5, -4.3), (-7.5, -4.3))
                Line((7.5, 4.3), (7.5, -4.3))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat parallelogram-shaped panel or plate with a grid of rectangular cutouts or slots arranged in a 2x3 pattern across its surface, featuring raised edges or flanges around the perimeter.
def model_24448_75004b6c_0005():
    """Model: P02-BASE PLATE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 39 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 47.6975222039, perimeter: 39.3097335529
            with BuildLine():
                Line((3.8, -3.2), (-3.8, -3.2))
                Line((3.8, 3.2), (3.8, -3.2))
                Line((-3.8, 3.2), (3.8, 3.2))
                Line((-3.8, -3.2), (-3.8, 3.2))
            make_face()
            with BuildLine():
                CenterArc((3.3, -2.4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.3, -2.4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 2.7), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.4, -2.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.4, -2.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.4, 0.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.4, 0.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.26, 0.7), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.26, 2.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.26, 2.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.26, 0.7), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cube-shaped structural frame or enclosure with an open top, featuring internal diagonal bracing/truss members, reinforced corners, and what appears to be access panels or cutouts on the sides.
def model_24448_75004b6c_0006():
    """Model: P04-CRANK SHAFT BEARING HOLDER"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 26 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.4286283306, perimeter: 11.0771739041
            with BuildLine():
                Line((1.9, -2), (-1.9, -2))
                Line((-1.67, -3), (-1.9, -2))
                Line((1.67, -3), (-1.67, -3))
                Line((1.67, -3), (1.9, -2))
            make_face()
            with BuildLine():
                CenterArc((1.4, -2.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.4, -2.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 8.7400002435, perimeter: 12.2000001281
            with BuildLine():
                Line((-1.9, 0.3000000641), (1.9, 0.3000000641))
                Line((-1.9, -2), (-1.9, 0.3000000641))
                Line((1.9, -2), (-1.9, -2))
                Line((1.9, 0.3000000641), (1.9, -2))
            make_face()
            # Profile area: 3.4286283306, perimeter: 11.0771739041
            with BuildLine():
                Line((-1.67, 1.3000000641), (-1.9, 0.3000000641))
                Line((-1.9, 0.3000000641), (1.9, 0.3000000641))
                Line((1.67, 1.3000000641), (1.9, 0.3000000641))
                Line((-1.67, 1.3000000641), (1.67, 1.3000000641))
            make_face()
            with BuildLine():
                CenterArc((-1.4, 0.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.4, 0.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a parallelpiped or skewed rectangular prism with a uniform cross-section, featuring flat faces and sharp edges throughout, with no holes, slots, or curved surfaces.
def model_24448_75004b6c_0007():
    """Model: P01-WOODEN BASE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 72, perimeter: 34
            with BuildLine():
                Line((4.5, -4), (-4.5, -4))
                Line((4.5, 4), (4.5, -4))
                Line((-4.5, 4), (4.5, 4))
                Line((-4.5, -4), (-4.5, 4))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform hollow circular cross-section, featuring a slightly tapered or textured end cap at the top and a clean open end at the bottom.
def model_24470_21c25a2d_0002():
    """Model: Shaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


# Description: This is a cylindrical sleeve or tube with a smooth outer surface, rounded ends, and subtle ribbed or textured detailing along its edges, designed as a hollow structural component or connector.
def model_24470_21c25a2d_0003():
    """Model: Bush v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9792033718, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a hexagonal or octagonal-shaped container or enclosure with a central elongated slot or opening running across its top face and triangular faceted surfaces on its ends, suggesting a geometric design for structural efficiency or aesthetic purposes.
def model_24470_21c25a2d_0008():
    """Model: Nut v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4136764459, perimeter: 14.741205313
            with BuildLine():
                Line((1.3115, -0.757194878), (1.3115, 0.757194878))
                Line((1.3115, 0.757194878), (0, 1.5143897561))
                Line((0, 1.5143897561), (-1.3115, 0.757194878))
                Line((-1.3115, 0.757194878), (-1.3115, -0.757194878))
                Line((-1.3115, -0.757194878), (0, -1.5143897561))
                Line((0, -1.5143897561), (1.3115, -0.757194878))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered, rounded top end and a uniform hollow body, appearing to be a simple tubular component with an angled orientation.
def model_24470_21c25a2d_0009():
    """Model: King-pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a pair of blue and black wing-shaped hydrofoil or fin components with curved, tapered profiles, internal rib structures for reinforcement, and dark end caps or flanges.
def model_24472_5019aefa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.9405609082, perimeter: 30.2829189369
            with BuildLine():
                Line((1.2000000006, 0.0000379498), (1.2000000006, -1.6059620502))
                CenterArc((1.9000000006, -1.6059620502), 0.7, 180, 73.9246781605)
                Line((1.7061694368, -2.2785910062), (3.6251694368, -2.2785910062))
                CenterArc((3.6251694368, -1.5785910062), 0.7, -90, 95.7916969842)
                Line((4.3215961769, -1.5079525201), (4.3215961769, 1.4160474799))
                CenterArc((3.6215961769, 1.4160474799), 0.7, 0, 89.5321500662)
                CenterArc((0.0000000006, -22.5954734467), 24.9762988718, 81.6493923078, 16.7012153845)
                CenterArc((-3.6215961757, 1.4160474799), 0.7, 90.4678499338, 89.5321500662)
                Line((-4.3215961757, -1.5079525201), (-4.3215961757, 1.4160474799))
                CenterArc((-3.6251694356, -1.5785910062), 0.7, 174.2083030158, 95.7916969842)
                Line((-1.7061694356, -2.2785910062), (-3.6251694356, -2.2785910062))
                CenterArc((-1.8999999994, -1.6059620502), 0.7, -73.9246781605, 73.9246781605)
                Line((-1.1999999994, 0.0000379498), (-1.1999999994, -1.6059620502))
                CenterArc((0.0000000006, 0.0000379498), 1.2, 0, 180)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is an elongated, hexagonal-profile component with a tapered left end, featuring a central longitudinal slot or depression running along its length, and angled faceted surfaces characteristic of a geometric, low-polygon design aesthetic.
def model_24476_568e9ca0_0006():
    """Model: reifenheber v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0444925802, perimeter: 6.6437812755
            with BuildLine():
                Line((0, 0), (3, 0))
                Line((3, 0), (3, 0.2233547646))
                Line((2.1818302128, 0.3733668438), (3, 0.2233547646))
                Line((0.5124657175, 0.3467336876), (2.1818302128, 0.3733668438))
                Line((0.3000000045, 0.4), (0.5124657175, 0.3467336876))
                Line((0, 0.4), (0.3000000045, 0.4))
                Line((0, 0), (0, 0.4))
            make_face()
        # OneSide extrude, distance=0.45
        extrude(amount=0.45)
    return part.part


# Description: This is a cable stripper tool with a prominent circular loop handle on the left, a tapered blade section in the center, and a flat body with notched cutting edges along the right side for stripping insulation from electrical wires of various gauges.
def model_24476_568e9ca0_0015():
    """Model: apribottiglie v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2749262705, perimeter: 11.1700952218
            with BuildLine():
                Line((0.6108789253, 0.020485339), (0.574348255, 0.1394448671))
                Line((0.574348255, 0.1394448671), (0.7296805566, 0.1394448671))
                CenterArc((0.7296805566, 0.1494448671), 0.01, -90, 107.0709295757)
                Line((0.7392399774, 0.1523804205), (0.7028061476, 0.2710245942))
                CenterArc((0.6789075956, 0.2636857106), 0.025, 17.0709295757, 72.9290704243)
                Line((0.6789075956, 0.2886857106), (0.628942821, 0.2886857106))
                CenterArc((0.628942821, 0.0886857106), 0.2, 90, 16.4686815987)
                Line((0.5722445805, 0.280480678), (0.2893874059, 0.196862717))
                CenterArc((0, 0), 0.35, 34.2264343763, 235.7735656237)
                Line((0, -0.35), (3.075, -0.3605551329))
                CenterArc((3.075, -0.3355551329), 0.025, -90, 90)
                Line((3.1, -0.3355551329), (3.1, -0.2105551329))
                CenterArc((3.075, -0.2105551329), 0.025, 0, 90)
                Line((3.075, -0.1855551329), (2.8436140677, -0.1855551329))
                CenterArc((2.8436140677, -0.2105551329), 0.025, 90, 55.1500843238)
                CenterArc((2.7000000209, -0.1105551051), 0.15, 34.8498934819, 290.3001908419)
                CenterArc((2.8436141064, -0.0105551329), 0.025, -145.1501065181, 55.1501065181)
                Line((3.075, -0.0355551329), (2.8436141064, -0.0355551329))
                CenterArc((3.075, -0.0105551329), 0.025, -90, 90)
                Line((3.1, -0.0105551329), (3.1, 0.1144448671))
                CenterArc((3.075, 0.1144448671), 0.025, 0, 90)
                Line((3.075, 0.1394448671), (2.4744482568, 0.1394448671))
                CenterArc((2.4744482568, -1.8605551329), 2, 90, 9.9699141326)
                Line((2.1281861894, 0.109242466), (0.8366935481, -0.1177833524))
                CenterArc((0.8020673414, 0.0791964075), 0.2, -162.9290704243, 82.8989845568)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a uniform circular cross-section, featuring a smooth curved outer surface and a hollow center, commonly used as a spacer, seal, or structural component in mechanical assemblies.
def model_24476_568e9ca0_0022():
    """Model: spacer 1,5 mm v8 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a dark blue/navy rectangular bracket or mounting plate with a horizontal slot running through its center and flanged edges on the sides, featuring a compact, low-profile design typical of structural support or attachment hardware.
def model_24540_92ecb906_0000():
    """Model: Cavity"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3107, perimeter: 24.856
            with BuildLine():
                Line((0.025, -0.625), (1.514, -0.625))
                Line((1.514, -0.625), (1.514, 0.625))
                Line((0.025, 0.625), (1.514, 0.625))
                Line((0.025, 0.7), (0.025, 0.625))
                Line((-2.925, 0.7), (0.025, 0.7))
                Line((-2.925, 0.66), (-2.925, 0.7))
                Line((-3.025, 0.66), (-2.925, 0.66))
                Line((-3.025, 0.3875), (-3.025, 0.66))
                Line((-2.695, 0.3875), (-3.025, 0.3875))
                Line((-2.695, -0.3825), (-2.695, 0.3875))
                Line((-3.025, -0.3825), (-2.695, -0.3825))
                Line((-3.025, -0.655), (-3.025, -0.3825))
                Line((-2.925, -0.655), (-3.025, -0.655))
                Line((-2.925, -0.695), (-2.925, -0.655))
                Line((0.025, -0.695), (-2.925, -0.695))
                Line((0.025, -0.625), (0.025, -0.695))
            make_face()
            with BuildLine():
                Line((0, 0.675), (0, 0.6))
                Line((0, 0.6), (1.489, 0.6))
                Line((1.489, -0.6), (1.489, 0.6))
                Line((0, -0.6), (1.489, -0.6))
                Line((0, -0.6), (0, -0.67))
                Line((0, -0.67), (-2.9, -0.67))
                Line((-2.9, -0.67), (-2.9, -0.63))
                Line((-2.9, -0.63), (-3, -0.63))
                Line((-3, -0.63), (-3, -0.4075))
                Line((-3, -0.4075), (-2.67, -0.4075))
                Line((-2.67, -0.4075), (-2.67, 0.4125))
                Line((-2.67, 0.4125), (-3, 0.4125))
                Line((-3, 0.4125), (-3, 0.635))
                Line((-3, 0.635), (-2.9, 0.635))
                Line((-2.9, 0.635), (-2.9, 0.675))
                Line((-2.9, 0.675), (0, 0.675))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.7564, perimeter: 9.35
            with BuildLine():
                Line((-2.9, 0.675), (0, 0.675))
                Line((-2.9, 0.635), (-2.9, 0.675))
                Line((-3, 0.635), (-2.9, 0.635))
                Line((-3, 0.4125), (-3, 0.635))
                Line((-2.67, 0.4125), (-3, 0.4125))
                Line((-2.67, -0.4075), (-2.67, 0.4125))
                Line((-3, -0.4075), (-2.67, -0.4075))
                Line((-3, -0.63), (-3, -0.4075))
                Line((-2.9, -0.63), (-3, -0.63))
                Line((-2.9, -0.67), (-2.9, -0.63))
                Line((0, -0.67), (-2.9, -0.67))
                Line((0, -0.6), (0, -0.67))
                Line((0, 0.6), (0, -0.6))
                Line((0, 0.675), (0, 0.6))
            make_face()
            # Profile area: 1.7868, perimeter: 5.378
            with BuildLine():
                Line((0, -0.6), (1.489, -0.6))
                Line((1.489, -0.6), (1.489, 0.6))
                Line((0, 0.6), (1.489, 0.6))
                Line((0, 0.6), (0, -0.6))
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a standard twist drill bit featuring a cylindrical shank with helical (spiral) flutes running along its length, a tapered conical point at the tip for cutting, and a flat or slightly rounded end at the base for chuck mounting.
def model_24543_6b6469fa_0003():
    """Model: up"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.2004581787, perimeter: 20.7287584938
            with BuildLine():
                CenterArc((0, 7), 1.1, 61.944293246, 118.055706754)
                Line((-1.0996450011, 6.9720559213), (-1.1, 7))
                Line((-1.0110726726, 0), (-1.0996450011, 6.9720559213))
                Line((-1, 0), (-1.0110726726, 0))
                CenterArc((0, 0), 1, 180, 180)
                Line((1, 0), (1.0697513801, 3.9960538898))
                CenterArc((1.022862781, 4.4993745721), 0.5055, -180, 95.3222279381)
                Line((0.517362781, 7.9707397967), (0.517362781, 4.4993745721))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a linear rail or guide block with an elongated rectangular body, featuring a slotted top surface, rounded end caps, and internal channels designed for smooth sliding motion along a shaft or rail system.
def model_24544_d06c82dd_0008():
    """Model: limauñas"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0103612148, perimeter: 6.783365938
            with BuildLine():
                Line((-1.3035678012, 0.1692425065), (-1.3035678012, -0.2036912457))
                Line((-1.3035678012, -0.2036912457), (1.3035678012, -0.2036912457))
                Line((1.3035678012, -0.2036912457), (1.3035678012, 0.2036912457))
                Line((1.3035678012, 0.2036912457), (-1.0583001249, 0.2036912457))
                Line((-1.0583001249, 0.2036912457), (-1.0807168223, 0.2036912457))
                CenterArc((-1.0695084736, -0.6068588466), 0.8106275835, 90.792239931, 15.9902022046)
            make_face()
            with BuildLine():
                CenterArc((1.1000000164, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0583118123, perimeter: 1.2847818605
            with BuildLine():
                CenterArc((-1.0695084736, -0.6068588466), 0.8106275835, 106.7824421356, 32.8202302329)
                CenterArc((-1.555644768, -0.3321675291), 0.282929236, 27.0066136608, 90.6235940928)
                Line((-1.3035678012, 0.1692425065), (-1.3035678012, -0.2036912457))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or torus with a hollow circular center, featuring a textured or ribbed surface pattern across its outer and inner curved surfaces.
def model_24544_d06c82dd_0009():
    """Model: goma"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0765763209, perimeter: 2.0420352248
            with BuildLine():
                CenterArc((-0.3000000045, -0.8000000119), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.3000000045, -0.8000000119), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.042
        extrude(amount=0.042)
    return part.part


# Description: This is a long, thin rectangular extrusion or beam with a beveled or chamfered edge on the left end and an angled top surface, featuring a hollow or recessed channel running along its length.
def model_24603_a4021250_0000():
    """Model: 60x60 profile"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 22 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.4683185307, perimeter: 44.6831853072
            with BuildLine():
                CenterArc((0.6, 5.4), 0.6, 90, 90)
                Line((0, 5.4), (0, 0.6))
                CenterArc((0.6, 0.6), 0.6, -180, 90)
                Line((0.6, 0), (5.4, 0))
                CenterArc((5.4, 0.6), 0.6, -90, 90)
                Line((6, 0.6), (6, 5.4))
                CenterArc((5.4, 5.4), 0.6, 0, 90)
                Line((5.4, 6), (0.6, 6))
            make_face()
            with BuildLine():
                Line((0.2, 5.4), (0.2, 0.6))
                CenterArc((0.6, 5.4), 0.4, 90, 90)
                Line((5.4, 5.8), (0.6, 5.8))
                CenterArc((5.4, 5.4), 0.4, 0, 90)
                Line((5.8, 0.6), (5.8, 5.4))
                CenterArc((5.4, 0.6), 0.4, -90, 90)
                Line((0.6, 0.2), (5.4, 0.2))
                CenterArc((0.6, 0.6), 0.4, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=60
        extrude(amount=60)
    return part.part


# Description: This is a thin, flat parallelogram-shaped metal plate with a uniform thickness, featuring slanted parallel edges and no holes or additional features—commonly used as a shim, spacer, or alignment component.
def model_24603_a4021250_0002():
    """Model: Table_deck"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9000, perimeter: 460
            with BuildLine():
                Line((-145.710264591, 57.323645636), (34.289735409, 57.323645636))
                Line((-145.710264591, 7.323645636), (-145.710264591, 57.323645636))
                Line((34.289735409, 7.323645636), (-145.710264591, 7.323645636))
                Line((34.289735409, 57.323645636), (34.289735409, 7.323645636))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is an elongated hexagonal or chamfered rectangular bar with a central longitudinal slot or groove running along its top surface, featuring beveled edges at both ends.
def model_24603_a4021250_0005():
    """Model: Scissor_bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.3052211349, perimeter: 35.3681408993
            with BuildLine():
                CenterArc((-16.0533760472, 17.9481620133), 0.8, 90, 90)
                Line((-16.8533760472, 14.5481620133), (-16.8533760472, 17.9481620133))
                CenterArc((-16.0533760472, 14.5481620133), 0.8, -180, 90)
                Line((-12.6533760472, 13.7481620133), (-16.0533760472, 13.7481620133))
                CenterArc((-12.6533760472, 14.5481620133), 0.8, -90, 90)
                Line((-11.8533760472, 17.9481620133), (-11.8533760472, 14.5481620133))
                CenterArc((-12.6533760472, 17.9481620133), 0.8, 0, 90)
                Line((-16.0533760472, 18.7481620133), (-12.6533760472, 18.7481620133))
            make_face()
            with BuildLine():
                Line((-16.5533760472, 14.5481620133), (-16.5533760472, 17.9481620133))
                CenterArc((-16.0533760472, 17.9481620133), 0.5, 90, 90)
                Line((-16.0533760472, 18.4481620133), (-12.6533760472, 18.4481620133))
                CenterArc((-12.6533760472, 17.9481620133), 0.5, 0, 90)
                Line((-12.1533760472, 17.9481620133), (-12.1533760472, 14.5481620133))
                CenterArc((-12.6533760472, 14.5481620133), 0.5, -90, 90)
                Line((-12.6533760472, 14.0481620133), (-16.0533760472, 14.0481620133))
                CenterArc((-16.0533760472, 14.5481620133), 0.5, -180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=30.6
        extrude(amount=30.6)
    return part.part


# Description: This is a dark blue metal bracket or mounting plate with a parallelogram shape, featuring a circular hole near the center and a protruding flange or tab on the lower left side.
def model_24603_a4021250_0008():
    """Model: Actuator_lower_mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.9984073464, perimeter: 31.5802998913
            with BuildLine():
                Line((-33.3725198317, 2), (-30.7725198317, 2))
                Line((-30.7725198317, 0.4), (-30.7725198317, 2))
                Line((-26.2725198317, 0.4), (-30.7725198317, 0.4))
                Line((-26.2725198317, 6.9), (-26.2725198317, 0.4))
                Line((-30.7725198317, 6.9), (-26.2725198317, 6.9))
                Line((-33.3725198317, 2.4), (-30.7725198317, 6.9))
                Line((-33.3725198317, 2), (-33.3725198317, 2.4))
            make_face()
            with BuildLine():
                CenterArc((-28.2725198317, 4.8), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a dark blue elongated rectangular plate or bar with rounded ends and a slightly beveled or angled edge on the left side, featuring a simple, streamlined design with no holes or slots.
def model_24612_e91cc2f4_0001():
    """Model: HYDRAULICLAST"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((61.5, -20.5), (61.5, -18.5))
                CenterArc((61.5, -19.5), 1, -90, 180)
            make_face()
            # Profile area: 13.4292036732, perimeter: 20.1415926536
            with BuildLine():
                CenterArc((61.5, -19.5), 1, 90, 180)
                Line((61.5, -18.5), (54, -18.5))
                Line((54, -18.5), (54, -20.5))
                Line((54, -20.5), (61.5, -20.5))
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                CenterArc((61.5, -19.5), 1, 90, 180)
                Line((61.5, -20.5), (61.5, -18.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a elongated hexagonal prism or coffin-shaped structural part with tapered ends and faceted surfaces, featuring a hollow or recessed central section along its length.
def model_24627_7ee9cadb_0006():
    """Model: Segment F"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.9895409812, perimeter: 14.9999990377
            with BuildLine():
                Line((-2.9169454746, -3.1034365109), (-3.9126042668, -3.939297486))
                Line((-3.9126042668, -3.939297486), (-3.2053372878, -4.7817780024))
                Line((1.8946627122, -4.7817780024), (-3.2053372878, -4.7817780024))
                Line((2.8903208856, -3.9459162903), (1.8946627122, -4.7817780024))
                Line((2.1830545254, -3.1034365109), (2.8903208856, -3.9459162903))
                Line((-2.9169454746, -3.1034365109), (2.1830545254, -3.1034365109))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical sleeve or tube with a dark gray body and a textured blue band at the top, featuring a simple hollow tubular form with no additional features like holes, slots, or flanges.
def model_24659_d2ba8a0f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # TwoSides extrude, along=10, against=-1
        extrude(amount=10)
        extrude(sk.sketch, amount=-1)
    return part.part


# Description: This is a flat parallelogram plate or shim with a slanted rectangular shape, featuring clean edges and a uniform thickness, commonly used as a spacer or structural component.
def model_24722_02c0cd8a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 200, perimeter: 60
            with BuildLine():
                Line((5, -12.5), (-5, -12.5))
                Line((5, 7.5), (5, -12.5))
                Line((-5, 7.5), (5, 7.5))
                Line((-5, -12.5), (-5, 7.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular box-like structural frame or tray with an open top, featuring internal cross-bracing, reinforcing ribs, and mounting bosses or pads positioned symmetrically within the cavity.
def model_24788_26865dc0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 96.8584073464, perimeter: 62.2831853072
            with BuildLine():
                Line((14, -8), (0, -8))
                Line((14, 0), (14, -8))
                Line((0, 0), (14, 0))
                Line((0, -8), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((5, -4), 1, 90, 180)
                Line((11, -3), (5, -3))
                CenterArc((11, -4), 1, -90, 180)
                Line((5, -5), (11, -5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a uniform conical shape that gradually reduces in diameter from one end to the other, commonly used as a dowel, alignment pin, or drift pin in mechanical assemblies.
def model_24869_5c729cf1_0003():
    """Model: Lead tube"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0548239334, perimeter: 1.7404423301
            with BuildLine():
                CenterArc((0, 0), 0.17, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.107, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is an oval or elliptical dome/shell structure with a smooth curved surface subdivided by internal triangular wireframe segments, featuring a symmetrical egg-like or capsule shape with no apparent holes, slots, or flanges.
def model_24890_5f8a67df_0006():
    """Model: Mesh"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 62.0716661894, perimeter: 27.9287586904
            Circle(4.445)
        # Symmetric extrude, each_side=0.079375
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a toroidal (ring-shaped) component with a circular cross-section and radial ribbing or fins extending across its entire outer surface, likely used for heat dissipation or structural reinforcement in an industrial application.
def model_24890_5f8a67df_0010():
    """Model: Impeller Direction Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50.9874387905, perimeter: 45.882961215
            with BuildLine():
                CenterArc((0, 0), 4.7625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5400000811, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a curved sheet metal pan or tray with a parallelogram-like shape, featuring a horizontally striated top surface and a recessed bottom flange, designed for containment or mounting applications.
def model_24890_5f8a67df_0012():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6049304324, perimeter: 5.9293450604
            with BuildLine():
                CenterArc((0, 0), 5.08, -120.8630917945, 30.1188900154)
                Line((-2.6059811031, -5.0795714872), (-2.6059811031, -4.3606493198))
                Line((-0.0659811031, -5.0795714872), (-2.6059811031, -5.0795714872))
            make_face()
            # Profile area: 0.5151456751, perimeter: 5.5687947519
            with BuildLine():
                Line((2.4740188969, -5.0795714872), (2.4740188969, -4.4368491633))
                CenterArc((0, 0), 5.08, -89.2557982209, 28.4001490568)
                Line((0.0659811031, -5.0795714872), (2.4740188969, -5.0795714872))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


# Description: This is a rubber or elastomer O-ring or gasket with a circular torus shape, featuring a uniform cross-sectional diameter and smooth curved profile designed for sealing applications.
def model_24890_5f8a67df_0013():
    """Model: Casing Threads"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.8174574075, perimeter: 61.8422513859
            with BuildLine():
                CenterArc((0, 5.0800001621), 5.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.0800001621), 4.7625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a disc or washer-like component with a flat, elongated oval shape featuring a central hole and radial ridge or fin patterns across its surface for structural reinforcement.
def model_24896_58b4730f_0007():
    """Model: rubber seal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9040097092, perimeter: 8.0110612667
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a circular cross-section, featuring a textured or mesh-patterned outer surface and a smooth dark inner core, commonly used as a gasket, seal, or structural component.
def model_24896_58b4730f_0012():
    """Model: spring support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0053096491, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a V-belt (or V-groove belt) with an elliptical/oval overall shape, featuring a trapezoidal cross-section with textured sides designed to grip pulley grooves for power transmission in mechanical systems.
def model_24896_58b4730f_0013():
    """Model: distance washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3820176667, perimeter: 9.5504416669
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.72, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a tool holder or lathe cutting tool insert featuring an elongated rectangular body with a tapered/angled cutting edge at one end and a mounting slot or groove at the opposite end for secure attachment to a machine spindle.
def model_24896_58b4730f_0014():
    """Model: rotation blockade"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5928539816, perimeter: 5.8424777961
            with BuildLine():
                Line((-0.25, -1.45), (-0.25, -2))
                CenterArc((-0.2, -2), 0.05, 180, 180)
                Line((-0.15, -2), (-0.15, -1.6))
                CenterArc((-0.1, -1.6), 0.05, 90, 90)
                Line((0.1, -1.55), (-0.1, -1.55))
                CenterArc((0.1, -1.6), 0.05, 0, 90)
                Line((0.15, -2), (0.15, -1.6))
                CenterArc((0.2, -2), 0.05, 180, 180)
                Line((0.25, -1.45), (0.25, -2))
                CenterArc((0.2, -1.45), 0.05, 0, 90)
                CenterArc((0.2, -1.35), 0.05, -180, 90)
                Line((0.15, -0.05), (0.15, -1.35))
                CenterArc((0.1, -0.05), 0.05, 0, 90)
                Line((-0.1, 0), (0.1, 0))
                CenterArc((-0.1, -0.05), 0.05, 90, 90)
                Line((-0.15, -0.05), (-0.15, -1.35))
                CenterArc((-0.2, -1.35), 0.05, -90, 90)
                CenterArc((-0.2, -1.45), 0.05, 90, 90)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a sheet metal angle bracket or corner guard featuring two perpendicular flanges that form a V-shaped channel, with a folded design typical of protective edge trim or structural reinforcement components.
def model_24896_58b4730f_0015():
    """Model: cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8764951873, perimeter: 29.1649557114
            with BuildLine():
                Line((0, 0), (0, -3.8))
                CenterArc((0.4, -3.8), 0.4, -180, 90)
                Line((0.4, -4.2), (6.24, -4.2))
                CenterArc((6.24, -3.8), 0.4, -90, 90)
                Line((6.64, -3.8), (6.64, 0))
                Line((6.64, 0), (6.44, 0))
                Line((6.44, 0), (6.44, -3.8000000596))
                CenterArc((6.24, -3.8000000596), 0.2, -90, 90)
                Line((6.24, -4.0000000596), (0.4, -4.0000000596))
                CenterArc((0.4, -3.8000000596), 0.2, -180, 90)
                Line((0.2, 0), (0.2, -3.8000000596))
                Line((0, 0), (0.2, 0))
            make_face()
        # OneSide extrude, distance=13.45
        extrude(amount=13.45)
    return part.part


# Description: This is a long, slender bracket or support arm with a diagonal orientation, featuring rectangular flanges or mounting pads at both the upper and lower ends, connected by a narrow rectangular shaft.
def model_24896_58b4730f_0016():
    """Model: rotation blockade guide"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.1507955863, perimeter: 42.7072563597
            with BuildLine():
                CenterArc((-0.4100212017, 1.7158296609), 0.05, 90, 90)
                Line((-0.4600212017, 1.7158296609), (-0.4600212017, 0.0508296423))
                CenterArc((-0.4100212017, 0.0508296609), 0.05, -179.9999787356, 89.9999787356)
                Line((-0.4100212017, 0.0008296609), (1.2499787983, 0.0008296609))
                CenterArc((1.2499787983, 0.0508296609), 0.05, -90, 90)
                Line((1.2999787983, 0.0508296609), (1.2999787983, 8.6008296609))
                CenterArc((1.2499787983, 8.6008296609), 0.05, 0, 90)
                Line((1.2499787983, 8.6508296609), (-0.4100212017, 8.6508296609))
                CenterArc((-0.4100212017, 8.6008296609), 0.05, 90, 90)
                Line((-0.4600212017, 8.6008296609), (-0.4600212017, 6.9358296609))
                CenterArc((-0.4100212017, 6.9358296609), 0.05, 180, 90)
                Line((-0.4100212017, 6.8858296609), (0.5499787983, 6.8858296609))
                CenterArc((0.5499787983, 6.8358296609), 0.05, 0, 90)
                Line((0.5999787983, 1.8158296609), (0.5999787983, 6.8358296609))
                CenterArc((0.5499787983, 1.8158296609), 0.05, -90, 90)
                Line((-0.4100212017, 1.7658296609), (0.5499787983, 1.7658296609))
            make_face()
            with BuildLine():
                CenterArc((-0.2000212017, 7.2008296609), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.2000212017, 1.4508296609), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.2000212017, 8.1508296609), 0.11, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.2000212017, 0.5008296609), 0.11, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.7999787983, 0.1508296609), (1.0999787983, 0.1508296609))
                Line((0.7999787983, 8.5008296609), (0.7999787983, 0.1508296609))
                Line((1.0999787983, 8.5008296609), (0.7999787983, 8.5008296609))
                Line((1.0999787983, 0.1508296609), (1.0999787983, 8.5008296609))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: A cylindrical rubber disk with a flat circular face, slightly beveled edges, and a textured surface, designed for use in ice hockey.
def model_24907_c72322ea_0010():
    """Model: Handle_Pivot_Rubber v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a curved structural bracket or handle component featuring a smooth S-shaped bend with flanged end sections at both terminals, designed for gripping or mounting applications.
def model_24907_c72322ea_0012():
    """Model: Bridge_Cover v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 26 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.4231460315, perimeter: 27.2537129283
            with BuildLine():
                CenterArc((-10.7482215772, 0.8728008104), 0.3, -150, 60)
                Line((-10.18766456, 0.5728008104), (-10.7482215772, 0.5728008104))
                CenterArc((-10.18766456, 0.8728008104), 0.3, -90, 90)
                Line((-9.88766456, 0.819859634), (-9.88766456, 0.8728008104))
                CenterArc((-8.509636281, 0.5728008104), 1.4, 90, 79.8357513783)
                Line((-5.009636281, 1.9728008104), (-8.509636281, 1.9728008104))
                CenterArc((-5.009636281, 0.5728008104), 1.4, 10.1642486217, 79.8357513783)
                CenterArc((-3.336316228, 0.8728008104), 0.3, -169.8357513783, 79.8357513783)
                Line((-3.336316228, 0.5728008104), (-2.362316228, 0.5728008104))
                CenterArc((-2.362316228, 0.8728008104), 0.3, -90, 75.0003270203)
                Line((-1.6674671347, 2.3069364528), (-2.0725380369, 0.7951567508))
                CenterArc((-3.406136281, 2.7728008104), 1.8, -14.9996729797, 104.9996729797)
                Line((-3.406136281, 4.5728008104), (-10.113136281, 4.5728008104))
                CenterArc((-10.113136281, 2.7728008104), 1.8, 90, 120)
                Line((-11.0080291983, 0.7228008104), (-11.6719820079, 1.8728008104))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a solid cylindrical component with a uniform circular cross-section, featuring a slightly tapered or curved top surface and a flat bottom face, commonly used as a structural or mechanical part in assemblies.
def model_24907_c72322ea_0013():
    """Model: Handle_Bush v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.25
        extrude(amount=1.25)
    return part.part


# Description: This is a cylindrical or barrel-shaped container with an open top, featuring a curved body with a flange or rim around the upper edge, and appears to be a truncated cone or bucket-like component with textured surface details.
def model_25128_d2840160_0000():
    """Model: springhousing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=1.305
        extrude(amount=1.305)
    return part.part


# Description: This is a swivel or articulating connector featuring a rounded cylindrical head with a tapered neck that connects to an angular trapezoidal base, allowing for directional adjustment or rotation between two components.
def model_25156_78e996ae_0001():
    """Model: Wedge v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 68.0117967647, perimeter: 59.2551868025
            with BuildLine():
                Line((-0.1426584774, 0.6463525492), (-6, 2.5495181774))
                Line((-6, -2.5495181863), (-6, 2.5495181774))
                Line((-0.1426584774, -0.6463525581), (-6, -2.5495181863))
                CenterArc((0, -0.6000000089), 0.15, 0, 198)
                Line((0.15, -0.6000000089), (10.0402020285, -0.6000000089))
                CenterArc((10.0402020285, -1.4000000089), 0.8, 19.4712207639, 70.5287792361)
                CenterArc((14, 0), 3.4, -160.5287792361, 321.0575586017)
                CenterArc((10.0402020254, 1.4), 0.8, -90, 70.5287793655)
                Line((0.15, 0.6), (10.0402020254, 0.6))
                CenterArc((0, 0.6), 0.15, 162, 198)
            make_face()
        # TwoSides extrude (symmetric), distance=2.9
        extrude(amount=2.9, both=True)
    return part.part


# Description: This is a triangular or wedge-shaped structural component with a tapered profile, featuring a flat upper surface, angled sides, and a reinforced perimeter rim or flange around its edges.
def model_25184_9594f8f3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 46.8343058527, perimeter: 29.7582085749
            with BuildLine():
                CenterArc((4.4052965027, 2.5169181427), 1, 0, 106.6703580355)
                Line((-5.1407092602, 0.7022343721), (4.1184315506, 3.4748891753))
                CenterArc((-4.9436424385, 0.0441396646), 0.6869672308, 106.6703580355, 146.6592839289)
                Line((-5.1407092602, -0.6139550428), (4.1184315506, -3.3866098461))
                CenterArc((4.4052965027, -2.4286388135), 1, -106.6703580355, 106.6703580355)
                Line((5.4052965027, 2.5169181427), (5.4052965027, -2.4286388135))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a circular annular (ring-shaped) component with a large central rectangular slot and a textured outer rim, appearing to be a bearing housing, spacer, or mechanical seal component.
def model_25199_39e3c0d3_0004():
    """Model: Part 8 - Washer B v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6298673702, perimeter: 4.32849533
            with BuildLine():
                CenterArc((0, 0), 0.482, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.125, -0.200000003), (0.125, -0.200000003))
                Line((-0.125, 0.200000003), (-0.125, -0.200000003))
                Line((0.125, 0.200000003), (-0.125, 0.200000003))
                Line((0.125, -0.200000003), (0.125, 0.200000003))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical foam roller with a textured surface pattern, featuring a solid, uniform tubular body with rounded ends and a slightly knurled or mesh-like grip surface along its length.
def model_25199_39e3c0d3_0006():
    """Model: Part 16 - Screw B v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.034636059, perimeter: 0.6597344573
            Circle(0.105)
        # OneSide extrude, distance=0.763
        extrude(amount=0.763)
    return part.part


# Description: This is a torus-shaped ring or washer with a circular cross-section, featuring two small cylindrical protrusions or lugs on opposite sides that appear to serve as mounting or attachment points.
def model_25199_b2422c18_0005():
    """Model: Part 5 - Eared Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1175626197, perimeter: 9.2090054599
            with BuildLine():
                CenterArc((0, 0), 0.94, 7.6247446256, 164.7505107488)
                CenterArc((-0.94, 0), 0.125, 86.1876276872, 187.6247446256)
                CenterArc((0, 0), 0.94, -172.3752553744, 164.7505107488)
                CenterArc((0.94, 0), 0.125, -93.8123723128, 187.6247446256)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.475, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.076
        extrude(amount=0.076)
    return part.part


# Description: This is a circular disc or washer with a large central rectangular slot, featuring a flat face with curved edges and a slightly beveled or rounded perimeter.
def model_25199_b2422c18_0008():
    """Model: Part 3 - Key Washer v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6519654182, perimeter: 7.2504862255
            with BuildLine():
                CenterArc((0, 0), 0.9375, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.13, -0.21), (0.13, -0.21))
                Line((-0.13, 0.21), (-0.13, -0.21))
                Line((0.13, 0.21), (-0.13, 0.21))
                Line((0.13, -0.21), (0.13, 0.21))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.077
        extrude(amount=0.077)
    return part.part


# Description: This is a hollow rectangular box or enclosure with an open front face, featuring a sloped or angled top section and vertical side walls, designed as a container or mounting bracket structure.
def model_25199_b2422c18_0010():
    """Model: Part 39 - Rear Cover v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6257763342, perimeter: 12.5229589837
            with BuildLine():
                Line((0.979982774, 0.4893099697), (-1.02, 0.4893099697))
                Line((-1.02, 0.4893099697), (-1.02, -3.38))
                Line((-1.02, -3.38), (-0.6, -2.68))
                Line((-0.6, -2.68), (0.5745724593, -2.68))
                Line((0.979982774, -3.3716991711), (0.5745724593, -2.68))
                Line((0.979982774, -3.3716991711), (0.979982774, 0.4893099697))
            make_face()
        # OneSide extrude, distance=6.14
        extrude(amount=6.14)
    return part.part


# Description: A circular flat washer with a large central hole, featuring a thin, disk-like profile with a slightly beveled outer edge.
def model_25199_b2422c18_0011():
    """Model: Part 4 - Drag Washer v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4504422698, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)
    return part.part


# Description: This is a dark blue/navy plastic or metal bracket or mounting clip with an angular, bent design featuring two flat rectangular sections connected at an angle, with linear ribbing or reinforcing patterns visible on the interior surfaces for structural support.
def model_25199_d7aff7a5_0014():
    """Model: Part 36 - AntiReverse Cam Spring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1461651259, perimeter: 4.9898999756
            with BuildLine():
                Line((0, 0), (0, 1.1))
                CenterArc((-0.0495644088, 0.867860377), 0.2373719343, 77.9476779634, 78.383792981)
                Line((-0.2669693836, 0.9631520982), (-0.4928565146, 0.6330384753))
                Line((-0.4928565146, 0.6330384753), (-0.5883630123, 0.0913942111))
                Line((-0.5883630123, 0.0913942111), (-0.5292745471, 0.0809753205))
                Line((-0.4360190468, 0.6098535441), (-0.5292745471, 0.0809753205))
                Line((-0.2140416565, 0.9342534345), (-0.4360190468, 0.6098535441))
                CenterArc((-0.0495644088, 0.867860377), 0.1773719343, 93.3729170167, 64.6450724711)
                Line((-0.06, -0.06), (-0.06, 1.0449250587))
                Line((-0.06, -0.06), (0.1000000015, -0.06))
                Line((0.1000000015, 0), (0.1000000015, -0.06))
                Line((0, 0), (0.1000000015, 0))
            make_face()
        # OneSide extrude, distance=0.23
        extrude(amount=0.23)
    return part.part


# Description: This is a hexagonal ring or connector with a central elliptical hole, featuring a thick, faceted geometric body with angled surfaces and internal mesh-textured walls that create a complex 3D topology suitable for structural or mechanical assembly purposes.
def model_25199_d7aff7a5_0020():
    """Model: Part 11 - Rotor Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7444217569, perimeter: 6.670196061
            with BuildLine():
                Line((0.3464101615, 0.6), (-0.3464101615, 0.6))
                Line((-0.3464101615, 0.6), (-0.692820323, 0))
                Line((-0.692820323, 0), (-0.3464101615, -0.6))
                Line((-0.3464101615, -0.6), (0.3464101615, -0.6))
                Line((0.3464101615, -0.6), (0.692820323, 0))
                Line((0.692820323, 0), (0.3464101615, 0.6))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: A flat, ring-shaped disk with a large central hole, commonly used as a fastener component to distribute load and provide spacing in bolted assemblies.
def model_25199_d7aff7a5_0022():
    """Model: Part 7 - Washer A v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5688442548, perimeter: 4.0997784129
            with BuildLine():
                CenterArc((0, 0), 0.465, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a cylindrical tube or pipe with a hollow, uniform circular cross-section and straight, parallel walls, featuring a simple open-ended design with no additional features, holes, or flanges.
def model_25203_1cc0cb3c_0000():
    """Model: Hex shaft w/spacer (short) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0584567148, perimeter: 0.9
            with BuildLine():
                Line((0.1299038106, 0.075), (0, 0.15))
                Line((0, 0.15), (-0.1299038106, 0.075))
                Line((-0.1299038106, 0.075), (-0.1299038106, -0.075))
                Line((-0.1299038106, -0.075), (0, -0.15))
                Line((0, -0.15), (0.1299038106, -0.075))
                Line((0.1299038106, -0.075), (0.1299038106, 0.075))
            make_face()
        # OneSide extrude, distance=3.455
        extrude(amount=3.455)
    return part.part


# Description: This is a dual-motor propeller mount or thrust vectoring bracket with a streamlined wedge-shaped body featuring two protruding cylindrical motor attachment points on the left side, a tapered aerodynamic profile, and internal ribbing for structural reinforcement.
def model_25203_1cc0cb3c_0005():
    """Model: Body - Side plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.947816, perimeter: 21.6527404727
            with BuildLine():
                Line((-0.58, -0.641), (0, -0.641))
                Line((-0.58, -1.706), (-0.58, -0.641))
                Line((0, -1.706), (-0.58, -1.706))
                Line((0, -3.46), (0, -1.706))
                Line((3.681, -3.46), (0, -3.46))
                Line((3.681, -4.04), (3.681, -3.46))
                Line((4.584, -4.04), (3.681, -4.04))
                Line((4.584, 1.956), (4.584, -4.04))
                Line((3.498, 1.956), (4.584, 1.956))
                Line((2.658, 0), (3.498, 1.956))
                Line((0, 0), (2.658, 0))
                Line((0, -0.641), (0, 0))
            make_face()
        # OneSide extrude, distance=0.58
        extrude(amount=0.58)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a rounded rectangular profile, featuring a large central bore through its length and thick-walled construction with curved, filleted edges.
def model_25203_1cc0cb3c_0012():
    """Model: G6 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1028086196, perimeter: 2.4190263433
            with BuildLine():
                CenterArc((0, 0), 0.235, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform diameter and rounded ends, appearing to be a simple mechanical component such as a pin, dowel, or axle.
def model_25203_92cee759_0001():
    """Model: Round shaft (short) v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.061575216, perimeter: 0.879645943
            Circle(0.14)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a cylindrical sleeve or tube with a uniform hollow bore throughout its length, featuring a smooth exterior surface and straight parallel sides.
def model_25203_92cee759_0002():
    """Model: Hex shaft w/spacer (long) v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0584567148, perimeter: 0.9
            with BuildLine():
                Line((0.1299038106, 0.075), (0, 0.15))
                Line((0, 0.15), (-0.1299038106, 0.075))
                Line((-0.1299038106, 0.075), (-0.1299038106, -0.075))
                Line((-0.1299038106, -0.075), (0, -0.15))
                Line((0, -0.15), (0.1299038106, -0.075))
                Line((0.1299038106, -0.075), (0.1299038106, 0.075))
            make_face()
        # OneSide extrude, distance=4.6
        extrude(amount=4.6)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a solid body and an open, mesh-textured top end, designed to allow fluid or air flow while containing or filtering material.
def model_25203_92cee759_0004():
    """Model: WormGear v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3871227547, perimeter: 2.9216811678
            with BuildLine():
                CenterArc((0, 0), 0.365, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a elongated tool or holder with a streamlined, tapered design featuring a rounded nose cone on the left end, a blue metallic body with internal slot details, and a flat pointed tail section on the right end.
def model_25203_92cee759_0007():
    """Model: Bucket Arm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.9258624772, perimeter: 28.6844719586
            with BuildLine():
                Line((0.35, 0), (12.06, 0))
                Line((12.06, 0), (12.06, 0.7496970215))
                Line((1.72, 1.3), (12.06, 0.7496970215))
                Line((0.2200515089, 0.6749821374), (1.72, 1.3))
                CenterArc((0.35, 0.35), 0.35, 111.7946664615, 68.2053335385)
                Line((0.2, 0.35), (0, 0.35))
                CenterArc((0.35, 0.35), 0.15, 0, 360)
                CenterArc((0.35, 0.35), 0.35, 180, 90)
            make_face()
            with BuildLine():
                CenterArc((11.66, 0.35), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.31, 0.35), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47
        extrude(amount=0.47)
    return part.part


# Description: This is a torus (donut-shaped ring) featuring a smooth outer surface with a textured or mesh-patterned finish on the upper portion and a solid dark band around the bottom, with a central hollow opening.
def model_25203_92cee759_0009():
    """Model: Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2391537408, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with an open top and bottom, featuring a solid darker cylindrical body with a lighter blue mesh or grid-pattern surface on the upper rim and side sections.
def model_25203_92cee759_0012():
    """Model: Poly Cap v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical pipe or tube with a slightly tapered rounded end, featuring a smooth hollow interior design typical of a sleeve, bushing, or connector component.
def model_25203_92cee759_0014():
    """Model: M4 Pillar v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


# Description: This is a housing or bracket component with an angular, wedge-like shape featuring a curved top surface, flat base, internal ribbing or internal structure visible through cutout sections, and what appears to be a transparent or open window panel on one side.
def model_25211_336c083f_0008():
    """Model: 12-Piston Crank end v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1417699082, perimeter: 8.826990817
            with BuildLine():
                CenterArc((0.5, 1.3), 0.5, 0, 180)
                Line((0, 0), (0, 1.3))
                Line((0, 0), (1.95, 0))
                Line((1.95, 0.75), (1.95, 0))
                Line((1.3000002641, 0.75), (1.95, 0.75))
                CenterArc((1.3, 1.05), 0.3, -179.9999507438, 90.0000011815)
                Line((1, 1.3), (1, 1.0499997421))
            make_face()
            with BuildLine():
                CenterArc((0.5, 1.3), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a flat rectangular plate or panel with a slightly tapered parallelogram shape, featuring a recessed or stepped surface on top and a raised edge or flange along one side, designed as a thin sheet metal or composite component.
def model_25211_336c083f_0011():
    """Model: Base plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5000, perimeter: 300
            with BuildLine():
                Line((-25, 50), (25, 50))
                Line((-25, -50), (-25, 50))
                Line((25, -50), (-25, -50))
                Line((25, 50), (25, -50))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a torus or ring-shaped spacer with a large central hole and a mesh-textured outer surface, featuring a smooth inner diameter and curved toroidal geometry.
def model_25211_336c083f_0017():
    """Model: 9-Bearing v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.638937829, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: A rounded rectangular bar or rod with hemispherical end caps, featuring a simple cylindrical profile with no holes or additional features.
def model_25216_ff3bf7e2_0003():
    """Model: my handle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a horizontal rod or shaft with circular holes at both ends for attachment or assembly purposes.
def model_25338_2a285026_0011():
    """Model: Connecting Rod 1 v2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2983567062, perimeter: 7.4432651858
            with BuildLine():
                Line((1.3633974596, 0.05), (-1.3633974596, 0.05))
                CenterArc((-1.45, 0), 0.1, 30, 300)
                Line((-1.3633974596, -0.05), (1.3633974596, -0.05))
                CenterArc((1.45, 0), 0.1, -150, 300)
            make_face()
            with BuildLine():
                CenterArc((-1.45, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.45, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a black plastic or composite housing/enclosure with an irregular hexagonal or trapezoidal shape, featuring open slots or ventilation cutouts on multiple sides and a blue transparent panel or window on the upper surface.
def model_25338_2a285026_0013():
    """Model: Connecting Bracket 1_MDP v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1177133013, perimeter: 3.0318045293
            with BuildLine():
                Line((0, 0.1499999966), (0, -0.1500000034))
                Line((0, -0.1500000034), (0.3000000045, -0.1500000034))
                Line((0.3000000045, -0.1500000034), (0.6160208295, -0.098708323))
                CenterArc((0.6, 0), 0.1, -80.7810133952, 161.562028103)
                Line((0.3, 0.1499999966), (0.6160208272, 0.0987083233))
                Line((0, 0.1499999966), (0.3, 0.1499999966))
            make_face()
            with BuildLine():
                CenterArc((0.15, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6, 0), 0.0675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a clevis rod or clevis link — a mechanical fastener with a elongated rectangular body featuring two circular holes at each end for pin/bolt attachment, commonly used in machinery and structural connections.
def model_25338_2a285026_0020():
    """Model: Mechanism Wheel Drive Minor v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5241549619, perimeter: 7.0508207704
            with BuildLine():
                CenterArc((-0.7, 0), 0.200000003, 29.9999995071, 108.5903782761)
                CenterArc((-1, 0), 0.2, 41.4096229698, 277.1807540604)
                CenterArc((-0.7, 0), 0.200000003, -138.5903777832, 108.5903782761)
                Line((0.8267949192, -0.1), (-0.5267949158, -0.1))
                CenterArc((1, 0), 0.2, -150, 300)
                Line((-0.5267949158, 0.1), (0.8267949192, 0.1))
            make_face()
            with BuildLine():
                CenterArc((1, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a horizontal axle or shaft assembly consisting of a cylindrical dark blue/navy rod with two dark gray wheel hubs or flanges mounted on each end, each featuring a central hole for mounting.
def model_25338_2a285026_0021():
    """Model: Mechanism Wheel Drive Major"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6916862071, perimeter: 8.3292705134
            with BuildLine():
                CenterArc((1.3, 0), 0.2, -150, 108.5903821933)
                CenterArc((1.6000000238, 0), 0.200000003, -138.5903829463, 277.1807658926)
                CenterArc((1.3, 0), 0.2, 41.4096178067, 108.5903821933)
                Line((-0.5267949158, 0.1), (1.1267949192, 0.1))
                CenterArc((-0.7, 0), 0.200000003, 29.9999995071, 108.5903782761)
                CenterArc((-1, 0), 0.2, 41.4096229698, 277.1807540604)
                CenterArc((-0.7, 0), 0.200000003, -138.5903777832, 108.5903782761)
                Line((1.1267949192, -0.1), (-0.5267949158, -0.1))
            make_face()
            with BuildLine():
                CenterArc((-0.7, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.3, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a dumbbell or barbell connector featuring a cylindrical central bar with two circular flanged ends, each containing a large central hole for weight plate attachment.
def model_25338_6583bda1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.07507189, perimeter: 2.7490177197
            with BuildLine():
                CenterArc((0.2999999401, -0.0001895096), 0.1, -150.1252995712, 299.9998415961)
                Line((-0.21350709, 0.05), (0.21350709, 0.05))
                CenterArc((-0.2999999401, -0.0001895096), 0.1, 30.1254579751, 299.9998415961)
                Line((-0.2132882624, -0.05), (0.2132882624, -0.05))
            make_face()
            with BuildLine():
                CenterArc((0.2999999401, -0.0001895096), 0.0675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.2999999401, -0.0001895096), 0.0675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a flat metal tie rod or suspension link featuring a long rectangular bar with reinforced end flanges containing elongated slots for mounting or pivoting connections at both ends.
def model_25338_6b1e4a2c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2705027245, perimeter: 6.9574244511
            with BuildLine():
                Line((2.3, -0.1), (2.5, -0.1))
                CenterArc((2.5, 0), 0.1, -90, 180)
                Line((2.5, 0.1), (2.3, 0.1))
                CenterArc((2.3, 0), 0.1, 90, 60)
                Line((0.0866025404, 0.05), (2.2133974596, 0.05))
                CenterArc((0, 0), 0.1, 30, 300)
                Line((2.2133974596, -0.05), (0.0866025404, -0.05))
                CenterArc((2.3, 0), 0.1, -150, 60)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.3, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a metal strap or bracket with an elongated rectangular shape featuring a circular hole on the left end and multiple elongated slots on the right end for fastening or adjustment purposes.
def model_25338_b3f9f319_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2976667204, perimeter: 5.6105010945
            with BuildLine():
                Line((1.4999999665, 0.1), (0.078062475, 0.0625))
                CenterArc((0, 0), 0.1, 38.6821874535, 282.635625093)
                Line((1.4999999665, -0.1), (0.078062475, -0.0625))
                Line((1.9, -0.1), (1.4999999665, -0.1))
                Line((1.9, 0.1), (1.9, -0.1))
                Line((1.4999999665, 0.1), (1.9, 0.1))
            make_face()
            with BuildLine():
                CenterArc((1.4999999665, 0), 0.0675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.7, 0), 0.0675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.0675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a stylus or pen-like tool with a long, tapered cylindrical shaft that gradually narrows toward a pointed tip at one end, featuring a slightly flattened or faceted diamond-shaped point for precision work.
def model_25364_b3985755_0003():
    """Model: Trigger Lock v14 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4577133774, perimeter: 15.8885039734
            with BuildLine():
                Line((0, 0), (-1.3716, 0))
                Line((-1.3716, 0), (-7.394823675, 1.6139179195))
                Line((-7.394823675, 1.6139179195), (-7.554843675, 1.6139179195))
                Line((-7.554843675, 1.6139179195), (-7.554843675, 1.4513579195))
                Line((-7.554843675, 1.4513579195), (-7.5143631689, 1.4513579195))
                Line((-7.5143631689, 1.4513579195), (-1.3963454034, -0.18796))
                Line((0, -0.18796), (-1.3963454034, -0.18796))
                Line((0, 0), (0, -0.18796))
            make_face()
        # Symmetric extrude, each_side=0.34544
        extrude(amount=0.34544, both=True)
    return part.part


# Description: This is a linear ski or snowboard with a tapered, elongated rectangular shape, featuring a slight curve along its length, rounded edges, and what appears to be a central groove or channel running along the top surface for structural reinforcement and performance.
def model_25365_60f03255_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3189683823, perimeter: 22.3965595328
            with BuildLine():
                Line((0.5, -0.4), (2.518611256, -0.2493062798))
                CenterArc((2.5, 0), 0.25, -85.7306646313, 171.4613292626)
                Line((0.5, 0.4), (2.518611256, 0.2493062798))
                Line((0.5, 0.4), (-2.5124585833, 0.2496893744))
                CenterArc((-2.5, 0), 0.25, 92.8564801165, 174.2870397671)
                Line((0.5, -0.4), (-2.5124585833, -0.2496893744))
            make_face()
            with BuildLine():
                CenterArc((1.75, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.15, 0), 0.26, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.15, 0), 0.26, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.75, 0), 0.24, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.3, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.8, 0), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a sound suppressor (silencer) featuring a long, tapered cylindrical body with a slightly larger diameter at the front end and a smaller threaded connection point at the rear, designed to reduce firearm noise.
def model_25365_b2552618_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # Symmetric extrude, each_side=1.25
        extrude(amount=1.25, both=True)
    return part.part


# Description: This is a rectangular parallelepiped (box-shaped solid) with a triangular wedge or chamfered cut on the left end, creating an angled face that tapers the part.
def model_25365_bb0e4ede_0000():
    """Model: Base Support v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.76, perimeter: 7
            with BuildLine():
                Line((1.15, -0.6), (-1.15, -0.6))
                Line((1.15, 0.6), (1.15, -0.6))
                Line((-1.15, 0.6), (1.15, 0.6))
                Line((-1.15, -0.6), (-1.15, 0.6))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a horizontal elongated bar or rail component with a rounded rectangular profile featuring two parallel blue slots or grooves running along its length, commonly used as a mounting rail or guide track.
def model_25365_bb0e4ede_0010():
    """Model: Crankrod 1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2453960138, perimeter: 8.318583772
            with BuildLine():
                CenterArc((-1.2000001488, 0), 0.25, 89.9999520653, 180.0000958663)
                Line((1.1999999396, -0.25), (-1.1999999396, -0.25))
                CenterArc((1.1999998512, 0), 0.25, -89.9999797356, 179.999959493)
                Line((-1.1999999396, 0.25), (1.1999999395, 0.25))
            make_face()
            with BuildLine():
                CenterArc((1.1999998512, 0), 0.155, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2000001488, 0), 0.155, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a elongated rectangular connector or bracket with rounded ends, featuring two parallel slots or grooves running along its top surface and mounting points on either end.
def model_25365_bb0e4ede_0013():
    """Model: Crankrod 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2953960138, perimeter: 8.518583772
            with BuildLine():
                CenterArc((-1.2500002084, 0), 0.25, 90, 180)
                Line((1.2500002084, -0.25), (-1.2500002084, -0.25))
                CenterArc((1.2499997916, 0), 0.25, -89.9999044606, 179.9998089225)
                Line((-1.2500002084, 0.25), (1.2500002084, 0.25))
            make_face()
            with BuildLine():
                CenterArc((1.2499997916, 0), 0.155, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2500002084, 0), 0.155, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a cylindrical roller or shaft with a knurled or textured surface pattern along its length, featuring rounded ends and a dark gray finish.
def model_25365_eaa0fb26_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a curved sheet metal bracket or housing with two rectangular box-like sections connected by a curved transition, featuring open top surfaces and reinforcing ribs or internal structure visible through the wireframe.
def model_25375_3a1db479_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.9198866183, perimeter: 23.6719621628
            with BuildLine():
                Line((-3.489, 2.07), (-3.489, -0.315))
                CenterArc((-1.734, -0.315), 1.755, -180, 90)
                Line((1.174, -2.07), (-1.734, -2.07))
                Line((1.174, -1.366), (1.174, -2.07))
                Line((1.174, -1.366), (-1.734, -1.366))
                CenterArc((-1.8120177445, -0.5255), 0.844113155, -135.9783185994, 51.2814895617)
                Line((-2.419, 1.1121), (-2.419, -1.1121))
                CenterArc((-1.8120177445, 0.5255), 0.844113155, 84.6968290378, 51.2814895617)
                Line((1.174, 1.366), (-1.734, 1.366))
                Line((1.174, 2.07), (1.174, 1.366))
                Line((-3.489, 2.07), (1.174, 2.07))
            make_face()
        # Symmetric extrude, each_side=1.17
        extrude(amount=1.17, both=True)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a simple planar surface and beveled or angled edges, featuring no holes, slots, or additional features—essentially a thin, four-sided geometric form.
def model_25378_c6523377_0004():
    """Model: P12.TopBack"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.6454461296, perimeter: 18.8148007194
            with BuildLine():
                Line((5.3960507068, -4.0113496529), (0, -4.0113496529))
                Line((5.3960507068, 0), (5.3960507068, -4.0113496529))
                Line((0, 0), (5.3960507068, 0))
                Line((0, -4.0113496529), (0, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a torus or ring-shaped component with a large central hole and a curved, mesh-textured surface that tapers toward the edges, featuring a smooth, donut-like geometry.
def model_25378_c6523377_0006():
    """Model: Washer-M3-steel-mono42855407"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7147123287, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a flat, trapezoidal plate or base component with a uniform thickness, featuring a parallelogram-like shape when viewed from above with no holes, slots, or additional features.
def model_25378_c6523377_0009():
    """Model: Pertier v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((-2, 2), (-2, -2))
                Line((-2, -2), (2, -2))
                Line((2, -2), (2, 2))
                Line((2, 2), (-2, 2))
            make_face()
        # OneSide extrude, distance=0.356
        extrude(amount=0.356)
    return part.part


# Description: This is a toroidal (donut-shaped) rubber or elastomer ring featuring a smooth outer surface with a central circular opening, commonly used as a gasket, seal, or vibration dampening component.
def model_25378_c6523377_0014():
    """Model: Washer-M3-steel v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2712576761, perimeter: 3.1541590242
            with BuildLine():
                CenterArc((0, 0), 0.337, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)
    return part.part


# Description: This is a trapezoidal prism or wedge-shaped component with an elongated rectangular base, angled top surfaces, and a tapered profile that narrows toward one end, featuring flat faces on all sides with no holes or slots.
def model_25380_a3a68e11_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.4128824, perimeter: 13.08608
            with BuildLine():
                Line((2.73304, -3.81), (0, -3.81))
                Line((2.73304, 0), (2.73304, -3.81))
                Line((0, 0), (2.73304, 0))
                Line((0, -3.81), (0, 0))
            make_face()
        # OneSide extrude, distance=0.9398
        extrude(amount=0.9398)
    return part.part


# Description: This is a rectangular duct or enclosure with a slanted/angled top cover, featuring a cylindrical or curved bottom section with vertical ribbing or fluting on its sides, and a flat or gently curved upper surface with an offset lid or flange.
def model_25380_c892ca4e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.2208169269, perimeter: 18.486019092
            with BuildLine():
                CenterArc((1.17856, -1.6211296), 1.6211296, 43.3645832265, 93.270833547)
                Line((0, -7.112), (0, -0.508))
                CenterArc((1.17856, -5.9988704), 1.6211296, -136.6354167735, 93.270833547)
                Line((2.35712, -0.508), (2.35712, -7.112))
            make_face()
        # OneSide extrude, distance=3.4798
        extrude(amount=3.4798)
    return part.part


# Description: This is a black tapered connector or adapter with a rectangular cross-section that narrows to a pointed tip, featuring a grooved or slotted upper section and a conical lower section.
def model_25387_28d66a17_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 32.1441119184, perimeter: 33.0639561273
            with BuildLine():
                Line((0, 0.635), (5.3843519613, 1.011510567))
                CenterArc((0, 0), 0.635, 90, 180)
                Line((0, -0.635), (5.3843519613, -1.011510567))
                Line((5.3843519613, -1.011510567), (5.7055866424, -1.487760567))
                Line((5.7055866424, -1.487760567), (12.85875, -1.487760567))
                Line((12.85875, -1.487760567), (13.4671752936, 0.9525))
                Line((13.4671752936, 0.9525), (12.9909252936, 0.9525))
                Line((12.9909252936, 0.9525), (12.6298874824, 1.487760567))
                Line((5.7055866424, 1.487760567), (12.6298874824, 1.487760567))
                Line((5.3843519613, 1.011510567), (5.7055866424, 1.487760567))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.224536, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a torus or ring-shaped component with a flattened, disc-like profile featuring a large central hole and radial ridge patterns or fins on its outer surfaces, suggesting it may function as a heat sink, bearing, or structural ring element.
def model_25393_9ff2a7d6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 135.0884841044, perimeter: 59.8477367395
            with BuildLine():
                CenterArc((0, 0), 7, 0, 360)
            make_face()
            with BuildLine():
                EllipticalCenterArc((0, 0), 3, 2, 0, 360, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical disk or wheel with a flat circular face and a curved outer edge, featuring a textured or mesh-patterned rim section on one side.
def model_25395_5e6c2bd3_0000():
    """Model: Magnet v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            Circle(0.9525)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)
    return part.part


# Description: This is a parallelogram-shaped plate or panel with a slightly beveled or chamfered edge on the left side, featuring a uniform flat surface with a subtle 3D depth.
def model_25395_5e6c2bd3_0003():
    """Model: Tinyduino Battery v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.84, perimeter: 8.8
            with BuildLine():
                Line((1.1, -1.1), (-1.1, -1.1))
                Line((1.1, 1.1), (1.1, -1.1))
                Line((-1.1, 1.1), (1.1, 1.1))
                Line((-1.1, -1.1), (-1.1, 1.1))
            make_face()
        # OneSide extrude, distance=0.368
        extrude(amount=0.368)
    return part.part


MODELS = {
    "model_23554_a0845d54_0003": {"func": model_23554_a0845d54_0003, "volume": 6.7764463343, "area": 53.76381627},
    "model_23554_a0845d54_0006": {"func": model_23554_a0845d54_0006, "volume": 8.3939428713, "area": 52.1308030955},
    "model_23568_4de5a366_0000": {"func": model_23568_4de5a366_0000, "volume": 1665274829.8998458385, "area": 9334905.2903724983},
    "model_23602_5daaccf5_0001": {"func": model_23602_5daaccf5_0001, "volume": 4.0902936688, "area": 35.334374518},
    "model_23602_5daaccf5_0003": {"func": model_23602_5daaccf5_0003, "volume": 0.4581079487, "area": 4.3702792653},
    "model_23649_45d06d26_0000": {"func": model_23649_45d06d26_0000, "volume": 0.0353429174, "area": 0.9778207134},
    "model_23649_45d06d26_0002": {"func": model_23649_45d06d26_0002, "volume": 0.0320000013, "area": 1.4400000557},
    "model_23649_45d06d26_0004": {"func": model_23649_45d06d26_0004, "volume": 11.3882733693, "area": 68.4521788708},
    "model_23681_932e722e_0005": {"func": model_23681_932e722e_0005, "volume": 0.0114029124, "area": 2.3737111122},
    "model_23681_932e722e_0006": {"func": model_23681_932e722e_0006, "volume": 0.0157532194, "area": 3.2903109876},
    "model_23681_932e722e_0012": {"func": model_23681_932e722e_0012, "volume": 0.0267253542, "area": 2.3643311671},
    "model_23681_932e722e_0015": {"func": model_23681_932e722e_0015, "volume": 0.1571836108, "area": 2.6673582437},
    "model_23706_ef15ef9c_0003": {"func": model_23706_ef15ef9c_0003, "volume": 0.5252353805, "area": 10.8531946901},
    "model_23706_ef15ef9c_0005": {"func": model_23706_ef15ef9c_0005, "volume": 8.4106192983, "area": 29.8477868423},
    "model_23706_ef15ef9c_0007": {"func": model_23706_ef15ef9c_0007, "volume": 2.3199381532, "area": 29.0638681913},
    "model_23706_ef15ef9c_0008": {"func": model_23706_ef15ef9c_0008, "volume": 0.9355774035, "area": 16.3450972965},
    "model_23706_ef15ef9c_0009": {"func": model_23706_ef15ef9c_0009, "volume": 1.3510362535, "area": 20.589452036},
    "model_23751_5e8bc03f_0008": {"func": model_23751_5e8bc03f_0008, "volume": 1.0141851536, "area": 8.3910758539},
    "model_23770_f35c1c3b_0006": {"func": model_23770_f35c1c3b_0006, "volume": 12, "area": 50},
    "model_23770_f35c1c3b_0012": {"func": model_23770_f35c1c3b_0012, "volume": 437.76, "area": 2964.24},
    "model_23774_716b8bc4_0003": {"func": model_23774_716b8bc4_0003, "volume": 7.1628312502, "area": 40.5893770844},
    "model_23790_2abde9b6_0001": {"func": model_23790_2abde9b6_0001, "volume": 25.1115955133, "area": 114.4698963702},
    "model_23792_5b4c1ce0_0001": {"func": model_23792_5b4c1ce0_0001, "volume": 520.6606227999, "area": 1756.4808209285},
    "model_23792_5b4c1ce0_0002": {"func": model_23792_5b4c1ce0_0002, "volume": 89.2759655624, "area": 1127.665575509},
    "model_23792_5b4c1ce0_0022": {"func": model_23792_5b4c1ce0_0022, "volume": 133.9139483436, "area": 1690.0338625161},
    "model_23801_7ebe01f7_0000": {"func": model_23801_7ebe01f7_0000, "volume": 136.7606845737, "area": 285.6587750424},
    "model_23862_7a684f76_0000": {"func": model_23862_7a684f76_0000, "volume": 15504.3208021061, "area": 18196.1571869978},
    "model_23876_74957d38_0008": {"func": model_23876_74957d38_0008, "volume": 2.4494648229, "area": 31.1967358359},
    "model_23881_bec7f38c_0000": {"func": model_23881_bec7f38c_0000, "volume": 22.7042901075, "area": 157.5822875041},
    "model_23881_bec7f38c_0003": {"func": model_23881_bec7f38c_0003, "volume": 0.3392920066, "area": 14.7026536188},
    "model_23881_bec7f38c_0004": {"func": model_23881_bec7f38c_0004, "volume": 1.4074335088, "area": 18.0955736847},
    "model_23881_bec7f38c_0010": {"func": model_23881_bec7f38c_0010, "volume": 0.0226194671, "area": 1.9603538158},
    "model_23881_bec7f38c_0012": {"func": model_23881_bec7f38c_0012, "volume": 2.1696624264, "area": 22.4623874732},
    "model_23881_bec7f38c_0015": {"func": model_23881_bec7f38c_0015, "volume": 0.2199114858, "area": 6.5973445725},
    "model_23910_316134bd_0011": {"func": model_23910_316134bd_0011, "volume": 2.300863, "area": 95.31154},
    "model_23910_316134bd_0014": {"func": model_23910_316134bd_0014, "volume": 1.623750645, "area": 61.021111},
    "model_23913_b3ac2abf_0000": {"func": model_23913_b3ac2abf_0000, "volume": 114.770031154, "area": 403.3144329773},
    "model_23956_ee17fe48_0003": {"func": model_23956_ee17fe48_0003, "volume": 235.6194490192, "area": 251.3274122872},
    "model_24013_13d47495_0002": {"func": model_24013_13d47495_0002, "volume": 1.0414379647, "area": 14.6869456555},
    "model_24032_d6172503_0005": {"func": model_24032_d6172503_0005, "volume": 14.0447158823, "area": 49.1181482727},
    "model_24032_d6172503_0009": {"func": model_24032_d6172503_0009, "volume": 0.6511932522, "area": 10.2612270048},
    "model_24032_d6172503_0014": {"func": model_24032_d6172503_0014, "volume": 2.6725351569, "area": 26.7590266269},
    "model_24032_d6172503_0028": {"func": model_24032_d6172503_0028, "volume": 46.98829312, "area": 224.950528},
    "model_24032_d6172503_0031": {"func": model_24032_d6172503_0031, "volume": 0.0157079637, "area": 0.4546555714},
    "model_24047_9eb475f0_0002": {"func": model_24047_9eb475f0_0002, "volume": 1817.5210895334, "area": 2054.7591861664},
    "model_24047_9eb475f0_0008": {"func": model_24047_9eb475f0_0008, "volume": 5.4076023799, "area": 35.2961108544},
    "model_24051_4852a192_0003": {"func": model_24051_4852a192_0003, "volume": 12.8935078516, "area": 52.5307998124},
    "model_24051_4852a192_0004": {"func": model_24051_4852a192_0004, "volume": 4.7986703182, "area": 25.2069664602},
    "model_24070_485194e7_0004": {"func": model_24070_485194e7_0004, "volume": 0.0111199997, "area": 0.3283464465},
    "model_24090_a2bf0d93_0001": {"func": model_24090_a2bf0d93_0001, "volume": 0.0387140729, "area": 0.8269466059},
    "model_24131_3ea7d5a8_0022": {"func": model_24131_3ea7d5a8_0022, "volume": 8.4393384987, "area": 72.5327243182},
    "model_24146_08d7c016_0000": {"func": model_24146_08d7c016_0000, "volume": 17.3795273174, "area": 57.3691064359},
    "model_24195_9791f5d3_0003": {"func": model_24195_9791f5d3_0003, "volume": 0.0120637158, "area": 0.5428672105},
    "model_24195_9791f5d3_0004": {"func": model_24195_9791f5d3_0004, "volume": 0.2638937829, "area": 6.5973445725},
    "model_24195_9791f5d3_0011": {"func": model_24195_9791f5d3_0011, "volume": 0.0129072334, "area": 0.5866924281},
    "model_24195_9791f5d3_0022": {"func": model_24195_9791f5d3_0022, "volume": 0.0824668072, "area": 1.7318029503},
    "model_24195_9791f5d3_0025": {"func": model_24195_9791f5d3_0025, "volume": 0.0160722207, "area": 0.5163901527},
    "model_24195_9791f5d3_0034": {"func": model_24195_9791f5d3_0034, "volume": 0.259477497, "area": 3.774200656},
    "model_24195_9791f5d3_0035": {"func": model_24195_9791f5d3_0035, "volume": 0.1291756975, "area": 1.7090524227},
    "model_24195_9791f5d3_0039": {"func": model_24195_9791f5d3_0039, "volume": 0.0942477796, "area": 2.2619467106},
    "model_24221_0b711dbf_0004": {"func": model_24221_0b711dbf_0004, "volume": 168.9911485751, "area": 176.2654824574},
    "model_24221_0b711dbf_0005": {"func": model_24221_0b711dbf_0005, "volume": 30.9038514942, "area": 127.651189355},
    "model_24230_636208ab_0005": {"func": model_24230_636208ab_0005, "volume": 1.2203693748, "area": 13.8398614458},
    "model_24230_636208ab_0009": {"func": model_24230_636208ab_0009, "volume": 0.1130064891, "area": 1.3970820763},
    "model_24230_636208ab_0014": {"func": model_24230_636208ab_0014, "volume": 0.3675663405, "area": 5.042256209},
    "model_24230_636208ab_0015": {"func": model_24230_636208ab_0015, "volume": 0.3301224489, "area": 8.481996323},
    "model_24230_636208ab_0019": {"func": model_24230_636208ab_0019, "volume": 0.4869468613, "area": 11.6867246714},
    "model_24250_dd7e0408_0001": {"func": model_24250_dd7e0408_0001, "volume": 0.0476147637, "area": 0.8600109889},
    "model_24250_dd7e0408_0003": {"func": model_24250_dd7e0408_0003, "volume": 0.0436877728, "area": 0.7971791358},
    "model_24250_dd7e0408_0007": {"func": model_24250_dd7e0408_0007, "volume": 0.0417242774, "area": 0.7657632093},
    "model_24250_dd7e0408_0009": {"func": model_24250_dd7e0408_0009, "volume": 0.0505600068, "area": 0.9071348787},
    "model_24250_dd7e0408_0010": {"func": model_24250_dd7e0408_0010, "volume": 0.0456512682, "area": 0.8285950624},
    "model_24250_dd7e0408_0011": {"func": model_24250_dd7e0408_0011, "volume": 0.0387790343, "area": 0.7186393195},
    "model_24250_dd7e0408_0017": {"func": model_24250_dd7e0408_0017, "volume": 0.0441786467, "area": 0.8050331175},
    "model_24267_8a216138_0001": {"func": model_24267_8a216138_0001, "volume": 12.813641773, "area": 89.2024835377},
    "model_24267_8a216138_0003": {"func": model_24267_8a216138_0003, "volume": 0.2284036859, "area": 4.523003514},
    "model_24284_3710e946_0000": {"func": model_24284_3710e946_0000, "volume": 2.9208532423, "area": 19.7494307053},
    "model_24300_ed2686dc_0006": {"func": model_24300_ed2686dc_0006, "volume": 1.0367255757, "area": 41.6418106233},
    "model_24300_ed2686dc_0010": {"func": model_24300_ed2686dc_0010, "volume": 3.1777209691, "area": 12.0165919},
    "model_24300_ed2686dc_0011": {"func": model_24300_ed2686dc_0011, "volume": 0.1549956622, "area": 6.4114991462},
    "model_24300_ed2686dc_0014": {"func": model_24300_ed2686dc_0014, "volume": 2.3460136589, "area": 30.034519889},
    "model_24315_6ffc3461_0002": {"func": model_24315_6ffc3461_0002, "volume": 395.2980591698, "area": 524.099348477},
    "model_24330_a1e03326_0000": {"func": model_24330_a1e03326_0000, "volume": 824.6680715673, "area": 989.6016858808},
    "model_24331_fb99e8e6_0003": {"func": model_24331_fb99e8e6_0003, "volume": 0.0611599981, "area": 2.1028765749},
    "model_24372_03b260fe_0014": {"func": model_24372_03b260fe_0014, "volume": 6.4402649399, "area": 27.3318560862},
    "model_24372_03b260fe_0016": {"func": model_24372_03b260fe_0016, "volume": 106.8141502221, "area": 219.9114857513},
    "model_24372_03b260fe_0017": {"func": model_24372_03b260fe_0017, "volume": 1.935, "area": 20.58},
    "model_24372_03b260fe_0020": {"func": model_24372_03b260fe_0020, "volume": 1116.8361883512, "area": 983.5217694388},
    "model_24372_03b260fe_0025": {"func": model_24372_03b260fe_0025, "volume": 0.0659205345, "area": 3.333852001},
    "model_24372_03b260fe_0029": {"func": model_24372_03b260fe_0029, "volume": 447.67131962, "area": 495.6735606482},
    "model_24405_b96b34b6_0000": {"func": model_24405_b96b34b6_0000, "volume": 0.1528352152, "area": 4.8516082187},
    "model_24405_b96b34b6_0001": {"func": model_24405_b96b34b6_0001, "volume": 0.1590320852, "area": 5.1069075502},
    "model_24405_b96b34b6_0002": {"func": model_24405_b96b34b6_0002, "volume": 0.1128364881, "area": 3.7901200385},
    "model_24405_b96b34b6_0007": {"func": model_24405_b96b34b6_0007, "volume": 0.5771340677, "area": 24.2075676103},
    "model_24405_b96b34b6_0008": {"func": model_24405_b96b34b6_0008, "volume": 0.3056172946, "area": 9.521007486},
    "model_24405_b96b34b6_0009": {"func": model_24405_b96b34b6_0009, "volume": 0.1090609283, "area": 3.8159658528},
    "model_24405_b96b34b6_0012": {"func": model_24405_b96b34b6_0012, "volume": 0.1561728767, "area": 5.0157447004},
    "model_24405_b96b34b6_0013": {"func": model_24405_b96b34b6_0013, "volume": 0.2126088597, "area": 7.059875207},
    "model_24405_b96b34b6_0014": {"func": model_24405_b96b34b6_0014, "volume": 0.2746043847, "area": 16.5293841409},
    "model_24405_b96b34b6_0015": {"func": model_24405_b96b34b6_0015, "volume": 0.1172437358, "area": 3.9686651183},
    "model_24405_b96b34b6_0016": {"func": model_24405_b96b34b6_0016, "volume": 0.3396662414, "area": 10.5381671215},
    "model_24405_b96b34b6_0017": {"func": model_24405_b96b34b6_0017, "volume": 0.4697794048, "area": 13.7723067232},
    "model_24412_a8e106be_0004": {"func": model_24412_a8e106be_0004, "volume": 0.0408407045, "area": 1.3477432484},
    "model_24412_a8e106be_0005": {"func": model_24412_a8e106be_0005, "volume": 3.2333190113, "area": 16.5794500769},
    "model_24412_a8e106be_0006": {"func": model_24412_a8e106be_0006, "volume": 0.6144262977, "area": 7.5552605584},
    "model_24412_a8e106be_0009": {"func": model_24412_a8e106be_0009, "volume": 65.6, "area": 124.24},
    "model_24412_a8e106be_0010": {"func": model_24412_a8e106be_0010, "volume": 1.68, "area": 14.08},
    "model_24415_217d80f6_0000": {"func": model_24415_217d80f6_0000, "volume": 0.0019964793, "area": 0.0942637289},
    "model_24430_90535b35_0000": {"func": model_24430_90535b35_0000, "volume": 10022.0494602496, "area": 5131.5462786375},
    "model_24443_996411f9_0002": {"func": model_24443_996411f9_0002, "volume": 258, "area": 352.4},
    "model_24448_75004b6c_0005": {"func": model_24448_75004b6c_0005, "volume": 23.848761102, "area": 115.0499111843},
    "model_24448_75004b6c_0006": {"func": model_24448_75004b6c_0006, "volume": 54.5903991663, "area": 98.2347315867},
    "model_24448_75004b6c_0007": {"func": model_24448_75004b6c_0007, "volume": 144, "area": 212},
    "model_24470_21c25a2d_0002": {"func": model_24470_21c25a2d_0002, "volume": 33.0809706423, "area": 78.6026481928},
    "model_24470_21c25a2d_0003": {"func": model_24470_21c25a2d_0003, "volume": 11.8752202306, "area": 83.126541614},
    "model_24470_21c25a2d_0008": {"func": model_24470_21c25a2d_0008, "volume": 3.0723088013, "area": 20.0944376735},
    "model_24470_21c25a2d_0009": {"func": model_24470_21c25a2d_0009, "volume": 15.2681402964, "area": 39.0185807576},
    "model_24472_5019aefa_0000": {"func": model_24472_5019aefa_0000, "volume": 15.4702804541, "area": 77.0225812847},
    "model_24476_568e9ca0_0006": {"func": model_24476_568e9ca0_0006, "volume": 0.4700216611, "area": 5.0786867343},
    "model_24476_568e9ca0_0015": {"func": model_24476_568e9ca0_0015, "volume": 0.2549852541, "area": 4.7838715854},
    "model_24476_568e9ca0_0022": {"func": model_24476_568e9ca0_0022, "volume": 0.0282743339, "area": 0.9424777961},
    "model_24540_92ecb906_0000": {"func": model_24540_92ecb906_0000, "volume": 2.92695, "area": 17.9718},
    "model_24543_6b6469fa_0003": {"func": model_24543_6b6469fa_0003, "volume": 4.0501145447, "area": 37.5831059809},
    "model_24544_d06c82dd_0008": {"func": model_24544_d06c82dd_0008, "volume": 0.2137346054, "area": 3.6018021131},
    "model_24544_d06c82dd_0009": {"func": model_24544_d06c82dd_0009, "volume": 0.0032162055, "area": 0.2389181213},
    "model_24603_a4021250_0000": {"func": model_24603_a4021250_0000, "volume": 268.0991118431, "area": 2689.9277554922},
    "model_24603_a4021250_0002": {"func": model_24603_a4021250_0002, "volume": 4500, "area": 18230},
    "model_24603_a4021250_0005": {"func": model_24603_a4021250_0005, "volume": 162.3397667279, "area": 1092.8755537894},
    "model_24603_a4021250_0008": {"func": model_24603_a4021250_0008, "volume": 19.7990444078, "area": 84.9449946276},
    "model_24612_e91cc2f4_0001": {"func": model_24612_e91cc2f4_0001, "volume": 8.2853981634, "area": 43.2123889804},
    "model_24627_7ee9cadb_0006": {"func": model_24627_7ee9cadb_0006, "volume": 9.9895409812, "area": 34.9790810001},
    "model_24659_d2ba8a0f_0000": {"func": model_24659_d2ba8a0f_0000, "volume": 77.7544181763, "area": 117.8097245096},
    "model_24722_02c0cd8a_0000": {"func": model_24722_02c0cd8a_0000, "volume": 100, "area": 430},
    "model_24788_26865dc0_0000": {"func": model_24788_26865dc0_0000, "volume": 193.7168146928, "area": 318.2831853072},
    "model_24869_5c729cf1_0003": {"func": model_24869_5c729cf1_0003, "volume": 0.548239334, "area": 17.5140711677},
    "model_24890_5f8a67df_0006": {"func": model_24890_5f8a67df_0006, "volume": 9.8538770076, "area": 128.577022821},
    "model_24890_5f8a67df_0010": {"func": model_24890_5f8a67df_0010, "volume": 16.188511816, "area": 116.5427177667},
    "model_24890_5f8a67df_0012": {"func": model_24890_5f8a67df_0012, "volume": 11.3799732519, "area": 119.0612527073},
    "model_24890_5f8a67df_0013": {"func": model_24890_5f8a67df_0013, "volume": 6.2340854538, "area": 58.9047444451},
    "model_24896_58b4730f_0007": {"func": model_24896_58b4730f_0007, "volume": 0.1452004855, "area": 6.2085724817},
    "model_24896_58b4730f_0012": {"func": model_24896_58b4730f_0012, "volume": 0.1005309649, "area": 3.0159289474},
    "model_24896_58b4730f_0013": {"func": model_24896_58b4730f_0013, "volume": 0.0382017667, "area": 1.7190795},
    "model_24896_58b4730f_0014": {"func": model_24896_58b4730f_0014, "volume": 0.0889280972, "area": 2.0620796327},
    "model_24896_58b4730f_0015": {"func": model_24896_58b4730f_0015, "volume": 38.6888602689, "area": 398.0216446924},
    "model_24896_58b4730f_0016": {"func": model_24896_58b4730f_0016, "volume": 2.1452386759, "area": 27.1137680806},
    "model_24907_c72322ea_0010": {"func": model_24907_c72322ea_0010, "volume": 0.1005309649, "area": 1.5079644737},
    "model_24907_c72322ea_0012": {"func": model_24907_c72322ea_0012, "volume": 9.1269438094, "area": 69.0224059415},
    "model_24907_c72322ea_0013": {"func": model_24907_c72322ea_0013, "volume": 0.9817477042, "area": 5.4977871438},
    "model_25128_d2840160_0000": {"func": model_25128_d2840160_0000, "volume": 6.6125326022, "area": 20.5475867508},
    "model_25156_78e996ae_0001": {"func": model_25156_78e996ae_0001, "volume": 394.4684212354, "area": 479.7036769841},
    "model_25184_9594f8f3_0000": {"func": model_25184_9594f8f3_0000, "volume": 9.3668611705, "area": 99.6202534204},
    "model_25199_39e3c0d3_0004": {"func": model_25199_39e3c0d3_0004, "volume": 0.062986737, "area": 1.6925842733},
    "model_25199_39e3c0d3_0006": {"func": model_25199_39e3c0d3_0006, "volume": 0.026427313, "area": 0.5726495089},
    "model_25199_b2422c18_0005": {"func": model_25199_b2422c18_0005, "volume": 0.1609347591, "area": 4.9350096544},
    "model_25199_b2422c18_0008": {"func": model_25199_b2422c18_0008, "volume": 0.2042013372, "area": 5.8622182758},
    "model_25199_b2422c18_0010": {"func": model_25199_b2422c18_0010, "volume": 40.6822666919, "area": 90.1425208283},
    "model_25199_b2422c18_0011": {"func": model_25199_b2422c18_0011, "volume": 0.0980176908, "area": 5.2024774343},
    "model_25199_d7aff7a5_0014": {"func": model_25199_d7aff7a5_0014, "volume": 0.033617979, "area": 1.4400072461},
    "model_25199_d7aff7a5_0020": {"func": model_25199_d7aff7a5_0020, "volume": 0.2233265271, "area": 3.4899023321},
    "model_25199_d7aff7a5_0022": {"func": model_25199_d7aff7a5_0022, "volume": 0.0284422127, "area": 1.3426774302},
    "model_25203_1cc0cb3c_0000": {"func": model_25203_1cc0cb3c_0000, "volume": 0.2019679495, "area": 3.2264134295},
    "model_25203_1cc0cb3c_0005": {"func": model_25203_1cc0cb3c_0005, "volume": 11.56973328, "area": 52.4542214742},
    "model_25203_1cc0cb3c_0012": {"func": model_25203_1cc0cb3c_0012, "volume": 0.0308425859, "area": 0.9313251422},
    "model_25203_92cee759_0001": {"func": model_25203_92cee759_0001, "volume": 0.246300864, "area": 3.641734204},
    "model_25203_92cee759_0002": {"func": model_25203_92cee759_0002, "volume": 0.2689008879, "area": 4.2569134295},
    "model_25203_92cee759_0004": {"func": model_25203_92cee759_0004, "volume": 0.3871227547, "area": 3.6959266773},
    "model_25203_92cee759_0007": {"func": model_25203_92cee759_0007, "volume": 5.6051553643, "area": 37.239426775},
    "model_25203_92cee759_0009": {"func": model_25203_92cee759_0009, "volume": 0.011957687, "area": 0.6432410958},
    "model_25203_92cee759_0012": {"func": model_25203_92cee759_0012, "volume": 0.0628318531, "area": 1.5079644737},
    "model_25203_92cee759_0014": {"func": model_25203_92cee759_0014, "volume": 0.1272345025, "area": 1.8378317024},
    "model_25211_336c083f_0008": {"func": model_25211_336c083f_0008, "volume": 2.5701238898, "area": 14.8759287967},
    "model_25211_336c083f_0011": {"func": model_25211_336c083f_0011, "volume": 25000, "area": 11500},
    "model_25211_336c083f_0017": {"func": model_25211_336c083f_0017, "volume": 1.8472564803, "area": 11.4353972591},
    "model_25216_ff3bf7e2_0003": {"func": model_25216_ff3bf7e2_0003, "volume": 22.6194671058, "area": 77.6601703967},
    "model_25338_2a285026_0011": {"func": model_25338_2a285026_0011, "volume": 0.0149178353, "area": 0.9688766716},
    "model_25338_2a285026_0013": {"func": model_25338_2a285026_0013, "volume": 0.0235426603, "area": 0.8417875084},
    "model_25338_2a285026_0020": {"func": model_25338_2a285026_0020, "volume": 0.0524154962, "area": 1.7533920009},
    "model_25338_2a285026_0021": {"func": model_25338_2a285026_0021, "volume": 0.0691686207, "area": 2.2162994655},
    "model_25338_6583bda1_0000": {"func": model_25338_6583bda1_0000, "volume": 0.0037535945, "area": 0.2875946659},
    "model_25338_6b1e4a2c_0000": {"func": model_25338_6b1e4a2c_0000, "volume": 0.0135251362, "area": 0.8888766716},
    "model_25338_b3f9f319_0000": {"func": model_25338_b3f9f319_0000, "volume": 0.014883336, "area": 0.8758584955},
    "model_25364_b3985755_0003": {"func": model_25364_b3985755_0003, "volume": 1.0071050182, "area": 13.89247638},
    "model_25365_60f03255_0000": {"func": model_25365_60f03255_0000, "volume": 0.4637936765, "area": 9.1172486712},
    "model_25365_b2552618_0000": {"func": model_25365_b2552618_0000, "volume": 0.1767145868, "area": 2.4975661596},
    "model_25365_bb0e4ede_0000": {"func": model_25365_bb0e4ede_0000, "volume": 1.656, "area": 9.72},
    "model_25365_bb0e4ede_0010": {"func": model_25365_bb0e4ede_0010, "volume": 0.2490792028, "area": 4.1545087821},
    "model_25365_bb0e4ede_0013": {"func": model_25365_bb0e4ede_0013, "volume": 0.2590792028, "area": 4.2945087821},
    "model_25365_eaa0fb26_0000": {"func": model_25365_eaa0fb26_0000, "volume": 0.0251327412, "area": 0.5654866776},
    "model_25375_3a1db479_0000": {"func": model_25375_3a1db479_0000, "volume": 20.8725346869, "area": 73.2321646976},
    "model_25378_c6523377_0004": {"func": model_25378_c6523377_0004, "volume": 4.3290892259, "area": 47.0538524032},
    "model_25378_c6523377_0006": {"func": model_25378_c6523377_0006, "volume": 0.0714712329, "area": 1.8378317024},
    "model_25378_c6523377_0009": {"func": model_25378_c6523377_0009, "volume": 5.696, "area": 37.696},
    "model_25378_c6523377_0014": {"func": model_25378_c6523377_0014, "volume": 0.0217006141, "area": 0.7948480741},
    "model_25380_a3a68e11_0000": {"func": model_25380_a3a68e11_0000, "volume": 9.7860268795, "area": 33.124062784},
    "model_25380_c892ca4e_0000": {"func": model_25380_c892ca4e_0000, "volume": 59.9249987423, "area": 98.7692830901},
    "model_25387_28d66a17_0000": {"func": model_25387_28d66a17_0000, "volume": 10.2057555341, "area": 74.7860299072},
    "model_25393_9ff2a7d6_0000": {"func": model_25393_9ff2a7d6_0000, "volume": 67.5442420522, "area": 300.1008365784},
    "model_25395_5e6c2bd3_0000": {"func": model_25395_5e6c2bd3_0000, "volume": 1.3574218327, "area": 8.5506887098},
    "model_25395_5e6c2bd3_0003": {"func": model_25395_5e6c2bd3_0003, "volume": 1.78112, "area": 12.9184},
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
