"""Batch 004 - passing/04_6to7ops
90 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_22323_aa6edb8b_0003():
    """Model: Valve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 43.0084034276, perimeter: 23.2477856366
            Circle(3.7)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.0976760488, perimeter: 49.3230046614
            with BuildLine():
                CenterArc((0, 0), 4.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 43.0084034276, perimeter: 23.2477856366
            Circle(3.7)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_22340_ec24cd79_0018():
    """Model: set screw 12 v1 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.4890342854, perimeter: 4.0566370614
            with BuildLine():
                Line((0.8660254038, -0.5), (0, -1))
                Line((0.8660254038, 0.5), (0.8660254038, -0.5))
                Line((0.5196152423, 0.3), (0.8660254038, 0.5))
                CenterArc((0, 0), 0.6, -90, 120)
                Line((0, -0.6), (0, -1))
            make_face()
            # Profile area: 0.4890342854, perimeter: 4.0566370614
            with BuildLine():
                CenterArc((0, 0), 0.6, 150, 120)
                Line((-0.5196152423, 0.3), (-0.8660254038, 0.5))
                Line((-0.8660254038, 0.5), (-0.8660254038, -0.5))
                Line((-0.8660254038, -0.5), (0, -1))
                Line((0, -0.6), (0, -1))
            make_face()
            # Profile area: 0.2445171427, perimeter: 2.4283185307
            with BuildLine():
                CenterArc((0, 0), 0.6, 90, 60)
                Line((0, 0.6), (0, 1))
                Line((0, 1), (-0.8660254038, 0.5))
                Line((-0.5196152423, 0.3), (-0.8660254038, 0.5))
            make_face()
            # Profile area: 0.2445171427, perimeter: 2.4283185307
            with BuildLine():
                CenterArc((0, 0), 0.6, 30, 60)
                Line((0.5196152423, 0.3), (0.8660254038, 0.5))
                Line((0, 1), (0.8660254038, 0.5))
                Line((0, 0.6), (0, 1))
            make_face()
            # Profile area: 0.3769911184, perimeter: 2.4566370614
            with BuildLine():
                CenterArc((0, 0), 0.6, -90, 120)
                Line((0, 0), (0.5196152423, 0.3))
                Line((0, 0), (0, -0.6))
            make_face()
            # Profile area: 0.1884955592, perimeter: 1.8283185307
            with BuildLine():
                Line((0, 0), (0.5196152423, 0.3))
                CenterArc((0, 0), 0.6, 30, 60)
                Line((0, 0), (0, 0.6))
            make_face()
            # Profile area: 0.1884955592, perimeter: 1.8283185307
            with BuildLine():
                Line((0, 0), (-0.5196152423, 0.3))
                Line((0, 0), (0, 0.6))
                CenterArc((0, 0), 0.6, 90, 60)
            make_face()
            # Profile area: 0.3769911184, perimeter: 2.4566370614
            with BuildLine():
                CenterArc((0, 0), 0.6, 150, 120)
                Line((0, 0), (0, -0.6))
                Line((0, 0), (-0.5196152423, 0.3))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_22340_ec24cd79_0031():
    """Model: part 3 v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1654.6847046274, perimeter: 144.1991027998
            Circle(22.95)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 40 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8456119087, perimeter: 11.5748254494
            with BuildLine():
                CenterArc((0, 0), 21.45, 60, 7.5029024665)
                CenterArc((0, 0), 21.45, 52.4970972866, 7.5029027134)
                Line((13.0587947709, 17.0167675877), (13.150115014, 17.1357659624))
                CenterArc((0, 0), 21.6, 52.4970972866, 15.0058051799)
                Line((8.2649512157, 19.9562166104), (8.2075557212, 19.8176317728))
            make_face()
            # Profile area: 15.0877525741, perimeter: 25.1553601097
            with BuildLine():
                CenterArc((0, 0), 21.6, 67.5029024665, 6.3694770734)
                CenterArc((0, 0), 21.6, 52.4970972866, 15.0058051799)
                CenterArc((0, 0), 21.6, 46.1276202132, 6.3694770734)
                Line((14.9699749582, 15.5711223022), (16.1840265586, 16.2720553204))
                CenterArc((0, 0), 22.95, 45.1553996623, 29.6892004442)
                Line((6.0000000894, 20.7499397331), (6.0000000894, 22.1518057712))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 611.3617843702, perimeter: 87.6504350352
            Circle(13.95)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


def model_22344_51f483c9_0005():
    """Model: Piston Crank End v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3167367185, perimeter: 8.9840704422
            with BuildLine():
                Line((2, 0.75), (1.4000000075, 0.75))
                CenterArc((1.4000000075, 1.05), 0.3, -179.9999982925, 89.9999982925)
                Line((1.1, 1.3000000194), (1.1000000075, 1.0499999911))
                CenterArc((0.55, 1.3), 0.55, 0.000002018, 179.9999960875)
                Line((0, 1.3000000182), (0, 0))
                Line((0, 0), (2, 0))
                Line((2, 0), (2, 0.75))
            make_face()
            with BuildLine():
                CenterArc((0.55, 1.3), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.3167367185, perimeter: 8.9840704422
            with BuildLine():
                Line((0, 0), (2, 0))
                Line((0, -1.3000000194), (0, 0))
                CenterArc((0.55, -1.3), 0.55, -179.999997982, 179.999995964)
                Line((1.1, -1.3000000194), (1.1000000075, -1.0499999911))
                CenterArc((1.4000000075, -1.05), 0.3, 90, 89.9999982925)
                Line((2, -0.75), (1.4000000075, -0.75))
                Line((2, 0), (2, -0.75))
            make_face()
            with BuildLine():
                CenterArc((0.55, -1.3), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.7000000037, perimeter: 3.8000000149
            with BuildLine():
                Line((0, 0.35), (0, 0.85))
                Line((-1.4000000075, 0.85), (0, 0.85))
                Line((-1.4000000075, 0.85), (-1.4000000075, 0.35))
                Line((0, 0.35), (-1.4000000075, 0.35))
            make_face()
        # TwoSides extrude, along=1.1098, against=-0.1
        extrude(amount=1.1098, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2999999963, perimeter: 2.1999999851
            with BuildLine():
                Line((-1.4000000075, 0.85), (-1.4000000075, 0.35))
                Line((-2, 0.85), (-1.4000000075, 0.85))
                Line((-2, 0.35), (-2, 0.85))
                Line((-1.4000000075, 0.35), (-2, 0.35))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0, 0.6)):
                Circle(0.4)
        # OneSide extrude, distance=-4.7
        extrude(amount=-4.7, mode=Mode.SUBTRACT)
    return part.part


def model_22357_e2f7b060_0002():
    """Model: DIN 94 2 x 12 v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0109271609, perimeter: 0.4415873949
            with BuildLine():
                Line((-0.0894427191, 0.0099999998), (0.0894427191, 0.0099999998))
                CenterArc((0, 0), 0.09, 6.3793700653, 167.2412598695)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0109271609, perimeter: 0.4415873949
            with BuildLine():
                Line((0.0894427191, -0.0099999998), (-0.0894427191, -0.0099999998))
                CenterArc((0, 0), 0.09, -173.6206299347, 167.2412598695)
            make_face()
        # OneSide extrude, distance=1.45
        extrude(amount=1.45)
    return part.part


def model_22433_9f17ac4c_0004():
    """Model: Slave Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.816173205, perimeter: 7.6277869629
            with BuildLine():
                CenterArc((0, 0), 0.714, 42.8785276146, 274.2429447709)
                CenterArc((0, 0), 0.714, -42.8785276146, 85.7570552291)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.597
        extrude(amount=0.597)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5566708353, perimeter: 6.1427769867
            with BuildLine():
                CenterArc((3.017, 0), 0.437, 134.8480472816, 90.3039054368)
                Line((0.5232177412, 0.4858386515), (2.7088149286, 0.309824082))
                CenterArc((0, 0), 0.714, -42.8785276146, 85.7570552291)
                Line((0.5232177412, -0.4858386515), (2.7088149286, -0.309824082))
            make_face()
        # OneSide extrude, distance=0.268
        extrude(amount=0.268, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.3657410322, perimeter: 4.4613033692
            with BuildLine():
                CenterArc((3.017, 0), 0.437, 134.8480472816, 90.3039054368)
                CenterArc((3.017, 0), 0.437, -134.8480472816, 269.6960945632)
            make_face()
            with BuildLine():
                CenterArc((3.017, 0), 0.2730384838, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.268, against=-0.605
        extrude(amount=0.268, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.605, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.468705989, perimeter: 5.1365039886
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.597
        extrude(amount=0.597, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.1085420691, perimeter: 2.9721884514
            with BuildLine():
                CenterArc((3.017, 0), 0.2730384838, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.017, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.268, against=-0.605
        extrude(amount=0.268, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.605, mode=Mode.ADD)
    return part.part


def model_22447_4062c6cb_0000():
    """Model: Ball bearing Final v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=-7.4
        extrude(amount=-7.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6022122533, perimeter: 10.6814150222
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.ADD)
    return part.part


def model_22447_4062c6cb_0008():
    """Model: Wrench2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6335828231, perimeter: 12.900950232
            with BuildLine():
                CenterArc((0, 0), 1.15325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.085782299, perimeter: 15.3793526764
            with BuildLine():
                CenterArc((0, 0), 1.29445, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.15325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6335828231, perimeter: 12.900950232
            with BuildLine():
                CenterArc((0, 0), 1.15325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.2749900593, perimeter: 11.9031804052
            Circle(1.89445)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_22447_4062c6cb_0011():
    """Model: Gold Screw Final v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5264506296, perimeter: 7.2017869991
            with BuildLine():
                CenterArc((0, 0), 0.6462, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6987705053, perimeter: 9.0867425912
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6462, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.311848793, perimeter: 4.0601943455
            Circle(0.6462)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_22457_a6c2776f_0001():
    """Model: Stepper Motor Base Plate v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.8929, perimeter: 16.92
            with BuildLine():
                Line((4.23, -4.23), (0, -4.23))
                Line((4.23, 0), (4.23, -4.23))
                Line((0, 0), (4.23, 0))
                Line((0, -4.23), (0, 0))
            make_face()
        # OneSide extrude, distance=0.85
        extrude(amount=0.85)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.85, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0351125, perimeter: 0.904766594
            with BuildLine():
                Line((0, 0.265), (-0.265, 0))
                Line((-0.265, 0), (0, 0))
                Line((0, 0), (0, 0.265))
            make_face()
            # Profile area: 0.0351125, perimeter: 0.904766594
            with BuildLine():
                Line((-4.23, 3.965), (-3.965, 4.23))
                Line((-3.965, 4.23), (-4.23, 4.23))
                Line((-4.23, 4.23), (-4.23, 3.965))
            make_face()
            # Profile area: 0.0351125, perimeter: 0.904766594
            with BuildLine():
                Line((-3.965, 0), (-4.23, 0.265))
                Line((-4.23, 0.265), (-4.23, 0))
                Line((-4.23, 0), (-3.965, 0))
            make_face()
            # Profile area: 0.0351125, perimeter: 0.904766594
            with BuildLine():
                Line((-0.265, 4.23), (0, 3.965))
                Line((0, 3.965), (0, 4.23))
                Line((0, 4.23), (-0.265, 4.23))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.565, 0.565)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.665, 0.565)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.665, 3.665)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.565, 3.665)):
                Circle(0.2)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0.565, 0.565), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.565, 0.565), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((3.665, 0.565), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.665, 0.565), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((3.665, 3.665), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.665, 3.665), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0.565, 3.665), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.565, 3.665), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_22457_a6c2776f_0002():
    """Model: Stepper Motor Base Plate v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.8929, perimeter: 16.92
            with BuildLine():
                Line((4.23, -4.23), (0, -4.23))
                Line((4.23, 0), (4.23, -4.23))
                Line((0, 0), (4.23, 0))
                Line((0, -4.23), (0, 0))
            make_face()
        # OneSide extrude, distance=0.85
        extrude(amount=0.85)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.85, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.01125, perimeter: 0.5121320344
            with BuildLine():
                Line((0, 0.15), (-0.15, 0))
                Line((-0.15, 0), (0, 0))
                Line((0, 0), (0, 0.15))
            make_face()
            # Profile area: 0.01125, perimeter: 0.5121320344
            with BuildLine():
                Line((-4.08, 0), (-4.23, 0.15))
                Line((-4.23, 0.15), (-4.23, 0))
                Line((-4.23, 0), (-4.08, 0))
            make_face()
            # Profile area: 0.01125, perimeter: 0.5121320344
            with BuildLine():
                Line((-4.23, 4.08), (-4.08, 4.23))
                Line((-4.08, 4.23), (-4.23, 4.23))
                Line((-4.23, 4.23), (-4.23, 4.08))
            make_face()
            # Profile area: 0.01125, perimeter: 0.5121320344
            with BuildLine():
                Line((-0.15, 4.23), (0, 4.08))
                Line((0, 4.08), (0, 4.23))
                Line((0, 4.23), (-0.15, 4.23))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.565, 0.565)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.665, 0.565)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.665, 3.665)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.565, 3.665)):
                Circle(0.2)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0.565, 0.565), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.565, 0.565), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((3.665, 0.565), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.665, 0.565), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((3.665, 3.665), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.665, 3.665), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0.565, 3.665), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.565, 3.665), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_22463_c48bb23e_0004():
    """Model: 17 - Slave Rod v2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.5999468075, perimeter: 2.7457519792
            with Locations((3.017, 0)):
                Circle(0.437)
        # TwoSides extrude, along=0.268, against=-0.605
        extrude(amount=0.268)
        extrude(sk.sketch, amount=-0.605)
    return part.part


def model_22492_047b125b_0004():
    """Model: Baut Penahan Poros v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 38 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.7816077992, perimeter: 22.5286954036
            with BuildLine():
                CenterArc((0, 2.3846557142), 1.1153442858, 20.2934872255, 139.4130173679)
                CenterArc((-1.7505032187, 3.0319605136), 0.7510064374, -99.7064927729, 79.413003903)
                CenterArc((-2.0651724278, 1.1923278571), 1.1153442858, 80.293483046, 139.4130360051)
                CenterArc((-3.5010064374, 0), 0.7510064374, -39.7065364692, 79.4130261277)
                CenterArc((-2.0651724278, -1.1923278571), 1.1153442858, 140.2935124684, 139.4129704906)
                CenterArc((-1.7505032187, -3.0319605136), 0.7510064374, 20.2934630928, 79.4130801672)
                CenterArc((0, -2.3846557142), 1.1153442858, -159.7064872366, 139.4129697872)
                CenterArc((1.7505032187, -3.0319605136), 0.7510064374, 80.2934627331, 79.4130811335)
                CenterArc((2.0651724278, -1.1923278571), 1.1153442858, -99.7064869944, 139.4130190954)
                CenterArc((3.5010064374, 0), 0.7510064374, 140.2935235149, 79.4129467626)
                CenterArc((2.0651724278, 1.1923278571), 1.1153442858, -39.7065279213, 139.4130098494)
                CenterArc((1.7505032187, 3.0319605136), 0.7510064374, -159.70649898, 79.413043771)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


