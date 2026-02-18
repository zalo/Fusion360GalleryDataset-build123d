"""Batch 003 - passing/06_11to15ops
48 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a TIE Fighter-inspired spaceship model featuring a distinctive angular, elongated fuselage with a pointed nose cone, dual wing-like stabilizers extending from the sides, a ribbed/trussed internal structure, and a stepped base or landing gear configuration.
def model_24861_c05860c8_0005():
    """Model: 1_Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0487223393, perimeter: 8.8897787144
            with BuildLine():
                Line((0.5, 3.02), (0.25, 3.02))
                Line((0.25, 0.3), (0.25, 3.02))
                CenterArc((0.55, 0.3), 0.3, -180, 90)
                Line((0.55, 0), (1.75, 0))
                Line((1.75, 0), (1.75, 0.25))
                Line((1.75, 0.25), (0.55, 0.25))
                CenterArc((0.55, 0.3), 0.05, 180, 90)
                Line((0.5, 0.3), (0.5, 3.02))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0434568719, perimeter: 1.6068583471
            with BuildLine():
                Line((0, 3.02), (0, 2.57))
                Line((0, 3.02), (-0.45, 3.02))
                CenterArc((-0.45, 2.57), 0.45, 0, 90)
            make_face()
            # Profile area: 1.9443976787, perimeter: 6.6812559006
            with BuildLine():
                Line((-2.6, 1.575), (-2.0813999397, 1.5749974167))
                Line((-2.0813999397, 1.5749974167), (-0.7681980515, 2.8881980515))
                CenterArc((-0.45, 2.57), 0.45, 90, 45)
                Line((-2.7, 3.02), (-0.45, 3.02))
                Line((-2.7, 1.475), (-2.7, 3.02))
                CenterArc((-2.6, 1.475), 0.1, 90, 90)
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.45, 2.57)):
                Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.85, 1.17)):
                Circle(0.15)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.198425, perimeter: 2.0874
            with BuildLine():
                Line((-1.189264363, 1.0318563509), (-1.064264363, 0.81535))
                Line((-1.064264363, 0.81535), (-0.3769, 1.2122))
                Line((-0.3769, 1.2122), (-0.5019, 1.4287063509))
                Line((-0.5019, 1.4287063509), (-1.189264363, 1.0318563509))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2888588383, 0.7441229972), x_dir=(1, 0, 0), z_dir=(0, 0.8660254038, 0.5))):
            # Profile area: 0.0116423809, perimeter: 0.671533531
            with BuildLine():
                CenterArc((0.4498993264, -0.1171549747), 0.4, 41.3878157507, 41.4168938003)
                Line((0.75, 0.2796950253), (0.75, 0.1473059594))
                Line((0.75, 0.2796950253), (0.5, 0.2796950253))
            make_face()
            # Profile area: 0.0116423809, perimeter: 0.671533531
            with BuildLine():
                Line((0.5, -0.5140049747), (0.75, -0.5140049747))
                Line((0.75, -0.3816159088), (0.75, -0.5140049747))
                CenterArc((0.4498993264, -0.1171549747), 0.4, -82.8047095509, 41.4168938003)
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.241945281, perimeter: 1.8113998881
            with BuildLine():
                CenterArc((-1.2, 2.15), 0.3, -48.5903778907, 97.1807557815)
                Line((-1.0015686517, 2.375), (-1.3984313483, 2.375))
                CenterArc((-1.2, 2.15), 0.3, 131.4096221093, 97.1807557815)
                Line((-1.0015686517, 1.925), (-1.3984313483, 1.925))
            make_face()
            # Profile area: 0.241945281, perimeter: 1.8113998881
            with BuildLine():
                Line((-1.0015686517, 0.775), (-1.3984313483, 0.775))
                CenterArc((-1.2, 0.55), 0.3, 131.4096221093, 97.1807557815)
                Line((-1.0015686517, 0.325), (-1.3984313483, 0.325))
                CenterArc((-1.2, 0.55), 0.3, -48.5903778907, 97.1807557815)
            make_face()
            # Profile area: 0.0134126148, perimeter: 0.8926990817
            with BuildLine():
                CenterArc((-1.5, 0.25), 0.25, 180, 90)
                Line((-1.75, 0.25), (-1.75, 0))
                Line((-1.75, 0), (-1.5, 0))
            make_face()
            # Profile area: 0.0134126148, perimeter: 0.8926990817
            with BuildLine():
                CenterArc((-1.5, 2.45), 0.25, 90, 90)
                Line((-1.5, 2.7), (-1.75, 2.7))
                Line((-1.75, 2.7), (-1.75, 2.45))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a spherical bearing or ball joint component featuring a main spherical body with a cylindrical post extending from one side and a flat circular flange or mounting base on the opposite end.
