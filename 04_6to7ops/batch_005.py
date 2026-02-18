"""Batch 005 - passing/04_6to7ops
94 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_25211_336c083f_0015():
    """Model: 3-Main Cylinder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0265482457, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8902652413, perimeter: 28.902652413
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.0265482457, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0265482457, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.6
        extrude(amount=5.6, mode=Mode.ADD)
    return part.part


def model_25284_3364996e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.760093699, perimeter: 27.3304056403
            with BuildLine():
                Line((-5, 0), (-5.9187169816, 0))
                Line((-5.9187169816, 0), (-5.9187169816, -0.3183283395))
                Line((-5.9187169816, -0.3183283395), (-4.8450169396, -0.3183283395))
                CenterArc((-9.2058314998, 33.7346493152), 34.3310645156, -82.7024375403, 14.3594900796)
                Line((5.2180064494, 1.8270330705), (3.4640547017, 1.8270330705))
                Line((6.7673304932, 3.4348221726), (5.2180064494, 1.8270330705))
                Line((5.2180064494, 2.4704014779), (6.7673304932, 3.4348221726))
                Line((3.4640547017, 2.4704014779), (5.2180064494, 2.4704014779))
                CenterArc((-8.9952713563, 29.4234555338), 29.6934660954, -82.2673704481, 17.0765956341)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-5.9187169816, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.294971129, perimeter: 2.1729724182
            with BuildLine():
                Line((0, 0.7775785163), (-0.5313291764, 0.7775785163))
                Line((-0.5313291764, 0.7775785163), (-0.5313291764, 0.2224214837))
                Line((-0.5313291764, 0.2224214837), (0, 0.2224214837))
                Line((0, 0.2224214837), (0, 0.7775785163))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7775785163), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-5.6530523934, 0.1591641697)):
                Circle(0.1)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)
    return part.part


def model_25284_c88414c8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.2300283735, perimeter: 29.407289083
            with BuildLine():
                Line((5.2180064494, 4.8379835707), (3.4640547017, 4.8379835707))
                Line((3.4640547017, 4.8379835707), (3.4640547017, 4.3086433671))
                CenterArc((13.5738025705, -26.0191797263), 31.9684822217, 108.4357539155, 17.0854060881)
                Line((-5, 0), (-5.9448083641, -0.6744518546))
                Line((-5.3983097212, -1.0463667145), (-5.9448083641, -0.6744518546))
                Line((-4.471673766, -0.3176708976), (-5.3983097212, -1.0463667145))
                CenterArc((10.2528383653, -19.0418930584), 23.8203222698, 105.128071019, 23.0530307124)
                Line((4.0362703766, 4.4725769566), (4.0362703766, 3.9529332179))
                Line((5.2180064494, 4.4725769566), (4.0362703766, 4.4725769566))
                Line((6.7673304932, 4.1071703425), (5.2180064494, 4.4725769566))
                Line((5.2180064494, 4.8379835707), (6.7673304932, 4.1071703425))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.6878257912, 2.3643969748, 0), x_dir=(-0.8139010024, -0.5810035785, 0), z_dir=(-0.5810035785, 0.8139010024, 0))):
            # Profile area: 0.1196092512, perimeter: 1.4864662926
            with BuildLine():
                Line((5.2303444278, 0), (5.2303444278, 0.235640008))
                Line((4.7227512895, 0.235640008), (5.2303444278, 0.235640008))
                Line((4.7227512895, 0.235640008), (4.7227512895, 0))
                Line((4.7227512895, 0), (5.2303444278, 0))
            make_face()
            # Profile area: 0.1196092512, perimeter: 1.4864662926
            with BuildLine():
                Line((4.7227512895, 0.764359992), (4.7227512895, 1))
                Line((5.2303444278, 0.764359992), (4.7227512895, 0.764359992))
                Line((5.2303444278, 0.764359992), (5.2303444278, 1))
                Line((5.2303444278, 1), (4.7227512895, 1))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.764359992), x_dir=(-0.8139010024, -0.5810035785, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((4.9410086593, -2.5949081204)):
                Circle(0.1)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)
    return part.part


def model_25284_da61a614_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.8950444096, perimeter: 24.1056505916
            with BuildLine():
                Line((-4.6178234548, 5.1951045168), (-5, 5))
                CenterArc((4.2759736276, 15.522834434), 14.0276060418, -131.3964678523, 43.8171873364)
                Line((6, 1.5), (4.8684570207, 1.5077463253))
                Line((6, 1.8544210271), (6, 1.5))
                Line((4.8054252568, 1.8544210271), (6, 1.8544210271))
                CenterArc((4.0544636763, 14.6968209777), 12.8643375184, -132.3869353179, 45.7335051454)
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8544210271, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4775490657, perimeter: 2.7936343865
            with BuildLine():
                Line((-6, 1.1782553095), (-5.4027126284, 1.1782553095))
                Line((-6, 0.3787254878), (-6, 1.1782553095))
                Line((-5.4027126284, 0.3787254878), (-6, 0.3787254878))
                Line((-5.4027126284, 1.1782553095), (-5.4027126284, 0.3787254878))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3787254878), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-5.8447831836, -1.6010649277)):
                Circle(0.1)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_25285_89960b57_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7, perimeter: 28
            with BuildLine():
                Line((-1.5, -2.5), (-1.5, 2.5))
                Line((1.5, -2.5), (-1.5, -2.5))
                Line((1.5, 2.5), (1.5, -2.5))
                Line((-1.5, 2.5), (1.5, 2.5))
            make_face()
            with BuildLine():
                Line((-1, -2), (-1, 2))
                Line((-1, 2), (1, 2))
                Line((1, 2), (1, -2))
                Line((1, -2), (-1, -2))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=75
        extrude(amount=75)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 72.5)):
                Circle(0.5)
        # OneSide extrude, distance=-4.1
        extrude(amount=-4.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_25285_992982f8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7, perimeter: 28
            with BuildLine():
                Line((-1.5, -2.5), (-1.5, 2.5))
                Line((1.5, -2.5), (-1.5, -2.5))
                Line((1.5, 2.5), (1.5, -2.5))
                Line((-1.5, 2.5), (1.5, 2.5))
            make_face()
            with BuildLine():
                Line((-1, -2), (-1, 2))
                Line((-1, 2), (1, 2))
                Line((1, 2), (1, -2))
                Line((1, -2), (-1, -2))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=80
        extrude(amount=80)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 78.5)):
                Circle(0.5)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 1.5)):
                Circle(0.5)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)
    return part.part