def model_22535_0ba01cc9_0007():
    """Model: PART 2 v4 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4222562326, perimeter: 2.59994089
            with BuildLine():
                Line((0, 0), (-0.3175, 0.5499261314))
                Line((0, 0), (0.635, 0))
                CenterArc((0, 0), 0.635, 0, 120)
            make_face()
            # Profile area: 0.8445124652, perimeter: 3.92988178
            with BuildLine():
                CenterArc((0, 0), 0.635, 120, 240)
                Line((0, 0), (0.635, 0))
                Line((0, 0), (-0.3175, 0.5499261314))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5563765679, perimeter: 3.0846132505
            with BuildLine():
                Line((0, 0), (0.7000000104, 0))
                Line((0.7000000104, 0), (0.6000000089, 0.7000000104))
                Line((0.6000000089, 0.7000000104), (-0.3580624406, 0.6201823394))
                Line((0, 0), (-0.3580624406, 0.6201823394))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)
    return part.part


def model_22604_7063d5c9_0007():
    """Model: A20 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_22612_28fe0ac2_0000():
    """Model: Part 10"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7805304826, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1.2
        extrude(amount=1.2, both=True)

        # Sketch7 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.3067472521, perimeter: 22.9336263712
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.45
        extrude(amount=0.45, both=True, mode=Mode.ADD)
    return part.part


def model_22624_7af10d7d_0006():
    """Model: column v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=4.1
        extrude(amount=4.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-1.15
        extrude(amount=-1.15, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-1.15
        extrude(amount=-1.15, mode=Mode.SUBTRACT)
    return part.part


def model_22666_bdaa1303_0002():
    """Model: CenterCrankshaftRear v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=-1.93294
        extrude(amount=-1.93294)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.93294), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.6626339158, perimeter: 6.9821896726
            with BuildLine():
                CenterArc((0, 0), 0.79375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=0.23876
        extrude(amount=0.23876, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.1717), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1233123321, perimeter: 1.2448246731
            with Locations((0, -0.55626)):
                Circle(0.19812)
        # OneSide extrude, distance=0.37592
        extrude(amount=0.37592, mode=Mode.ADD)
    return part.part


def model_22711_33843a5d_0002():
    """Model: Slider Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 124.8526539311, perimeter: 72.8886444276
            with BuildLine():
                CenterArc((0, 4), 11.5, -115.7714617406, 51.5429234811)
                Line((5, -6.3561575886), (5, 6.3561575886))
                CenterArc((0, -4), 11.5, 64.2285382594, 51.5429234811)
                Line((-5, 6.3561575886), (-5, -6.3561575886))
            make_face()
            with BuildLine():
                CenterArc((0, -4), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -4), 8, 65.852260083, 48.295479834)
                CenterArc((-3.6, 4.02994396), 0.8, 114.147739917, 180)
                CenterArc((0, -4), 9.6, 65.852260083, 48.295479834)
                CenterArc((3.6, 4.02994396), 0.8, -114.147739917, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.9606676294, perimeter: 19.8981183944
            with BuildLine():
                Line((-3.3, 1.5), (-3.3, -7.0163514831))
                Line((-5, 1.5), (-3.3, 1.5))
                Line((-5, 1.5), (-5, -6.3561575886))
                CenterArc((0, 4), 11.5, -115.7714617406, 9.0956268892)
            make_face()
            # Profile area: 13.9606676294, perimeter: 19.8981183944
            with BuildLine():
                Line((5, -6.3561575886), (5, 1.5))
                Line((5, 1.5), (3.3, 1.5))
                Line((3.3, 1.5), (3.3, -7.0163514831))
                CenterArc((0, 4), 11.5, -73.3241651487, 9.0956268892)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2672563597, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((0, -4), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -4), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((0, -4)):
                Circle(1.1)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_22734_f6bad9f7_0013():
    """Model: Crankshaft end v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5857538458, perimeter: 2.7130794156
            Circle(0.4318)
        # OneSide extrude, distance=2.4765
        extrude(amount=2.4765)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4765, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4813209451, perimeter: 10.6927247558
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4318, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5857538458, perimeter: 2.7130794156
            Circle(0.4318)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.9845, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1781393481, perimeter: 1.4961835013
            with Locations((0, -0.79375)):
                Circle(0.238125)
        # OneSide extrude, distance=2.2225
        extrude(amount=2.2225, mode=Mode.ADD)
    return part.part


def model_22734_f6bad9f7_0029():
    """Model: Piston v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2968989135, perimeter: 7.4809175064
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.555625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9698697842, perimeter: 3.4910948363
            Circle(0.555625)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.48091362, perimeter: 2.7516078775
            with BuildLine():
                CenterArc((-0.301625, 0.0127), 0.254, -177.1340160183, 87.1340160183)
                Line((-0.301625, -0.2413), (0.3016254492, -0.2413))
                CenterArc((0.301625, 0.0127), 0.254, -89.9998986652, 87.1339146826)
                CenterArc((0.301625, -0.0127), 0.254, 2.8659839826, 87.1339146815)
                Line((0.3016254492, 0.2413), (-0.3016254492, 0.2413))
                CenterArc((-0.301625, -0.0127), 0.254, 90.0001013383, 87.1339146782)
            make_face()
        # OneSide extrude, distance=-1.11125
        extrude(amount=-1.11125, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4889561642, perimeter: 6.2427027138
            with BuildLine():
                CenterArc((0, 0), 0.555625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.301625, 0.0127), 0.254, -89.9998986652, 87.1339146826)
                Line((0.3016254492, -0.2413), (-0.301625, -0.2413))
                CenterArc((-0.301625, 0.0127), 0.254, -177.1340160183, 87.1340160183)
                CenterArc((-0.301625, -0.0127), 0.254, 90.0001013383, 87.1339146782)
                Line((-0.3016254492, 0.2413), (0.3016254492, 0.2413))
                CenterArc((0.301625, -0.0127), 0.254, 2.8659839826, 87.1339146815)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875, mode=Mode.SUBTRACT)
    return part.part


def model_22734_f6bad9f7_0032():
    """Model: Valve Tube v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1781393481, perimeter: 1.4961835013
            Circle(0.238125)
        # OneSide extrude, distance=6.096
        extrude(amount=6.096)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.096, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.061311605, perimeter: 0.8777609874
            Circle(0.1397)
        # OneSide extrude, distance=-4.445
        extrude(amount=-4.445, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.096, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2778973831, perimeter: 3.8900771033
            with BuildLine():
                CenterArc((0, 0), 0.381, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.ADD)
    return part.part


def model_22742_3c107495_0008():
    """Model: Axis v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.1238898038, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((0, -3), 1, 0, 360)
                CenterArc((0, 0), 4, 0, 360)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -3)):
                Circle(1)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.999396, perimeter: 5.656
            with BuildLine():
                Line((-0.707, 3.707), (-0.707, 2.293))
                Line((-0.707, 2.293), (0.707, 2.293))
                Line((0.707, 2.293), (0.707, 3.707))
                Line((0.707, 3.707), (-0.707, 3.707))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 3)):
                Circle(0.5)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_22742_3c107495_0009():
    """Model: Exterior Shovel v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0530205405, perimeter: 1.3352793916
            with BuildLine():
                Line((1.2649110641, 0.3), (1.2, 0.3))
                Line((1.2, 0.3), (1.2, -0.3))
                Line((1.2, -0.3), (1.2649110641, -0.3))
                CenterArc((0, 0), 1.3, -13.3423637971, 26.6847275942)
            make_face()
            # Profile area: 2.1146783905, perimeter: 14.5756910712
            with BuildLine():
                CenterArc((0, 0), 1.3, 13.3423637971, 333.3152724058)
                Line((1.2, -0.3), (1.2649110641, -0.3))
                Line((1.2, 0.3), (1.2, -0.3))
                Line((1.2649110641, 0.3), (1.2, 0.3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0013157496, perimeter: 22.9322722155
            with BuildLine():
                CenterArc((0, 0), 1.3, -13.3423637971, 26.6847275942)
                Line((1.2649110641, -0.3), (11.5, -0.3))
                Line((11.5, -0.3), (11.5, 0.3))
                Line((11.5, 0.3), (1.2649110641, 0.3))
            make_face()
            with BuildLine():
                CenterArc((6.5, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8, perimeter: 4.8
            with BuildLine():
                Line((7.8, 1.8), (7.8, 2.2))
                Line((7.8, 2.2), (5.8, 2.2))
                Line((5.8, 2.2), (5.8, 1.8))
                Line((5.8, 1.8), (7.8, 1.8))
            make_face()
        # OneSide extrude, distance=-2.3808
        extrude(amount=-2.3808, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0530205405, perimeter: 1.3352793916
            with BuildLine():
                Line((1.2649110641, 0.3), (1.2, 0.3))
                Line((1.2, 0.3), (1.2, -0.3))
                Line((1.2, -0.3), (1.2649110641, -0.3))
                CenterArc((0, 0), 1.3, -13.3423637971, 26.6847275942)
            make_face()
            # Profile area: 2.1146783905, perimeter: 14.5756910712
            with BuildLine():
                CenterArc((0, 0), 1.3, 13.3423637971, 333.3152724058)
                Line((1.2, -0.3), (1.2649110641, -0.3))
                Line((1.2, 0.3), (1.2, -0.3))
                Line((1.2649110641, 0.3), (1.2, 0.3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


def model_22772_2b5f6629_0000():
    """Model: Spur Gear 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.7529155256, perimeter: 7.7283179278
            Circle(1.23)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Intersect)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.016146619, perimeter: 0.5716231778
            with BuildLine():
                CenterArc((0, 0), 1.025, 90, 5.8706528391)
                Line((0, 1.23), (0, 1.025))
                CenterArc((0, 0), 1.23, 90, 1.9581428007)
                CenterArc((0.6801, 0.8987), 0.7942, 155.4022578276, 15.8398715093)
            make_face()
            # Profile area: 0.016146619, perimeter: 0.5716231778
            with BuildLine():
                CenterArc((0, 0), 1.23, 88.0418571993, 1.9581428007)
                Line((0, 1.23), (0, 1.025))
                CenterArc((0, 0), 1.025, 84.1293471609, 5.8706528391)
                CenterArc((-0.6801, 0.8987), 0.7942, 8.757870663, 15.8398715093)
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.INTERSECT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7612553814, perimeter: 10.8384946549
            with BuildLine():
                CenterArc((0, 0), 1.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)
    return part.part


def model_22776_facf9bcf_0000():
    """Model: Gancho v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.6963010302, perimeter: 31.5680617858
            with BuildLine():
                CenterArc((1.6000000297, -4.9999646251), 3.3, 147.5081445013, 32.6318320223)
                Line((-1.6999901222, -5.008026686), (0.5330102565, -5.008026686))
                CenterArc((3.8330000297, -4.9998110736), 3.3, 127.4748193497, 52.667823197)
                CenterArc((0, 0), 3, -52.5251806503, 234.5749769013)
                Line((-2.9980803544, -0.1073041875), (-2.8987948146, -1.5346948551))
                CenterArc((-2.4, -1.5), 0.5, -176.0210650435, 174.0430532498)
                Line((-1.8493172204, -0.0411197725), (-1.9002979267, -1.5172579807))
                CenterArc((-0.5999999703, 0.0001889264), 1.25, -25.8498352205, 207.7436313101)
                CenterArc((-0.5999999703, 0.0001889264), 1.25, -39.133875777, 13.2840405565)
                Line((0.3695917651, -0.7887292359), (-1.183443755, -3.2272715616))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.008026686), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with Locations((-0.5834897435, 0.7000000104)):
                Circle(0.65)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.408026686), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7118094971, perimeter: 2.9907962062
            with Locations((-0.5834897435, 0.7000000104)):
                Circle(0.476)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_22822_b5d896dd_0003():
    """Model: Chaveta de Vastago v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-0.5, 0.5), (-0.5, -0.5))
                Line((-0.5, -0.5), (0.5, -0.5))
                Line((0.5, -0.5), (0.5, 0.5))
                Line((0.5, 0.5), (-0.5, 0.5))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.66, perimeter: 3.4
            with BuildLine():
                Line((0, 0), (0.6, 0))
                Line((0, -1.1), (0, 0))
                Line((0.6, -1.1), (0, -1.1))
                Line((0.6, 0), (0.6, -1.1))
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True, mode=Mode.ADD)
    return part.part


def model_22848_cc91b848_0017():
    """Model: Left side rod holder v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.9372121094, perimeter: 17.78
            with BuildLine():
                Line((-1.5478125, 2.8971875), (1.5478125, 2.8971875))
                Line((-1.5478125, -2.8971875), (-1.5478125, 2.8971875))
                Line((1.5478125, -2.8971875), (-1.5478125, -2.8971875))
                Line((1.5478125, 2.8971875), (1.5478125, -2.8971875))
            make_face()
        # OneSide extrude, distance=-5.318125
        extrude(amount=-5.318125)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5478125, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            with Locations((-1.4339231924, -2.6590625)):
                Circle(0.79375)
        # OneSide extrude, distance=-1.80578125
        extrude(amount=-1.80578125, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.8971875), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            with Locations((-0.0009525, -1.190625)):
                Circle(0.47625)
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            with Locations((0, -3.730625)):
                Circle(0.47625)
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)
    return part.part


def model_23008_3d1bb7b2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch52 -> Extrude54 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 20
            with BuildLine():
                Line((-2, -15), (-3, -15))
                Line((-3, -15), (-3, -17))
                Line((-3, -17), (-5, -17))
                Line((-5, -17), (-5, -18))
                Line((-5, -18), (-3, -18))
                Line((-3, -18), (-3, -20))
                Line((-3, -20), (-2, -20))
                Line((-2, -20), (-2, -18))
                Line((-2, -18), (0, -18))
                Line((0, -18), (0, -17))
                Line((0, -17), (-2, -17))
                Line((-2, -17), (-2, -15))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch54 -> Extrude56 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14, perimeter: 30
            with BuildLine():
                Line((-34, 10), (-35, 10))
                Line((-35, 10), (-35, 2))
                Line((-35, 2), (-28, 2))
                Line((-28, 2), (-28, 3))
                Line((-28, 3), (-34, 3))
                Line((-34, 3), (-34, 10))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5)
    return part.part


def model_23138_630f02f9_0005():
    """Model: Part 6 and 3 v10 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 182.4146924751, perimeter: 47.8778720407
            Circle(7.62)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 95.0331777711, perimeter: 34.5575191895
            Circle(5.5)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 81.0731966556, perimeter: 31.9185813605
            Circle(5.08)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_23144_88ca00a5_0005():
    """Model: Top  v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2709.672, perimeter: 208.28
            with BuildLine():
                Line((25.4, -26.67), (-25.4, -26.67))
                Line((25.4, 26.67), (25.4, -26.67))
                Line((-25.4, 26.67), (25.4, 26.67))
                Line((-25.4, -26.67), (-25.4, 26.67))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2630.897964, perimeter: 205.232
            with BuildLine():
                Line((-25.019, 26.289), (25.019, 26.289))
                Line((-25.019, -26.289), (-25.019, 26.289))
                Line((25.019, -26.289), (-25.019, -26.289))
                Line((25.019, 26.289), (25.019, -26.289))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.286, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1268.70714, perimeter: 153.416
            with BuildLine():
                Line((0.889, -26.289), (0.889, 26.289))
                Line((25.019, -26.289), (0.889, -26.289))
                Line((25.019, 26.289), (25.019, -26.289))
                Line((0.889, 26.289), (25.019, 26.289))
            make_face()
            # Profile area: 1268.70714, perimeter: 153.416
            with BuildLine():
                Line((-0.889, 26.289), (-25.019, 26.289))
                Line((-25.019, 26.289), (-25.019, -26.289))
                Line((-25.019, -26.289), (-0.889, -26.289))
                Line((-0.889, -26.289), (-0.889, 26.289))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


def model_23144_88ca00a5_0006():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2709.672, perimeter: 208.28
            with BuildLine():
                Line((25.4, -26.67), (-25.4, -26.67))
                Line((25.4, 26.67), (25.4, -26.67))
                Line((-25.4, 26.67), (25.4, 26.67))
                Line((-25.4, -26.67), (-25.4, 26.67))
            make_face()
        # OneSide extrude, distance=50.8
        extrude(amount=50.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-25.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2206.4471668625, perimeter: 187.9599986267
            with BuildLine():
                Line((24.13, 2.5399999619), (-24.13, 2.5399999619))
                Line((24.13, 48.2599992752), (24.13, 2.5399999619))
                Line((-24.13, 48.2599992752), (24.13, 48.2599992752))
                Line((-24.13, 2.5399999619), (-24.13, 48.2599992752))
            make_face()
        # OneSide extrude, distance=-48.26
        extrude(amount=-48.26, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -24.13), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 65.5129313646, perimeter: 55.9585676349
            with BuildLine():
                Line((12.6999998093, 35.5599994659), (12.6999998093, 32.9509792767))
                Line((-12.6999998093, 35.5599994659), (12.6999998093, 35.5599994659))
                Line((-12.6999998093, 33.010521045), (-12.6999998093, 35.5599994659))
                Line((12.6999998093, 32.9509792767), (-12.6999998093, 33.010521045))
            make_face()
            # Profile area: 64.5159980621, perimeter: 55.8799991608
            with BuildLine():
                Line((-12.6999998093, 27.9399995804), (-12.6999998093, 25.3999996185))
                Line((-12.6999998093, 25.3999996185), (12.6999998093, 25.3999996185))
                Line((12.6999998093, 25.3999996185), (12.6999998093, 27.9399995804))
                Line((12.6999998093, 27.9399995804), (-12.6999998093, 27.9399995804))
            make_face()
            # Profile area: 65.0656158939, perimeter: 55.923276156
            with BuildLine():
                Line((12.6999998093, 17.779999733), (-12.6999998093, 17.779999733))
                Line((12.6999998093, 20.3416381925), (12.6999998093, 17.779999733))
                Line((-12.6999998093, 20.3416381925), (12.6999998093, 20.3416381925))
                Line((-12.6999998093, 17.779999733), (-12.6999998093, 20.3416381925))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


def model_23144_88ca00a5_0011():
    """Model: handle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4596620816, perimeter: 12.498401921
            with BuildLine():
                Line((0, 0), (0, 1.905))
                Line((0, 1.905), (-2.54, 1.905))
                Line((-2.54, 1.905), (-3.175, 0))
                Line((-3.175, 0), (-2.9210000021, 0.0000325896))
                Line((-2.9210000021, 0.0000325896), (-2.413, 1.651))
                Line((-0.254, 1.651), (-2.413, 1.651))
                Line((-0.254, 0), (-0.254, 1.651))
                Line((0, 0), (-0.254, 0))
            make_face()
        # OneSide extrude, distance=48.26
        extrude(amount=48.26)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(48.26, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.9838754184, perimeter: 8.7123556068
            with BuildLine():
                Line((-3.175, 0), (-0.254, 0))
                Line((-0.254, 1.651), (-0.254, 0))
                Line((-2.413, 1.651), (-0.254, 1.651))
                Line((-2.9210000021, 0.0000325896), (-2.413, 1.651))
                Line((-3.175, 0), (-2.9210000021, 0.0000325896))
            make_face()
            # Profile area: 1.4596620816, perimeter: 12.498401921
            with BuildLine():
                Line((-3.175, 0), (-2.54, 1.905))
                Line((-3.175, 0), (-2.9210000021, 0.0000325896))
                Line((-2.9210000021, 0.0000325896), (-2.413, 1.651))
                Line((-2.413, 1.651), (-0.254, 1.651))
                Line((-0.254, 1.651), (-0.254, 0))
                Line((-0.254, 0), (0, 0))
                Line((0, 1.905), (0, 0))
                Line((-2.54, 1.905), (0, 1.905))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.4435375, perimeter: 9.6280463142
            with BuildLine():
                Line((-2.54, 1.905), (-3.175, 0))
                Line((-3.175, 0), (0, 0))
                Line((0, 1.905), (0, 0))
                Line((0, 1.905), (-2.54, 1.905))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.ADD)
    return part.part


