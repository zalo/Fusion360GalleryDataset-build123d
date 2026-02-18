"""Batch 014 - passing/03_4to5ops
121 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_55611_69142616_0002():
    """Model: bearing 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((31.6918316342, 98.5082553947)):
                Circle(1.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((31.6918316342, -98.5082553947)):
                Circle(0.75)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


def model_55611_69142616_0003():
    """Model: bearing 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3014376029, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((37.5, 87.5), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((37.5, 87.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((-37.5, -87.5), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-37.5, -87.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.3014376029, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((-37.5, -87.5), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-37.5, -87.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_55611_69142616_0006():
    """Model: mounting bracket 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 21 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.101782682, perimeter: 14.4051579097
            with BuildLine():
                CenterArc((-12, 0), 1.2999998406, 22.0243151467, 144.6333193896)
                Line((-13.2649109002, 0.3), (-14.9, 0.3))
                CenterArc((-14.9, 0.2), 0.1, 90, 90)
                Line((-15, 0.2), (-15, 0))
                Line((-15, 0), (-13.1832157904, 0))
                CenterArc((-13.1832157904, 0.2), 0.2, -90, 80.4059304503)
                CenterArc((-12, 0), 0.9999998361, 9.5940695497, 160.8118609005)
                CenterArc((-10.8167842096, 0.2), 0.2, -170.4059304503, 80.4059304503)
                Line((-10.8167842096, 0), (-9, 0))
                Line((-9, 0), (-9, 0.2))
                CenterArc((-9.1, 0.2), 0.1, 0, 90)
                Line((-9.1, 0.3), (-10.5167604746, 0.3))
                CenterArc((-10.5167604746, 0.6), 0.3, -157.9756848533, 67.9756848533)
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.0606601718, 10.0606601718)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-4.9393398282, 10.0606601718)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.0606601718, 13.9393398282)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-4.9393398282, 13.9393398282)):
                Circle(0.3)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_55633_282eaae6_0007():
    """Model: sumbu1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1178097245, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_55636_6180bfce_0002():
    """Model: mesa"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3848.4510006475, perimeter: 219.9114857513
            Circle(35)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((-13.7990381057, 20.9006350946), (-11.2009618943, 22.4006350946))
                Line((-11.2009618943, 22.4006350946), (-12.7009618943, 24.998711306))
                Line((-12.7009618943, 24.998711306), (-15.2990381057, 23.498711306))
                Line((-15.2990381057, 23.498711306), (-13.7990381057, 20.9006350946))
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((28, -1.5), (25, -1.5))
                Line((28, 1.5), (28, -1.5))
                Line((25, 1.5), (28, 1.5))
                Line((25, -1.5), (25, 1.5))
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((-15.2990381057, -23.498711306), (-13.7990381057, -20.9006350946))
                Line((-12.7009618943, -24.998711306), (-15.2990381057, -23.498711306))
                Line((-11.2009618943, -22.4006350946), (-12.7009618943, -24.998711306))
                Line((-13.7990381057, -20.9006350946), (-11.2009618943, -22.4006350946))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_55636_6180bfce_0005():
    """Model: tuerca"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7942286341, perimeter: 10.3923048454
            with BuildLine():
                Line((1.5, -0.8660254038), (1.5, 0.8660254038))
                Line((1.5, 0.8660254038), (0, 1.7320508076))
                Line((0, 1.7320508076), (-1.5, 0.8660254038))
                Line((-1.5, 0.8660254038), (-1.5, -0.8660254038))
                Line((-1.5, -0.8660254038), (0, -1.7320508076))
                Line((0, -1.7320508076), (1.5, -0.8660254038))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_55707_c78416ed_0024():
    """Model: Chromed Rod Holder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.7473451754, perimeter: 16.5132741229
            with BuildLine():
                Line((-2.5, 0), (2.5, 0))
                Line((2.5, 0), (2.5, 0.75))
                Line((2.5, 0.75), (1, 0.75))
                Line((1, 0.75), (1, 2))
                Line((1, 2), (-1, 2))
                Line((-1, 0.75), (-1, 2))
                Line((-2.5, 0.75), (-1, 0.75))
                Line((-2.5, 0), (-2.5, 0.75))
            make_face()
            with BuildLine():
                CenterArc((0, 1.2), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.81), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0, 1.2)):
                Circle(0.4)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)
    return part.part


def model_55715_525d1d3e_0003():
    """Model: Motor Shaft Adapter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.794), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.8241469248, perimeter: 4.7877872041
            Circle(0.762)
        # OneSide extrude, distance=2.794
        extrude(amount=2.794)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.588), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0476092803, perimeter: 3.81
            with BuildLine():
                Line((0.5499261314, 0.3175), (0, 0.635))
                Line((0, 0.635), (-0.5499261314, 0.3175))
                Line((-0.5499261314, 0.3175), (-0.5499261314, -0.3175))
                Line((-0.5499261314, -0.3175), (0, -0.635))
                Line((0, -0.635), (0.5499261314, -0.3175))
                Line((0.5499261314, -0.3175), (0.5499261314, 0.3175))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


def model_55715_525d1d3e_0006():
    """Model: Motor Box"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.254), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.4516004118, perimeter: 10.1600003242
            with BuildLine():
                Line((1.2700000405, -1.2700000405), (1.2700000405, 1.2700000405))
                Line((1.2700000405, 1.2700000405), (-1.2700000405, 1.2700000405))
                Line((-1.2700000405, 1.2700000405), (-1.2700000405, -1.2700000405))
                Line((-1.2700000405, -1.2700000405), (1.2700000405, -1.2700000405))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.334), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.8241469248, perimeter: 4.7877872041
            Circle(0.762)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


def model_55715_525d1d3e_0007():
    """Model: Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3579067176, perimeter: 4.3420776189
            with BuildLine():
                Line((-0.2309401077, -0.4), (0.2309401077, -0.4))
                Line((0.2309401077, -0.4), (0.4618802154, 0))
                Line((0.4618802154, 0), (0.2309401077, 0.4))
                Line((0.2309401077, 0.4), (-0.2309401077, 0.4))
                Line((-0.2309401077, 0.4), (-0.4618802154, 0))
                Line((-0.4618802154, 0), (-0.2309401077, -0.4))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


def model_55752_a77535b1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 900, perimeter: 120
            with BuildLine():
                Line((-15, 15), (15, 15))
                Line((-15, 15), (-15, -15))
                Line((15, -15), (-15, -15))
                Line((15, 15), (15, -15))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_55756_070bfb3e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.8495559215, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.4511891032, perimeter: 10.424448245
            with BuildLine():
                CenterArc((4.9862572368, -6.2520350684), 1.25, -89.9999982861, 179.9416793397)
                Line((4.9875295587, -5.002035716), (2.9875295588, -5))
                Line((2.9875295588, -5), (2.9875295588, -7.5))
                Line((2.9875295588, -7.5), (4.9862572742, -7.5020350684))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.ADD)
    return part.part


def model_55767_a6177f06_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 59.5893233456, perimeter: 29.280972451
            with BuildLine():
                CenterArc((-1.25, -2.5), 3.75, 180, 180)
                Line((2.5, -2.5), (2.5, 2.5))
                Line((2.5, 2.5), (-5, 2.5))
                Line((-5, 2.5), (-5, -2.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((-1.25, -2.5)):
                Circle(1.6)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_55786_39249e3d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.5, perimeter: 17
            with BuildLine():
                Line((5.5, -4), (0.5, -4))
                Line((5.5, -0.5), (5.5, -4))
                Line((0.5, -0.5), (5.5, -0.5))
                Line((0.5, -4), (0.5, -0.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8105637508, perimeter: 8.9977871438
            with BuildLine():
                Line((-5.5, 4), (-5.5, 0.5))
                CenterArc((-5.5, 2.25), 1.75, -90, 180)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_55788_c93cc797_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 120.9955742876, perimeter: 90.5575191895
            with BuildLine():
                Line((0, 0), (25, 0))
                Line((25, 0), (25, 2))
                Line((25, 2), (17.5, 2))
                Line((17.5, 2), (17.5, 8))
                CenterArc((12.5, 8), 5, 0, 180)
                Line((7.5, 2), (7.5, 8))
                Line((0, 2), (7.5, 2))
                Line((0, 0), (0, 2))
            make_face()
            with BuildLine():
                CenterArc((12.5, 8), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-21.25, 17)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-21.25, 3)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-3.75, 17)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-3.75, 3)):
                Circle(1)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


def model_55789_3be2e914_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 68.3746368021, perimeter: 34.187318401
            with BuildLine():
                CenterArc((0, 0), 4, 90, 270)
                Line((4, 0), (7.6688812397, 0))
                Line((7.6688812397, 0), (7.6688812397, 4))
                Line((7.6688812397, 4), (0, 4))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((-3, 4), (-1, 4))
                Line((-3, 1), (-3, 4))
                Line((-1, 1), (-3, 1))
                Line((-1, 4), (-1, 1))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_55834_09fd959e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.8564064606, perimeter: 13.8564064606
            with BuildLine():
                Line((-3.6547005384, 0.5), (-1.3452994616, 0.5))
                Line((-1.3452994616, 0.5), (-0.1905989232, 2.5))
                Line((-0.1905989232, 2.5), (-1.3452994616, 4.5))
                Line((-1.3452994616, 4.5), (-3.6547005384, 4.5))
                Line((-3.6547005384, 4.5), (-4.8094010768, 2.5))
                Line((-4.8094010768, 2.5), (-3.6547005384, 0.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-2.5, 2.5)):
                Circle(1.25)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_55838_a1513314_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 64.9519052838, perimeter: 30
            with BuildLine():
                Line((-3.5, 1.5), (-8.5, 1.5))
                Line((-8.5, 1.5), (-11, -2.8301270189))
                Line((-11, -2.8301270189), (-8.5, -7.1602540378))
                Line((-8.5, -7.1602540378), (-3.5, -7.1602540378))
                Line((-3.5, -7.1602540378), (-1, -2.8301270189))
                Line((-1, -2.8301270189), (-3.5, 1.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.1327412287, perimeter: 17.7715317526
            with Locations((-6, -3)):
                Circle(2.8284271247)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_55852_4f1a2c5b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((2.5, -2.5), (-2.5, -2.5))
                Line((2.5, 2.5), (2.5, -2.5))
                Line((-2.5, 2.5), (2.5, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 22 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2125293655, perimeter: 1.683959999
            with Locations((-1.7410835905, 1.466272151)):
                Ellipse(0.3181058399, 0.2126656906, rotation=57.094757077)
            # Profile area: 1.0381949717, perimeter: 3.7852737199
            with Locations((-0.7042151657, 0.7278961515)):
                Ellipse(0.74017272, 0.446473795, rotation=-17.9324737795)
            # Profile area: 0.7237919163, perimeter: 3.241629548
            with Locations((1, 1)):
                Ellipse(0.6580890916, 0.350089563, rotation=-57.4772301047)
            # Profile area: 1.0483009802, perimeter: 4.5205982413
            with Locations((-0.7042151657, -1.0316381451)):
                Ellipse(1.0211582971, 0.3267706551)
            # Profile area: 0.5935568333, perimeter: 3.0470416799
            with Locations((1.7936951304, -1.660043251)):
                Ellipse(0.6433031688, 0.2936951304, rotation=-90)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_55884_8d78f117_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.420321364, perimeter: 27.0907762642
            with BuildLine():
                CenterArc((-0.4613465856, -0.3161078457), 2.3898474177, 0, 360)
            make_face()
            with BuildLine():
                Line((1.5511404283, -0.3161078457), (0.5448969214, 1.4267570331))
                Line((0.5448969214, -2.0589727244), (1.5511404283, -0.3161078457))
                Line((-1.4675900925, -2.0589727244), (0.5448969214, -2.0589727244))
                Line((-2.4738335994, -0.3161078457), (-1.4675900925, -2.0589727244))
                Line((-1.4675900925, 1.4267570331), (-2.4738335994, -0.3161078457))
                Line((0.5448969214, 1.4267570331), (-1.4675900925, 1.4267570331))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.9878006128, perimeter: 17.9759860539
            with Locations((-2.8511940033, 0)):
                Ellipse(3.2399008168, 2.4549714386, rotation=62.0525893692)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.SUBTRACT)
    return part.part


def model_55887_a5ee694a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 500, perimeter: 90
            with BuildLine():
                Line((10, 0), (-10, 0))
                Line((10, 25), (10, 0))
                Line((-10, 25), (10, 25))
                Line((-10, 0), (-10, 25))
            make_face()
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(15, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 210.7836904424, perimeter: 51.466357687
            with Locations((0, 15)):
                Circle(8.1911252288)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_55927_f8b31711_0007():
    """Model: Conrod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6611725124, perimeter: 7.3274333882
            with BuildLine():
                CenterArc((0, 1.125), 0.45, 0, 180)
                Line((-0.45, 1.125), (-0.45, -1.125))
                CenterArc((0, -1.125), 0.45, 180, 180)
                Line((0.45, -1.125), (0.45, 1.125))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0, 1.125)):
                Circle(0.45)
        # Symmetric extrude, each_side=0.45
        extrude(amount=0.45, both=True, mode=Mode.ADD)
    return part.part


def model_55927_f8b31711_0009():
    """Model: Engine-Block v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7255391011, perimeter: 10.8842917353
            with BuildLine():
                Line((-1.125, 0), (1.125, 0))
                Line((1.125, 0), (1.125, 2.55))
                CenterArc((0, 2.55), 1.125, 0, 180)
                Line((-1.125, 0), (-1.125, 2.55))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


def model_55931_84bfa135_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.76, perimeter: 4.8566370614
            with BuildLine():
                CenterArc((1.9, -0.1), 0.1, -90, 90)
                Line((2, -0.1), (2, 0.1))
                CenterArc((1.9, 0.1), 0.1, 0, 90)
                Line((1.9, 0.2), (1.1, 0.2))
                CenterArc((1, 0.2), 0.1, 180, 180)
                Line((0.9, 0.2), (0.1, 0.2))
                CenterArc((0.1, 0.1), 0.1, 90, 90)
                Line((0, 0.1), (0, -0.1))
                CenterArc((0.1, -0.1), 0.1, 180, 90)
                Line((0.1, -0.2), (0.9, -0.2))
                CenterArc((1, -0.2), 0.1, 0, 180)
                Line((1.1, -0.2), (1.9, -0.2))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


def model_56036_b04a363c_0001():
    """Model: prt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 32 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 80.3957167102, perimeter: 90.2718502679
            with BuildLine():
                CenterArc((-3.25, -2.9577798247), 1.5, -180, 90)
                Line((8.7006633882, -4.4577798247), (-3.25, -4.4577798247))
                CenterArc((8.7006633882, -2.9577798247), 1.5, -90, 90)
                Line((10.2006633882, 6.25), (10.2006633882, -2.9577798247))
                CenterArc((8.7006633882, 6.25), 1.5, 0, 90)
                Line((-3.25, 7.75), (8.7006633882, 7.75))
                CenterArc((-3.25, 6.25), 1.5, 90, 90)
                Line((-4.75, -2.9577798247), (-4.75, 6.25))
            make_face()
            with BuildLine():
                Line((-1.6430924155, 5.4096115447), (7.5, 5.4096115447))
                CenterArc((7.5, 3.9096115447), 1.5, 0, 90)
                Line((9, -1.5), (9, 3.9096115447))
                CenterArc((7.5, -1.5), 1.5, -90, 90)
                Line((-1.6430924155, -3), (7.5, -3))
                CenterArc((-1.6430924155, -1.5), 1.5, 180, 90)
                Line((-3.1430924155, 3.9096115447), (-3.1430924155, -1.5))
                CenterArc((-1.6430924155, 3.9096115447), 1.5, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 100.187273637, perimeter: 38.5301858813
            with BuildLine():
                CenterArc((-1.6430924155, 3.9096115447), 1.5, 90, 90)
                Line((-3.1430924155, 3.9096115447), (-3.1430924155, -1.5))
                CenterArc((-1.6430924155, -1.5), 1.5, 180, 90)
                Line((-1.6430924155, -3), (7.5, -3))
                CenterArc((7.5, -1.5), 1.5, -90, 90)
                Line((9, -1.5), (9, 3.9096115447))
                CenterArc((7.5, 3.9096115447), 1.5, 0, 90)
                Line((-1.6430924155, 5.4096115447), (7.5, 5.4096115447))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 72.4855931234, perimeter: 113.1664423474
            with BuildLine():
                CenterArc((-4.5, -4.5), 1.5, 180, 90)
                Line((9.5, -6), (-4.5, -6))
                CenterArc((9.5, -4.5), 1.5, -90, 90)
                Line((11, 7.5), (11, -4.5))
                CenterArc((9.5, 7.5), 1.5, 0, 90)
                Line((-4.5, 9), (9.5, 9))
                CenterArc((-4.5, 7.5), 1.5, 90, 90)
                Line((-6, -4.5), (-6, 7.5))
            make_face()
            with BuildLine():
                CenterArc((-3.25, 6.25), 1.5, 90, 90)
                Line((8.7006633882, 7.75), (-3.25, 7.75))
                CenterArc((8.7006633882, 6.25), 1.5, 0, 90)
                Line((10.2006633882, -2.9577798247), (10.2006633882, 6.25))
                CenterArc((8.7006633882, -2.9577798247), 1.5, -90, 90)
                Line((-3.25, -4.4577798247), (8.7006633882, -4.4577798247))
                CenterArc((-3.25, -2.9577798247), 1.5, -180, 90)
                Line((-4.75, 6.25), (-4.75, -2.9577798247))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


def model_56065_00bbe5da_0002():
    """Model: Flywheel_Shaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, each_side=2.6
        extrude(amount=2.6, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.1000000045, perimeter: 2.2000000089
            with BuildLine():
                Line((-2.6, 0.3000000045), (-1.6, 0.3000000045))
                Line((-2.6, 0.2), (-2.6, 0.3000000045))
                Line((-1.6, 0.2), (-2.6, 0.2))
                Line((-1.6, 0.3000000045), (-1.6, 0.2))
            make_face()
        # TwoSides extrude, along=1.1, against=-0.7
        extrude(amount=1.1, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_56065_00bbe5da_0008():
    """Model: Heat_Exchange_Cylinder_Head v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.0446616728, perimeter: 11.780972451
            Circle(1.875)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.05), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 10.4634670319, perimeter: 11.4668131856
            Circle(1.825)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_56065_00bbe5da_0009():
    """Model: Counterweight_A v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.7902646384, perimeter: 19.6805298797
            with BuildLine():
                Line((-2.5, 0), (-0.6, 0))
                CenterArc((0, 0), 2.5, 180, 180)
                Line((0.6, 0), (2.5, 0))
                Line((0.6, 1.5), (0.6, 0))
                CenterArc((0, 1.5), 0.6, 0, 180)
                Line((-0.6, 0), (-0.6, 1.5))
            make_face()
            with BuildLine():
                CenterArc((0, 1.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # TwoSides offset extrude, full=2.6, trim=1.4
        extrude(amount=2.6, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=1.4, mode=Mode.ADD)
    return part.part


def model_56065_00bbe5da_0015():
    """Model: Heat_Exchange_Piston_Head v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.3482016398, perimeter: 10.8384946549
            Circle(1.725)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.05), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            Circle(1.7)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_56065_00bbe5da_0016():
    """Model: Counterweight_B v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.9866141793, perimeter: 18.1097335529
            with BuildLine():
                Line((-0.6, 0), (-2.5, 0))
                CenterArc((0, 0), 2.5, 180, 180)
                Line((0.6, 0), (2.5, 0))
                Line((0.6, 0), (0.6, 1.5))
                CenterArc((0, 1.5), 0.6, 0, 180)
                Line((-0.6, 0), (-0.6, 1.5))
            make_face()
            with BuildLine():
                CenterArc((0, 1.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # TwoSides offset extrude, full=2.6, trim=1.5
        extrude(amount=2.6, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=1.5, mode=Mode.ADD)
    return part.part


def model_56065_00bbe5da_0017():
    """Model: Heat_Exchange_Piston_Shaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, each_side=4.5
        extrude(amount=4.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.135000004, perimeter: 2.1000000089
            with BuildLine():
                Line((3.6, 0.15), (4.5, 0.15))
                Line((4.5, 0.15), (4.5, 0.3000000045))
                Line((3.6, 0.3000000045), (4.5, 0.3000000045))
                Line((3.6, 0.15), (3.6, 0.3000000045))
            make_face()
        # TwoSides extrude, along=0.8, against=-1
        extrude(amount=0.8, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_56065_00bbe5da_0021():
    """Model: Crankrod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.1782742736, perimeter: 19.3115038379
            with BuildLine():
                CenterArc((-3.1, 0), 0.6, 90, 180)
                Line((3.1, -0.6), (-3.1, -0.6))
                CenterArc((3.1, 0), 0.6, -90, 180)
                Line((-3.1, 0.6), (3.1, 0.6))
            make_face()
            with BuildLine():
                CenterArc((3.1, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.1, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2, 0)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1, 0)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1, 0)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2, 0)):
                Circle(0.3)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.1319560399, perimeter: 22.881400523
            with BuildLine():
                CenterArc((-2.7591379492, -0.400000006), 0.1, 146.5126622611, 123.4873377389)
                Line((2.7591379492, -0.500000006), (-2.7591379492, -0.500000006))
                CenterArc((2.7591379492, -0.400000006), 0.1, -90, 123.4873377389)
                CenterArc((3.1692408322, -0.00001938), 0.475, 131.8752570688, 94.6690128576)
                CenterArc((2.763555249, 0.400000006), 0.1, -27.6031297244, 117.6031297244)
                Line((-2.763555249, 0.500000006), (2.763555249, 0.500000006))
                CenterArc((-2.763555249, 0.400000006), 0.1, 90, 117.6031297244)
                CenterArc((-3.1692408322, -0.00001938), 0.475, -46.5442699264, 94.6690128576)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_56068_f346988c_0001():
    """Model: base cutting v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.25, perimeter: 34
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 5))
                Line((7.5, 5), (7, 5))
                Line((7, 5), (7, 0.5))
                Line((7, 0.5), (0.5, 0.5))
                Line((0.5, 5), (0.5, 0.5))
                Line((0, 5), (0.5, 5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.25, 4.7471485477)):
                Circle(0.125)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5, mode=Mode.ADD)
    return part.part


