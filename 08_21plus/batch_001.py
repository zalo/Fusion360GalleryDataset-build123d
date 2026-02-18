"""Batch 001 - passing/08_21plus
20 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a horizontal aerospace or marine component with a streamlined, elongated shape featuring a raised central hub, tapered ends, and blue accent striping along the wings or flanges.
def model_113355_e82de238_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9806858347, perimeter: 11.7424777961
            with BuildLine():
                CenterArc((-1.85, 0.85), 0.15, 90, 90)
                Line((-2, -0.85), (-2, 0.85))
                CenterArc((-1.85, -0.85), 0.15, 180, 90)
                Line((1.85, -1), (-1.85, -1))
                CenterArc((1.85, -0.85), 0.15, -90, 90)
                Line((2, 0.85), (2, -0.85))
                CenterArc((1.85, 0.85), 0.15, 0, 90)
                Line((-1.85, 1), (1.85, 1))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.8496962709, perimeter: 19.5058276425
            with BuildLine():
                Line((2, 1.6), (2, 0))
                Line((2, 0), (6, 0))
                Line((6, 0), (10.5, 0))
                Line((10.5, 0), (10.5, 0.8))
                Line((6.0000000894, 0.8), (10.5, 0.8))
                CenterArc((6.0000000894, 11.200000447), 10.400000447, -112.6198644555, 22.6198644555)
            make_face()
            # Profile area: 1.600000149, perimeter: 5.6000003725
            with BuildLine():
                Line((10.5, 0), (12.5000001863, 0))
                Line((12.5000001863, 0), (12.5000001863, 0.8))
                Line((10.5, 0.8), (12.5000001863, 0.8))
                Line((10.5, 0), (10.5, 0.8))
            make_face()
            # Profile area: 7.8496962709, perimeter: 19.5058276425
            with BuildLine():
                Line((-10.5, 0), (-10.5, 0.8))
                Line((-6, 0), (-10.5, 0))
                Line((-2, 0), (-6, 0))
                Line((-2, 1.6), (-2, 0))
                CenterArc((-6.0000000894, 11.200000447), 10.400000447, -90, 22.6198644555)
                Line((-6.0000000894, 0.8), (-10.5, 0.8))
            make_face()
            # Profile area: 2.4000000358, perimeter: 7.6000000894
            with BuildLine():
                Line((-13.5000000894, 0.8), (-13.5, 0))
                Line((-10.5, 0), (-13.5, 0))
                Line((-10.5, 0), (-10.5, 0.8))
                Line((-10.5, 0.8), (-13.5000000894, 0.8))
            make_face()
        # Start offset: -0.15 (not directly supported, may affect result)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-11.5000001863, 0.5)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-11.5000001714, -0.5000000075)):
                Circle(0.225)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((10.7500000894, 0.5)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((10.7500000894, -0.5)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((11.5000000894, -0.5)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((11.5000000894, 0.5)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((12.2500000894, 0.5)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((12.2500000894, -0.5)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((13.0000000894, -0.5)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((13.0000000894, 0.5)):
                Circle(0.225)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.11, perimeter: 8
            with BuildLine():
                Line((-1.85, 0.55), (-1.85, 0.85))
                Line((1.85, 0.55), (-1.85, 0.55))
                Line((1.85, 0.85), (1.85, 0.55))
                Line((-1.85, 0.85), (1.85, 0.85))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, taper=-10, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on Profile plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.42, perimeter: 2.6
            with BuildLine():
                Line((1.85, 0.55), (1.25, 0.55))
                Line((1.25, -0.15), (1.25, 0.55))
                Line((1.85, -0.15), (1.25, -0.15))
                Line((1.85, 0.55), (1.85, -0.15))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, taper=-10, mode=Mode.ADD)

        # Sketch10 -> Extrude8 (Join)
        # Sketch on Profile plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3, perimeter: 2.2
            with BuildLine():
                Line((-1.25, 0.55), (-1.25, 0.05))
                Line((-1.85, 0.55), (-1.25, 0.55))
                Line((-1.85, 0.05), (-1.85, 0.55))
                Line((-1.25, 0.05), (-1.85, 0.05))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, taper=-10, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on Profile plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.285, perimeter: 2.15
            with BuildLine():
                Line((-1.85, -0.425), (-1.25, -0.425))
                Line((-1.25, -0.425), (-1.25, 0.05))
                Line((-1.25, 0.05), (-1.85, 0.05))
                Line((-1.85, 0.05), (-1.85, -0.425))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, taper=-10, mode=Mode.ADD)

        # Sketch8 -> Extrude10 (Join)
        # Sketch on Profile plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.255, perimeter: 2.05
            with BuildLine():
                Line((-1.85, -0.425), (-1.85, -0.85))
                Line((-1.85, -0.85), (-1.25, -0.85))
                Line((-1.25, -0.85), (-1.25, -0.425))
                Line((-1.25, -0.425), (-1.85, -0.425))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, taper=-10, mode=Mode.ADD)

        # Sketch11 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.42, perimeter: 2.6
            with BuildLine():
                Line((1.85, -0.85), (1.85, -0.15))
                Line((1.85, -0.15), (1.25, -0.15))
                Line((1.25, -0.85), (1.25, -0.15))
                Line((1.85, -0.85), (1.25, -0.85))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, taper=-10, mode=Mode.ADD)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5, perimeter: 7.8
            with BuildLine():
                Line((1.25, -0.15), (1.25, 0.55))
                Line((1.25, 0.55), (-1.25, 0.55))
                Line((-1.25, 0.55), (-1.25, 0.05))
                Line((-1.25, 0.05), (-1.25, -0.425))
                Line((-1.25, -0.425), (-1.25, -0.85))
                Line((-1.25, -0.85), (1.25, -0.85))
                Line((1.25, -0.85), (1.25, -0.15))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5250000093, perimeter: 21.1000003725
            with BuildLine():
                Line((2, 0.05), (2, 0))
                Line((2, 0), (12.5000001863, 0))
                Line((12.5000001863, 0), (12.5000001863, 0.05))
                Line((12.5000001863, 0.05), (2, 0.05))
            make_face()
        # Start offset: -0.15 (not directly supported, may affect result)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude14 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5750000001, perimeter: 23.1000000056
            with BuildLine():
                Line((-13.5, 0), (-2, 0))
                Line((-2, 0), (-2, 0.05))
                Line((-2, 0.05), (-13.5000000056, 0.05))
                Line((-13.5000000056, 0.05), (-13.5, 0))
            make_face()
        # Start offset: -0.15 (not directly supported, may affect result)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch18 -> Extrude16 (Cut)
        # Sketch on Profile plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0198000002, perimeter: 1.0199999996
            with BuildLine():
                Line((1.6000000238, -0.5500000082), (1.6000000238, -0.5099999886))
                Line((1.6799999624, -0.5099999886), (1.6000000238, -0.5099999886))
                Line((1.6799999624, -0.4799999893), (1.6799999624, -0.5099999886))
                Line((1.6000000238, -0.4799999893), (1.6799999624, -0.4799999893))
                Line((1.6000000238, -0.3500000052), (1.6000000238, -0.4799999893))
                Line((1.5500000231, -0.3500000052), (1.6000000238, -0.3500000052))
                Line((1.5500000231, -0.4799999893), (1.5500000231, -0.3500000052))
                Line((1.4699999671, -0.4799999893), (1.5500000231, -0.4799999893))
                Line((1.4699999671, -0.5099999886), (1.4699999671, -0.4799999893))
                Line((1.5500000231, -0.5099999886), (1.4699999671, -0.5099999886))
                Line((1.5500000231, -0.5500000082), (1.5500000231, -0.5099999886))
                Line((1.5500000231, -0.6500000097), (1.5500000231, -0.5500000082))
                Line((1.6000000238, -0.6500000097), (1.5500000231, -0.6500000097))
                Line((1.6000000238, -0.5500000082), (1.6000000238, -0.6500000097))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch19 -> Extrude17 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0263554634, perimeter: 0.8706229269
            with BuildLine():
                Line((1.3873665231, 0.2226779627), (1.7500000261, 0.2226779627))
                Line((1.3873665231, 0.1500000022), (1.3873665231, 0.2226779627))
                Line((1.7500000261, 0.1500000022), (1.3873665231, 0.1500000022))
                Line((1.7500000261, 0.2226779627), (1.7500000261, 0.1500000022))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch20 -> Extrude18 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.01, perimeter: 0.5
            with BuildLine():
                Line((0.150000003, 0.8000000089), (0.200000003, 0.8000000089))
                Line((0.150000003, 0.6000000089), (0.150000003, 0.8000000089))
                Line((0.200000003, 0.6000000089), (0.150000003, 0.6000000089))
                Line((0.200000003, 0.8000000089), (0.200000003, 0.6000000089))
            make_face()
        # OneSide extrude, distance=-0.015
        extrude(amount=-0.015, mode=Mode.SUBTRACT)

        # Sketch21 -> Extrude19 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0087500001, perimeter: 0.5700000075
            with BuildLine():
                Line((0.1000000015, 0.8000000119), (0.0720000015, 0.8210000119))
                Line((0.0720000015, 0.8210000119), (-0.0780000007, 0.6210000089))
                Line((-0.0500000007, 0.6000000089), (-0.0780000007, 0.6210000089))
                Line((0.1000000015, 0.8000000119), (-0.0500000007, 0.6000000089))
            make_face()
        # OneSide extrude, distance=-0.015
        extrude(amount=-0.015, mode=Mode.SUBTRACT)

        # Sketch22 -> Extrude20 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.200000003, 0.7000000104)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.015
        extrude(amount=-0.015, mode=Mode.SUBTRACT)

        # Sketch23 -> Extrude21 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.02920601, perimeter: 1.3255555591
            with BuildLine():
                Line((-1.55, -0.7000000104), (-1.6276970956, -0.7000000104))
                Line((-1.6276970956, -0.7000000104), (-1.6276970956, -0.7477320115))
                Line((-1.6276970956, -0.7477320115), (-1.4000000209, -0.7477320115))
                Line((-1.4000000209, -0.7477320115), (-1.4000000209, -0.7000000104))
                Line((-1.4000000209, -0.7000000104), (-1.5000000224, -0.7000000104))
                Line((-1.5000000224, -0.5312497234), (-1.5000000224, -0.7000000104))
                Line((-1.403196945, -0.5312497234), (-1.5000000224, -0.5312497234))
                Line((-1.403196945, -0.4871514796), (-1.403196945, -0.5312497234))
                Line((-1.6276970956, -0.4871514796), (-1.403196945, -0.4871514796))
                Line((-1.6276970956, -0.5312497234), (-1.6276970956, -0.4871514796))
                Line((-1.55, -0.5312497234), (-1.6276970956, -0.5312497234))
                Line((-1.55, -0.7000000104), (-1.55, -0.5312497234))
            make_face()
        # OneSide extrude, distance=-0.015
        extrude(amount=-0.015, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal bracket or frame assembly with an angular, open-sided design featuring a central horizontal base, two vertical flanges on opposing sides, and a triangulated internal bracing structure for rigidity.
def model_121701_05cb78e4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6000, perimeter: 340
            with BuildLine():
                Line((60, -25), (60, 25))
                Line((60, 25), (-60, 25))
                Line((-60, 25), (-60, -25))
                Line((-60, -25), (60, -25))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2000, perimeter: 180
            with BuildLine():
                Line((20, -25), (20, 25))
                Line((60, -25), (20, -25))
                Line((60, 25), (60, -25))
                Line((20, 25), (60, 25))
            make_face()
        # OneSide extrude, distance=55
        extrude(amount=55, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1128.125, perimeter: 142.5
            with BuildLine():
                Line((25, -23.75), (25, 0))
                Line((25, 0), (-22.5, 0))
                Line((-22.5, 0), (-22.5, -23.75))
                Line((-22.5, -23.75), (25, -23.75))
            make_face()
            # Profile area: 1128.125, perimeter: 142.5
            with BuildLine():
                Line((25, -51.25), (25, -27.5))
                Line((25, -27.5), (-22.5, -27.5))
                Line((-22.5, -27.5), (-22.5, -51.25))
                Line((-22.5, -51.25), (25, -51.25))
            make_face()
        # OneSide extrude, distance=-37.5
        extrude(amount=-37.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 63.5603165161, perimeter: 55.8482532129
            with BuildLine():
                Line((-22.5, -23.75), (-22.5, -27.5))
                Line((-22.5, -20), (-22.5, -23.75))
                Line((-25, -20), (-22.5, -20))
                Line((-25, -45.4241266064), (-25, -20))
                Line((-22.5, -45.4241266064), (-25, -45.4241266064))
                Line((-22.5, -27.5), (-22.5, -45.4241266064))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 25, perimeter: 25
            with BuildLine():
                Line((-22.5, -10), (-22.5, 0))
                Line((-22.5, 0), (-25, 0))
                Line((-25, 0), (-25, -10))
                Line((-25, -10), (-22.5, -10))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(57.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 25, perimeter: 25
            with BuildLine():
                Line((22.5, -10), (25, -10))
                Line((25, -10), (25, 0))
                Line((25, 0), (22.5, 0))
                Line((22.5, 0), (22.5, -10))
            make_face()
        # OneSide extrude, distance=117.5
        extrude(amount=117.5, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-60, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 450, perimeter: 110
            with BuildLine():
                Line((22.5, -10), (-22.5, -10))
                Line((22.5, 0), (22.5, -10))
                Line((-22.5, 0), (22.5, 0))
                Line((-22.5, -10), (-22.5, 0))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -10, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3595.5, perimeter: 249.8
            with BuildLine():
                Line((20, -22.5), (-59.9, -22.5))
                Line((20, 22.5), (20, -22.5))
                Line((-59.9, 22.5), (20, 22.5))
                Line((-59.9, -22.5), (-59.9, 22.5))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-60, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2250, perimeter: 190
            with BuildLine():
                Line((25, -55), (-25, -55))
                Line((25, -10), (25, -55))
                Line((-25, -10), (25, -10))
                Line((-25, -55), (-25, -10))
            make_face()
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-60, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 625, perimeter: 125
            with BuildLine():
                Line((25, 2.5), (25, -10))
                Line((-25, 2.5), (25, 2.5))
                Line((-25, -10), (-25, 2.5))
                Line((-25, -10), (25, -10))
            make_face()
            # Profile area: 2250, perimeter: 190
            with BuildLine():
                Line((25, -55), (-25, -55))
                Line((25, -10), (25, -55))
                Line((-25, -10), (25, -10))
                Line((-25, -55), (-25, -10))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch11 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-60, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1520, perimeter: 156
            with BuildLine():
                Line((18, -53), (-22, -53))
                Line((18, -15), (18, -53))
                Line((-22, -15), (18, -15))
                Line((-22, -53), (-22, -15))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 178.125, perimeter: 102.5
            with BuildLine():
                Line((25, -27.5), (-22.5, -27.5))
                Line((25, -23.75), (25, -27.5))
                Line((25, -23.75), (-22.5, -23.75))
                Line((-22.5, -23.75), (-22.5, -27.5))
            make_face()
            # Profile area: 659.0749879372, perimeter: 130.2789626855
            with BuildLine():
                Line((-22.5226005806, -9.8831192378), (25, -9.8831192378))
                Line((-22.5226005806, -27.5), (-22.5226005806, -9.8831192378))
                Line((-22.5, -27.5), (-22.5226005806, -27.5))
                Line((-22.5, -23.75), (-22.5, -27.5))
                Line((25, -23.75), (-22.5, -23.75))
                Line((25, -9.8831192378), (25, -23.75))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 515.625, perimeter: 102.5
            with BuildLine():
                Line((57.5, -10), (20, -10))
                Line((20, -23.75), (20, -10))
                Line((57.5, -23.75), (20, -23.75))
                Line((57.5, -23.75), (57.5, -10))
            make_face()
            # Profile area: 140.8, perimeter: 110.02
            with BuildLine():
                Line((57.5, -23.75), (20, -23.75))
                Line((20, -23.75), (20, -10))
                Line((20, -10), (19.99, -10))
                Line((19.99, -10), (19.99, -27.5))
                Line((19.99, -27.5), (57.5, -27.5))
                Line((57.5, -27.5), (57.5, -23.75))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch16 -> Extrude16 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 890.625, perimeter: 122.5
            with BuildLine():
                Line((20, -27.5), (20, -51.25))
                Line((20, -51.25), (57.5, -51.25))
                Line((57.5, -51.25), (57.5, -27.5))
                Line((57.5, -27.5), (20, -27.5))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01)

        # Sketch17 -> Extrude17 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(19.99, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1130.3056254086, perimeter: 142.6017985859
            with BuildLine():
                Line((25.01, -51.290899293), (25.01, -27.5))
                Line((25.01, -27.5), (-22.5, -27.5))
                Line((-22.5, -27.5), (-22.5, -51.290899293))
                Line((-22.5, -51.290899293), (25.01, -51.290899293))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.ADD)

        # Sketch14 -> Extrude14 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 179.5232692121, perimeter: 114.4437868246
            with BuildLine():
                Line((-22.6460200187, -55), (-22.6460200187, -45.4241266064))
                Line((25, -55), (-22.6460200187, -55))
                Line((25, -51.25), (25, -55))
                Line((25, -51.25), (-22.5, -51.25))
                Line((-22.5, -51.25), (-22.5, -45.4241266064))
                Line((-22.5, -45.4241266064), (-22.6460200187, -45.4241266064))
            make_face()
            # Profile area: 1312.0500198338, perimeter: 150.4026542486
            with BuildLine():
                Line((-22.5, -45.4241266064), (-22.6460200187, -45.4241266064))
                Line((-22.5, -51.25), (-22.5, -45.4241266064))
                Line((25, -51.25), (-22.5, -51.25))
                Line((25, -23.6946928944), (25, -51.25))
                Line((-22.6460200187, -23.6946928944), (25, -23.6946928944))
                Line((-22.6460200187, -45.4241266064), (-22.6460200187, -23.6946928944))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch18 -> Extrude18 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            with Locations((-11.1151012197, -16.9696346444)):
                Circle(2.4)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch19 -> Extrude19 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            with Locations((53.182380864, -16.940895335)):
                Circle(2.4)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex geometric bracket or mounting component featuring an irregular polyhedron shape with angular faceted surfaces, internal geometric framework, a rectangular opening or slot, and a protruding base or foot element for attachment or mounting purposes.
def model_122019_3a524981_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0156, perimeter: 3.1199999955
            with BuildLine():
                Line((0.2500000037, -0.200000003), (-0.1499999966, -0.200000003))
                Line((0.2500000037, 0.1999999955), (0.2500000037, -0.200000003))
                Line((-0.1499999966, 0.1999999955), (0.2500000037, 0.1999999955))
                Line((-0.1499999966, -0.200000003), (-0.1499999966, 0.1999999955))
            make_face()
            with BuildLine():
                Line((0.2400000037, 0.1899999955), (0.2400000037, -0.190000003))
                Line((0.2400000037, -0.190000003), (-0.1399999966, -0.190000003))
                Line((-0.1399999966, -0.190000003), (-0.1399999966, 0.1899999955))
                Line((-0.1399999966, 0.1899999955), (0.2400000037, 0.1899999955))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.200000003), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0391366127, perimeter: 0.8342035038
            with BuildLine():
                Line((0.0999999978, 0), (0.0999999978, 0.2499999944))
                CenterArc((0.0349999992, 0.2499999944), 0.0649999985, 0, 180)
                Line((-0.0299999993, 0.2499999944), (-0.0299999993, 0))
                Line((-0.0299999993, 0), (0.0999999978, 0))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1599999996, perimeter: 1.5999999978
            with BuildLine():
                Line((-0.1499999966, 0.1999999955), (-0.1499999966, -0.200000003))
                Line((-0.1499999966, -0.200000003), (0.2500000037, -0.200000003))
                Line((0.2500000037, -0.200000003), (0.2500000037, 0.1999999955))
                Line((0.2500000037, 0.1999999955), (-0.1499999966, 0.1999999955))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1599999996, perimeter: 1.5999999978
            with BuildLine():
                Line((0.2500000037, -0.200000003), (-0.1499999966, -0.200000003))
                Line((0.2500000037, 0.1999999955), (0.2500000037, -0.200000003))
                Line((-0.1499999966, 0.1999999955), (0.2500000037, 0.1999999955))
                Line((-0.1499999966, -0.200000003), (-0.1499999966, 0.1999999955))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.200000003), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.001428908, perimeter: 0.8065232015
            with BuildLine():
                Line((0.2500000037, 0.4), (-0.1499999966, 0.4))
                Line((0.2500000037, 0.4), (-0.1492783928, 0.40714454))
                Line((-0.1499999966, 0.4), (-0.1492783928, 0.40714454))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2500000037, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0303999986, perimeter: 0.6999999844
            with BuildLine():
                Line((0.0999999978, 0.1199999973), (-0.089999998, 0.1199999973))
                Line((0.0999999978, 0.2799999937), (0.0999999978, 0.1199999973))
                Line((-0.089999998, 0.2799999937), (0.0999999978, 0.2799999937))
                Line((-0.089999998, 0.1199999973), (-0.089999998, 0.2799999937))
            make_face()
        # OneSide extrude, distance=-0.08
        extrude(amount=-0.08, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.200000003), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0013, perimeter: 0.2799999942
            with BuildLine():
                Line((0.0999999978, 0.01), (0.0999999978, 0))
                Line((0.0999999978, 0.01), (-0.0299999993, 0.01))
                Line((-0.0299999993, 0), (-0.0299999993, 0.01))
                Line((-0.0299999993, 0), (0.0999999978, 0))
            make_face()
            # Profile area: 0.0025999999, perimeter: 0.2999999933
            with BuildLine():
                Line((-0.0299999993, 0), (0.0999999978, 0))
                Line((-0.0299999993, -0.0199999996), (-0.0299999993, 0))
                Line((-0.0299999993, -0.0199999996), (0.0999999978, -0.0199999996))
                Line((0.0999999978, 0), (0.0999999978, -0.0199999996))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.200000003), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0038999998, perimeter: 0.3199999928
            with BuildLine():
                Line((-0.0299999993, -0.0199999996), (0.0999999978, -0.0199999996))
                Line((-0.0299999993, -0.0499999989), (-0.0299999993, -0.0199999996))
                Line((-0.0299999993, -0.0499999989), (0.0999999978, -0.0499999989))
                Line((0.0999999978, -0.0199999996), (0.0999999978, -0.0499999989))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch9 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.200000003), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0038999998, perimeter: 0.3199999928
            with BuildLine():
                Line((-0.0299999993, -0.0499999989), (0.0999999978, -0.0499999989))
                Line((-0.0299999993, -0.0799999982), (-0.0299999993, -0.0499999989))
                Line((-0.0299999993, -0.0799999982), (0.0999999978, -0.0799999982))
                Line((0.0999999978, -0.0499999989), (0.0999999978, -0.0799999982))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch9 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.200000003), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0038999998, perimeter: 0.3199999928
            with BuildLine():
                Line((-0.0299999993, -0.0799999982), (0.0999999978, -0.0799999982))
                Line((-0.0299999993, -0.1099999975), (-0.0299999993, -0.0799999982))
                Line((0.0999999978, -0.1099999975), (-0.0299999993, -0.1099999975))
                Line((0.0999999978, -0.0799999982), (0.0999999978, -0.1099999975))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch10 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.200000003), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0394563412, perimeter: 0.9551555392
            with BuildLine():
                Line((-0.1431143444, 0.4070342428), (0.2500000037, 0.4))
                Line((0.0500000035, 0.6043159488), (0.2500000037, 0.4))
                Line((-0.1431143444, 0.4070342428), (0.0500000035, 0.6043159488))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch11 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.1999999955), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1600000001, perimeter: 1.6000000007
            with BuildLine():
                Line((-0.2500000037, 0.4), (0.1499999966, 0.4))
                Line((-0.2500000037, 0.4), (-0.2500000037, 0))
                Line((-0.2500000037, 0), (0.1499999966, 0))
                Line((0.1499999966, 0), (0.1499999966, 0.4))
            make_face()
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch12 -> Extrude14 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2500000037, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.18, perimeter: 1.7
            with BuildLine():
                Line((0.6499999955, 0), (0.6499999955, 0.4))
                Line((0.6499999955, 0.4), (0.1999999955, 0.4))
                Line((0.1999999955, 0.4), (0.1999999955, 0))
                Line((0.1999999955, 0), (0.6499999955, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch13 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0710708753, perimeter: 5.5968251711
            with BuildLine():
                Line((0.1499999966, -0.6499999955), (0.1499999966, -0.1999999955))
                Line((0.1499999966, -0.1999999955), (-0.2500000037, -0.1999999955))
                Line((-0.2500000037, -0.1999999955), (-0.8500000037, -0.1999999955))
                Line((-0.8500000037, -0.1999999955), (-0.8500000037, -0.6499999955))
                Line((-0.8500000037, -0.6499999955), (0.1499999966, -0.6499999955))
            make_face()
            with BuildLine():
                Line((-0.8246031499, -0.6246031417), (0.1246031428, -0.6246031417))
                Line((-0.8246031499, -0.2253968493), (-0.8246031499, -0.6246031417))
                Line((-0.2500000037, -0.2253968493), (-0.8246031499, -0.2253968493))
                Line((0.1246031428, -0.2253968493), (-0.2500000037, -0.2253968493))
                Line((0.1246031428, -0.6246031417), (0.1246031428, -0.2253968493))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a structural assembly or bracket component featuring an elongated body with two large cylindrical bosses (one at each end), connected by a truss-latticed framework with triangular bracing, designed for load distribution and structural rigidity.
def model_132294_69821e40_0000():
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
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0134083704, perimeter: 1.3079616194
            with BuildLine():
                CenterArc((0.4254017094, -0.3176057162), 0.1143356271, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.4254017094, -0.3176057162), 0.09383293, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0032838064, perimeter: 0.371542032
            with BuildLine():
                Line((-0.7412378986, -0.2783801322), (-0.7406775914, -0.2733201711))
                Line((-0.7425905334, -0.2905953607), (-0.7412378986, -0.2783801322))
                Line((-0.5810334049, -0.2920999965), (-0.7425905334, -0.2905953607))
                Line((-0.5723509649, -0.2694825123), (-0.5810334049, -0.2920999965))
                Line((-0.5723509649, -0.2694825123), (-0.7406775914, -0.2733201711))
            make_face()
            # Profile area: 0.006002322, perimeter: 0.4763218762
            with BuildLine():
                Line((0.7463926231, -0.0961087463), (0.6993566199, -0.1437470262))
                Line((0.7457888674, -0.0888725519), (0.7463926231, -0.0961087463))
                Line((0.6058847822, -0.1005455238), (0.7457888674, -0.0888725519))
                Line((0.6058847822, -0.1005455238), (0.5314462429, -0.1199278863))
                _nurbs_edge([(0.5261928237, -0.1242869397), (0.5262513145, -0.1240920418), (0.526581328, -0.1233433465), (0.5273272979, -0.1225235528), (0.528489586, -0.1216326651), (0.5300670685, -0.1206708764), (0.5314462429, -0.1199278863)], [1, 1, 1, 1, 1, 1, 1], [0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.6993566199, -0.1437470262), (0.6974710685, -0.1431284348), (0.6938252373, -0.1419138531), (0.6887323242, -0.1401597824), (0.6826963486, -0.1379571922), (0.676371883, -0.1354380361), (0.6711211954, -0.1331689468), (0.6666294875, -0.1311771255), (0.6623320705, -0.1295048878), (0.6573875972, -0.1282089697), (0.6508933497, -0.1273411201), (0.6420757369, -0.1269298508), (0.6304725365, -0.1269632714), (0.6161748632, -0.1273648586), (0.5998763769, -0.1279905941), (0.5826433271, -0.1286570698), (0.5657631101, -0.1291608476), (0.5505631991, -0.1293013384), (0.5382529287, -0.1289010322), (0.5303534203, -0.1279083793), (0.5269727117, -0.1266430262), (0.5260604025, -0.1254619007), (0.5260908114, -0.1246268564), (0.5261928237, -0.1242869397)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281], 5)
            make_face()
            # Profile area: 0.0127780431, perimeter: 0.6818787023
            with BuildLine():
                _nurbs_edge([(0.5261928237, -0.1242869397), (0.5262513145, -0.1240920418), (0.526581328, -0.1233433465), (0.5273272979, -0.1225235528), (0.528489586, -0.1216326651), (0.5300670685, -0.1206708764), (0.5314462429, -0.1199278863)], [1, 1, 1, 1, 1, 1, 1], [0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0.6058847822, -0.1005455238), (0.5314462429, -0.1199278863))
                Line((0.5896076711, -0.0961087463), (0.6058847822, -0.1005455238))
                Line((0.330199996, -0.0253999997), (0.5896076711, -0.0961087463))
                Line((0.2944288952, -0.0132714189), (0.330199996, -0.0253999997))
                Line((0.2944288952, -0.0132714189), (0.4017420183, -0.110236705))
                Line((0.4017420183, -0.110236705), (0.4172916507, -0.1242869397))
                Line((0.4172916507, -0.1242869397), (0.5261928237, -0.1242869397))
            make_face()
            # Profile area: 0.0034226441, perimeter: 0.3971336242
            with BuildLine():
                Line((0.7379496568, -0.2544621321), (0.7379496568, -0.2727924934))
                Line((0.7379496568, -0.2544621321), (0.5562600035, -0.2544621321))
                Line((0.5562600035, -0.2544621321), (0.5613400035, -0.2743200017))
                Line((0.5613400035, -0.2743200017), (0.7379496568, -0.2727924934))
            make_face()
            # Profile area: 0.0053869582, perimeter: 0.6725174027
            with BuildLine():
                Line((-0.2007220347, -0.1346608173), (-0.0761999991, -0.0634999992))
                Line((-0.0761999991, -0.0634999992), (0.0188436074, -0.0194601428))
                Line((0.0188436074, -0.0194601428), (0.0352262351, -0.0118690107))
                Line((0.0352262351, -0.0118690107), (0.0516088628, -0.0042778785))
                Line((0.0124604498, -0.0042778785), (0.0516088628, -0.0042778785))
                Line((-0.0091874172, -0.0147015591), (0.0124604498, -0.0042778785))
                Line((-0.2540119951, -0.1325872237), (-0.0091874172, -0.0147015591))
                Line((-0.2540119951, -0.1325872237), (-0.2007220347, -0.1346608173))
            make_face()
            # Profile area: 0.0019288015, perimeter: 0.1872426777
            with BuildLine():
                Line((0.704876108, -0.1671479692), (0.7029324818, -0.2323904079))
                Line((0.7029324818, -0.1652289157), (0.704876108, -0.1671479692))
                Line((0.7029324818, -0.1652289157), (0.6731000042, -0.1803400011))
                Line((0.6731000042, -0.1803400011), (0.6705600042, -0.2336800015))
                Line((0.6705600042, -0.2336800015), (0.7029324818, -0.2323904079))
            make_face()
            # Profile area: 0.0133954006, perimeter: 1.3141772122
            with BuildLine():
                CenterArc((-0.4465879508, -0.3300338749), 0.1148731569, 102.6673993189, 334.6652013622)
                Line((-0.4213972899, -0.2179567908), (-0.4392027784, -0.2179567908))
                Line((-0.4392027784, -0.2179567908), (-0.4717786118, -0.2179567908))
            make_face()
            with BuildLine():
                CenterArc((-0.4465879508, -0.3300338749), 0.0943503403, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1715450556, perimeter: 5.8330589018
            with BuildLine():
                Line((0.6993566199, -0.1437470262), (0.7009888555, -0.1633098621))
                _nurbs_edge([(0.6993566199, -0.1437470262), (0.6974710685, -0.1431284348), (0.6938252373, -0.1419138531), (0.6887323242, -0.1401597824), (0.6826963486, -0.1379571922), (0.676371883, -0.1354380361), (0.6711211954, -0.1331689468), (0.6666294875, -0.1311771255), (0.6623320705, -0.1295048878), (0.6573875972, -0.1282089697), (0.6508933497, -0.1273411201), (0.6420757369, -0.1269298508), (0.6304725365, -0.1269632714), (0.6161748632, -0.1273648586), (0.5998763769, -0.1279905941), (0.5826433271, -0.1286570698), (0.5657631101, -0.1291608476), (0.5505631991, -0.1293013384), (0.5382529287, -0.1289010322), (0.5303534203, -0.1279083793), (0.5269727117, -0.1266430262), (0.5260604025, -0.1254619007), (0.5260908114, -0.1246268564), (0.5261928237, -0.1242869397)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281], 5)
                Line((0.4172916507, -0.1242869397), (0.5261928237, -0.1242869397))
                Line((0.4017420183, -0.110236705), (0.4172916507, -0.1242869397))
                Line((0.2944288952, -0.0132714189), (0.4017420183, -0.110236705))
                Line((0.2832754406, -0.0094897188), (0.2944288952, -0.0132714189))
                Line((0.2151346098, -0.0042778785), (0.2832754406, -0.0094897188))
                Line((0.2151346098, -0.0042778785), (0.2105263628, -0.0042778785))
                _nurbs_edge([(0.2105263628, -0.0042778785), (0.2113048517, -0.004716319), (0.2128834101, -0.0057141015), (0.2153159901, -0.0075734861), (0.2186892432, -0.010779926), (0.2231188042, -0.0159883553), (0.2277476017, -0.0223414815), (0.2325456734, -0.0297143581), (0.2374595844, -0.037879596), (0.2424086121, -0.0464933023), (0.2472967971, -0.0551689361), (0.2520224561, -0.0635368458), (0.2564888489, -0.0713117384), (0.2606138781, -0.0783519709), (0.2643419009, -0.0847387033), (0.267641578, -0.0907138616), (0.2705014407, -0.0965937305), (0.272926657, -0.1026915185), (0.27493567, -0.109238065), (0.2765572945, -0.1162982722), (0.2778266313, -0.1238129163), (0.2787811255, -0.1316454218), (0.2794567593, -0.1396257118), (0.2798843456, -0.1475944689), (0.2800858293, -0.1554475129), (0.2800756777, -0.1631241937), (0.279904999, -0.1691013128), (0.2796872902, -0.1734879646), (0.2795023883, -0.1763697599), (0.2793999966, -0.1777999979)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((0.2793999966, -0.1777999979), (0.277759975, -0.1973938579))
                _nurbs_edge([(0.277759975, -0.1973938579), (0.2772491875, -0.1988877404), (0.2761421609, -0.2021956339), (0.2742252782, -0.2081178336), (0.2711545457, -0.2179428913), (0.266975772, -0.2317142228), (0.2632890561, -0.2440456415), (0.2604950675, -0.2534399278), (0.2587885681, -0.2591834052), (0.2582361569, -0.2610427452)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378], 5)
                Line((0.3022600019, -0.2616200016), (0.2582361569, -0.2610427452))
                Line((0.3022600019, -0.2616200016), (0.2946400018, -0.2819400018))
                Line((0.2946400018, -0.2819400018), (0.2540000016, -0.2794000017))
                Line((0.2540000016, -0.2794000017), (0.2582361569, -0.2610427452))
                _nurbs_edge([(0.2582361569, -0.2610427452), (0.2576229438, -0.2631067359), (0.2558308475, -0.2691391042), (0.2528126131, -0.2792921109), (0.2485627512, -0.2935001846), (0.2432635626, -0.3106311871), (0.2376767508, -0.3265582772), (0.2319918943, -0.3383448076), (0.2251251781, -0.3457897796), (0.2154291916, -0.349527404), (0.2010938766, -0.3505987896), (0.1804623665, -0.3501411449), (0.1524072369, -0.3490187569), (0.1162327295, -0.3478561122), (0.0715673234, -0.347082509), (0.0182737009, -0.3469698234), (-0.0436348112, -0.3476699529), (-0.0999813088, -0.3489335752), (-0.1460319761, -0.3502836011), (-0.1784103562, -0.3513616931), (-0.195019031, -0.351945258)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.195019031, -0.351945258), (-0.1953841543, -0.350153593), (-0.1961138978, -0.3465126815), (-0.1972070074, -0.3408785702), (-0.1986614285, -0.3330184138), (-0.2004682598, -0.3225932672), (-0.2022452331, -0.3115346822), (-0.2039556664, -0.2997969028), (-0.2055359246, -0.2873245241), (-0.2068968052, -0.2740563714), (-0.2079382432, -0.2599301581), (-0.2085617623, -0.2448901428), (-0.2086830383, -0.2288948363), (-0.2082503814, -0.2119325776), (-0.2072463265, -0.1940206605), (-0.2056719694, -0.175187882), (-0.2039650991, -0.1594095765), (-0.20243865, -0.1471857845), (-0.2013123512, -0.1388644901), (-0.2007220347, -0.1346608173)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.2540119951, -0.1325872237), (-0.2007220347, -0.1346608173))
                Line((-0.2612481895, -0.1325872237), (-0.2540119951, -0.1325872237))
                Line((-0.4094645566, -0.1325872237), (-0.2612481895, -0.1325872237))
                Line((-0.4585379103, -0.1413402258), (-0.4094645566, -0.1325872237))
                Line((-0.467969192, -0.1439372454), (-0.4585379103, -0.1413402258))
                Line((-0.4874738496, -0.1493080932), (-0.467969192, -0.1439372454))
                Line((-0.5332084965, -0.1666616419), (-0.4874738496, -0.1493080932))
                Line((-0.6164247324, -0.1895762576), (-0.5332084965, -0.1666616419))
                Line((-0.6857999917, -0.2158999974), (-0.6164247324, -0.1895762576))
                Line((-0.7111999914, -0.2285999972), (-0.6857999917, -0.2158999974))
                Line((-0.7278849297, -0.2411711791), (-0.7111999914, -0.2285999972))
                Line((-0.7387602349, -0.2560051149), (-0.7278849297, -0.2411711791))
                Line((-0.7406775914, -0.2733201711), (-0.7387602349, -0.2560051149))
                Line((-0.5723509649, -0.2694825123), (-0.7406775914, -0.2733201711))
                Line((-0.5723509649, -0.2694825123), (-0.5810334049, -0.2920999965))
                Line((-0.5810334049, -0.2920999965), (-0.7425905334, -0.2905953607))
                Line((-0.7456776348, -0.3184740219), (-0.7425905334, -0.2905953607))
                Line((-0.739503432, -0.3227959638), (-0.7456776348, -0.3184740219))
                Line((-0.7380170377, -0.3608592177), (-0.739503432, -0.3227959638))
                Line((-0.7409898264, -0.3651060586), (-0.7380170377, -0.3608592177))
                Line((-0.757148386, -0.3726503116), (-0.7409898264, -0.3651060586))
                Line((-0.7578389792, -0.3812063602), (-0.757148386, -0.3726503116))
                Line((-0.7466062106, -0.3890692982), (-0.7578389792, -0.3812063602))
                Line((-0.6765886201, -0.3988043642), (-0.7466062106, -0.3890692982))
                Line((-0.5824831637, -0.4063999951), (-0.6765886201, -0.3988043642))
                Line((-0.5824831637, -0.3207108117), (-0.5824831637, -0.4063999951))
                Line((-0.5714999931, -0.2920999965), (-0.5824831637, -0.3207108117))
                Line((-0.560142253, -0.2625134394), (-0.5714999931, -0.2920999965))
                Line((-0.5283160754, -0.2351803693), (-0.560142253, -0.2625134394))
                Line((-0.4994853029, -0.2239476007), (-0.5283160754, -0.2351803693))
                Line((-0.472901084, -0.2179567908), (-0.4994853029, -0.2239476007))
                Line((-0.4717786118, -0.2179567908), (-0.472901084, -0.2179567908))
                CenterArc((-0.4465879508, -0.3300338749), 0.1148731569, 77.3326006811, 25.3347986378)
                Line((-0.4118697083, -0.2179567908), (-0.4213972899, -0.2179567908))
                Line((-0.3871576175, -0.2228243239), (-0.4118697083, -0.2179567908))
                Line((-0.3646920804, -0.2329338156), (-0.3871576175, -0.2228243239))
                Line((-0.3428999959, -0.2539999969), (-0.3646920804, -0.2329338156))
                Line((-0.3229225173, -0.2909956382), (-0.3428999959, -0.2539999969))
                Line((-0.3156423245, -0.3377729885), (-0.3229225173, -0.2909956382))
                Line((-0.3109228647, -0.3680968866), (-0.3156423245, -0.3377729885))
                Line((-0.3104003659, -0.3939368312), (-0.3109228647, -0.3680968866))
                Line((-0.1067128298, -0.3898181494), (-0.3104003659, -0.3939368312))
                Line((0.2156676272, -0.3898181494), (-0.1067128298, -0.3898181494))
                Line((0.2846062162, -0.3936999952), (0.2156676272, -0.3898181494))
                Line((0.2846062162, -0.3481938359), (0.2846062162, -0.3936999952))
                Line((0.2920999965, -0.3174999962), (0.2846062162, -0.3481938359))
                Line((0.3014110937, -0.2793625922), (0.2920999965, -0.3174999962))
                Line((0.313767139, -0.2561482039), (0.3014110937, -0.2793625922))
                Line((0.3336116968, -0.234431518), (0.313767139, -0.2561482039))
                Line((0.3590726388, -0.2179567908), (0.3336116968, -0.234431518))
                Line((0.3774194941, -0.208970576), (0.3590726388, -0.2179567908))
                Line((0.4036292873, -0.204103043), (0.3774194941, -0.208970576))
                Line((0.4365787417, -0.2022309149), (0.4036292873, -0.204103043))
                Line((0.4627885349, -0.2059751711), (0.4365787417, -0.2022309149))
                Line((0.4807609646, -0.2123404066), (0.4627885349, -0.2059751711))
                Line((0.5079999939, -0.2285999972), (0.4807609646, -0.2123404066))
                Line((0.5384850383, -0.2622502196), (0.5079999939, -0.2285999972))
                Line((0.5475392186, -0.2896070757), (0.5384850383, -0.2622502196))
                Line((0.5584400431, -0.3428999959), (0.5475392186, -0.2896070757))
                Line((0.5584400431, -0.3832025948), (0.5584400431, -0.3428999959))
                Line((0.5870978401, -0.3737178479), (0.5584400431, -0.3832025948))
                Line((0.6632283883, -0.34852125), (0.5870978401, -0.3737178479))
                Line((0.677334414, -0.3456359265), (0.6632283883, -0.34852125))
                Line((0.7267585955, -0.3355264348), (0.677334414, -0.3456359265))
                Line((0.7379496568, -0.3149572417), (0.7267585955, -0.3355264348))
                Line((0.7270953651, -0.2999282225), (0.7379496568, -0.3149572417))
                Line((0.7379496568, -0.2920890119), (0.7270953651, -0.2999282225))
                Line((0.7379496568, -0.2793999966), (0.7379496568, -0.2920890119))
                Line((0.7379496568, -0.2727924934), (0.7379496568, -0.2793999966))
                Line((0.5613400035, -0.2743200017), (0.7379496568, -0.2727924934))
                Line((0.5562600035, -0.2544621321), (0.5613400035, -0.2743200017))
                Line((0.7379496568, -0.2544621321), (0.5562600035, -0.2544621321))
                Line((0.7379496568, -0.2456567643), (0.7379496568, -0.2544621321))
                Line((0.7029324818, -0.2323904079), (0.7379496568, -0.2456567643))
                Line((0.6705600042, -0.2336800015), (0.7029324818, -0.2323904079))
                Line((0.6731000042, -0.1803400011), (0.6705600042, -0.2336800015))
                Line((0.7029324818, -0.1652289157), (0.6731000042, -0.1803400011))
                Line((0.7009888555, -0.1633098621), (0.7029324818, -0.1652289157))
            make_face()
            with BuildLine():
                Line((-0.3168488665, -0.2689662558), (-0.2111507911, -0.2668825287))
                Line((-0.2111507911, -0.2668825287), (-0.210824321, -0.2830279594))
                Line((-0.210824321, -0.2830279594), (-0.3083060103, -0.2849990965))
                Line((-0.3083060103, -0.2849990965), (-0.3168488665, -0.2689662558))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.6857999917, -0.3555999957), 0.0359210241, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0276605256, perimeter: 0.5895696872
            with Locations((0.4254017094, -0.3176057162)):
                Circle(0.09383293)
            # Profile area: 0.0007499931, perimeter: 0.532215698
            with BuildLine():
                Line((-0.2007220347, -0.1346608173), (0.0352262351, -0.0118690107))
                Line((0.0188436074, -0.0194601428), (0.0352262351, -0.0118690107))
                Line((-0.0761999991, -0.0634999992), (0.0188436074, -0.0194601428))
                Line((-0.2007220347, -0.1346608173), (-0.0761999991, -0.0634999992))
            make_face()
            # Profile area: 0.1017363048, perimeter: 3.3465406948
            with BuildLine():
                Line((0.2105263628, -0.0042778785), (0.0516088628, -0.0042778785))
                Line((0.0352262351, -0.0118690107), (0.0516088628, -0.0042778785))
                Line((-0.2007220347, -0.1346608173), (0.0352262351, -0.0118690107))
                _nurbs_edge([(-0.195019031, -0.351945258), (-0.1953841543, -0.350153593), (-0.1961138978, -0.3465126815), (-0.1972070074, -0.3408785702), (-0.1986614285, -0.3330184138), (-0.2004682598, -0.3225932672), (-0.2022452331, -0.3115346822), (-0.2039556664, -0.2997969028), (-0.2055359246, -0.2873245241), (-0.2068968052, -0.2740563714), (-0.2079382432, -0.2599301581), (-0.2085617623, -0.2448901428), (-0.2086830383, -0.2288948363), (-0.2082503814, -0.2119325776), (-0.2072463265, -0.1940206605), (-0.2056719694, -0.175187882), (-0.2039650991, -0.1594095765), (-0.20243865, -0.1471857845), (-0.2013123512, -0.1388644901), (-0.2007220347, -0.1346608173)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.2582361569, -0.2610427452), (0.2576229438, -0.2631067359), (0.2558308475, -0.2691391042), (0.2528126131, -0.2792921109), (0.2485627512, -0.2935001846), (0.2432635626, -0.3106311871), (0.2376767508, -0.3265582772), (0.2319918943, -0.3383448076), (0.2251251781, -0.3457897796), (0.2154291916, -0.349527404), (0.2010938766, -0.3505987896), (0.1804623665, -0.3501411449), (0.1524072369, -0.3490187569), (0.1162327295, -0.3478561122), (0.0715673234, -0.347082509), (0.0182737009, -0.3469698234), (-0.0436348112, -0.3476699529), (-0.0999813088, -0.3489335752), (-0.1460319761, -0.3502836011), (-0.1784103562, -0.3513616931), (-0.195019031, -0.351945258)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.277759975, -0.1973938579), (0.2772491875, -0.1988877404), (0.2761421609, -0.2021956339), (0.2742252782, -0.2081178336), (0.2711545457, -0.2179428913), (0.266975772, -0.2317142228), (0.2632890561, -0.2440456415), (0.2604950675, -0.2534399278), (0.2587885681, -0.2591834052), (0.2582361569, -0.2610427452)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378, 0.2236959378], 5)
                Line((0.2793999966, -0.1777999979), (0.277759975, -0.1973938579))
                _nurbs_edge([(0.2105263628, -0.0042778785), (0.2113048517, -0.004716319), (0.2128834101, -0.0057141015), (0.2153159901, -0.0075734861), (0.2186892432, -0.010779926), (0.2231188042, -0.0159883553), (0.2277476017, -0.0223414815), (0.2325456734, -0.0297143581), (0.2374595844, -0.037879596), (0.2424086121, -0.0464933023), (0.2472967971, -0.0551689361), (0.2520224561, -0.0635368458), (0.2564888489, -0.0713117384), (0.2606138781, -0.0783519709), (0.2643419009, -0.0847387033), (0.267641578, -0.0907138616), (0.2705014407, -0.0965937305), (0.272926657, -0.1026915185), (0.27493567, -0.109238065), (0.2765572945, -0.1162982722), (0.2778266313, -0.1238129163), (0.2787811255, -0.1316454218), (0.2794567593, -0.1396257118), (0.2798843456, -0.1475944689), (0.2800858293, -0.1554475129), (0.2800756777, -0.1631241937), (0.279904999, -0.1691013128), (0.2796872902, -0.1734879646), (0.2795023883, -0.1763697599), (0.2793999966, -0.1777999979)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                Line((0.1225480482, -0.2610427452), (0.2523575763, -0.2613313734))
                Line((0.2523575763, -0.2613313734), (0.2484353738, -0.2783281243))
                Line((0.2484353738, -0.2783281243), (0.1252641373, -0.2780542562))
                Line((0.1252641373, -0.2780542562), (-0.0205142852, -0.2817165263))
                Line((-0.0205142852, -0.2817165263), (-0.200582467, -0.2849636409))
                Line((-0.2012961411, -0.2668825287), (-0.200582467, -0.2849636409))
                Line((-0.2012961411, -0.2668825287), (0.1225480482, -0.2610427452))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.1941593366, -0.0192146721), (0.2008170797, -0.0223255929))
                Line((0.2008170797, -0.0223255929), (0.2132246192, -0.0335367159))
                Line((0.2132246192, -0.0335367159), (0.2393151042, -0.087694622))
                Line((0.2393151042, -0.087694622), (0.2393151042, -0.1311700077))
                Line((0.2393151042, -0.1311700077), (-0.0888999989, -0.1396999983))
                Line((-0.0888999989, -0.1396999983), (-0.089010842, -0.135435003))
                Line((-0.089010842, -0.135435003), (-0.093167835, -0.1094323149))
                Line((-0.093167835, -0.1094323149), (-0.089010842, -0.0926719832))
                Line((-0.089010842, -0.0926719832), (0.0475249456, -0.023025557))
                Line((0.0475249456, -0.023025557), (0.1941593366, -0.0192146721))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.2358692368, -0.1754353835), (0.2358692368, -0.157480001))
                Line((0.2260600014, -0.1803400011), (0.2358692368, -0.1754353835))
                Line((0.1854200012, -0.1803400011), (0.2260600014, -0.1803400011))
                Line((0.1803400011, -0.1727200011), (0.1854200012, -0.1803400011))
                Line((0.1803400011, -0.157480001), (0.1803400011, -0.1727200011))
                Line((0.1905000012, -0.152400001), (0.1803400011, -0.157480001))
                Line((0.2184400014, -0.152400001), (0.1905000012, -0.152400001))
                Line((0.2358692368, -0.157480001), (0.2184400014, -0.152400001))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0079548484, perimeter: 0.9383387226
            with BuildLine():
                Line((-0.2012961411, -0.2668825287), (0.1225480482, -0.2610427452))
                Line((-0.2012961411, -0.2668825287), (-0.200582467, -0.2849636409))
                Line((-0.0205142852, -0.2817165263), (-0.200582467, -0.2849636409))
                Line((0.1252641373, -0.2780542562), (-0.0205142852, -0.2817165263))
                Line((0.2484353738, -0.2783281243), (0.1252641373, -0.2780542562))
                Line((0.2523575763, -0.2613313734), (0.2484353738, -0.2783281243))
                Line((0.1225480482, -0.2610427452), (0.2523575763, -0.2613313734))
            make_face()
            # Profile area: 0.0314942508, perimeter: 0.8038116498
            with BuildLine():
                Line((0.0475249456, -0.023025557), (0.1941593366, -0.0192146721))
                Line((-0.089010842, -0.0926719832), (0.0475249456, -0.023025557))
                Line((-0.093167835, -0.1094323149), (-0.089010842, -0.0926719832))
                Line((-0.089010842, -0.135435003), (-0.093167835, -0.1094323149))
                Line((-0.0888999989, -0.1396999983), (-0.089010842, -0.135435003))
                Line((0.2393151042, -0.1311700077), (-0.0888999989, -0.1396999983))
                Line((0.2393151042, -0.087694622), (0.2393151042, -0.1311700077))
                Line((0.2132246192, -0.0335367159), (0.2393151042, -0.087694622))
                Line((0.2008170797, -0.0223255929), (0.2132246192, -0.0335367159))
                Line((0.1941593366, -0.0192146721), (0.2008170797, -0.0223255929))
            make_face()
            # Profile area: 0.0014380001, perimeter: 0.1514142335
            with BuildLine():
                Line((0.2358692368, -0.157480001), (0.2184400014, -0.152400001))
                Line((0.2184400014, -0.152400001), (0.1905000012, -0.152400001))
                Line((0.1905000012, -0.152400001), (0.1803400011, -0.157480001))
                Line((0.1803400011, -0.157480001), (0.1803400011, -0.1727200011))
                Line((0.1803400011, -0.1727200011), (0.1854200012, -0.1803400011))
                Line((0.1854200012, -0.1803400011), (0.2260600014, -0.1803400011))
                Line((0.2260600014, -0.1803400011), (0.2358692368, -0.1754353835))
                Line((0.2358692368, -0.1754353835), (0.2358692368, -0.157480001))
            make_face()
            # Profile area: 0.027966416, perimeter: 0.5928206716
            with Locations((-0.4465879508, -0.3300338749)):
                Circle(0.0943503403)
            # Profile area: 0.0016434844, perimeter: 0.2375357528
            with BuildLine():
                Line((-0.3083060103, -0.2849990965), (-0.3168488665, -0.2689662558))
                Line((-0.210824321, -0.2830279594), (-0.3083060103, -0.2849990965))
                Line((-0.2111507911, -0.2668825287), (-0.210824321, -0.2830279594))
                Line((-0.3168488665, -0.2689662558), (-0.2111507911, -0.2668825287))
            make_face()
            # Profile area: 0.0040536597, perimeter: 0.2256984505
            with Locations((-0.6857999917, -0.3555999957)):
                Circle(0.0359210241)
            # Profile area: 0.000827881, perimeter: 0.1252883859
            with BuildLine():
                Line((0.2540000016, -0.2794000017), (0.2582361569, -0.2610427452))
                Line((0.2946400018, -0.2819400018), (0.2540000016, -0.2794000017))
                Line((0.3022600019, -0.2616200016), (0.2946400018, -0.2819400018))
                Line((0.3022600019, -0.2616200016), (0.2582361569, -0.2610427452))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314942508, perimeter: 0.8038116498
            with BuildLine():
                Line((0.0475249456, -0.023025557), (0.1941593366, -0.0192146721))
                Line((-0.089010842, -0.0926719832), (0.0475249456, -0.023025557))
                Line((-0.093167835, -0.1094323149), (-0.089010842, -0.0926719832))
                Line((-0.089010842, -0.135435003), (-0.093167835, -0.1094323149))
                Line((-0.0888999989, -0.1396999983), (-0.089010842, -0.135435003))
                Line((0.2393151042, -0.1311700077), (-0.0888999989, -0.1396999983))
                Line((0.2393151042, -0.087694622), (0.2393151042, -0.1311700077))
                Line((0.2132246192, -0.0335367159), (0.2393151042, -0.087694622))
                Line((0.2008170797, -0.0223255929), (0.2132246192, -0.0335367159))
                Line((0.1941593366, -0.0192146721), (0.2008170797, -0.0223255929))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0034226441, perimeter: 0.3971336242
            with BuildLine():
                Line((0.7379496568, -0.2544621321), (0.7379496568, -0.2727924934))
                Line((0.7379496568, -0.2544621321), (0.5562600035, -0.2544621321))
                Line((0.5562600035, -0.2544621321), (0.5613400035, -0.2743200017))
                Line((0.5613400035, -0.2743200017), (0.7379496568, -0.2727924934))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0034226441, perimeter: 0.3971336242
            with BuildLine():
                Line((0.7379496568, -0.2544621321), (0.7379496568, -0.2727924934))
                Line((0.7379496568, -0.2544621321), (0.5562600035, -0.2544621321))
                Line((0.5562600035, -0.2544621321), (0.5613400035, -0.2743200017))
                Line((0.5613400035, -0.2743200017), (0.7379496568, -0.2727924934))
            make_face()
            # Profile area: 0.0019288015, perimeter: 0.1872426777
            with BuildLine():
                Line((0.704876108, -0.1671479692), (0.7029324818, -0.2323904079))
                Line((0.7029324818, -0.1652289157), (0.704876108, -0.1671479692))
                Line((0.7029324818, -0.1652289157), (0.6731000042, -0.1803400011))
                Line((0.6731000042, -0.1803400011), (0.6705600042, -0.2336800015))
                Line((0.6705600042, -0.2336800015), (0.7029324818, -0.2323904079))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0127780431, perimeter: 0.6818787023
            with BuildLine():
                _nurbs_edge([(0.5261928237, -0.1242869397), (0.5262513145, -0.1240920418), (0.526581328, -0.1233433465), (0.5273272979, -0.1225235528), (0.528489586, -0.1216326651), (0.5300670685, -0.1206708764), (0.5314462429, -0.1199278863)], [1, 1, 1, 1, 1, 1, 1], [0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.9317789281, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0.6058847822, -0.1005455238), (0.5314462429, -0.1199278863))
                Line((0.5896076711, -0.0961087463), (0.6058847822, -0.1005455238))
                Line((0.330199996, -0.0253999997), (0.5896076711, -0.0961087463))
                Line((0.2944288952, -0.0132714189), (0.330199996, -0.0253999997))
                Line((0.2944288952, -0.0132714189), (0.4017420183, -0.110236705))
                Line((0.4017420183, -0.110236705), (0.4172916507, -0.1242869397))
                Line((0.4172916507, -0.1242869397), (0.5261928237, -0.1242869397))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0014380001, perimeter: 0.1514142335
            with BuildLine():
                Line((0.2358692368, -0.157480001), (0.2184400014, -0.152400001))
                Line((0.2184400014, -0.152400001), (0.1905000012, -0.152400001))
                Line((0.1905000012, -0.152400001), (0.1803400011, -0.157480001))
                Line((0.1803400011, -0.157480001), (0.1803400011, -0.1727200011))
                Line((0.1803400011, -0.1727200011), (0.1854200012, -0.1803400011))
                Line((0.1854200012, -0.1803400011), (0.2260600014, -0.1803400011))
                Line((0.2260600014, -0.1803400011), (0.2358692368, -0.1754353835))
                Line((0.2358692368, -0.1754353835), (0.2358692368, -0.157480001))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude7 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.000827881, perimeter: 0.1252883859
            with BuildLine():
                Line((0.2540000016, -0.2794000017), (0.2582361569, -0.2610427452))
                Line((0.2946400018, -0.2819400018), (0.2540000016, -0.2794000017))
                Line((0.3022600019, -0.2616200016), (0.2946400018, -0.2819400018))
                Line((0.3022600019, -0.2616200016), (0.2582361569, -0.2610427452))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude8 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0079548484, perimeter: 0.9383387226
            with BuildLine():
                Line((-0.2012961411, -0.2668825287), (0.1225480482, -0.2610427452))
                Line((-0.2012961411, -0.2668825287), (-0.200582467, -0.2849636409))
                Line((-0.0205142852, -0.2817165263), (-0.200582467, -0.2849636409))
                Line((0.1252641373, -0.2780542562), (-0.0205142852, -0.2817165263))
                Line((0.2484353738, -0.2783281243), (0.1252641373, -0.2780542562))
                Line((0.2523575763, -0.2613313734), (0.2484353738, -0.2783281243))
                Line((0.1225480482, -0.2610427452), (0.2523575763, -0.2613313734))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude9 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0016434844, perimeter: 0.2375357528
            with BuildLine():
                Line((-0.3083060103, -0.2849990965), (-0.3168488665, -0.2689662558))
                Line((-0.210824321, -0.2830279594), (-0.3083060103, -0.2849990965))
                Line((-0.2111507911, -0.2668825287), (-0.210824321, -0.2830279594))
                Line((-0.3168488665, -0.2689662558), (-0.2111507911, -0.2668825287))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude10 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0032838064, perimeter: 0.371542032
            with BuildLine():
                Line((-0.7412378986, -0.2783801322), (-0.7406775914, -0.2733201711))
                Line((-0.7425905334, -0.2905953607), (-0.7412378986, -0.2783801322))
                Line((-0.5810334049, -0.2920999965), (-0.7425905334, -0.2905953607))
                Line((-0.5723509649, -0.2694825123), (-0.5810334049, -0.2920999965))
                Line((-0.5723509649, -0.2694825123), (-0.7406775914, -0.2733201711))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude11 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314942508, perimeter: 0.8038116498
            with BuildLine():
                Line((0.0475249456, -0.023025557), (0.1941593366, -0.0192146721))
                Line((-0.089010842, -0.0926719832), (0.0475249456, -0.023025557))
                Line((-0.093167835, -0.1094323149), (-0.089010842, -0.0926719832))
                Line((-0.089010842, -0.135435003), (-0.093167835, -0.1094323149))
                Line((-0.0888999989, -0.1396999983), (-0.089010842, -0.135435003))
                Line((0.2393151042, -0.1311700077), (-0.0888999989, -0.1396999983))
                Line((0.2393151042, -0.087694622), (0.2393151042, -0.1311700077))
                Line((0.2132246192, -0.0335367159), (0.2393151042, -0.087694622))
                Line((0.2008170797, -0.0223255929), (0.2132246192, -0.0335367159))
                Line((0.1941593366, -0.0192146721), (0.2008170797, -0.0223255929))
            make_face()
        # OneSide extrude, distance=0.3048
        extrude(amount=0.3048, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude12 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0040536597, perimeter: 0.2256984505
            with Locations((-0.6857999917, -0.3555999957)):
                Circle(0.0359210241)
        # OneSide extrude, distance=0.2794
        extrude(amount=0.2794, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude13 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0044828492, perimeter: 0.3053995215
            with BuildLine():
                Line((-0.7387602349, -0.2560051149), (-0.651112362, -0.2027381275))
                Line((-0.651112362, -0.2027381275), (-0.7365999911, -0.1523999982))
                Line((-0.7365999911, -0.1523999982), (-0.7387602349, -0.2560051149))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude14 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0052712188, perimeter: 0.3342300806
            with BuildLine():
                Line((-0.7406775914, -0.2733201711), (-0.651112362, -0.2027381275))
                Line((-0.651112362, -0.2027381275), (-0.7365999911, -0.1523999982))
                Line((-0.7365999911, -0.1523999982), (-0.7406775914, -0.2733201711))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude15 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0276605256, perimeter: 0.5895696872
            with Locations((0.4254017094, -0.3176057162)):
                Circle(0.09383293)
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude16 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 64 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.027966416, perimeter: 0.5928206716
            with Locations((-0.4465879508, -0.3300338749)):
                Circle(0.0943503403)
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stepped pyramidal or wedge-shaped mechanical part featuring a series of horizontal rectangular slots or steps that progressively decrease in size from bottom to top, creating a tiered, fan-like profile when viewed from the side.
def model_132447_7c00b7da_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3125, perimeter: 300
            with BuildLine():
                Line((0, 25), (0, 0))
                Line((0, 0), (125, 0))
                Line((125, 0), (125, 25))
                Line((125, 25), (0, 25))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1250, perimeter: 150
            with BuildLine():
                Line((0, 50), (0, 0))
                Line((0, 0), (25, 0))
                Line((25, 0), (25, 50))
                Line((25, 50), (0, 50))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1875, perimeter: 200
            with BuildLine():
                Line((25, 75), (25, 0))
                Line((25, 0), (50, 0))
                Line((50, 0), (50, 75))
                Line((50, 75), (25, 75))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2500, perimeter: 250
            with BuildLine():
                Line((50, 100), (50, 0))
                Line((50, 0), (75, 0))
                Line((75, 0), (75, 100))
                Line((75, 100), (50, 100))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3125, perimeter: 300
            with BuildLine():
                Line((100, 125), (100, 0))
                Line((100, 125), (75, 125))
                Line((75, 125), (75, 0))
                Line((75, 0), (100, 0))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3750, perimeter: 350
            with BuildLine():
                Line((100, 150), (100, 125))
                Line((100, 125), (100, 0))
                Line((100, 0), (125, 0))
                Line((125, 0), (125, 150))
                Line((125, 150), (100, 150))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4375, perimeter: 400
            with BuildLine():
                Line((125, 175), (125, 0))
                Line((125, 0), (150, 0))
                Line((150, 0), (150, 175))
                Line((150, 175), (125, 175))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5000, perimeter: 450
            with BuildLine():
                Line((150, 200), (150, 175))
                Line((150, 175), (150, 0))
                Line((150, 0), (175, 0))
                Line((175, 0), (175, 200))
                Line((175, 200), (150, 200))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5625, perimeter: 500
            with BuildLine():
                Line((175, 225), (175, 200))
                Line((175, 200), (175, 0))
                Line((175, 0), (200, 0))
                Line((200, 0), (200, 225))
                Line((200, 225), (175, 225))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25000, perimeter: 700
            with BuildLine():
                Line((200, 250), (200, 0))
                Line((200, 0), (300, 0))
                Line((300, 0), (300, 250))
                Line((300, 250), (200, 250))
            make_face()
        # OneSide extrude, distance=125
        extrude(amount=125, mode=Mode.ADD)
    return part.part


# Description: A modular solar panel array assembly consisting of five rectangular photovoltaic panels with textured surfaces arranged in a clustered configuration, accompanied by a separate black mounting bracket or connector component.
def model_134072_a64e5fc0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 88.8, perimeter: 38.8
            with BuildLine():
                Line((-5, -2.4), (-17, -2.4))
                Line((-5, 5), (-5, -2.4))
                Line((-17, 5), (-5, 5))
                Line((-17, -2.4), (-17, 5))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-15.5, 1.3)):
                Circle(0.75)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-6.5, 1.3)):
                Circle(0.8)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-8.7, -1.5)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-13.3, -1.5)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-13.3, 4.1)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-8.7, 4.1)):
                Circle(0.35)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7461282552, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((-13.3, 4.1), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.3, 4.1), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7461282552, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((-8.7, 4.1), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.7, 4.1), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7461282552, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((-8.7, -1.5), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.7, -1.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7461282552, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((-13.3, -1.5), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.3, -1.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.85
        extrude(amount=-0.85, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 88.8, perimeter: 38.8
            with BuildLine():
                Line((10, -2.4), (-2, -2.4))
                Line((10, 5), (10, -2.4))
                Line((-2, 5), (10, 5))
                Line((-2, -2.4), (-2, 5))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-0.5, 1.3)):
                Circle(0.75)
            # Profile area: 0.1320254313, perimeter: 1.288052988
            with Locations((-0.5, 2.75)):
                Circle(0.205)
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((1.7, 4.1)):
                Circle(0.255)
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((6.3, 4.1)):
                Circle(0.255)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((8.5, 1.3)):
                Circle(0.8)
            # Profile area: 0.1320254313, perimeter: 1.288052988
            with Locations((8.5, 2.75)):
                Circle(0.205)
            # Profile area: 0.1320254313, perimeter: 1.288052988
            with Locations((8.5, -0.15)):
                Circle(0.205)
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((6.3, -1.3220876572)):
                Circle(0.255)
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((1.7, -1.2367729062)):
                Circle(0.255)
            # Profile area: 0.1320254313, perimeter: 1.288052988
            with Locations((-0.5, -0.15)):
                Circle(0.205)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 45.88, perimeter: 27.2
            with BuildLine():
                Line((-5, -11.4), (-11.2, -11.4))
                Line((-5, -4), (-5, -11.4))
                Line((-11.2, -4), (-5, -4))
                Line((-11.2, -11.4), (-11.2, -4))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((-10.4, -4.9)):
                Circle(0.255)
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((-5.8, -4.9)):
                Circle(0.255)
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((-5.8, -10.5)):
                Circle(0.255)
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((-10.4, -10.5)):
                Circle(0.255)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 45.88, perimeter: 27.2
            with BuildLine():
                Line((4, -11.4), (-2.2, -11.4))
                Line((4, -4), (4, -11.4))
                Line((-2.2, -4), (4, -4))
                Line((-2.2, -11.4), (-2.2, -4))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((-1.4, -10.5)):
                Circle(0.325)
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((3.2, -4.9)):
                Circle(0.325)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.4, -10.5)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((3.2, -4.9)):
                Circle(0.6)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch15 -> Extrude11 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((7, 4)):
                Circle(0.75)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch16 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.3876104167, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((7, 4), 1.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7, 4), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((7, 4)):
                Circle(0.75)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch17 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((7, 4)):
                Circle(0.75)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch18 -> Extrude14 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, 4)):
                Circle(0.8)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch19 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.1441369861, perimeter: 12.252211349
            with BuildLine():
                CenterArc((10, 4), 1.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((10, 4), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, 4)):
                Circle(0.8)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch20 -> Extrude16 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, 4)):
                Circle(0.8)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch21 -> Extrude17 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 45.88, perimeter: 27.2
            with BuildLine():
                Line((17, -11.4), (10.8, -11.4))
                Line((17, -4), (17, -11.4))
                Line((10.8, -4), (17, -4))
                Line((10.8, -11.4), (10.8, -4))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2)

        # Sketch22 -> Extrude18 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((11.6, -4.9)):
                Circle(0.325)
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((16.2, -4.9)):
                Circle(0.325)
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((16.2, -10.5)):
                Circle(0.325)
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((11.6, -10.5)):
                Circle(0.325)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch23 -> Extrude19 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((11.6, -4.9)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((16.2, -10.5)):
                Circle(0.6)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or mounting component with a roughly trapezoidal/wedge-shaped body featuring a flat mounting base, angled support arm, and a rectangular slot or opening on the upper section for attachment or assembly purposes.
def model_134579_efc1d669_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.2554993749, perimeter: 26.2330253846
            with BuildLine():
                Line((6, 3.5), (6, 0))
                CenterArc((1.125, 3.5), 4.875, 0, 67.380135052)
                Line((0, 8), (3, 8))
                Line((0, 0), (0, 8))
                Line((6, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> 拉伸2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 11.9600003564, perimeter: 14.4000002146
            with BuildLine():
                Line((3.2000000477, 4.8000000715), (3.2000000477, 0.200000003))
                Line((3.2000000477, 0.200000003), (5.8000000864, 0.200000003))
                Line((5.8000000864, 0.200000003), (5.8000000864, 4.8000000715))
                Line((5.8000000864, 4.8000000715), (3.2000000477, 4.8000000715))
            make_face()
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.SUBTRACT)

        # Sketch3 -> 拉伸3 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.2000000477, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3000000685, perimeter: 10.200000152
            with BuildLine():
                Line((-4.8000000715, 0), (-0.200000003, 0))
                Line((-0.200000003, 0.5000000075), (-0.200000003, 0))
                Line((-0.200000003, 0.5000000075), (-4.8000000715, 0.5000000075))
                Line((-4.8000000715, 0), (-4.8000000715, 0.5000000075))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6, mode=Mode.ADD)

        # Sketch4 -> 拉伸4 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8000000238, perimeter: 4.2000000626
            with BuildLine():
                Line((-0.7000000104, 3.5000000522), (-0.7000000104, 4.0000000596))
                Line((-0.7000000104, 4.0000000596), (-2.3000000343, 4.0000000596))
                Line((-2.3000000343, 4.0000000596), (-2.3000000343, 3.7500000559))
                Line((-2.3000000343, 3.5000000522), (-2.3000000343, 3.7500000559))
                Line((-0.7000000104, 3.5000000522), (-2.3000000343, 3.5000000522))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> 拉伸5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 10.000000054, perimeter: 13.0000000522
            with BuildLine():
                Line((0.5, 3), (0.5, 0.5000000075))
                Line((0.5, 0.5000000075), (4.5000000671, 0.5000000075))
                Line((4.5000000671, 0.5000000075), (4.5, 3))
                Line((0.5, 3), (4.5, 3))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch6 -> 拉伸6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6600001389, perimeter: 13.6000002027
            with BuildLine():
                Line((-2.8000000417, 2.7000000402), (-2.8000000417, 4.8000000715))
                Line((-2.8000000417, 2.7000000402), (-0.200000003, 2.7000000402))
                Line((-0.200000003, 4.8000000715), (-0.200000003, 2.7000000402))
                Line((-2.8000000417, 4.8000000715), (-0.200000003, 4.8000000715))
            make_face()
            with BuildLine():
                Line((-2.3000000343, 3.5000000522), (-2.3000000343, 4.0000000596))
                Line((-2.3000000343, 4.0000000596), (-0.7000000104, 4.0000000596))
                Line((-0.7000000104, 4.0000000596), (-0.7000000104, 3.5000000522))
                Line((-0.7000000104, 3.5000000522), (-2.3000000343, 3.5000000522))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch7 -> 拉伸7 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.7000000402), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7799997133, perimeter: 5.799999848
            with BuildLine():
                Line((2.8000000417, 7.7000001147), (0.200000003, 7.7000001147))
                Line((2.8000000417, 7.7000001147), (2.8000000417, 8))
                Line((0.200000003, 8), (2.8000000417, 8))
                Line((0.200000003, 8), (0.200000003, 7.7000001147))
            make_face()
        # OneSide extrude, distance=2.1
        extrude(amount=2.1, mode=Mode.ADD)

        # Sketch8 -> 拉伸8 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8000000238, perimeter: 4.2000000626
            with BuildLine():
                Line((-2.3000000343, 3.5000000522), (-0.7000000104, 3.5000000522))
                Line((-0.7000000104, 3.5000000522), (-0.7000000104, 4.0000000596))
                Line((-0.7000000104, 4.0000000596), (-2.3000000343, 4.0000000596))
                Line((-2.3000000343, 4.0000000596), (-2.3000000343, 3.7500000559))
                Line((-2.3000000343, 3.7500000559), (-2.3000000343, 3.5000000522))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch9 -> 拉伸9 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6600000575, perimeter: 13.6000001401
            with BuildLine():
                Line((-2.8000000417, 4.8000000402), (-2.8000000417, 2.7000000402))
                Line((-2.8000000417, 2.7000000402), (-0.200000003, 2.7000000402))
                Line((-0.200000003, 4.8000000402), (-0.200000003, 2.7000000402))
                Line((-0.200000003, 4.8000000402), (-2.8000000417, 4.8000000402))
            make_face()
            with BuildLine():
                Line((-2.3000000343, 4.0000000596), (-0.7000000104, 4.0000000596))
                Line((-0.7000000104, 4.0000000596), (-0.7000000104, 3.5000000522))
                Line((-0.7000000104, 3.5000000522), (-2.3000000343, 3.5000000522))
                Line((-2.3000000343, 3.5000000522), (-2.3000000343, 4.0000000596))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch10 -> 拉伸10 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9800001782, perimeter: 9.800000146
            with BuildLine():
                Line((-0.200000003, 0.5), (-0.200000003, 0.200000003))
                Line((-0.200000003, 2.5000000373), (-0.200000003, 0.5))
                Line((-2.8000000417, 2.5000000373), (-0.200000003, 2.5000000373))
                Line((-2.8000000417, 0.200000003), (-2.8000000417, 2.5000000373))
                Line((-0.200000003, 0.200000003), (-2.8000000417, 0.200000003))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch11 -> 拉伸11 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0536504607, perimeter: 1.78539819
            with BuildLine():
                Line((0, 0.5000000075), (0, 1.0000000149))
                Line((0.200000003, 0.5000000075), (0, 0.5000000075))
                Line((0.200000003, 0.5000000075), (0.5000000075, 0.5000000075))
                CenterArc((0.5000000075, 1.0000000149), 0.5000000075, 180, 90)
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.ADD)

        # Sketch12 -> 拉伸12 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.0000000596, perimeter: 17.0000000149
            with BuildLine():
                Line((0.2500000037, 0), (8.2500000037, 0))
                Line((8.2500000037, 0), (8.2500000037, 0.5000000075))
                Line((8.2500000037, 0.5000000075), (0.5000000075, 0.5000000075))
                Line((0.5000000075, 0.5000000075), (0.2500000037, 0.5000000075))
                Line((0.2500000037, 0), (0.2500000037, 0.5000000075))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


# Description: This is a complex polyhedral geometric solid featuring multiple faceted surfaces with angular protrusions and recessed pyramidal elements, characterized by an irregular, fragmented crystalline-like structure with both convex and concave geometric features.
def model_134924_4c5e911a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 300, perimeter: 80
            with BuildLine():
                Line((15, -5), (-15, -5))
                Line((15, 5), (15, -5))
                Line((-15, 5), (15, 5))
                Line((-15, -5), (-15, 5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 88.5599750682, perimeter: 40.7544401656
            with BuildLine():
                Line((-2.3728952903, -5), (10.6695498617, -5))
                Line((-2.3728952903, -5), (6, -15))
                Line((6, -15), (13.6672739532, -8.5802718028))
                Line((13.6672739532, -8.5802718028), (10.6695498617, -5))
            make_face()
            # Profile area: 130.4244515196, perimeter: 52.1697806079
            with BuildLine():
                Line((-10.7457905806, 5), (-2.3728952903, -5))
                Line((-2.3728952903, -5), (10.6695498617, -5))
                Line((10.6695498617, -5), (2.2966545714, 5))
                Line((2.2966545714, 5), (-10.7457905806, 5))
            make_face()
            # Profile area: 81.0155734121, perimeter: 39.2455598344
            with BuildLine():
                Line((2.2966545714, 5), (-10.7457905806, 5))
                Line((2.2966545714, 5), (-5.5919106384, 14.4215500569))
                Line((-5.5919106384, 14.4215500569), (-13.2591845917, 8.0018218597))
                Line((-13.2591845917, 8.0018218597), (-10.7457905806, 5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 18, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 80.1645894599, perimeter: 37.1682835024
            with BuildLine():
                Line((4.9336049288, 1.8506110898), (-2.2149971308, 10.3884009602))
                Line((9.1841539816, 11.4143464586), (4.9336049288, 1.8506110898))
                Line((0.0460384954, 15.4757311191), (9.1841539816, 11.4143464586))
                Line((-2.2149971308, 10.3884009602), (0.0460384954, 15.4757311191))
            make_face()
            # Profile area: 108.4817544357, perimeter: 42.8317164976
            with BuildLine():
                Line((-12.1381154862, -11.9386153395), (-6.7374974388, 0.2127752673))
                Line((-3, -16), (-12.1381154862, -11.9386153395))
                Line((0.4111046208, -8.3250146032), (-3, -16))
                Line((-6.7374974388, 0.2127752673), (0.4111046208, -8.3250146032))
            make_face()
            # Profile area: 111.3536561044, perimeter: 44.5414624418
            with BuildLine():
                Line((-6.7374974388, 0.2127752673), (-2.2149971308, 10.3884009602))
                Line((-6.7374974388, 0.2127752673), (0.4111046208, -8.3250146032))
                Line((4.9336049288, 1.8506110898), (0.4111046208, -8.3250146032))
                Line((4.9336049288, 1.8506110898), (-2.2149971308, 10.3884009602))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)
    return part.part


# Description: This is a drill bit or twist drill, characterized by a long, cylindrical shaft with a helical flute pattern and a pointed conical tip for boring holes into materials.
def model_138125_431e6a10_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((2.5, 2.5)):
                Circle(0.75)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2.5, 2.5), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2.5, 2.5), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch7 -> Extrude7 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2.5, 2.5), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch8 -> Extrude8 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch9 -> Extrude9 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2.5, 2.5), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch10 -> Extrude10 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch11 -> Extrude11 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2.5, 2.5), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch12 -> Extrude12 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch13 -> Extrude13 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2.5, 2.5), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch14 -> Extrude14 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 16.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch15 -> Extrude15 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 17.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2.5, 2.5), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch16 -> Extrude16 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5419247327, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((2.5, 2.5), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch17 -> Extrude17 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch19 -> Extrude20 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((2.5, 2.5)):
                Circle(0.45)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch20 -> Extrude21 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 20.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((2.5, 2.5)):
                Circle(0.35)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch21 -> Extrude22 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 20.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2.5, 2.5)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal or plastic enclosure/housing with an elongated rectangular base, a tall angled back panel, and integrated ribbing and flanges designed for structural rigidity and component mounting.
def model_138539_b5a9ff56_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9059.25, perimeter: 756.4
            with BuildLine():
                Line((176.25, -12.85), (176.25, 12.85))
                Line((176.25, 12.85), (-176.25, 12.85))
                Line((-176.25, 12.85), (-176.25, -12.85))
                Line((-176.25, -12.85), (176.25, -12.85))
            make_face()
        # OneSide extrude, distance=69
        extrude(amount=69)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 25.52, perimeter: 20.4
            with BuildLine():
                Line((170.45, 12.85), (170.45, 8.45))
                Line((170.45, 8.45), (176.25, 8.45))
                Line((176.25, 8.45), (176.25, 12.85))
                Line((176.25, 12.85), (170.45, 12.85))
            make_face()
            # Profile area: 25.52, perimeter: 20.4
            with BuildLine():
                Line((170.45, -8.45), (176.25, -8.45))
                Line((170.45, -12.85), (170.45, -8.45))
                Line((176.25, -12.85), (170.45, -12.85))
                Line((176.25, -8.45), (176.25, -12.85))
            make_face()
            # Profile area: 25.52, perimeter: 20.4
            with BuildLine():
                Line((-170.45, -12.85), (-170.45, -8.45))
                Line((-170.45, -8.45), (-176.25, -8.45))
                Line((-176.25, -8.45), (-176.25, -12.85))
                Line((-176.25, -12.85), (-170.45, -12.85))
            make_face()
            # Profile area: 25.52, perimeter: 20.4
            with BuildLine():
                Line((-176.25, 8.45), (-176.25, 12.85))
                Line((-170.45, 8.45), (-176.25, 8.45))
                Line((-170.45, 12.85), (-170.45, 8.45))
                Line((-176.25, 12.85), (-170.45, 12.85))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 129.74, perimeter: 202.2
            with BuildLine():
                Line((-76.45, -11.55), (-176.25, -11.55))
                Line((-176.25, -11.55), (-176.25, -12.85))
                Line((-176.25, -12.85), (-76.45, -12.85))
                Line((-76.45, -12.85), (-76.45, -11.55))
            make_face()
        # OneSide extrude, distance=6.3
        extrude(amount=6.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 369.26, perimeter: 207
            with BuildLine():
                Line((-76.45, 12.85), (-76.45, 9.15))
                Line((-176.25, 12.85), (-76.45, 12.85))
                Line((-176.25, 9.15), (-176.25, 12.85))
                Line((-76.45, 9.15), (-176.25, 9.15))
            make_face()
        # OneSide extrude, distance=6.3
        extrude(amount=6.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 75.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 59.88, perimeter: 200.8
            with BuildLine():
                Line((-176.25, 9.75), (-176.25, 9.15))
                Line((-176.25, 9.15), (-76.45, 9.15))
                Line((-76.45, 9.15), (-76.45, 9.75))
                Line((-76.45, 9.75), (-176.25, 9.75))
            make_face()
        # OneSide extrude, distance=3.1
        extrude(amount=3.1, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.85, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3348, perimeter: 232
            with BuildLine():
                Line((122.25, 0), (122.25, 62))
                Line((170.45, 0), (122.25, 0))
                Line((176.25, 0), (170.45, 0))
                Line((176.25, 62), (176.25, 0))
                Line((122.25, 62), (176.25, 62))
            make_face()
        # OneSide extrude, distance=64
        extrude(amount=64, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 318.6, perimeter: 119.8
            with BuildLine():
                Line((122.25, -70.95), (176.25, -70.95))
                Line((122.25, -76.85), (122.25, -70.95))
                Line((176.25, -76.85), (122.25, -76.85))
                Line((176.25, -70.95), (176.25, -76.85))
            make_face()
        # OneSide extrude, distance=37.4
        extrude(amount=37.4, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 25.52, perimeter: 20.4
            with BuildLine():
                Line((-170.45, -76.85), (-170.45, -72.45))
                Line((-170.45, -72.45), (-176.25, -72.45))
                Line((-176.25, -72.45), (-176.25, -76.85))
                Line((-176.25, -76.85), (-170.45, -76.85))
            make_face()
            # Profile area: 25.52, perimeter: 20.4
            with BuildLine():
                Line((-122.25, -72.45), (-122.25, -76.85))
                Line((-128.05, -72.45), (-122.25, -72.45))
                Line((-128.05, -76.85), (-128.05, -72.45))
                Line((-122.25, -76.85), (-128.05, -76.85))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 653.05, perimeter: 360.4
            with BuildLine():
                Line((-76.45, 12.85), (-76.45, 9.15))
                Line((-76.45, 9.15), (100.05, 9.15))
                Line((100.05, 9.15), (100.05, 12.85))
                Line((100.05, 12.85), (-76.45, 12.85))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)

        # Sketch11 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 70.9), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 38.11, perimeter: 28
            with BuildLine():
                Line((-41.95, 9.15), (-41.95, 12.85))
                Line((-41.95, 12.85), (-52.25, 12.85))
                Line((-52.25, 12.85), (-52.25, 9.15))
                Line((-52.25, 9.15), (-41.95, 9.15))
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 653.05, perimeter: 360.4
            with BuildLine():
                Line((100.05, -12.85), (100.05, -9.15))
                Line((100.05, -9.15), (-76.45, -9.15))
                Line((-76.45, -9.15), (-76.45, -11.55))
                Line((-76.45, -11.55), (-76.45, -12.85))
                Line((-76.45, -12.85), (100.05, -12.85))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 70.9), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 38.11, perimeter: 28
            with BuildLine():
                Line((-41.95, -12.85), (-41.95, -9.15))
                Line((-41.95, -9.15), (-52.25, -9.15))
                Line((-52.25, -9.15), (-52.25, -12.85))
                Line((-52.25, -12.85), (-41.95, -12.85))
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch15 -> Extrude14 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5711.91, perimeter: 640
            with BuildLine():
                Line((-174.25, -11.55), (-174.25, 9.15))
                Line((-174.25, -11.55), (-76.45, -11.55))
                Line((-76.45, -11.55), (-76.45, -9.15))
                Line((-76.45, -9.15), (100.05, -9.15))
                Line((125.05, -9.15), (100.05, -9.15))
                Line((125.05, -9.15), (125.05, 9.15))
                Line((125.05, 9.15), (100.05, 9.15))
                Line((100.05, 9.15), (-174.25, 9.15))
            make_face()
        # OneSide extrude, distance=-10.3
        extrude(amount=-10.3, mode=Mode.SUBTRACT)

        # Sketch16 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1635.3, perimeter: 199.4
            with BuildLine():
                Line((-78.25, 9.15), (-157.25, 9.15))
                Line((-157.25, 9.15), (-157.25, -11.55))
                Line((-157.25, -11.55), (-78.25, -11.55))
                Line((-78.25, -11.55), (-78.25, 9.15))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch17 -> Extrude16 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1515.24, perimeter: 202.2
            with BuildLine():
                Line((21.55, -9.15), (21.55, 9.15))
                Line((21.55, 9.15), (-61.25, 9.15))
                Line((-61.25, 9.15), (-61.25, -9.15))
                Line((-61.25, -9.15), (21.55, -9.15))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch18 -> Extrude17 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1171.2, perimeter: 164.6
            with BuildLine():
                Line((102.55, -9.15), (102.55, 9.15))
                Line((102.55, 9.15), (38.55, 9.15))
                Line((38.55, 9.15), (38.55, -9.15))
                Line((38.55, -9.15), (102.55, -9.15))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch19 -> Extrude18 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 311.1, perimeter: 70.6
            with BuildLine():
                Line((142.05, -9.15), (142.05, 9.15))
                Line((142.05, 9.15), (125.05, 9.15))
                Line((125.05, 9.15), (125.05, -9.15))
                Line((125.05, -9.15), (142.05, -9.15))
            make_face()
        # OneSide extrude, distance=-10.3
        extrude(amount=-10.3, mode=Mode.SUBTRACT)

        # Sketch20 -> Extrude19 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9.15, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 22.5, perimeter: 47
            with BuildLine():
                Line((-119.55, 69), (-119.55, 68))
                Line((-142.05, 69), (-119.55, 69))
                Line((-142.05, 68), (-142.05, 69))
                Line((-119.55, 68), (-142.05, 68))
            make_face()
        # OneSide extrude, distance=18.3
        extrude(amount=18.3, mode=Mode.ADD)

        # Sketch21 -> Extrude20 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -12.85, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4418, perimeter: 282
            with BuildLine():
                Line((170.45, 6), (76.45, 6))
                Line((170.45, 53), (170.45, 6))
                Line((76.45, 53), (170.45, 53))
                Line((76.45, 6), (76.45, 53))
            make_face()
        # OneSide extrude, distance=-19.2
        extrude(amount=-19.2, mode=Mode.SUBTRACT)

        # Sketch23 -> Extrude21 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -12.85, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4418, perimeter: 282
            with BuildLine():
                Line((70.65, 6), (-23.35, 6))
                Line((70.65, 53), (70.65, 6))
                Line((-23.35, 53), (70.65, 53))
                Line((-23.35, 6), (-23.35, 53))
            make_face()
        # OneSide extrude, distance=-19.2
        extrude(amount=-19.2, mode=Mode.SUBTRACT)

        # Sketch24 -> Extrude22 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -12.85, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4418, perimeter: 282
            with BuildLine():
                Line((-29.15, 6), (-123.15, 6))
                Line((-29.15, 53), (-29.15, 6))
                Line((-123.15, 53), (-29.15, 53))
                Line((-123.15, 6), (-123.15, 53))
            make_face()
        # OneSide extrude, distance=-19.2
        extrude(amount=-19.2, mode=Mode.SUBTRACT)

        # Sketch25 -> Extrude23 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -12.85, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1950.5, perimeter: 177
            with BuildLine():
                Line((-128.95, 6), (-170.45, 6))
                Line((-128.95, 53), (-128.95, 6))
                Line((-170.45, 53), (-128.95, 53))
                Line((-170.45, 6), (-170.45, 53))
            make_face()
        # OneSide extrude, distance=-100
        extrude(amount=-100, mode=Mode.SUBTRACT)

        # Sketch26 -> Extrude30 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.35, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 598.8, perimeter: 405.2
            with BuildLine():
                Line((170.45, 50), (-29.15, 50))
                Line((170.45, 53), (170.45, 50))
                Line((-29.15, 53), (170.45, 53))
                Line((-29.15, 50), (-29.15, 53))
            make_face()
            # Profile area: 279.3, perimeter: 192.2
            with BuildLine():
                Line((-122.25, 50), (-122.25, 53))
                Line((-29.15, 50), (-122.25, 50))
                Line((-29.15, 50), (-29.15, 53))
                Line((-122.25, 53), (-29.15, 53))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch27 -> Extrude24 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(76.45, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 695.6, perimeter: 123.6
            with BuildLine():
                Line((6.35, 50), (6.35, 6))
                Line((6.35, 50), (6.35, 53))
                Line((-8.45, 53), (6.35, 53))
                Line((-8.45, 6), (-8.45, 53))
                Line((6.35, 6), (-8.45, 6))
            make_face()
        # OneSide extrude, distance=-167.5
        extrude(amount=-167.5, mode=Mode.SUBTRACT)

        # Sketch28 -> Extrude25 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1391.2, perimeter: 217.6
            with BuildLine():
                Line((-170.45, 8.45), (-170.45, -6.35))
                Line((-170.45, -6.35), (-76.45, -6.35))
                Line((-76.45, -6.35), (-76.45, 8.45))
                Line((-76.45, 8.45), (-170.45, 8.45))
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch29 -> Extrude26 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1391.2, perimeter: 217.6
            with BuildLine():
                Line((-70.65, -6.35), (-70.65, 8.45))
                Line((23.35, -6.35), (-70.65, -6.35))
                Line((23.35, 8.45), (23.35, -6.35))
                Line((-70.65, 8.45), (23.35, 8.45))
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch30 -> Extrude27 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1391.2, perimeter: 217.6
            with BuildLine():
                Line((29.15, -6.35), (29.15, 8.45))
                Line((123.15, -6.35), (29.15, -6.35))
                Line((123.15, 8.45), (123.15, -6.35))
                Line((29.15, 8.45), (123.15, 8.45))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch31 -> Extrude28 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 37.7, perimeter: 24.6
            with BuildLine():
                Line((76.45, -12.85), (76.45, -6.35))
                Line((76.45, -6.35), (70.65, -6.35))
                Line((70.65, -6.35), (70.65, -12.85))
                Line((70.65, -12.85), (76.45, -12.85))
            make_face()
            # Profile area: 25.52, perimeter: 20.4
            with BuildLine():
                Line((70.65, 12.85), (70.65, 8.45))
                Line((70.65, 8.45), (76.45, 8.45))
                Line((76.45, 8.45), (76.45, 12.85))
                Line((76.45, 12.85), (70.65, 12.85))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5, mode=Mode.ADD)

        # Sketch32 -> Extrude29 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-123.15, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 94, perimeter: 98
            with BuildLine():
                Line((-6.45, 6), (-6.45, 53))
                Line((-6.45, 53), (-8.45, 53))
                Line((-8.45, 53), (-8.45, 6))
                Line((-8.45, 6), (-6.45, 6))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

    export_step(part.part, "my_model.step")
    return part.part


# Description: This is an airship or blimp envelope structure featuring an elongated, streamlined fusiform (torpedo-like) body with a latticed or wireframe upper surface, a solid lower section, and a vertical stabilizer fin protruding from the rear.
def model_139750_18e8f39b_0000():
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
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 120, perimeter: 68
            with BuildLine():
                Line((30, -4), (0, -4))
                Line((30, 0), (30, -4))
                Line((0, 0), (30, 0))
                Line((0, -4), (0, 0))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 75.1822771226, perimeter: 70.1603128538
            with BuildLine():
                CenterArc((-21.25, -35), 40.9458483854, 58.7362683056, 43.6028189727)
                Line((0, 0), (0, 7))
                Line((0, 7), (-30, 7))
                Line((-30, 7), (-30, 5))
            make_face()
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 19.7382259372, perimeter: 17.9113297592
            with BuildLine():
                Line((-10, 0), (-10, 3.3289486319))
                CenterArc((-21.25, -35), 39.9458483854, 73.6424118681, 7.3560014709)
                Line((-15, 0), (-15, 4.4538756427))
                Line((-15, 0), (-10, 0))
            make_face()
            # Profile area: 30.2029014662, perimeter: 22.1623821514
            with BuildLine():
                Line((-22.5, 0), (-22.5, 4.9262858682))
                CenterArc((-21.25, -35), 39.9458483854, 91.7932130853, 9.3938381891)
                Line((-29, 4.1868383929), (-29, 1))
                Line((-29, 1), (-29, 0))
                Line((-29, 0), (-22.5, 0))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 29.8531992223, perimeter: 22.018052554
            with BuildLine():
                Line((29, 1), (29, 4.1868383929))
                CenterArc((21.25, -35), 39.9458483854, 78.8129487257, 9.2919427597)
                Line((22.5710033213, 4.9239997176), (22.5710033213, 0))
                Line((22.5710033213, 0), (29, 0))
                Line((29, 0), (29, 1))
            make_face()
            # Profile area: 19.7382259372, perimeter: 17.9113297592
            with BuildLine():
                Line((10, 0), (10, 3.3289486319))
                Line((10, 0), (15, 0))
                Line((15, 0), (15, 4.4538756427))
                CenterArc((21.25, -35), 39.9458483854, 99.0015866611, 7.3560014709)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(30, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.44, perimeter: 14.8
            with BuildLine():
                Line((-3.6, 4.6), (-3.6, 0.4))
                Line((-3.6, 0.4), (-0.4, 0.4))
                Line((-0.4, 0.4), (-0.4, 4.6))
                Line((-0.4, 4.6), (-3.6, 4.6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch9 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 10, perimeter: 22.1980390272
            with BuildLine():
                Line((0, 4), (0, 2))
                Line((10, 4), (0, 2))
                Line((10, 4), (0, 4))
            make_face()
            # Profile area: 10, perimeter: 22.1980390272
            with BuildLine():
                Line((10, 0), (0, 2))
                Line((0, 2), (0, 0))
                Line((0, 0), (10, 0))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.35, perimeter: 6.4
            with BuildLine():
                Line((-30.75, 0.65), (-30.25, 0.65))
                Line((-30.25, 0.65), (-30.25, 3.35))
                Line((-30.25, 3.35), (-30.75, 3.35))
                Line((-30.75, 3.35), (-30.75, 0.65))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a dual-cylinder mounting bracket with a rectangular base frame featuring two parallel cylindrical posts that angle upward, designed to support or secure components between the two vertical shafts.
def model_141845_2c9bd259_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3150, perimeter: 230
            with BuildLine():
                Line((0, 45), (0, 0))
                Line((0, 0), (70, 0))
                Line((70, 0), (70, 45))
                Line((70, 45), (0, 45))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 86, perimeter: 90
            with BuildLine():
                Line((-67, -44), (-67, -42))
                Line((-67, -42), (-67, -3))
                Line((-67, -3), (-67, -1))
                Line((-67, -1), (-69, -1))
                Line((-69, -1), (-69, -44))
                Line((-69, -44), (-67, -44))
            make_face()
            # Profile area: 62, perimeter: 66
            with BuildLine():
                Line((-67, -3), (-67, -1))
                Line((-36, -3), (-67, -3))
                Line((-36, -3), (-36, -1))
                Line((-36, -1), (-67, -1))
            make_face()
            # Profile area: 86, perimeter: 90
            with BuildLine():
                Line((-34, -44), (-34, -1))
                Line((-34, -1), (-36, -1))
                Line((-36, -3), (-36, -1))
                Line((-36, -42), (-36, -3))
                Line((-36, -44), (-36, -42))
                Line((-36, -44), (-34, -44))
            make_face()
            # Profile area: 62, perimeter: 66
            with BuildLine():
                Line((-36, -44), (-36, -42))
                Line((-36, -42), (-67, -42))
                Line((-67, -44), (-67, -42))
                Line((-67, -44), (-36, -44))
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 30, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1209, perimeter: 140
            with BuildLine():
                Line((-67, -42), (-67, -3))
                Line((-36, -42), (-67, -42))
                Line((-36, -3), (-36, -42))
                Line((-67, -3), (-36, -3))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 30, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 296, perimeter: 296
            with BuildLine():
                Line((-69, -1), (-34, -1))
                Line((-69, -44), (-69, -1))
                Line((-34, -44), (-69, -44))
                Line((-34, -1), (-34, -44))
            make_face()
            with BuildLine():
                Line((-67, -3), (-36, -3))
                Line((-36, -3), (-36, -42))
                Line((-36, -42), (-67, -42))
                Line((-67, -42), (-67, -3))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1209, perimeter: 140
            with BuildLine():
                Line((-67, -42), (-67, -3))
                Line((-36, -42), (-67, -42))
                Line((-36, -3), (-36, -42))
                Line((-67, -3), (-36, -3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 49.0747170733, perimeter: 24.8332656439
            with BuildLine():
                CenterArc((50, 12.7), 3.9523369803, 179.3586982081, 180.5057991329)
                CenterArc((50, 12.7), 3.9523369803, -0.135502659, 179.4942008671)
            make_face()
            # Profile area: 60.5508012604, perimeter: 41.8865118699
            with BuildLine():
                CenterArc((50, 12.7), 3.9523369803, 179.3586982081, 180.5057991329)
                Line((46.0479105903, 12.7442369034), (45.9276471749, 2))
                Line((45.9276471749, 2), (53.9270428333, 2))
                Line((53.9523259275, 12.69065286), (53.9270428333, 2))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 31, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with Locations((-51.5, -22.5)):
                Circle(5)
        # OneSide extrude, distance=69
        extrude(amount=69, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 31, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.143360527, perimeter: 67.8584013175
            with BuildLine():
                CenterArc((-51.5, -22.5), 5.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-51.5, -22.5), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=69
        extrude(amount=69, mode=Mode.ADD)

        # Sketch10 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 105.6831768668, perimeter: 36.4424747816
            with Locations((-17, -22.5)):
                Circle(5.8)
        # OneSide extrude, distance=98
        extrude(amount=98, mode=Mode.ADD)
    return part.part


# Description: This is a stepped shaft or spindle with a cylindrical body that tapers to a smaller diameter at one end, featuring a pointed or conical tip.
def model_142842_736420da_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20, perimeter: 18
            with BuildLine():
                Line((20, 19), (20, 15))
                Line((20, 15), (25, 15))
                Line((25, 15), (25, 19))
                Line((25, 19), (20, 19))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -20), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 36, perimeter: 26
            with BuildLine():
                Line((0, 15), (0, 19))
                Line((9, 15), (0, 15))
                Line((9, 15), (9, 19))
                Line((9, 19), (0, 19))
            make_face()
            # Profile area: 5, perimeter: 12
            with BuildLine():
                Line((-1, 20), (0, 20))
                Line((-1, 15), (-1, 20))
                Line((0, 15), (-1, 15))
                Line((0, 15), (0, 19))
                Line((0, 19), (0, 20))
            make_face()
            # Profile area: 14, perimeter: 30
            with BuildLine():
                Line((0, 20), (10, 20))
                Line((0, 19), (0, 20))
                Line((9, 19), (0, 19))
                Line((9, 15), (9, 19))
                Line((10, 15), (9, 15))
                Line((10, 20), (10, 15))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -19), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1, 17.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((8, 17.5)):
                Circle(0.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch18 -> Extrude9 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((25, 15)):
                Circle(1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch19 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((25, 15), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((25, 15), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((25, 15)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch20 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((25, 15), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((25, 15), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((25, 15)):
                Circle(1.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch21 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 13), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((25, 15)):
                Circle(1)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch22 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 18), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((25, 15), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((25, 15), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((25, 15)):
                Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch23 -> Extrude14 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 18.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((25, 15)):
                Circle(1.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch24 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0000000298, perimeter: 4.0000000596
            with BuildLine():
                Line((25.50000038, 14.5000002161), (24.5000003651, 14.5000002161))
                Line((25.50000038, 15.500000231), (25.50000038, 14.5000002161))
                Line((24.5000003651, 15.500000231), (25.50000038, 15.500000231))
                Line((24.5000003651, 14.5000002161), (24.5000003651, 15.500000231))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a CubeSat deployment mechanism or structural component consisting of two stacked cubic frames with cross-braced panels and mounting points, designed for modular satellite assembly with corner attachment holes and internal reinforcement ribs.
def model_143025_16ccf8cb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((3, -3), (-3, -3))
                Line((3, 3), (3, -3))
                Line((-3, 3), (3, 3))
                Line((-3, -3), (-3, 3))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.5530461501, 1.7538378828)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.5530461501, 1.7538378828)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.4469538499, 1.7538378828)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.4469538499, 1.7538378828)):
                Circle(0.3)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.4505936909, 0.7719750238)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.5494063091, 0.7719750238)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.5494063091, -0.7280249762)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.5494063091, -1.7280249762)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.5494063091, -1.7280249762)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.4505936909, -1.7280249762)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.4505936909, -1.7280249762)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.4505936909, -0.7280249762)):
                Circle(0.3)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 36.0000010729, perimeter: 24.0000003576
            with BuildLine():
                Line((9.5000001416, -3.0000000447), (3.5000000522, -3.0000000447))
                Line((9.5000001416, 3.0000000447), (9.5000001416, -3.0000000447))
                Line((3.5000000522, 3.0000000447), (9.5000001416, 3.0000000447))
                Line((3.5000000522, -3.0000000447), (3.5000000522, 3.0000000447))
            make_face()
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            with Locations((6.5000000969, 0)):
                Circle(0.275)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            with Locations((4.0000000596, 2.5000000373)):
                Circle(0.275)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            with Locations((9.0000001341, 2.5000000373)):
                Circle(0.275)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            with Locations((4.0000000596, -2.5000000373)):
                Circle(0.275)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            with Locations((9.0000001341, -2.5000000373)):
                Circle(0.275)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a compact drone or quadcopter featuring a dark blue central body with four extended arms terminating in propeller motors, integrated cable routing along the arms, and a modular design with visible internal structural elements.
def model_143262_9b4e4d19_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 584.5671475545, perimeter: 90
            with BuildLine():
                Line((7.5, -12.9903810568), (15, 0))
                Line((15, 0), (7.5, 12.9903810568))
                Line((7.5, 12.9903810568), (-7.5, 12.9903810568))
                Line((-7.5, 12.9903810568), (-15, 0))
                Line((-15, 0), (-7.5, -12.9903810568))
                Line((-7.5, -12.9903810568), (7.5, -12.9903810568))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11.25, -6.4951905284, 0), x_dir=(0.5, 0.8660254038, 0), z_dir=(0.8660254038, -0.5, 0))):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((1.5, 8), (-1.5, 8))
                Line((-1.5, 8), (-1.5, 2))
                Line((-1.5, 2), (1.5, 2))
                Line((1.5, 2), (1.5, 8))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 7.1898088151, perimeter: 14.8198736095
            with BuildLine():
                CenterArc((-21.6423048454, 12.4951905284), 2, 18.5903778907, 262.8192442185)
                Line((-22.3923048454, 11.1961524227), (-21.2466609217, 10.5347145949))
                Line((-20.8923048454, 13.7942286341), (-22.3923048454, 11.1961524227))
                Line((-19.7466609217, 13.1327908063), (-20.8923048454, 13.7942286341))
            make_face()
            # Profile area: 5.3765617992, perimeter: 9.037999627
            with BuildLine():
                Line((-19.7466609217, 13.1327908063), (-20.8923048454, 13.7942286341))
                Line((-20.8923048454, 13.7942286341), (-22.3923048454, 11.1961524227))
                Line((-22.3923048454, 11.1961524227), (-21.2466609217, 10.5347145949))
                CenterArc((-21.6423048454, 12.4951905284), 2, -78.5903778907, 97.1807557815)
            make_face()
        # TwoSides extrude, along=1, against=-7.5
        extrude(amount=1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-7.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-11.25, -6.4951905284, 0), x_dir=(0.5, -0.8660254038, 0), z_dir=(-0.8660254038, -0.5, 0))):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((-1.5, 2), (1.5, 2))
                Line((1.5, 2), (1.5, 8))
                Line((1.5, 8), (-1.5, 8))
                Line((-1.5, 8), (-1.5, 2))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 5.3765617992, perimeter: 9.037999627
            with BuildLine():
                CenterArc((21.6423048454, 12.4951905284), 2, 161.4096221093, 97.1807557815)
                Line((21.2466609217, 10.5347145949), (22.3923048454, 11.1961524227))
                Line((22.3923048454, 11.1961524227), (20.8923048454, 13.7942286341))
                Line((20.8923048454, 13.7942286341), (19.7466609217, 13.1327908063))
            make_face()
            # Profile area: 7.1898088151, perimeter: 14.8198736095
            with BuildLine():
                Line((20.8923048454, 13.7942286341), (19.7466609217, 13.1327908063))
                Line((22.3923048454, 11.1961524227), (20.8923048454, 13.7942286341))
                Line((21.2466609217, 10.5347145949), (22.3923048454, 11.1961524227))
                CenterArc((21.6423048454, 12.4951905284), 2, -101.4096221093, 262.8192442185)
            make_face()
        # TwoSides extrude, along=1, against=-7.5
        extrude(amount=1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-7.5, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11.25, 6.4951905284, 0), x_dir=(-0.5, 0.8660254038, 0), z_dir=(0.8660254038, 0.5, 0))):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((-1.5, 2), (1.5, 2))
                Line((1.5, 2), (1.5, 8))
                Line((1.5, 8), (-1.5, 8))
                Line((-1.5, 8), (-1.5, 2))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 7.1898088151, perimeter: 14.8198736095
            with BuildLine():
                CenterArc((-21.6423048454, -12.4951905284), 2, 78.5903778907, 262.8192442185)
                Line((-20.8923048454, -13.7942286341), (-19.7466609217, -13.1327908063))
                Line((-22.3923048454, -11.1961524227), (-20.8923048454, -13.7942286341))
                Line((-21.2466609217, -10.5347145949), (-22.3923048454, -11.1961524227))
            make_face()
            # Profile area: 5.3765617992, perimeter: 9.037999627
            with BuildLine():
                Line((-21.2466609217, -10.5347145949), (-22.3923048454, -11.1961524227))
                Line((-22.3923048454, -11.1961524227), (-20.8923048454, -13.7942286341))
                Line((-20.8923048454, -13.7942286341), (-19.7466609217, -13.1327908063))
                CenterArc((-21.6423048454, -12.4951905284), 2, -18.5903778907, 97.1807557815)
            make_face()
        # TwoSides extrude, along=1, against=-7.5
        extrude(amount=1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-7.5, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-11.25, 6.4951905284, 0), x_dir=(-0.5, -0.8660254038, 0), z_dir=(-0.8660254038, 0.5, 0))):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((1.5, 2), (1.5, 8))
                Line((1.5, 8), (-1.5, 8))
                Line((-1.5, 8), (-1.5, 2))
                Line((-1.5, 2), (1.5, 2))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 5.3765617992, perimeter: 9.037999627
            with BuildLine():
                CenterArc((21.6423048454, -12.4951905284), 2, 101.4096221093, 97.1807557815)
                Line((19.7466609217, -13.1327908063), (20.8923048454, -13.7942286341))
                Line((20.8923048454, -13.7942286341), (22.3923048454, -11.1961524227))
                Line((22.3923048454, -11.1961524227), (21.2466609217, -10.5347145949))
            make_face()
            # Profile area: 7.1898088151, perimeter: 14.8198736095
            with BuildLine():
                Line((22.3923048454, -11.1961524227), (21.2466609217, -10.5347145949))
                Line((20.8923048454, -13.7942286341), (22.3923048454, -11.1961524227))
                Line((19.7466609217, -13.1327908063), (20.8923048454, -13.7942286341))
                CenterArc((21.6423048454, -12.4951905284), 2, -161.4096221093, 262.8192442185)
            make_face()
        # TwoSides extrude, along=1, against=-7.5
        extrude(amount=1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-7.5, mode=Mode.ADD)

        # Sketch11 -> Extrude10 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 12.9903810568, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.9751682144, perimeter: 32.090672095
            with BuildLine():
                Line((-7.5, 0), (-2, 0))
                Line((-7.5, 7.7696960071), (-7.5, 0))
                CenterArc((-6, 3), 5, 107.4576031237, 215.6724992304)
            make_face()
            # Profile area: 45.5646481254, perimeter: 25.8646464551
            with BuildLine():
                CenterArc((-6, 3), 5, -36.8698976458, 144.3275007696)
                Line((-7.5, 7.7696960071), (-7.5, 0))
                Line((-7.5, 0), (-2, 0))
            make_face()
            # Profile area: 32.9751682144, perimeter: 32.090672095
            with BuildLine():
                CenterArc((6, 3), 5, -143.1301023542, 215.6724992304)
                Line((7.5, 0), (7.5, 7.7696960071))
                Line((2, 0), (7.5, 0))
            make_face()
            # Profile area: 45.5646481254, perimeter: 25.8646464551
            with BuildLine():
                Line((2, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 7.7696960071))
                CenterArc((6, 3), 5, 72.5423968763, 144.3275007696)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch12 -> Extrude11 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -12.9903810568, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 45.5646481254, perimeter: 25.8646464551
            with BuildLine():
                CenterArc((-6, 3), 5, -36.8698976458, 144.3275007696)
                Line((-7.5, 7.7696960071), (-7.5, 0))
                Line((-7.5, 0), (-2, 0))
            make_face()
            # Profile area: 32.9751682144, perimeter: 32.090672095
            with BuildLine():
                Line((-7.5, 0), (-2, 0))
                Line((-7.5, 7.7696960071), (-7.5, 0))
                CenterArc((-6, 3), 5, 107.4576031237, 215.6724992304)
            make_face()
            # Profile area: 45.5646481254, perimeter: 25.8646464551
            with BuildLine():
                Line((2, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 7.7696960071))
                CenterArc((6, 3), 5, 72.5423968763, 144.3275007696)
            make_face()
            # Profile area: 32.9751682144, perimeter: 32.090672095
            with BuildLine():
                CenterArc((6, 3), 5, -143.1301023542, 215.6724992304)
                Line((7.5, 0), (7.5, 7.7696960071))
                Line((2, 0), (7.5, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch11 -> Extrude12 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 12.9903810568, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.9751682144, perimeter: 32.090672095
            with BuildLine():
                CenterArc((6, 3), 5, -143.1301023542, 215.6724992304)
                Line((7.5, 0), (7.5, 7.7696960071))
                Line((2, 0), (7.5, 0))
            make_face()
            # Profile area: 45.5646481254, perimeter: 25.8646464551
            with BuildLine():
                Line((2, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 7.7696960071))
                CenterArc((6, 3), 5, 72.5423968763, 144.3275007696)
            make_face()
            # Profile area: 32.9751682144, perimeter: 32.090672095
            with BuildLine():
                Line((-7.5, 0), (-2, 0))
                Line((-7.5, 7.7696960071), (-7.5, 0))
                CenterArc((-6, 3), 5, 107.4576031237, 215.6724992304)
            make_face()
            # Profile area: 45.5646481254, perimeter: 25.8646464551
            with BuildLine():
                CenterArc((-6, 3), 5, -36.8698976458, 144.3275007696)
                Line((-7.5, 7.7696960071), (-7.5, 0))
                Line((-7.5, 0), (-2, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude13 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -12.9903810568, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 45.5646481254, perimeter: 25.8646464551
            with BuildLine():
                CenterArc((-6, 3), 5, -36.8698976458, 144.3275007696)
                Line((-7.5, 7.7696960071), (-7.5, 0))
                Line((-7.5, 0), (-2, 0))
            make_face()
            # Profile area: 32.9751682144, perimeter: 32.090672095
            with BuildLine():
                Line((-7.5, 0), (-2, 0))
                Line((-7.5, 7.7696960071), (-7.5, 0))
                CenterArc((-6, 3), 5, 107.4576031237, 215.6724992304)
            make_face()
            # Profile area: 45.5646481254, perimeter: 25.8646464551
            with BuildLine():
                Line((2, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 7.7696960071))
                CenterArc((6, 3), 5, 72.5423968763, 144.3275007696)
            make_face()
            # Profile area: 32.9751682144, perimeter: 32.090672095
            with BuildLine():
                CenterArc((6, 3), 5, -143.1301023542, 215.6724992304)
                Line((7.5, 0), (7.5, 7.7696960071))
                Line((2, 0), (7.5, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.SUBTRACT)

        # Sketch13 -> Extrude14 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -14.4903810568, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-6, 3)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((6, 3)):
                Circle(1)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)

        # Sketch14 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 14.4903810568, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-6, 3)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((6, 3)):
                Circle(1)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)

        # Sketch15 -> Extrude16 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.913222955, perimeter: 5.7792483588
            with BuildLine():
                Line((21.6423048454, -12.4951905284), (21.6423048454, -11.4951905284))
                Line((21.6423048454, -11.4951905284), (19.9102540378, -11.4951905284))
                CenterArc((21.6423048454, -12.4951905284), 2, 150, 30)
                Line((21.6423048454, -12.4951905284), (19.6423048454, -12.4951905284))
            make_face()
            # Profile area: 5.7396688649, perimeter: 11.3377450763
            with BuildLine():
                Line((21.6423048454, -12.4951905284), (19.6423048454, -12.4951905284))
                CenterArc((21.6423048454, -12.4951905284), 2, 180, 30)
                Line((19.9102540378, -13.4951905284), (23.374355653, -13.4951905284))
                CenterArc((21.6423048454, -12.4951905284), 2, -30, 60)
                Line((21.6423048454, -11.4951905284), (23.374355653, -11.4951905284))
                Line((21.6423048454, -12.4951905284), (21.6423048454, -11.4951905284))
            make_face()
            # Profile area: 12.8889443992, perimeter: 17.3456837964
            with BuildLine():
                Line((23.374355653, -13.4951905284), (30, -13.4951905284))
                Line((30, -13.4951905284), (30, -11.4951905284))
                Line((23.374355653, -11.4951905284), (30, -11.4951905284))
                CenterArc((21.6423048454, -12.4951905284), 2, -30, 60)
            make_face()
            # Profile area: 13.4581637809, perimeter: 17.9149031781
            with BuildLine():
                CenterArc((21.6423048454, -12.4951905284), 2, 150, 30)
                Line((19.9102540378, -11.4951905284), (13, -11.4951905284))
                Line((13, -11.4951905284), (13, -13.4951905284))
                Line((13, -13.4951905284), (19.9102540378, -13.4951905284))
                CenterArc((21.6423048454, -12.4951905284), 2, 180, 30)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch16 -> Extrude17 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 13.17355409, perimeter: 17.6302934873
            with BuildLine():
                CenterArc((21.6423048454, 12.4951905284), 2, -30, 60)
                Line((30.1423048454, 11.4951905284), (23.374355653, 11.4951905284))
                Line((30.1423048454, 13.4951905284), (30.1423048454, 11.4951905284))
                Line((23.374355653, 13.4951905284), (30.1423048454, 13.4951905284))
            make_face()
            # Profile area: 7.6528918199, perimeter: 11.1169934351
            with BuildLine():
                Line((23.374355653, 11.4951905284), (19.9102540378, 11.4951905284))
                CenterArc((21.6423048454, 12.4951905284), 2, -30, 60)
                Line((19.9102540378, 13.4951905284), (23.374355653, 13.4951905284))
                CenterArc((21.6423048454, 12.4951905284), 2, 150, 30)
                CenterArc((21.6423048454, 12.4951905284), 2, 180, 30)
            make_face()
            # Profile area: 6.586777045, perimeter: 15.3151467436
            with BuildLine():
                CenterArc((21.6423048454, 12.4951905284), 2, 150, 30)
                Line((13.1423048454, 13.4951905284), (19.9102540378, 13.4951905284))
                Line((13.1423048454, 12.9951905284), (13.1423048454, 13.4951905284))
                Line((13.1423048454, 12.4951905284), (13.1423048454, 12.9951905284))
                Line((19.6423048454, 12.4951905284), (13.1423048454, 12.4951905284))
            make_face()
            # Profile area: 6.586777045, perimeter: 15.3151467436
            with BuildLine():
                Line((19.9102540378, 11.4951905284), (13.1423048454, 11.4951905284))
                CenterArc((21.6423048454, 12.4951905284), 2, 180, 30)
                Line((19.6423048454, 12.4951905284), (13.1423048454, 12.4951905284))
                Line((13.1423048454, 11.4951905284), (13.1423048454, 12.4951905284))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch17 -> Extrude18 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 13.17355409, perimeter: 17.6302934873
            with BuildLine():
                CenterArc((-21.6423048454, -12.4951905284), 2, 150, 60)
                Line((-23.374355653, -11.4951905284), (-30.1423048454, -11.4951905284))
                Line((-30.1423048454, -11.4951905284), (-30.1423048454, -13.4951905284))
                Line((-23.374355653, -13.4951905284), (-30.1423048454, -13.4951905284))
            make_face()
            # Profile area: 7.6528918199, perimeter: 11.1169934351
            with BuildLine():
                CenterArc((-21.6423048454, -12.4951905284), 2, -30, 30)
                CenterArc((-21.6423048454, -12.4951905284), 2, 0, 30)
                Line((-19.9102540378, -11.4951905284), (-23.374355653, -11.4951905284))
                CenterArc((-21.6423048454, -12.4951905284), 2, 150, 60)
                Line((-19.9102540378, -13.4951905284), (-23.374355653, -13.4951905284))
            make_face()
            # Profile area: 6.586777045, perimeter: 15.3151467436
            with BuildLine():
                Line((-13.1423048454, -13.4951905284), (-13.1423048454, -12.4951905284))
                Line((-19.6423048454, -12.4951905284), (-13.1423048454, -12.4951905284))
                CenterArc((-21.6423048454, -12.4951905284), 2, -30, 30)
                Line((-13.1423048454, -13.4951905284), (-19.9102540378, -13.4951905284))
            make_face()
            # Profile area: 6.586777045, perimeter: 15.3151467436
            with BuildLine():
                CenterArc((-21.6423048454, -12.4951905284), 2, 0, 30)
                Line((-19.6423048454, -12.4951905284), (-13.1423048454, -12.4951905284))
                Line((-13.1423048454, -12.4951905284), (-13.1423048454, -11.4951905284))
                Line((-13.1423048454, -11.4951905284), (-19.9102540378, -11.4951905284))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch18 -> Extrude19 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 6.586777045, perimeter: 15.3151467436
            with BuildLine():
                Line((-19.6423048454, 12.4951905284), (-13.1423048454, 12.4951905284))
                Line((-13.1423048454, 12.4951905284), (-13.1423048454, 13.4951905284))
                Line((-13.1423048454, 13.4951905284), (-19.9102540378, 13.4951905284))
                CenterArc((-21.6423048454, 12.4951905284), 2, 0, 30)
            make_face()
            # Profile area: 6.586777045, perimeter: 15.3151467436
            with BuildLine():
                Line((-19.9102540378, 11.4951905284), (-13.1423048454, 11.4951905284))
                Line((-13.1423048454, 12.4951905284), (-13.1423048454, 11.4951905284))
                Line((-19.6423048454, 12.4951905284), (-13.1423048454, 12.4951905284))
                CenterArc((-21.6423048454, 12.4951905284), 2, -30, 30)
            make_face()
            # Profile area: 13.17355409, perimeter: 17.6302934873
            with BuildLine():
                Line((-23.374355653, 13.4951905284), (-30.1423048454, 13.4951905284))
                Line((-30.1423048454, 13.4951905284), (-30.1423048454, 11.4951905284))
                Line((-30.1423048454, 11.4951905284), (-23.374355653, 11.4951905284))
                CenterArc((-21.6423048454, 12.4951905284), 2, 150, 60)
            make_face()
            # Profile area: 7.6528918199, perimeter: 11.1169934351
            with BuildLine():
                CenterArc((-21.6423048454, 12.4951905284), 2, 150, 60)
                Line((-23.374355653, 11.4951905284), (-19.9102540378, 11.4951905284))
                CenterArc((-21.6423048454, 12.4951905284), 2, -30, 30)
                CenterArc((-21.6423048454, 12.4951905284), 2, 0, 30)
                Line((-19.9102540378, 13.4951905284), (-23.374355653, 13.4951905284))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a dark blue parallelogram-shaped box or container with slanted sides, featuring a hollow interior with open top and bottom, and triangular cutouts or slots visible on the upper right and lower left edges.
def model_145201_a104c55b_0005():
    """Model: 1. etg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1413872.7000000002, perimeter: 4984.6
            with BuildLine():
                Line((0, 873.3), (0, 0))
                Line((0, 0), (1619, 0))
                Line((1619, 0), (1619, 873.3))
                Line((1619, 873.3), (0, 873.3))
            make_face()
        # OneSide extrude, distance=248
        extrude(amount=248)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 11760, perimeter: 436
            with BuildLine():
                Line((266, 85), (168, 85))
                Line((266, 205), (266, 85))
                Line((168, 205), (266, 205))
                Line((168, 85), (168, 205))
            make_face()
            # Profile area: 11760, perimeter: 436
            with BuildLine():
                Line((604, 85), (506, 85))
                Line((604, 205), (604, 85))
                Line((506, 205), (604, 205))
                Line((506, 85), (506, 205))
            make_face()
            # Profile area: 18009, perimeter: 588
            with BuildLine():
                Line((907, 0), (907, 207))
                Line((907, 207), (820, 207))
                Line((820, 207), (820, 0))
                Line((820, 0), (907, 0))
            make_face()
            # Profile area: 11760, perimeter: 436
            with BuildLine():
                Line((1254, 85), (1156, 85))
                Line((1254, 205), (1254, 85))
                Line((1156, 205), (1254, 205))
                Line((1156, 85), (1156, 205))
            make_face()
            # Profile area: 11760, perimeter: 436
            with BuildLine():
                Line((1492, 85), (1394, 85))
                Line((1492, 205), (1492, 85))
                Line((1394, 205), (1492, 205))
                Line((1394, 85), (1394, 205))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1619, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 20079, perimeter: 608
            with BuildLine():
                Line((487.3, 217), (390.3, 217))
                Line((390.3, 217), (390.3, 10))
                Line((390.3, 10), (487.3, 10))
                Line((487.3, 10), (487.3, 217))
            make_face()
        # OneSide extrude, distance=-27
        extrude(amount=-27, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1619, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2300, perimeter: 480
            with BuildLine():
                Line((390.3, 10), (487.3, 10))
                Line((390.3, 10), (323.8, 10))
                Line((323.8, 10), (323.8, 0))
                Line((323.8, 0), (553.8, 0))
                Line((553.8, 0), (553.8, 10))
                Line((553.8, 10), (487.3, 10))
            make_face()
        # OneSide extrude, distance=45
        extrude(amount=45, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1619, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 16440, perimeter: 514
            with BuildLine():
                Line((709.3, 100), (572.3, 100))
                Line((709.3, 220), (709.3, 100))
                Line((572.3, 220), (709.3, 220))
                Line((572.3, 100), (572.3, 220))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch1 (1) -> Extrude1 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 9680, perimeter: 396
            with BuildLine():
                Line((173, 90), (261, 90))
                Line((261, 90), (261, 200))
                Line((261, 200), (173, 200))
                Line((173, 200), (173, 90))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch2 (1) -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 9680, perimeter: 396
            with BuildLine():
                Line((511, 90), (599, 90))
                Line((599, 90), (599, 200))
                Line((599, 200), (511, 200))
                Line((511, 200), (511, 90))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 (1) -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 9680, perimeter: 396
            with BuildLine():
                Line((1249, 200), (1161, 200))
                Line((1161, 200), (1161, 90))
                Line((1161, 90), (1249, 90))
                Line((1249, 90), (1249, 200))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 9680, perimeter: 396
            with BuildLine():
                Line((1399, 90), (1487, 90))
                Line((1487, 90), (1487, 200))
                Line((1487, 200), (1399, 200))
                Line((1399, 200), (1399, 90))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1800, perimeter: 270
            with BuildLine():
                Line((847.4839903918, 76.0203123519), (832.4839903918, 76.0203123519))
                Line((847.4839903918, 196.0203123519), (847.4839903918, 76.0203123519))
                Line((832.4839903918, 196.0203123519), (847.4839903918, 196.0203123519))
                Line((832.4839903918, 76.0203123519), (832.4839903918, 196.0203123519))
            make_face()
            # Profile area: 1800, perimeter: 270
            with BuildLine():
                Line((871.4428837764, 76.308973718), (856.4428837764, 76.308973718))
                Line((871.4428837764, 196.308973718), (871.4428837764, 76.308973718))
                Line((856.4428837764, 196.308973718), (871.4428837764, 196.308973718))
                Line((856.4428837764, 76.308973718), (856.4428837764, 196.308973718))
            make_face()
            # Profile area: 1800, perimeter: 270
            with BuildLine():
                Line((895.9790998931, 76.308973718), (880.9790998931, 76.308973718))
                Line((895.9790998931, 196.308973718), (895.9790998931, 76.308973718))
                Line((880.9790998931, 196.308973718), (895.9790998931, 196.308973718))
                Line((880.9790998931, 76.308973718), (880.9790998931, 196.308973718))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1609, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 13970, perimeter: 474
            with BuildLine():
                Line((577.3, 105), (704.3, 105))
                Line((704.3, 105), (704.3, 215))
                Line((704.3, 215), (577.3, 215))
                Line((577.3, 215), (577.3, 105))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1592, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2280, perimeter: 334
            with BuildLine():
                Line((467.3, 50), (467.3, 202))
                Line((467.3, 202), (452.3, 202))
                Line((452.3, 202), (452.3, 50))
                Line((452.3, 50), (467.3, 50))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat-bottomed angular bracket or mounting plate with a distinctive arrow-like or chevron shape, featuring a protruding arm on the left, a recessed base section, and internal ribbing or web structures for structural reinforcement.
def model_21339_4c044144_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 14.5207972894
            with BuildLine():
                Line((-2.2944219067, -1.9605138607), (-2.2944219067, 2.0394861393))
                Line((2.2055780933, -1.9605138607), (-2.2944219067, -1.9605138607))
                Line((-2.2944219067, 2.0394861393), (2.2055780933, -1.9605138607))
            make_face()
            # Profile area: 9, perimeter: 14.5207972894
            with BuildLine():
                Line((-2.2944219067, 2.0394861393), (2.2055780933, -1.9605138607))
                Line((2.2055780933, 2.0394861393), (2.2055780933, -1.9605138607))
                Line((-2.2944219067, 2.0394861393), (2.2055780933, 2.0394861393))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.2944219067, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.30000002, perimeter: 2.20000008
            with BuildLine():
                Line((1.9605138607, 0.5), (2.5605139007, 0.5))
                Line((1.9605138607, 0), (1.9605138607, 0.5))
                Line((2.5605139007, 0), (1.9605138607, 0))
                Line((2.5605139007, 0.5), (2.5605139007, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-2.2944219067, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.30000002, perimeter: 2.20000008
            with BuildLine():
                Line((-1.9605138607, 0), (-2.5605139007, 0))
                Line((-1.9605138607, 0.5), (-1.9605138607, 0))
                Line((-2.5605139007, 0.5), (-1.9605138607, 0.5))
                Line((-2.5605139007, 0), (-2.5605139007, 0.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.2944219067, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.321248387, perimeter: 2.2849935479
            with BuildLine():
                Line((-1.3969893653, 0), (-2.0394861393, 0))
                Line((-1.3969893653, 0.5), (-1.3969893653, 0))
                Line((-2.0394861393, 0.5), (-1.3969893653, 0.5))
                Line((-2.0394861393, 0), (-2.0394861393, 0.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7500000149, perimeter: 4.3027756923
            with BuildLine():
                Line((1.7944219067, -0.5394861393), (0.7944219067, -0.5394861393))
                Line((1.7944219067, -0.5394861393), (1.7944219067, 0.9605138905))
                Line((1.7944219067, 0.9605138905), (0.7944219067, -0.5394861393))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2459016381, perimeter: 2.4084056775
            with BuildLine():
                Line((1.0724685794, -1.4220458259), (0.0724685794, -1.4220458259))
                Line((1.0724685794, -1.4220458259), (0.4823046317, -0.9302425496))
                Line((0.0724685794, -1.4220458259), (0.4823046317, -0.9302425496))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8962822887, perimeter: 4.1930343942
            with BuildLine():
                Line((-0.6284157309, -1.4220458259), (0.0201365929, -0.5297335415))
                Line((0.0201365929, -0.5297335415), (-0.9364919487, 0.1779337911))
                Line((-0.9284157309, -1.4220458259), (-0.9364919487, 0.1779337911))
                Line((-0.6284157309, -1.4220458259), (-0.9284157309, -1.4220458259))
            make_face()
            # Profile area: 0.3942758942, perimeter: 3.0231411078
            with BuildLine():
                Line((-0.4561078542, 0.5121678913), (0.776748148, 0.5112522977))
                Line((0.312113434, -0.1280164981), (-0.4561078542, 0.5121678913))
                Line((0.776748148, 0.5112522977), (0.312113434, -0.1280164981))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude14 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.9605138607), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((4.0444219067, 0.25), 0.25, 90, 180)
                CenterArc((4.0444219067, 0.25), 0.25, -90, 90)
                CenterArc((4.0444219067, 0.25), 0.25, 0, 90)
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.ADD)

        # Sketch13 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.3969893653), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((-4.0444219067, 0.25), 0.25, -90, 180)
                CenterArc((-4.0444219067, 0.25), 0.25, 90, 90)
                CenterArc((-4.0444219067, 0.25), 0.25, -180, 90)
            make_face()
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.ADD)

        # Sketch17 -> Extrude19 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5605139007), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-4.0444219067, 0.25)):
                Circle(0.1)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch18 -> Extrude20 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.9605138607), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.3633738194, 0.25)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.1574973958, 0.25)):
                Circle(0.1)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: A hollow cylindrical body with a mesh or perforated top cap and vertical ribbed/fluted side walls, designed as an air or liquid filter element.
def model_22062_2d6b3b72_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.7225986992, perimeter: 28.2977347462
            Circle(4.5037243632)
        # OneSide extrude, distance=17
        extrude(amount=17)
    return part.part


# Description: A dark blue parallelogram-shaped flat plate with a slightly trapezoidal profile, featuring small mounting holes or attachment points.
def model_23325_292b3294_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 258.6764061866, perimeter: 80.6128329804
            with BuildLine():
                CenterArc((2.3898571622, 26.0654037011), 18, -114.3957293245, 56.7033243133)
                CenterArc((-5.1687116796, 9.3993292663), 0.3, 65.6042706755, 112.2514469138)
                CenterArc((2.9256164927, 9.0962592412), 8.4, 177.8557175893, 92.1503085124)
                Line((2.9264999653, 0.6962592877), (21.8264999653, 0.6962592877))
                CenterArc((21.8264999653, 3.3962592877), 2.7, -90, 149.9435823031)
                Line((19.4574211047, 7.886626127), (23.1788017441, 5.7331974339))
                CenterArc((20.2083991958, 9.1850990404), 1.5, 179.9886776352, 59.9681729887)
                Line((18.7092751065, 13.6177121644), (18.7083992251, 9.1853954592))
                CenterArc((15.7092751065, 13.6177121644), 3, 0, 180)
                Line((12.7092751065, 13.6177121644), (12.7092751065, 12.1177121644))
                CenterArc((11.2092772214, 12.1202310791), 1.5, -57.7266378744, 57.6304223746)
            make_face()
        # OneSide extrude, distance=2.35
        extrude(amount=2.35)

        # Sketch16 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 126.1747227147, perimeter: 62.0827427359
            with BuildLine():
                Line((-122.5, 25), (-97.5, 25))
                CenterArc((-122.5, 22.65), 2.35, 90, 180)
                Line((-97.5, 20.3), (-122.5, 20.3))
                Line((-97.5, 25), (-97.5, 20.3))
            make_face()
        # Symmetric extrude, each_side=11
        extrude(amount=11, both=True)

        # Sketch23 -> Extrude14 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.1274315796, perimeter: 60.3185789489
            with BuildLine():
                CenterArc((-17.5, 12.5), 5.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-17.5, 12.5), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch30 -> Extrude16 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.3133251936, perimeter: 9.3530743609
            with BuildLine():
                Line((-12.8696501555, -13.0481308537), (-11.3247230196, -12.8402844086))
                Line((-11.3247230196, -12.8402844086), (-10.7322597532, -11.3984150393))
                Line((-10.7322597532, -11.3984150393), (-11.6847236228, -10.1643921152))
                Line((-11.6847236228, -10.1643921152), (-13.2296507587, -10.3722385603))
                Line((-13.2296507587, -10.3722385603), (-13.8221140251, -11.8141079296))
                Line((-13.8221140251, -11.8141079296), (-12.8696501555, -13.0481308537))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch34 -> Extrude17 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 66.1022104447, perimeter: 32.9646003294
            with BuildLine():
                CenterArc((-24, -5.3), 2.7, -90, 180)
                Line((-24, -2.6), (-32, -2.6))
                CenterArc((-32, -5.3), 2.7, 90, 180)
                Line((-32, -8), (-24, -8))
            make_face()
        # OneSide extrude, distance=4.7
        extrude(amount=4.7)

        # Sketch35 -> Extrude18 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.8576824547, perimeter: 16.3500981815
            with BuildLine():
                CenterArc((-32, -5.3), 2.7, -90, 42.2054464037)
                Line((-32, -8), (-24, -8))
                CenterArc((-24, -5.3), 2.7, -132.2054464037, 42.2054464037)
                Line((-30.1861642853, -7.3), (-25.8138357147, -7.3))
            make_face()
            # Profile area: 3.8576824547, perimeter: 16.3500981815
            with BuildLine():
                CenterArc((-24, -5.3), 2.7, 90, 42.2054464037)
                Line((-32, -2.6), (-24, -2.6))
                CenterArc((-32, -5.3), 2.7, 47.7945535963, 42.2054464037)
                Line((-25.8138357147, -3.3), (-30.1861642853, -3.3))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)

        # Sketch36 -> Extrude19 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -7.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 12.1873578258, perimeter: 14.4276724636
            with BuildLine():
                Line((-21.2999994829, 3.7), (-25.8138357147, 3.7))
                Line((-25.8138357147, 1), (-25.8138357147, 3.7))
                Line((-25.8138357147, 1), (-21.2999994829, 1))
                Line((-21.2999994829, 3.7), (-21.2999994829, 1))
            make_face()
            # Profile area: 2.6626421742, perimeter: 7.3723275364
            with BuildLine():
                Line((-25.8138357147, 3.7), (-26.7999994829, 3.7))
                Line((-26.7999994829, 3.7), (-26.7999994829, 1))
                Line((-26.7999994829, 1), (-25.8138357147, 1))
                Line((-25.8138357147, 1), (-25.8138357147, 3.7))
            make_face()
            # Profile area: 12.1873578258, perimeter: 14.4276724636
            with BuildLine():
                Line((-30.1861642853, 3.7), (-30.1861642853, 1))
                Line((-34.7000005171, 3.7), (-30.1861642853, 3.7))
                Line((-34.7000005171, 3.7), (-34.7000005171, 1))
                Line((-30.1861642853, 1), (-34.7000005171, 1))
            make_face()
            # Profile area: 2.6626421742, perimeter: 7.3723275364
            with BuildLine():
                Line((-29.2000005171, 1), (-30.1861642853, 1))
                Line((-29.2000005171, 3.7), (-29.2000005171, 1))
                Line((-30.1861642853, 3.7), (-29.2000005171, 3.7))
                Line((-30.1861642853, 3.7), (-30.1861642853, 1))
            make_face()
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True, mode=Mode.SUBTRACT)

        # Sketch39 -> Extrude20 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 51.0508806208, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((-2, -11), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2, -11), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch40 -> Extrude21 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.1704642476, perimeter: 55.6061899685
            with BuildLine():
                CenterArc((-2, -11), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2, -11), 4.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 48.5561274442, perimeter: 65.8191371119
            with BuildLine():
                CenterArc((-2, -11), 5.9754410214, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2, -11), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch42 -> Extrude22 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 90.9342784535, perimeter: 42.9886990661
            with BuildLine():
                Line((-21.5, 10), (-17.4807754524, 6.069577555))
                CenterArc((-15.5930316426, 7.9999721541), 2.7, -134.36, 180)
                Line((-13.7052878327, 9.9303667532), (-16.8443, 13))
                Line((-13.7052878327, 16.0696332468), (-16.8443, 13))
                CenterArc((-15.5930316426, 18.0000278459), 2.7, -45.64, 180)
                Line((-21.5, 16), (-17.4807754524, 19.930422445))
                Line((-21.5, 10), (-21.5, 16))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)
    return part.part


