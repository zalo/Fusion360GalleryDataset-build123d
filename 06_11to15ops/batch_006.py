"""Batch 006 - passing/06_11to15ops
22 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_82614_a8ef3280_0000():
    """Model: body v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.68438204, perimeter: 3.2805257079
            with BuildLine():
                CenterArc((-0.0058407964, 0.4524675021), 0.15, 30.5566060611, 119.4433939389)
                Line((-0.135744607, 0.5274675021), (-0.5232275146, -0.1436725811))
                CenterArc((-0.3933237041, -0.2186725811), 0.15, 150, 120)
                Line((-0.3933237041, -0.3686725811), (0.3903845712, -0.3686725811))
                CenterArc((0.3903845712, -0.2186725811), 0.15, -90, 120.5566060611)
                Line((0.1233283003, 0.5287259079), (0.5195536679, -0.1424141753))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4896543817, perimeter: 4.8556450651
            with BuildLine():
                CenterArc((0.3933237041, 0.2186725811), 0.15, -30, 120)
                Line((-0.3918336411, 0.3686725811), (0.3933237041, 0.3686725811))
                CenterArc((-0.3918336411, 0.2186725811), 0.15, 90, 120.5566060611)
                Line((-0.1240447529, -0.5299668401), (-0.5210027378, 0.1424141753))
                CenterArc((0.0051243438, -0.4537084343), 0.15, -149.4433939389, 119.4433939389)
                Line((0.5232275146, 0.1436725811), (0.1350281544, -0.5287084343))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-15.5
        extrude(amount=-15.5, mode=Mode.SUBTRACT)
    return part.part


def model_82875_02bdc953_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.8064, perimeter: 20.32
            with BuildLine():
                Line((2.54, -2.54), (-2.54, -2.54))
                Line((2.54, 2.54), (2.54, -2.54))
                Line((-2.54, 2.54), (2.54, 2.54))
                Line((-2.54, -2.54), (-2.54, 2.54))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13.97, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.3848949106, perimeter: 25.7124827145
            with BuildLine():
                CenterArc((0, 0), 1.905, 93.1493446466, 173.7013107068)
                Line((-8.1711208185, 1.9021229279), (-0.1046583361, 1.9021229279))
                Line((-8.1711208185, -1.9021229279), (-8.1711208185, 1.9021229279))
                Line((-0.1046583361, -1.9021229279), (-8.1711208185, -1.9021229279))
            make_face()
            # Profile area: 11.4001151995, perimeter: 11.9692571324
            with BuildLine():
                CenterArc((0, 0), 1.905, 93.1493446466, 173.7013107068)
                Line((0.1046583361, -1.9021229279), (-0.1046583361, -1.9021229279))
                CenterArc((0, 0), 1.905, -86.8506553534, 173.7013107068)
                Line((-0.1046583361, 1.9021229279), (0.1046583361, 1.9021229279))
            make_face()
            # Profile area: 25.3848949106, perimeter: 25.7124827145
            with BuildLine():
                Line((8.1711208185, -1.9021229279), (0.1046583361, -1.9021229279))
                Line((8.1711208185, 1.9021229279), (8.1711208185, -1.9021229279))
                Line((0.1046583361, 1.9021229279), (8.1711208185, 1.9021229279))
                CenterArc((0, 0), 1.905, -86.8506553534, 173.7013107068)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15.24, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.5805377639, perimeter: 21.2211098479
            with BuildLine():
                Line((-4.8642801568, 0.4409973052), (4.8642801568, 0.4409973052))
                Line((-4.8642801568, -0.4409973052), (-4.8642801568, 0.4409973052))
                Line((4.8642801568, -0.4409973052), (-4.8642801568, -0.4409973052))
                Line((4.8642801568, 0.4409973052), (4.8642801568, -0.4409973052))
            make_face()
        # OneSide extrude, distance=60.96
        extrude(amount=60.96, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4409973052), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 39.601215548, perimeter: 38.1402538131
            with BuildLine():
                Line((0, 76.2), (4.8642801568, 59.9175432862))
                Line((4.8642801568, 59.9175432862), (4.8642801568, 76.2))
                Line((4.8642801568, 76.2), (0, 76.2))
            make_face()
            # Profile area: 39.601215548, perimeter: 38.1402538131
            with BuildLine():
                Line((-4.8642801568, 76.2), (-4.8642801568, 59.9175432862))
                Line((0, 76.2), (-4.8642801568, 59.9175432862))
                Line((0, 76.2), (-4.8642801568, 76.2))
            make_face()
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on Profile plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4409973052), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 81.2814018996, perimeter: 90.4901584945
            with BuildLine():
                Line((4.8642801568, 15.24), (2.286000073, 20.3200006485))
                Line((4.8642801568, 15.24), (4.8642801568, 59.9175432862))
                Line((3.5751401149, 58.4920992287), (4.8642801568, 59.9175432862))
                Line((2.286000073, 20.3200006485), (3.5751401149, 58.4920992287))
            make_face()
            # Profile area: 76.3787299779, perimeter: 90.4364632879
            with BuildLine():
                Line((-4.8642801568, 59.9175432862), (-3.5560001135, 58.6740018725))
                Line((-4.8642801568, 59.9175432862), (-4.8642801568, 15.24))
                Line((-4.8642801568, 15.24), (-2.5400000811, 20.3200006485))
                Line((-3.5560001135, 58.6740018725), (-2.5400000811, 20.3200006485))
            make_face()
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)
    return part.part


def model_83407_56b3a419_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 364, perimeter: 80
            with BuildLine():
                Line((16, -7), (-10, -7))
                Line((16, 7), (16, -7))
                Line((-10, 7), (16, 7))
                Line((-10, -7), (-10, 7))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(16, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.031415876, perimeter: 0.6283180251
            with Locations((-5.5, 0.5)):
                Circle(0.0999999195)
            # Profile area: 0.4456637194, perimeter: 2.856637104
            with BuildLine():
                CenterArc((-3.7000000551, 0.5000000075), 0.200000003, -90, 180)
                Line((-3.7000000551, 0.7000000104), (-4.5000000671, 0.7000000104))
                CenterArc((-4.5000000671, 0.5000000075), 0.200000003, 90, 180)
                Line((-4.5000000671, 0.3000000045), (-3.7000000551, 0.3000000045))
            make_face()
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-10, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((2.9904609582, 0.5597475727)):
                Circle(0.175)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-10, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0514159281, perimeter: 0.8283185431
            with BuildLine():
                CenterArc((4.1000000611, 0.5000000075), 0.1000000015, 90, 180)
                Line((4.1000000611, 0.400000006), (4.2000000626, 0.400000006))
                CenterArc((4.2000000626, 0.5000000075), 0.1000000015, -90, 180)
                Line((4.2000000626, 0.6000000089), (4.1000000611, 0.6000000089))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -7), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1914159429, perimeter: 2.2283185511
            with BuildLine():
                CenterArc((1.3999999911, 0.5), 0.1000000089, -90, 180)
                Line((1.3999999911, 0.6000000089), (0.6000000089, 0.6000000089))
                CenterArc((0.6000000089, 0.5), 0.1000000089, 90, 180)
                Line((0.6000000089, 0.3999999911), (1.3999999911, 0.3999999911))
            make_face()
            # Profile area: 0.3818954138, perimeter: 4.3068161451
            with BuildLine():
                Line((1.8000204666, 0.4190810958), (3.6995738543, 0.4000009142))
                CenterArc((3.7000000551, 0.5000000075), 0.1000000015, -90.2441958286, 180.2441958286)
                Line((3.7000000551, 0.6000000089), (1.8587752965, 0.6000000089))
                CenterArc((1.8587752965, 0.5000000075), 0.1000000015, 90, 144.0167802366)
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