def model_25199_39e3c0d3_0005():
    """Model: Part 6 - Spool v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.3834599574, perimeter: 17.8599542357
            Circle(2.8425)
        # OneSide extrude, distance=-2.425
        extrude(amount=-2.425)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.8422956244, perimeter: 11.1212379937
            Circle(1.77)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.425), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 20.6289736355, perimeter: 16.1006623496
            Circle(2.5625)
        # OneSide extrude, distance=-2.25
        extrude(amount=-2.25, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.175), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.0265482457, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.175), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.425), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.4812488302, perimeter: 34.8245548178
            with BuildLine():
                CenterArc((0, 0), 2.8425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.7000000402, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.32
        extrude(amount=-1.32, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.425), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.2546742486, perimeter: 33.4579620135
            with BuildLine():
                CenterArc((0, 0), 2.7000000402, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or mounting clamp with a curved cylindrical body featuring a large central hole, angular flanges on one side, and mesh or textured surface details for grip or ventilation.
def model_25211_336c083f_0001():
    """Model: 4-Stand Collor v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 67.1696883915, perimeter: 36.1353966562
            with BuildLine():
                Line((0, 3.2999999103), (0, -3.2999999103))
                CenterArc((0.5, -3.3), 0.5, 179.9999897263, 90.0000102737)
                Line((0.5, -3.8), (6, -3.8))
                CenterArc((6, 0), 3.8, -90, 180)
                Line((0.5, 3.8), (6, 3.8))
                CenterArc((0.5, 3.3), 0.5, 90, 90.0000102737)
            make_face()
            with BuildLine():
                CenterArc((1, -2.6), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 2.6), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.1
        extrude(amount=1.1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 36.3168110755, perimeter: 21.3628300444
            with Locations((6, 0)):
                Circle(3.4)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.2053084434, perimeter: 13.8230076758
            with Locations((6, 0)):
                Circle(2.2)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.8902652413, perimeter: 28.902652413
            with BuildLine():
                CenterArc((-6, 0), 2.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-6, 0), 2.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((6, -2.9)):
                Circle(0.25)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8246680716, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((1, -2.6), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, -2.6), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.8246680716, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((1, 2.6), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, 2.6), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.8, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((5, 0)):
                Circle(0.4)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hydraulic or pneumatic directional control valve with a cylindrical body, featuring a blue-highlighted port section at the top, a central spool mechanism, and end ports for fluid/air connections.
def model_25335_491efa81_0008():
    """Model: bid v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.1369491158, perimeter: 9.553841332
            with BuildLine():
                CenterArc((0, 0), 0.7, -126.3753822467, 253.3702438224)
                Line((-0.4151511003, -0.5636040843), (-0.7710488643, -0.9195018483))
                CenterArc((0, 0), 1.2, -129.9815365633, 260.3219154162)
                Line((-0.7767925257, 0.914654783), (-0.421220378, 0.5590826353))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0596214093, perimeter: 10.2733952564
            with BuildLine():
                CenterArc((0, 0), 0.7, -126.3753822467, 253.3702438224)
                Line((-0.421220378, 0.5590826353), (-0.7767925257, 0.914654783))
                CenterArc((0, 0), 1.2, 130.3403788529, 99.6780845838)
                Line((-0.7710488643, -0.9195018483), (-0.4151511003, -0.5636040843))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.3823007676, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4.8
        extrude(amount=-4.8, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7015926536, perimeter: 11.0831853072
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.6, -0.6), (0.6, -0.6))
                Line((-0.6, 0.6), (-0.6, -0.6))
                Line((0.6, 0.6), (-0.6, 0.6))
                Line((0.6, -0.6), (0.6, 0.6))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0772566612, perimeter: 2.1424778024
            with BuildLine():
                Line((-0.6, -0.6), (-0.6, 0.0000000063))
                Line((0, -0.6), (-0.6, -0.6))
                CenterArc((0, 0), 0.6, -180, 90)
            make_face()
            # Profile area: 0.0772566612, perimeter: 2.1424777961
            with BuildLine():
                CenterArc((0, 0), 0.6, -90, 90)
                Line((0.6, -0.6), (0, -0.6))
                Line((0.6, 0), (0.6, -0.6))
            make_face()
            # Profile area: 0.0772566612, perimeter: 2.1424777961
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 90)
                Line((0.6, 0.6), (0.6, 0))
                Line((0, 0.6), (0.6, 0.6))
            make_face()
            # Profile area: 0.0772566612, perimeter: 2.1424777835
            with BuildLine():
                Line((-0.6, 0.6), (0, 0.6))
                Line((-0.6, 0.0000000063), (-0.6, 0.6))
                CenterArc((0, 0), 0.6, 90, 89.9999993998)
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a solar panel assembly with a rectangular frame featuring two large radiator fins or heat dissipation surfaces, mounting brackets on the sides, and an angled/tilted orientation typical of spacecraft power systems.
def model_26086_bf892d7f_0021():
    """Model: Tractor_Transmission v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 94.7927830103, perimeter: 48.9150163619
            with BuildLine():
                CenterArc((0, 6), 6, -90, 80.5466377442)
                CenterArc((-17.0307160155, 6.5418399542), 23, -3.8075114305, 46.0363920259)
                Line((0, 0), (0, 22))
            make_face()
        # Symmetric extrude, each_side=9
        extrude(amount=9, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 396, perimeter: 80
            with BuildLine():
                Line((9, 0), (9, 22))
                Line((9, 22), (-9, 22))
                Line((-9, 22), (-9, 0))
                Line((-9, 0), (9, 0))
            make_face()
            # Profile area: 279, perimeter: 148
            with BuildLine():
                Line((9, 0), (12.5, 0))
                Line((12.5, 0), (12.5, 27))
                Line((12.5, 27), (-12.5, 27))
                Line((-12.5, 27), (-12.5, 0))
                Line((-12.5, 0), (-9, 0))
                Line((-9, 22), (-9, 0))
                Line((9, 22), (-9, 22))
                Line((9, 0), (9, 22))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 4.4374351329, perimeter: 10.506643286
            with BuildLine():
                Line((0, 22), (0, 25))
                CenterArc((-17.0307160155, 6.5418399542), 23, 37.5671037065, 4.6617768888)
                Line((1.2, 25), (1.2, 20.5647138952))
                Line((0, 25), (1.2, 25))
            make_face()
            # Profile area: 2.7276912258, perimeter: 8.4856485994
            with BuildLine():
                CenterArc((-17.0307160155, 6.5418399542), 23, 26.7931360186, 8.680863189)
                Line((3.5, 20), (3.5, 16.9095639037))
                Line((1.7, 20), (3.5, 20))
                Line((1.7, 19.8895093219), (1.7, 20))
            make_face()
        # TwoSides offset extrude, full=-15, trim=-3
        extrude(amount=-15, mode=Mode.ADD)
        extrude(sk.sketch, amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.2831853072, perimeter: 15.2831853072
            with BuildLine():
                CenterArc((2.5, 6.5), 2, -90, 180)
                Line((0, 8.5), (2.5, 8.5))
                Line((0, 8.5), (0, 4.5))
                Line((2.5, 4.5), (0, 4.5))
            make_face()
            # Profile area: 3.2838173568, perimeter: 7.5405775484
            with BuildLine():
                Line((0, 17.5023278193), (0, 20.4976721807))
                CenterArc((-0.083534658, 19), 1.5, -86.8075595048, 173.6151190097)
            make_face()
        # OneSide extrude, distance=-25
        extrude(amount=-25, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0.0336109751, 6.5)):
                Circle(1)
        # OneSide extrude, distance=16
        extrude(amount=16, mode=Mode.ADD)
    return part.part


# Description: This is a compact satellite or space probe with a cubic/hexagonal body featuring solar panels on top surfaces, a protruding communication antenna, and an angular, faceted geometric design typical of CubeSat or small satellite architecture.
def model_26086_bf892d7f_0022():
    """Model: Tractor_Clutch_Box v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 740.7831853072, perimeter: 107.2831853072
            with BuildLine():
                CenterArc((-11.5, -11.75), 2, 180, 90)
                Line((11.5, -13.75), (-11.5, -13.75))
                CenterArc((11.5, -11.75), 2, -90, 90)
                Line((13.5, 13.75), (13.5, -11.75))
                Line((-13.5, 13.75), (13.5, 13.75))
                Line((-13.5, -11.75), (-13.5, 13.75))
            make_face()
        # Symmetric extrude, each_side=21.75
        extrude(amount=21.75, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-13.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 24.5006581802, perimeter: 29.399957843
            with BuildLine():
                Line((-5.0025486614, -11.75), (8.858420888, -11.75))
                CenterArc((-2.0076590422, -10.5076590422), 3.2423409578, -157.4703347152, 67.4703347152)
                Line((-2.0076590422, -13.75), (5.9923409578, -13.75))
                CenterArc((5.9923409578, -10.6963964585), 3.0536035415, -90, 69.8159988491)
            make_face()
            # Profile area: 146.3958608829, perimeter: 50.098026609
            with BuildLine():
                CenterArc((5.9923409578, -10.6963964585), 3.0536035415, -20.1840011509, 58.621275801)
                Line((-0.3459547157, 2.2018990625), (8.3841956155, -8.7981009375))
                CenterArc((-2.5, 0.4923409578), 2.75, 38.4372746501, 141.5627253499)
                Line((-5.25, 0.4923409578), (-5.25, -10.5076590422))
                CenterArc((-2.0076590422, -10.5076590422), 3.2423409578, -180, 22.5296652848)
                Line((-5.0025486614, -11.75), (8.858420888, -11.75))
            make_face()
        # TwoSides extrude, along=-5, against=3
        extrude(amount=-5, mode=Mode.ADD)
        extrude(sk.sketch, amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 5.625, perimeter: 12.1478150705
            with BuildLine():
                Line((13.5, -9.7500845185), (13.5, -5.2500845185))
                Line((16, -5.2500845185), (13.5, -9.7500845185))
                Line((13.5, -5.2500845185), (16, -5.2500845185))
            make_face()
        # TwoSides offset extrude, full=-10, trim=-9
        extrude(amount=-10, mode=Mode.ADD)
        extrude(sk.sketch, amount=-9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 5.625, perimeter: 12.1478150705
            with BuildLine():
                Line((13.5, -9.7500845185), (13.5, -5.2500845185))
                Line((16, -5.2500845185), (13.5, -9.7500845185))
                Line((13.5, -5.2500845185), (16, -5.2500845185))
            make_face()
        # TwoSides offset extrude, full=-19, trim=-18
        extrude(amount=-19, mode=Mode.ADD)
        extrude(sk.sketch, amount=-18, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-16.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-2.5, 0.4923409578)):
                Circle(0.8)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-2.0076590422, -10.5076590422)):
                Circle(0.8)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((5.9923409578, -10.6963964585)):
                Circle(0.8)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 48.1604578289, perimeter: 39.5163970228
            with BuildLine():
                Line((1.0365675668, 17.7104512007), (-1.25, 13.75))
                Line((-1.25, 13.75), (16.75, 13.75))
                Line((16.75, 13.75), (3.452658661, 18.5898364423))
                CenterArc((2.7686183744, 16.7104512007), 2, 70, 80)
            make_face()
        # Symmetric extrude, each_side=8
        extrude(amount=8, both=True, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.5249017776, -6.3785426055), x_dir=(-1, 0, 0), z_dir=(0, 0.9396926208, -0.3420201433))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((0, -5)):
                Circle(1.5)
        # OneSide extrude, distance=50
        extrude(amount=50, mode=Mode.ADD)

        # Sketch7 -> Extrude8 (NewBody)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 21.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 25.4861970865, perimeter: 35.1873512437
            with BuildLine():
                Line((8, 13.75), (-8.0008754556, 13.75))
                Line((8, 15.3428001663), (8, 13.75))
                Line((-8.0008754556, 15.3428001663), (8, 15.3428001663))
                Line((-8.0008754556, 13.75), (-8.0008754556, 15.3428001663))
            make_face()
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((13.5, 1.749836299), (13.5, 4.749836299))
                Line((16, 1.749836299), (13.5, 1.749836299))
                Line((16, 4.749836299), (16, 1.749836299))
                Line((13.5, 4.749836299), (16, 4.749836299))
            make_face()
            # Profile area: 10.8149450146, perimeter: 18.5251831618
            with BuildLine():
                Line((-13.5, 5.2581674217), (-13.5, -3.4463161237))
                Line((-15.4809948942, 2.1990846815), (-13.5, 5.2581674217))
                Line((-15.4809948942, -0.0151323175), (-15.4809948942, 2.1990846815))
                Line((-13.5, -3.4463161237), (-15.4809948942, -0.0151323175))
            make_face()
            # Profile area: 542.3071296698, perimeter: 86.1005936221
            with BuildLine():
                Line((8, 13.75), (13.5, 8.25))
                Line((8, 13.75), (-8.0008754556, 13.75))
                Line((-13.5, 5.2581674217), (-8.0008754556, 13.75))
                Line((-13.5, 5.2581674217), (-13.5, -3.4463161237))
                Line((-10, -9.5084939502), (-13.5, -3.4463161237))
                Line((7, -9.5084939502), (-10, -9.5084939502))
                Line((13.5, 1.749836299), (7, -9.5084939502))
                Line((13.5, 1.749836299), (13.5, 4.749836299))
                Line((13.5, 8.25), (13.5, 4.749836299))
            make_face()
        # TwoSides offset extrude, full=10, trim=8
        extrude(amount=10)
        extrude(sk.sketch, amount=8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated container with a solid dark base and a ventilated mesh top section, designed for airflow or filtering applications.
def model_26384_83eddf22_0018():
    """Model: Cylinder Head v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.2347438066, perimeter: 10.7725212092
            Circle(1.7145)
        # OneSide extrude, distance=0.381
        extrude(amount=0.381)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.381, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 9.2347438066, perimeter: 10.7725212092
            Circle(1.7145)
        # OneSide extrude, distance=1.524
        extrude(amount=1.524, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.524, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.4828666476, perimeter: 5.5857517381
            Circle(0.889)
        # OneSide extrude, distance=-1.397
        extrude(amount=-1.397, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.381, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((1.43002, 0)):
                Circle(0.15875)
        # OneSide extrude, distance=-5.2
        extrude(amount=-5.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a streamlined aerospace or marine component with an elongated, tapered body featuring a pointed nose cone at one end, a broader mid-section with angular faceted surfaces, and a stepped rear section, suggesting a shape optimized for aerodynamic or hydrodynamic efficiency.
def model_26768_c4df841f_0011():
    """Model: Pieza 5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23, perimeter: 20.8284271247
            with BuildLine():
                Line((-2, 0), (6, 0))
                Line((6, 0), (6, 2))
                Line((5, 3), (6, 2))
                Line((-1, 3), (5, 3))
                Line((-2, 2), (-1, 3))
                Line((-2, 0), (-2, 2))
            make_face()
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3, perimeter: 7
            with BuildLine():
                Line((2, 1.5), (0, 1.5))
                Line((0, 1.5), (0, 0))
                Line((0, 0), (2, 0))
                Line((2, 0), (2, 1.5))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3, perimeter: 7
            with BuildLine():
                Line((-2, 0), (-2, 1.5))
                Line((0, 0), (-2, 0))
                Line((0, 0), (0, 1.5))
                Line((-2, 1.5), (0, 1.5))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7, mode=Mode.ADD)
    return part.part


# Description: This is a curved brake pad with a dark friction material backing plate featuring ventilation slots and a blue mesh or perforated pattern on the upper surface for heat dissipation.
def model_26942_279de65e_0008():
    """Model: Rear Hub Link v4"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 120.3815597501, perimeter: 56.006605534
            with BuildLine():
                CenterArc((9.75, -2.1898675195), 2.5, -115.3172822949, 179.9999431423)
                CenterArc((0.0000031212, -22.8), 25.3, 64.6826608484, 50.6346956569)
                CenterArc((-9.75, -2.1898704726), 2.5, 115.3173565053, 180)
                CenterArc((0.0000031212, -22.8), 20.3, 64.6826538464, 50.634702659)
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.95, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.4755731997, perimeter: 25.8298868135
            with BuildLine():
                Line((3.2626663161, 2.7639078625), (4.5620071421, -2.0852981167))
                CenterArc((-0.0000031212, 22.8), 20.3, -99.3364174491, 18.5852603143)
                Line((-3.2932931976, 2.7689181402), (-4.5924750557, -2.0796945626))
                CenterArc((-0.0000031212, 22.8), 25.3, -100.4583447299, 20.8465467797)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.95, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.3754828418, perimeter: 25.0969657256
            with BuildLine():
                CenterArc((-9.75, 2.1898675195), 2.5, 64.6827177051, 179.9999431423)
                CenterArc((-0.0000031212, 22.8), 25.3, -115.3173391517, 14.8589944218)
                Line((-4.5924750557, -2.0796945626), (-3.2932931976, 2.7689181402))
                CenterArc((-0.0000031212, 22.8), 20.3, -115.3173461536, 15.9809287045)
            make_face()
            # Profile area: 40.5305037087, perimeter: 25.1595943619
            with BuildLine():
                Line((3.2626663161, 2.7639078625), (4.5620071421, -2.0852981167))
                CenterArc((-0.0000031212, 22.8), 25.3, -79.6117979502, 14.9291544555)
                CenterArc((9.75, 2.1898704726), 2.5, -64.6826434947, 180)
                CenterArc((-0.0000031212, 22.8), 20.3, -80.7511571348, 16.0685136402)
            make_face()
            # Profile area: 39.4755731997, perimeter: 25.8298868135
            with BuildLine():
                Line((-4.5924750557, -2.0796945626), (-3.2932931976, 2.7689181402))
                CenterArc((-0.0000031212, 22.8), 25.3, -100.4583447299, 20.8465467797)
                Line((3.2626663161, 2.7639078625), (4.5620071421, -2.0852981167))
                CenterArc((-0.0000031212, 22.8), 20.3, -99.3364174491, 18.5852603143)
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((9.75, 2.1898704726)):
                Circle(0.95)
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((-9.75, 2.1898675195)):
                Circle(0.95)
        # OneSide extrude, distance=-10.5
        extrude(amount=-10.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((9.75, 2.1898704726)):
                Circle(0.95)
        # TwoSides extrude, along=0.6, against=-4.4
        extrude(amount=0.6, mode=Mode.ADD)
        extrude(sk.sketch, amount=-4.4, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((-9.75, 2.1898675195)):
                Circle(0.95)
        # TwoSides extrude, along=0.6, against=-4.4
        extrude(amount=0.6, mode=Mode.ADD)
        extrude(sk.sketch, amount=-4.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or barrel with a threaded or knurled surface finish, featuring a slightly tapered end on one side and a hollow bore running through its length.
def model_27054_342fcf5c_0000():
    """Model: 22 - Axis v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            Circle(2.25)
        # Symmetric extrude, each_side=3.5
        extrude(amount=3.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.0831853072, perimeter: 14.0831853072
            with BuildLine():
                CenterArc((8, 3.65), 2, -90, 90)
                Line((10, 3.65), (4.1, 3.65))
                CenterArc((6.1, 3.65), 2, 180, 90)
                Line((6.1, 1.65), (8, 1.65))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


# Description: This is a microphone or lavalier mic consisting of a spherical head mounted on top of a long, cylindrical shaft or boom arm.
def model_27694_7801dc67_0001():
    """Model: Small piston holding (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0972653627, perimeter: 1.3280319851
            with BuildLine():
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
                CenterArc((0.5015034115, 0.4999956217), 0.25, -113.5781784782, 47.1563569564)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
                CenterArc((0.5015034115, 0.4999956217), 0.25, 66.4218215218, 47.1563569564)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, -66.4218215218, 132.8436430436)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
            make_face()
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, 113.5781784782, 132.8436430436)
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
            make_face()
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, -66.4218215218, 132.8436430436)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
            make_face()
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, 113.5781784782, 132.8436430436)
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4015034115, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.261825244, perimeter: 2.8853981872
            with BuildLine():
                CenterArc((0.4999956217, -0.5), 0.25, -179.9999982925, 179.9999965849)
                Line((0.1000000015, -0.5000000075), (0.2499956217, -0.5000000075))
                Line((0.1000000015, -0.9000000134), (0.1000000015, -0.5000000075))
                Line((1.0000000149, -0.9000000134), (0.1000000015, -0.9000000134))
                Line((1.0000000149, -0.5000000075), (1.0000000149, -0.9000000134))
                Line((0.7499956217, -0.5000000075), (1.0000000149, -0.5000000075))
            make_face()
            # Profile area: 0.0245436945, perimeter: 0.6426990891
            with BuildLine():
                CenterArc((0.4999956217, -0.5), 0.125, -0.0000034151, 180.0000034151)
                Line((0.3749956217, -0.5000000075), (0.6249956217, -0.5000000075))
            make_face()
            # Profile area: 0.0245436907, perimeter: 0.6426990668
            with BuildLine():
                Line((0.3749956217, -0.5000000075), (0.6249956217, -0.5000000075))
                CenterArc((0.4999956217, -0.5), 0.125, -179.9999965849, 179.9999931698)
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                Line((0.3750000075, 2.5000000373), (0.6250000075, 2.5000000373))
                CenterArc((0.5000000075, 2.5000000373), 0.125, 0, 180)
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                CenterArc((0.5000000075, 2.5000000373), 0.125, 180, 180)
                Line((0.3750000075, 2.5000000373), (0.6250000075, 2.5000000373))
            make_face()
            # Profile area: 0.2597158337, perimeter: 3.3640159598
            with BuildLine():
                Line((0.7291244065, 2.6000100857), (0.7291244065, 2.8))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 0, 23.580691198)
                Line((0.7500000075, 2.5000000373), (1.0000000149, 2.5000000373))
                Line((1.0000000149, 2.5000000373), (1.0000000149, 2.9000000432))
                Line((1.0000000149, 2.9000000432), (0, 2.9000000432))
                Line((0, 2.9000000432), (0, 2.5000000373))
                Line((0, 2.5000000373), (0.2500000075, 2.5000000373))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 156.4243344941, 23.5756655059)
                Line((0.270866837, 2.8), (0.270866837, 2.5999899877))
                Line((0.7291244065, 2.8), (0.270866837, 2.8))
            make_face()
            # Profile area: 0.0421094078, perimeter: 1.4378972377
            with BuildLine():
                Line((0.7291244065, 2.8), (0.270866837, 2.8))
                Line((0.270866837, 2.8), (0.270866837, 2.5999899877))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 23.580691198, 132.8436432961)
                Line((0.7291244065, 2.6000100857), (0.7291244065, 2.8))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4015034115, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.261825244, perimeter: 2.8853981872
            with BuildLine():
                CenterArc((0.4999956217, -0.5), 0.25, -179.9999982925, 179.9999965849)
                Line((0.1000000015, -0.5000000075), (0.2499956217, -0.5000000075))
                Line((0.1000000015, -0.9000000134), (0.1000000015, -0.5000000075))
                Line((1.0000000149, -0.9000000134), (0.1000000015, -0.9000000134))
                Line((1.0000000149, -0.5000000075), (1.0000000149, -0.9000000134))
                Line((0.7499956217, -0.5000000075), (1.0000000149, -0.5000000075))
            make_face()
            # Profile area: 0.0245436945, perimeter: 0.6426990891
            with BuildLine():
                CenterArc((0.4999956217, -0.5), 0.125, -0.0000034151, 180.0000034151)
                Line((0.3749956217, -0.5000000075), (0.6249956217, -0.5000000075))
            make_face()
            # Profile area: 0.0245436907, perimeter: 0.6426990668
            with BuildLine():
                Line((0.3749956217, -0.5000000075), (0.6249956217, -0.5000000075))
                CenterArc((0.4999956217, -0.5), 0.125, -179.9999965849, 179.9999931698)
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                Line((0.3750000075, 2.5000000373), (0.6250000075, 2.5000000373))
                CenterArc((0.5000000075, 2.5000000373), 0.125, 0, 180)
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                CenterArc((0.5000000075, 2.5000000373), 0.125, 180, 180)
                Line((0.3750000075, 2.5000000373), (0.6250000075, 2.5000000373))
            make_face()
            # Profile area: 0.2597158337, perimeter: 3.3640159598
            with BuildLine():
                Line((0.7291244065, 2.6000100857), (0.7291244065, 2.8))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 0, 23.580691198)
                Line((0.7500000075, 2.5000000373), (1.0000000149, 2.5000000373))
                Line((1.0000000149, 2.5000000373), (1.0000000149, 2.9000000432))
                Line((1.0000000149, 2.9000000432), (0, 2.9000000432))
                Line((0, 2.9000000432), (0, 2.5000000373))
                Line((0, 2.5000000373), (0.2500000075, 2.5000000373))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 156.4243344941, 23.5756655059)
                Line((0.270866837, 2.8), (0.270866837, 2.5999899877))
                Line((0.7291244065, 2.8), (0.270866837, 2.8))
            make_face()
            # Profile area: 0.0421094078, perimeter: 1.4378972377
            with BuildLine():
                Line((0.7291244065, 2.8), (0.270866837, 2.8))
                Line((0.270866837, 2.8), (0.270866837, 2.5999899877))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 23.580691198, 132.8436432961)
                Line((0.7291244065, 2.6000100857), (0.7291244065, 2.8))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, -66.4218215218, 132.8436430436)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
            make_face()
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, 113.5781784782, 132.8436430436)
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
            make_face()
            # Profile area: 0.0972653627, perimeter: 1.3280319851
            with BuildLine():
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
                CenterArc((0.5015034115, 0.4999956217), 0.25, -113.5781784782, 47.1563569564)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
                CenterArc((0.5015034115, 0.4999956217), 0.25, 66.4218215218, 47.1563569564)
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch3 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0036504949, perimeter: 6.7707964043
            with BuildLine():
                Line((-0.200000003, -1.5000000224), (-0.200000003, 0.5000000075))
                Line((-0.200000003, 0.5000000075), (-0.8000000119, 0.5000000075))
                Line((-0.8000000119, 0.5000000075), (-0.8000000119, -1.5000000224))
                Line((-0.8000000119, -1.5000000224), (-0.200000003, -1.5000000224))
            make_face()
            with BuildLine():
                CenterArc((-0.5015034115, -0.4999956217), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5015034115, -0.4999956217)):
                Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8000000119, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8600169443, perimeter: 12.0891891308
            with BuildLine():
                Line((0.1950610559, 7), (-0.1667999285, 7.5933333744))
                CenterArc((0.5000000075, 8), 0.7810249029, -31.3780972278, 242.7561944556)
                Line((0.804938959, 7), (1.1667999434, 7.5933333744))
                Line((0.804938959, 7), (1.5000000224, 7))
                Line((1.5000000224, 7), (1.5000000224, 9))
                Line((1.5000000224, 9), (-0.5000000075, 9))
                Line((-0.5000000075, 9), (-0.5000000075, 7))
                Line((-0.5000000075, 7), (0.1950610559, 7))
            make_face()
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.5000000075, 8)):
                Circle(0.25)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0036504949, perimeter: 6.7707964043
            with BuildLine():
                Line((-0.200000003, -1.5000000224), (-0.200000003, 0.5000000075))
                Line((-0.200000003, 0.5000000075), (-0.8000000119, 0.5000000075))
                Line((-0.8000000119, 0.5000000075), (-0.8000000119, -1.5000000224))
                Line((-0.8000000119, -1.5000000224), (-0.200000003, -1.5000000224))
            make_face()
            with BuildLine():
                CenterArc((-0.5015034115, -0.4999956217), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5015034115, -0.4999956217)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: A spherical head mounted on a long, cylindrical shaft, resembling a lollipop or ball-shaped object on a stick with a tapered or rounded connection point between the head and handle.