# Description: This is a folding stairs or step ladder assembly featuring a rigid frame with four rectangular rungs, a triangular support brace on the left side, and a hinged design that allows the ladder to collapse for compact storage.
def model_23365_696893ff_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9993957381, perimeter: 7.3294083714
            with BuildLine():
                Line((-2.8333333333, -5.3125), (-4.4117647059, -2.3529411765))
                Line((-2.8333333333, -5.3125), (-2.3529411765, -4.4117647059))
                CenterArc((0, 0), 5, -151.9275130641, 33.8550261283)
            make_face()
            # Profile area: 748.1770833333, perimeter: 310.9583333333
            with BuildLine():
                Line((0, -10.625), (2.8333333333, -5.3125))
                Line((69, -140), (0, -10.625))
                Line((74.6666666667, -140), (69, -140))
                Line((74.6666666667, -140), (2.8333333333, -5.3125))
            make_face()
            # Profile area: 8.9276167552, perimeter: 15.1164532979
            with BuildLine():
                Line((-2.8333333333, -5.3125), (-2.3529411765, -4.4117647059))
                Line((0, -10.625), (-2.8333333333, -5.3125))
                Line((0, -5), (0, -10.625))
                CenterArc((0, 0), 5, -118.0724869359, 28.0724869359)
            make_face()
            # Profile area: 748.1770833333, perimeter: 310.9583333333
            with BuildLine():
                Line((0, -10.625), (-2.8333333333, -5.3125))
                Line((-74.6666666667, -140), (-2.8333333333, -5.3125))
                Line((-69, -140), (-74.6666666667, -140))
                Line((-69, -140), (0, -10.625))
            make_face()
            # Profile area: 6.1244665782, perimeter: 12.4497866313
            with BuildLine():
                Line((2.3529411765, -4.4117647059), (0, 0))
                Line((0, 0), (0, -5))
                CenterArc((0, 0), 5, -90, 28.0724869359)
            make_face()
            # Profile area: 0.9993957381, perimeter: 7.3294083714
            with BuildLine():
                CenterArc((0, 0), 5, -61.9275130641, 33.8550261283)
                Line((2.8333333333, -5.3125), (2.3529411765, -4.4117647059))
                Line((2.8333333333, -5.3125), (4.4117647059, -2.3529411765))
            make_face()
            # Profile area: 6.1244665782, perimeter: 12.4497866313
            with BuildLine():
                CenterArc((0, 0), 5, -118.0724869359, 28.0724869359)
                Line((0, 0), (0, -5))
                Line((-2.3529411765, -4.4117647059), (0, 0))
            make_face()
            # Profile area: 8.9276167552, perimeter: 15.1164532979
            with BuildLine():
                CenterArc((0, 0), 5, -90, 28.0724869359)
                Line((0, -5), (0, -10.625))
                Line((0, -10.625), (2.8333333333, -5.3125))
                Line((2.8333333333, -5.3125), (2.3529411765, -4.4117647059))
            make_face()
            # Profile area: 66.2908831834, perimeter: 36.5163532734
            with BuildLine():
                CenterArc((0, 0), 5, -28.0724869359, 56.1449738717)
                CenterArc((0, 0), 5, 28.0724869359, 123.8550261283)
                CenterArc((0, 0), 5, 151.9275130641, 56.1449738717)
                CenterArc((0, 0), 5, -151.9275130641, 33.8550261283)
                Line((-2.3529411765, -4.4117647059), (0, 0))
                Line((2.3529411765, -4.4117647059), (0, 0))
                CenterArc((0, 0), 5, -61.9275130641, 33.8550261283)
            make_face()
            # Profile area: 779.365650177, perimeter: 327.8995732625
            with BuildLine():
                Line((-80.3333333333, -140), (-4.4117647059, 2.3529411765))
                Line((-74.6666666667, -140), (-80.3333333333, -140))
                Line((-74.6666666667, -140), (-2.8333333333, -5.3125))
                Line((-2.8333333333, -5.3125), (-4.4117647059, -2.3529411765))
                CenterArc((0, 0), 5, 151.9275130641, 56.1449738717)
            make_face()
            # Profile area: 779.365650177, perimeter: 327.8995732625
            with BuildLine():
                Line((2.8333333333, -5.3125), (4.4117647059, -2.3529411765))
                Line((74.6666666667, -140), (2.8333333333, -5.3125))
                Line((80.3333333333, -140), (74.6666666667, -140))
                Line((80.3333333333, -140), (4.4117647059, 2.3529411765))
                CenterArc((0, 0), 5, -28.0724869359, 56.1449738717)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.25, perimeter: 31.25
            with BuildLine():
                Line((0, 10.625), (-5, 10.625))
                Line((-5, 5), (-5, 10.625))
                Line((5, 5), (-5, 5))
                Line((5, 10.625), (5, 5))
                Line((0, 10.625), (5, 10.625))
            make_face()
        # OneSide extrude, distance=38
        extrude(amount=38, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 43, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3097.2293083469, perimeter: 680.6417233387
            with BuildLine():
                Line((-80.3333333333, 140), (-4.4117647059, -2.3529411765))
                CenterArc((0, 0), 5, -151.9275130641, 123.8550261283)
                Line((4.4117647059, -2.3529411765), (80.3333333333, 140))
                Line((80.3333333333, 140), (69, 140))
                Line((69, 140), (0, 10.625))
                Line((5, 10.625), (0, 10.625))
                Line((5, 5), (5, 10.625))
                Line((-5, 5), (5, 5))
                Line((-5, 10.625), (-5, 5))
                Line((0, 10.625), (-5, 10.625))
                Line((0, 10.625), (-69, 140))
                Line((-80.3333333333, 140), (-69, 140))
            make_face()
            # Profile area: 56.25, perimeter: 31.25
            with BuildLine():
                Line((0, 10.625), (-5, 10.625))
                Line((-5, 10.625), (-5, 5))
                Line((-5, 5), (5, 5))
                Line((5, 5), (5, 10.625))
                Line((5, 10.625), (0, 10.625))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((13.3333333333, 35.625), (24.6666666667, 35.625))
                Line((13.3333333333, 35.625), (10.1333333333, 29.625))
                Line((10.1333333333, 29.625), (21.4666666667, 29.625))
                Line((21.4666666667, 29.625), (24.6666666667, 35.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((-21.4666666667, 29.625), (-10.1333333333, 29.625))
                Line((-10.1333333333, 29.625), (-13.3333333333, 35.625))
                Line((-24.6666666667, 35.625), (-13.3333333333, 35.625))
                Line((-24.6666666667, 35.625), (-21.4666666667, 29.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((26.6666666667, 60.625), (38, 60.625))
                Line((26.6666666667, 60.625), (23.4666666667, 54.625))
                Line((23.4666666667, 54.625), (34.8, 54.625))
                Line((34.8, 54.625), (38, 60.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((40, 85.625), (51.3333333333, 85.625))
                Line((40, 85.625), (36.8, 79.625))
                Line((36.8, 79.625), (48.1333333333, 79.625))
                Line((48.1333333333, 79.625), (51.3333333333, 85.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((53.3333333333, 110.625), (64.6666666667, 110.625))
                Line((53.3333333333, 110.625), (50.1333333333, 104.625))
                Line((50.1333333333, 104.625), (61.4666666667, 104.625))
                Line((61.4666666667, 104.625), (64.6666666667, 110.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((66.6666666667, 135.625), (78, 135.625))
                Line((66.6666666667, 135.625), (63.4666666667, 129.625))
                Line((63.4666666667, 129.625), (74.8, 129.625))
                Line((74.8, 129.625), (78, 135.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((-48.1333333333, 79.625), (-36.8, 79.625))
                Line((-36.8, 79.625), (-40, 85.625))
                Line((-51.3333333333, 85.625), (-40, 85.625))
                Line((-51.3333333333, 85.625), (-48.1333333333, 79.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((-61.4666666667, 104.625), (-50.1333333333, 104.625))
                Line((-50.1333333333, 104.625), (-53.3333333333, 110.625))
                Line((-64.6666666667, 110.625), (-53.3333333333, 110.625))
                Line((-64.6666666667, 110.625), (-61.4666666667, 104.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((-34.8, 54.625), (-23.4666666667, 54.625))
                Line((-23.4666666667, 54.625), (-26.6666666667, 60.625))
                Line((-38, 60.625), (-26.6666666667, 60.625))
                Line((-38, 60.625), (-34.8, 54.625))
            make_face()
            # Profile area: 68, perimeter: 36.2666666667
            with BuildLine():
                Line((-74.8, 129.625), (-63.4666666667, 129.625))
                Line((-63.4666666667, 129.625), (-66.6666666667, 135.625))
                Line((-78, 135.625), (-66.6666666667, 135.625))
                Line((-78, 135.625), (-74.8, 129.625))
            make_face()
        # OneSide extrude, distance=38
        extrude(amount=38, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 140), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 106.6666666667, perimeter: 85.3333333333
            with BuildLine():
                Line((66.5, 50.5), (66.5, 40.5))
                Line((66.5, 40.5), (82.8333333333, 40.5))
                Line((82.8333333333, 40.5), (82.8333333333, 50.5))
                Line((82.8333333333, 50.5), (66.5, 50.5))
            make_face()
            with BuildLine():
                Line((80.3333333333, 48), (69, 48))
                Line((80.3333333333, 43), (80.3333333333, 48))
                Line((69, 43), (80.3333333333, 43))
                Line((69, 48), (69, 43))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 56.6666666667, perimeter: 32.6666666667
            with BuildLine():
                Line((69, 48), (69, 43))
                Line((69, 43), (80.3333333333, 43))
                Line((80.3333333333, 43), (80.3333333333, 48))
                Line((80.3333333333, 48), (69, 48))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 140), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 106.6666666667, perimeter: 85.3333333333
            with BuildLine():
                Line((66.5, 7.5), (66.5, -2.5))
                Line((66.5, -2.5), (82.8333333333, -2.5))
                Line((82.8333333333, -2.5), (82.8333333333, 7.5))
                Line((82.8333333333, 7.5), (66.5, 7.5))
            make_face()
            with BuildLine():
                Line((80.3333333333, 5), (69, 5))
                Line((80.3333333333, 0), (80.3333333333, 5))
                Line((69, 0), (80.3333333333, 0))
                Line((69, 5), (69, 0))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 56.6666666667, perimeter: 32.6666666667
            with BuildLine():
                Line((69, 5), (69, 0))
                Line((69, 0), (80.3333333333, 0))
                Line((80.3333333333, 0), (80.3333333333, 5))
                Line((80.3333333333, 5), (69, 5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 140), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 106.6666666667, perimeter: 85.3333333333
            with BuildLine():
                Line((-82.8333333333, 7.5), (-82.8333333333, -2.5))
                Line((-82.8333333333, -2.5), (-66.5, -2.5))
                Line((-66.5, -2.5), (-66.5, 7.5))
                Line((-66.5, 7.5), (-82.8333333333, 7.5))
            make_face()
            with BuildLine():
                Line((-69, 5), (-80.3333333333, 5))
                Line((-69, 0), (-69, 5))
                Line((-80.3333333333, 0), (-69, 0))
                Line((-80.3333333333, 5), (-80.3333333333, 0))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 56.6666666667, perimeter: 32.6666666667
            with BuildLine():
                Line((-80.3333333333, 5), (-80.3333333333, 0))
                Line((-80.3333333333, 0), (-69, 0))
                Line((-69, 0), (-69, 5))
                Line((-69, 5), (-80.3333333333, 5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch10 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 140), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 106.6666666667, perimeter: 85.3333333333
            with BuildLine():
                Line((-82.8333333333, 50.5), (-82.8333333333, 40.5))
                Line((-82.8333333333, 40.5), (-66.5, 40.5))
                Line((-66.5, 40.5), (-66.5, 50.5))
                Line((-66.5, 50.5), (-82.8333333333, 50.5))
            make_face()
            with BuildLine():
                Line((-69, 48), (-80.3333333333, 48))
                Line((-69, 43), (-69, 48))
                Line((-80.3333333333, 43), (-69, 43))
                Line((-80.3333333333, 48), (-80.3333333333, 43))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 56.6666666667, perimeter: 32.6666666667
            with BuildLine():
                Line((-80.3333333333, 48), (-80.3333333333, 43))
                Line((-80.3333333333, 43), (-69, 43))
                Line((-69, 43), (-69, 48))
                Line((-69, 48), (-80.3333333333, 48))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch11 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            Circle(3.75)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch12 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 48, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            Circle(3.75)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_113355_e82de238_0000": {"func": model_113355_e82de238_0000, "volume": 44.4464684956, "area": 146.4982162162},
    "model_121701_05cb78e4_0000": {"func": model_121701_05cb78e4_0000, "volume": 54191.1071810245, "area": 55133.4897172775},
    "model_122019_3a524981_0000": {"func": model_122019_3a524981_0000, "volume": 0.2195199089, "area": 4.7603999827},
    "model_132294_69821e40_0000": {"func": model_132294_69821e40_0000, "volume": 0.0993026417, "area": 2.5307554747},
    "model_132447_7c00b7da_0000": {"func": model_132447_7c00b7da_0000, "volume": 6640625, "area": 250000},
    "model_134072_a64e5fc0_0000": {"func": model_134072_a64e5fc0_0000, "volume": 494.1019381523, "area": 1052.9875462457},
    "model_134579_efc1d669_0000": {"func": model_134579_efc1d669_0000, "volume": 127.8473276925, "area": 484.4238507269},
    "model_134924_4c5e911a_0000": {"func": model_134924_4c5e911a_0000, "volume": 7800, "area": 3396.443784752},
    "model_138125_431e6a10_0000": {"func": model_138125_431e6a10_0000, "volume": 19.5925425841, "area": 147.5291910126},
    "model_138539_b5a9ff56_0000": {"func": model_138539_b5a9ff56_0000, "volume": 333565.5330000001, "area": 137175.38},
    "model_139750_18e8f39b_0000": {"func": model_139750_18e8f39b_0000, "volume": 422.7135977788, "area": 561.0743715809},
    "model_141845_2c9bd259_0000": {"func": model_141845_2c9bd259_0000, "volume": 35940.8395000816, "area": 23292.2757128929},
    "model_142842_736420da_0000": {"func": model_142842_736420da_0000, "volume": 324.1791961967, "area": 459.0707813738},
    "model_143025_16ccf8cb_0000": {"func": model_143025_16ccf8cb_0000, "volume": 31.7583331745, "area": 174.8046973812},
    "model_143262_9b4e4d19_0000": {"func": model_143262_9b4e4d19_0000, "volume": 7355.5330439179, "area": 4183.5901071583},
    "model_145201_a104c55b_0005": {"func": model_145201_a104c55b_0005, "volume": 349205796.6000000238, "area": 4138268.2000000002},
    "model_21339_4c044144_0000": {"func": model_21339_4c044144_0000, "volume": 9.3489038909, "area": 58.5835940743},
    "model_22062_2d6b3b72_0000": {"func": model_22062_2d6b3b72_0000, "volume": 1083.2841778865, "area": 608.5066880832},
    "model_23325_292b3294_0000": {"func": model_23325_292b3294_0000, "volume": 3954.3516212471, "area": 3450.7488943649},
    "model_23365_696893ff_0000": {"func": model_23365_696893ff_0000, "volume": 62955.6743368995, "area": 34605.0822463826},
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
