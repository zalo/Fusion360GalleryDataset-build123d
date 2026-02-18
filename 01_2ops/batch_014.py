"""Batch 014 - passing/01_2ops
202 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_45798_b573e9da_0006():
    """Model: Head pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0, 3.5000000522)):
                Circle(0.4)
        # TwoSides extrude (symmetric), distance=2.65
        extrude(amount=2.65, both=True)
    return part.part


def model_45798_b573e9da_0010():
    """Model: O ring"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9008845396, perimeter: 32.6725635973
            with BuildLine():
                CenterArc((-10, 7), 2.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10, 7), 2.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_45798_b573e9da_0011():
    """Model: cylinder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6442483208, perimeter: 36.4424750625
            with BuildLine():
                CenterArc((0, 0), 3.0000000447, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_45901_95d52151_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((5, -5), (0, -5))
                Line((5, 0), (5, -5))
                Line((0, 0), (5, 0))
                Line((0, -5), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_45922_26941172_0000():
    """Model: sealant 11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.5292030703, perimeter: 27.6460153516
            with BuildLine():
                CenterArc((65.0464344963, 0.1980667181), 2.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((65.0464344963, 0.1980667181), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_45922_26941172_0002():
    """Model: mirror 15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2725660089, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((25, 62.5), 1.9, 142.5341684027, 255.4334076802)
                CenterArc((25, 62.5), 1.9, 37.9675760829, 104.5665923198)
            make_face()
            with BuildLine():
                CenterArc((25, 62.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.8068617699, perimeter: 12.218277421
            with BuildLine():
                CenterArc((25, 62.5), 1.9, 37.9675760829, 104.5665923198)
                Line((26, 67), (26.4978821623, 63.6689093327))
                Line((24, 67), (26, 67))
                Line((23.491939154, 63.6557475869), (24, 67))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)
    return part.part


def model_45922_26941172_0006():
    """Model: saddle 7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((70, -45)):
                Circle(2)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_45922_26941172_0008():
    """Model: nut 13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4616784181, perimeter: 7.2985145918
            with BuildLine():
                Line((20.2721539031, 61.8628718708), (20.6878460969, 62.4171281292))
                Line((20.6878460969, 62.4171281292), (20.4156921938, 63.0542562584))
                Line((20.4156921938, 63.0542562584), (19.7278460969, 63.1371281292))
                Line((19.7278460969, 63.1371281292), (19.3121539031, 62.5828718708))
                Line((19.3121539031, 62.5828718708), (19.5843078062, 61.9457437416))
                Line((19.5843078062, 61.9457437416), (20.2721539031, 61.8628718708))
            make_face()
            with BuildLine():
                CenterArc((20, 62.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_46016_d699e580_0000():
    """Model: Pickups"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.15, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((-1.5, 25.5), (1.5, 25.5))
                Line((-1.5, 24), (-1.5, 25.5))
                Line((1.5, 24), (-1.5, 24))
                Line((1.5, 25.5), (1.5, 24))
            make_face()
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((-1.5, 17.5), (1.5, 17.5))
                Line((-1.5, 16), (-1.5, 17.5))
                Line((1.5, 16), (-1.5, 16))
                Line((1.5, 17.5), (1.5, 16))
            make_face()
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


def model_46016_d699e580_0003():
    """Model: Head"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 76.81761955, perimeter: 35.27295218
            with BuildLine():
                Line((4, 16), (4, 23))
                Line((4, 23), (-4, 23))
                Line((-4, 23), (-4, 16))
                CenterArc((-7, 12), 5, 0, 53.1301023542)
                Line((-2, 12), (2, 12))
                CenterArc((7, 12), 5, 126.8698976458, 53.1301023542)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_46016_d699e580_0004():
    """Model: Pegheads"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((2, 18.5)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((2, 21)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2, 21)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2, 18.5)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2, 16)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((2, 16)):
                Circle(0.15)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_46086_371b5052_0021():
    """Model: Plate 1 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.506973461, perimeter: 19.504542379
            with BuildLine():
                Line((1.825, 4.95), (1.7272554447, 7.976164396))
                CenterArc((1.2837429054, 7.9618390223), 0.4437438325, 1.85, 59.1643522554)
                Line((1.498776959, 8.35), (1, 8.35))
                Line((1, 1.44), (1, 8.35))
                Line((0.61, 1.05), (1, 1.44))
                Line((0.61, 0.65), (0.61, 1.05))
                Line((0, 0.65), (0.61, 0.65))
                Line((0, 0.45), (0, 0.65))
                CenterArc((0.8710068801, 1.0586673127), 1.0626047632, -145.0538095327, 60.8852629424)
                CenterArc((0.9483133424, 0.3017326374), 0.3017326374, -84.1685465903, 85.1688128571)
                Line((1.25, 3.233), (1.25, 0.307))
                Line((1.2, 3.718), (1.25, 3.233))
                Line((1.2, 4.95), (1.2, 3.718))
                Line((1.825, 4.95), (1.2, 4.95))
            make_face()
        # OneSide extrude, distance=0.18
        extrude(amount=0.18)
    return part.part


def model_46086_371b5052_0022():
    """Model: Pin 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.386
        extrude(amount=0.386)
    return part.part


def model_47999_d642cd79_0002():
    """Model: clothspin (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.5497912984, perimeter: 15.5026458825
            with BuildLine():
                Line((1.3, 0), (1.3, 0.2))
                Line((1.3, 0), (3.6, 0))
                Line((3.6, 0), (3.6, 0.2))
                Line((3.6, 0.2), (3.2, 0.6))
                Line((3.2, 0.6), (2.5316625033, 0.6))
                CenterArc((2.2000000328, 1.1000000164), 0.6000000089, -123.5573082174, 67.1146164348)
                Line((1.8683375623, 0.6), (0.779865801, 0.6))
                CenterArc((0.7006053499, 0.6609736106), 0.1000000015, -142.4295764811, 104.8591529622)
                Line((0.6213448988, 0.6), (-0.3000000164, 0.6))
                CenterArc((-0.6000000089, 1.0000000149), 0.5000000075, -126.8698976458, 73.7397935841)
                Line((-3.6, 0.2), (-0.9000000134, 0.6000000089))
                Line((-3.6, 0), (-3.6, 0.2))
                Line((-3.6, 0), (1, 0))
                Line((1, 0.2), (1, 0))
                Line((1.3, 0.2), (1, 0.2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_48224_53cae924_0013():
    """Model: cocpit v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 373.0639662657, perimeter: 104.7797567684
            with BuildLine():
                CenterArc((22.212375864, 26.4729635533), 10, 130, 20)
                Line((1.3397459622, 10.3205080757), (13.5521218262, 31.4729635533))
                CenterArc((10, 5.3205080757), 10, 150, 30)
                Line((0, 0), (0, 5.3205080757))
                Line((0, 0), (8.5, 0))
                Line((8.5, 0), (8.5, 5.3205080757))
                CenterArc((10, 5.3205080757), 1.5, 150, 30)
                Line((8.7009618943, 6.0705080757), (20.9133377584, 27.2229635533))
                CenterArc((22.212375864, 26.4729635533), 1.5, 130, 20)
                Line((21.2481944495, 27.622030218), (28.2397265602, 33.4886222335))
                Line((22.7760318779, 40), (28.2397265602, 33.4886222335))
                Line((15.7844997672, 34.1334079845), (22.7760318779, 40))
            make_face()
        # Symmetric extrude, each_side=11
        extrude(amount=11, both=True)
    return part.part


def model_48290_3a237df1_0004():
    """Model: Gear Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 15.2400004864)):
                Circle(0.635)
        # TwoSides extrude, along=6.35, against=-1.27
        extrude(amount=6.35)
        extrude(sk.sketch, amount=-1.27)
    return part.part


def model_48290_3a237df1_0007():
    """Model: Driver Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 7.6200004864)):
                Circle(0.635)
        # TwoSides extrude (symmetric), distance=5.08
        extrude(amount=5.08, both=True)
    return part.part


def model_48332_fb679f90_0002():
    """Model: manometer pointer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6517113787, perimeter: 6.6550939301
            with BuildLine():
                Line((-22.5, -1), (-22.3000003323, -0.8000000119))
                Line((-22.3419252451, -0.2549752377), (-22.3000003323, -0.8000000119))
                CenterArc((-22.5, 0), 0.3, -58.2026929159, 125.2027819423)
                Line((-22.5, 1.8), (-22.3827810905, 0.2761516382))
                Line((-22.6172193121, 0.2761514673), (-22.5, 1.8))
                CenterArc((-22.5, 0), 0.3, 112.9999945177, 125.2025857354)
                Line((-22.7000003323, -0.8000000119), (-22.6580752563, -0.2549749269))
                Line((-22.5, -1), (-22.7000003323, -0.8000000119))
            make_face()
            with BuildLine():
                CenterArc((-22.5, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.07
        extrude(amount=0.07)
    return part.part


def model_48332_fb679f90_0004():
    """Model: manometer disk"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.4933614313, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((-15.5, 0), 2.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-15.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_48475_02526608_0004():
    """Model: long_crossbar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=80
        extrude(amount=80)
    return part.part


def model_48475_02526608_0005():
    """Model: Short_crossbar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


def model_48639_796136da_0007():
    """Model: Narta_2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 792.2859708633, perimeter: 179.8071492716
            with BuildLine():
                Line((17.5, 60), (27.4035746358, 60))
                Line((17.5, 60), (17.5, -20))
                Line((27.4035746358, -20), (17.5, -20))
                Line((27.4035746358, 60), (27.4035746358, -20))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_48724_70685a9d_0004():
    """Model: cutter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 27.75, perimeter: 40
            with BuildLine():
                Line((-124.25, 10), (-124.25, 5.75))
                Line((-124.25, 5.75), (-128.5, 5.75))
                Line((-128.5, 5.75), (-128.5, 4.25))
                Line((-128.5, 4.25), (-124.25, 4.25))
                Line((-124.25, 4.25), (-124.25, 0))
                Line((-124.25, 0), (-122.75, 0))
                Line((-122.75, 0), (-122.75, 4.25))
                Line((-122.75, 4.25), (-118.5, 4.25))
                Line((-118.5, 4.25), (-118.5, 5.75))
                Line((-118.5, 5.75), (-122.75, 5.75))
                Line((-122.75, 5.75), (-122.75, 10))
                Line((-124.25, 10), (-122.75, 10))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_48724_70685a9d_0005():
    """Model: fan"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.6148123484, perimeter: 13.8936345718
            with BuildLine():
                CenterArc((87.5, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                Line((87.1, 0.634428877), (87.1, -0.634428877))
                CenterArc((87.5, 0), 0.75, -122.2309526355, 244.461905271)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_48724_70685a9d_0006():
    """Model: washers (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.2026819954, perimeter: 12.723450247
            with BuildLine():
                CenterArc((15, 20), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((15, 20), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_48724_70685a9d_0009():
    """Model: washers"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.4889357189, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((50, 25), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((50, 25), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_48833_b97e9993_0001():
    """Model: output"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.6361725124, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.5, against=-2
        extrude(amount=0.5)
        extrude(sk.sketch, amount=-2)
    return part.part


def model_48907_25974aa4_0004():
    """Model: slide shell v1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1055575132, perimeter: 2.638937829
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)
    return part.part


def model_48916_5b0c9682_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3014376029, perimeter: 19.1811550331
            with BuildLine():
                CenterArc((0, 0), 1.8027756377, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_49016_cd1b47bf_0003():
    """Model: lina v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=35
        extrude(amount=35)
    return part.part


def model_49016_cd1b47bf_0019():
    """Model: karma 2 v2 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1321191174, perimeter: 1.334030549
            with BuildLine():
                CenterArc((-0.200000003, -0.3000000045), 0.2121320375, -19.4712206345, 38.942441269)
                CenterArc((0.200000003, -0.3000000045), 0.2121320375, -160.5287793655, 256.167024493)
                CenterArc((0, 0), 0.200000003, -86.2303499617, 59.8408349754)
                CenterArc((0.200000003, -0.3000000045), 0.2121320375, 151.7418899245, 8.786889441)
            make_face()
            # Profile area: 0.0001781045, perimeter: 0.0749804849
            with BuildLine():
                CenterArc((0.200000003, -0.3000000045), 0.2121320375, 151.7418899245, 8.786889441)
                CenterArc((0, 0), 0.200000003, -90, 3.7696500383)
                Line((0, -0.200000003), (0, -0.2292893253))
            make_face()
            # Profile area: 0.0069515055, perimeter: 0.4166021976
            with BuildLine():
                CenterArc((-0.200000003, -0.3000000045), 0.2121320375, 28.2581100755, 56.103644797)
                CenterArc((0, 0), 0.200000003, -153.6104850137, 59.8408349754)
            make_face()
            # Profile area: 0.0069515055, perimeter: 0.4166021976
            with BuildLine():
                CenterArc((0.200000003, -0.3000000045), 0.2121320375, 95.6382451275, 56.103644797)
                CenterArc((0, 0), 0.200000003, -86.2303499617, 59.8408349754)
            make_face()
            # Profile area: 0.1117606988, perimeter: 1.2543057849
            with BuildLine():
                CenterArc((0, 0), 0.200000003, -93.7696500383, 3.7696500383)
                CenterArc((0, 0), 0.200000003, -90, 3.7696500383)
                CenterArc((0.200000003, -0.3000000045), 0.2121320375, 95.6382451275, 56.103644797)
                CenterArc((0, 0), 0.200000003, -26.3895149863, 232.7790299726)
                CenterArc((-0.200000003, -0.3000000045), 0.2121320375, 28.2581100755, 56.103644797)
            make_face()
            # Profile area: 0.0001781045, perimeter: 0.0749804849
            with BuildLine():
                Line((0, -0.200000003), (0, -0.2292893253))
                CenterArc((0, 0), 0.200000003, -93.7696500383, 3.7696500383)
                CenterArc((-0.200000003, -0.3000000045), 0.2121320375, 19.4712206345, 8.786889441)
            make_face()
            # Profile area: 0.1321191174, perimeter: 1.334030549
            with BuildLine():
                CenterArc((0.200000003, -0.3000000045), 0.2121320375, 160.5287793655, 38.942441269)
                CenterArc((-0.200000003, -0.3000000045), 0.2121320375, 19.4712206345, 8.786889441)
                CenterArc((0, 0), 0.200000003, -153.6104850137, 59.8408349754)
                CenterArc((-0.200000003, -0.3000000045), 0.2121320375, 84.3617548725, 256.167024493)
            make_face()
            # Profile area: 0.0011505253, perimeter: 0.2856019504
            with BuildLine():
                Line((0, -0.2292893253), (0, -0.3707106836))
                CenterArc((-0.200000003, -0.3000000045), 0.2121320375, -19.4712206345, 38.942441269)
            make_face()
            # Profile area: 0.0011505253, perimeter: 0.2856019504
            with BuildLine():
                CenterArc((0.200000003, -0.3000000045), 0.2121320375, 160.5287793655, 38.942441269)
                Line((0, -0.2292893253), (0, -0.3707106836))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_49016_cd1b47bf_0020():
    """Model: karma 3 v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2577757425, perimeter: 2.1964844004
            with BuildLine():
                Line((0, -0.5), (0, 0.2933983877))
                CenterArc((-0.1949367074, 0.168584251), 0.2314711399, 32.6306356105, 162.2858810216)
                CenterArc((0.930133663, 0.5877132672), 1.4311774113, -160.4585660087, 29.9238994459)
            make_face()
            # Profile area: 0.2577757425, perimeter: 2.1964844004
            with BuildLine():
                CenterArc((0.1949367074, 0.168584251), 0.2314711399, -14.9165166322, 162.2858810216)
                Line((0, -0.5), (0, 0.2933983877))
                CenterArc((-0.930133663, 0.5877132672), 1.4311774113, -49.4653334372, 29.9238994459)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_49024_b7f02205_0002():
    """Model: laczenie smiglo tylne v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2031623309, perimeter: 8.1043227963
            with BuildLine():
                CenterArc((-0.0426283636, 1.3210575332), 1.6216179321, -110.2836968895, 21.7900361195)
                CenterArc((0.0426283636, 1.3210575332), 1.6216179321, -91.5063392299, 21.7900361195)
                Line((0.604792654, -0.200000003), (1.4000000209, -0.200000003))
                Line((1.4000000209, -0.200000003), (1.4000000209, -0.1000000015))
                Line((1.4000000209, -0.1000000015), (1.5000000224, -0.1000000015))
                Line((1.5000000224, -0.1000000015), (1.5, 0.1000000015))
                Line((1.4000000209, 0.1000000015), (1.5, 0.1000000015))
                Line((1.4000000209, 0.200000003), (1.4000000209, 0.1000000015))
                Line((0.604792654, 0.200000003), (1.4000000209, 0.200000003))
                CenterArc((0.0426283636, -1.3210575332), 1.6216179321, 69.7163031105, 21.7900361195)
                CenterArc((-0.0426283636, -1.3210575332), 1.6216179321, 88.4936607701, 21.7900361195)
                Line((-0.604792654, 0.200000003), (-1.4000000209, 0.200000003))
                Line((-1.4000000209, 0.200000003), (-1.4000000209, 0.1000000015))
                Line((-1.4000000209, 0.1000000015), (-1.5, 0.1000000015))
                Line((-1.5000000224, -0.1000000015), (-1.5, 0.1000000015))
                Line((-1.4000000209, -0.1000000015), (-1.5000000224, -0.1000000015))
                Line((-1.4000000209, -0.200000003), (-1.4000000209, -0.1000000015))
                Line((-0.604792654, -0.200000003), (-1.4000000209, -0.200000003))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_49024_b7f02205_0003():
    """Model: tylne skrzydlo v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24.7215950362, perimeter: 21.9420576138
            with BuildLine():
                Line((-3, 0), (0, 0))
                Line((0, 0), (-1.9366871325, 7))
                Line((-6, 7), (-1.9366871325, 7))
                Line((-3, 0), (-6, 7))
            make_face()
            # Profile area: 38.8482207712, perimeter: 29.6342549605
            with BuildLine():
                Line((-1.9366871325, 7), (0, 18))
                Line((0, 18), (-3, 18))
                Line((-3, 18), (-6, 7))
                Line((-6, 7), (-1.9366871325, 7))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_49024_b7f02205_0005():
    """Model: TYLNE SMIGLO v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.2564279454, perimeter: 13.818702993
            with BuildLine():
                CenterArc((5.6172498504, -0.7213053193), 0.5, -90, 90)
                Line((6.1172498504, -0.5), (6.1172498504, -0.7213053193))
                CenterArc((5.6172498504, -0.5), 0.5, 0, 90)
                Line((0.5, 0), (5.6172498504, 0))
                CenterArc((0.5, -0.5), 0.5, 90, 90)
                Line((0, -0.7213053193), (0, -0.5))
                CenterArc((0.5, -0.7213053193), 0.5, 180, 90)
                Line((5.6172498504, -1.2213053193), (0.5, -1.2213053193))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_49134_e9867f8b_0000():
    """Model: Raczka_drzwiczki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-17.5, -75)):
                Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_49134_e9867f8b_0001():
    """Model: Nozka_prosta_1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((0, 0), (4, 0))
                Line((0, -4), (0, 0))
                Line((4, -4), (0, -4))
                Line((4, 0), (4, -4))
            make_face()
        # OneSide extrude, distance=103
        extrude(amount=103)
    return part.part


def model_49134_e9867f8b_0004():
    """Model: Nozka_kolko_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 400, perimeter: 208
            with BuildLine():
                Line((0, 100), (0, 0))
                Line((0, 0), (4, 0))
                Line((4, 0), (4, 100))
                Line((4, 100), (0, 100))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_49134_e9867f8b_0009():
    """Model: Grill_tylna"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 57.4731747704, perimeter: 230.7853981634
            with BuildLine():
                CenterArc((-228.75, 70.25), 0.25, 180, 90)
                Line((-120.25, 70), (-228.75, 70))
                CenterArc((-120.25, 70.25), 0.25, -90, 90)
                Line((-120, 70.25), (-120, 73.5))
                Line((-120.5, 73.5), (-120, 73.5))
                Line((-120.5, 70.5), (-120.5, 73.5))
                Line((-120.5, 70.5), (-228.5, 70.5))
                Line((-228.5, 70.5), (-228.5, 73.5))
                Line((-229, 73.5), (-228.5, 73.5))
                Line((-229, 70.25), (-229, 73.5))
            make_face()
        # OneSide extrude, distance=70
        extrude(amount=70)
    return part.part


def model_49134_e9867f8b_0011():
    """Model: Deska_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 602, perimeter: 157.2
            with BuildLine():
                Line((-25, -20), (-25, 50))
                Line((-33.6, 50), (-25, 50))
                Line((-33.6, -20), (-33.6, 50))
                Line((-25, -20), (-33.6, -20))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_49134_e9867f8b_0012():
    """Model: Haczyk_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.5429931489, perimeter: 24.2199543263
            with BuildLine():
                Line((-27.6302252396, 40.6015368961), (-29.1569897547, 40.6015368961))
                CenterArc((-29.1569897547, 40.9015368961), 0.3, -149.5118029372, 59.5118029372)
                Line((-29.4155098633, 40.7493286391), (-30.2414798915, 42.1522082569))
                Line((-30.2414798915, 42.1522082569), (-30.5, 42))
                Line((-29.6740299718, 40.5971203822), (-30.5, 42))
                CenterArc((-29.1569897547, 40.9015368961), 0.6, -149.5118029372, 59.5118029372)
                Line((-27.6302252396, 40.3015368961), (-29.1569897547, 40.3015368961))
                CenterArc((-27.6302252396, 40.9015368961), 0.6, -90, 70)
                Line((-25.6676395578, 44.5394141003), (-27.0664096671, 40.6963248101))
                CenterArc((-25.0098547233, 44.3), 0.7, 90, 70)
                Line((-22.5, 45), (-25.0098547233, 45))
                Line((-22.5, 45.3), (-22.5, 45))
                Line((-22.5, 45.3), (-25.0098547233, 45.3))
                CenterArc((-25.0098547233, 44.3), 1, 90, 70)
                Line((-25.949547344, 44.6420201433), (-27.3483174533, 40.7989308531))
                CenterArc((-27.6302252396, 40.9015368961), 0.3, -90, 70)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_49145_4a5b250e_0001():
    """Model: stoper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1806415776, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_49222_cbe1959b_0003():
    """Model: Allen Key"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.51341563, perimeter: 4.5573097189
            with BuildLine():
                CenterArc((-0.9978159687, 1.2498824721), 0.4753167932, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.9978159687, 1.2498824721), 0.2470214814, 179.9951327758, 19.6189974083)
                CenterArc((-0.9948379367, 1.2503971155), 0.25, -160.5038754495, 340.6170138589)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


def model_49222_cbe1959b_0004():
    """Model: Knife"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.270000008, perimeter: 2.4000000358
            with BuildLine():
                Line((-1.7000000253, 1.7000000253), (-1.4000000209, 1.7000000253))
                Line((-1.7000000253, 0.8000000119), (-1.7000000253, 1.7000000253))
                Line((-1.4000000209, 0.8000000119), (-1.7000000253, 0.8000000119))
                Line((-1.4000000209, 1.7000000253), (-1.4000000209, 0.8000000119))
            make_face()
        # OneSide extrude, distance=-6.4
        extrude(amount=-6.4)
    return part.part


def model_49222_cbe1959b_0005():
    """Model: Key Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9278079678, perimeter: 9.8295408455
            with BuildLine():
                CenterArc((0.125, 2.150000032), 0.5081551147, -139.1626658781, 27.7992756555)
                CenterArc((0.125, 0.9645730923), 0.9357609484, 114.2580458498, 311.4839083003)
                CenterArc((0.125, 2.150000032), 0.5081551147, -68.6366097774, 27.7992756555)
                CenterArc((0.125, 0.9645730923), 0.7358517335, 104.5699084044, 330.8601831912)
            make_face()
            # Profile area: 0.3177637887, perimeter: 4.4094216471
            with BuildLine():
                CenterArc((0.125, 0.9645730923), 0.9357609484, 103.4438091965, 10.8142366534)
                CenterArc((0.125, 2.150000032), 0.3508917263, -51.6830909185, 283.366181837)
                CenterArc((0.125, 0.9645730923), 0.9357609484, 65.7419541502, 10.8142366534)
                CenterArc((0.125, 2.150000032), 0.5081551147, -40.8373341219, 261.6746682439)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


def model_49222_cbe1959b_0007():
    """Model: Key Ring Holder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0125309704, perimeter: 0.6616770712
            with BuildLine():
                Line((0, 2.2500000335), (0, 2.2938526305))
                Line((0, 2.2500000335), (0.2809055451, 2.2500000335))
                CenterArc((0.5905812144, 2.1969263309), 0.314190767, 162.0314407773, 8.2434170137)
                Line((0, 2.2938526305), (0.2917148052, 2.2938526305))
            make_face()
            # Profile area: 0.0035964176, perimeter: 0.4074900575
            with BuildLine():
                CenterArc((0.5905812144, 2.1969263309), 0.314190767, 170.274857791, 18.3147540607)
                CenterArc((0.5905812144, 2.1969263309), 0.314190767, -171.4103881483, 9.378947371)
                Line((0.3000000045, 2.1000000313), (0.2917148052, 2.1000000313))
                Line((0.3000000045, 2.2938526305), (0.3000000045, 2.1000000313))
                Line((0.2917148052, 2.2938526305), (0.3000000045, 2.2938526305))
                CenterArc((0.5905812144, 2.1969263309), 0.314190767, 162.0314407773, 8.2434170137)
            make_face()
            # Profile area: 0.0142547003, perimeter: 0.6730603715
            with BuildLine():
                CenterArc((0.5905812144, 2.1969263309), 0.314190767, -171.4103881483, 9.378947371)
                Line((0, 2.150000032), (0.2799145754, 2.150000032))
                Line((0, 2.1000000313), (0, 2.150000032))
                Line((0.2917148052, 2.1000000313), (0, 2.1000000313))
            make_face()
            # Profile area: 0.0950755963, perimeter: 3.6175655387
            with BuildLine():
                Line((0.2917148052, 2.2938526305), (0.3000000045, 2.2938526305))
                Line((0.3000000045, 2.2938526305), (0.3000000045, 2.1000000313))
                Line((0.3000000045, 2.1000000313), (0.2917148052, 2.1000000313))
                CenterArc((0.5905812144, 2.1969263309), 0.314190767, -162.0314407773, 324.0628815547)
            make_face()
            with BuildLine():
                CenterArc((0.5905812144, 2.1969263309), 0.2594370069, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_49222_cbe1959b_0008():
    """Model: Bit for the Interchangeable Adapter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2893851364, perimeter: 1.9292342143
            with BuildLine():
                Line((-5.0803848334, -5.6000000834), (-4.9196153156, -5.6000000834))
                Line((-4.9196153156, -5.6000000834), (-4.780384829, -5.5196153245))
                Line((-4.780384829, -5.5196153245), (-4.70000007, -5.3803848379))
                Line((-4.70000007, -5.3803848379), (-4.70000007, -5.21961532))
                Line((-4.70000007, -5.21961532), (-4.780384829, -5.0803848334))
                Line((-4.780384829, -5.0803848334), (-4.9196153156, -5.0000000745))
                Line((-4.9196153156, -5.0000000745), (-5.0803848334, -5.0000000745))
                Line((-5.0803848334, -5.0000000745), (-5.21961532, -5.0803848334))
                Line((-5.21961532, -5.0803848334), (-5.300000079, -5.21961532))
                Line((-5.300000079, -5.21961532), (-5.300000079, -5.3803848379))
                Line((-5.300000079, -5.3803848379), (-5.21961532, -5.5196153245))
                Line((-5.21961532, -5.5196153245), (-5.0803848334, -5.6000000834))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_49222_cbe1959b_0010():
    """Model: Front Face"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5210651218, perimeter: 5.6586646119
            with BuildLine():
                CenterArc((-0.4773573881, 1.2361613942), 1.3251283215, -68.885380989, 137.770761978)
                Line((0, 0), (0, 2.4723227884))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_49223_c0e227df_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 149.1821210227, perimeter: 63.7073305287
            with BuildLine():
                Line((0, 0), (22.5, 0))
                Line((22.5, 0), (22.6257179169, 10.9992815677))
                Line((2.1810035604, 2.739080788), (22.6257179169, 10.9992815677))
                Line((1.2980573964, 4.9244492308), (2.1810035604, 2.739080788))
                Line((0, 4.4), (1.2980573964, 4.9244492308))
                Line((0, 0), (0, 4.4))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_49300_a92e7ac9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.4238468925, perimeter: 23.8916909151
            Circle(3.802480708)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_49330_c6744767_0012():
    """Model: vices 11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.8357293382, perimeter: 23.5619449019
            with BuildLine():
                CenterArc((50, 5), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((50, 5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_49418_9aa6df68_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((2, 2), (2, 0))
                Line((0, 2), (2, 2))
                Line((0, 0), (0, 2))
                Line((2, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_49502_0ed856f7_0006():
    """Model: Crank Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7673438324), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-6.7719988164, 22.8059138953)):
                Circle(1.5)
        # TwoSides extrude, along=0.1, against=-3.6
        extrude(amount=0.1)
        extrude(sk.sketch, amount=-3.6)
    return part.part


def model_49503_e42c01c0_0004():
    """Model: Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=57
        extrude(amount=57)
    return part.part


def model_49503_e42c01c0_0006():
    """Model: Back bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.2831853072, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((65, 5), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((65, 5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_49562_6df35938_0001():
    """Model: Nut 7mm 20d"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2132311113, perimeter: 8.1991148575
            with BuildLine():
                Line((0.5, -0.8660254038), (1, 0))
                Line((1, 0), (0.5, 0.8660254038))
                Line((0.5, 0.8660254038), (-0.5, 0.8660254038))
                Line((-0.5, 0.8660254038), (-1, 0))
                Line((-1, 0), (-0.5, -0.8660254038))
                Line((-0.5, -0.8660254038), (0.5, -0.8660254038))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_49562_6df35938_0003():
    """Model: Button"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_49562_6df35938_0011():
    """Model: Washer 7mm 25d"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5238934212, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_49562_6df35938_0014():
    """Model: Nut 7mm 10d"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2646739528, perimeter: 5.1991148575
            with BuildLine():
                Line((0.4368572304, -0.243219572), (0.4290629433, 0.2567196734))
                Line((0.4290629433, 0.2567196734), (-0.0077942872, 0.4999392454))
                Line((-0.0077942872, 0.4999392454), (-0.4368572304, 0.243219572))
                Line((-0.4368572304, 0.243219572), (-0.4290629433, -0.2567196734))
                Line((-0.4290629433, -0.2567196734), (0.0077942872, -0.4999392454))
                Line((0.0077942872, -0.4999392454), (0.4368572304, -0.243219572))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_49613_1b97c07b_0011():
    """Model: small tube"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-16.5000002459, -5.500000082)):
                Circle(1.5)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_49613_1b97c07b_0013():
    """Model: main profile"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 292.2835737772, perimeter: 77.9422863406
            with BuildLine():
                Line((12.9903810568, -7.5), (0, 15))
                Line((0, 15), (-12.9903810568, -7.5))
                Line((-12.9903810568, -7.5), (12.9903810568, -7.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_49613_1b97c07b_0018():
    """Model: tube part 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.8495559215, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((25, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((25, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_49703_b92021be_0002():
    """Model: Cover3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.6977988715, -10.8989717776, 70.2410177687), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.7819799037, perimeter: 20.4555846442
            with BuildLine():
                Line((68.1330446111, 15.7423341925), (66.0494979328, 15.7423341925))
                CenterArc((62.9494979328, 15.7423341925), 3.1, -90, 90)
                Line((62.9494979328, 12.6423341925), (62.9494979328, 11.6423341925))
                CenterArc((62.9494979328, 15.7423341925), 4.1, -90, 60.8035955904)
                CenterArc((62.9494979328, 15.7423341925), 4.1, -29.1964044096, 9.807517652)
                CenterArc((67.7494979328, 14.7423341925), 1, -158.8315874625, 68.8315874625)
                CenterArc((67.7494979328, 14.7423341925), 1, -90, 90)
                CenterArc((67.7494979328, 14.7423341925), 1, 0, 48.0316993172)
                Line((68.4182172863, 15.4858491057), (68.1330446111, 15.7423341925))
            make_face()
            with BuildLine():
                CenterArc((67.7494979328, 14.7423341925), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2485852372, perimeter: 3.1240430423
            with BuildLine():
                CenterArc((62.9494979328, 15.7423341925), 4.1, -160.6111132424, 9.807517652)
                CenterArc((58.1494979328, 14.7423341925), 1, -90, 68.8315874625)
                Line((58.1494979328, 13.7423341925), (59.3703918991, 13.7423341925))
            make_face()
            # Profile area: 7.7819799037, perimeter: 20.4555846442
            with BuildLine():
                CenterArc((58.1494979328, 14.7423341925), 1, 180, 90)
                CenterArc((58.1494979328, 14.7423341925), 1, -90, 68.8315874625)
                CenterArc((62.9494979328, 15.7423341925), 4.1, -160.6111132424, 9.807517652)
                CenterArc((62.9494979328, 15.7423341925), 4.1, -150.8035955904, 60.8035955904)
                Line((62.9494979328, 12.6423341925), (62.9494979328, 11.6423341925))
                CenterArc((62.9494979328, 15.7423341925), 3.1, -180, 90)
                Line((59.8494979328, 15.7423341925), (57.7659512544, 15.7423341925))
                Line((57.4807785792, 15.4858491057), (57.7659512544, 15.7423341925))
                CenterArc((58.1494979328, 14.7423341925), 1, 131.9683006828, 48.0316993172)
            make_face()
            with BuildLine():
                CenterArc((58.1494979328, 14.7423341925), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2485852372, perimeter: 3.1240430423
            with BuildLine():
                CenterArc((67.7494979328, 14.7423341925), 1, -158.8315874625, 68.8315874625)
                CenterArc((62.9494979328, 15.7423341925), 4.1, -29.1964044096, 9.807517652)
                Line((66.5286039664, 13.7423341925), (67.7494979328, 13.7423341925))
            make_face()
            # Profile area: 42.6667985584, perimeter: 27.8298170975
            with BuildLine():
                Line((59.8494979328, 15.7423341925), (57.7659512544, 15.7423341925))
                CenterArc((62.9494979328, 15.7423341925), 3.1, -180, 90)
                CenterArc((62.9494979328, 15.7423341925), 3.1, -90, 90)
                Line((68.1330446111, 15.7423341925), (66.0494979328, 15.7423341925))
                Line((68.1330446111, 15.7423341925), (67.1542249625, 16.6226872709))
                CenterArc((68.0394247114, 17.6068956851), 1.3237238375, -156.510792748, 24.5424920651)
                CenterArc((62.9494979328, 15.7423341925), 4.1, 19.0314409251, 141.9371181498)
                CenterArc((57.8595711541, 17.6068956851), 1.3237238375, -48.0316993172, 24.5424920651)
                Line((57.7659512544, 15.7423341925), (58.744770903, 16.6226872709))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_49703_b92021be_0004():
    """Model: Sleeve 35x44x13,2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.5841809418, perimeter: 24.8185819634
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.32
        extrude(amount=1.32)
    return part.part


def model_49703_b92021be_0007():
    """Model: Sleeve 60x50x15,3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.6393797974, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.53
        extrude(amount=1.53)
    return part.part


def model_49703_b92021be_0014():
    """Model: Sleeve 35x44x15,2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.5841809418, perimeter: 24.8185819634
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.52
        extrude(amount=1.52)
    return part.part


def model_49812_47872520_0011():
    """Model: Electrode_Stand"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 26
            with BuildLine():
                Line((-3.5, 7.5), (-3.5, 3.5))
                Line((-3.5, 3.5), (5.5, 3.5))
                Line((5.5, 3.5), (5.5, 7.5))
                Line((5.5, 7.5), (-3.5, 7.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_49930_20f0e2ee_0003():
    """Model: Wooden Panel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 63.8826156511, perimeter: 59.8698226701
            with BuildLine():
                Line((-2.54, 25.4), (0, 25.4))
                Line((-2.54, 0), (-2.54, 25.4))
                Line((0, 0), (-2.54, 0))
                Line((0, 25.4), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-1.27, 7.62), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.27, 17.78), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_49930_20f0e2ee_0004():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # Symmetric extrude, each_side=30.48
        extrude(amount=30.48, both=True)
    return part.part


def model_50020_810cddd7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.5007223858, perimeter: 16.113234717
            with BuildLine():
                Line((0, 0), (0.5, 0))
                CenterArc((0.5, 1), 1, -90, 60.9217865104)
                CenterArc((2.5974970091, -0.1664074318), 1.4, 75, 75.9217865104)
                Line((2.9598436722, 1.185888725), (4.4, 0.8))
                Line((4.4, 0.8), (6, 0.8))
                Line((6.5, 1.3), (6, 0.8))
                Line((6.5, 1.7), (6.5, 1.3))
                Line((5.2349351573, 1.7), (6.5, 1.7))
                CenterArc((5.2349351573, 3.2), 1.5, -133.9455195623, 43.9455195623)
                CenterArc((3.5, 1.4), 1, 46.0544804377, 43.9455195623)
                Line((1, 2.4), (3.5, 2.4))
                Line((0, 1.4), (1, 2.4))
                Line((0, 0), (0, 1.4))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_50039_be53f8de_0018():
    """Model: mill pulley"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 108.0594044487, perimeter: 46.1001936115
            with BuildLine():
                CenterArc((2.5, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                Line((3.9999487555, 0.2386814949), (3.7270008737, 0.2386814949))
                Line((3.9999487555, -0.2613185051), (3.9999487555, 0.2386814949))
                Line((3.7223799078, -0.2613185051), (3.9999487555, -0.2613185051))
                CenterArc((2.5, 0), 1.25, 11.0079498821, 336.9250830076)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=11.6
        extrude(amount=11.6)
    return part.part


def model_50214_683032e0_0005():
    """Model: glass"""
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
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 28.401513221, perimeter: 20.7987043395
            with BuildLine():
                Line((-33.8127879766, 0.1496238437), (-38.8127449924, 0.149597971))
                _nurbs_edge([(-33.8127879766, 0.1496238437), (-33.8156331278, 0.2008077145), (-33.8211007877, 0.3003199471), (-33.8286343614, 0.4410218678), (-33.8373423252, 0.6114795547), (-33.8460508122, 0.7964221626), (-33.8527444544, 0.9546683866), (-33.8577566499, 1.0892000187), (-33.8616428859, 1.2050102102), (-33.8652594092, 1.3098119813), (-33.8697578483, 1.4140204635), (-33.8762361463, 1.5277818889), (-33.885480296, 1.6587701518), (-33.8975906403, 1.8090263519), (-33.9119512369, 1.9746237921), (-33.9275721348, 2.1484018841), (-33.9433396915, 2.3219391315), (-33.9582908979, 2.4877337709), (-33.9719079079, 2.6415244672), (-33.9843143627, 2.7838754607), (-33.9959821227, 2.9180484149), (-34.0074904121, 3.0482876513), (-34.019295735, 3.178150055), (-34.0314218539, 3.308322041), (-34.0435082884, 3.4367767242), (-34.0551722731, 3.5609490447), (-34.0662454948, 3.6791522736), (-34.0771421286, 3.7927070677), (-34.0888977899, 3.9064035234), (-34.1025991193, 4.0260334249), (-34.1190077361, 4.1567440051), (-34.1379722672, 4.3006715649), (-34.1583923272, 4.4562364572), (-34.1789664273, 4.6197495724), (-34.1987802808, 4.7865076625), (-34.2179065136, 4.9520197805), (-34.2381290064, 5.1133453797), (-34.2632126717, 5.2698515469), (-34.2978701753, 5.4222322081), (-34.346962882, 5.5718464416), (-34.4146261583, 5.7199458416), (-34.503387121, 5.8669190146), (-34.6133911304, 6.0116151201), (-34.7430325416, 6.1518003255), (-34.8894736507, 6.284523762), (-35.0492036681, 6.4065172523), (-35.2185742373, 6.5145768854), (-35.3943523229, 6.6059590844), (-35.5742419758, 6.6787533008), (-35.7567096869, 6.7317206013), (-35.9407630433, 6.7641403014), (-36.0889482334, 6.7734039937), (-36.2005373956, 6.7709412039), (-36.275113503, 6.7651234), (-36.3124163435, 6.7611753502)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 0.9999602291, 0.9999602291, 0.9999602291, 0.9999602291, 0.9999602291, 0.9999602291], 5)
                Line((-36.3124163435, 6.7611753502), (-36.3146281439, 6.7613087725))
                _nurbs_edge([(-38.8127449924, 0.149597971), (-38.8098998412, 0.2007818418), (-38.8044321812, 0.3002940744), (-38.7968986074, 0.4409959951), (-38.7881906436, 0.611453682), (-38.7794821566, 0.79639629), (-38.7727885145, 0.954642514), (-38.767776319, 1.0891741461), (-38.7638900831, 1.2049843376), (-38.7602735598, 1.3097861086), (-38.7557751207, 1.4139945909), (-38.7492968227, 1.5277560162), (-38.7400526729, 1.6587442792), (-38.7279423287, 1.8090004793), (-38.713581732, 1.9745979195), (-38.6979608341, 2.1483760115), (-38.6821932775, 2.3219132589), (-38.6672420711, 2.4877078982), (-38.6536250611, 2.6414985945), (-38.6412186063, 2.783849588), (-38.6295508463, 2.9180225422), (-38.6180425569, 3.0482617787), (-38.606237234, 3.1781241823), (-38.5941111151, 3.3082961684), (-38.5820246806, 3.4367508516), (-38.5703606959, 3.560923172), (-38.5592874742, 3.6791264009), (-38.5483908404, 3.7926811951), (-38.5366351791, 3.9063776508), (-38.5229338497, 4.0260075523), (-38.5065252329, 4.1567181324), (-38.4875607018, 4.3006456923), (-38.4671406418, 4.4562105846), (-38.4465665417, 4.6197236998), (-38.4267526882, 4.7864817898), (-38.4076264554, 4.9519939079), (-38.3874039625, 5.113319507), (-38.3623202973, 5.2698256743), (-38.3276627936, 5.4222063354), (-38.2785700869, 5.571820569), (-38.2109068106, 5.719919969), (-38.1221458479, 5.866893142), (-38.0121418385, 6.0115892475), (-37.8825004273, 6.1517744529), (-37.7360593183, 6.2844978894), (-37.5763293009, 6.4064913797), (-37.4069587317, 6.5145510128), (-37.2311806461, 6.6059332117), (-37.0512909932, 6.6787274282), (-36.868823282, 6.7316947287), (-36.6850677727, 6.7640619651), (-36.5371842985, 6.7733405713), (-36.4258987068, 6.7709350583), (-36.3516270052, 6.7651913205), (-36.3146281439, 6.7613087725)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 0.999798467, 0.999798467, 0.999798467, 0.999798467, 0.999798467, 0.999798467], 5)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_50214_683032e0_0006():
    """Model: handle glass"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1007798852, perimeter: 2.29226625
            with BuildLine():
                Line((-30.0149993283, 1.9500000291), (-29.9849993306, 1.9500000291))
                CenterArc((-29.9849993306, 1.9850000291), 0.035, -90, 90)
                Line((-29.9499993306, 1.9850000291), (-29.9491578572, 1.992454748))
                CenterArc((-28.6499993306, 1.9456880639), 1.3, 164.17337901, 13.7649964406)
                Line((-29.9007181268, 2.3002335371), (-29.8556862927, 2.4590909069))
                CenterArc((-30, 2.5), 0.15, -15.8266209899, 211.6532419799)
                Line((-30.099280532, 2.3002288062), (-30.1443137073, 2.4590909069))
                CenterArc((-31.3499993283, 1.9456833329), 1.3, 1.9491436352, 13.8774773548)
                Line((-30.0499993283, 1.9850000291), (-30.0507514947, 1.9898994695))
                CenterArc((-30.0149993283, 1.9850000291), 0.035, 180, 90)
            make_face()
            with BuildLine():
                CenterArc((-30, 2.5), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_50315_0f1419bf_0009():
    """Model: Phillips Screwdriver Small"""
    with BuildPart() as part:
        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1664027377, perimeter: 6.5956456009
            with BuildLine():
                CenterArc((-1.2266357872, -1.0116871696), 0.9511685946, -17.1677352032, 17.151941312)
                CenterArc((-0.2027719585, -1.7287781946), 0.4512538489, 55.0159642837, 49.7582871933)
                CenterArc((-0.2027719585, -1.7287781946), 0.4512538489, -34.9997824192, 90.0157467029)
                CenterArc((0.0060169592, -1.3721979646), 0.6360828794, -75.3515386899, 109.8187774646)
                Line((0.3304355207, -1.0120348005), (0.5304354382, -1.0122164535))
                Line((0.3304355207, 0.1879651995), (0.3304355207, -1.0120348005))
                Line((-0.2751364658, 0.1879651995), (0.3304355207, 0.1879651995))
                Line((-0.2754672287, -1.0119493644), (-0.2751364658, 0.1879651995))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2356119353, perimeter: 2.2413319651
            with BuildLine():
                Line((-0.8908788075, -2.7120796252), (-0.6453206129, -2.8840291323))
                Line((-0.6453206129, -2.8840291323), (-0.1494570344, -2.1768714383))
                CenterArc((-0.2027719585, -1.7287781946), 0.4512538489, -124.9840357163, 41.7692897147)
                Line((-0.8908788075, -2.7120796252), (-0.461497529, -2.0984958103))
            make_face()
            # Profile area: 0.234924792, perimeter: 2.2377194906
            with BuildLine():
                Line((-0.8908788075, -2.7120796252), (-0.461497529, -2.0984958103))
                CenterArc((-0.2027719585, -1.7287781946), 0.4512538489, -166.4996696421, 41.5156339258)
                Line((-0.6415570203, -1.8341238435), (-1.1363754415, -2.5400423259))
                Line((-1.1363754415, -2.5400423259), (-0.8908788075, -2.7120796252))
            make_face()
            # Profile area: 0.253972214, perimeter: 2.2555159996
            with BuildLine():
                CenterArc((-1.2266357872, -1.0116871696), 0.9511685946, -35.0287993182, 17.861064115)
                Line((-0.4477584127, -1.5576466286), (-0.6415570203, -1.8341238435))
                CenterArc((-0.2027719585, -1.7287781946), 0.4512538489, -166.4996696421, 41.5156339258)
                Line((-0.461497529, -2.0984958103), (0.0559536119, -1.3590605788))
                CenterArc((-0.2027719585, -1.7287781946), 0.4512538489, 55.0159642837, 49.7582871933)
            make_face()
            # Profile area: 0.2848089391, perimeter: 2.427238824
            with BuildLine():
                Line((-0.461497529, -2.0984958103), (0.0559536119, -1.3590605788))
                CenterArc((-0.2027719585, -1.7287781946), 0.4512538489, -124.9840357163, 41.7692897147)
                Line((-0.1494570344, -2.1768714383), (0.0437190002, -1.9013805067))
                Line((0.0437190002, -1.9013805067), (0.1668745372, -1.9876053654))
                CenterArc((-0.2027719585, -1.7287781946), 0.4512538489, -34.9997824192, 90.0157467029)
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


def model_50379_ebec8fae_0001():
    """Model: Drive Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            with Locations((-13.8277462773, -1.3034914106)):
                Circle(0.79375)
        # Symmetric extrude, each_side=15.24
        extrude(amount=15.24, both=True)
    return part.part


def model_50379_ebec8fae_0004():
    """Model: Drive Shaft 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            with Locations((-15.2399997711, 2.5399999619)):
                Circle(0.79375)
        # Symmetric extrude, each_side=10.16
        extrude(amount=10.16, both=True)
    return part.part


def model_50382_cb85058c_0009():
    """Model: Front Wing Big Insert v2"""
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
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.6374245264, perimeter: 14.586093392
            with BuildLine():
                Line((0, 0), (4.7277508695, 0.0000000007))
                _nurbs_edge([(0, 0), (-0.0063076373, 0.0306246558), (0.0312804441, 0.089406627), (0.2381277653, 0.1691616534), (0.7900616287, 0.2639001436), (1.797104919, 0.4033268369), (2.9363693016, 0.6119261229), (4.0182213335, 0.9274593373), (4.8886072205, 1.3563429693), (5.4619188141, 1.8581227187), (5.7747227966, 2.3145712927), (5.9364209265, 2.5746831497), (6.0533600324, 2.5180962798), (6.1448504861, 2.128243382), (6.1216668364, 1.5096825502), (5.8883527648, 0.8775657053), (5.4963755602, 0.4385170692), (5.1048075182, 0.1794297006), (4.8305925556, 0.0451433651), (4.7277508695, 0.0000000007)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.7280553128, 0.7280553128, 0.7280553128, 0.7280553128, 0.7280553128, 0.7280553128], 5)
            make_face()
        # OneSide extrude, distance=25.5
        extrude(amount=25.5)
    return part.part


def model_50382_cb85058c_0010():
    """Model: Steering Wheel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5753007155, perimeter: 12.7762027136
            with BuildLine():
                Line((0, 1.5), (0, 0))
                CenterArc((-0.5, 1.5), 0.5, 0, 90)
                Line((-2, 2), (-0.5, 2))
                CenterArc((-2, 1.5), 0.5, 90, 90)
                Line((-2.5, 0), (-2.5, 1.5))
                Line((0, 0), (-2.5, 0))
            make_face()
            with BuildLine():
                EllipticalCenterArc((-0.5000000075, 1.0000000149), 0.4999999851, 0.1000000015, 0, 360, 89.9999991462)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-2.0000000298, 1.0000000149), 0.4999999851, 0.1020620802, 0, 360, 89.9999965849)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_50409_4a322fbf_0006():
    """Model: lead"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0015705328, perimeter: 0.2394043773
            with BuildLine():
                Line((0.0475, -0.0475), (0.0475, -0.0625))
                Line((0.0475, -0.0625), (0.0745, -0.0625))
                CenterArc((0.0745, -0.0395), 0.023, -90, 90)
                Line((0.0975, -0.0395), (0.0975, -0.0308751047))
                CenterArc((0.1125, -0.0308751047), 0.015, 95, 85)
                Line((0.1111926639, -0.0159321842), (0.1225, -0.0149429205))
                Line((0.1211926639, 0), (0.1225, -0.0149429205))
                Line((0.1098853277, -0.0009892637), (0.1211926639, 0))
                CenterArc((0.1125, -0.0308751047), 0.03, 95, 85)
                Line((0.0825, -0.0395), (0.0825, -0.0308751047))
                CenterArc((0.0745, -0.0395), 0.008, -90, 90)
                Line((0.0475, -0.0475), (0.0745, -0.0475))
            make_face()
        # Symmetric extrude, each_side=0.01
        extrude(amount=0.01, both=True)
    return part.part


def model_50410_f8f03667_0003():
    """Model: watchPin v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)
    return part.part


def model_50410_f8f03667_0004():
    """Model: battery v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_50410_f8f03667_0007():
    """Model: caseBackPin v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)
    return part.part


def model_50410_f8f03667_0011():
    """Model: strapLoop v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.44, perimeter: 6
            with BuildLine():
                Line((-3, 0.6), (-3, 0))
                Line((-3, 0), (-0.6, 0))
                Line((-0.6, 0), (-0.6, 0.6))
                Line((-0.6, 0.6), (-3, 0.6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_50417_199cffee_0007():
    """Model: Bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1451.61, perimeter: 152.4
            with BuildLine():
                Line((-19.05, 19.05), (19.05, 19.05))
                Line((-19.05, -19.05), (-19.05, 19.05))
                Line((19.05, -19.05), (-19.05, -19.05))
                Line((19.05, 19.05), (19.05, -19.05))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_50417_199cffee_0008():
    """Model: Front"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72.5805, perimeter: 80.01
            with BuildLine():
                Line((19.05, 17.145), (19.05, 19.05))
                Line((19.05, 19.05), (-19.05, 19.05))
                Line((-19.05, 19.05), (-19.05, 17.145))
                Line((-19.05, 17.145), (19.05, 17.145))
            make_face()
        # OneSide extrude, distance=57.15
        extrude(amount=57.15)
    return part.part


def model_50479_a1f097b3_0001():
    """Model: Wing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.0342917353, perimeter: 23.7123889804
            with BuildLine():
                CenterArc((3.5, 1), 1.5, 0, 90)
                Line((3.5, 2.5), (-3.5, 2.5))
                CenterArc((-3.5, 1), 1.5, 90, 90)
                Line((-5, 1), (-5, 0))
                Line((-5, 0), (5, 0))
                Line((5, 0), (5, 1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_50479_a1f097b3_0017():
    """Model: Wheel v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4535674543, perimeter: 3.2986723237
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_50479_a1f097b3_0018():
    """Model: Main body v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.5356639019, perimeter: 11.2668240667
            with BuildLine():
                Line((-1.7472136179, 1.5000000224), (-3.5000000522, 1.5000000224))
                Line((-3.5000000522, 0), (-3.5000000522, 1.5000000224))
                Line((0.400000006, 0), (-3.5000000522, 0))
                Line((0.400000006, 1.5000000283), (0.400000006, 0))
                CenterArc((0.000000006, 1.5000000283), 0.4, 0, 90)
                Line((-1.0527864239, 1.9000000283), (0.000000006, 1.9000000283))
                CenterArc((-1.0527864239, 1.5000000283), 0.4, 90, 63.4349488229)
                Line((-1.3894427415, 1.7211145842), (-1.4105573003, 1.6788854665))
                CenterArc((-1.7472136179, 1.9000000224), 0.4, -90, 63.4349488229)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_50681_eb7a9f92_0000():
    """Model: Rect Button v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4800000143, perimeter: 2.8000000417
            with BuildLine():
                Line((0, 0.6000000089), (0, 0))
                Line((0, 0), (0.8000000119, 0))
                Line((0.8000000119, 0), (0.8000000119, 0.6000000089))
                Line((0.8000000119, 0.6000000089), (0, 0.6000000089))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_50681_eb7a9f92_0007():
    """Model: Strap Holder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7600000226, perimeter: 14.3415928801
            with BuildLine():
                CenterArc((-2.4500000402, 0.1499999985), 0.25, 180, 90)
                Line((-2.4500000402, -0.1000000015), (-0.1499999985, -0.1000000015))
                CenterArc((-0.1499999985, 0.1499999985), 0.25, -90, 90)
                Line((0.1000000015, 0.1499999985), (0.1000000015, 0.8500000164))
                CenterArc((-0.1499999985, 0.8500000164), 0.25, 0, 90)
                Line((-0.1499999985, 1.1000000164), (-2.4500000402, 1.1000000164))
                CenterArc((-2.4500000402, 0.8500000164), 0.25, 90, 90)
                Line((-2.7000000402, 0.8500000164), (-2.7000000402, 0.1499999985))
            make_face()
            with BuildLine():
                Line((-2.3500000387, 1.0000000149), (-0.25, 1.0000000149))
                CenterArc((-0.25, 0.7500000149), 0.25, 0, 90)
                Line((0, 0.7500000149), (0, 0.25))
                CenterArc((-0.25, 0.25), 0.25, -90, 90)
                Line((-0.25, 0), (-2.3500000387, 0))
                CenterArc((-2.3500000387, 0.25), 0.25, 180, 90)
                Line((-2.6000000387, 0.25), (-2.6000000387, 0.7500000149))
                CenterArc((-2.3500000387, 0.7500000149), 0.25, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_50681_eb7a9f92_0009():
    """Model: Circular Button v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_50681_eb7a9f92_0010():
    """Model: Buckle Hole Picker v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1885973867, perimeter: 2.6994611072
            with BuildLine():
                CenterArc((0, 0), 0.1341194732, -71.7090802762, 161.8257630838)
                Line((0.5133986609, 0.0284436935), (0.0420923219, -0.1273431174))
                CenterArc((1.1018523854, -1.751822358), 1.875, 90, 18.2909197238)
                Line((1.1102883103, 0.123177642), (1.1018523854, 0.123177642))
                CenterArc((1.1102883103, 0.148177642), 0.025, -90, 158.0779571053)
                Line((1.0172898462, 0.2125529309), (1.1196219281, 0.1713699592))
                CenterArc((0.7279476935, -0.5064089031), 0.775, 68.0779571053, 33.6324917448)
                Line((-0.000273134, 0.1341191951), (0.5706491445, 0.2524601017))
            make_face()
            # Profile area: 0.0249965997, perimeter: 1.4706463875
            with BuildLine():
                Line((-0.053059416, 0.123177642), (-0.000273134, 0.1341191951))
                CenterArc((0, 0), 0.1341194732, 113.3042148928, 174.9867048311)
                CenterArc((0, 0), 0.1341194732, -71.7090802762, 161.8257630838)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_50681_eb7a9f92_0011():
    """Model: Elliptical Button v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3769911297, perimeter: 2.210349249
            Ellipse(0.400000006, 0.3000000045)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_50681_eb7a9f92_0020():
    """Model: Hour Hand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1375751806, perimeter: 2.3531170412
            with BuildLine():
                Line((0.1846153851, 0.0769230759), (0, 1.0000000149))
                Line((0, 1.0000000149), (-0.1846153903, 0.0769230632))
                CenterArc((0, 0), 0.2, 22.6198646197, 134.7602747012)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_50717_f1aaa3b1_0000():
    """Model: Flashlight_Terminal v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1840124629, perimeter: 18.5858254913
            with BuildLine():
                Line((1.6063556719, 1.068413171), (1.6063556719, 1.088256921))
                Line((1.6063556719, 1.088256921), (-5.7815570738, 1.088256921))
                Line((-5.7815570738, 1.088256921), (-5.7815570738, -0.816743079))
                Line((-5.7815570738, -0.816743079), (-5.7617133238, -0.816743079))
                Line((-5.7617133238, -0.816743079), (-5.7617133238, 1.068413171))
                Line((-5.7617133238, 1.068413171), (1.6063556719, 1.068413171))
            make_face()
        # Symmetric extrude, each_side=0.15875
        extrude(amount=0.15875, both=True)
    return part.part


def model_50717_f1aaa3b1_0001():
    """Model: Flashlight_Terminal_2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1706907913, perimeter: 16.607347453
            with BuildLine():
                Line((2.3637516822, -0.0342671212), (2.3834835615, -0.0321510501))
                CenterArc((2.3256875491, -0.0383491658), 0.0581274091, 6.1210761003, 83.8789238997)
                Line((-4.0243124509, 0.0197782433), (2.3256875491, 0.0197782433))
                Line((-4.0243124509, 0.3372769733), (-4.0243124509, 0.0197782433))
                Line((-4.0639999509, 0.3372769733), (-4.0243124509, 0.3372769733))
                Line((-4.0639999509, 0.0197769733), (-4.0639999509, 0.3372769733))
                Line((-5.5700789237, 0.0197769673), (-4.0639999509, 0.0197769733))
                Line((-5.570065517, -0.0000667767), (-5.5700789237, 0.0197769673))
                Line((-5.570065517, -0.0000667767), (2.3256875491, -0.0000667767))
                CenterArc((2.3256875491, -0.0383491658), 0.0382823891, 6.1210761003, 83.8789238997)
            make_face()
        # Symmetric extrude, each_side=0.15875
        extrude(amount=0.15875, both=True)
    return part.part


def model_50717_f1aaa3b1_0002():
    """Model: Flashlight_Button v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3365561097, perimeter: 5.8196444968
            with BuildLine():
                Line((0, 0), (0, 0.3175))
                CenterArc((-0.127, 0.3175), 0.127, 0, 71.210397233)
                CenterArc((-1.1470598195, -2.6806893321), 3.2939640519, 71.210397233, 42.3510935948)
                CenterArc((-2.413, 0.22225), 0.127, 113.5614908278, 66.4385091722)
                Line((-2.54, 0), (-2.54, 0.22225))
                Line((0, 0), (-2.54, 0))
            make_face()
        # Symmetric extrude, each_side=0.47625
        extrude(amount=0.47625, both=True)
    return part.part


def model_50777_2934de55_0011():
    """Model: Date Viewer Glass v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.24, perimeter: 2
            with BuildLine():
                Line((0, 0.4), (0, 0))
                Line((0, 0), (0.6, 0))
                Line((0.6, 0), (0.6, 0.4))
                Line((0.6, 0.4), (0, 0.4))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_50777_2934de55_0014():
    """Model: Hole Holder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3945844326, perimeter: 4.1367212794
            with BuildLine():
                CenterArc((0, 0), 0.2, -44.3068685315, 149.6321771603)
                Line((0.8636116098, 0.2300133824), (0.1431218007, -0.1397002153))
                CenterArc((1.3201547279, -0.6596879052), 1, 99.7334359035, 17.4308292925)
                Line((1.5000000224, 0.3857669096), (1.1510901534, 0.3259170712))
                Line((1.7456765342, 0.3857669096), (1.5000000224, 0.3857669096))
                CenterArc((1.7456765342, 0.3957669096), 0.01, -90, 167.0814848173)
                Line((1.4075141994, 0.4835911242), (1.7479121852, 0.4055137996))
                CenterArc((1.0498100405, -1.0759112755), 1.6, 77.0814848173, 36.0532380397)
                Line((-0.0528598175, 0.1928881533), (0.4211788689, 0.3954224223))
            make_face()
            # Profile area: 0.0992663323, perimeter: 1.8197121543
            with BuildLine():
                Line((-0.1028404198, 0.1715338102), (-0.0528598175, 0.1928881533))
                CenterArc((0, 0), 0.2, 120.9441370852, 157.6912618382)
                Line((0.1431218007, -0.1397002153), (0.0300292392, -0.1977327611))
                CenterArc((0, 0), 0.2, -44.3068685315, 149.6321771603)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.09, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_50777_2934de55_0017():
    """Model: Button v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0, 0.4)):
                Circle(0.4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_50777_2934de55_0020():
    """Model: TimeKeeper v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0308309379, perimeter: 0.6574638592
            with BuildLine():
                CenterArc((0, 0), 0.1000000015, -147.2473237724, 16.3021308491)
                CenterArc((0, 0), 0.1000000015, -130.9451929233, 81.8903858466)
                Line((0.0599999987, -0.0699999984), (0.0655336811, -0.0755336809))
                Line((0.0799999982, -0.0499999989), (0.0599999987, -0.0699999984))
                Line((0.0841013756, -0.0541013763), (0.0799999982, -0.0499999989))
                CenterArc((0, 0), 0.1000000015, -32.7526762276, 111.2157176305)
                Line((0.0199999996, 0.089999998), (0.0199999996, 0.0979795913))
                Line((-0.0199999996, 0.089999998), (0.0199999996, 0.089999998))
                Line((-0.0199999996, 0.0979795913), (-0.0199999996, 0.089999998))
                CenterArc((0, 0), 0.1000000015, 101.5369585971, 111.2157176305)
            make_face()
            # Profile area: 0.0034959732, perimeter: 0.3187216813
            with BuildLine():
                CenterArc((0, 0.7099999841), 0.0400000159, 90, 150.0000138635)
                Line((-0.0199999996, 0.7099999841), (-0.0199999996, 0.6753589494))
                Line((0.0199999996, 0.7099999841), (-0.0199999996, 0.7099999841))
                Line((0.0199999996, 0.6753589494), (0.0199999996, 0.7099999841))
                CenterArc((0, 0.7099999841), 0.0400000159, -60.0000138635, 150.0000138635)
            make_face()
            # Profile area: 0.001530579, perimeter: 0.1511699679
            with BuildLine():
                CenterArc((0, 0.7099999841), 0.0400000159, -119.9999861365, 59.9999722729)
                Line((0.0199999996, 0.6753589494), (0.0199999996, 0.7099999841))
                Line((0.0199999996, 0.7099999841), (-0.0199999996, 0.7099999841))
                Line((-0.0199999996, 0.7099999841), (-0.0199999996, 0.6753589494))
            make_face()
            # Profile area: 0.0228962488, perimeter: 1.2369181987
            with BuildLine():
                CenterArc((0, 0), 0.1000000015, 78.4630414029, 23.0739171943)
                Line((0.0199999996, 0.0979795913), (0.0199999996, 0.6753589494))
                CenterArc((0, 0.7099999841), 0.0400000159, -119.9999861365, 59.9999722729)
                Line((-0.0199999996, 0.6753589494), (-0.0199999996, 0.0979795913))
            make_face()
            # Profile area: 0.003062866, perimeter: 0.2908937205
            with BuildLine():
                CenterArc((-0.5099999886, -0.4999999888), 0.0359151374, -130.6089755116, 152.4199834902)
                Line((-0.4766558557, -0.4866558555), (-0.4999999888, -0.5099999886))
                Line((-0.4999999888, -0.5099999886), (-0.5199999884, -0.489999989))
                Line((-0.5199999884, -0.489999989), (-0.4966558553, -0.4666558559))
                CenterArc((-0.5099999886, -0.4999999888), 0.0359151374, 68.1889920213, 151.2854506705)
                CenterArc((0, 0), 0.75, -135.8044077721, 0.4742827245)
            make_face()
            # Profile area: 0.0009914378, perimeter: 0.1235661141
            with BuildLine():
                CenterArc((0.5099999886, -0.4999999888), 0.0360012242, 111.8696851755, 46.2606296491)
                Line((0.4765896476, -0.4865896473), (0.4999999888, -0.5099999886))
                Line((0.4999999888, -0.5099999886), (0.5199999884, -0.489999989))
                Line((0.5199999884, -0.489999989), (0.4965896471, -0.4665896478))
            make_face()
            # Profile area: 0.0009889353, perimeter: 0.1233829048
            with BuildLine():
                Line((-0.5199999884, -0.489999989), (-0.4966558553, -0.4666558559))
                Line((-0.4999999888, -0.5099999886), (-0.5199999884, -0.489999989))
                Line((-0.4766558557, -0.4866558555), (-0.4999999888, -0.5099999886))
                CenterArc((-0.5099999886, -0.4999999888), 0.0359151374, 21.8110079787, 46.3779840426)
            make_face()
            # Profile area: 0.016396743, perimeter: 1.2221874161
            with BuildLine():
                CenterArc((0, 0), 0.1000000015, -49.0548070767, 16.3021308491)
                Line((0.0655336811, -0.0755336809), (0.4765896476, -0.4865896473))
                CenterArc((0.5099999886, -0.4999999888), 0.0360012242, 111.8696851755, 46.2606296491)
                Line((0.4965896471, -0.4665896478), (0.0841013756, -0.0541013763))
            make_face()
            # Profile area: 0.0030791959, perimeter: 0.2916169513
            with BuildLine():
                CenterArc((0.5099999886, -0.4999999888), 0.0360012242, -38.0262083422, 149.8958935176)
                Line((0.5199999884, -0.489999989), (0.4965896471, -0.4665896478))
                Line((0.4999999888, -0.5099999886), (0.5199999884, -0.489999989))
                Line((0.4765896476, -0.4865896473), (0.4999999888, -0.5099999886))
                CenterArc((0.5099999886, -0.4999999888), 0.0360012242, 158.1303148245, 151.0304263373)
                CenterArc((0, 0), 0.75, -44.7396183205, 0.6137694608)
            make_face()
            # Profile area: 0.0163992455, perimeter: 1.2223787366
            with BuildLine():
                CenterArc((-0.5099999886, -0.4999999888), 0.0359151374, 21.8110079787, 46.3779840426)
                Line((-0.0655336811, -0.0755336809), (-0.4766558557, -0.4866558555))
                CenterArc((0, 0), 0.1000000015, -147.2473237724, 16.3021308491)
                Line((-0.4966558553, -0.4666558559), (-0.0841013756, -0.0541013763))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_50778_c57149b9_0000():
    """Model: base rack floor beam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2164557564, 63.7852063529), x_dir=(1, 0, 0), z_dir=(0, 0.0033934908, 0.9999942421))):
            # Profile area: 0.387096, perimeter: 2.54
            with BuildLine():
                Line((-23.2752258589, 7.1249350381), (-22.5132258589, 7.1249350381))
                Line((-22.5132258589, 7.1249350381), (-22.5132258589, 7.3789350381))
                Line((-22.5132258589, 7.3789350381), (-22.5132258589, 7.6329350381))
                Line((-22.5132258589, 7.6329350381), (-23.2752258589, 7.6329350381))
                Line((-23.2752258589, 7.6329350381), (-23.2752258589, 7.1249350381))
            make_face()
        # OneSide extrude, distance=-32.35452
        extrude(amount=-32.35452)
    return part.part


def model_50778_c57149b9_0003():
    """Model: Inner Right Slant Beam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 109.5851475885, perimeter: 83.8469868463
            with BuildLine():
                CenterArc((-7.4602752609, 1.2278150397), 1.27, -173.8018918998, 83.8018918998)
                Line((-1.7539017088, -0.0421849603), (-7.4602752609, -0.0421849603))
                CenterArc((-1.7539017088, 0.5928150397), 0.635, -90, 140.1944289077)
                Line((-1.3473846151, 1.0806355523), (-30.48, 25.3578150397))
                CenterArc((-31.2930341876, 24.3821740146), 1.27, 50.1944289077, 180.0005552405)
                Line((-11.4650581097, 6.2056911017), (-32.1060589204, 23.4065251106))
                CenterArc((-16.4245666539, 0.2542808487), 7.747, 6.1981081002, 43.9963208076)
            make_face()
        # OneSide extrude, distance=1.778
        extrude(amount=1.778)
    return part.part


def model_50782_2d82ef9f_0003():
    """Model: Jack Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=8.3354945162
        extrude(amount=8.3354945162)
    return part.part


def model_50782_2d82ef9f_0005():
    """Model: Gear Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=10.4775
        extrude(amount=10.4775)
    return part.part


def model_50782_2d82ef9f_0006():
    """Model: Cam Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=9.8425
        extrude(amount=9.8425)
    return part.part


def model_50897_3be92e2f_0019():
    """Model: 2.5 inch motor support v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3185438272, perimeter: 29.2100009727
            with BuildLine():
                Line((0, 5.0800001621), (0, 0))
                Line((0, 0), (2.5400000811, 0))
                Line((2.5400000811, 0), (2.5400000811, 5.0800001621))
                Line((2.5400000811, 5.0800001621), (0, 5.0800001621))
            make_face()
            with BuildLine():
                Line((2.3812500811, 4.9212501621), (0.15875, 4.9212501621))
                Line((2.3812500811, 0.15875), (2.3812500811, 4.9212501621))
                Line((0.15875, 0.15875), (2.3812500811, 0.15875))
                Line((0.15875, 4.9212501621), (0.15875, 0.15875))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_50897_3be92e2f_0020():
    """Model: 20 inch straight cross bar v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3185438272, perimeter: 29.2100009727
            with BuildLine():
                Line((0, 5.0800001621), (0, 0))
                Line((0, 0), (2.5400000811, 0))
                Line((2.5400000811, 0), (2.5400000811, 5.0800001621))
                Line((2.5400000811, 5.0800001621), (0, 5.0800001621))
            make_face()
            with BuildLine():
                Line((2.3812500811, 4.9212501621), (0.15875, 4.9212501621))
                Line((2.3812500811, 0.15875), (2.3812500811, 4.9212501621))
                Line((0.15875, 0.15875), (2.3812500811, 0.15875))
                Line((0.15875, 4.9212501621), (0.15875, 0.15875))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=50.8
        extrude(amount=50.8)
    return part.part


def model_50897_3be92e2f_0024():
    """Model: 9 inch axle support bar v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.31854375, perimeter: 29.21
            with BuildLine():
                Line((2.54, 5.08), (0, 5.08))
                Line((0, 5.08), (0, 0))
                Line((0, 0), (2.54, 0))
                Line((2.54, 0), (2.54, 5.08))
            make_face()
            with BuildLine():
                Line((0.15875, 4.92125), (0.15875, 0.15875))
                Line((0.15875, 4.92125), (2.38125, 4.92125))
                Line((2.38125, 0.15875), (2.38125, 4.92125))
                Line((0.15875, 0.15875), (2.38125, 0.15875))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=22.86
        extrude(amount=22.86)
    return part.part


def model_50897_3be92e2f_0027():
    """Model: Seat Support v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.31854375, perimeter: 29.21
            with BuildLine():
                Line((0, 5.08), (0, 0))
                Line((0, 0), (2.54, 0))
                Line((2.54, 0), (2.54, 5.08))
                Line((2.54, 5.08), (0, 5.08))
            make_face()
            with BuildLine():
                Line((2.38125, 4.92125), (0.15875, 4.92125))
                Line((2.38125, 0.15875), (2.38125, 4.92125))
                Line((0.15875, 0.15875), (2.38125, 0.15875))
                Line((0.15875, 4.92125), (0.15875, 0.15875))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)
    return part.part


def model_50897_3be92e2f_0034():
    """Model: 1/4" nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3677458887, perimeter: 5.0744976709
            with BuildLine():
                Line((0.445908679, -0.2541766773), (0.4430777991, 0.2590799051))
                Line((0.4430777991, 0.2590799051), (-0.0028308799, 0.5132565825))
                Line((-0.0028308799, 0.5132565825), (-0.445908679, 0.2541766773))
                Line((-0.445908679, 0.2541766773), (-0.4430777991, -0.2590799051))
                Line((-0.4430777991, -0.2590799051), (0.0028308799, -0.5132565825))
                Line((0.0028308799, -0.5132565825), (0.445908679, -0.2541766773))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_50900_0326428a_0012():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.3293804003, perimeter: 42.798229715
            with BuildLine():
                CenterArc((-6.8, 0.7), 0.7, 180, 90)
                Line((9.3, 0), (-6.8, 0))
                CenterArc((9.3, 0.7), 0.7, -90, 90)
                Line((10, 3.8), (10, 0.7))
                CenterArc((9.3, 3.8), 0.7, 0, 90)
                Line((-6.8, 4.5), (9.3, 4.5))
                CenterArc((-6.8, 3.8), 0.7, 90, 90)
                Line((-7.5, 0.7), (-7.5, 3.8))
            make_face()
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)
    return part.part


def model_50903_f7c8e57e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.853981634, perimeter: 9.9345882658
            Circle(1.5811388301)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


def model_50903_f7c8e57e_0001():
    """Model: 12 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7123889804, perimeter: 22.5009588802
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5811388301, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_50914_67b32535_0002():
    """Model: cpart5 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 35.1415926536, perimeter: 24.2831853072
            with BuildLine():
                CenterArc((3.5, -1), 1, -90, 90)
                Line((4.5, 1), (4.5, -1))
                CenterArc((3.5, 1), 1, 0, 90)
                Line((-3.5, 2), (3.5, 2))
                CenterArc((-3.5, 1), 1, 90, 90)
                Line((-4.5, -1), (-4.5, 1))
                CenterArc((-3.5, -1), 1, 180, 90)
                Line((3.5, -2), (-3.5, -2))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_50947_49287c16_0007():
    """Model: Light Switch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 3.2290451208, perimeter: 6.3700374974
            with Locations((0, 154.939997673)):
                Circle(1.0138229554)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


def model_51022_47816098_0002():
    """Model: Frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3640484718, perimeter: 13.5088484104
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=155
        extrude(amount=155)
    return part.part


def model_51022_47816098_0004():
    """Model: fuel reservoir"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 122.1371669412, perimeter: 47.4247779608
            with BuildLine():
                Line((9, 0), (-9, 0))
                Line((-9, 0), (-9, -4))
                CenterArc((-6, -4), 3, 180, 90)
                Line((-6, -7), (6, -7))
                CenterArc((6, -4), 3, -90, 90)
                Line((9, -4), (9, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_51109_97b211c3_0008():
    """Model: Spacer v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2731153312, perimeter: 3.9100262167
            with BuildLine():
                CenterArc((0, 0), 0.381, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)
    return part.part


def model_51109_97b211c3_0009():
    """Model: 12 tooth compinion gear v1"""
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6182501438, perimeter: 10.9771480714
            with BuildLine():
                CenterArc((0, 0), 0.8889999866, -123.2085736605, 6.4171473209)
                _nurbs_edge([(-0.0497581379, -0.8876063902), (-0.0576340677, -0.8743399691), (-0.0670628099, -0.8566561701), (-0.0769549726, -0.834434204), (-0.0818125559, -0.8224542711), (-0.0859779718, -0.8111009473), (-0.0894988594, -0.8004064182), (-0.0924253923, -0.7904000948), (-0.0948051943, -0.7811095628), (-0.0966993697, -0.7725573273), (-0.0981299265, -0.7647711749), (-0.0992478356, -0.7577507779), (-0.0999866539, -0.7495258986), (-0.1020222226, -0.740351197), (-0.097372317, -0.7319308244), (-0.0950832355, -0.7245204582), (-0.0928613691, -0.7176713764), (-0.090982714, -0.7109203795), (-0.0893401248, -0.7042892289), (-0.0879569559, -0.6977754012), (-0.0868234418, -0.6913817812), (-0.0859390538, -0.6851089255), (-0.0853018026, -0.678956973), (-0.0849112788, -0.6729250719), (-0.0847682243, -0.6670114613), (-0.0848750912, -0.6612134146), (-0.0852364598, -0.6555272761), (-0.0858596293, -0.6499485749), (-0.0867553194, -0.6444722871), (-0.0879385064, -0.6390933292), (-0.0894293611, -0.6338074096), (-0.0912542129, -0.6286124092), (-0.0934463549, -0.6235105086), (-0.0960463388, -0.6185112868), (-0.0991011764, -0.6136359654), (-0.1026615256, -0.6089225782), (-0.1067759506, -0.6044317362), (-0.1114807651, -0.6002497953), (-0.1167881303, -0.5964925521), (-0.1226651068, -0.5932831403), (-0.1284006195, -0.5910445179), (-0.1396677427, -0.5878213834), (-0.1565854126, -0.5843847156), (-0.1729548784, -0.5789021222), (-0.1843240606, -0.576059877), (-0.1904104715, -0.5751308246), (-0.1971047884, -0.5749717684), (-0.2035797231, -0.5755719539), (-0.2097451824, -0.5768412137), (-0.2155537999, -0.5786731845), (-0.2209938464, -0.580974923), (-0.2260770741, -0.5836696563), (-0.2308283371, -0.5866991174), (-0.235277738, -0.5900214219), (-0.2394556063, -0.5936079984), (-0.2433896841, -0.5974403116), (-0.247103833, -0.6015070324), (-0.2506176674, -0.6058017917), (-0.2539466985, -0.6103215039), (-0.2571027221, -0.61506516), (-0.260094295, -0.6200329822), (-0.2629272115, -0.6252258465), (-0.2656049585, -0.630644888), (-0.268129059, -0.6362912608), (-0.2704995844, -0.6421659071), (-0.2727147423, -0.6482697015), (-0.2747737968, -0.6546024263), (-0.2766668482, -0.6611664657), (-0.2784153835, -0.6679523281), (-0.2799157317, -0.6749947402), (-0.281638512, -0.6825568462), (-0.281821762, -0.6921740557), (-0.288171967, -0.6991017959), (-0.292924242, -0.7058553412), (-0.2974025782, -0.7113762288), (-0.3025345529, -0.7174039562), (-0.3084510747, -0.7238633217), (-0.3151573097, -0.7307192574), (-0.3226949233, -0.7379217212), (-0.3310913659, -0.7454230113), (-0.3403753838, -0.7531725702), (-0.3505721408, -0.7611187048), (-0.370249988, -0.7754174106), (-0.3872574178, -0.7860176586), (-0.4007113836, -0.7935687515)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, -93.2085736605, 6.4171473209)
                _nurbs_edge([(0.4007113836, -0.7935687515), (0.3872574178, -0.7860176586), (0.370249988, -0.7754174106), (0.3505721408, -0.7611187048), (0.3403753838, -0.7531725702), (0.3310913659, -0.7454230113), (0.3226949233, -0.7379217212), (0.3151573097, -0.7307192574), (0.3084510747, -0.7238633217), (0.3025345529, -0.7174039562), (0.2974025782, -0.7113762288), (0.292924242, -0.7058553412), (0.288171967, -0.6991017959), (0.281821762, -0.6921740557), (0.281638512, -0.6825568462), (0.2799157317, -0.6749947402), (0.2784153835, -0.6679523281), (0.2766668482, -0.6611664657), (0.2747737968, -0.6546024263), (0.2727147423, -0.6482697015), (0.2704995844, -0.6421659071), (0.268129059, -0.6362912608), (0.2656049585, -0.630644888), (0.2629272115, -0.6252258465), (0.260094295, -0.6200329822), (0.2571027221, -0.61506516), (0.2539466985, -0.6103215039), (0.2506176674, -0.6058017917), (0.247103833, -0.6015070324), (0.2433896841, -0.5974403116), (0.2394556063, -0.5936079984), (0.235277738, -0.5900214219), (0.2308283371, -0.5866991174), (0.2260770741, -0.5836696563), (0.2209938464, -0.580974923), (0.2155537999, -0.5786731845), (0.2097451824, -0.5768412137), (0.2035797231, -0.5755719539), (0.1971047884, -0.5749717684), (0.1904104715, -0.5751308246), (0.1843240606, -0.576059877), (0.1729548784, -0.5789021222), (0.1565854126, -0.5843847156), (0.1396677427, -0.5878213834), (0.1284006195, -0.5910445179), (0.1226651068, -0.5932831403), (0.1167881303, -0.5964925521), (0.1114807651, -0.6002497953), (0.1067759506, -0.6044317362), (0.1026615256, -0.6089225782), (0.0991011764, -0.6136359654), (0.0960463388, -0.6185112868), (0.0934463549, -0.6235105086), (0.0912542129, -0.6286124092), (0.0894293611, -0.6338074096), (0.0879385064, -0.6390933292), (0.0867553194, -0.6444722871), (0.0858596293, -0.6499485749), (0.0852364598, -0.6555272761), (0.0848750912, -0.6612134146), (0.0847682243, -0.6670114613), (0.0849112788, -0.6729250719), (0.0853018026, -0.678956973), (0.0859390538, -0.6851089255), (0.0868234418, -0.6913817812), (0.0879569559, -0.6977754012), (0.0893401248, -0.7042892289), (0.090982714, -0.7109203795), (0.0928613691, -0.7176713764), (0.0950832355, -0.7245204582), (0.097372317, -0.7319308244), (0.1020222226, -0.740351197), (0.0999866539, -0.7495258986), (0.0992478356, -0.7577507779), (0.0981299265, -0.7647711749), (0.0966993697, -0.7725573273), (0.0948051943, -0.7811095628), (0.0924253923, -0.7904000948), (0.0894988594, -0.8004064182), (0.0859779718, -0.8111009473), (0.0818125559, -0.8224542711), (0.0769549726, -0.834434204), (0.0670628099, -0.8566561701), (0.0576340677, -0.8743399691), (0.0497581379, -0.8876063902)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, -63.2085736605, 6.4171473209)
                _nurbs_edge([(0.7438106135, -0.4868950066), (0.7283835909, -0.4870825513), (0.7083546007, -0.4864061821), (0.6841637322, -0.4838620632), (0.6713600143, -0.4820788873), (0.6594450395, -0.4800095814), (0.6484228618, -0.4777114949), (0.6382938651, -0.4752427851), (0.6290581274, -0.4726584881), (0.6207045865, -0.4700227744), (0.6132463023, -0.4673685966), (0.6066075056, -0.4648265359), (0.599115142, -0.4613539316), (0.590151833, -0.4585294351), (0.5851845292, -0.4502923124), (0.5799115046, -0.4446047266), (0.575090959, -0.4392559928), (0.5701837518, -0.4342535314), (0.5652623015, -0.4295154321), (0.5603127456, -0.4250606588), (0.5553424654, -0.4208821968), (0.550352207, -0.4169798666), (0.5453430854, -0.4133520145), (0.5403145677, -0.4099978604), (0.535264758, -0.4069171663), (0.5301900688, -0.4041106925), (0.5250850441, -0.4015805776), (0.5199421624, -0.3993309076), (0.5147517129, -0.3973684541), (0.5095018053, -0.3957036451), (0.5041786373, -0.3943518034), (0.498767209, -0.3933346712), (0.4932527625, -0.3926821715), (0.4876233175, -0.3924342128), (0.4818737465, -0.3926421191), (0.4760116589, -0.3933687783), (0.4700652631, -0.3946865538), (0.4640911888, -0.3966700722), (0.4581836381, -0.3993877637), (0.4524657178, -0.4028726688), (0.4476592576, -0.4067204573), (0.4392343796, -0.4148665049), (0.427799303, -0.427799303), (0.4148665049, -0.4392343796), (0.4067204573, -0.4476592576), (0.4028726688, -0.4524657178), (0.3993877637, -0.4581836381), (0.3966700722, -0.4640911888), (0.3946865538, -0.4700652631), (0.3933687783, -0.4760116589), (0.3926421191, -0.4818737465), (0.3924342128, -0.4876233175), (0.3926821715, -0.4932527625), (0.3933346712, -0.498767209), (0.3943518034, -0.5041786373), (0.3957036451, -0.5095018053), (0.3973684541, -0.5147517129), (0.3993309076, -0.5199421624), (0.4015805776, -0.5250850441), (0.4041106925, -0.5301900688), (0.4069171663, -0.535264758), (0.4099978604, -0.5403145677), (0.4133520145, -0.5453430854), (0.4169798666, -0.550352207), (0.4208821968, -0.5553424654), (0.4250606588, -0.5603127456), (0.4295154321, -0.5652623015), (0.4342535314, -0.5701837518), (0.4392559928, -0.575090959), (0.4446047266, -0.5799115046), (0.4502923124, -0.5851845292), (0.4585294351, -0.590151833), (0.4613539316, -0.599115142), (0.4648265359, -0.6066075056), (0.4673685966, -0.6132463023), (0.4700227744, -0.6207045865), (0.4726584881, -0.6290581274), (0.4752427851, -0.6382938651), (0.4777114949, -0.6484228618), (0.4800095814, -0.6594450395), (0.4820788873, -0.6713600143), (0.4838620632, -0.6841637322), (0.4864061821, -0.7083546007), (0.4870825513, -0.7283835909), (0.4868950066, -0.7438106135)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, -33.2085736605, 6.4171473209)
                _nurbs_edge([(0.8876063902, -0.0497581379), (0.8743399691, -0.0576340677), (0.8566561701, -0.0670628099), (0.834434204, -0.0769549726), (0.8224542711, -0.0818125559), (0.8111009473, -0.0859779718), (0.8004064182, -0.0894988594), (0.7904000948, -0.0924253923), (0.7811095628, -0.0948051943), (0.7725573273, -0.0966993697), (0.7647711749, -0.0981299265), (0.7577507779, -0.0992478356), (0.7495258986, -0.0999866539), (0.740351197, -0.1020222226), (0.7319308244, -0.097372317), (0.7245204582, -0.0950832355), (0.7176713764, -0.0928613691), (0.7109203795, -0.090982714), (0.7042892289, -0.0893401248), (0.6977754012, -0.0879569559), (0.6913817812, -0.0868234418), (0.6851089255, -0.0859390538), (0.678956973, -0.0853018026), (0.6729250719, -0.0849112788), (0.6670114613, -0.0847682243), (0.6612134146, -0.0848750912), (0.6555272761, -0.0852364598), (0.6499485749, -0.0858596293), (0.6444722871, -0.0867553194), (0.6390933292, -0.0879385064), (0.6338074096, -0.0894293611), (0.6286124092, -0.0912542129), (0.6235105086, -0.0934463549), (0.6185112868, -0.0960463388), (0.6136359654, -0.0991011764), (0.6089225782, -0.1026615256), (0.6044317362, -0.1067759506), (0.6002497953, -0.1114807651), (0.5964925521, -0.1167881303), (0.5932831403, -0.1226651068), (0.5910445179, -0.1284006195), (0.5878213834, -0.1396677427), (0.5843847156, -0.1565854126), (0.5789021222, -0.1729548784), (0.576059877, -0.1843240606), (0.5751308246, -0.1904104715), (0.5749717684, -0.1971047884), (0.5755719539, -0.2035797231), (0.5768412137, -0.2097451824), (0.5786731845, -0.2155537999), (0.580974923, -0.2209938464), (0.5836696563, -0.2260770741), (0.5866991174, -0.2308283371), (0.5900214219, -0.235277738), (0.5936079984, -0.2394556063), (0.5974403116, -0.2433896841), (0.6015070324, -0.247103833), (0.6058017917, -0.2506176674), (0.6103215039, -0.2539466985), (0.61506516, -0.2571027221), (0.6200329822, -0.260094295), (0.6252258465, -0.2629272115), (0.630644888, -0.2656049585), (0.6362912608, -0.268129059), (0.6421659071, -0.2704995844), (0.6482697015, -0.2727147423), (0.6546024263, -0.2747737968), (0.6611664657, -0.2766668482), (0.6679523281, -0.2784153835), (0.6749947402, -0.2799157317), (0.6825568462, -0.281638512), (0.6921740557, -0.281821762), (0.6991017959, -0.288171967), (0.7058553412, -0.292924242), (0.7113762288, -0.2974025782), (0.7174039562, -0.3025345529), (0.7238633217, -0.3084510747), (0.7307192574, -0.3151573097), (0.7379217212, -0.3226949233), (0.7454230113, -0.3310913659), (0.7531725702, -0.3403753838), (0.7611187048, -0.3505721408), (0.7754174106, -0.370249988), (0.7860176586, -0.3872574178), (0.7935687515, -0.4007113836)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, -3.2085736605, 6.4171473209)
                _nurbs_edge([(0.7935687515, 0.4007113836), (0.7860176586, 0.3872574178), (0.7754174106, 0.370249988), (0.7611187048, 0.3505721408), (0.7531725702, 0.3403753838), (0.7454230113, 0.3310913659), (0.7379217212, 0.3226949233), (0.7307192574, 0.3151573097), (0.7238633217, 0.3084510747), (0.7174039562, 0.3025345529), (0.7113762288, 0.2974025782), (0.7058553412, 0.292924242), (0.6991017959, 0.288171967), (0.6921740557, 0.281821762), (0.6825568462, 0.281638512), (0.6749947402, 0.2799157317), (0.6679523281, 0.2784153835), (0.6611664657, 0.2766668482), (0.6546024263, 0.2747737968), (0.6482697015, 0.2727147423), (0.6421659071, 0.2704995844), (0.6362912608, 0.268129059), (0.630644888, 0.2656049585), (0.6252258465, 0.2629272115), (0.6200329822, 0.260094295), (0.61506516, 0.2571027221), (0.6103215039, 0.2539466985), (0.6058017917, 0.2506176674), (0.6015070324, 0.247103833), (0.5974403116, 0.2433896841), (0.5936079984, 0.2394556063), (0.5900214219, 0.235277738), (0.5866991174, 0.2308283371), (0.5836696563, 0.2260770741), (0.580974923, 0.2209938464), (0.5786731845, 0.2155537999), (0.5768412137, 0.2097451824), (0.5755719539, 0.2035797231), (0.5749717684, 0.1971047884), (0.5751308246, 0.1904104715), (0.576059877, 0.1843240606), (0.5789021222, 0.1729548784), (0.5843847156, 0.1565854126), (0.5878213834, 0.1396677427), (0.5910445179, 0.1284006195), (0.5932831403, 0.1226651068), (0.5964925521, 0.1167881303), (0.6002497953, 0.1114807651), (0.6044317362, 0.1067759506), (0.6089225782, 0.1026615256), (0.6136359654, 0.0991011764), (0.6185112868, 0.0960463388), (0.6235105086, 0.0934463549), (0.6286124092, 0.0912542129), (0.6338074096, 0.0894293611), (0.6390933292, 0.0879385064), (0.6444722871, 0.0867553194), (0.6499485749, 0.0858596293), (0.6555272761, 0.0852364598), (0.6612134146, 0.0848750912), (0.6670114613, 0.0847682243), (0.6729250719, 0.0849112788), (0.678956973, 0.0853018026), (0.6851089255, 0.0859390538), (0.6913817812, 0.0868234418), (0.6977754012, 0.0879569559), (0.7042892289, 0.0893401248), (0.7109203795, 0.090982714), (0.7176713764, 0.0928613691), (0.7245204582, 0.0950832355), (0.7319308244, 0.097372317), (0.740351197, 0.1020222226), (0.7495258986, 0.0999866539), (0.7577507779, 0.0992478356), (0.7647711749, 0.0981299265), (0.7725573273, 0.0966993697), (0.7811095628, 0.0948051943), (0.7904000948, 0.0924253923), (0.8004064182, 0.0894988594), (0.8111009473, 0.0859779718), (0.8224542711, 0.0818125559), (0.834434204, 0.0769549726), (0.8566561701, 0.0670628099), (0.8743399691, 0.0576340677), (0.8876063902, 0.0497581379)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, 26.7914263395, 6.4171473209)
                _nurbs_edge([(0.4868950066, 0.7438106135), (0.4870825513, 0.7283835909), (0.4864061821, 0.7083546007), (0.4838620632, 0.6841637322), (0.4820788873, 0.6713600143), (0.4800095814, 0.6594450395), (0.4777114949, 0.6484228618), (0.4752427851, 0.6382938651), (0.4726584881, 0.6290581274), (0.4700227744, 0.6207045865), (0.4673685966, 0.6132463023), (0.4648265359, 0.6066075056), (0.4613539316, 0.599115142), (0.4585294351, 0.590151833), (0.4502923124, 0.5851845292), (0.4446047266, 0.5799115046), (0.4392559928, 0.575090959), (0.4342535314, 0.5701837518), (0.4295154321, 0.5652623015), (0.4250606588, 0.5603127456), (0.4208821968, 0.5553424654), (0.4169798666, 0.550352207), (0.4133520145, 0.5453430854), (0.4099978604, 0.5403145677), (0.4069171663, 0.535264758), (0.4041106925, 0.5301900688), (0.4015805776, 0.5250850441), (0.3993309076, 0.5199421624), (0.3973684541, 0.5147517129), (0.3957036451, 0.5095018053), (0.3943518034, 0.5041786373), (0.3933346712, 0.498767209), (0.3926821715, 0.4932527625), (0.3924342128, 0.4876233175), (0.3926421191, 0.4818737465), (0.3933687783, 0.4760116589), (0.3946865538, 0.4700652631), (0.3966700722, 0.4640911888), (0.3993877637, 0.4581836381), (0.4028726688, 0.4524657178), (0.4067204573, 0.4476592576), (0.4148665049, 0.4392343796), (0.427799303, 0.427799303), (0.4392343796, 0.4148665049), (0.4476592576, 0.4067204573), (0.4524657178, 0.4028726688), (0.4581836381, 0.3993877637), (0.4640911888, 0.3966700722), (0.4700652631, 0.3946865538), (0.4760116589, 0.3933687783), (0.4818737465, 0.3926421191), (0.4876233175, 0.3924342128), (0.4932527625, 0.3926821715), (0.498767209, 0.3933346712), (0.5041786373, 0.3943518034), (0.5095018053, 0.3957036451), (0.5147517129, 0.3973684541), (0.5199421624, 0.3993309076), (0.5250850441, 0.4015805776), (0.5301900688, 0.4041106925), (0.535264758, 0.4069171663), (0.5403145677, 0.4099978604), (0.5453430854, 0.4133520145), (0.550352207, 0.4169798666), (0.5553424654, 0.4208821968), (0.5603127456, 0.4250606588), (0.5652623015, 0.4295154321), (0.5701837518, 0.4342535314), (0.575090959, 0.4392559928), (0.5799115046, 0.4446047266), (0.5851845292, 0.4502923124), (0.590151833, 0.4585294351), (0.599115142, 0.4613539316), (0.6066075056, 0.4648265359), (0.6132463023, 0.4673685966), (0.6207045865, 0.4700227744), (0.6290581274, 0.4726584881), (0.6382938651, 0.4752427851), (0.6484228618, 0.4777114949), (0.6594450395, 0.4800095814), (0.6713600143, 0.4820788873), (0.6841637322, 0.4838620632), (0.7083546007, 0.4864061821), (0.7283835909, 0.4870825513), (0.7438106135, 0.4868950066)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, 56.7914263395, 6.4171473209)
                _nurbs_edge([(0.0497581379, 0.8876063902), (0.0576340677, 0.8743399691), (0.0670628099, 0.8566561701), (0.0769549726, 0.834434204), (0.0818125559, 0.8224542711), (0.0859779718, 0.8111009473), (0.0894988594, 0.8004064182), (0.0924253923, 0.7904000948), (0.0948051943, 0.7811095628), (0.0966993697, 0.7725573273), (0.0981299265, 0.7647711749), (0.0992478356, 0.7577507779), (0.0999866539, 0.7495258986), (0.1020222226, 0.740351197), (0.097372317, 0.7319308244), (0.0950832355, 0.7245204582), (0.0928613691, 0.7176713764), (0.090982714, 0.7109203795), (0.0893401248, 0.7042892289), (0.0879569559, 0.6977754012), (0.0868234418, 0.6913817812), (0.0859390538, 0.6851089255), (0.0853018026, 0.678956973), (0.0849112788, 0.6729250719), (0.0847682243, 0.6670114613), (0.0848750912, 0.6612134146), (0.0852364598, 0.6555272761), (0.0858596293, 0.6499485749), (0.0867553194, 0.6444722871), (0.0879385064, 0.6390933292), (0.0894293611, 0.6338074096), (0.0912542129, 0.6286124092), (0.0934463549, 0.6235105086), (0.0960463388, 0.6185112868), (0.0991011764, 0.6136359654), (0.1026615256, 0.6089225782), (0.1067759506, 0.6044317362), (0.1114807651, 0.6002497953), (0.1167881303, 0.5964925521), (0.1226651068, 0.5932831403), (0.1284006195, 0.5910445179), (0.1396677427, 0.5878213834), (0.1565854126, 0.5843847156), (0.1729548784, 0.5789021222), (0.1843240606, 0.576059877), (0.1904104715, 0.5751308246), (0.1971047884, 0.5749717684), (0.2035797231, 0.5755719539), (0.2097451824, 0.5768412137), (0.2155537999, 0.5786731845), (0.2209938464, 0.580974923), (0.2260770741, 0.5836696563), (0.2308283371, 0.5866991174), (0.235277738, 0.5900214219), (0.2394556063, 0.5936079984), (0.2433896841, 0.5974403116), (0.247103833, 0.6015070324), (0.2506176674, 0.6058017917), (0.2539466985, 0.6103215039), (0.2571027221, 0.61506516), (0.260094295, 0.6200329822), (0.2629272115, 0.6252258465), (0.2656049585, 0.630644888), (0.268129059, 0.6362912608), (0.2704995844, 0.6421659071), (0.2727147423, 0.6482697015), (0.2747737968, 0.6546024263), (0.2766668482, 0.6611664657), (0.2784153835, 0.6679523281), (0.2799157317, 0.6749947402), (0.281638512, 0.6825568462), (0.281821762, 0.6921740557), (0.288171967, 0.6991017959), (0.292924242, 0.7058553412), (0.2974025782, 0.7113762288), (0.3025345529, 0.7174039562), (0.3084510747, 0.7238633217), (0.3151573097, 0.7307192574), (0.3226949233, 0.7379217212), (0.3310913659, 0.7454230113), (0.3403753838, 0.7531725702), (0.3505721408, 0.7611187048), (0.370249988, 0.7754174106), (0.3872574178, 0.7860176586), (0.4007113836, 0.7935687515)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, 86.7914263395, 6.4171473209)
                _nurbs_edge([(-0.4007113836, 0.7935687515), (-0.3872574178, 0.7860176586), (-0.370249988, 0.7754174106), (-0.3505721408, 0.7611187048), (-0.3403753838, 0.7531725702), (-0.3310913659, 0.7454230113), (-0.3226949233, 0.7379217212), (-0.3151573097, 0.7307192574), (-0.3084510747, 0.7238633217), (-0.3025345529, 0.7174039562), (-0.2974025782, 0.7113762288), (-0.292924242, 0.7058553412), (-0.288171967, 0.6991017959), (-0.281821762, 0.6921740557), (-0.281638512, 0.6825568462), (-0.2799157317, 0.6749947402), (-0.2784153835, 0.6679523281), (-0.2766668482, 0.6611664657), (-0.2747737968, 0.6546024263), (-0.2727147423, 0.6482697015), (-0.2704995844, 0.6421659071), (-0.268129059, 0.6362912608), (-0.2656049585, 0.630644888), (-0.2629272115, 0.6252258465), (-0.260094295, 0.6200329822), (-0.2571027221, 0.61506516), (-0.2539466985, 0.6103215039), (-0.2506176674, 0.6058017917), (-0.247103833, 0.6015070324), (-0.2433896841, 0.5974403116), (-0.2394556063, 0.5936079984), (-0.235277738, 0.5900214219), (-0.2308283371, 0.5866991174), (-0.2260770741, 0.5836696563), (-0.2209938464, 0.580974923), (-0.2155537999, 0.5786731845), (-0.2097451824, 0.5768412137), (-0.2035797231, 0.5755719539), (-0.1971047884, 0.5749717684), (-0.1904104715, 0.5751308246), (-0.1843240606, 0.576059877), (-0.1729548784, 0.5789021222), (-0.1565854126, 0.5843847156), (-0.1396677427, 0.5878213834), (-0.1284006195, 0.5910445179), (-0.1226651068, 0.5932831403), (-0.1167881303, 0.5964925521), (-0.1114807651, 0.6002497953), (-0.1067759506, 0.6044317362), (-0.1026615256, 0.6089225782), (-0.0991011764, 0.6136359654), (-0.0960463388, 0.6185112868), (-0.0934463549, 0.6235105086), (-0.0912542129, 0.6286124092), (-0.0894293611, 0.6338074096), (-0.0879385064, 0.6390933292), (-0.0867553194, 0.6444722871), (-0.0858596293, 0.6499485749), (-0.0852364598, 0.6555272761), (-0.0848750912, 0.6612134146), (-0.0847682243, 0.6670114613), (-0.0849112788, 0.6729250719), (-0.0853018026, 0.678956973), (-0.0859390538, 0.6851089255), (-0.0868234418, 0.6913817812), (-0.0879569559, 0.6977754012), (-0.0893401248, 0.7042892289), (-0.090982714, 0.7109203795), (-0.0928613691, 0.7176713764), (-0.0950832355, 0.7245204582), (-0.097372317, 0.7319308244), (-0.1020222226, 0.740351197), (-0.0999866539, 0.7495258986), (-0.0992478356, 0.7577507779), (-0.0981299265, 0.7647711749), (-0.0966993697, 0.7725573273), (-0.0948051943, 0.7811095628), (-0.0924253923, 0.7904000948), (-0.0894988594, 0.8004064182), (-0.0859779718, 0.8111009473), (-0.0818125559, 0.8224542711), (-0.0769549726, 0.834434204), (-0.0670628099, 0.8566561701), (-0.0576340677, 0.8743399691), (-0.0497581379, 0.8876063902)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, 116.7914263395, 6.4171473209)
                _nurbs_edge([(-0.7438106135, 0.4868950066), (-0.7283835909, 0.4870825513), (-0.7083546007, 0.4864061821), (-0.6841637322, 0.4838620632), (-0.6713600143, 0.4820788873), (-0.6594450395, 0.4800095814), (-0.6484228618, 0.4777114949), (-0.6382938651, 0.4752427851), (-0.6290581274, 0.4726584881), (-0.6207045865, 0.4700227744), (-0.6132463023, 0.4673685966), (-0.6066075056, 0.4648265359), (-0.599115142, 0.4613539316), (-0.590151833, 0.4585294351), (-0.5851845292, 0.4502923124), (-0.5799115046, 0.4446047266), (-0.575090959, 0.4392559928), (-0.5701837518, 0.4342535314), (-0.5652623015, 0.4295154321), (-0.5603127456, 0.4250606588), (-0.5553424654, 0.4208821968), (-0.550352207, 0.4169798666), (-0.5453430854, 0.4133520145), (-0.5403145677, 0.4099978604), (-0.535264758, 0.4069171663), (-0.5301900688, 0.4041106925), (-0.5250850441, 0.4015805776), (-0.5199421624, 0.3993309076), (-0.5147517129, 0.3973684541), (-0.5095018053, 0.3957036451), (-0.5041786373, 0.3943518034), (-0.498767209, 0.3933346712), (-0.4932527625, 0.3926821715), (-0.4876233175, 0.3924342128), (-0.4818737465, 0.3926421191), (-0.4760116589, 0.3933687783), (-0.4700652631, 0.3946865538), (-0.4640911888, 0.3966700722), (-0.4581836381, 0.3993877637), (-0.4524657178, 0.4028726688), (-0.4476592576, 0.4067204573), (-0.4392343796, 0.4148665049), (-0.427799303, 0.427799303), (-0.4148665049, 0.4392343796), (-0.4067204573, 0.4476592576), (-0.4028726688, 0.4524657178), (-0.3993877637, 0.4581836381), (-0.3966700722, 0.4640911888), (-0.3946865538, 0.4700652631), (-0.3933687783, 0.4760116589), (-0.3926421191, 0.4818737465), (-0.3924342128, 0.4876233175), (-0.3926821715, 0.4932527625), (-0.3933346712, 0.498767209), (-0.3943518034, 0.5041786373), (-0.3957036451, 0.5095018053), (-0.3973684541, 0.5147517129), (-0.3993309076, 0.5199421624), (-0.4015805776, 0.5250850441), (-0.4041106925, 0.5301900688), (-0.4069171663, 0.535264758), (-0.4099978604, 0.5403145677), (-0.4133520145, 0.5453430854), (-0.4169798666, 0.550352207), (-0.4208821968, 0.5553424654), (-0.4250606588, 0.5603127456), (-0.4295154321, 0.5652623015), (-0.4342535314, 0.5701837518), (-0.4392559928, 0.575090959), (-0.4446047266, 0.5799115046), (-0.4502923124, 0.5851845292), (-0.4585294351, 0.590151833), (-0.4613539316, 0.599115142), (-0.4648265359, 0.6066075056), (-0.4673685966, 0.6132463023), (-0.4700227744, 0.6207045865), (-0.4726584881, 0.6290581274), (-0.4752427851, 0.6382938651), (-0.4777114949, 0.6484228618), (-0.4800095814, 0.6594450395), (-0.4820788873, 0.6713600143), (-0.4838620632, 0.6841637322), (-0.4864061821, 0.7083546007), (-0.4870825513, 0.7283835909), (-0.4868950066, 0.7438106135)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, 146.7914263395, 6.4171473209)
                _nurbs_edge([(-0.8876063902, 0.0497581379), (-0.8743399691, 0.0576340677), (-0.8566561701, 0.0670628099), (-0.834434204, 0.0769549726), (-0.8224542711, 0.0818125559), (-0.8111009473, 0.0859779718), (-0.8004064182, 0.0894988594), (-0.7904000948, 0.0924253923), (-0.7811095628, 0.0948051943), (-0.7725573273, 0.0966993697), (-0.7647711749, 0.0981299265), (-0.7577507779, 0.0992478356), (-0.7495258986, 0.0999866539), (-0.740351197, 0.1020222226), (-0.7319308244, 0.097372317), (-0.7245204582, 0.0950832355), (-0.7176713764, 0.0928613691), (-0.7109203795, 0.090982714), (-0.7042892289, 0.0893401248), (-0.6977754012, 0.0879569559), (-0.6913817812, 0.0868234418), (-0.6851089255, 0.0859390538), (-0.678956973, 0.0853018026), (-0.6729250719, 0.0849112788), (-0.6670114613, 0.0847682243), (-0.6612134146, 0.0848750912), (-0.6555272761, 0.0852364598), (-0.6499485749, 0.0858596293), (-0.6444722871, 0.0867553194), (-0.6390933292, 0.0879385064), (-0.6338074096, 0.0894293611), (-0.6286124092, 0.0912542129), (-0.6235105086, 0.0934463549), (-0.6185112868, 0.0960463388), (-0.6136359654, 0.0991011764), (-0.6089225782, 0.1026615256), (-0.6044317362, 0.1067759506), (-0.6002497953, 0.1114807651), (-0.5964925521, 0.1167881303), (-0.5932831403, 0.1226651068), (-0.5910445179, 0.1284006195), (-0.5878213834, 0.1396677427), (-0.5843847156, 0.1565854126), (-0.5789021222, 0.1729548784), (-0.576059877, 0.1843240606), (-0.5751308246, 0.1904104715), (-0.5749717684, 0.1971047884), (-0.5755719539, 0.2035797231), (-0.5768412137, 0.2097451824), (-0.5786731845, 0.2155537999), (-0.580974923, 0.2209938464), (-0.5836696563, 0.2260770741), (-0.5866991174, 0.2308283371), (-0.5900214219, 0.235277738), (-0.5936079984, 0.2394556063), (-0.5974403116, 0.2433896841), (-0.6015070324, 0.247103833), (-0.6058017917, 0.2506176674), (-0.6103215039, 0.2539466985), (-0.61506516, 0.2571027221), (-0.6200329822, 0.260094295), (-0.6252258465, 0.2629272115), (-0.630644888, 0.2656049585), (-0.6362912608, 0.268129059), (-0.6421659071, 0.2704995844), (-0.6482697015, 0.2727147423), (-0.6546024263, 0.2747737968), (-0.6611664657, 0.2766668482), (-0.6679523281, 0.2784153835), (-0.6749947402, 0.2799157317), (-0.6825568462, 0.281638512), (-0.6921740557, 0.281821762), (-0.6991017959, 0.288171967), (-0.7058553412, 0.292924242), (-0.7113762288, 0.2974025782), (-0.7174039562, 0.3025345529), (-0.7238633217, 0.3084510747), (-0.7307192574, 0.3151573097), (-0.7379217212, 0.3226949233), (-0.7454230113, 0.3310913659), (-0.7531725702, 0.3403753838), (-0.7611187048, 0.3505721408), (-0.7754174106, 0.370249988), (-0.7860176586, 0.3872574178), (-0.7935687515, 0.4007113836)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, 176.7914263395, 6.4171473209)
                _nurbs_edge([(-0.7935687515, -0.4007113836), (-0.7860176586, -0.3872574178), (-0.7754174106, -0.370249988), (-0.7611187048, -0.3505721408), (-0.7531725702, -0.3403753838), (-0.7454230113, -0.3310913659), (-0.7379217212, -0.3226949233), (-0.7307192574, -0.3151573097), (-0.7238633217, -0.3084510747), (-0.7174039562, -0.3025345529), (-0.7113762288, -0.2974025782), (-0.7058553412, -0.292924242), (-0.6991017959, -0.288171967), (-0.6921740557, -0.281821762), (-0.6825568462, -0.281638512), (-0.6749947402, -0.2799157317), (-0.6679523281, -0.2784153835), (-0.6611664657, -0.2766668482), (-0.6546024263, -0.2747737968), (-0.6482697015, -0.2727147423), (-0.6421659071, -0.2704995844), (-0.6362912608, -0.268129059), (-0.630644888, -0.2656049585), (-0.6252258465, -0.2629272115), (-0.6200329822, -0.260094295), (-0.61506516, -0.2571027221), (-0.6103215039, -0.2539466985), (-0.6058017917, -0.2506176674), (-0.6015070324, -0.247103833), (-0.5974403116, -0.2433896841), (-0.5936079984, -0.2394556063), (-0.5900214219, -0.235277738), (-0.5866991174, -0.2308283371), (-0.5836696563, -0.2260770741), (-0.580974923, -0.2209938464), (-0.5786731845, -0.2155537999), (-0.5768412137, -0.2097451824), (-0.5755719539, -0.2035797231), (-0.5749717684, -0.1971047884), (-0.5751308246, -0.1904104715), (-0.576059877, -0.1843240606), (-0.5789021222, -0.1729548784), (-0.5843847156, -0.1565854126), (-0.5878213834, -0.1396677427), (-0.5910445179, -0.1284006195), (-0.5932831403, -0.1226651068), (-0.5964925521, -0.1167881303), (-0.6002497953, -0.1114807651), (-0.6044317362, -0.1067759506), (-0.6089225782, -0.1026615256), (-0.6136359654, -0.0991011764), (-0.6185112868, -0.0960463388), (-0.6235105086, -0.0934463549), (-0.6286124092, -0.0912542129), (-0.6338074096, -0.0894293611), (-0.6390933292, -0.0879385064), (-0.6444722871, -0.0867553194), (-0.6499485749, -0.0858596293), (-0.6555272761, -0.0852364598), (-0.6612134146, -0.0848750912), (-0.6670114613, -0.0847682243), (-0.6729250719, -0.0849112788), (-0.678956973, -0.0853018026), (-0.6851089255, -0.0859390538), (-0.6913817812, -0.0868234418), (-0.6977754012, -0.0879569559), (-0.7042892289, -0.0893401248), (-0.7109203795, -0.090982714), (-0.7176713764, -0.0928613691), (-0.7245204582, -0.0950832355), (-0.7319308244, -0.097372317), (-0.740351197, -0.1020222226), (-0.7495258986, -0.0999866539), (-0.7577507779, -0.0992478356), (-0.7647711749, -0.0981299265), (-0.7725573273, -0.0966993697), (-0.7811095628, -0.0948051943), (-0.7904000948, -0.0924253923), (-0.8004064182, -0.0894988594), (-0.8111009473, -0.0859779718), (-0.8224542711, -0.0818125559), (-0.834434204, -0.0769549726), (-0.8566561701, -0.0670628099), (-0.8743399691, -0.0576340677), (-0.8876063902, -0.0497581379)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
                CenterArc((0, 0), 0.8889999866, -153.2085736605, 6.4171473209)
                _nurbs_edge([(-0.4868950066, -0.7438106135), (-0.4870825513, -0.7283835909), (-0.4864061821, -0.7083546007), (-0.4838620632, -0.6841637322), (-0.4820788873, -0.6713600143), (-0.4800095814, -0.6594450395), (-0.4777114949, -0.6484228618), (-0.4752427851, -0.6382938651), (-0.4726584881, -0.6290581274), (-0.4700227744, -0.6207045865), (-0.4673685966, -0.6132463023), (-0.4648265359, -0.6066075056), (-0.4613539316, -0.599115142), (-0.4585294351, -0.590151833), (-0.4502923124, -0.5851845292), (-0.4446047266, -0.5799115046), (-0.4392559928, -0.575090959), (-0.4342535314, -0.5701837518), (-0.4295154321, -0.5652623015), (-0.4250606588, -0.5603127456), (-0.4208821968, -0.5553424654), (-0.4169798666, -0.550352207), (-0.4133520145, -0.5453430854), (-0.4099978604, -0.5403145677), (-0.4069171663, -0.535264758), (-0.4041106925, -0.5301900688), (-0.4015805776, -0.5250850441), (-0.3993309076, -0.5199421624), (-0.3973684541, -0.5147517129), (-0.3957036451, -0.5095018053), (-0.3943518034, -0.5041786373), (-0.3933346712, -0.498767209), (-0.3926821715, -0.4932527625), (-0.3924342128, -0.4876233175), (-0.3926421191, -0.4818737465), (-0.3933687783, -0.4760116589), (-0.3946865538, -0.4700652631), (-0.3966700722, -0.4640911888), (-0.3993877637, -0.4581836381), (-0.4028726688, -0.4524657178), (-0.4067204573, -0.4476592576), (-0.4148665049, -0.4392343796), (-0.427799303, -0.427799303), (-0.4392343796, -0.4148665049), (-0.4476592576, -0.4067204573), (-0.4524657178, -0.4028726688), (-0.4581836381, -0.3993877637), (-0.4640911888, -0.3966700722), (-0.4700652631, -0.3946865538), (-0.4760116589, -0.3933687783), (-0.4818737465, -0.3926421191), (-0.4876233175, -0.3924342128), (-0.4932527625, -0.3926821715), (-0.498767209, -0.3933346712), (-0.5041786373, -0.3943518034), (-0.5095018053, -0.3957036451), (-0.5147517129, -0.3973684541), (-0.5199421624, -0.3993309076), (-0.5250850441, -0.4015805776), (-0.5301900688, -0.4041106925), (-0.535264758, -0.4069171663), (-0.5403145677, -0.4099978604), (-0.5453430854, -0.4133520145), (-0.550352207, -0.4169798666), (-0.5553424654, -0.4208821968), (-0.5603127456, -0.4250606588), (-0.5652623015, -0.4295154321), (-0.5701837518, -0.4342535314), (-0.575090959, -0.4392559928), (-0.5799115046, -0.4446047266), (-0.5851845292, -0.4502923124), (-0.590151833, -0.4585294351), (-0.599115142, -0.4613539316), (-0.6066075056, -0.4648265359), (-0.6132463023, -0.4673685966), (-0.6207045865, -0.4700227744), (-0.6290581274, -0.4726584881), (-0.6382938651, -0.4752427851), (-0.6484228618, -0.4777114949), (-0.6594450395, -0.4800095814), (-0.6713600143, -0.4820788873), (-0.6841637322, -0.4838620632), (-0.7083546007, -0.4864061821), (-0.7283835909, -0.4870825513), (-0.7438106135, -0.4868950066)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651128399, 0.084472582, 0.1026590064, 0.1196721132, 0.1355119023, 0.1501783737, 0.1636715275, 0.1759913636, 0.1871378821, 0.197111083, 0.2059109663, 0.222284364, 0.2346807737, 0.2450604039, 0.25517642, 0.2650349305, 0.2746428534, 0.2840080476, 0.2931394691, 0.3020473549, 0.3107434414, 0.3192412203, 0.3275562393, 0.3357064505, 0.3437126078, 0.3515987105, 0.3593924769, 0.3671258168, 0.3748352374, 0.3825620726, 0.390352349, 0.3982560087, 0.4063250987, 0.4146104578, 0.4231564893, 0.4319939541, 0.4411315305, 0.4505481313, 0.4601891357, 0.4670510698, 0.5, 0.5329489302, 0.5398108643, 0.5494518687, 0.5588684695, 0.5680060459, 0.5768435107, 0.5853895422, 0.5936749013, 0.6017439913, 0.609647651, 0.6174379274, 0.6251647626, 0.6328741832, 0.6406075231, 0.6484012895, 0.6562873922, 0.6642935495, 0.6724437607, 0.6807587797, 0.6892565586, 0.6979526451, 0.7068605309, 0.7159919524, 0.7253571466, 0.7349650695, 0.74482358, 0.7549395961, 0.7653192263, 0.777715636, 0.7940890337, 0.802888917, 0.8128621179, 0.8240086364, 0.8363284725, 0.8498216263, 0.8644880977, 0.8803278868, 0.8973409936, 0.915527418, 0.9348871601, 1, 1, 1, 1], 3)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


def model_51336_33ff2eba_0015():
    """Model: Glass v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_51336_33ff2eba_0016():
    """Model: Tiny Hands v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with BuildLine():
                CenterArc((0, 0), 0.05, 101.0063845079, 165.4102938471)
                CenterArc((0, 0), 0.05, -93.583321645, 194.5897061529)
            make_face()
            # Profile area: 0.0359843254, perimeter: 1.7347600514
            with BuildLine():
                Line((-0.0095459189, 0.0490802958), (-0.8000000119, 0))
                Line((-0.8000000119, 0), (-0.003125, -0.0499022482))
                CenterArc((0, 0), 0.05, 101.0063845079, 165.4102938471)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_51341_6ba06c4a_0000():
    """Model: Frame"""
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
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7570953846, perimeter: 25.2987305031
            with BuildLine():
                Line((-2.7940000892, -1.2700000405), (-2.7940000892, 1.2700000405))
                _nurbs_edge([(-2.7940000892, -1.2700000405), (-2.7542767023, -1.2685212384), (-2.6759678712, -1.2685579949), (-2.5619186535, -1.2775965641), (-2.4167290017, -1.3077424366), (-2.2466685803, -1.3758327907), (-2.0873696871, -1.4736314212), (-1.9371189256, -1.5987017751), (-1.7924427639, -1.7455203565), (-1.6484017469, -1.9059563961), (-1.4994401625, -2.0707561215), (-1.34007541, -2.230685784), (-1.1655774843, -2.3776560827), (-0.9729095834, -2.5061999587), (-0.7606709921, -2.6134386736), (-0.5284360527, -2.6981222914), (-0.3267833615, -2.7476803399), (-0.1667763603, -2.7747419223), (-0.0562368323, -2.7883238985), (0, -2.7940000892)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(2.7940000892, -1.2700000405), (2.7542767023, -1.2685212384), (2.6759678712, -1.2685579949), (2.5619186535, -1.2775965641), (2.4167290017, -1.3077424366), (2.2466685803, -1.3758327907), (2.0873696871, -1.4736314212), (1.9371189256, -1.5987017751), (1.7924427639, -1.7455203565), (1.6484017469, -1.9059563961), (1.4994401625, -2.0707561215), (1.34007541, -2.230685784), (1.1655774843, -2.3776560827), (0.9729095834, -2.5061999587), (0.7606709921, -2.6134386736), (0.5284360527, -2.6981222914), (0.3267833615, -2.7476803399), (0.1667763603, -2.7747419223), (0.0562368323, -2.7883238985), (0, -2.7940000892)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((2.7940000892, 0), (2.7940000892, -1.2700000405))
                Line((2.2225, 0), (2.7940000892, 0))
                CenterArc((0, 0), 2.2225, 90, 270)
                Line((0, 2.2225), (0, 2.7940000892))
                _nurbs_edge([(-2.7940000892, 1.2700000405), (-2.7542767023, 1.2685212384), (-2.6759678712, 1.2685579949), (-2.5619186535, 1.2775965641), (-2.4167290017, 1.3077424366), (-2.2466685803, 1.3758327907), (-2.0873696871, 1.4736314212), (-1.9371189256, 1.5987017751), (-1.7924427639, 1.7455203565), (-1.6484017469, 1.9059563961), (-1.4994401625, 2.0707561215), (-1.34007541, 2.230685784), (-1.1655774843, 2.3776560827), (-0.9729095834, 2.5061999587), (-0.7606709921, 2.6134386736), (-0.5284360527, 2.6981222914), (-0.3267833615, 2.7476803399), (-0.1667763603, 2.7747419223), (-0.0562368323, 2.7883238985), (0, 2.7940000892)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 1.9190300519, perimeter: 9.1949102866
            with BuildLine():
                Line((0, 2.2225), (0, 2.7940000892))
                CenterArc((0, 0), 2.2225, 0, 90)
                Line((2.2225, 0), (2.7940000892, 0))
                Line((2.7940000892, 0), (2.7940000892, 1.2700000405))
                _nurbs_edge([(2.7940000892, 1.2700000405), (2.7542767023, 1.2685212384), (2.6759678712, 1.2685579949), (2.5619186535, 1.2775965641), (2.4167290017, 1.3077424366), (2.2466685803, 1.3758327907), (2.0873696871, 1.4736314212), (1.9371189256, 1.5987017751), (1.7924427639, 1.7455203565), (1.6484017469, 1.9059563961), (1.4994401625, 2.0707561215), (1.34007541, 2.230685784), (1.1655774843, 2.3776560827), (0.9729095834, 2.5061999587), (0.7606709921, 2.6134386736), (0.5284360527, 2.6981222914), (0.3267833615, 2.7476803399), (0.1667763603, 2.7747419223), (0.0562368323, 2.7883238985), (0, 2.7940000892)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_51341_6ba06c4a_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.3502475318, perimeter: 12.7674325442
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_51341_6ba06c4a_0005():
    """Model: Rim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 4.1169982677, perimeter: 25.9338473554
            with BuildLine():
                CenterArc((0, 0), 2.2225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.508, against=-0.127
        extrude(amount=0.508)
        extrude(sk.sketch, amount=-0.127)
    return part.part


def model_51341_6ba06c4a_0008():
    """Model: Hingepin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1140091828, perimeter: 1.196946801
            with Locations((-3.1326667693, 0.254)):
                Circle(0.1905)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54)
    return part.part


def model_51345_4b292361_0004():
    """Model: Driving Handle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.516624371, perimeter: 22.3169794189
            with BuildLine():
                Line((2.2186621267, -3.5), (2.216085913, -3.3000165929))
                Line((2.216085913, -3.3000165929), (3.216085913, -3.3000165929))
                Line((3.216085913, -3.3000165929), (3.216085913, -2.3000165929))
                CenterArc((3.216085913, -2.1500165929), 0.15, 0, 360)
                Line((3.216085913, -3.3000165929), (4.216085913, -3.3000165929))
                Line((4.216085913, -3.3000165929), (4.216085913, -3.5))
                Line((4.216085913, -3.5), (5.2186621267, -3.5))
                CenterArc((5.2186562909, -3.1182253274), 0.3817746726, -89.9991241795, 92.7351508042)
                Line((5.5999957624, -3.1000014941), (6.7363878441, -2.7))
                Line((6.7363878441, -1.2), (6.7363878441, -2.7))
                CenterArc((4.5, -2.6839294123), 2.6839294123, 33.5658050769, 56.4341949231)
                Line((0, 0), (4.5, 0))
                CenterArc((1.851488884, -1.3174940882), 2.2724, 144.5648671089, 40.0417571464)
                Line((-0.4135703541, -1.5), (0.0864296459, -1.5))
                CenterArc((0.3364296459, -1.5), 0.25, 0, 180)
                Line((1.2186621267, -1.5), (0.5864296459, -1.5))
                Line((1.2186621267, -3.5), (1.2186621267, -1.5))
                Line((1.2186621267, -3.5), (2.2186621267, -3.5))
            make_face()
            # Profile area: 2.2394544483, perimeter: 6.6630997646
            with BuildLine():
                Line((1.2186621267, -3.5), (1.2186621267, -1.5))
                Line((1.2186621267, -1.5), (0.5864296459, -1.5))
                CenterArc((0.3364296459, -1.5), 0.25, 180, 180)
                Line((-0.4135703541, -1.5), (0.0864296459, -1.5))
                CenterArc((1.851488884, -1.3174940882), 2.2724, -175.3933757447, 69.2236372941)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_51346_87465d9e_0001():
    """Model: Cubierta escritorio"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 90), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14895.3266813654, perimeter: 583.4370001861
            with BuildLine():
                CenterArc((-60, 153.2050807569), 200, -120, 60)
                Line((40, 20), (40, -20))
                CenterArc((-60, -153.2050807569), 200, 60, 60)
                Line((-160, -20), (-160, 20))
            make_face()
            with BuildLine():
                CenterArc((26.4575131106, 0), 33, 143.2968533228, 73.4062933544)
                CenterArc((-26.4575131106, 0), 33, -36.7031466772, 73.4062933544)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 351.5592151209, perimeter: 84.5579797074
            with BuildLine():
                CenterArc((-26.4575131106, 0), 33, -36.7031466772, 73.4062933544)
                CenterArc((26.4575131106, 0), 33, 143.2968533228, 73.4062933544)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_51459_874dd272_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 120, perimeter: 46
            with BuildLine():
                Line((7.5, -4), (7.5, 4))
                Line((7.5, 4), (-7.5, 4))
                Line((-7.5, 4), (-7.5, -4))
                Line((-7.5, -4), (7.5, -4))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5)
    return part.part


def model_51509_fd5fcb9c_0001():
    """Model: Engine-011"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.6297695219, perimeter: 48.6689447899
            with BuildLine():
                CenterArc((0, 0), 3.556, -55.6804178939, 291.3608357879)
                CenterArc((1.3839941333, -3.7364510225), 1.0123123448, -50.7463103739, 102.9137118248)
                CenterArc((0, 0), 4.953, -65.8736478801, 311.7472957602)
                CenterArc((-1.3839941333, -3.7364510225), 1.0123123448, 127.8325985491, 102.9137118248)
            make_face()
        # Symmetric extrude, each_side=0.254
        extrude(amount=0.254, both=True)
    return part.part


def model_51536_a18dc325_0008():
    """Model: Tiny Hand for Stopwatch v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0028272564, perimeter: 0.1884926058
            with BuildLine():
                CenterArc((0, 0), 0.0299999993, 97.6281496686, 168.5492966021)
                CenterArc((0, 0), 0.0299999993, -93.8225537293, 183.8225537293)
                Line((0, 0.0299999993), (-0.0039823008, 0.0297345126))
            make_face()
            # Profile area: 0.0121014652, perimeter: 0.9842588205
            with BuildLine():
                Line((-0.0039823008, 0.0297345126), (-0.4499999899, 0))
                Line((-0.4499999899, 0), (-0.002, -0.0299332584))
                CenterArc((0, 0), 0.0299999993, 97.6281496686, 168.5492966021)
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


def model_51536_a18dc325_0011():
    """Model: Glass Cover v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_51536_a18dc325_0013():
    """Model: Hour hand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0545646812, perimeter: 2.1980757831
            with BuildLine():
                Line((-0.1845417695, 0.0770995155), (-0.1999998927, -0.000207154))
                CenterArc((0, 0), 0.2, -179.9406547323, 179.8813094646)
                Line((0.1845417695, 0.0770995155), (0.1999998927, -0.000207154))
                CenterArc((0, 0), 0.2, 22.6746339583, 134.6507320833)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1500000022, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1375398, perimeter: 2.3523597523
            with BuildLine():
                CenterArc((0, 0), 0.2, 22.6746339583, 134.6507320833)
                Line((0, 1.0000000149), (0.1845417695, 0.0770995155))
                Line((0, 1.0000000149), (-0.1845417695, 0.0770995155))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


def model_51559_4293c0e0_0001():
    """Model: silicone v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1074114104, perimeter: 14.7654854719
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_51567_5f9bb333_0007():
    """Model: weight"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.7265166763, perimeter: 25.572936269
            with BuildLine():
                Line((0.6479149289, -0.7143192141), (0.6479149289, -5.3335957953))
                Line((0.6479149289, -5.3335957953), (8.8151064823, -5.3335957953))
                Line((8.8151064823, -5.3335957953), (8.8151064823, -0.7143192141))
                Line((8.8151064823, -0.7143192141), (0.6479149289, -0.7143192141))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


def model_51585_b695905b_0006():
    """Model: PTFE_Seal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64, perimeter: 128
            with BuildLine():
                Line((21, 1), (-1, 1))
                Line((-1, 1), (-1, -11))
                Line((-1, -11), (21, -11))
                Line((21, -11), (21, 1))
            make_face()
            with BuildLine():
                Line((20, 0), (0, 0))
                Line((20, -10), (20, 0))
                Line((0, -10), (20, -10))
                Line((0, 0), (0, -10))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05)
    return part.part


def model_51585_b695905b_0007():
    """Model: ClampingMechanism"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.84, perimeter: 118.4
            with BuildLine():
                Line((-20.1262296395, 10), (-20.1262296395, 0))
                Line((-20.1262296395, 0), (-0.1262296395, 0))
                Line((-0.1262296395, 0), (-0.1262296395, 10))
                Line((-0.1262296395, 10), (-20.1262296395, 10))
            make_face()
            with BuildLine():
                Line((-19.9262296395, 9.8), (-19.9262296395, 0.2))
                Line((-0.3262296395, 9.8), (-19.9262296395, 9.8))
                Line((-0.3262296395, 0.2), (-0.3262296395, 9.8))
                Line((-19.9262296395, 0.2), (-0.3262296395, 0.2))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_51585_b695905b_0011():
    """Model: Baseplate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on Plane1 construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(10, -7, 5), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 875, perimeter: 120
            with BuildLine():
                Line((-17.5, 12.5), (17.5, 12.5))
                Line((-17.5, -12.5), (-17.5, 12.5))
                Line((17.5, -12.5), (-17.5, -12.5))
                Line((17.5, 12.5), (17.5, -12.5))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)
    return part.part


def model_51593_174d44c2_0008():
    """Model: VelcroPatch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.5108425617, 0.7, 3.4416146278), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63, perimeter: 32
            with BuildLine():
                Line((-16, 14), (-9, 14))
                Line((-16, 5), (-16, 14))
                Line((-9, 5), (-16, 5))
                Line((-9, 14), (-9, 5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_51595_41f3d1a3_0001():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3, perimeter: 20.6
            with BuildLine():
                Line((0.3, 10), (0.3, 0))
                Line((0, 10), (0.3, 10))
                Line((0, 0), (0, 10))
                Line((0.3, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=9.7
        extrude(amount=9.7)
    return part.part


def model_51595_41f3d1a3_0002():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.82, perimeter: 19.4
            with BuildLine():
                Line((0.3, 0.3), (9.7, 0.3))
                Line((0.3, 0), (0.3, 0.3))
                Line((9.7, 0), (0.3, 0))
                Line((9.7, 0.3), (9.7, 0))
            make_face()
        # OneSide extrude, distance=9.7
        extrude(amount=9.7)
    return part.part


def model_51595_41f3d1a3_0005():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((0, -10), (-10, -10))
                Line((0, 0), (0, -10))
                Line((-10, 0), (0, 0))
                Line((-10, -10), (-10, 0))
            make_face()
        # TwoSides extrude, along=0.3, against=-0.5
        extrude(amount=0.3)
        extrude(sk.sketch, amount=-0.5)
    return part.part


def model_51601_2616f89b_0007():
    """Model: glass v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_51601_2616f89b_0015():
    """Model: antiscratch rubber v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_51601_2616f89b_0018():
    """Model: lampshade glass v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 103.8689071093, perimeter: 36.1283155163
            Circle(5.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_51602_42da13f0_0000():
    """Model: Glass Covering v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_51602_42da13f0_0004():
    """Model: Hole for strap v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5370796492, perimeter: 10.7415928239
            with BuildLine():
                CenterArc((0.2, 0.5000000104), 0.3000000015, 90, 90)
                Line((-0.1000000015, 0.5000000104), (-0.1000000015, 0.2))
                CenterArc((0.2, 0.2), 0.3000000015, -180, 90)
                Line((0.2, -0.1000000015), (1.8000000298, -0.1000000015))
                CenterArc((1.8000000298, 0.2), 0.3000000015, -90, 90)
                Line((2.1000000313, 0.2), (2.1000000313, 0.5000000104))
                CenterArc((1.8000000298, 0.5000000104), 0.3000000015, 0, 90)
                Line((1.8000000298, 0.8000000119), (0.2, 0.8000000119))
            make_face()
            with BuildLine():
                Line((2.0000000298, 0.2), (2.0000000298, 0.5000000104))
                CenterArc((1.8000000298, 0.2), 0.2, -90, 90)
                Line((0.2, 0), (1.8000000298, 0))
                CenterArc((0.2, 0.2), 0.2, -180, 90)
                Line((0, 0.5000000104), (0, 0.2))
                CenterArc((0.2, 0.5000000104), 0.2, 90, 90)
                Line((1.8000000298, 0.7000000104), (0.2, 0.7000000104))
                CenterArc((1.8000000298, 0.5000000104), 0.2, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_51602_42da13f0_0006():
    """Model: Hole Pick v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1889610152, perimeter: 2.8431460373
            with BuildLine():
                Line((-0.0097398324, 0.1496834538), (-0.2551291312, 0.2386716428))
                CenterArc((-0.8346869631, -1.3594875231), 1.7, 70.0672857849, 31.1106366085)
                Line((-1.1642427554, 0.3082633516), (-1.1777968914, 0.3055849875))
                CenterArc((-1.1729504827, 0.2810592393), 0.025, 101.1779223934, 162.083077318)
                Line((-1.1758841513, 0.2562319642), (-0.9496510246, 0.2294995491))
                CenterArc((-1.1080691302, -1.1111733058), 1.35, 62.1641681379, 21.0968315735)
                Line((-0.4777004651, 0.0826170218), (-0.0700409638, -0.1326433717))
                CenterArc((0, 0), 0.1500000022, 93.7229611405, 148.4412069974)
            make_face()
            # Profile area: 0.0628318552, perimeter: 1.2566370755
            with BuildLine():
                CenterArc((0, 0), 0.1500000022, 93.7229611405, 148.4412069974)
                CenterArc((0, 0), 0.1500000022, -117.8358318621, 211.5587930026)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_51602_42da13f0_0012():
    """Model: Hour Hand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2312561655, perimeter: 6.0695141557
            with BuildLine():
                Line((0.0499999989, 0.4099999908), (0.200000003, 0.4099999908))
                Line((0.200000003, 0.4099999908), (0.200000003, 1.0000000149))
                Line((0.200000003, 1.0000000149), (0, 1.2000000179))
                Line((0, 1.2000000179), (-0.200000003, 1.0000000149))
                Line((-0.200000003, 1.0000000149), (-0.200000003, 0.4099999908))
                Line((-0.200000003, 0.4099999908), (-0.0499999989, 0.4099999908))
                Line((-0.0499999989, 0.1936491676), (-0.0499999989, 0.4099999908))
                CenterArc((0, 0), 0.2, 104.4775118553, 331.0449762895)
                Line((0.0499999989, 0.4099999908), (0.0499999989, 0.1936491676))
            make_face()
            with BuildLine():
                Line((-0.1147690185, 0.4952309753), (0.1147690185, 0.4952309753))
                Line((-0.1147690185, 0.9646961852), (-0.1147690185, 0.4952309753))
                Line((0, 1.0794652037), (-0.1147690185, 0.9646961852))
                Line((0.1147690185, 0.9646961852), (0, 1.0794652037))
                Line((0.1147690185, 0.4952309753), (0.1147690185, 0.9646961852))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


def model_51606_b72fa3d6_0008():
    """Model: Height Lock Handle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3754273957, perimeter: 16.7432302674
            with BuildLine():
                CenterArc((2.4809731254, -2.5052626673), 2.4453974485, -1.9172327917, 90.5510188054)
                Line((0.0302715865, -0.0007219608), (2.5392779366, -0.0605603889))
                Line((0, 0), (0.0302715865, -0.0007219608))
                CenterArc((0, -0.635), 0.635, 90, 249.8001756729)
                CenterArc((2.0886659398, -2.9093490089), 2.54, 7.3955636315, 118.5974007426)
                Line((4.9250016372, -2.5870753475), (4.607536015, -2.5824032268))
            make_face()
            with BuildLine():
                CenterArc((0, -0.635), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_51606_b72fa3d6_0021():
    """Model: Pin Nut v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0801201993, perimeter: 6.3943203863
            with BuildLine():
                Line((0.3666174209, 0.635), (-0.3666174209, 0.635))
                Line((-0.3666174209, 0.635), (-0.7332348419, 0))
                Line((-0.7332348419, 0), (-0.3666174209, -0.635))
                Line((-0.3666174209, -0.635), (0.3666174209, -0.635))
                Line((0.3666174209, -0.635), (0.7332348419, 0))
                Line((0.7332348419, 0), (0.3666174209, 0.635))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_51674_a70c1c6c_0004():
    """Model: Glass Cover v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.2025431267, perimeter: 12.8805298797
            Circle(2.05)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_51708_867d4509_0000():
    """Model: SF25-25"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 84 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7052895939, perimeter: 29.7060764943
            with BuildLine():
                Line((-0.6, 0.925), (-0.6, 1.05))
                Line((-0.6, 1.05), (-0.3, 1.05))
                Line((-0.3, 1.2), (-0.3, 1.05))
                CenterArc((-0.35, 1.2), 0.05, 0, 90)
                Line((-0.35, 1.25), (-1.15, 1.25))
                CenterArc((-1.15, 1.15), 0.1, 90, 90)
                Line((-1.25, 0.35), (-1.25, 1.15))
                CenterArc((-1.2, 0.35), 0.05, 180, 90)
                Line((-1.2, 0.3), (-1.05, 0.3))
                Line((-1.05, 0.3), (-1.05, 0.6))
                Line((-0.925, 0.6), (-1.05, 0.6))
                Line((-0.6, 0.275), (-0.925, 0.6))
                Line((-0.6, 0.05), (-0.6, 0.275))
                Line((-0.55, 0), (-0.6, 0.05))
                Line((-0.6, -0.05), (-0.55, 0))
                Line((-0.6, -0.275), (-0.6, -0.05))
                Line((-0.925, -0.6), (-0.6, -0.275))
                Line((-0.925, -0.6), (-1.05, -0.6))
                Line((-1.05, -0.3), (-1.05, -0.6))
                Line((-1.2, -0.3), (-1.05, -0.3))
                CenterArc((-1.2, -0.35), 0.05, 90, 90)
                Line((-1.25, -1.15), (-1.25, -0.35))
                CenterArc((-1.15, -1.15), 0.1, -180, 90)
                Line((-0.35, -1.25), (-1.15, -1.25))
                CenterArc((-0.35, -1.2), 0.05, -90, 90)
                Line((-0.3, -1.05), (-0.3, -1.2))
                Line((-0.6, -1.05), (-0.3, -1.05))
                Line((-0.6, -0.925), (-0.6, -1.05))
                Line((-0.275, -0.6), (-0.6, -0.925))
                Line((-0.05, -0.6), (-0.275, -0.6))
                Line((0, -0.55), (-0.05, -0.6))
                Line((0.05, -0.6), (0, -0.55))
                Line((0.275, -0.6), (0.05, -0.6))
                Line((0.6, -0.925), (0.275, -0.6))
                Line((0.6, -0.925), (0.6, -1.05))
                Line((0.6, -1.05), (0.3, -1.05))
                Line((0.3, -1.2), (0.3, -1.05))
                CenterArc((0.35, -1.2), 0.05, 180, 90)
                Line((0.35, -1.25), (1.15, -1.25))
                CenterArc((1.15, -1.15), 0.1, -90, 90)
                Line((1.25, -0.35), (1.25, -1.15))
                CenterArc((1.2, -0.35), 0.05, 0, 90)
                Line((1.05, -0.3), (1.2, -0.3))
                Line((1.05, -0.3), (1.05, -0.6))
                Line((0.925, -0.6), (1.05, -0.6))
                Line((0.6, -0.275), (0.925, -0.6))
                Line((0.6, -0.05), (0.6, -0.275))
                Line((0.55, 0), (0.6, -0.05))
                Line((0.6, 0.05), (0.55, 0))
                Line((0.6, 0.275), (0.6, 0.05))
                Line((0.925, 0.6), (0.6, 0.275))
                Line((0.925, 0.6), (1.05, 0.6))
                Line((1.05, 0.6), (1.05, 0.3))
                Line((1.05, 0.3), (1.2, 0.3))
                CenterArc((1.2, 0.35), 0.05, -90, 90)
                Line((1.25, 1.15), (1.25, 0.35))
                CenterArc((1.15, 1.15), 0.1, 0, 90)
                Line((0.35, 1.25), (1.15, 1.25))
                CenterArc((0.35, 1.2), 0.05, 90, 90)
                Line((0.3, 1.05), (0.3, 1.2))
                Line((0.3, 1.05), (0.6, 1.05))
                Line((0.6, 1.05), (0.6, 0.925))
                Line((0.275, 0.6), (0.6, 0.925))
                Line((0.05, 0.6), (0.275, 0.6))
                Line((0, 0.55), (0.05, 0.6))
                Line((-0.05, 0.6), (0, 0.55))
                Line((-0.275, 0.6), (-0.05, 0.6))
                Line((-0.6, 0.925), (-0.275, 0.6))
            make_face()
            with BuildLine():
                Line((0.7278012621, -0.8528012621), (0.6125, -0.7375))
                CenterArc((0.675, -0.675), 0.0883883476, 45, 179.9999987926)
                Line((0.7375, -0.6125), (0.8528012621, -0.7278012621))
                CenterArc((0.925, -0.925), 0.21, 159.8912250834, 310.2175498332)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.925, 0.925), 0.21, -110.1087749166, 310.2175498332)
                Line((0.8528012621, 0.7278012621), (0.7375, 0.6125))
                CenterArc((0.675, 0.675), 0.0883883476, 135, 180)
                Line((0.7278012621, 0.8528012621), (0.6125, 0.7375))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.7375, 0.6125), (-0.8528012621, 0.7278012621))
                CenterArc((-0.925, 0.925), 0.21, -20.1087749166, 310.2175498332)
                Line((-0.7278012621, 0.8528012621), (-0.6125, 0.7375))
                CenterArc((-0.675, 0.675), 0.0883883476, -135, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.6125, -0.7375), (-0.7278012621, -0.8528012621))
                CenterArc((-0.925, -0.925), 0.21, 69.8912250834, 310.2175498332)
                Line((-0.7375, -0.6125), (-0.8528012621, -0.7278012621))
                CenterArc((-0.675, -0.675), 0.0883883476, -45, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.2946502746, 0.1696502746), (-0.3535533906, 0.2285533906))
                CenterArc((-0.3535533906, 0.3535533906), 0.125, 0, 270)
                Line((-0.2285533906, 0.3535533906), (-0.1696502746, 0.2946502746))
                CenterArc((0, 0), 0.34, 60.0680285985, 59.8639428031)
                Line((0.2285533906, 0.3535533906), (0.1696502746, 0.2946502746))
                CenterArc((0.3535533906, 0.3535533906), 0.125, -90, 270)
                Line((0.3535533906, 0.2285533906), (0.2946502746, 0.1696502746))
                CenterArc((0, 0), 0.34, -29.9319714015, 59.8639428031)
                Line((0.2946502746, -0.1696502746), (0.3535533906, -0.2285533906))
                CenterArc((0.3535533906, -0.3535533906), 0.125, 180, 270)
                Line((0.2285533906, -0.3535533906), (0.1696502746, -0.2946502746))
                CenterArc((0, 0), 0.34, -119.9319714015, 59.8639428031)
                Line((-0.1696502746, -0.2946502746), (-0.2285533906, -0.3535533906))
                CenterArc((-0.3535533906, -0.3535533906), 0.125, 90, 270)
                Line((-0.2946502746, -0.1696502746), (-0.3535533906, -0.2285533906))
                CenterArc((0, 0), 0.34, 150.0680285985, 59.8639428031)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-16.18
        extrude(amount=-16.18)
    return part.part


def model_51747_3d58eae0_0003():
    """Model: whisk arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0398551956, perimeter: 41.5942078251
            with BuildLine():
                CenterArc((4.4216816602, -1.2), 0.2, 90, 81.2512665873)
                CenterArc((-135.0579384152, 20.2648104313), 140.9215876585, -11.5164511062, 2.7677176936)
                CenterArc((3.5164678891, -7.9699088562), 0.5, 168.4835488938, 31.9680576611)
                CenterArc((5, -7.4166666667), 2.0833333333, -159.5483934452, 139.0967868903)
                CenterArc((6.4835321109, -7.9699088562), 0.5, -20.4516065548, 31.9680576611)
                CenterArc((145.0579384152, 20.2648104313), 140.9215876585, -171.2512665873, 2.7677176936)
                CenterArc((5.5783183398, -1.2), 0.2, 8.7487334127, 81.2512665873)
                Line((5.5783183398, -1), (4.4216816602, -1))
            make_face()
            with BuildLine():
                CenterArc((-135.0579384152, 20.2648104313), 140.9715876585, -11.5164511062, 2.7677176936)
                CenterArc((4.4216816602, -1.2), 0.15, 90, 81.2512665873)
                Line((5.5783183398, -1.05), (4.4216816602, -1.05))
                CenterArc((5.5783183398, -1.2), 0.15, 8.7487334127, 81.2512665873)
                CenterArc((145.0579384152, 20.2648104313), 140.9715876585, -171.2512665873, 2.7677176936)
                CenterArc((6.4835321109, -7.9699088562), 0.45, -20.4516065548, 31.9680576612)
                CenterArc((5, -7.4166666667), 2.0333333333, -159.5483934452, 139.0967868903)
                CenterArc((3.5164678891, -7.9699088562), 0.45, 168.4835488938, 31.9680576611)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)
    return part.part


def model_51777_87ff5835_0001():
    """Model: Table-009"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.41935, perimeter: 6.35
            with BuildLine():
                Line((36.83, -1.27), (34.925, -1.27))
                Line((34.925, -1.27), (34.925, -2.54))
                Line((34.925, -2.54), (36.83, -2.54))
                Line((36.83, -1.27), (36.83, -2.54))
            make_face()
            # Profile area: 2.41935, perimeter: 6.35
            with BuildLine():
                Line((36.83, 2.54), (34.925, 2.54))
                Line((34.925, 2.54), (34.925, 1.27))
                Line((34.925, 1.27), (36.83, 1.27))
                Line((36.83, 2.54), (36.83, 1.27))
            make_face()
            # Profile area: 2.41935, perimeter: 6.35
            with BuildLine():
                Line((-36.83, -2.54), (-36.83, -1.27))
                Line((-34.925, -2.54), (-36.83, -2.54))
                Line((-34.925, -1.27), (-34.925, -2.54))
                Line((-36.83, -1.27), (-34.925, -1.27))
            make_face()
            # Profile area: 2.41935, perimeter: 6.35
            with BuildLine():
                Line((-34.925, 1.27), (-36.83, 1.27))
                Line((-34.925, 2.54), (-34.925, 1.27))
                Line((-36.83, 2.54), (-34.925, 2.54))
                Line((-36.83, 1.27), (-36.83, 2.54))
            make_face()
            # Profile area: 1.45161, perimeter: 15.6305192164
            with BuildLine():
                Line((34.925, -2.54), (34.544, 5.08))
                Line((34.925, -1.27), (34.925, -2.54))
                Line((34.925, 1.27), (34.925, -1.27))
                Line((34.925, 2.54), (34.925, 1.27))
                Line((34.925, 2.54), (34.925, 5.0800001621))
                Line((34.544, 5.08), (34.925, 5.0800001621))
            make_face()
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)
    return part.part


def model_51777_87ff5835_0002():
    """Model: Table-010"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2301097643, perimeter: 7.8920969285
            with BuildLine():
                Line((0.9525, -0.635), (-0.9525, -0.635))
                Line((0.9525, 0.635), (0.9525, -0.635))
                Line((-0.9525, 0.635), (0.9525, 0.635))
                Line((-0.9525, -0.635), (-0.9525, 0.635))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2454323489, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1892402357, perimeter: 1.5420969285
            Circle(0.2454323489)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_51786_e1ecf142_0001():
    """Model: mouth"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.0160000324), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4053659874, perimeter: 2.6119290842
            with BuildLine():
                Line((0.508, 9.2710002959), (-0.5080000162, 9.2710002959))
                CenterArc((0, 9.2710002959), 0.508, 180, 180)
            make_face()
        # OneSide extrude, distance=0.0762
        extrude(amount=0.0762)
    return part.part


def model_51789_37152c12_0000():
    """Model: Upper Base Columon"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 706.8583470577, perimeter: 94.2477796077
            Circle(15)
        # OneSide extrude, distance=170
        extrude(amount=170)
    return part.part


def model_51791_b6580a7f_0002():
    """Model: Inner Bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.3014376029, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_51791_b6580a7f_0003():
    """Model: GyroHolder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.3917007315, perimeter: 78.7202763255
            with BuildLine():
                Line((10.25, -1.5), (10.25, 1.5))
                CenterArc((0, 0), 10.3591746776, -81.6743496696, 73.3486993391)
                Line((-1.5, -10.25), (1.5, -10.25))
                Line((-1.5, -10.25), (-1.5, -11.75))
                Line((-1.5, -11.75), (1.5, -11.75))
                CenterArc((0, 0), 11.8453577405, -82.7249950421, 75.4499900842)
                Line((11.75, -1.5), (11.75, 1.5))
                CenterArc((0, 0), 11.8453577405, 7.2750049579, 75.4499900842)
                Line((-1.5, 11.75), (1.5, 11.75))
                Line((-1.5, 10.25), (-1.5, 11.75))
                Line((-1.5, 10.25), (1.5, 10.25))
                CenterArc((0, 0), 10.3591746776, 8.3256503304, 73.3486993391)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_51791_b6580a7f_0004():
    """Model: InnerSpacers"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


def model_51791_b6580a7f_0005():
    """Model: AdjustmentPin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_51791_b6580a7f_0006():
    """Model: Outer Bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_51791_b6580a7f_0008():
    """Model: Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # Symmetric extrude, each_side=12.5
        extrude(amount=12.5, both=True)
    return part.part


def model_51791_b6580a7f_0009():
    """Model: Inner Gyro"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 54.1924732744, perimeter: 72.2566310326
            with BuildLine():
                CenterArc((0, 0), 6.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_51791_b6580a7f_0010():
    """Model: Counterweight"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((3, -3), (3, 3))
                Line((3, 3), (-3, 3))
                Line((-3, 3), (-3, -3))
                Line((-3, -3), (3, -3))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


def model_51791_b6580a7f_0011():
    """Model: OuterGyro"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70.6858347058, perimeter: 94.2477796077
            with BuildLine():
                CenterArc((0, 0), 8.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_51794_e733d914_0000():
    """Model: Brake Pad Holder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0653338748, perimeter: 17.2238074798
            with BuildLine():
                Line((0.635, -4.7625), (0.635, 0))
                Line((0.635, 0), (0, 0))
                Line((0, 0), (0, -4.7625))
                CenterArc((0.9525, -4.7625), 0.9525, 180, 90)
                Line((3.1694480724, -5.715), (0.9525, -5.715))
                Line((3.1694480724, -5.715), (3.1694480724, -5.08))
                Line((3.1694480724, -5.08), (0.9525, -5.08))
                CenterArc((0.9525, -4.7625), 0.3175, 180, 90)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_51794_e733d914_0001():
    """Model: Frame support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 114.5159, perimeter: 95.25
            with BuildLine():
                Line((22.5425, -1.27), (22.5425, 1.27))
                Line((22.5425, 1.27), (-22.5425, 1.27))
                Line((-22.5425, 1.27), (-22.5425, -1.27))
                Line((-22.5425, -1.27), (22.5425, -1.27))
            make_face()
        # Symmetric extrude, each_side=0.3175
        extrude(amount=0.3175, both=True)
    return part.part


def model_51794_e733d914_0002():
    """Model: Engine Frame Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 296.7736, perimeter: 69.85
            with BuildLine():
                Line((10.16, -7.3025), (-10.16, -7.3025))
                Line((10.16, 7.3025), (10.16, -7.3025))
                Line((-10.16, 7.3025), (10.16, 7.3025))
                Line((-10.16, -7.3025), (-10.16, 7.3025))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_51794_e733d914_0003():
    """Model: Engine Frame Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 214.7173125, perimeter: 99.695
            with BuildLine():
                Line((22.5425, -2.38125), (22.5425, 2.38125))
                Line((22.5425, 2.38125), (-22.5425, 2.38125))
                Line((-22.5425, 2.38125), (-22.5425, -2.38125))
                Line((-22.5425, -2.38125), (22.5425, -2.38125))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_51794_e733d914_0009():
    """Model: Rear Mounting Bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 68.9268195634, perimeter: 61.9537443029
            with BuildLine():
                CenterArc((0, 0), 2.8575, -48.1896851042, 276.3793702084)
                Line((1.905, -2.1298547486), (1.905, -3.81))
                Line((1.905, -3.81), (5.715, -3.81))
                Line((5.715, -3.81), (5.715, 5.08))
                Line((5.715, 5.08), (-5.715, 5.08))
                Line((-5.715, 5.08), (-5.715, -3.81))
                Line((-5.715, -3.81), (-1.905, -3.81))
                Line((-1.905, -3.81), (-1.905, -2.1298547486))
            make_face()
            with BuildLine():
                CenterArc((3.81, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.81, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3175
        extrude(amount=0.3175, both=True)
    return part.part


def model_51794_e733d914_0010():
    """Model: Sprocket Key"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.403225, perimeter: 2.54
            with BuildLine():
                Line((0.3175, -0.3175), (0.3175, 0.3175))
                Line((0.3175, 0.3175), (-0.3175, 0.3175))
                Line((-0.3175, 0.3175), (-0.3175, -0.3175))
                Line((-0.3175, -0.3175), (0.3175, -0.3175))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_51794_e733d914_0011():
    """Model: Brake Key"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.403225, perimeter: 2.54
            with BuildLine():
                Line((0.3175, -0.3175), (0.3175, 0.3175))
                Line((0.3175, 0.3175), (-0.3175, 0.3175))
                Line((-0.3175, 0.3175), (-0.3175, -0.3175))
                Line((-0.3175, -0.3175), (0.3175, -0.3175))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


def model_51863_0b8751d1_0005():
    """Model: Pedal nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.065), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 29.8532345531, perimeter: 29.9766905962
            with BuildLine():
                Line((27.0623479404, -18.4887206645), (25.2923890825, -15.2781009463))
                Line((25.2923890825, -15.2781009463), (21.6269314157, -15.2056204218))
                Line((21.6269314157, -15.2056204218), (19.7314326068, -18.3437596155))
                Line((19.7314326068, -18.3437596155), (21.5013914647, -21.5543793336))
                Line((21.5013914647, -21.5543793336), (25.1668491315, -21.6268598581))
                Line((25.1668491315, -21.6268598581), (27.0623479404, -18.4887206645))
            make_face()
            with BuildLine():
                CenterArc((23.3968902736, -18.41624014), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


def model_51863_0b8751d1_0010():
    """Model: Front tire mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((49.4180662762, 26.8133738724)):
                Circle(1.27)
        # OneSide extrude, distance=36.83
        extrude(amount=36.83)
    return part.part


def model_51864_39932fe9_0006():
    """Model: Door Handle v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.808688385, perimeter: 43.0575151143
            with BuildLine():
                CenterArc((0, -10.5), 14.5, 46.3971810273, 87.2056379454)
                Line((-8.5, 0), (-10, 0))
                CenterArc((0, -13.0038198542), 15.5354218095, 56.8291979368, 66.3416041264)
                Line((10, 0), (8.5, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_51864_39932fe9_0011():
    """Model: Door Pin v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=47
        extrude(amount=47)
    return part.part


def model_51871_86ebf5b2_0015():
    """Model: Lid Side Panels v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 353.4291735289, perimeter: 77.1238898038
            with BuildLine():
                Line((-15, 0), (15, 0))
                CenterArc((0, 0), 15, 0, 180)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_51876_8346832d_0002():
    """Model: carrier v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2670.9624, perimeter: 208.28
            with BuildLine():
                Line((-22.86, 29.21), (22.86, 29.21))
                Line((-22.86, -29.21), (-22.86, 29.21))
                Line((22.86, -29.21), (-22.86, -29.21))
                Line((22.86, 29.21), (22.86, -29.21))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_51877_0032e502_0002():
    """Model: base 11 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.122121821, perimeter: 1.6220184029
            with BuildLine():
                CenterArc((0.8000000119, 0), 0.8000000119, -51.992416157, 37.4769484044)
                Line((1.4745772971, -0.8045074005), (1.292612638, -0.6303434141))
                Line((1.8000000268, -0.3000000045), (1.4745772971, -0.8045074005))
                Line((1.5744640328, -0.2005130903), (1.8000000268, -0.3000000045))
            make_face()
            # Profile area: 0.1444619996, perimeter: 1.7095769381
            with BuildLine():
                Line((-0.2657908708, -0.3619247817), (0.0233609159, -0.1919159545))
                Line((0.1406896638, -0.8045074005), (-0.2657908708, -0.3619247817))
                Line((0.3073873858, -0.6303434141), (0.1406896638, -0.8045074005))
                CenterArc((0.8000000119, 0), 0.8000000119, -166.1196603041, 38.1120764611)
            make_face()
            # Profile area: 0.1315001136, perimeter: 1.7317951676
            with BuildLine():
                Line((1.1000000164, 1.0000000149), (1.1000000164, 0.7416198598))
                Line((0.5000000075, 1.0000000149), (1.1000000164, 1.0000000149))
                Line((0.5000000075, 1.0000000149), (0.5000000075, 0.7416198598))
                CenterArc((0.8000000119, 0), 0.8000000119, 67.975687163, 44.0486256741)
            make_face()
            # Profile area: 2.0106193582, perimeter: 5.0265483206
            with BuildLine():
                CenterArc((0.8000000119, 0), 0.8000000119, -14.5154677526, 82.4911549155)
                CenterArc((0.8000000119, 0), 0.8000000119, 67.975687163, 44.0486256741)
                CenterArc((0.8000000119, 0), 0.8000000119, 112.024312837, 81.8560268589)
                CenterArc((0.8000000119, 0), 0.8000000119, -166.1196603041, 38.1120764611)
                CenterArc((0.8000000119, 0), 0.8000000119, -128.007583843, 76.015167686)
                CenterArc((0.8000000119, 0), 0.8000000119, -51.992416157, 37.4769484044)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_51877_0032e502_0007():
    """Model: Base 6 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.270000008, perimeter: 2.4000000358
            with BuildLine():
                Line((0.9000000134, -0.3000000045), (0, -0.3000000045))
                Line((0.9000000134, 0), (0.9000000134, -0.3000000045))
                Line((0, 0), (0.9000000134, 0))
                Line((0, -0.3000000045), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_51877_0032e502_0008():
    """Model: Third v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685836812, perimeter: 9.4247781012
            with Locations((1.5000000224, 0)):
                Circle(1.5000000224)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_51877_0032e502_0009():
    """Model: Front thing v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((3, 0)):
                Circle(3)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_51877_0032e502_0010():
    """Model: Second part v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.4207950041, perimeter: 18.2212376623
            with Locations((2.9000000432, 0)):
                Circle(2.9000000432)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_51877_0032e502_0011():
    """Model: base 9 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0772566635, perimeter: 2.142477828
            with BuildLine():
                Line((0, -0.6000000089), (0.6000000089, -0.6000000089))
                CenterArc((0.6000000089, 0), 0.6000000089, -180, 90)
                Line((0, 0), (0, -0.6000000089))
            make_face()
            # Profile area: 1.130973389, perimeter: 3.7699112405
            with BuildLine():
                CenterArc((0.6000000089, 0), 0.6000000089, -180, 90)
                CenterArc((0.6000000089, 0), 0.6000000089, -90, 90)
                CenterArc((0.6000000089, 0), 0.6000000089, 0, 180)
            make_face()
            # Profile area: 0.0772566635, perimeter: 2.142477828
            with BuildLine():
                CenterArc((0.6000000089, 0), 0.6000000089, -90, 90)
                Line((0.6000000089, -0.6000000089), (1.2000000179, -0.6000000089))
                Line((1.2000000179, -0.6000000089), (1.2000000179, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_51883_d97df863_0000():
    """Model: Pressure Plate v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 287.1415926536, perimeter: 70.2831853072
            with BuildLine():
                CenterArc((11, 5), 1, 0, 90)
                Line((11, 6), (-11, 6))
                CenterArc((-11, 5), 1, 90, 90)
                Line((-12, 5), (-12, -5))
                CenterArc((-11, -5), 1, 180, 90)
                Line((-11, -6), (11, -6))
                CenterArc((11, -5), 1, -90, 90)
                Line((12, -5), (12, 5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_51883_d97df863_0001():
    """Model: Distance Pad v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.5508836353, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_51883_d97df863_0011():
    """Model: Plastic Plug v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 122.3373451754, perimeter: 52.5681408993
            with BuildLine():
                CenterArc((7.4, -3.7), 0.3, -90, 90)
                Line((7.7, -3.7), (7.7, 3.7))
                CenterArc((7.4, 3.7), 0.3, 0, 90)
                Line((7.4, 4), (-7.4, 4))
                CenterArc((-7.4, 3.7), 0.3, 90, 90)
                Line((-7.7, 3.7), (-7.7, -3.7))
                CenterArc((-7.4, -3.7), 0.3, 180, 90)
                Line((-7.4, -4), (7.4, -4))
            make_face()
            with BuildLine():
                CenterArc((-7.2, 3.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.2, -3.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.2, 3.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.2, -3.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.17
        extrude(amount=0.17)
    return part.part


def model_51883_d97df863_0013():
    """Model: Half Plate v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9384713834, perimeter: 7.3345175598
            with BuildLine():
                CenterArc((0, 0), 3.95, 45, 43.5493189458)
                Line((0.1, 3.9487339743), (0.1, 2.7481812167))
                CenterArc((0, 0), 2.75, 52.2971208366, 35.6189368288)
                CenterArc((1.9445436483, 1.9445436483), 0.35, 45, 93.6485604183)
                Line((2.1920310217, 2.1920310217), (2.7930717857, 2.7930717857))
            make_face()
            # Profile area: 2.196746059, perimeter: 5.8926958935
            with BuildLine():
                CenterArc((1.9445436483, 1.9445436483), 0.35, 138.6485604183, 86.3514395817)
                CenterArc((0, 0), 2.75, 52.2971208366, 35.6189368288)
                Line((0.1, 2.7481812167), (0.1, 1.1456439237))
                CenterArc((0, 0), 1.15, 45, 40.0114580244)
                Line((0.8131727984, 0.8131727984), (1.6970562748, 1.6970562748))
            make_face()
            # Profile area: 2.9384713834, perimeter: 7.3345175598
            with BuildLine():
                Line((0.1, -2.7481812167), (0.1, -3.9487339743))
                CenterArc((0, 0), 3.95, -88.5493189458, 43.5493189458)
                Line((2.1920310217, -2.1920310217), (2.7930717857, -2.7930717857))
                CenterArc((1.9445436483, -1.9445436483), 0.35, -138.6485604183, 93.6485604183)
                CenterArc((0, 0), 2.75, -87.9160576654, 35.6189368288)
            make_face()
            # Profile area: 2.196746059, perimeter: 5.8926958935
            with BuildLine():
                CenterArc((1.9445436483, -1.9445436483), 0.35, 135, 86.3514395817)
                Line((0.8131727984, -0.8131727984), (1.6970562748, -1.6970562748))
                CenterArc((0, 0), 1.15, -85.0114580244, 40.0114580244)
                Line((0.1, -1.1456439237), (0.1, -2.7481812167))
                CenterArc((0, 0), 2.75, -87.9160576654, 35.6189368288)
            make_face()
            # Profile area: 4.7136610666, perimeter: 8.9806142138
            with BuildLine():
                CenterArc((1.9445436483, -1.9445436483), 0.35, 48.6485604183, 86.3514395817)
                CenterArc((0, 0), 2.75, -37.7028791634, 75.4057583269)
                CenterArc((1.9445436483, 1.9445436483), 0.35, -135, 86.3514395817)
                Line((0.8131727984, 0.8131727984), (1.6970562748, 1.6970562748))
                CenterArc((0, 0), 1.15, -45, 90)
                Line((0.8131727984, -0.8131727984), (1.6970562748, -1.6970562748))
            make_face()
            # Profile area: 6.1169796067, perimeter: 12.667995078
            with BuildLine():
                CenterArc((1.9445436483, -1.9445436483), 0.35, -45, 93.6485604183)
                Line((2.1920310217, -2.1920310217), (2.7930717857, -2.7930717857))
                CenterArc((0, 0), 3.95, -45, 90)
                Line((2.1920310217, 2.1920310217), (2.7930717857, 2.7930717857))
                CenterArc((1.9445436483, 1.9445436483), 0.35, -48.6485604183, 93.6485604183)
                CenterArc((0, 0), 2.75, -37.7028791634, 75.4057583269)
            make_face()
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)
    return part.part


def model_51892_6da749d8_0002():
    """Model: podkladka krzyzak"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_51892_6da749d8_0010():
    """Model: podkladka 2mm"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0053096491, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_51892_6da749d8_0011():
    """Model: walce srodek"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-5.5, -0.6000226811)):
                Circle(0.7)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # TwoSides extrude, along=-1.3, against=0.4
        extrude(amount=-1.3)
        extrude(sk.sketch, amount=0.4)
    return part.part


def model_51892_6da749d8_0012():
    """Model: podkladka 3mm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.730420292, perimeter: 9.7389372261
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.375
        extrude(amount=0.375)
    return part.part


def model_51892_6da749d8_0013():
    """Model: podkladka 4mm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4712389729, perimeter: 9.4247780544
            with BuildLine():
                CenterArc((0, 0), 0.8000000149, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.475
        extrude(amount=0.475)
    return part.part


def model_51892_6da749d8_0014():
    """Model: podkladka 5mm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2307544227, perimeter: 9.1146022854
            with BuildLine():
                CenterArc((0, 0), 0.750634008, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_51892_6da749d8_0015():
    """Model: podladka 1,5mm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.151344751, perimeter: 10.2130942424
            with BuildLine():
                CenterArc((0, 0), 0.9254644329, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_51892_6da749d8_0016():
    """Model: baza metal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 26.5686095674, perimeter: 34.1367205934
            with BuildLine():
                Line((-6.8, -1.9000226811), (2.4647375731, -1.9000226811))
                Line((1.3000245682, 1.3), (2.4647375731, -1.9000226811))
                Line((-7.9647130049, 1.3), (1.3000245682, 1.3))
                Line((-6.8, -1.9000226811), (-7.9647130049, 1.3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.5, -0.6000226811), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_51895_5760b481_0004():
    """Model: Horizontal pole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 543.75, perimeter: 368.5
            with BuildLine():
                Line((111.25, -13), (-70, -13))
                Line((111.25, -10), (111.25, -13))
                Line((-70, -10), (111.25, -10))
                Line((-70, -13), (-70, -10))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_51895_5760b481_0008():
    """Model: Short pole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 70.5, perimeter: 53
            with BuildLine():
                Line((-4, 23.5), (-4, 0))
                Line((-4, 0), (-1, 0))
                Line((-1, 0), (-1, 23.5))
                Line((-1, 23.5), (-4, 23.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_51895_5760b481_0009():
    """Model: Midium pole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 300, perimeter: 206
            with BuildLine():
                Line((-120, 100), (-120, 0))
                Line((-120, 0), (-117, 0))
                Line((-117, 0), (-117, 100))
                Line((-117, 100), (-120, 100))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_51895_5760b481_0013():
    """Model: Long pole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 450, perimeter: 306
            with BuildLine():
                Line((10, 150), (10, 0))
                Line((10, 0), (13, 0))
                Line((13, 0), (13, 150))
                Line((13, 150), (10, 150))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


MODELS = {
    "model_45798_b573e9da_0006": {"func": model_45798_b573e9da_0006, "volume": 2.6640705702, "area": 14.3256625004},
    "model_45798_b573e9da_0010": {"func": model_45798_b573e9da_0010, "volume": 0.7351326809, "area": 14.7026536188},
    "model_45798_b573e9da_0011": {"func": model_45798_b573e9da_0011, "volume": 21.8654899248, "area": 225.9433470167},
    "model_45901_95d52151_0000": {"func": model_45901_95d52151_0000, "volume": 125, "area": 150},
    "model_45922_26941172_0000": {"func": model_45922_26941172_0000, "volume": 5.5292030703, "area": 38.7044214922},
    "model_45922_26941172_0002": {"func": model_45922_26941172_0002, "volume": 22.1588555575, "area": 75.4508324291},
    "model_45922_26941172_0006": {"func": model_45922_26941172_0006, "volume": 188.4955592154, "area": 213.6283004441},
    "model_45922_26941172_0008": {"func": model_45922_26941172_0008, "volume": 0.230839209, "area": 4.572614132},
    "model_46016_d699e580_0000": {"func": model_46016_d699e580_0000, "volume": 0.675, "area": 19.35},
    "model_46016_d699e580_0003": {"func": model_46016_d699e580_0003, "volume": 76.81761955, "area": 188.9081912799},
    "model_46016_d699e580_0004": {"func": model_46016_d699e580_0004, "volume": 0.4241150082, "area": 6.5030967929},
    "model_46086_371b5052_0021": {"func": model_46086_371b5052_0021, "volume": 0.811255223, "area": 12.5247645502},
    "model_46086_371b5052_0022": {"func": model_46086_371b5052_0022, "volume": 0.0121265476, "area": 0.3053628059},
    "model_47999_d642cd79_0002": {"func": model_47999_d642cd79_0002, "volume": 3.5497912984, "area": 22.6022284793},
    "model_48224_53cae924_0013": {"func": model_48224_53cae924_0013, "volume": 8207.4072578447, "area": 3051.282581436},
    "model_48290_3a237df1_0004": {"func": model_48290_3a237df1_0004, "volume": 9.6527774768, "area": 32.9359861413},
    "model_48290_3a237df1_0007": {"func": model_48290_3a237df1_0007, "volume": 12.8703699691, "area": 43.0701357233},
    "model_48332_fb679f90_0002": {"func": model_48332_fb679f90_0002, "volume": 0.0456197965, "area": 1.7692793325},
    "model_48332_fb679f90_0004": {"func": model_48332_fb679f90_0004, "volume": 1.6493361431, "area": 34.5575191895},
    "model_48475_02526608_0004": {"func": model_48475_02526608_0004, "volume": 439.8229715026, "area": 1770.2874602978},
    "model_48475_02526608_0005": {"func": model_48475_02526608_0005, "volume": 164.9336143135, "area": 670.7300315414},
    "model_48639_796136da_0007": {"func": model_48639_796136da_0007, "volume": 792.2859708633, "area": 1764.3790909981},
    "model_48724_70685a9d_0004": {"func": model_48724_70685a9d_0004, "volume": 22.2, "area": 87.5},
    "model_48724_70685a9d_0005": {"func": model_48724_70685a9d_0005, "volume": 16.8444370452, "area": 52.9105284122},
    "model_48724_70685a9d_0006": {"func": model_48724_70685a9d_0006, "volume": 1.2405363991, "area": 14.9500540403},
    "model_48724_70685a9d_0009": {"func": model_48724_70685a9d_0009, "volume": 5.4977871438, "area": 59.3761011528},
    "model_48833_b97e9993_0001": {"func": model_48833_b97e9993_0001, "volume": 1.5904312809, "area": 22.4780954364},
    "model_48907_25974aa4_0004": {"func": model_48907_25974aa4_0004, "volume": 0.200559275, "area": 5.2250969015},
    "model_48916_5b0c9682_0000": {"func": model_48916_5b0c9682_0000, "volume": 7.9521564044, "area": 39.3746077555},
    "model_49016_cd1b47bf_0003": {"func": model_49016_cd1b47bf_0003, "volume": 6.8722339297, "area": 55.3705705195},
    "model_49016_cd1b47bf_0019": {"func": model_49016_cd1b47bf_0019, "volume": 0.1570236817, "area": 1.868886},
    "model_49016_cd1b47bf_0020": {"func": model_49016_cd1b47bf_0020, "volume": 0.206220594, "area": 2.1535717802},
    "model_49024_b7f02205_0002": {"func": model_49024_b7f02205_0002, "volume": 0.3609487006, "area": 4.8376215006},
    "model_49024_b7f02205_0003": {"func": model_49024_b7f02205_0003, "volume": 63.5698158074, "area": 170.589318454},
    "model_49024_b7f02205_0005": {"func": model_49024_b7f02205_0005, "volume": 3.6282139727, "area": 21.4222073874},
    "model_49134_e9867f8b_0000": {"func": model_49134_e9867f8b_0000, "volume": 1.5707963268, "area": 9.4247779608},
    "model_49134_e9867f8b_0001": {"func": model_49134_e9867f8b_0001, "volume": 1648, "area": 1680},
    "model_49134_e9867f8b_0004": {"func": model_49134_e9867f8b_0004, "volume": 1600, "area": 1632},
    "model_49134_e9867f8b_0009": {"func": model_49134_e9867f8b_0009, "volume": 4023.1222339297, "area": 16269.9242209787},
    "model_49134_e9867f8b_0011": {"func": model_49134_e9867f8b_0011, "volume": 1505, "area": 1597},
    "model_49134_e9867f8b_0012": {"func": model_49134_e9867f8b_0012, "volume": 8.8574828724, "area": 67.6358721137},
    "model_49145_4a5b250e_0001": {"func": model_49145_4a5b250e_0001, "volume": 0.0180641578, "area": 1.0838494655},
    "model_49222_cbe1959b_0003": {"func": model_49222_cbe1959b_0003, "volume": 0.256707815, "area": 3.3054861195},
    "model_49222_cbe1959b_0004": {"func": model_49222_cbe1959b_0004, "volume": 1.7280000515, "area": 15.900000245},
    "model_49222_cbe1959b_0005": {"func": model_49222_cbe1959b_0005, "volume": 0.2491143513, "area": 5.3389360115},
    "model_49222_cbe1959b_0007": {"func": model_49222_cbe1959b_0007, "volume": 0.0313644212, "area": 1.4373345732},
    "model_49222_cbe1959b_0008": {"func": model_49222_cbe1959b_0008, "volume": 0.2025695955, "area": 1.9292342229},
    "model_49222_cbe1959b_0010": {"func": model_49222_cbe1959b_0010, "volume": 15.2106512181, "area": 59.6287763629},
    "model_49223_c0e227df_0000": {"func": model_49223_c0e227df_0000, "volume": 298.3642420455, "area": 425.7789031029},
    "model_49300_a92e7ac9_0000": {"func": model_49300_a92e7ac9_0000, "volume": 113.5596172314, "area": 150.5769210728},
    "model_49330_c6744767_0012": {"func": model_49330_c6744767_0012, "volume": 35.3429173529, "area": 111.9192382841},
    "model_49418_9aa6df68_0000": {"func": model_49418_9aa6df68_0000, "volume": 1.6, "area": 11.2},
    "model_49502_0ed856f7_0006": {"func": model_49502_0ed856f7_0006, "volume": 26.1537588411, "area": 49.008845396},
    "model_49503_e42c01c0_0004": {"func": model_49503_e42c01c0_0004, "volume": 44.7676953137, "area": 180.6415775814},
    "model_49503_e42c01c0_0006": {"func": model_49503_e42c01c0_0006, "volume": 18.8495559215, "area": 50.2654824574},
    "model_49562_6df35938_0001": {"func": model_49562_6df35938_0001, "volume": 1.1066155556, "area": 8.5260196513},
    "model_49562_6df35938_0003": {"func": model_49562_6df35938_0003, "volume": 0.2945243113, "area": 2.7488935719},
    "model_49562_6df35938_0011": {"func": model_49562_6df35938_0011, "volume": 1.3571680264, "area": 12.0637157898},
    "model_49562_6df35938_0014": {"func": model_49562_6df35938_0014, "volume": 0.0794021858, "area": 2.0890823628},
    "model_49613_1b97c07b_0011": {"func": model_49613_1b97c07b_0011, "volume": 70.6858347058, "area": 108.3849465488},
    "model_49613_1b97c07b_0013": {"func": model_49613_1b97c07b_0013, "volume": 1461.4178688862, "area": 974.2785792575},
    "model_49613_1b97c07b_0018": {"func": model_49613_1b97c07b_0018, "volume": 376.9911184308, "area": 791.6813487046},
    "model_49703_b92021be_0002": {"func": model_49703_b92021be_0002, "volume": 58.7279288402, "area": 155.0202726817},
    "model_49703_b92021be_0004": {"func": model_49703_b92021be_0004, "volume": 7.3711188431, "area": 43.9288900751},
    "model_49703_b92021be_0007": {"func": model_49703_b92021be_0007, "volume": 13.21825109, "area": 70.1517639547},
    "model_49703_b92021be_0014": {"func": model_49703_b92021be_0014, "volume": 8.4879550315, "area": 48.8926064678},
    "model_49812_47872520_0011": {"func": model_49812_47872520_0011, "volume": 54, "area": 111},
    "model_49930_20f0e2ee_0003": {"func": model_49930_20f0e2ee_0003, "volume": 81.1309218769, "area": 203.7999060932},
    "model_49930_20f0e2ee_0004": {"func": model_49930_20f0e2ee_0004, "volume": 77.2222198145, "area": 245.7531273623},
    "model_50020_810cddd7_0000": {"func": model_50020_810cddd7_0000, "volume": 17.0014447715, "area": 49.2279142055},
    "model_50039_be53f8de_0018": {"func": model_50039_be53f8de_0018, "volume": 1253.4890916048, "area": 750.8810547907},
    "model_50214_683032e0_0005": {"func": model_50214_683032e0_0005, "volume": 2.8401643542, "area": 58.8831433231},
    "model_50214_683032e0_0006": {"func": model_50214_683032e0_0006, "volume": 0.0100779885, "area": 0.4307863954},
    "model_50315_0f1419bf_0009": {"func": model_50315_0f1419bf_0009, "volume": 0.4351441236, "area": 6.1396550208},
    "model_50379_ebec8fae_0001": {"func": model_50379_ebec8fae_0001, "volume": 60.32985923, "area": 155.9708959097},
    "model_50379_ebec8fae_0004": {"func": model_50379_ebec8fae_0004, "volume": 40.2199061534, "area": 105.3001479999},
    "model_50382_cb85058c_0009": {"func": model_50382_cb85058c_0009, "volume": 118.2542035313, "area": 381.2198695402},
    "model_50382_cb85058c_0010": {"func": model_50382_cb85058c_0010, "volume": 2.2876503578, "area": 15.5387027879},
    "model_50409_4a322fbf_0006": {"func": model_50409_4a322fbf_0006, "volume": 0.0000314107, "area": 0.0079291532},
    "model_50410_f8f03667_0003": {"func": model_50410_f8f03667_0003, "volume": 0.0219911486, "area": 0.8953539063},
    "model_50410_f8f03667_0004": {"func": model_50410_f8f03667_0004, "volume": 2.0357520395, "area": 22.6194671058},
    "model_50410_f8f03667_0007": {"func": model_50410_f8f03667_0007, "volume": 0.0188495559, "area": 0.7696902001},
    "model_50410_f8f03667_0011": {"func": model_50410_f8f03667_0011, "volume": 1.44, "area": 8.88},
    "model_50417_199cffee_0007": {"func": model_50417_199cffee_0007, "volume": 2765.31705, "area": 3193.542},
    "model_50417_199cffee_0008": {"func": model_50417_199cffee_0008, "volume": 4147.975575, "area": 4717.7325},
    "model_50479_a1f097b3_0001": {"func": model_50479_a1f097b3_0001, "volume": 12.0171458676, "area": 59.9247779608},
    "model_50479_a1f097b3_0017": {"func": model_50479_a1f097b3_0017, "volume": 0.2721404726, "area": 2.8863383029},
    "model_50479_a1f097b3_0018": {"func": model_50479_a1f097b3_0018, "volume": 16.3391597549, "area": 41.2383879706},
    "model_50681_eb7a9f92_0000": {"func": model_50681_eb7a9f92_0000, "volume": 0.4800000143, "area": 3.7600000703},
    "model_50681_eb7a9f92_0007": {"func": model_50681_eb7a9f92_0007, "volume": 0.3800000113, "area": 8.6907964853},
    "model_50681_eb7a9f92_0009": {"func": model_50681_eb7a9f92_0009, "volume": 0.1963495408, "area": 1.9634954085},
    "model_50681_eb7a9f92_0010": {"func": model_50681_eb7a9f92_0010, "volume": 0.0640781959, "area": 1.4509366102},
    "model_50681_eb7a9f92_0011": {"func": model_50681_eb7a9f92_0011, "volume": 0.3769911297, "area": 2.9643315083},
    "model_50681_eb7a9f92_0020": {"func": model_50681_eb7a9f92_0020, "volume": 0.006878759, "area": 0.3928062132},
    "model_50717_f1aaa3b1_0000": {"func": model_50717_f1aaa3b1_0000, "volume": 0.058423957, "area": 6.2690245192},
    "model_50717_f1aaa3b1_0001": {"func": model_50717_f1aaa3b1_0001, "volume": 0.0541943262, "area": 5.614214399},
    "model_50717_f1aaa3b1_0002": {"func": model_50717_f1aaa3b1_0002, "volume": 1.2730696945, "area": 8.2163236025},
    "model_50777_2934de55_0011": {"func": model_50777_2934de55_0011, "volume": 0.072, "area": 1.08},
    "model_50777_2934de55_0014": {"func": model_50777_2934de55_0014, "volume": 0.098770153, "area": 1.9700622839},
    "model_50777_2934de55_0017": {"func": model_50777_2934de55_0017, "volume": 0.2513274123, "area": 2.2619467106},
    "model_50777_2934de55_0020": {"func": model_50777_2934de55_0020, "volume": 0.0049836081, "area": 0.4386021449},
    "model_50778_c57149b9_0000": {"func": model_50778_c57149b9_0000, "volume": 12.5243052739, "area": 82.9546728},
    "model_50778_c57149b9_0003": {"func": model_50778_c57149b9_0003, "volume": 194.8423924122, "area": 368.2502377897},
    "model_50782_2d82ef9f_0003": {"func": model_50782_2d82ef9f_0003, "volume": 42.2365741333, "area": 76.6484395556},
    "model_50782_2d82ef9f_0005": {"func": model_50782_2d82ef9f_0005, "volume": 53.0902761224, "area": 93.740883633},
    "model_50782_2d82ef9f_0006": {"func": model_50782_2d82ef9f_0006, "volume": 49.8726836302, "area": 88.6738088421},
    "model_50897_3be92e2f_0019": {"func": model_50897_3be92e2f_0019, "volume": 14.7227533028, "area": 190.1205938314},
    "model_50897_3be92e2f_0020": {"func": model_50897_3be92e2f_0020, "volume": 117.7820264224, "area": 1488.50513707},
    "model_50897_3be92e2f_0024": {"func": model_50897_3be92e2f_0024, "volume": 53.001910125, "area": 672.3776875},
    "model_50897_3be92e2f_0027": {"func": model_50897_3be92e2f_0027, "volume": 35.33460675, "area": 449.7974875},
    "model_50897_3be92e2f_0034": {"func": model_50897_3be92e2f_0034, "volume": 0.1868149115, "area": 3.3133365942},
    "model_50900_0326428a_0012": {"func": model_50900_0326428a_0012, "volume": 58.7470353002, "area": 188.7574330868},
    "model_50903_f7c8e57e_0000": {"func": model_50903_f7c8e57e_0000, "volume": 43.1968989869, "area": 70.3481987298},
    "model_50903_f7c8e57e_0001": {"func": model_50903_f7c8e57e_0001, "volume": 14.1371669412, "area": 76.9276546012},
    "model_50914_67b32535_0002": {"func": model_50914_67b32535_0002, "volume": 24.5991148575, "area": 87.2814150222},
    "model_50947_49287c16_0007": {"func": model_50947_49287c16_0007, "volume": 24.6053238202, "area": 54.9977759715},
    "model_51022_47816098_0002": {"func": model_51022_47816098_0002, "volume": 366.4275131331, "area": 2098.5996005612},
    "model_51022_47816098_0004": {"func": model_51022_47816098_0004, "volume": 732.8230016469, "area": 528.8230016469},
    "model_51109_97b211c3_0008": {"func": model_51109_97b211c3_0008, "volume": 0.8671411767, "area": 12.9605639004},
    "model_51109_97b211c3_0009": {"func": model_51109_97b211c3_0009, "volume": 1.4564331897, "area": 13.1209650285},
    "model_51336_33ff2eba_0015": {"func": model_51336_33ff2eba_0015, "volume": 1.8849555922, "area": 27.0176968209},
    "model_51336_33ff2eba_0016": {"func": model_51336_33ff2eba_0016, "volume": 0.0021919154, "area": 0.1756878086},
    "model_51341_6ba06c4a_0000": {"func": model_51341_6ba06c4a_0000, "volume": 3.8994627367, "area": 31.7137235714},
    "model_51341_6ba06c4a_0002": {"func": model_51341_6ba06c4a_0002, "volume": 3.6037035913, "area": 26.7541548963},
    "model_51341_6ba06c4a_0005": {"func": model_51341_6ba06c4a_0005, "volume": 2.6142939, "area": 24.701989606},
    "model_51341_6ba06c4a_0008": {"func": model_51341_6ba06c4a_0008, "volume": 0.2895833243, "area": 3.2682632402},
    "model_51345_4b292361_0004": {"func": model_51345_4b292361_0004, "volume": 3.2634118229, "area": 46.769499772},
    "model_51346_87465d9e_0001": {"func": model_51346_87465d9e_0001, "volume": 38727.0901770755, "area": 31760.9245049885},
    "model_51459_874dd272_0000": {"func": model_51459_874dd272_0000, "volume": 1500, "area": 815},
    "model_51509_fd5fcb9c_0001": {"func": model_51509_fd5fcb9c_0001, "volume": 15.5599229171, "area": 85.9833629971},
    "model_51536_a18dc325_0008": {"func": model_51536_a18dc325_0008, "volume": 0.0002985744, "area": 0.0497823836},
    "model_51536_a18dc325_0011": {"func": model_51536_a18dc325_0011, "volume": 3.926990817, "area": 42.4115008235},
    "model_51536_a18dc325_0013": {"func": model_51536_a18dc325_0013, "volume": 0.0038420896, "area": 0.4564168841},
    "model_51559_4293c0e0_0001": {"func": model_51559_4293c0e0_0001, "volume": 0.2214822821, "area": 5.1679199152},
    "model_51567_5f9bb333_0007": {"func": model_51567_5f9bb333_0007, "volume": 207.4958417197, "area": 216.1041828322},
    "model_51585_b695905b_0006": {"func": model_51585_b695905b_0006, "volume": 3.2, "area": 134.4},
    "model_51585_b695905b_0007": {"func": model_51585_b695905b_0007, "volume": 2.368, "area": 47.36},
    "model_51585_b695905b_0011": {"func": model_51585_b695905b_0011, "volume": 262.5, "area": 1786},
    "model_51593_174d44c2_0008": {"func": model_51593_174d44c2_0008, "volume": 12.6, "area": 132.4},
    "model_51595_41f3d1a3_0001": {"func": model_51595_41f3d1a3_0001, "volume": 29.1, "area": 205.82},
    "model_51595_41f3d1a3_0002": {"func": model_51595_41f3d1a3_0002, "volume": 27.354, "area": 193.82},
    "model_51595_41f3d1a3_0005": {"func": model_51595_41f3d1a3_0005, "volume": 80, "area": 232},
    "model_51601_2616f89b_0007": {"func": model_51601_2616f89b_0007, "volume": 2.8274333882, "area": 17.9070781255},
    "model_51601_2616f89b_0015": {"func": model_51601_2616f89b_0015, "volume": 0.3926990817, "area": 3.1415926536},
    "model_51601_2616f89b_0018": {"func": model_51601_2616f89b_0018, "volume": 51.9344535547, "area": 225.8019719768},
    "model_51602_42da13f0_0000": {"func": model_51602_42da13f0_0000, "volume": 3.7699111843, "area": 28.902652413},
    "model_51602_42da13f0_0004": {"func": model_51602_42da13f0_0004, "volume": 0.2685398246, "area": 6.4449557103},
    "model_51602_42da13f0_0006": {"func": model_51602_42da13f0_0006, "volume": 0.0503585741, "area": 1.1680950925},
    "model_51602_42da13f0_0012": {"func": model_51602_42da13f0_0012, "volume": 0.0023125617, "area": 0.5232074725},
    "model_51606_b72fa3d6_0008": {"func": model_51606_b72fa3d6_0008, "volume": 4.2867927925, "area": 28.014757231},
    "model_51606_b72fa3d6_0021": {"func": model_51606_b72fa3d6_0021, "volume": 0.6858763266, "area": 6.2206338439},
    "model_51674_a70c1c6c_0004": {"func": model_51674_a70c1c6c_0004, "volume": 1.3202543127, "area": 27.6931392414},
    "model_51708_867d4509_0000": {"func": model_51708_867d4509_0000, "volume": 43.7715856027, "area": 486.0548968659},
    "model_51747_3d58eae0_0003": {"func": model_51747_3d58eae0_0003, "volume": 0.8318841565, "area": 35.3550766513},
    "model_51777_87ff5835_0001": {"func": model_51777_87ff5835_0001, "volume": 28.2676855569, "area": 113.5723388097},
    "model_51777_87ff5835_0002": {"func": model_51777_87ff5835_0002, "volume": 6.145149, "area": 20.9677},
    "model_51786_e1ecf142_0001": {"func": model_51786_e1ecf142_0001, "volume": 0.0308888879, "area": 1.009760971},
    "model_51789_37152c12_0000": {"func": model_51789_37152c12_0000, "volume": 120165.9189998097, "area": 17435.8392274234},
    "model_51791_b6580a7f_0002": {"func": model_51791_b6580a7f_0002, "volume": 10.6028752059, "area": 38.8772090882},
    "model_51791_b6580a7f_0003": {"func": model_51791_b6580a7f_0003, "volume": 112.783401463, "area": 270.2239541139},
    "model_51791_b6580a7f_0004": {"func": model_51791_b6580a7f_0004, "volume": 2.3561944902, "area": 10.9955742876},
    "model_51791_b6580a7f_0005": {"func": model_51791_b6580a7f_0005, "volume": 0.5890486225, "area": 5.1050880621},
    "model_51791_b6580a7f_0006": {"func": model_51791_b6580a7f_0006, "volume": 10.9955742876, "area": 54.9778714378},
    "model_51791_b6580a7f_0008": {"func": model_51791_b6580a7f_0008, "volume": 44.1786466911, "area": 121.3440162449},
    "model_51791_b6580a7f_0009": {"func": model_51791_b6580a7f_0009, "volume": 108.3849465488, "area": 252.898208614},
    "model_51791_b6580a7f_0010": {"func": model_51791_b6580a7f_0010, "volume": 216, "area": 216},
    "model_51791_b6580a7f_0011": {"func": model_51791_b6580a7f_0011, "volume": 141.3716694115, "area": 329.8672286269},
    "model_51794_e733d914_0000": {"func": model_51794_e733d914_0000, "volume": 12.865948042, "area": 53.8791387482},
    "model_51794_e733d914_0001": {"func": model_51794_e733d914_0001, "volume": 72.7175965, "area": 289.51555},
    "model_51794_e733d914_0002": {"func": model_51794_e733d914_0002, "volume": 188.451236, "area": 637.90195},
    "model_51794_e733d914_0003": {"func": model_51794_e733d914_0003, "volume": 136.3454934375, "area": 492.74095},
    "model_51794_e733d914_0009": {"func": model_51794_e733d914_0009, "volume": 43.7685304228, "area": 177.1942667592},
    "model_51794_e733d914_0010": {"func": model_51794_e733d914_0010, "volume": 2.56047875, "area": 16.93545},
    "model_51794_e733d914_0011": {"func": model_51794_e733d914_0011, "volume": 2.048383, "area": 13.70965},
    "model_51863_0b8751d1_0005": {"func": model_51863_0b8751d1_0005, "volume": 37.9136078825, "area": 97.7768661635},
    "model_51863_0b8751d1_0010": {"func": model_51863_0b8751d1_0010, "volume": 186.6203645516, "area": 304.0244874585},
    "model_51864_39932fe9_0006": {"func": model_51864_39932fe9_0006, "volume": 51.6173767701, "area": 137.7324069987},
    "model_51864_39932fe9_0011": {"func": model_51864_39932fe9_0011, "volume": 36.9137136797, "area": 149.2256510455},
    "model_51871_86ebf5b2_0015": {"func": model_51871_86ebf5b2_0015, "volume": 141.3716694115, "area": 737.7079029792},
    "model_51876_8346832d_0002": {"func": model_51876_8346832d_0002, "volume": 3392.122248, "area": 5606.4404},
    "model_51877_0032e502_0002": {"func": model_51877_0032e502_0002, "volume": 1.4452219754, "area": 8.8668217776},
    "model_51877_0032e502_0007": {"func": model_51877_0032e502_0007, "volume": 0.270000008, "area": 2.9400000519},
    "model_51877_0032e502_0008": {"func": model_51877_0032e502_0008, "volume": 5.654866945, "area": 21.6769898434},
    "model_51877_0032e502_0009": {"func": model_51877_0032e502_0009, "volume": 141.3716694115, "area": 150.7964473723},
    "model_51877_0032e502_0010": {"func": model_51877_0032e502_0010, "volume": 396.3119250614, "area": 326.1601549433},
    "model_51877_0032e502_0011": {"func": model_51877_0032e502_0011, "volume": 1.9282300739, "area": 8.9984069159},
    "model_51883_d97df863_0000": {"func": model_51883_d97df863_0000, "volume": 430.7123889804, "area": 679.7079632679},
    "model_51883_d97df863_0001": {"func": model_51883_d97df863_0001, "volume": 6.2203534541, "area": 42.4115008235},
    "model_51883_d97df863_0011": {"func": model_51883_d97df863_0011, "volume": 20.7973486798, "area": 253.6112743037},
    "model_51883_d97df863_0013": {"func": model_51883_d97df863_0013, "volume": 11.6055915569, "area": 56.2965930546},
    "model_51892_6da749d8_0002": {"func": model_51892_6da749d8_0002, "volume": 0.1884955592, "area": 4.7123889804},
    "model_51892_6da749d8_0010": {"func": model_51892_6da749d8_0010, "volume": 0.2513274123, "area": 4.5238934212},
    "model_51892_6da749d8_0011": {"func": model_51892_6da749d8_0011, "volume": 5.2338933609, "area": 21.1115026321},
    "model_51892_6da749d8_0012": {"func": model_51892_6da749d8_0012, "volume": 0.2739076095, "area": 5.1129420437},
    "model_51892_6da749d8_0013": {"func": model_51892_6da749d8_0013, "volume": 0.2238385121, "area": 5.4192475217},
    "model_51892_6da749d8_0014": {"func": model_51892_6da749d8_0014, "volume": 0.1615280959, "area": 6.8417304452},
    "model_51892_6da749d8_0015": {"func": model_51892_6da749d8_0015, "volume": 0.2302689502, "area": 4.3453083505},
    "model_51892_6da749d8_0016": {"func": model_51892_6da749d8_0016, "volume": 2.6568609567, "area": 56.5508911941},
    "model_51895_5760b481_0004": {"func": model_51895_5760b481_0004, "volume": 1631.25, "area": 2193},
    "model_51895_5760b481_0008": {"func": model_51895_5760b481_0008, "volume": 211.5, "area": 300},
    "model_51895_5760b481_0009": {"func": model_51895_5760b481_0009, "volume": 900, "area": 1218},
    "model_51895_5760b481_0013": {"func": model_51895_5760b481_0013, "volume": 1350, "area": 1818},
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