def model_27694_7801dc67_0004():
    """Model: Large piston holding 33"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0972653627, perimeter: 1.3280319851
            with BuildLine():
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
                CenterArc((0.5015034115, 0.4999956217), 0.25, -113.5781784782, 47.1563569564)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
                CenterArc((0.5015034115, 0.4999956217), 0.25, 66.4218215218, 47.1563569564)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, 113.5781784782, 132.8436430436)
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
            make_face()
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, -66.4218215218, 132.8436430436)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
            make_face()
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, 113.5781784782, 132.8436430436)
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
            make_face()
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, -66.4218215218, 132.8436430436)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4015034115, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.261825244, perimeter: 2.8853981872
            with BuildLine():
                CenterArc((0.4999956217, -0.5), 0.25, -179.9999982925, 179.9999965849)
                Line((0.1000000015, -0.5000000075), (0.2499956217, -0.5000000075))
                Line((0.1000000015, -0.9000000134), (0.1000000015, -0.5000000075))
                Line((1.0000000149, -0.9000000134), (0.1000000015, -0.9000000134))
                Line((1.0000000149, -0.5000000075), (1.0000000149, -0.9000000134))
                Line((0.7499956217, -0.5000000075), (1.0000000149, -0.5000000075))
            make_face()
            # Profile area: 0.0245436945, perimeter: 0.6426990891
            with BuildLine():
                CenterArc((0.4999956217, -0.5), 0.125, -0.0000034151, 180.0000034151)
                Line((0.3749956217, -0.5000000075), (0.6249956217, -0.5000000075))
            make_face()
            # Profile area: 0.0245436907, perimeter: 0.6426990668
            with BuildLine():
                Line((0.3749956217, -0.5000000075), (0.6249956217, -0.5000000075))
                CenterArc((0.4999956217, -0.5), 0.125, -179.9999965849, 179.9999931698)
            make_face()
            # Profile area: 0.2597158337, perimeter: 3.3640159598
            with BuildLine():
                CenterArc((0.5000000075, 2.5000000373), 0.25, 0, 23.580691198)
                Line((0.7500000075, 2.5000000373), (1.0000000149, 2.5000000373))
                Line((1.0000000149, 2.5000000373), (1.0000000149, 2.9000000432))
                Line((1.0000000149, 2.9000000432), (0, 2.9000000432))
                Line((0, 2.9000000432), (0, 2.5000000373))
                Line((0, 2.5000000373), (0.2500000075, 2.5000000373))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 156.4243344941, 23.5756655059)
                Line((0.270866837, 2.8), (0.270866837, 2.5999899877))
                Line((0.7291244065, 2.8), (0.270866837, 2.8))
                Line((0.7291244065, 2.6000100857), (0.7291244065, 2.8))
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                Line((0.3750000075, 2.5000000373), (0.6250000075, 2.5000000373))
                CenterArc((0.5000000075, 2.5000000373), 0.125, 180, 180)
            make_face()
            # Profile area: 0.0421094078, perimeter: 1.4378972377
            with BuildLine():
                Line((0.7291244065, 2.6000100857), (0.7291244065, 2.8))
                Line((0.7291244065, 2.8), (0.270866837, 2.8))
                Line((0.270866837, 2.8), (0.270866837, 2.5999899877))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 23.580691198, 132.8436432961)
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                CenterArc((0.5000000075, 2.5000000373), 0.125, 0, 180)
                Line((0.3750000075, 2.5000000373), (0.6250000075, 2.5000000373))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4015034115, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.261825244, perimeter: 2.8853981872
            with BuildLine():
                CenterArc((0.4999956217, -0.5), 0.25, -179.9999982925, 179.9999965849)
                Line((0.1000000015, -0.5000000075), (0.2499956217, -0.5000000075))
                Line((0.1000000015, -0.9000000134), (0.1000000015, -0.5000000075))
                Line((1.0000000149, -0.9000000134), (0.1000000015, -0.9000000134))
                Line((1.0000000149, -0.5000000075), (1.0000000149, -0.9000000134))
                Line((0.7499956217, -0.5000000075), (1.0000000149, -0.5000000075))
            make_face()
            # Profile area: 0.0245436945, perimeter: 0.6426990891
            with BuildLine():
                CenterArc((0.4999956217, -0.5), 0.125, -0.0000034151, 180.0000034151)
                Line((0.3749956217, -0.5000000075), (0.6249956217, -0.5000000075))
            make_face()
            # Profile area: 0.0245436907, perimeter: 0.6426990668
            with BuildLine():
                Line((0.3749956217, -0.5000000075), (0.6249956217, -0.5000000075))
                CenterArc((0.4999956217, -0.5), 0.125, -179.9999965849, 179.9999931698)
            make_face()
            # Profile area: 0.2597158337, perimeter: 3.3640159598
            with BuildLine():
                CenterArc((0.5000000075, 2.5000000373), 0.25, 0, 23.580691198)
                Line((0.7500000075, 2.5000000373), (1.0000000149, 2.5000000373))
                Line((1.0000000149, 2.5000000373), (1.0000000149, 2.9000000432))
                Line((1.0000000149, 2.9000000432), (0, 2.9000000432))
                Line((0, 2.9000000432), (0, 2.5000000373))
                Line((0, 2.5000000373), (0.2500000075, 2.5000000373))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 156.4243344941, 23.5756655059)
                Line((0.270866837, 2.8), (0.270866837, 2.5999899877))
                Line((0.7291244065, 2.8), (0.270866837, 2.8))
                Line((0.7291244065, 2.6000100857), (0.7291244065, 2.8))
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                Line((0.3750000075, 2.5000000373), (0.6250000075, 2.5000000373))
                CenterArc((0.5000000075, 2.5000000373), 0.125, 180, 180)
            make_face()
            # Profile area: 0.0421094078, perimeter: 1.4378972377
            with BuildLine():
                Line((0.7291244065, 2.6000100857), (0.7291244065, 2.8))
                Line((0.7291244065, 2.8), (0.270866837, 2.8))
                Line((0.270866837, 2.8), (0.270866837, 2.5999899877))
                CenterArc((0.5000000075, 2.5000000373), 0.25, 23.580691198, 132.8436432961)
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                CenterArc((0.5000000075, 2.5000000373), 0.125, 0, 180)
                Line((0.3750000075, 2.5000000373), (0.6250000075, 2.5000000373))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0972653627, perimeter: 1.3280319851
            with BuildLine():
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
                CenterArc((0.5015034115, 0.4999956217), 0.25, -113.5781784782, 47.1563569564)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
                CenterArc((0.5015034115, 0.4999956217), 0.25, 66.4218215218, 47.1563569564)
            make_face()
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, 113.5781784782, 132.8436430436)
                Line((0.4015034115, 0.7291244065), (0.4015034115, 0.270866837))
            make_face()
            # Profile area: 0.0495420891, perimeter: 1.0378973099
            with BuildLine():
                CenterArc((0.5015034115, 0.4999956217), 0.25, -66.4218215218, 132.8436430436)
                Line((0.6015034115, 0.7291244065), (0.6015034115, 0.270866837))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch3 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0036504949, perimeter: 6.7707964043
            with BuildLine():
                Line((-0.200000003, -1.5000000224), (-0.200000003, 0.5000000075))
                Line((-0.200000003, 0.5000000075), (-0.8000000119, 0.5000000075))
                Line((-0.8000000119, 0.5000000075), (-0.8000000119, -1.5000000224))
                Line((-0.8000000119, -1.5000000224), (-0.200000003, -1.5000000224))
            make_face()
            with BuildLine():
                CenterArc((-0.5015034115, -0.4999956217), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5015034115, -0.4999956217)):
                Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8000000119, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8600169443, perimeter: 12.0891891308
            with BuildLine():
                Line((0.1950610559, 7), (-0.1667999285, 7.5933333744))
                CenterArc((0.5000000075, 8), 0.7810249029, -31.3780972278, 242.7561944556)
                Line((0.804938959, 7), (1.1667999434, 7.5933333744))
                Line((0.804938959, 7), (1.5000000224, 7))
                Line((1.5000000224, 7), (1.5000000224, 9))
                Line((1.5000000224, 9), (-0.5000000075, 9))
                Line((-0.5000000075, 9), (-0.5000000075, 7))
                Line((-0.5000000075, 7), (0.1950610559, 7))
            make_face()
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.5000000075, 8)):
                Circle(0.25)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical bearing or bushing component with a hollow center bore, featuring a ribbed or grooved outer surface and a mesh-textured upper flange or retaining ring.
def model_27725_5cceaeb7_0010():
    """Model: Motor Cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 136.3820610728, perimeter: 41.3984000245
            Circle(6.58876)
        # OneSide extrude, distance=5.715
        extrude(amount=5.715)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.715, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.8272998334, perimeter: 80.801888714
            with BuildLine():
                CenterArc((0, 0), 6.58876, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.27126, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.175
        extrude(amount=-3.175, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.715, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 91.8855437959, perimeter: 59.3526020398
            with BuildLine():
                CenterArc((0, 0), 6.27126, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.5875
        extrude(amount=-1.5875, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.1275, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.6384374105, perimeter: 48.8753277082
            with BuildLine():
                CenterArc((0, 0), 4.1275, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.65125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.238125
        extrude(amount=-0.238125, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.715, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3949845692, perimeter: 5.4860061713
            Circle(0.873125)
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.1275, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6781637899, perimeter: 3.803780582
            with BuildLine():
                CenterArc((0, -4.6244117729), 0.1905, 3.7167917409, 172.5664165182)
                Line((-0.1900993143, -4.612062655), (-0.2768395183, -5.9473202385))
                CenterArc((0, 0), 5.95376, -92.6651153748, 5.3302307496)
                Line((0.1900993143, -4.612062655), (0.2768395183, -5.9473202385))
            make_face()
        # OneSide extrude, distance=-2.44475
        extrude(amount=-2.44475, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular sheet metal bracket or deflector with a flat central panel and angled vertical flanges on both ends, featuring a curved or wrapped geometry with small holes or mounting points along the top surface.
def model_27839_4a077326_0000():
    """Model: Blokada"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5, perimeter: 9
            with BuildLine():
                Line((3.9879232523, 5.5995020954), (3.9879232523, 8.0995020954))
                Line((3.9879232523, 8.0995020954), (1.9879232523, 8.0995020954))
                Line((1.9879232523, 8.0995020954), (1.9879232523, 5.5995020954))
                Line((1.9879232523, 5.5995020954), (3.9879232523, 5.5995020954))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5995020954, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8.64, perimeter: 16.8
            with BuildLine():
                Line((0.4, -2.3879232523), (0.4, -3.5879232523))
                Line((0.4, -3.5879232523), (7.6, -3.5879232523))
                Line((7.6, -3.5879232523), (7.6, -2.3879232523))
                Line((7.6, -2.3879232523), (0.4, -2.3879232523))
            make_face()
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.9879232523), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.12, perimeter: 18.6
            with BuildLine():
                Line((7.6, 5.5995020954), (7.6, 7.6995020954))
                Line((7.6, 7.6995020954), (0.4, 7.6995020954))
                Line((0.4, 7.6995020954), (0.4, 5.5995020954))
                Line((0.4, 5.5995020954), (7.6, 5.5995020954))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.9879232523), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-6.5, 6.8495020954)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-3.5, 6.8495020954)):
                Circle(0.4)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.6, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.0978249525, perimeter: 4.4450061807
            with BuildLine():
                Line((-2.6579232523, 5.5995020954), (-2.6579232523, 6.6234490043))
                CenterArc((-2.9879232523, 6.8495020954), 0.4, -34.4115086698, 248.8230173395)
                Line((-3.3179232523, 5.5995020954), (-3.3179232523, 6.6234490043))
                Line((-2.6579232523, 5.5995020954), (-3.3179232523, 5.5995020954))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6649110643, perimeter: 9.5455538843
            with BuildLine():
                Line((2.6579232523, 5.5995020954), (2.6579232523, 6.6234490043))
                CenterArc((2.9879232523, 6.8495020954), 0.4, -34.4115086698, 248.8230173395)
                Line((3.3179232523, 6.6234490043), (3.3179232523, 5.5995020954))
                Line((3.3179232523, 5.5995020954), (3.6179232523, 5.5995020954))
                Line((3.6179232523, 6.3266693921), (3.6179232523, 5.5995020954))
                CenterArc((2.9879232523, 6.8495020954), 0.8186904394, -39.6890490956, 259.3780981912)
                Line((2.3579232523, 6.3266693921), (2.3579232523, 5.5995020954))
                Line((2.3579232523, 5.5995020954), (2.6579232523, 5.5995020954))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.5879232523), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((5, 6.8495020954)):
                Circle(0.4)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stamped or cast metal bracket with an angular, L-shaped profile featuring multiple internal reinforcing ribs, mounting flanges, and cutout slots for fastening and assembly.
def model_28446_d757d32d_0009():
    """Model: trzymanieDrzwiZamrazalnika v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((3, -2), (0, -2))
                Line((3, 0), (3, -2))
                Line((0, 0), (3, 0))
                Line((0, -2), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8, perimeter: 4.8
            with BuildLine():
                Line((-0.5, 1.5), (-2.5, 1.5))
                Line((-2.5, 1.1), (-2.5, 1.5))
                Line((-0.5, 1.1), (-2.5, 1.1))
                Line((-0.5, 1.1), (-0.5, 1.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((-1.5000000224, 2.0000000298), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5000000224, 2.0000000298), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.5000000075, 0.5000000075)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.5000000373, 0.5000000075)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-1.5000000224, 1.75)):
                Circle(0.1)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on Profile plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((1.5000000224, -1.75), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5000000224, -1.75), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0.5000000075, -0.5000000075), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.5000000075, -0.5000000075), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((2.5000000373, -0.5000000075), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5000000373, -0.5000000075), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: A cylindrical filter or strainer component with a mesh or perforated top surface and an O-ring seal displayed separately to the left.
def model_28870_da6bdb2e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with Locations((0, 10)):
                Circle(3.5)
        # OneSide extrude, distance=13
        extrude(amount=13)

        # Sketch2 -> 押し出し2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 74.6128255228, perimeter: 59.6902604182
            with BuildLine():
                CenterArc((0, 10), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 10), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch6 -> 押し出し3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.5504416669, perimeter: 47.7522083346
            with BuildLine():
                CenterArc((0, 35), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 35), 3.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)
    return part.part


# Description: This is a bracket or mounting assembly featuring an L-shaped base with a vertical rectangular box section and an angled flange, designed to support or position components with multiple attachment points and internal structural geometry.
def model_28879_7c56f134_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((8, -8), (0, -8))
                Line((8, 0), (8, -8))
                Line((0, 0), (8, 0))
                Line((0, -8), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9937597915, perimeter: 8.450078332
            with BuildLine():
                Line((-2.4678191998, 4), (-6.4428583658, 4))
                Line((-6.4428583658, 3.75), (-6.4428583658, 4))
                Line((-2.4678191998, 3.75), (-6.4428583658, 3.75))
                Line((-2.4678191998, 4), (-2.4678191998, 3.75))
            make_face()
            # Profile area: 0.9937597915, perimeter: 8.450078332
            with BuildLine():
                Line((-2.4678191998, 4.25), (-2.4678191998, 4))
                Line((-6.4428583658, 4.25), (-2.4678191998, 4.25))
                Line((-6.4428583658, 4), (-6.4428583658, 4.25))
                Line((-2.4678191998, 4), (-6.4428583658, 4))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9943180213, perimeter: 9
            with BuildLine():
                Line((-2.4905471148, 4.25), (-2.4678191998, 4.25))
                Line((-2.4678191998, 4.25), (-2.4678191998, 4))
                Line((-1.9905471148, 4), (-2.4678191998, 4))
                Line((-1.9905471148, 8), (-1.9905471148, 4))
                Line((-2.4905471148, 8), (-1.9905471148, 8))
                Line((-2.4905471148, 4.25), (-2.4905471148, 8))
            make_face()
            # Profile area: 1.875, perimeter: 8.5
            with BuildLine():
                Line((-2.4905471148, 4.25), (-2.4905471148, 8))
                Line((-2.4905471148, 8), (-2.9905471148, 8))
                Line((-2.9905471148, 8), (-2.9905471148, 4.25))
                Line((-2.9905471148, 4.25), (-2.4905471148, 4.25))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5, mode=Mode.ADD)
    return part.part


# Description: This is a projector mount bracket featuring a rectangular base platform with an angled arm extending upward to support a cylindrical projector head, designed for ceiling or wall mounting.
def model_28896_5698192a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12, perimeter: 19
            with BuildLine():
                Line((3, 0), (-5, 0))
                Line((3, 1.5), (3, 0))
                Line((-5, 1.5), (3, 1.5))
                Line((-5, 0), (-5, 1.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch8 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5, perimeter: 15
            with BuildLine():
                Line((0, 1.5), (0, 0.5))
                Line((-6.5, 1.5), (0, 1.5))
                Line((-6.5, 0.5), (-6.5, 1.5))
                Line((0, 0.5), (-6.5, 0.5))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)

        # Sketch9 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.7367424424, perimeter: 11.1858688007
            with BuildLine():
                Line((4, 3.5), (5.5, 3.5))
                Line((5.5, 3.5), (6.5, 1.5265151151))
                Line((6.5, 1.5265151151), (6.5, 5))
                Line((6.5, 5), (4, 5))
                Line((4, 5), (4, 3.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 5.3296977755, perimeter: 14.289229088
            with BuildLine():
                Line((1.5, 5), (0.5, 5))
                Line((1.5, 5), (1.5, 5.0857864376))
                CenterArc((1, 6.5), 1.5, -70.5287793655, 321.057558731)
                Line((0.5, 5), (0.5, 5.0857864376))
            make_face()
            with BuildLine():
                CenterArc((1, 6.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)
    return part.part


# Description: This is a centrifugal pump impeller featuring a circular disk base with radial vanes/blades extending outward, a central boss with a shaft mounting hole on top, and a curved inlet shroud, designed to move fluid through rotational motion.
def model_28924_34ec542a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.1972213807, perimeter: 22.19384624
            with Locations((2.5, -1.5)):
                Circle(3.5322603353)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4031312695, perimeter: 11.9706296282
            with Locations((-2.5, 1.5)):
                Circle(1.9051848773)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.7720965923, perimeter: 11.6346963034
            with Locations((-2.5, 1.5)):
                Circle(1.8517194281)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-2.5, 1.5)):
                Circle(0.75)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4313881528, perimeter: 4.2411500823
            with Locations((-2.5, 1.5)):
                Circle(0.675)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.4999907524, 0.3332322726)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0385691774, perimeter: 3.3749940003
            with BuildLine():
                Line((-2.6037166436, 0.6154754236), (-2.7962834369, 0.3845245913))
                Line((-2.7962834369, 0.3845245913), (-2.6925575457, 0.1022814403))
                Line((-2.6925575457, 0.1022814403), (-2.3962648613, 0.0509891215))
                Line((-2.3962648613, 0.0509891215), (-2.203698068, 0.2819399538))
                Line((-2.203698068, 0.2819399538), (-2.3074239592, 0.5641831049))
                Line((-2.3074239592, 0.5641831049), (-2.6037166436, 0.6154754236))
            make_face()
            with BuildLine():
                CenterArc((-2.4999907524, 0.3332322726), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


# Description: This is a dual wheel assembly consisting of two dark gray cylindrical wheels with textured treads mounted side-by-side on a common axle, featuring a grooved tire pattern around the outer circumference of each wheel.
def model_29184_9d7cf184_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 69.9004365424, perimeter: 29.6377258186
            with Locations((-5, 2.5)):
                Circle(4.716990566)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1263448606, perimeter: 1.4635262373
            with BuildLine():
                CenterArc((-5, 2.5), 4.716990566, 87.6604994767, 4.6129422782)
                Line((-4.8902973071, 7.6373247701), (-4.807449418, 7.2130589083))
                Line((-5.1109396011, 7.6373247701), (-4.8902973071, 7.6373247701))
                Line((-5.1871165669, 7.2132777756), (-5.1109396011, 7.6373247701))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 42.2574064422, perimeter: 23.0439196005
            with Locations((4, 3)):
                Circle(3.6675537126)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0718774246, perimeter: 1.1083145886
            with BuildLine():
                Line((0.3347236124, 3.1292255297), (0.0019731893, 3.0726521585))
                Line((0.0019731893, 3.0726521585), (0.0019731893, 2.9068269586))
                Line((0.0019731893, 2.9068269586), (0.3350952654, 2.8606317063))
                CenterArc((4, 3), 3.6675537126, 177.9807765849, 4.1970069491)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch8 -> Extrude7 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2944856756, perimeter: 1.9236985574
            with Locations((-5, 2.5)):
                Circle(0.3061661344)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch9 -> Extrude8 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7736558351, perimeter: 5.5873936991
            with BuildLine():
                CenterArc((-5, 2.5), 0.5830951918, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, 2.5), 0.3061661344, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2944856756, perimeter: 1.9236985574
            with Locations((-5, 2.5)):
                Circle(0.3061661344)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a composite bracket or support arm featuring an angular, bent configuration with two perpendicular sections connected by a curved transitional joint, incorporating ribbed reinforcement patterns on its internal surfaces for structural stiffness.
def model_29726_73b01e1f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.4908627684, perimeter: 37.7002075382
            with BuildLine():
                Line((0.5, 5.8), (-1.5, 4.3))
                Line((-1.5, 4.3), (-6.6360297657, 4.3))
                Line((-6.6360297657, 4.3), (-7, 3.3))
                Line((-7, 3.3), (-1.3847680763, 3.3))
                Line((-1.3847680763, 3.3), (0.6152319237, 4.8))
                Line((0.6152319237, 4.8), (10.5, 4.8))
                Line((10.5, 4.8), (10.5, 5.8))
                Line((10.5, 5.8), (0.5, 5.8))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7)

        # Sketch3 -> 押し出し2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.0175605987, perimeter: 15.4685041199
            with BuildLine():
                CenterArc((0, 0), 4, 171.1523303946, 98.8476696054)
                Line((0, 0.6152319237), (0, -4))
                Line((0, 0.6152319237), (-3.952403026, 0.6152319237))
            make_face()
            # Profile area: 10.11518063, perimeter: 13.0026725465
            with BuildLine():
                Line((0, 0.6152319237), (-3.952403026, 0.6152319237))
                Line((0, 4), (0, 0.6152319237))
                CenterArc((0, 0), 4, 90, 81.1523303946)
            make_face()
        # OneSide extrude, distance=8.5
        extrude(amount=8.5, mode=Mode.SUBTRACT)

        # Sketch3 -> 押し出し3 (Intersect)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4115661718, perimeter: 14.5179592802
            with BuildLine():
                CenterArc((0, 0), 4, 171.1523303946, 98.8476696054)
                Line((-3.952403026, 0.6152319237), (-4.1546948961, 0.6152319237))
                CenterArc((0, 0), 4.2, 171.5767882885, 98.4232117115)
                Line((0, -4), (0, -4.2))
            make_face()
            # Profile area: 1.1645398041, perimeter: 12.0476842195
            with BuildLine():
                CenterArc((0, 0), 4, 90, 81.1523303946)
                Line((0, 4.2), (0, 4))
                CenterArc((0, 0), 4.2, 90, 81.5767882885)
                Line((-3.952403026, 0.6152319237), (-4.1546948961, 0.6152319237))
            make_face()
            # Profile area: 29.2632861866, perimeter: 25.4944189721
            with BuildLine():
                Line((-4.1546948961, 0.6152319237), (-6.0177279883, 0.6152319237))
                Line((-6, 0.5), (-6.0177279883, 0.6152319237))
                Line((-6, -7), (-6, 0.5))
                Line((0, -7), (-6, -7))
                Line((0, -4.2), (0, -7))
                CenterArc((0, 0), 4.2, 171.5767882885, 98.4232117115)
            make_face()
            # Profile area: 30.2778666087, perimeter: 24.1028095762
            with BuildLine():
                CenterArc((0, 0), 4.2, 90, 81.5767882885)
                Line((0, 7), (0, 4.2))
                Line((-7, 7), (0, 7))
                Line((-6.0177279883, 0.6152319237), (-7, 7))
                Line((-4.1546948961, 0.6152319237), (-6.0177279883, 0.6152319237))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.INTERSECT)

        # Sketch4 -> 押し出し4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 5.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 54.2298911143, perimeter: 26.4766012501
            with BuildLine():
                CenterArc((0, 0), 4, -90, 82.8192442185)
                Line((4.1701318924, -0.5), (3.9686269666, -0.5))
                CenterArc((0, 0), 4.2, -6.8371411681, 276.8371411681)
                Line((0, -4), (0, -4.2))
            make_face()
            # Profile area: 1.1878032951, perimeter: 12.2795348567
            with BuildLine():
                Line((0, -4), (0, -4.2))
                CenterArc((0, 0), 4.2, -90, 83.1628588319)
                Line((4.1701318924, -0.5), (3.9686269666, -0.5))
                CenterArc((0, 0), 4, -90, 82.8192442185)
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mounting bracket or adapter featuring a hexagonal base with a cylindrical tube extending upward at an angle, designed to attach or position components in an angled orientation.
def model_30400_8824ce97_0000():
    """Model: 18-03-001002"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4635829324, perimeter: 4.5033320997
            with BuildLine():
                Line((0.375277675, 0.65), (-0.375277675, 0.65))
                Line((-0.375277675, 0.65), (-0.7505553499, 0))
                Line((-0.7505553499, 0), (-0.375277675, -0.65))
                Line((-0.375277675, -0.65), (0.375277675, -0.65))
                Line((0.375277675, -0.65), (0.7505553499, 0))
                Line((0.7505553499, 0), (0.375277675, 0.65))
            make_face()
        # OneSide extrude, distance=0.53
        extrude(amount=0.53)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.53, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch9 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.65), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, 0.265)):
                Circle(0.1)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5629165125, 0, -0.325), x_dir=(-0.5, 0, -0.8660254038), z_dir=(0.8660254038, 0, -0.5))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.265), 0.1, 90, 180)
                Line((0, 0.165), (0, 0.365))
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.165), (0, 0.365))
                CenterArc((0, 0.265), 0.1, -90, 180)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This image shows three cylindrical components: a rectangular prism (left), a larger cylinder with a rounded end (center), and a smaller cylinder (right), likely representing different views or components of a mechanical assembly or connector parts.
def model_30669_de468b6f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=-3.15
        extrude(amount=-3.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.15), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.3640484718, perimeter: 13.5088484104
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4.25), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.2271846303, perimeter: 3.926990817
            Circle(0.625)
        # OneSide extrude, distance=-3.45
        extrude(amount=-3.45, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.39, perimeter: 3.2
            with BuildLine():
                Line((-0.15, 3.25), (0.15, 3.25))
                Line((-0.15, 1.95), (-0.15, 3.25))
                Line((0.15, 1.95), (-0.15, 1.95))
                Line((0.15, 3.25), (0.15, 1.95))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.39, perimeter: 3.2
            with BuildLine():
                Line((-4.7, 2.2), (-5, 2.2))
                Line((-4.7, 3.5), (-4.7, 2.2))
                Line((-5, 3.5), (-4.7, 3.5))
                Line((-5, 2.2), (-5, 3.5))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch8 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2271846303, perimeter: 3.926990817
            with Locations((5, 0)):
                Circle(0.625)
        # OneSide extrude, distance=-3.25
        extrude(amount=-3.25)
    return part.part


# Description: This is a wedge-shaped or tapered flat plate with a rectangular base that gradually slopes upward, featuring a trapezoidal profile when viewed from the side, commonly used as a shim, ramp, or positioning block in assemblies.
def model_30810_c5e00443_0000():
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
        # Sketch25 -> Extrude18 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1258, perimeter: 142
            with BuildLine():
                Line((0, 47), (0, 10))
                Line((0, 10), (34, 10))
                Line((34, 10), (34, 47))
                Line((34, 47), (0, 47))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a magazine or cartridge holder with a tall, rectangular body featuring a grid-pattern latticed or ribbed structural design, a horizontal base platform, and an angled top opening for inserting or removing items.
def model_30905_511b96bf_0015():
    """Model: OPARCIE v12 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 75.1543258053, perimeter: 76.8110477803
            with BuildLine():
                Line((0.8003634265, 0.5545046388), (-9.3535248287, 0.5545046388))
                CenterArc((0.8003634265, 1.5545046388), 1, -90, 99.9150647785)
                CenterArc((75.1715450031, 14.5545046388), 74.4988254816, 169.1684358963, 20.7466288822)
                Line((2, 28.5545046388), (0, 28.5545046388))
                CenterArc((73.1715450031, 14.5545046388), 74.4988254816, 169.1684358963, 18.3471975995)
                CenterArc((-2.6700951042, 4.5487100225), 2, -90, 97.5156334957)
                Line((-2.6700951042, 2.5487100225), (-9.3535248287, 2.5487100225))
                Line((-9.3535248287, 2.5487100225), (-9.3535248287, 0.5545046388))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 55.0572788111, perimeter: 53.6051542224
            with BuildLine():
                Line((-6, 28.5545046388), (-6, 4.8103034406))
                Line((-3, 4.8103034406), (-6, 4.8103034406))
                CenterArc((65.5581446413, 16.6824040397), 69.5784878342, 170.1756135696, 19.6487728607)
                Line((-6, 28.5545046388), (-3, 28.5545046388))
            make_face()
            # Profile area: 55.0572788111, perimeter: 53.6051542224
            with BuildLine():
                Line((-6, 28.5545046388), (-9, 28.5545046388))
                CenterArc((-77.5581446413, 16.6824040397), 69.5784878342, -9.8243864304, 19.6487728607)
                Line((-6, 4.8103034406), (-9, 4.8103034406))
                Line((-6, 28.5545046388), (-6, 4.8103034406))
            make_face()
        # OneSide extrude, distance=32.5
        extrude(amount=32.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-8.3997877628, -6)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-6.9584288986, -6)):
                Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 28.5545046388, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.9821074186, 10.3329695705)):
                Circle(0.25)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 28.5545046388, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.9821074186, 1.7144778685)):
                Circle(0.25)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shoulder bag or carrying case with an ergonomic curved profile, featuring a large oval carry handle at the top, a tapered body with ribbed/textured side panels, and a flat rectangular base for stability.