def model_25294_decd8b5a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 103.2286376297, perimeter: 140.918249645
            with BuildLine():
                Line((-0.2367470345, 1.496996523), (-20.9867470345, 1.496996523))
                Line((-20.9867470345, 13.4780606728), (-20.9867470345, 1.496996523))
                Line((-20.9867470345, 13.4780606728), (-22.5, 13.4780606728))
                Line((-22.5, 0), (-22.5, 13.4780606728))
                Line((-22.5, 0), (22.5, 0))
                Line((22.5, 13.4780606728), (22.5, 0))
                Line((21.0198799524, 13.4780606728), (22.5, 13.4780606728))
                Line((21.0198799524, 13.4780606728), (21.0198799524, 1.496996523))
                Line((21.0198799524, 1.496996523), (0.7632529655, 1.496996523))
                Line((-0.2367470345, 1.496996523), (0.7632529655, 1.496996523))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 103.2286376297, perimeter: 140.918249645
            with BuildLine():
                Line((-0.2367470345, 1.496996523), (-20.9867470345, 1.496996523))
                Line((-20.9867470345, 13.4780606728), (-20.9867470345, 1.496996523))
                Line((-20.9867470345, 13.4780606728), (-22.5, 13.4780606728))
                Line((-22.5, 0), (-22.5, 13.4780606728))
                Line((-22.5, 0), (22.5, 0))
                Line((22.5, 13.4780606728), (22.5, 0))
                Line((21.0198799524, 13.4780606728), (22.5, 13.4780606728))
                Line((21.0198799524, 13.4780606728), (21.0198799524, 1.496996523))
                Line((21.0198799524, 1.496996523), (0.7632529655, 1.496996523))
                Line((-0.2367470345, 1.496996523), (0.7632529655, 1.496996523))
            make_face()
            # Profile area: 500.2840926446, perimeter: 113.9753822733
            with BuildLine():
                Line((-0.2367470345, 4.496996523), (0.7632529655, 4.496996523))
                Line((0.7632529655, 4.496996523), (0.7632529655, 1.496996523))
                Line((21.0198799524, 1.496996523), (0.7632529655, 1.496996523))
                Line((21.0198799524, 13.4780606728), (21.0198799524, 1.496996523))
                Line((-20.9867470345, 13.4780606728), (21.0198799524, 13.4780606728))
                Line((-20.9867470345, 13.4780606728), (-20.9867470345, 1.496996523))
                Line((-0.2367470345, 1.496996523), (-20.9867470345, 1.496996523))
                Line((-0.2367470345, 4.496996523), (-0.2367470345, 1.496996523))
            make_face()
            # Profile area: 3, perimeter: 8
            with BuildLine():
                Line((-0.2367470345, 4.496996523), (-0.2367470345, 1.496996523))
                Line((-0.2367470345, 1.496996523), (0.7632529655, 1.496996523))
                Line((0.7632529655, 4.496996523), (0.7632529655, 1.496996523))
                Line((-0.2367470345, 4.496996523), (0.7632529655, 4.496996523))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.9810641497, perimeter: 7.9621282995
            with BuildLine():
                Line((-0.2367470345, 10.496996523), (-0.2367470345, 13.4780606728))
                Line((-0.2367470345, 10.496996523), (0.7632529655, 10.496996523))
                Line((0.7632529655, 10.496996523), (0.7632529655, 13.4780606728))
                Line((0.7632529655, 13.4780606728), (-0.2367470345, 13.4780606728))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(22.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((6.7390303364, 6.75)):
                Circle(3)
        # OneSide extrude, distance=-47.5
        extrude(amount=-47.5, mode=Mode.SUBTRACT)
    return part.part


def model_25335_d0469c67_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 24.6300864041, perimeter: 17.5929188601
            Circle(2.8)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.7567475535, perimeter: 36.756634047
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_25378_c6523377_0003():
    """Model: M3_5mm v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2215608219, perimeter: 2.8588493148
            with BuildLine():
                CenterArc((0, 0), 0.305, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0125, perimeter: 0.45
            with BuildLine():
                Line((-0.175, 0.05), (-0.175, -0.05))
                Line((-0.175, -0.05), (-0.05, -0.05))
                Line((-0.05, 0.05), (-0.05, -0.05))
                Line((-0.05, 0.05), (-0.175, 0.05))
            make_face()
            # Profile area: 0.0125, perimeter: 0.45
            with BuildLine():
                Line((0.05, 0.05), (-0.05, 0.05))
                Line((0.05, 0.05), (0.05, 0.175))
                Line((0.05, 0.175), (-0.05, 0.175))
                Line((-0.05, 0.175), (-0.05, 0.05))
            make_face()
            # Profile area: 0.0125, perimeter: 0.45
            with BuildLine():
                Line((0.05, -0.05), (0.05, 0.05))
                Line((0.05, -0.05), (0.175, -0.05))
                Line((0.175, -0.05), (0.175, 0.05))
                Line((0.175, 0.05), (0.05, 0.05))
            make_face()
            # Profile area: 0.0125, perimeter: 0.45
            with BuildLine():
                Line((-0.05, -0.05), (0.05, -0.05))
                Line((-0.05, -0.05), (-0.05, -0.175))
                Line((-0.05, -0.175), (0.05, -0.175))
                Line((0.05, -0.175), (0.05, -0.05))
            make_face()
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((-0.05, 0.05), (-0.05, -0.05))
                Line((-0.05, -0.05), (0.05, -0.05))
                Line((0.05, -0.05), (0.05, 0.05))
                Line((0.05, 0.05), (-0.05, 0.05))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_25381_9c263e4d_0000():
    """Model: Part13_MeatGrinder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7865924223, perimeter: 3.143980264
            Circle(0.50038)
        # OneSide extrude, distance=5.4991
        extrude(amount=5.4991)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.4991), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1097430136, perimeter: 1.4150721164
            with BuildLine():
                CenterArc((0, 0), 0.50038, 66.5169873071, 46.9660253857)
                Line((0.19939, 0.4589376562), (0.19939, 0.7620000243))
                Line((0.19939, 0.7620000243), (-0.19939, 0.7620000243))
                Line((-0.19939, 0.7620000243), (-0.19939, 0.4589376562))
            make_face()
            # Profile area: 0.3882547123, perimeter: 2.6560853854
            with BuildLine():
                Line((-0.19939, 0.4589376562), (-0.19939, -0.4589376562))
                CenterArc((0, 0), 0.50038, -113.4830126929, 46.9660253857)
                Line((0.19939, -0.4589376562), (0.19939, 0.4589376562))
                CenterArc((0, 0), 0.50038, 66.5169873071, 46.9660253857)
            make_face()
            # Profile area: 0.0923051437, perimeter: 1.3276160263
            with BuildLine():
                CenterArc((0, 0), 0.50038, -113.4830126929, 46.9660253857)
                Line((-0.19939, -0.4589376562), (-0.19939, -0.7182719793))
                Line((-0.19939, -0.7182719793), (0.19939, -0.7182719793))
                Line((0.19939, -0.7182719793), (0.19939, -0.4589376562))
            make_face()
        # OneSide extrude, distance=-1.50114
        extrude(amount=-1.50114, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.19939, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.1966481056, perimeter: 1.571990132
            with Locations((-4.69773, 0)):
                Circle(0.25019)
        # TwoSides extrude, along=1.143, against=-0.635
        extrude(amount=1.143, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


def model_25389_035e5844_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 225, perimeter: 60
            with BuildLine():
                Line((15, -15), (0, -15))
                Line((15, 0), (15, -15))
                Line((0, 0), (15, 0))
                Line((0, -15), (0, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((-7.5, 7.5)):
                Circle(3)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


def model_25416_b0423b7d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2411500823, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.1787601976, perimeter: 33.9292006588
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.2411500823, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, 2.7000000402)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2411500823, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_25416_bd13dfb0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2400000072, perimeter: 4.8000000715
            with BuildLine():
                Line((-1.0000000149, 0.400000006), (0, 0.400000006))
                Line((-1.0000000149, 0), (-1.0000000149, 0.400000006))
                Line((0, 0), (-1.0000000149, 0))
                Line((0, 0.400000006), (0, 0))
            make_face()
            with BuildLine():
                Line((-0.9000000134, 0.1000000015), (-0.9000000134, 0.3000000045))
                Line((-0.9000000134, 0.3000000045), (-0.1000000015, 0.3000000045))
                Line((-0.1000000015, 0.3000000045), (-0.1000000015, 0.1000000015))
                Line((-0.1000000015, 0.1000000015), (-0.9000000134, 0.1000000015))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.0000000149), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.034636059, perimeter: 0.6597344573
            with Locations((0.1882373989, 0.200000003)):
                Circle(0.105)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.400000006, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.185612496, perimeter: 2.0640312569
            with BuildLine():
                Line((-0.3101265077, 0.1000000015), (-0.3101265077, 0.9000000134))
                Line((-0.0781108912, 0.1000000015), (-0.3101265077, 0.1000000015))
                Line((-0.0781108912, 0.9000000134), (-0.0781108912, 0.1000000015))
                Line((-0.3101265077, 0.9000000134), (-0.0781108912, 0.9000000134))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_25425_3ba62cc0_0000():
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
        # Sketch6 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 48.1330065252, perimeter: 34.5037381799
            with BuildLine():
                _nurbs_edge([(2.4668209785, 14.5825147459), (2.4167215496, 14.5864730633), (2.2951016407, 14.5725342939), (2.048435643, 14.4860874933), (1.5821475887, 14.2306389826), (0.6582549861, 13.5633807138), (-0.5255968398, 12.5758184353), (-1.7893070256, 11.4517049045), (-2.8255411337, 10.5046063604), (-3.3921419658, 9.9815902077)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.3921419658, 9.9815902077), (-4.0415036147, 1.206415527))
                Line((-4.0415036147, 1.206415527), (-3.0804691082, 0.2582046553))
                _nurbs_edge([(-3.0804691082, 0.2582046553), (-2.8524234807, 0.7563585521), (-2.3895682828, 1.7516232421), (-1.6750021891, 3.2413922828), (-0.6788617519, 5.2210602738), (0.6739987327, 7.6790385989), (1.8967181689, 9.6237646445), (2.9324276414, 11.0640084667), (3.6840827731, 12.0147357919), (4.0752196485, 12.487738525)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((2.4668209785, 14.5825147459), (4.0752196485, 12.487738525))
            make_face()
        # Symmetric extrude, each_side=7
        extrude(amount=7, both=True)
    return part.part


def model_25436_61a7f978_0006():
    """Model: Short Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1075210086, perimeter: 1.1623892818
            Circle(0.185)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.16, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0283528737, perimeter: 0.5969026042
            Circle(0.095)
        # OneSide extrude, distance=0.43
        extrude(amount=0.43, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0175, perimeter: 0.8
            with BuildLine():
                Line((0.1, -0.025), (0.1, 0.025))
                Line((0.1, 0.025), (0.025, 0.025))
                Line((0.025, 0.1), (0.025, 0.025))
                Line((-0.025, 0.1), (0.025, 0.1))
                Line((-0.025, 0.025), (-0.025, 0.1))
                Line((-0.025, 0.025), (-0.1, 0.025))
                Line((-0.1, 0.025), (-0.1, -0.025))
                Line((-0.1, -0.025), (-0.025, -0.025))
                Line((-0.025, -0.1), (-0.025, -0.025))
                Line((0.025, -0.1), (-0.025, -0.1))
                Line((0.025, -0.025), (0.025, -0.1))
                Line((0.025, -0.025), (0.1, -0.025))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_25436_61a7f978_0007():
    """Model: Long Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1075210086, perimeter: 1.1623892818
            Circle(0.185)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0283528737, perimeter: 0.5969026042
            Circle(0.095)
        # OneSide extrude, distance=0.66
        extrude(amount=0.66, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.16, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0175, perimeter: 0.8
            with BuildLine():
                Line((-0.025, -0.1), (0.025, -0.1))
                Line((0.025, -0.1), (0.025, -0.025))
                Line((0.1, -0.025), (0.025, -0.025))
                Line((0.1, 0.025), (0.1, -0.025))
                Line((0.025, 0.025), (0.1, 0.025))
                Line((0.025, 0.025), (0.025, 0.1))
                Line((0.025, 0.1), (-0.025, 0.1))
                Line((-0.025, 0.1), (-0.025, 0.025))
                Line((-0.1, 0.025), (-0.025, 0.025))
                Line((-0.1, -0.025), (-0.1, 0.025))
                Line((-0.025, -0.025), (-0.1, -0.025))
                Line((-0.025, -0.025), (-0.025, -0.1))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_25474_5422a377_0001():
    """Model: KOREK_WLEWOWY v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5429650903, perimeter: 3.5931592772
            with BuildLine():
                Line((-0.75, 2.1), (-0.75, 2.3848480035))
                Line((0.75, 2.1), (-0.75, 2.1))
                Line((0.75, 2.3848480035), (0.75, 2.1))
                CenterArc((0, 0), 2.5, 72.5423968763, 17.4576031237)
                CenterArc((0, 0), 2.5, 90, 17.4576031237)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_25474_5422a377_0011():
    """Model: POKRYWA_SILNIKA v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 109.9557428756, perimeter: 43.9822971503
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.1238898038, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, -5)):
                Circle(0.25)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_25560_7660b86f_0006():
    """Model: biodra"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 490.8738521234, perimeter: 78.5398163397
            with Locations((0, 50.265463403)):
                Circle(12.5)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            with Locations((0, 50.265463403)):
                Circle(7.5)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(16, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((0, 50.265463403)):
                Circle(3)
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)
    return part.part


def model_25837_b59623dc_0001():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 63.2749939803, perimeter: 28.1981741426
            with Locations((-1.5021601549, 8.4860505551)):
                Circle(4.487878801)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.2594664188, perimeter: 8.129723504
            with Locations((1.7664666871, -6.4467555131)):
                Circle(1.2938856816)
        # OneSide extrude, distance=13
        extrude(amount=13, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7353926776, perimeter: 8.4895859738
            with Locations((1.7471485313, 3.4844825512)):
                Circle(1.3511595725)
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.SUBTRACT)
    return part.part


def model_26086_bf892d7f_0015():
    """Model: Tractor_Lift_Rod v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.853981634, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-8.5
        extrude(amount=-8.5, mode=Mode.SUBTRACT)
    return part.part


def model_26086_bf892d7f_0030():
    """Model: Tractor_Light v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 188.6919087562, perimeter: 48.6946861306
            Circle(7.75)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 186.2650284313, perimeter: 48.3805268653
            Circle(7.7)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 186.2650284313, perimeter: 48.3805268653
            Circle(7.7)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_26384_83eddf22_0002():
    """Model: Crankcase v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.7436936139, perimeter: 15.8643972252
            with BuildLine():
                Line((0, 4.686), (0, 0))
                Line((0, 0), (2.54, 0))
                Line((2.54, 0), (2.54, 4.686))
                Line((2.54, 4.686), (0, 4.686))
            make_face()
            with BuildLine():
                CenterArc((1.27, 4.381), 0.22479, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.686, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-0.2588016172, 2.2809999962)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-0.2589774743, 0.2590000038)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-2.281, 2.281)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-2.281, 0.259)):
                Circle(0.15875)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_26403_1f4a2618_0004():
    """Model: 05_Manette D"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_26768_c4df841f_0001():
    """Model: Pieza 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.8775435789, perimeter: 18.5353966562
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5132741229, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=3.3
        extrude(amount=3.3, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.9038708404, perimeter: 30.4734487398
            with BuildLine():
                CenterArc((0, 0), 2.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4.5
        extrude(amount=4.5, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 18.7312669192, perimeter: 47.0009343026
            with BuildLine():
                CenterArc((0, 0), 3.75, 111.0394697813, 137.9210604374)
                Line((-1.3462912018, -3.5), (1.3462912018, -3.5))
                CenterArc((0, 0), 3.75, -68.9605302187, 137.9210604374)
                Line((-1.3462912018, 3.5), (1.3462912018, 3.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.2980970389, -2.2980970389), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.2980970389, -2.2980970389), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.2980970389, 2.2980970389), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.2980970389, 2.2980970389), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2.2980970389, -2.2980970389)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.2980970389, -2.2980970389)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2.2980970389, 2.2980970389)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.2980970389, 2.2980970389)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2.2980970389, 2.2980970389)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.2980970389, 2.2980970389)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.2980970389, -2.2980970389)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2.2980970389, -2.2980970389)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_26768_c4df841f_0004():
    """Model: Pasador 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.4137166941, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 19 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.8589889474, perimeter: 3.45
            with BuildLine():
                Line((-0.575, 0), (-0.2875, -0.4979646072))
                Line((-0.2875, -0.4979646072), (0.2875, -0.4979646072))
                Line((0.575, 0), (0.2875, -0.4979646072))
                Line((0.575, 0), (0.2875, 0.4979646072))
                Line((-0.2875, 0.4979646072), (0.2875, 0.4979646072))
                Line((-0.575, 0), (-0.2875, 0.4979646072))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_26768_c4df841f_0005():
    """Model: Rotula"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.5763034994, perimeter: 6.8048391763
            with BuildLine():
                CenterArc((0, 0), 1.1, -59.7273586811, 119.4547173622)
                Line((0.5545268253, 0.95), (-0.5545268253, 0.95))
                CenterArc((0, 0), 1.1, 120.2726413189, 119.4547173622)
                Line((0.5545268253, -0.95), (-0.5545268253, -0.95))
            make_face()
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.65, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.4052818754, perimeter: 5.4977871438
            Circle(0.875)
        # OneSide extrude, distance=3.35
        extrude(amount=3.35, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0772521209, perimeter: 7.9796453401
            with BuildLine():
                CenterArc((5, 0), 0.77, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2948713167, perimeter: 13.6345121166
            with BuildLine():
                CenterArc((5, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, 0), 0.77, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)
    return part.part


def model_26942_279de65e_0019():
    """Model: Rear Axle v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3774.9385429778, perimeter: 352.5767324205
            with BuildLine():
                Line((-76, -40), (-76, -50))
                Line((-76, -50), (-51, -50))
                CenterArc((-51, -60), 10, 21.9864029972, 68.0135970028)
                CenterArc((0, -39.408739718), 45, -158.0135970028, 136.0271940055)
                CenterArc((51, -60), 10, 90, 68.0135970028)
                Line((76, -50), (51, -50))
                Line((76, -40), (76, -50))
                Line((76, -40), (-76, -40))
            make_face()
        # OneSide extrude, distance=25.5
        extrude(amount=25.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1600, perimeter: 160
            with BuildLine():
                Line((-20, 0), (20, 0))
                Line((20, 0), (20, 40))
                Line((-20, 40), (20, 40))
                Line((-20, 0), (-20, 40))
            make_face()
        # OneSide extrude, distance=-25
        extrude(amount=-25, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(76, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 654.129164219, perimeter: 104.817479436
            with BuildLine():
                Line((-81.908739718, 23), (-81.908739718, 2.5))
                Line((-81.908739718, 2.5), (-50, 2.5))
                Line((-50, 23), (-50, 2.5))
                Line((-50, 23), (-81.908739718, 23))
            make_face()
            # Profile area: 153.75, perimeter: 56
            with BuildLine():
                Line((-50, 23), (-50, 2.5))
                Line((-50, 2.5), (-42.5, 2.5))
                Line((-42.5, 2.5), (-42.5, 23))
                Line((-42.5, 23), (-50, 23))
            make_face()
        # OneSide extrude, distance=-54
        extrude(amount=-54, mode=Mode.SUBTRACT)
    return part.part


def model_27036_aead8e6e_0005():
    """Model: 17 v7 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.7878753513, perimeter: 27.1496322342
            with BuildLine():
                CenterArc((-0.427894227, -1.5961305625), 0.6, 158.2613633477, 21.7386366523)
                Line((-1.027894227, -1.5961305625), (-1.027894227, -13.8961305625))
                Line((-1.027894227, -13.8961305625), (0.172105773, -13.8961305625))
                Line((0.172105773, -13.8961305625), (0.172105773, -1.6832190149))
                CenterArc((0.2386234693, 0.8854661668), 2.5695462959, -118.4433321408, 26.9599539022)
            make_face()
            # Profile area: 2.6195018691, perimeter: 11.4274792518
            with BuildLine():
                Line((-0.5332513739, -0.6688301541), (-0.2540297171, -0.9480518109))
                CenterArc((0.2386234693, 0.8854661668), 1.7354042258, -135.1379100974, 18.7285814364)
                Line((-0.9914427197, -0.3386927271), (-0.7067417701, 0.7238256818))
                CenterArc((-0.012163987, -0.8497992348), 1.7200969958, 113.816046056, 54.2124837276)
                CenterArc((-1.2057251014, -0.5967210943), 0.5, 168.0285297837, 57.7122356081)
                CenterArc((0.2386234693, 0.8854661668), 2.5695462959, -134.2592346083, 14.7281647106)
                CenterArc((0.2386234693, 0.8854661668), 2.5695462959, -119.5310698976, 1.0877377569)
                CenterArc((-0.427894227, -1.5961305625), 0.6, 0, 158.2613633477)
                Line((0.172105773, -1.6832190149), (0.172105773, -1.5961305625))
                CenterArc((0.2386234693, 0.8854661668), 2.5695462959, -91.4833782385, 12.3671522898)
                CenterArc((0.6293897133, -1.1468535948), 0.5, -79.1162259487, 57.9011345799)
                CenterArc((-0.6369582539, -0.6552858201), 1.8584093828, -21.2150913688, 51.1470290066)
                Line((0.97357416, 0.2720063547), (0.6888732104, -0.7905120542))
                CenterArc((0.2386234693, 0.8854661668), 1.7354042258, -93.7265888377, 18.7639881763)
                Line((-0.2540297171, -0.9480518109), (0.1258301831, -0.8462686574))
            make_face()
            # Profile area: 0.0517923624, perimeter: 1.4751655247
            with BuildLine():
                Line((-0.2540297171, -0.9480518109), (0.1258301831, -0.8462686574))
                CenterArc((0.2386234693, 0.8854661668), 1.7354042258, -116.409328661, 22.6827398233)
                Line((-0.5332513739, -0.6688301541), (-0.2540297171, -0.9480518109))
            make_face()
            # Profile area: 0.5376113264, perimeter: 2.9534717897
            with BuildLine():
                CenterArc((0.2386234693, 0.8854661668), 2.5695462959, -118.4433321408, 26.9599539022)
                Line((0.172105773, -1.6832190149), (0.172105773, -1.5961305625))
                CenterArc((-0.427894227, -1.5961305625), 0.6, 0, 158.2613633477)
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14.7878753513, perimeter: 27.1496322342
            with BuildLine():
                CenterArc((0.427894227, 1.5961305625), 0.6, -21.7386366523, 21.7386366523)
                Line((1.027894227, 1.5961305625), (1.027894227, 13.8961305625))
                Line((1.027894227, 13.8961305625), (-0.172105773, 13.8961305625))
                Line((-0.172105773, 13.8961305625), (-0.172105773, 1.6832190149))
                CenterArc((-0.2386234693, -0.8854661668), 2.5695462959, 61.5566678592, 26.9599539022)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.3264701276, perimeter: 23.3820175855
            with BuildLine():
                CenterArc((0.427894227, 12.9961305625), 0.375, 0, 180)
                Line((0.052894227, 12.9961305625), (0.052894227, 2.4832190149))
                CenterArc((0.427894227, 2.4832190149), 0.375, 180, 180)
                Line((0.802894227, 2.4832190149), (0.802894227, 12.9961305625))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_27054_342fcf5c_0048():
    """Model: 14 - Greaser v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.55, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.07
        extrude(amount=0.07, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2624925752, perimeter: 6.9521044302
            with BuildLine():
                Line((0, 0.6350852961), (-0.55, 0.3175426481))
                Line((-0.55, 0.3175426481), (-0.55, -0.3175426481))
                Line((-0.55, -0.3175426481), (0, -0.6350852961))
                Line((0, -0.6350852961), (0.55, -0.3175426481))
                Line((0.55, -0.3175426481), (0.55, 0.3175426481))
                Line((0.55, 0.3175426481), (0, 0.6350852961))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_27663_023746a1_0002():
    """Model: 14pinDipSocket v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0211780211, perimeter: 9.5391609874
            with BuildLine():
                CenterArc((0.88265, 0), 0.0889, 90, 180)
                Line((0.88265, 0.0889), (0.88265, 0.508))
                Line((0.88265, 0.508), (-0.88265, 0.508))
                Line((-0.88265, 0.508), (-0.88265, -0.508))
                Line((-0.88265, -0.508), (0.88265, -0.508))
                Line((0.88265, -0.508), (0.88265, -0.0889))
            make_face()
            with BuildLine():
                Line((0.75565, -0.15875), (0.75565, 0.15875))
                CenterArc((0.6604, -0.15875), 0.09525, -90, 90)
                Line((-0.6604, -0.254), (0.6604, -0.254))
                CenterArc((-0.6604, -0.15875), 0.09525, 180, 90)
                Line((-0.75565, 0.15875), (-0.75565, -0.15875))
                CenterArc((-0.6604, 0.15875), 0.09525, 90, 90)
                Line((0.6604, 0.254), (-0.6604, 0.254))
                CenterArc((0.6604, 0.15875), 0.09525, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.087612728, perimeter: 1.9407989266
            with BuildLine():
                Line((0.44958, 0.508), (-0.44958, 0.508))
                Line((-0.41275, 0.4064), (-0.44958, 0.508))
                Line((0.41275, 0.4064), (-0.41275, 0.4064))
                Line((0.44958, 0.508), (0.41275, 0.4064))
            make_face()
        # Symmetric extrude, each_side=1.143
        extrude(amount=1.143, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0020268299, perimeter: 0.1595929068
            with Locations((0.762, 0.381)):
                Circle(0.0254)
            # Profile area: 0.0020268299, perimeter: 0.1595929068
            with Locations((0.762, -0.381)):
                Circle(0.0254)
        # OneSide extrude, distance=-0.1524
        extrude(amount=-0.1524)
    return part.part


def model_27679_501db761_0005():
    """Model: 13_4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3778714795, perimeter: 5.4663712172
            Circle(0.87)
        # OneSide extrude, distance=0.13
        extrude(amount=0.13, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.73, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7637211741, perimeter: 11.7495565244
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.87, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.3778714795, perimeter: 5.4663712172
            Circle(0.87)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)
    return part.part


def model_27679_501db761_0008():
    """Model: 21_17"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=5.6
        extrude(amount=5.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=5.4
        extrude(amount=5.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.138544236, perimeter: 1.3194689145
            Circle(0.21)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_27679_501db761_0017():
    """Model: paraf"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4137166941, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8660254296, perimeter: 3.4641016668
            with BuildLine():
                Line((-0.2886751389, -0.5000000075), (0.2886751389, -0.5000000075))
                Line((0.2886751389, -0.5000000075), (0.5773502778, 0))
                Line((0.5773502778, 0), (0.2886751389, 0.5000000075))
                Line((0.2886751389, 0.5000000075), (-0.2886751389, 0.5000000075))
                Line((-0.2886751389, 0.5000000075), (-0.5773502778, 0))
                Line((-0.5773502778, 0), (-0.2886751389, -0.5000000075))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_27694_7801dc67_0000():
    """Model: Small piston"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.0061935859, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((2.5, 2.5), 2.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.25, 65.7976797718, 47.1593104122)
                CenterArc((2.5, 2.5), 0.25, -65.7976797718, 131.5953595436)
                CenterArc((2.5, 2.5), 0.25, -112.9569901839, 47.1593104122)
                CenterArc((2.5, 2.5), 0.25, 112.9569901839, 134.0860196321)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0972599507, perimeter: 1.3279933282
            with BuildLine():
                Line((2.4024899926, 2.7301994754), (2.4024899926, 2.2698005246))
                CenterArc((2.5, 2.5), 0.25, -112.9569901839, 47.1593104122)
                Line((2.6024899926, 2.7280258788), (2.6024899926, 2.2719741212))
                CenterArc((2.5, 2.5), 0.25, 65.7976797718, 47.1593104122)
            make_face()
            # Profile area: 0.0506858263, perimeter: 1.0454595816
            with BuildLine():
                CenterArc((2.5, 2.5), 0.25, 112.9569901839, 134.0860196321)
                Line((2.4024899926, 2.7301994754), (2.4024899926, 2.2698005246))
            make_face()
            # Profile area: 0.0484037639, perimeter: 1.0302448338
            with BuildLine():
                CenterArc((2.5, 2.5), 0.25, -65.7976797718, 131.5953595436)
                Line((2.6024899926, 2.7280258788), (2.6024899926, 2.2719741212))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0972599507, perimeter: 1.3279933282
            with BuildLine():
                Line((2.4024899926, 2.7301994754), (2.4024899926, 2.2698005246))
                CenterArc((2.5, 2.5), 0.25, -112.9569901839, 47.1593104122)
                Line((2.6024899926, 2.7280258788), (2.6024899926, 2.2719741212))
                CenterArc((2.5, 2.5), 0.25, 65.7976797718, 47.1593104122)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.6024899926, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0416710222, perimeter: 1.4252648486
            with BuildLine():
                Line((2.7280258788, 0.6024899926), (2.7280258788, 0.8))
                Line((2.7280258788, 0.8), (2.2719741212, 0.8))
                Line((2.2719741212, 0.8), (2.2719741212, 0.6024899926))
                CenterArc((2.5, 0.5), 0.25, 24.2023202282, 131.5953595436)
            make_face()
            # Profile area: 0.248260582, perimeter: 3.3028086945
            with BuildLine():
                CenterArc((2.5, 0.5), 0.25, 0, 24.2023202282)
                Line((2.75, 0.5), (3.0000000447, 0.5))
                Line((3.0000000447, 0.5), (3.0000000447, 0.9000000134))
                Line((3.0000000447, 0.9000000134), (2.0297341407, 0.9000000134))
                Line((2.0297341407, 0.9000000134), (2.0297341407, 0.5))
                Line((2.0297341407, 0.5), (2.25, 0.5))
                CenterArc((2.5, 0.5), 0.25, 155.7976797718, 24.2023202282)
                Line((2.2719741212, 0.8), (2.2719741212, 0.6024899926))
                Line((2.7280258788, 0.8), (2.2719741212, 0.8))
                Line((2.7280258788, 0.6024899926), (2.7280258788, 0.8))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.6024899926, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                Line((2.375, 0.5), (2.625, 0.5))
                CenterArc((2.5, 0.5), 0.125, 180, 180)
            make_face()
            # Profile area: 0.0245436926, perimeter: 0.6426990817
            with BuildLine():
                CenterArc((2.5, 0.5), 0.125, 0, 180)
                Line((2.375, 0.5), (2.625, 0.5))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_27694_7801dc67_0017():
    """Model: Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1, 1)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3561944902, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((1, 1), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, 1), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((1, 1), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((1, 1), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1, 1)):
                Circle(0.25)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.2831857145, perimeter: 12.5663708859
            with BuildLine():
                CenterArc((1, -1), 1.5000000432, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, -1), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1, -1)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_27725_5cceaeb7_0006():
    """Model: Release"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4336904421, perimeter: 15.2343793452
            with BuildLine():
                CenterArc((0, 0), 2.54, 180, 180)
                Line((1.905, 0), (2.54, 0))
                CenterArc((0, 0), 1.905, 180, 180)
                Line((-2.54, 0), (-1.905, 0))
            make_face()
        # OneSide extrude, distance=4.318
        extrude(amount=4.318)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.1458076916, perimeter: 8.9536064993
            with BuildLine():
                Line((-3.103755587, 2.5215760908), (-2.8876883765, 1.9882005432))
                CenterArc((-2.5757446469, 2.1145670626), 0.3365670626, -157.9474279818, 67.9474279818)
                Line((-2.1748640669, 1.778), (-2.5757446469, 1.778))
                Line((-2.1748640669, 4.318), (-2.1748640669, 1.778))
                Line((-2.1748640669, 4.318), (-4.5561140669, 4.318))
                Line((-4.5561140669, 4.318), (-4.5561140669, 3.8099999995))
                CenterArc((-3.7971826748, 3.7416835191), 0.7619999997, 174.856287714, 95.143712286)
                CenterArc((-3.7837819839, 2.2461015076), 0.7337043999, 22.0525720182, 68.9939607854)
            make_face()
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0566902092, perimeter: 1.7005330875
            with BuildLine():
                Line((-4.3588322669, 4.17068), (-3.5892122669, 4.318))
                Line((-3.5892122669, 4.318), (-4.3588322669, 4.318))
                Line((-4.3588322669, 4.318), (-4.3588322669, 4.17068))
            make_face()
        # Symmetric extrude, each_side=0.508
        extrude(amount=0.508, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_27835_ab6ef1dc_0002():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.125036173, perimeter: 1.2534954688
            Circle(0.1995)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1577071658, perimeter: 3.1384510609
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1995, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.125036173, perimeter: 1.2534954688
            Circle(0.1995)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1577071658, perimeter: 3.1384510609
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1995, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.125036173, perimeter: 1.2534954688
            Circle(0.1995)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_27835_ab6ef1dc_0003():
    """Model: Component10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0956622817, perimeter: 1.0964158361
            with Locations((0.9000000134, -0.5000000075)):
                Circle(0.1745)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0633808464, perimeter: 2.5101325302
            with BuildLine():
                CenterArc((-0.9000000134, 0.5000000075), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.9000000134, 0.5000000075), 0.1745, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0956622817, perimeter: 1.0964158361
            with Locations((-0.9000000134, 0.5000000075)):
                Circle(0.1745)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0633808464, perimeter: 2.5101325302
            with BuildLine():
                CenterArc((0.9000000134, 0.5000000075), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.9000000134, 0.5000000075), 0.1745, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0956622817, perimeter: 1.0964158361
            with Locations((0.9000000134, 0.5000000075)):
                Circle(0.1745)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_27839_4a077326_0012():
    """Model: Zatyczka stelaza"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((0, 17.5)):
                Circle(0.9)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7775441818, perimeter: 10.3672557568
            with BuildLine():
                CenterArc((0, 17.5), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 17.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 17.5)):
                Circle(0.6)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_27839_4a077326_0014():
    """Model: Sruba rolki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2, 12)):
                Circle(0.5)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2252211349, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((-2, 12), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2, 12), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2, 12)):
                Circle(0.5)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6495190528, perimeter: 3
            with BuildLine():
                Line((-2.4330127019, 11.75), (-2, 11.5))
                Line((-2, 11.5), (-1.5669872981, 11.75))
                Line((-1.5669872981, 11.75), (-1.5669872981, 12.25))
                Line((-1.5669872981, 12.25), (-2, 12.5))
                Line((-2, 12.5), (-2.4330127019, 12.25))
                Line((-2.4330127019, 12.25), (-2.4330127019, 11.75))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_27839_4a077326_0017():
    """Model: Zatyczka prawej raczki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2566370614, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_27872_07f8a3a0_0003():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 46 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.4203663446, perimeter: 16.7786335649
            with BuildLine():
                CenterArc((14.2324720715, 2.1503150542), 0.9, 25.0061570309, 39.2992247708)
                CenterArc((14.4926167381, 2.6909857048), 0.3, 64.3053818017, 119.4646181983)
                Line((14.1932659284, 2.6712602717), (14.2154110146, 2.3351890959))
                CenterArc((14.3176720715, 2.3419274897), 0.1024828264, -176.23, 70.9818537234)
                CenterArc((14.2387720715, 2.0524887397), 0.1975171736, 35.396020189, 39.3558335344)
                Line((13.9733433614, -0.7814457674), (14.399781757, 2.166895536))
                CenterArc((13.6726720715, -0.7379576603), 0.3038, -75.4599397325, 67.2299397325)
                CenterArc((14, -2), 1, 104.5400602675, 251.6445193463)
                CenterArc((15.2971186741, -2.0865051756), 0.3, 159.2931944591, 16.8913851546)
                CenterArc((8.9363848102, 0.3178793012), 6.5, -20.7068055409, 40.6106750363)
            make_face()
            with BuildLine():
                CenterArc((14, -2), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0009810414, perimeter: 9.9216551229
            with BuildLine():
                CenterArc((14.2324720715, 2.1503150542), 0.7, 25.6955601247, 38.609821677)
                CenterArc((14.4926167381, 2.6909857048), 0.1, 64.3053818017, 119.4646181983)
                Line((14.3928331349, 2.6844105604), (14.4108607442, 2.4108257208))
                CenterArc((14.2387720715, 2.0524887397), 0.3975171736, 22.1385086772, 42.2091908646)
                Line((14.6069825142, 2.2022918547), (14.1712836443, -0.8100751994))
                CenterArc((13.6726720715, -0.7379576603), 0.5038, -38.6076202816, 30.3776202816)
                CenterArc((14, -2), 0.95, 18.1146957021, 67.8797645169)
                CenterArc((8.9363848102, 0.3178793012), 6.3, -18.7253809239, 38.5437409975)
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14.3071639999, 0.9427567835, 0), x_dir=(0, 0, 1), z_dir=(-0.9978360324, -0.0657514437, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.5, 1.5638520253)):
                Circle(0.05)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_27975_30e87eca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3521342739, perimeter: 2.1035802319
            Circle(0.3347951921)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.4386985704, perimeter: 5.4138825342
            with BuildLine():
                Line((-0.0502375795, -0.5494250534), (0.450697264, -0.3182195467))
                Line((0.450697264, -0.3182195467), (0.5009348434, 0.2312055067))
                Line((0.5009348434, 0.2312055067), (0.0502375795, 0.5494250534))
                Line((0.0502375795, 0.5494250534), (-0.450697264, 0.3182195467))
                Line((-0.450697264, 0.3182195467), (-0.5009348434, -0.2312055067))
                Line((-0.5009348434, -0.2312055067), (-0.0502375795, -0.5494250534))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3347951921, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3521342739, perimeter: 2.1035802319
            Circle(0.3347951921)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_28283_1a9ffb0b_0001():
    """Model: Arm 3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 7.29, perimeter: 10.8
            with BuildLine():
                Line((38.852566172, 3.0494062418), (36.152566172, 3.0494062418))
                Line((38.852566172, 5.7494062418), (38.852566172, 3.0494062418))
                Line((36.152566172, 5.7494062418), (38.852566172, 5.7494062418))
                Line((36.152566172, 3.0494062418), (36.152566172, 5.7494062418))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-37.502566172, 4.3994062418)):
                Circle(0.75)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(36.152566172, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.6902905132, perimeter: 8.9504548655
            with BuildLine():
                Line((5, 5.2494062418), (2.2000276003, 5.2487303437))
                Line((2.2004260178, 3.5982480076), (2.2000276003, 5.2487303437))
                Line((5, 3.5494062418), (2.2004260178, 3.5982480076))
                Line((5, 5.2494062418), (5, 3.5494062418))
            make_face()
        # OneSide extrude, distance=-6.4
        extrude(amount=-6.4, mode=Mode.SUBTRACT)
    return part.part


def model_28300_b3a6ab79_0010():
    """Model: Wejscie pod kabel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((11.5000001714, 0.8000000119)):
                Circle(0.4)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((-11.5000001714, 0.8000000119), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-11.5000001714, 0.8000000119), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-11.5000001714, 0.8000000119)):
                Circle(0.4)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-11.5000001714, 0.8000000119)):
                Circle(0.25)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_28308_4e6832d8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 84, perimeter: 38
            with BuildLine():
                Line((0, 6), (0, -6))
                Line((7, -6), (0, -6))
                Line((7, 6), (7, -6))
                Line((7, 6), (0, 6))
            make_face()
            # Profile area: 64.6862199998, perimeter: 32.2880676922
            with BuildLine():
                Line((0, 6), (-2.5, 6))
                CenterArc((0, 0), 6.5, 112.619864948, 134.7602701039)
                Line((0, -6), (-2.5, -6))
                Line((0, 6), (0, -6))
            make_face()
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5)

        # Sketch4 -> 押し出し2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.5, perimeter: 23
            with BuildLine():
                Line((-6.5, 5), (0, 5))
                Line((-6.5, 0), (-6.5, 5))
                Line((0, 0), (-6.5, 0))
                Line((0, 5), (0, 0))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)
    return part.part