def model_23162_7e2f3d77_0001():
    """Model: Wall Roller Mount Small"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5272647481, perimeter: 5.0525364784
            with BuildLine():
                Line((-17.8518900988, -1.5240000486), (-17.8241744812, 0))
                Line((-16.8358900988, -1.5240000486), (-17.8518900988, -1.5240000486))
                Line((-16.8358900988, 0), (-16.8358900988, -1.5240000486))
                Line((-16.8358900988, 0), (-17.8241744812, 0))
            make_face()
        # OneSide extrude, distance=0.889
        extrude(amount=0.889)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0091516969, perimeter: 0.7158312352
            with BuildLine():
                Line((17.8241744812, 0.9363320068), (17.8241744812, 1.2665320068))
                Line((17.8241744812, 0.9363320068), (17.8518900988, 0.9363320068))
                Line((17.8518900988, 0.9363320068), (17.8518900988, 1.2665320068))
                Line((17.8241744812, 1.2665320068), (17.8518900988, 1.2665320068))
            make_face()
            # Profile area: 0.0181972179, perimeter: 0.7706193696
            with BuildLine():
                Line((17.8518900988, 0.9363320068), (17.8518900988, 1.2665320068))
                Line((17.8518900988, 0.9363320068), (17.9069997836, 0.9363320068))
                Line((17.9069997836, 0.9363320068), (17.9069997836, 1.2665320068))
                Line((17.8518900988, 1.2665320068), (17.9069997836, 1.2665320068))
            make_face()
            # Profile area: 0.3263315031, perimeter: 2.6369687648
            with BuildLine():
                Line((16.8358900988, 1.2665320068), (17.8241744812, 1.2665320068))
                Line((16.8358900988, 0.9363320068), (16.8358900988, 1.2665320068))
                Line((17.8241744812, 0.9363320068), (16.8358900988, 0.9363320068))
                Line((17.8241744812, 0.9363320068), (17.8241744812, 1.2665320068))
            make_face()
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.524, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.012667687, perimeter: 0.398982267
            with Locations((-17.3438900988, -0.381)):
                Circle(0.0635)
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)
    return part.part


def model_23206_b99a5251_0015():
    """Model: 1_006-a v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.9909922943, perimeter: 23.9806313201
            with BuildLine():
                Line((1.8942614091, 2.3903769648), (2.7000000402, -0.400000006))
                Line((2.7000000402, -0.400000006), (3.6607482086, -0.1225780224))
                Line((3.6607482086, -0.1225780224), (2.8550095774, 2.6677989484))
                CenterArc((1.7468382057, 2.3478076019), 1.1534462497, 16.1064007106, 71.2218548474)
                Line((-1.8035941808, 3.5000000373), (1.8006047646, 3.5000000373))
                CenterArc((-1.7498276219, 2.3478076019), 1.1534462497, 92.671744442, 71.2218548474)
                Line((-3.6637376248, -0.1225780224), (-2.8579989937, 2.6677989484))
                Line((-2.7029894565, -0.400000006), (-3.6637376248, -0.1225780224))
                Line((-1.8972508253, 2.3903769648), (-2.7029894565, -0.400000006))
                CenterArc((-1.7514947081, 2.3482889833), 0.1517110539, 90, 73.8935992894)
                Line((-1.7514947081, 2.5000000373), (1.7485052919, 2.5000000373))
                CenterArc((1.7485052919, 2.3482889833), 0.1517110539, 16.1064007106, 73.8935992894)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5000000373, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-0.0506047646, 1.25)):
                Circle(0.7)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5000000373, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0053096491, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((-0.0506047646, 1.25), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.0506047646, 1.25), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_23206_b99a5251_0048():
    """Model: 1_008-a v3 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2146018366, perimeter: 7.5707963268
            with BuildLine():
                Line((0, 0), (0, -2))
                Line((0, -2), (1, -2))
                CenterArc((2, -2), 1, 90, 90)
                Line((2, 0), (2, -1))
                Line((0, 0), (2, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((1, 1.5), (1, 0.5))
                Line((1, 0.5), (2, 0.5))
                Line((2, 0.5), (2, 1.5))
                Line((2, 1.5), (1, 1.5))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-1, 0.5), (-2, 0.5))
                Line((-1, 1.5), (-1, 0.5))
                Line((-2, 1.5), (-1, 1.5))
                Line((-2, 0.5), (-2, 1.5))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_23231_efe613bb_0018():
    """Model: Heated block v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7545630739, perimeter: 10.3561944902
            with BuildLine():
                Line((2, -2), (0, -2))
                Line((2, 0), (2, -2))
                Line((0, 0), (2, 0))
                Line((0, -2), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((1.5000000224, -1.5000000224), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, -0.8000000149), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((1.5000000224, -1.5000000224)):
                Circle(0.125)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1, -0.8000000149)):
                Circle(0.25)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314394867, perimeter: 0.6285540883
            with Locations((0.6972618816, 0.6)):
                Circle(0.1000374902)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((1.5000000209, 0.6000000089)):
                Circle(0.3000000045)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1, -0.8000000149)):
                Circle(0.25)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((1.5000000224, -1.5000000224)):
                Circle(0.125)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.SUBTRACT)
    return part.part