def model_31008_8fa25b35_0005():
    """Model: welded unit v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 160, perimeter: 52
            with BuildLine():
                Line((5, -8), (5, 8))
                Line((5, 8), (-5, 8))
                Line((-5, 8), (-5, -8))
                Line((-5, -8), (5, -8))
            make_face()
        # OneSide extrude, distance=2.24
        extrude(amount=2.24)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 273.573987104, perimeter: 82.4997564925
            with BuildLine():
                Line((8, 14), (3.4578376268, 21.8108105198))
                CenterArc((0, 19.8), 4, 30.1789662209, 119.6420675581)
                Line((-8, 14), (-3.4578376268, 21.8108105198))
                Line((-8, 2.24), (-8, 14))
                Line((8, 2.24), (-8, 2.24))
                Line((8, 14), (8, 2.24))
            make_face()
            with BuildLine():
                CenterArc((-2.913, 19.8), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 19.8), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.569
        extrude(amount=-2.569, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 51.7141815255, perimeter: 32.2694772881
            with BuildLine():
                Line((3.74, 2.24), (3.74, 5.5))
                Line((3.74, 5.5), (-1.1674772881, 14))
                Line((-1.1674772881, 14), (-2.431, 14))
                Line((-2.431, 14), (-2.431, 2.24))
                Line((3.74, 2.24), (-2.431, 2.24))
            make_face()
        # Symmetric extrude, each_side=7.399
        extrude(amount=7.399, both=True, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 14, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 95.4318652446, perimeter: 40.0431331767
            with BuildLine():
                Line((-3.74, -6.099), (-3.74, 6.099))
                Line((-11.5635665883, 6.099), (-3.74, 6.099))
                Line((-11.5635665883, -6.099), (-11.5635665883, 6.099))
                Line((-3.74, -6.099), (-11.5635665883, -6.099))
            make_face()
            # Profile area: 15.4124500396, perimeter: 26.9230454238
            with BuildLine():
                Line((1.1674772881, 6.099), (1.1674772881, -6.099))
                Line((1.1674772881, -6.099), (2.431, -6.099))
                Line((2.431, -6.099), (2.431, 6.099))
                Line((2.431, 6.099), (1.1674772881, 6.099))
            make_face()
            # Profile area: 43.8942259604, perimeter: 31.5929545762
            with BuildLine():
                Line((1.1674772881, 6.099), (-2.431, 6.099))
                Line((-2.431, 6.099), (-2.431, -6.099))
                Line((-2.431, -6.099), (1.1674772881, -6.099))
                Line((1.1674772881, 6.099), (1.1674772881, -6.099))
            make_face()
            # Profile area: 15.967182, perimeter: 27.014
            with BuildLine():
                Line((-3.74, 6.099), (-2.431, 6.099))
                Line((-3.74, -6.099), (-3.74, 6.099))
                Line((-2.431, -6.099), (-3.74, -6.099))
                Line((-2.431, 6.099), (-2.431, -6.099))
            make_face()
        # OneSide extrude, distance=-11.76
        extrude(amount=-11.76, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.431, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 123.6737209086, perimeter: 59.8036037613
            with BuildLine():
                Line((-5.059, 12.7795), (-5.059, 19.0574135954))
                CenterArc((0.0205, 12.7795), 5.0795, 180, 180.000007092)
                Line((5.1, 12.7795006287), (5.1, 18.9869090196))
                Line((5.1, 18.9869090196), (3.4578376268, 21.8108105198))
                CenterArc((0, 19.8), 4, 30.1789662209, 119.6420675581)
                Line((-3.4578376268, 21.8108105198), (-5.059, 19.0574135954))
            make_face()
            with BuildLine():
                CenterArc((2.913, 19.8), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 19.8), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.305
        extrude(amount=-0.305, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.24, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7118094971, perimeter: 2.9907962062
            with Locations((-3.129, -4.194)):
                Circle(0.476)
            # Profile area: 0.7118094971, perimeter: 2.9907962062
            with Locations((0.531, 4.196)):
                Circle(0.476)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling component with a blue mesh textured body, featuring a dark band or collar around its middle, a flange or lip at the top, and what appears to be a mounting bracket or tab on the side.
def model_31016_60e3fd8e_0006():
    """Model: Component31"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.1631454095, perimeter: 9.4876098138
            with Locations((-6.70567384, 2.584732462)):
                Circle(1.51)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((6.70567384, -2.584732462)):
                Circle(0.45)
        # OneSide extrude, distance=0.62
        extrude(amount=0.62, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.22, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3340082523, perimeter: 2.1801303001
            with BuildLine():
                CenterArc((6.70567384, -2.584732462), 0.37, 48.5350192248, 82.9299615505)
                Line((6.46067384, -2.3074690493), (6.46067384, -2.8619958746))
                CenterArc((6.70567384, -2.584732462), 0.37, -131.4649807752, 82.9299615505)
                Line((6.95067384, -2.3074690493), (6.95067384, -2.8619958746))
            make_face()
        # OneSide extrude, distance=-0.62
        extrude(amount=-0.62, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7353812243, perimeter: 20.0622106858
            with BuildLine():
                CenterArc((-6.70567384, -2.584732462), 1.683, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-6.70567384, -2.584732462), 1.51, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.28
        extrude(amount=0.28)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0636898714, perimeter: 1.3246043694
            with BuildLine():
                Line((-5.46567384, -1.544732462), (-5.46567384, -1.723048065))
                CenterArc((-5.69567384, -1.544732462), 0.23, 0, 90)
                Line((-5.8888507257, -1.314732462), (-5.69567384, -1.314732462))
                CenterArc((-6.70567384, -2.584732462), 1.51, 34.7956985355, 22.4564822272)
            make_face()
            # Profile area: 0.0636898714, perimeter: 1.3246043694
            with BuildLine():
                CenterArc((-6.70567384, -2.584732462), 1.51, 122.7478192373, 22.4564822272)
                Line((-7.71567384, -1.314732462), (-7.5224969543, -1.314732462))
                CenterArc((-7.71567384, -1.544732462), 0.23, 90, 90)
                Line((-7.94567384, -1.544732462), (-7.94567384, -1.723048065))
            make_face()
            # Profile area: 2.1584105085, perimeter: 6.1632387837
            with BuildLine():
                CenterArc((-7.71567384, -2.024732462), 0.23, 180, 90)
                Line((-7.71567384, -2.254732462), (-5.69567384, -2.254732462))
                CenterArc((-5.69567384, -2.024732462), 0.23, -90, 90)
                Line((-5.46567384, -1.723048065), (-5.46567384, -2.024732462))
                CenterArc((-6.70567384, -2.584732462), 1.51, 34.7956985355, 22.4564822272)
                Line((-7.5224969543, -1.314732462), (-5.8888507257, -1.314732462))
                CenterArc((-6.70567384, -2.584732462), 1.51, 122.7478192373, 22.4564822272)
                Line((-7.94567384, -1.723048065), (-7.94567384, -2.024732462))
            make_face()
        # OneSide extrude, distance=0.97
        extrude(amount=0.97, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.97, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.389706193, perimeter: 5.5026548246
            with BuildLine():
                CenterArc((-7.71567384, -1.544732462), 0.08, 90, 90)
                Line((-7.79567384, -1.544732462), (-7.79567384, -2.024732462))
                CenterArc((-7.71567384, -2.024732462), 0.08, 180, 90)
                Line((-7.71567384, -2.104732462), (-5.69567384, -2.104732462))
                CenterArc((-5.69567384, -2.024732462), 0.08, -90, 90)
                Line((-5.61567384, -2.024732462), (-5.61567384, -1.544732462))
                CenterArc((-5.69567384, -1.544732462), 0.08, 0, 90)
                Line((-5.69567384, -1.464732462), (-7.71567384, -1.464732462))
            make_face()
        # OneSide extrude, distance=-0.76
        extrude(amount=-0.76, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.4247033448, perimeter: 7.390538296
            with BuildLine():
                CenterArc((-6.70567384, -2.584732462), 1.28, 160.0971960041, 219.8056079919)
                CenterArc((-5.69567384, -2.024732462), 0.23, -90, 57.2999996648)
                Line((-5.69567384, -2.254732462), (-7.71567384, -2.254732462))
                CenterArc((-7.71567384, -2.024732462), 0.23, -147.2999996648, 57.2999996648)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or octagonal housing/enclosure with an irregular geometric form, featuring angular faceted surfaces, an internal cavity or pocket, and a protruding slot or flange on the lower section, likely designed as a connector housing, junction box, or mechanical component interface.
def model_31136_987852a4_0001():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.12, perimeter: 12.12
            with BuildLine():
                Line((4.56, -3.5068151638), (0.5, -3.5068151638))
                Line((0.5, -3.5068151638), (0.5, -5.5068151638))
                Line((0.5, -5.5068151638), (4.56, -5.5068151638))
                Line((4.56, -5.5068151638), (4.56, -3.5068151638))
            make_face()
        # OneSide extrude, distance=3.89
        extrude(amount=3.89)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5, perimeter: 4.5
            with BuildLine():
                Line((3.5068151638, 1.24), (5.5068151638, 1.24))
                Line((3.5068151638, 1.24), (3.5068151638, 0.99))
                Line((3.5068151638, 0.99), (5.5068151638, 0.99))
                Line((5.5068151638, 0.99), (5.5068151638, 1.24))
            make_face()
        # OneSide extrude, distance=0.695
        extrude(amount=0.695, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4.56, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5, perimeter: 4.5
            with BuildLine():
                Line((-5.5068151638, 1.24), (-3.5068151638, 1.24))
                Line((-5.5068151638, 1.24), (-5.5068151638, 0.99))
                Line((-5.5068151638, 0.99), (-3.5068151638, 0.99))
                Line((-3.5068151638, 0.99), (-3.5068151638, 1.24))
            make_face()
        # OneSide extrude, distance=0.695
        extrude(amount=0.695, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.24, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.055, 4.0068151638)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.055, 5.0068151638)):
                Circle(0.225)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.24, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-5.005, 5.0068151638)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-5.005, 4.0068151638)):
                Circle(0.225)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1634609928, perimeter: 2.9059732046
            with BuildLine():
                CenterArc((1.54, 4.5068151638), 0.2875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.54, 4.5068151638), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.38
        extrude(amount=0.38, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or axle with rounded ends and a central groove or keyway, featuring a smooth, elongated body with symmetrical design suitable for rotational applications.
def model_31280_c8bd4b11_0000():
    """Model: Horizontal Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # Symmetric extrude, each_side=0.625
        extrude(amount=0.625, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.625, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1335176878, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.375
        extrude(amount=4.375)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.625, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1335176878, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.375
        extrude(amount=4.375)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-5.1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a gray industrial connector or coupling assembly featuring a polygonal housing on the left with blue transparent panels, a cylindrical barrel section in the center, and a protruding cylindrical nozzle on the right, with multiple circular openings or ports visible throughout the design.
def model_31360_a1accb4b_0000():
    """Model: Bloc"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.6, perimeter: 11.6
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (3.8, 0))
                Line((3.8, 0), (3.8, 2))
                Line((3.8, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((1, 1)):
                Circle(0.7)
        # OneSide extrude, distance=-3.8
        extrude(amount=-3.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((1.4, 1)):
                Circle(0.75)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1.4, 1)):
                Circle(0.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7301993078, perimeter: 13.3407075111
            with BuildLine():
                Line((-2, 0), (0, 0))
                Line((0, 0), (0, 2))
                Line((0, 2), (-2, 2))
                Line((-2, 2), (-2, 0))
            make_face()
            with BuildLine():
                CenterArc((-1, 1), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or octagonal structural housing/enclosure with multiple rectangular cutouts and slots distributed across its faces, featuring a pyramidal or angular top section and designed to provide ventilation or access points while maintaining structural integrity.
def model_31962_e5291336_0014():
    """Model: caja"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8.2
            with BuildLine():
                Line((2.7071200397, -0.7958728887), (2.7071200397, 0.8041271113))
                Line((5.2071200397, -0.7958728887), (2.7071200397, -0.7958728887))
                Line((5.2071200397, 0.8041271113), (5.2071200397, -0.7958728887))
                Line((2.7071200397, 0.8041271113), (5.2071200397, 0.8041271113))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-4.4071200397, 0.0041271113)):
                Circle(0.3)
        # OneSide extrude, distance=-3.9
        extrude(amount=-3.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.7071200397), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((0.5, 0.0041271113)):
                Circle(0.325)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.7958728887, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.5, -3.3071200397)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.5, -4.4071200397)):
                Circle(0.15)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8041271113, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.5000000075, -4.4071200397)):
                Circle(0.15)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical spacer or sleeve with an elongated oval slot cut through its center, used for alignment, mounting, or cable routing applications.
def model_31962_e5291336_0026():
    """Model: Cuerpo doble"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0148451001, perimeter: 3.9991148575
            with BuildLine():
                CenterArc((-4.551640337, -4.5169533976), 0.35, 180, 180)
                Line((-4.201640337, -3.6169533976), (-4.201640337, -4.5169533976))
                CenterArc((-4.551640337, -3.6169533976), 0.35, 0, 180)
                Line((-4.901640337, -4.5169533976), (-4.901640337, -3.6169533976))
            make_face()
        # OneSide extrude, distance=7.8
        extrude(amount=7.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.901640337, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0815961157, perimeter: 1.6610064907
            with BuildLine():
                Line((4.6968626967, -3.6169533976), (3.9031373033, -3.6169533976))
                CenterArc((4.3, -4.0669533976), 0.6, 48.5903778907, 82.8192442185)
            make_face()
            # Profile area: 0.9677811239, perimeter: 3.6227997762
            with BuildLine():
                CenterArc((4.3, -4.0669533976), 0.6, 131.4096221093, 97.1807557815)
                Line((3.9031373033, -4.5169533976), (4.6968626967, -4.5169533976))
                CenterArc((4.3, -4.0669533976), 0.6, -48.5903778907, 97.1807557815)
                Line((4.6968626967, -3.6169533976), (3.9031373033, -3.6169533976))
            make_face()
            # Profile area: 0.0815961157, perimeter: 1.6610064907
            with BuildLine():
                CenterArc((4.3, -4.0669533976), 0.6, -131.4096221093, 82.8192442185)
                Line((3.9031373033, -4.5169533976), (4.6968626967, -4.5169533976))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.901640337, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.5, -4.0669533976)):
                Circle(0.15)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1.3, -4.0669533976)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3, -4.0669533976)):
                Circle(0.25)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.901640337, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5596856691, perimeter: 4.6821151455
            with BuildLine():
                CenterArc((3, -4.0669533976), 0.5, 115.8419327632, 128.3161344737)
                Line((2.7820550528, -4.5169533976), (3.2179449472, -4.5169533976))
                CenterArc((3, -4.0669533976), 0.5, -64.1580672368, 128.3161344737)
                Line((3.2179449472, -3.6169533976), (2.7820550528, -3.6169533976))
            make_face()
            with BuildLine():
                CenterArc((3, -4.0669533976), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0146814767, perimeter: 0.8869167062
            with BuildLine():
                Line((3.2179449472, -3.6169533976), (2.7820550528, -3.6169533976))
                CenterArc((3, -4.0669533976), 0.5, 64.1580672368, 51.6838655263)
            make_face()
            # Profile area: 0.0146814767, perimeter: 0.8869167062
            with BuildLine():
                CenterArc((3, -4.0669533976), 0.5, -115.8419327632, 51.6838655263)
                Line((2.7820550528, -4.5169533976), (3.2179449472, -4.5169533976))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.901640337, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.6, -4.0669533976)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((7.3, -4.0669533976)):
                Circle(0.25)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.901640337, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5596856691, perimeter: 4.6821151455
            with BuildLine():
                Line((5.3820550528, -4.5169533976), (5.8179449472, -4.5169533976))
                CenterArc((5.6, -4.0669533976), 0.5, -64.1580672368, 128.3161344737)
                Line((5.8179449472, -3.6169533976), (5.3820550528, -3.6169533976))
                CenterArc((5.6, -4.0669533976), 0.5, 115.8419327632, 128.3161344737)
            make_face()
            with BuildLine():
                CenterArc((5.6, -4.0669533976), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0146814767, perimeter: 0.8869167062
            with BuildLine():
                CenterArc((5.6, -4.0669533976), 0.5, -115.8419327632, 51.6838655263)
                Line((5.3820550528, -4.5169533976), (5.8179449472, -4.5169533976))
            make_face()
            # Profile area: 0.0146814767, perimeter: 0.8869167062
            with BuildLine():
                Line((5.8179449472, -3.6169533976), (5.3820550528, -3.6169533976))
                CenterArc((5.6, -4.0669533976), 0.5, 64.1580672368, 51.6838655263)
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular fan or impeller shroud with a dominant disc-shaped body featuring radial fins or blades extending outward around its circumference, a central hub, and an offset rounded protrusion on one side.
def model_31962_e5291336_0035():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            with Locations((10, 2)):
                Circle(1.7)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, 2)):
                Circle(0.8)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((10, 2)):
                Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((-10, 2)):
                Circle(1.6)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-10, 2)):
                Circle(0.35)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-10, 2)):
                Circle(0.25)
        # OneSide extrude, distance=-2.9
        extrude(amount=-2.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (donut-shaped) component with a smooth outer surface and a large central hole, featuring a dual-lobed or figure-eight internal geometry with ribbed or textured surface patterns, commonly used as a transformer core or magnetic circuit element.
def model_31962_e5291336_0053():
    """Model: Rotatorio"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((22.5507604917, 0.4931093652)):
                Circle(1.5)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.15, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((22.5507604917, 0.4931093652)):
                Circle(1.1)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.85, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.2672563597, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((22.5507604917, 0.4931093652), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((22.5507604917, 0.4931093652), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((22.5507604917, 0.4931093652)):
                Circle(1.1)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((-22.5507604917, 0.4931093652)):
                Circle(0.95)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-22.5507604917, 0.4931093652)):
                Circle(0.8)
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6283185307, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-22.5507604917, 0.4931093652), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-22.5507604917, 0.4931093652), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6283185307, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-22.5507604917, 0.4931093652), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-22.5507604917, 0.4931093652), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a toroidal (donut-shaped) core or transformer component with a hollow circular center, featuring vertical ribbing or lamination patterns on its outer and inner surfaces, and a split or gap visible at the bottom.
def model_31962_e5291336_0056():
    """Model: Component53"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((8, 1)):
                Circle(1.5)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.15, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((8, 1)):
                Circle(1.1)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.85, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.2672563597, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((8, 1), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8, 1), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((8, 1)):
                Circle(1.1)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-8, 1)):
                Circle(0.8)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.8246680716, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((-8, 1), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8, 1), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6283185307, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-8, 1), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8, 1), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6283185307, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-8, 1), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8, 1), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical silencer or muffler with a smaller diameter stub connector at the bottom, featuring a tapered or slightly curved body design.