def model_56151_408ea220_0006():
    """Model: 3. Zewnetrzny pierscien lozyska"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4476767696, perimeter: 17.9070782565
            with BuildLine():
                CenterArc((0, 0), 1.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4000000209, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4476767696, perimeter: 17.9070782565
            with BuildLine():
                CenterArc((0, 0), 1.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4000000209, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4319691734, perimeter: 17.2787597258
            with BuildLine():
                CenterArc((0, 0), 1.4000000209, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_56151_408ea220_0007():
    """Model: 2. Wewetrzny pierscien lozyska"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.596902441, perimeter: 11.9380520805
            with BuildLine():
                CenterArc((0, 0), 0.9999999861, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9000000134, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3220134376, perimeter: 12.8805298906
            with BuildLine():
                CenterArc((0, 0), 1.0500000156, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9999999861, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.596902441, perimeter: 11.9380520805
            with BuildLine():
                CenterArc((0, 0), 0.9999999861, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9000000134, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_56320_6df1f5fe_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 77.5071361047, perimeter: 77.9159265359
            with BuildLine():
                Line((3.875, -6.7116968793), (7.75, 0))
                Line((7.75, 0), (3.875, 6.7116968793))
                Line((3.875, 6.7116968793), (-3.875, 6.7116968793))
                Line((-3.875, 6.7116968793), (-7.75, 0))
                Line((-7.75, 0), (-3.875, -6.7116968793))
                Line((-3.875, -6.7116968793), (3.875, -6.7116968793))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 34.3611696486, perimeter: 54.9778714378
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            Circle(3.75)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 34.3611696486, perimeter: 54.9778714378
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            Circle(3.75)
        # OneSide extrude, distance=22.5
        extrude(amount=22.5, mode=Mode.SUBTRACT)
    return part.part


def model_56324_4361f734_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 369.04510892, perimeter: 193.9437893941
            with BuildLine():
                Line((-7.4999254718, -13.1665647362), (-7.4778835029, -8.2222901759))
                CenterArc((0, -13.2), 7.5, 179.7445725536, 179.6955260083)
                Line((7.4996418989, -13.2732897604), (7.5496977711, -8.1511401597))
                CenterArc((12.549459037, -8.2), 5, 90, 89.440098562)
                Line((12.549459037, -3.2), (32.5, -3.2))
                Line((32.5, 0), (32.5, -3.2))
                Line((32.5, 0), (-32.5, 0))
                Line((-32.5, 0), (-32.5, -3.2))
                Line((-32.5, -3.2), (-12.4778338175, -3.2))
                CenterArc((-12.4778338175, -8.2), 5, -0.2554274464, 90.2554274464)
            make_face()
            with BuildLine():
                CenterArc((0, -13.2), 5.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


def model_56325_1ca40934_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.52, perimeter: 7.6
            with BuildLine():
                Line((2.2, 1.5731819618), (4.4, 1.5731819618))
                Line((4.4, 1.5731819618), (4.4, 3.1731819618))
                Line((4.4, 3.1731819618), (2.2, 3.1731819618))
                Line((2.2, 3.1731819618), (2.2, 1.5731819618))
            make_face()
            # Profile area: 30.48, perimeter: 36.777708764
            with BuildLine():
                Line((-10, 1.5731819618), (2.2, 1.5731819618))
                Line((2.2, 3.1731819618), (2.2, 1.5731819618))
                Line((2.2, 3.1731819618), (-7.4, 3.1731819618))
                Line((-7.4, 3.1731819618), (-7.4, 8.3731819618))
                Line((-7.4, 8.3731819618), (-8.4, 8.3731819618))
                Line((-8.4, 8.3731819618), (-10, 5.1731819618))
                Line((-10, 1.5731819618), (-10, 5.1731819618))
            make_face()
            # Profile area: 11.44, perimeter: 14.8
            with BuildLine():
                Line((4.4, 3.1731819618), (2.2, 3.1731819618))
                Line((4.4, 3.1731819618), (4.4, 8.3731819618))
                Line((2.2, 8.3731819618), (4.4, 8.3731819618))
                Line((2.2, 3.1731819618), (2.2, 8.3731819618))
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)
    return part.part


def model_56343_60e8809c_0010():
    """Model: Label"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8796459692, perimeter: 3.5203162727
            with Locations((-2.1000000313, 0.5000000075)):
                Ellipse(0.7000000104, 0.400000006)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.01, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0695235002, perimeter: 2.6096530506
            with BuildLine():
                Line((-2.350000035, 0.2500000037), (-2.1378680007, 0.4621320381))
                Line((-2.1378680007, 0.4621320381), (-2.167141375, 0.2538411565))
                Line((-2.167141375, 0.2538411565), (-1.8617629814, 0.5603485742))
                Line((-1.8617629814, 0.5603485742), (-1.8618461123, 0.5103486433))
                Line((-1.7416650533, 0.7230645504), (-1.8618461123, 0.5103486433))
                Line((-1.9542180319, 0.602637223), (-1.7416650533, 0.7230645504))
                Line((-1.9042181508, 0.6027462569), (-1.9542180319, 0.602637223))
                Line((-1.9042181508, 0.6027462569), (-2.0826918894, 0.4236126775))
                Line((-2.0534953307, 0.6313569874), (-2.0826918894, 0.4236126775))
                Line((-2.392275596, 0.2925767221), (-2.0534953307, 0.6313569874))
                Line((-2.392275596, 0.2925767221), (-2.4135639552, 0.2714389416))
                Line((-2.4135639552, 0.2714389416), (-2.3911376895, 0.2713593464))
                CenterArc((-2.391208673, 0.2513594723), 0.02, -0.2033530994, 90)
                Line((-2.371208799, 0.2512884889), (-2.3712883942, 0.2288622232))
                Line((-2.350000035, 0.2500000037), (-2.3712883942, 0.2288622232))
            make_face()
        # OneSide extrude, distance=-0.005
        extrude(amount=-0.005, mode=Mode.SUBTRACT)
    return part.part


def model_56344_3a89f085_0010():
    """Model: pressure"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((13, -13)):
                Circle(0.5)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1052164022, perimeter: 1.6935528337
            with BuildLine():
                Line((-12.6063814241, 13.3083251801), (-13.3936185759, 13.3083251801))
                CenterArc((-13, 13), 0.5, 38.0719365216, 103.8561269569)
            make_face()
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)
    return part.part


def model_56344_3a89f085_0011():
    """Model: screw M20x80"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((60, 25)):
                Circle(1)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.6526359805, perimeter: 16.6754901526
            with BuildLine():
                Line((61.5, 24.1339745962), (61.5, 25.8660254038))
                Line((61.5, 25.8660254038), (60, 26.7320508076))
                Line((60, 26.7320508076), (58.5, 25.8660254038))
                Line((58.5, 25.8660254038), (58.5, 24.1339745962))
                Line((58.5, 24.1339745962), (60, 23.2679491924))
                Line((60, 23.2679491924), (61.5, 24.1339745962))
            make_face()
            with BuildLine():
                CenterArc((60, 25), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((60, 25)):
                Circle(1)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0012():
    """Model: screw M12x30"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((63, 17)):
                Circle(0.6)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.3331282598, perimeter: 10.6981144146
            with BuildLine():
                Line((-62, 16.4226497308), (-62, 17.5773502692))
                Line((-62, 17.5773502692), (-63, 18.1547005384))
                Line((-63, 18.1547005384), (-64, 17.5773502692))
                Line((-64, 17.5773502692), (-64, 16.4226497308))
                Line((-64, 16.4226497308), (-63, 15.8452994616))
                Line((-63, 15.8452994616), (-62, 16.4226497308))
            make_face()
            with BuildLine():
                CenterArc((-63, 17), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-63, 17)):
                Circle(0.6)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0014():
    """Model: screw M10x21,5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((65, 0)):
                Circle(0.5)
        # OneSide extrude, distance=2.15
        extrude(amount=2.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.912011628, perimeter: 7.9913349148
            with BuildLine():
                Line((-65.7, 0.4041451884), (-65.7, -0.4041451884))
                Line((-65.7, -0.4041451884), (-65, -0.8082903769))
                Line((-65, -0.8082903769), (-64.3, -0.4041451884))
                Line((-64.3, -0.4041451884), (-64.3, 0.4041451884))
                Line((-64.3, 0.4041451884), (-65, 0.8082903769))
                Line((-65, 0.8082903769), (-65.7, 0.4041451884))
            make_face()
            with BuildLine():
                CenterArc((-65, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-65, 0)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0017():
    """Model: screw M10x55"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((63.9472793384, 26.5466355717)):
                Circle(0.5)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.912011628, perimeter: 7.9913349148
            with BuildLine():
                Line((64.6472793384, 26.1424903833), (64.6472793384, 26.9507807602))
                Line((64.6472793384, 26.9507807602), (63.9472793384, 27.3549259486))
                Line((63.9472793384, 27.3549259486), (63.2472793384, 26.9507807602))
                Line((63.2472793384, 26.9507807602), (63.2472793384, 26.1424903833))
                Line((63.2472793384, 26.1424903833), (63.9472793384, 25.7383451949))
                Line((63.9472793384, 25.7383451949), (64.6472793384, 26.1424903833))
            make_face()
            with BuildLine():
                CenterArc((63.9472793384, 26.5466355717), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((63.9472793384, 26.5466355717)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0020():
    """Model: blockade 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((62.0390521584, 16.5544102305)):
                Circle(0.25)
        # OneSide extrude, distance=0.946
        extrude(amount=0.946)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.946), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3063052837, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((62.0390521584, 16.5544102305), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((62.0390521584, 16.5544102305), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((62.0390521584, 16.5544102305)):
                Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0023():
    """Model: blockade 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((40.5, -19)):
                Circle(0.4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((40.5, 19), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((40.5, 19), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((40.5, 19)):
                Circle(0.4)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0024():
    """Model: srew M15x80"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((59, 16)):
                Circle(0.75)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6969557475, perimeter: 11.6405922107
            with BuildLine():
                Line((60, 15.4226497308), (60, 16.5773502692))
                Line((60, 16.5773502692), (59, 17.1547005384))
                Line((59, 17.1547005384), (58, 16.5773502692))
                Line((58, 16.5773502692), (58, 15.4226497308))
                Line((58, 15.4226497308), (59, 14.8452994616))
                Line((59, 14.8452994616), (60, 15.4226497308))
            make_face()
            with BuildLine():
                CenterArc((59, 16), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((59, 16)):
                Circle(0.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0025():
    """Model: screw M16x55"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-0.1634143055, -17.7304521483)):
                Circle(0.8)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9776870275, perimeter: 13.3403921221
            with BuildLine():
                Line((-1.0365856945, 18.4232724713), (-1.0365856945, 17.0376318253))
                Line((-1.0365856945, 17.0376318253), (0.1634143055, 16.3448115022))
                Line((0.1634143055, 16.3448115022), (1.3634143055, 17.0376318253))
                Line((1.3634143055, 17.0376318253), (1.3634143055, 18.4232724713))
                Line((1.3634143055, 18.4232724713), (0.1634143055, 19.1160927943))
                Line((0.1634143055, 19.1160927943), (-1.0365856945, 18.4232724713))
            make_face()
            with BuildLine():
                CenterArc((0.1634143055, 17.7304521483), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((0.1634143055, 17.7304521483)):
                Circle(0.8)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0027():
    """Model: shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((51, 8)):
                Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((51, 8), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((51, 8), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((51, 8)):
                Circle(0.5)
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)
    return part.part


def model_56344_3a89f085_0028():
    """Model: screw M12x51,5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((61, 14)):
                Circle(0.6)
        # OneSide extrude, distance=5.15
        extrude(amount=5.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0860516784, perimeter: 9.3124737685
            with BuildLine():
                Line((61.8, 13.5381197846), (61.8, 14.4618802154))
                Line((61.8, 14.4618802154), (61, 14.9237604307))
                Line((61, 14.9237604307), (60.2, 14.4618802154))
                Line((60.2, 14.4618802154), (60.2, 13.5381197846))
                Line((60.2, 13.5381197846), (61, 13.0762395693))
                Line((61, 13.0762395693), (61.8, 13.5381197846))
            make_face()
            with BuildLine():
                CenterArc((61, 14), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((61, 14)):
                Circle(0.6)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_56345_80dc7bcc_0009():
    """Model: Helix"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0942477834, perimeter: 1.8849556109
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_56364_8e6032c8_0008():
    """Model: 1.Kolo zebate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.1279292506, perimeter: 9.7690966416
            with BuildLine():
                CenterArc((0.2045022432, 1.5297564937), 0.363285054, 152.7919186667, 33.2080813333)
                CenterArc((0, 0), 1.5000000224, 96, 348)
                CenterArc((-0.2045022432, 1.5297564937), 0.363285054, -6, 33.2080813333)
                CenterArc((0, 0), 1.7000000253, 86, 8)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0593455694, perimeter: 0.9726370805
            with BuildLine():
                CenterArc((0, 0), 1.5000000224, 84, 12)
                CenterArc((-0.2045022432, 1.5297564937), 0.363285054, -6, 33.2080813333)
                CenterArc((0, 0), 1.7000000253, 86, 8)
                CenterArc((0.2045022432, 1.5297564937), 0.363285054, 152.7919186667, 33.2080813333)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


def model_56368_b79cbf07_0002():
    """Model: podst"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            Circle(25)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            Circle(7.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_56430_4f35ba2f_0010():
    """Model: HandleHolderA (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 108.5946509601, perimeter: 70.6517518972
            with BuildLine():
                Line((-12.5, 0), (-37.5, 0))
                Line((-12.5, 0), (-23.7506099049, 9.0004879239))
                CenterArc((-25, 7.438750305), 2, 51.3401917459, 77.3196165082)
                Line((-37.5, 0), (-26.2493900951, 9.0004879239))
            make_face()
            with BuildLine():
                CenterArc((-25, 4), 2.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 37.5, perimeter: 53
            with BuildLine():
                Line((-37.5, 0), (-37.5, -1.5))
                Line((-37.5, -1.5), (-12.5, -1.5))
                Line((-12.5, -1.5), (-12.5, 0))
                Line((-12.5, 0), (-37.5, 0))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((7.5, 25)):
                Circle(0.6)
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)
    return part.part


def model_56430_4f35ba2f_0017():
    """Model: PinionWheel"""
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
            # Profile area: 232.4833105196, perimeter: 71.9948316448
            with BuildLine():
                CenterArc((0, 0), 8.9583333333, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 8.9583333333, -4.5891664191, 9.1783328383)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3321556524, perimeter: 5.9998307591
            with BuildLine():
                Line((8.9296131387, 0.7167602839), (9.3666054798, 0.751836692))
                CenterArc((0, 0), 8.9583333333, -4.5891664191, 9.1783328383)
                Line((8.9296131387, -0.7167602839), (9.3666054798, -0.751836692))
                _nurbs_edge([(9.3666054798, -0.751836692), (9.4202577409, -0.7507994716), (9.5284959876, -0.74870698), (9.6903568764, -0.7226296145), (9.8529549244, -0.6877704374), (10.0159404161, -0.6427607757), (10.1791244753, -0.589328827), (10.3423433307, -0.5278943146), (10.5053690124, -0.4588263503), (10.6683037266, -0.3829124279), (10.7753250852, -0.3271031433), (10.8292309286, -0.2989924316)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1607993588, 0.3243971517, 0.490692576, 0.6596741405, 0.8313371176, 1.0056787057, 1.1826969102, 1.3623901591, 1.5447571399, 1.5447571399, 1.5447571399, 1.5447571399], 3)
                CenterArc((-0.0643365017, 0), 10.897669835, -1.5721851245, 3.144370249)
                _nurbs_edge([(9.3666054798, 0.751836692), (9.4202577409, 0.7507994716), (9.5284959876, 0.74870698), (9.6903568764, 0.7226296145), (9.8529549244, 0.6877704374), (10.0159404161, 0.6427607757), (10.1791244753, 0.589328827), (10.3423433307, 0.5278943146), (10.5053690124, 0.4588263503), (10.6683037266, 0.3829124279), (10.7753250852, 0.3271031433), (10.8292309286, 0.2989924316)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1607993588, 0.3243971517, 0.490692576, 0.6596741405, 0.8313371176, 1.0056787057, 1.1826969102, 1.3623901591, 1.5447571399, 1.5447571399, 1.5447571399, 1.5447571399], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=12.5
        extrude(amount=12.5, mode=Mode.SUBTRACT)
    return part.part


def model_56436_2a8fc254_0006():
    """Model: sod0603_03"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0017505817, perimeter: 0.1944859826
            with BuildLine():
                Line((0.0529048766, -0.038), (0.074, -0.038))
                Line((0.074, -0.038), (0.074, 0.038))
                Line((0.074, 0.038), (0.0529048766, 0.038))
                CenterArc((0.3, 0), 0.25, 171.2571526865, 17.485694627)
            make_face()
            # Profile area: 0.0005530242, perimeter: 0.2515063079
            with BuildLine():
                Line((0.0532207464, -0.04), (0.075, -0.04))
                CenterArc((0.075, -0.035), 0.005, -90, 90)
                Line((0.08, -0.035), (0.08, 0.035))
                CenterArc((0.075, 0.035), 0.005, 0, 90)
                Line((0.075, 0.04), (0.0532207464, 0.04))
                CenterArc((0.3, 0), 0.25, 170.7931037787, 0.4640489078)
                Line((0.074, 0.038), (0.0529048766, 0.038))
                Line((0.074, -0.038), (0.074, 0.038))
                Line((0.0529048766, -0.038), (0.074, -0.038))
                CenterArc((0.3, 0), 0.25, -171.2571526865, 0.4640489078)
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)
    return part.part


def model_56436_2a8fc254_0007():
    """Model: resistor_0603"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0018342794, perimeter: 0.2018988131
            with BuildLine():
                Line((0.074, 0.039997061), (0.0532207465, 0.039997061))
                CenterArc((0.3000000001, -0.000002939), 0.25, 170.7931037791, 18.4131351716)
                Line((0.0532202877, -0.040000108), (0.074, -0.0400003276))
                Line((0.074, -0.0400003276), (0.074, 0.039997061))
            make_face()
            # Profile area: 0.0004693374, perimeter: 0.2092693728
            with BuildLine():
                Line((0.074, -0.0400003276), (0.074, 0.039997061))
                Line((0.0532202877, -0.040000108), (0.074, -0.0400003276))
                CenterArc((0.3000000001, -0.000002939), 0.25, -170.7937610494, 0.0006572703)
                Line((0.0532207465, -0.040002939), (0.075, -0.040002939))
                CenterArc((0.075, -0.035002939), 0.005, -89.9999999966, 89.9999999966)
                Line((0.08, -0.035002939), (0.08, 0.0350021569))
                CenterArc((0.0750050958, 0.0350021569), 0.0049949042, 0, 90.0000000034)
                Line((0.0750050958, 0.039997061), (0.074, 0.039997061))
            make_face()
        # OneSide extrude, distance=0.045
        extrude(amount=0.045)
    return part.part


def model_56457_dd352142_0002():
    """Model: podstawa"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 942.4777960769, perimeter: 133.6489303634
            Ellipse(30, 10)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_56458_c027ed41_0010():
    """Model: przegub"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((-7.791393906, -1), (-9.291393906, -1))
                Line((-7.791393906, 0), (-7.791393906, -1))
                Line((-9.291393906, 0), (-7.791393906, 0))
                Line((-9.291393906, -1), (-9.291393906, 0))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-8.5000001267, -0.5000000075)):
                Circle(0.25)
        # Symmetric extrude, each_side=1.8
        extrude(amount=1.8, both=True, mode=Mode.ADD)
    return part.part


def model_56459_7b640aed_0009():
    """Model: zawieszenie"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 750, perimeter: 310
            with BuildLine():
                Line((75, 60), (-75, 60))
                Line((75, 65), (75, 60))
                Line((-75, 65), (75, 65))
                Line((-75, 60), (-75, 65))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 65), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 545.5456625464, perimeter: 319.6278347724
            with BuildLine():
                CenterArc((0, 141.277027027), 161.277027027, -64.6697409746, 2.382443978)
                CenterArc((0, 141.277027027), 161.277027027, -115.3302590254, 50.6605180508)
                CenterArc((0, 141.277027027), 161.277027027, -117.7127030034, 2.382443978)
                Line((-75, -1.5), (-75, -5.4419854965))
                CenterArc((0, 141.277027027), 164.777027027, -117.0752638948, 54.1505277896)
                Line((75, -1.5), (75, -5.4419854965))
            make_face()
            # Profile area: 9.1387176927, perimeter: 15.7004382
            with BuildLine():
                Line((75, -1.5), (69, -1.5))
                Line((69, -1.5), (69, -4.4942988456))
                CenterArc((0, 141.277027027), 161.277027027, -64.6697409746, 2.382443978)
            make_face()
            # Profile area: 9.1387176927, perimeter: 15.7004382
            with BuildLine():
                CenterArc((0, 141.277027027), 161.277027027, -117.7127030034, 2.382443978)
                Line((-69, -1.5), (-69, -4.4942988456))
                Line((-75, -1.5), (-69, -1.5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)
    return part.part


def model_56459_7b640aed_0010():
    """Model: blotnik"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 65), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.6502161924, perimeter: 12.4163979258
            with BuildLine():
                Line((-30.3108891325, 1.5), (-28.6661821664, 1.5))
                CenterArc((0, -37), 49, 128.2132107017, 5.3603678948)
                Line((-33.7749907476, -1.5), (-32.3071199583, -1.5))
                CenterArc((0, -37), 48, 126.6704909008, 5.6335750474)
            make_face()
            # Profile area: 4.6502161924, perimeter: 12.4163979258
            with BuildLine():
                Line((28.6661821664, 1.5), (30.3108891325, 1.5))
                CenterArc((0, -37), 48, 47.6959340518, 5.6335750474)
                Line((32.3071199583, -1.5), (33.7749907476, -1.5))
                CenterArc((0, -37), 49, 46.4264214035, 5.3603678948)
            make_face()
            # Profile area: 63.4090212983, perimeter: 130.0921529294
            with BuildLine():
                CenterArc((0, -37), 49, 51.7867892983, 76.4264214035)
                Line((-30.3108891325, 1.5), (-28.6661821664, 1.5))
                CenterArc((0, -37), 48, 53.3295090992, 73.3409818016)
                Line((28.6661821664, 1.5), (30.3108891325, 1.5))
            make_face()
        # OneSide extrude, distance=16
        extrude(amount=16)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 65), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 32.4035599792, perimeter: 130.6142399166
            with BuildLine():
                Line((32.5, -1.5), (32.5, -1))
                Line((32.5, -1), (-32.3071199583, -1))
                Line((-32.3071199583, -1), (-32.3071199583, -1.5))
                Line((-32.3071199583, -1.5), (32.5, -1.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_56460_78d17e23_0004():
    """Model: felga-tyl"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21.2057504117, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((-75.9950577708, 5), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-75.9950577708, 5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 208.1305133003, perimeter: 166.5044106403
            with BuildLine():
                CenterArc((-76, 5), 14.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-76, 5), 12, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


def model_56461_9a5be0e9_0003():
    """Model: rama"""
    with BuildPart() as part:
        # Sketch19 -> Extrude29 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((-35, 0)):
                Circle(3)
        # Symmetric extrude, each_side=-6.5
        extrude(amount=-6.5, both=True)

        # Sketch19 -> Extrude33 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((-35, 0)):
                Circle(3)
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_56463_450f3e67_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 409.8, perimeter: 272.3327412287
            with BuildLine():
                Line((-4.3751151156, 0.1929009306), (22.3748848844, 0.1929009306))
                Line((22.3748848844, 0.1929009306), (22.3748848844, 3.1929009306))
                Line((22.3748848844, 3.1929009306), (-7.3751151156, 3.1929009306))
                CenterArc((-7.3751151156, 1.1929009306), 2, 90, 90)
                Line((-9.3751151156, 1.1929009306), (-9.3751151156, -15.6070990694))
                CenterArc((-11.3751151156, -15.6070990694), 2, -90, 90)
                Line((-11.3751151156, -17.6070990694), (-38.8751151156, -17.6070990694))
                CenterArc((-38.8751151156, -15.6070990694), 2, -180, 90)
                Line((-40.8751151156, -15.6070990694), (-40.8751151156, 1.1929009306))
                CenterArc((-42.8751151156, 1.1929009306), 2, 0, 90)
                Line((-42.8751151156, 3.1929009306), (-72.6251151156, 3.1929009306))
                Line((-72.6251151156, 3.1929009306), (-72.6251151156, 0.1929009306))
                Line((-72.6251151156, 0.1929009306), (-45.8751151156, 0.1929009306))
                CenterArc((-45.8751151156, -1.8070990694), 2, 0, 90)
                Line((-43.8751151156, -1.8070990694), (-43.8751151156, -18.6070990694))
                CenterArc((-41.8751151156, -18.6070990694), 2, -180, 90)
                Line((-41.8751151156, -20.6070990694), (-8.3751151156, -20.6070990694))
                CenterArc((-8.3751151156, -18.6070990694), 2, -90, 90)
                Line((-6.3751151156, -18.6070990694), (-6.3751151156, -1.8070990694))
                CenterArc((-4.3751151156, -1.8070990694), 2, 90, 90)
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -17.6070990694, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 157.0796326795, perimeter: 125.6637061436
            with BuildLine():
                CenterArc((25, 15), 11.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((25, 15), 8.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -17.6070990694, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((59.2501151156, 15)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-7.5, 15)):
                Circle(2.5)
        # OneSide extrude, distance=35
        extrude(amount=35, mode=Mode.SUBTRACT)
    return part.part


def model_56477_620f7fc8_0011():
    """Model: Locking screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671456804, perimeter: 14.1371671284
            with BuildLine():
                CenterArc((0, 2.0000000298), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 2.0000000298), 1.0000000298, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_56486_82b3e23a_0010():
    """Model: Podstawa v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 300, perimeter: 70
            with BuildLine():
                Line((-10, 7.5), (10, 7.5))
                Line((-10, -7.5), (-10, 7.5))
                Line((10, -7.5), (-10, -7.5))
                Line((10, 7.5), (10, -7.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_56564_976c253c_0013():
    """Model: 1.Podstawa"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.9225651046, perimeter: 59.6902604182
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


def model_56568_d3018fcb_0000():
    """Model: Ocular Head v1"""
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
        # Sketch has 50 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 40.3318675426, perimeter: 24.8827733391
            with BuildLine():
                Line((2.4118570964, 32.9230672352), (4.6813660901, 33.3081883263))
                Line((4.6813660901, 33.3081883263), (5.1808409705, 34.3698764973))
                Line((5.1808409705, 34.3698764973), (6.8568108294, 37.932332677))
                Line((1.1109137654, 40.6355098688), (6.8568108294, 37.932332677))
                Line((0.0296428887, 38.3371510432), (1.1109137654, 40.6355098688))
                Line((0.0296428887, 38.3371510432), (-1.1597550757, 35.808956335))
                Line((-1.1597550757, 35.808956335), (-1.700390514, 34.6597769222))
                Line((-1.700390514, 34.6597769222), (2.1026914766, 32.8706038164))
                Line((2.1026914766, 32.8706038164), (2.4118570964, 32.9230672352))
            make_face()
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-14.7431528287, 6.9359673549, 0), x_dir=(0, 0, 1), z_dir=(-0.9048656794, 0.4256971955, 0))):
            # Profile area: 2.580590508, perimeter: 10.8006434978
            with BuildLine():
                Line((9.6064788426, 30.6385911184), (12.7, 30.6385911184))
                Line((12.7, 30.6385911184), (12.7, 33.6820338197))
                _nurbs_edge([(12.7, 33.6820338197), (12.6890789664, 33.6189841866), (12.6578068028, 33.4643045764), (12.5899324754, 33.2105010993), (12.4594816111, 32.8455961123), (12.2820482367, 32.4590259346), (12.1096691226, 32.1328000266), (11.9821941213, 31.909526289), (11.9153175185, 31.7964418762)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(9.6064788426, 30.6385911184), (9.7042953626, 30.6601273743), (9.8994470314, 30.7083687147), (10.1907306603, 30.7962252247), (10.5757026898, 30.9417803472), (11.0466512188, 31.1672695767), (11.4088302117, 31.3867141709), (11.6678079658, 31.5792984567), (11.8339073945, 31.7217200815), (11.9153175185, 31.7964418762)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 7.8040746655, perimeter: 16.5678881753
            with BuildLine():
                Line((12.7, 34.4306308067), (12.7, 37.2425911184))
                Line((6.35, 37.2425911184), (12.7, 37.2425911184))
                _nurbs_edge([(11.4862416451, 35.7108506632), (11.4283972508, 35.7155988592), (11.2303437953, 35.7294615897), (10.8832125863, 35.7412906676), (10.3828071114, 35.7392394607), (9.7592788941, 35.7350517613), (9.1408386142, 35.77617245), (8.6449434467, 35.8954656111), (8.2710761675, 36.0956474039), (7.9845857441, 36.3505230901), (7.736182005, 36.6213059856), (7.4752319285, 36.867563317), (7.168570616, 37.0628090777), (6.8742985895, 37.1683755866), (6.6237295661, 37.2172391972), (6.4434494568, 37.2363800977), (6.35, 37.2425911184)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.6193923689, 0.6193923689, 0.6193923689, 0.6193923689, 0.6193923689, 0.6193923689, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(11.4862416451, 35.7108506632), (11.5757445317, 35.6698780094), (11.747324644, 35.5845084836), (11.982416934, 35.4461811278), (12.2505922897, 35.2408640712), (12.4787594632, 34.9780947054), (12.6039584296, 34.7500886884), (12.6655226527, 34.5749839824), (12.6923769941, 34.4661187985), (12.7, 34.4306308067)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724], 5)
            make_face()
            # Profile area: 7.8040746655, perimeter: 16.5678881753
            with BuildLine():
                _nurbs_edge([(1.2137583549, 35.7108506632), (1.1242554683, 35.6698780094), (0.952675356, 35.5845084836), (0.717583066, 35.4461811278), (0.4494077103, 35.2408640712), (0.2212405368, 34.9780947054), (0.0960415704, 34.7500886884), (0.0344773473, 34.5749839824), (0.0076230059, 34.4661187985), (0, 34.4306308067)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724], 5)
                _nurbs_edge([(1.2137583549, 35.7108506632), (1.2716027492, 35.7155988592), (1.4696562047, 35.7294615897), (1.8167874137, 35.7412906676), (2.3171928886, 35.7392394607), (2.9407211059, 35.7350517613), (3.5591613858, 35.77617245), (4.0550565533, 35.8954656111), (4.4289238325, 36.0956474039), (4.7154142559, 36.3505230901), (4.963817995, 36.6213059856), (5.2247680715, 36.867563317), (5.531429384, 37.0628090777), (5.8257014105, 37.1683755866), (6.0762704339, 37.2172391972), (6.2565505432, 37.2363800977), (6.35, 37.2425911184)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.6193923689, 0.6193923689, 0.6193923689, 0.6193923689, 0.6193923689, 0.6193923689, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 37.2425911184), (6.35, 37.2425911184))
                Line((0, 37.2425911184), (0, 34.4306308067))
            make_face()
            # Profile area: 2.5805904822, perimeter: 10.8006435027
            with BuildLine():
                Line((0, 33.6820338197), (0, 30.6385911184))
                Line((0, 30.6385911184), (3.0935211574, 30.6385911184))
                _nurbs_edge([(3.0935211574, 30.6385911184), (2.9957046312, 30.6601273731), (2.8005529531, 30.7083687111), (2.509269319, 30.7962252167), (2.1242972972, 30.9417803326), (1.6533487869, 31.1672695563), (1.2911698033, 31.3867141519), (1.0321920465, 31.5792984445), (0.8660926105, 31.7217200769), (0.7846824815, 31.7964418762)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0, 33.6820338197), (0.0109210336, 33.6189841866), (0.0421931972, 33.4643045764), (0.1100675246, 33.2105010993), (0.2405183889, 32.8455961123), (0.4179517633, 32.4590259346), (0.5903308774, 32.1328000266), (0.7178058787, 31.909526289), (0.7846824815, 31.7964418762)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 19.8349457682, perimeter: 42.1633466777
            with BuildLine():
                _nurbs_edge([(0, 34.4306308067), (-0.0084514945, 34.3912858852), (-0.0293551999, 34.2754376928), (-0.0417738043, 34.131444925), (-0.0394509193, 33.9806543684), (-0.0230621806, 33.8233775811), (-0.0045616293, 33.7083691525), (0, 33.6820338197)], [1, 1, 1, 1, 1, 1, 1, 1], [0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724, 0.4474229724, 0.5, 0.6, 0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213, 0.6294628213], 5)
                Line((0, 37.2425911184), (0, 34.4306308067))
                Line((-2.0815298809, 30.6385911184), (0, 37.2425911184))
                Line((0, 29.6939787386), (-2.0815298809, 30.6385911184))
                Line((12.7, 29.6939787386), (0, 29.6939787386))
                Line((12.7, 30.6385911184), (12.7, 29.6939787386))
                Line((9.6064788426, 30.6385911184), (12.7, 30.6385911184))
                Line((3.0935211574, 30.6385911184), (9.6064788426, 30.6385911184))
                Line((0, 30.6385911184), (3.0935211574, 30.6385911184))
                Line((0, 33.6820338197), (0, 30.6385911184))
            make_face()
        # OneSide extrude, distance=-12.954
        extrude(amount=-12.954, mode=Mode.SUBTRACT)
    return part.part


def model_56568_d3018fcb_0012():
    """Model: Elevation Adjustment v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3459417414, perimeter: 16.9567463478
            with BuildLine():
                CenterArc((17.1572631413, 5.4940343462), 1.42875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.1572631413, 5.4940343462), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((17.1572631413, 5.4940343462)):
                Circle(1.27)
        # OneSide extrude, distance=4.445
        extrude(amount=4.445)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3459417414, perimeter: 16.9567463478
            with BuildLine():
                CenterArc((17.1572631413, 5.4940343462), 1.42875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.1572631413, 5.4940343462), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3459417414, perimeter: 16.9567463478
            with BuildLine():
                CenterArc((17.1572631413, 5.4940343462), 1.42875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.1572631413, 5.4940343462), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254)
    return part.part


def model_56568_d3018fcb_0013():
    """Model: Coarse/Fine Adjustment v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.9411451924, perimeter: 26.7318118894
            with BuildLine():
                CenterArc((24.6934534606, 12.2830779314), 2.3495, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((24.6934534606, 12.2830779314), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((24.6934534606, 12.2830779314)):
                Circle(1.905)
        # OneSide extrude, distance=4.445
        extrude(amount=4.445)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.9411451924, perimeter: 26.7318118894
            with BuildLine():
                CenterArc((24.6934534606, 12.2830779314), 2.3495, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((24.6934534606, 12.2830779314), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.445), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((24.6934534606, 12.2830779314)):
                Circle(1.27)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_56793_e1f0d3ac_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1736634286, perimeter: 5.265181738
            with BuildLine():
                CenterArc((-0.4972242005, -0.2588540878), 0.1201021199, 91.9234035115, 169.6853599203)
                Line((-0.0650834621, -0.3776704233), (-0.514750909, -0.3776704743))
                CenterArc((-0.0650834541, -0.4488352135), 0.0711647902, -90.0000064984, 180.0000129481)
                Line((-0.1828268082, -0.5199999903), (-0.0650834621, -0.5200000037))
                CenterArc((-0.1914134019, -0.5199999894), 0.0085865937, -0.0000064984, 180)
                Line((-0.200000003, -0.5856912777), (-0.1999999955, -0.5199999884))
                Line((-0.0631334394, -0.5856912777), (-0.200000003, -0.5856912777))
                CenterArc((-0.0631334394, -0.4480576205), 0.1376336572, -90, 180)
                Line((-0.5012552383, -0.3104239633), (-0.0631334394, -0.3104239633))
                CenterArc((-0.5012351752, -0.2599823088), 0.0504416585, 90.0227893182, 179.9544213636)
                Line((-0.1380883114, -0.2093962051), (-0.5012552383, -0.2095406543))
                Line((-0.1236634247, -0.2095406543), (-0.1380883114, -0.2093962051))
                CenterArc((-0.1221662795, -0.0600337252), 0.1495144251, -90.5737341749, 45.8830497584)
                CenterArc((-0.5052500684, 0.364325799), 0.7210196045, -47.2557334147, 24.5726280054)
                CenterArc((-0.5483446684, 0.3981380544), 0.7739573809, -23.7623877618, 47.5247755237)
                Line((0.089999998, 0.7099999841), (0.1599999964, 0.7099999841))
                Line((0.1234553034, 0.6190686433), (0.089999998, 0.7099999841))
                CenterArc((-0.4777977475, 0.4098305978), 0.636620602, -8.5812701384, 27.7693353705)
                CenterArc((-0.5516448988, 0.394301853), 0.7078154986, -38.7689221517, 32.3230346444)
                CenterArc((-0.1414828946, 0.0180622289), 0.1567387523, -89.9772106818, 64.6782405867)
                Line((-0.5012552383, -0.1388196347), (-0.141420552, -0.138676511))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_57251_414ca79f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=-0.375
        extrude(amount=-0.375)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0209999991, perimeter: 0.7399999835
            with BuildLine():
                Line((-0.1499999966, 0.1199999973), (-0.1499999966, 0.0499999989))
                Line((-0.1499999966, 0.0499999989), (0.1499999966, 0.0499999989))
                Line((0.1499999966, 0.0499999989), (0.1499999966, 0.1199999973))
                Line((0.1499999966, 0.1199999973), (-0.1499999966, 0.1199999973))
            make_face()
        # OneSide extrude, distance=-0.187
        extrude(amount=-0.187, mode=Mode.SUBTRACT)
    return part.part


def model_57755_3c6610d1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.1161965748, perimeter: 14.3574974608
            with BuildLine():
                Line((11.825, 1.5), (6.1180339887, 1.5))
                CenterArc((11.825, 1.675), 0.175, -90, 90)
                Line((12, 2.325), (12, 1.675))
                CenterArc((11.825, 2.325), 0.175, 0, 90)
                Line((9.5, 2.5), (11.825, 2.5))
                Line((9.5, 2.85), (9.5, 2.5))
                CenterArc((9.35, 2.85), 0.15, 0, 90)
                Line((6.4142135624, 3), (9.35, 3))
                CenterArc((5, 2.5), 1.5, -41.8103148958, 61.2815355303)
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((5, 2.5), 1.5, 19.4712206345, 298.7184644697)
                CenterArc((5, 2.5), 1.5, -41.8103148958, 61.2815355303)
            make_face()
        # TwoSides extrude, along=0.5, against=-3.5
        extrude(amount=0.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-3.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0183655448, perimeter: 5.3249738036
            with BuildLine():
                Line((-11.8082356634, -0.2684991047), (-11.8082356634, -0.7315008953))
                Line((-11.8082356634, -0.7315008953), (-9.6087505522, -0.7315008953))
                Line((-9.6087505522, -0.7315008953), (-9.6087505522, -0.2684991047))
                Line((-9.6087505522, -0.2684991047), (-11.8082356634, -0.2684991047))
            make_face()
            # Profile area: 0.5600000167, perimeter: 3.6000000536
            with BuildLine():
                Line((-10.3000001535, -1.3000000194), (-11.7000001743, -1.3000000194))
                Line((-10.3000001535, -0.9000000134), (-10.3000001535, -1.3000000194))
                Line((-11.7000001743, -0.9000000134), (-10.3000001535, -0.9000000134))
                Line((-11.7000001743, -1.3000000194), (-11.7000001743, -0.9000000134))
            make_face()
            # Profile area: 0.5600000167, perimeter: 3.6000000536
            with BuildLine():
                Line((-10.3000001535, -2.0999999866), (-10.3000001535, -1.6999999806))
                Line((-10.3000001535, -1.6999999806), (-11.7000001743, -1.6999999806))
                Line((-11.7000001743, -1.6999999806), (-11.7000001743, -2.0999999866))
                Line((-11.7000001743, -2.0999999866), (-10.3000001535, -2.0999999866))
            make_face()
            # Profile area: 1.0183655448, perimeter: 5.3249738036
            with BuildLine():
                Line((-9.6087505522, -2.7315008953), (-11.8082356634, -2.7315008953))
                Line((-9.6087505522, -2.2684991047), (-9.6087505522, -2.7315008953))
                Line((-11.8082356634, -2.2684991047), (-9.6087505522, -2.2684991047))
                Line((-11.8082356634, -2.7315008953), (-11.8082356634, -2.2684991047))
            make_face()
        # OneSide extrude, distance=-0.015
        extrude(amount=-0.015, mode=Mode.SUBTRACT)
    return part.part


def model_57854_7f40fb28_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.9248682591, perimeter: 113.1077145663
            with BuildLine():
                Line((12, -6), (-5.5, -6))
                Line((12, 5), (12, -6))
                Line((-5.5, 5), (12, 5))
                Line((-5.5, -6), (-5.5, 5))
            make_face()
            with BuildLine():
                CenterArc((-4.649921512, -5), 0.6, 90, 270)
                Line((-4.649921512, -4.4), (-4.649921512, 3.5490689947))
                CenterArc((-4.649921512, 4.1490689947), 0.6, 0, 270)
                Line((-4.049921512, 4.1490689947), (10.4, 4.1490689947))
                CenterArc((11, 4.1490689947), 0.6, -90, 270)
                Line((11, 3.5490689947), (11, -4.4))
                CenterArc((11, -5), 0.6, 180, 270)
                Line((10.4, -5), (-4.049921512, -5))
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 142.0512383197, perimeter: 48.5678921977
            with BuildLine():
                Line((10.4, -5), (-4.049921512, -5))
                CenterArc((11, -5), 0.6, 90, 90)
                Line((11, 3.5490689947), (11, -4.4))
                CenterArc((11, 4.1490689947), 0.6, 180, 90)
                Line((-4.049921512, 4.1490689947), (10.4, 4.1490689947))
                CenterArc((-4.649921512, 4.1490689947), 0.6, -90, 90)
                Line((-4.649921512, -4.4), (-4.649921512, 3.5490689947))
                CenterArc((-4.649921512, -5), 0.6, 0, 90)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((9.6850796324, 5.5)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-3.1840109727, -4.5971205476)):
                Circle(0.4)
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                CenterArc((-3.2038357668, 5.5), 0.4, 90, 180)
                Line((-3.2038357668, 5.9), (-3.2038357668, 5.1))
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                Line((-3.2038357668, 5.9), (-3.2038357668, 5.1))
                CenterArc((-3.2038357668, 5.5), 0.4, -90, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                CenterArc((9.6322180105, -4.5745344974), 0.4, -90, 180)
                Line((9.6322180105, -4.1745344974), (9.6322180105, -4.9745344974))
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                Line((9.6322180105, -4.1745344974), (9.6322180105, -4.9745344974))
                CenterArc((9.6322180105, -4.5745344974), 0.4, 90, 180)
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_57888_fa22ef0f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.8407044967, perimeter: 22.6543467983
            Circle(3.6055512755)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_60294_f8d4a189_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4288059606, perimeter: 2.3213217404
            Circle(0.3694498295)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 41.1972966995, perimeter: 25.1924614859
            with BuildLine():
                CenterArc((0, 0), 3.6400549446, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3694498295, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_60298_4d6233b0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1798819309, perimeter: 3.8505627673
            with Locations((0.1456441293, 0)):
                Circle(0.6128360981)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0724190337, perimeter: 15.2010787719
            with BuildLine():
                CenterArc((-0.1456441293, 0), 1.8064907288, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.1456441293, 0), 0.6128360981, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1798819309, perimeter: 3.8505627673
            with Locations((-0.1456441293, 0)):
                Circle(0.6128360981)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_60303_d31fd2a9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.25, perimeter: 30
            with BuildLine():
                Line((0, 7.5), (0, 0))
                Line((0, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 1.5))
                Line((7.5, 1.5), (1.5, 1.5))
                Line((1.5, 1.5), (1.5, 7.5))
                Line((1.5, 7.5), (0, 7.5))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-4.1769005505, 1.5940695813)):
                Circle(0.6)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_60529_79e8313a_0013():
    """Model: Kushan v1 (4)"""
    with BuildPart() as part:
        # Sketch5 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18225, perimeter: 540
            with BuildLine():
                Line((50, 185), (50, 50))
                Line((50, 50), (185, 50))
                Line((185, 50), (185, 185))
                Line((185, 185), (50, 185))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


def model_60692_269557b8_0005():
    """Model: bush v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_60707_15529a7f_0001():
    """Model: Leg-2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.4495348041, perimeter: 33.7449590345
            with BuildLine():
                CenterArc((-6.1098130841, -12.6985981308), 18.2516189306, 44.0871624144, 50.281165807)
                Line((7, 0), (7.5, 0))
                CenterArc((-6.125, -12.3125), 18.3640486073, 42.1031663563, 52.1908483148)
                Line((-7.5, 5.5), (-7.5, 6))
            make_face()
        # TwoSides extrude (symmetric), distance=4.5
        extrude(amount=4.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-6.4957198544, 3.5000000522)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-6.5, -3.5)):
                Circle(0.25)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.SUBTRACT)
    return part.part


def model_60707_15529a7f_0002():
    """Model: Leg-3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.2071182431, perimeter: 33.255626507
            with BuildLine():
                CenterArc((-8.4, 18), 24.0168690716, -87.8524145717, 39.3076481161)
                Line((7, 0), (7.5, 0))
                CenterArc((-8.5, 19), 24.5203996705, -87.6626941409, 36.8698976458)
                Line((-7.5, -5.5), (-7.5, -6))
            make_face()
        # TwoSides extrude (symmetric), distance=4.5
        extrude(amount=4.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-6.5, 3.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-6.5, -3.5)):
                Circle(0.25)
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)
    return part.part


def model_60717_7ba1f3ab_0000():
    """Model: back part v1"""
    with BuildPart() as part:
        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_60721_57103153_0002():
    """Model: chair back v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 900, perimeter: 120
            with BuildLine():
                Line((0.5, -26.5), (-29.5, -26.5))
                Line((0.5, 3.5), (0.5, -26.5))
                Line((-29.5, 3.5), (0.5, 3.5))
                Line((-29.5, -26.5), (-29.5, 3.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 75.6102072148, perimeter: 45.4302611351
            with BuildLine():
                Line((-20.9488758445, -21.164006412), (-25, -21.164006412))
                Line((-20.9488758445, -2.5), (-20.9488758445, -21.164006412))
                Line((-25, -2.5), (-20.9488758445, -2.5))
                Line((-25, -21.164006412), (-25, -2.5))
            make_face()
        # TwoSides extrude (symmetric), distance=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_60725_a5735a6c_0004():
    """Model: 1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.6892523856, perimeter: 28.3136487129
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2, 1.5), 0.2515642874, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, -2), 0.2515642874, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -1.5), 0.2515642874, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 2), 0.2515642874, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.6892523856, perimeter: 28.3136487129
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, 2), 0.2515642874, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, -2), 0.2515642874, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -1.5), 0.2515642874, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, 1.5), 0.2515642874, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1988144052, perimeter: 1.5806250344
            with Locations((1, 2)):
                Circle(0.2515642874)
            # Profile area: 0.1988144052, perimeter: 1.5806250344
            with Locations((-2, -2)):
                Circle(0.2515642874)
            # Profile area: 0.1988144052, perimeter: 1.5806250344
            with Locations((2, -1.5)):
                Circle(0.2515642874)
            # Profile area: 0.1988144052, perimeter: 1.5806250344
            with Locations((-2, 1.5)):
                Circle(0.2515642874)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_60738_365811c2_0001():
    """Model: Untitled v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 37.0948353097, perimeter: 29.4422980132
            with BuildLine():
                CenterArc((5, 0), 1.5, -89.8888809795, 179.8888809795)
                Line((5, 1.5), (4.9941818363, 1.4999887163))
                Line((4.9941818363, 1.4999887163), (-5.0116502872, 1.4805834535))
                CenterArc((-5.0087411999, -0.0194137256), 1.5, 90.1111190205, 179.8888809795)
                Line((-5.0087411999, -1.5194137256), (-5.0029230362, -1.5194024419))
                Line((-5.0029230362, -1.5194024419), (5.0029090873, -1.4999971791))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((5, 0)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-5.0087411999, -0.0194137256)):
                Circle(0.75)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_60738_365811c2_0002():
    """Model: Untitled v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.6, perimeter: 23.2
            with BuildLine():
                Line((-5.5, 0.3), (5.5, 0.3))
                Line((-5.5, -0.3), (-5.5, 0.3))
                Line((5.5, -0.3), (-5.5, -0.3))
                Line((5.5, 0.3), (5.5, -0.3))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((5, 0)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-5.0087, 0)):
                Circle(0.15)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_60753_80b955c8_0002():
    """Model: ch4 v2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3561944902, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-6
        extrude(amount=-6)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((0, -1.0000000149)):
                Circle(0.200000003)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.SUBTRACT)
    return part.part


def model_60756_88dc9000_0000():
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
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 57.4211340581, perimeter: 50.8601393018
            with BuildLine():
                _nurbs_edge([(-5.4315464993, -1.8824447541), (-5.7510251755, -2.1031196172), (-6.3494433288, -2.5417685754), (-7.1254519627, -3.1916494411), (-7.9162670069, -4.0418457286), (-8.4974325378, -5.0678500308), (-8.675164499, -6.0272334457), (-8.4620568078, -6.8631187231), (-7.8845984182, -7.4742826177), (-6.9846867787, -7.7317581908), (-5.8154785106, -7.5412636203), (-4.4388485618, -6.9018787944), (-2.9224027586, -5.9482244367), (-1.3367035576, -4.8906933497), (0.2475273243, -3.9713861406), (1.7621315577, -3.4140086497), (3.1443057817, -3.3772732754), (4.3393741464, -3.9037291354), (5.3038606899, -4.8759108467), (5.8967702692, -5.8802489808), (6.2121318996, -6.6179741488), (6.3674046666, -7.0616596546), (6.4348066782, -7.2774332973), (6.4455621263, -7.3126234418)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.7279971446, 0.7279971446, 0.7279971446, 0.7279971446, 0.7279971446, 0.7279971446], 5)
                _nurbs_edge([(6.4455621263, -7.3126234418), (6.420007235, -7.1315695594), (6.3609957278, -6.6614757093), (6.2694803675, -5.7021499681), (6.1739822577, -3.8937178751), (6.1706315, -1.3648800101), (6.2509548516, 1.0884101168), (6.3444547579, 2.928509584), (6.4011926055, 3.899702293)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.8478632399, 0.8478632399, 0.8478632399, 0.8478632399, 0.8478632399, 0.8478632399, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(6.4011926055, 3.899702293), (6.3292210322, 3.892187718), (6.1775102443, 3.8564495817), (5.9272192002, 3.7406232985), (5.5478364771, 3.4606888977), (4.9965926668, 2.9033946342), (4.3682852899, 2.1521705335), (3.6673838828, 1.2461914943), (2.9016034665, 0.2478359284), (2.0805385575, -0.7676512621), (1.2146859497, -1.7191823552), (0.3143677001, -2.528268457), (-0.6110879274, -3.1263840358), (-1.5542654572, -3.4649207103), (-2.510177231, -3.5205890912), (-3.4756811696, -3.2855334604), (-4.2544138277, -2.8661757857), (-4.8417219215, -2.4237061175), (-5.2346986472, -2.0722740943), (-5.4315464993, -1.8824447541)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0002351784, 0.0002351784, 0.0002351784, 0.0002351784, 0.0002351784, 0.0002351784, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-8.5
        extrude(amount=-8.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.2915890423, perimeter: 15.4814089532
            with BuildLine():
                Line((-2, -1), (-6.6998324408, -1))
                Line((-2, 2.0408720358), (-2, -1))
                Line((-6.6998324408, 2.0408720358), (-2, 2.0408720358))
                Line((-6.6998324408, -1), (-6.6998324408, 2.0408720358))
            make_face()
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.SUBTRACT)
    return part.part


def model_60759_23829707_0008():
    """Model: base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.0196487541, perimeter: 40.3859051045
            with BuildLine():
                CenterArc((0, 0), 8.5, 90, 6.7563270306)
                Line((0, 8.5), (0, 21.5))
                Line((5, 21.5), (0, 21.5))
                Line((5, 23.5), (5, 21.5))
                Line((-1, 21.5), (5, 23.5))
                Line((-1, 21.5), (-1, 8.4409715081))
            make_face()
            # Profile area: 24.7523901035, perimeter: 53.0041324319
            with BuildLine():
                CenterArc((0, 0), 8.5, 173.2436729694, 6.7563270306)
                Line((-7.5, 0), (-8.5, 0))
                CenterArc((0, 0), 7.5, 0, 180)
                Line((7.5, 0), (8.5, 0))
                CenterArc((0, 0), 8.5, 0, 90)
                Line((0, 8.1000001207), (0, 8.5))
                Line((-1, 8.1000001207), (0, 8.1000001207))
                Line((-1, 8.4409715081), (-1, 8.1000001207))
                CenterArc((0, 0), 8.5, 96.7563270306, 76.4873459388)
            make_face()
            # Profile area: 14.1061170845, perimeter: 30.2122582594
            with BuildLine():
                CenterArc((-32.5, 0), 4, 0, 179.5552426716)
                Line((-27.5, 0), (-28.5, 0))
                CenterArc((-32.5, 0), 5, 0, 11.5369590328)
                CenterArc((-32.5, 0), 5, 11.5369590328, 168.1072363908)
                Line((-36.4998794884, 0.0310496072), (-37.4999035913, 0.0310496072))
            make_face()
            # Profile area: 14.1682167978, perimeter: 30.3364577109
            with BuildLine():
                Line((-36.4998794884, 0.0310496072), (-37.4999035913, 0.0310496072))
                CenterArc((-32.5, 0), 5, 179.6441954236, 180.3558045764)
                Line((-27.5, 0), (-28.5, 0))
                CenterArc((-32.5, 0), 4, 179.5552426716, 180.4447573284)
            make_face()
            # Profile area: 25.1327412287, perimeter: 52.2654824574
            with BuildLine():
                Line((7.5, 0), (8.5, 0))
                CenterArc((0, 0), 7.5, -180, 180)
                Line((-7.5, 0), (-8.5, 0))
                CenterArc((0, 0), 8.5, -180, 180)
            make_face()
            # Profile area: 43.1968989869, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((-32.5, 0), 4, 179.5552426716, 180.4447573284)
                CenterArc((-32.5, 0), 4, 0, 179.5552426716)
            make_face()
            with BuildLine():
                CenterArc((-32.5, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3803511252, perimeter: 2.7432925589
            with BuildLine():
                Line((-1, 8.4409715081), (-1, 8.1000001207))
                Line((-1, 8.1000001207), (0, 8.1000001207))
                Line((0, 8.1000001207), (0, 8.5))
                CenterArc((0, 0), 8.5, 90, 6.7563270306)
            make_face()
            # Profile area: 19.0531850014, perimeter: 40.1691599025
            with BuildLine():
                Line((-8.5, 0), (-27.5, 0))
                CenterArc((0, 0), 8.5, 173.2436729694, 6.7563270306)
                Line((-8.4409715081, 1), (-27.6010205144, 1))
                CenterArc((-32.5, 0), 5, 0, 11.5369590328)
            make_face()
            # Profile area: 169.6460032938, perimeter: 56.5486677646
            with BuildLine():
                CenterArc((0, 0), 7.5, -180, 180)
                CenterArc((0, 0), 7.5, 0, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=8
        extrude(amount=8, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 131.3165965236, perimeter: 46.2292921504
            with BuildLine():
                Line((-5, 8.4409715081), (-5, 21.5))
                Line((5.0556175832, 8.4409715081), (-5, 8.4409715081))
                Line((5.0556175832, 21.5), (5.0556175832, 8.4409715081))
                Line((5.0556175832, 21.5), (-5, 21.5))
            make_face()
            # Profile area: 25.1390439581, perimeter: 25.1112351665
            with BuildLine():
                Line((-5, 21.5), (-5, 24))
                Line((5.0556175832, 21.5), (-5, 21.5))
                Line((5.0556175832, 24), (5.0556175832, 21.5))
                Line((-5, 24), (5.0556175832, 24))
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.SUBTRACT)
    return part.part


def model_60767_0746a46e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 119.5596687091, perimeter: 43.7373376397
            with BuildLine():
                Line((5.4669031661, -5.4674312439), (-5.4669031661, -5.4674312439))
                Line((5.4669031661, 5.4674312439), (5.4669031661, -5.4674312439))
                Line((-5.4669031661, 5.4674312439), (5.4669031661, 5.4674312439))
                Line((-5.4669031661, -5.4674312439), (-5.4669031661, 5.4674312439))
            make_face()
        # OneSide extrude, distance=4.1727
        extrude(amount=4.1727)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.1727, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.9977978492, perimeter: 26.6519846024
            with BuildLine():
                Line((-2.4773722987, -2.9995069556), (2.3176995875, -2.9995069556))
                Line((-2.4773722987, -5.4674312439), (-2.4773722987, -2.9995069556))
                Line((2.3176995875, -5.4674312439), (-2.4773722987, -5.4674312439))
                Line((2.3176995875, -2.9995069556), (2.3176995875, -5.4674312439))
            make_face()
            with BuildLine():
                Line((2.0176995756, -3.2995069676), (2.0176995756, -5.1674312319))
                Line((2.0176995756, -5.1674312319), (-2.1773722868, -5.1674312319))
                Line((-2.1773722868, -5.1674312319), (-2.1773722868, -3.2995069676))
                Line((-2.1773722868, -3.2995069676), (2.0176995756, -3.2995069676))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.3245395616, perimeter: 35.4969304106
            with BuildLine():
                Line((-5.4669031661, -5.4674312439), (-5.4669031661, 1.0172704915))
                Line((-2.4773722987, -5.4674312439), (-5.4669031661, -5.4674312439))
                Line((-2.4773722987, -5.4674312439), (-2.4773722987, -2.9995069556))
                Line((-2.4773722987, 1.0172704915), (-2.4773722987, -2.9995069556))
                Line((-5.4669031661, 1.0172704915), (-2.4773722987, 1.0172704915))
            make_face()
            with BuildLine():
                Line((-2.7773722987, 0.7172704915), (-2.7773722987, -5.1674312439))
                Line((-2.7773722987, -5.1674312439), (-5.1669031661, -5.1674312439))
                Line((-5.1669031661, -5.1674312439), (-5.1669031661, 0.7172704915))
                Line((-5.1669031661, 0.7172704915), (-2.7773722987, 0.7172704915))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.3695494115, perimeter: 35.7969960766
            with BuildLine():
                Line((2.3176995875, -2.9995069556), (2.3176995875, -5.4674312439))
                Line((2.3176995875, -5.4674312439), (5.4669031661, -5.4674312439))
                Line((5.4669031661, -5.4674312439), (5.4669031661, 0.9326141967))
                Line((5.4669031661, 0.9326141967), (2.3176995875, 0.9326141967))
                Line((2.3176995875, 0.9326141967), (2.3176995875, -2.9995069556))
            make_face()
            with BuildLine():
                Line((2.6176995875, 0.6326141967), (2.6176995875, -5.1674312439))
                Line((5.1669031661, 0.6326141967), (2.6176995875, 0.6326141967))
                Line((5.1669031661, -5.1674312439), (5.1669031661, 0.6326141967))
                Line((2.6176995875, -5.1674312439), (5.1669031661, -5.1674312439))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_60860_249af7ce_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.7079632679, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.0458249062, perimeter: 14.1223549572
            with BuildLine():
                CenterArc((0, 0), 3, -30, 61.4254004803)
                Line((5, -1.5), (2.5980762114, -1.5))
                Line((5, -0.5), (5, -1.5))
                Line((3.5, -0.5), (5, -0.5))
                Line((3.5, 0.5), (3.5, -0.5))
                Line((5, 0.5), (3.5, 0.5))
                Line((5, 1.5641639355), (5, 0.5))
                Line((2.5599592151, 1.5641639355), (5, 1.5641639355))
            make_face()
            # Profile area: 7.0717282575, perimeter: 18.0914229969
            with BuildLine():
                Line((-6, 1.5530308328), (-6, 0.5))
                Line((-6, 0.5), (-3.5, 0.5))
                Line((-3.5, 0.5), (-3.5, -0.5))
                Line((-3.5, -0.5), (-6, -0.5))
                Line((-6, -0.5), (-6, -1.5))
                Line((-6, -1.5), (-2.5980762114, -1.5))
                CenterArc((0, 0), 3, 148.8234458811, 61.1765541189)
                Line((-2.5667285077, 1.5530308328), (-6, 1.5530308328))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_60865_19bbdeb4_0003():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3653544672, perimeter: 2.25
            with BuildLine():
                Line((0.1875, 0.3247595264), (0.375, 0))
                Line((-0.1875, 0.3247595264), (0.1875, 0.3247595264))
                Line((-0.375, 0), (-0.1875, 0.3247595264))
                Line((-0.1875, -0.3247595264), (-0.375, 0))
                Line((0.1875, -0.3247595264), (-0.1875, -0.3247595264))
                Line((0.375, 0), (0.1875, -0.3247595264))
            make_face()
        # OneSide extrude, distance=0.313
        extrude(amount=0.313)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_60996_662df59e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6584396144, perimeter: 5.5678868101
            with BuildLine():
                CenterArc((0, 0), 7.4, -17.2640689174, 15.6247900441)
                Line((7.0666085415, -2.1961429192), (8.1126129745, -2.1046293893))
                Line((8.3403312296, -0.6727468344), (8.1126129745, -2.1046293893))
                Line((7.3969714656, -0.2116911376), (8.3403312296, -0.6727468344))
            make_face()
        # Symmetric extrude, each_side=1.8
        extrude(amount=1.8, both=True)
    return part.part


def model_61091_f7d8529d_0002():
    """Model: Component3"""
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
        # Symmetric extrude, each_side=1.65
        extrude(amount=1.65, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_61198_0c99f50a_0005():
    """Model: 支撐桿"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 174.8102047457, perimeter: 151.9783939411
            with BuildLine():
                Line((-88.4456106641, 0.3102432409), (-33.8456106641, 0.3102432409))
                Line((-33.8456106641, 0.3102432409), (-27.5761759728, 1.6384708764))
                CenterArc((-27.8456106641, 2.9102432409), 1.3, -78.038319676, 180.5516450388)
                Line((-33.8456106641, 2.9102432409), (-28.1272773307, 4.1793625768))
                Line((-33.8456106641, 2.9102432409), (-88.4456106641, 2.9102432409))
                Line((-88.4456106641, 2.9102432409), (-94.1639439974, 4.1793625768))
                CenterArc((-94.4456106641, 2.9102432409), 1.3, 77.4866746371, 180.5516450388)
                Line((-88.4456106641, 0.3102432409), (-94.7150453554, 1.6384708764))
            make_face()
            with BuildLine():
                CenterArc((-94.4456106641, 2.9102432409), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-27.8456106641, 2.9102432409), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> 拉伸2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 60.8337498843, perimeter: 103.2745387323
            with BuildLine():
                CenterArc((-84.8456106641, 1.6102432409), 0.6, 89.9663913878, 179.9999991462)
                Line((-84.8459626216, 1.0102433441), (-35.093657389, 0.9810595868))
                CenterArc((-35.0933054405, 1.5810594836), 0.6, -90.0336086122, 179.9999991462)
                Line((-35.0929534919, 2.1810593803), (-84.8452587155, 2.2102431377))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_61198_0c99f50a_0006():
    """Model: 輪軸承"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5969026042, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((13.2302192627, 5.2054150802), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((13.2302192627, 5.2054150802), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2748893572, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((13.2302192627, 5.2054150802), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((13.2302192627, 5.2054150802), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8, mode=Mode.ADD)

        # Sketch1 -> 拉伸3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9424777961, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((13.2302192627, 5.2054150802), 0.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((13.2302192627, 5.2054150802), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.95
        extrude(amount=3.95, mode=Mode.ADD)
    return part.part


def model_61198_0c99f50a_0007():
    """Model: 輪架軸承"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.730420292, perimeter: 9.7389372261
            with BuildLine():
                CenterArc((-3.4971777081, 12.7397187936), 0.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.4971777081, 12.7397187936), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2748893572, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((-3.4971777081, 12.7397187936), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.4971777081, 12.7397187936), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.85
        extrude(amount=3.85, mode=Mode.ADD)

        # Sketch1 -> 拉伸3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5969026042, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((-3.4971777081, 12.7397187936), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.4971777081, 12.7397187936), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8, mode=Mode.ADD)
    return part.part


def model_61198_0c99f50a_0009():
    """Model: 傳動軸"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-63.3213480194, -12.6956803418)):
                Circle(0.8)
        # Symmetric extrude, each_side=13
        extrude(amount=13, both=True)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((-63.3213480194, -12.6956803418), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-63.3213480194, -12.6956803418), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=11
        extrude(amount=11, both=True, mode=Mode.ADD)

        # Sketch1 -> 拉伸3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((-63.3213480194, -12.6956803418), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-63.3213480194, -12.6956803418), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True, mode=Mode.ADD)
    return part.part


def model_61198_0c99f50a_0010():
    """Model: 底座螺栓"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((9.1574165787, -26.9133095101)):
                Circle(0.6)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((9.1574165787, -26.9133095101), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((9.1574165787, -26.9133095101), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((9.1574165787, -26.9133095101)):
                Circle(0.6)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch2 -> 拉伸3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.2170250337, perimeter: 5.5425625842
            with BuildLine():
                Line((9.6192967941, 27.7133095101), (8.6955363634, 27.7133095101))
                Line((8.6955363634, 27.7133095101), (8.233656148, 26.9133095101))
                Line((8.233656148, 26.9133095101), (8.6955363634, 26.1133095101))
                Line((8.6955363634, 26.1133095101), (9.6192967941, 26.1133095101))
                Line((9.6192967941, 26.1133095101), (10.0811770094, 26.9133095101))
                Line((10.0811770094, 26.9133095101), (9.6192967941, 27.7133095101))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_61198_0c99f50a_0014():
    """Model: 輪軸栓"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.879645943, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((8.4233820844, 5.3382945678), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.4233820844, 5.3382945678), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((8.4233820844, 5.3382945678)):
                Circle(0.6)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((8.4233820844, 5.3382945678)):
                Circle(0.6)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.ADD)

        # Sketch2 -> 拉伸3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9353074361, perimeter: 3.6
            with BuildLine():
                Line((8.9429973266, 5.6382945678), (8.4233820844, 5.9382945678))
                Line((8.4233820844, 5.9382945678), (7.9037668421, 5.6382945678))
                Line((7.9037668421, 5.6382945678), (7.9037668421, 5.0382945678))
                Line((7.9037668421, 5.0382945678), (8.4233820844, 4.7382945678))
                Line((8.4233820844, 4.7382945678), (8.9429973266, 5.0382945678))
                Line((8.9429973266, 5.0382945678), (8.9429973266, 5.6382945678))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_61198_0c99f50a_0015():
    """Model: 控制器"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 44 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 178.2532698248, perimeter: 66.5530076949
            with BuildLine():
                CenterArc((-49.3966828168, 32.6557767238), 1.2, 90, 90)
                Line((-50.5966828168, 29.1344245887), (-50.5966828168, 32.6557767238))
                CenterArc((-49.3966828168, 29.1344245887), 1.2, -180, 90)
                Line((-45.7166828168, 27.9344245887), (-49.3966828168, 27.9344245887))
                CenterArc((-45.7166828168, 26.7344245887), 1.2, 0, 90)
                Line((-44.5166828168, 26.7344245887), (-44.5166828168, 22.8834383301))
                CenterArc((-43.3166828168, 22.8834383301), 1.2, 180, 90.0563673375)
                Line((-43.3155022623, 21.6834389108), (-39.8440502637, 21.6868541112))
                CenterArc((-39.8452308183, 22.8868535305), 1.2, -89.9436326625, 90.0473043438)
                Line((-38.6452327827, 22.889024824), (-38.6521867747, 26.7322532953))
                CenterArc((-37.452188739, 26.7344245887), 1.2, 90, 90.1036716813)
                Line((-33.6366828168, 27.9344245887), (-37.452188739, 27.9344245887))
                CenterArc((-33.6366828168, 29.1344245887), 1.2, -90, 90)
                Line((-32.4366828168, 32.6557767238), (-32.4366828168, 29.1344245887))
                CenterArc((-33.6366828168, 32.6557767238), 1.2, 0, 90)
                Line((-37.4672455114, 33.8557767238), (-33.6366828168, 33.8557767238))
                CenterArc((-37.4672455114, 35.0557767238), 1.2, -179.8963283187, 89.8963283187)
                Line((-38.667243547, 35.0536054304), (-38.6738359708, 38.6970077894))
                CenterArc((-39.8738340064, 38.694836496), 1.2, 0.1036716813, 90)
                Line((-39.8760052999, 39.8948345316), (-43.3188541103, 39.8886049922))
                CenterArc((-43.3166828168, 38.6886069566), 1.2, 90.1036716813, 89.8963283187)
                Line((-44.5166828168, 38.6886069566), (-44.5166828168, 35.0557767238))
                CenterArc((-45.7166828168, 35.0557767238), 1.2, -90, 90)
                Line((-49.3966828168, 33.8557767238), (-45.7166828168, 33.8557767238))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> 拉伸2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9228357378, perimeter: 7.7942286341
            with BuildLine():
                Line((34.0885238787, -30.7956334549), (36.3397699535, -32.092510901))
                Line((36.3397699535, -32.092510901), (36.33727573, -29.4944358869))
                Line((36.33727573, -29.4944358869), (34.0885238787, -30.7956334549))
            make_face()
            # Profile area: 2.9228357378, perimeter: 7.7942286341
            with BuildLine():
                Line((42.8825177874, -25.5371885594), (41.5813202194, -23.288436708))
                Line((41.5813202194, -23.288436708), (40.2844427733, -25.5396827829))
                Line((40.2844427733, -25.5396827829), (42.8825177874, -25.5371885594))
            make_face()
            # Profile area: 2.9228357378, perimeter: 7.7942286341
            with BuildLine():
                Line((49.0885169663, -30.7812330487), (46.8372708914, -29.4843556026))
                Line((46.8372708914, -29.4843556026), (46.8397651149, -32.0824306167))
                Line((46.8397651149, -32.0824306167), (49.0885169663, -30.7812330487))
            make_face()
            # Profile area: 2.9228357378, perimeter: 7.7942286341
            with BuildLine():
                Line((41.5957206255, -38.2884297956), (42.8925980717, -36.0371837207))
                Line((42.8925980717, -36.0371837207), (40.2945230576, -36.0396779442))
                Line((40.2945230576, -36.0396779442), (41.5957206255, -38.2884297956))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_61198_0c99f50a_0016():
    """Model: 輪架螺栓"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-11.6109394672, 11.5055542107), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-11.6109394672, 11.5055542107), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-11.6109394672, 11.5055542107)):
                Circle(0.7)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> 拉伸2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-11.6109394672, 11.5055542107)):
                Circle(0.7)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.ADD)

        # Sketch2 -> 拉伸3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2730573436, perimeter: 4.2
            with BuildLine():
                Line((-11.0065594776, 11.8587182352), (-11.6145984893, 12.2055446475))
                Line((-11.6145984893, 12.2055446475), (-12.2189784789, 11.8523806231))
                Line((-12.2189784789, 11.8523806231), (-12.2153194568, 11.1523901863))
                Line((-12.2153194568, 11.1523901863), (-11.6072804451, 10.805563774))
                Line((-11.6072804451, 10.805563774), (-11.0029004555, 11.1587277984))
                Line((-11.0029004555, 11.1587277984), (-11.0065594776, 11.8587182352))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_61257_7a82d02b_0000():
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
        # Sketch has 39 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.3364146884, perimeter: 80.7268312603
            with BuildLine():
                Line((-3.836546569, 9.9999999989), (-14.599590623, 10))
                CenterArc((-14.5995906231, 9.5), 0.5, 89.9999999943, 78.2773792881)
                _nurbs_edge([(-15.0891619594, 9.6015869412), (-15.0936941568, 9.5797452171), (-15.1189923364, 9.4564881155), (-15.162198748, 9.2320104165), (-15.2170861773, 8.9067365573), (-15.2734234848, 8.4813638767), (-15.3151116869, 7.9785224731), (-15.3295713432, 7.4775369252), (-15.3155860494, 6.9784901412), (-15.2741872278, 6.4813118211), (-15.2074046604, 5.985863618), (-15.1353178944, 5.5907769409), (-15.0714203995, 5.2951320956), (-15.0245232819, 5.0983285309), (-15, 5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0784671834, 0.0784671834, 0.0784671834, 0.0784671834, 0.0784671834, 0.0784671834, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-15, 5), (-9, 5))
                _nurbs_edge([(-8.8716931473, 8.6948976183), (-8.8576978727, 8.6302584414), (-8.8268825325, 8.4813267211), (-8.7838597394, 8.2481024575), (-8.7368970292, 7.9305856506), (-8.6991055054, 7.5287763003), (-8.6855342537, 7.1073135836), (-8.6991055054, 6.6858508669), (-8.7387454945, 6.2643881502), (-8.8024873274, 5.8429254334), (-8.8711804658, 5.5057552601), (-8.9320236336, 5.25287763), (-8.9766618411, 5.0842925433), (-9, 5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1233156643, 0.1233156643, 0.1233156643, 0.1233156643, 0.1233156643, 0.1233156643, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-8.3830161239, 8.8007029433), 0.5, 98.3210722857, 93.8956848782)
                _nurbs_edge([(-8.4553761838, 9.2954392587), (-8.3592491832, 9.3094987795), (-8.1573045083, 9.3388469747), (-7.8441951362, 9.3837184059), (-7.4113237588, 9.4441513213), (-6.84797315, 9.5178227173), (-6.2583799288, 9.584863483), (-5.6566420357, 9.6350489354), (-5.0519063472, 9.6541409088), (-4.4562135771, 9.6247772052), (-3.8832331689, 9.5298074687), (-3.3472047566, 9.3553568432), (-2.8618419377, 9.0938328387), (-2.4390829624, 8.7477986522), (-2.0882424333, 8.3316227849), (-1.8164954262, 7.8663773694), (-1.6290053107, 7.3759906602), (-1.5291143799, 6.8833065915), (-1.5182862075, 6.4055619824), (-1.594645838, 5.9621898953), (-1.7219728456, 5.6314505686), (-1.8529066972, 5.3983382527), (-1.9540258604, 5.2512569629), (-2.0050963233, 5.1831637961)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0537045577, 0.0537045577, 0.0537045577, 0.0537045577, 0.0537045577, 0.0537045577, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.9945341283, 0.9945341283, 0.9945341283, 0.9945341283, 0.9945341283, 0.9945341283], 5)
                CenterArc((-1.9250966548, 5.1231633541), 0.1, 143.1297858211, 106.0776866468)
                _nurbs_edge([(-1.9605951588, 5.029676156), (-1.9546061751, 5.0274020482), (-1.9420100847, 5.0230545476), (-1.9214557831, 5.0171817162), (-1.8909727523, 5.0105828747), (-1.8567937053, 5.005483285), (-1.829142471, 5.0024392326), (-1.8098562028, 5.000755515), (-1.8000000268, 5.0000000745)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.6010522862, 0.6010522862, 0.6010522862, 0.6010522862, 0.6010522862, 0.6010522862, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-1.8000000268, 5.0000000745), (-1.5195575191, 5.0000000996))
                _nurbs_edge([(-3.7095197474, 9.9835950636), (-3.3991820995, 9.9020780922), (-3.0995099376, 9.7846466932), (-2.8223571848, 9.6261148125), (-2.3745638637, 9.3699762153), (-1.9913002752, 9.009049533), (-1.7004281017, 8.5952557442), (-1.3282667216, 8.0658201998), (-1.1005612289, 7.4569429087), (-1.043904513, 6.8597235652), (-0.9966151734, 6.3612458853), (-1.0736161123, 5.8673664259), (-1.2776011677, 5.4237306874), (-1.3451941759, 5.2767264176), (-1.4262114828, 5.1352824678), (-1.5195575191, 5.0000000996)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4748504977, 0.4748504977, 0.4748504977, 0.4748504977, 0.5475354185, 0.5475354185, 0.5475354185, 0.6649718205, 0.6649718205, 0.6649718205, 0.8152278348, 0.8152278348, 0.8152278348, 0.9406411694, 0.9406411694, 0.9406411694, 0.9821984518, 0.9821984518, 0.9821984518, 0.9821984518], 3)
                CenterArc((-3.836546569, 9.4999999989), 0.5, 75.2824836842, 14.7175163101)
            make_face()
            with BuildLine():
                _nurbs_edge([(-9.4511522677, 9.3536255593), (-9.446964692, 9.3385796003), (-9.4390096295, 9.3087079072), (-9.4283372858, 9.2645608336), (-9.4166312373, 9.2067180473), (-9.406752953, 9.137800988), (-9.4020799074, 9.0820271182), (-9.4003891978, 9.039755073), (-9.4000239325, 9.0121370318), (-9.4000001401, 9.0000001341)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716], 5)
                _nurbs_edge([(-9.4000001401, 9.0000001341), (-9.3999534126, 8.9959653019), (-9.3997477788, 8.9699777548), (-9.4004957925, 8.9217064357), (-9.404607953, 8.8504340649), (-9.4148658714, 8.7612489748), (-9.4299743268, 8.6746692717), (-9.4436660669, 8.6105111334), (-9.4533605429, 8.5695424403), (-9.4576335253, 8.5521869934)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.5, 0.6, 0.7, 0.8, 0.8731088977, 0.8731088977, 0.8731088977, 0.8731088977, 0.8731088977, 0.8731088977], 5)
                CenterArc((-9.6518342354, 8.600000006), 0.2, -90, 76.1686337971)
                Line((-9.6518342354, 8.400000006), (-14.4414462357, 8.400000006))
                CenterArc((-14.4414462357, 8.600000006), 0.2, -167.3393127543, 77.3393127543)
                _nurbs_edge([(-14.6485693767, 9.3537492944), (-14.6524581604, 9.3398115549), (-14.6599581114, 9.3118586107), (-14.6703750949, 9.2696966611), (-14.6824448879, 9.2128218639), (-14.6936396707, 9.1396074682), (-14.6999360601, 9.0631556372), (-14.7005124867, 8.9826754865), (-14.6952265295, 8.8982841837), (-14.684937501, 8.8113695209), (-14.6709200993, 8.7238934606), (-14.6578010848, 8.6551280973), (-14.6473684586, 8.6049960001), (-14.6402119115, 8.5723178789), (-14.6365832675, 8.5561646455)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-14.4559271895, 9.2999999901), 0.2, 90, 74.4103087896)
                Line((-14.4559271895, 9.4999999901), (-9.6438289355, 9.4999999901))
                CenterArc((-9.6438289355, 9.2999999901), 0.2, 15.5528931145, 74.4471068855)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-14.4561713364, 8.1000001177), (-9.6438289505, 8.1000001177))
                CenterArc((-9.6438289505, 7.9000001177), 0.2, 15.5528906246, 74.4471093754)
                _nurbs_edge([(-9.4511522804, 7.9536256786), (-9.448114663, 7.9427115177), (-9.4397181408, 7.9113919743), (-9.427271663, 7.8592775522), (-9.4132838698, 7.7856217699), (-9.4017791418, 7.6892271161), (-9.3977149551, 7.5804364707), (-9.4024700583, 7.4690215209), (-9.4148658699, 7.3612490171), (-9.4299743241, 7.2746693284), (-9.4436660629, 7.2105112038), (-9.4533605377, 7.1695425219), (-9.4576335188, 7.1521870824)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786], 5)
                CenterArc((-9.6518342274, 7.2000001013), 0.2, -90, 76.1686319314)
                Line((-9.6518342274, 7.0000001013), (-14.44816605, 7.0000001013))
                CenterArc((-14.44816605, 7.2000001013), 0.2, -166.1686114882, 76.1686114882)
                _nurbs_edge([(-14.6488479838, 7.9536257601), (-14.6518856106, 7.9427115833), (-14.6602821503, 7.9113920243), (-14.6727286511, 7.8592775865), (-14.6867164685, 7.7856217882), (-14.6982212148, 7.6892271178), (-14.7022854072, 7.5804364725), (-14.6975302974, 7.4690215226), (-14.6851344667, 7.3612490051), (-14.6700259878, 7.2746693022), (-14.6563342255, 7.2105111631), (-14.6466397327, 7.1695424668), (-14.6423667415, 7.1521870131)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376], 5)
                CenterArc((-14.4561713364, 7.9000001177), 0.2, 90, 74.4470851409)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-14.4579788158, 6.681167223), (-9.6420215433, 6.681167223))
                CenterArc((-9.6420215433, 6.481167223), 0.2, 15.8851626535, 74.1148373465)
                _nurbs_edge([(-9.4496590989, 6.5359092543), (-9.4468995046, 6.526212093), (-9.4387993347, 6.4967011727), (-9.4266356688, 6.4468537027), (-9.4128942715, 6.3756520994), (-9.4015704946, 6.2814608081), (-9.3976376389, 6.1730707775), (-9.4025225874, 6.061071052), (-9.4150792223, 5.951185048), (-9.4303749, 5.8621777777), (-9.444266985, 5.7957450887), (-9.4541677105, 5.7529463205), (-9.4586382545, 5.7343704754)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106], 5)
                CenterArc((-9.6530863606, 5.7811672066), 0.2, -90, 76.4682796333)
                Line((-9.6530863606, 5.5811672066), (-14.4469139985, 5.5811672066))
                CenterArc((-14.4469139985, 5.7811672066), 0.2, -166.4682796328, 76.4682796328)
                _nurbs_edge([(-14.6503412602, 6.5359092543), (-14.6531008545, 6.526212093), (-14.6612010244, 6.4967011727), (-14.6733646904, 6.4468537027), (-14.6871060876, 6.3756520994), (-14.6984298645, 6.2814608081), (-14.7023627202, 6.1730707775), (-14.6974777718, 6.061071052), (-14.6849211368, 5.951185048), (-14.6696254591, 5.8621777777), (-14.6557333741, 5.7957450887), (-14.6458326487, 5.7529463205), (-14.6413621046, 5.7343704754)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106], 5)
                CenterArc((-14.4579788158, 6.481167223), 0.2, 90, 74.1148373464)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.000171831, perimeter: 0.7167870142
            with BuildLine():
                _nurbs_edge([(-9.4511522672, 9.3536255595), (-9.4481146524, 9.3427114094), (-9.439718133, 9.3113918814), (-9.4272716579, 9.2592774782), (-9.4140116273, 9.1894538973), (-9.40526167, 9.1182882768), (-9.4013144302, 9.0575115738), (-9.40020732, 9.0178897479), (-9.4000001401, 9.0000001341)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.2, 0.3, 0.4, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515], 5)
                _nurbs_edge([(-9.4511522677, 9.3536255593), (-9.446964692, 9.3385796003), (-9.4390096295, 9.3087079072), (-9.4283372858, 9.2645608336), (-9.4166312373, 9.2067180473), (-9.406752953, 9.137800988), (-9.4020799074, 9.0820271182), (-9.4003891978, 9.039755073), (-9.4000239325, 9.0121370318), (-9.4000001401, 9.0000001341)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716], 5)
            make_face()
            # Profile area: 5.734113196, perimeter: 12.2757549844
            with BuildLine():
                CenterArc((-9.6438289355, 9.2999999901), 0.2, 15.5528931145, 74.4471068855)
                Line((-14.4559271895, 9.4999999901), (-9.6438289355, 9.4999999901))
                CenterArc((-14.4559271895, 9.2999999901), 0.2, 90, 74.4103087896)
                _nurbs_edge([(-14.6485693767, 9.3537492944), (-14.6524581604, 9.3398115549), (-14.6599581114, 9.3118586107), (-14.6703750949, 9.2696966611), (-14.6824448879, 9.2128218639), (-14.6936396707, 9.1396074682), (-14.6999360601, 9.0631556372), (-14.7005124867, 8.9826754865), (-14.6952265295, 8.8982841837), (-14.684937501, 8.8113695209), (-14.6709200993, 8.7238934606), (-14.6578010848, 8.6551280973), (-14.6473684586, 8.6049960001), (-14.6402119115, 8.5723178789), (-14.6365832675, 8.5561646455)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-14.4414462357, 8.600000006), 0.2, -167.3393127543, 77.3393127543)
                Line((-9.6518342354, 8.400000006), (-14.4414462357, 8.400000006))
                CenterArc((-9.6518342354, 8.600000006), 0.2, -90, 76.1686337971)
                _nurbs_edge([(-9.4000001401, 9.0000001341), (-9.3999930578, 8.9963873391), (-9.4000192956, 8.9769693472), (-9.4006903689, 8.9412135021), (-9.403291242, 8.8879638025), (-9.4096887263, 8.8157870666), (-9.4214067513, 8.728178738), (-9.4339592529, 8.657477643), (-9.4451192574, 8.6046765199), (-9.453333119, 8.5696538272), (-9.4576335253, 8.5521869934)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-9.4511522672, 9.3536255595), (-9.4481146524, 9.3427114094), (-9.439718133, 9.3113918814), (-9.4272716579, 9.2592774782), (-9.4140116273, 9.1894538973), (-9.40526167, 9.1182882768), (-9.4013144302, 9.0575115738), (-9.40020732, 9.0178897479), (-9.4000001401, 9.0000001341)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.2, 0.3, 0.4, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515], 5)
            make_face()
            # Profile area: 0.0002771871, perimeter: 0.905271197
            with BuildLine():
                _nurbs_edge([(-9.4000001401, 9.0000001341), (-9.3999930578, 8.9963873391), (-9.4000192956, 8.9769693472), (-9.4006903689, 8.9412135021), (-9.403291242, 8.8879638025), (-9.4096887263, 8.8157870666), (-9.4214067513, 8.728178738), (-9.4339592529, 8.657477643), (-9.4451192574, 8.6046765199), (-9.453333119, 8.5696538272), (-9.4576335253, 8.5521869934)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-9.4000001401, 9.0000001341), (-9.3999534126, 8.9959653019), (-9.3997477788, 8.9699777548), (-9.4004957925, 8.9217064357), (-9.404607953, 8.8504340649), (-9.4148658714, 8.7612489748), (-9.4299743268, 8.6746692717), (-9.4436660669, 8.6105111334), (-9.4533605429, 8.5695424403), (-9.4576335253, 8.5521869934)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.5, 0.6, 0.7, 0.8, 0.8731088977, 0.8731088977, 0.8731088977, 0.8731088977, 0.8731088977, 0.8731088977], 5)
            make_face()
            # Profile area: 5.737766962, perimeter: 12.2822512837
            with BuildLine():
                CenterArc((-14.4561713364, 7.9000001177), 0.2, 90, 74.4470851409)
                _nurbs_edge([(-14.6488479838, 7.9536257601), (-14.6518856106, 7.9427115833), (-14.6602821503, 7.9113920243), (-14.6727286511, 7.8592775865), (-14.6867164685, 7.7856217882), (-14.6982212148, 7.6892271178), (-14.7022854072, 7.5804364725), (-14.6975302974, 7.4690215226), (-14.6851344667, 7.3612490051), (-14.6700259878, 7.2746693022), (-14.6563342255, 7.2105111631), (-14.6466397327, 7.1695424668), (-14.6423667415, 7.1521870131)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376], 5)
                CenterArc((-14.44816605, 7.2000001013), 0.2, -166.1686114882, 76.1686114882)
                Line((-9.6518342274, 7.0000001013), (-14.44816605, 7.0000001013))
                CenterArc((-9.6518342274, 7.2000001013), 0.2, -90, 76.1686319314)
                _nurbs_edge([(-9.4511522804, 7.9536256786), (-9.448114663, 7.9427115177), (-9.4397181408, 7.9113919743), (-9.427271663, 7.8592775522), (-9.4132838698, 7.7856217699), (-9.4017791418, 7.6892271161), (-9.3977149551, 7.5804364707), (-9.4024700583, 7.4690215209), (-9.4148658699, 7.3612490171), (-9.4299743241, 7.2746693284), (-9.4436660629, 7.2105112038), (-9.4533605377, 7.1695425219), (-9.4576335188, 7.1521870824)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786], 5)
                CenterArc((-9.6438289505, 7.9000001177), 0.2, 15.5528906246, 74.4471093754)
                Line((-14.4561713364, 8.1000001177), (-9.6438289505, 8.1000001177))
            make_face()
            # Profile area: 5.7379320272, perimeter: 12.2832296354
            with BuildLine():
                CenterArc((-14.4579788158, 6.481167223), 0.2, 90, 74.1148373464)
                _nurbs_edge([(-14.6503412602, 6.5359092543), (-14.6531008545, 6.526212093), (-14.6612010244, 6.4967011727), (-14.6733646904, 6.4468537027), (-14.6871060876, 6.3756520994), (-14.6984298645, 6.2814608081), (-14.7023627202, 6.1730707775), (-14.6974777718, 6.061071052), (-14.6849211368, 5.951185048), (-14.6696254591, 5.8621777777), (-14.6557333741, 5.7957450887), (-14.6458326487, 5.7529463205), (-14.6413621046, 5.7343704754)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106], 5)
                CenterArc((-14.4469139985, 5.7811672066), 0.2, -166.4682796328, 76.4682796328)
                Line((-9.6530863606, 5.5811672066), (-14.4469139985, 5.5811672066))
                CenterArc((-9.6530863606, 5.7811672066), 0.2, -90, 76.4682796333)
                _nurbs_edge([(-9.4496590989, 6.5359092543), (-9.4468995046, 6.526212093), (-9.4387993347, 6.4967011727), (-9.4266356688, 6.4468537027), (-9.4128942715, 6.3756520994), (-9.4015704946, 6.2814608081), (-9.3976376389, 6.1730707775), (-9.4025225874, 6.061071052), (-9.4150792223, 5.951185048), (-9.4303749, 5.8621777777), (-9.444266985, 5.7957450887), (-9.4541677105, 5.7529463205), (-9.4586382545, 5.7343704754)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106], 5)
                CenterArc((-9.6420215433, 6.481167223), 0.2, 15.8851626535, 74.1148373465)
                Line((-14.4579788158, 6.681167223), (-9.6420215433, 6.681167223))
            make_face()
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.7379320272, perimeter: 12.2832296354
            with BuildLine():
                CenterArc((-14.4579788158, 6.481167223), 0.2, 90, 74.1148373464)
                _nurbs_edge([(-14.6503412602, 6.5359092543), (-14.6531008545, 6.526212093), (-14.6612010244, 6.4967011727), (-14.6733646904, 6.4468537027), (-14.6871060876, 6.3756520994), (-14.6984298645, 6.2814608081), (-14.7023627202, 6.1730707775), (-14.6974777718, 6.061071052), (-14.6849211368, 5.951185048), (-14.6696254591, 5.8621777777), (-14.6557333741, 5.7957450887), (-14.6458326487, 5.7529463205), (-14.6413621046, 5.7343704754)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106], 5)
                CenterArc((-14.4469139985, 5.7811672066), 0.2, -166.4682796328, 76.4682796328)
                Line((-9.6530863606, 5.5811672066), (-14.4469139985, 5.5811672066))
                CenterArc((-9.6530863606, 5.7811672066), 0.2, -90, 76.4682796333)
                _nurbs_edge([(-9.4496590989, 6.5359092543), (-9.4468995046, 6.526212093), (-9.4387993347, 6.4967011727), (-9.4266356688, 6.4468537027), (-9.4128942715, 6.3756520994), (-9.4015704946, 6.2814608081), (-9.3976376389, 6.1730707775), (-9.4025225874, 6.061071052), (-9.4150792223, 5.951185048), (-9.4303749, 5.8621777777), (-9.444266985, 5.7957450887), (-9.4541677105, 5.7529463205), (-9.4586382545, 5.7343704754)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.1507870873, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106, 0.876117106], 5)
                CenterArc((-9.6420215433, 6.481167223), 0.2, 15.8851626535, 74.1148373465)
                Line((-14.4579788158, 6.681167223), (-9.6420215433, 6.681167223))
            make_face()
            # Profile area: 5.737766962, perimeter: 12.2822512837
            with BuildLine():
                CenterArc((-14.4561713364, 7.9000001177), 0.2, 90, 74.4470851409)
                _nurbs_edge([(-14.6488479838, 7.9536257601), (-14.6518856106, 7.9427115833), (-14.6602821503, 7.9113920243), (-14.6727286511, 7.8592775865), (-14.6867164685, 7.7856217882), (-14.6982212148, 7.6892271178), (-14.7022854072, 7.5804364725), (-14.6975302974, 7.4690215226), (-14.6851344667, 7.3612490051), (-14.6700259878, 7.2746693022), (-14.6563342255, 7.2105111631), (-14.6466397327, 7.1695424668), (-14.6423667415, 7.1521870131)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.1462815263, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376, 0.8731089376], 5)
                CenterArc((-14.44816605, 7.2000001013), 0.2, -166.1686114882, 76.1686114882)
                Line((-9.6518342274, 7.0000001013), (-14.44816605, 7.0000001013))
                CenterArc((-9.6518342274, 7.2000001013), 0.2, -90, 76.1686319314)
                _nurbs_edge([(-9.4511522804, 7.9536256786), (-9.448114663, 7.9427115177), (-9.4397181408, 7.9113919743), (-9.427271663, 7.8592775522), (-9.4132838698, 7.7856217699), (-9.4017791418, 7.6892271161), (-9.3977149551, 7.5804364707), (-9.4024700583, 7.4690215209), (-9.4148658699, 7.3612490171), (-9.4299743241, 7.2746693284), (-9.4436660629, 7.2105112038), (-9.4533605377, 7.1695425219), (-9.4576335188, 7.1521870824)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.1462816057, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786, 0.8731088786], 5)
                CenterArc((-9.6438289505, 7.9000001177), 0.2, 15.5528906246, 74.4471093754)
                Line((-14.4561713364, 8.1000001177), (-9.6438289505, 8.1000001177))
            make_face()
            # Profile area: 5.734113196, perimeter: 12.2757549844
            with BuildLine():
                CenterArc((-9.6438289355, 9.2999999901), 0.2, 15.5528931145, 74.4471068855)
                Line((-14.4559271895, 9.4999999901), (-9.6438289355, 9.4999999901))
                CenterArc((-14.4559271895, 9.2999999901), 0.2, 90, 74.4103087896)
                _nurbs_edge([(-14.6485693767, 9.3537492944), (-14.6524581604, 9.3398115549), (-14.6599581114, 9.3118586107), (-14.6703750949, 9.2696966611), (-14.6824448879, 9.2128218639), (-14.6936396707, 9.1396074682), (-14.6999360601, 9.0631556372), (-14.7005124867, 8.9826754865), (-14.6952265295, 8.8982841837), (-14.684937501, 8.8113695209), (-14.6709200993, 8.7238934606), (-14.6578010848, 8.6551280973), (-14.6473684586, 8.6049960001), (-14.6402119115, 8.5723178789), (-14.6365832675, 8.5561646455)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-14.4414462357, 8.600000006), 0.2, -167.3393127543, 77.3393127543)
                Line((-9.6518342354, 8.400000006), (-14.4414462357, 8.400000006))
                CenterArc((-9.6518342354, 8.600000006), 0.2, -90, 76.1686337971)
                _nurbs_edge([(-9.4000001401, 9.0000001341), (-9.3999930578, 8.9963873391), (-9.4000192956, 8.9769693472), (-9.4006903689, 8.9412135021), (-9.403291242, 8.8879638025), (-9.4096887263, 8.8157870666), (-9.4214067513, 8.728178738), (-9.4339592529, 8.657477643), (-9.4451192574, 8.6046765199), (-9.453333119, 8.5696538272), (-9.4576335253, 8.5521869934)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.4770611716, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-9.4511522672, 9.3536255595), (-9.4481146524, 9.3427114094), (-9.439718133, 9.3113918814), (-9.4272716579, 9.2592774782), (-9.4140116273, 9.1894538973), (-9.40526167, 9.1182882768), (-9.4013144302, 9.0575115738), (-9.40020732, 9.0178897479), (-9.4000001401, 9.0000001341)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.1462816472, 0.2, 0.3, 0.4, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515, 0.4815966515], 5)
            make_face()
        # OneSide extrude, distance=-4.2
        extrude(amount=-4.2, mode=Mode.SUBTRACT)
    return part.part


def model_61377_2c5e62c1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.5, perimeter: 29
            with BuildLine():
                Line((11, -3.5), (0, -3.5))
                Line((11, 0), (11, -3.5))
                Line((0, 0), (11, 0))
                Line((0, -3.5), (0, 0))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 22, perimeter: 19
            with BuildLine():
                Line((6, 6.5), (0.5, 6.5))
                Line((6, 10.5), (6, 6.5))
                Line((0.5, 10.5), (6, 10.5))
                Line((0.5, 6.5), (0.5, 10.5))
            make_face()
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((10.5, 6.5), (6.5, 6.5))
                Line((10.5, 10.5), (10.5, 6.5))
                Line((6.5, 10.5), (10.5, 10.5))
                Line((6.5, 6.5), (6.5, 10.5))
            make_face()
            # Profile area: 14, perimeter: 15
            with BuildLine():
                Line((4.5, 2.5), (0.5, 2.5))
                Line((4.5, 6), (4.5, 2.5))
                Line((0.5, 6), (4.5, 6))
                Line((0.5, 2.5), (0.5, 6))
            make_face()
            # Profile area: 19.25, perimeter: 18
            with BuildLine():
                Line((10.5, 2.5), (5, 2.5))
                Line((10.5, 6), (10.5, 2.5))
                Line((5, 6), (10.5, 6))
                Line((5, 2.5), (5, 6))
            make_face()
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((10.5, 0.5), (0.5, 0.5))
                Line((10.5, 2), (10.5, 0.5))
                Line((0.5, 2), (10.5, 2))
                Line((0.5, 0.5), (0.5, 2))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_61412_df7154f9_0001():
    """Model: CUP v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_61495_24e309c1_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 348.0005878884, perimeter: 348.0005878884
            with BuildLine():
                Line((10, 25), (10, -10))
                Line((55, -20), (10, -10))
                Line((55, 35), (55, -20))
                Line((10, 25), (55, 35))
            make_face()
            with BuildLine():
                Line((12, 23.3956567873), (53, 32.5067678984))
                Line((53, 32.5067678984), (53, -17.5067678984))
                Line((53, -17.5067678984), (12, -8.3956567873))
                Line((12, 23.3956567873), (12, -8.3956567873))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_61643_303cdd31_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-3.5, 0)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, -3.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3.5, 0)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 3.5)):
                Circle(0.25)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.ADD)
    return part.part


def model_63132_330141d7_0003():
    """Model: Antenna"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((10, 5)):
                Circle(0.75)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((10, 5)):
                Circle(0.5)
        # OneSide extrude, distance=42.5
        extrude(amount=42.5, mode=Mode.ADD)
    return part.part


def model_63411_46a912fc_0002():
    """Model: Untitled v1 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6400000191, perimeter: 4.0000000596
            with BuildLine():
                Line((1.4000000209, 0.400000006), (1.0000000149, 0.400000006))
                Line((1.4000000209, 2.0000000298), (1.4000000209, 0.400000006))
                Line((1.0000000149, 2.0000000298), (1.4000000209, 2.0000000298))
                Line((1.0000000149, 0.400000006), (1.0000000149, 2.0000000298))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6000000179, perimeter: 3.7164913701
            with BuildLine():
                Line((1.9376968702, 1.4434547596), (1.7461538722, 1.7307692566))
                Line((1.7461538722, 1.7307692566), (1.4000000209, 1.5000000224))
                Line((1.4000000209, 1.5000000224), (2.2000000328, 0.3000000045))
                Line((2.2000000328, 0.3000000045), (2.5461538841, 0.5307692387))
                Line((2.5461538841, 0.5307692387), (1.9376968702, 1.4434547596))
            make_face()
            # Profile area: 0.6037214232, perimeter: 3.5583207143
            with BuildLine():
                Line((2.7699980391, 0.4153846216), (3.1247356981, 0.7025718059))
                Line((3.1247356981, 0.7025718059), (2.2924345291, 1.7306419439))
                Line((2.2924345291, 1.7306419439), (1.9376968702, 1.4434547596))
                Line((1.9376968702, 1.4434547596), (2.7699980391, 0.4153846216))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_64836_b59b00e7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 75.6167017892, perimeter: 65.4933614313
            with BuildLine():
                CenterArc((2, -1.5), 6.5, 0, 90)
                Line((-2.5, 5), (2, 5))
                Line((-2.5, 5), (-2.5, 2.5))
                Line((-2.5, 2.5), (2, 2.5))
                CenterArc((2, -1.5), 4, 0, 90)
                Line((6, -19), (6, -1.5))
                Line((8.5, -19), (6, -19))
                Line((8.5, -1.5), (8.5, -19))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_64965_49fab8b9_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 5.5)):
                Circle(1)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_65482_f5dcf75b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.3344298561, perimeter: 5.4162081519
            with Locations((-2.374727373, 2.1441926159)):
                Circle(0.8620163002)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


def model_65569_bd890a32_0006():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7425.1949427464, perimeter: 368.5853025629
            with BuildLine():
                CenterArc((10.6752080633, -5), 5, 90, 129.8055710923)
                Line((6.8341016653, -8.2009219983), (45.5023049958, -54.602765995))
                CenterArc((57.0256241898, -45), 15, -140.1944289077, 50.1944289077)
                Line((140, -60), (57.0256241898, -60))
                CenterArc((140, -50), 10, -90, 90)
                Line((150, -10), (150, -50))
                CenterArc((140, -10), 10, 0, 90)
                Line((10.6752080633, 0), (140, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 296.3975139747, perimeter: 658.6611421659
            with BuildLine():
                CenterArc((-16.0128120949, 7.5), 2.5, -90, 129.8055710923)
                Line((-14.0922588959, 9.1004609992), (-49.3434113938, 51.4018439966))
                CenterArc((-57.0256241898, 45), 10, 39.8055710923, 50.1944289077)
                Line((-57.0256241898, 55), (-140, 55))
                CenterArc((-140, 50), 5, 90, 90)
                Line((-145, 50), (-145, 10))
                CenterArc((-140, 10), 5, -180, 90)
                Line((-140, 5), (-16.0128120949, 5))
            make_face()
            with BuildLine():
                Line((-14.7836580475, 8.5242950395), (-50.0348105454, 50.8256780369))
                CenterArc((-16.0128120949, 7.5), 1.6, -90, 129.8055710923)
                Line((-140, 5.9), (-16.0128120949, 5.9))
                CenterArc((-140, 10), 4.1, -180, 90)
                Line((-144.1, 50), (-144.1, 10))
                CenterArc((-140, 50), 4.1, 90, 90)
                Line((-57.0256241898, 54.1), (-140, 54.1))
                CenterArc((-57.0256241898, 45), 9.1, 39.8055710923, 50.1944289077)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_65827_d1469ad6_0000():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((6.2277637545, 4.4254595649)):
                Circle(0.225)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((6.2277637545, 4.4254595649)):
                Circle(0.2)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_66562_6591e2f5_0000():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.7255526112, perimeter: 8.4823001647
            with Locations((10.5000001565, 0)):
                Circle(1.35)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7225663103, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((-10.5000001565, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10.5000001565, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_66803_dbe9d79a_0001():
    """Model: glass v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8717919614, perimeter: 11.6238928183
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_67403_bb0225a8_0009():
    """Model: Component24"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4906858337, perimeter: 3.8849555887
            with BuildLine():
                Line((6, 3.6), (5.3002429958, 3.6))
                CenterArc((5.300000079, 3.3000000492), 0.3000000492, 89.9536063007, 180.0463936993)
                Line((5.300000079, 3), (6, 3))
                Line((6, 3), (6, 3.0937651502))
                Line((6, 3.5000000522), (6, 3.0937651502))
                Line((6, 3.5000000522), (6, 3.6))
            make_face()
            with BuildLine():
                CenterArc((5.300000079, 3.3000000492), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0400000012, perimeter: 1.0000000149
            with BuildLine():
                Line((3.5000000522, 0.1000000015), (3.1000000462, 0.1000000015))
                Line((3.5000000522, 0.200000003), (3.5000000522, 0.1000000015))
                Line((3.1000000462, 0.200000003), (3.5000000522, 0.200000003))
                Line((3.1000000462, 0.1000000015), (3.1000000462, 0.200000003))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_67578_a806a2cf_0000():
    """Model: toolprt4 v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 52 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0101148306, perimeter: 0.4858571804
            with BuildLine():
                Line((2.0100164557, 1.5023261246), (2.1105157691, 1.5975443046))
                Line((2.1105157691, 1.3962527676), (2.0100164557, 1.5023261246))
                Line((2.1105157691, 1.5975443046), (2.1105157691, 1.3962527676))
            make_face()
            # Profile area: 0.0105968759, perimeter: 0.5024712203
            with BuildLine():
                Line((2.1105157691, -0.1947242944), (2.1105157691, -0.4056088379))
                Line((2.1105157691, -0.1947242944), (2.0100164557, -0.2912978725))
                Line((2.1105157691, -0.4056088379), (2.0100164557, -0.2912978725))
            make_face()
            # Profile area: 0.0103286006, perimeter: 0.4932281062
            with BuildLine():
                Line((2.1105157691, 0.4085656653), (2.0100164557, 0.3133454339))
                Line((2.1105157691, 0.2030199711), (2.0100164557, 0.3133454339))
                Line((2.1105157691, 0.4085656653), (2.1105157691, 0.2030199711))
            make_face()
            # Profile area: 0.0053301498, perimeter: 0.3526947738
            with BuildLine():
                Line((2.0100164557, 1.7036176616), (2.1105157691, 1.7036176616))
                Line((2.1105157691, 1.5975443046), (2.0100164557, 1.7036176616))
                Line((2.1105157691, 1.7036176616), (2.1105157691, 1.5975443046))
            make_face()
            # Profile area: 0.0104627382, perimeter: 0.4976574907
            with BuildLine():
                Line((2.1105157691, -0.9902128254), (2.0100164557, -1.0977651615))
                Line((2.1105157691, -1.1984279443), (2.0100164557, -1.0977651615))
                Line((2.1105157691, -0.9902128254), (2.1105157691, -1.1984279443))
            make_face()
            # Profile area: 0.0102500712, perimeter: 0.4905150758
            with BuildLine():
                Line((2.1105157691, -2.3920854201), (2.0100164557, -2.487277445))
                Line((2.1105157691, -2.5960683305), (2.0100164557, -2.487277445))
                Line((2.1105157691, -2.3920854201), (2.1105157691, -2.5960683305))
            make_face()
            # Profile area: 2.2, perimeter: 9.8
            with BuildLine():
                Line((2.1105157691, -0.4056088379), (2.1105157691, -0.6004768337))
                Line((2.1105157691, -0.6004768337), (2.1105157691, -0.7953448296))
                Line((2.1105157691, -0.7953448296), (2.1105157691, -0.9902128254))
                Line((2.1105157691, -0.9902128254), (2.1105157691, -1.1984279443))
                Line((2.1105157691, -1.1984279443), (2.1105157691, -1.3959653647))
                Line((2.1105157691, -1.3959653647), (2.1105157691, -1.5988416344))
                Line((2.1105157691, -1.5988416344), (2.1105157691, -1.8073344104))
                Line((2.1105157691, -1.8073344104), (2.1105157691, -1.9943187449))
                Line((2.1105157691, -1.9943187449), (2.1105157691, -2.1877323877))
                Line((2.1105157691, -2.1877323877), (2.1105157691, -2.3920854201))
                Line((2.1105157691, -2.3920854201), (2.1105157691, -2.5960683305))
                Line((2.1105157691, -2.5960683305), (2.1105157691, -2.6493113282))
                Line((2.6105157691, -2.6493113282), (2.1105157691, -2.6493113282))
                Line((2.6105157691, 1.7506886718), (2.6105157691, -2.6493113282))
                Line((2.6105157691, 1.7506886718), (2.1105157691, 1.7506886718))
                Line((2.1105157691, 1.7506886718), (2.1105157691, 1.7036176616))
                Line((2.1105157691, 1.7036176616), (2.1105157691, 1.5975443046))
                Line((2.1105157691, 1.5975443046), (2.1105157691, 1.3962527676))
                Line((2.1105157691, 1.3962527676), (2.1105157691, 1.1987153471))
                Line((2.1105157691, 1.1987153471), (2.1105157691, 0.9958390775))
                Line((2.1105157691, 0.9958390775), (2.1105157691, 0.8171086901))
                Line((2.1105157691, 0.8171086901), (2.1105157691, 0.6126547389))
                Line((2.1105157691, 0.6126547389), (2.1105157691, 0.4085656653))
                Line((2.1105157691, 0.4085656653), (2.1105157691, 0.2030199711))
                Line((2.1105157691, 0.2030199711), (2.1105157691, 0.002813126))
                Line((2.1105157691, 0.002813126), (2.1105157691, -0.1947242944))
                Line((2.1105157691, -0.1947242944), (2.1105157691, -0.4056088379))
            make_face()
            # Profile area: 0.0099261876, perimeter: 0.4795484008
            with BuildLine():
                Line((2.1105157691, 1.3962527676), (2.0100164557, 1.3047887042))
                Line((2.1105157691, 1.1987153471), (2.0100164557, 1.3047887042))
                Line((2.1105157691, 1.3962527676), (2.1105157691, 1.1987153471))
            make_face()
            # Profile area: 0.0102554059, perimeter: 0.4917734949
            with BuildLine():
                Line((2.0100164557, 0.491712995), (2.1105157691, 0.6126547389))
                Line((2.1105157691, 0.4085656653), (2.0100164557, 0.491712995))
                Line((2.1105157691, 0.6126547389), (2.1105157691, 0.4085656653))
            make_face()
            # Profile area: 0.0102747221, perimeter: 0.489682248
            with BuildLine():
                Line((2.0092252424, 1.1027475313), (2.1105157691, 1.1987153471))
                Line((2.1105157691, 0.9958390775), (2.0092252424, 1.1027475313))
                Line((2.1105157691, 1.1987153471), (2.1105157691, 0.9958390775))
            make_face()
            # Profile area: 0.0104766904, perimeter: 0.4981113825
            with BuildLine():
                Line((2.1105157691, -1.5988416344), (2.0100164557, -1.7008969306))
                Line((2.1105157691, -1.8073344104), (2.0100164557, -1.7008969306))
                Line((2.1105157691, -1.5988416344), (2.1105157691, -1.8073344104))
            make_face()
            # Profile area: 0.0099261876, perimeter: 0.4794777739
            with BuildLine():
                Line((2.1105157691, 0.002813126), (2.1105157691, -0.1947242944))
                Line((2.1105157691, 0.002813126), (2.0100164557, -0.0901396637))
                Line((2.1105157691, -0.1947242944), (2.0100164557, -0.0901396637))
            make_face()
            # Profile area: 0.0093958986, perimeter: 0.4615162889
            with BuildLine():
                Line((2.1105157691, -1.8073344104), (2.0100164557, -1.9022268489))
                Line((2.1105157691, -1.9943187449), (2.0100164557, -1.9022268489))
                Line((2.1105157691, -1.8073344104), (2.1105157691, -1.9943187449))
            make_face()
            # Profile area: 0.0097920499, perimeter: 0.4748465768
            with BuildLine():
                Line((2.1105157691, -0.6004768337), (2.0100164557, -0.6953032928))
                Line((2.1105157691, -0.7953448296), (2.0100164557, -0.6953032928))
                Line((2.1105157691, -0.6004768337), (2.1105157691, -0.7953448296))
            make_face()
            # Profile area: 0.0100603252, perimeter: 0.4841618625
            with BuildLine():
                Line((2.1105157691, 0.2030199711), (2.0100164557, 0.11147164))
                Line((2.1105157691, 0.002813126), (2.0100164557, 0.11147164))
                Line((2.1105157691, 0.2030199711), (2.1105157691, 0.002813126))
            make_face()
            # Profile area: 0.0099261876, perimeter: 0.4793644589
            with BuildLine():
                Line((2.1105157691, -1.1984279443), (2.0100164557, -1.2987640538))
                Line((2.1105157691, -1.3959653647), (2.0100164557, -1.2987640538))
                Line((2.1105157691, -1.1984279443), (2.1105157691, -1.3959653647))
            make_face()
            # Profile area: 0.0097189692, perimeter: 0.4729847005
            with BuildLine():
                Line((2.1105157691, -1.9943187449), (2.0100164557, -2.1039930206))
                Line((2.1105157691, -2.1877323877), (2.0100164557, -2.1039930206))
                Line((2.1105157691, -1.9943187449), (2.1105157691, -2.1877323877))
            make_face()
            # Profile area: 0.0101944629, perimeter: 0.488483219
            with BuildLine():
                Line((2.1105157691, -1.3959653647), (2.0100164557, -1.4998745806))
                Line((2.1105157691, -1.5988416344), (2.0100164557, -1.4998745806))
                Line((2.1105157691, -1.3959653647), (2.1105157691, -1.5988416344))
            make_face()
            # Profile area: 0.0097920499, perimeter: 0.4748673087
            with BuildLine():
                Line((2.1105157691, -0.7953448296), (2.0100164557, -0.8963040144))
                Line((2.1105157691, -0.9902128254), (2.0100164557, -0.8963040144))
                Line((2.1105157691, -0.7953448296), (2.1105157691, -0.9902128254))
            make_face()
            # Profile area: 0.0102737409, perimeter: 0.4923712687
            with BuildLine():
                Line((2.0100164557, 0.6961669463), (2.1105157691, 0.8171086901))
                Line((2.1105157691, 0.6126547389), (2.0100164557, 0.6961669463))
                Line((2.1105157691, 0.8171086901), (2.1105157691, 0.6126547389))
            make_face()
            # Profile area: 0.0102686697, perimeter: 0.4921634576
            with BuildLine():
                Line((2.0100164557, -2.3083460531), (2.1105157691, -2.1877323877))
                Line((2.1105157691, -2.3920854201), (2.0100164557, -2.3083460531))
                Line((2.1105157691, -2.1877323877), (2.1105157691, -2.3920854201))
            make_face()
            # Profile area: 0.0097920499, perimeter: 0.475125443
            with BuildLine():
                Line((2.1105157691, -0.4056088379), (2.0100164557, -0.4939652958))
                Line((2.1105157691, -0.6004768337), (2.0100164557, -0.4939652958))
                Line((2.1105157691, -0.4056088379), (2.1105157691, -0.6004768337))
            make_face()
            # Profile area: 0.0089811406, perimeter: 0.447842978
            with BuildLine():
                Line((2.1105157691, 0.9958390775), (2.0100164557, 0.9006208975))
                Line((2.1105157691, 0.8171086901), (2.0100164557, 0.9006208975))
                Line((2.1105157691, 0.9958390775), (2.1105157691, 0.8171086901))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.6105157691, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8725037084, perimeter: 8.4900148335
            with BuildLine():
                Line((-1.9943187449, 1.15), (-1.9943187449, 0.65))
                Line((-1.9943187449, 0.65), (1.7506886718, 0.65))
                Line((1.7506886718, 1.15), (1.7506886718, 0.65))
                Line((-1.9943187449, 1.15), (1.7506886718, 1.15))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_67880_ffcf9ee5_0000():
    """Model: knife cap v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0655, perimeter: 2.72
            with BuildLine():
                Line((0.3806350833, 0.26), (0.05, 0.26))
                Line((0.4193649167, 0.26), (0.3806350833, 0.26))
                Line((0.55, 0.26), (0.4193649167, 0.26))
                Line((0.55, 0.31), (0.55, 0.26))
                Line((0, 0.31), (0.55, 0.31))
                Line((0, 0), (0, 0.31))
                Line((0.55, 0), (0, 0))
                Line((0.55, 0.05), (0.55, 0))
                Line((0.05, 0.05), (0.55, 0.05))
                Line((0.05, 0.26), (0.05, 0.05))
            make_face()
            # Profile area: 0.0003604478, perimeter: 0.0914544763
            with BuildLine():
                CenterArc((0.3806350833, 0.255), 0.005, 14.4775121859, 75.5224878141)
                CenterArc((0.4, 0.26), 0.015, -165.5224878141, 151.0449756281)
                CenterArc((0.4193649167, 0.255), 0.005, 90, 75.5224878141)
                Line((0.4193649167, 0.26), (0.3806350833, 0.26))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0655, perimeter: 2.72
            with BuildLine():
                Line((0.4193649167, 0.26), (0.55, 0.26))
                Line((0.55, 0.26), (0.55, 0.31))
                Line((0.55, 0.31), (0, 0.31))
                Line((0, 0.31), (0, 0))
                Line((0, 0), (0.55, 0))
                Line((0.55, 0), (0.55, 0.05))
                Line((0.55, 0.05), (0.05, 0.05))
                Line((0.05, 0.05), (0.05, 0.26))
                Line((0.05, 0.26), (0.3806350833, 0.26))
                Line((0.3806350833, 0.26), (0.4193649167, 0.26))
            make_face()
        # OneSide extrude, distance=1.175
        extrude(amount=1.175, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0655, perimeter: 2.72
            with BuildLine():
                Line((0.3806350833, 0.26), (0.05, 0.26))
                Line((0.4193649167, 0.26), (0.3806350833, 0.26))
                Line((0.55, 0.26), (0.4193649167, 0.26))
                Line((0.55, 0.31), (0.55, 0.26))
                Line((0, 0.31), (0.55, 0.31))
                Line((0, 0), (0, 0.31))
                Line((0.55, 0), (0, 0))
                Line((0.55, 0.05), (0.55, 0))
                Line((0.05, 0.05), (0.55, 0.05))
                Line((0.05, 0.26), (0.05, 0.05))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_67880_ffcf9ee5_0001():
    """Model: Blade head v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4619495561, perimeter: 2.9148547699
            with BuildLine():
                Line((-0.2, 0.5), (-0.2, 0.2236068037))
                CenterArc((0, 0), 0.3000000045, 131.8103141321, 96.3793717357)
                Line((-0.2, -0.2236068037), (-0.2, -0.4999997734))
                Line((-0.2, -0.4999997734), (0.200000003, -0.4999997734))
                Line((0.200000003, -0.4999997734), (0.2000000013, -0.2236068026))
                CenterArc((0, 0), 0.3000000045, -48.1896855264, 96.3793713942)
                Line((0.2, 0.5), (0.2, 0.2236068037))
                Line((0.2, 0.5), (-0.2, 0.5))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_55611_69142616_0002": {"func": model_55611_69142616_0002, "volume": 7.9521564044, "area": 31.8086256176},
    "model_55611_69142616_0003": {"func": model_55611_69142616_0003, "volume": 8.5412050269, "area": 40.919244313},
    "model_55611_69142616_0006": {"func": model_55611_69142616_0006, "volume": 12.2714040854, "area": 90.634512822},
    "model_55633_282eaae6_0007": {"func": model_55633_282eaae6_0007, "volume": 0.0058904862, "area": 0.3141592654},
    "model_55636_6180bfce_0002": {"func": model_55636_6180bfce_0002, "volume": 19174.7550032375, "area": 8886.4594300514},
    "model_55636_6180bfce_0005": {"func": model_55636_6180bfce_0005, "volume": 8.5497502975, "area": 37.4600998434},
    "model_55707_c78416ed_0024": {"func": model_55707_c78416ed_0024, "volume": 22.5357567456, "area": 72.2237162721},
    "model_55715_525d1d3e_0003": {"func": model_55715_525d1d3e_0003, "volume": 2.4357389357, "area": 26.7027712977},
    "model_55715_525d1d3e_0006": {"func": model_55715_525d1d3e_0006, "volume": 28.1407969031, "area": 76.6769819691},
    "model_55715_525d1d3e_0007": {"func": model_55715_525d1d3e_0007, "volume": 0.6395089234, "area": 5.8022406351},
    "model_55752_a77535b1_0000": {"func": model_55752_a77535b1_0000, "volume": 2700, "area": 2160},
    "model_55756_070bfb3e_0000": {"func": model_55756_070bfb3e_0000, "volume": 168.0132852146, "area": 355.8067808323},
    "model_55767_a6177f06_0000": {"func": model_55767_a6177f06_0000, "volume": 103.0936923047, "area": 181.7618301896},
    "model_55786_39249e3d_0000": {"func": model_55786_39249e3d_0000, "volume": 22.3105637508, "area": 60.9977871438},
    "model_55788_c93cc797_0000": {"func": model_55788_c93cc797_0000, "volume": 2394.7787445226, "area": 2078.2742735936},
    "model_55789_3be2e914_0000": {"func": model_55789_3be2e914_0000, "volume": 329.8731840104, "area": 327.6858656093},
    "model_55834_09fd959e_0000": {"func": model_55834_09fd959e_0000, "volume": 47.347767006, "area": 86.8415523781},
    "model_55838_a1513314_0000": {"func": model_55838_a1513314_0000, "volume": 446.1831281387, "area": 397.619128094},
    "model_55852_4f1a2c5b_0000": {"func": model_55852_4f1a2c5b_0000, "volume": 106.9181296648, "area": 224.1597679647},
    "model_55884_8d78f117_0000": {"func": model_55884_8d78f117_0000, "volume": 25.7690025938, "area": 113.2475130324},
    "model_55887_a5ee694a_0000": {"func": model_55887_a5ee694a_0000, "volume": 17107.8369044242, "area": 4214.6635768696},
    "model_55927_f8b31711_0007": {"func": model_55927_f8b31711_0007, "volume": 1.7875552611, "area": 10.5670350741},
    "model_55927_f8b31711_0009": {"func": model_55927_f8b31711_0009, "volume": 23.1766173033, "area": 48.1039534081},
    "model_55931_84bfa135_0000": {"func": model_55931_84bfa135_0000, "volume": 22.8, "area": 147.2191118431},
    "model_56036_b04a363c_0001": {"func": model_56036_b04a363c_0001, "volume": 506.1371669412, "area": 628.9867228627},
    "model_56065_00bbe5da_0002": {"func": model_56065_00bbe5da_0002, "volume": 1.0107987931, "area": 8.5390894266},
    "model_56065_00bbe5da_0008": {"func": model_56065_00bbe5da_0008, "volume": 2.1508128705, "area": 24.4141019092},
    "model_56065_00bbe5da_0009": {"func": model_56065_00bbe5da_0009, "volume": 9.4069698697, "area": 39.52316776},
    "model_56065_00bbe5da_0015": {"func": model_56065_00bbe5da_0015, "volume": 1.8427404409, "area": 20.8483942474},
    "model_56065_00bbe5da_0016": {"func": model_56065_00bbe5da_0016, "volume": 9.5640495024, "area": 38.6592297803},
    "model_56065_00bbe5da_0017": {"func": model_56065_00bbe5da_0017, "volume": 1.7419855116, "area": 14.4725831748},
    "model_56065_00bbe5da_0021": {"func": model_56065_00bbe5da_0021, "volume": 3.4389411417, "area": 31.3756609284},
    "model_56068_f346988c_0001": {"func": model_56068_f346988c_0001, "volume": 4.4440680039, "area": 38.5069132917},
    "model_56151_408ea220_0006": {"func": model_56151_408ea220_0006, "volume": 0.44610601, "area": 17.8442463773},
    "model_56151_408ea220_0007": {"func": model_56151_408ea220_0007, "volume": 0.5694135406, "area": 12.6134945747},
    "model_56320_6df1f5fe_0000": {"func": model_56320_6df1f5fe_0000, "volume": 898.9498356397, "area": 954.0286105582},
    "model_56324_4361f734_0000": {"func": model_56324_4361f734_0000, "volume": 9226.1277229996, "area": 5586.6849526928},
    "model_56325_1ca40934_0000": {"func": model_56325_1ca40934_0000, "volume": 290.816, "area": 420.9773360896},
    "model_56343_60e8809c_0010": {"func": model_56343_60e8809c_0010, "volume": 0.0084488422, "area": 1.8075433664},
    "model_56344_3a89f085_0010": {"func": model_56344_3a89f085_0010, "volume": 4.6316142524, "area": 21.4552951897},
    "model_56344_3a89f085_0011": {"func": model_56344_3a89f085_0011, "volume": 31.368124136, "area": 74.1677836019},
    "model_56344_3a89f085_0012": {"func": model_56344_3a89f085_0012, "volume": 5.1249708734, "area": 21.7020383983},
    "model_56344_3a89f085_0014": {"func": model_56344_3a89f085_0014, "volume": 2.537310947, "area": 12.5741149186},
    "model_56344_3a89f085_0017": {"func": model_56344_3a89f085_0017, "volume": 5.1683947944, "area": 23.0984503082},
    "model_56344_3a89f085_0020": {"func": model_56344_3a89f085_0020, "volume": 1.1910563148, "area": 7.51783122},
    "model_56344_3a89f085_0023": {"func": model_56344_3a89f085_0023, "volume": 4.9637163927, "area": 21.6769893098},
    "model_56344_3a89f085_0024": {"func": model_56344_3a89f085_0024, "volume": 15.8692177487, "area": 48.0914166885},
    "model_56344_3a89f085_0025": {"func": model_56344_3a89f085_0025, "volume": 14.5502205687, "area": 43.4423187166},
    "model_56344_3a89f085_0027": {"func": model_56344_3a89f085_0027, "volume": 27.6852852598, "area": 78.9325154214},
    "model_56344_3a89f085_0028": {"func": model_56344_3a89f085_0028, "volume": 7.1547278, "area": 27.1746302171},
    "model_56345_80dc7bcc_0009": {"func": model_56345_80dc7bcc_0009, "volume": 0.0471238917, "area": 1.1309733721},
    "model_56364_8e6032c8_0008": {"func": model_56364_8e6032c8_0008, "volume": 7.1279292506, "area": 24.0249551428},
    "model_56368_b79cbf07_0002": {"func": model_56368_b79cbf07_0002, "volume": 10170.906215997, "area": 4806.6367599924},
    "model_56430_4f35ba2f_0010": {"func": model_56430_4f35ba2f_0010, "volume": 669.3981909272, "area": 1111.2339738833},
    "model_56430_4f35ba2f_0017": {"func": model_56430_4f35ba2f_0017, "volume": 469.6331164339, "area": 619.8800000538},
    "model_56436_2a8fc254_0006": {"func": model_56436_2a8fc254_0006, "volume": 0.0001842885, "area": 0.0213761555},
    "model_56436_2a8fc254_0007": {"func": model_56436_2a8fc254_0007, "volume": 0.0001036628, "area": 0.0140398628},
    "model_56457_dd352142_0002": {"func": model_56457_dd352142_0002, "volume": 2042.0352248334, "area": 2215.0853096416},
    "model_56458_c027ed41_0010": {"func": model_56458_c027ed41_0010, "volume": 3.3141592654, "area": 15.5132741229},
    "model_56459_7b640aed_0009": {"func": model_56459_7b640aed_0009, "volume": 3944.1154896585, "area": 4593.6669646382},
    "model_56459_7b640aed_0010": {"func": model_56459_7b640aed_0010, "volume": 1169.7571646751, "area": 2608.3386227753},
    "model_56460_78d17e23_0004": {"func": model_56460_78d17e23_0004, "volume": 1086.9910581421, "area": 1463.9821765728},
    "model_56461_9a5be0e9_0003": {"func": model_56461_9a5be0e9_0003, "volume": 28.2743338823, "area": 131.9468914508},
    "model_56463_450f3e67_0000": {"func": model_56463_450f3e67_0000, "volume": 14375.3051330033, "area": 10764.5820861398},
    "model_56477_620f7fc8_0011": {"func": model_56477_620f7fc8_0011, "volume": 1.274908206, "area": 13.4625317504},
    "model_56486_82b3e23a_0010": {"func": model_56486_82b3e23a_0010, "volume": 300, "area": 670},
    "model_56564_976c253c_0013": {"func": model_56564_976c253c_0013, "volume": 35.5392668937, "area": 172.002197784},
    "model_56568_d3018fcb_0000": {"func": model_56568_d3018fcb_0000, "volume": 386.3033307204, "area": 319.5376094765},
    "model_56568_d3018fcb_0012": {"func": model_56568_d3018fcb_0012, "volume": 24.5743626597, "area": 56.5612223543},
    "model_56568_d3018fcb_0013": {"func": model_56568_d3018fcb_0013, "volume": 75.9754027237, "area": 106.8899427156},
    "model_56793_e1f0d3ac_0000": {"func": model_56793_e1f0d3ac_0000, "volume": 0.1041980571, "area": 3.5064358999},
    "model_57251_414ca79f_0000": {"func": model_57251_414ca79f_0000, "volume": 0.0062647788, "area": 0.2093727633},
    "model_57755_3c6610d1_0000": {"func": model_57755_3c6610d1_0000, "volume": 49.5755726399, "area": 99.7828324409},
    "model_57854_7f40fb28_0000": {"func": model_57854_7f40fb28_0000, "volume": 96.5827169482, "area": 516.9638927412},
    "model_57888_fa22ef0f_0000": {"func": model_57888_fa22ef0f_0000, "volume": 83.6920282916, "area": 137.0431990814},
    "model_60294_f8d4a189_0000": {"func": model_60294_f8d4a189_0000, "volume": 22.7426781527, "area": 105.1337230247},
    "model_60298_4d6233b0_0000": {"func": model_60298_4d6233b0_0000, "volume": 8.665796275, "area": 37.7315482334},
    "model_60303_d31fd2a9_0000": {"func": model_60303_d31fd2a9_0000, "volume": 150.1785399671, "area": 268.8929200659},
    "model_60529_79e8313a_0013": {"func": model_60529_79e8313a_0013, "volume": 911249.9999999998, "area": 63450},
    "model_60692_269557b8_0005": {"func": model_60692_269557b8_0005, "volume": 24.3473430653, "area": 53.407075111},
    "model_60707_15529a7f_0001": {"func": model_60707_15529a7f_0001, "volume": 66.8499074004, "area": 319.38022579},
    "model_60707_15529a7f_0002": {"func": model_60707_15529a7f_0002, "volume": 64.6652867838, "area": 314.5016136352},
    "model_60717_7ba1f3ab_0000": {"func": model_60717_7ba1f3ab_0000, "volume": 1.4726215564, "area": 12.1736715327},
    "model_60721_57103153_0002": {"func": model_60721_57103153_0002, "volume": 3297.559171141, "area": 2310.500630111},
    "model_60725_a5735a6c_0004": {"func": model_60725_a5735a6c_0004, "volume": 56.9315073888, "area": 116.2782430134},
    "model_60738_365811c2_0001": {"func": model_60738_365811c2_0001, "volume": 81.25825409, "area": 151.9238225673},
    "model_60738_365811c2_0002": {"func": model_60738_365811c2_0002, "volume": 2.5834513322, "area": 22.951238898},
    "model_60753_80b955c8_0002": {"func": model_60753_80b955c8_0002, "volume": 14.0736188478, "area": 61.6480113138},
    "model_60756_88dc9000_0000": {"func": model_60756_88dc9000_0000, "volume": 443.0289083554, "area": 563.6101521902},
    "model_60759_23829707_0008": {"func": model_60759_23829707_0008, "volume": 5079.2425484067, "area": 3162.3900700734},
    "model_60767_0746a46e_0000": {"func": model_60767_0746a46e_0000, "volume": 572.346063734, "area": 861.9931958707},
    "model_60860_249af7ce_0000": {"func": model_60860_249af7ce_0000, "volume": 90.6573695035, "area": 232.1055968341},
    "model_60865_19bbdeb4_0003": {"func": model_60865_19bbdeb4_0003, "volume": 2.0163939504, "area": 16.6512629521},
    "model_60996_662df59e_0000": {"func": model_60996_662df59e_0000, "volume": 5.9703826118, "area": 23.3612717451},
    "model_61091_f7d8529d_0002": {"func": model_61091_f7d8529d_0002, "volume": 8.4057048593, "area": 72.5859315428},
    "model_61198_0c99f50a_0005": {"func": model_61198_0c99f50a_0005, "volume": 313.1201595541, "area": 715.5419206078},
    "model_61198_0c99f50a_0006": {"func": model_61198_0c99f50a_0006, "volume": 7.1549772686, "area": 46.8254385018},
    "model_61198_0c99f50a_0007": {"func": model_61198_0c99f50a_0007, "volume": 6.1021510305, "area": 44.3435803054},
    "model_61198_0c99f50a_0009": {"func": model_61198_0c99f50a_0009, "volume": 155.6973319119, "area": 235.3052897539},
    "model_61198_0c99f50a_0010": {"func": model_61198_0c99f50a_0010, "volume": 3.1774715005, "area": 14.5096073973},
    "model_61198_0c99f50a_0014": {"func": model_61198_0c99f50a_0014, "volume": 7.7491484531, "area": 29.8060153516},
    "model_61198_0c99f50a_0015": {"func": model_61198_0c99f50a_0015, "volume": 73.6395765201, "area": 389.3631256347},
    "model_61198_0c99f50a_0016": {"func": model_61198_0c99f50a_0016, "volume": 10.6568521361, "area": 34.7759265359},
    "model_61257_7a82d02b_0000": {"func": model_61257_7a82d02b_0000, "volume": 96.6780125741, "area": 427.3106332681},
    "model_61377_2c5e62c1_0000": {"func": model_61377_2c5e62c1_0000, "volume": 164.75, "area": 669},
    "model_61412_df7154f9_0001": {"func": model_61412_df7154f9_0001, "volume": 1178.0972450962, "area": 628.318530718},
    "model_61495_24e309c1_0001": {"func": model_61495_24e309c1_0001, "volume": 870.0014697211, "area": 1566.002645498},
    "model_61643_303cdd31_0000": {"func": model_61643_303cdd31_0000, "volume": 83.2522053201, "area": 226.1946710585},
    "model_63132_330141d7_0003": {"func": model_63132_330141d7_0003, "volume": 34.0862802914, "area": 138.936935105},
    "model_63411_46a912fc_0002": {"func": model_63411_46a912fc_0002, "volume": 2.7655821903, "area": 20.5996611364},
    "model_64836_b59b00e7_0000": {"func": model_64836_b59b00e7_0000, "volume": 45.3700210735, "area": 190.5294204372},
    "model_64965_49fab8b9_0001": {"func": model_64965_49fab8b9_0001, "volume": 180.9600118981, "area": 220.0521735262},
    "model_65482_f5dcf75b_0000": {"func": model_65482_f5dcf75b_0000, "volume": 1.167214928, "area": 7.376963788},
    "model_65569_bd890a32_0006": {"func": model_65569_bd890a32_0006, "volume": 36977.7759567447, "area": 17022.64696939},
    "model_65827_d1469ad6_0000": {"func": model_65827_d1469ad6_0000, "volume": 0.0367173641, "area": 3.004147975},
    "model_66562_6591e2f5_0000": {"func": model_66562_6591e2f5_0000, "volume": 1.2951215714, "area": 26.7506614453},
    "model_66803_dbe9d79a_0001": {"func": model_66803_dbe9d79a_0001, "volume": 8.7179196137, "area": 117.9825121056},
    "model_67403_bb0225a8_0009": {"func": model_67403_bb0225a8_0009, "volume": 0.2272057525, "area": 4.1468583738},
    "model_67578_a806a2cf_0000": {"func": model_67578_a806a2cf_0000, "volume": 8.0940558245, "area": 42.8819765815},
    "model_67880_ffcf9ee5_0000": {"func": model_67880_ffcf9ee5_0000, "volume": 0.1228845896, "area": 5.2345198575},
    "model_67880_ffcf9ee5_0001": {"func": model_67880_ffcf9ee5_0001, "volume": 0.0881419899, "area": 1.5496228896},
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