def model_23393_d47067ad_0005():
    """Model: Guard Rail"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 270, perimeter: 274
            with BuildLine():
                Line((1, 0), (1, 135))
                Line((1, 135), (-1, 135))
                Line((-1, 0), (-1, 135))
                Line((1, 0), (-1, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, -2)):
                Circle(0.5)
        # OneSide extrude, distance=16
        extrude(amount=16)
    return part.part


def model_23393_d47067ad_0007():
    """Model: P16A-Axle Block (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((-2, 3), (-2, 2))
                Line((2, 2), (-2, 2))
                Line((2, 3), (2, 2))
                Line((-2, 3), (2, 3))
            make_face()
            # Profile area: 3, perimeter: 8
            with BuildLine():
                Line((-3, -1), (-3, 2))
                Line((-2, -1), (-3, -1))
                Line((-2, 2), (-2, -1))
                Line((-2, 2), (-3, 2))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((2, -1), (2, -3))
                Line((2, -1), (-2, -1))
                Line((-2, -1), (-2, -3))
                Line((2, -3), (-2, -3))
            make_face()
            # Profile area: 3, perimeter: 8
            with BuildLine():
                Line((3, 2), (2, 2))
                Line((2, 2), (2, -1))
                Line((3, -1), (2, -1))
                Line((3, 2), (3, -1))
            make_face()
            # Profile area: 12, perimeter: 14
            with BuildLine():
                Line((-2, 2), (-2, -1))
                Line((2, -1), (-2, -1))
                Line((2, 2), (2, -1))
                Line((2, 2), (-2, 2))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, -0.5)):
                Circle(0.5)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_23393_d47067ad_0014():
    """Model: P2-Front/Rear Axle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=21
        extrude(amount=21)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(21, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(25.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_23472_ed1faab6_0007():
    """Model: LED"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0544314675, perimeter: 2.7430030857
            with BuildLine():
                CenterArc((0, 0), 0.238125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1984375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1237078806, perimeter: 1.2468195844
            Circle(0.1984375)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0031501953, perimeter: 0.238125
            with BuildLine():
                Line((-0.0728774244, -0.01984375), (-0.1522524244, -0.01984375))
                Line((-0.0728774244, 0.01984375), (-0.0728774244, -0.01984375))
                Line((-0.1522524244, 0.01984375), (-0.0728774244, 0.01984375))
                Line((-0.1522524244, -0.01984375), (-0.1522524244, 0.01984375))
            make_face()
            # Profile area: 0.0031501953, perimeter: 0.238125
            with BuildLine():
                Line((0.1375789777, -0.01984375), (0.0582039777, -0.01984375))
                Line((0.1375789777, 0.01984375), (0.1375789777, -0.01984375))
                Line((0.0582039777, 0.01984375), (0.1375789777, 0.01984375))
                Line((0.0582039777, -0.01984375), (0.0582039777, 0.01984375))
            make_face()
        # OneSide extrude, distance=0.79375
        extrude(amount=0.79375, mode=Mode.ADD)
    return part.part


def model_23472_ed1faab6_0009():
    """Model: Bit"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3492030934, perimeter: 2.1997045256
            with BuildLine():
                Line((0.1833087105, 0.3175), (-0.1833087105, 0.3175))
                Line((-0.1833087105, 0.3175), (-0.3666174209, 0))
                Line((-0.3666174209, 0), (-0.1833087105, -0.3175))
                Line((-0.1833087105, -0.3175), (0.1833087105, -0.3175))
                Line((0.1833087105, -0.3175), (0.3666174209, 0))
                Line((0.3666174209, 0), (0.1833087105, 0.3175))
            make_face()
        # OneSide extrude, distance=1.5875
        extrude(amount=1.5875)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0132872434, 1.5875, 0.0325881615), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1085042722, perimeter: 1.6421917116
            with BuildLine():
                Line((0.303539097, -0.1119631615), (-0.3301301443, -0.1119631615))
                Line((0.303539097, -0.1119631615), (0.3533301775, -0.0325881615))
                Line((0.3533301775, -0.0325881615), (0.3036155475, 0.0467868385))
                Line((-0.3302114404, 0.0467868385), (0.3036155475, 0.0467868385))
                Line((-0.3799046644, -0.0325881615), (-0.3302114404, 0.0467868385))
                Line((-0.3301301443, -0.1119631615), (-0.3799046644, -0.0325881615))
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000005864, 0, 0.0000000789), x_dir=(1, 0, 0.0000000044), z_dir=(0, -1, 0))):
            # Profile area: 0.1320048029, perimeter: 3.2998266364
            with BuildLine():
                CenterArc((-0.0000005878, -0.3175000789), 0.3175000789, 149.9999915211, 240.0000164506)
                Line((-0.3223412583, -0.0766896571), (-0.2749636984, -0.1587499988))
                CenterArc((-0.0000005878, -0.3175000789), 0.4023594999, 143.237765641, 253.5244682107)
                Line((0.2749625242, -0.1587500012), (0.3223400848, -0.0766896599))
            make_face()
            # Profile area: 0.0599052497, perimeter: 1.6022049745
            with BuildLine():
                CenterArc((-0.0000005878, -0.3175000789), 0.3175000789, 30.0000079717, 119.9999835494)
                Line((0.2749625242, -0.1587500012), (0.3223400848, -0.0766896599))
                CenterArc((-0.0000005878, -0.3175000789), 0.4023594999, 36.7622338517, 106.4755317893)
                Line((-0.3223412583, -0.0766896571), (-0.2749636984, -0.1587499988))
            make_face()
        # OneSide extrude, distance=-0.0396875
        extrude(amount=-0.0396875, mode=Mode.SUBTRACT)
    return part.part


def model_23493_57512264_0003():
    """Model: bolec"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5, 4)):
                Circle(0.2)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((-0.5, 4), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.5, 4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5, 4)):
                Circle(0.2)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0.5, 4), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.5, 4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.5, 4)):
                Circle(0.2)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_23552_10239b96_0001():
    """Model: conrod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((5.500000082, -4.1000000611), 0.2, 0, 180)
                CenterArc((5.500000082, -4.1000000611), 0.2, 180, 180)
            make_face()
            # Profile area: 0.3171681469, perimeter: 2.9283185307
            with BuildLine():
                CenterArc((5.500000082, -4.1000000611), 0.2, 180, 180)
                Line((5.300000082, -5.0500000611), (5.300000082, -4.1000000611))
                Line((5.700000082, -5.0500000611), (5.300000082, -5.0500000611))
                Line((5.700000082, -4.1000000611), (5.700000082, -5.0500000611))
            make_face()
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2217920367, perimeter: 2.5141592654
            with BuildLine():
                Line((5.600000082, -5.3000000611), (5.975000082, -5.3000000611))
                Line((5.975000082, -5.3000000611), (5.975000082, -5.0500000611))
                Line((5.975000082, -5.0500000611), (5.025000082, -5.0500000611))
                Line((5.025000082, -5.0500000611), (5.025000082, -5.3000000611))
                Line((5.025000082, -5.3000000611), (5.400000082, -5.3000000611))
                CenterArc((5.500000082, -5.3000000611), 0.1, 0, 180)
            make_face()
        # TwoSides extrude (symmetric), distance=0.15
        extrude(amount=0.15, both=True, mode=Mode.ADD)

        # Sketch7 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-5.500000082, 4.1000000611)):
                Circle(0.1)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_23554_a0845d54_0013():
    """Model: tappo pistone v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.190705401, perimeter: 19.4778744523
            Circle(3.1)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.2938046055, perimeter: 41.4690230274
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 30.190705401, perimeter: 19.4778744523
            Circle(3.1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_23602_5daaccf5_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.1767320736, perimeter: 34.3997822678
            with BuildLine():
                Line((3.4163, 1.5875), (0.9914244587, 4.6164112465))
                CenterArc((0, 3.8227), 1.27, 38.6799477989, 102.6401044023)
                Line((-3.4163, 1.5875), (-0.9914244587, 4.6164112465))
                Line((-3.4163, -1.5875), (-3.4163, 1.5875))
                Line((-3.4163, -1.5875), (-0.9914244587, -4.6164112465))
                CenterArc((0, -3.8227), 1.27, -141.3200522011, 102.6401044023)
                Line((3.4163, -1.5875), (0.9914244587, -4.6164112465))
                Line((3.4163, -1.5875), (3.4163, 1.5875))
            make_face()
            with BuildLine():
                CenterArc((0, 3.8227), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -3.8227), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.4163, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.8281116394, perimeter: 16.0020840588
            with BuildLine():
                Line((-1.5875, 1.27), (1.5875, 1.27))
                Line((1.5875, 1.27), (1.6001642407, 3.1643022005))
                CenterArc((0, 3.175), 1.6002, -0.3830416975, 180.766083395)
                Line((-1.5875, 1.27), (-1.6001642407, 3.1643022005))
            make_face()
            with BuildLine():
                CenterArc((0, 3.175), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.4163, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.8281116394, perimeter: 16.0020840588
            with BuildLine():
                Line((-1.5875, 1.27), (1.5875, 1.27))
                Line((1.5875, 1.27), (1.6001642407, 3.1643022005))
                CenterArc((0, 3.175), 1.6002, -0.3830416975, 180.766083395)
                Line((-1.5875, 1.27), (-1.6001642407, 3.1643022005))
            make_face()
            with BuildLine():
                CenterArc((0, 3.175), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)
    return part.part


def model_23631_d2b74fdc_0000():
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
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.4933614313, perimeter: 65.9734457254
            with BuildLine():
                CenterArc((0, 0), 5.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 7.2286872506, perimeter: 17.5192408359
            with BuildLine():
                CenterArc((0, -0.0833333333), 6.0833333333, 48.8879095608, 82.2241808783)
                Line((-3.5, 4), (-4, 4.5))
                CenterArc((0, -1.625), 6.625, 58.1092081982, 63.7815836037)
                Line((4, 4.5), (3.5, 4))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1589707167, perimeter: 3.6483216287
            with BuildLine():
                Line((-1.0419662172, -0.0751048877), (-1.1218373129, -0.2953705146))
                Line((-0.7378607119, -0.0751048877), (-1.0419662172, -0.0751048877))
                Line((-0.6530286992, -0.2953705146), (-0.7378607119, -0.0751048877))
                Line((-0.5433919752, -0.2953705146), (-0.6530286992, -0.2953705146))
                Line((-0.8410482133, 0.4319029496), (-0.5433919752, -0.2953705146))
                Line((-0.944731834, 0.4319029496), (-0.8410482133, 0.4319029496))
                Line((-1.224032626, -0.2953705146), (-0.944731834, 0.4319029496))
                Line((-1.1218373129, -0.2953705146), (-1.224032626, -0.2953705146))
            make_face()
            with BuildLine():
                _nurbs_edge([(-0.8435286904, 0.2046920107), (-0.8539292477, 0.2324495707), (-0.8725804778, 0.2822269649), (-0.888208939, 0.3330306755), (-0.8951224411, 0.3555045173)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0889008672, 0.1594251622, 0.1594251622, 0.1594251622, 0.1594251622], 3)
                Line((-0.7676263476, 0.003277962), (-0.8435286904, 0.2046920107))
                Line((-1.0141849691, 0.003277962), (-0.7676263476, 0.003277962))
                Line((-0.934313866, 0.2165982769), (-1.0141849691, 0.003277962))
                _nurbs_edge([(-0.8951224411, 0.3555045173), (-0.9002589365, 0.3321455033), (-0.9106086624, 0.2850785105), (-0.926373171, 0.2395375715), (-0.934313866, 0.2165982769)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0716839353, 0.1444387704, 0.1444387704, 0.1444387704, 0.1444387704], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1104954602, perimeter: 2.774840001
            with BuildLine():
                _nurbs_edge([(-0.2065443123, -0.209794338), (-0.1957035482, -0.2024126809), (-0.1743760701, -0.1878904455), (-0.162517614, -0.1649939511), (-0.1566868151, -0.1537357523)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0386712057, 0.0760794428, 0.0760794428, 0.0760794428, 0.0760794428], 3)
                _nurbs_edge([(-0.281950506, -0.2303822591), (-0.2687393944, -0.229510787), (-0.2422110674, -0.2277608437), (-0.2184648894, -0.2157991207), (-0.2065443123, -0.209794338)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0392820053, 0.0788795002, 0.0788795002, 0.0788795002, 0.0788795002], 3)
                _nurbs_edge([(-0.3494192684, -0.2102904274), (-0.3395044732, -0.2161471571), (-0.3187218919, -0.2284235537), (-0.2945766961, -0.2297096985), (-0.281950506, -0.2303822591)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0340281065, 0.071326928, 0.071326928, 0.071326928, 0.071326928], 3)
                _nurbs_edge([(-0.3851380075, -0.1549759462), (-0.381626925, -0.1660225427), (-0.374730675, -0.187719581), (-0.3577530756, -0.2028589526), (-0.3494192684, -0.2102904274)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0340778593, 0.0669336129, 0.0669336129, 0.0669336129, 0.0669336129], 3)
                _nurbs_edge([(-0.3905950511, -0.0607181742), (-0.390687739, -0.0802688706), (-0.3908373366, -0.1118235718), (-0.3867086412, -0.1430839192), (-0.3851380075, -0.1549759462)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0585549882, 0.0945073829, 0.0945073829, 0.0945073829, 0.0945073829], 3)
                Line((-0.3905950511, 0.2314810202), (-0.3905950511, -0.0607181742))
                Line((-0.4798919285, 0.2314810202), (-0.3905950511, 0.2314810202))
                Line((-0.4798919285, -0.0949486449), (-0.4798919285, 0.2314810202))
                _nurbs_edge([(-0.4744348849, -0.1782923891), (-0.4760138916, -0.1669807885), (-0.4798709081, -0.1393501084), (-0.4798841234, -0.1114354475), (-0.4798919285, -0.0949486449)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0342279763, 0.0836081729, 0.0836081729, 0.0836081729, 0.0836081729], 3)
                _nurbs_edge([(-0.4469017113, -0.2445208981), (-0.4530019182, -0.2347232701), (-0.4657973219, -0.2141723927), (-0.4714678042, -0.1906174934), (-0.4744348849, -0.1782923891)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0343919776, 0.0721384115, 0.0721384115, 0.0721384115, 0.0721384115], 3)
                _nurbs_edge([(-0.3868743504, -0.2894173815), (-0.3991958821, -0.2834601944), (-0.4221551384, -0.2723599037), (-0.4390662684, -0.2533354899), (-0.4469017113, -0.2445208981)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0405809256, 0.0756162374, 0.0756162374, 0.0756162374, 0.0756162374], 3)
                _nurbs_edge([(-0.2998099054, -0.3072767808), (-0.3149998727, -0.3065746971), (-0.3449653516, -0.3051896858), (-0.3730340914, -0.2946261143), (-0.3868743504, -0.2894173815)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0453030589, 0.0893700314, 0.0893700314, 0.0893700314, 0.0893700314], 3)
                _nurbs_edge([(-0.1326263273, -0.2179799034), (-0.154833507, -0.2440243873), (-0.1989079073, -0.2957146528), (-0.2663493045, -0.3034426075), (-0.2998099054, -0.3072767808)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0987389797, 0.1959664127, 0.1959664127, 0.1959664127, 0.1959664127], 3)
                Line((-0.1326263273, -0.2953705146), (-0.1326263273, -0.2179799034))
                Line((-0.0527552689, -0.2953705146), (-0.1326263273, -0.2953705146))
                Line((-0.0527552689, 0.2314810202), (-0.0527552689, -0.2953705146))
                Line((-0.1420520867, 0.2314810202), (-0.0527552689, 0.2314810202))
                Line((-0.1420520867, -0.0507962658), (-0.1420520867, 0.2314810202))
                _nurbs_edge([(-0.1566868151, -0.1537357523), (-0.1524397098, -0.1393372417), (-0.1425485262, -0.1058042113), (-0.1422324469, -0.0707810689), (-0.1420520867, -0.0507962658)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.044834534, 0.1044162014, 0.1044162014, 0.1044162014, 0.1044162014], 3)
            make_face()
            # Profile area: 0.1152657253, perimeter: 2.9167265942
            with BuildLine():
                _nurbs_edge([(0.2766509926, -0.3072767808), (0.2457089699, -0.3064036136), (0.1898419757, -0.304827077), (0.1416391167, -0.2770191795), (0.1201334869, -0.2646127298)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0911016156, 0.1644874189, 0.1644874189, 0.1644874189, 0.1644874189], 3)
                _nurbs_edge([(0.3877759849, -0.2856966808), (0.3705078061, -0.2919884439), (0.3346315434, -0.3050601726), (0.2964531379, -0.3065197408), (0.2766509926, -0.3072767808)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0547832993, 0.1138174473, 0.1138174473, 0.1138174473, 0.1138174473], 3)
                _nurbs_edge([(0.4629342233, -0.2246771409), (0.4530318906, -0.237190959), (0.4325379771, -0.2630896146), (0.4030274797, -0.2779939058), (0.3877759849, -0.2856966808)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0472782506, 0.0978472851, 0.0978472851, 0.0978472851, 0.0978472851], 3)
                _nurbs_edge([(0.4889791881, -0.1405892923), (0.4878296404, -0.1553516645), (0.485495141, -0.1853310615), (0.4705301796, -0.2114298474), (0.4629342233, -0.2246771409)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0438324769, 0.0890149091, 0.0890149091, 0.0890149091, 0.0890149091], 3)
                _nurbs_edge([(0.4676471626, -0.0641908004), (0.4738642456, -0.0754289456), (0.4869932598, -0.09916126), (0.4882942604, -0.1263011585), (0.4889791881, -0.1405892923)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0380096933, 0.0802675153, 0.0802675153, 0.0802675153, 0.0802675153], 3)
                _nurbs_edge([(0.4088600551, -0.0173099592), (0.4205882161, -0.0231730327), (0.4435242449, -0.0346390778), (0.4597287204, -0.0544903317), (0.4676471626, -0.0641908004)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0388394774, 0.0759559301, 0.0759559301, 0.0759559301, 0.0759559301], 3)
                _nurbs_edge([(0.2766509926, 0.0241138981), (0.3036228268, 0.0169508612), (0.3483140237, 0.0050820099), (0.391670062, -0.0109525186), (0.4088600551, -0.0173099592)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0836549409, 0.1386127249, 0.1386127249, 0.1386127249, 0.1386127249], 3)
                _nurbs_edge([(0.197772113, 0.046934192), (0.2065653239, 0.0441633538), (0.2326755392, 0.0359357359), (0.259115375, 0.0288279649), (0.2766509926, 0.0241138981)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0276561258, 0.082121014, 0.082121014, 0.082121014, 0.082121014], 3)
                _nurbs_edge([(0.1635416424, 0.0707467244), (0.1679863339, 0.0660463904), (0.1777179564, 0.0557550405), (0.1907125156, 0.0500393656), (0.197772113, 0.046934192)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192157066, 0.0420726611, 0.0420726611, 0.0420726611, 0.0420726611], 3)
                _nurbs_edge([(0.1526275551, 0.1020005987), (0.1530908041, 0.0963467911), (0.1540216648, 0.0849859303), (0.1603584169, 0.0755079334), (0.1635416424, 0.0707467244)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0167192633, 0.0335959831, 0.0335959831, 0.0335959831, 0.0335959831], 3)
                _nurbs_edge([(0.1789205944, 0.1496256039), (0.1712594532, 0.1428477548), (0.1567706339, 0.1300294252), (0.153954584, 0.1109782372), (0.1526275551, 0.1020005987)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0296011857, 0.0559820301, 0.0559820301, 0.0559820301, 0.0559820301], 3)
                _nurbs_edge([(0.2667292034, 0.1699654505), (0.2487582959, 0.1698206578), (0.2177997656, 0.169571223), (0.1904107471, 0.1555202308), (0.1789205944, 0.1496256039)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0529546438, 0.0912251061, 0.0912251061, 0.0912251061, 0.0912251061], 3)
                _nurbs_edge([(0.3473443662, 0.1471451268), (0.3361534622, 0.1537852335), (0.31140975, 0.168466879), (0.2825412633, 0.169435119), (0.2667292034, 0.1699654505)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0384372531, 0.0849869071, 0.0849869071, 0.0849869071, 0.0849869071], 3)
                _nurbs_edge([(0.3818229114, 0.0836451695), (0.3790624984, 0.0963260085), (0.3737170568, 0.1208820025), (0.3559408502, 0.1385843573), (0.3473443662, 0.1471451268)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.038026119, 0.0736362277, 0.0736362277, 0.0736362277, 0.0736362277], 3)
                Line((0.4691353714, 0.0955513761), (0.3818229114, 0.0836451695))
                _nurbs_edge([(0.4383775865, 0.1771588073), (0.4453302359, 0.1655325762), (0.4604654098, 0.1402235148), (0.4660929539, 0.111227489), (0.4691353714, 0.0955513761)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0403334348, 0.0878015731, 0.0878015731, 0.0878015731, 0.0878015731], 3)
                _nurbs_edge([(0.3691725408, 0.2255279467), (0.3834411168, 0.2194825623), (0.4099945997, 0.2082322446), (0.4293998109, 0.1869875949), (0.4383775865, 0.1771588073)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0458454884, 0.0853173713, 0.0853173713, 0.0853173713, 0.0853173713], 3)
                _nurbs_edge([(0.2602799808, 0.2433872864), (0.2798450268, 0.242818028), (0.3169664884, 0.2417379536), (0.3524097987, 0.230732787), (0.3691725408, 0.2255279467)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0583998943, 0.1108042085, 0.1108042085, 0.1108042085, 0.1108042085], 3)
                _nurbs_edge([(0.1831373846, 0.2327212737), (0.1954982289, 0.2358317093), (0.2208181533, 0.2422031184), (0.2469204646, 0.2429863949), (0.2602799808, 0.2433872864)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0381178467, 0.0780805069, 0.0780805069, 0.0780805069, 0.0780805069], 3)
                _nurbs_edge([(0.126334635, 0.2066763685), (0.1343857652, 0.2117411144), (0.1521519482, 0.2229173343), (0.1721835413, 0.2292554256), (0.1831373846, 0.2327212737)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0284206862, 0.0627150595, 0.0627150595, 0.0627150595, 0.0627150595], 3)
                _nurbs_edge([(0.0824303305, 0.1568189607), (0.0882929187, 0.1664015536), (0.1000243802, 0.1855770124), (0.1175614183, 0.1996407383), (0.126334635, 0.2066763685)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0334230161, 0.0668818629, 0.0668818629, 0.0668818629, 0.0668818629], 3)
                _nurbs_edge([(0.066307274, 0.0915826009), (0.0669553408, 0.1030621034), (0.0682402901, 0.1258229971), (0.0777278436, 0.1465471005), (0.0824303305, 0.1568189607)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0341590487, 0.0677285864, 0.0677285864, 0.0677285864, 0.0677285864], 3)
                _nurbs_edge([(0.0859030163, 0.0208892868), (0.0801876842, 0.0318860906), (0.0686630968, 0.0540604149), (0.0670968033, 0.0790074343), (0.066307274, 0.0915826009)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0367399373, 0.0740836428, 0.0740836428, 0.0740836428, 0.0740836428], 3)
                _nurbs_edge([(0.1434498703, -0.0292162254), (0.1316708261, -0.0227721148), (0.108805135, -0.0102626922), (0.0933813733, 0.0107170567), (0.0859030163, 0.0208892868)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0397333832, 0.0771311541, 0.0771311541, 0.0771311541, 0.0771311541], 3)
                _nurbs_edge([(0.2796276485, -0.072128351), (0.2516780281, -0.065127097), (0.2054039441, -0.0535356474), (0.1610241844, -0.0361148381), (0.1434498703, -0.0292162254)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0863147275, 0.1429048013, 0.1429048013, 0.1429048013, 0.1429048013], 3)
                _nurbs_edge([(0.3709088241, -0.1023900463), (0.3603287951, -0.0976388532), (0.3309860107, -0.0844618349), (0.2996591125, -0.0769388186), (0.2796276485, -0.072128351)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0347365028, 0.0963386501, 0.0963386501, 0.0963386501, 0.0963386501], 3)
                _nurbs_edge([(0.3972018635, -0.1500150516), (0.3960541171, -0.1404311042), (0.3937304201, -0.1210276973), (0.3785773306, -0.1086526647), (0.3709088241, -0.1023900463)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0278247031, 0.0563331597, 0.0563331597, 0.0563331597, 0.0563331597], 3)
                _nurbs_edge([(0.3674362575, -0.208802159), (0.3761135324, -0.2003388293), (0.3927836661, -0.184079711), (0.3957700004, -0.1610548316), (0.3972018635, -0.1500150516)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0352061227, 0.0676353783, 0.0676353783, 0.0676353783, 0.0676353783], 3)
                _nurbs_edge([(0.2761549627, -0.2338548853), (0.2945101818, -0.233432692), (0.3271995458, -0.2326807952), (0.3551709275, -0.2160810678), (0.3674362575, -0.208802159)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0539429749, 0.096068673, 0.096068673, 0.096068673, 0.096068673], 3)
                _nurbs_edge([(0.1811530268, -0.2055775478), (0.1943681725, -0.2138085766), (0.2233268517, -0.2318454358), (0.2575495944, -0.2331471835), (0.2761549627, -0.2338548853)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0459310725, 0.1006499071, 0.1006499071, 0.1006499071, 0.1006499071], 3)
                _nurbs_edge([(0.1397291099, -0.1242181613), (0.1429872399, -0.1405938225), (0.1491745793, -0.1716919595), (0.1708781332, -0.1946898768), (0.1811530268, -0.2055775478)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0489487076, 0.0929558569, 0.0929558569, 0.0929558569, 0.0929558569], 3)
                Line((0.0514244711, -0.1381087854), (0.1397291099, -0.1242181613))
                _nurbs_edge([(0.1201334869, -0.2646127298), (0.1036946056, -0.2479314153), (0.0687539166, -0.2124754371), (0.0574239301, -0.1638545415), (0.0514244711, -0.1381087854)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0689094587, 0.1464664117, 0.1464664117, 0.1464664117, 0.1464664117], 3)
            make_face()
            # Profile area: 0.0781122043, perimeter: 2.011102467
            with BuildLine():
                _nurbs_edge([(0.7204068577, -0.2125228598), (0.7246672562, -0.2143969219), (0.7343551474, -0.218658427), (0.7449698457, -0.2188594579), (0.750916568, -0.2189720824)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0138336045, 0.031456789, 0.031456789, 0.031456789, 0.031456789], 3)
                _nurbs_edge([(0.7050279056, -0.1951595499), (0.7068690628, -0.1986248005), (0.7105987752, -0.2056445098), (0.7171099152, -0.2102107336), (0.7204068577, -0.2125228598)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0115954299, 0.0234893679, 0.0234893679, 0.0234893679, 0.0234893679], 3)
                _nurbs_edge([(0.7003150856, -0.1460462763), (0.7001833949, -0.1565673083), (0.6999758604, -0.1731476616), (0.7036757676, -0.1892682504), (0.7050279056, -0.1951595499)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0314000857, 0.0494841681, 0.0494841681, 0.0494841681, 0.0494841681], 3)
                Line((0.7003150856, 0.1620279298), (0.7003150856, -0.1460462763))
                Line((0.7901080524, 0.1620279298), (0.7003150856, 0.1620279298))
                Line((0.7901080524, 0.2314810798), (0.7901080524, 0.1620279298))
                Line((0.7003150856, 0.2314810798), (0.7901080524, 0.2314810798))
                Line((0.7003150856, 0.4155318783), (0.7003150856, 0.2314810798))
                Line((0.6115142977, 0.3619537399), (0.7003150856, 0.4155318783))
                Line((0.6115142977, 0.2314810798), (0.6115142977, 0.3619537399))
                Line((0.5460298931, 0.2314810798), (0.6115142977, 0.2314810798))
                Line((0.5460298931, 0.1620279298), (0.5460298931, 0.2314810798))
                Line((0.6115142977, 0.1620279298), (0.5460298931, 0.1620279298))
                Line((0.6115142977, -0.1410853221), (0.6115142977, 0.1620279298))
                _nurbs_edge([(0.622428385, -0.2465052559), (0.6192914724, -0.2335958057), (0.6108970233, -0.199049824), (0.6112765782, -0.1634081179), (0.6115142977, -0.1410853221)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0397336479, 0.1063281429, 0.1063281429, 0.1063281429, 0.1063281429], 3)
                _nurbs_edge([(0.6601314222, -0.2869369342), (0.6519288561, -0.2815540216), (0.6360483523, -0.2711324826), (0.626867272, -0.2545315216), (0.622428385, -0.2465052559)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0289398382, 0.0560287114, 0.0560287114, 0.0560287114, 0.0560287114], 3)
                _nurbs_edge([(0.7355377352, -0.3023158266), (0.7209312525, -0.3020348818), (0.6947804909, -0.3015318913), (0.6707428584, -0.2914067067), (0.6601314222, -0.2869369342)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0433311076, 0.0775779835, 0.0775779835, 0.0775779835, 0.0775779835], 3)
                _nurbs_edge([(0.8030064976, -0.2943783357), (0.7911377282, -0.296690487), (0.7688421341, -0.3010338848), (0.7461500047, -0.3019073427), (0.7355377352, -0.3023158266)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0362113774, 0.0680234104, 0.0680234104, 0.0680234104, 0.0680234104], 3)
                Line((0.7901080524, -0.2154993965), (0.8030064976, -0.2943783357))
                _nurbs_edge([(0.750916568, -0.2189720824), (0.7566702008, -0.2187678513), (0.7697924182, -0.2183020647), (0.7828024589, -0.2165072486), (0.7901080524, -0.2154993965)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0172611804, 0.0393672956, 0.0393672956, 0.0393672956, 0.0393672956], 3)
            make_face()
            # Profile area: 0.0470461708, perimeter: 1.2322968245
            with BuildLine():
                Line((0.9672134792, 0.2314810798), (0.9672134792, -0.2953705146))
                Line((0.8779166614, 0.2314810798), (0.9672134792, 0.2314810798))
                Line((0.8779166614, -0.2953705146), (0.8779166614, 0.2314810798))
                Line((0.9672134792, -0.2953705146), (0.8779166614, -0.2953705146))
            make_face()
            # Profile area: 0.0091700163, perimeter: 0.3839764595
            with BuildLine():
                Line((0.9672134792, 0.4319029496), (0.9672134792, 0.3292115376))
                Line((0.8779166614, 0.4319029496), (0.9672134792, 0.4319029496))
                Line((0.8779166614, 0.3292115376), (0.8779166614, 0.4319029496))
                Line((0.9672134792, 0.3292115376), (0.8779166614, 0.3292115376))
            make_face()
            # Profile area: 0.1109777129, perimeter: 2.7738482474
            with BuildLine():
                _nurbs_edge([(1.3323386585, 0.1659966753), (1.314043263, 0.1645488229), (1.277813755, 0.1616817093), (1.2484161451, 0.140344208), (1.2338639175, 0.1297818468)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0539096654, 0.1067547652, 0.1067547652, 0.1067547652, 0.1067547652], 3)
                _nurbs_edge([(1.3945983326, 0.1498736487), (1.385163766, 0.1545744268), (1.3655709636, 0.1643365517), (1.343685543, 0.1654298404), (1.3323386585, 0.1659966753)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.031268149, 0.0649346913, 0.0649346913, 0.0649346913, 0.0649346913], 3)
                _nurbs_edge([(1.4315575039, 0.1067134783), (1.4273324896, 0.1153194005), (1.4187206709, 0.1328607945), (1.4027391932, 0.1441321126), (1.3945983326, 0.1498736487)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0282785752, 0.0576400323, 0.0576400323, 0.0576400323, 0.0576400323], 3)
                _nurbs_edge([(1.4419754421, 0.0251060174), (1.4418896596, 0.0411123391), (1.4417413542, 0.0687849253), (1.4345776097, 0.0954654494), (1.4315575039, 0.1067134783)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0477581242, 0.0825668026, 0.0825668026, 0.0825668026, 0.0825668026], 3)
                Line((1.4419754421, -0.2953705146), (1.4419754421, 0.0251060174))
                Line((1.5312722599, -0.2953705146), (1.4419754421, -0.2953705146))
                Line((1.5312722599, 0.0285787032), (1.5312722599, -0.2953705146))
                _nurbs_edge([(1.5263112461, 0.1153951333), (1.5277429315, 0.1040389733), (1.5313747765, 0.0752310995), (1.5313109349, 0.0461786065), (1.5312722599, 0.0285787032)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0343088461, 0.0870333726, 0.0870333726, 0.0870333726, 0.0870333726], 3)
                _nurbs_edge([(1.498529998, 0.1813755975), (1.5046898335, 0.1714756037), (1.5174485506, 0.1509699881), (1.5232900099, 0.1275223737), (1.5263112461, 0.1153951333)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0347533288, 0.0719837225, 0.0719837225, 0.0719837225, 0.0719837225], 3)
                _nurbs_edge([(1.4387508308, 0.2262720511), (1.4509801691, 0.2204520091), (1.4739807158, 0.209505861), (1.4907002173, 0.1903475011), (1.498529998, 0.1813755975)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.040127163, 0.0754698796, 0.0754698796, 0.0754698796, 0.0754698796], 3)
                _nurbs_edge([(1.3511901771, 0.2433872864), (1.3665794367, 0.2427440493), (1.3966470158, 0.2414872907), (1.424939213, 0.2312632158), (1.4387508308, 0.2262720511)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0459025556, 0.0896845437, 0.0896845437, 0.0896845437, 0.0896845437], 3)
                _nurbs_edge([(1.1835103905, 0.156570916), (1.2052675451, 0.1818908479), (1.2494258995, 0.2332802205), (1.31694052, 0.2399856651), (1.3511901771, 0.2433872864)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0962927814, 0.1954359764, 0.1954359764, 0.1954359764, 0.1954359764], 3)
                Line((1.1835103905, 0.2314810798), (1.1835103905, 0.156570916))
                Line((1.1031433021, 0.2314810798), (1.1835103905, 0.2314810798))
                Line((1.1031433021, -0.2953705146), (1.1031433021, 0.2314810798))
                Line((1.1924401199, -0.2953705146), (1.1031433021, -0.2953705146))
                Line((1.1924401199, -0.0076361253), (1.1924401199, -0.2953705146))
                _nurbs_edge([(1.2338639175, 0.1297818468), (1.2218653444, 0.1128534761), (1.1930243951, 0.072162781), (1.1926555285, 0.0217838696), (1.1924401199, -0.0076361253)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0609710134, 0.1465559192, 0.1465559192, 0.1465559192, 0.1465559192], 3)
            make_face()
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)
    return part.part


def model_23667_fc4a5d41_0000():
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.283920012, perimeter: 45.8829607057
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9793260902, perimeter: 13.1031958439
            with BuildLine():
                CenterArc((0, 0), 3.81, 45, 90)
                Line((2.6940768363, 2.6940768363), (2.9185832393, 2.9185832393))
                CenterArc((0, 0), 4.1275, 45, 90)
                Line((-2.6940768363, 2.6940768363), (-2.9185832393, 2.9185832393))
            make_face()
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0.0223251689, 3.8099345909)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-0.0160627558, -3.80996614)):
                Circle(0.635)
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_23686_cba4f679_0007():
    """Model: asse piccolo v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


def model_23699_90c77de4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64.4911674149, perimeter: 48.9047134255
            with BuildLine():
                CenterArc((0.635, -7.62), 3.175, 168.5978245904, 101.4021754096)
                Line((0.635, -10.795), (2.54, -10.795))
                Line((2.54, -10.795), (2.54, -12.065))
                Line((2.54, -12.065), (9.525, -12.065))
                Line((9.525, -12.065), (12.065, -10.16))
                Line((12.065, -8.89), (12.065, -10.16))
                Line((5.715, -8.89), (12.065, -8.89))
                Line((5.715, -7.62), (5.715, -8.89))
                Line((0.635, -7.62), (5.715, -7.62))
                Line((0.635, -0.2053095981), (0.635, -7.62))
                CenterArc((-0.0594780723, -1.2686065039), 1.2700000405, 56.8499787919, 30.4656988445)
                CenterArc((-0.0594780723, -1.2686065039), 1.2700000405, 87.3156776364, 86.1401805772)
                Line((-2.4773371499, -6.9923197744), (-1.3212032331, -1.1238663173))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.62), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 22.8018365594, perimeter: 19.5894680102
            with BuildLine():
                CenterArc((-5.715, 3.81), 3.81, 90, 180)
                Line((-5.715, 7.62), (-5.715, 0))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.62), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((-5.715, 3.81)):
                Circle(1.905)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_23790_2abde9b6_0007():
    """Model: screw v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0779422863, perimeter: 1.0392304845
            with BuildLine():
                Line((0.1200575924, 0.1248446014), (-0.0480898001, 0.1663952257))
                Line((-0.0480898001, 0.1663952257), (-0.1681473926, 0.0415506243))
                Line((-0.1681473926, 0.0415506243), (-0.1200575924, -0.1248446014))
                Line((-0.1200575924, -0.1248446014), (0.0480898001, -0.1663952257))
                Line((0.0480898001, -0.1663952257), (0.1681473926, -0.0415506243))
                Line((0.1681473926, -0.0415506243), (0.1200575924, 0.1248446014))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_23876_74957d38_0002():
    """Model: Endcap Clevis v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 127.4605078283, perimeter: 42.3418218652
            with BuildLine():
                Line((6, 6), (6, 0.8))
                CenterArc((0, 6), 6, 0, 180)
                Line((-6, 6), (-6, 0.8))
                Line((-6, 0.8), (-5.4223344622, 0.6451724982))
                CenterArc((-5.500000082, 0.3554), 0.300000082, 0, 74.9960682402)
                Line((-5.2, 0), (-5.2, 0.3554))
                Line((5.2, 0), (-5.2, 0))
                Line((5.2, 0), (5.2, 0.3554))
                CenterArc((5.500000082, 0.3554), 0.300000082, 105.0039317598, 74.9960682402)
                Line((6, 0.8), (5.4223344622, 0.6451724982))
            make_face()
        # TwoSides extrude (symmetric), distance=1.9
        extrude(amount=1.9, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5440799416, perimeter: 2.9461329437
            with BuildLine():
                CenterArc((1.4, 0.3554), 0.3, 105.0038733597, 74.9961266403)
                Line((1.1, 0), (1.1, 0.3554))
                Line((1.1, 0), (1.9, 0))
                Line((1.9, 0), (1.9, 0.8))
                Line((1.9, 0.8), (1.3223346968, 0.6451724982))
            make_face()
            # Profile area: 0.5440799416, perimeter: 2.9461329437
            with BuildLine():
                Line((-1.9, 0), (-1.9, 0.8))
                Line((-1.9, 0), (-1.1, 0))
                Line((-1.1, 0), (-1.1, 0.3554))
                CenterArc((-1.4, 0.3554), 0.3, 0, 74.9961266403)
                Line((-1.9, 0.8), (-1.3223346968, 0.6451724982))
            make_face()
        # OneSide extrude, distance=-24.3
        extrude(amount=-24.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((0, 6)):
                Circle(3.75)
        # OneSide extrude, distance=-27
        extrude(amount=-27, mode=Mode.SUBTRACT)
    return part.part


def model_23876_74957d38_0005():
    """Model: Rod End GIHR-K 50 DO v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 154.7635659289, perimeter: 46.3157842711
            with BuildLine():
                Line((-3.1055, -10), (3.1055, -10))
                CenterArc((3.1055, -8.5), 1.5, -90, 81.3)
                Line((4.5882408302, -8.7268912304), (4.5912623068, -8.7061804251))
                Line((4.5912623068, -8.7061804251), (5.7392457429, -0.8372922448))
                CenterArc((0, 0), 5.8, -8.3002623467, 196.6005246935)
                Line((-4.5912623068, -8.7061804251), (-5.7392457429, -0.8372922448))
                Line((-4.5882408302, -8.7268912304), (-4.5912623068, -8.7061804251))
                CenterArc((-3.1055, -8.5), 1.5, -171.3, 81.3)
            make_face()
        # TwoSides extrude (symmetric), distance=2
        extrude(amount=2, both=True)

        # Sketch7 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            Circle(3.75)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