def model_32219_e5edc7ce_0027():
    """Model: chamber v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            Circle(0.400000006)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # OneSide extrude, distance=-6.8
        extrude(amount=-6.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a forked connector or clevis bracket with a cylindrical shaft extending upward and two parallel prongs at the base featuring elongated slots or mounting holes for pin or bolt fastening.
def model_33655_f8991a06_0003():
    """Model: pieza 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9374792479, perimeter: 3.8909477023
            with BuildLine():
                CenterArc((0, 0), 0.7, 150, 30)
                CenterArc((0, 0), 0.7, -180, 30)
                Line((-0.6062177826, -0.35), (0.6062177826, -0.35))
                CenterArc((0, 0), 0.7, -30, 30)
                CenterArc((0, 0), 0.7, 0, 30)
                Line((0.6062177826, 0.35), (-0.6062177826, 0.35))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.026288725, perimeter: 1.2497787144
            with BuildLine():
                Line((-0.35, 0), (-0.35, 0.35))
                Line((0, 0), (-0.35, 0))
                CenterArc((0, 0.35), 0.35, -180, 90)
            make_face()
            # Profile area: 0.026288725, perimeter: 1.2497787144
            with BuildLine():
                CenterArc((0, 0.35), 0.35, -90, 90)
                Line((0.35, 0), (0, 0))
                Line((0.35, 0.35), (0.35, 0))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 0.35)):
                Circle(0.2)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.026288725, perimeter: 1.2497787144
            with BuildLine():
                Line((-0.35, 0), (-0.35, 0.35))
                Line((0, 0), (-0.35, 0))
                CenterArc((0, 0.35), 0.35, -180, 90)
            make_face()
            # Profile area: 0.026288725, perimeter: 1.2497787144
            with BuildLine():
                CenterArc((0, 0.35), 0.35, -90, 90)
                Line((0.35, 0), (0, 0))
                Line((0.35, 0.35), (0.35, 0))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 0.35)):
                Circle(0.2)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.35), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                Line((0, 0.8), (-0.4, 0.8))
                Line((0, 0.8), (0, 1.2))
                CenterArc((0, 0.8), 0.4, 90, 90)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                Line((0, 0.8), (0, 1.2))
                Line((0, 0.4), (0, 0.8))
                CenterArc((0, 0.8), 0.4, -90, 90)
                CenterArc((0, 0.8), 0.4, 0, 90)
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((0, 0.8), 0.4, 180, 90)
                Line((0, 0.4), (0, 0.8))
                Line((0, 0.8), (-0.4, 0.8))
            make_face()
            # Profile area: 0.0543362939, perimeter: 1.5283185307
            with BuildLine():
                Line((0.4, 0.35), (0.4, 0.8))
                CenterArc((0, 0.8), 0.4, -90, 90)
                Line((0, 0.35), (0, 0.4))
                Line((0, 0.35), (0.4, 0.35))
            make_face()
            # Profile area: 0.14, perimeter: 1.5
            with BuildLine():
                Line((0, 0), (0, 0.35))
                Line((-0.4, 0.35), (0, 0.35))
                Line((-0.4, 0.35), (-0.4, 0))
                Line((-0.4, 0), (0, 0))
            make_face()
            # Profile area: 0.14, perimeter: 1.5
            with BuildLine():
                Line((0, 0), (0.4, 0))
                Line((0.4, 0), (0.4, 0.35))
                Line((0, 0.35), (0.4, 0.35))
                Line((0, 0), (0, 0.35))
            make_face()
            # Profile area: 0.0543362939, perimeter: 1.5283185307
            with BuildLine():
                Line((-0.4, 0.35), (0, 0.35))
                Line((0, 0.35), (0, 0.4))
                CenterArc((0, 0.8), 0.4, 180, 90)
                Line((-0.4, 0.8), (-0.4, 0.35))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1237002107, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch7 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0309748208, perimeter: 0.9518547978
            with BuildLine():
                Line((0.2, 0), (0.2, -0.2236067977))
                CenterArc((0, 0), 0.3, -48.1896851042, 96.3793702084)
                Line((0.2, 0.2236067977), (0.2, 0))
            make_face()
            # Profile area: 0.0590251792, perimeter: 1.5574276068
            with BuildLine():
                CenterArc((0, 0), 0.3, -48.1896851042, 96.3793702084)
                Line((0.2, -0.2236067977), (0.2, -0.3))
                Line((0.2, -0.3), (0.35, -0.3))
                Line((0.35, -0.3), (0.35, 0.3))
                Line((0.35, 0.3), (0.2, 0.3))
                Line((0.2, 0.3), (0.2, 0.2236067977))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical housing or container with a polygonal top section, featuring a wide circular base flange, vertical walls with triangular structural ribs or fins, and an angular upper assembly with multiple faceted surfaces.