def model_28446_d757d32d_0021():
    """Model: dodatekPolkaDrzwi v22"""
    with BuildPart() as part:
        # Sketch19 -> Extrude9 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 237.9, perimeter: 86.2
            with BuildLine():
                Line((36.6, -6.5), (0, -6.5))
                Line((36.6, 0), (36.6, -6.5))
                Line((0, 0), (36.6, 0))
                Line((0, -6.5), (0, 0))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch31 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 208.86, perimeter: 82.6
            with BuildLine():
                Line((-0.6, 0), (-0.6, 5.9))
                Line((-0.6, 5.9), (-36, 5.9))
                Line((-36, 5.9), (-36, 0))
                Line((-36, 0), (-0.6, 0))
            make_face()
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)

        # Sketch32 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 28.91, perimeter: 21.6
            with BuildLine():
                Line((6.5, 0), (0.6, 0))
                Line((6.5, 0), (6.5, 4.9))
                Line((0.6, 4.9), (6.5, 4.9))
                Line((0.6, 4.9), (0.6, 0))
            make_face()
        # OneSide extrude, distance=-37.5
        extrude(amount=-37.5, mode=Mode.SUBTRACT)
    return part.part


def model_28664_2958a53a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6698591795, perimeter: 8.5256338168
            with BuildLine():
                Line((0, 3.5), (0, 0))
                Line((0, 0), (1.4777777778, 3.1727232529))
                CenterArc((0, 0), 3.5, 65.0250346323, 24.9749653677)
            make_face()
            # Profile area: 11.8546730244, perimeter: 15.4950571318
            with BuildLine():
                Line((0, 0), (1.4777777778, 3.1727232529))
                Line((6.1, 0), (0, 0))
                CenterArc((4.5, 0), 1.6, 0, 65.0250346323)
                Line((1.4777777778, 3.1727232529), (5.1755555556, 1.4503877728))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> 押し出し2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.SUBTRACT)
    return part.part