def model_83470_1e871838_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((1, -2), (1, 2))
                Line((1, 2), (-1, 2))
                Line((-1, 2), (-1, -2))
                Line((-1, -2), (1, -2))
            make_face()
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1971258343, perimeter: 1.9962679785
            with Locations((0, 1.5000000224)):
                Ellipse(0.454314403, 0.1381138293)
        # OneSide extrude, distance=0.005
        extrude(amount=0.005, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6267121991, perimeter: 5.6267121991
            with BuildLine():
                Line((1, -0.5933219651), (-1, -0.5933219651))
                Line((-1, -0.5933219651), (-1, -1.4066780647))
                Line((-1, -1.4066780647), (1, -1.4066780647))
                Line((1, -1.4066780647), (1, -0.5933219651))
            make_face()
        # OneSide extrude, distance=0.005
        extrude(amount=0.005, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6168722686, perimeter: 3.1441479682
            with BuildLine():
                Line((0.5933219651, 0.75), (0.5896040806, 0.75))
                Line((0.5896040806, 0.75), (0.5896040806, 0))
                Line((0.5896040806, 0), (1.4066780647, 0))
                Line((1.4066780647, 0), (1.4066780647, 0.75))
                Line((1.4066780647, 0.75), (1.4066780647, 0.755))
                Line((1.4066780647, 0.755), (0.5933219651, 0.755))
                Line((0.5933219651, 0.755), (0.5933219651, 0.75))
            make_face()
        # OneSide extrude, distance=0.005
        extrude(amount=0.005, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6148226, perimeter: 3.1386821854
            with BuildLine():
                Line((-1.4066780647, 0.75), (-1.4076630578, 0.75))
                Line((-1.4076630578, 0.75), (-1.4076630578, 0))
                Line((-1.4076630578, 0), (-0.5933219651, 0))
                Line((-0.5933219651, 0), (-0.5933219651, 0.75))
                Line((-0.5933219651, 0.75), (-0.5933219651, 0.755))
                Line((-0.5933219651, 0.755), (-1.4066780647, 0.755))
                Line((-1.4066780647, 0.755), (-1.4066780647, 0.75))
            make_face()
        # OneSide extrude, distance=0.005
        extrude(amount=0.005, mode=Mode.ADD)
    return part.part


def model_84025_ec3401ea_0015():
    """Model: Zunit"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 126, perimeter: 50
            with BuildLine():
                Line((0, 7), (0, 0))
                Line((0, 0), (18, 0))
                Line((18, 0), (18, 7))
                Line((18, 7), (0, 7))
            make_face()
        # OneSide extrude, distance=43
        extrude(amount=43)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 714, perimeter: 118
            with BuildLine():
                Line((0.5, 0.5), (17.5, 0.5))
                Line((17.5, 0.5), (17.5, 42.5))
                Line((17.5, 42.5), (0.5, 42.5))
                Line((0.5, 42.5), (0.5, 0.5))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 306, perimeter: 70
            with BuildLine():
                Line((17.5, 27.9415026443), (0.5, 27.9415026443))
                Line((0.5, 27.9415026443), (0.5, 9.9415026443))
                Line((0.5, 9.9415026443), (17.5, 9.9415026443))
                Line((17.5, 9.9415026443), (17.5, 27.9415026443))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 22 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 14.7806318592, perimeter: 37.6422924288
            with BuildLine():
                Line((3.0838516801, 27.9415026443), (3.9049978945, 27.9415026443))
                Line((3.0838516801, 9.9415026443), (3.0838516801, 27.9415026443))
                Line((3.9049978945, 9.9415026443), (3.0838516801, 9.9415026443))
                Line((3.9049978945, 27.9415026443), (3.9049978945, 9.9415026443))
            make_face()
            # Profile area: 20.0889513019, perimeter: 38.1223883764
            with BuildLine():
                Line((7.6803084382, 27.9415026443), (8.8000001311, 27.9415026443))
                Line((7.6803084382, 10.000000149), (7.6803084382, 27.9415026443))
                Line((8.8000001311, 10.000000149), (7.6803084382, 10.000000149))
                Line((8.8000001311, 27.9415026443), (8.8000001311, 10.000000149))
            make_face()
            # Profile area: 17.4690590066, perimeter: 37.8303401161
            with BuildLine():
                Line((11.0000001639, 10.000000149), (11.9736677267, 10.000000149))
                Line((11.9736677267, 10.000000149), (11.9736677267, 27.9415026443))
                Line((11.9736677267, 27.9415026443), (11.0000001639, 27.9415026443))
                Line((11.0000001639, 27.9415026443), (11.0000001639, 10.000000149))
            make_face()
            # Profile area: 19.5315492425, perimeter: 38.1701721381
            with BuildLine():
                Line((13.9933656714, 9.9415026443), (15.0784517404, 9.9415026443))
                Line((15.0784517404, 9.9415026443), (15.0784517404, 27.9415026443))
                Line((15.0784517404, 27.9415026443), (13.9933656714, 27.9415026443))
                Line((13.9933656714, 27.9415026443), (13.9933656714, 9.9415026443))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 43), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 48.8246929799, perimeter: 27.94991228
            with BuildLine():
                Line((-5.5, -0.02504386), (-5.5, -7))
                Line((-12.5, -0.02504386), (-5.5, -0.02504386))
                Line((-12.5, -7), (-12.5, -0.02504386))
                Line((-12.5, -7), (-5.5, -7))
            make_face()
        # OneSide extrude, distance=13
        extrude(amount=13, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((8.3365808611, 9.837482921)):
                Circle(4)
        # OneSide extrude, distance=21.4
        extrude(amount=21.4)
    return part.part


def model_85195_c6ef0067_0000():
    """Model: cup v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.1925807224, perimeter: 45.2652972525
            with BuildLine():
                CenterArc((0, 0), 7, 64.1558991173, 51.6882017654)
                Line((-7.1999999979, 6.2998845345), (-3.0514676555, 6.2998845345))
                Line((-7.1999999979, 3.0998845345), (-7.1999999979, 6.2998845345))
                Line((-3.5999999979, 3.0998845345), (-7.1999999979, 3.0998845345))
                Line((-3.5999999979, -0.0001154655), (-3.5999999979, 3.0998845345))
                Line((-3.1999999979, -0.0001154655), (-3.5999999979, -0.0001154655))
                CenterArc((0, 0), 3.2, -0.0020674026, 180.0041348052)
                Line((3.6000000021, -0.0001154655), (3.1999999979, -0.0001154655))
                Line((3.6000000021, 3.0998845345), (3.6000000021, -0.0001154655))
                Line((7.2000000021, 3.0998845345), (3.6000000021, 3.0998845345))
                Line((7.2000000021, 6.2998845345), (7.2000000021, 3.0998845345))
                Line((3.0514676555, 6.2998845345), (7.2000000021, 6.2998845345))
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.2998845345, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((5.2500000021, 3.2)):
                Circle(1.75)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 3.8173929354, perimeter: 13.8936782338
            with BuildLine():
                CenterArc((0, 0), 3.2, -0.0020674026, 10.806885554)
                Line((-3.1432687676, 0.5998845345), (3.1432687676, 0.5998845345))
                CenterArc((0, 0), 3.2, 169.1951818486, 10.806885554)
                Line((3.1999999979, -0.0001154655), (-3.1999999979, -0.0001154655))
            make_face()
            # Profile area: 1.0078920265, perimeter: 4.5596400884
            with BuildLine():
                Line((3.6000000021, -0.0001154655), (3.6000000021, 0.5998845345))
                Line((5.2798200463, -0.0001154655), (3.6000000021, -0.0001154655))
                Line((5.2798200463, 0.5998845345), (5.2798200463, -0.0001154655))
                Line((3.6000000021, 0.5998845345), (5.2798200463, 0.5998845345))
            make_face()
            # Profile area: 0.251303531, perimeter: 2.0603015817
            with BuildLine():
                CenterArc((0, 0), 3.2, 169.1951818486, 10.806885554)
                Line((-3.5999999979, 0.5998845345), (-3.1432687676, 0.5998845345))
                Line((-3.5999999979, 0.5998845345), (-3.5999999979, -0.0001154655))
                Line((-3.1999999979, -0.0001154655), (-3.5999999979, -0.0001154655))
            make_face()
            # Profile area: 0.2513035335, perimeter: 2.06030159
            with BuildLine():
                Line((3.1432687676, 0.5998845345), (3.6000000021, 0.5998845345))
                CenterArc((0, 0), 3.2, -0.0020674026, 10.806885554)
                Line((3.6000000021, -0.0001154655), (3.1999999979, -0.0001154655))
                Line((3.6000000021, -0.0001154655), (3.6000000021, 0.5998845345))
            make_face()
            # Profile area: 0.9302258531, perimeter: 4.3007528438
            with BuildLine():
                Line((-3.5999999979, 0.5998845345), (-3.5999999979, -0.0001154655))
                Line((-5.1503764198, 0.5998845345), (-3.5999999979, 0.5998845345))
                Line((-5.1503764198, -0.0001154655), (-5.1503764198, 0.5998845345))
                Line((-3.5999999979, -0.0001154655), (-5.1503764198, -0.0001154655))
            make_face()
        # TwoSides extrude, along=7.3, against=-7.6
        extrude(amount=7.3, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-7.6, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.7901238625, perimeter: 19.7633255437
            with BuildLine():
                Line((3.1432687676, 0.5998845345), (3.5496673852, 0.5998845345))
                CenterArc((0, 0), 3.6, 9.592204473, 160.8155910541)
                Line((-3.5496673852, 0.5998845345), (-3.1432687676, 0.5998845345))
                CenterArc((0, 0), 3.2, 10.8048181514, 158.3903636972)
            make_face()
        # OneSide extrude, distance=0.11
        extrude(amount=0.11, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.7901238625, perimeter: 19.7633255437
            with BuildLine():
                Line((3.1432687676, 0.5998845345), (3.5496673852, 0.5998845345))
                CenterArc((0, 0), 3.6, 9.592204473, 160.8155910541)
                Line((-3.5496673852, 0.5998845345), (-3.1432687676, 0.5998845345))
                CenterArc((0, 0), 3.2, 10.8048181514, 158.3903636972)
            make_face()
        # OneSide extrude, distance=0.11
        extrude(amount=0.11, mode=Mode.ADD)

        # Sketch11 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.2998845345, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8603718124, perimeter: 9.3063666394
            with BuildLine():
                Line((-7.2000000021, 0), (-5.1257338288, 0))
                CenterArc((-3.694524103, 3.2), 3.5054758991, 180, 65.903274172)
                Line((-7.2000000021, 3.2), (-7.2000000021, 0))
            make_face()
            # Profile area: 1.8603718124, perimeter: 9.3063666394
            with BuildLine():
                CenterArc((-3.694524103, 3.2), 3.5054758991, 114.096725828, 65.903274172)
                Line((-5.1257338288, 6.4), (-7.2000000021, 6.4))
                Line((-7.2000000021, 6.4), (-7.2000000021, 3.2))
            make_face()
        # TwoSides extrude (symmetric), distance=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.2998845345, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8603718112, perimeter: 9.3063666358
            with BuildLine():
                CenterArc((3.6945240974, 3.2), 3.5054759006, -65.9032741195, 65.9032741195)
                Line((5.1257338267, 0), (7.1999999979, 0))
                Line((7.1999999979, 0), (7.1999999979, 3.2))
            make_face()
            # Profile area: 1.8603718112, perimeter: 9.3063666358
            with BuildLine():
                Line((7.1999999979, 6.4), (5.1257338267, 6.4))
                CenterArc((3.6945240974, 3.2), 3.5054759006, 0, 65.9032741195)
                Line((7.1999999979, 3.2), (7.1999999979, 6.4))
            make_face()
        # TwoSides extrude (symmetric), distance=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_87178_f19385af_0000():
    """Model: Platform v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6700, perimeter: 334
            with BuildLine():
                Line((33.5, -50), (33.5, 50))
                Line((33.5, 50), (-33.5, 50))
                Line((-33.5, 50), (-33.5, -50))
                Line((-33.5, -50), (33.5, -50))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-33.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 148.0475538004, perimeter: 58.5530934771
            with BuildLine():
                Line((-50, 15), (-50, 21))
                CenterArc((-50, 10.5), 10.5, 90, 180)
                Line((-50, 7), (-50, 0))
                CenterArc((-50, 11), 4, 90, 180)
            make_face()
        # OneSide extrude, distance=-67
        extrude(amount=-67, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-33.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 18.8495559215, perimeter: 18.2831853072
            with BuildLine():
                CenterArc((-50, 15), 6, 30, 60)
                Line((-50, 21), (-50, 15))
                Line((-44.8038475773, 18), (-50, 15))
            make_face()
        # OneSide extrude, distance=-67
        extrude(amount=-67, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 101.25, perimeter: 42
            with BuildLine():
                Line((-33.5, 42.5), (-33.5, 50))
                Line((-20, 42.5), (-33.5, 42.5))
                Line((-20, 50), (-20, 42.5))
                Line((-33.5, 50), (-20, 50))
            make_face()
            # Profile area: 101.25, perimeter: 42
            with BuildLine():
                Line((20, 50), (20, 42.5))
                Line((20, 42.5), (33.5, 42.5))
                Line((33.5, 42.5), (33.5, 50))
                Line((33.5, 50), (20, 50))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-33.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.3151467436, perimeter: 2.5112991663
            with BuildLine():
                Line((50, 7.2679491924), (50, 8))
                Line((50, 8), (49.2679491924, 8))
                CenterArc((51, 9), 2, -150, 30)
            make_face()
        # OneSide extrude, distance=-13.5
        extrude(amount=-13.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(33.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3151467436, perimeter: 2.5112991663
            with BuildLine():
                Line((-49.2679491924, 8), (-50, 8))
                Line((-50, 8), (-50, 7.2679491924))
                CenterArc((-51, 9), 2, -60, 30)
            make_face()
        # OneSide extrude, distance=-13.5
        extrude(amount=-13.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((23.5, -40)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-23.5, -40)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-23.5, 35)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((23.5, 34.2679491924)):
                Circle(1.5)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


def model_87278_bb9c8879_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4, perimeter: 15.8
            with BuildLine():
                Line((0, 1.9), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 1.9))
                Line((6, 1.9), (0, 1.9))
            make_face()
        # OneSide extrude, distance=0.625
        extrude(amount=0.625)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0766104592, perimeter: 1.494960031
            with BuildLine():
                Line((3.3510608922, 0.625), (2.6489391078, 0.625))
                CenterArc((3, 0.3125), 0.47, 41.6741644997, 96.6516710006)
            make_face()
            # Profile area: 0.5407568988, perimeter: 2.7716641697
            with BuildLine():
                CenterArc((3, 0.3125), 0.47, 138.3258355003, 83.3483289994)
                Line((2.6489391078, 0), (3.3510608922, 0))
                CenterArc((3, 0.3125), 0.47, -41.6741644997, 83.3483289994)
                Line((3.3510608922, 0.625), (2.6489391078, 0.625))
            make_face()
            # Profile area: 0.0766104592, perimeter: 1.494960031
            with BuildLine():
                CenterArc((3, 0.3125), 0.47, -138.3258355003, 96.6516710006)
                Line((2.6489391078, 0), (3.3510608922, 0))
            make_face()
        # OneSide extrude, distance=1.875
        extrude(amount=1.875, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.875), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9125221828, perimeter: 8.1130970944
            with BuildLine():
                Line((2.235, -0.2125), (2.235, 0.8375))
                Line((3.765, -0.2125), (2.235, -0.2125))
                Line((3.765, 0.8375), (3.765, -0.2125))
                Line((2.235, 0.8375), (3.765, 0.8375))
            make_face()
            with BuildLine():
                CenterArc((3, 0.3125), 0.47, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6939778172, perimeter: 2.9530970944
            with Locations((3, 0.3125)):
                Circle(0.47)
        # OneSide extrude, distance=0.95
        extrude(amount=0.95, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.825), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.24485, perimeter: 2.0366639389
            with BuildLine():
                Line((3, 0.6075), (2.585, 0.3125))
                Line((3, 0.0175), (2.585, 0.3125))
                Line((3.415, 0.3125), (3, 0.0175))
                Line((3, 0.6075), (3.415, 0.3125))
            make_face()
        # OneSide extrude, distance=-0.68
        extrude(amount=-0.68, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3117245311, perimeter: 1.9792033718
            with Locations((-0.83, -0.95)):
                Circle(0.315)
        # OneSide extrude, distance=0.67
        extrude(amount=0.67, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-5.46, -1.36)):
                Circle(0.125)
        # OneSide extrude, distance=-0.625
        extrude(amount=-0.625, mode=Mode.SUBTRACT)
    return part.part


def model_87394_c44702f0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.037167544, perimeter: 70.3716754404
            with BuildLine():
                CenterArc((0, 0), 5.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 91.8915851175, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 5.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-2, -3)):
                Circle(1)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2, -2)):
                Circle(0.25)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-1.5, 1.5)):
                Circle(0.2)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-3, 3)):
                Circle(0.3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.SUBTRACT)
    return part.part


def model_89822_0157c8d0_0000():
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
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50, perimeter: 30
            with BuildLine():
                Line((0, 10), (0, 0))
                Line((-5, 10), (0, 10))
                Line((-5, 0), (-5, 10))
                Line((0, 0), (-5, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1531997063, perimeter: 43.2773490872
            with BuildLine():
                Line((0.4383558051, 1.2107647007), (0.5271919543, 1.1648502271))
                _nurbs_edge([(0.5271919543, 1.1648502271), (0.7731108601, 1.6406585483), (1.0667931103, 1.9737082944), (1.3916035594, 2.1706590513), (1.651132753, 2.3280261287), (1.9331326223, 2.3991504621), (2.1908533182, 2.3843145546), (2.4103765678, 2.3716775151), (2.6048004831, 2.2966798597), (2.747051144, 2.1659546814), (2.8741255054, 2.0491761832), (2.961395571, 1.8845630832), (3.0214597843, 1.6790369941), (3.1011879782, 1.4062252317), (3.1330277967, 1.0655785213), (3.2349327999, 0.7488196544), (3.3048989548, 0.5313386745), (3.4125639384, 0.3255505283), (3.5730171478, 0.1655536704), (3.7698870504, -0.0307563066), (4.0427677126, -0.1546157399), (4.3403431569, -0.1841923521), (4.649184934, -0.2148887474), (4.9807112179, -0.1452260152), (5.2775523277, 0.0149380159), (5.5815122254, 0.1789430709), (5.8478002497, 0.4364798297), (6.067207797, 0.7476407797), (6.3909913991, 1.2068265029), (6.6152660821, 1.7798164903), (6.8274786652, 2.3228386699), (7.0087370256, 2.7866533433), (7.1851093465, 3.2268056429), (7.4098836019, 3.5826069972), (7.6402390144, 3.947242919), (7.9202276301, 4.2222902874), (8.2899155039, 4.4050873555), (8.6308636705, 4.5736736946), (9.0518838626, 4.6652891533), (9.5419060126, 4.7012312378), (10.026894503, 4.736804114), (10.5785277794, 4.7201406426), (11.137830755, 4.6786630935), (11.7474163267, 4.6334566194), (12.3656376353, 4.5612520882), (12.8580234024, 4.4591914457), (13.1702767454, 4.3944682572), (13.4297873613, 4.3156331854), (13.6098147126, 4.2225294349), (13.7597890234, 4.1449680493), (13.8522430296, 4.0602155946), (13.903771842, 3.9679049155), (13.9588172343, 3.8692945011), (13.9721689792, 3.7535582159), (13.9629398942, 3.6093881362), (13.9492905439, 3.3961678741), (13.8869873546, 3.1315099255), (13.9007919523, 2.8467818628), (13.9125479486, 2.6043074264), (13.9824456684, 2.3482220555), (14.1401461247, 2.0958835608), (14.3441424929, 1.7694663917), (14.6898305329, 1.4480123394), (15.1827456553, 1.1269706229)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0625, 0.0625, 0.0625, 0.1124385862, 0.1124385862, 0.1124385862, 0.1549756462, 0.1549756462, 0.1549756462, 0.1929745539, 0.1929745539, 0.1929745539, 0.2434136443, 0.2434136443, 0.2434136443, 0.2780442228, 0.2780442228, 0.2780442228, 0.3205346077, 0.3205346077, 0.3205346077, 0.3646336965, 0.3646336965, 0.3646336965, 0.4097903615, 0.4097903615, 0.4097903615, 0.4764288515, 0.4764288515, 0.4764288515, 0.5333471702, 0.5333471702, 0.5333471702, 0.5916787739, 0.5916787739, 0.5916787739, 0.6454756517, 0.6454756517, 0.6454756517, 0.6987199112, 0.6987199112, 0.6987199112, 0.7567509495, 0.7567509495, 0.7567509495, 0.7935521467, 0.7935521467, 0.7935521467, 0.8242099003, 0.8242099003, 0.8242099003, 0.85695989, 0.85695989, 0.85695989, 0.9053954697, 0.9053954697, 0.9053954697, 0.9466432125, 0.9466432125, 0.9466432125, 1, 1, 1, 1], 3)
                Line((15.1827456553, 1.1269706229), (15.2373217748, 1.2107647007))
                _nurbs_edge([(0.4383558051, 1.2107647007), (0.4867303412, 1.3043606232), (0.5865527544, 1.483029227), (0.7455065103, 1.7254624368), (0.9758961607, 1.9975337767), (1.2928143113, 2.2520059712), (1.6330574698, 2.4202050546), (1.9853436531, 2.5010784921), (2.3306907479, 2.4930808396), (2.6407437995, 2.3941668947), (2.8887383185, 2.2052386366), (3.0588896095, 1.9331154626), (3.1585705206, 1.5944033583), (3.2225864035, 1.2168106398), (3.2973193472, 0.8338708038), (3.4281305734, 0.4808068364), (3.6466224126, 0.1901807202), (3.9550161581, -0.0129523884), (4.3313509754, -0.111832553), (4.7415387554, -0.0975378626), (5.1484758849, 0.0311073178), (5.5237657636, 0.2675714826), (5.8536073512, 0.5982670335), (6.1347594903, 1.0045453428), (6.3726977102, 1.4643586527), (6.5788798362, 1.9540756661), (6.768506786, 2.4501487749), (6.9578496292, 2.9310292511), (7.1627550473, 3.3781957514), (7.3980275989, 3.7764796397), (7.6765684842, 4.1145842022), (8.0085988223, 4.3855680098), (8.4008620607, 4.587281706), (8.8557636152, 4.7230386317), (9.3711145548, 4.8002444512), (9.9399637197, 4.8286779025), (10.5504032484, 4.8189144022), (11.1853283458, 4.7806685154), (11.8222980438, 4.7212317171), (12.433105424, 4.6437208118), (12.9841451209, 4.5458224506), (13.4428933496, 4.4221559561), (13.7835500474, 4.2662081568), (13.9934554166, 4.0725342504), (14.0782097894, 3.8386053892), (14.0699559776, 3.5674337243), (14.0195554859, 3.2662801545), (13.9831712816, 2.9439777191), (14.009779057, 2.6085414344), (14.1309155982, 2.2651494303), (14.365572431, 1.9169651524), (14.6514627349, 1.6358338319), (14.9224206832, 1.4237714172), (15.1281696061, 1.2818568584), (15.2373217748, 1.2107647007)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.684891814, 0.5711145484)):
                Circle(0.25)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.087975745, perimeter: 1.0514446333
            with Locations((-0.684891814, 0.5711145484)):
                Circle(0.1673426108)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.684891814, 0.5711145484)):
                Circle(0.1)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_91441_71022c53_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7, perimeter: 11
            with BuildLine():
                Line((2.5, -5), (0.5, -5))
                Line((2.5, -1.5), (2.5, -5))
                Line((0.5, -1.5), (2.5, -1.5))
                Line((0.5, -5), (0.5, -1.5))
            make_face()
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7, perimeter: 11
            with BuildLine():
                Line((7.5, -5), (5.5, -5))
                Line((7.5, -1.5), (7.5, -5))
                Line((5.5, -1.5), (7.5, -1.5))
                Line((5.5, -5), (5.5, -1.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((5.5, -4), (2.5, -4))
                Line((5.5, -2.5), (5.5, -4))
                Line((2.5, -2.5), (5.5, -2.5))
                Line((2.5, -4), (2.5, -2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.8221237934, perimeter: 4.7851314395
            with Locations((1.4000000209, 1.5000000224)):
                Circle(0.7615773219)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.8221237934, perimeter: 4.7851314395
            with Locations((6.5000000969, 1.5000000224)):
                Circle(0.7615773219)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0681415341, perimeter: 3.6636951818
            with Locations((-3.9000000581, 3.2000000477)):
                Circle(0.5830951982)
            # Profile area: 0.2831570545, perimeter: 1.8863341405
            with Locations((-2.8337722981, 3.25)):
                Circle(0.3002194028)
            # Profile area: 0.305048703, perimeter: 1.9578955687
            with Locations((-4.9139893455, 3.25)):
                Circle(0.3116087578)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1570796374, perimeter: 1.4049629671
            with Locations((1.4000000209, 0.400000006)):
                Circle(0.2236068011)
            # Profile area: 0.1570796374, perimeter: 1.4049629671
            with Locations((6.5000000969, 0.400000006)):
                Circle(0.2236068011)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_91537_04ffbad0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.2522547518, perimeter: 10.7827298135
            Circle(1.7161247498)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.3561944902, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_91570_7989dd01_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 237.0856209268, perimeter: 94.2397908686
            with BuildLine():
                CenterArc((-7.5, 7.5), 5, 90, 180)
                Line((12.5, 2.5), (-7.5, 2.5))
                CenterArc((12.5, 7.5), 5, -90, 180)
                Line((-7.5, 12.5), (12.5, 12.5))
            make_face()
            with BuildLine():
                CenterArc((3.0277447744, 7.5), 3.632530829, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 10.626534003, perimeter: 42.5061360119
            with BuildLine():
                CenterArc((3.0277447744, 7.5), 3.632530829, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.0277447744, 7.5), 3.132530829, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.6219381649, perimeter: 37.4795877661
            with BuildLine():
                CenterArc((3.0277447744, 7.5), 3.132530829, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.0277447744, 7.5), 2.832530829, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 25.2057232451, perimeter: 17.797316087
            with Locations((3.0277447744, 7.5)):
                Circle(2.832530829)
        # OneSide extrude, distance=-8
        extrude(amount=-8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.780972451, perimeter: 47.1238898038
            with BuildLine():
                CenterArc((-7.5, 7.5), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.5, 7.5), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.4027629051, perimeter: 24.8185819634
            with BuildLine():
                CenterArc((-7.5, 7.5), 3.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.5, 7.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.780972451, perimeter: 47.1238898038
            with BuildLine():
                CenterArc((12.5, 7.5), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12.5, 7.5), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.4027629051, perimeter: 24.8185819634
            with BuildLine():
                CenterArc((12.5, 7.5), 3.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12.5, 7.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.626534003, perimeter: 42.5061360119
            with BuildLine():
                CenterArc((3.0277447744, 7.5), 3.632530829, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.0277447744, 7.5), 3.132530829, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.2057232451, perimeter: 17.797316087
            with Locations((3.0277447744, 7.5)):
                Circle(2.832530829)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((3.0277447744, 7.5)):
                Circle(0.75)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_91682_69b6d4ec_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6051985542, perimeter: 9.1106186954
            Circle(1.45)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            Circle(1.15)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.65, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5277008297, perimeter: 9.1620317825
            with BuildLine():
                Line((-0.8248130576, 0.0175618901), (-1.0040529407, 0.0433326947))
                CenterArc((0, 0), 0.825, 178.7802446135, 18.8031471366)
                Line((-0.9511735108, -0.3244518183), (-0.7864545771, -0.2492272018))
                Line((-0.868090507, -0.5063782201), (-0.9511735108, -0.3244518183))
                Line((-0.7033715733, -0.4311536036), (-0.868090507, -0.5063782201))
                CenterArc((0, 0), 0.825, -148.4924826592, 18.8031471366)
                Line((-0.62476618, -0.7871894628), (-0.5268652933, -0.6348527095))
                Line((-0.456515471, -0.8953176279), (-0.62476618, -0.7871894628))
                Line((-0.3586145842, -0.7429808746), (-0.456515471, -0.8953176279))
                CenterArc((0, 0), 0.825, -115.7652099319, 18.8031471366)
                Line((-0.1000000015, -1.0000000149), (-0.1000000015, -0.8189169675))
                Line((0.1000000015, -1.0000000149), (-0.1000000015, -1.0000000149))
                Line((0.1000000015, -0.8189169675), (0.1000000015, -1.0000000149))
                CenterArc((0, 0), 0.825, -83.0379372047, 18.8031471366)
                Line((0.456515471, -0.8953176279), (0.3586145842, -0.7429808746))
                Line((0.62476618, -0.7871894628), (0.456515471, -0.8953176279))
                Line((0.5268652933, -0.6348527095), (0.62476618, -0.7871894628))
                CenterArc((0, 0), 0.825, -50.3106644774, 18.8031471366)
                Line((0.868090507, -0.5063782201), (0.7033715733, -0.4311536036))
                Line((0.9511735108, -0.3244518183), (0.868090507, -0.5063782201))
                Line((0.7864545771, -0.2492272018), (0.9511735108, -0.3244518183))
                CenterArc((0, 0), 0.825, -17.5833917501, 18.8031471366)
                Line((1.0040529407, 0.0433326947), (0.8248130576, 0.0175618901))
                Line((0.9755899726, 0.2412969861), (1.0040529407, 0.0433326947))
                Line((0.7963500895, 0.2155261815), (0.9755899726, 0.2412969861))
                CenterArc((0, 0), 0.825, 15.1438809772, 18.8031471366)
                Line((0.82123566, 0.5792857851), (0.684382224, 0.4607016078))
                Line((0.6902635112, 0.7304357023), (0.82123566, 0.5792857851))
                Line((0.5534100753, 0.611851525), (0.6902635112, 0.7304357023))
                CenterArc((0, 0), 0.825, 47.8711537044, 18.8031471366)
                Line((0.3776818598, 0.9313197318), (0.3266648699, 0.7575718202))
                Line((0.1857832622, 0.987666244), (0.3776818598, 0.9313197318))
                Line((0.1347662723, 0.8139183324), (0.1857832622, 0.987666244))
                CenterArc((0, 0), 0.825, 80.5984264317, 18.8031471366)
                Line((-0.1857832622, 0.987666244), (-0.1347662723, 0.8139183324))
                Line((-0.3776818598, 0.9313197318), (-0.1857832622, 0.987666244))
                Line((-0.3266648699, 0.7575718202), (-0.3776818598, 0.9313197318))
                CenterArc((0, 0), 0.825, 113.325699159, 18.8031471366)
                Line((-0.6902635112, 0.7304357023), (-0.5534100753, 0.611851525))
                Line((-0.82123566, 0.5792857851), (-0.6902635112, 0.7304357023))
                Line((-0.684382224, 0.4607016078), (-0.82123566, 0.5792857851))
                CenterArc((0, 0), 0.825, 146.0529718862, 18.8031471366)
                Line((-0.9755899726, 0.2412969861), (-0.7963500895, 0.2155261815))
                Line((-1.0040529407, 0.0433326947), (-0.9755899726, 0.2412969861))
            make_face()
        # OneSide extrude, distance=2.25
        extrude(amount=2.25, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.7225, perimeter: 6.6
            with BuildLine():
                Line((-0.825, 0.825), (0.825, 0.825))
                Line((-0.825, -0.825), (-0.825, 0.825))
                Line((0.825, -0.825), (-0.825, -0.825))
                Line((0.825, 0.825), (0.825, -0.825))
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=-3.38
        extrude(amount=-3.38, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.95, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)
    return part.part


def model_93385_c56fafc6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 96.774, perimeter: 40.64
            with BuildLine():
                Line((12.7, -7.62), (0, -7.62))
                Line((12.7, 0), (12.7, -7.62))
                Line((0, 0), (12.7, 0))
                Line((0, -7.62), (0, 0))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.62), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11.741912, perimeter: 19.3548
            with BuildLine():
                Line((10.4902, 0), (10.4902, 1.4224))
                Line((10.4902, 1.4224), (2.2352, 1.4224))
                Line((2.2352, 1.4224), (2.2352, 0))
                Line((2.2352, 0), (10.4902, 0))
            make_face()
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.62), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 49.8156752213, perimeter: 41.363738686
            with BuildLine():
                Line((7.9502, 3.81), (4.7752, 3.81))
                Line((7.9502, 3.81), (7.9502, 7.7935128953))
                Line((13.1560742426, 4.7879), (7.9502, 7.7935128953))
                Line((14.4260742426, 6.9876045256), (13.1560742426, 4.7879))
                Line((2.7456432116, 13.7313045256), (14.4260742426, 6.9876045256))
                Line((2.7456432116, 13.7313045256), (1.4756432116, 11.5316))
                Line((4.7752, 9.6266), (1.4756432116, 11.5316))
                Line((4.7752, 3.81), (4.7752, 9.6266))
            make_face()
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.632240076, 11.4873767797, 0), x_dir=(0, 0, -1), z_dir=(0.5, 0.8660254038, 0))):
            # Profile area: 3.1151817203, perimeter: 13.6047338888
            with BuildLine():
                CenterArc((-3.81, 0.6778554918), 3.81, 90.0000008748, 89.9999991252)
                Line((-3.8100000582, 4.4878554918), (-7.62, 4.4878554918))
                Line((-7.62, 0.6778554918), (-7.62, 4.4878554918))
            make_face()
            # Profile area: 3.1151817203, perimeter: 13.6047341214
            with BuildLine():
                CenterArc((-3.81, 0.6778554918), 3.81, 0, 90.0000008748)
                Line((0, 4.4878554918), (0, 0.6778554918))
                Line((0, 4.4878554918), (-3.8100000582, 4.4878554918))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.632240076, 11.4873767797, 0), x_dir=(0, 0, -1), z_dir=(0.5, 0.8660254038, 0))):
            # Profile area: 8.23804804, perimeter: 11.4808
            with BuildLine():
                Line((-3.81, 2.7073933752), (-1.7804621166, 0.6778554918))
                Line((-5.8395378834, 0.6778554918), (-3.81, 2.7073933752))
                Line((-3.81, -1.3516823915), (-5.8395378834, 0.6778554918))
                Line((-1.7804621166, 0.6778554918), (-3.81, -1.3516823915))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.632240076, 11.4873767797, 0), x_dir=(0, 0, -1), z_dir=(0.5, 0.8660254038, 0))):
            # Profile area: 10.6206205007, perimeter: 12.5087127255
            with BuildLine():
                Line((0, -8.9995445082), (0.9652, -8.9995445082))
                CenterArc((0.9652, -6.9421445082), 2.0574, -90, 180)
                Line((0, -4.8847445082), (0.9652, -4.8847445082))
                Line((0, -8.9995445082), (0, -4.8847445082))
            make_face()
            # Profile area: 10.6206205007, perimeter: 12.5087127255
            with BuildLine():
                Line((-7.62, -4.8847445082), (-7.62, -8.9995445082))
                Line((-8.5852, -4.8847445082), (-7.62, -4.8847445082))
                CenterArc((-8.5852, -6.9421445082), 2.0574, 90, 180)
                Line((-8.5852, -8.9995445082), (-7.62, -8.9995445082))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.632240076, 11.4873767797, 0), x_dir=(0, 0, -1), z_dir=(0.5, 0.8660254038, 0))):
            # Profile area: 3.9239427181, perimeter: 7.0220878993
            with Locations((-8.5852, -6.9421445082)):
                Circle(1.1176)
            # Profile area: 7.27998544, perimeter: 13.6652
            with BuildLine():
                Line((-2.2098, -8.9995445082), (-2.2098, -8.1359445082))
                Line((-1.27, -8.1359445082), (-2.2098, -8.1359445082))
                Line((-1.27, -7.2469445082), (-1.27, -8.1359445082))
                Line((-6.35, -7.2469445082), (-1.27, -7.2469445082))
                Line((-6.35, -8.1359445082), (-6.35, -7.2469445082))
                Line((-5.4102, -8.1359445082), (-6.35, -8.1359445082))
                Line((-5.4102, -8.1359445082), (-5.4102, -8.9995445082))
                Line((-5.4102, -8.9995445082), (-2.2098, -8.9995445082))
            make_face()
            # Profile area: 3.9239427181, perimeter: 7.0220878993
            with Locations((0.9652, -6.9421445082)):
                Circle(1.1176)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


def model_93389_b1801754_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.17, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.182605073, perimeter: 2.9216811678
            with BuildLine():
                CenterArc((0, 0), 0.295, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.06
        extrude(amount=0.06, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.048301987, perimeter: 3.8641589639
            with BuildLine():
                CenterArc((0, 0), 0.32, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.295, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.28
        extrude(amount=0.28, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.28, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.23090706, perimeter: 3.0787608005
            with BuildLine():
                CenterArc((0, 0), 0.32, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.38, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0574911456, perimeter: 3.8327430374
            with BuildLine():
                CenterArc((0, 0), 0.32, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.29, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1353322101, perimeter: 2.0492984311
            with BuildLine():
                Line((-0.57, 0.2), (-0.2497999199, 0.2))
                CenterArc((-0.57, 0.08), 0.12, 90, 90)
                Line((-0.69, -0.08), (-0.69, 0.08))
                CenterArc((-0.57, -0.08), 0.12, -180, 90)
                Line((-0.2497999199, -0.2), (-0.57, -0.2))
                CenterArc((0, 0), 0.32, 141.3178125465, 77.364374907)
            make_face()
            with BuildLine():
                CenterArc((-0.505, 0), 0.07, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1353322101, perimeter: 2.0492984311
            with BuildLine():
                Line((0.57, -0.2), (0.2497999199, -0.2))
                CenterArc((0.57, -0.08), 0.12, -90, 90)
                Line((0.69, 0.08), (0.69, -0.08))
                CenterArc((0.57, 0.08), 0.12, 0, 90)
                Line((0.2497999199, 0.2), (0.57, 0.2))
                CenterArc((0, 0), 0.32, -38.6821874535, 77.364374907)
            make_face()
            with BuildLine():
                CenterArc((0.505, 0), 0.07, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.06
        extrude(amount=0.06, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0375357589, perimeter: 0.9662021013
            with BuildLine():
                Line((0.295, 0.06), (0.2497999199, 0.06))
                Line((0.47, 0.06), (0.295, 0.06))
                Line((0.47, 0.06), (0.2492014183, 0.4))
                Line((0.2492014183, 0.4), (0.2492014183, 0.06))
                Line((0.2497999199, 0.06), (0.2492014183, 0.06))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.ADD)
    return part.part


def model_94399_be0c8a51_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0670751144, perimeter: 7.9796455948
            Circle(1.2700000405)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=-0.96012
        extrude(amount=-0.96012, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.96012, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=-5.588
        extrude(amount=-5.588, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5067075114, perimeter: 2.5233855
            Circle(0.4016092757)
        # OneSide extrude, distance=-1.397
        extrude(amount=-1.397)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.397, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.5603672795, perimeter: 10.5030308402
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4016092757, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.ADD)
    return part.part


def model_95913_7c66e78a_0000():
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
        # headphone -> Extrude6 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.2410787381, perimeter: 11.7488692984
            with BuildLine():
                Line((0.2449984367, 0.4736203813), (-1.1787479129, 0.2675766118))
                Line((-1.5005391267, -1.0486958884), (-1.1787479129, 0.2675766118))
                Line((-1.5005391267, -1.0486958884), (0.2461063356, -1.049307982))
                Line((0.2461063356, -1.049307982), (0.2615541417, -1.0493133955))
                CenterArc((0.2540970889, -0.2878375842), 0.7615123235, -89.4389263721, 180.1235203802)
            make_face()
            with BuildLine():
                CenterArc((0.1920186484, -0.2939641211), 0.4909215208, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.0304164463, -0.0601036732), (-1.0685036321, -0.3207628513))
                Line((-0.6643784447, -0.0038889266), (-1.0304164463, -0.0601036732))
                Line((-0.7566211857, -0.6351751852), (-0.6643784447, -0.0038889266))
                Line((-1.0685036321, -0.3207628513), (-0.7566211857, -0.6351751852))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7571362061, perimeter: 3.0845508865
            with Locations((0.1920186484, -0.2939641211)):
                Circle(0.4909215208)
            # Profile area: 0.1595797307, perimeter: 1.7146073382
            with BuildLine():
                Line((-1.0685036321, -0.3207628513), (-0.7566211857, -0.6351751852))
                Line((-0.7566211857, -0.6351751852), (-0.6643784447, -0.0038889266))
                Line((-0.6643784447, -0.0038889266), (-1.0304164463, -0.0601036732))
                Line((-1.0304164463, -0.0601036732), (-1.0685036321, -0.3207628513))
            make_face()
        # OneSide extrude, distance=9.271
        extrude(amount=9.271)
    return part.part


def model_96186_05427635_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.8709021619, perimeter: 25.4000008106
            with BuildLine():
                Line((0, 3.8100001216), (0, 0))
                Line((0, 0), (8.8900002837, 0))
                Line((8.8900002837, 0), (8.8900002837, 3.8100001216))
                Line((8.8900002837, 3.8100001216), (0, 3.8100001216))
            make_face()
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 26.123094079, perimeter: 22.3149121457
            with BuildLine():
                CenterArc((-0.635, -0.635), 0.3175, 0, 90)
                Line((-0.635, -0.3175), (-8.2550002837, -0.3175))
                CenterArc((-8.2550002837, -0.635), 0.3175, 90, 90)
                Line((-8.5725002837, -0.635), (-8.5725002837, -3.1750001216))
                CenterArc((-8.2550002837, -3.1750001216), 0.3175, 180, 90)
                Line((-8.2550002837, -3.4925001216), (-0.635, -3.4925001216))
                CenterArc((-0.635, -3.1750001216), 0.3175, -90, 90)
                Line((-0.3175, -3.1750001216), (-0.3175, -0.635))
            make_face()
        # OneSide extrude, distance=-0.381
        extrude(amount=-0.381, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 50 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.381), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5042878286, perimeter: 9.9745566751
            with BuildLine():
                CenterArc((-0.9525, -1.4287501216), 0.15875, -180, 180)
                CenterArc((-1.42875, -1.4287501216), 0.635, 0, 270)
                CenterArc((-1.42875, -2.3812501216), 0.3175, 180, 270)
                CenterArc((-1.905, -2.3812501216), 0.15875, 0, 180)
                CenterArc((-1.42875, -2.3812501216), 0.635, 180, 270)
                CenterArc((-1.42875, -1.4287501216), 0.3175, 0, 270)
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on Profile plane
        # Sketch has 107 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.381), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9538494931, perimeter: 11.8843555934
            with BuildLine():
                CenterArc((2.9529367436, 2.8575001216), 0.15875, 28.1715040787, 61.8284959213)
                Line((2.9529367436, 3.0162501216), (2.8892502837, 3.0162501216))
                CenterArc((2.8892502837, 2.8575001216), 0.15875, 90, 90)
                Line((2.7305002837, 2.8575001216), (2.7305002837, 0.9525001216))
                CenterArc((2.8892502837, 0.9525001216), 0.15875, 180, 90)
                CenterArc((2.8892502837, 0.9525001216), 0.15875, -90, 90)
                Line((3.0480002837, 0.9525001216), (3.0480002837, 2.3437407674))
                Line((3.0480002837, 2.3437407674), (3.2126118528, 2.0363745219))
                Line((3.2126118528, 2.0363745219), (3.3525560683, 1.7750676871))
                CenterArc((3.4925002837, 1.8500155293), 0.15875, -151.8284959213, 123.6569918426)
                Line((3.7723887146, 2.0363745219), (3.6324444992, 1.7750676871))
                Line((3.9370002837, 2.3437407674), (3.7723887146, 2.0363745219))
                Line((3.9370002837, 0.9525001216), (3.9370002837, 2.3437407674))
                CenterArc((4.0957502837, 0.9525001216), 0.15875, 180, 90)
                CenterArc((4.0957502837, 0.9525001216), 0.15875, -90, 90)
                Line((4.2545002837, 2.8575001216), (4.2545002837, 0.9525001216))
                CenterArc((4.0957502837, 2.8575001216), 0.15875, 0, 90)
                Line((4.0320638238, 3.0162501216), (4.0957502837, 3.0162501216))
                CenterArc((4.0320638238, 2.8575001216), 0.15875, 90, 61.8284959213)
                Line((3.8921196084, 2.9324479639), (3.4925002837, 2.1862702064))
                Line((3.0928809591, 2.9324479639), (3.4925002837, 2.1862702064))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 50 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.381), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6840105436, perimeter: 4.8074556675
            with BuildLine():
                CenterArc((-2.3622, -2.8575001216), 0.15875, 180, 90)
                CenterArc((-2.3622, -2.8575001216), 0.15875, -90, 90)
                Line((-2.20345, -0.9525001216), (-2.20345, -2.8575001216))
                CenterArc((-2.3622, -0.9525001216), 0.15875, 0, 90)
                CenterArc((-2.3622, -0.9525001216), 0.15875, 90, 90)
                Line((-2.52095, -2.8575001216), (-2.52095, -0.9525001216))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 50 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.381), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.425114785, perimeter: 9.2418336104
            with BuildLine():
                EllipticalCenterArc((-5.0800002837, -1.9050001216), 1.11125, 0.635, 0, 360, -90)
            make_face()
            with BuildLine():
                EllipticalCenterArc((-5.0800002837, -1.9050001216), 0.79375, 0.3175, 0, 360, -90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on Profile plane
        # Sketch has 107 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.381), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9558328866, perimeter: 6.3165223197
            with BuildLine():
                Line((6.3753175351, 1.9050001216), (6.9367943371, 1.9050001216))
                Line((6.9367943371, 1.9050001216), (6.9390650102, 2.8544628813))
                CenterArc((6.7803154642, 2.8548425363), 0.15875, -0.1370245814, 90.1370245814)
                Line((6.7803154642, 3.0135925363), (6.7797135016, 3.0135925363))
                CenterArc((6.7797135016, 2.8548425363), 0.15875, 90, 89.6444533714)
                Line((6.6209665581, 2.8558276466), (6.6166423675, 2.1590000689))
                Line((6.6166423675, 2.1379439908), (6.6166423675, 2.1590000689))
                Line((6.1905957602, 2.9325175555), (6.6166423675, 2.1379439908))
                CenterArc((6.0506888372, 2.8575001216), 0.15875, 28.2, 61.8)
                Line((5.98656955, 3.0162501216), (6.0506888372, 3.0162501216))
                CenterArc((5.98656955, 2.8575001216), 0.15875, 90, 89.8629754186)
                Line((5.8255411593, 1.9050001216), (5.827820004, 2.8578797766))
                Line((5.8255411593, 1.9050001216), (6.1403835664, 1.9050001216))
                Line((6.1403835664, 1.9050001216), (6.1403835664, 2.3431501216))
                Line((6.1403835664, 2.3431501216), (6.3753175351, 1.9050001216))
            make_face()
            # Profile area: 0.3403435437, perimeter: 2.7172158649
            with BuildLine():
                Line((5.8255411593, 1.9050001216), (6.1403835664, 1.9050001216))
                Line((5.8232641305, 0.9528797766), (5.8255411593, 1.9050001216))
                CenterArc((5.9818238484, 0.9528797766), 0.158559718, 180, 180)
                Line((6.1403835664, 0.9528797766), (6.1403835664, 1.9050001216))
            make_face()
            # Profile area: 0.3982166851, perimeter: 3.0287430441
            with BuildLine():
                CenterArc((6.7753923675, 0.9512274658), 0.15875, -180, 89.502290352)
                Line((6.7743839032, 0.7924802365), (6.7740133756, 0.7924834553))
                CenterArc((6.7757628951, 0.9512242471), 0.15875, -90.497709648, 90.3606850666)
                Line((6.9345124411, 0.950844592), (6.9367943371, 1.9050001216))
                Line((6.3753175351, 1.9050001216), (6.9367943371, 1.9050001216))
                Line((6.3753175351, 1.9050001216), (6.6166423675, 1.4549312112))
                Line((6.6166423675, 0.9512274658), (6.6166423675, 1.4549312112))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude8 (Cut)
        # Sketch on Profile plane
        # Sketch has 107 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.381), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.3115689819, perimeter: 8.9291120977
            with BuildLine():
                Line((7.0612002837, 1.9050001216), (7.0612002837, 0.9525001216))
                CenterArc((7.2199502837, 0.9525001216), 0.15875, 180, 90)
                Line((7.2199502837, 0.7937501216), (7.9438502837, 0.7937501216))
                CenterArc((7.9438502837, 0.9525001216), 0.15875, -90, 90)
                CenterArc((7.9438502837, 0.9525001216), 0.15875, 0, 90)
                Line((7.9438502837, 1.1112501216), (7.3532999024, 1.1112501216))
                Line((7.3532999024, 1.1112501216), (7.3532999024, 1.7462501216))
                Line((7.3532999024, 1.7462501216), (7.9184499024, 1.7462501216))
                CenterArc((7.9184499024, 1.9050001216), 0.15875, -90, 90)
                CenterArc((7.9184499024, 1.9050001216), 0.15875, 0, 90)
                Line((7.3532999024, 2.0637501216), (7.9184499024, 2.0637501216))
                Line((7.3532999024, 2.6987501216), (7.3532999024, 2.0637501216))
                Line((7.9438502837, 2.6987501216), (7.3532999024, 2.6987501216))
                CenterArc((7.9438502837, 2.8575001216), 0.15875, -90, 90)
                CenterArc((7.9438502837, 2.8575001216), 0.15875, 0, 90)
                Line((7.2199502837, 3.0162501216), (7.9438502837, 3.0162501216))
                CenterArc((7.2199502837, 2.8575001216), 0.15875, 90, 90)
                Line((7.0612002837, 1.9050001216), (7.0612002837, 2.8575001216))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


def model_97828_a0e0ba49_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.4, perimeter: 20.6
            with BuildLine():
                Line((0, 4.8), (0, 0))
                Line((0, 0), (5.5, 0))
                Line((5.5, 0), (5.5, 4.8))
                Line((5.5, 4.8), (0, 4.8))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.32, perimeter: 11.6
            with BuildLine():
                Line((1.1, 5.5), (1.1, 2.3))
                Line((1.1, 2.3), (3.7, 2.3))
                Line((3.7, 2.3), (3.7, 5.5))
                Line((3.7, 5.5), (1.1, 5.5))
            make_face()
        # OneSide extrude, distance=-8.5
        extrude(amount=-8.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.52, perimeter: 8.6
            with BuildLine():
                Line((4.4, 2.3), (4.4, 5.5))
                Line((5.5, 2.3), (4.4, 2.3))
                Line((5.5, 2.3), (5.5, 5.5))
                Line((5.5, 5.5), (4.4, 5.5))
            make_face()
            # Profile area: 3.52, perimeter: 8.6
            with BuildLine():
                Line((1.1, 2.3), (0, 2.3))
                Line((1.1, 2.3), (1.1, 5.5))
                Line((1.1, 5.5), (0, 5.5))
                Line((0, 5.5), (0, 2.3))
            make_face()
            # Profile area: 2.6880252142, perimeter: 5.8119464091
            with Locations((2.75, 4.1)):
                Circle(0.925)
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1827310943, perimeter: 12.7862821001
            with BuildLine():
                CenterArc((2.75, 4.1), 1.11, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.75, 4.1), 0.925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.75
        extrude(amount=-0.75, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.1827310943, perimeter: 12.7862821001
            with BuildLine():
                CenterArc((-2.75, 4.1), 1.11, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.75, 4.1), 0.925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 23 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 5.2340024173, perimeter: 9.3561579112
            with BuildLine():
                CenterArc((0.7, -0.85), 0.5408326831, -123.6900673508, 96.1576629117)
                Line((0.400000006, -1.299999994), (0.400000006, -3.500000006))
                CenterArc((0.7, -3.95), 0.5408326831, 27.5324024809, 96.1576648699)
                Line((1.179583143, -3.7), (2.55, -3.7))
                Line((2.55, -1.1000000164), (2.55, -3.7))
                Line((1.1795831345, -1.1000000164), (2.55, -1.1000000164))
            make_face()
            # Profile area: 5.2340024173, perimeter: 9.3561579112
            with BuildLine():
                Line((2.95, -3.7), (2.95, -1.1000000164))
                Line((2.95, -3.7), (4.320416857, -3.7))
                CenterArc((4.8, -3.95), 0.5408326831, 56.3099326492, 96.1576648699)
                Line((5.099999994, -3.500000006), (5.099999994, -1.299999994))
                CenterArc((4.8, -0.85), 0.5408326831, -152.4675955608, 96.1576629117)
                Line((2.95, -1.1000000164), (4.3204168655, -1.1000000164))
            make_face()
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((0.7, -0.85)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((0.7, -3.95)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((4.8, -3.95)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((4.8, -0.85)):
                Circle(0.225)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-0.7, -3.95), 0.375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.7, -3.95), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-0.7, -0.85), 0.375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.7, -0.85), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-4.8, -3.95), 0.375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.8, -3.95), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-4.8, -0.85), 0.375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.8, -0.85), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_99094_559fbfc2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8610854828, perimeter: 26.3927517197
            with BuildLine():
                Line((1.7, 3), (0, 0))
                Line((0, 0), (0.075, 0))
                Line((0.075, 0), (3.3, 0))
                Line((3.3, 0), (5, 3))
                Line((1.7, 3), (5, 3))
            make_face()
            with BuildLine():
                Line((1.1619759429, 0.0652516639), (2.2119759429, 0.0652516639))
                Line((0.1119759429, 0.0652516639), (1.1619759429, 0.0652516639))
                Line((0.1119759429, 0.0652516639), (1.7380240571, 2.9347483361))
                Line((1.7380240571, 2.9347483361), (2.7880240571, 2.9347483361))
                Line((2.7880240571, 2.9347483361), (3.8380240571, 2.9347483361))
                Line((3.8380240571, 2.9347483361), (4.8880240571, 2.9347483361))
                Line((4.8880240571, 2.9347483361), (3.2619759429, 0.0652516639))
                Line((2.2119759429, 0.0652516639), (3.2619759429, 0.0652516639))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.674619429, perimeter: 16.9496326633
            with BuildLine():
                Line((3.55, 0), (5.25, 3))
                Line((3.55, 0), (4.85, 0))
                Line((4.85, 0), (5.5031743052, 1.178357639))
                Line((5.5031743052, 1.178357639), (5.5031743052, 0))
                Line((5.5031743052, 0), (6.7031743052, 0))
                Line((6.7031743052, 0), (8.4031743052, 2.984817639))
                Line((7.2031743052, 2.984817639), (8.4031743052, 2.984817639))
                Line((6.55, 1.80646), (7.2031743052, 2.984817639))
                Line((6.55, 3), (6.55, 1.80646))
                Line((5.25, 3), (6.55, 3))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7498982088, perimeter: 22.1696352781
            with BuildLine():
                Line((8.6531743052, 2.984817639), (8.6531743052, 1.084817639))
                Line((8.6531743052, 1.084817639), (10.9531743052, 1.084817639))
                Line((10.9531743052, 1.084817639), (10.9531743052, 0.584817639))
                Line((10.9531743052, 0.584817639), (9.6531743052, 0.584817639))
                Line((9.6531743052, 0.584817639), (9.6531743052, 0.784817639))
                Line((9.6531743052, 0.784817639), (8.6531743052, 0.784817639))
                Line((8.6531743052, 0.784817639), (8.6531743052, 0))
                Line((8.6531743052, 0), (11.9531743052, 0))
                Line((11.9531743052, 1.884817639), (11.9531743052, 0))
                Line((9.6531743052, 1.884817639), (11.9531743052, 1.884817639))
                Line((9.6531743052, 2.384817639), (9.6531743052, 1.884817639))
                Line((11.9531743052, 2.384817639), (9.6531743052, 2.384817639))
                Line((11.9531743052, 2.984817639), (11.9531743052, 2.384817639))
                Line((8.6531743052, 2.984817639), (11.9531743052, 2.984817639))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.2775, perimeter: 14.558991472
            with BuildLine():
                Line((13.4031743052, 2.984817639), (12.2031743052, 1.584817639))
                Line((12.2031743052, 0.884817639), (12.2031743052, 1.584817639))
                Line((12.2031743052, 0.884817639), (14.5031743052, 0.884817639))
                Line((14.5031743052, 0.884817639), (14.5031743052, -0.015182361))
                Line((14.5031743052, -0.015182361), (15.5031743052, -0.015182361))
                Line((15.5031743052, -0.015182361), (15.5031743052, 2.084817639))
                Line((15.5031743052, 2.084817639), (14.5031743052, 2.084817639))
                Line((14.5031743052, 2.084817639), (14.5031743052, 1.484817639))
                Line((14.5031743052, 1.484817639), (13.5031743052, 1.484817639))
                Line((13.5031743052, 1.484817639), (13.5031743052, 1.734817639))
                Line((14.6031743052, 2.984817639), (13.5031743052, 1.734817639))
                Line((13.4031743052, 2.984817639), (14.6031743052, 2.984817639))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.75, perimeter: 7.3963758598
            with BuildLine():
                Line((3.3, 0), (3.55, 0))
                Line((3.55, 0), (5.25, 3))
                Line((5, 3), (5.25, 3))
                Line((3.3, 0), (5, 3))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25)

        # Sketch2 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.674619429, perimeter: 16.9496326633
            with BuildLine():
                Line((3.55, 0), (5.25, 3))
                Line((3.55, 0), (4.85, 0))
                Line((4.85, 0), (5.5031743052, 1.178357639))
                Line((5.5031743052, 1.178357639), (5.5031743052, 0))
                Line((5.5031743052, 0), (6.7031743052, 0))
                Line((6.7031743052, 0), (8.4031743052, 2.984817639))
                Line((7.2031743052, 2.984817639), (8.4031743052, 2.984817639))
                Line((6.55, 1.80646), (7.2031743052, 2.984817639))
                Line((6.55, 3), (6.55, 1.80646))
                Line((5.25, 3), (6.55, 3))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)

        # Sketch2 -> Extrude7 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8610854828, perimeter: 26.3927517197
            with BuildLine():
                Line((1.7, 3), (0, 0))
                Line((0, 0), (0.075, 0))
                Line((0.075, 0), (3.3, 0))
                Line((3.3, 0), (5, 3))
                Line((1.7, 3), (5, 3))
            make_face()
            with BuildLine():
                Line((1.1619759429, 0.0652516639), (2.2119759429, 0.0652516639))
                Line((0.1119759429, 0.0652516639), (1.1619759429, 0.0652516639))
                Line((0.1119759429, 0.0652516639), (1.7380240571, 2.9347483361))
                Line((1.7380240571, 2.9347483361), (2.7880240571, 2.9347483361))
                Line((2.7880240571, 2.9347483361), (3.8380240571, 2.9347483361))
                Line((3.8380240571, 2.9347483361), (4.8880240571, 2.9347483361))
                Line((4.8880240571, 2.9347483361), (3.2619759429, 0.0652516639))
                Line((2.2119759429, 0.0652516639), (3.2619759429, 0.0652516639))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)

        # Sketch2 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0129715057, perimeter: 8.6963758598
            with BuildLine():
                Line((2.7880240571, 2.9347483361), (1.1619759429, 0.0652516639))
                Line((1.7380240571, 2.9347483361), (2.7880240571, 2.9347483361))
                Line((0.1119759429, 0.0652516639), (1.7380240571, 2.9347483361))
                Line((0.1119759429, 0.0652516639), (1.1619759429, 0.0652516639))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)

        # Sketch2 -> Extrude9 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0129715057, perimeter: 8.6963758598
            with BuildLine():
                Line((2.2119759429, 0.0652516639), (3.8380240571, 2.9347483361))
                Line((2.7880240571, 2.9347483361), (3.8380240571, 2.9347483361))
                Line((2.7880240571, 2.9347483361), (1.1619759429, 0.0652516639))
                Line((1.1619759429, 0.0652516639), (2.2119759429, 0.0652516639))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)

        # Sketch2 -> Extrude10 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0129715057, perimeter: 8.6963758598
            with BuildLine():
                Line((2.2119759429, 0.0652516639), (3.2619759429, 0.0652516639))
                Line((4.8880240571, 2.9347483361), (3.2619759429, 0.0652516639))
                Line((3.8380240571, 2.9347483361), (4.8880240571, 2.9347483361))
                Line((2.2119759429, 0.0652516639), (3.8380240571, 2.9347483361))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)

        # Sketch2 -> Extrude11 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7498982088, perimeter: 22.1696352781
            with BuildLine():
                Line((8.6531743052, 2.984817639), (8.6531743052, 1.084817639))
                Line((8.6531743052, 1.084817639), (10.9531743052, 1.084817639))
                Line((10.9531743052, 1.084817639), (10.9531743052, 0.584817639))
                Line((10.9531743052, 0.584817639), (9.6531743052, 0.584817639))
                Line((9.6531743052, 0.584817639), (9.6531743052, 0.784817639))
                Line((9.6531743052, 0.784817639), (8.6531743052, 0.784817639))
                Line((8.6531743052, 0.784817639), (8.6531743052, 0))
                Line((8.6531743052, 0), (11.9531743052, 0))
                Line((11.9531743052, 1.884817639), (11.9531743052, 0))
                Line((9.6531743052, 1.884817639), (11.9531743052, 1.884817639))
                Line((9.6531743052, 2.384817639), (9.6531743052, 1.884817639))
                Line((11.9531743052, 2.384817639), (9.6531743052, 2.384817639))
                Line((11.9531743052, 2.984817639), (11.9531743052, 2.384817639))
                Line((8.6531743052, 2.984817639), (11.9531743052, 2.984817639))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)

        # Sketch2 -> Extrude12 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 41 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.2775, perimeter: 14.558991472
            with BuildLine():
                Line((13.4031743052, 2.984817639), (12.2031743052, 1.584817639))
                Line((12.2031743052, 0.884817639), (12.2031743052, 1.584817639))
                Line((12.2031743052, 0.884817639), (14.5031743052, 0.884817639))
                Line((14.5031743052, 0.884817639), (14.5031743052, -0.015182361))
                Line((14.5031743052, -0.015182361), (15.5031743052, -0.015182361))
                Line((15.5031743052, -0.015182361), (15.5031743052, 2.084817639))
                Line((15.5031743052, 2.084817639), (14.5031743052, 2.084817639))
                Line((14.5031743052, 2.084817639), (14.5031743052, 1.484817639))
                Line((14.5031743052, 1.484817639), (13.5031743052, 1.484817639))
                Line((13.5031743052, 1.484817639), (13.5031743052, 1.734817639))
                Line((14.6031743052, 2.984817639), (13.5031743052, 1.734817639))
                Line((13.4031743052, 2.984817639), (14.6031743052, 2.984817639))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)
    return part.part


def model_99556_ccd166fd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60, perimeter: 83
            with BuildLine():
                Line((0, 0), (40, 0))
                Line((40, 0), (40, 1.5))
                Line((40, 1.5), (0, 1.5))
                Line((0, 1.5), (0, 0))
            make_face()
            # Profile area: 60, perimeter: 83
            with BuildLine():
                Line((0, -59), (0, -60.5))
                Line((0, -60.5), (40, -60.5))
                Line((40, -60.5), (40, -59))
                Line((40, -59), (0, -59))
            make_face()
        # OneSide extrude, distance=64
        extrude(amount=64)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 59), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 30, perimeter: 43
            with BuildLine():
                Line((0, 52), (-1.5, 52))
                Line((-1.5, 52), (-1.5, 32))
                Line((-1.5, 32), (0, 32))
                Line((0, 32), (0, 52))
            make_face()
        # OneSide extrude, distance=59
        extrude(amount=59, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 64, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60, perimeter: 83
            with BuildLine():
                Line((-40, 60.5), (-40, 59))
                Line((-40, 59), (0, 59))
                Line((0, 60.5), (0, 59))
                Line((0, 60.5), (-40, 60.5))
            make_face()
            # Profile area: 3039.9196208258, perimeter: 230.0460059563
            with BuildLine():
                Line((-40, 60.5), (-44.5, 60.5))
                Line((-44.5, 60.5), (-44.500000596, -1.5000000224))
                Line((-44.500000596, -1.5000000224), (-40.000000596, -1.5000000224))
                Line((-40.000000596, -1.5000000224), (-40.000000596, -10.0000000224))
                Line((-40.000000596, -10.0000000224), (0, -10.0459789122))
                Line((0, -1.5459789122), (0, -10.0459789122))
                Line((0, 59), (0, -1.5459789122))
                Line((-40, 59), (0, 59))
                Line((-40, 60.5), (-40, 59))
            make_face()
            # Profile area: 60, perimeter: 83
            with BuildLine():
                Line((0, 60.5), (-40, 60.5))
                Line((0, 62), (0, 60.5))
                Line((-40, 62), (0, 62))
                Line((-40, 62), (-40, 60.5))
            make_face()
            # Profile area: 38.25, perimeter: 26
            with BuildLine():
                Line((-44.500000596, -10.0000000224), (-44.500000596, -1.5000000224))
                Line((-40.000000596, -10.0000000224), (-44.500000596, -10.0000000224))
                Line((-40.000000596, -1.5000000224), (-40.000000596, -10.0000000224))
                Line((-44.500000596, -1.5000000224), (-40.000000596, -1.5000000224))
            make_face()
            # Profile area: 6.75, perimeter: 12
            with BuildLine():
                Line((-40, 62), (-40, 60.5))
                Line((-44.5, 62), (-40, 62))
                Line((-44.5, 60.5), (-44.5, 62))
                Line((-40, 60.5), (-44.5, 60.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 60, perimeter: 83
            with BuildLine():
                Line((0, 6.5), (-40, 6.5))
                Line((-40, 6.5), (-40, 5))
                Line((-40, 5), (0, 5))
                Line((0, 5), (0, 6.5))
            make_face()
        # OneSide extrude, distance=24
        extrude(amount=24, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 60, perimeter: 83
            with BuildLine():
                Line((0, 24), (-40, 24))
                Line((0, 25.5), (0, 24))
                Line((-40, 25.5), (0, 25.5))
                Line((-40, 24), (-40, 25.5))
            make_face()
        # OneSide extrude, distance=24
        extrude(amount=24, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -25.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1092.5, perimeter: 153
            with BuildLine():
                Line((0, 6.5), (-19, 6.5))
                Line((0, 64), (0, 6.5))
                Line((-19, 64), (0, 64))
                Line((-19, 6.5), (-19, 64))
            make_face()
            # Profile area: 28.5, perimeter: 41
            with BuildLine():
                Line((-19, 5), (-19, 6.5))
                Line((0, 5), (-19, 5))
                Line((0, 6.5), (0, 5))
                Line((0, 6.5), (-19, 6.5))
            make_face()
            # Profile area: 95, perimeter: 48
            with BuildLine():
                Line((0, 5), (-19, 5))
                Line((-19, 0), (-19, 5))
                Line((0, 0), (-19, 0))
                Line((0, 5), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 59), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 39, perimeter: 55
            with BuildLine():
                Line((-40, 57), (-40, 55.5))
                Line((-66, 57), (-40, 57))
                Line((-66, 55.5), (-66, 57))
                Line((-40, 55.5), (-66, 55.5))
            make_face()
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((-35, 55.5), (-40, 55.5))
                Line((-35, 57), (-35, 55.5))
                Line((-40, 57), (-35, 57))
                Line((-40, 57), (-40, 55.5))
            make_face()
        # OneSide extrude, distance=59
        extrude(amount=59, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_82614_a8ef3280_0000": {"func": model_82614_a8ef3280_0000, "volume": 6.8510487024, "area": 55.2169547619},
    "model_82875_02bdc953_0000": {"func": model_82875_02bdc953_0000, "volume": 570.6796476577, "area": 1196.6854925538},
    "model_83407_56b3a419_0000": {"func": model_83407_56b3a419_0000, "volume": 325.6228299872, "area": 818.1687349821},
    "model_83470_1e871838_0000": {"func": model_83470_1e871838_0000, "volume": 6.0152776645, "area": 25.0695290517},
    "model_84025_ec3401ea_0015": {"func": model_84025_ec3401ea_0015, "volume": 4332.6619505078, "area": 4437.627577678},
    "model_85195_c6ef0067_0000": {"func": model_85195_c6ef0067_0000, "volume": 329.9232377188, "area": 361.262217345},
    "model_87178_f19385af_0000": {"func": model_87178_f19385af_0000, "volume": 58078.1770521171, "area": 19756.6530164234},
    "model_87278_bb9c8879_0000": {"func": model_87278_bb9c8879_0000, "volume": 9.9640612273, "area": 48.3492400735},
    "model_87394_c44702f0_0000": {"func": model_87394_c44702f0_0000, "volume": 67.8049942424, "area": 475.1790177753},
    "model_89822_0157c8d0_0000": {"func": model_89822_0157c8d0_0000, "volume": 250.2015957515, "area": 258.9586887999},
    "model_91441_71022c53_0000": {"func": model_91441_71022c53_0000, "volume": 38.8671376379, "area": 98.0205964529},
    "model_91537_04ffbad0_0000": {"func": model_91537_04ffbad0_0000, "volume": 21.6461021573, "area": 54.2071360717},
    "model_91570_7989dd01_0000": {"func": model_91570_7989dd01_0000, "volume": 2288.7718238716, "area": 1231.4437205794},
    "model_91682_69b6d4ec_0000": {"func": model_91682_69b6d4ec_0000, "volume": 8.1775102268, "area": 57.1954428307},
    "model_93385_c56fafc6_0000": {"func": model_93385_c56fafc6_0000, "volume": 637.6092107037, "area": 801.2597124787},
    "model_93389_b1801754_0000": {"func": model_93389_b1801754_0000, "volume": 0.0693772826, "area": 3.1035093792},
    "model_94399_be0c8a51_0000": {"func": model_94399_be0c8a51_0000, "volume": 17.1075378268, "area": 62.1576045318},
    "model_95913_7c66e78a_0000": {"func": model_95913_7c66e78a_0000, "volume": 29.2759144304, "area": 70.7463607141},
    "model_96186_05427635_0000": {"func": model_96186_05427635_0000, "volume": 50.2159716027, "area": 152.6455428745},
    "model_97828_a0e0ba49_0000": {"func": model_97828_a0e0ba49_0000, "volume": 49.6528031888, "area": 197.825722099},
    "model_99094_559fbfc2_0000": {"func": model_99094_559fbfc2_0000, "volume": 10.3443147215, "area": 87.9057012422},
    "model_99556_ccd166fd_0000": {"func": model_99556_ccd166fd_0000, "volume": 21704.8794003728, "area": 30309.4082505861},
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