def model_34063_0ca1585e_0005():
    """Model: Inner Swashplate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7611210824, perimeter: 12.9794487618
            with BuildLine():
                Line((0.4970562823, 1.2000000179), (-0.4970562823, 1.2000000179))
                Line((-0.4970562823, 1.2000000179), (-1.2000000179, 0.4970562823))
                Line((-1.2000000179, 0.4970562823), (-1.2000000179, -0.4970562823))
                Line((-1.2000000179, -0.4970562823), (-0.4970562823, -1.2000000179))
                Line((-0.4970562823, -1.2000000179), (0.4970562823, -1.2000000179))
                Line((0.4970562823, -1.2000000179), (1.2000000179, -0.4970562823))
                Line((1.2000000179, -0.4970562823), (1.2000000179, 0.4970562823))
                Line((1.2000000179, 0.4970562823), (0.4970562823, 1.2000000179))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7611210824, perimeter: 12.9794487618
            with BuildLine():
                Line((0.4970562823, 1.2000000179), (-0.4970562823, 1.2000000179))
                Line((-0.4970562823, 1.2000000179), (-1.2000000179, 0.4970562823))
                Line((-1.2000000179, 0.4970562823), (-1.2000000179, -0.4970562823))
                Line((-1.2000000179, -0.4970562823), (-0.4970562823, -1.2000000179))
                Line((-0.4970562823, -1.2000000179), (0.4970562823, -1.2000000179))
                Line((0.4970562823, -1.2000000179), (1.2000000179, -0.4970562823))
                Line((1.2000000179, -0.4970562823), (1.2000000179, 0.4970562823))
                Line((1.2000000179, 0.4970562823), (0.4970562823, 1.2000000179))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.2968433005, perimeter: 17.3776786173
            with BuildLine():
                CenterArc((0, 0), 1.5000000224, 0, 360)
            make_face()
            with BuildLine():
                Line((-1.2000000179, 0.4970562823), (-1.2000000179, -0.4970562823))
                Line((-0.4970562823, 1.2000000179), (-1.2000000179, 0.4970562823))
                Line((0.4970562823, 1.2000000179), (-0.4970562823, 1.2000000179))
                Line((1.2000000179, 0.4970562823), (0.4970562823, 1.2000000179))
                Line((1.2000000179, -0.4970562823), (1.2000000179, 0.4970562823))
                Line((0.4970562823, -1.2000000179), (1.2000000179, -0.4970562823))
                Line((-0.4970562823, -1.2000000179), (0.4970562823, -1.2000000179))
                Line((-1.2000000179, -0.4970562823), (-0.4970562823, -1.2000000179))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.7611210824, perimeter: 12.9794487618
            with BuildLine():
                Line((-1.2000000179, -0.4970562823), (-0.4970562823, -1.2000000179))
                Line((-0.4970562823, -1.2000000179), (0.4970562823, -1.2000000179))
                Line((0.4970562823, -1.2000000179), (1.2000000179, -0.4970562823))
                Line((1.2000000179, -0.4970562823), (1.2000000179, 0.4970562823))
                Line((1.2000000179, 0.4970562823), (0.4970562823, 1.2000000179))
                Line((0.4970562823, 1.2000000179), (-0.4970562823, 1.2000000179))
                Line((-0.4970562823, 1.2000000179), (-1.2000000179, 0.4970562823))
                Line((-1.2000000179, 0.4970562823), (-1.2000000179, -0.4970562823))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.0106193582, perimeter: 20.1061932826
            with BuildLine():
                CenterArc((0, 0), 1.7000000253, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5000000224, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.0579643829, perimeter: 14.451326347
            with BuildLine():
                CenterArc((0, 0), 1.5000000224, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.2000000179, 0.0000004024, 0.0000000185), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.0000000185, -0.2000004024)):
                Circle(0.1)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.8485281501, -0.0000000083, 0.8485281501), x_dir=(0.7071067812, 0, 0.7071067812), z_dir=(-0.7071067812, 0, 0.7071067812))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -0.1999999917)):
                Circle(0.1)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or rod with rounded ends and a small radial flange or collar protruding from one side near the right end.
def model_34317_e9c65aa6_0007():
    """Model: shaft v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((-3, 0.5)):
                Circle(4)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 36.3246650571, perimeter: 58.1194640914
            with BuildLine():
                CenterArc((3, 0.5), 5.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3, 0.5), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((3, 0.5)):
                Circle(4)
        # OneSide extrude, distance=46
        extrude(amount=46, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((-3, 0.5)):
                Circle(4)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with Locations((-3, 0.5)):
                Circle(3.5)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-46, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((3, 0.5)):
                Circle(4)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-54, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with Locations((3, 0.5)):
                Circle(3.5)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular enclosure or housing with a curved, ribbed internal structure featuring multiple parallel fins or baffles running lengthwise, likely designed for aerodynamic flow management or structural reinforcement.
def model_34520_035b5e9a_0004():
    """Model: WS2812_led_module"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((0, 0.5), (0, 0))
                Line((0, 0), (0.5, 0))
                Line((0.5, 0), (0.5, 0.5))
                Line((0.5, 0.5), (0, 0.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.2500000037, -0.2500000037)):
                Circle(0.225)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 24 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0200287757, perimeter: 0.6704542161
            with BuildLine():
                CenterArc((-0.2500000037, -0.2500000037), 0.225, 7.7039667462, 25.3854959415)
                CenterArc((-0.0799999982, -0.1202381674), 0.0197618294, -90, 69.4912605238)
                Line((-0.2869953188, -0.1399999969), (-0.0799999982, -0.1399999969))
                Line((-0.2869953188, -0.2198376752), (-0.2869953188, -0.1399999969))
                Line((-0.0270308715, -0.2198376752), (-0.2869953188, -0.2198376752))
            make_face()
            # Profile area: 0.0113460633, perimeter: 0.4527183012
            with BuildLine():
                CenterArc((-0.2500000037, -0.2500000037), 0.225, -24.3446574898, 24.4346224546)
                Line((-0.0250002811, -0.2496467123), (-0.1699999962, -0.2496467123))
                Line((-0.1699999962, -0.2496467123), (-0.1699999962, -0.3299999926))
                Line((-0.1699999962, -0.3299999926), (-0.0599999987, -0.3299999926))
                CenterArc((-0.0599999987, -0.3451907754), 0.0151907828, 9.2440055956, 80.7559944044)
            make_face()
            # Profile area: 0.0129645087, perimeter: 0.4944722142
            with BuildLine():
                CenterArc((-0.2500000037, -0.2500000037), 0.225, 180, 25.1940462715)
                CenterArc((-0.4317137879, -0.3531030109), 0.0230753443, 90.000003234, 71.4950010739)
                Line((-0.3099999886, -0.3300276598), (-0.4317137892, -0.3300276666))
                Line((-0.3099999931, -0.2499999944), (-0.3099999886, -0.3300276598))
                Line((-0.3099999931, -0.2499999944), (-0.4750000037, -0.2500000037))
            make_face()
            # Profile area: 0.0125049813, perimeter: 0.4871250022
            with BuildLine():
                Line((-0.3099999931, -0.2199999951), (-0.3097757866, -0.1395689494))
                Line((-0.3097757866, -0.1395689494), (-0.4097885801, -0.1392901576))
                CenterArc((-0.4097246521, -0.116356818), 0.0229334287, -174.6836047393, 84.5238896844)
                CenterArc((-0.2500000037, -0.2500000037), 0.225, 144.2305117289, 27.990517442)
                Line((-0.3099999931, -0.2199999951), (-0.4729294604, -0.2195458193))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0179999992, perimeter: 0.5399999879
            with BuildLine():
                Line((-0.2999999933, -0.2499999944), (-0.179999996, -0.2499999944))
                Line((-0.2999999933, -0.3999999911), (-0.2999999933, -0.2499999944))
                Line((-0.179999996, -0.3999999911), (-0.2999999933, -0.3999999911))
                Line((-0.179999996, -0.2499999944), (-0.179999996, -0.3999999911))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 24 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0011999999, perimeter: 0.1399999969
            with BuildLine():
                Line((-0.2399999946, -0.3499999922), (-0.1999999955, -0.3499999922))
                Line((-0.2399999946, -0.3799999915), (-0.2399999946, -0.3499999922))
                Line((-0.1999999955, -0.3799999915), (-0.2399999946, -0.3799999915))
                Line((-0.1999999955, -0.3499999922), (-0.1999999955, -0.3799999915))
            make_face()
            # Profile area: 0.0015999999, perimeter: 0.1999999955
            with BuildLine():
                Line((-0.2799999937, -0.2999999933), (-0.2599999942, -0.2999999933))
                Line((-0.2799999937, -0.3799999915), (-0.2799999937, -0.2999999933))
                Line((-0.2599999942, -0.3799999915), (-0.2799999937, -0.3799999915))
                Line((-0.2599999942, -0.2999999933), (-0.2599999942, -0.3799999915))
            make_face()
            # Profile area: 0.0011999999, perimeter: 0.1399999969
            with BuildLine():
                Line((-0.2399999946, -0.2999999933), (-0.1999999955, -0.2999999933))
                Line((-0.2399999946, -0.3299999926), (-0.2399999946, -0.2999999933))
                Line((-0.1999999955, -0.3299999926), (-0.2399999946, -0.3299999926))
                Line((-0.1999999955, -0.2999999933), (-0.1999999955, -0.3299999926))
            make_face()
            # Profile area: 0.0006, perimeter: 0.0999999978
            with BuildLine():
                Line((-0.2199999951, -0.2599999942), (-0.1999999955, -0.2599999942))
                Line((-0.2199999951, -0.2899999935), (-0.2199999951, -0.2599999942))
                Line((-0.1999999955, -0.2899999935), (-0.2199999951, -0.2899999935))
                Line((-0.1999999955, -0.2599999942), (-0.1999999955, -0.2899999935))
            make_face()
            # Profile area: 0.0006, perimeter: 0.0999999978
            with BuildLine():
                Line((-0.2499999944, -0.2599999942), (-0.2299999949, -0.2599999942))
                Line((-0.2499999944, -0.2899999935), (-0.2499999944, -0.2599999942))
                Line((-0.2299999949, -0.2899999935), (-0.2499999944, -0.2899999935))
                Line((-0.2299999949, -0.2599999942), (-0.2299999949, -0.2899999935))
            make_face()
            # Profile area: 0.0006, perimeter: 0.0999999978
            with BuildLine():
                Line((-0.2799999937, -0.2599999942), (-0.2599999942, -0.2599999942))
                Line((-0.2799999937, -0.2899999935), (-0.2799999937, -0.2599999942))
                Line((-0.2599999942, -0.2899999935), (-0.2799999937, -0.2899999935))
                Line((-0.2599999942, -0.2599999942), (-0.2599999942, -0.2899999935))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


# Description: This is a dual-channel curved air intake or duct component with two symmetrical black curved passages featuring blue internal surfaces, designed to direct airflow with smooth transitions and flanged mounting points.
def model_34570_2041f80b_0006():
    """Model: Pieza 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.2016337509, perimeter: 18.4886783881
            with BuildLine():
                Line((0, 0), (-4.8, 0))
                CenterArc((-4.8, -1.3), 1.3, 90, 156.1016290901)
                CenterArc((-5.8938120974, -3.7685167805), 1.4, -5.3889659284, 71.4905950185)
                Line((0, -3.9), (-4.5, -3.9))
                Line((0, 0), (0, -3.9))
            make_face()
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-0.8000638632, -3.100022641)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-2.6000131375, -3.100022641)):
                Circle(0.4)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.599990392, -1.0000169846)):
                Circle(0.2)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.9, perimeter: 5.8
            with BuildLine():
                Line((4.8, 2.1), (2.9, 2.1))
                Line((2.9, 2.1), (2.9, 1.1))
                Line((2.9, 1.1), (4.8, 1.1))
                Line((4.8, 1.1), (4.8, 2.1))
            make_face()
            # Profile area: 3.7, perimeter: 9.4
            with BuildLine():
                Line((4.8, 1.1), (4.8, 2.1))
                Line((4.8, 1.1), (8.5, 1.1))
                Line((8.5, 1.1), (8.5, 2.1))
                Line((8.5, 2.1), (4.8, 2.1))
            make_face()
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2276799454, perimeter: 4.372154496
            with BuildLine():
                CenterArc((-5.4499938577, -1.3000212923), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.4499938577, -1.3000212923), 0.29585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2749748792, perimeter: 1.8588803731
            with Locations((-5.4499938577, -1.3000212923)):
                Circle(0.29585)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2276799454, perimeter: 4.372154496
            with BuildLine():
                CenterArc((-5.4499938577, -1.3000212923), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.4499938577, -1.3000212923), 0.29585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2749748792, perimeter: 1.8588803731
            with Locations((-5.4499938577, -1.3000212923)):
                Circle(0.29585)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch2 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2749748792, perimeter: 1.8588803731
            with Locations((-5.4499938577, -1.3000212923)):
                Circle(0.29585)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2723450247, perimeter: 4.6274333882
            with BuildLine():
                CenterArc((-1.95, 1.6), 0.9, -140.6306827576, 180)
                Line((-1.2542339666, 2.1708849505), (-2.6457660334, 1.0291150495))
            make_face()
            # Profile area: 1.2723450247, perimeter: 4.6274333882
            with BuildLine():
                Line((-1.2542339666, 2.1708849505), (-2.6457660334, 1.0291150495))
                CenterArc((-1.95, 1.6), 0.9, 39.3693172424, 180)
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.9, perimeter: 5.8
            with BuildLine():
                Line((4.8, 2.1), (2.9, 2.1))
                Line((2.9, 2.1), (2.9, 1.1))
                Line((2.9, 1.1), (4.8, 1.1))
                Line((4.8, 1.1), (4.8, 2.1))
            make_face()
            # Profile area: 3.7, perimeter: 9.4
            with BuildLine():
                Line((4.8, 1.1), (4.8, 2.1))
                Line((4.8, 1.1), (8.5, 1.1))
                Line((8.5, 1.1), (8.5, 2.1))
                Line((8.5, 2.1), (4.8, 2.1))
            make_face()
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a geometric, abstract sculptural form with an irregular polygonal shape featuring multiple angular facets, sharp edges, and protruding planes that create a complex, asymmetrical silhouette with no obvious functional holes or slots.
def model_34769_44655d03_0003():
    """Model: Central"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.6945317917, perimeter: 14.0269593129
            with BuildLine():
                Line((-4.8185923537, 4.2417186212), (-5.2685923537, 4.2417186212))
                Line((-5.2685923537, 4.2417186212), (-5.2685923537, 4.4417186212))
                Line((-5.2685923537, 4.4417186212), (-6.2685923537, 4.4417186212))
                Line((-6.2685923537, 4.4417186212), (-6.2685923537, 3.6018186212))
                Line((-6.2685923537, 3.6018186212), (-7.0685923537, 2.3024536909))
                Line((-7.0685923537, 2.1174186212), (-7.0685923537, 2.3024536909))
                Line((-6.2685923537, 2.1174186212), (-7.0685923537, 2.1174186212))
                Line((-6.2685923537, 2.1174186212), (-6.2685923537, 1.6174186212))
                Line((-6.2685923537, 1.6174186212), (-4.9201923537, 0.2690186212))
                Line((-4.7657923537, 0.2690186212), (-4.9201923537, 0.2690186212))
                Line((-4.7657923537, 0.9647023936), (-4.7657923537, 0.2690186212))
                Line((-4.9281755218, 1.1270855617), (-4.7657923537, 0.9647023936))
                CenterArc((-4.7238194705, 1.3469350599), 0.3001586207, -137.091709338, 4.1834186761)
                CenterArc((-4.7238194705, 1.3469350599), 0.3001586207, 47.091709338, 175.8165813239)
                CenterArc((-4.7238194705, 1.3469350599), 0.3001586207, 42.908290662, 4.1834186761)
                Line((-4.5039699723, 1.5512911112), (-4.2917974823, 1.3391186212))
                Line((-3.4759923537, 1.3391186212), (-4.2917974823, 1.3391186212))
                Line((-3.4759923537, 1.5148186212), (-3.4759923537, 1.3391186212))
                Line((-4.8185923537, 2.8574186212), (-3.4759923537, 1.5148186212))
                Line((-4.8185923537, 4.2417186212), (-4.8185923537, 2.8574186212))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5.2685923537, 1.8417186212)):
                Circle(0.25)
        # OneSide extrude, distance=-3.7
        extrude(amount=-3.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.2417186212, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4324776918, perimeter: 3.4831846121
            with BuildLine():
                Line((4.6415923537, 0.55), (4.6415923537, 0.85))
                Line((4.6415923537, 0.85), (3.2000000477, 0.85))
                Line((3.2000000477, 0.85), (3.2000000477, 0.55))
                Line((4.6415923537, 0.55), (3.2000000477, 0.55))
            make_face()
        # OneSide extrude, distance=-4.4
        extrude(amount=-4.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.2685923537, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.7101, 1.8777186212)):
                Circle(0.125)
        # OneSide extrude, distance=-0.95
        extrude(amount=-0.95, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.8185923537, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-0.7, 3.8417186212)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-0.7, 3.1417186212)):
                Circle(0.125)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.4417186212, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.7810923537, 0.7097)):
                Circle(0.25)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a black plastic or composite bracket or enclosure with a curved top housing section, two rectangular cutout windows, internal compartments, and a base frame structure designed for mounting or containing components.
def model_35580_2ab34839_0001():
    """Model: Fuselage_walls_1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on Profile plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 49574.1055446669, perimeter: 897.9901960268
            with BuildLine():
                Line((-53, -3), (52.8247343827, -3))
                Line((52.8247343827, -3), (52.8247343827, 47))
                Line((52.8247343827, 47), (103, 47))
                Line((103, 47), (103, 200))
                CenterArc((0, 177.5903614458), 105.4096385542, 12.2745118985, 155.450976203)
                Line((-103, 47), (-103, 200))
                Line((-53, 47), (-103, 47))
                Line((-53, -3), (-53, 47))
            make_face()
        # OneSide extrude, distance=-275
        extrude(amount=-275)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 46927.9940484724, perimeter: 876.6437863117
            with BuildLine():
                Line((-50, 0), (50, 0))
                Line((50, 0), (50, 50))
                Line((50, 50), (100, 50))
                Line((100, 50), (100, 200))
                CenterArc((0, 177.5), 102.5, 12.6803834918, 154.6392330164)
                Line((-100, 50), (-100, 200))
                Line((-50, 50), (-100, 50))
                Line((-50, 0), (-50, 50))
            make_face()
        # OneSide extrude, distance=-275
        extrude(amount=-275, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(103, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13200, perimeter: 560
            with BuildLine():
                Line((250, 120), (30, 120))
                Line((250, 180), (250, 120))
                Line((30, 180), (250, 180))
                Line((30, 120), (30, 180))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-103, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 13200, perimeter: 560
            with BuildLine():
                Line((-30, 120), (-30, 180))
                Line((-30, 180), (-250, 180))
                Line((-250, 180), (-250, 120))
                Line((-250, 120), (-30, 120))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(103, -0.0000000281, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            with Locations((50, 85.0000000281)):
                Circle(7.5)
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            with Locations((225, 85.0000000281)):
                Circle(7.5)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch5 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-103, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            with Locations((-225, 85)):
                Circle(7.5)
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            with Locations((-50, 85)):
                Circle(7.5)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical heater or heating element with a rounded rectangular body, featuring a small protruding nozzle or connector on the left side and internal heating coils or filaments visible through the semi-transparent surface.
def model_36088_1ea9c8a9_0008():
    """Model: Engine"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1.35
        extrude(amount=1.35)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.35, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.471238898, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.2986722863, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=4.79
        extrude(amount=4.79, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.39, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.49, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or support arm featuring a tall, angled rectangular panel with an integrated cylindrical or rounded support post protruding from its lower portion.
def model_37040_ecbcd25e_0030():
    """Model: zawias1 v3 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((-0.3083039878, -0.075), 0.3, 165.5224878141, 28.9550243719)
                CenterArc((-0.3083039878, -0.075), 0.3, -165.5224878141, 331.0449756281)
            make_face()
            # Profile area: 0.1940443084, perimeter: 2.9016081531
            with BuildLine():
                CenterArc((-0.3083039878, -0.075), 0.3, 165.5224878141, 28.9550243719)
                Line((-1.8987777387, 0), (-0.5987777387, 0))
                Line((-1.8987777387, -0.15), (-1.8987777387, 0))
                Line((-0.5987777387, -0.15), (-1.8987777387, -0.15))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3269709884, perimeter: 2.4857919884
            with BuildLine():
                Line((0.9000000134, 0), (0.9000000134, 0.075))
                Line((0.9000000134, 0.075), (0.9000000134, 0.15))
                Line((0.9000000134, 0.15), (0.5987777387, 0.15))
                CenterArc((0.3083039878, 0.075), 0.3, 14.4775121859, 331.0449756281)
                Line((0.5987777387, 0), (0.9000000134, 0))
            make_face()
            # Profile area: 0.6789122728, perimeter: 6.2525761207
            with BuildLine():
                Line((0.5987777387, 0), (0.9000000134, 0))
                CenterArc((0.3083039878, 0.075), 0.3, 14.4775121859, 331.0449756281)
                Line((0.9000000134, 0.15), (0.5987777387, 0.15))
                Line((0.9000000134, 0.15), (0.9000000134, 0.5000000075))
                Line((0.9000000134, 0.5000000075), (-0.2833920379, 0.5000000075))
                Line((-0.2833920379, 0.5000000075), (-0.2833920379, -0.3500000075))
                Line((-0.2833920379, -0.3500000075), (0.9000000134, -0.3500000075))
                Line((0.9000000134, -0.3500000075), (0.9000000134, 0))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.3083039878, 0.075)):
                Circle(0.2)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5680882414, perimeter: 6.0809915562
            with BuildLine():
                Line((0.5987777387, 0), (0.8973097759, 0))
                CenterArc((0.3083039878, 0.075), 0.3, 14.4775121859, 331.0449756281)
                Line((0.8973097759, 0.15), (0.5987777387, 0.15))
                Line((0.8973097759, 0.15), (0.8973097759, 0.4439848819))
                Line((0.8973097759, 0.4439848819), (-0.3150104819, 0.4439848819))
                Line((-0.3150104819, 0.4439848819), (-0.3150104819, -0.2939848819))
                Line((-0.3150104819, -0.2939848819), (0.8973097759, -0.2939848819))
                Line((0.8973097759, -0.2939848819), (0.8973097759, 0))
            make_face()
            # Profile area: 0.2009037466, perimeter: 3.7370485747
            with BuildLine():
                Line((0.8973097759, 0), (0.8973097759, 0.15))
                Line((0.8973097759, 0.15), (0.5987777387, 0.15))
                CenterArc((0.3083039878, 0.075), 0.3, 14.4775121859, 331.0449756281)
                Line((0.5987777387, 0), (0.8973097759, 0))
            make_face()
            with BuildLine():
                CenterArc((0.3083039878, 0.075), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.3083039878, 0.075)):
                Circle(0.2)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2129155054, perimeter: 1.6378145981
            with BuildLine():
                Line((-0.8973097759, 0), (-0.8973097759, 0.15))
                CenterArc((-0.6473097759, 0.075), 0.2610076627, -163.300755766, 326.601511532)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.6473097759, 0.075)):
                Circle(0.2)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved brake caliper or similar automotive suspension component featuring a long arc-shaped body with two cylindrical bosses (one on each end) and internal cooling passages or slots along its curved surface.
