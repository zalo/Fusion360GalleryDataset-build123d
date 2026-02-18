"""Batch 010 - passing/04_6to7ops
93 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_55613_d38aaa88_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 626.5216114485, perimeter: 139.1656905167
            with BuildLine():
                CenterArc((-15, 1.1568393409), 6.3464438263, -10.5026793894, 100.5026793894)
                Line((0, 0), (-8.7598820541, 0))
                Line((0, 40.9042568102), (0, 0))
                CenterArc((-7.5, 40.9042568102), 7.5, 0, 180)
                Line((-15, 7.5032831671), (-15, 40.9042568102))
            make_face()
            with BuildLine():
                CenterArc((-7.5, 40.9042568102), 3.4069214974, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 116.2389281828, perimeter: 38.2191241574
            Circle(6.0827625303)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.5775444198, perimeter: 18.2752092518
            Circle(2.9085898885)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_55625_453e11ac_0001():
    """Model: BlockArrow v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.2695519105, perimeter: 20.6418741854
            with BuildLine():
                Line((-1.4253178087, 2.5204771745), (-0.25, 0))
                Line((-0.25, 0), (0.25, 0))
                Line((0.25, 0), (1.4253178087, 2.5204771745))
                Line((1.4253178087, 2.5204771745), (0.75, 2.2198063144))
                Line((0.75, 8.0204771745), (0.75, 2.2198063144))
                Line((-0.75, 8.0204771745), (0.75, 8.0204771745))
                Line((-0.75, 2.2198063144), (-0.75, 8.0204771745))
                Line((-1.4253178087, 2.5204771745), (-0.75, 2.2198063144))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 7.0204771745)):
                Circle(0.25)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 7.0204771745)):
                Circle(0.25)
        # TwoSides extrude, along=2.6, against=-0.7
        extrude(amount=2.6, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.7, mode=Mode.ADD)
    return part.part


def model_55625_453e11ac_0011():
    """Model: ArrowBox v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7, perimeter: 17.4
            with BuildLine():
                Line((-1.5, 0), (0, 0))
                Line((0, 0), (0, 1.5))
                Line((0, 1.5), (2.5, 1.5))
                Line((2.5, 1.5), (2.5, 0))
                Line((2.5, 0), (4, 0))
                Line((4, 0), (4, 0.2))
                Line((4, 0.2), (2.7, 0.2))
                Line((2.7, 0.2), (2.7, 1.7))
                Line((2.7, 1.7), (-0.2, 1.7))
                Line((-0.2, 1.7), (-0.2, 0.2))
                Line((-0.2, 0.2), (-1.5, 0.2))
                Line((-1.5, 0.2), (-1.5, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.75, perimeter: 8
            with BuildLine():
                Line((2.5, 0), (0, 0))
                Line((2.5, 0), (2.5, 1.5))
                Line((2.5, 1.5), (0, 1.5))
                Line((0, 1.5), (0, 0))
            make_face()
            # Profile area: 1.7, perimeter: 17.4
            with BuildLine():
                Line((4, 0.2), (4, 0))
                Line((2.7, 0.2), (4, 0.2))
                Line((2.7, 1.7), (2.7, 0.2))
                Line((-0.2, 1.7), (2.7, 1.7))
                Line((-0.2, 0.2), (-0.2, 1.7))
                Line((-1.5, 0.2), (-0.2, 0.2))
                Line((-1.5, 0), (-1.5, 0.2))
                Line((0, 0), (-1.5, 0))
                Line((0, 1.5), (0, 0))
                Line((2.5, 1.5), (0, 1.5))
                Line((2.5, 0), (2.5, 1.5))
                Line((4, 0), (2.5, 0))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.85, 3.2)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.85, 0.6)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.35, 0.6)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.35, 3.2)):
                Circle(0.2)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_55722_df6cad0f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 100.8743684534, perimeter: 35.6077707768
            with BuildLine():
                Line((-4.5211437083, 8.7052455278), (-3.1952426084, 8.0924171087))
                CenterArc((-6.2163026429, 3.296881308), 5.667800927, 72.5972958686, 212.5963211113)
                CenterArc((-6.2163026429, 3.296881308), 5.667800927, -74.8063830201, 132.5965459915)
            make_face()
            # Profile area: 218.8944146006, perimeter: 89.9060892481
            with BuildLine():
                Line((-3.1952426084, 8.0924171087), (5.2936930857, 4.1688506814))
                CenterArc((-6.2163026429, 3.296881308), 5.667800927, -74.8063830201, 132.5965459915)
                Line((5.0974030876, -6.2557015976), (-4.7308759129, -2.1728055914))
                CenterArc((7.1926001384, -1.2121782883), 5.461408065, -112.5591364676, 98.9201175983)
                Line((12.5, -2.5), (20.3801212565, 16.4688961339))
                Line((20.3801212565, 16.4688961339), (20.5000694903, 16.7733316868))
                CenterArc((18.6392924702, 17.5064816588), 2, 151.6694057047, 186.8260520775)
                Line((10.3992412762, 6.4370481046), (16.8788443131, 18.4555982407))
                CenterArc((6.852239277, 7.5408844264), 3.7147917583, -114.80627058, 97.5199918571)
            make_face()
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((18.6392924702, 17.5064816588), 2, -21.5045422179, 173.1739479225)
                CenterArc((18.6392924702, 17.5064816588), 2, 151.6694057047, 186.8260520775)
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.5401317975, perimeter: 14.4169839487
            with Locations((-7.151712725, 3.296881308)):
                Circle(2.2945342599)
            # Profile area: 18.0594452618, perimeter: 15.0645837065
            with Locations((7.1926001384, -1.2121782883)):
                Circle(2.3976029625)
            # Profile area: 5.5468178693, perimeter: 8.3488543571
            with Locations((17.5, 15)):
                Circle(1.3287614401)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 221.5579582685, perimeter: 132.0563309492
            with BuildLine():
                Line((4.9866589835, 3.5045589464), (-4.7837077243, 8.020399822))
                CenterArc((-6.2163026429, 3.296881308), 4.9359857529, 73.1279853437, 214.8818891573)
                Line((-4.6901901388, -1.3972571622), (5.3781543108, -5.5798819472))
                CenterArc((7.1926001384, -1.2121782883), 4.7295928909, -112.5591364676, 99.5869192046)
                Line((11.8014892265, -2.2738704693), (19.7017177598, 16.7434275653))
                Line((19.7017177598, 16.7434275653), (19.8191970608, 17.041596824))
                CenterArc((18.6392924702, 17.5064816588), 1.2681848259, -21.5045422179, 173.1739479225)
                Line((17.5230056504, 18.1083092824), (11.0754570489, 6.1492146155))
                CenterArc((6.852239277, 7.5408844264), 4.4466069324, -114.80627058, 96.567755871)
            make_face()
            with BuildLine():
                CenterArc((17.5, 15), 1.3287614401, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.1926001384, -1.2121782883), 2.3976029625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.151712725, 3.296881308), 2.2945342599, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_55769_a112414f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.4203522483, perimeter: 16.0190422444
            with Locations((-5.5, 3)):
                Circle(2.5495097568)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.3528634239, perimeter: 7.3349036517
            with BuildLine():
                Line((-4.0678500058, 1.7646981684), (-6, 1.7646981684))
                Line((-4.0678500058, 3.5), (-4.0678500058, 1.7646981684))
                Line((-6, 3.5), (-4.0678500058, 3.5))
                Line((-6, 1.7646981684), (-6, 3.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 14.35438944, perimeter: 31.4898426045
            with BuildLine():
                CenterArc((5.5, 3), 2.5495097568, 0, 360)
            make_face()
            with BuildLine():
                Line((6.2139728385, 4.0308260495), (4.0778500058, 4.0308260495))
                CenterArc((6.2139728385, 3.49), 0.5408260495, -90, 180)
                Line((4.0778500058, 2.9491739505), (6.2139728385, 2.9491739505))
                CenterArc((4.0778500058, 3.49), 0.5408260495, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((6.5879333503, 2.2545136184), (4.0778500058, 2.2545136184))
                CenterArc((6.5879333503, 1.8120186765), 0.4424949419, -90, 180)
                Line((4.0778500058, 1.3695237345), (6.5879333503, 1.3695237345))
                CenterArc((4.0778500058, 1.8120186765), 0.4424949419, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_56065_00bbe5da_0023():
    """Model: Piston v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6597344573, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude7 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 1.2)):
                Circle(0.25)
        # TwoSides extrude, along=2.4, against=-1.9
        extrude(amount=2.4, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1.9, mode=Mode.SUBTRACT)
    return part.part


