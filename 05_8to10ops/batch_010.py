"""Batch 010 - passing/05_8to10ops
70 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_62281_fbc75133_0000():
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

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.4017831179, perimeter: 11.6011887453
            with BuildLine():
                Line((-3.5, 4.1994056274), (-3.5, 7))
                Line((-0.5, 4.1994056274), (-3.5, 4.1994056274))
                Line((-0.5, 7), (-0.5, 4.1994056274))
                Line((-3.5, 7), (-0.5, 7))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((-3.5, 3.5375260802), (-1, 3.5375260802))
                Line((-3.5, 0.5375260802), (-3.5, 3.5375260802))
                Line((-1, 0.5375260802), (-3.5, 0.5375260802))
                Line((-1, 3.5375260802), (-1, 0.5375260802))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


def model_63132_330141d7_0010():
    """Model: Right Motor 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3986122047, perimeter: 4.4401224361
            with BuildLine():
                Line((24.4916017533, 5.5513902636), (24.4916017533, 4.4486097364))
                CenterArc((25, 5), 0.75, -132.6769787467, 85.3539574934)
                Line((25.5083982467, 5.5513902636), (25.5083982467, 4.4486097364))
                CenterArc((25, 5), 0.75, 47.3230212533, 85.3539574934)
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((25, 5)):
                Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-25, 5)):
                Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-25, 5)):
                Circle(0.05)
        # OneSide extrude, distance=0.09
        extrude(amount=0.09, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((25, 5)):
                Circle(0.05)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


def model_65211_73eab9de_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 68, perimeter: 36
            with BuildLine():
                Line((-2, 6), (-2, 4))
                Line((-2, 4), (-3, 4))
                Line((-3, -6), (-3, 4))
                Line((3, -6), (-3, -6))
                Line((3, 4), (3, -6))
                Line((2, 4), (3, 4))
                Line((2, 6), (2, 4))
                Line((-2, 6), (2, 6))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0, 1.5)):
                Circle(0.4)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.5, 5)):
                Circle(0.15)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.5, 5)):
                Circle(0.15)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_65532_72eb1a5e_0004():
    """Model: H1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.4720688936, perimeter: 6.9361659329
            with BuildLine():
                Line((0.579999987, -0.9999999776), (1.1560253779, 0.0022947341))
                Line((1.1560253779, 0.0022947341), (0.5760253909, 1.0022947118))
                Line((0.5760253909, 1.0022947118), (-0.579999987, 0.9999999776))
                Line((-0.579999987, 0.9999999776), (-1.1560253779, -0.0022947341))
                Line((-1.1560253779, -0.0022947341), (-0.5760253909, -1.0022947118))
                Line((-0.5760253909, -1.0022947118), (0.579999987, -0.9999999776))
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 0.7000000104)):
                Circle(0.25)
        # OneSide extrude, distance=-6.4
        extrude(amount=-6.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((0, 0.7000000104), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.7000000104), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.9988665002, perimeter: 13.0622716074
            with BuildLine():
                Line((-1.1560253779, -0.0022947341), (-0.5760253909, -1.0022947118))
                Line((-0.5760253909, -1.0022947118), (0.579999987, -0.9999999776))
                Line((0.579999987, -0.9999999776), (1.1560253779, 0.0022947341))
                Line((1.1560253779, 0.0022947341), (0.5760253909, 1.0022947118))
                Line((0.5760253909, 1.0022947118), (-0.579999987, 0.9999999776))
                Line((-0.579999987, 0.9999999776), (-1.1560253779, -0.0022947341))
            make_face()
            with BuildLine():
                CenterArc((0, 0.7000000104), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.6062177917, 0.3500000052), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.6062177917, -0.3500000052), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.7000000104), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6062177917, -0.3500000052), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6062177917, 0.3500000052), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-0.6062177917, -0.3500000052)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0, -0.7000000104)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.6062177917, -0.3500000052)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.6062177917, 0.3500000052)):
                Circle(0.125)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


def model_65813_123f1f95_0000():
    """Model: Untitled-1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.3635113683, perimeter: 30.7333736157
            with BuildLine():
                CenterArc((-12.91648223, -5.8378479263), 4.8095651144, 59.6428418921, 56.0458233856)
                Line((-15.0013364483, -1.5036467913), (-15.0013364483, -5.0262033637))
                CenterArc((-14.3513364483, -5.0262033637), 0.65, 180, 124.4430767159)
                CenterArc((-13.3897486655, -6.6621218574), 1.25, 15.2116837316, 103.158402671)
                Line((-11.6590958304, -8.2628781203), (-12.1835449043, -6.3341394087))
                Line((-10.4857824001, -8.2628781203), (-11.6590958304, -8.2628781203))
                Line((-10.4857824001, -1.6877135999), (-10.4857824001, -8.2628781203))
            make_face()
            with BuildLine():
                Line((-12.0042378221, -4.9006233516), (-12.0042378221, -1.7523233516))
                Line((-13.4042378221, -4.9006233516), (-12.0042378221, -4.9006233516))
                Line((-13.4042378221, -1.7523233516), (-13.4042378221, -4.9006233516))
                Line((-12.0042378221, -1.7523233516), (-13.4042378221, -1.7523233516))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-15.0013364483, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.7886599839, perimeter: 6.4240872899
            with BuildLine():
                Line((1.2168389895, -4.4952046554), (0.5, -4.4952046554))
                Line((1.2168389895, -2), (1.2168389895, -4.4952046554))
                Line((0.5, -2), (1.2168389895, -2))
                Line((0.5, -4.4952046554), (0.5, -2))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-12.9485099431, -3.5208678126, 0), x_dir=(0, 0, 1), z_dir=(-0.9649630089, -0.262385959, 0))):
            # Profile area: 0.6407933653, perimeter: 3.2308381802
            with BuildLine():
                Line((1.2000000179, -2.9154191095), (0.5000000075, -2.9154191095))
                Line((1.2000000179, -2.0000000298), (1.2000000179, -2.9154191095))
                Line((0.5000000075, -2.0000000298), (1.2000000179, -2.0000000298))
                Line((0.5000000075, -2.9154191095), (0.5000000075, -2.0000000298))
            make_face()
            # Profile area: 0.8992066806, perimeter: 3.9691619271
            with BuildLine():
                Line((0.5000000075, -4.2000000626), (0.5000000075, -2.9154191095))
                Line((1.2000000179, -4.2000000626), (0.5000000075, -4.2000000626))
                Line((1.2000000179, -2.9154191095), (1.2000000179, -4.2000000626))
                Line((1.2000000179, -2.9154191095), (0.5000000075, -2.9154191095))
            make_face()
        # OneSide extrude, distance=-6.9
        extrude(amount=-6.9, mode=Mode.SUBTRACT)
    return part.part


def model_65827_d1469ad6_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1273939329, perimeter: 8.0542828023
            with BuildLine():
                Line((5.9952550935, 2.9681136924), (2, 2.9681136924))
                Line((5.9952550935, 3), (5.9952550935, 2.9681136924))
                Line((2, 3), (5.9952550935, 3))
                Line((2, 2.9681136924), (2, 3))
            make_face()
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.520000093, perimeter: 5.6000001013
            with BuildLine():
                Line((-2.2000000328, 0.200000003), (-2.2000000328, 2.8000000417))
                Line((-2, 0.200000003), (-2.2000000328, 0.200000003))
                Line((-2, 0.200000003), (-2, 2.8000000417))
                Line((-2.2000000328, 2.8000000417), (-2, 2.8000000417))
            make_face()
            # Profile area: 0.7990510306, perimeter: 8.390510193
            with BuildLine():
                Line((-5.8000000864, 0.200000003), (-2.2000000328, 0.200000003))
                Line((-5.9952550935, 0.200000003), (-5.8000000864, 0.200000003))
                Line((-5.9952550935, 0), (-5.9952550935, 0.200000003))
                Line((-2, 0), (-5.9952550935, 0))
                Line((-2, 0), (-2, 0.200000003))
                Line((-2, 0.200000003), (-2.2000000328, 0.200000003))
            make_face()
            # Profile area: 0.507663026, perimeter: 5.5905100917
            with BuildLine():
                Line((-5.8000000864, 2.8000000417), (-5.9952550935, 2.8000000417))
                Line((-5.9952550935, 2.8000000417), (-5.9952550935, 0.200000003))
                Line((-5.9952550935, 0.200000003), (-5.8000000864, 0.200000003))
                Line((-5.8000000864, 0.200000003), (-5.8000000864, 2.8000000417))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5400000161, perimeter: 5.8000000864
            with BuildLine():
                Line((-5.4000000805, 0), (-5.4000000805, 0.200000003))
                Line((-2.7000000402, 0), (-5.4000000805, 0))
                Line((-2.7000000402, 0.200000003), (-2.7000000402, 0))
                Line((-5.4000000805, 0.200000003), (-2.7000000402, 0.200000003))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.200000003), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.1000000611, 4.2000000626)):
                Circle(0.2)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