def model_37615_8399c412_0005():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36.3129029735, perimeter: 32.8919936516
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 2.8, -93.4087228566, 93.4939105811)
                Line((-10.6, -2.4), (-10.2041661509, -2.4))
                CenterArc((-10.6, 0), 2.4, 128.6947399219, 141.3052600781)
                CenterArc((-13.1632011236, 3.2), 1.7, -51.3052600781, 179.9999991462)
                CenterArc((-10.6, 0), 5.8, 128.6947399219, 114.9960749483)
            make_face()
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-13.004163056, 2.404163056), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.3798878776, perimeter: 36.2026513164
            with BuildLine():
                CenterArc((-10.6, 0), 5.8, -116.3091851299, 7.8005077155)
                Line((-10.1000001729, -5.4999997639), (-12.4412, -5.4999984145))
                CenterArc((-10.1, -5.1999997639), 0.3, -90.0000330233, 90.0000330233)
                Line((-9.8, -3.8), (-9.8, -5.1999997639))
                CenterArc((-9, -3.8), 0.8, 89.9999954767, 90.0000045233)
                Line((-0.200000002, -3.0000006947), (-8.9999999368, -3))
                CenterArc((-0.1999999388, -2.2000006947), 0.8, -90.0000045233, 90.000007445)
                Line((0.6000000612, -2.2000006539), (0.6000000288, -1.5651999271))
                Line((0.6000000288, -1.5651999271), (0.599999949, 0))
                Line((0, 0), (0.599999949, 0))
                Line((-0.0000006335, -2.2000006947), (0, 0))
                CenterArc((-0.1999999388, -2.2000006947), 0.1999993053, -90, 90)
                Line((-10.2041661509, -2.4), (-0.1999999388, -2.4))
                CenterArc((-13.004163056, -2.404163056), 2.8, -93.4087228566, 93.4939105811)
            make_face()
            # Profile area: 0.1178097245, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-13.004163056, -2.404163056)):
                Circle(0.35)
            # Profile area: 0.1178097245, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-13.004163056, 2.404163056), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.004163056, 2.404163056), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-13.004163056, 2.404163056)):
                Circle(0.35)
        # TwoSides extrude (symmetric), distance=1.6
        extrude(amount=1.6, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 46.7524595515, perimeter: 55.6621605481
            with BuildLine():
                Line((-13.170646429, -5.1992092608), (-17.470646429, -5.1992092608))
                CenterArc((-10.6, 0), 5.8, 128.6947399219, 114.9960749483)
                CenterArc((-13.1632011236, 3.2), 1.7, -51.3052600781, 179.9999991462)
                CenterArc((-10.6, 0), 2.4, 128.6947399219, 141.3052600781)
                Line((-10.6, -2.4), (-10.2041661509, -2.4))
                Line((-10.2041661509, -2.4), (-10.2041661509, 6.6))
                Line((-10.2041661509, 6.6), (-17.470646429, 6.6))
                Line((-17.470646429, -5.1992092608), (-17.470646429, 6.6))
            make_face()
            # Profile area: 36.3129029735, perimeter: 32.8919936516
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 2.8, -93.4087228566, 93.4939105811)
                Line((-10.6, -2.4), (-10.2041661509, -2.4))
                CenterArc((-10.6, 0), 2.4, 128.6947399219, 141.3052600781)
                CenterArc((-13.1632011236, 3.2), 1.7, -51.3052600781, 179.9999991462)
                CenterArc((-10.6, 0), 5.8, 128.6947399219, 114.9960749483)
            make_face()
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-13.004163056, 2.404163056), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1178097245, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-13.004163056, 2.404163056), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.004163056, 2.404163056), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1178097245, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-13.004163056, 2.404163056)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-13.004163056, -2.404163056)):
                Circle(0.35)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-13.004163056, 2.404163056)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-13.004163056, -2.404163056)):
                Circle(0.35)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4733219032, perimeter: 34.5107506463
            with BuildLine():
                Line((0.6000000612, -2.2000006539), (0.6000000288, -1.5651999271))
                CenterArc((-0.1999999388, -2.2000006947), 0.8, -90.0000045233, 90.000007445)
                Line((-0.200000002, -3.0000006947), (-8.9999999368, -3))
                CenterArc((-9, -3.8), 0.8, 89.9999954767, 90.0000045233)
                Line((-9.8, -3.8), (-9.8, -5.1999997639))
                CenterArc((-10.1, -5.1999997639), 0.3, -90.0000330233, 90.0000330233)
                Line((-10.1000001729, -5.4999997639), (2.9999998271, -5.4999997639))
                CenterArc((2.9999998271, -4.6999997639), 0.8, -90, 90)
                Line((3.7999998271, -4.6999997639), (3.7999998271, -1.5651997639))
                Line((3.7999998271, -1.5651997639), (0.6000000288, -1.5651999271))
            make_face()
        # TwoSides extrude (symmetric), distance=0.9
        extrude(amount=0.9, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-0.000000288, 0, 1), z_dir=(-1, 0, -0.000000288))):
            # Profile area: 2.6035949117, perimeter: 9.3110612667
            with BuildLine():
                CenterArc((0, 0), 1.6, -90, 180)
                Line((0, 1.6), (0, 0.95))
                CenterArc((0, 0), 0.95, -90, 180)
                Line((0, -0.95), (0, -1.6))
            make_face()
            # Profile area: 2.6035949117, perimeter: 9.3110612667
            with BuildLine():
                Line((0, -0.95), (0, -1.6))
                CenterArc((0, 0), 0.95, 90, 180)
                Line((0, 1.6), (0, 0.95))
                CenterArc((0, 0), 1.6, 90, 180)
            make_face()
            # Profile area: 1.4176436849, perimeter: 4.8845130209
            with BuildLine():
                CenterArc((0, 0), 0.95, -90, 180)
                Line((0, 0.95), (0, -0.95))
            make_face()
            # Profile area: 1.4176436849, perimeter: 4.8845130209
            with BuildLine():
                Line((0, 0.95), (0, -0.95))
                CenterArc((0, 0), 0.95, 90, 180)
            make_face()
        # OneSide extrude, distance=-3.8
        extrude(amount=-3.8, mode=Mode.ADD)

        # Sketch2 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-0.000000288, 0, 1), z_dir=(-1, 0, -0.000000288))):
            # Profile area: 1.4176436849, perimeter: 4.8845130209
            with BuildLine():
                Line((0, 0.95), (0, -0.95))
                CenterArc((0, 0), 0.95, 90, 180)
            make_face()
            # Profile area: 1.4176436849, perimeter: 4.8845130209
            with BuildLine():
                CenterArc((0, 0), 0.95, -90, 180)
                Line((0, 0.95), (0, -0.95))
            make_face()
        # OneSide extrude, distance=-3.8
        extrude(amount=-3.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.7999998271, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0641541813, perimeter: 1.8114857105
            with BuildLine():
                Line((-1.5651997639, -0.331888197), (-1.5651997639, -0.9))
                CenterArc((-1.5651997639, -1.4), 0.5, 42.4085473275, 47.5914526725)
                CenterArc((0, 0), 1.6000000238, -168.0282069216, 29.6527188822)
            make_face()
            # Profile area: 0.0641541813, perimeter: 1.8114857105
            with BuildLine():
                CenterArc((-1.5651997639, 1.4), 0.5, -90, 47.5914526724)
                Line((-1.5651997639, 0.9), (-1.5651997639, 0.331888197))
                CenterArc((0, 0), 1.6000000238, 138.3754880394, 29.6527188822)
            make_face()
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.ADD)

        # Sketch1 -> Extrude9 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1178097245, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-13.004163056, 2.404163056), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.004163056, 2.404163056), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1178097245, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.004163056, -2.404163056), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex sheet metal or molded plastic component with an angular, asymmetrical design featuring multiple flat faces, internal ribbing or reinforcement structures, and what appears to be mounting flanges or tabs on the left side.