def model_56167_90101372_0005():
    """Model: Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.0972340804, perimeter: 18.5353966562
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=66
        extrude(amount=66, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 73), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)
    return part.part


def model_56250_3b6024e3_0008():
    """Model: Column Short"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=7.57
        extrude(amount=7.57)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.57, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_56250_3b6024e3_0009():
    """Model: Column Long"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=9.27
        extrude(amount=9.27)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9.27, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_56250_3b6024e3_0025():
    """Model: Bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=9.7
        extrude(amount=9.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.08552986, perimeter: 1.0367255757
            Circle(0.165)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_56318_df6463e8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 398.9867228627, perimeter: 271.9911485751
            with BuildLine():
                CenterArc((-13, -47), 5, 180, 90)
                Line((13, -52), (-13, -52))
                CenterArc((13, -47), 5, -90, 90)
                Line((18, -47), (18, 1))
                Line((18, 1), (15, 1))
                Line((15, 1), (15, -47))
                CenterArc((13, -47), 2, -90, 90)
                Line((-13, -49), (13, -49))
                CenterArc((-13, -47), 2, 180, 90)
                Line((-15, 1), (-15, -47))
                Line((-18, 1), (-15, 1))
                Line((-18, -47), (-18, 1))
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(18, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 111.9298189273, perimeter: 100.2635708224
            with BuildLine():
                Line((1, 28), (-13.1408945759, 27.9736157765))
                CenterArc((-14, 14), 14, -90, 176.4818528542)
                Line((-14, 0), (1, 0))
                Line((1, 0), (1, 28))
            make_face()
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                CenterArc((-14, 14), 2.5, -90, 180)
                Line((-14, 11.5), (-14, 16.5))
            make_face()
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                Line((-14, 11.5), (-14, 16.5))
                CenterArc((-14, 14), 2.5, 90, 180)
            make_face()
        # OneSide extrude, distance=-112.5
        extrude(amount=-112.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 52), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((0, 14)):
                Circle(3.75)
        # OneSide extrude, distance=32.5
        extrude(amount=32.5, mode=Mode.ADD)
    return part.part


def model_56343_60e8809c_0004():
    """Model: Knife"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.852219216, perimeter: 16.1652130448
            with BuildLine():
                Line((0, 0), (-5.5999998748, 0))
                CenterArc((-5.4973766015, -4.2499693617), 4.2512081943, 91.3832424543, 26.7206375571)
                CenterArc((-5.4973766015, 3.2499693468), 4.2512081943, -118.1038800114, 26.7206375571)
                Line((0, -1), (-5.5999998748, -1.0000000149))
                Line((0, 0), (0, -1))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0343362891, perimeter: 1.4283185371
            with BuildLine():
                CenterArc((-0.400000006, -0.6000000089), 0.400000006, -90, 90)
                Line((-0.400000006, -1.0000000149), (0, -1))
                Line((0, -1), (0, -0.6000000089))
            make_face()
            # Profile area: 0.2339665439, perimeter: 3.0246551838
            with BuildLine():
                Line((-1.000000006, -0.200000003), (-0.996302455, 0))
                Line((-0.400000006, -0.200000003), (-1.000000006, -0.200000003))
                CenterArc((-0.400000006, -0.6000000089), 0.400000006, 0, 90)
                Line((0, -0.6000000089), (0, 0))
                Line((0, 0), (-0.996302455, 0))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.400000006, -0.6000000089)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_56344_3a89f085_0032():
    """Model: screw M8x9,5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((56, 13)):
                Circle(0.4)
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.95), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((56, 13), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((56, 13), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((56, 13)):
                Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2388842145, perimeter: 2.7683073059
            with BuildLine():
                Line((55.8999999985, 13.5916079781), (55.8999999985, 12.4083920219))
                CenterArc((56, 13), 0.6, -99.5940683712, 19.188136598)
                Line((56.1, 13.5916079783), (56.1, 12.4083920217))
                CenterArc((56, 13), 0.6, 80.4059317731, 19.188136598)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_56345_80dc7bcc_0004():
    """Model: FIx Box 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 29 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.1449778714, perimeter: 7.5415926536
            with BuildLine():
                CenterArc((-0.55, -0.55), 0.2, -180, 90)
                Line((-0.55, -0.75), (0.55, -0.75))
                CenterArc((0.55, -0.55), 0.2, -90, 90)
                Line((0.75, -0.55), (0.75, 0.55))
                CenterArc((0.55, 0.55), 0.2, 0, 90)
                Line((0.55, 0.75), (-0.55, 0.75))
                CenterArc((-0.55, 0.55), 0.2, 90, 90)
                Line((-0.75, 0.55), (-0.75, -0.55))
            make_face()
            with BuildLine():
                CenterArc((-0.55, 0.55), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.55, 0.55), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.55, -0.55), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.55, -0.55), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.05, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3595796846, perimeter: 10.683185354
            with BuildLine():
                Line((-0.75, 0.55), (-0.75, -0.55))
                CenterArc((-0.55, -0.55), 0.2, 180, 90)
                Line((-0.55, -0.75), (0.55, -0.75))
                CenterArc((0.55, -0.55), 0.2, -90, 90)
                Line((0.75, -0.55), (0.75, 0.55))
                CenterArc((0.55, 0.55), 0.2, 0, 90)
                Line((0.55, 0.75), (-0.55, 0.75))
                CenterArc((-0.55, 0.55), 0.2, 90, 90)
            make_face()
            with BuildLine():
                CenterArc((-0.55, -0.55), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.55, 0.55), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.55, 0.55), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.55, -0.55), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.05, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_56357_f92aa53e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4800, perimeter: 520
            with BuildLine():
                Line((-40, 60), (-40, 0))
                Line((40, 60), (-40, 60))
                Line((40, 0), (40, 60))
                Line((60, 0), (40, 0))
                Line((60, 80), (60, 0))
                Line((-60, 80), (60, 80))
                Line((-60, 0), (-60, 80))
                Line((-40, 0), (-60, 0))
            make_face()
        # Symmetric extrude, each_side=35
        extrude(amount=35, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 630, perimeter: 158
            with BuildLine():
                Line((35, 63), (-35, 63))
                Line((35, 72), (35, 63))
                Line((-35, 72), (35, 72))
                Line((-35, 63), (-35, 72))
            make_face()
        # OneSide extrude, distance=-30
        extrude(amount=-30, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 614.2400183058, perimeter: 157.2000023425
            with BuildLine():
                Line((34.9000005201, 63.1000009403), (-34.9000005201, 63.1000009403))
                Line((34.9000005201, 71.9000010714), (34.9000005201, 63.1000009403))
                Line((-34.9000005201, 71.9000010714), (34.9000005201, 71.9000010714))
                Line((-34.9000005201, 63.1000009403), (-34.9000005201, 71.9000010714))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


def model_56459_7b640aed_0006():
    """Model: kolo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 697.2372195561, perimeter: 105.2433538953
            with BuildLine():
                CenterArc((208.2127483959, -21.25), 15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((208.2127483959, -21.25), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((208.2127483959, -21.25)):
                Circle(1.75)
        # Symmetric extrude, each_side=-5
        extrude(amount=-5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((208.2127483959, -11.0270923331)):
                Circle(1.5)
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


def model_56459_7b640aed_0008():
    """Model: trojkat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1736.0403394541, perimeter: 497.6291932109
            with BuildLine():
                Line((183.8782593608, -5), (204.3086203236, -5))
                Line((204.3086203236, -5), (204.3086203236, 5))
                Line((204.3086203236, 5), (183.8782593608, 5))
                Line((90.3, 64), (183.8782593608, 5))
                Line((90.3, 64), (90.3, 55.7248407345))
                Line((90.3, 55.7248407345), (178.6836203236, 0))
                Line((90.3, -55.7248407345), (178.6836203236, 0))
                Line((90.3, -64), (90.3, -55.7248407345))
                Line((90.3, -64), (183.8782593608, -5))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-185, 0)):
                Circle(1.5)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(90.3, 0.0000008347, -0.0000000251), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 58.0075994153, perimeter: 233.0303976611
            with BuildLine():
                Line((-60.290358071, 0.4999991653), (55.7248407596, 0.4999991653))
                Line((-60.290358071, -0.0000008347), (-60.290358071, 0.4999991653))
                Line((55.7248407596, -0.0000008347), (-60.290358071, -0.0000008347))
                Line((55.7248407596, 0.4999991653), (55.7248407596, -0.0000008347))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


def model_56459_7b640aed_0013():
    """Model: wzmocnienia-k"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(90, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 64.0464230932, perimeter: 131.9227997196
            with BuildLine():
                Line((2.1911437906, 16.5), (64, 2.0135493259))
                Line((2.1911437906, 16.5), (0, 15.9864506741))
                Line((0, 15.9864506741), (61.8088562094, 1.5))
                Line((61.8088562094, 1.5), (64, 1.5))
                Line((64, 1.5), (64, 2.0135493259))
            make_face()
            # Profile area: 64.0464230932, perimeter: 131.9227997196
            with BuildLine():
                Line((64, 31.5), (61.8088562094, 31.5))
                Line((61.8088562094, 31.5), (0, 17.0135493259))
                Line((0, 17.0135493259), (2.1911437906, 16.5))
                Line((64, 30.9864506741), (2.1911437906, 16.5))
                Line((64, 30.9864506741), (64, 31.5))
            make_face()
            # Profile area: 64.0464230932, perimeter: 131.9227997196
            with BuildLine():
                Line((0, 15.9864506741), (-61.8088562094, 1.5))
                Line((-2.1911437906, 16.5), (0, 15.9864506741))
                Line((-2.1911437906, 16.5), (-64, 2.0135493259))
                Line((-64, 2.0135493259), (-64, 1.5))
                Line((-64, 1.5), (-61.8088562094, 1.5))
            make_face()
            # Profile area: 64.0464230932, perimeter: 131.9227997196
            with BuildLine():
                Line((-64, 30.9864506741), (-2.1911437906, 16.5))
                Line((0, 17.0135493259), (-2.1911437906, 16.5))
                Line((-61.8088562094, 31.5), (0, 17.0135493259))
                Line((-61.8088562094, 31.5), (-64, 31.5))
                Line((-64, 31.5), (-64, 30.9864506741))
            make_face()
            # Profile area: 2.2505208333, perimeter: 9.0020833333
            with BuildLine():
                Line((0, 17.0135493259), (-2.1911437906, 16.5))
                Line((-2.1911437906, 16.5), (0, 15.9864506741))
                Line((2.1911437906, 16.5), (0, 15.9864506741))
                Line((0, 17.0135493259), (2.1911437906, 16.5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 31.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 128, perimeter: 258
            with BuildLine():
                Line((-90, 64), (-90, -64))
                Line((-89, -64), (-90, -64))
                Line((-89, 64), (-89, -64))
                Line((-90, 64), (-89, 64))
            make_face()
            # Profile area: 38.4, perimeter: 256.6
            with BuildLine():
                Line((-90.3, 64), (-90, 64))
                Line((-90.3, -64), (-90.3, 64))
                Line((-90, -64), (-90.3, -64))
                Line((-90, 64), (-90, -64))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 31.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 37.0853137256, perimeter: 247.8354248376
            with BuildLine():
                Line((90, -61.8088562094), (90, 61.8088562094))
                Line((90.3, -61.8088562094), (90, -61.8088562094))
                Line((90.3, 61.8088562094), (90.3, -61.8088562094))
                Line((90, 61.8088562094), (90.3, 61.8088562094))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_56472_753de501_0003():
    """Model: dziubek v7"""
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
        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.2947649065, perimeter: 28.3292492748
            with BuildLine():
                _nurbs_edge([(6.5, -2.5), (6.6387520705, -2.5400893288), (6.9143035755, -2.6211454912), (7.3217729514, -2.7453621564), (7.8533016672, -2.916271483), (8.4976173804, -3.1392848857), (9.1208584509, -3.3731679616), (9.7214499378, -3.6207237403), (10.2971103306, -3.8865445514), (10.844785415, -4.1772941031), (11.3605034682, -4.5025170214), (11.8396325019, -4.873187223), (12.2773931559, -5.2988568152), (12.6693140781, -5.7852454113), (13.0117837114, -6.3313837098), (13.3025631603, -6.9271366797), (13.5415456847, -7.5494252717), (13.7302810761, -8.1659790345), (13.8712670613, -8.7406252567), (13.9673807449, -9.2381646773), (14.0213394518, -9.6289991738), (14.0323800364, -9.841871885), (14.0230206549, -9.9434525159), (14.0089746806, -9.9854387724), (14, -10)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((6.5, -2.5), (5, -2))
                _nurbs_edge([(5, -2), (4.8483651048, -2.2156047887), (4.5753924558, -2.6273188858), (4.2568249408, -3.1864034583), (4.0151726133, -3.8140269513), (4.0209803816, -4.4018488848), (4.3286483565, -4.8010818117), (4.914665945, -5.0354080637), (5.7274203119, -5.1525624921), (6.6977021587, -5.2152678189), (7.7488740766, -5.2923079587), (8.8065053719, -5.4498022446), (9.8073124183, -5.7429535428), (10.7099663091, -6.2056972652), (11.4911845929, -6.8550101857), (12.1400394899, -7.6968666673), (12.5509518163, -8.5238874578), (12.7987777216, -9.229135294), (12.9373644041, -9.7367958063), (13, -10)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((14, -10), (13, -10))
            make_face()
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True)
    return part.part


def model_56489_241ed182_0009():
    """Model: Sleeve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7539822369, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_56489_241ed182_0014():
    """Model: Height_Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 50, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 5.3092917428, perimeter: 8.168141021
            Circle(1.3000000194)
        # OneSide extrude, distance=-46
        extrude(amount=-46, mode=Mode.SUBTRACT)
    return part.part


def model_56666_b0aba65d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch7 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1783294141, perimeter: 1.4969814658
            Circle(0.238252)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_56998_2ed56cb9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 477.7476928608, perimeter: 154.4948550097
            with BuildLine():
                Line((-10.6571916872, 5), (-31.6077765411, 5))
                CenterArc((-31.6077765411, 2.5), 2.5, 90, 180)
                Line((-31.6077765411, 0), (3.5, 0))
                Line((3.5, 0), (3.5, 40.5))
                CenterArc((-0.2120121167, 39.97279273), 3.7492641225, 8.0835045871, 163.8329908259)
                Line((-3.9240242334, 40.5), (-4, 10.5))
                CenterArc((-10.6571916872, 11.7789273781), 6.7789273781, -90, 79.1252777705)
            make_face()
        # OneSide extrude, distance=115
        extrude(amount=115)
    return part.part


def model_57020_310f992c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12250, perimeter: 1030
            with BuildLine():
                Line((25, 120), (0, 120))
                Line((0, 120), (0, 0))
                Line((0, 0), (300, 0))
                Line((300, 0), (300, 120))
                Line((300, 120), (275, 120))
                Line((275, 120), (275, 25))
                Line((275, 25), (25, 25))
                Line((25, 25), (25, 120))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch9 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36000, perimeter: 840
            with BuildLine():
                Line((300, 0), (0, 0))
                Line((300, 120), (300, 0))
                Line((0, 120), (300, 120))
                Line((0, 0), (0, 120))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.ADD)
    return part.part


def model_57255_263121a5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch10 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2650966878, perimeter: 1.8745166283
            with BuildLine():
                Line((0.1171572893, -0.2828427167), (0.2828427167, -0.1171572893))
                Line((0.2828427167, -0.1171572893), (0.2828427167, 0.1171572893))
                Line((0.2828427167, 0.1171572893), (0.1171572893, 0.2828427167))
                Line((0.1171572893, 0.2828427167), (-0.1171572893, 0.2828427167))
                Line((-0.1171572893, 0.2828427167), (-0.2828427167, 0.1171572893))
                Line((-0.2828427167, 0.1171572893), (-0.2828427167, -0.1171572893))
                Line((-0.2828427167, -0.1171572893), (-0.1171572893, -0.2828427167))
                Line((-0.1171572893, -0.2828427167), (0.1171572893, -0.2828427167))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_57433_498aa3b9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2127807639, perimeter: 5.9926236774
            with BuildLine():
                Line((0, 0), (0.6532368768, -0.0216721603))
                Line((0.6532368768, -0.0216721603), (0.398756739, 2.4935566983))
                Line((0.398756739, 2.4935566983), (0.0827276634, 2.4935566983))
                Line((0.0827276634, 2.4935566983), (0, 0))
            make_face()
            # Profile area: 1.5745613255, perimeter: 7.2607902932
            with BuildLine():
                Line((0.398756739, 2.4935566983), (0.0827276634, 2.4935566983))
                Line((1.0493004875, 2.4935566983), (0.398756739, 2.4935566983))
                Line((1, 3), (1.0493004875, 2.4935566983))
                Line((-2, 3), (1, 3))
                Line((-2.1688144339, 2.4935566983), (-2, 3))
                Line((0.0827276634, 2.4935566983), (-2.1688144339, 2.4935566983))
            make_face()
            # Profile area: 5.2743366273, perimeter: 13.9163214504
            with BuildLine():
                Line((-2.1688144339, 2.4935566983), (-2, 3))
                Line((-2, 3), (-2.5, 6.0486732546))
                Line((-2.5, 6.0486732546), (-3, 6))
                Line((-3, 6), (-3, 3))
                Line((-3, 3), (-4, 0))
                Line((-4, 0), (-3, 0))
                Line((-3, 0), (-2.1688144339, 2.4935566983))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch12 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 129.5885857049, perimeter: 59.8027270764
            with BuildLine():
                CenterArc((4.9142273929, -27.0675552023), 2.4935786398, 180, 180)
                Line((7.4078060327, -27.0675552023), (7.4078060327, -5))
                CenterArc((4.9142273929, -5), 2.4935786398, 0, 180)
                Line((2.4206487531, -5), (2.4206487531, -27.0675552023))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_57872_a723a393_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28, perimeter: 22
            with BuildLine():
                Line((7, -4), (0, -4))
                Line((7, 0), (7, -4))
                Line((0, 0), (7, 0))
                Line((0, -4), (0, 0))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((6.5, 4), (0.5, 4))
                Line((6.5, 7), (6.5, 4))
                Line((0.5, 7), (6.5, 7))
                Line((0.5, 4), (0.5, 7))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.125, perimeter: 11.5
            with BuildLine():
                Line((3, 0.5), (0.5, 0.5))
                Line((3, 3.75), (3, 0.5))
                Line((0.5, 3.75), (3, 3.75))
                Line((0.5, 0.5), (0.5, 3.75))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.3778612058, perimeter: 11.6556068959
            with BuildLine():
                Line((3.9221965521, 0.5), (3.9221965521, 3.75))
                Line((6.5, 0.5), (3.9221965521, 0.5))
                Line((6.5, 3.75), (6.5, 0.5))
                Line((3.9221965521, 3.75), (6.5, 3.75))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_57877_1100841a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36.75, perimeter: 28
            with BuildLine():
                Line((0, -3.5), (0, 0))
                Line((0, 0), (-10.5, 0))
                Line((-10.5, 0), (-10.5, -3.5))
                Line((-10.5, -3.5), (0, -3.5))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.6937725441, perimeter: 22.5144784303
            with BuildLine():
                Line((-0.5, 2.3776278875), (-10, 2.3776278875))
                Line((-0.5, 4.1348671027), (-0.5, 2.3776278875))
                Line((-10, 4.1348671027), (-0.5, 4.1348671027))
                Line((-10, 2.3776278875), (-10, 4.1348671027))
            make_face()
            # Profile area: 15.150091042, perimeter: 22.189492851
            with BuildLine():
                Line((-0.5, 0.1884097539), (-10, 0.1884097539))
                Line((-0.5, 1.7831561794), (-0.5, 0.1884097539))
                Line((-10, 1.7831561794), (-0.5, 1.7831561794))
                Line((-10, 0.1884097539), (-10, 1.7831561794))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3776278875, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7246976045, perimeter: 5.5797580836
            with BuildLine():
                Line((8.2898790418, 0.5), (8, 0.5))
                Line((8.2898790418, 3), (8.2898790418, 0.5))
                Line((8, 3), (8.2898790418, 3))
                Line((8, 0.5), (8, 3))
            make_face()
            # Profile area: 0.625, perimeter: 5.5
            with BuildLine():
                Line((5.5, 3), (5.5, 0.5))
                Line((5.25, 3), (5.5, 3))
                Line((5.25, 0.5), (5.25, 3))
                Line((5.5, 0.5), (5.25, 0.5))
            make_face()
            # Profile area: 0.5808408555, perimeter: 5.4646726844
            with BuildLine():
                Line((3, 0.5), (2.7676636578, 0.5))
                Line((3, 3), (3, 0.5))
                Line((2.7676636578, 3), (3, 3))
                Line((2.7676636578, 0.5), (2.7676636578, 3))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_60279_4d453fb2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.75, perimeter: 20
            with BuildLine():
                Line((7.956364269, -2.5), (0.456364269, -2.5))
                Line((7.956364269, 0), (7.956364269, -2.5))
                Line((0.456364269, 0), (7.956364269, 0))
                Line((0.456364269, -2.5), (0.456364269, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.75, perimeter: 16
            with BuildLine():
                Line((-7.5, 2), (-1, 2))
                Line((-7.5, 0.5), (-7.5, 2))
                Line((-1, 0.5), (-7.5, 0.5))
                Line((-1, 2), (-1, 0.5))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5149707608, perimeter: 16.2181788183
            with BuildLine():
                Line((-7.5393710898, 2.0697183447), (-1.0000000164, 2.0697183447))
                Line((-7.5393710898, 0.5000000089), (-7.5393710898, 2.0697183447))
                Line((-7.5, 0.5000000089), (-7.5393710898, 0.5000000089))
                Line((-7.5, 2), (-7.5, 0.5000000089))
                Line((-1.0000000164, 2), (-7.5, 2))
                Line((-1.0000000164, 2.0697183447), (-1.0000000164, 2))
            make_face()
            # Profile area: 9.7499999173, perimeter: 15.9999999493
            with BuildLine():
                Line((-1.0000000164, 0.5000000089), (-7.5, 0.5000000089))
                Line((-1.0000000164, 2), (-1.0000000164, 0.5000000089))
                Line((-1.0000000164, 2), (-7.5, 2))
                Line((-7.5, 2), (-7.5, 0.5000000089))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_60716_dcd9370c_0001():
    """Model: motor v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0218818406, perimeter: 6.2175053652
            with BuildLine():
                Line((1.4999999603, 2.0000000298), (-1.4999999603, 2.0000000298))
                CenterArc((0, 0), 2.5, 53.1301034925, 73.739793015)
            make_face()
            # Profile area: 3.7781183025, perimeter: 11.817505697
            with BuildLine():
                Line((-1.4999999603, 2.0000000298), (-2.5000000373, 2.0000000298))
                CenterArc((0, 0), 2.5, 53.1301034925, 73.739793015)
                Line((2.3000000343, 2.0000000298), (1.4999999603, 2.0000000298))
                Line((2.3000000343, 3.0000000447), (2.3000000343, 2.0000000298))
                Line((-2.5000000373, 3.0000000447), (2.3000000343, 3.0000000447))
                Line((-2.5000000373, 2.0000000298), (-2.5000000373, 3.0000000447))
            make_face()
        # OneSide extrude, distance=-6.3
        extrude(amount=-6.3, mode=Mode.SUBTRACT)
    return part.part


def model_60720_ef9a0a95_0008():
    """Model: bed v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9, perimeter: 15
            with BuildLine():
                Line((3.5, 0), (3.5, -1.5))
                Line((-2.5, 0), (3.5, 0))
                Line((-2.5, -1.5), (-2.5, 0))
                Line((3.5, -1.5), (-2.5, -1.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.5, perimeter: 25
            with BuildLine():
                Line((-3, 0.5), (-3, 8))
                Line((2, 0.5), (-3, 0.5))
                Line((2, 8), (2, 0.5))
                Line((2, 8), (-3, 8))
            make_face()
            # Profile area: 2, perimeter: 10.8
            with BuildLine():
                Line((2, 8), (-3, 8))
                Line((2, 8.4), (2, 8))
                Line((-3, 8.4), (2, 8.4))
                Line((-3, 8), (-3, 8.4))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 37.5, perimeter: 25
            with BuildLine():
                Line((3, 8), (-2, 8))
                Line((-2, 0.5), (-2, 8))
                Line((3, 0.5), (-2, 0.5))
                Line((3, 8), (3, 0.5))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_60720_ef9a0a95_0010():
    """Model: STORAGE DR v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0, 1), (-2, 1))
                Line((-2, 1), (-2, 0))
                Line((-2, 0), (0, 0))
                Line((0, 0), (0, 1))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.1600002432, perimeter: 13.4000001997
            with BuildLine():
                Line((1.8000000268, 0.200000003), (1.8000000268, 5.300000079))
                Line((1.8000000268, 5.300000079), (0.200000003, 5.300000079))
                Line((0.200000003, 5.300000079), (0.200000003, 0.200000003))
                Line((0.200000003, 0.200000003), (1.8000000268, 0.200000003))
            make_face()
        # OneSide extrude, distance=-0.95
        extrude(amount=-0.95, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.200000003, perimeter: 2.400000006
            with BuildLine():
                Line((0, 1), (-0.200000003, 1))
                Line((0, 2), (0, 1))
                Line((-0.200000003, 2), (0, 2))
                Line((-0.200000003, 1), (-0.200000003, 2))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.ADD)
    return part.part


def model_60723_c8e7621d_0000():
    """Model: sitting part v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 894.6349540849, perimeter: 115.7079632679
            with BuildLine():
                CenterArc((12.5, 12.5), 2.5, 0, 90)
                Line((12.5, 15), (-12.5, 15))
                CenterArc((-12.5, 12.5), 2.5, 90, 90)
                Line((-15, 12.5), (-15, -12.5))
                CenterArc((-12.5, -12.5), 2.5, 180, 90)
                Line((-12.5, -15), (12.5, -15))
                CenterArc((12.5, -12.5), 2.5, -90, 90)
                Line((15, -12.5), (15, 12.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((8.1471901165, -8.6533081126)):
                Circle(0.25)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((5.6032743535, -7.3214285846)):
                Circle(0.2)
        # OneSide extrude, distance=-11.5
        extrude(amount=-11.5, mode=Mode.SUBTRACT)
    return part.part


def model_60759_23829707_0007():
    """Model: cradle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 285.095707183, perimeter: 105.547492495
            with BuildLine():
                Line((-31.4999999686, 8.3044812403), (-7, 8))
                Line((-31.4999999686, 3.9992690198), (-31.4999999686, 8.3044812403))
                CenterArc((-31.4999999686, -0.0007309802), 4, 0, 90)
                Line((-8.4999999686, -0.0007309802), (-27.4999999686, -0.0007309802))
                CenterArc((0, 0), 8.5, 95.8276284829, 84.1772988206)
                Line((-0.8630562112, 25.9927289658), (-0.8630562112, 8.4560708356))
                Line((-6.8191258325, 22.5539905666), (-0.8630562112, 25.9927289658))
                Line((-7, 8), (-6.8191258325, 22.5539905666))
            make_face()
        # Symmetric extrude, each_side=8
        extrude(amount=8, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0983261069, 7.911783382, 0), x_dir=(0, 0, -1), z_dir=(0.0124268461, 0.9999227838, 0))):
            # Profile area: 96, perimeter: 44
            with BuildLine():
                Line((8, 25.6007661676), (-8, 25.6007661676))
                Line((8, 31.6007661676), (8, 25.6007661676))
                Line((-8, 31.6007661676), (8, 31.6007661676))
                Line((-8, 25.6007661676), (-8, 31.6007661676))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.4175879751, perimeter: 39.0928896656
            with BuildLine():
                Line((-6.9350083663, 13.2295340824), (-6.9486734905, 12.129973589))
                Line((-25.4383290354, 13.2295340824), (-6.9350083663, 13.2295340824))
                Line((-25.4383290354, 13.2295340824), (-25.4383290354, 12.2295340824))
                Line((-25.4383290354, 12.2295340824), (-6.9486734905, 12.129973589))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


def model_60760_f95d00ad_0014():
    """Model: part2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.6393797974, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 8.6393797974, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_60762_ffc5da86_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1600, perimeter: 160
            with BuildLine():
                Line((-20, 20), (20, 20))
                Line((-20, -20), (-20, 20))
                Line((20, -20), (-20, -20))
                Line((20, 20), (20, -20))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 112.5, perimeter: 75.7721296361
            with BuildLine():
                Line((-35, -30), (-32.5, -30))
                Line((-32.5, -30), (-15, 0))
                Line((-20, 0), (-15, 0))
                Line((-20, 0), (-35, -30))
            make_face()
            # Profile area: 112.5, perimeter: 71.6227766017
            with BuildLine():
                Line((15, 0), (20, 0))
                Line((27.5, -30), (15, 0))
                Line((30, -30), (27.5, -30))
                Line((20, 0), (30, -30))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 217.5001655224, perimeter: 112.4245204535
            with BuildLine():
                Line((20, 3), (16, 3))
                Line((20, 3), (40, 50))
                Line((40, 50), (35.682775917, 51.8371166311))
                Line((35.682775917, 51.8371166311), (16, 3))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)
    return part.part


def model_61007_2d0c5172_0000():
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70.8821842466, perimeter: 29.8451302091
            Circle(4.75)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.0166993776, perimeter: 24.8185819634
            Circle(3.95)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.8875198295, perimeter: 14.3445505284
            with BuildLine():
                _nurbs_edge([(1.1339528421, -2.548507529), (1.1745208994, -2.5487515453), (1.2553703884, -2.5458963208), (1.3757846986, -2.5315837193), (1.5346165485, -2.4924275959), (1.7300143165, -2.4100377856), (1.9214649616, -2.2943630243), (2.107351697, -2.1458243303), (2.2850222313, -1.96520845), (2.4510862504, -1.753700717), (2.6016710994, -1.5129252192), (2.7326848858, -1.2449847272), (2.8400932362, -0.9525016085), (2.9201375841, -0.6386644686), (2.9693186717, -0.3072952251), (2.9844199333, 0.0370863217), (2.9625129564, 0.3891921093), (2.9009811558, 0.7429010518), (2.7975165197, 1.0911759315), (2.6501905234, 1.4260247759), (2.4580764152, 1.73883936), (2.2218367131, 2.0206942385), (1.9443021832, 2.2626670882), (1.6311224399, 2.4561352385), (1.2912513002, 2.5931198475), (0.9378734951, 2.666522104), (0.5874228964, 2.6708480792), (0.2574567974, 2.6032450746), (-0.0350873594, 2.4644173571), (-0.2758587921, 2.2596765782), (-0.4548202838, 1.9997765119), (-0.5684830866, 1.702305528), (-0.6188183817, 1.3892992335), (-0.6114709881, 1.0840572971), (-0.5541532188, 0.8081432906), (-0.4551318655, 0.5785204005), (-0.3212850454, 0.404090072), (-0.157928103, 0.2845219323), (0.029444768, 0.2111895541), (0.2341279616, 0.1678025501), (0.4464322908, 0.1304441904), (0.6545670478, 0.0715695848), (0.8468349114, -0.0336049911), (1.0132439519, -0.2020800986), (1.1477808111, -0.4359904332), (1.2482944537, -0.7238674216), (1.3152543447, -1.0459289206), (1.3508495122, -1.3781738586), (1.3579896116, -1.6967647436), (1.3392637714, -1.9827405723), (1.2961918905, -2.2251755772), (1.2429113329, -2.3798881994), (1.1924951652, -2.473078125), (1.154240885, -2.5250557924), (1.1339528421, -2.548507529)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_61007_3de87d8b_0000():
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70.8821842466, perimeter: 29.8451302091
            Circle(4.75)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.0166993776, perimeter: 24.8185819634
            Circle(3.95)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0697221535, perimeter: 5.5754281374
            with BuildLine():
                Line((0, 0.5000000045), (0, 3.1000000432))
                _nurbs_edge([(0, 3.1000000432), (0.0154461539, 3.0999043553), (0.0462842531, 3.0972257172), (0.0923784663, 3.0857461585), (0.1535129176, 3.0554543777), (0.2290506124, 2.9924575864), (0.3027495317, 2.9044625667), (0.3725957052, 2.7922901601), (0.4356404694, 2.6575605024), (0.4885808121, 2.5025747706), (0.528211402, 2.3302974299), (0.5519317209, 2.1443291324), (0.5582678807, 1.9489210872), (0.5473746183, 1.748982356), (0.5205844013, 1.5497649278), (0.4800317543, 1.3565679063), (0.4282870441, 1.174445956), (0.3679995521, 1.0078889928), (0.3015814108, 0.8605403835), (0.23081221, 0.734758626), (0.1567488295, 0.6316391112), (0.0953121955, 0.567541446), (0.0480966758, 0.5297775501), (0.0161161527, 0.5091652591), (0, 0.5000000045)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_61007_ea617ece_0000():
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70.8821842466, perimeter: 29.8451302091
            Circle(4.75)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.0166993776, perimeter: 24.8185819634
            Circle(3.95)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7251131386, perimeter: 10.5935309347
            with BuildLine():
                _nurbs_edge([(-0.6000000089, -0.5000000075), (-0.6138414998, -0.4886165643), (-0.6405738305, -0.4648700621), (-0.6778204059, -0.4263114667), (-0.7217707958, -0.3690144556), (-0.7673204768, -0.2876142036), (-0.8039475988, -0.1966041538), (-0.8326533878, -0.0963852014), (-0.8551391178, 0.0123219471), (-0.8733538869, 0.1285062968), (-0.8890613634, 0.2508854178), (-0.9034266838, 0.3779315304), (-0.9165289393, 0.5078791607), (-0.9270962935, 0.6387793608), (-0.93308053, 0.7687300272), (-0.9320927132, 0.8960760229), (-0.9218976607, 1.0196275136), (-0.9008691375, 1.1388608179), (-0.8685059888, 1.2541634961), (-0.8251995904, 1.3664807934), (-0.7719513438, 1.47692386), (-0.7101098256, 1.5863834399), (-0.6411105793, 1.6951640237), (-0.5661973349, 1.8025455294), (-0.4863802694, 1.9070723338), (-0.4024281492, 2.0069300251), (-0.3148446785, 2.1003042204), (-0.2238574476, 2.1857122081), (-0.1293833582, 2.2624338897), (-0.031072841, 2.3305509537), (0.0715813533, 2.3906493689), (0.179150396, 2.4436134697), (0.2921773696, 2.4904010797), (0.4110645331, 2.5317899474), (0.5360479836, 2.5682948221), (0.6672512899, 2.6002447954), (0.7772227546, 2.6223007566), (0.8625176395, 2.6369035609), (0.9206308893, 2.6457780045), (0.9500000142, 2.6500000395)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.6000000089, -0.5000000075), (-0.6195257292, -0.4974695929), (-0.6588089483, -0.491773513), (-0.7184291051, -0.4813235859), (-0.7993144851, -0.4635761476), (-0.9026469229, -0.4348335048), (-1.0079126827, -0.3989677929), (-1.1145156497, -0.3548555728), (-1.2214591251, -0.3006855601), (-1.32739197, -0.234563424), (-1.4306360182, -0.1551132586), (-1.5292369389, -0.0619943121), (-1.6209618525, 0.0433291854), (-1.7035000147, 0.1578441038), (-1.7747979384, 0.2779776476), (-1.8333810572, 0.4004195798), (-1.8786284739, 0.5229036494), (-1.9112065395, 0.6452808712), (-1.9328248024, 0.7692415905), (-1.9455472462, 0.897135073), (-1.9512219415, 1.0310358593), (-1.9508983897, 1.1717658598), (-1.9441526983, 1.3177796727), (-1.929546729, 1.4658569092), (-1.9052242773, 1.612020122), (-1.8694895983, 1.7524111848), (-1.8213196434, 1.8840888989), (-1.7610929222, 2.0061035505), (-1.6903357743, 2.1192982541), (-1.6109232867, 2.2253924385), (-1.5244150929, 2.3262612542), (-1.4314123783, 2.4231984167), (-1.3307062904, 2.5160238632), (-1.2197814309, 2.6032975235), (-1.0957387142, 2.6828871488), (-0.9561140319, 2.7524327441), (-0.799658095, 2.8098141541), (-0.6273424477, 2.8537143293), (-0.4424627957, 2.8837632533), (-0.2498267771, 2.9002506308), (-0.0551946842, 2.9039584292), (0.1353752619, 2.8959478303), (0.3161476561, 2.8773651244), (0.4823251858, 2.8492459676), (0.6307249015, 2.8123058241), (0.759492142, 2.766986402), (0.8460862733, 2.7242166401), (0.9016779324, 2.6885161848), (0.9345849916, 2.6631069163), (0.9500000142, 2.6500000395)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_61091_f7d8529d_0001():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.6714586764, perimeter: 26.5619449019
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 180)
                Line((-3, 0), (-4.5, 0))
                CenterArc((0, 0), 3, 0, 180)
                Line((4.5, 0), (3, 0))
            make_face()
        # Symmetric extrude, each_side=2.4
        extrude(amount=2.4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.2310793461, perimeter: 32.1028096399
            with BuildLine():
                Line((4.5, 0), (4.5, 4.1581245773))
                Line((3.6, 4.1581245773), (4.5, 4.1581245773))
                CenterArc((0, 0), 5.5, 49.1148071073, 81.7703857854)
                Line((-3.6, 4.1581245773), (-4.5, 4.1581245773))
                Line((-4.5, 0), (-4.5, 4.1581245773))
                CenterArc((0, 0), 4.5, 0, 180)
            make_face()
        # Symmetric extrude, each_side=1.65
        extrude(amount=1.65, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((3.6, 0)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-3.6, 0)):
                Circle(0.6)
        # OneSide extrude, distance=-4.9
        extrude(amount=-4.9, mode=Mode.SUBTRACT)
    return part.part


def model_61091_f7d8529d_0003():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9444864606, perimeter: 6.3874878642
            with BuildLine():
                Line((0.719615253, 0.7845299579), (-0.319615247, 1.015470069))
                Line((-0.319615247, 1.015470069), (-1.0392305, 0.2309401111))
                Line((-1.0392305, 0.2309401111), (-0.719615253, -0.7845299579))
                Line((-0.719615253, -0.7845299579), (0.319615247, -1.015470069))
                Line((0.319615247, -1.015470069), (1.0392305, -0.2309401111))
                Line((1.0392305, -0.2309401111), (0.719615253, 0.7845299579))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=9.4
        extrude(amount=9.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.0028365705, 9.6206422626)):
                Circle(0.1)
        # Symmetric extrude, each_side=1.1
        extrude(amount=1.1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_61198_0c99f50a_0011():
    """Model: 支撐桿固定套"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-27.6367178757, 7.8240963563)):
                Circle(0.7)
        # OneSide extrude, distance=-5.8
        extrude(amount=-5.8)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-27.6367178757, 7.8240963563), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-27.6367178757, 7.8240963563), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-27.6367178757, 7.8240963563)):
                Circle(0.7)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch1 -> 拉伸3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((-27.6367178757, 7.8240963563), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-27.6367178757, 7.8240963563), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch2 -> 拉伸4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2470765814, perimeter: 4.1569219382
            with BuildLine():
                Line((-27.2903077142, 8.4240963563), (-27.9831280372, 8.4240963563))
                Line((-27.9831280372, 8.4240963563), (-28.3295381987, 7.8240963563))
                Line((-28.3295381987, 7.8240963563), (-27.9831280372, 7.2240963563))
                Line((-27.9831280372, 7.2240963563), (-27.2903077142, 7.2240963563))
                Line((-27.2903077142, 7.2240963563), (-26.9438975527, 7.8240963563))
                Line((-26.9438975527, 7.8240963563), (-27.2903077142, 8.4240963563))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_61198_0c99f50a_0012():
    """Model: 固定螺栓"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2252211349, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((-32.7640158409, 8.1798378254), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-32.7640158409, 8.1798378254), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-32.7640158409, 8.1798378254)):
                Circle(0.5)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((-32.7640158409, 8.1798378254), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-32.7640158409, 8.1798378254), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch1 -> 拉伸3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-32.7640158409, 8.1798378254)):
                Circle(0.5)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch2 -> 拉伸4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.2470765814, perimeter: 4.1569219382
            with BuildLine():
                Line((33.1104260024, 8.7798378254), (32.4176056794, 8.7798378254))
                Line((32.4176056794, 8.7798378254), (32.0711955179, 8.1798378254))
                Line((32.0711955179, 8.1798378254), (32.4176056794, 7.5798378254))
                Line((32.4176056794, 7.5798378254), (33.1104260024, 7.5798378254))
                Line((33.1104260024, 7.5798378254), (33.4568361639, 8.1798378254))
                Line((33.4568361639, 8.1798378254), (33.1104260024, 8.7798378254))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_61270_6fc99e6c_0005():
    """Model: Moveable jaw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 45 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0442982456, perimeter: 1.0540687339
            with BuildLine():
                Line((1.1236102527, 0.7096485807), (1.4981470036, 0.7096485807))
                Line((1.4981470036, 0.7096485807), (1.4981470036, 0.9461981075))
                Line((1.1236102527, 0.7096485807), (1.4981470036, 0.9461981075))
            make_face()
            # Profile area: 0.0442982456, perimeter: 1.0540687339
            with BuildLine():
                Line((3.0509264982, 0.2365495269), (3.0509264982, 0.4730990538))
                Line((3.4254632491, 0.2365495269), (3.0509264982, 0.2365495269))
                Line((3.0509264982, 0.4730990538), (3.4254632491, 0.2365495269))
            make_face()
            # Profile area: 0.0442982456, perimeter: 1.0540687339
            with BuildLine():
                Line((0.3745367509, 0.2365495269), (0.7490735018, 0.2365495269))
                Line((0.7490735018, 0.2365495269), (0.7490735018, 0.4730990538))
                Line((0.3745367509, 0.2365495269), (0.7490735018, 0.4730990538))
            make_face()
            # Profile area: 20.52, perimeter: 20.2944410108
            with BuildLine():
                Line((3.0509264982, 0.4730990538), (3.4254632491, 0.2365495269))
                Line((3.4254632491, 0.2365495269), (3.8, 0))
                Line((3.8, 0), (3.8, 6))
                Line((3.8, 6), (0, 6))
                Line((0, 6), (0, 0))
                Line((0, 0), (0.3745367509, 0.2365495269))
                Line((0.3745367509, 0.2365495269), (0.7490735018, 0.4730990538))
                Line((0.7490735018, 0.4730990538), (1.1236102527, 0.7096485807))
                Line((1.1236102527, 0.7096485807), (1.4981470036, 0.9461981075))
                Line((1.4981470036, 0.9461981075), (1.9, 1.2))
                Line((1.9, 1.2), (2.3018529964, 0.9461981075))
                Line((2.3018529964, 0.9461981075), (2.6763897473, 0.7096485807))
                Line((2.6763897473, 0.7096485807), (3.0509264982, 0.4730990538))
            make_face()
            # Profile area: 0.0442982456, perimeter: 1.0540687339
            with BuildLine():
                Line((3.4254632491, 0), (3.4254632491, 0.2365495269))
                Line((3.4254632491, 0), (3.8, 0))
                Line((3.4254632491, 0.2365495269), (3.8, 0))
            make_face()
            # Profile area: 0.0442982456, perimeter: 1.0540687339
            with BuildLine():
                Line((0, 0), (0.3745367509, 0))
                Line((0.3745367509, 0), (0.3745367509, 0.2365495269))
                Line((0, 0), (0.3745367509, 0.2365495269))
            make_face()
            # Profile area: 0.0442982456, perimeter: 1.0540687339
            with BuildLine():
                Line((2.6763897473, 0.7096485807), (3.0509264982, 0.4730990538))
                Line((2.6763897473, 0.4730990538), (2.6763897473, 0.7096485807))
                Line((3.0509264982, 0.4730990538), (2.6763897473, 0.4730990538))
            make_face()
            # Profile area: 0.0442982456, perimeter: 1.0540687339
            with BuildLine():
                Line((0.7490735018, 0.4730990538), (1.1236102527, 0.4730990538))
                Line((1.1236102527, 0.4730990538), (1.1236102527, 0.7096485807))
                Line((0.7490735018, 0.4730990538), (1.1236102527, 0.7096485807))
            make_face()
            # Profile area: 0.1015197811, perimeter: 1.764271313
            with BuildLine():
                Line((1.4981470036, 0.9461981075), (1.8726837545, 0.9461981075))
                Line((1.8726837545, 0.9461981075), (1.9, 0.9634504731))
                Line((1.9, 0.9634504731), (1.9273162455, 0.9461981075))
                Line((2.3018529964, 0.9461981075), (1.9273162455, 0.9461981075))
                Line((1.9, 1.2), (2.3018529964, 0.9461981075))
                Line((1.4981470036, 0.9461981075), (1.9, 1.2))
            make_face()
            # Profile area: 0.0442982456, perimeter: 1.0540687339
            with BuildLine():
                Line((2.3018529964, 0.9461981075), (2.6763897473, 0.7096485807))
                Line((2.3018529964, 0.7096485807), (2.3018529964, 0.9461981075))
                Line((2.6763897473, 0.7096485807), (2.3018529964, 0.7096485807))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.8, 5.5823955097)):
                Circle(0.25)
        # OneSide extrude, distance=-5.1
        extrude(amount=-5.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 2.1424777961
            with BuildLine():
                CenterArc((-1.9, 0.8), 0.6, 0, 90)
                Line((-1.9, 0.8), (-1.9, 1.4))
                Line((-1.3, 0.8), (-1.9, 0.8))
            make_face()
            # Profile area: 0.2827433388, perimeter: 2.1424777961
            with BuildLine():
                Line((-1.9, 0.8), (-1.9, 0.2))
                Line((-1.9, 0.8), (-2.5, 0.8))
                CenterArc((-1.9, 0.8), 0.6, -180, 90)
            make_face()
            # Profile area: 0.2827433388, perimeter: 2.1424777961
            with BuildLine():
                CenterArc((-1.9, 0.8), 0.6, -90, 90)
                Line((-1.3, 0.8), (-1.9, 0.8))
                Line((-1.9, 0.8), (-1.9, 0.2))
            make_face()
            # Profile area: 0.2827433388, perimeter: 2.1424777961
            with BuildLine():
                Line((-1.9, 0.8), (-2.5, 0.8))
                Line((-1.9, 0.8), (-1.9, 1.4))
                CenterArc((-1.9, 0.8), 0.6, 90, 90)
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_61901_f74dfb53_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.75, perimeter: 20
            with BuildLine():
                Line((6.5, -3.5), (0, -3.5))
                Line((6.5, 0), (6.5, -3.5))
                Line((0, 0), (6.5, 0))
                Line((0, -3.5), (0, 0))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.5, perimeter: 17
            with BuildLine():
                Line((6, 7.5), (0.5, 7.5))
                Line((6, 10.5), (6, 7.5))
                Line((0.5, 10.5), (6, 10.5))
                Line((0.5, 7.5), (0.5, 10.5))
            make_face()
            # Profile area: 27.5, perimeter: 21
            with BuildLine():
                Line((6, 2), (0.5, 2))
                Line((6, 7), (6, 2))
                Line((0.5, 7), (6, 7))
                Line((0.5, 2), (0.5, 7))
            make_face()
            # Profile area: 5.5, perimeter: 13
            with BuildLine():
                Line((6, 0.5), (0.5, 0.5))
                Line((6, 1.5), (6, 0.5))
                Line((0.5, 1.5), (6, 1.5))
                Line((0.5, 0.5), (0.5, 1.5))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((3, 10.5), (0.5, 10.5))
                Line((0.5, 10.5), (0.5, 7.5))
                Line((3, 7.5), (0.5, 7.5))
                Line((3, 7.5), (3, 10.5))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((0.5, 2), (0.5, 7))
                Line((3, 2), (0.5, 2))
                Line((3, 7), (3, 2))
                Line((3, 7), (0.5, 7))
            make_face()
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((0.5, 1.5), (0.5, 0.5))
                Line((3, 0.5), (0.5, 0.5))
                Line((3, 0.5), (3, 1.5))
                Line((3, 1.5), (0.5, 1.5))
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)
    return part.part


def model_62101_f765b04e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, -2.5)):
                Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0525587993, perimeter: 40.4204703946
            with BuildLine():
                Line((-7.5, 0), (-5, 1.5))
                Line((-5, 6), (-5, 1.5))
                Line((-11, 7), (-5, 6))
                Line((-7.5, 0), (-11, 7))
            make_face()
            with BuildLine():
                Line((-7.397127154, 0.3532713023), (-10.5568370365, 6.6726910673))
                Line((-10.5568370365, 6.6726910673), (-5.25, 5.7882182279))
                Line((-5.25, 5.7882182279), (-5.25, 1.6415475947))
                Line((-7.397127154, 0.3532713023), (-5.25, 1.6415475947))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.2800117739, perimeter: 49.7400941908
            with BuildLine():
                Line((-5, 1.5), (3.5, 1.5))
                Line((3.5, 5), (3.5, 1.5))
                Line((-4, 5), (3.5, 5))
                Line((-5, 1.5), (-4, 5))
            make_face()
            with BuildLine():
                Line((0, 4.75), (3.25, 4.75))
                Line((3.25, 4.75), (3.25, 1.75))
                Line((0, 1.75), (3.25, 1.75))
                Line((0, 4.75), (0, 1.75))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.8114246468, 4.75), (-0.25, 4.75))
                Line((-0.25, 4.75), (-0.25, 1.75))
                Line((-4.668567504, 1.75), (-0.25, 1.75))
                Line((-4.668567504, 1.75), (-3.8114246468, 4.75))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5, 0)):
                Circle(0.25)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_64383_e298386f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 392.9867228627, perimeter: 267.9911485751
            with BuildLine():
                Line((0, 5), (0, 52))
                CenterArc((5, 5), 5, 180, 90)
                Line((31, 0), (5, 0))
                CenterArc((31, 5), 5, -90, 90)
                Line((36, 52), (36, 5))
                Line((33, 52), (36, 52))
                Line((33, 5), (33, 52))
                CenterArc((31, 5), 2, -90, 90)
                Line((5, 3), (31, 3))
                CenterArc((5, 5), 2, 180, 90)
                Line((3, 52), (3, 5))
                Line((0, 52), (3, 52))
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((14, -18)):
                Circle(3.75)
        # OneSide extrude, distance=32.5
        extrude(amount=32.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 42.0619599741, perimeter: 49.9911485751
            with BuildLine():
                CenterArc((14, 38), 14, 90, 90)
                Line((14, 52), (0, 52))
                Line((0, 38), (0, 52))
            make_face()
            # Profile area: 42.0619599741, perimeter: 49.9911485751
            with BuildLine():
                CenterArc((14, 38), 14, 0, 90)
                Line((28, 38), (28, 52))
                Line((14, 52), (28, 52))
            make_face()
            # Profile area: 15.8220999521, perimeter: 14.1005805517
            with Locations((14, 38)):
                Circle(2.2441770953)
        # OneSide extrude, distance=-47.5
        extrude(amount=-47.5, mode=Mode.SUBTRACT)
    return part.part


def model_64386_2e79ddd8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 21 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 391.7734457254, perimeter: 267.1822971503
            with BuildLine():
                CenterArc((-16.75, 5), 5, 180, 90)
                Line((16.75, 0), (-16.75, 0))
                CenterArc((16.75, 5), 5, -90, 90)
                Line((21.75, 18.8), (21.75, 5))
                CenterArc((23.75, 18.8), 2, 90, 90)
                Line((47.5, 20.8), (23.75, 20.8))
                Line((47.5, 23.8), (47.5, 20.8))
                Line((23.75, 23.8), (47.5, 23.8))
                CenterArc((23.75, 18.8), 5, 90, 90)
                Line((18.75, 5), (18.75, 18.8))
                CenterArc((16.75, 5), 2, -90, 90)
                Line((-16.75, 3), (16.75, 3))
                CenterArc((-16.75, 5), 2, 180, 90)
                Line((-18.75, 5), (-18.75, 18.8))
                CenterArc((-23.75, 18.8), 5, 0, 90)
                Line((-23.75, 23.8), (-47.5, 23.8))
                Line((-47.5, 23.8), (-47.5, 20.8))
                Line((-47.5, 20.8), (-23.75, 20.8))
                CenterArc((-23.75, 18.8), 2, 0, 90)
                Line((-21.75, 18.8), (-21.75, 5))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 23.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-15, -35.625)):
                Circle(2.5)
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((-15, 0)):
                Circle(3.75)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-15, 35.625)):
                Circle(2.5)
        # OneSide extrude, distance=-57.5
        extrude(amount=-57.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 157.0796326795, perimeter: 125.6637061436
            with BuildLine():
                CenterArc((-15, 0), 11.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-15, 0), 8.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)
    return part.part


def model_64675_42df5e14_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 83.1903753028, perimeter: 52.6493372018
            with BuildLine():
                CenterArc((-5.235667632, 4.5283626914), 3.0830969177, -112.6687207388, 157.8332816295)
                Line((-6.4239004208, 1.6834392401), (-1.0139683499, -3.0072676247))
                CenterArc((0.9513254469, -0.7406356977), 3, -130.9270761138, 101.608728013)
                Line((3.5670629782, -2.2096207784), (9.0834927503, 7.6131695167))
                CenterArc((5.8974823512, 9.4024169801), 3.6540482685, 166.8679584043, 163.8136934949)
                Line((0.4316722241, 5.2245927569), (2.3389908634, 10.2326019473))
                CenterArc((-0.502846198, 5.5805075201), 1, -134.8354391093, 113.9859205907)
                Line((-3.0618593458, 6.7146938966), (-1.2079191633, 4.8713727561))
            make_face()
            # Profile area: 41.925087073, perimeter: 22.9560885553
            with BuildLine():
                CenterArc((5.8974823512, 9.4024169801), 3.6540482685, 166.8679584043, 163.8136934949)
                CenterArc((5.8974823512, 9.4024169801), 3.6540482685, -29.3183481008, 180.7513526593)
                Line((2.3389908634, 10.2326019473), (2.6882831276, 11.1497318034))
            make_face()
            # Profile area: 29.8623668835, perimeter: 19.3716692538
            with BuildLine():
                CenterArc((-5.235667632, 4.5283626914), 3.0830969177, 45.1645608907, 202.1667183705)
                CenterArc((-5.235667632, 4.5283626914), 3.0830969177, -112.6687207388, 157.8332816295)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9878618502, perimeter: 10.0189037537
            with Locations((5.235667632, -4.5283626914)):
                Circle(1.5945580568)
            # Profile area: 10.1583627509, perimeter: 11.2983959553
            with Locations((-0.9513254469, 0.7406356977)):
                Circle(1.7981955653)
            # Profile area: 14.963035234, perimeter: 13.7124412949
            with Locations((-5.8974823512, -9.4024169801)):
                Circle(2.1824028139)
        # OneSide extrude, distance=-21
        extrude(amount=-21, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.7184103227, perimeter: 110.9416086655
            with BuildLine():
                Line((1.2079191633, -4.8713727561), (3.0618593458, -6.7146938966))
                CenterArc((5.235667632, -4.5283626914), 3.0830969177, -134.8354391093, 202.1667183705)
                Line((6.4239004208, -1.6834392401), (1.0139683499, 3.0072676247))
                CenterArc((-0.9513254469, 0.7406356977), 3, 49.0729238862, 101.608728013)
                Line((-3.5670629782, 2.2096207784), (-9.0834927503, -7.6131695167))
                CenterArc((-5.8974823512, -9.4024169801), 3.6540482685, 150.6816518992, 180.7513526593)
                Line((-2.6882831276, -11.1497318034), (-0.4316722241, -5.2245927569))
                CenterArc((0.502846198, -5.5805075201), 1, 45.1645608907, 113.9859205907)
            make_face()
            with BuildLine():
                CenterArc((0.502846198, -5.5805075201), 1.517721513, 45.1645608907, 113.9859205907)
                Line((-3.1591979974, -10.9315815607), (-0.9154925156, -5.0403280272))
                CenterArc((-5.8974823512, -9.4024169801), 3.1363267555, 150.6816518992, 180.137656911)
                Line((-3.1156551141, 1.9561123855), (-8.6320848862, -7.8666779095))
                CenterArc((-0.9513254469, 0.7406356977), 2.482278487, 49.0729238862, 101.608728013)
                Line((6.1505690559, -2.1316761554), (0.6748100573, 2.6161062544))
                CenterArc((5.235667632, -4.5283626914), 2.5653754047, -134.8354391093, 203.9417855264)
                Line((1.5729506057, -4.5042384331), (3.4268907882, -6.3475595736))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_65326_373e91b3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 200, perimeter: 60
            with BuildLine():
                Line((20, -10), (0, -10))
                Line((20, 0), (20, -10))
                Line((0, 0), (20, 0))
                Line((0, -10), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-5, 3.5)):
                Circle(2.5)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -10, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((5, 3.5)):
                Circle(2.5)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


def model_65343_ce99dbac_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.3994418676, perimeter: 40.6263156132
            with BuildLine():
                Line((9.5285248953, -0.0269414346), (-7.5, -1))
                CenterArc((9.5, 0.4722442327), 0.5, -86.7295120768, 86.7295120768)
                Line((10, 2), (10, 0.4722442327))
                CenterArc((9.5, 2), 0.5, 0, 90)
                Line((-7.5, 2.5), (9.5, 2.5))
                Line((-7.5, -1), (-7.5, 2.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18, perimeter: 32.5663706144
            with BuildLine():
                CenterArc((-14, -2), 1, 180, 90)
                Line((-14, -3), (-11, -3))
                CenterArc((-11, -2), 1, -90, 90)
                Line((-10, -2), (-10, 2))
                CenterArc((-11, 2), 1, 0, 90)
                Line((-11, 3), (-14, 3))
                CenterArc((-14, 2), 1, 90, 90)
                Line((-15, 2), (-15, -2))
            make_face()
            with BuildLine():
                Line((-12, 2), (-13, 2))
                CenterArc((-12, 1), 1, 0, 90)
                Line((-11, -1), (-11, 1))
                CenterArc((-12, -1), 1, -90, 90)
                Line((-13, -2), (-12, -2))
                CenterArc((-13, -1), 1, 180, 90)
                Line((-14, 1), (-14, -1))
                CenterArc((-13, 1), 1, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1611760396, perimeter: 7.9884162385
            with BuildLine():
                Line((-17.0427967866, 1.1505473503), (-17.95, 1.1505473503))
                CenterArc((-17.95, 0.9005473503), 0.25, 90, 90)
                Line((-18.2, 0.9005473503), (-18.2, -0.75))
                CenterArc((-17.95, -0.75), 0.25, -180, 90)
                Line((-17.95, -1), (-17.0427967866, -1.0000000149))
                Line((-17.0427967866, -0.6843338631), (-17.0427967866, -1.0000000149))
                Line((-17.6938561713, -0.6843338631), (-17.0427967866, -0.6843338631))
                CenterArc((-17.6938561713, -0.4343338631), 0.25, -180, 90)
                Line((-17.9438561713, 0.5388701167), (-17.9438561713, -0.4343338631))
                CenterArc((-17.6938561713, 0.5388701167), 0.25, 90, 90)
                Line((-17.0427967866, 0.7888701167), (-17.6938561713, 0.7888701167))
                Line((-17.0427967866, 1.1505473503), (-17.0427967866, 0.7888701167))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


def model_65569_bd890a32_0002():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3474.6979723542, perimeter: 231.2622527765
            with BuildLine():
                CenterArc((45, -64.9231631203), 5, -90, 90)
                Line((50, -5), (50, -64.9231631203))
                CenterArc((45, -5), 5, 0, 90)
                Line((5, 0), (45, 0))
                CenterArc((5, -5), 5, 90, 90)
                Line((0, -64.9231631203), (0, -5))
                CenterArc((5, -64.9231631203), 5, 180, 90)
                Line((45, -69.9231631203), (5, -69.9231631203))
            make_face()
        # OneSide extrude, distance=23
        extrude(amount=23)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 23, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 178.5435506071, perimeter: 396.7634457935
            with BuildLine():
                CenterArc((-42.5, 62.4231631203), 3.4, 90, 90)
                Line((-45.9, 62.4231631203), (-45.9, 7.5))
                CenterArc((-42.5, 7.5), 3.4, 180, 90)
                Line((-42.5, 4.1), (-7.5, 4.1))
                CenterArc((-7.5, 7.5), 3.4, -90, 90)
                Line((-4.1, 7.5), (-4.1, 62.4231631203))
                CenterArc((-7.5, 62.4231631203), 3.4, 0, 90)
                Line((-7.5, 65.8231631203), (-42.5, 65.8231631203))
            make_face()
            with BuildLine():
                Line((-45, 62.4231631203), (-45, 7.5))
                CenterArc((-42.5, 62.4231631203), 2.5, 90, 90)
                Line((-7.5, 64.9231631203), (-42.5, 64.9231631203))
                CenterArc((-7.5, 62.4231631203), 2.5, 0, 90)
                Line((-5, 7.5), (-5, 62.4231631203))
                CenterArc((-7.5, 7.5), 2.5, -90, 90)
                Line((-42.5, 5), (-7.5, 5))
                CenterArc((-42.5, 7.5), 2.5, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69.9231631203), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 17, perimeter: 36
            with BuildLine():
                Line((34, 14), (17, 14))
                Line((34, 15), (34, 14))
                Line((17, 15), (34, 15))
                Line((17, 14), (17, 15))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_65808_662bbe75_0011():
    """Model: wm v10"""
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
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27, perimeter: 24
            with BuildLine():
                Line((6.5, 1), (-2.5, 1))
                Line((-2.5, 1), (-2.5, -2))
                Line((-2.5, -2), (6.5, -2))
                Line((6.5, -2), (6.5, 1))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.4600001627, perimeter: 9.4000001401
            with BuildLine():
                Line((0.8000000119, 0.200000003), (-1.8000000268, 0.200000003))
                Line((0.8000000119, 2.3000000343), (0.8000000119, 0.200000003))
                Line((-1.8000000268, 2.3000000343), (0.8000000119, 2.3000000343))
                Line((-1.8000000268, 0.200000003), (-1.8000000268, 2.3000000343))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6674284978, perimeter: 5.7395294279
            with BuildLine():
                _nurbs_edge([(-1.8142818373, 0), (-1.8149773066, 0.0007924948), (-1.820849269, 0.0078304476), (-1.8342921109, 0.0291560047), (-1.8606857302, 0.0828727085), (-1.9083610945, 0.1972826811), (-1.9846183318, 0.4006201369), (-2.0765714763, 0.6628246165), (-2.1781797623, 0.9702248304), (-2.2801122386, 1.3007315275), (-2.3663334224, 1.6160039787), (-2.4301860096, 1.8936769397), (-2.47093964, 2.1217493922), (-2.4916141964, 2.2916422269), (-2.4978836059, 2.3874663518), (-2.4995150645, 2.4385228871), (-2.4999113679, 2.4637782528), (-2.5, 2.473824899)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0574310382, 0.0574310382, 0.0574310382, 0.0574310382, 0.0574310382, 0.0574310382, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8578180917, 0.8578180917, 0.8578180917, 0.8578180917, 0.8578180917, 0.8578180917], 5)
                Line((-2.5, 2.473824899), (-2.5, 0))
                Line((-2.5, 0), (-1.8142818373, 0))
            make_face()
        # OneSide extrude, distance=-5.4
        extrude(amount=-5.4, mode=Mode.SUBTRACT)
    return part.part


def model_66243_bf31a991_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.04, perimeter: 45.4627416998
            with BuildLine():
                Line((0, 0), (14.4, 0))
                Line((14.4, 0), (14.4, 5.2))
                Line((14.4, 5.2), (12.2, 5.2))
                Line((12.2, 5.2), (12.2, 1.6))
                Line((2.6, 1.6), (12.2, 1.6))
                Line((2.6, 5.2), (2.6, 1.6))
                Line((1.6, 5.2), (2.6, 5.2))
                Line((0, 3.6), (1.6, 5.2))
                Line((0, 0), (0, 3.6))
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.7306139655, perimeter: 11.9353745225
            with BuildLine():
                Line((5.2, 3.2), (5.2, 6.4))
                Line((5.2, 6.4), (1.6, 6.4))
                Line((1.6, 6.2192354826), (1.6, 6.4))
                CenterArc((1.8, 6.2192354826), 0.2, -180, 61.6048843988)
                Line((1.7048901563, 6.0432976594), (4.3608787493, 4.6075025857))
                CenterArc((3.6, 3.2), 1.6, 0, 61.6048843988)
            make_face()
            # Profile area: 4.7306139655, perimeter: 11.9353745225
            with BuildLine():
                Line((1.6, 0), (5.2, 0))
                Line((5.2, 0), (5.2, 3.2))
                CenterArc((3.6, 3.2), 1.6, -61.6048843988, 61.6048843988)
                Line((1.7048901563, 0.3567023406), (4.3608787493, 1.7924974143))
                CenterArc((1.8, 0.1807645174), 0.2, 118.3951156012, 61.6048843988)
                Line((1.6, 0), (1.6, 0.1807645174))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((3.6, 3.2)):
                Circle(0.8)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.68, perimeter: 9.6
            with BuildLine():
                Line((0, 4.8), (0, 1.6))
                Line((0.7, 1.6), (0, 1.6))
                Line((0.7, 2.4), (0.7, 1.6))
                Line((0.7, 2.4), (1.6, 2.4))
                Line((1.6, 2.4), (1.6, 4))
                Line((0.7, 4), (1.6, 4))
                Line((0.7, 4.8), (0.7, 4))
                Line((0, 4.8), (0.7, 4.8))
            make_face()
        # OneSide extrude, distance=-17
        extrude(amount=-17, mode=Mode.SUBTRACT)
    return part.part


def model_67221_275ba7e6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458325, perimeter: 4.7123889336
            with Locations((-1.0000000075, -1.7500000075)):
                Circle(0.7499999925)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)

        # Sketch10 -> Extrude12 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 3)):
                Circle(0.5)
        # OneSide extrude, distance=-4
        extrude(amount=-4)
    return part.part


def model_67262_d9978c87_0001():
    """Model: SCREW"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4813705343, perimeter: 7.1314153236
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.48
        extrude(amount=1.48, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3067961576, perimeter: 1.9634954085
            Circle(0.3125)
        # OneSide extrude, distance=0.72
        extrude(amount=0.72, mode=Mode.ADD)
    return part.part


def model_67403_bb0225a8_0000():
    """Model: -DRIVER"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5121460184, perimeter: 3.9707963268
            with BuildLine():
                CenterArc((5.2, 5.9), 0.2, 90, 90)
                Line((5, 5.7), (5, 5.9))
                CenterArc((5.2, 5.7), 0.2, -180, 90)
                Line((5.2, 5.5), (6, 5.5))
                Line((6, 6.1), (6, 5.5))
                Line((5.2, 6.1), (6, 6.1))
            make_face()
            with BuildLine():
                CenterArc((5.3307834527, 5.7972174614), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((5.8, 0.15), 0.15, 90.000002192, 179.9999956161)
                CenterArc((5.8, 0.15), 0.15, -90.000002192, 180.0000043839)
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(12.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0206255184, perimeter: 0.6521305314
            with BuildLine():
                CenterArc((5.8, 0.15), 0.15, 19.4712215401, 141.0575569199)
                Line((5.6585786446, 0.2000000022), (5.9414213554, 0.2000000022))
            make_face()
            # Profile area: 0.0206255197, perimeter: 0.652130544
            with BuildLine():
                CenterArc((5.8, 0.15), 0.15, -160.5287802711, 141.0575605421)
                Line((5.658578643, 0.1000000022), (5.941421357, 0.1000000022))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_67403_bb0225a8_0005():
    """Model: Component13"""
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
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6696917297, perimeter: 15.2096386647
            with BuildLine():
                _nurbs_edge([(0.1972566189, 5.8588332657), (0.2280977558, 5.8677533453), (0.2920754874, 5.8850725069), (0.3949284882, 5.9094882511), (0.5458633113, 5.9389109665), (0.7574120417, 5.9704747261), (0.9912348012, 5.996896515), (1.2459306418, 6.0183645185), (1.5189581445, 6.0352376427), (1.8063586722, 6.0480879897), (2.1022728096, 6.0577813176), (2.3994199685, 6.0653800618), (2.6899912067, 6.071969855), (2.9664118707, 6.078510529), (3.2221418344, 6.085678669), (3.4525089563, 6.0937072494), (3.6554503207, 6.1022345486), (3.8325442316, 6.1101177361), (3.989237514, 6.1153414057), (4.1325996597, 6.115245123), (4.2694483536, 6.1066785047), (4.4044848634, 6.0862103983), (4.5380299558, 6.0502401076), (4.6666149093, 5.9957092138), (4.7843973114, 5.9210462291), (4.8842495253, 5.8269338309), (4.959048292, 5.7174499273), (5.0022438873, 5.5988395922), (5.0082795788, 5.4778533776), (4.9731324787, 5.3601189907), (4.8946506916, 5.2488548127), (4.7964762272, 5.166303428), (4.7028799175, 5.1082436909), (4.6316245778, 5.0712476211), (4.5937824755, 5.05317715)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(4.5937824755, 5.05317715), (4.6228624041, 5.0834795031), (4.6747054411, 5.1423913326), (4.7335195907, 5.2256804571), (4.7740124722, 5.3265686792), (4.7624742561, 5.4358866236), (4.6921902434, 5.5289201929), (4.5701878878, 5.606739518), (4.4083195474, 5.6711676273), (4.2209262014, 5.7242887166), (4.0226175357, 5.7679819255), (3.825934356, 5.8034241117), (3.6392331415, 5.830653534), (3.464045119, 5.8479875149), (3.2939372284, 5.8518598145), (3.1192028229, 5.838288954), (2.9306218895, 5.8040857187), (2.7236468528, 5.7481859566), (2.5022728843, 5.6728860818), (2.2834054475, 5.5852458823), (2.1000954452, 5.4981066497), (1.9900102264, 5.426071741), (1.9842157874, 5.3815897591), (2.0969298354, 5.3713799695), (2.3120474279, 5.3917293724), (2.5891240166, 5.4305919921), (2.8756997211, 5.4719088422), (3.1172031415, 5.4990742783), (3.2684471685, 5.4989776144), (3.3030786697, 5.4652870353), (3.2273334743, 5.403343081), (3.0797768106, 5.3297901223), (2.9099834241, 5.2642356678), (2.763622913, 5.2234064029), (2.662129276, 5.2130546203), (2.5934132135, 5.2246330205), (2.5303753439, 5.2439921073), (2.4460218723, 5.2587451711), (2.3256463778, 5.2639192228), (2.1628930701, 5.2592366891), (1.958809802, 5.2479121918), (1.7197641392, 5.234915973), (1.4557865541, 5.2253328469), (1.1789831286, 5.2231202278), (0.9028775196, 5.2314292927), (0.6415709408, 5.2526359056), (0.4089733599, 5.2884845416), (0.2180140315, 5.3401814983), (0.0798349688, 5.4085084965), (0.0030409848, 5.4939244745), (-0.0072277039, 5.59667448), (0.0397266357, 5.6928193686), (0.1063038934, 5.7727762224), (0.1646175525, 5.8295666145), (0.1972566189, 5.8588332657)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((0.400000006, 5.6000000834), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3885253123, perimeter: 9.5593187818
            with BuildLine():
                Line((2.2099139191, 8.7428963961), (3.7972721599, 8.1517481297))
                Line((3.7972721599, 8.1517481297), (3.2816763382, 9.0650078793))
                Line((3.2816763382, 9.0650078793), (-0.0088688245, 8.7676100471))
                Line((-0.0088688245, 8.7676100471), (0.200000003, 8.3000001237))
                Line((0.200000003, 8.3000001237), (2.2099139191, 8.7428963961))
            make_face()
            with BuildLine():
                CenterArc((0.3338319281, 8.5645883445), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_67403_bb0225a8_0010():
    """Model: Component25"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4942286794, perimeter: 3.8967650745
            with BuildLine():
                CenterArc((2.7940952588, 2.8), 0.3, 90, 180)
                Line((2.7940952588, 2.5), (3.5, 2.5))
                Line((3.5, 2.5), (3.5, 3.1))
                Line((3.5, 3.1), (2.7940952588, 3.1))
            make_face()
            with BuildLine():
                CenterArc((2.7940952588, 2.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0260999986, perimeter: 0.7599999785
            with BuildLine():
                Line((2.9399999332, 0.1599999964), (2.6499999419, 0.1599999964))
                Line((2.9399999332, 0.2499999944), (2.9399999332, 0.1599999964))
                Line((2.6499999419, 0.2499999944), (2.9399999332, 0.2499999944))
                Line((2.6499999419, 0.1599999964), (2.6499999419, 0.2499999944))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0260999986, perimeter: 0.7599999785
            with BuildLine():
                Line((2.9399999332, 0.1599999964), (2.6499999419, 0.1599999964))
                Line((2.9399999332, 0.2499999944), (2.9399999332, 0.1599999964))
                Line((2.6499999419, 0.2499999944), (2.9399999332, 0.2499999944))
                Line((2.6499999419, 0.1599999964), (2.6499999419, 0.2499999944))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_68475_17ef1725_0000():
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
        # Sketch7 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 46.0901194575, perimeter: 27.8669030648
            with BuildLine():
                Line((-13, 2), (-13, -2))
                Line((-13, -2), (-7.5151979032, -2.7815854213))
                Line((-7.5151979032, -2.7815854213), (-3.9499962397, -2.8273547475))
                Line((-3.9499962397, -2.8273547475), (-3.9970130167, 0.0602131082))
                Line((-3.9499962397, 2.8273547475), (-3.9970130167, 0.0602131082))
                Line((-7.5151979032, 2.7815854213), (-3.9499962397, 2.8273547475))
                Line((-13, 2), (-7.5151979032, 2.7815854213))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch9 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.2882708017, perimeter: 14.6152703803
            with BuildLine():
                Line((70.5, 2.5), (67, 2.5))
                Line((70.5, 7), (70.5, 2.5))
                Line((69, 7), (70.5, 7))
                _nurbs_edge([(67, 3.5), (67.0211605959, 3.5187194097), (67.0640912169, 3.5573238873), (67.1303154854, 3.6187275821), (67.222285679, 3.7076216427), (67.3433140227, 3.8305874753), (67.4700850299, 3.9655383665), (67.6018421808, 4.1125187357), (67.7371611268, 4.2713738549), (67.8740886024, 4.4417057626), (68.0103716584, 4.6228409249), (68.1436546462, 4.8137703049), (68.271672872, 5.0130994002), (68.3924849946, 5.218937226), (68.5045756909, 5.4289343015), (68.6067668469, 5.6405443023), (68.6981878806, 5.8512194312), (68.7782401102, 6.058637459), (68.8465753959, 6.2608985735), (68.9030982813, 6.4567950883), (68.9478846213, 6.6457025284), (68.9744444324, 6.7910426472), (68.9892161431, 6.8967850575), (68.9967851765, 6.9658357276), (69, 7)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((67, 2.5), (67, 3.5))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_69488_f2085c68_0006():
    """Model: Puertas/Marcos"""
    with BuildPart() as part:
        # Sketch7 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10830.8885422414), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1350, perimeter: 1354
            with BuildLine():
                Line((2355.6564902908, 273), (2480.6564902908, 273))
                Line((2480.6564902908, 273), (2480.6564902908, 0))
                Line((2480.6564902908, 0), (2482.6564902908, 0))
                Line((2482.6564902908, 275), (2482.6564902908, 0))
                Line((2353.6564902908, 275), (2482.6564902908, 275))
                Line((2353.6564902908, 0), (2353.6564902908, 275))
                Line((2353.6564902908, 0), (2355.6564902908, 0))
                Line((2355.6564902908, 0), (2355.6564902908, 273))
            make_face()
            # Profile area: 2748, perimeter: 1382
            with BuildLine():
                Line((2482.6564902908, 0), (2486.6564902908, 0))
                Line((2486.6564902908, 279), (2486.6564902908, 0))
                Line((2349.6564902908, 279), (2486.6564902908, 279))
                Line((2349.6564902908, 0), (2349.6564902908, 279))
                Line((2349.6564902908, 0), (2353.6564902908, 0))
                Line((2353.6564902908, 0), (2353.6564902908, 275))
                Line((2353.6564902908, 275), (2482.6564902908, 275))
                Line((2482.6564902908, 275), (2482.6564902908, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch7 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10830.8885422414), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1350, perimeter: 1354
            with BuildLine():
                Line((2355.6564902908, 273), (2480.6564902908, 273))
                Line((2480.6564902908, 273), (2480.6564902908, 0))
                Line((2480.6564902908, 0), (2482.6564902908, 0))
                Line((2482.6564902908, 275), (2482.6564902908, 0))
                Line((2353.6564902908, 275), (2482.6564902908, 275))
                Line((2353.6564902908, 0), (2353.6564902908, 275))
                Line((2353.6564902908, 0), (2355.6564902908, 0))
                Line((2355.6564902908, 0), (2355.6564902908, 273))
            make_face()
        # OneSide extrude, distance=-24
        extrude(amount=-24, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -10854.8885422414), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2748, perimeter: 1382
            with BuildLine():
                Line((-2349.6564902908, 279), (-2486.6564902908, 279))
                Line((-2486.6564902908, 279), (-2486.6564902908, 0))
                Line((-2482.6564902908, 0), (-2486.6564902908, 0))
                Line((-2482.6564902908, 275), (-2482.6564902908, 0))
                Line((-2353.6564902908, 275), (-2482.6564902908, 275))
                Line((-2353.6564902908, 0), (-2353.6564902908, 275))
                Line((-2349.6564902908, 0), (-2353.6564902908, 0))
                Line((-2349.6564902908, 0), (-2349.6564902908, 279))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10829.3885422414), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 33856.92, perimeter: 793.6
            with BuildLine():
                Line((2356.0564902908, 0), (2480.2564902908, 0))
                Line((2480.2564902908, 272.6), (2480.2564902908, 0))
                Line((2356.0564902908, 272.6), (2480.2564902908, 272.6))
                Line((2356.0564902908, 0), (2356.0564902908, 272.6))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7)
    return part.part


def model_69649_70b07cac_0000():
    """Model: table"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 706.8583470577, perimeter: 94.2477796077
            Circle(15)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_70008_fa163f57_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 26, perimeter: 21
            with BuildLine():
                Line((2.5, -2), (-4, -2))
                Line((2.5, 2), (2.5, -2))
                Line((-4, 2), (2.5, 2))
                Line((-4, -2), (-4, 2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 22.2017589695, perimeter: 24
            with BuildLine():
                Line((-3.5, -0.1591667508), (-3.5, -2))
                Line((-3.5, -2), (-1, -2))
                Line((-1, -1.5), (-1, -2))
                Line((1.5, -1.5), (-1, -1.5))
                Line((1.5, -2), (1.5, -1.5))
                Line((1.5, -2), (2.5, -2))
                Line((2.5, -2), (2.5, 0))
                Line((2, 0), (2.5, 0))
                Line((2, 1.2556488118), (2, 0))
                Line((2.5, 1.2556488118), (2, 1.2556488118))
                Line((2.5, 1.2556488118), (2.5, 2))
                Line((2.5, 2), (0.5, 2))
                Line((0.5, 2), (0.5, 1.5))
                Line((0.5, 1.5), (-1.5, 1.5))
                Line((-1.5, 1.5), (-1.5, 2))
                Line((-1.5, 2), (-4, 2))
                Line((-4, 2), (-4, -0.1591667508))
                Line((-4, -0.1591667508), (-3.5, -0.1591667508))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5, 1)):
                Circle(0.25)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_70321_eccffc7e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.5481105956, perimeter: 26.5238240935
            with BuildLine():
                Line((2.5, 4), (2.5, 0))
                Line((1.5, 4), (2.5, 4))
                Line((1.5, 1), (1.5, 4))
                Line((-1.2070669218, 1), (1.5, 1))
                Line((-1.2070669218, 3.1659103442), (-1.2070669218, 1))
                Line((-2, 4), (-1.2070669218, 3.1659103442))
                Line((-4, 4), (-2, 4))
                Line((-4, 0), (-4, 4))
                Line((2.5, 0), (-4, 0))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.5, perimeter: 13
            with BuildLine():
                Line((-1, 6.5), (-1, 4.5))
                Line((0, 6.5), (-1, 6.5))
                Line((0, 7.5), (0, 6.5))
                Line((-3.5, 7.5), (0, 7.5))
                Line((-3.5, 6.5), (-3.5, 7.5))
                Line((-2, 6.5), (-3.5, 6.5))
                Line((-2, 4.5), (-2, 6.5))
                Line((-1, 4.5), (-2, 4.5))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_71855_15b7cfef_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3449155782, perimeter: 2.1613682138
            with Locations((-3.5837454816, -1.248546352)):
                Ellipse(0.4151442214, 0.2644624031, rotation=122.905242923)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3794044468, perimeter: 2.3649694216
            with Locations((3.2951201191, -1.1814620857)):
                Ellipse(0.4845719194, 0.2492265471, rotation=-158.1985905136)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)
    return part.part


def model_72824_38a3b7ba_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30, perimeter: 26
            with BuildLine():
                Line((10, -3), (0, -3))
                Line((10, 0), (10, -3))
                Line((0, 0), (10, 0))
                Line((0, -3), (0, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 33 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.8781992624, perimeter: 9.7326153163
            with BuildLine():
                Line((0, 2.4), (0, 2))
                Line((-2.4, 2.4), (0, 2.4))
                Line((-3, 2.4), (-2.4, 2.4))
                Line((-3, 0), (-3, 2.4))
                Line((-2, 0), (-3, 0))
                Line((-0.3218007376, 2), (-2, 0))
                Line((-0.3218007376, 2), (0, 2))
            make_face()
            # Profile area: 4.8781992027, perimeter: 9.7326153163
            with BuildLine():
                Line((-2.0000000298, 6), (-3, 6))
                Line((-3, 6), (-3, 3.6))
                Line((-3, 3.6), (-2.4, 3.6))
                Line((-2.4, 3.6), (0, 3.6))
                Line((0, 3.6), (0, 4))
                Line((0, 4), (-0.3218007674, 4))
                Line((-2.0000000298, 6), (-0.3218007674, 4))
            make_face()
            # Profile area: 2.88, perimeter: 7.2
            with BuildLine():
                Line((-2.4, 2.4), (0, 2.4))
                Line((0, 3.6), (0, 2.4))
                Line((-2.4, 3.6), (0, 3.6))
                Line((-2.4, 3.6), (-2.4, 2.4))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 33 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.72, perimeter: 3.6
            with BuildLine():
                Line((3, 3.6), (2.4, 3.6))
                Line((2.4, 3.6), (2.4, 2.4))
                Line((2.4, 2.4), (3, 2.4))
                Line((3, 2.4), (3, 3.6))
            make_face()
        # OneSide extrude, distance=-14.5
        extrude(amount=-14.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 33 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.3218007973, perimeter: 6.9326153759
            with BuildLine():
                Line((0, 4), (0.3218007674, 4))
                Line((2.0000000298, 6), (0.3218007674, 4))
                Line((2.0000000298, 6), (0, 6))
                Line((0, 6), (0, 4))
            make_face()
        # OneSide extrude, distance=-17.5
        extrude(amount=-17.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 33 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.3218007376, perimeter: 6.9326153163
            with BuildLine():
                Line((0.3218007376, 2), (2, 0))
                Line((0.3218007376, 2), (0, 2))
                Line((0, 2), (0, 0))
                Line((0, 0), (2, 0))
            make_face()
        # OneSide extrude, distance=-16
        extrude(amount=-16, mode=Mode.SUBTRACT)
    return part.part


def model_73294_550ba932_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Paredes -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20700, perimeter: 2790
            with BuildLine():
                Line((-300, 165), (15, 165))
                Line((-300, 165), (-300, 150))
                Line((-300, 150), (0, 150))
                Line((0, 150), (0, -300))
                Line((0, -300), (-600, -300))
                Line((-600, -300), (-600, -315))
                Line((15, -315), (-600, -315))
                Line((15, 165), (15, -315))
            make_face()
        # OneSide extrude, distance=250
        extrude(amount=250)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 27000, perimeter: 740
            with BuildLine():
                Line((240, 125), (-30, 125))
                Line((240, 225), (240, 125))
                Line((-30, 225), (240, 225))
                Line((-30, 125), (-30, 225))
            make_face()
        # OneSide extrude, distance=-100
        extrude(amount=-100, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2323.9996413142, perimeter: 206.3999883026
            with BuildLine():
                Line((-300, 92.5000013784), (-266.8000044703, 92.5000013784))
                Line((-266.8000044703, 92.5000013784), (-266.8000044703, 162.5))
                Line((-266.8000044703, 162.5), (-300, 162.5))
                Line((-300, 162.5), (-300, 92.5000013784))
            make_face()
        # OneSide extrude, distance=35
        extrude(amount=35)
    return part.part


def model_73388_10a40b49_0030():
    """Model: Bottom_Bolt_Short"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7542963961, perimeter: 3.0787608005
            Circle(0.49)
        # OneSide extrude, distance=0.48
        extrude(amount=0.48)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.101787602, perimeter: 1.1309733553
            Circle(0.18)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.48), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3119308756, perimeter: 2.079
            with BuildLine():
                Line((-0.3000778024, -0.17325), (-0.3000778024, 0.17325))
                Line((0, -0.3465), (-0.3000778024, -0.17325))
                Line((0.3000778024, -0.17325), (0, -0.3465))
                Line((0.3000778024, 0.17325), (0.3000778024, -0.17325))
                Line((0, 0.3465), (0.3000778024, 0.17325))
                Line((-0.3000778024, 0.17325), (0, 0.3465))
            make_face()
        # OneSide extrude, distance=-0.28
        extrude(amount=-0.28, mode=Mode.SUBTRACT)
    return part.part


def model_75646_4baf69b2_0014():
    """Model: ?? v3"""
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_75860_539df258_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180.6445979178, perimeter: 59.4761041673
            with BuildLine():
                CenterArc((0, -8.9), 3.8, 180, 180)
                Line((3.8, -8.9), (3.8, 8.9))
                CenterArc((0, 8.9), 3.8, 0, 180)
                Line((-3.8, 8.9), (-3.8, -8.9))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 136.925, perimeter: 47.9865007051
            with BuildLine():
                Line((0, 13.9), (-3.8, 13.9))
                Line((-3.8, 13.9), (-3.8, 0))
                Line((-3.8, 0), (8.9, 0))
                Line((8.9, 0), (8.9, 5))
                Line((8.9, 5), (0, 13.9))
            make_face()
        # Symmetric extrude, each_side=3.8
        extrude(amount=3.8, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.52, perimeter: 34.0499566724
            with BuildLine():
                Line((-2.6, 13.9), (8.9, 2.4))
                Line((8.9, 5), (8.9, 2.4))
                Line((0, 13.9), (8.9, 5))
                Line((-2.6, 13.9), (0, 13.9))
            make_face()
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_75966_08c4ab3e_0003():
    """Model: 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.8903761032, perimeter: 30.9698971518
            with BuildLine():
                Line((0, 5), (-0.0406866736, 4.9709380903))
                CenterArc((0.1046228749, 4.7675047225), 0.25, 125.537677792, 90)
                Line((-0.0988104929, 4.6221951741), (1.8537789751, 1.8885699188))
                CenterArc((3.0743791819, 2.7604272094), 1.5, -144.462322208, 54.462322208)
                Line((3.0743791819, 1.2604272094), (3.4609671955, 1.2604272094))
                CenterArc((3.4609671955, 0.2604272094), 1, -37.8749836511, 127.8749836511)
                Line((4.2503194128, -0.3535134041), (2.4306956324, -2.6930296932))
                CenterArc((2.8253717411, -3), 0.5, 142.1250163489, 127.8749836511)
                Line((2.8253717411, -3.5), (5.5, -3.5))
                CenterArc((5.5, -3), 0.5, -90, 90)
                Line((2.9089278722, -3), (6, -3))
                CenterArc((2.9089278722, -2.8), 0.2, 142.1250163489, 127.8749836511)
                Line((5.3723564281, 0.6930296932), (2.7510574288, -2.6772118773))
                CenterArc((4.9776803194, 1), 0.5, -37.8749836511, 127.8749836511)
                Line((3.2719268429, 1.5), (4.9776803194, 1.5))
                CenterArc((3.2719268429, 3), 1.5, -144.462322208, 54.462322208)
                Line((0, 5), (2.0513266361, 2.1281427094))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 48.2453815813, perimeter: 24.6225373465
            with Locations((-2.3696375239, -3.9993688801)):
                Circle(3.9187985302)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5912569374, perimeter: 4.4717249936
            with Locations((-2.3843624851, -4.0128349634)):
                Circle(0.7116971369)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)
    return part.part


def model_77194_49a0e425_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.407645922, perimeter: 39.2424140334
            with BuildLine():
                CenterArc((0, 0), 0.5, -106.3070054163, 180)
                Line((-1.9352856442, 1.0871316122), (0.1403920299, 0.4798854842))
                CenterArc((-1.8510504262, 1.3750629028), 0.3, 106.3038064535, 147.3891881302)
                Line((0.1403652366, 2.2701066781), (-1.9352695681, 1.6629988959))
                CenterArc((0, 2.75), 0.5, -73.6961935465, 180)
                Line((-0.1403652366, 3.2298933219), (-4.6162445032, 1.9207318407))
                CenterArc((-4.7004636451, 2.2086678338), 0.3, -106.3070054163, 32.6108118698)
                Line((-9.2596079701, 3.2298854842), (-4.7846988631, 1.9207365433))
                CenterArc((-9.4, 2.75), 0.5, 73.6929945837, 180)
                Line((-9.5403920299, 2.2701145158), (-7.4656881838, 1.6631532842))
                CenterArc((-7.5499234018, 1.3752219937), 0.3, -73.6961935465, 147.3891881302)
                Line((-7.4657042599, 1.0872860006), (-9.5423121827, 0.4798935885))
                CenterArc((-9.4019469462, 0.0000002666), 0.5, 106.3038064535, 180)
                Line((-4.7847293248, 0.8295530558), (-9.2615817096, -0.4798930552))
                CenterArc((-4.7005101829, 0.5416170627), 0.3, 73.6929945837, 32.6108118698)
                Line((-4.6162749649, 0.8295483532), (-0.1403920299, -0.4798854842))
            make_face()
            with BuildLine():
                CenterArc((-9.4019469462, 0.0000002666), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.4, 2.75), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 2.75), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.121863317, perimeter: 2.6485526469
            with BuildLine():
                Line((6.4000000954, -0.7752219937), (6.300501808, -0.7752219937))
                Line((6.300501808, -0.7752219937), (6.300501808, -2.0000000298))
                Line((6.300501808, -2.0000000298), (6.4000000954, -2.0000000298))
                Line((6.4000000954, -2.0000000298), (6.4000000954, -0.7752219937))
            make_face()
            # Profile area: 0.1231026096, perimeter: 2.6505763485
            with BuildLine():
                Line((3.0000000447, -2.0000000298), (3.0000000447, -0.7752219937))
                Line((3.1005101829, -2.0000000298), (3.0000000447, -2.0000000298))
                Line((3.1005101829, -0.7752219937), (3.1005101829, -2.0000000298))
                Line((3.0000000447, -0.7752219937), (3.1005101829, -0.7752219937))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2449556072, perimeter: 2.8495560721
            with BuildLine():
                Line((3.0000000447, -0.7752219937), (3.0000000447, -2.0000000298))
                Line((3.0000000447, -2.0000000298), (3.2000000447, -2.0000000298))
                Line((3.2000000447, -2.0000000298), (3.2000000447, -0.7752219937))
                Line((3.2000000447, -0.7752219937), (3.0000000447, -0.7752219937))
            make_face()
            # Profile area: 0.1230922902, perimeter: 2.6505594974
            with BuildLine():
                Line((6.2000000954, -0.7752219937), (6.300501808, -0.7752219937))
                Line((6.2000000954, -2.0000000298), (6.2000000954, -0.7752219937))
                Line((6.300501808, -2.0000000298), (6.2000000954, -2.0000000298))
                Line((6.300501808, -0.7752219937), (6.300501808, -2.0000000298))
            make_face()
            # Profile area: 0.121863317, perimeter: 2.6485526469
            with BuildLine():
                Line((6.300501808, -0.7752219937), (6.300501808, -2.0000000298))
                Line((6.4000000954, -2.0000000298), (6.300501808, -2.0000000298))
                Line((6.4000000954, -0.7752219937), (6.4000000954, -2.0000000298))
                Line((6.300501808, -0.7752219937), (6.4000000954, -0.7752219937))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_77211_d46ae17d_0013():
    """Model: piramide"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((0, 6), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 6))
                Line((6, 6), (0, 6))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9, perimeter: 15.7082039325
            with BuildLine():
                Line((3, 6), (0, 6))
                Line((0, 6), (0, 0))
                Line((0, 0), (3, 6))
            make_face()
            # Profile area: 9, perimeter: 15.7082039325
            with BuildLine():
                Line((3, 6), (6, 0))
                Line((6, 0), (6, 6))
                Line((6, 6), (3, 6))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9, perimeter: 15.7082039325
            with BuildLine():
                Line((3, 6), (0, 6))
                Line((0, 6), (0, 0))
                Line((0, 0), (3, 6))
            make_face()
            # Profile area: 9, perimeter: 15.7082039325
            with BuildLine():
                Line((3, 6), (6, 0))
                Line((6, 0), (6, 6))
                Line((6, 6), (3, 6))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)
    return part.part


def model_78513_7ad0bd6a_0004():
    """Model: flange"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 41.1057763768, perimeter: 42.5685804561
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.0066147231, 3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.6340701482, perimeter: 50.8938009882
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.15
        extrude(amount=1.15, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.45), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 23.1221219304, perimeter: 57.8053048261
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


def model_78603_4720dcb8_0005():
    """Model: Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0007068583, perimeter: 0.0942477796
            Circle(0.015)
        # OneSide extrude, distance=0.024
        extrude(amount=0.024)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0002552544, perimeter: 0.2042035225
            with BuildLine():
                CenterArc((0, 0), 0.0175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.0942477796
            Circle(0.015)
        # OneSide extrude, distance=0.002
        extrude(amount=0.002, mode=Mode.ADD)
    return part.part


def model_78767_404295e7_0005():
    """Model: 拉動銷 v1"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch2 -> 拉伸2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.9216811678, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch7 -> 拉伸6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.5, 0)):
                Circle(0.3)
        # OneSide extrude, distance=2.375
        extrude(amount=2.375, mode=Mode.SUBTRACT)
    return part.part


def model_78862_dcbc8940_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 409.8, perimeter: 279.2
            with BuildLine():
                Line((-9.5, 0), (-9.5, -3))
                Line((-9.5, -3), (16.25, -3))
                Line((16.25, -3), (16.25, -23.8))
                Line((16.25, -23.8), (59.75, -23.8))
                Line((59.75, -23.8), (59.75, -3))
                Line((59.75, -3), (85.5, -3))
                Line((85.5, 0), (85.5, -3))
                Line((56.75, 0), (85.5, 0))
                Line((56.75, -20.8), (56.75, 0))
                Line((19.25, -20.8), (56.75, -20.8))
                Line((19.25, 0), (19.25, -20.8))
                Line((-9.5, 0), (19.25, 0))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -20.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 157.0796326795, perimeter: 125.6637061436
            with BuildLine():
                CenterArc((-37.5, 15), 11.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-37.5, 15), 8.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=17
        extrude(amount=17, mode=Mode.ADD)
    return part.part


def model_78967_e53ff839_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 506.7359254479, perimeter: 291.5914572369
            with BuildLine():
                Line((3, 0.5), (3, 21.8))
                CenterArc((-2, 21.8), 5, 0, 90)
                Line((-2, 26.8), (-28.75, 26.8))
                Line((-28.75, 26.8), (-28.75, 23.8))
                Line((-2, 23.8), (-28.75, 23.8))
                CenterArc((-2, 21.8), 2, 0, 90)
                Line((0, 2), (0, 21.8))
                CenterArc((5, 2), 5, 180, 90)
                Line((5, -3), (35.5, -3))
                CenterArc((35.5, 2), 5, -90, 90)
                Line((40.5, 2), (40.5, 18.8000000011))
                CenterArc((42.5, 18.8000000011), 2, 90, 90)
                Line((42.5, 20.8000000011), (66.1355429876, 20.8000000011))
                Line((66.1355429876, 20.8000000011), (66.1298073219, 26.8000007629))
                Line((42.3798073219, 26.8000007629), (66.1298073219, 26.8000007629))
                CenterArc((42.3798073219, 21.8000007629), 5, 90, 90)
                Line((37.3798073219, 2), (37.3798073219, 21.8000007629))
                CenterArc((35.3798073219, 2), 2, -90, 90)
                Line((3.5, 0), (35.3798073219, 0))
                CenterArc((3.5, 0.5), 0.5, 180, 90)
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 157.0796326795, perimeter: 125.6637061436
            with BuildLine():
                CenterArc((-18.8798073219, 15), 11.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-18.8798073219, 15), 8.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=17
        extrude(amount=17, mode=Mode.ADD)
    return part.part


def model_78974_a0ff53c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 261.372968935, perimeter: 78.1079632679
            with BuildLine():
                Line((-19.8972589703, -9.0621208325), (-14.600602632, -0.1119570556))
                Line((-14.600602632, -0.1119570556), (-19.7033436617, 8.9501637769))
                Line((-19.7033436617, 8.9501637769), (-30.1027410297, 9.0621208325))
                Line((-30.1027410297, 9.0621208325), (-35.399397368, 0.1119570556))
                Line((-35.399397368, 0.1119570556), (-30.2966563383, -8.9501637769))
                Line((-30.2966563383, -8.9501637769), (-19.8972589703, -9.0621208325))
            make_face()
            with BuildLine():
                CenterArc((-25, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.5061423047, perimeter: 15.0123425582
            with BuildLine():
                Line((-25.4030423457, 9.0115251674), (-25.4030423457, 2.5))
                Line((-25.4030423457, 2.5), (-25, 2.5))
                Line((-25, 2.5), (-24.4030423457, 2.5))
                Line((-24.4030423457, 2.5), (-24.4030423457, 9.0007594421))
                Line((-24.4030423457, 9.0007594421), (-25.4030423457, 9.0115251674))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.5248301396, perimeter: 15.1249528959
            with BuildLine():
                CenterArc((-25, 0), 2.5, -103.8147268154, 23.0922655361)
                Line((-25.5969576543, -2.4276823431), (-25.5969576543, -9.0007594421))
                Line((-25.5969576543, -9.0007594421), (-24.5969576543, -9.0115251674))
                Line((-24.5969576543, -9.0115251674), (-24.5969576543, -2.4672974826))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_78977_79bd8a43_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.9, perimeter: 46.6
            with BuildLine():
                Line((15, 0), (15, -0.3))
                Line((15, 0), (10, 0))
                Line((10, 0), (10, -4))
                Line((10, -4), (5, -4))
                Line((5, 0), (5, -4))
                Line((0, 0), (5, 0))
                Line((0, 0), (0, -0.3))
                Line((0, -0.3), (4.7, -0.3))
                Line((4.7, -0.3), (4.7, -4.3))
                Line((4.7, -4.3), (10.3, -4.3))
                Line((10.3, -0.3), (10.3, -4.3))
                Line((15, -0.3), (10.3, -0.3))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5406596081, perimeter: 2.6065550083
            with Locations((-7.5, 2)):
                Circle(0.414846114)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9171426123, perimeter: 19.1979046204
            with BuildLine():
                CenterArc((-7.5, 2), 1.6275827848, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.5, 2), 1.4278586326, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_78989_d3a05073_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 422.4626114718, perimeter: 213.4787535659
            with BuildLine():
                Line((21.9, -5.7), (21.9, -13.2))
                CenterArc((32.5, -13.2), 10.6, 180, 180)
                Line((43.1, -5.7), (43.1, -13.2))
                CenterArc((45.6, -5.7), 2.5, 90, 90)
                Line((65, -3.2), (45.6, -3.2))
                Line((65, 0), (65, -3.2))
                Line((0, 0), (65, 0))
                Line((0, 0), (0, -3.2))
                Line((0, -3.2), (19.4, -3.2))
                CenterArc((19.4, -5.7), 2.5, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((32.5, -13.2), 7.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


def model_79206_50124982_0000():
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
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5978.5398163397, perimeter: 311.4159265359
            with BuildLine():
                CenterArc((25, -45), 5, -90, 90)
                Line((30, -45), (30, 45))
                CenterArc((25, 45), 5, 0, 90)
                Line((25, 50), (-25, 50))
                CenterArc((-25, 45), 5, 90, 90)
                Line((-30, 45), (-30, -45))
                CenterArc((-25, -45), 5, 180, 90)
                Line((-25, -50), (25, -50))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 931, perimeter: 532
            with BuildLine():
                Line((25, -45), (25, 45))
                Line((25, 45), (-25, 45))
                Line((-25, 45), (-25, -45))
                Line((-25, -45), (25, -45))
            make_face()
            with BuildLine():
                Line((-21.5, -41.5), (21.5, -41.5))
                Line((-21.5, 41.5), (-21.5, -41.5))
                Line((21.5, 41.5), (-21.5, 41.5))
                Line((21.5, -41.5), (21.5, 41.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_79228_87a014bf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch11 -> Extrude8 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.3075680535, perimeter: 19.1474829172
            with BuildLine():
                Line((0.0248038216, -1.7372673817), (3.4065538751, -1.6378133416))
                CenterArc((3.4002507033, -1.4234856844), 0.2144203223, -88.3154713653, 57.1514115223)
                Line((3.5837278224, -1.5344461341), (4.304168293, -0.3431717444))
                CenterArc((4.120691174, -0.2322112947), 0.2144203223, -31.1640598431, 120.916716186)
                Line((0, 0), (4.1216168153, -0.0177929704))
                Line((0, 0), (-4.1110194837, 0))
                CenterArc((-4.1110194837, -0.2144203223), 0.2144203223, 90, 122.2696698715)
                Line((-4.292321425, -0.3289003672), (-3.5341691479, -1.5295854278))
                CenterArc((-3.3528672066, -1.4151053829), 0.2144203223, -147.7303301285, 55.9051608853)
                Line((0.0248038216, -1.7372673817), (-3.3596964564, -1.6294169224))
            make_face()
        # OneSide extrude, distance=0.3325
        extrude(amount=0.3325)
    return part.part


def model_79427_59912769_0000():
    """Model: box-pivot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.0053096491, perimeter: 20.0530964915
            with BuildLine():
                CenterArc((2.5, 0), 0.8, -90, 180)
                Line((-2.5, 0.8), (2.5, 0.8))
                CenterArc((-2.5, 0), 0.8, 90, 180)
                Line((2.5, -0.8), (-2.5, -0.8))
            make_face()
            with BuildLine():
                CenterArc((-2.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.6
        extrude(amount=0.3, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.1780972451, perimeter: 21.7123889804
            with BuildLine():
                Line((-1.3, 5.5), (-1.3, 1.8))
                CenterArc((-0.3, 1.8), 1, 180, 90)
                Line((-0.3, 0.8), (0.3, 0.8))
                CenterArc((0.3, 1.8), 1, -90, 90)
                Line((1.3, 1.8), (1.3, 5.5))
                Line((0.8, 5.5), (1.3, 5.5))
                Line((0.8, 1.8), (0.8, 5.5))
                CenterArc((0.3, 1.8), 0.5, -90, 90)
                Line((-0.3, 1.3), (0.3, 1.3))
                CenterArc((-0.3, 1.8), 0.5, 180, 90)
                Line((-0.8, 5.5), (-0.8, 1.8))
                Line((-1.3, 5.5), (-0.8, 5.5))
            make_face()
        # Symmetric extrude, full_length=True, total=3
        extrude(amount=1.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 4.5)):
                Circle(0.3)
        # TwoSides extrude, along=1.6818, against=-1.9208
        extrude(amount=1.6818, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1.9208, mode=Mode.SUBTRACT)
    return part.part


def model_79658_c548e8b7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            Circle(0.65)
        # OneSide extrude, distance=24
        extrude(amount=24, mode=Mode.ADD)
    return part.part


def model_79981_7148f1e3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.4, perimeter: 43.0796447372
            with BuildLine():
                CenterArc((5.5, -1.5), 0.8, -90, 90)
                Line((6.3, 1.5), (6.3, -1.5))
                CenterArc((5.5, 1.5), 0.8, 0, 90)
                Line((-5.5, 2.3), (5.5, 2.3))
                CenterArc((-5.5, 1.5), 0.8, 90, 90)
                Line((-6.3, -1.5), (-6.3, 1.5))
                CenterArc((-5.5, -1.5), 0.8, -180, 90)
                Line((5.5, -2.3), (-5.5, -2.3))
            make_face()
            with BuildLine():
                CenterArc((-5.5, 1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.1, 1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.5, -1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.1, -1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_79990_4affd434_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 26.2015149025, perimeter: 29.3204420793
            with BuildLine():
                CenterArc((-6.998250247, -0.0836417987), 2, 108.9603960051, 144.4488544264)
                Line((-7.569317531, -2.0003791717), (-0.6360825965, -2.4177259833))
                CenterArc((0, 0), 2.5, 105.2436277392, 150.0163796281)
                Line((-7.6480792775, 1.8078449792), (-0.6573097804, 2.4120414285))
            make_face()
            with BuildLine():
                CenterArc((-6.998250247, -0.0836417987), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 26.3470349115, perimeter: 29.0902573021
            with BuildLine():
                CenterArc((0, 0), 2.5, -73.6232078782, 147.2464157565)
                Line((7.4811454619, -1.9412622297), (0.7048821496, -2.3985706484))
                CenterArc((7, 0), 2, -76.0796541377, 153.9118522365)
                Line((0.7048821496, 2.3985706484), (7.4215509834, 1.9550689933))
            make_face()
            with BuildLine():
                CenterArc((7, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_80190_f72bfc7b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.2443198103, perimeter: 47.0215990513
            with BuildLine():
                Line((15.1107995256, 0), (10.1107995256, 0))
                Line((10.1107995256, 0), (10.1107995256, -4))
                Line((5, -4), (10.1107995256, -4))
                Line((5, 0), (5, -4))
                Line((0, 0), (5, 0))
                Line((0, 0), (0, -0.4))
                Line((0, -0.4), (4.6, -0.4))
                Line((4.6, -0.4), (4.6, -4.4))
                Line((10.5107995256, -4.4), (4.6, -4.4))
                Line((10.5107995256, -0.4), (10.5107995256, -4.4))
                Line((15.1107995256, -0.4), (10.5107995256, -0.4))
                Line((15.1107995256, 0), (15.1107995256, -0.4))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9001273731, perimeter: 15.3099475845
            with BuildLine():
                CenterArc((-7.5553997628, 2.5), 1.342437557, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.5553997628, 2.5), 1.0942162796, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5541405937, perimeter: 2.6388512791
            with Locations((-7.5553997628, 2.5)):
                Circle(0.4199862252)
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)
    return part.part


def model_81549_4d4d7118_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.52, perimeter: 34.0499566724
            with BuildLine():
                Line((12.7, 5), (3.8, 13.9))
                Line((1.2, 13.9), (3.8, 13.9))
                Line((1.2, 13.9), (12.7, 2.4))
                Line((12.7, 2.4), (12.7, 5))
            make_face()
            # Profile area: 110.405, perimeter: 46.4634559673
            with BuildLine():
                Line((1.2, 13.9), (12.7, 2.4))
                Line((0, 13.9), (1.2, 13.9))
                Line((0, 13.9), (0, 0))
                Line((0, 0), (12.7, 0))
                Line((12.7, 0), (12.7, 2.4))
            make_face()
        # Symmetric extrude, full_length=True, total=7.6
        extrude(amount=3.8, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.52, perimeter: 34.0499566724
            with BuildLine():
                Line((12.7, 5), (3.8, 13.9))
                Line((1.2, 13.9), (3.8, 13.9))
                Line((1.2, 13.9), (12.7, 2.4))
                Line((12.7, 2.4), (12.7, 5))
            make_face()
        # Symmetric extrude, full_length=True, total=2.6
        extrude(amount=1.3, both=True, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.8470115891, perimeter: 41.7831822927
            with BuildLine():
                CenterArc((3.8, 8.9), 3.8, 180, 180)
                CenterArc((3.8, 8.9), 3.8, 0, 180)
            make_face()
            with BuildLine():
                CenterArc((3.8, 8.9), 2.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 44.9577010411, perimeter: 37.3380520836
            with BuildLine():
                Line((0, 8.9), (0, 0))
                Line((0, 0), (7.6, 0))
                Line((7.6, 8.9), (7.6, 0))
                CenterArc((3.8, 8.9), 3.8, 180, 180)
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1764368493, perimeter: 29.8451302091
            with BuildLine():
                CenterArc((3.8, 8.9), 2.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.8, 8.9), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


def model_81829_9dffccb3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 28, perimeter: 22
            with BuildLine():
                Line((-3.5, 2), (-3.5, -2))
                Line((-3.5, -2), (3.5, -2))
                Line((3.5, -2), (3.5, 2))
                Line((3.5, 2), (-3.5, 2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.095585526, perimeter: 1.0959758871
            with Locations((3.1726347083, -1.6726347083)):
                Circle(0.1744299799)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.05, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0084331205, perimeter: 0.442589891
            with BuildLine():
                Line((3.1993592085, -1.6726347083), (3.1993592085, -1.8450052945))
                Line((3.1504348493, -1.6726347083), (3.1993592085, -1.6726347083))
                Line((3.1504348493, -1.8450052945), (3.1504348493, -1.6726347083))
                Line((3.1993592085, -1.8450052945), (3.1504348493, -1.8450052945))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


def model_82000_bea5ae68_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6943990677, perimeter: 32.185818144
            with BuildLine():
                Line((1.3000000194, -1.5000000224), (2.0771451762, -1.4606080294))
                Line((-4.2000000626, 0.9000000134), (1.3000000194, -1.5000000224))
                Line((-5.9359387751, 1.9492603487), (-4.2000000626, 0.9000000134))
                CenterArc((-6.5000000969, 1.5000000224), 0.7211102658, -102.9614739552, 141.4978935028)
                Line((-5.2143140411, 0.4641227233), (-6.6617421231, 0.7972628507))
                Line((-5.2143140411, 0.4641227233), (0.7119941462, -2.1125330103))
                Line((0.7119941462, -2.1125330103), (1.2517463221, -2.6765338542))
                CenterArc((2.3000000343, -2.5000000373), 1.0630145971, 102.1015030116, 87.457839969)
            make_face()
            with BuildLine():
                Line((-4.7645940808, 0.465869913), (-4.4959775411, 0.8104635358))
                Line((-4.4959775411, 0.8104635358), (0.297213021, -1.2811105276))
                Line((0.297213021, -1.2811105276), (-0.0865967754, -1.5680419589))
                Line((-0.0865967754, -1.5680419589), (-4.7645940808, 0.465869913))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1682170259, perimeter: 11.2468142408
            with BuildLine():
                Line((-0.0865967754, -1.5680419589), (-4.7645940808, 0.465869913))
                Line((0.297213021, -1.2811105276), (-0.0865967754, -1.5680419589))
                Line((-4.4959775411, 0.8104635358), (0.297213021, -1.2811105276))
                Line((-4.7645940808, 0.465869913), (-4.4959775411, 0.8104635358))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9443342902, perimeter: 7.8079425033
            with BuildLine():
                CenterArc((2.3000000343, -2.5000000373), 1.0630145971, -158.0589425732, 7.6510594064)
                CenterArc((2.0949952292, -2.5989557837), 0.8360214465, -149.3669551039, 93.0880473472)
                Line((2.5591130839, -3.2943164642), (1.9305686464, -2.7555640892))
                CenterArc((2.663047574, -2.7152391017), 0.7335880888, 102.8418312974, 80.3092786687)
                Line((3.1620026464, -2.5374976517), (2.5, -2))
                CenterArc((1.5732374753, -2.7231912457), 1.5995802199, 6.6664382056, 44.8132077407)
                CenterArc((2.3000000343, -2.5000000373), 1.0630145971, 75.3169509154, 8.3850049074)
                Line((2.0771451762, -1.4606080294), (2.4166131412, -1.4434010514))
                CenterArc((2.3000000343, -2.5000000373), 1.0630145971, 102.1015030116, 87.457839969)
                CenterArc((2.3000000343, -2.5000000373), 1.0630145971, -170.4406570194, 12.3817144463)
            make_face()
        # Symmetric extrude, each_side=0.35
        extrude(amount=0.35, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7942738957, perimeter: 7.7785821028
            with BuildLine():
                CenterArc((-6.5000000969, 1.5000000224), 0.7211102658, -102.9614739552, 141.4978935028)
                CenterArc((-6.5000000969, 1.5000000224), 0.7211102658, 38.5364195476, 218.5021064972)
            make_face()
            with BuildLine():
                CenterArc((-6.5000000969, 1.5000000224), 0.5168895261, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.35
        extrude(amount=0.35, both=True, mode=Mode.ADD)
    return part.part


def model_82147_ce3b87f4_0000():
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
        # Sketch7 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1255936136, perimeter: 4.1222697541
            with BuildLine():
                Line((0.5000000075, 0.5000000075), (0, 0))
                Line((0, 1.0000000149), (0.5000000075, 0.5000000075))
                Line((0, 0), (0, 1.0000000149))
            make_face()
            with BuildLine():
                Line((0.401199807, 0.5000000075), (0.0509373572, 0.1399014467))
                Line((0.0509373572, 0.1399014467), (0.0509373572, 0.8502624573))
                Line((0.0509373572, 0.8502624573), (0.401199807, 0.5000000075))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1391799065, perimeter: 4.0215802428
            with BuildLine():
                Line((0, -1.0000000149), (0.5000000075, -0.5000000075))
                Line((0.5000000075, -0.5000000075), (0, 0))
                Line((0, 0), (0, -1.0000000149))
            make_face()
            with BuildLine():
                Line((0.0595242813, -0.8417064588), (0.3924208133, -0.5088099268))
                Line((0.0595242813, -0.1759133949), (0.0595242813, -0.8417064588))
                Line((0.3924208133, -0.5088099268), (0.0595242813, -0.1759133949))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0865509858, perimeter: 2.7986927289
            with BuildLine():
                Line((0, 0), (-0.5000000075, 0.5000000075))
                Line((-0.5000000075, 0.5000000075), (-0.5423423484, 0.4576576665))
                Line((-0.5423423484, 0.4576576665), (-0.09220407, 0.007519388))
                Line((-0.09220407, 0.007519388), (-0.5211711779, -0.42144772))
                Line((-0.5211711779, -0.42144772), (-0.5000000075, -0.5000000075))
                Line((0, 0), (-0.5000000075, -0.5000000075))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_82877_d5d034aa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # base principal -> Extrude principal (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 108, perimeter: 42
            with BuildLine():
                Line((8, -3.5), (-4, -3.5))
                Line((8, 5.5), (8, -3.5))
                Line((-4, 5.5), (8, 5.5))
                Line((-4, -3.5), (-4, 5.5))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.9063742947, perimeter: 25.5066051147
            with BuildLine():
                Line((-5.2533025573, -5.5), (-5.2533025573, 4))
                Line((-2, -5.5), (-5.2533025573, -5.5))
                Line((-2, 4), (-2, -5.5))
                Line((-2, 4), (-5.2533025573, 4))
            make_face()
            # Profile area: 0.0571151807, perimeter: 6.5417172382
            with BuildLine():
                Line((-2, 4), (-5.2533025573, 4))
                Line((-2, 4.0175560618), (-2, 4))
                Line((-5.2533025573, 4.0175560618), (-2, 4.0175560618))
                Line((-5.2533025573, 4), (-5.2533025573, 4.0175560618))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-3.5, -1.5)):
                Circle(1)
        # OneSide extrude, distance=-11.5
        extrude(amount=-11.5, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_55613_d38aaa88_0000": {"func": model_55613_d38aaa88_0000, "volume": 2748.4930526635, "area": 2070.005397636},
    "model_55625_453e11ac_0001": {"func": model_55625_453e11ac_0001, "volume": 9.0991951436, "area": 43.0724862005},
    "model_55625_453e11ac_0011": {"func": model_55625_453e11ac_0011, "volume": 7.7894690351, "area": 83.38},
    "model_55722_df6cad0f_0000": {"func": model_55722_df6cad0f_0000, "volume": 1969.8577322796, "area": 1665.5306969395},
    "model_55769_a112414f_0000": {"func": model_55769_a112414f_0000, "volume": 213.1871097049, "area": 422.1335164038},
    "model_56065_00bbe5da_0023": {"func": model_56065_00bbe5da_0023, "volume": 10.3206628471, "area": 59.0428664596},
    "model_56167_90101372_0005": {"func": model_56167_90101372_0005, "volume": 688.6528176302, "area": 841.711211713},
    "model_56250_3b6024e3_0008": {"func": model_56250_3b6024e3_0008, "volume": 2.6619499952, "area": 19.9302637944},
    "model_56250_3b6024e3_0009": {"func": model_56250_3b6024e3_0009, "volume": 3.3161866653, "area": 23.6687590521},
    "model_56250_3b6024e3_0025": {"func": model_56250_3b6024e3_0025, "volume": 4.8185119802, "area": 27.470086163},
    "model_56318_df6463e8_0000": {"func": model_56318_df6463e8_0000, "volume": 11818.0456195431, "area": 8833.0589276348},
    "model_56343_60e8809c_0004": {"func": model_56343_60e8809c_0004, "volume": 1.3105001004, "area": 16.3957809876},
    "model_56344_3a89f085_0032": {"func": model_56344_3a89f085_0032, "volume": 0.769037247, "area": 6.1734417865},
    "model_56345_80dc7bcc_0004": {"func": model_56345_80dc7bcc_0004, "volume": 0.3378893846, "area": 5.9867698319},
    "model_56357_f92aa53e_0000": {"func": model_56357_f92aa53e_0000, "volume": 335527.2005491733, "area": 56684.4801068854},
    "model_56459_7b640aed_0006": {"func": model_56459_7b640aed_0006, "volume": 2856.8858193582, "area": 1880.2432031735},
    "model_56459_7b640aed_0008": {"func": model_56459_7b640aed_0008, "volume": 17300.8499182154, "area": 8684.0998078876},
    "model_56459_7b640aed_0013": {"func": model_56459_7b640aed_0013, "volume": 146.6161776874, "area": 1287.8825074823},
    "model_56472_753de501_0003": {"func": model_56472_753de501_0003, "volume": 48.5895681986, "area": 105.248035573},
    "model_56489_241ed182_0009": {"func": model_56489_241ed182_0009, "volume": 0.7539822369, "area": 8.7964594301},
    "model_56489_241ed182_0014": {"func": model_56489_241ed182_0014, "volume": 107.1911340619, "area": 870.1583387902},
    "model_56666_b0aba65d_0000": {"func": model_56666_b0aba65d_0000, "volume": 1.1323917795, "area": 9.8624911361},
    "model_56998_2ed56cb9_0000": {"func": model_56998_2ed56cb9_0000, "volume": 54940.9846789929, "area": 18722.4037118322},
    "model_57020_310f992c_0000": {"func": model_57020_310f992c_0000, "volume": 785000, "area": 105200},
    "model_57255_263121a5_0000": {"func": model_57255_263121a5_0000, "volume": 0.0265096688, "area": 0.7176450385},
    "model_57433_498aa3b9_0000": {"func": model_57433_498aa3b9_0000, "volume": 177.9586580054, "area": 487.9232621831},
    "model_57872_a723a393_0000": {"func": model_57872_a723a393_0000, "volume": 105.8692775884, "area": 341.8112137917},
    "model_57877_1100841a_0000": {"func": model_57877_1100841a_0000, "volume": 71.0017323176, "area": 342.6119138439},
    "model_60279_4d453fb2_0000": {"func": model_60279_4d453fb2_0000, "volume": 21.8294911911, "area": 62.3654535949},
    "model_60716_dcd9370c_0001": {"func": model_60716_dcd9370c_0001, "volume": 89.1383704049, "area": 128.8156001492},
    "model_60720_ef9a0a95_0008": {"func": model_60720_ef9a0a95_0008, "volume": 19.5, "area": 159},
    "model_60720_ef9a0a95_0010": {"func": model_60720_ef9a0a95_0010, "volume": 4.3479997854, "area": 61.1300001957},
    "model_60723_c8e7621d_0000": {"func": model_60723_c8e7621d_0000, "volume": 2235.7823520949, "area": 2084.9643733163},
    "model_60759_23829707_0007": {"func": model_60759_23829707_0007, "volume": 5156.9489029037, "area": 2600.8793599014},
    "model_60760_f95d00ad_0014": {"func": model_60760_f95d00ad_0014, "volume": 79.3252145031, "area": 334.5796176073},
    "model_60762_ffc5da86_0000": {"func": model_60762_ffc5da86_0000, "volume": 6127.5004965672, "area": 5284.4586111187},
    "model_61007_2d0c5172_0000": {"func": model_61007_2d0c5172_0000, "volume": 51.8175843749, "area": 191.1910621785},
    "model_61007_3de87d8b_0000": {"func": model_61007_3de87d8b_0000, "volume": 46.9086945103, "area": 186.8065057978},
    "model_61007_ea617ece_0000": {"func": model_61007_ea617ece_0000, "volume": 48.2363989376, "area": 189.3155743124},
    "model_61091_f7d8529d_0001": {"func": model_61091_f7d8529d_0001, "volume": 115.5505781949, "area": 227.5839884223},
    "model_61091_f7d8529d_0003": {"func": model_61091_f7d8529d_0003, "volume": 12.3602385583, "area": 45.8438839071},
    "model_61198_0c99f50a_0011": {"func": model_61198_0c99f50a_0011, "volume": 10.5060327309, "area": 36.0463627032},
    "model_61198_0c99f50a_0012": {"func": model_61198_0c99f50a_0012, "volume": 5.5046172264, "area": 26.244593624},
    "model_61270_6fc99e6c_0005": {"func": model_61270_6fc99e6c_0005, "volume": 32.3481808364, "area": 82.0640246132},
    "model_61901_f74dfb53_0000": {"func": model_61901_f74dfb53_0000, "volume": 54.5, "area": 288},
    "model_62101_f765b04e_0000": {"func": model_62101_f765b04e_0000, "volume": 93.9985067798, "area": 764.7627091596},
    "model_64383_e298386f_0000": {"func": model_64383_e298386f_0000, "volume": 11839.7581382143, "area": 8668.2020017521},
    "model_64386_2e79ddd8_0000": {"func": model_64386_2e79ddd8_0000, "volume": 13701.9725646915, "area": 10556.3441965603},
    "model_64675_42df5e14_0000": {"func": model_64675_42df5e14_0000, "volume": 638.0612574436, "area": 815.3100681813},
    "model_65326_373e91b3_0000": {"func": model_65326_373e91b3_0000, "volume": 219.6349540849, "area": 554.2477796077},
    "model_65343_ce99dbac_0000": {"func": model_65343_ce99dbac_0000, "volume": 38.6410644131, "area": 208.084471097},
    "model_65569_bd890a32_0002": {"func": model_65569_bd890a32_0002, "volume": 79878.9272337816, "area": 12650.4858260434},
    "model_65808_662bbe75_0011": {"func": model_65808_662bbe75_0011, "volume": 72.5957148075, "area": 123.1468041788},
    "model_66243_bf31a991_0000": {"func": model_66243_bf31a991_0000, "volume": 171.6259360957, "area": 357.83190646},
    "model_67221_275ba7e6_0000": {"func": model_67221_275ba7e6_0000, "volume": 17.2787593139, "area": 55.3705700748},
    "model_67262_d9978c87_0001": {"func": model_67262_d9978c87_0001, "volume": 8.3788962133, "area": 34.98493287},
    "model_67403_bb0225a8_0000": {"func": model_67403_bb0225a8_0000, "volume": 0.5718506929, "area": 8.1687463838},
    "model_67403_bb0225a8_0005": {"func": model_67403_bb0225a8_0005, "volume": 1.2174828064, "area": 15.5472302306},
    "model_67403_bb0225a8_0010": {"func": model_67403_bb0225a8_0010, "volume": 0.2004686011, "area": 3.6774868383},
    "model_68475_17ef1725_0000": {"func": model_68475_17ef1725_0000, "volume": 68.6666629507, "area": 171.8542217878},
    "model_69488_f2085c68_0006": {"func": model_69488_f2085c68_0006, "volume": 279667.4399999997, "area": 121560.0399999999},
    "model_69649_70b07cac_0000": {"func": model_69649_70b07cac_0000, "volume": 1413.7166941154, "area": 1602.2122533308},
    "model_70008_fa163f57_0000": {"func": model_70008_fa163f57_0000, "volume": 24.0812445307, "area": 74.6570796327},
    "model_70321_eccffc7e_0000": {"func": model_70321_eccffc7e_0000, "volume": 75.6924423823, "area": 165.1915175651},
    "model_71855_15b7cfef_0000": {"func": model_71855_15b7cfef_0000, "volume": 0.0724320025, "area": 1.9012738136},
    "model_72824_38a3b7ba_0002": {"func": model_72824_38a3b7ba_0002, "volume": 252.7279693021, "area": 351.8502065128},
    "model_73294_550ba932_0000": {"func": model_73294_550ba932_0000, "volume": 4851339.9874459952, "area": 707871.9988732189},
    "model_73388_10a40b49_0030": {"func": model_73388_10a40b49_0030, "volume": 0.3765092269, "area": 4.6994913318},
    "model_75646_4baf69b2_0014": {"func": model_75646_4baf69b2_0014, "volume": 42.4115008235, "area": 70.6858347058},
    "model_75860_539df258_0000": {"func": model_75860_539df258_0000, "volume": 1291.1779545864, "area": 1008.9945557112},
    "model_75966_08c4ab3e_0003": {"func": model_75966_08c4ab3e_0003, "volume": 78.1719137439, "area": 274.6605412971},
    "model_77194_49a0e425_0000": {"func": model_77194_49a0e425_0000, "volume": 3.2051039364, "area": 51.0605847345},
    "model_77211_d46ae17d_0013": {"func": model_77211_d46ae17d_0013, "volume": 72, "area": 116.49844719},
    "model_78513_7ad0bd6a_0004": {"func": model_78513_7ad0bd6a_0004, "volume": 28.0475501626, "area": 201.2622063614},
    "model_78603_4720dcb8_0005": {"func": model_78603_4720dcb8_0005, "volume": 0.0000188888, "area": 0.0044060837},
    "model_78767_404295e7_0005": {"func": model_78767_404295e7_0005, "volume": 31.6978141046, "area": 63.176901939},
    "model_78862_dcbc8940_0000": {"func": model_78862_dcbc8940_0000, "volume": 14964.3537555513, "area": 11331.8830044411},
    "model_78967_e53ff839_0000": {"func": model_78967_e53ff839_0000, "volume": 17872.4315189895, "area": 11897.4985724452},
    "model_78974_a0ff53c9_0000": {"func": model_78974_a0ff53c9_0000, "volume": 882.2279601618, "area": 856.428517639},
    "model_78977_79bd8a43_0000": {"func": model_78977_79bd8a43_0000, "volume": 31.2720873422, "area": 238.2964565272},
    "model_78989_d3a05073_0000": {"func": model_78989_d3a05073_0000, "volume": 10561.5652867945, "area": 6181.8940620904},
    "model_79206_50124982_0000": {"func": model_79206_50124982_0000, "volume": 20728.6194490192, "area": 14487.3274122872},
    "model_79228_87a014bf_0000": {"func": model_79228_87a014bf_0000, "volume": 4.4247663778, "area": 32.9816741769},
    "model_79427_59912769_0000": {"func": model_79427_59912769_0000, "volume": 20.654734186, "area": 102.6898208614},
    "model_79658_c548e8b7_0000": {"func": model_79658_c548e8b7_0000, "volume": 172.9132596536, "area": 270.8052867394},
    "model_79981_7148f1e3_0000": {"func": model_79981_7148f1e3_0000, "volume": 44.32, "area": 145.2637157898},
    "model_79990_4affd434_0000": {"func": model_79990_4affd434_0000, "volume": 118.5219955393, "area": 258.5180435567},
    "model_80190_f72bfc7b_0000": {"func": model_80190_f72bfc7b_0000, "volume": 49.8001975601, "area": 284.1637893702},
    "model_81549_4d4d7118_0000": {"func": model_81549_4d4d7118_0000, "volume": 1100.5233449617, "area": 857.2645614386},
    "model_81829_9dffccb3_0000": {"func": model_81829_9dffccb3_0000, "volume": 28.0048636075, "area": 78.0592246933},
    "model_82000_bea5ae68_0000": {"func": model_82000_bea5ae68_0000, "volume": 4.2284287624, "area": 38.0152031117},
    "model_82147_ce3b87f4_0000": {"func": model_82147_ce3b87f4_0000, "volume": 0.0702649012, "area": 2.8911575569},
    "model_82877_d5d034aa_0000": {"func": model_82877_d5d034aa_0000, "volume": 797.2804081722, "area": 639.9419691823},
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