def model_28720_ef4be90b_0005():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8796452015, perimeter: 11.6146457069
            with BuildLine():
                CenterArc((3, -9), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3, -9), 0.8485282765, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6599989967, perimeter: 16.5999996215
            with BuildLine():
                Line((11.5, -9.5), (4.1000000611, -9.5))
                Line((11.5, -8.6000001281), (11.5, -9.5))
                Line((4.1000000611, -8.6000001281), (11.5, -8.6000001281))
                Line((4.1000000611, -9.5), (4.1000000611, -8.6000001281))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2052481095, perimeter: 1.8852613564
            with BuildLine():
                Line((1.9012770442, -9.2000001371), (1.9012770442, -8.8586464823))
                Line((1.9012770442, -8.8586464823), (1.3000000209, -8.8586464823))
                Line((1.3000000209, -8.8586464823), (1.3000000209, -9.2000001371))
                Line((1.3000000209, -9.2000001371), (1.9012770442, -9.2000001371))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_28894_2ddb6bca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.3296977755, perimeter: 37.289229088
            with BuildLine():
                Line((0.5, 3.8357864376), (0.5, 0.75))
                CenterArc((0, 5.25), 1.5, -70.5287793655, 321.057558731)
                Line((-0.5, 3.8357864376), (-0.5, 0.75))
                Line((-4, 0.75), (-0.5, 0.75))
                Line((-4, -0.75), (-4, 0.75))
                Line((4, -0.75), (-4, -0.75))
                Line((4, 0.75), (4, -0.75))
                Line((0.5, 0.75), (4, 0.75))
            make_face()
            with BuildLine():
                CenterArc((0, 5.25), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 30.1568542495, perimeter: 39.8284271247
            with BuildLine():
                Line((0.5, 7), (0.5, 3.8357864376))
                Line((4.5, 7), (0.5, 7))
                Line((4.5, 3.8357864376), (4.5, 7))
                Line((8, 3.8357864376), (4.5, 3.8357864376))
                Line((8, 7.5), (8, 3.8357864376))
                Line((-2, 7.5), (8, 7.5))
                Line((-2, 0.75), (-2, 7.5))
                Line((0, 0.75), (-2, 0.75))
                Line((0, 3.8357864376), (0, 0.75))
                Line((0.5, 3.8357864376), (0, 3.8357864376))
            make_face()
            # Profile area: 7.3002525317, perimeter: 12.7331256881
            with BuildLine():
                Line((4.5, 2.75), (4.5, 3.8357864376))
                Line((4.5, 2.75), (6, 2.75))
                Line((6, 2.75), (6.5, 0.75))
                Line((6.5, 0.75), (8, 0.75))
                Line((8, 3.8357864376), (8, 0.75))
                Line((8, 3.8357864376), (4.5, 3.8357864376))
            make_face()
        # Symmetric extrude, each_side=-3.5
        extrude(amount=-3.5, both=True, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.125, perimeter: 5.1213203436
            with BuildLine():
                Line((8, -0.75), (8, 0.75))
                Line((8, 0.75), (6.5, 0.75))
                Line((6.5, 0.75), (8, -0.75))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_28901_f6dbf9dc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32, perimeter: 24
            with BuildLine():
                Line((-15, 5), (-15, 1))
                Line((-15, 1), (-7, 1))
                Line((-7, 1), (-7, 5))
                Line((-7, 5), (-15, 5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.125, perimeter: 5.1213203436
            with BuildLine():
                Line((8.5, 1.5), (7, 0))
                Line((7, 1.5), (8.5, 1.5))
                Line((7, 0), (7, 1.5))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_28928_ea3d1075_0000():
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
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 169.6460032938, perimeter: 56.5486677646
            with BuildLine():
                CenterArc((0, 0), 7.5, 87, 6)
                CenterArc((0, 0), 7.5, 93, 354)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9241567832, perimeter: 3.7771811246
            with BuildLine():
                _nurbs_edge([(0.3928531702, 7.4960850387), (0.3967418937, 7.5250376158), (0.403851331, 7.5826068073), (0.412511569, 7.6679527634), (0.4199838146, 7.7796980616), (0.4220611021, 7.9157268906), (0.4161858559, 8.0477561484), (0.4016430735, 8.1754262384), (0.3779298297, 8.2984842242), (0.3452461411, 8.4170307002), (0.3042027776, 8.5313728413), (0.2651950883, 8.6197419653), (0.2326827667, 8.6843809878), (0.2095839386, 8.7267575232), (0.1976785386, 8.7477667547)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 8.75, 88.7054731834, 2.5890536333)
                _nurbs_edge([(-0.3928531702, 7.4960850387), (-0.3967418937, 7.5250376158), (-0.403851331, 7.5826068073), (-0.412511569, 7.6679527634), (-0.4199838146, 7.7796980616), (-0.4220611021, 7.9157268906), (-0.4161858559, 8.0477561484), (-0.4016430735, 8.1754262384), (-0.3779298297, 8.2984842242), (-0.3452461411, 8.4170307002), (-0.3042027776, 8.5313728413), (-0.2651950883, 8.6197419653), (-0.2326827667, 8.6843809878), (-0.2095839386, 8.7267575232), (-0.1976785386, 8.7477667547)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.3925196718, 7.4897215107), (-0.3928531702, 7.4960850387))
                CenterArc((0, 0), 7.5, 87, 6)
                Line((0.3925196718, 7.4897215107), (0.3928531702, 7.4960850387))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 65.3843971028, perimeter: 58.1194640914
            with BuildLine():
                CenterArc((0, 0), 5.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 65.3843971028, perimeter: 58.1194640914
            with BuildLine():
                CenterArc((0, 0), 5.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_28941_e88e96e5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.3296977755, perimeter: 37.289229088
            with BuildLine():
                CenterArc((-4, 6), 1.5, -70.5287793655, 321.057558731)
                Line((-4.5, 1.5), (-4.5, 4.5857864376))
                Line((-8, 1.5), (-4.5, 1.5))
                Line((-8, 0), (-8, 1.5))
                Line((0, 0), (-8, 0))
                Line((0, 0), (0, 1.5))
                Line((-3.5, 1.5), (0, 1.5))
                Line((-3.5, 1.5), (-3.5, 4.5857864376))
            make_face()
            with BuildLine():
                CenterArc((-4, 6), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


def model_28943_72aa939d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.3517687778, perimeter: 25.4438202052
            with BuildLine():
                CenterArc((0, 0), 2.5495097568, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-1, 1), (-1, -1))
                Line((-1, -1), (1, -1))
                Line((1, -1), (1, 1))
                Line((1, 1), (-1, 1))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_29442_365e23df_0007():
    """Model: SA-208-Steering Wheel & Column"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_29592_2cae5105_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0506707479, perimeter: 0.797964534
            Circle(0.127)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0222951291, perimeter: 1.7555219748
            with BuildLine():
                CenterArc((0, 0), 0.1524, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0506707479, perimeter: 0.797964534
            Circle(0.127)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0285022957, perimeter: 0.5984734005
            Circle(0.09525)
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


def model_29592_cbd4536f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 51 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((-8.2737685136, -1.3241409726), (-8.2737685136, 2.0625256941))
                Line((-8.2737685136, 2.0625256941), (-9.0357685136, 0.3691923607))
                Line((-9.0357685136, 0.3691923607), (-8.2737685136, -1.3241409726))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((-4.8871018469, 5.4491923607), (-1.5004351802, 5.4491923607))
                Line((-3.1937685136, 6.2111923607), (-1.5004351802, 5.4491923607))
                Line((-4.8871018469, 5.4491923607), (-3.1937685136, 6.2111923607))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((-8.2737685136, 5.4491923607), (-6.5804351802, 6.2111923607))
                Line((-8.2737685136, 5.4491923607), (-4.8871018469, 5.4491923607))
                Line((-6.5804351802, 6.2111923607), (-4.8871018469, 5.4491923607))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((-1.5004351802, -4.7108076393), (-4.8871018469, -4.7108076393))
                Line((-4.8871018469, -4.7108076393), (-3.1937685136, -5.4728076393))
                Line((-3.1937685136, -5.4728076393), (-1.5004351802, -4.7108076393))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((1.8862314864, -1.3241409726), (1.8862314864, -4.7108076393))
                Line((1.8862314864, -4.7108076393), (2.6482314864, -3.0174743059))
                Line((2.6482314864, -3.0174743059), (1.8862314864, -1.3241409726))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((1.8862314864, 5.4491923607), (1.8862314864, 2.0625256941))
                Line((1.8862314864, 2.0625256941), (2.6482314864, 3.7558590274))
                Line((2.6482314864, 3.7558590274), (1.8862314864, 5.4491923607))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((-8.2737685136, 5.4491923607), (-9.0357685136, 3.7558590274))
                Line((-9.0357685136, 3.7558590274), (-8.2737685136, 2.0625256941))
                Line((-8.2737685136, 2.0625256941), (-8.2737685136, 5.4491923607))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((-4.8871018469, -4.7108076393), (-8.2737685136, -4.7108076393))
                Line((-8.2737685136, -4.7108076393), (-6.5804351802, -5.4728076393))
                Line((-6.5804351802, -5.4728076393), (-4.8871018469, -4.7108076393))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((1.8862314864, 2.0625256941), (1.8862314864, -1.3241409726))
                Line((1.8862314864, -1.3241409726), (2.6482314864, 0.3691923607))
                Line((2.6482314864, 0.3691923607), (1.8862314864, 2.0625256941))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((1.8862314864, -4.7108076393), (-1.5004351802, -4.7108076393))
                Line((-1.5004351802, -4.7108076393), (0.1928981531, -5.4728076393))
                Line((0.1928981531, -5.4728076393), (1.8862314864, -4.7108076393))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((-1.5004351802, 5.4491923607), (1.8862314864, 5.4491923607))
                Line((0.1928981531, 6.2111923607), (1.8862314864, 5.4491923607))
                Line((-1.5004351802, 5.4491923607), (0.1928981531, 6.2111923607))
            make_face()
            # Profile area: 1.29032, perimeter: 7.1004365991
            with BuildLine():
                Line((-8.2737685136, -4.7108076393), (-8.2737685136, -1.3241409726))
                Line((-8.2737685136, -1.3241409726), (-9.0357685136, -3.0174743059))
                Line((-9.0357685136, -3.0174743059), (-8.2737685136, -4.7108076393))
            make_face()
            # Profile area: 103.0229170084, perimeter: 43.831858136
            with BuildLine():
                Line((-8.2737685136, 2.0625256941), (-8.2737685136, 5.4491923607))
                Line((-8.2737685136, -1.3241409726), (-8.2737685136, 2.0625256941))
                Line((-8.2737685136, -4.7108076393), (-8.2737685136, -1.3241409726))
                Line((-4.8871018469, -4.7108076393), (-8.2737685136, -4.7108076393))
                Line((-1.5004351802, -4.7108076393), (-4.8871018469, -4.7108076393))
                Line((1.8862314864, -4.7108076393), (-1.5004351802, -4.7108076393))
                Line((1.8862314864, -1.3241409726), (1.8862314864, -4.7108076393))
                Line((1.8862314864, 2.0625256941), (1.8862314864, -1.3241409726))
                Line((1.8862314864, 5.4491923607), (1.8862314864, 2.0625256941))
                Line((-1.5004351802, 5.4491923607), (1.8862314864, 5.4491923607))
                Line((-4.8871018469, 5.4491923607), (-1.5004351802, 5.4491923607))
                Line((-8.2737685136, 5.4491923607), (-4.8871018469, 5.4491923607))
            make_face()
            with BuildLine():
                CenterArc((0.2987314864, 3.8616923607), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.2987314864, -3.1233076393), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.6862685136, 3.8616923607), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.6862685136, -3.1233076393), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3175, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0182414692, perimeter: 0.4787787204
            with Locations((7.239000231, 4.5720001459)):
                Circle(0.0762)
            # Profile area: 0.0182414692, perimeter: 0.4787787204
            with Locations((6.923278231, 4.5720001459)):
                Circle(0.0762)
            # Profile area: 0.0182414692, perimeter: 0.4787787204
            with Locations((6.607302231, 4.5720001459)):
                Circle(0.0762)
            # Profile area: 0.0182414692, perimeter: 0.4787787204
            with Locations((6.291580231, 4.5720001459)):
                Circle(0.0762)
        # OneSide extrude, distance=-1.17475
        extrude(amount=-1.17475, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.012667687, perimeter: 0.398982267
            with Locations((-3.0480001378, -0.3691923607)):
                Circle(0.0635)
            # Profile area: 0.012667687, perimeter: 0.398982267
            with Locations((-4.3180001378, -0.3691923607)):
                Circle(0.0635)
        # OneSide extrude, distance=-0.0254
        extrude(amount=-0.0254, mode=Mode.SUBTRACT)
    return part.part


def model_29746_74549e58_0003():
    """Model: Pieza 4 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8721320344, perimeter: 11.9284271247
            with BuildLine():
                Line((-2.4449420449, -0.150000006), (-1.5828100106, -0.150000006))
                Line((-1.5828100106, -0.150000006), (-1.0828100106, 0.349999994))
                Line((-1.0828100106, 0.349999994), (-0.2070740793, 0.349999994))
                Line((-0.2070740793, 0.349999994), (0.2929259207, -0.150000006))
                Line((0.2929259207, -0.150000006), (2.0050579551, -0.150000006))
                Line((2.0050579551, -0.150000006), (2.0050579551, -0.550000006))
                Line((2.0050579551, -0.550000006), (2.5550579551, -0.550000006))
                Line((2.5550579551, -0.550000006), (2.5550579551, -0.400000006))
                Line((2.1550579551, -0.400000006), (2.5550579551, -0.400000006))
                Line((2.1550579551, -0.000000006), (2.1550579551, -0.400000006))
                Line((0.3550579551, -0.000000006), (2.1550579551, -0.000000006))
                Line((-0.1449420449, 0.499999994), (0.3550579551, -0.000000006))
                Line((-1.1449420449, 0.499999994), (-0.1449420449, 0.499999994))
                Line((-1.6449420449, -0.000000006), (-1.1449420449, 0.499999994))
                Line((-2.4449420449, -0.000000006), (-1.6449420449, -0.000000006))
                Line((-2.4449420449, -0.150000006), (-2.4449420449, -0.000000006))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.000000006), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((2.0449420449, 0.4)):
                Circle(0.125)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.000000006), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.8000000119, 0.400000006)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_29746_74549e58_0005():
    """Model: Pieza 3 v4"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.9186394664, perimeter: 13.8222911601
            with BuildLine():
                Line((0.0000000105, 2.9000000267), (1.0000000105, 2.9000000267))
                Line((0, 2.5), (0.0000000105, 2.9000000267))
                Line((0, 0), (0, 2.5))
                Line((2.6, 0), (0, 0))
                Line((2.6, 1.5000000267), (2.6, 0))
                Line((2.85, 2.0000000267), (2.6, 1.5000000267))
                Line((2.85, 2.5000000267), (2.85, 2.0000000267))
                Line((1.0000000105, 2.5000000267), (2.85, 2.5000000267))
                Line((1.0000000105, 2.9000000267), (1.0000000105, 2.5000000267))
            make_face()
            with BuildLine():
                CenterArc((1.4000000209, 0.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.1000000313, 1.5000000224), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5000000053, 2.5000000133), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.52, perimeter: 5.6
            with BuildLine():
                Line((2.6, 0), (2.6, 0.2))
                Line((2.6, 0.2), (0, 0.2))
                Line((0, 0.2), (0, 0))
                Line((0, 0), (2.6, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5000000075, 1.2000000179)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-2.1, 1.2000000179)):
                Circle(0.2)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)
    return part.part


def model_30031_782a9f60_0000():
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
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42, perimeter: 26.8
            with BuildLine():
                Line((-4.2, 2.5), (4.2, 2.5))
                Line((-4.2, -2.5), (-4.2, 2.5))
                Line((4.2, -2.5), (-4.2, -2.5))
                Line((4.2, 2.5), (4.2, -2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2.9999997078, -3.5075060678), 0.75, 0, 180)
                CenterArc((2.9999997078, -3.5075060678), 0.75, 180, 180)
            make_face()
            with BuildLine():
                CenterArc((2.9999997078, -3.5075060678), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6276861678, perimeter: 5.8712066257
            with BuildLine():
                Line((2.2499997078, -3.5075060678), (2.2499997078, -2.5))
                CenterArc((2.9999997078, -3.5075060678), 0.75, 0, 180)
                Line((3.7499997078, -3.5075060678), (3.7499997078, -2.5))
                Line((3.7499997078, -2.5), (2.2499997078, -2.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


def model_30261_723e95cf_0002():
    """Model: Component16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.2057504117, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((20, -13), 3, -104.2031452336, 33.6743658681)
                CenterArc((20, -13), 3, -70.5287793655, 326.3256341319)
            make_face()
            with BuildLine():
                CenterArc((20, -13), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 15.0855769671, perimeter: 20.8861958997
            with BuildLine():
                Line((19.2639181913, -15.9082956471), (19.2639181913, -24))
                Line((19.2639181913, -24), (20, -25))
                Line((20, -25), (20.5, -25))
                Line((20.5, -25), (21, -24))
                Line((21, -24), (21, -15.8284271247))
                CenterArc((20, -13), 3, -104.2031452336, 33.6743658681)
            make_face()
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((20, -13)):
                Circle(1.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1265159009, perimeter: 9.6792705196
            with BuildLine():
                CenterArc((-20, 13), 2.4219019231, -153.3045065264, 126.6090130528)
                Line((-17.8362565318, 11.9119636363), (-22.1637434682, 11.9119636363))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3944711182, perimeter: 3.7493149787
            with BuildLine():
                Line((-20.400000304, 20.3000003025), (-21, 19.9142135624))
                Line((-20.9000003114, 20.7000003085), (-20.400000304, 20.3000003025))
                Line((-20.400000304, 20.9000003114), (-20.9000003114, 20.7000003085))
                Line((-21, 21.1291182153), (-20.400000304, 20.9000003114))
                Line((-21, 21.1291182153), (-21, 19.9142135624))
            make_face()
            # Profile area: 0.5767473784, perimeter: 4.6089969614
            with BuildLine():
                Line((-20.5000003055, 22.7897408788), (-21, 21.9481389672))
                Line((-20.75, 22.9939654657), (-20.5000003055, 22.7897408788))
                Line((-20.5000003055, 23.3000003472), (-20.75, 22.9939654657))
                Line((-21, 24), (-20.5000003055, 23.3000003472))
                Line((-21, 24), (-21, 21.9481389672))
            make_face()
            # Profile area: 0.328702098, perimeter: 3.2403481034
            with BuildLine():
                Line((-21, 19.0134311602), (-21, 17.4871361879))
                Line((-20.6774352084, 18), (-21, 17.4871361879))
                Line((-20.6774352084, 18.5117581975), (-20.6774352084, 18))
                Line((-21, 19.0134311602), (-20.6774352084, 18.5117581975))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_30297_fd93a92a_0011():
    """Model: Part 12 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            Circle(0.9525)
        # OneSide extrude, distance=1.11125
        extrude(amount=1.11125)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.11125, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3984694499, perimeter: 5.489995994
            Circle(0.87376)
        # OneSide extrude, distance=-1.03124
        extrude(amount=-1.03124, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            Circle(0.79375)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)
    return part.part


def model_30375_4ff65965_0003():
    """Model: AttachmentPlate"""
    with BuildPart() as part:
        # Sketch29 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1590545549, perimeter: 8.7961356485
            with BuildLine():
                Line((-13.0060935246, -3.2925207938), (-13.0060935246, -4.1966818968))
                Line((-13.0060935246, -3.2925207938), (-16.5000002459, -3.2925207938))
                Line((-16.5000002459, -3.2925207938), (-16.5000002459, -4.1966818968))
                Line((-16.5000002459, -4.1966818968), (-13.0060935246, -4.1966818968))
            make_face()
            # Profile area: 9.9516153586, perimeter: 23.8212473925
            with BuildLine():
                Line((-13.0060935246, -4.1966818968), (-1.9996309314, -4.1966818968))
                Line((-1.9996309314, -4.1966818968), (-1.9996309314, -3.2925207938))
                Line((-1.9996309314, -3.2925207938), (-13.0060935246, -3.2925207938))
                Line((-13.0060935246, -3.2925207938), (-13.0060935246, -4.1966818968))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude1 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.9996309314, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2597528292, perimeter: 3.1162409633
            with BuildLine():
                Line((3.2925207938, -2), (4.1966818968, -2))
                Line((3.0241421233, -2), (3.2925207938, -2))
                CenterArc((3.0241421233, -2.01), 0.01, 90, 135.0000042689)
                Line((3.2000000477, -2.2000000328), (3.017071056, -2.0170710683))
                Line((4.3000000641, -2.2000000328), (3.2000000477, -2.2000000328))
                Line((4.4829290023, -2.0170710673), (4.3000000641, -2.2000000328))
                CenterArc((4.475857934, -2.01), 0.01, -44.9999957311, 134.9999957311)
                Line((4.1966818968, -2), (4.475857934, -2))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.ADD)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.2000000328, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-3.4996309314, -3.7500000559)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-9.4996309314, -3.7500000559)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-15.4996309314, -3.7500000559)):
                Circle(0.2)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_30379_f1d5e193_0005():
    """Model: Motor Controller Housing Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.16, perimeter: 6
            with BuildLine():
                Line((-0.9, 0.6), (0.9, 0.6))
                Line((-0.9, -0.6), (-0.9, 0.6))
                Line((0.9, -0.6), (-0.9, -0.6))
                Line((0.9, 0.6), (0.9, -0.6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -0.6), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.3000000045, 0.6000000089)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, 0.6000000089)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.3000000045, 0.6000000089)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((0.5, -0.5), (0.5, 0.5))
                Line((0.5, 0.5), (-0.5, 0.5))
                Line((-0.5, 0.5), (-0.5, -0.5))
                Line((-0.5, -0.5), (0.5, -0.5))
            make_face()
        # OneSide extrude, distance=-0.95
        extrude(amount=-0.95, mode=Mode.SUBTRACT)
    return part.part


def model_30379_f1d5e193_0013():
    """Model: Flange Attachment"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.16, perimeter: 6
            with BuildLine():
                Line((-0.9, 0.6), (0.9, 0.6))
                Line((-0.9, -0.6), (-0.9, 0.6))
                Line((0.9, -0.6), (-0.9, -0.6))
                Line((0.9, 0.6), (0.9, -0.6))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.9, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0018397241, perimeter: 0.1723135674
            with BuildLine():
                CenterArc((0, 0), 0.2500000037, 90, 8.6269264291)
                Line((-0.0375, 0.2000000037), (-0.0375, 0.2471715029))
                Line((0, 0.2000000037), (-0.0375, 0.2000000037))
                Line((0, 0.2000000037), (0, 0.2500000037))
            make_face()
            # Profile area: 0.1926700984, perimeter: 1.6648552122
            with BuildLine():
                Line((0, 0.2000000037), (-0.0375, 0.2000000037))
                Line((-0.0375, 0.2000000037), (-0.0375, 0.2471715029))
                CenterArc((0, 0), 0.2500000037, 98.6269264291, 342.7461471417)
                Line((0.0375, 0.2471715029), (0.0375, 0.2000000037))
                Line((0.0375, 0.2000000037), (0, 0.2000000037))
            make_face()
            # Profile area: 0.0018397241, perimeter: 0.1723135674
            with BuildLine():
                Line((0, 0.2000000037), (0, 0.2500000037))
                Line((0.0375, 0.2000000037), (0, 0.2000000037))
                Line((0.0375, 0.2471715029), (0.0375, 0.2000000037))
                CenterArc((0, 0), 0.2500000037, 81.3730735709, 8.6269264291)
            make_face()
            # Profile area: 0.0038205517, perimeter: 0.255941138
            with BuildLine():
                CenterArc((0, 0), 0.2500000037, 81.3730735709, 8.6269264291)
                Line((0.0375, 0.3000000037), (0.0375, 0.2471715029))
                Line((-0.0375, 0.3000000037), (0.0375, 0.3000000037))
                Line((-0.0375, 0.2471715029), (-0.0375, 0.3000000037))
                CenterArc((0, 0), 0.2500000037, 90, 8.6269264291)
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_30380_4d422f95_0013():
    """Model: Cylinder Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 228, perimeter: 62
            with BuildLine():
                Line((-6, 9.5), (-6, -9.5))
                Line((-6, -9.5), (6, -9.5))
                Line((6, -9.5), (6, 9.5))
                Line((6, 9.5), (-6, 9.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 76.9768739946, perimeter: 31.1017672705
            with Locations((0, 1.1)):
                Circle(4.95)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_30400_8824ce97_0004():
    """Model: 5.1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0549778714, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.68
        extrude(amount=0.68, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.98, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.131
        extrude(amount=0.131, mode=Mode.ADD)
    return part.part


def model_30400_8824ce97_0012():
    """Model: 3s-1-1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=1.555
        extrude(amount=1.555)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.555, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2290221044, perimeter: 1.6964600329
            Circle(0.27)
        # OneSide extrude, distance=0.175
        extrude(amount=0.175, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.73, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1558229956, perimeter: 3.8955748905
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2290221044, perimeter: 1.6964600329
            Circle(0.27)
        # OneSide extrude, distance=0.58
        extrude(amount=0.58, mode=Mode.ADD)
    return part.part


def model_30400_8824ce97_0018():
    """Model: 18-03-001100-1_18-03-001105-1-solid1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 62.1645787922, perimeter: 36.8194659001
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.4749, -2.4749), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4749, 2.4749), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.4749, -2.4749), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.4749, 2.4749), 0.34, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.0138265833, perimeter: 26.7035375555
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.0138265833, perimeter: 26.7035375555
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4.7
        extrude(amount=-4.7, mode=Mode.ADD)
    return part.part


def model_30400_8824ce97_0042():
    """Model: M8.88 (1) (1)"""
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
    return part.part


def model_30417_0010bc7c_0007():
    """Model: Mobile end"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.6402708335, 0.3914730201, 0.7601829671), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=4.4
        extrude(amount=4.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.6402708335, 0.3914730201, 0.7601829671), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.9163142077, perimeter: 12.7917910899
            with BuildLine():
                Line((-0.5, 1.1), (0, 1.1))
                CenterArc((-2.0491933385, 0), 1.9, 35.3765401519, 289.2469196961)
                Line((0, -1.1), (-0.5, -1.1))
                Line((0, 1.1), (0, -1.1))
            make_face()
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.6402708335, 0.3914730201, 0.7601829671), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            with Locations((-2.0491933385, 0)):
                Circle(0.85)
        # TwoSides extrude (symmetric), distance=0.7
        extrude(amount=0.7, both=True, mode=Mode.ADD)
    return part.part


def model_30418_de83ae84_0001():
    """Model: Part5 Biela"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.001275361, perimeter: 0.2500707752
            with BuildLine():
                CenterArc((0, 0), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0148, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0006881345, perimeter: 0.0929911425
            Circle(0.0148)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0006881345, perimeter: 0.0929911425
            Circle(0.0148)
        # OneSide extrude, distance=0.1812
        extrude(amount=0.1812, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0009375, perimeter: 0.175
            with BuildLine():
                Line((0, 0.3999999911), (-0.0125, 0.3999999911))
                Line((-0.0125, 0.3999999911), (-0.0125, 0.3249999911))
                Line((-0.0125, 0.3249999911), (0, 0.3249999911))
                Line((0, 0.3999999911), (0, 0.3249999911))
            make_face()
            # Profile area: 0.0009375, perimeter: 0.175
            with BuildLine():
                Line((0, 0.3999999911), (0, 0.3249999911))
                Line((0, 0.3249999911), (0.0125, 0.3249999911))
                Line((0.0125, 0.3249999911), (0.0125, 0.3999999911))
                Line((0.0125, 0.3999999911), (0, 0.3999999911))
            make_face()
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            with Locations((0, 0.3749999911)):
                Circle(0.0125)
        # Symmetric extrude, each_side=0.035
        extrude(amount=0.035, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_30426_2cde26de_0004():
    """Model: mozzo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 58.9048622548, perimeter: 78.5398163397
            with BuildLine():
                CenterArc((0, 0), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 95.0331777711, perimeter: 34.5575191895
            Circle(5.5)
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(15, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_30426_2cde26de_0008():
    """Model: CerchioneEsterno"""
    with BuildPart() as part:
        # Sketch1 -> Extrude13 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.6548667765, perimeter: 10.8274333882
            with BuildLine():
                Line((-29.7075464604, 24.4890114807), (-32.794044794, 27.0333243618))
                CenterArc((0, 0), 38.5, 138.5, 2)
                Line((-28.8347952504, 25.5108718563), (-31.8306181335, 28.1613520492))
                CenterArc((0, 0), 42.5, 138.5, 2)
            make_face()
            # Profile area: 5.6548667765, perimeter: 10.8274333882
            with BuildLine():
                Line((-30.5441036012, 23.4373150168), (-33.7175169624, 25.8723607329))
                CenterArc((0, 0), 38.5, 140.5, 2)
                Line((-29.7075464604, 24.4890114807), (-32.794044794, 27.0333243618))
                CenterArc((0, 0), 42.5, 140.5, 2)
            make_face()
            # Profile area: 327.9822730348, perimeter: 171.9911365174
            with BuildLine():
                Line((-28.8347952504, 25.5108718563), (-31.8306181335, 28.1613520492))
                CenterArc((0, 0), 38.5, 22.5, 116)
                Line((35.5693620017, 14.7333121461), (39.2648801317, 16.2640458755))
                CenterArc((0, 0), 42.5, 22.5, 116)
            make_face()
        # Symmetric extrude, each_side=4.5
        extrude(amount=4.5, both=True)

        # Sketch1 -> Extrude14 (Join)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.6548667765, perimeter: 10.8274333882
            with BuildLine():
                Line((35.5693620017, 14.7333121461), (39.2648801317, 16.2640458755))
                CenterArc((0, 0), 38.5, 20.5, 2)
                Line((36.0618792861, 13.4829841785), (39.8085680431, 14.8838137035))
                CenterArc((0, 0), 42.5, 20.5, 2)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude15 (Join)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.6548667765, perimeter: 10.8274333882
            with BuildLine():
                Line((36.0618792861, 13.4829841785), (39.8085680431, 14.8838137035))
                CenterArc((0, 0), 38.5, 18.5, 2)
                Line((36.5104607254, 12.2162292716), (40.3037553463, 13.4854478972))
                CenterArc((0, 0), 42.5, 18.5, 2)
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude16 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.6548667765, perimeter: 10.8274333882
            with BuildLine():
                Line((-31.3434474567, 22.3570637949), (-34.5999095301, 24.6798756177))
                CenterArc((0, 0), 38.5, 142.5, 2)
                Line((-30.5441036012, 23.4373150168), (-33.7175169624, 25.8723607329))
                CenterArc((0, 0), 42.5, 142.5, 2)
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch1 -> Extrude17 (Join)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.6548667765, perimeter: 10.8274333882
            with BuildLine():
                Line((-32.1046041496, 21.2495739345), (-35.4401474379, 23.4573218758))
                CenterArc((0, 0), 38.5, 144.5, 2)
                Line((-31.3434474567, 22.3570637949), (-34.5999095301, 24.6798756177))
                CenterArc((0, 0), 42.5, 144.5, 2)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude19 (Join)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 327.9822730348, perimeter: 171.9911365174
            with BuildLine():
                Line((-5.0252584005, -38.1706271629), (-5.5473631694, -42.1364066084))
                CenterArc((0, 0), 38.5, 146.5, 116)
                Line((-32.1046041496, 21.2495739345), (-35.4401474379, 23.4573218758))
                CenterArc((0, 0), 42.5, 146.5, 116)
            make_face()
        # Symmetric extrude, each_side=4.5
        extrude(amount=4.5, both=True, mode=Mode.ADD)
    return part.part


def model_30426_2cde26de_0032():
    """Model: PortaTavolaSX (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.96, perimeter: 80
            with BuildLine():
                Line((-0.1, 10), (0.1, 10))
                Line((-0.1, -9.8), (-0.1, 10))
                Line((-19.9, -9.8), (-0.1, -9.8))
                Line((-19.9, -10), (-19.9, -9.8))
                Line((0.1, -10), (-19.9, -10))
                Line((0.1, 10), (0.1, -10))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -9.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((17.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((14.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((12.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((9.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((7.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.4, 0)):
                Circle(0.2)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6, perimeter: 40.6
            with BuildLine():
                Line((-0.95, 10), (-0.95, -10))
                Line((-1.25, 10), (-0.95, 10))
                Line((-1.25, -10), (-1.25, 10))
                Line((-0.95, -10), (-1.25, -10))
            make_face()
            # Profile area: 6, perimeter: 40.6
            with BuildLine():
                Line((1.25, -10), (1.25, 10))
                Line((1.25, 10), (0.95, 10))
                Line((0.95, 10), (0.95, -10))
                Line((0.95, -10), (1.25, -10))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)
    return part.part


def model_30445_791b6800_0005():
    """Model: Component14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-8.5, 2.5)):
                Circle(0.2)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0292812431, perimeter: 0.9245686342
            with BuildLine():
                CenterArc((8.5, 2.5), 0.2, 90, 22.024312837)
                Line((8.425, 2.6854049622), (8.425, 2.3145950378))
                CenterArc((8.5, 2.5), 0.2, -112.024312837, 22.024312837)
                Line((8.5, 2.7), (8.5, 2.3))
            make_face()
            # Profile area: 0.0292812431, perimeter: 0.9245686342
            with BuildLine():
                CenterArc((8.5, 2.5), 0.2, 67.975687163, 22.024312837)
                Line((8.5, 2.7), (8.5, 2.3))
                CenterArc((8.5, 2.5), 0.2, -90, 22.024312837)
                Line((8.575, 2.6854049622), (8.575, 2.3145950378))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0754308884, perimeter: 2.0511458435
            with BuildLine():
                CenterArc((-8.5, 2.5), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.5, 2.5), 0.12645, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_30445_791b6800_0011():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.7401998256, perimeter: 14.7978235455
            with BuildLine():
                CenterArc((-7.947822341, 4.1860833779), 1.2999920856, 39.7147172989, 100.5705654021)
                Line((-8.947822341, 3.3554333779), (-8.947822341, 5.0167333779))
                CenterArc((-7.947822341, 4.1860833779), 1.2999920856, -140.2852827011, 100.5705654021)
                Line((-6.947822341, 5.0167333779), (-6.947822341, 3.3554333779))
            make_face()
            with BuildLine():
                CenterArc((-7.347822341, 3.3860734848), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.547822341, 3.3860734848), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.347822341, 4.9860734848), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.547822341, 4.9860734848), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.947822341, 4.1860833779), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((-7.947822341, 4.1860833779), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.947822341, 4.1860833779), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.1
        extrude(amount=2.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((7.947822341, 4.1860833779), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.947822341, 4.1860833779), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)
    return part.part


def model_30445_791b6800_0015():
    """Model: Component18"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((-18, 3)):
                Circle(2)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((18, 3)):
                Circle(0.75)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-18, 3)):
                Circle(0.3)
        # OneSide extrude, distance=-5.4
        extrude(amount=-5.4, mode=Mode.SUBTRACT)
    return part.part


def model_30445_791b6800_0016():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            with Locations((3.5, 2.5)):
                Circle(0.275)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0541265877, perimeter: 0.8660254038
            with BuildLine():
                Line((3.4278312164, 2.375), (3.5721687836, 2.375))
                Line((3.5721687836, 2.375), (3.6443375673, 2.5))
                Line((3.6443375673, 2.5), (3.5721687836, 2.625))
                Line((3.5721687836, 2.625), (3.4278312164, 2.625))
                Line((3.4278312164, 2.625), (3.3556624327, 2.5))
                Line((3.3556624327, 2.5), (3.4278312164, 2.375))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-3.5, 2.5)):
                Circle(0.15)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_30447_4ed3b778_0007():
    """Model: Eccentric Strap Front"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.403285333, perimeter: 7.5855942937
            with BuildLine():
                Line((0.3175, 1.43002), (-0.3175, 1.43002))
                Line((-0.3175, 1.43002), (-0.3175, 1.148169908))
                CenterArc((0, 0), 1.19126, 105.4575597379, 74.5424402621)
                Line((-1.19126, 0), (-0.79248, 0))
                CenterArc((0, 0), 0.79248, 0, 180)
                Line((0.79248, 0), (1.19126, 0))
                CenterArc((0, 0), 1.19126, 0, 74.5424402621)
                Line((0.3175, 1.43002), (0.3175, 1.148169908))
            make_face()
        # Symmetric extrude, each_side=0.238125
        extrude(amount=0.238125, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.238125, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.212736068, perimeter: 5.3972073431
            with BuildLine():
                Line((-0.79248, 0), (-0.87376, 0))
                CenterArc((0, 0), 0.87376, -180, 180)
                Line((0.87376, 0), (0.79248, 0))
                CenterArc((0, 0), 0.79248, 180, 180)
            make_face()
        # OneSide extrude, distance=-0.16129
        extrude(amount=-0.16129, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1401592349, perimeter: 1.4148923365
            with BuildLine():
                Line((-1.07188, -0.19812), (-1.07188, 0.19812))
                Line((-1.07188, 0.19812), (-1.27, 0.19812))
                CenterArc((-1.27, 0), 0.19812, 90, 180)
                Line((-1.27, -0.19812), (-1.07188, -0.19812))
            make_face()
            # Profile area: 0.0473031312, perimeter: 1.03124
            with BuildLine():
                Line((1.19126, -0.19812), (1.07188, -0.19812))
                Line((1.19126, -0.19812), (1.19126, 0.19812))
                Line((1.07188, 0.19812), (1.19126, 0.19812))
                Line((1.07188, -0.19812), (1.07188, 0.19812))
            make_face()
            # Profile area: 0.0928561037, perimeter: 1.1761323365
            with BuildLine():
                Line((1.27, -0.19812), (1.19126, -0.19812))
                CenterArc((1.27, 0), 0.19812, -90, 180)
                Line((1.19126, 0.19812), (1.27, 0.19812))
                Line((1.19126, -0.19812), (1.19126, 0.19812))
            make_face()
        # OneSide extrude, distance=-0.47625
        extrude(amount=-0.47625, mode=Mode.ADD)
    return part.part


def model_30690_3df2c9e2_0002():
    """Model: Anillo por soldar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.1380508779, perimeter: 65.3451271947
            with BuildLine():
                CenterArc((7.3675766323, -19.4749608982), 5.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.3675766323, -19.4749608982), 4.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.5610609652, perimeter: 57.8053048261
            with BuildLine():
                CenterArc((-7.3675766323, 19.4749608982), 4.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.3675766323, 19.4749608982), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.5610609652, perimeter: 57.8053048261
            with BuildLine():
                CenterArc((-7.3675766323, 19.4749608982), 4.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.3675766323, 19.4749608982), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_30690_3df2c9e2_0008():
    """Model: Anillo por soldar 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.6991118431, perimeter: 62.8318530718
            with BuildLine():
                CenterArc((8.6160755219, -29.1989226019), 5.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.6160755219, -29.1989226019), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.5610609652, perimeter: 57.8053048261
            with BuildLine():
                CenterArc((-8.6160755219, 29.1989226019), 4.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.6160755219, 29.1989226019), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 11.5610609652, perimeter: 57.8053048261
            with BuildLine():
                CenterArc((8.6160755219, 29.1989226019), 4.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.6160755219, 29.1989226019), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_30690_3df2c9e2_0009():
    """Model: Anillo por soldar 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30.9132717113, perimeter: 51.5221195189
            with BuildLine():
                CenterArc((29, 8), 4.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((29, 8), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.2991142546, perimeter: 46.4955712731
            with BuildLine():
                CenterArc((29, 8), 3.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((29, 8), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 9.2991142546, perimeter: 46.4955712731
            with BuildLine():
                CenterArc((-29, 8), 3.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-29, 8), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_30690_3df2c9e2_0013():
    """Model: Prisionero"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9103910692, perimeter: 6.0475658582
            with Locations((25, 2.5)):
                Circle(0.9625)
        # OneSide extrude, distance=1.45
        extrude(amount=1.45)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((25, -2.5)):
                Circle(0.6)
        # OneSide extrude, distance=4.2
        extrude(amount=4.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.45, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5772136912, perimeter: 2.8280925586
            with BuildLine():
                Line((-25.4703253742, -2.4689565505), (-25.262047103, -2.8917919973))
                Line((-25.262047103, -2.8917919973), (-24.7917217288, -2.9228354468))
                Line((-24.7917217288, -2.9228354468), (-24.5296746258, -2.5310434495))
                Line((-24.5296746258, -2.5310434495), (-24.737952897, -2.1082080027))
                Line((-24.737952897, -2.1082080027), (-25.2082782712, -2.0771645532))
                Line((-25.2082782712, -2.0771645532), (-25.4703253742, -2.4689565505))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_30729_b4d83b07_0010():
    """Model: 8 Bar v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-85
        extrude(amount=-85)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-85, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 14.7262155637, perimeter: 23.5619449019
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-86.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=23.5
        extrude(amount=23.5, mode=Mode.ADD)
    return part.part


def model_30904_54099e05_0005():
    """Model: Inserto v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1963495558, perimeter: 5.5707963864
            with BuildLine():
                Line((1.0000000149, 0.25), (-1.0000000149, 0.25))
                CenterArc((-1.0000000149, 0), 0.25, 90, 180)
                Line((-1.0000000149, -0.25), (1.0000000149, -0.25))
                CenterArc((1.0000000149, 0), 0.25, -90, 180)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.4430308445, perimeter: 12.9690261014
            with BuildLine():
                CenterArc((-0.75, 0), 0.7, 90, 180)
                Line((-0.75, -0.7), (0.75, -0.7))
                CenterArc((0.75, 0), 0.7, -90, 180)
                Line((0.75, 0.7), (-0.75, 0.7))
            make_face()
            with BuildLine():
                Line((-1.0000000149, -0.25), (1.0000000149, -0.25))
                CenterArc((-1.0000000149, 0), 0.25, 90, 180)
                Line((1.0000000149, 0.25), (-1.0000000149, 0.25))
                CenterArc((1.0000000149, 0), 0.25, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1963495558, perimeter: 5.5707963864
            with BuildLine():
                CenterArc((1.0000000149, 0), 0.25, -90, 180)
                Line((1.0000000149, 0.25), (-1.0000000149, 0.25))
                CenterArc((-1.0000000149, 0), 0.25, 90, 180)
                Line((-1.0000000149, -0.25), (1.0000000149, -0.25))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.2398230292, perimeter: 12.3982298764
            with BuildLine():
                CenterArc((-1.0000000149, 0), 0.4500000067, 89.9999205838, 180.0000794193)
                Line((-1.0000000149, -0.4500000067), (1.0000000149, -0.4500000067))
                CenterArc((1.0000000149, 0), 0.4500000067, -90, 180)
                Line((1.0000000149, 0.4500000067), (-0.9999993912, 0.4500000067))
            make_face()
            with BuildLine():
                Line((-1.0000000149, -0.25), (1.0000000149, -0.25))
                CenterArc((-1.0000000149, 0), 0.25, 90, 180)
                Line((1.0000000149, 0.25), (-1.0000000149, 0.25))
                CenterArc((1.0000000149, 0), 0.25, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1963495558, perimeter: 5.5707963864
            with BuildLine():
                CenterArc((1.0000000149, 0), 0.25, -90, 180)
                Line((1.0000000149, 0.25), (-1.0000000149, 0.25))
                CenterArc((-1.0000000149, 0), 0.25, 90, 180)
                Line((-1.0000000149, -0.25), (1.0000000149, -0.25))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_30905_511b96bf_0018():
    """Model: Osłona na koła v6 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.5394781073, perimeter: 12.2037152674
            with BuildLine():
                CenterArc((-0.0223223616, 0.2853786015), 2.9504287055, -0.4636868095, 79.5869686504)
                Line((3.3765727974, 0.2615014512), (2.9280097262, 0.2615014512))
                Line((3.3765727974, 0.2615014512), (4.4280097262, 2.6307507256))
                Line((4.4280097262, 2.6307507256), (4.4280097262, 3.6518195634))
                Line((1.1921086516, 3.6518195634), (4.4280097262, 3.6518195634))
                Line((0.5344129537, 3.1828042408), (1.1921086516, 3.6518195634))
            make_face()
            # Profile area: 1.4659961482, perimeter: 18.4489455595
            with BuildLine():
                CenterArc((-0.0223223616, 0.2853786015), 2.9504287055, 79.1232818409, 101.3404049686)
                Line((-2.9726544494, 0.2615014512), (-2.8108874251, 0.2615014512))
                CenterArc((-0.0223223616, 0.2853786015), 2.7886672859, -0.4905843959, 180.9811687919)
                Line((2.9280097262, 0.2615014512), (2.7662427019, 0.2615014512))
                CenterArc((-0.0223223616, 0.2853786015), 2.9504287055, -0.4636868095, 79.5869686504)
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3.6518195634, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.75, -2.74466501)):
                Circle(0.6)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_31008_8fa25b35_0006():
    """Model: 3 v24"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.5707963279, perimeter: 30.5663706154
            with BuildLine():
                CenterArc((0, 8.9999999994), 1.0000000008, -0.002201405, 180.0044497514)
                Line((-1, 8.9999607583), (-1, 0.0000023566))
                CenterArc((0, 0), 1, 179.9998649785, 180.0001350205)
                Line((1, 8.9999615776), (1, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 8.9999999994), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5374401408, perimeter: 3.4769079766
            with BuildLine():
                Line((0, 1.9480005849), (0, 0.6))
                Line((0.6, 1.5045340337), (0, 0.6))
                Line((0.6, 1.9480005849), (0.6, 1.5045340337))
                Line((0, 1.9480005849), (0.6, 1.9480005849))
            make_face()
            # Profile area: 1.3000000194, perimeter: 6.2000000775
            with BuildLine():
                Line((0.6341607793, 8.0000001192), (1.1341607793, 8.0000001192))
                Line((1.1341607793, 10.600000158), (1.1341607793, 8.0000001192))
                Line((0.6341607793, 10.600000158), (1.1341607793, 10.600000158))
                Line((0.6341607793, 8.0000001192), (0.6341607793, 10.600000158))
            make_face()
            # Profile area: 6.9174040098, perimeter: 17.4174041066
            with BuildLine():
                Line((0.6, 8.0000001192), (0.6341607793, 8.0000001192))
                Line((0.6341607793, 8.0000001192), (0.6341607793, 10.600000158))
                Line((0.6341607793, 10.600000158), (1.1341607793, 10.600000158))
                Line((1.1341607793, 10.600000158), (1.1341607793, 8.0000001192))
                Line((1.1341607793, 8.0000001192), (2, 8.0000001192))
                Line((2, 8.0000001192), (2, 12.1087021338))
                Line((2, 12.1087021338), (0, 12.1087021338))
                Line((0, 12.1087021338), (0, 8.0000001192))
                Line((0, 8.0000001192), (0.6, 8.0000001192))
            make_face()
            # Profile area: 3.6311997206, perimeter: 13.3039990685
            with BuildLine():
                Line((0, 8.0000001192), (0.6, 8.0000001192))
                Line((0, 8.0000001192), (0, 1.9480005849))
                Line((0, 1.9480005849), (0.6, 1.9480005849))
                Line((0.6, 8.0000001192), (0.6, 1.9480005849))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.5167054005, perimeter: 15.4713556357
            with BuildLine():
                Line((0.6341607793, 1.5560333463), (0.6341607793, 8.0000001192))
                Line((0.6341607793, 1.5560333463), (0.6, 1.5045340337))
                Line((0.6, 1.5045340337), (0.6, 0.6))
                Line((1.1341607793, 1.405277674), (0.6, 0.6))
                Line((1.1341607793, 8.0000001192), (1.1341607793, 1.405277674))
                Line((0.6341607793, 8.0000001192), (1.1341607793, 8.0000001192))
            make_face()
            # Profile area: 0.2713602101, perimeter: 2.5899748742
            with BuildLine():
                Line((0.6, 1.5045340337), (0, 0.6))
                Line((0.6, 0.6), (0, 0.6))
                Line((0.6, 1.5045340337), (0.6, 0.6))
            make_face()
            # Profile area: 1.3000000194, perimeter: 6.2000000775
            with BuildLine():
                Line((0.6341607793, 8.0000001192), (1.1341607793, 8.0000001192))
                Line((1.1341607793, 10.600000158), (1.1341607793, 8.0000001192))
                Line((0.6341607793, 10.600000158), (1.1341607793, 10.600000158))
                Line((0.6341607793, 8.0000001192), (0.6341607793, 10.600000158))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch8 -> Extrude16 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1341607793), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 7.5)):
                Circle(0.5)
            # Profile area: 4.6292039891, perimeter: 11.3415937169
            with BuildLine():
                CenterArc((0, 7.5), 1, -0.000010706, 180.0000214125)
                Line((1, 7.4999998131), (1, 10.600000158))
                Line((1, 10.600000158), (-1, 10.600000158))
                Line((-1, 10.600000158), (-1, 7.4999998131))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


def model_31008_8fa25b35_0008():
    """Model: 1 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 31.2617807017, perimeter: 33.5530964915
            with BuildLine():
                Line((2.38, -3.495), (2.38, 3.495))
                Line((2.38, 3.495), (-2.38, 3.495))
                Line((-2.38, 3.495), (-2.38, -3.495))
                Line((-2.38, -3.495), (2.38, -3.495))
            make_face()
            with BuildLine():
                CenterArc((1.1815, 2.7), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.1815, -2.7), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.1815, -2.7), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.1815, 2.7), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47
        extrude(amount=0.47)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.3393477042, perimeter: 23.006990817
            with BuildLine():
                CenterArc((0.5, -7.25), 0.5, 179.9999141563, 90.0001716741)
                Line((0.500000749, -7.75), (1.879999251, -7.75))
                CenterArc((1.88, -7.25), 0.5, -90.0000858306, 90.0001716612)
                Line((2.38, -7.249999251), (2.38, -0.47))
                Line((-2.38, -0.47), (2.38, -0.47))
                Line((-2.38, -0.47), (-2.38, -4.2099996255))
                CenterArc((-1.38, -4.21), 1, 179.9999785402, 90.0000213963)
                Line((-1.3800000011, -5.21), (-0.500000749, -5.21))
                CenterArc((-0.5, -5.71), 0.5, -0.0000858436, 90.0001716742)
                Line((0, -5.7100007491), (0, -7.2499992509))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-1.3800000011, 3.8244681923)):
                Circle(0.5)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((1.19, 6.5)):
                Circle(0.75)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


def model_31008_8fa25b35_0010():
    """Model: 7 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0647953485, perimeter: 5.1836278784
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0647953485, perimeter: 5.1836278784
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3436116965, perimeter: 3.926990817
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_31008_8fa25b35_0013():
    """Model: 8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=1.1
        extrude(amount=1.1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3455751919, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3455751919, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_31008_8fa25b35_0016():
    """Model: 11 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.8346094772, perimeter: 4.0924201459
            with BuildLine():
                Line((0.2886751346, 0.5), (-0.2886751346, 0.5))
                Line((-0.2886751346, 0.5), (-0.5773502692, 0))
                Line((-0.5773502692, 0), (-0.2886751346, -0.5))
                Line((-0.2886751346, -0.5), (0.2886751346, -0.5))
                Line((0.2886751346, -0.5), (0.5773502692, 0))
                Line((0.5773502692, 0), (0.2886751346, 0.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_31008_8fa25b35_0017():
    """Model: 5 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=1.64
        extrude(amount=1.64, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.64, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1649336143, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -1.64, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1649336143, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_25211_336c083f_0015": {"func": model_25211_336c083f_0015, "volume": 47.2746862512, "area": 233.7344934271},
    "model_25284_3364996e_0000": {"func": model_25284_3364996e_0000, "volume": 5.6834747889, "area": 38.9445002412},
    "model_25284_c88414c8_0000": {"func": model_25284_c88414c8_0000, "volume": 6.0993274993, "area": 41.7405805364},
    "model_25284_da61a614_0000": {"func": model_25284_da61a614_0000, "volume": 6.0857851022, "area": 46.2615143573},
    "model_25285_89960b57_0000": {"func": model_25285_89960b57_0000, "volume": 523.4292036732, "area": 2114},
    "model_25285_992982f8_0000": {"func": model_25285_992982f8_0000, "volume": 558.4292036732, "area": 2254},
    "model_25294_decd8b5a_0000": {"func": model_25294_decd8b5a_0000, "volume": 2418.2789940973, "area": 3564.9917282084},
    "model_25335_d0469c67_0000": {"func": model_25335_d0469c67_0000, "volume": 3.3591479449, "area": 54.1924732744},
    "model_25378_c6523377_0003": {"func": model_25378_c6523377_0003, "volume": 0.126135166, "area": 1.980245413},
    "model_25381_9c263e4d_0000": {"func": model_25381_9c263e4d_0000, "volume": 3.6307065568, "area": 20.4291305957},
    "model_25389_035e5844_0000": {"func": model_25389_035e5844_0000, "volume": 587.9469004941, "area": 616.9646003294},
    "model_25416_b0423b7d_0000": {"func": model_25416_b0423b7d_0000, "volume": 6.2706189364, "area": 63.9628264271},
    "model_25416_bd13dfb0_0000": {"func": model_25416_bd13dfb0_0000, "volume": 0.0519502912, "area": 2.0637589739},
    "model_25425_3ba62cc0_0000": {"func": model_25425_3ba62cc0_0000, "volume": 673.8621160908, "area": 579.3183488261},
    "model_25436_61a7f978_0006": {"func": model_25436_61a7f978_0006, "volume": 0.0285200971, "area": 0.697692422},
    "model_25436_61a7f978_0007": {"func": model_25436_61a7f978_0007, "volume": 0.035041258, "area": 0.834980021},
    "model_25474_5422a377_0001": {"func": model_25474_5422a377_0001, "volume": 23.6899750626, "area": 69.1626165693},
    "model_25474_5422a377_0011": {"func": model_25474_5422a377_0011, "volume": 54.9386015297, "area": 250.6205539401},
    "model_25560_7660b86f_0006": {"func": model_25560_7660b86f_0006, "volume": 6534.5127194668, "area": 2426.8803248981},
    "model_25837_b59623dc_0001": {"func": model_25837_b59623dc_0001, "volume": 180.0648305179, "area": 214.415855924},
    "model_26086_bf892d7f_0015": {"func": model_26086_bf892d7f_0015, "volume": 120.3986686779, "area": 256.8537641613},
    "model_26086_bf892d7f_0030": {"func": model_26086_bf892d7f_0030, "volume": 1776.7984110724, "area": 837.9413005287},
    "model_26384_83eddf22_0002": {"func": model_26384_83eddf22_0002, "volume": 29.5756280397, "area": 66.9748143158},
    "model_26403_1f4a2618_0004": {"func": model_26403_1f4a2618_0004, "volume": 2.6703537556, "area": 18.7867240685},
    "model_26768_c4df841f_0001": {"func": model_26768_c4df841f_0001, "volume": 162.3533417078, "area": 318.1966074657},
    "model_26768_c4df841f_0004": {"func": model_26768_c4df841f_0004, "volume": 7.5950368834, "area": 33.6092894745},
    "model_26768_c4df841f_0005": {"func": model_26768_c4df841f_0005, "volume": 15.8840681372, "area": 52.8030871164},
    "model_26942_279de65e_0019": {"func": model_26942_279de65e_0019, "volume": 119523.4022270563, "area": 23688.4478642359},
    "model_27036_aead8e6e_0005": {"func": model_27036_aead8e6e_0005, "volume": 2.6040841858, "area": 43.5701461423},
    "model_27054_342fcf5c_0048": {"func": model_27054_342fcf5c_0048, "volume": 0.7600806793, "area": 5.0767667125},
    "model_27663_023746a1_0002": {"func": model_27663_023746a1_0002, "volume": 0.4431859285, "area": 6.6172750582},
    "model_27679_501db761_0005": {"func": model_27679_501db761_0005, "volume": 25.7560237864, "area": 59.4150569018},
    "model_27679_501db761_0008": {"func": model_27679_501db761_0008, "volume": 25.6977566675, "area": 67.1986668603},
    "model_27679_501db761_0017": {"func": model_27679_501db761_0017, "volume": 6.1460093732, "area": 28.5340110424},
    "model_27694_7801dc67_0000": {"func": model_27694_7801dc67_0000, "volume": 6.659580575, "area": 33.8193895619},
    "model_27694_7801dc67_0017": {"func": model_27694_7801dc67_0017, "volume": 8.5412052306, "area": 42.2544221411},
    "model_27725_5cceaeb7_0006": {"func": model_27725_5cceaeb7_0006, "volume": 27.9727291223, "area": 91.3315319754},
    "model_27835_ab6ef1dc_0002": {"func": model_27835_ab6ef1dc_0002, "volume": 0.1815848408, "area": 2.5113875965},
    "model_27835_ab6ef1dc_0003": {"func": model_27835_ab6ef1dc_0003, "volume": 0.1274709073, "area": 1.8240071239},
    "model_27839_4a077326_0012": {"func": model_27839_4a077326_0012, "volume": 1.081493271, "area": 11.0269902141},
    "model_27839_4a077326_0014": {"func": model_27839_4a077326_0014, "volume": 6.5093030069, "area": 29.9283161192},
    "model_27839_4a077326_0017": {"func": model_27839_4a077326_0017, "volume": 4.4139376783, "area": 36.1911473694},
    "model_27872_07f8a3a0_0003": {"func": model_27872_07f8a3a0_0003, "volume": 6.9694337902, "area": 33.139030449},
    "model_27975_30e87eca_0000": {"func": model_27975_30e87eca_0000, "volume": 0.8358781189, "area": 6.1508427734},
    "model_28283_1a9ffb0b_0001": {"func": model_28283_1a9ffb0b_0001, "volume": 25.5533614821, "area": 78.8980360908},
    "model_28300_b3a6ab79_0010": {"func": model_28300_b3a6ab79_0010, "volume": 0.8953539063, "area": 9.9745566751},
    "model_28308_4e6832d8_0000": {"func": model_28308_4e6832d8_0000, "volume": 1869.3077024432, "area": 888.0527418141},
    "model_28446_d757d32d_0021": {"func": model_28446_d757d32d_0021, "volume": 20.952, "area": 140.4},
    "model_28664_2958a53a_0000": {"func": model_28664_2958a53a_0000, "volume": 11.3829395503, "area": 38.9281627028},
    "model_28720_ef4be90b_0005": {"func": model_28720_ef4be90b_0005, "volume": 19.3622307692, "area": 90.7395513271},
    "model_28894_2ddb6bca_0000": {"func": model_28894_2ddb6bca_0000, "volume": 130.9866843207, "area": 275.0776121842},
    "model_28901_f6dbf9dc_0000": {"func": model_28901_f6dbf9dc_0000, "volume": 46.3125, "area": 98.6819805153},
    "model_28928_ea3d1075_0000": {"func": model_28928_ea3d1075_0000, "volume": 361.0410031729, "area": 550.0744065682},
    "model_28941_e88e96e5_0000": {"func": model_28941_e88e96e5_0000, "volume": 162.6375822038, "area": 338.9732282553},
    "model_28943_72aa939d_0000": {"func": model_28943_72aa939d_0000, "volume": 80.1836218496, "area": 128.0026787893},
    "model_29442_365e23df_0007": {"func": model_29442_365e23df_0007, "volume": 2.5486170402, "area": 25.855307539},
    "model_29592_2cae5105_0000": {"func": model_29592_2cae5105_0000, "volume": 0.1103634225, "area": 2.1727616704},
    "model_29592_cbd4536f_0000": {"func": model_29592_cbd4536f_0000, "volume": 37.6878018297, "area": 253.838392949},
    "model_29746_74549e58_0003": {"func": model_29746_74549e58_0003, "volume": 0.6856301306, "area": 11.3380566487},
    "model_29746_74549e58_0005": {"func": model_29746_74549e58_0005, "volume": 2.1134624108, "area": 25.0017371648},
    "model_30031_782a9f60_0000": {"func": model_30031_782a9f60_0000, "volume": 210.804716936, "area": 225.7252673839},
    "model_30261_723e95cf_0002": {"func": model_30261_723e95cf_0002, "volume": 11.3800423062, "area": 90.2373056239},
    "model_30297_fd93a92a_0011": {"func": model_30297_fd93a92a_0011, "volume": 0.5355540936, "area": 14.4528782312},
    "model_30375_4ff65965_0003": {"func": model_30375_4ff65965_0003, "volume": 10.2631318354, "area": 64.552606118},
    "model_30379_f1d5e193_0005": {"func": model_30379_f1d5e193_0005, "volume": 1.2052876109, "area": 14.214247781},
    "model_30379_f1d5e193_0013": {"func": model_30379_f1d5e193_0013, "volume": 0.6437393083, "area": 8.4526103368},
    "model_30380_4d422f95_0013": {"func": model_30380_4d422f95_0013, "volume": 151.0231260054, "area": 395.1480192814},
    "model_30400_8824ce97_0004": {"func": model_30400_8824ce97_0004, "volume": 0.2216315077, "area": 2.5029068671},
    "model_30400_8824ce97_0012": {"func": model_30400_8824ce97_0012, "volume": 0.8617231569, "area": 6.0733269179},
    "model_30400_8824ce97_0018": {"func": model_30400_8824ce97_0018, "volume": 99.6084362321, "area": 278.4085692797},
    "model_30400_8824ce97_0042": {"func": model_30400_8824ce97_0042, "volume": 2.2836634279, "area": 12.8537542462},
    "model_30417_0010bc7c_0007": {"func": model_30417_0010bc7c_0007, "volume": 34.4226839781, "area": 78.7356987418},
    "model_30418_de83ae84_0001": {"func": model_30418_de83ae84_0001, "volume": 0.0005595141, "area": 0.0858816469},
    "model_30426_2cde26de_0004": {"func": model_30426_2cde26de_0004, "volume": 3734.5682669549, "area": 1768.7166639711},
    "model_30426_2cde26de_0008": {"func": model_30426_2cde26de_0008, "volume": 6073.3269179198, "area": 4592.4509524165},
    "model_30426_2cde26de_0032": {"func": model_30426_2cde26de_0032, "volume": 64.9280708114, "area": 557.68},
    "model_30445_791b6800_0005": {"func": model_30445_791b6800_0005, "volume": 0.1042966302, "area": 1.5933431107},
    "model_30445_791b6800_0011": {"func": model_30445_791b6800_0011, "volume": 1.8713297956, "area": 26.9051436725},
    "model_30445_791b6800_0015": {"func": model_30445_791b6800_0015, "volume": 38.3352843554, "area": 74.5185777431},
    "model_30445_791b6800_0016": {"func": model_30445_791b6800_0016, "volume": 0.1142919042, "area": 1.9640172645},
    "model_30447_4ed3b778_0007": {"func": model_30447_4ed3b778_0007, "volume": 0.7347294579, "area": 7.3008915922},
    "model_30690_3df2c9e2_0002": {"func": model_30690_3df2c9e2_0002, "volume": 39.7599966238, "area": 159.0902519778},
    "model_30690_3df2c9e2_0008": {"func": model_30690_3df2c9e2_0008, "volume": 39.7599966238, "area": 159.0902519778},
    "model_30690_3df2c9e2_0009": {"func": model_30690_3df2c9e2_0009, "volume": 32.747961821, "area": 130.8159180955},
    "model_30690_3df2c9e2_0013": {"func": model_30690_3df2c9e2_0013, "volume": 8.681548297, "area": 31.8374258862},
    "model_30729_b4d83b07_0010": {"func": model_30729_b4d83b07_0010, "volume": 612.8069169909, "area": 951.9025740377},
    "model_30904_54099e05_0005": {"func": model_30904_54099e05_0005, "volume": 5.8959733844, "area": 31.5353975736},
    "model_30905_511b96bf_0018": {"func": model_30905_511b96bf_0018, "volume": 27.4536732166, "area": 96.4920701181},
    "model_31008_8fa25b35_0006": {"func": model_31008_8fa25b35_0006, "volume": 8.6600690818, "area": 48.5537520016},
    "model_31008_8fa25b35_0008": {"func": model_31008_8fa25b35_0008, "volume": 40.479840603, "area": 151.2080965518},
    "model_31008_8fa25b35_0010": {"func": model_31008_8fa25b35_0010, "volume": 1.0620546665, "area": 6.5580746644},
    "model_31008_8fa25b35_0013": {"func": model_31008_8fa25b35_0013, "volume": 1.9540706305, "area": 10.6185831691},
    "model_31008_8fa25b35_0016": {"func": model_31008_8fa25b35_0016, "volume": 0.525063458, "area": 10.0275253523},
    "model_31008_8fa25b35_0017": {"func": model_31008_8fa25b35_0017, "volume": 2.7661723315, "area": 13.2261050716},
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