def model_38196_ea48fa42_0004():
    """Model: Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.325), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4193141653, perimeter: 4.4424777961
            with BuildLine():
                Line((1.4, 0), (0, 0))
                Line((1.4, 0.3), (1.4, 0))
                Line((1.4, 0.35), (1.4, 0.3))
                Line((0, 0.35), (1.4, 0.35))
                Line((0, 0.35), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((0.95, 0.1704497403), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4193141653, perimeter: 4.4424777961
            with BuildLine():
                Line((-1.4, 0), (-1.4, 0.35))
                Line((0, 0), (-1.4, 0))
                Line((0, 0.35), (0, 0))
                Line((-1.4, 0.35), (0, 0.35))
            make_face()
            with BuildLine():
                CenterArc((-0.95, 0.1704497403), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.95, 0.1704497403)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.95, 0.1704497403)):
                Circle(0.15)
        # OneSide extrude, distance=0.42
        extrude(amount=0.42)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2240000017, perimeter: 5.7600000417
            with BuildLine():
                Line((1.4, 2.745), (-1.4000000209, 2.745))
                Line((1.4, 2.825), (1.4, 2.745))
                Line((-1.4000000209, 2.825), (1.4, 2.825))
                Line((-1.4000000209, 2.745), (-1.4000000209, 2.825))
            make_face()
            # Profile area: 0.9520000035, perimeter: 6.2800000209
            with BuildLine():
                Line((-1.4, 2.405), (1.4, 2.405))
                Line((1.4, 2.405), (1.4, 2.745))
                Line((1.4, 2.745), (-1.4000000209, 2.745))
                Line((-1.4000000209, 2.745), (-1.4, 2.405))
            make_face()
        # OneSide extrude, distance=0.366
        extrude(amount=0.366, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.716, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.15, perimeter: 1.7
            with BuildLine():
                Line((0.8, 2.575), (0.8, 2.825))
                Line((1.4, 2.575), (0.8, 2.575))
                Line((1.4, 2.575), (1.4, 2.825))
                Line((1.4, 2.825), (0.8, 2.825))
            make_face()
            # Profile area: 0.1500000026, perimeter: 1.7000000209
            with BuildLine():
                Line((-0.8, 2.825), (-1.4000000209, 2.825))
                Line((-1.4000000209, 2.825), (-1.4, 2.575))
                Line((-0.8, 2.575), (-1.4, 2.575))
                Line((-0.8, 2.825), (-0.8, 2.575))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.825), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5744, perimeter: 5.168
            with BuildLine():
                Line((0.8, 0.716), (0.8, 1.7))
                Line((0.8, 1.7), (-0.8, 1.7))
                Line((-0.8, 1.7), (-0.8, 0.716))
                Line((0.8, 0.716), (-0.8, 0.716))
            make_face()
            # Profile area: 0.5856, perimeter: 3.932
            with BuildLine():
                Line((0.8, 0.716), (-0.8, 0.716))
                Line((-0.8, 0.716), (-0.8, 0.35))
                Line((-0.8, 0.35), (0.8, 0.35))
                Line((0.8, 0.35), (0.8, 0.716))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.425), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 1.2245)):
                Circle(0.3)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.425), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0122454766, perimeter: 1.0501450741
            with BuildLine():
                Line((0.2999981306, 1.2255590767), (0.8, 1.2273242221))
                Line((0.8, 1.2273242221), (0.8, 1.250912111))
                Line((0.8, 1.250912111), (0.2988350722, 1.250912111))
                CenterArc((0, 1.2245), 0.3, 0.2022691647, 4.8486118415)
            make_face()
            # Profile area: 0.0127720694, perimeter: 1.0520171874
            with BuildLine():
                CenterArc((0, 1.2245), 0.3, -4.5096095897, 4.7118787543)
                Line((0.2990712482, 1.200912111), (0.8, 1.200912111))
                Line((0.8, 1.200912111), (0.8, 1.2273242221))
                Line((0.2999981306, 1.2255590767), (0.8, 1.2273242221))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or polygonal container/bin with a pyramidal top section, featuring an open or removable lid and interior geometric ribbing or structural reinforcement visible through the semi-transparent surfaces.
def model_39109_816b707e_0006():
    """Model: bark v7 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5600000083, perimeter: 3.0000000209
            with BuildLine():
                Line((-4.3000000641, 2.5000000373), (-5.0000000745, 2.5000000373))
                Line((-5.0000000745, 2.5000000373), (-5.0000000745, 1.7000000373))
                Line((-5.0000000745, 1.7000000373), (-4.3000000641, 1.7000000373))
                Line((-4.3000000641, 1.7000000373), (-4.3000000641, 2.5000000373))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5600000083, perimeter: 3.0000000209
            with BuildLine():
                Line((-5.0000000745, -1.7000000373), (-5.0000000745, -2.5000000373))
                Line((-5.0000000745, -2.5000000373), (-4.3000000641, -2.5000000373))
                Line((-4.3000000641, -2.5000000373), (-4.3000000641, -1.7000000373))
                Line((-4.3000000641, -1.7000000373), (-5.0000000745, -1.7000000373))
            make_face()

        # Sketch4 -> Extrude2 (Join)
        # Sketch on Profile plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1400000021, perimeter: 1.5000000104
            with BuildLine():
                Line((-5.0000000745, -2.1000000373), (-4.6500000693, -2.1000000373))
                Line((-4.6500000693, -1.7000000373), (-4.6500000693, -2.1000000373))
                Line((-5.0000000745, -1.7000000373), (-4.6500000693, -1.7000000373))
                Line((-5.0000000745, -2.1000000373), (-5.0000000745, -1.7000000373))
            make_face()
            # Profile area: 0.1400000021, perimeter: 1.5000000104
            with BuildLine():
                Line((-4.6500000693, -2.1000000373), (-4.3000000641, -2.1000000373))
                Line((-4.3000000641, -1.7000000373), (-4.3000000641, -2.1000000373))
                Line((-4.6500000693, -1.7000000373), (-4.3000000641, -1.7000000373))
                Line((-4.6500000693, -1.7000000373), (-4.6500000693, -2.1000000373))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch7 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0003141593, perimeter: 0.0628318517
            with Locations((4.6999998949, -1.9749999559)):
                Circle(0.0099999998)
            # Profile area: 0.0003141593, perimeter: 0.0628318517
            with Locations((4.6499998961, -1.9749999559)):
                Circle(0.0099999998)
            # Profile area: 0.0003141593, perimeter: 0.0628318517
            with Locations((4.6049998971, -1.9749999559)):
                Circle(0.0099999998)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)

        # Sketch7 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0090575225, perimeter: 0.6884955625
            with BuildLine():
                Line((4.5500000678, -1.9500000291), (4.7500000708, -1.9500000291))
                Line((4.5500000678, -2.0000000298), (4.5500000678, -1.9500000291))
                Line((4.7500000708, -2.0000000298), (4.5500000678, -2.0000000298))
                Line((4.7500000708, -1.9500000291), (4.7500000708, -2.0000000298))
            make_face()
            with BuildLine():
                CenterArc((4.6999998949, -1.9749999559), 0.0099999998, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.6499998961, -1.9749999559), 0.0099999998, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.6049998971, -1.9749999559), 0.0099999998, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.5000000373), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((4.8000000715, 0), (4.5000000671, 0))
                Line((4.8000000715, 0.1000000015), (4.8000000715, 0))
                Line((4.5000000671, 0.1000000015), (4.8000000715, 0.1000000015))
                Line((4.5000000671, 0), (4.5000000671, 0.1000000015))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_24861_c05860c8_0005": {"func": model_24861_c05860c8_0005, "volume": 2.2526562855, "area": 22.3592701583},
    "model_25199_39e3c0d3_0005": {"func": model_25199_39e3c0d3_0005, "volume": 28.6233909837, "area": 164.5920841926},
    "model_25211_336c083f_0001": {"func": model_25211_336c083f_0001, "volume": 104.9917322984, "area": 224.2576545086},
    "model_25335_491efa81_0008": {"func": model_25335_491efa81_0008, "volume": 18.387790987, "area": 54.5237958663},
    "model_26086_bf892d7f_0021": {"func": model_26086_bf892d7f_0021, "volume": 2770.7502642028, "area": 1919.4725801271},
    "model_26086_bf892d7f_0022": {"func": model_26086_bf892d7f_0022, "volume": 35035.4569882227, "area": 8374.9055106739},
    "model_26384_83eddf22_0018": {"func": model_26384_83eddf22_0018, "volume": 14.294556846, "area": 49.5496576122},
    "model_26768_c4df841f_0011": {"func": model_26768_c4df841f_0011, "volume": 80.6, "area": 142.1195959493},
    "model_26942_279de65e_0008": {"func": model_26942_279de65e_0008, "volume": 325.2548916178, "area": 586.3142287228},
    "model_27054_342fcf5c_0000": {"func": model_27054_342fcf5c_0000, "volume": 313.3063664814, "area": 343.1297389877},
    "model_27694_7801dc67_0001": {"func": model_27694_7801dc67_0001, "volume": 2.5002307377, "area": 20.0999020227},
    "model_27694_7801dc67_0004": {"func": model_27694_7801dc67_0004, "volume": 2.5984055229, "area": 20.4926011044},
    "model_27725_5cceaeb7_0010": {"func": model_27725_5cceaeb7_0010, "volume": 588.0189536503, "area": 493.9469474142},
    "model_27839_4a077326_0000": {"func": model_27839_4a077326_0000, "volume": 15.2651575488, "area": 90.6380187325},
    "model_28446_d757d32d_0009": {"func": model_28446_d757d32d_0009, "volume": 7.672256631, "area": 36.3752208335},
    "model_28870_da6bdb2e_0000": {"func": model_28870_da6bdb2e_0000, "volume": 1396.607580524, "area": 724.4512659178},
    "model_28879_7c56f134_0000": {"func": model_28879_7c56f134_0000, "volume": 125.1256063041, "area": 255.809245004},
    "model_28896_5698192a_0000": {"func": model_28896_5698192a_0000, "volume": 135.3320486595, "area": 278.0817260492},
    "model_28924_34ec542a_0000": {"func": model_28924_34ec542a_0000, "volume": 34.7770489464, "area": 115.623898549},
    "model_29184_9d7cf184_0000": {"func": model_29184_9d7cf184_0000, "volume": 112.9305647117, "area": 285.1181984921},
    "model_29726_73b01e1f_0000": {"func": model_29726_73b01e1f_0000, "volume": 59.973536979, "area": 167.6474565002},
    "model_30400_8824ce97_0000": {"func": model_30400_8824ce97_0000, "volume": 2.2081404218, "area": 14.1769666338},
    "model_30669_de468b6f_0000": {"func": model_30669_de468b6f_0000, "volume": 14.4929208284, "area": 78.9768802465},
    "model_30810_c5e00443_0000": {"func": model_30810_c5e00443_0000, "volume": 6290, "area": 3226},
    "model_30905_511b96bf_0015": {"func": model_30905_511b96bf_0015, "volume": 785.4330220672, "area": 1117.4959151284},
    "model_31008_8fa25b35_0005": {"func": model_31008_8fa25b35_0005, "volume": 1154.7590534125, "area": 1320.5397014811},
    "model_31016_60e3fd8e_0006": {"func": model_31016_60e3fd8e_0006, "volume": 5.4115686699, "area": 43.3818531557},
    "model_31136_987852a4_0001": {"func": model_31136_987852a4_0001, "volume": 32.1848720492, "area": 70.8874414871},
    "model_31280_c8bd4b11_0000": {"func": model_31280_c8bd4b11_0000, "volume": 2.3762221434, "area": 57.0041986994},
    "model_31360_a1accb4b_0000": {"func": model_31360_a1accb4b_0000, "volume": 9.0857023899, "area": 66.2651764628},
    "model_31962_e5291336_0014": {"func": model_31962_e5291336_0014, "volume": 3.1796202169, "area": 21.1875159546},
    "model_31962_e5291336_0026": {"func": model_31962_e5291336_0026, "volume": 6.0561578254, "area": 38.1301933783},
    "model_31962_e5291336_0035": {"func": model_31962_e5291336_0035, "volume": 5.4828645787, "area": 38.5944657494},
    "model_31962_e5291336_0053": {"func": model_31962_e5291336_0053, "volume": 1.965851603, "area": 31.5101743155},
    "model_31962_e5291336_0056": {"func": model_31962_e5291336_0056, "volume": 1.965851603, "area": 31.5101743155},
    "model_32219_e5edc7ce_0027": {"func": model_32219_e5edc7ce_0027, "volume": 13.7004855368, "area": 143.6336161558},
    "model_33655_f8991a06_0003": {"func": model_33655_f8991a06_0003, "volume": 1.4415723158, "area": 11.7888377194},
    "model_34063_0ca1585e_0005": {"func": model_34063_0ca1585e_0005, "volume": 8.2501797825, "area": 41.8623180978},
    "model_34317_e9c65aa6_0007": {"func": model_34317_e9c65aa6_0007, "volume": 3425.3177401171, "area": 1905.7686434839},
    "model_34520_035b5e9a_0004": {"func": model_34520_035b5e9a_0004, "volume": 0.0352621305, "area": 1.0783293974},
    "model_34570_2041f80b_0006": {"func": model_34570_2041f80b_0006, "volume": 49.0007694894, "area": 144.715731578},
    "model_34769_44655d03_0003": {"func": model_34769_44655d03_0003, "volume": 8.3490168179, "area": 40.4575440291},
    "model_35580_2ab34839_0001": {"func": model_35580_2ab34839_0001, "volume": 655549.2449240768, "area": 445761.5237276119},
    "model_36088_1ea9c8a9_0008": {"func": model_36088_1ea9c8a9_0008, "volume": 18.4361223283, "area": 42.6251291239},
    "model_37040_ecbcd25e_0030": {"func": model_37040_ecbcd25e_0030, "volume": 0.5934993494, "area": 11.3930222474},
    "model_37615_8399c412_0005": {"func": model_37615_8399c412_0005, "volume": 203.5509639093, "area": 472.9941640246},
    "model_38196_ea48fa42_0004": {"func": model_38196_ea48fa42_0004, "volume": 1.7721594691, "area": 14.5565126299},
    "model_39109_816b707e_0006": {"func": model_39109_816b707e_0006, "volume": 0.221309428, "area": 2.416884982},
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