def model_66226_49fc804a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0174922225, perimeter: 0.9197488607
            with BuildLine():
                Line((0, 0), (0, -0.400000006))
                CenterArc((0.6000000089, -0.400000006), 0.6000000089, 146.4426902381, 33.5573097619)
                Line((0.1000000015, 0), (0.1000000015, -0.068337522))
                Line((0, 0), (0.1000000015, 0))
            make_face()
            # Profile area: 0.0225077787, perimeter: 0.7830738168
            with BuildLine():
                Line((0, -0.400000006), (0.1000000015, -0.400000006))
                Line((0.1000000015, -0.068337522), (0.1000000015, -0.400000006))
                CenterArc((0.6000000089, -0.400000006), 0.6000000089, 146.4426902381, 33.5573097619)
            make_face()
            # Profile area: 0.1727876011, perimeter: 3.6557519734
            with BuildLine():
                CenterArc((0.6000000089, -0.400000006), 0.6000000089, -180, 180)
                Line((1.1000000164, -0.400000006), (1.2000000179, -0.400000006))
                CenterArc((0.6000000089, -0.400000006), 0.5000000075, -180, 180)
                Line((0, -0.400000006), (0.1000000015, -0.400000006))
            make_face()
            # Profile area: 0.0225077787, perimeter: 0.7830738168
            with BuildLine():
                Line((1.1000000164, -0.400000006), (1.1000000164, -0.068337522))
                Line((1.1000000164, -0.400000006), (1.2000000179, -0.400000006))
                CenterArc((0.6000000089, -0.400000006), 0.6000000089, 0, 33.5573097619)
            make_face()
            # Profile area: 0.0174922225, perimeter: 0.9197488607
            with BuildLine():
                CenterArc((0.6000000089, -0.400000006), 0.6000000089, 0, 33.5573097619)
                Line((1.2000000179, -0.400000006), (1.2000000179, 0))
                Line((1.1000000164, 0), (1.2000000179, 0))
                Line((1.1000000164, -0.068337522), (1.1000000164, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_66331_6ff90f6b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 300398, perimeter: 2202
            with BuildLine():
                Line((-500, 600), (-1, 600))
                Line((-500, -2), (-500, 600))
                Line((-1, -2), (-500, -2))
                Line((-1, 600), (-1, -2))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7479.697495167, perimeter: 1027.2929993556
            with BuildLine():
                Line((500, 2), (1.3535003222, 2))
                Line((500, 17), (500, 2))
                Line((1.3535003222, 17), (500, 17))
                Line((1.3535003222, 2), (1.3535003222, 17))
            make_face()
        # OneSide extrude, distance=350
        extrude(amount=350)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9270.0016362177, perimeter: 1266.0002181624
            with BuildLine():
                Line((-65, 18.0001090812), (-50, 18.0001090812))
                Line((-65, -600), (-65, 18.0001090812))
                Line((-50, -600), (-65, -600))
                Line((-50, 18.0001090812), (-50, -600))
            make_face()
        # OneSide extrude, distance=350
        extrude(amount=350)
    return part.part


def model_66762_5098cf7d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0159406196, perimeter: 5.0331955021
            Circle(0.8010579437)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_67207_15bfd1aa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)
    return part.part


def model_67262_f7710fc0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.1415926536, perimeter: 12.2831853072
            with BuildLine():
                CenterArc((-1.5, 0), 1, 90, 180)
                Line((-1.5, -1), (1.5, -1))
                CenterArc((1.5, 0), 1, -90, 180)
                Line((1.5, 1), (-1.5, 1))
            make_face()
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-1.5, 0)):
                Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.25), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981306, perimeter: 3.1415925881
            with Locations((-1.5, 0)):
                Circle(0.4999999896)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.5707963268, perimeter: 28.5663706144
            with BuildLine():
                CenterArc((9.2371527559, -0.4862999036), 1, 90, 180)
                Line((9.2371527559, -1.4862999036), (17.2371527559, -1.4862999036))
                CenterArc((17.2371527559, -0.4862999036), 1, -90, 180)
                Line((17.2371527559, 0.5137000964), (9.2371527559, 0.5137000964))
            make_face()
            with BuildLine():
                CenterArc((9.2371527559, -0.4862999036), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((17.2371527559, -0.4862999036), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 46.4292036732, perimeter: 38.2831853072
            with BuildLine():
                Line((-17, 4), (-17, 0))
                Line((-17, 0), (-5, 0))
                Line((-5, 0), (-5, 4))
                Line((-5, 4), (-17, 4))
            make_face()
            with BuildLine():
                CenterArc((-15, 2), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.0001964281, 1.9439392199), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.5
        extrude(amount=0.75, both=True)
    return part.part


def model_67378_1f022261_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            Circle(7.5)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8.0436121947, perimeter: 19.3190046427
            with BuildLine():
                CenterArc((0, 0), 7.5, 78.4630409672, 23.0739180656)
                Line((1.5, 10), (1.5, 7.3484692283))
                CenterArc((0, 10), 1.5, 0, 180)
                Line((-1.5, 10), (-1.5, 7.3484692283))
            make_face()
            with BuildLine():
                CenterArc((0, 10), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 41 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.2719790666, perimeter: 16.1623547618
            with BuildLine():
                CenterArc((3.6619414394, 3.9816199521), 0.35, 0, 180)
                Line((3.3119414394, 3.9816199521), (3.3119414394, -3))
                CenterArc((3.6619414394, -3), 0.35, 180, 180)
                Line((4.0119414394, -3), (4.0119414394, 3.9816199521))
            make_face()
            # Profile area: 5.2719790666, perimeter: 16.1623547618
            with BuildLine():
                CenterArc((2.6619414394, 3.9816199521), 0.35, 0, 180)
                Line((2.3119414394, 3.9816199521), (2.3119414394, -3))
                CenterArc((2.6619414394, -3), 0.35, 180, 180)
                Line((3.0119414394, -3), (3.0119414394, 3.9816199521))
            make_face()
            # Profile area: 3.8311366602, perimeter: 16.5645227667
            with BuildLine():
                CenterArc((1.6619414394, -3), 0.35, 180, 180)
                Line((2.0119414394, -3), (2.0119414394, 3.9816199521))
                CenterArc((1.6619414394, 3.9816199521), 0.35, 0, 180)
                Line((1.3119414394, 3.9816199521), (1.3119414394, 1.5095726745))
                CenterArc((0, 0), 2, -49.0067038914, 98.0134077828)
                Line((1.3119414394, -1.5095726745), (1.3119414394, -3))
            make_face()
            # Profile area: 0.9799018471, perimeter: 4.146726515
            with BuildLine():
                CenterArc((0, 0), 2, -81.0269008567, 21.4227129805)
                Line((0.3119414394, -1.9755233581), (0.3119414394, -3))
                CenterArc((0.6619414394, -3), 0.35, 180, 180)
                Line((1.0119414394, -3), (1.0119414394, -1.7251013081))
            make_face()
            # Profile area: 5.268502389, perimeter: 16.1632254911
            with BuildLine():
                CenterArc((0, 0), 2, 173.7357757384, 12.5284485231)
                Line((-1.9880585606, 0.2182273122), (-1.9880585606, 3.9816199521))
                CenterArc((-2.3380585606, 3.9816199521), 0.35, 0, 180)
                Line((-2.6880585606, 3.9816199521), (-2.6880585606, -3))
                CenterArc((-2.3380585606, -3), 0.35, 180, 180)
                Line((-1.9880585606, -3), (-1.9880585606, -0.2182273122))
            make_face()
            # Profile area: 1.6670358136, perimeter: 6.1099664193
            with BuildLine():
                CenterArc((0, 0), 2, 59.6041878762, 21.4227129805)
                Line((1.0119414394, 1.7251013081), (1.0119414394, 3.9816199521))
                CenterArc((0.6619414394, 3.9816199521), 0.35, 0, 180)
                Line((0.3119414394, 3.9816199521), (0.3119414394, 1.9755233581))
            make_face()
            # Profile area: 1.6072055293, perimeter: 5.8992661793
            with BuildLine():
                CenterArc((0, 0), 2, 89.6579009266, 20.4646497661)
                Line((0.0119414394, 1.9999643502), (0.0119414394, 3.9816199521))
                CenterArc((-0.3380585606, 3.9816199521), 0.35, 0, 180)
                Line((-0.6880585606, 3.9816199521), (-0.6880585606, 1.8779178409))
            make_face()
            # Profile area: 0.9200715628, perimeter: 3.936026275
            with BuildLine():
                CenterArc((0, 0), 2, -110.1225506927, 20.4646497661)
                Line((-0.6880585606, -1.8779178409), (-0.6880585606, -3))
                CenterArc((-0.3380585606, -3), 0.35, 180, 180)
                Line((0.0119414394, -3), (0.0119414394, -1.9999643502))
            make_face()
            # Profile area: 1.2701153972, perimeter: 5.2641417959
            with BuildLine():
                CenterArc((0, 0), 2, -147.5680799753, 27.9623196442)
                Line((-1.6880585606, -1.0725941899), (-1.6880585606, -3))
                CenterArc((-1.3380585606, -3), 0.35, 180, 180)
                Line((-0.9880585606, -3), (-0.9880585606, -1.7388905316))
            make_face()
            # Profile area: 1.9572493637, perimeter: 7.2273817001
            with BuildLine():
                CenterArc((0, 0), 2, 119.6057603311, 27.9623196442)
                Line((-0.9880585606, 1.7388905316), (-0.9880585606, 3.9816199521))
                CenterArc((-1.3380585606, 3.9816199521), 0.35, 0, 180)
                Line((-1.6880585606, 3.9816199521), (-1.6880585606, 1.0725941899))
            make_face()
            # Profile area: 5.2719790666, perimeter: 16.1623547618
            with BuildLine():
                CenterArc((-3.3380585606, 3.9816199521), 0.35, 0, 180)
                Line((-3.6880585606, 3.9816199521), (-3.6880585606, -3))
                CenterArc((-3.3380585606, -3), 0.35, 180, 180)
                Line((-2.9880585606, -3), (-2.9880585606, 3.9816199521))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_67567_e5be20ab_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 102.3578449418, perimeter: 119.9711674313
            with BuildLine():
                CenterArc((0, 0), 9.5, 39.1667107161, 281.6665785678)
                Line((7.3654599313, 6), (10, 6))
                Line((10, 6), (10, 10))
                Line((10, 10), (-10, 10))
                Line((-10, 10), (-10, -10))
                Line((-10, -10), (10, -10))
                Line((10, -10), (10, -6))
                Line((10, -6), (7.3654599313, -6))
            make_face()
            # Profile area: 14.1134180717, perimeter: 30.2572532616
            with BuildLine():
                CenterArc((0, 0), 9.5, -39.1667107161, 78.3334214322)
                Line((10, -6), (7.3654599313, -6))
                Line((10, -6), (10, 6))
                Line((7.3654599313, 6), (10, 6))
            make_face()
            # Profile area: 261.6421550582, perimeter: 59.4330071566
            with BuildLine():
                CenterArc((0, 0), 9.5, 39.1667107161, 281.6665785678)
                Line((7.3654599313, -6), (7, -6))
                Line((7, -6), (7, 6))
                Line((7, 6), (7.3654599313, 6))
            make_face()
            # Profile area: 21.8865819283, perimeter: 25.7190929869
            with BuildLine():
                Line((7, 6), (7.3654599313, 6))
                Line((7, -6), (7, 6))
                Line((7.3654599313, -6), (7, -6))
                CenterArc((0, 0), 9.5, -39.1667107161, 78.3334214322)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 261.6421550582, perimeter: 59.4330071566
            with BuildLine():
                CenterArc((0, 0), 9.5, 39.1667107161, 281.6665785678)
                Line((7.3654599313, -6), (7, -6))
                Line((7, -6), (7, 6))
                Line((7, 6), (7.3654599313, 6))
            make_face()
            # Profile area: 21.8865819283, perimeter: 25.7190929869
            with BuildLine():
                Line((7, 6), (7.3654599313, 6))
                Line((7, -6), (7, 6))
                Line((7.3654599313, -6), (7, -6))
                CenterArc((0, 0), 9.5, -39.1667107161, 78.3334214322)
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1134180717, perimeter: 30.2572532616
            with BuildLine():
                CenterArc((0, 0), 9.5, -39.1667107161, 78.3334214322)
                Line((10, -6), (7.3654599313, -6))
                Line((10, -6), (10, 6))
                Line((7.3654599313, 6), (10, 6))
            make_face()
            # Profile area: 36, perimeter: 30
            with BuildLine():
                Line((10, -6), (10, 6))
                Line((13, -6), (10, -6))
                Line((13, 6), (13, -6))
                Line((10, 6), (13, 6))
            make_face()
            # Profile area: 21.8865819283, perimeter: 25.7190929869
            with BuildLine():
                Line((7, 6), (7.3654599313, 6))
                Line((7, -6), (7, 6))
                Line((7.3654599313, -6), (7, -6))
                CenterArc((0, 0), 9.5, -39.1667107161, 78.3334214322)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 213.824649985, perimeter: 51.8362787842
            Circle(8.25)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 18, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=-25
        extrude(amount=-25, mode=Mode.SUBTRACT)
    return part.part


def model_67572_05561813_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch23 -> Extrude12 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.7457559291, perimeter: 12.1245977993
            with Locations((8.3301107301, -9.9109040011)):
                Ellipse(2.6317126166, 1.0578132874, rotation=90)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_68939_82bcae5a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10, perimeter: 22
            with BuildLine():
                Line((-1.5, -7), (-2.5, -7))
                Line((-1.5, 3), (-1.5, -7))
                Line((-2.5, 3), (-1.5, 3))
                Line((-2.5, -7), (-2.5, 3))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 66, perimeter: 34
            with BuildLine():
                Line((-9.5, 3), (1.5, 3))
                Line((-9.5, -3), (-9.5, 3))
                Line((1.5, -3), (-9.5, -3))
                Line((1.5, 3), (1.5, -3))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12, perimeter: 14
            with BuildLine():
                Line((-1.5, -3), (-1.5, -7))
                Line((-1.5, -7), (1.5, -7))
                Line((1.5, -7), (1.5, -3))
                Line((1.5, -3), (-1.5, -3))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12, perimeter: 14
            with BuildLine():
                Line((-1.5, 7), (1.5, 7))
                Line((-1.5, 3), (-1.5, 7))
                Line((1.5, 3), (-1.5, 3))
                Line((1.5, 7), (1.5, 3))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_69255_6e76c12f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8036528696, perimeter: 23.0599666982
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6701076875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch7 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((-2, -0.5), (-2, 0))
                Line((-2, 0), (-5, 0))
                Line((-5, 0), (-5, -0.5))
                Line((-5, -0.5), (-2, -0.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_69454_807423c7_0000():
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
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 33, perimeter: 28
            with BuildLine():
                Line((5, 0), (-6, 0))
                Line((5, 3), (5, 0))
                Line((-6, 3), (5, 3))
                Line((-6, 0), (-6, 3))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-5.8000000864, 2.8000000417)):
                Circle(0.05)
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 1)):
                Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-5.4000000805, 0.200000003)):
                Circle(0.1)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.11508925, perimeter: 7.0388607304
            with BuildLine():
                _nurbs_edge([(1.5000000224, 1.5000000224), (1.5622255424, 1.4915555232), (1.6828817114, 1.4790780866), (1.8524813053, 1.473596674), (2.0557857558, 1.4928262024), (2.2725805416, 1.5598763349), (2.4547963101, 1.6655618565), (2.6084235178, 1.800564612), (2.7439692144, 1.9487247075), (2.877624878, 2.0852706285), (3.0256926442, 2.1830897794), (3.1992316229, 2.2187426255), (3.3984614858, 2.1787079914), (3.6074682746, 2.0653745872), (3.8009119679, 1.8922253004), (3.9505099141, 1.6793284287), (4.0312352873, 1.4489876727), (4.028421172, 1.2210059601), (3.9422857924, 1.009277736), (3.7826693228, 0.8233885089), (3.5653138473, 0.6694004561), (3.3078732099, 0.5508758523), (3.0255617927, 0.4698270111), (2.7288245548, 0.4274110746), (2.4247149914, 0.4240839823), (2.1173952132, 0.4598598967), (1.8706480859, 0.519575756), (1.6853974976, 0.5817269062), (1.5618131837, 0.6308582857), (1.5000000224, 0.6573483003)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((1.5000000224, 0.6573483003), (1.5000000224, 1.5000000224))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


def model_69800_f99575cb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((0, -2.5), (0, -1.5))
                Line((6, -2.5), (0, -2.5))
                Line((6, -1.5), (6, -2.5))
                Line((0, -1.5), (6, -1.5))
            make_face()
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24, perimeter: 20
            with BuildLine():
                Line((6, -4), (0, -4))
                Line((6, 0), (6, -4))
                Line((0, 0), (6, 0))
                Line((0, -4), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((0, -2.5), (0, -1.5))
                Line((6, -2.5), (0, -2.5))
                Line((6, -1.5), (6, -2.5))
                Line((0, -1.5), (6, -1.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2701155065, perimeter: 5.3410778681
            with Locations((-3, 3)):
                Circle(0.8500589441)
            # Profile area: 1.1936942854, perimeter: 3.8730356041
            with Locations((-1.0743832675, 0.75)):
                Circle(0.6164127612)
            # Profile area: 0.5736584189, perimeter: 2.6849216558
            with Locations((-4.9946013889, 0.75)):
                Circle(0.4273185533)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6650440156, perimeter: 4.5742278243
            with Locations((-3, 3)):
                Circle(0.7280109691)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0400000104, perimeter: 0.8000001043
            with BuildLine():
                Line((-3.2000000477, 0.3000000045), (-3, 0.3000000045))
                Line((-3.2000000477, 0.1), (-3.2000000477, 0.3000000045))
                Line((-3, 0.1), (-3.2000000477, 0.1))
                Line((-3, 0.3000000045), (-3, 0.1))
            make_face()
            # Profile area: 0.3000887772, perimeter: 3.4008877135
            with BuildLine():
                Line((-0.3000000045, 3.4000000507), (-0.1, 3.4000000507))
                Line((-0.3000000045, 1.8995561984), (-0.3000000045, 3.4000000507))
                Line((-0.1, 1.8995561984), (-0.3000000045, 1.8995561984))
                Line((-0.1, 3.4000000507), (-0.1, 1.8995561984))
            make_face()
            # Profile area: 0.2336538346, perimeter: 3.2230701439
            with BuildLine():
                Line((-5.7389087297, 1.8995561984), (-5.9, 1.8995561984))
                Line((-5.7389087297, 3.35), (-5.7389087297, 1.8995561984))
                Line((-5.9, 3.35), (-5.7389087297, 3.35))
                Line((-5.9, 1.8995561984), (-5.9, 3.35))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)
    return part.part


def model_71422_338eb6ff_0000():
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

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.137118444, perimeter: 27.8707962344
            with BuildLine():
                Line((-3.5, -1.4302095726), (-3.5, -2))
                Line((-3.5, -2), (-1, -2))
                Line((-1, -2), (-1, -1.5))
                Line((-1, -1.5), (1.5, -1.5))
                Line((1.5, -1.5), (1.5, -2))
                Line((1.5, -2), (2.5, -2))
                Line((2.5, -2), (2.5, -1.5))
                Line((2, -1.5), (2.5, -1.5))
                Line((2, -0.3725855273), (2, -1.5))
                Line((2.5, -0.3725855273), (2, -0.3725855273))
                Line((2.5, -0.3725855273), (2.5, 0))
                Line((2.5, 0), (2, 0))
                Line((2, 0), (2, 1.2556488118))
                Line((2, 1.2556488118), (2.5, 1.2556488118))
                Line((2.5, 1.2556488118), (2.5, 2))
                Line((2.5, 2), (1.7500000298, 2))
                Line((1.7500000298, 2), (1.7500000298, 1.7000000253))
                Line((1.7500000298, 1.7000000253), (0.5, 1.7000000253))
                Line((0.5, 1.7000000253), (0.5, 1.5))
                Line((0.5, 1.5), (-1.5, 1.5))
                Line((-1.5, 1.5), (-1.5, 2))
                Line((-1.5, 2), (-1.75, 2))
                Line((-1.75, 2), (-1.75, 1.75))
                Line((-1.75, 1.75), (-3.5, 1.75))
                Line((-3.5, 1.75), (-3.5, 2))
                Line((-3.5, 2), (-4, 2))
                Line((-4, 2), (-4, -0.1591667508))
                Line((-4, -0.1591667508), (-3.5, -0.1591667508))
                Line((-3.5, -0.1591667508), (-3.5, -0.200000003))
                Line((-3.1000000462, -0.200000003), (-3.5, -0.200000003))
                Line((-3.1000000462, -1.4302095726), (-3.1000000462, -0.200000003))
                Line((-3.5, -1.4302095726), (-3.1000000462, -1.4302095726))
            make_face()
            with BuildLine():
                CenterArc((-2.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_73388_10a40b49_0026():
    """Model: Bottom_Bolt_Long"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7542963961, perimeter: 3.0787608005
            Circle(0.49)
        # OneSide extrude, distance=0.48
        extrude(amount=0.48)

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

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_73764_0bd59074_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 41.2806195997, perimeter: 91.398229715
            with BuildLine():
                Line((9.15, 14.3), (16, 14.3))
                Line((16, 14.3), (16, 15.2))
                Line((16, 15.2), (0, 15.2))
                Line((0, 15.2), (0, 14.3))
                Line((0, 14.3), (6.85, 14.3))
                CenterArc((6.85, 13.6), 0.7, 0, 90)
                Line((7.55, 1.6), (7.55, 13.6))
                CenterArc((6.85, 1.6), 0.7, -90, 90)
                Line((0, 0.9), (6.85, 0.9))
                Line((0, 0), (0, 0.9))
                Line((0, 0), (16, 0))
                Line((16, 0), (16, 0.9))
                Line((16, 0.9), (9.15, 0.9))
                CenterArc((9.15, 1.6), 0.7, 180, 90)
                Line((8.45, 1.6), (8.45, 13.6))
                CenterArc((9.15, 13.6), 0.7, 90, 90)
            make_face()
        # OneSide extrude, distance=95
        extrude(amount=95)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-8, 91)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-8, 4)):
                Circle(2.5)
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8, perimeter: 13.6
            with BuildLine():
                Line((-11, 32.5), (-5, 32.5))
                Line((-5, 32.5), (-5, 33.3))
                Line((-5, 33.3), (-11, 33.3))
                Line((-11, 33.3), (-11, 32.5))
            make_face()
            # Profile area: 4.8, perimeter: 13.6
            with BuildLine():
                Line((-11, 61.7), (-11, 62.5))
                Line((-5, 61.7), (-11, 61.7))
                Line((-5, 62.5), (-5, 61.7))
                Line((-11, 62.5), (-5, 62.5))
            make_face()
        # OneSide extrude, distance=42
        extrude(amount=42, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 61.7), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-8, 55.3955412823)):
                Circle(1.5)
        # OneSide extrude, distance=28.4
        extrude(amount=28.4, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 322.3174770425, perimeter: 137.853981634
            with BuildLine():
                Line((-2.5, 80), (0, 80))
                CenterArc((-2.5, 77.5), 2.5, 90, 90)
                Line((-5, 62.5), (-5, 77.5))
                Line((-5, 61.7), (-5, 62.5))
                Line((-5, 61.7), (-5, 33.3))
                Line((-5, 33.3), (-5, 32.5))
                Line((-5, 32.5), (-5, 17.5))
                CenterArc((-2.5, 17.5), 2.5, 180, 90)
                Line((-2.5, 15), (0, 15))
                Line((0, 15), (0, 80))
            make_face()
        # OneSide extrude, distance=-16
        extrude(amount=-16, mode=Mode.SUBTRACT)
    return part.part


def model_76300_7cb02add_0000():
    """Model: Spade Common"""
    with BuildPart() as part:
        # Form -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2724738644, perimeter: 7.2447061274
            with BuildLine():
                CenterArc((0.1500000015, -1.0500000164), 0.1275, -180, 90)
                Line((0.1500000015, -1.1775000164), (1.0152000015, -1.1775000164))
                Line((1.1562540967, -1.1485457689), (1.0152000015, -1.1775000164))
                CenterArc((1.1542433174, -1.1387500164), 0.01, -78.4, 156.8)
                Line((1.0152000015, -1.1000000164), (1.1562540967, -1.1289542639))
                Line((0.1500000015, -1.1000000164), (1.0152000015, -1.1000000164))
                CenterArc((0.1500000015, -1.0500000164), 0.05, -180, 90)
                Line((0.1000000015, -1.0500000164), (0.1000000015, -0.1975000164))
                CenterArc((-0.0274999985, -0.1975000164), 0.1275, 0, 90)
                Line((-0.0274999985, -0.0700000164), (-0.5499999985, -0.0700000164))
                CenterArc((-0.5499999985, -0.0200000164), 0.05, 180, 90)
                Line((-0.5999999985, -0.0200000164), (-0.5999999985, 0.7474999836))
                Line((-0.6774999985, 0.7474999836), (-0.5999999985, 0.7474999836))
                Line((-0.6774999985, -0.0200000164), (-0.6774999985, 0.7474999836))
                CenterArc((-0.5499999985, -0.0200000164), 0.1275, 180, 90)
                Line((-0.0274999985, -0.1475000164), (-0.5499999985, -0.1475000164))
                CenterArc((-0.0274999985, -0.1975000164), 0.05, 0, 90)
                Line((0.0225000015, -1.0500000164), (0.0225000015, -0.1975000164))
            make_face()
        # Symmetric extrude, each_side=0.385
        extrude(amount=0.385, both=True)

        # Tab Cut -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1775000164), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.048269, perimeter: 1.6152
            with BuildLine():
                Line((0.2726000015, -0.385), (1.0152000015, -0.385))
                Line((1.0152000015, -0.385), (1.0152000015, -0.32))
                Line((0.2726000015, -0.32), (1.0152000015, -0.32))
                Line((0.2726000015, -0.385), (0.2726000015, -0.32))
            make_face()
            # Profile area: 0.0370271642, perimeter: 0.8633199205
            with BuildLine():
                Line((1.0152000015, -0.385), (1.0152000015, -0.32))
                Line((1.0152000015, -0.385), (1.2299844334, -0.385))
                Line((1.2299844334, -0.1052155681), (1.2299844334, -0.385))
                Line((1.0152000015, -0.32), (1.2299844334, -0.1052155681))
            make_face()
            # Profile area: 0.0370271642, perimeter: 0.8633199205
            with BuildLine():
                Line((1.0152000015, 0.32), (1.2299844334, 0.1052155681))
                Line((1.2299844334, 0.1052155681), (1.2299844334, 0.385))
                Line((1.0152000015, 0.385), (1.2299844334, 0.385))
                Line((1.0152000015, 0.32), (1.0152000015, 0.385))
            make_face()
            # Profile area: 0.048269, perimeter: 1.6152
            with BuildLine():
                Line((1.0152000015, 0.32), (1.0152000015, 0.385))
                Line((0.2726000015, 0.385), (1.0152000015, 0.385))
                Line((0.2726000015, 0.385), (0.2726000015, 0.32))
                Line((0.2726000015, 0.32), (1.0152000015, 0.32))
            make_face()
            # Profile area: 0.019880391, perimeter: 0.5784291735
            with BuildLine():
                CenterArc((0.6902000015, 0), 0.1125, 180, 180)
                Line((0.5777000015, 0), (0.8027000015, 0))
            make_face()
            # Profile area: 0.019880391, perimeter: 0.5784291735
            with BuildLine():
                Line((0.5777000015, 0), (0.8027000015, 0))
                CenterArc((0.6902000015, 0), 0.1125, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.0775
        extrude(amount=-0.0775, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1000000015, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0893, perimeter: 1.77
            with BuildLine():
                Line((-0.2675000164, -0.2), (-0.1975000164, -0.2))
                Line((-0.2675000164, -0.32), (-0.2675000164, -0.2))
                Line((-0.4175000164, -0.32), (-0.2675000164, -0.32))
                Line((-0.4175000164, -0.2), (-0.4175000164, -0.32))
                Line((-0.7775000164, -0.2), (-0.4175000164, -0.2))
                Line((-0.7775000164, -0.385), (-0.7775000164, -0.2))
                Line((-0.7775000164, -0.385), (-0.1975000164, -0.385))
                Line((-0.1975000164, -0.385), (-0.1975000164, -0.2))
            make_face()
            # Profile area: 0.0242695962, perimeter: 0.6323740132
            with BuildLine():
                Line((-0.1975000164, -0.385), (-0.1975000164, -0.2))
                Line((-0.1975000164, -0.385), (-0.0663130098, -0.385))
                Line((-0.0663130098, -0.2), (-0.0663130098, -0.385))
                Line((-0.1975000164, -0.2), (-0.0663130098, -0.2))
            make_face()
            # Profile area: 0.0070000001, perimeter: 0.340000003
            with BuildLine():
                Line((-0.1975000164, -0.1000000015), (-0.1975000164, 0))
                Line((-0.2675000164, 0), (-0.1975000164, 0))
                Line((-0.2675000164, -0.1000000015), (-0.2675000164, 0))
                Line((-0.2675000164, -0.1000000015), (-0.1975000164, -0.1000000015))
            make_face()
            # Profile area: 0.0127500002, perimeter: 0.455000003
            with BuildLine():
                Line((-0.1975000164, 0), (-0.0700000164, 0))
                Line((-0.1975000164, -0.1000000015), (-0.1975000164, 0))
                Line((-0.1975000164, -0.1000000015), (-0.0700000164, -0.1000000015))
                Line((-0.0700000164, -0.1000000015), (-0.0700000164, 0))
            make_face()
            # Profile area: 0.0127500002, perimeter: 0.455000003
            with BuildLine():
                Line((-0.1975000164, 0), (-0.1975000164, 0.1000000015))
                Line((-0.1975000164, 0), (-0.0700000164, 0))
                Line((-0.0700000164, 0.1000000015), (-0.0700000164, 0))
                Line((-0.1975000164, 0.1000000015), (-0.0700000164, 0.1000000015))
            make_face()
            # Profile area: 0.0070000001, perimeter: 0.340000003
            with BuildLine():
                Line((-0.2675000164, 0.1000000015), (-0.1975000164, 0.1000000015))
                Line((-0.2675000164, 0.1000000015), (-0.2675000164, 0))
                Line((-0.2675000164, 0), (-0.1975000164, 0))
                Line((-0.1975000164, 0), (-0.1975000164, 0.1000000015))
            make_face()
            # Profile area: 0.0242695962, perimeter: 0.6323740132
            with BuildLine():
                Line((-0.1975000164, 0.2), (-0.1975000164, 0.385))
                Line((-0.1975000164, 0.2), (-0.0663130098, 0.2))
                Line((-0.0663130098, 0.2), (-0.0663130098, 0.385))
                Line((-0.1975000164, 0.385), (-0.0663130098, 0.385))
            make_face()
            # Profile area: 0.0893, perimeter: 1.77
            with BuildLine():
                Line((-0.7775000164, 0.385), (-0.1975000164, 0.385))
                Line((-0.7775000164, 0.385), (-0.7775000164, 0.2))
                Line((-0.7775000164, 0.2), (-0.4175000164, 0.2))
                Line((-0.4175000164, 0.2), (-0.4175000164, 0.32))
                Line((-0.4175000164, 0.32), (-0.2675000164, 0.32))
                Line((-0.2675000164, 0.32), (-0.2675000164, 0.2))
                Line((-0.2675000164, 0.2), (-0.1975000164, 0.2))
                Line((-0.1975000164, 0.2), (-0.1975000164, 0.385))
            make_face()
        # OneSide extrude, distance=-0.19
        extrude(amount=-0.19, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.6774999985, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0253757704, perimeter: 0.7199557034
            with BuildLine():
                CenterArc((0.0200000164, 0), 0.035, -90, 90)
                Line((0.0200000164, -0.105), (0.0200000164, -0.035))
                Line((0.1499999966, -0.105), (0.0200000164, -0.105))
                Line((0.1499999966, -0.105), (0.1499999966, 0.105))
                Line((0.1499999966, 0.105), (0.0200000164, 0.105))
                Line((0.0200000164, 0.035), (0.0200000164, 0.105))
                CenterArc((0.0200000164, 0), 0.035, 0, 90)
            make_face()
            # Profile area: 0.0019242272, perimeter: 0.17995579
            with BuildLine():
                CenterArc((0.0199999928, -0.07), 0.035, 89.9999614094, 180.0000771757)
                Line((0.0200000164, -0.105), (0.0200000164, -0.035))
            make_face()
            # Profile area: 0.0019242272, perimeter: 0.17995579
            with BuildLine():
                Line((0.0200000164, 0.035), (0.0200000164, 0.105))
                CenterArc((0.0199999928, 0.07), 0.035, 89.9999614094, 180.0000771757)
            make_face()
        # OneSide extrude, distance=-0.22
        extrude(amount=-0.22, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.6774999985, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0240499991, perimeter: 0.6299999877
            with BuildLine():
                Line((0.1499999966, 0.1999999955), (0.1499999966, 0.3850000183))
                Line((0.1499999966, 0.3850000183), (0.0200000164, 0.3850000156))
                Line((0.0200000164, 0.1999999955), (0.0200000164, 0.3850000156))
                Line((0.1499999966, 0.1999999955), (0.0200000164, 0.1999999955))
            make_face()
            # Profile area: 0.1419875094, perimeter: 1.9050000089
            with BuildLine():
                Line((0.0200000164, -0.1999999955), (-0.7474999836, -0.1999999955))
                Line((-0.7474999836, -0.1999999955), (-0.7474999836, -0.385))
                Line((0.0200000164, -0.3850000156), (-0.7474999836, -0.385))
                Line((0.0200000164, -0.3850000156), (0.0200000164, -0.1999999955))
            make_face()
            # Profile area: 0.073125, perimeter: 1.1
            with BuildLine():
                Line((-0.4224999836, -0.0250000045), (-0.7474999836, -0.0250000045))
                Line((-0.4224999836, 0.1999999955), (-0.4224999836, -0.0250000045))
                Line((-0.4224999836, 0.1999999955), (-0.7474999836, 0.1999999955))
                Line((-0.7474999836, 0.1999999955), (-0.7474999836, -0.0250000045))
            make_face()
            # Profile area: 0.1419875094, perimeter: 1.9050000089
            with BuildLine():
                Line((0.0200000164, 0.1999999955), (0.0200000164, 0.3850000156))
                Line((0.0200000164, 0.3850000156), (-0.7474999836, 0.385))
                Line((-0.7474999836, 0.385), (-0.7474999836, 0.1999999955))
                Line((-0.4224999836, 0.1999999955), (-0.7474999836, 0.1999999955))
                Line((0.0200000164, 0.1999999955), (-0.4224999836, 0.1999999955))
            make_face()
            # Profile area: 0.0240499991, perimeter: 0.6299999877
            with BuildLine():
                Line((0.0200000164, -0.3850000156), (0.0200000164, -0.1999999955))
                Line((0.1499999966, -0.3850000183), (0.0200000164, -0.3850000156))
                Line((0.1499999966, -0.1999999955), (0.1499999966, -0.3850000183))
                Line((0.1499999966, -0.1999999955), (0.0200000164, -0.1999999955))
            make_face()
        # OneSide extrude, distance=-0.5875
        extrude(amount=-0.5875, mode=Mode.SUBTRACT)
    return part.part


def model_78102_5458aba8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 136.925, perimeter: 47.9865007051
            with BuildLine():
                Line((3.8, 13.9), (0, 13.9))
                Line((0, 13.9), (0, 0))
                Line((0, 0), (12.7, 0))
                Line((12.7, 0), (12.7, 5))
                Line((12.7, 5), (3.8, 13.9))
            make_face()
        # Symmetric extrude, full_length=True, total=7.6
        extrude(amount=3.8, both=True)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 35.9247126301, perimeter: 47.6451302091
            with BuildLine():
                Line((8.2, 3.8), (0.6, 3.8))
                Line((8.2, 3.8), (8.2, 8.9))
                CenterArc((4.4, 8.9), 3.8, 0, 180)
                Line((0.6, 8.9), (0.6, 3.8))
            make_face()
            with BuildLine():
                CenterArc((4.4, 8.9), 2.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 35.9247126301, perimeter: 47.6451302091
            with BuildLine():
                Line((0.6, -3.8), (8.2, -3.8))
                Line((0.6, -3.8), (0.6, -8.9))
                CenterArc((4.4, -8.9), 3.8, 180, 180)
                Line((8.2, -8.9), (8.2, -3.8))
            make_face()
            with BuildLine():
                CenterArc((4.4, -8.9), 2.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 14.1764368493, perimeter: 29.8451302091
            with BuildLine():
                CenterArc((4.4, -8.9), 2.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.4, -8.9), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 14.1764368493, perimeter: 29.8451302091
            with BuildLine():
                CenterArc((4.4, 8.9), 2.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.4, 8.9), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1764368493, perimeter: 29.8451302091
            with BuildLine():
                CenterArc((-4.4, 8.9), 2.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.4, 8.9), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 14.1764368493, perimeter: 29.8451302091
            with BuildLine():
                CenterArc((-4.4, -8.9), 2.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.4, -8.9), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.52, perimeter: 34.0499566724
            with BuildLine():
                Line((1.2, 13.9), (12.7, 2.4))
                Line((12.7, 2.4), (12.7, 5))
                Line((12.7, 5), (3.8, 13.9))
                Line((1.2, 13.9), (3.8, 13.9))
            make_face()
        # Symmetric extrude, full_length=True, total=2.6
        extrude(amount=1.3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_78433_1f73539f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 660.7300918301, perimeter: 115.7079632679
            with BuildLine():
                CenterArc((35, -10), 5, 90, 180)
                Line((35, 0), (35, -5))
                Line((0, 0), (35, 0))
                Line((0, -20), (0, 0))
                Line((35, -20), (0, -20))
                Line((35, -15), (35, -20))
            make_face()
            # Profile area: 117.8097245096, perimeter: 57.1238898038
            with BuildLine():
                CenterArc((35, -10), 5, -90, 180)
                Line((35, -15), (35, -20))
                CenterArc((35, -10), 10, -90, 180)
                Line((35, 0), (35, -5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 75, perimeter: 40
            with BuildLine():
                Line((0, 5), (-15, 5))
                Line((-15, 0), (-15, 5))
                Line((-15, 0), (0, 0))
                Line((0, 0), (0, 5))
            make_face()
            # Profile area: 75, perimeter: 40
            with BuildLine():
                Line((0, 15), (0, 20))
                Line((0, 20), (-15, 20))
                Line((-15, 15), (-15, 20))
                Line((0, 15), (-15, 15))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 20), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 88.3572933822, perimeter: 38.5619449019
            with BuildLine():
                Line((15, 15), (0, 15))
                CenterArc((7.5, 15), 7.5, 0, 180)
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 66.2679700367, perimeter: 42.8429173529
            with BuildLine():
                CenterArc((-7.5, 15), 7.5, 0, 180)
                Line((-11.25, 15), (-15, 15))
                CenterArc((-7.5, 15), 3.75, 0, 180)
                Line((0, 15), (-3.75, 15))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 22.0893233456, perimeter: 19.280972451
            with BuildLine():
                Line((-3.75, 15), (-11.25, 15))
                CenterArc((-7.5, 15), 3.75, 180, 180)
            make_face()
            # Profile area: 22.0893233456, perimeter: 19.280972451
            with BuildLine():
                CenterArc((-7.5, 15), 3.75, 0, 180)
                Line((-3.75, 15), (-11.25, 15))
            make_face()
        # OneSide extrude, distance=-32.5
        extrude(amount=-32.5, mode=Mode.SUBTRACT)
    return part.part


def model_78861_0f81caaa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.92, perimeter: 11.6
            with BuildLine():
                Line((10.4, 5.2), (8.2, 5.2))
                Line((8.2, 5.2), (8.2, 1.6))
                Line((10.4, 1.6), (8.2, 1.6))
                Line((10.4, 1.6), (10.4, 5.2))
            make_face()
            # Profile area: 31.12, perimeter: 38.2627416998
            with BuildLine():
                Line((10.4, 1.6), (8.2, 1.6))
                Line((8.2, 1.6), (-1.4, 1.6))
                Line((-1.4, 1.6), (-1.4, 5.2))
                Line((-1.4, 5.2), (-2.4, 5.2))
                Line((-4, 3.6), (-2.4, 5.2))
                Line((-4, 0), (-4, 3.6))
                Line((-4, 0), (10.4, 0))
                Line((10.4, 0), (10.4, 1.6))
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.72, perimeter: 3.4
            with BuildLine():
                Line((-2.4, 1.6), (-3.2, 1.6))
                Line((-3.2, 1.6), (-3.2, 0.7))
                Line((-3.2, 0.7), (-2.4, 0.7))
                Line((-2.4, 0.7), (-2.4, 1.6))
            make_face()
            # Profile area: 0.72, perimeter: 3.4
            with BuildLine():
                Line((-3.2, 0.7), (-4, 0.7))
                Line((-3.2, 1.6), (-3.2, 0.7))
                Line((-4, 1.6), (-3.2, 1.6))
                Line((-4, 0.7), (-4, 1.6))
            make_face()
            # Profile area: 1.12, perimeter: 4.6
            with BuildLine():
                Line((-3.2, 0), (-4.8, 0))
                Line((-3.2, 0.7), (-3.2, 0))
                Line((-3.2, 0.7), (-4, 0.7))
                Line((-4.8, 0.7), (-4, 0.7))
                Line((-4.8, 0), (-4.8, 0.7))
            make_face()
            # Profile area: 1.12, perimeter: 4.6
            with BuildLine():
                Line((-3.2, 0.7), (-2.4, 0.7))
                Line((-3.2, 0.7), (-3.2, 0))
                Line((-3.2, 0), (-1.6, 0))
                Line((-1.6, 0), (-1.6, 0.7))
                Line((-1.6, 0.7), (-2.4, 0.7))
            make_face()
        # OneSide extrude, distance=-14.4
        extrude(amount=-14.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(10.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.4230725527, perimeter: 21.7919185377
            with BuildLine():
                CenterArc((-3.2, 3.6), 1.4976419978, 47.9263002362, 84.1473995277)
                CenterArc((-3.2, 3.6), 1.4976419978, 31.2084682728, 16.7178319633)
                Line((0, 2.0535422236), (-1.91908524, 4.3760083319))
                Line((0, 5.2), (0, 2.0535422236))
                Line((0, 5.2), (-6.4, 5.2))
                Line((-6.4, 2.0535422236), (-6.4, 5.2))
                Line((-6.4, 2.0535422236), (-4.48091476, 4.3760083319))
                CenterArc((-3.2, 3.6), 1.4976419978, 132.0736997638, 16.7178319633)
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_78978_24711a0f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 33 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 342.2734457254, perimeter: 234.1822971503
            with BuildLine():
                Line((2, 37.5), (28.75, 37.5))
                Line((28.75, 37.5), (28.75, 40.5))
                Line((2, 40.5), (28.75, 40.5))
                CenterArc((2, 35.5), 5, 90, 90)
                Line((-3, 30), (-3, 35.5))
                CenterArc((-5, 30), 2, -90, 90)
                Line((-5, 28), (-32.5, 28))
                CenterArc((-32.5, 30), 2, 180, 90)
                Line((-34.5, 30), (-34.5, 35.6))
                CenterArc((-39.5, 35.6), 5, 0, 90)
                Line((-39.5, 40.6), (-66.25, 40.6))
                Line((-66.25, 37.6), (-66.25, 40.6))
                Line((-39.5, 37.6), (-66.25, 37.6))
                CenterArc((-39.5, 35.6), 2, 0, 90)
                Line((-37.5, 30), (-37.5, 35.6))
                CenterArc((-32.5, 30), 5, 180, 90)
                Line((-5, 25), (-32.5, 25))
                CenterArc((-5, 30), 5, -90, 90)
                Line((0, 30), (0, 35.5))
                CenterArc((2, 35.5), 2, 90, 90)
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 28, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 397.60782022, perimeter: 70.6858347058
            with Locations((17.9586404197, 14.954756147)):
                Circle(11.25)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((52.875, 15)):
                Circle(2.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-15.375, 15)):
                Circle(2.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 35.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 122.7184630309, perimeter: 39.2699081699
            with Locations((17.9586404197, 14.954756147)):
                Circle(6.25)
        # OneSide extrude, distance=-100
        extrude(amount=-100, mode=Mode.SUBTRACT)
    return part.part


def model_78980_e36c37a8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 120.4314165294, perimeter: 76.4247779608
            with BuildLine():
                Line((-7.5, 0), (-7.5, -3.5))
                Line((-7.5, -3.5), (-2.5, -3.5))
                Line((-2.5, -3.5), (-2.5, -18.5))
                Line((-2.5, -18.5), (2.5, -18.5))
                Line((2.5, -18.5), (2.5, -3.5))
                Line((2.5, -3.5), (7.5, -3.5))
                Line((7.5, -3.5), (7.5, 0))
                Line((-7.5, 0), (7.5, 0))
            make_face()
            with BuildLine():
                CenterArc((0, -2), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 88.3572933822, perimeter: 38.5619449019
            with BuildLine():
                Line((-7.5, 0), (7.5, 0))
                CenterArc((0, 0), 7.5, 0, 180)
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -18.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 5), 2.5, 0, 180)
                CenterArc((0, 5), 2.5, 180, 180)
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)
    return part.part


def model_79530_946fa2d1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=33
        extrude(amount=33)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 12.0579583412, perimeter: 18.7703473215
            with BuildLine():
                Line((0, 1), (6.814377334, 1))
                CenterArc((0, 0), 1, -90, 180)
                Line((6.814377334, -1), (0, -1))
                Line((6.814377334, 1), (6.814377334, -1))
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((0, -1), (0, 1))
                CenterArc((0, 0), 1, -90, 180)
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                CenterArc((0, 0), 1, 90, 180)
                Line((0, -1), (0, 1))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.7888903963, perimeter: 8.0752869843
            with BuildLine():
                Line((3.4583384919, -0.7333305266), (0.9040255263, -0.7333305266))
                Line((3.4583384919, 0.75), (3.4583384919, -0.7333305266))
                Line((0.9040255263, 0.75), (3.4583384919, 0.75))
                Line((0.9040255263, -0.7333305266), (0.9040255263, 0.75))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_80193_e198f23e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.78, perimeter: 25.8
            with BuildLine():
                Line((2.5, 3.5), (2.8, 3.5))
                Line((2.5, 3.5), (2.5, 0))
                Line((2.5, 0), (-2.5, 0))
                Line((-2.5, 3.5), (-2.5, 0))
                Line((-2.5, 3.5), (-2.8, 3.5))
                Line((-2.8, 3.5), (-2.8, -0.3))
                Line((-2.8, -0.3), (2.8, -0.3))
                Line((2.8, 3.5), (2.8, -0.3))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -0.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853982233, perimeter: 3.1415927734
            with Locations((1.3, 0)):
                Circle(0.5000000191)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.6546457923, perimeter: 6.6840704497
            with BuildLine():
                Line((-2.6, 3.5), (0, 3.5))
                CenterArc((-1.3, 3.5), 1.3, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.6546457923, perimeter: 6.6840704497
            with BuildLine():
                Line((0, 3.5), (2.6, 3.5))
                CenterArc((1.3, 3.5), 1.3, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5654866327, perimeter: 2.665729657
            with Locations((1.3, 3.5)):
                Circle(0.4242640519)
        # OneSide extrude, distance=-13.1
        extrude(amount=-13.1, mode=Mode.SUBTRACT)
    return part.part


def model_80331_b436d0d5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3252442161, perimeter: 2.0216674702
            with Locations((1.510293174, 2.1635091129)):
                Circle(0.3217583712)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3356604723, perimeter: 2.5015085332
            with BuildLine():
                Line((0.5345347051, 3.1358201504), (0.8919997665, 3.3844255667))
                Line((0.71942459, 2.7428740797), (0.5345347051, 3.1358201504))
                Line((1.5545520205, 3.1358201504), (0.71942459, 2.7428740797))
                CenterArc((0, 0), 3.5, 63.6305374697, 11.6043461212)
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_80471_4a6e9e76_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.7043692606, perimeter: 19.426990817
            with BuildLine():
                Line((0, 0), (0, -1.5))
                Line((0, -1.5), (2.5, -1.5))
                CenterArc((3.75, -1.5), 1.25, 180, 180)
                Line((5, -1.5), (7.5, -1.5))
                Line((7.5, 0), (7.5, -1.5))
                Line((0, 0), (7.5, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.2024460505, perimeter: 3.8872075729
            with Locations((3.75, -1.5)):
                Circle(0.6186683001)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.4582187586, perimeter: 2.3996138738
            with Locations((1.25, 1.3453614658)):
                Circle(0.3819104095)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.4751065571, perimeter: 2.4434330517
            with Locations((6.3071651174, 1.3159838042)):
                Circle(0.3888844483)
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)
    return part.part


def model_80472_01f15238_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-4, 0)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 4)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((4, 0)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, -4)):
                Circle(0.5)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


def model_80589_b85b71c6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.25, perimeter: 10
            with BuildLine():
                Line((2.5, -2.5), (0, -2.5))
                Line((2.5, 0), (2.5, -2.5))
                Line((0, 0), (2.5, 0))
                Line((0, -2.5), (0, 0))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)
    return part.part


def model_80785_5b40ac2b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.4, perimeter: 43.0796447372
            with BuildLine():
                CenterArc((-5.5, -1.5), 0.8, -180, 90)
                Line((-5.5, -2.3), (5.5, -2.3))
                CenterArc((5.5, -1.5), 0.8, -90, 90)
                Line((6.3, -1.5), (6.3, 1.5))
                CenterArc((5.5, 1.5), 0.8, 0, 90)
                Line((5.5, 2.3), (-5.5, 2.3))
                CenterArc((-5.5, 1.5), 0.8, 90, 90)
                Line((-6.3, 1.5), (-6.3, -1.5))
            make_face()
            with BuildLine():
                CenterArc((-5.5, 1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.5, -1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5, -1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5, 1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.8484510006, perimeter: 12.3955742876
            with BuildLine():
                CenterArc((2.3, 0), 1.4, 0, 180)
                Line((4.4, 0), (3.7, 0))
                CenterArc((2.3, 0), 2.1, 0, 180)
                Line((0.9, 0), (0.2, 0))
            make_face()
        # Symmetric extrude, each_side=2.8
        extrude(amount=2.8, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0787608005, perimeter: 7.198229715
            with BuildLine():
                CenterArc((2.3, 0), 1.4, -180, 180)
                Line((0.9, 0), (3.7, 0))
            make_face()
            # Profile area: 3.0787608005, perimeter: 7.198229715
            with BuildLine():
                Line((0.9, 0), (3.7, 0))
                CenterArc((2.3, 0), 1.4, 0, 180)
            make_face()
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.1469023027, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((-3.2, 4.5), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.2, 4.5), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.8
        extrude(amount=2.8, both=True)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((2.3000000343, 0)):
                Circle(0.6)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.SUBTRACT)
    return part.part


def model_81025_dc67f73b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 136.925, perimeter: 47.9865007051
            with BuildLine():
                Line((0, 0), (12.7, 0))
                Line((12.7, 5), (12.7, 0))
                Line((3.8, 13.9), (12.7, 5))
                Line((0, 13.9), (3.8, 13.9))
                Line((0, 0), (0, 13.9))
            make_face()
        # OneSide extrude, distance=3.95
        extrude(amount=3.95)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 26.52, perimeter: 34.0499566724
            with BuildLine():
                Line((-1.2, 13.9), (-12.7, 2.4))
                Line((-1.2, 13.9), (-3.8, 13.9))
                Line((-3.8, 13.9), (-12.7, 5))
                Line((-12.7, 5), (-12.7, 2.4))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 48.9611494795, perimeter: 41.3761041673
            with BuildLine():
                Line((8.2, 3.95), (0.6, 3.95))
                Line((8.2, 8.9), (8.2, 3.95))
                CenterArc((4.4, 8.9), 3.8, 0, 180)
                Line((0.6, 8.9), (0.6, 3.95))
            make_face()
            with BuildLine():
                CenterArc((4.4, 8.9), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1764368493, perimeter: 29.8451302091
            with BuildLine():
                CenterArc((-4.4, 8.9), 2.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.4, 8.9), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_81145_d4ae4770_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            Circle(0.65)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725313, perimeter: 2.8274334304
            Circle(0.4500000067)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.8125000201, perimeter: 13.987691158
            with BuildLine():
                Line((-1.1245361281, 0.4477678212), (-0.7830297419, 0.3562614673))
                Line((0.082995627, 0.8562614472), (-0.7830297419, 0.3562614673))
                Line((0.1745019776, 1.1977678212), (0.082995627, 0.8562614472))
                Line((0.1745019776, 1.1977678212), (-1.1754980224, 3.5360364114))
                Line((-1.1754980224, 3.5360364114), (-3.2817158051, 5.7841126227))
                Line((-3.9745361281, 5.3841126227), (-3.2817158051, 5.7841126227))
                Line((-1.1245361281, 0.4477678212), (-3.9745361281, 5.3841126227))
            make_face()
            # Profile area: 7.8125000201, perimeter: 13.987691158
            with BuildLine():
                Line((1.1500000112, -0.75), (3.8500000112, -0.75))
                Line((3.8500000112, -0.75), (6.8500000112, -0.05))
                Line((6.8500000112, 0.75), (6.8500000112, -0.05))
                Line((1.1500000112, 0.75), (6.8500000112, 0.75))
                Line((1.1500000112, 0.75), (0.8999999911, 0.4999999709))
                Line((0.8999999911, -0.4999999888), (0.8999999911, 0.4999999709))
                Line((1.1500000112, -0.75), (0.8999999911, -0.4999999888))
            make_face()
            # Profile area: 7.8125000201, perimeter: 13.987691158
            with BuildLine():
                Line((-1.1245681642, -0.4476958165), (-2.4745681642, -2.7859644067))
                Line((-2.4745681642, -2.7859644067), (-3.3683503815, -5.7340406181))
                Line((-2.6755300585, -6.1340406181), (-3.3683503815, -5.7340406181))
                Line((0.1744699415, -1.1976958165), (-2.6755300585, -6.1340406181))
                Line((0.1744699415, -1.1976958165), (0.0829635754, -0.8561894336))
                Line((-0.7830617935, -0.3561894537), (0.0829635754, -0.8561894336))
                Line((-1.1245681642, -0.4476958165), (-0.7830617935, -0.3561894537))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_81821_3f648668_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.7373561782, perimeter: 46.0061061941
            with BuildLine():
                Line((11.8176930361, 0), (9.0176930361, 0))
                Line((11.8176930361, 2.916221868), (11.8176930361, 0))
                Line((0, 5), (11.8176930361, 2.916221868))
                Line((0, 0), (0, 5))
                Line((2.8, 0), (0, 0))
                Line((2.8, 0.8), (2.8, 0))
                Line((0.8, 0.8), (2.8, 0.8))
                Line((0.8, 0.8), (0.8, 3.958110934))
                Line((0.8, 3.958110934), (11.0176930361, 2.1564559711))
                Line((11.0176930361, 0.8), (11.0176930361, 2.1564559711))
                Line((9.0176930361, 0.8), (11.0176930361, 0.8))
                Line((9.0176930361, 0), (9.0176930361, 0.8))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3000000089, perimeter: 4.322374906
            with BuildLine():
                Line((2.8000000417, 0.5000000075), (0.8000000119, 0.8000000119))
                Line((2.8000000417, 0.8000000119), (2.8000000417, 0.5000000075))
                Line((0.8000000119, 0.8000000119), (2.8000000417, 0.8000000119))
            make_face()
            # Profile area: 0.2999999925, perimeter: 4.3223748331
            with BuildLine():
                Line((9.0176930361, 0.5000000075), (11.0176930361, 0.8))
                Line((9.0176930361, 0.8), (11.0176930361, 0.8))
                Line((9.0176930361, 0.8), (9.0176930361, 0.5000000075))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9.0176930361, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2184, perimeter: 2.2
            with BuildLine():
                Line((-0.42, 0.1200000075), (-0.42, 0.3800000075))
                Line((0.42, 0.1200000075), (-0.42, 0.1200000075))
                Line((0.42, 0.3800000075), (0.42, 0.1200000075))
                Line((-0.42, 0.3800000075), (0.42, 0.3800000075))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8550503583, 4.849231552, 0), x_dir=(0, 0, -1), z_dir=(0.1736481777, 0.984807753, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((3, -5.1317591117), (-3, -5.1317591117))
                Line((-3, -5.1317591117), (-3, -11.1317591117))
                Line((-3, -11.1317591117), (3, -11.1317591117))
                Line((3, -11.1317591117), (3, -5.1317591117))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


def model_81926_1a4f5935_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.4740505355, perimeter: 12.0478767913
            with BuildLine():
                Line((14.6237718884, 16.0998334927), (10, 16.0998334927))
                Line((14.6237718884, 17.5), (14.6237718884, 16.0998334927))
                Line((10, 17.5), (14.6237718884, 17.5))
                Line((10, 16.0998334927), (10, 17.5))
            make_face()
            # Profile area: 6.0240979724, perimeter: 12.9383150006
            with BuildLine():
                Line((2.8413302112, 18.8721727109), (-2.5, 18.8721727109))
                Line((2.8413302112, 20), (2.8413302112, 18.8721727109))
                Line((-2.5, 20), (2.8413302112, 20))
                Line((-2.5, 18.8721727109), (-2.5, 20))
            make_face()
            # Profile area: 5.6299926152, perimeter: 10.8422231553
            with BuildLine():
                Line((-8.4790549297, 16.0998334927), (-12.5, 16.0998334927))
                Line((-8.4790549297, 17.5), (-8.4790549297, 16.0998334927))
                Line((-12.5, 17.5), (-8.4790549297, 17.5))
                Line((-12.5, 16.0998334927), (-12.5, 17.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_83111_3ad0d7a8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9, perimeter: 37
            with BuildLine():
                Line((-1, 6.5), (-1, 0))
                Line((-5, 0), (-1, 0))
                Line((-5, 6.5), (-5, 0))
                Line((-5, 6.5), (-5.5, 6.5))
                Line((-5.5, 6.5), (-5.5, -0.5))
                Line((-0.5, -0.5), (-5.5, -0.5))
                Line((-0.5, 6.5), (-0.5, -0.5))
                Line((-1, 6.5), (-0.5, 6.5))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.9817477042, perimeter: 3.5124073655
            with Locations((1.75, 3)):
                Circle(0.5590169944)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 4.8105637508, perimeter: 8.9977871438
            with BuildLine():
                Line((-3.5, 6.5), (0, 6.5))
                CenterArc((-1.75, 6.5), 1.75, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.8105637508, perimeter: 8.9977871438
            with BuildLine():
                Line((0, 6.5), (3.5, 6.5))
                CenterArc((1.75, 6.5), 1.75, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_83212_f8e72ef2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 391.7734457254, perimeter: 267.1822971503
            with BuildLine():
                Line((-18.75, -5), (-18.75, -18.8))
                CenterArc((-13.75, -18.8), 5, 180, 90)
                Line((-13.75, -23.8), (13.75, -23.8))
                CenterArc((13.75, -18.8), 5, -90, 90)
                Line((18.75, -18.8), (18.75, -5))
                CenterArc((20.75, -5), 2, 90, 90)
                Line((47.5, -3), (20.75, -3))
                Line((47.5, 0), (47.5, -3))
                Line((20.75, 0), (47.5, 0))
                CenterArc((20.75, -5), 5, 90, 90)
                Line((15.75, -5), (15.75, -18.8))
                CenterArc((13.75, -18.8), 2, -90, 90)
                Line((-13.75, -20.8), (13.75, -20.8))
                CenterArc((-13.75, -18.8), 2, 180, 90)
                Line((-15.75, -5), (-15.75, -18.8))
                CenterArc((-20.75, -5), 5, 0, 90)
                Line((-20.75, 0), (-47.5, 0))
                Line((-47.5, 0), (-47.5, -3))
                Line((-47.5, -3), (-20.75, -3))
                CenterArc((-20.75, -5), 2, 0, 90)
            make_face()
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -20.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 397.60782022, perimeter: 70.6858347058
            Circle(11.25)
        # OneSide extrude, distance=17.5
        extrude(amount=17.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 240.5281875405, perimeter: 54.9778714378
            Circle(8.75)
        # OneSide extrude, distance=-17.5
        extrude(amount=-17.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -20.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            Circle(3.75)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((0, -35)):
                Circle(2.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_83224_833dcf1f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 31 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 391.7734457254, perimeter: 267.1822971503
            with BuildLine():
                Line((71.25, 3.5), (95, 3.5))
                Line((95, 3.5), (95, 6.5))
                Line((71.25, 6.5), (95, 6.5))
                CenterArc((71.25, 1.5), 5, 90, 90)
                Line((66.25, -12.3), (66.25, 1.5))
                CenterArc((64.25, -12.3), 2, -90, 90)
                Line((30.75, -14.3), (64.25, -14.3))
                CenterArc((30.75, -12.3), 2, 180, 90)
                Line((28.75, 1.5), (28.75, -12.3))
                CenterArc((23.75, 1.5), 5, 0, 90)
                Line((0, 6.5), (23.75, 6.5))
                Line((0, 3.5), (0, 6.5))
                Line((0, 3.5), (23.75, 3.5))
                CenterArc((23.75, 1.5), 2, 0, 90)
                Line((25.75, 1.5), (25.75, -12.3))
                CenterArc((30.75, -12.3), 5, 180, 90)
                Line((30.75, -17.3), (64.25, -17.3))
                CenterArc((64.25, -12.3), 5, -90, 90)
                Line((69.25, -12.3), (69.25, 1.5))
                CenterArc((71.25, 1.5), 2, 90, 90)
            make_face()
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -14.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 397.60782022, perimeter: 70.6858347058
            with Locations((0, -47.5)):
                Circle(11.25)
        # OneSide extrude, distance=17
        extrude(amount=17, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -17.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 240.5281875405, perimeter: 54.9778714378
            with Locations((0, -47.5)):
                Circle(8.75)
        # OneSide extrude, distance=-17.5
        extrude(amount=-17.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((0, -83)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((0, -12)):
                Circle(2.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_83259_487d379e_0002():
    """Model: Front"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 168, perimeter: 56.8
            with BuildLine():
                Line((24.0175058541, 8.1119415127), (24.0175058541, -0.2880584873))
                Line((24.0175058541, -0.2880584873), (44.0175058541, -0.2880584873))
                Line((44.0175058541, -0.2880584873), (44.0175058541, 8.1119415127))
                Line((44.0175058541, 8.1119415127), (24.0175058541, 8.1119415127))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14.85, perimeter: 18.607788269
            with BuildLine():
                Line((24.0175058541, 2.7119415127), (29.5175058541, 8.1119415127))
                Line((29.5175058541, 8.1119415127), (24.0175058541, 8.1119415127))
                Line((24.0175058541, 2.7119415127), (24.0175058541, 8.1119415127))
            make_face()
            # Profile area: 14.85, perimeter: 18.607788269
            with BuildLine():
                Line((44.0175058541, 2.7119415127), (38.5175058541, 8.1119415127))
                Line((44.0175058541, 2.7119415127), (44.0175058541, 8.1119415127))
                Line((38.5175058541, 8.1119415127), (44.0175058541, 8.1119415127))
            make_face()
        # OneSide extrude, distance=-18.01
        extrude(amount=-18.01, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((34.0175058541, 6.1119415127)):
                Circle(1.5)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((34.0175058541, 3.6119415127)):
                Circle(0.25)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.4293536772, perimeter: 14.1716467639
            with BuildLine():
                CenterArc((24.5175058541, 7.9119415127), 4.75, -90.50037553, 89.9494818471)
                Line((29.2672862955, 7.8662714005), (24.4760236791, 3.1621226499))
            make_face()
            # Profile area: 6.4293536772, perimeter: 14.1716467639
            with BuildLine():
                CenterArc((43.5175058541, 7.9119415127), 4.75, -179.4491063171, 89.9494818471)
                Line((43.5589880292, 3.1621226499), (38.7677254128, 7.8662714005))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_83383_73ed7877_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 46.5056590762, perimeter: 28.7307029867
            with BuildLine():
                Line((1.0723568042, 7.4377082976), (6, 7.4377082976))
                Line((1.0723568042, -2), (1.0723568042, 7.4377082976))
                Line((6, -2), (1.0723568042, -2))
                Line((6, 7.4377082976), (6, -2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0571987607, perimeter: 1.0603479753
            with BuildLine():
                Line((-4.4794214488, -6.9492475058), (-4.1000000611, -6.9492475058))
                Line((-4.4794214488, -7.1000001058), (-4.4794214488, -6.9492475058))
                Line((-4.1000000611, -7.1000001058), (-4.4794214488, -7.1000001058))
                Line((-4.1000000611, -6.9492475058), (-4.1000000611, -7.1000001058))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch8 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1800000054, perimeter: 2.2000000328
            with BuildLine():
                Line((5.500000082, 0.400000006), (5.500000082, 0.6000000089))
                Line((5.500000082, 0.6000000089), (4.6000000685, 0.6000000089))
                Line((4.6000000685, 0.6000000089), (4.6000000685, 0.400000006))
                Line((4.6000000685, 0.400000006), (5.500000082, 0.400000006))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_83400_6db148a7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((11, 0)):
                Circle(2.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0776470611, perimeter: 1.4092122881
            with BuildLine():
                Line((-3.8000000566, 3.5000000522), (-3.2000000477, 3.5000000522))
                Line((-3.2000000477, 3.5000000522), (-3.4000000507, 3.7000000551))
                Line((-3.4000000507, 3.7000000551), (-3.5176471112, 3.6411765248))
                Line((-3.6500000544, 3.7000000551), (-3.5176471112, 3.6411765248))
                Line((-3.8000000566, 3.5000000522), (-3.6500000544, 3.7000000551))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5920466643, perimeter: 2.7276139399
            with Locations((-3.5000000522, 2.6000000387)):
                Circle(0.4341132414)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_84025_ec3401ea_0011():
    """Model: Spil"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=91.6
        extrude(amount=91.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 91.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=4.9
        extrude(amount=4.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 96.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)
    return part.part


def model_84025_ec3401ea_0012():
    """Model: SupportFF15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.8575120837, perimeter: 18.9015011539
            with BuildLine():
                CenterArc((2.6, 2.6), 3.15, 34.3712560241, 21.2574879518)
                Line((4.3783419244, 5.2), (0.8216580756, 5.2))
                CenterArc((2.6, 2.6), 3.15, 124.3712560241, 21.2574879518)
                Line((0, 4.3783419244), (0, 0.8216580756))
                CenterArc((2.6, 2.6), 3.15, -145.6287439759, 21.2574879518)
                Line((0.8216580756, 0), (4.3783419244, 0))
                CenterArc((2.6, 2.6), 3.15, -55.6287439759, 21.2574879518)
                Line((5.2, 0.8216580756), (5.2, 4.3783419244))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((-2.6, -2.6)):
                Circle(2)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-2.6, -2.6)):
                Circle(0.75)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((4.367766953, -0.832233047), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.367766953, -0.832233047), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((4.367766953, -4.367766953), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.367766953, -4.367766953), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0.832233047, -4.367766953), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.832233047, -4.367766953), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0.832233047, -0.832233047), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.832233047, -0.832233047), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((4.367766953, -0.832233047)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((4.367766953, -4.367766953)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.832233047, -4.367766953)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.832233047, -0.832233047)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((4.367766953, -4.367766953)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((4.367766953, -0.832233047)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.832233047, -0.832233047)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.832233047, -4.367766953)):
                Circle(0.25)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_85093_6c657024_0000():
    """Model: steadycamLower v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 212.4336293856, perimeter: 56.5663706144
            with BuildLine():
                Line((-7.5, 5.5), (-7.5, -5.5))
                CenterArc((-7.5, -7.5), 2, 0, 90)
                Line((-5.5, -7.5), (5.5, -7.5))
                CenterArc((7.5, -7.5), 2, 90, 90)
                Line((7.5, -5.5), (7.5, 5.5))
                CenterArc((7.5, 7.5), 2, 180, 90)
                Line((5.5, 7.5), (-5.5, 7.5))
                CenterArc((-7.5, 7.5), 2, -90, 90)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6597344573, perimeter: 6.9973445725
            with BuildLine():
                CenterArc((7.5, 7.5), 2.2, -180, 90)
                Line((7.5, 5.3), (7.5, 5.5))
                CenterArc((7.5, 7.5), 2, -180, 90)
                Line((5.5, 7.5), (5.3, 7.5))
            make_face()
            # Profile area: 0.6597344573, perimeter: 6.9973445725
            with BuildLine():
                CenterArc((-7.5, 7.5), 2.2, -90, 90)
                Line((-5.3, 7.5), (-5.5, 7.5))
                CenterArc((-7.5, 7.5), 2, -90, 90)
                Line((-7.5, 5.5), (-7.5, 5.3))
            make_face()
            # Profile area: 0.6597344573, perimeter: 6.9973445725
            with BuildLine():
                CenterArc((-7.5, -7.5), 2.2, 0, 90)
                Line((-7.5, -5.3), (-7.5, -5.5))
                CenterArc((-7.5, -7.5), 2, 0, 90)
                Line((-5.5, -7.5), (-5.3, -7.5))
            make_face()
            # Profile area: 0.6597344573, perimeter: 6.9973445725
            with BuildLine():
                Line((7.5, -5.5), (7.5, -5.3))
                CenterArc((7.5, -7.5), 2.2, 90, 90)
                Line((5.3, -7.5), (5.5, -7.5))
                CenterArc((7.5, -7.5), 2, 90, 90)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.2053084434, perimeter: 13.8230076758
            with Locations((-7.5, 7.5)):
                Circle(2.2)
            # Profile area: 15.2053084434, perimeter: 13.8230076758
            with Locations((7.5, -7.5)):
                Circle(2.2)
            # Profile area: 15.2053084434, perimeter: 13.8230076758
            with Locations((-7.5, -7.5)):
                Circle(2.2)
            # Profile area: 15.2053084434, perimeter: 13.8230076758
            with Locations((7.5, 7.5)):
                Circle(2.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((-2, -7.5), (2, -7.5))
                CenterArc((0, -7.5), 2, 180, 180)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((7.5, -2), (7.5, 2))
                CenterArc((7.5, 0), 2, -90, 180)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((-7.5, 2), (-7.5, -2))
                CenterArc((-7.5, 0), 2, 90, 180)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((2, 7.5), (-2, 7.5))
                CenterArc((0, 7.5), 2, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


def model_86702_c06b5954_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.2600413204, perimeter: 12.4880215827
            with BuildLine():
                CenterArc((0, 0), 2, 112.3316450092, 135.3367099816)
                Line((-0.7599342077, -1.85), (0.7599342077, -1.85))
                CenterArc((0, 0), 2, -67.6683549908, 135.3367099816)
                Line((-0.7599342077, 1.85), (0.7599342077, 1.85))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 4.0212385966, perimeter: 20.106192983
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.90725625, perimeter: 3.81
            with BuildLine():
                Line((0.47625, -0.47625), (-0.47625, -0.47625))
                Line((0.47625, 0.47625), (0.47625, -0.47625))
                Line((-0.47625, 0.47625), (0.47625, 0.47625))
                Line((-0.47625, -0.47625), (-0.47625, 0.47625))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)
    return part.part


def model_87358_854d47fe_0005():
    """Model: начало колонки v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=8.2
        extrude(amount=8.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 25.8336293856, perimeter: 38.1663706144
            with BuildLine():
                Line((4, -2.5), (4, 2.3))
                Line((4, 2.3), (-4, 2.3))
                Line((-4, 2.3), (-4, -2.5))
                Line((-4, -2.5), (4, -2.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8, mode=Mode.ADD)

        # Sketch7 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=8.2
        extrude(amount=8.2, mode=Mode.ADD)
    return part.part


def model_88396_5f13c951_0001():
    """Model: Untitled v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=-9
        extrude(amount=-9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2744217998, perimeter: 1.95
            with BuildLine():
                Line((-0.2814582562, 0.1625), (-0.2814582562, -0.1625))
                Line((-0.2814582562, -0.1625), (0, -0.325))
                Line((0, -0.325), (0.2814582562, -0.1625))
                Line((0.2814582562, -0.1625), (0.2814582562, 0.1625))
                Line((0.2814582562, 0.1625), (0, 0.325))
                Line((0, 0.325), (-0.2814582562, 0.1625))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_88680_0fb9b042_0001():
    """Model: Vice Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 76.3, perimeter: 33.0118963379
            with BuildLine():
                Line((3, 5), (-3, 5))
                Line((-3, 5), (-4, 3.15))
                Line((-4, 3.15), (-4, -3.15))
                Line((-4, -3.15), (-3, -5))
                Line((-3, -5), (3, -5))
                Line((4, -3.15), (3, -5))
                Line((4, -3.15), (4, 3.15))
                Line((3, 5), (4, 3.15))
            make_face()
        # OneSide extrude, distance=3.735
        extrude(amount=3.735)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 33 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.444551922, perimeter: 8.6760831279
            with BuildLine():
                Line((3.05, 4.2990200276), (3.05, 1.62))
                Line((3.05, 1.62), (4.7090215363, 1.62))
                Line((4.7090215363, 1.62), (4.7090215363, 4.2990200276))
                Line((4.7090215363, 4.2990200276), (3.05, 4.2990200276))
            make_face()
            # Profile area: 4.0790983901, perimeter: 8.4032568495
            with BuildLine():
                Line((-4.5726083971, 4.2990200276), (-3.05, 4.2990200276))
                Line((-4.5726083971, 1.62), (-4.5726083971, 4.2990200276))
                Line((-3.05, 1.62), (-4.5726083971, 1.62))
                Line((-3.05, 4.2990200276), (-3.05, 1.62))
            make_face()
            # Profile area: 4.0742661902, perimeter: 9.2284176775
            with BuildLine():
                CenterArc((-1.2712178481, 0.75), 0.15, 90, 90.7364976139)
                Line((-1.4115889792, 0), (-1.4212054558, 0.7480719069))
                Line((1.3884110208, 0), (-1.4115889792, 0))
                Line((1.3787449729, 0.7519280931), (1.3884110208, 0))
                CenterArc((1.2287573652, 0.75), 0.15, 0.7364976139, 89.2635023861)
                Line((0.7825, 0.9), (1.2287573652, 0.9))
                Line((0.7825, 0.9), (0.7825, 1.85))
                CenterArc((0.7325, 1.85), 0.05, 0, 90)
                Line((0.7325, 1.9), (-0.7325, 1.9))
                CenterArc((-0.7325, 1.85), 0.05, 90, 90)
                Line((-0.7825, 1.85), (-0.7825, 0.9))
                Line((-0.7825, 0.9), (-1.2712178481, 0.9))
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 25.375, perimeter: 21.5
            with BuildLine():
                Line((-3.45, 5.25), (-3.45, 1.75))
                Line((-3.45, 1.75), (3.8, 1.75))
                Line((3.8, 1.75), (3.8, 5.25))
                Line((3.8, 5.25), (-3.45, 5.25))
            make_face()
        # OneSide extrude, distance=-8.5
        extrude(amount=-8.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((2.2, -0.6)):
                Circle(0.325)
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((-2.2, -0.6)):
                Circle(0.325)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.2, 2.735)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-2.2, 2.735)):
                Circle(0.2)
        # Start offset: -8.5 (not directly supported, may affect result)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_88941_aa581346_0002():
    """Model: Roller (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6345133402, perimeter: 5.08495561
            with BuildLine():
                CenterArc((0, 0), 0.6, -90, 180)
                Line((0, -0.6000000089), (1, -0.6000000089))
                Line((1, -0.6000000089), (1, 0.6000000089))
                Line((1, 0.6000000089), (0, 0.6000000089))
            make_face()
            # Profile area: 0.6345133402, perimeter: 5.08495561
            with BuildLine():
                CenterArc((0, 0), 0.6, 90, 180)
                Line((0, 0.6000000089), (-1, 0.6000000089))
                Line((-1, 0.6000000089), (-1, -0.6000000089))
                Line((-1, -0.6000000089), (0, -0.6000000089))
            make_face()
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.6, 90, 180)
                CenterArc((0, 0), 0.6, -90, 180)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2399999893, perimeter: 2.8000000119
            with BuildLine():
                Line((-1, -0.6000000089), (-0.8000000119, -0.6000000089))
                Line((-0.8000000119, 0.6000000089), (-0.8000000119, -0.6000000089))
                Line((-1, 0.6000000089), (-0.8000000119, 0.6000000089))
                Line((-1, -0.6000000089), (-1, 0.6000000089))
            make_face()
            # Profile area: 0.2399999964, perimeter: 2.8000000238
            with BuildLine():
                Line((0.8, 0.6000000089), (0.8000000119, -0.6000000089))
                Line((0.8000000119, -0.6000000089), (1, -0.6000000089))
                Line((1, -0.6000000089), (1, 0.6000000089))
                Line((1, 0.6000000089), (0.8, 0.6000000089))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.1, 0)):
                Circle(0.05)
        # OneSide extrude, distance=-2.9
        extrude(amount=-2.9, mode=Mode.SUBTRACT)
    return part.part


def model_88941_aa581346_0013():
    """Model: Stopper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 565.684, perimeter: 96.5684
            with BuildLine():
                Line((-20, 28.2842), (0, 28.2842))
                Line((-20, 0), (-20, 28.2842))
                Line((0, 0), (-20, 0))
                Line((0, 28.2842), (0, 0))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-20, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0075398224, perimeter: 1.5079644737
            with BuildLine():
                CenterArc((0.125, 28.4092), 0.125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.125, 28.4092), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0075398224, perimeter: 1.5079644737
            with BuildLine():
                CenterArc((-0.125, 28.4092), 0.125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.125, 28.4092), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 20, perimeter: 42
            with BuildLine():
                Line((0, 1), (0, 0))
                Line((0, 0), (20, 0))
                Line((20, 0), (20, 1))
                Line((20, 1), (0, 1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_89527_b3bf425d_0020():
    """Model: 17 v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.6659380702, perimeter: 12.2464533403
            with BuildLine():
                CenterArc((0.0055479705, 5.1), 0.25, 1.6230835786, 176.6291759146)
                Line((-0.2443357281, 5.107624774), (-0.3998139177, 0.0121996384))
                CenterArc((0, 0), 0.4, 178.2522594932, 183.3708240854)
                Line((0.2554476666, 5.107081091), (0.3998395139, 0.0113297455))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, 5.1)):
                Circle(0.1)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # TwoSides extrude, along=0.175, against=-0.025
        extrude(amount=0.175, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.025, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.175), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_89906_b50b1875_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.54), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            Circle(0.9525)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            Circle(0.9525)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.175), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9477835497, perimeter: 4.9473801109
            Circle(0.7874)
        # OneSide extrude, distance=-4.699
        extrude(amount=-4.699, mode=Mode.SUBTRACT)
    return part.part


def model_89992_07da02f7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50, perimeter: 30
            with BuildLine():
                Line((5, -2.5), (-5, -2.5))
                Line((5, 2.5), (5, -2.5))
                Line((-5, 2.5), (5, 2.5))
                Line((-5, -2.5), (-5, 2.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.2146018366, perimeter: 19.1415926536
            with BuildLine():
                Line((2, -2), (-2, -2))
                Line((2, 2), (2, -2))
                Line((-2, 2), (2, 2))
                Line((-2, -2), (-2, 2))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.79510336, perimeter: 13.7376
            with BuildLine():
                Line((1.7172, -1.7172), (-1.7172, -1.7172))
                Line((1.7172, 1.7172), (1.7172, -1.7172))
                Line((-1.7172, 1.7172), (1.7172, 1.7172))
                Line((-1.7172, -1.7172), (-1.7172, 1.7172))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_90113_74d0a198_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=18
        extrude(amount=18)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(18, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.0912614788, perimeter: 27.853981634
            with BuildLine():
                Line((2.5, -2.5), (-2.5, -2.5))
                Line((2.5, 2.5), (2.5, -2.5))
                Line((-2.5, 2.5), (2.5, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((20, 0)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.8584073464, perimeter: 24.2831853072
            with BuildLine():
                Line((22, -2.5), (18, -2.5))
                Line((22, 2.5), (22, -2.5))
                Line((18, 2.5), (22, 2.5))
                Line((18, -2.5), (18, 2.5))
            make_face()
            with BuildLine():
                CenterArc((20, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((20, 0)):
                Circle(1)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_91289_267aa864_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.5000000075, 0.8000000119)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.5495155742, 1.0169418847)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.6882551093, 1.190915759)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.8887395463, 1.2874639753)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((1.1112604835, 1.2874639753)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((1.3117449205, 1.190915759)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((1.4504844556, 1.0169418847)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((1.5000000224, 0.8000000119)):
                Circle(0.1000000015)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


def model_91291_d83b41ea_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 44.832458868, perimeter: 28.0076763871
            with BuildLine():
                CenterArc((-3.9966921027, 2.5329702703), 0.5, 176.1859251657, 15.1240073083)
                Line((-4.0803883865, 0.4019419324), (-4.4869824405, 2.4349122027))
                CenterArc((-3.5900980486, 0.5), 0.5, -168.690067526, 78.690067526)
                Line((0, 0), (-3.5900980486, 0))
                Line((0, 0), (0.4732004997, 9.4640099947))
                CenterArc((-0.0261756697, 9.4889788031), 0.5, -2.8624052261, 92.7035264602)
                Line((-3.5309235644, 9.9986992676), (-0.0247891927, 9.9889768808))
                CenterArc((-3.5323100414, 9.4987011899), 0.5, 89.841121234, 86.3448039317)
                Line((-4.4955846816, 2.5662297756), (-4.0312026203, 9.5319606952))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4)
    return part.part


def model_91395_590c8d97_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6726724435, perimeter: 2.9074131504
            with Locations((-0.8312901651, 0)):
                Circle(0.4627291745)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1470982777, perimeter: 1.3595923925
            with Locations((0.8312901651, 0)):
                Circle(0.2163858499)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_91407_0dc942cf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.1367318646, perimeter: 6.4750085354
            with BuildLine():
                Line((1, 2.2912878475), (1, 3.5))
                Line((1, 3.5), (-1, 3.5))
                Line((-1, 2.2912878475), (-1, 3.5))
                CenterArc((0, 0), 2.5, 66.4218215218, 47.1563569564)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5200000468, perimeter: 3.4000000954
            with BuildLine():
                Line((-0.5, 2.5), (0.5, 2.5))
                Line((0.5, 2.5), (0.5, 2.9000000432))
                Line((0.5, 2.9000000432), (0.200000003, 2.9000000432))
                Line((0.200000003, 2.9000000432), (0.200000003, 3.2000000477))
                Line((0.200000003, 3.2000000477), (-0.200000003, 3.2000000477))
                Line((-0.200000003, 3.2000000477), (-0.200000003, 2.9000000432))
                Line((-0.5, 2.9000000432), (-0.200000003, 2.9000000432))
                Line((-0.5, 2.5), (-0.5, 2.9000000432))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 8.926990817
            with BuildLine():
                Line((0, 0), (1.767766953, 1.767766953))
                Line((0, 0), (1.767766953, -1.767766953))
                CenterArc((0, 0), 2.5, -45, 90)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)
    return part.part


def model_91457_9b6cdf83_0000():
    """Model: socket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)
    return part.part


def model_93674_f9477292_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70.1764132241, perimeter: 120.4914389462
            with BuildLine():
                CenterArc((0, 0), 11.1803398875, -63.4349488229, 243.4349488229)
                Line((-11.1803398875, 0), (-11.1803398875, -14))
                Line((-11.1803398875, -14), (-9.9919591874, -14))
                Line((-9.9919591874, 0), (-9.9919591874, -14))
                CenterArc((0, 0), 9.9919591874, -64.2875731744, 244.2875731744)
                Line((5, -10), (4.3350565382, -9.0025848073))
            make_face()
        # TwoSides extrude (symmetric), distance=2.5
        extrude(amount=2.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.2000000358, perimeter: 8.6000001281
            with BuildLine():
                Line((-10.7000001594, -2.0000000298), (-11.0000001639, -2.0000000298))
                Line((-10.7000001594, 2.0000000298), (-10.7000001594, -2.0000000298))
                Line((-11.0000001639, 2.0000000298), (-10.7000001594, 2.0000000298))
                Line((-11.0000001639, -2.0000000298), (-11.0000001639, 2.0000000298))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5014477131, perimeter: 8.1563287853
            with BuildLine():
                Line((-10.7140877438, -1.9749197078), (-10.8409961797, -1.9749197078))
                Line((-10.7140877438, 1.976336249), (-10.7140877438, -1.9749197078))
                Line((-10.8409961797, 1.976336249), (-10.7140877438, 1.976336249))
                Line((-10.8409961797, -1.9749197078), (-10.8409961797, 1.976336249))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.1538461538, 0, 0.7692307692), x_dir=(0.5547001962, 0, 0.8320502943), z_dir=(-0.8320502943, 0, 0.5547001962))):
            # Profile area: 2.0000000596, perimeter: 9.0000001341
            with BuildLine():
                Line((11.0000001639, -2.0000000298), (10.5000001565, -2.0000000298))
                Line((11.0000001639, 2.0000000298), (11.0000001639, -2.0000000298))
                Line((10.5000001565, 2.0000000298), (11.0000001639, 2.0000000298))
                Line((10.5000001565, -2.0000000298), (10.5000001565, 2.0000000298))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_93676_4f934980_0000():
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=27
        extrude(amount=27)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=-35
        extrude(amount=-35, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


def model_94137_7901e233_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7, perimeter: 19.3082039325
            with BuildLine():
                Line((9, 1.5), (9, 1.8))
                Line((9, 1.8), (6, 1.8))
                Line((6, 1.8), (3, 0.3))
                Line((3, 0.3), (0, 0.3))
                Line((0, 0.3), (0, 0))
                Line((0, 0), (3, 0))
                Line((6, 1.5), (3, 0))
                Line((6, 1.5), (9, 1.5))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((-0.9293317342, 0.6)):
                Circle(0.175)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.4064435496, perimeter: 3.6128315516
            with BuildLine():
                CenterArc((-0.9293317342, 0.6), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.9293317342, 0.6), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.4, against=-0.7
        extrude(amount=0.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-8.1320281947, 0.6)):
                Circle(0.3)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.8482300165, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((-8.1320281947, 0.6), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.1320281947, 0.6), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-8.1320281947, 0.6)):
                Circle(0.3)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_95699_8ce2351e_0000():
    """Model: bird 2 wings v2"""
    with BuildPart() as part:
        # Sketch8 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.1276375558, perimeter: 15.2985812744
            with BuildLine():
                CenterArc((0.2052025064, -5.131349919), 4.2798340052, -129.5962086398, 79.1924172795)
                Line((0.5309160167, -4.8870647862), (2.933053155, -8.4291992107))
                Line((-0.486938703, -4.8870647862), (0.5309160167, -4.8870647862))
                Line((-2.5226481423, -8.4291992107), (-0.486938703, -4.8870647862))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch11 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.8007218478, perimeter: 23.5064694396
            with BuildLine():
                CenterArc((4.4777782526, 3.3142885106), 6.6207083109, -91.5468538682, 103.8076077595)
                Line((6.2444227532, 2.1842379838), (10.9474765852, 4.7202693158))
                Line((4.4537832692, 0.1515660047), (6.2444227532, 2.1842379838))
                Line((4.2990561148, -3.304007111), (4.4537832692, 0.1515660047))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_96269_56363b24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # Symmetric extrude, each_side=0.9525
        extrude(amount=0.9525, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9525, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.9525, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.7625, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.7475383354, perimeter: 9.7737621469
            with BuildLine():
                Line((-0.635, 1.7960512242), (-0.635, -1.7960512242))
                CenterArc((0, 0), 1.905, -109.4712206345, 38.942441269)
                Line((0.635, -1.7960512242), (0.635, 1.7960512242))
                CenterArc((0, 0), 1.905, 70.5287793655, 38.942441269)
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_97250_82e8ae78_0000():
    """Model: Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3067961576, perimeter: 1.9634954085
            Circle(0.3125)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4786020058, perimeter: 5.1050880621
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3067961576, perimeter: 1.9634954085
            Circle(0.3125)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
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

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1809557368, perimeter: 1.5079644737
            with Locations((0, 9.43)):
                Circle(0.24)
        # Symmetric extrude, each_side=2.1
        extrude(amount=2.1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_98389_45ecb862_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 57.5539619013, perimeter: 38.7438052292
            with BuildLine():
                Line((9.238979698, 1.8337695102), (6.1179317411, 10.5))
                Line((6.1179317411, 10.5), (3.0319051636, 3.8))
                Line((3.0319051636, 3.8), (1.2821857758, 5.0129571976))
                Line((1.2821857758, 5.0129571976), (0, 4))
                Line((0, 4), (0, 0))
                Line((0, 0), (11.0743453492, 0))
                Line((10.032026317, 2.2081187535), (11.0743453492, 0))
                Line((10.032026317, 2.2081187535), (9.238979698, 1.8337695102))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.4869978967, -1.0573097237), x_dir=(1, 0, 0), z_dir=(0, 0.4183560863, 0.9082830974))):
            # Profile area: 10.0522623298, perimeter: 13.0418098638
            with BuildLine():
                Line((-1.2989281344, 4.7198917485), (1.2010718656, 4.7198917485))
                Line((1.2010718656, 4.7198917485), (1.2010718656, 8.7407966804))
                Line((1.2010718656, 8.7407966804), (-1.2989281344, 8.7407966804))
                Line((-1.2989281344, 8.7407966804), (-1.2989281344, 4.7198917485))
            make_face()
            # Profile area: 2.5936386224, perimeter: 7.0749108979
            with BuildLine():
                Line((-1.2989281344, 3.6824362996), (1.2010718656, 3.6824362996))
                Line((1.2010718656, 3.6824362996), (1.2010718656, 4.7198917485))
                Line((-1.2989281344, 4.7198917485), (1.2010718656, 4.7198917485))
                Line((-1.2989281344, 4.7198917485), (-1.2989281344, 3.6824362996))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.9861792133, -2.7633372538), x_dir=(-1, 0, 0), z_dir=(0, 0.8218374642, -0.569722022))):
            # Profile area: 1.04, perimeter: 10.8
            with BuildLine():
                Line((2.6, 1.3000000224), (-2.6, 1.3000000224))
                Line((2.6, 1.5000000224), (2.6, 1.3000000224))
                Line((-2.6, 1.5000000224), (2.6, 1.5000000224))
                Line((-2.6, 1.3000000224), (-2.6, 1.5000000224))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.0668539844, -0.9756364966), x_dir=(1, 0, 0), z_dir=(0, 0.9043124763, 0.4268711108))):
            # Profile area: 0.1592604333, perimeter: 3.3852086663
            with BuildLine():
                Line((-1.2871430941, 9.8546221559), (-1.2871430941, 9.7546221559))
                Line((-2.8797474272, 9.8546221559), (-1.2871430941, 9.8546221559))
                Line((-2.8797474272, 9.7546221559), (-2.8797474272, 9.8546221559))
                Line((-1.2871430941, 9.7546221559), (-2.8797474272, 9.7546221559))
            make_face()
            # Profile area: 0.1592604333, perimeter: 3.3852086663
            with BuildLine():
                Line((1.2798166078, 9.7546221559), (1.2798166078, 9.8546221559))
                Line((2.8724209409, 9.7546221559), (1.2798166078, 9.7546221559))
                Line((2.8724209409, 9.8546221559), (2.8724209409, 9.7546221559))
                Line((1.2798166078, 9.8546221559), (2.8724209409, 9.8546221559))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_98960_39ac72ce_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.15, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.0137444679, perimeter: 1.0995574288
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.225, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0162640728, perimeter: 0.674356888
            with BuildLine():
                CenterArc((0, 0), 0.075, 41.8103137503, 96.3793724994)
                Line((0.0559017004, 0.0499999989), (0.1199999973, 0.0499999989))
                Line((0.1199999973, 0.1199999973), (0.1199999973, 0.0499999989))
                Line((-0.1399999969, 0.1199999973), (0.1199999973, 0.1199999973))
                Line((-0.1399999969, 0.0499999989), (-0.1399999969, 0.1199999973))
                Line((-0.1399999969, 0.0499999989), (-0.0559017004, 0.0499999989))
            make_face()
            # Profile area: 0.0019359264, perimeter: 0.2379637045
            with BuildLine():
                Line((-0.0559017004, 0.0499999989), (0.0559017004, 0.0499999989))
                CenterArc((0, 0), 0.075, 41.8103137503, 96.3793724994)
            make_face()
        # OneSide extrude, distance=-0.187
        extrude(amount=-0.187, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.0499999989), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0011341149, perimeter: 0.1193805208
            with Locations((0.075, 0)):
                Circle(0.019)
        # OneSide extrude, distance=-0.088
        extrude(amount=-0.088, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_62281_fbc75133_0000": {"func": model_62281_fbc75133_0000, "volume": 75.3176099862, "area": 307.1050390339},
    "model_63132_330141d7_0010": {"func": model_63132_330141d7_0010, "volume": 4.9095940425, "area": 18.6643785718},
    "model_65211_73eab9de_0000": {"func": model_65211_73eab9de_0000, "volume": 201.4160400424, "area": 257.5088484104},
    "model_65532_72eb1a5e_0004": {"func": model_65532_72eb1a5e_0004, "volume": 20.7992775445, "area": 65.0290167369},
    "model_65813_123f1f95_0000": {"func": model_65813_123f1f95_0000, "volume": 24.7131084073, "area": 111.8928376689},
    "model_65827_d1469ad6_0002": {"func": model_65827_d1469ad6_0002, "volume": 2.4282844335, "area": 44.4972900686},
    "model_66226_49fc804a_0000": {"func": model_66226_49fc804a_0000, "volume": 0.505575207, "area": 11.0170792015},
    "model_66331_6ff90f6b_0000": {"func": model_66331_6ff90f6b_0000, "volume": 10368364.6959846243, "area": 1469978.0243940526},
    "model_66762_5098cf7d_0000": {"func": model_66762_5098cf7d_0000, "volume": 2.4620467764, "area": 11.0756960397},
    "model_67207_15bfd1aa_0000": {"func": model_67207_15bfd1aa_0000, "volume": 157.8650308429, "area": 196.3495408494},
    "model_67262_f7710fc0_0000": {"func": model_67262_f7710fc0_0000, "volume": 94.1415926044, "area": 247.8407043984},
    "model_67378_1f022261_0000": {"func": model_67378_1f022261_0000, "volume": 602.6522880684, "area": 680.3761565999},
    "model_67567_e5be20ab_0000": {"func": model_67567_e5be20ab_0000, "volume": 4996.2586114654, "area": 2249.7983734818},
    "model_67572_05561813_0000": {"func": model_67572_05561813_0000, "volume": 5.2474535574, "area": 24.7662705377},
    "model_68939_82bcae5a_0000": {"func": model_68939_82bcae5a_0000, "volume": 183.2, "area": 392.6},
    "model_69255_6e76c12f_0000": {"func": model_69255_6e76c12f_0000, "volume": 2.6518264348, "area": 25.6372890882},
    "model_69454_807423c7_0000": {"func": model_69454_807423c7_0000, "volume": 14.8246509168, "area": 78.0744995922},
    "model_69800_f99575cb_0000": {"func": model_69800_f99575cb_0000, "volume": 28.6394674139, "area": 92.2498520597},
    "model_71422_338eb6ff_0000": {"func": model_71422_338eb6ff_0000, "volume": 36.1635155971, "area": 91.3795573733},
    "model_73388_10a40b49_0026": {"func": model_73388_10a40b49_0026, "volume": 1.2784604778, "area": 11.6738270228},
    "model_73764_0bd59074_0000": {"func": model_73764_0bd59074_0000, "volume": 4730.8333372608, "area": 9514.5053787609},
    "model_76300_7cb02add_0000": {"func": model_76300_7cb02add_0000, "volume": 0.1249002264, "area": 4.1461745765},
    "model_78102_5458aba8_0000": {"func": model_78102_5458aba8_0000, "volume": 1229.3686899233, "area": 1026.9016338366},
    "model_78433_1f73539f_0000": {"func": model_78433_1f73539f_0000, "volume": 5834.4855486098, "area": 3619.1923828414},
    "model_78861_0f81caaa_0000": {"func": model_78861_0f81caaa_0000, "volume": 178.3332403841, "area": 352.2887941242},
    "model_78978_24711a0f_0000": {"func": model_78978_24711a0f_0000, "volume": 11843.9084370777, "area": 8422.7646392417},
    "model_78980_e36c37a8_0000": {"func": model_78980_e36c37a8_0000, "volume": 2382.4114103904, "area": 1503.0640974694},
    "model_79530_946fa2d1_0000": {"func": model_79530_946fa2d1_0000, "volume": 128.4921241133, "area": 270.6785186942},
    "model_80193_e198f23e_0000": {"func": model_80193_e198f23e_0000, "volume": 16.1865839473, "area": 105.9068697296},
    "model_80331_b436d0d5_0000": {"func": model_80331_b436d0d5_0000, "volume": 18.911802659, "area": 88.1955037597},
    "model_80471_4a6e9e76_0000": {"func": model_80471_4a6e9e76_0000, "volume": 29.8548200516, "area": 88.6872621516},
    "model_80472_01f15238_0000": {"func": model_80472_01f15238_0000, "volume": 293.2480392585, "area": 389.9501881268},
    "model_80589_b85b71c6_0000": {"func": model_80589_b85b71c6_0000, "volume": 0.625, "area": 13.5},
    "model_80785_5b40ac2b_0000": {"func": model_80785_5b40ac2b_0000, "volume": 73.2159805933, "area": 257.2152410825},
    "model_81025_dc67f73b_0000": {"func": model_81025_dc67f73b_0000, "volume": 632.2590949617, "area": 627.9937920241},
    "model_81145_d4ae4770_0000": {"func": model_81145_d4ae4770_0000, "volume": 3.0034844614, "area": 57.6686520449},
    "model_81821_3f648668_0000": {"func": model_81821_3f648668_0000, "volume": 109.0749373941, "area": 310.3198478539},
    "model_81926_1a4f5935_0000": {"func": model_81926_1a4f5935_0000, "volume": 45.3203528077, "area": 125.8273196141},
    "model_83111_3ad0d7a8_0000": {"func": model_83111_3ad0d7a8_0000, "volume": 41.7101761242, "area": 188.0582826574},
    "model_83212_f8e72ef2_0000": {"func": model_83212_f8e72ef2_0000, "volume": 14310.6561413245, "area": 10988.3131864289},
    "model_83224_833dcf1f_0000": {"func": model_83224_833dcf1f_0000, "volume": 14185.483309033, "area": 10978.4957093864},
    "model_83259_487d379e_0002": {"func": model_83259_487d379e_0002, "volume": 47.2705438537, "area": 261.5112132894},
    "model_83383_73ed7877_0000": {"func": model_83383_73ed7877_0000, "volume": 46.5236590767, "area": 121.9620211424},
    "model_83400_6db148a7_0000": {"func": model_83400_6db148a7_0000, "volume": 58.9383469411, "area": 127.2099349059},
    "model_84025_ec3401ea_0011": {"func": model_84025_ec3401ea_0011, "volume": 300.9881381588, "area": 618.5795934918},
    "model_84025_ec3401ea_0012": {"func": model_84025_ec3401ea_0012, "volume": 28.4357537997, "area": 90.4819043319},
    "model_85093_6c657024_0000": {"func": model_85093_6c657024_0000, "volume": 72.8722100226, "area": 755.6424530777},
    "model_86702_c06b5954_0000": {"func": model_86702_c06b5954_0000, "volume": 43.0078699221, "area": 113.1870957636},
    "model_87358_854d47fe_0005": {"func": model_87358_854d47fe_0005, "volume": 352.0084780755, "area": 380.1684780755},
    "model_88396_5f13c951_0001": {"func": model_88396_5f13c951_0001, "volume": 81.8099899628, "area": 128.0351220701},
    "model_88680_0fb9b042_0001": {"func": model_88680_0fb9b042_0001, "volume": 124.3033071029, "area": 280.7458176948},
    "model_88941_aa581346_0002": {"func": model_88941_aa581346_0002, "volume": 1.9438317492, "area": 16.0241590763},
    "model_88941_aa581346_0013": {"func": model_88941_aa581346_0013, "volume": 151.4963982237, "area": 1191.6199040267},
    "model_89527_b3bf425d_0020": {"func": model_89527_b3bf425d_0020, "volume": 0.5200455803, "area": 9.2159680314},
    "model_89906_b50b1875_0000": {"func": model_89906_b50b1875_0000, "volume": 9.0691061987, "area": 52.9570120554},
    "model_89992_07da02f7_0000": {"func": model_89992_07da02f7_0000, "volume": 34.3655658667, "area": 176.3736728747},
    "model_90113_74d0a198_0000": {"func": model_90113_74d0a198_0000, "volume": 271.4988860358, "area": 383.3716694115},
    "model_91289_267aa864_0000": {"func": model_91289_267aa864_0000, "volume": 0.0050265484, "area": 0.603185806},
    "model_91291_d83b41ea_0000": {"func": model_91291_d83b41ea_0000, "volume": 179.3298354721, "area": 201.6956232845},
    "model_91395_590c8d97_0000": {"func": model_91395_590c8d97_0000, "volume": 32.9628916225, "area": 80.0738561031},
    "model_91407_0dc942cf_0000": {"func": model_91407_0dc942cf_0000, "volume": 81.7147369076, "area": 145.3899578682},
    "model_91457_9b6cdf83_0000": {"func": model_91457_9b6cdf83_0000, "volume": 9.1420346219, "area": 54.1610573479},
    "model_93674_f9477292_0001": {"func": model_93674_f9477292_0001, "volume": 351.5298945926, "area": 776.7445146806},
    "model_93676_4f934980_0000": {"func": model_93676_4f934980_0000, "volume": 2043.6060211602, "area": 2148.8493750554},
    "model_94137_7901e233_0000": {"func": model_94137_7901e233_0000, "volume": 4.9500081513, "area": 38.9488814483},
    "model_95699_8ce2351e_0000": {"func": model_95699_8ce2351e_0000, "volume": 29.8243240714, "area": 117.9605380523},
    "model_96269_56363b24_0000": {"func": model_96269_56363b24_0000, "volume": 119.4567335125, "area": 167.9815958227},
    "model_97250_82e8ae78_0000": {"func": model_97250_82e8ae78_0000, "volume": 8.1624361821, "area": 36.5199467948},
    "model_98389_45ecb862_0000": {"func": model_98389_45ecb862_0000, "volume": 330.103675194, "area": 373.365283718},
    "model_98960_39ac72ce_0000": {"func": model_98960_39ac72ce_0000, "volume": 0.0070401926, "area": 0.2583386888},
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