def model_23910_316134bd_0008():
    """Model: valve cap v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3632466506, perimeter: 5.8119464091
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2650719139, perimeter: 7.0685835268
            with BuildLine():
                CenterArc((0, 0), 0.6000000089, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3632466506, perimeter: 5.8119464091
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_23951_3afdbe1c_0002():
    """Model: Part_Seven"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3063052837, perimeter: 12.252211349
            with BuildLine():
                CenterArc((4.1245583342, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.1245583342, 0), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.8246680716, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((4.1245583342, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.1245583342, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.3, against=-0.9
        extrude(amount=0.3, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.9, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2252211349, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((4.1245583342, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.1245583342, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 61.1119030198, perimeter: 44.5447466736
            with BuildLine():
                CenterArc((-2, -4.55), 0.05, 90, 90)
                Line((-2.05, -6.1), (-2.05, -4.55))
                Line((-2.05, -6.1), (-0.1422996777, -6.0983400038))
                Line((-0.1422996777, -6.0983400038), (0.1529124642, -6.0980831233))
                CenterArc((0, 0), 6.1, -88.5635808747, 179.9635243678)
                Line((-2.0508517542, 6.0981792346), (-0.1490302725, 6.0981792346))
                Line((-2.0508517542, 6.0981792346), (-2.0508517542, 4.5481792346))
                CenterArc((-2.0008517542, 4.5481792346), 0.05, 180, 90)
                Line((-2.0008517542, 4.4981792346), (-1.8853098392, 4.4981792346))
                CenterArc((-1.8853098392, 2.2981792346), 2.2, 0, 90)
                Line((0.3146901608, -2.3), (0.3146901608, 2.2981792346))
                CenterArc((-1.8853098392, -2.3), 2.2, -90, 90)
                Line((-2, -4.5), (-1.8853098392, -4.5))
            make_face()
            with BuildLine():
                CenterArc((4.1245583342, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (Join)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 5.733176241, perimeter: 77.6365194063
            with BuildLine():
                CenterArc((0, 0), 6.25, -90, 181.3830413216)
                Line((-0.1508517542, 6.2481792346), (-2.2008517542, 6.2481792346))
                Line((-2.2008517542, 6.2481792346), (-2.2, 4.6914383885))
                Line((-2.2, 4.6198088116), (-2.2, 4.6914383885))
                Line((-2.2, 4.5481792346), (-2.2, 4.6198088116))
                CenterArc((-2, 4.5481792346), 0.2, 180, 90)
                Line((-2, 4.3481792346), (-1.8352872861, 4.3481792346))
                CenterArc((-1.8352872861, 2.3481792346), 2, 0, 90)
                Line((0.1647127139, 2.3481792346), (0.1647127139, -2.35))
                CenterArc((-1.8352872861, -2.35), 2, -90, 90)
                Line((-2, -4.35), (-1.8352872861, -4.35))
                CenterArc((-2, -4.55), 0.2, 90, 90)
                Line((-2.2, -6.25), (-2.2, -4.55))
                Line((0, -6.25), (-2.2, -6.25))
            make_face()
            with BuildLine():
                Line((-2, -4.5), (-1.8853098392, -4.5))
                CenterArc((-1.8853098392, -2.3), 2.2, -90, 90)
                Line((0.3146901608, -2.3), (0.3146901608, 2.2981792346))
                CenterArc((-1.8853098392, 2.2981792346), 2.2, 0, 90)
                Line((-2.0008517542, 4.4981792346), (-1.8853098392, 4.4981792346))
                CenterArc((-2.0008517542, 4.5481792346), 0.05, 180, 90)
                Line((-2.0508517542, 6.0981792346), (-2.0508517542, 4.5481792346))
                Line((-2.0508517542, 6.0981792346), (-0.1490302725, 6.0981792346))
                CenterArc((0, 0), 6.1, -88.5635808747, 179.9635243678)
                CenterArc((0, 0), 6.1, -91.3367066578, 2.7731257831)
                Line((-2.05, -6.1), (-0.1422996777, -6.0983400038))
                Line((-2.05, -6.1), (-2.05, -4.55))
                CenterArc((-2, -4.55), 0.05, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=19.2, against=-1.2
        extrude(amount=19.2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-1.2, mode=Mode.ADD)
    return part.part


def model_23956_ee17fe48_0000():
    """Model: Frame v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((-14.75, 4.5), 3.5, 90, 90)
                CenterArc((-14.75, 4.5), 3.5, 180, 270)
            make_face()
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((14.75, 4.5), 3.5, 0, 90)
                CenterArc((14.75, 4.5), 3.5, 90, 270)
            make_face()
            # Profile area: 501.7732349903, perimeter: 123.9867228627
            with BuildLine():
                Line((18.25, 4.5), (18.25, -8))
                CenterArc((14.75, 4.5), 3.5, 90, 270)
                Line((-14.75, 8), (14.75, 8))
                CenterArc((-14.75, 4.5), 3.5, 180, 270)
                Line((-18.25, -8), (-18.25, 4.5))
                Line((18.25, -8), (-18.25, -8))
            make_face()
        # Symmetric extrude, each_side=5.5
        extrude(amount=5.5, both=True)

        # Sketch8 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -8, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 31.4159265359, perimeter: 62.8318530718
            with BuildLine():
                CenterArc((0, 0), 5.5, -180, 180)
                CenterArc((0, 0), 5.5, 0, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=17.5
        extrude(amount=17.5, mode=Mode.ADD)
    return part.part


def model_23957_99511a89_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 122.5, perimeter: 49
            with BuildLine():
                Line((7, -17.5), (0, -17.5))
                Line((7, 0), (7, -17.5))
                Line((0, 0), (7, 0))
                Line((0, -17.5), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_24032_d6172503_0026():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.3598829367, perimeter: 41.5232031636
            with BuildLine():
                Line((4.5555470141, -5), (5, -5))
                Line((5, 0.2), (5, -5))
                CenterArc((4.2, 0.2), 0.8, 0, 90)
                Line((-4.2, 1), (4.2, 1))
                CenterArc((-4.2, 0.2), 0.8, 90, 90)
                Line((-5, -5), (-5, 0.2))
                Line((-5, -5), (-4.555527428, -5))
                Line((-4.555527428, -5), (-4.555527428, -0.3516725411))
                CenterArc((-3.755527428, -0.3516725411), 0.8, 89.9999999999, 90.0000000001)
                Line((-3.755527428, 0.4483274589), (3.7555470141, 0.4483274589))
                CenterArc((3.7555470141, -0.3516725411), 0.8, 0, 90.0000000001)
                Line((4.5555470141, -0.3516725411), (4.5555470141, -5))
            make_face()
        # OneSide extrude, distance=50.8
        extrude(amount=50.8)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 66.675, perimeter: 57.58
            with BuildLine():
                Line((0, 26.25), (0, 0))
                Line((0, 26.25), (-2.54, 26.25))
                Line((-2.54, 26.25), (-2.54, 0))
                Line((0, 0), (-2.54, 0))
            make_face()
            # Profile area: 66.675, perimeter: 57.58
            with BuildLine():
                Line((2.54, 26.25), (2.54, 0))
                Line((2.54, 26.25), (0, 26.25))
                Line((0, 26.25), (0, 0))
                Line((2.54, 0), (0, 0))
            make_face()
            # Profile area: 1.4986, perimeter: 4.9
            with BuildLine():
                Line((-3.02, 1.27), (-3.02, 0))
                Line((-4.2, 1.27), (-3.02, 1.27))
                Line((-4.2, 0), (-4.2, 1.27))
                Line((-3.02, 0), (-4.2, 0))
            make_face()
            # Profile area: 1.4986, perimeter: 4.9
            with BuildLine():
                Line((4.2, 0), (3.02, 0))
                Line((4.2, 1.27), (4.2, 0))
                Line((3.02, 1.27), (4.2, 1.27))
                Line((3.02, 0), (3.02, 1.27))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.246300864, perimeter: 1.759291886
            with Locations((-2.5430982938, 31.75)):
                Circle(0.28)
            # Profile area: 0.246300864, perimeter: 1.759291886
            with Locations((2.5030982938, 31.75)):
                Circle(0.28)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_24036_1b426643_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.42, perimeter: 26.6
            with BuildLine():
                Line((4.1, -1.8), (4.1, 0))
                Line((0, -1.8), (4.1, -1.8))
                Line((0, -2.9), (0, -1.8))
                Line((5.2, -2.9), (0, -2.9))
                Line((5.2, 1.1), (5.2, -2.9))
                Line((0, 1.1), (5.2, 1.1))
                Line((0, 0), (0, 1.1))
                Line((4.1, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((-0.9, 1.6)):
                Circle(0.9)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5493807017, perimeter: 5.7132741229
            with BuildLine():
                CenterArc((1.6, 1.6), 1.6, 90, 90)
                Line((0, 3.2), (1.6, 3.2))
                Line((0, 3.2), (0, 1.6))
            make_face()
            # Profile area: 0.5493807017, perimeter: 5.7132741229
            with BuildLine():
                Line((0, 0), (1.6, 0))
                CenterArc((1.6, 1.6), 1.6, -180, 90)
                Line((0, 1.6), (0, 0))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((1.6, 1.6)):
                Circle(0.8)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_24086_a8e5514c_0003():
    """Model: Swivel Boss v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2563577619, perimeter: 5.1091881076
            with BuildLine():
                CenterArc((0, 0), 0.375, -53.1301023542, 106.2602047083)
                Line((-0.625, 0.3), (0.225, 0.3))
                Line((-0.625, 0.225), (-0.625, 0.3))
                Line((-0.275, 0.225), (-0.625, 0.225))
                Line((-0.275, -0.225), (-0.275, 0.225))
                Line((-0.625, -0.225), (-0.275, -0.225))
                Line((-0.625, -0.3), (-0.625, -0.225))
                Line((0.225, -0.3), (-0.625, -0.3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0.475, -0.45)):
                Circle(0.075)
        # OneSide extrude, distance=-0.75
        extrude(amount=-0.75, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.275, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.1, 0)):
                Circle(0.1)
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)
    return part.part


def model_24133_2ac9dc04_0002():
    """Model: Mordant"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 62, perimeter: 39
            with BuildLine():
                Line((7.75, -2), (7.75, 2))
                Line((7.75, 2), (-7.75, 2))
                Line((-7.75, 2), (-7.75, -2))
                Line((-7.75, -2), (7.75, -2))
            make_face()
        # OneSide extrude, distance=1.25
        extrude(amount=1.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((5.25, 0)):
                Circle(0.45)
        # OneSide extrude, distance=-1.25
        extrude(amount=-1.25, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((-5.25, 0)):
                Circle(0.45)
        # OneSide extrude, distance=-1.25
        extrude(amount=-1.25, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9475043443, perimeter: 7.2884949563
            with BuildLine():
                CenterArc((5.25, 0), 0.71, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.25, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9475043443, perimeter: 7.2884949563
            with BuildLine():
                CenterArc((-5.25, 0), 0.71, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.25, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


def model_24133_2ac9dc04_0004():
    """Model: Stop"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36.25, perimeter: 34
            with BuildLine():
                Line((7.25, -1.25), (7.25, 1.25))
                Line((7.25, 1.25), (-7.25, 1.25))
                Line((-7.25, 1.25), (-7.25, -1.25))
                Line((-7.25, -1.25), (7.25, -1.25))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9032078879, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((5.25, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.25, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9032078879, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((2.25, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.25, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9032078879, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((-5.25, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.25, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((5.25, 0)):
                Circle(0.45)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((2.25, 0)):
                Circle(0.45)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((-5.25, 0)):
                Circle(0.45)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((-5.25, 0)):
                Circle(0.45)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((2.25, 0)):
                Circle(0.45)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((5.25, 0)):
                Circle(0.45)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_24157_49bf3a04_0009():
    """Model: pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_24157_49bf3a04_0013():
    """Model: Tread 2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2672563597, perimeter: 32.6725635973
            with BuildLine():
                CenterArc((0, 0), 2.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_24284_3710e946_0005():
    """Model: guide_D‚faut v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5327901243, perimeter: 4.3888049371
            Circle(0.6985)
        # OneSide extrude, distance=1.1938
        extrude(amount=1.1938)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1938, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3425342559, perimeter: 2.0747077884
            Circle(0.3302)
        # OneSide extrude, distance=3.302
        extrude(amount=3.302, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.1297171146, perimeter: 1.2767432544
            with Locations((0, 0.6604)):
                Circle(0.2032)
        # TwoSides extrude, along=1.016, against=-1.143
        extrude(amount=1.016, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1.143, mode=Mode.SUBTRACT)
    return part.part


def model_24291_a6aa039b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 76.451461606, perimeter: 48.7303194844
            with BuildLine():
                Line((3.6962773806, 54.7106140726), (3.6962773806, 47.8526138537))
                Line((3.6962773806, 47.8526138537), (1.1562772996, 41.502613651))
                Line((1.1562772996, 41.502613651), (1.1562772996, 34.644613651))
                Line((1.1562772996, 34.644613651), (4.9662772996, 34.644613651))
                Line((4.9662772996, 34.644613651), (4.9662772996, 41.502613651))
                Line((7.5062773806, 47.8526138537), (4.9662772996, 41.502613651))
                Line((7.5062773806, 54.7106140726), (7.5062773806, 47.8526138537))
                Line((3.6962773806, 54.7106140726), (7.5062773806, 54.7106140726))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 38.7095988373, perimeter: 27.9399995804
            with BuildLine():
                Line((29.2099995613, 45.7199993134), (25.3999996185, 45.7199993134))
                Line((29.2099995613, 55.8799991608), (29.2099995613, 45.7199993134))
                Line((25.3999996185, 55.8799991608), (29.2099995613, 55.8799991608))
                Line((25.3999996185, 45.7199993134), (25.3999996185, 55.8799991608))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch7 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8064403397, perimeter: 10.4140002027
            with BuildLine():
                Line((3.8100001216, 7.6200002432), (3.8100001216, 5.7150001824))
                Line((3.8100001216, 5.7150001824), (4.4450001216, 5.7150001824))
                Line((4.4450001216, 5.7150001824), (4.4450001216, 4.9530001824))
                Line((4.4450001216, 4.9530001824), (5.7150001216, 4.9530001824))
                Line((5.7150001216, 4.9530001824), (5.7150002027, 5.7150001824))
                Line((6.3500002027, 5.7150001824), (5.7150002027, 5.7150001824))
                Line((6.3500002027, 7.6200002432), (6.3500002027, 5.7150001824))
                Line((3.8100001216, 7.6200002432), (6.3500002027, 7.6200002432))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_24302_2bcddd22_0000():
    """Model: 5SupportAdjustingScrew"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2026829916, perimeter: 1.595929068
            Circle(0.254)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.65, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2533537395, perimeter: 3.9898226701
            with BuildLine():
                CenterArc((0, 0), 0.381, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.254, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2026829916, perimeter: 1.595929068
            Circle(0.254)
        # OneSide extrude, distance=5.334
        extrude(amount=5.334, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.984, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=0.0635
        extrude(amount=0.0635, mode=Mode.ADD)
    return part.part


def model_24308_89c2be2b_0007():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 42 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.5120971613, perimeter: 56.5620780782
            with BuildLine():
                CenterArc((2.3622, -1.9812), 0.9017, -144.7898842577, 126.7653609957)
                CenterArc((2.0320000648, 0), 2.5532424461, -62.2798788402, 124.5597576804)
                CenterArc((2.3622, 1.9812), 0.9017, 18.0245232619, 126.7653609957)
                CenterArc((1.2104143212, 2.794), 0.508, -146.1184181195, 110.9083023772)
                CenterArc((0, 1.9812), 0.9499940565, 33.8815818805, 112.2368394573)
                CenterArc((-1.2104143212, 2.794), 0.508, -144.7898842577, 110.9082963588)
                CenterArc((-2.3622, 1.9812), 0.9017, 35.2101157423, 126.7653609957)
                CenterArc((-2.0320000648, 0), 2.5532424461, 117.7201211598, 124.5578453318)
                CenterArc((-2.3622428058, -1.9812606637), 0.9017, -161.9821791036, 126.7767810749)
                CenterArc((-1.2104143212, -2.794), 0.508, 33.8815878988, 110.9082963588)
                CenterArc((0, -1.9812), 0.9499940565, -146.1184213378, 112.2368394573)
                CenterArc((1.2104143212, -2.794), 0.508, 35.2101157423, 110.9083023772)
            make_face()
            with BuildLine():
                CenterArc((2.3622, 1.9812), 0.4191, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.3622, 1.9812), 0.4191, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.3622, -1.9812), 0.4191, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.3622, -1.9812), 0.4191, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5390811661, 1.3910107839), (0.5685379496, 1.3910107839))
                CenterArc((1.3335511842, 0), 1.5875, -121.5949915492, 240.4044350481)
                Line((-0.529168783, -1.3521892161), (0.5018417555, -1.3521892161))
                CenterArc((-1.3333976345, 0.0165226617), 1.5875, 59.9763894774, 240.4612887382)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.8862, 0), 0.3048, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8862, 0), 0.3048, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.9652
        extrude(amount=0.9652, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.9652, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5765119874, perimeter: 3.0563476661
            with BuildLine():
                CenterArc((0, -1.41605), 0.59055, -179.666197316, 180.9505487993)
                CenterArc((1.3335511842, 0), 1.5875, -118.8094434988, 0.8967431897)
                Line((0.5685379496, -1.3910107839), (-0.5390811661, -1.3910107839))
                CenterArc((-1.3333976345, -0.0165226617), 1.5875, -62.0992209391, 2.1228314616)
            make_face()
            # Profile area: 1.0510986074, perimeter: 4.0004752915
            with BuildLine():
                Line((-0.529168783, 1.3521892161), (0.5018417555, 1.3521892161))
                CenterArc((1.3335511842, 0), 1.5875, 110.0171984277, 11.5777931215)
                CenterArc((0, 1.41605), 0.79375, 5.4616701609, 170.2336895679)
                CenterArc((-1.3333976345, -0.0165226617), 1.5875, 59.5623217844, 10.4787780041)
            make_face()
        # OneSide extrude, distance=-1.7272
        extrude(amount=-1.7272, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.762, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0395865218, perimeter: 0.8162278338
            with BuildLine():
                Line((0.15875, -1.3910107839), (-0.15875, -1.3910107839))
                CenterArc((0, -1.3910107839), 0.15875, 180, 180)
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)
    return part.part


def model_24372_03b260fe_0002():
    """Model: Untitled v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((5.5, -5.5), (-2.5, -5.5))
                Line((5.5, 2.5), (5.5, -5.5))
                Line((-2.5, 2.5), (5.5, 2.5))
                Line((-2.5, -5.5), (-2.5, 2.5))
            make_face()
        # OneSide extrude, distance=112
        extrude(amount=112)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 79.5012419221, perimeter: 35.8753104805
            with BuildLine():
                Line((102.0623447597, 2.5), (112, 2.5))
                Line((102.0623447597, -5.5), (102.0623447597, 2.5))
                Line((112, -5.5), (102.0623447597, -5.5))
                Line((112, 2.5), (112, -5.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(112, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8, perimeter: 18
            with BuildLine():
                Line((-2.5, 2.5), (-2.5, -5.5))
                Line((-3.5, 2.5), (-2.5, 2.5))
                Line((-3.5, -5.5), (-3.5, 2.5))
                Line((-2.5, -5.5), (-3.5, -5.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)
    return part.part


def model_24372_03b260fe_0022():
    """Model: plate v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 109.2, perimeter: 43.6
            with BuildLine():
                Line((-14, 7.8), (0, 7.8))
                Line((-14, 0), (-14, 7.8))
                Line((0, 0), (-14, 0))
                Line((0, 7.8), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_24422_ed84404a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1300, perimeter: 168.2842712475
            with BuildLine():
                Line((130, 80), (140, 70))
                Line((140, 70), (150, 70))
                Line((150, 70), (150, 100))
                Line((150, 100), (100, 100))
                Line((100, 100), (100, 70))
                Line((100, 70), (110, 70))
                Line((110, 70), (120, 80))
                Line((120, 80), (130, 80))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 9.9944239171, perimeter: 21.9899348467
            with BuildLine():
                Line((116.9094132942, -92.4999991578), (116.9094132942, -82.5))
                Line((116.9094132942, -82.5), (115.9094632925, -82.5099997022))
                Line((115.9094632925, -82.5099997022), (115.9094785923, -92.5000006892))
                Line((115.9094785923, -92.5000006892), (116.9094132942, -92.4999991578))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -100, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2388.9944768912, perimeter: 228.5484319293
            with BuildLine():
                Line((158.4752284834, -102.7792485413), (90.4752284834, -102.7792485413))
                Line((158.4752284834, -67.5), (158.4752284834, -102.7792485413))
                Line((90.4752284834, -67.5), (158.4752284834, -67.5))
                Line((90.4752284834, -102.7792485413), (90.4752284834, -67.5))
            make_face()
            with BuildLine():
                Line((115.9094632925, -82.5099997022), (115.9094785923, -92.5000006892))
                Line((116.9094132942, -82.5), (115.9094632925, -82.5099997022))
                Line((116.9094132942, -92.4999991578), (116.9094132942, -82.5))
                Line((115.9094785923, -92.5000006892), (116.9094132942, -92.4999991578))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_24443_996411f9_0003():
    """Model: P14-CRANK SHAFT"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0309748208, perimeter: 0.9518547978
            with BuildLine():
                Line((-0.2236067977, -0.2), (0.2236067977, -0.2))
                CenterArc((0, 0), 0.3, -138.1896851042, 96.3793702084)
            make_face()
            # Profile area: 0.251768518, perimeter: 1.8275279853
            with BuildLine():
                CenterArc((0, 0), 0.3, -41.8103148958, 263.6206297916)
                Line((-0.2236067977, -0.2), (0.2236067977, -0.2))
            make_face()
        # Symmetric extrude, each_side=3.3
        extrude(amount=3.3, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0309748208, perimeter: 0.9518547978
            with BuildLine():
                Line((-0.2236067977, -0.2), (0.2236067977, -0.2))
                CenterArc((0, 0), 0.3, -138.1896851042, 96.3793702084)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -3.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0309748208, perimeter: 0.9518547978
            with BuildLine():
                Line((-0.2236067977, 0.2), (0.2236067977, 0.2))
                CenterArc((0, 0), 0.3, 41.8103148958, 96.3793702084)
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.3713805974, 3.3, -0.2405668646), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0309748208, perimeter: 0.9518547978
            with BuildLine():
                CenterArc((-0.3713805974, 0.2405668646), 0.3, 131.8103148958, 96.3793702084)
                Line((-0.5713805974, 0.4641736624), (-0.5713805974, 0.0169600669))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_24476_568e9ca0_0031():
    """Model: perno v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=3.33
        extrude(amount=3.33)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.4398229715, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.2, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.0779422863, perimeter: 1.0392304845
            with BuildLine():
                Line((0.0866025404, 0.15), (-0.0866025404, 0.15))
                Line((-0.0866025404, 0.15), (-0.1732050808, 0))
                Line((-0.1732050808, 0), (-0.0866025404, -0.15))
                Line((-0.0866025404, -0.15), (0.0866025404, -0.15))
                Line((0.0866025404, -0.15), (0.1732050808, 0))
                Line((0.1732050808, 0), (0.0866025404, 0.15))
            make_face()
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.SUBTRACT)
    return part.part


def model_24603_a4021250_0006():
    """Model: Scissor_lower_mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.4, perimeter: 13.6
            with BuildLine():
                Line((9.8, 3), (6, 3))
                Line((9.8, 6), (9.8, 3))
                Line((6, 6), (9.8, 6))
                Line((6, 3), (6, 6))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 7.9110085538, perimeter: 15.5898810327
            with BuildLine():
                Line((0.3, 3), (0.3, 6))
                Line((2.8475107331, 3.1009408979), (0.3, 3))
                CenterArc((2.8, 4.3), 1.2, -87.7309365198, 166.9013025525)
                Line((0.3, 6), (3.0254672063, 5.4786282446))
            make_face()
            with BuildLine():
                CenterArc((2.8, 4.3), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(9.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.9110085538, perimeter: 15.5898810327
            with BuildLine():
                Line((-0.3, 6), (-3.0254672063, 5.4786282446))
                CenterArc((-2.8, 4.3), 1.2, 100.8296339674, 166.9013025525)
                Line((-2.8475107331, 3.1009408979), (-0.3, 3))
                Line((-0.3, 3), (-0.3, 6))
            make_face()
            with BuildLine():
                CenterArc((-2.8, 4.3), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


def model_24660_cadd37c3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0386890711, perimeter: 3.6128315516
            Circle(0.575)
        # OneSide extrude, distance=3.025
        extrude(amount=3.025)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.025), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)
    return part.part


def model_24720_19eea793_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch12 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-24.1796052633, 50.8170378927)):
                Circle(0.2)
        # TwoSides extrude (symmetric), distance=10
        extrude(amount=10, both=True)
    return part.part


def model_24725_73d5dcf0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180, perimeter: 54
            with BuildLine():
                Line((-7.5, 6), (7.5, 6))
                Line((-7.5, -6), (-7.5, 6))
                Line((7.5, -6), (-7.5, -6))
                Line((7.5, 6), (7.5, -6))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch10 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 138.2548099579, perimeter: 50.5637024895
            with BuildLine():
                Line((-4, 23), (-4, 5.7181487553))
                Line((4, 5.7181487553), (-4, 5.7181487553))
                Line((4, 5.7181487553), (4, 23))
                Line((-4, 23), (4, 23))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_24861_c05860c8_0001():
    """Model: 6_"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.65, perimeter: 5.7
            with BuildLine():
                Line((0.5, -1.5999999851), (0.25, -1.5999999851))
                Line((0.5, 1.0000000149), (0.5, -1.5999999851))
                Line((0.25, 1.0000000149), (0.5, 1.0000000149))
                Line((0.25, -1.5999999851), (0.25, 1.0000000149))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3105194184, perimeter: 3.3020982194
            with BuildLine():
                CenterArc((0.0041000149, 0.9), 0.4, 50.0010985884, 39.9989014116)
                Line((0.8571091835, 0.7064227071), (0.2612091835, 1.2064227071))
                CenterArc((0.6000000149, 0.4), 0.4, 0, 50.0010985884)
                Line((1.0000000149, 0.4), (1.0000000149, 1.3))
                Line((1.0000000149, 1.3), (0.0041000149, 1.3))
            make_face()
            # Profile area: 0.3105194184, perimeter: 3.3020982192
            with BuildLine():
                Line((-0.6040999851, 1.3), (-1.5999999851, 1.3))
                Line((-1.5999999851, 1.3), (-1.5999999851, 0.4000000001))
                CenterArc((-1.1999999851, 0.4), 0.4, 129.9989014116, 50.0010985799)
                Line((-1.4571091537, 0.7064227071), (-0.8612091537, 1.2064227071))
                CenterArc((-0.6040999851, 0.9), 0.4, 90, 39.9989014116)
            make_face()
            # Profile area: 0.0343362939, perimeter: 1.4283185308
            with BuildLine():
                CenterArc((-1.1999999851, 0.4), 0.4, 179.9999999915, 90.0000000085)
                Line((-1.5999999851, 0.4000000001), (-1.5999999851, 0))
                Line((-1.5999999851, 0), (-1.1999999851, 0))
            make_face()
            # Profile area: 0.0343362939, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((0.6000000149, 0.4), 0.4, -90, 90)
                Line((0.6000000149, 0), (1.0000000149, 0))
                Line((1.0000000149, 0), (1.0000000149, 0.4))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0754767635, perimeter: 0.9738937226
            with Locations((0.6000000149, 0.4)):
                Circle(0.155)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.1999999851, 0.4)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5199999851, 1)):
                Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_24861_c05860c8_0003():
    """Model: 4_"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2271846303, perimeter: 3.926990817
            Circle(0.625)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            Circle(0.325)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_24869_5c729cf1_0004():
    """Model: Barrel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1250353876, perimeter: 5.0014155045
            with BuildLine():
                CenterArc((0, 0), 0.423, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.373, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.7
        extrude(amount=7.7)

        # Sketch8 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.2885757685, -0.7247976065, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1250353876, perimeter: 5.0014155045
            with BuildLine():
                CenterArc((-1.2885757685, 0.7247976065), 0.423, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.2885757685, 0.7247976065), 0.373, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1093274243, perimeter: 4.3730969738
            with BuildLine():
                CenterArc((-1.2885757685, 0.7247976065), 0.373, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.2885757685, 0.7247976065), 0.323, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-7.7
        extrude(amount=-7.7, mode=Mode.ADD)

        # Sketch10 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0248060156, perimeter: 4.1343359321
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.323, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0901762755, perimeter: 3.7573448137
            with BuildLine():
                CenterArc((0, 0), 0.323, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


def model_24927_543d2801_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 158.8535808733, perimeter: 83.4639957106
            with BuildLine():
                Line((-1.2066916708, 5.128652942), (15.5838403859, 4.5773502692))
                CenterArc((-1.2395081257, 4.1291915469), 1, 88.1194179916, 76.8805820084)
                Line((-3.1547005384, 0.8452994616), (-2.205433952, 4.388010592))
                Line((-0.8452994616, 3.1547005384), (-3.1547005384, 0.8452994616))
                Line((2.3094010768, 2.3094010768), (-0.8452994616, 3.1547005384))
                Line((3.1547005384, -0.8452994616), (2.3094010768, 2.3094010768))
                Line((0.8452994616, -3.1547005384), (3.1547005384, -0.8452994616))
                Line((0.8452994616, -3.1547005384), (6.0491327905, -0.8452994616))
                Line((6.0491327905, -0.8452994616), (29, -0.8452994616))
                CenterArc((29.0838403859, 1.1547005384), 2.0017565312, -92.4004446893, 180)
                Line((15.5838403859, 4.5773502692), (29.1676807719, 3.1547005384))
            make_face()
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.0942648997, perimeter: 51.2003280504
            with BuildLine():
                CenterArc((-29.0838403859, -1.1547005384), 1.2731687285, 87.7572409709, 180)
                Line((-29.1336639778, -2.4268940068), (-7.5498235918, -3.2721934684))
                CenterArc((-7.5, -2), 1.2731687285, -92.2427590291, 180)
                Line((-7.4501764082, -0.7278065316), (-29.0340167941, 0.11749293))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 108.2633854355, perimeter: 69.5683607966
            with BuildLine():
                Line((-2.7917293175, -2.6065212537), (-3.6397962892, 0.558507773))
                CenterArc((-4.1227592023, 0.4290982505), 0.5, 15, 98.9310948639)
                Line((-4.3255780522, 0.886115224), (-4.3278473465, 0.8851081375))
                CenterArc((-7.6385940187, 8.3452994616), 8.1618317871, -90, 23.9310948639)
                Line((-7.6385940187, 0.1834676745), (-29.0152535511, 0.1834676745))
                CenterArc((-29.0838403859, -1.1547005384), 1.3399247442, 87.0659141339, 181.3293473041)
                Line((-29.1213640537, -2.4940997673), (-15.538454227, -3.9166520397))
                Line((-15.538454227, -3.9166520397), (1.2284106438, -4.4671776208))
                CenterArc((1.2395081257, -4.1291915469), 0.3381682129, -91.8805820084, 76.8805820084)
                Line((1.5661535362, -4.2167159208), (1.6829545415, -3.7808086345))
                CenterArc((1.4897693763, -3.7290448255), 0.2, -15, 150)
                Line((1.34834802, -3.5876234692), (1.1247431687, -3.8112283206))
                CenterArc((0.9833218125, -3.6698069643), 0.2, -105, 60)
                Line((0.9315580035, -3.8629921296), (-2.4381759269, -2.9600746443))
                CenterArc((-2.3087664043, -2.4771117311), 0.5, -165, 60)
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


def model_25132_c8588afc_0004():
    """Model: bearingsupport(addscrewholes) v4 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.3118359171, perimeter: 19.1637151869
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.2986722863, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0602875206, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0602875206, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=2.1
        extrude(amount=2.1, mode=Mode.ADD)
    return part.part


def model_25134_ec81c644_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4093459036, perimeter: 4.9204652607
            with BuildLine():
                Line((0.9718899091, -1.6905413348), (2.8568835412, -0.6068610011))
                CenterArc((2.508, 0), 0.7, -147.9968445806, 87.8913801055)
                CenterArc((0, 0), 1.95, -60.1054608783, 49.1384254889)
            make_face()
            # Profile area: 0.4093458628, perimeter: 4.9204653338
            with BuildLine():
                CenterArc((2.508, 0), 0.7, 60.1054643184, 87.8913802622)
                Line((2.8568835429, 0.6068610002), (0.97188991, 1.6905413343))
                CenterArc((0, 0), 1.95, 10.9670353894, 49.1384275538)
            make_face()
            # Profile area: 0.4093458628, perimeter: 4.9204606094
            with BuildLine():
                CenterArc((-2.508, 0), 0.7, -119.8943511678, 87.8911957484)
                Line((-2.8568815885, -0.6068621237), (-0.9718900036, -1.6905412805))
                CenterArc((0, 0), 1.95, -169.0329646106, 49.1384243825)
            make_face()
            # Profile area: 1.4682541819, perimeter: 4.3627475279
            with BuildLine():
                CenterArc((0, 0), 1.95, 169.0329646106, 21.9340707788)
                CenterArc((-2.508, 0), 0.7, 32.0031554194, 87.8881665102)
                CenterArc((-2.508, 0), 0.7, 119.8913219297, 120.2143269025)
                CenterArc((-2.508, 0), 0.7, -119.8943511678, 87.8911957484)
            make_face()
            # Profile area: 11.8036535239, perimeter: 12.3231756518
            with BuildLine():
                CenterArc((0, 0), 1.95, -169.0329646106, 49.1384243825)
                CenterArc((0, 0), 1.95, -119.8945402281, 59.7890772533)
                CenterArc((0, 0), 1.95, -60.1054608783, 49.1384254889)
                CenterArc((2.508, 0), 0.7, 147.9968445806, 64.0063108389)
                CenterArc((0, 0), 1.95, 10.9670353894, 49.1384275538)
                CenterArc((0, 0), 1.95, 60.1054629432, 59.789077121)
                CenterArc((0, 0), 1.95, 119.8945400642, 49.1384245464)
                CenterArc((-2.508, 0), 0.7, -32.0031554194, 64.0063108389)
            make_face()
            # Profile area: 0.4093458626, perimeter: 4.9203866023
            with BuildLine():
                CenterArc((0, 0), 1.95, 119.8945400642, 49.1384245464)
                Line((-0.9718899987, 1.6905412832), (-2.8568495037, 0.6068805692))
                CenterArc((-2.508, 0), 0.7, 32.0031554194, 87.8881665102)
            make_face()
            # Profile area: 1.4682541819, perimeter: 4.3627475279
            with BuildLine():
                CenterArc((2.508, 0), 0.7, -147.9968445806, 87.8913801055)
                CenterArc((2.508, 0), 0.7, -60.105464475, 120.2109287934)
                CenterArc((2.508, 0), 0.7, 60.1054643184, 87.8913802622)
                CenterArc((0, 0), 1.95, -10.9670353894, 21.9340707788)
            make_face()
            # Profile area: 0.0711262184, perimeter: 1.5284870256
            with BuildLine():
                CenterArc((0, 0), 1.95, -10.9670353894, 21.9340707788)
                CenterArc((2.508, 0), 0.7, 147.9968445806, 64.0063108389)
            make_face()
            # Profile area: 0.0711262184, perimeter: 1.5284870256
            with BuildLine():
                CenterArc((-2.508, 0), 0.7, -32.0031554194, 64.0063108389)
                CenterArc((0, 0), 1.95, 169.0329646106, 21.9340707788)
            make_face()
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.4128249096, perimeter: 2.2776546739
            with Locations((2.508, 0)):
                Circle(0.3625)
            # Profile area: 0.4128249096, perimeter: 2.2776546739
            with Locations((-2.508, 0)):
                Circle(0.3625)
        # OneSide extrude, distance=-0.55
        extrude(amount=-0.55, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1415141138, perimeter: 18.7553081419
            with BuildLine():
                CenterArc((0, 0), 1.66, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_25139_f79f51e3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.3432604841, perimeter: 21.1862223351
            with BuildLine():
                Line((-0.9309081402, 3.865253384), (-0.9371126907, 3.8490269402))
                Line((-0.9371126907, 3.8490269402), (-2.1016027176, 0.8035956803))
                CenterArc((0, 0), 2.25, 159.0745064007, 47.108166118)
                Line((-2.0191316615, -0.9927775852), (-0.9351497192, -3.8542527384))
                CenterArc((0, -3.5), 1, -159.2523465991, 138.5046931983)
                Line((0.9351497192, -3.8542527384), (2.1016108143, -0.8035745052))
                CenterArc((0, 0), 2.25, -20.924916305, 41.8504099043)
                Line((0.9371126907, 3.8490269402), (2.1016027176, 0.8035956803))
                Line((0.9309081402, 3.865253384), (0.9371126907, 3.8490269402))
                CenterArc((0, 3.5), 1, 21.4231772175, 137.153645565)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9008845396, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, -3.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 3.5)):
                Circle(0.5)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_25186_e5476b73_0003():
    """Model: przycisk z nakretki v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.24, perimeter: 2.2
            with BuildLine():
                Line((0.4, -0.15), (0.4, 0.15))
                Line((0.4, 0.15), (-0.4, 0.15))
                Line((-0.4, 0.15), (-0.4, -0.15))
                Line((-0.4, -0.15), (0.4, -0.15))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.04, perimeter: 0.8
            with BuildLine():
                Line((-0.1, 0.1), (-0.1, -0.1))
                Line((-0.1, -0.1), (0.1, -0.1))
                Line((0.1, -0.1), (0.1, 0.1))
                Line((0.1, 0.1), (-0.1, 0.1))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0003976036, perimeter: 0.0797603643
            with BuildLine():
                Line((-0.3399999924, 0.0199999996), (-0.359880175, 0.0199999996))
                Line((-0.359880175, 0.0199999996), (-0.359880175, 0))
                Line((-0.3399999924, 0), (-0.359880175, 0))
                Line((-0.3399999924, 0), (-0.3399999924, 0.0199999996))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_25186_e5476b73_0004():
    """Model: śrubka do szyjki v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5654866776, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_25199_d7aff7a5_0012():
    """Model: Part 37 - AntiReverse Lever v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2788724976, perimeter: 3.5447331561
            with BuildLine():
                Line((0, 0.15), (-0.1, 0.15))
                Line((0, 0.15), (0, 1.471))
                Line((-0.125, 1.471), (0, 1.471))
                Line((-0.125, 1.471), (-0.2490891319, 0.0213214538))
                CenterArc((0, 0), 0.25, 175.107539447, 34.892460553)
                Line((-0.1, -0.125), (-0.2165063509, -0.125))
                Line((-0.1, 0.15), (-0.1, -0.125))
            make_face()
            # Profile area: 0.3122590507, perimeter: 4.3183319317
            with BuildLine():
                Line((0.1, 0.15), (0, 0.15))
                Line((0.1, -0.125), (0.1, 0.15))
                Line((0.1, -0.15), (0.1, -0.125))
                Line((-0.1, -0.15), (0.1, -0.15))
                Line((-0.1, -0.125), (-0.1, -0.15))
                Line((-0.1, -0.125), (-0.2165063509, -0.125))
                CenterArc((0, 0), 0.25, -150, 154.892460553)
                Line((0.125, 1.471), (0.2490891319, 0.0213214538))
                Line((0, 1.471), (0.125, 1.471))
                Line((0, 0.15), (0, 1.471))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.014375, perimeter: 0.6167728023
            with BuildLine():
                Line((0.125, -1.471), (0, -1.241))
                Line((0, -1.471), (0, -1.241))
                Line((0.125, -1.471), (0, -1.471))
            make_face()
            # Profile area: 0.014375, perimeter: 0.6167728023
            with BuildLine():
                Line((-0.125, -1.471), (0, -1.241))
                Line((0, -1.471), (-0.125, -1.471))
                Line((0, -1.471), (0, -1.241))
            make_face()
        # OneSide extrude, distance=0.53
        extrude(amount=0.53, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0627796713, perimeter: 1.4610337458
            with BuildLine():
                CenterArc((0, 0), 0.25, -62.6128924973, 57.7204319443)
                Line((0.115, -0.2219797288), (0.05, -0.65))
                Line((0.05, -0.65), (0.1952757018, -0.65))
                Line((0.1952757018, -0.65), (0.2490891319, -0.0213214538))
            make_face()
            # Profile area: 0.0627796713, perimeter: 1.4610337458
            with BuildLine():
                Line((-0.1952757018, -0.65), (-0.05, -0.65))
                Line((-0.115, -0.2219797288), (-0.05, -0.65))
                CenterArc((0, 0), 0.25, -175.107539447, 57.7204319443)
                Line((-0.2490891319, -0.0213214538), (-0.1952757018, -0.65))
            make_face()
        # OneSide extrude, distance=-0.26
        extrude(amount=-0.26, mode=Mode.SUBTRACT)
    return part.part


def model_25203_1cc0cb3c_0007():
    """Model: AxisHolder v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7, perimeter: 16.2
            with BuildLine():
                Line((7, -1.1), (0, -1.1))
                Line((7, 0), (7, -1.1))
                Line((0, 0), (7, 0))
                Line((0, -1.1), (0, 0))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4, perimeter: 14.4
            with BuildLine():
                Line((-7, 0.2), (0, 0.2))
                Line((-7, 0), (-7, 0.2))
                Line((0, 0), (-7, 0))
                Line((0, 0.2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.65
        extrude(amount=0.65, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1, 0.73)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-6, 0.73)):
                Circle(0.15)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


def model_25203_1cc0cb3c_0010():
    """Model: Axle Sleeve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1756150293, perimeter: 2.7017696821
            with BuildLine():
                CenterArc((0, 0), 0.28, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.65, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.321149309, perimeter: 4.4296456416
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.28, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1756150293, perimeter: 2.7017696821
            with BuildLine():
                CenterArc((0, 0), 0.28, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1416858287, perimeter: 2.5761059759
            with BuildLine():
                CenterArc((0, 0), 0.26, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_25203_1cc0cb3c_0011():
    """Model: SmallWheel v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1756150293, perimeter: 2.7017696821
            with BuildLine():
                CenterArc((0, 0), 0.28, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.86
        extrude(amount=0.86)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.86, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.281800861, perimeter: 4.335397862
            with BuildLine():
                CenterArc((0, 0), 0.41, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.28, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1756150293, perimeter: 2.7017696821
            with BuildLine():
                CenterArc((0, 0), 0.28, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.96, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3141592654, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_22323_aa6edb8b_0003": {"func": model_22323_aa6edb8b_0003, "volume": 223.1418283973, "area": 227.6869275689},
    "model_22340_ec24cd79_0018": {"func": model_22340_ec24cd79_0018, "volume": 6.1499650481, "area": 23.5678326862},
    "model_22340_ec24cd79_0031": {"func": model_22340_ec24cd79_0031, "volume": 924.6506001969, "area": 2264.912382769},
    "model_22344_51f483c9_0005": {"func": model_22344_51f483c9_0005, "volume": 4.046490116, "area": 30.2413927478},
    "model_22357_e2f7b060_0002": {"func": model_22357_e2f7b060_0002, "volume": 0.0289569763, "area": 1.2139152401},
    "model_22433_9f17ac4c_0004": {"func": model_22433_9f17ac4c_0004, "volume": 1.5983098101, "area": 14.6992535071},
    "model_22447_4062c6cb_0000": {"func": model_22447_4062c6cb_0000, "volume": 9.9949770274, "area": 37.1807490552},
    "model_22447_4062c6cb_0008": {"func": model_22447_4062c6cb_0008, "volume": 6.9579155711, "area": 40.8775918367},
    "model_22447_4062c6cb_0011": {"func": model_22447_4062c6cb_0011, "volume": 0.7775909538, "area": 6.5925693517},
    "model_22457_a6c2776f_0001": {"func": model_22457_a6c2776f_0001, "volume": 14.5058032264, "area": 55.4707963091},
    "model_22457_a6c2776f_0002": {"func": model_22457_a6c2776f_0002, "volume": 14.4819407264, "area": 55.0781617494},
    "model_22463_c48bb23e_0004": {"func": model_22463_c48bb23e_0004, "volume": 0.5237535629, "area": 3.5969350928},
    "model_22492_047b125b_0004": {"func": model_22492_047b125b_0004, "volume": 46.3649751206, "area": 108.6618078409},
    "model_22535_0ba01cc9_0007": {"func": model_22535_0ba01cc9_0007, "volume": 1.0725308308, "area": 6.679974791},
    "model_22604_7063d5c9_0007": {"func": model_22604_7063d5c9_0007, "volume": 0.0926769833, "area": 1.8221237391},
    "model_22612_28fe0ac2_0000": {"func": model_22612_28fe0ac2_0000, "volume": 19.5493456851, "area": 61.9679150921},
    "model_22624_7af10d7d_0006": {"func": model_22624_7af10d7d_0006, "volume": 1.7718582566, "area": 14.1999987942},
    "model_22666_bdaa1303_0002": {"func": model_22666_bdaa1303_0002, "volume": 1.1310864408, "area": 9.4734131634},
    "model_22711_33843a5d_0002": {"func": model_22711_33843a5d_0002, "volume": 331.1822341868, "area": 516.6305989696},
    "model_22734_f6bad9f7_0013": {"func": model_22734_f6bad9f7_0013, "volume": 4.4206080942, "area": 24.2320184191},
    "model_22734_f6bad9f7_0029": {"func": model_22734_f6bad9f7_0029, "volume": 0.9967591949, "area": 10.7757299951},
    "model_22734_f6bad9f7_0032": {"func": model_22734_f6bad9f7_0032, "volume": 0.9016398012, "area": 14.2194786322},
    "model_22742_3c107495_0008": {"func": model_22742_3c107495_0008, "volume": 38.1277115163, "area": 150.1692620651},
    "model_22742_3c107495_0009": {"func": model_22742_3c107495_0009, "volume": 25.7432274135, "area": 121.8335476509},
    "model_22772_2b5f6629_0000": {"func": model_22772_2b5f6629_0000, "volume": 2.869677791, "area": 21.4297306838},
    "model_22776_facf9bcf_0000": {"func": model_22776_facf9bcf_0000, "volume": 38.9007877425, "area": 105.7917814993},
    "model_22822_b5d896dd_0003": {"func": model_22822_b5d896dd_0003, "volume": 1.4591857895, "area": 11.3687032946},
    "model_22848_cc91b848_0017": {"func": model_22848_cc91b848_0017, "volume": 89.1032625425, "area": 150.837538709},
    "model_23008_3d1bb7b2_0000": {"func": model_23008_3d1bb7b2_0000, "volume": 86, "area": 231},
    "model_23138_630f02f9_0005": {"func": model_23138_630f02f9_0005, "volume": 439.8892591076, "area": 513.6466289507},
    "model_23144_88ca00a5_0005": {"func": model_23144_88ca00a5_0005, "volume": 4925.312342904, "area": 6156.374784},
    "model_23144_88ca00a5_0006": {"func": model_23144_88ca00a5_0006, "volume": 31663.7374723308, "area": 25497.0326148224},
    "model_23144_88ca00a5_0011": {"func": model_23144_88ca00a5_0011, "volume": 73.2086091104, "area": 626.9187500734},
    "model_23162_7e2f3d77_0001": {"func": model_23162_7e2f3d77_0001, "volume": 1.0581779927, "area": 8.9082518078},
    "model_23206_b99a5251_0015": {"func": model_23206_b99a5251_0015, "volume": 27.9424364485, "area": 85.2008192487},
    "model_23206_b99a5251_0048": {"func": model_23206_b99a5251_0048, "volume": 2.6073009183, "area": 14.2146018366},
    "model_23231_efe613bb_0018": {"func": model_23231_efe613bb_0018, "volume": 3.9681209856, "area": 22.7578471767},
    "model_23393_d47067ad_0005": {"func": model_23393_d47067ad_0005, "volume": 147.5663706144, "area": 728.8362787842},
    "model_23393_d47067ad_0007": {"func": model_23393_d47067ad_0007, "volume": 104.8810853546, "area": 181.1327412287},
    "model_23393_d47067ad_0014": {"func": model_23393_d47067ad_0014, "volume": 315.3373626041, "area": 362.8539514896},
    "model_23472_ed1faab6_0007": {"func": model_23472_ed1faab6_0007, "volume": 0.0725578087, "area": 1.3676864826},
    "model_23472_ed1faab6_0009": {"func": model_23472_ed1faab6_0009, "volume": 0.6553327405, "area": 5.8031698611},
    "model_23493_57512264_0003": {"func": model_23493_57512264_0003, "volume": 0.2583959958, "area": 3.0787608005},
    "model_23552_10239b96_0001": {"func": model_23552_10239b96_0001, "volume": 0.1488207963, "area": 2.5719911184},
    "model_23554_a0845d54_0013": {"func": model_23554_a0845d54_0013, "volume": 71.4987218049, "area": 137.9944573089},
    "model_23602_5daaccf5_0002": {"func": model_23602_5daaccf5_0002, "volume": 82.3378532974, "area": 197.8699276939},
    "model_23631_d2b74fdc_0000": {"func": model_23631_d2b74fdc_0000, "volume": 78.5512443962, "area": 313.1811110255},
    "model_23667_fc4a5d41_0000": {"func": model_23667_fc4a5d41_0000, "volume": 43.5972345251, "area": 248.4600689526},
    "model_23686_cba4f679_0007": {"func": model_23686_cba4f679_0007, "volume": 0.8175994881, "area": 6.5188047562},
    "model_23699_90c77de4_0000": {"func": model_23699_90c77de4_0000, "volume": 505.9018619171, "area": 522.3612998783},
    "model_23790_2abde9b6_0007": {"func": model_23790_2abde9b6_0007, "volume": 0.2011814358, "area": 2.4855007708},
    "model_23876_74957d38_0002": {"func": model_23876_74957d38_0002, "volume": 305.034130301, "area": 409.7189140279},
    "model_23876_74957d38_0005": {"func": model_23876_74957d38_0005, "volume": 442.3396769513, "area": 500.6807551676},
    "model_23910_316134bd_0008": {"func": model_23910_316134bd_0008, "volume": 0.6913467434, "area": 8.8749993307},
    "model_23951_3afdbe1c_0002": {"func": model_23951_3afdbe1c_0002, "volume": 130.812018703, "area": 1727.3453503399},
    "model_23956_ee17fe48_0000": {"func": model_23956_ee17fe48_0000, "volume": 6915.9435194138, "area": 3378.9932559261},
    "model_23957_99511a89_0000": {"func": model_23957_99511a89_0000, "volume": 122.5, "area": 294},
    "model_24032_d6172503_0026": {"func": model_24032_d6172503_0026, "volume": 450.7423981764, "area": 1890.3997275483},
    "model_24036_1b426643_0000": {"func": model_24036_1b426643_0000, "volume": 44.2463706144, "area": 125.6548631591},
    "model_24086_a8e5514c_0003": {"func": model_24086_a8e5514c_0003, "volume": 0.3040361177, "area": 6.6625908089},
    "model_24133_2ac9dc04_0002": {"func": model_24133_2ac9dc04_0002, "volume": 74.2040608993, "area": 180.2144241449},
    "model_24133_2ac9dc04_0004": {"func": model_24133_2ac9dc04_0004, "volume": 32.4447458983, "area": 114.4639373769},
    "model_24157_49bf3a04_0009": {"func": model_24157_49bf3a04_0009, "volume": 0.0219911486, "area": 0.7539822369},
    "model_24157_49bf3a04_0013": {"func": model_24157_49bf3a04_0013, "volume": 0.9801769079, "area": 16.3362817987},
    "model_24284_3710e946_0005": {"func": model_24284_3710e946_0005, "volume": 2.7816020616, "area": 16.6386733777},
    "model_24291_a6aa039b_0000": {"func": model_24291_a6aa039b_0000, "volume": 296.1961831417, "area": 443.2905021193},
    "model_24302_2bcddd22_0000": {"func": model_24302_2bcddd22_0000, "volume": 2.5843538218, "area": 14.8451326996},
    "model_24308_89c2be2b_0007": {"func": model_24308_89c2be2b_0007, "volume": 44.4988993595, "area": 160.5700712937},
    "model_24372_03b260fe_0002": {"func": model_24372_03b260fe_0002, "volume": 7311.5012419221, "area": 3891.8753104805},
    "model_24372_03b260fe_0022": {"func": model_24372_03b260fe_0022, "volume": 163.8, "area": 283.8},
    "model_24422_ed84404a_0000": {"func": model_24422_ed84404a_0000, "volume": 8271.928583942, "area": 10316.6377895236},
    "model_24443_996411f9_0003": {"func": model_24443_996411f9_0003, "volume": 1.7979614305, "area": 12.9418024924},
    "model_24476_568e9ca0_0031": {"func": model_24476_568e9ca0_0031, "volume": 0.7537986733, "area": 7.4323141402},
    "model_24603_a4021250_0006": {"func": model_24603_a4021250_0006, "volume": 8.1666051323, "area": 64.2779628346},
    "model_24660_cadd37c3_0000": {"func": model_24660_cadd37c3_0000, "volume": 3.4184945936, "area": 14.3884943534},
    "model_24720_19eea793_0000": {"func": model_24720_19eea793_0000, "volume": 473.7521721613, "area": 747.9503789667},
    "model_24725_73d5dcf0_0000": {"func": model_24725_73d5dcf0_0000, "volume": 1176.5096199159, "area": 1007.6370248949},
    "model_24861_c05860c8_0001": {"func": model_24861_c05860c8_0001, "volume": 0.6929728612, "area": 7.406564695},
    "model_24861_c05860c8_0003": {"func": model_24861_c05860c8_0003, "volume": 1.749867108, "area": 11.502156103},
    "model_24869_5c729cf1_0004": {"func": model_24869_5c729cf1_0004, "volume": 1.7773070349, "area": 36.6435367115},
    "model_24927_543d2801_0000": {"func": model_24927_543d2801_0000, "volume": 196.1909587262, "area": 473.0953275243},
    "model_25132_c8588afc_0004": {"func": model_25132_c8588afc_0004, "volume": 7.2665038078, "area": 32.185616736},
    "model_25134_ec81c644_0000": {"func": model_25134_ec81c644_0000, "volume": 8.1605543149, "area": 45.3443253294},
    "model_25139_f79f51e3_0000": {"func": model_25139_f79f51e3_0000, "volume": 48.4604653152, "area": 125.4216033754},
    "model_25186_e5476b73_0003": {"func": model_25186_e5476b73_0003, "volume": 0.1918807189, "area": 2.5112047924},
    "model_25186_e5476b73_0004": {"func": model_25186_e5476b73_0004, "volume": 0.7744025891, "area": 5.3564154744},
    "model_25199_d7aff7a5_0012": {"func": model_25199_d7aff7a5_0012, "volume": 0.2190446902, "area": 3.6909841738},
    "model_25203_1cc0cb3c_0007": {"func": model_25203_1cc0cb3c_0007, "volume": 2.7996570826, "area": 28.9984955592},
    "model_25203_1cc0cb3c_0010": {"func": model_25203_1cc0cb3c_0010, "volume": 0.1850633692, "area": 3.4156966126},
    "model_25203_1cc0cb3c_0011": {"func": model_25203_1cc0cb3c_0011, "volume": 0.4499828821, "area": 7.9256099465},
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
