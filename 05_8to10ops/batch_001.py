"""Batch 001 - passing/05_8to10ops
59 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_100893_3ffa90e7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 64.516, perimeter: 33.02
            with BuildLine():
                Line((3.175, -5.08), (3.175, 5.08))
                Line((3.175, 5.08), (-3.175, 5.08))
                Line((-3.175, 5.08), (-3.175, -5.08))
                Line((-3.175, -5.08), (3.175, -5.08))
            make_face()
        # OneSide extrude, distance=6.604
        extrude(amount=6.604)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.604), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6004051703, perimeter: 4.4845606811
            with Locations((0, -3.81)):
                Circle(0.71374)
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.175, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 17.90319, perimeter: 20.674982348
            with BuildLine():
                Line((2.54, 6.604), (-5.08, 6.604))
                Line((-5.08, 6.604), (-5.08, 2.54))
                Line((2.54, 5.969), (-5.08, 2.54))
                Line((2.54, 6.604), (2.54, 5.969))
            make_face()
        # OneSide extrude, distance=-24.13
        extrude(amount=-24.13, mode=Mode.SUBTRACT)
    return part.part


def model_101446_95204330_0002():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.6, perimeter: 16.4
            with BuildLine():
                Line((2.6, -1.5), (-2.6, -1.5))
                Line((2.6, 1.5), (2.6, -1.5))
                Line((-2.6, 1.5), (2.6, 1.5))
                Line((-2.6, -1.5), (-2.6, 1.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.12, perimeter: 31.2
            with BuildLine():
                Line((2.6, -1.5), (2.6, 1.5))
                Line((2.6, 1.5), (-2.6, 1.5))
                Line((-2.6, 1.5), (-2.6, -1.5))
                Line((-2.6, -1.5), (2.6, -1.5))
            make_face()
            with BuildLine():
                Line((-2.4, -1.3), (2.4, -1.3))
                Line((-2.4, 1.3), (-2.4, -1.3))
                Line((2.4, 1.3), (-2.4, 1.3))
                Line((2.4, -1.3), (2.4, 1.3))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9600000215, perimeter: 10.0000000775
            with BuildLine():
                Line((2.4, 0), (-2.4000000358, 0))
                Line((2.4, 0), (2.4, 0.200000003))
                Line((-2.4000000358, 0.200000003), (2.4, 0.200000003))
                Line((-2.4000000358, 0), (-2.4000000358, 0.200000003))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.6, 0.75)):
                Circle(0.15)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.6, 0.75)):
                Circle(0.15)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_102263_037b99d3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.76, perimeter: 36.4
            with BuildLine():
                Line((6, 0), (6, 0.4))
                Line((6, 0.4), (11, 0.4))
                Line((11, 0.4), (11, 7))
                Line((11, 7), (6, 7))
                Line((6, 7), (6, 3.8))
                Line((3.8, 3.8), (6, 3.8))
                Line((3.8, 2), (3.8, 3.8))
                Line((-0.2, 2), (3.8, 2))
                Line((-0.2, 0.4), (-0.2, 2))
                Line((3.8, 0.4), (-0.2, 0.4))
                Line((3.8, 0), (3.8, 0.4))
                Line((6, 0), (3.8, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.4, perimeter: 11.2
            with BuildLine():
                Line((3.8, 1.2), (-0.2, 1.2))
                Line((3.8, 1.2), (3.8, 2.8))
                Line((-0.2, 2.8), (3.8, 2.8))
                Line((-0.2, 1.2), (-0.2, 2.8))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8, perimeter: 13.2
            with BuildLine():
                Line((6, 1.2), (11, 1.2))
                Line((11, 1.2), (11, 2.8))
                Line((11, 2.8), (6, 2.8))
                Line((6, 2.8), (6, 1.2))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-8.5, 2)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.8, 2)):
                Circle(0.6)
        # OneSide extrude, distance=-23
        extrude(amount=-23, mode=Mode.SUBTRACT)
    return part.part


def model_104524_f829aab2_0003():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3014376029, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.0000004172, perimeter: 15.6000002325
            with BuildLine():
                Line((-2.5000000373, 3.8000000566), (2.5000000373, 3.8000000566))
                Line((-2.5000000373, 1.0000000149), (-2.5000000373, 3.8000000566))
                Line((2.5000000373, 1.0000000149), (-2.5000000373, 1.0000000149))
                Line((2.5000000373, 3.8000000566), (2.5000000373, 1.0000000149))
            make_face()
        # Symmetric extrude, full_length=True, total=8
        extrude(amount=4, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8000000566, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.3000000566, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.6000000566, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_106059_5d7ef4ef_0001():
    """Model: side wall"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3864789953, perimeter: 7.8234796501
            with BuildLine():
                Line((0.4005291547, 3.7982550415), (0.1019034462, 0))
                Line((0.2989291547, 3.7982550415), (0.4005291547, 3.7982550415))
                Line((0, 0), (0.2989291547, 3.7982550415))
                Line((0.1019034462, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=-17.78
        extrude(amount=-17.78)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2059459757, perimeter: 8.255
            with BuildLine():
                Line((0.2989291547, 3.7982550415), (-0.0185708453, 3.7982550415))
                Line((-0.0185708453, 3.7982550415), (-0.3175, 0))
                Line((-0.3175, 0), (0, 0))
                Line((0, 0), (0.2989291547, 3.7982550415))
            make_face()
        # OneSide extrude, distance=-0.2032
        extrude(amount=-0.2032, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -17.78), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.2059459757, perimeter: 8.255
            with BuildLine():
                Line((0, 0), (-0.2989291547, 3.7982550415))
                Line((0.3175, 0), (0, 0))
                Line((0.0185708453, 3.7982550415), (0.3175, 0))
                Line((-0.2989291547, 3.7982550415), (0.0185708453, 3.7982550415))
            make_face()
        # OneSide extrude, distance=-0.2032
        extrude(amount=-0.2032, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-0.9969173337, 0.0784590957, 0))):
            # Profile area: 0.9146933964, perimeter: 4.617155104
            with BuildLine():
                Line((-15.598422448, 3.048), (-17.399, 3.048))
                Line((-15.598422448, 3.556), (-15.598422448, 3.048))
                Line((-17.399, 3.556), (-15.598422448, 3.556))
                Line((-17.399, 3.048), (-17.399, 3.556))
            make_face()
        # OneSide extrude, distance=-1.016
        extrude(amount=-1.016, mode=Mode.SUBTRACT)
    return part.part


def model_106094_e167f3da_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 51.6128032944, perimeter: 30.4800009727
            with BuildLine():
                Line((0, 5.0800001621), (0, 0))
                Line((0, 0), (10.1600003242, 0))
                Line((10.1600003242, 0), (10.1600003242, 5.0800001621))
                Line((10.1600003242, 5.0800001621), (0, 5.0800001621))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3845252974, perimeter: 9.0698229595
            with BuildLine():
                Line((-2.5400000811, -5.0800001621), (0, -5.0800001621))
                Line((0, -5.0800001621), (0, -2.5400000811))
                CenterArc((-2.5400000811, -2.5400000811), 2.5400000811, -90, 90)
            make_face()
            # Profile area: 1.3845252974, perimeter: 9.0698229595
            with BuildLine():
                CenterArc((-2.5400000811, -2.5400000811), 2.5400000811, 0, 90)
                Line((0, -2.5400000811), (0, 0))
                Line((0, 0), (-2.5400000811, 0))
            make_face()
        # OneSide extrude, distance=-4.572
        extrude(amount=-4.572, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.3548012354, perimeter: 17.7800005674
            with BuildLine():
                Line((-6.3500002027, 0), (-6.3500002027, -5.0800001621))
                Line((-10.1600003242, 0), (-6.3500002027, 0))
                Line((-10.1600003242, -5.0800001621), (-10.1600003242, 0))
                Line((-6.3500002027, -5.0800001621), (-10.1600003242, -5.0800001621))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.81, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6207166619, perimeter: 2.792875869
            with Locations((-8.1280002594, -1.2700000405)):
                Circle(0.4445)
            # Profile area: 0.6207166619, perimeter: 2.792875869
            with Locations((-8.1280002594, -3.8100001216)):
                Circle(0.4445)
        # OneSide extrude, distance=-8.128
        extrude(amount=-8.128, mode=Mode.SUBTRACT)
    return part.part


def model_106645_558b1d4b_0003():
    """Model: Ball screw (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6956599995, perimeter: 8.5765479443
            with BuildLine():
                CenterArc((0, 0), 1.23, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.135, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0572555261, perimeter: 0.8482300165
            Circle(0.135)
        # OneSide extrude, distance=40.2
        extrude(amount=40.2)

        # Sketch6 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.6, perimeter: 5.6
            with BuildLine():
                Line((30.57, 0.962), (29.77, 0.962))
                Line((30.57, 2.962), (30.57, 0.962))
                Line((29.77, 2.962), (30.57, 2.962))
                Line((29.77, 0.962), (29.77, 2.962))
            make_face()
            # Profile area: 1.6, perimeter: 5.6
            with BuildLine():
                Line((30.57, -2.962), (29.77, -2.962))
                Line((30.57, -0.962), (30.57, -2.962))
                Line((29.77, -0.962), (30.57, -0.962))
                Line((29.77, -2.962), (29.77, -0.962))
            make_face()
        # Symmetric extrude, each_side=1.2671
        extrude(amount=1.2671, both=True, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.611322872, perimeter: 14.011503235
            with BuildLine():
                CenterArc((0, 0), 1.23, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-8.652
        extrude(amount=-8.652, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0572555261, perimeter: 0.8482300165
            Circle(0.135)
        # OneSide extrude, distance=0.4132
        extrude(amount=0.4132, mode=Mode.SUBTRACT)
    return part.part


def model_107386_2a58ec34_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.8183329641, perimeter: 29.0824637877
            with BuildLine():
                Line((5.5972159615, -0.9323174089), (1.2194304659, 1.8908964379))
                CenterArc((0, 0), 2.25, 57.1822153974, 65.6990131599)
                Line((-1.2215235187, 1.8895449964), (-5.586593783, -0.9323174089))
                Line((-5.586593783, -0.9323174089), (-3.4040586508, -4.3084278771))
                Line((-3.4040586508, -4.3084278771), (-0.2053945728, -2.240605514))
                CenterArc((0, 0), 2.25, -95.2376214715, 9.7634145968)
                Line((3.4083232137, -4.32649987), (0.1775427187, -2.2429843029))
                Line((5.5972159615, -0.9323174089), (3.4083232137, -4.32649987))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3, perimeter: 8
            with BuildLine():
                Line((-1.5, -0.5), (1.5, -0.5))
                Line((-1.5, -1.5), (-1.5, -0.5))
                Line((1.5, -1.5), (-1.5, -1.5))
                Line((1.5, -0.5), (1.5, -1.5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 208.5, perimeter: 75
            with BuildLine():
                Line((1.5, 4), (1.5, 10.5))
                Line((9.5, 4), (1.5, 4))
                Line((9.5, 16), (9.5, 4))
                Line((-9.5, 16), (9.5, 16))
                Line((-9.5, 4), (-9.5, 16))
                Line((-1.5, 4), (-9.5, 4))
                Line((-1.5, 10.5), (-1.5, 4))
                Line((1.5, 10.5), (-1.5, 10.5))
            make_face()
            # Profile area: 19.5, perimeter: 19
            with BuildLine():
                Line((1.5, 10.5), (-1.5, 10.5))
                Line((-1.5, 10.5), (-1.5, 4))
                Line((1.5, 4), (-1.5, 4))
                Line((1.5, 4), (1.5, 10.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 198, perimeter: 58
            with BuildLine():
                Line((9, 4.5), (9, 15.5))
                Line((9, 15.5), (-9, 15.5))
                Line((-9, 15.5), (-9, 4.5))
                Line((-9, 4.5), (9, 4.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_107386_52beca0a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3250, perimeter: 230
            with BuildLine():
                Line((0, -65), (45, -65))
                Line((45, -65), (50, -65))
                Line((50, -65), (50, 0))
                Line((50, 0), (45, 0))
                Line((0, 0), (45, 0))
                Line((0, -65), (0, 0))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 65), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 25, perimeter: 101
            with BuildLine():
                Line((0, 47), (50, 47))
                Line((0, 46.5), (0, 47))
                Line((50, 46.5), (0, 46.5))
                Line((50, 47), (50, 46.5))
            make_face()
            # Profile area: 50, perimeter: 102
            with BuildLine():
                Line((0, 31), (50, 31))
                Line((0, 30), (0, 31))
                Line((50, 30), (0, 30))
                Line((50, 31), (50, 30))
            make_face()
            # Profile area: 50, perimeter: 102
            with BuildLine():
                Line((50, 13.5), (0, 13.5))
                Line((0, 13.5), (0, 12.5))
                Line((0, 12.5), (50, 12.5))
                Line((50, 12.5), (50, 13.5))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(50, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23.5, perimeter: 95
            with BuildLine():
                Line((-63, 47), (-63, 0))
                Line((-63.5, 47), (-63, 47))
                Line((-63.5, 46.5), (-63.5, 47))
                Line((-63.5, 31), (-63.5, 46.5))
                Line((-63.5, 30), (-63.5, 31))
                Line((-63.5, 13.5), (-63.5, 30))
                Line((-63.5, 12.5), (-63.5, 13.5))
                Line((-63.5, 0), (-63.5, 12.5))
                Line((-63, 0), (-63.5, 0))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 23.5, perimeter: 95
            with BuildLine():
                Line((63.5, 47), (63, 47))
                Line((63, 47), (63, 0))
                Line((63, 0), (63.5, 0))
                Line((63.5, 0), (63.5, 12.5))
                Line((63.5, 12.5), (63.5, 13.5))
                Line((63.5, 13.5), (63.5, 30))
                Line((63.5, 30), (63.5, 31))
                Line((63.5, 31), (63.5, 46.5))
                Line((63.5, 46.5), (63.5, 47))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_107667_92c0fd66_0000():
    """Model: Block"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.09675, perimeter: 13.97
            with BuildLine():
                Line((0, 3.175), (0, 0))
                Line((0, 0), (3.81, 0))
                Line((3.81, 0), (3.81, 3.175))
                Line((3.81, 3.175), (0, 3.175))
            make_face()
        # OneSide extrude, distance=2.2225
        extrude(amount=2.2225)
    return part.part


def model_107832_665a08a7_0002():
    """Model: Component2"""
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
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 3.0000000447), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 102.3693883598, perimeter: 96.7178162343
            with BuildLine():
                _nurbs_edge([(-0.8366861903, 0), (-0.838762692, -0.0181166862), (-0.8586058046, -0.1913944574), (-0.8968403774, -0.5279793764), (-0.9550766764, -1.0459595985), (-1.0366280878, -1.7714708626), (-1.1451213979, -2.7103158624), (-1.2654227758, -3.698610256), (-1.3997611331, -4.7267139569), (-1.5499747254, -5.7837948274), (-1.7173174253, -6.858127285), (-1.9024965301, -7.9378281226), (-2.1056584981, -9.0114967695), (-2.3263776277, -10.0689105993), (-2.5636376171, -11.1016674148), (-2.8157808996, -12.1039736393), (-3.0805210711, -13.0731016679), (-3.3552351303, -14.0085205241), (-3.637199951, -14.9112708697), (-3.9238530436, -15.7832629018), (-4.2130194038, -16.6266693932), (-4.5032074341, -17.4432064829), (-4.7935440904, -18.2340435738), (-5.0255822101, -18.8467479087), (-5.1994172278, -19.2952140727), (-5.3152213223, -19.5892880252), (-5.3731018966, -19.7350991173)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, -22), 5.8309518948, 157.1433234421, 225.7133531158)
                _nurbs_edge([(0.8366861903, 0), (0.838762692, -0.0181166862), (0.8586058046, -0.1913944574), (0.8968403774, -0.5279793764), (0.9550766764, -1.0459595985), (1.0366280878, -1.7714708626), (1.1451213979, -2.7103158624), (1.2654227758, -3.698610256), (1.3997611331, -4.7267139569), (1.5499747254, -5.7837948274), (1.7173174253, -6.858127285), (1.9024965301, -7.9378281226), (2.1056584981, -9.0114967695), (2.3263776277, -10.0689105993), (2.5636376171, -11.1016674148), (2.8157808996, -12.1039736393), (3.0805210711, -13.0731016679), (3.3552351303, -14.0085205241), (3.637199951, -14.9112708697), (3.9238530436, -15.7832629018), (4.2130194038, -16.6266693932), (4.5032074341, -17.4432064829), (4.7935440904, -18.2340435738), (5.0255822101, -18.8467479087), (5.1994172278, -19.2952140727), (5.3152213223, -19.5892880252), (5.3731018966, -19.7350991173)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((0.8366861903, 0), (-0.8366861903, 0))
            make_face()
            with BuildLine():
                CenterArc((0, -22), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.22962942, perimeter: 7.7957562872
            with BuildLine():
                CenterArc((0, 3.0000000447), 0.75, -134.212396333, 88.424792666)
                _nurbs_edge([(-0.5229901463, 2.4624302289), (-0.5378132787, 2.3637811576), (-0.5677816821, 2.1592215256), (-0.6137008485, 1.8305980119), (-0.6750141678, 1.3628545817), (-0.738935321, 0.8401578712), (-0.7880793978, 0.422116578), (-0.821030461, 0.136590277), (-0.8366861903, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705], 5)
                Line((0.8366861903, 0), (-0.8366861903, 0))
                _nurbs_edge([(0.5229901463, 2.4624302289), (0.5378132787, 2.3637811576), (0.5677816821, 2.1592215256), (0.6137008485, 1.8305980119), (0.6750141678, 1.3628545817), (0.738935321, 0.8401578712), (0.7880793978, 0.422116578), (0.821030461, 0.136590277), (0.8366861903, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705, 0.1553158705], 5)
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with Locations((0, -22)):
                Circle(5)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -22)):
                Circle(1)
        # Symmetric extrude, each_side=17
        extrude(amount=17, both=True, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -22)):
                Circle(1)
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True, mode=Mode.ADD)
    return part.part


def model_110528_cfdc9482_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5164.1798995258, perimeter: 1682.5250779748
            with BuildLine():
                Line((0, 213.36), (0, 0))
                Line((0, 0), (152.3999977112, 0))
                Line((152.3999977112, 0), (152.3999977112, 213.36))
                Line((152.3999977112, 213.36), (0, 213.36))
            make_face()
            with BuildLine():
                Line((146.3134925405, 207.2640025616), (146.3134925405, 106.6800013185))
                Line((6.0960000753, 106.6800013781), (146.3134925405, 106.6800013185))
                Line((6.0960000753, 207.2640025616), (6.0960000753, 106.6800013781))
                Line((146.3134925405, 207.2640025616), (6.0960000753, 207.2640025616))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((146.3134925405, 100.5795552676), (146.3134925405, 6.0960000753))
                Line((146.3134925405, 6.0960000753), (6.0960000753, 6.0960001945))
                Line((6.0960000753, 100.5795552676), (6.0960000753, 6.0960001945))
                Line((6.0960000753, 100.5795552676), (146.3134925405, 100.5795552676))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.096
        extrude(amount=6.096)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 42.3672396971, perimeter: 62.1689367277
            with BuildLine():
                Line((-9.7493770663, 6.1086894192), (-11.1245414809, 6.1086894203))
                Line((-11.1245414809, 6.1086894203), (-15.6965414809, 6.1086894242))
                Line((-15.6965414809, 6.1086894242), (-15.6965414822, 4.591391767))
                Line((-15.6965414822, 4.591391767), (-11.1245414822, 4.6049388917))
                Line((-11.1245414822, 4.6049388917), (-11.1245414835, 3.1011883631))
                CenterArc((-11.1626414835, 3.1011883631), 0.0381, -90.0000000487, 90)
                Line((-11.1626414835, 3.0630883631), (-15.2400000727, 3.0630883666))
                Line((-15.2400000727, 3.0630883666), (-15.2400000753, 0.0000000078))
                Line((-6.0960000753, 0), (-15.2400000753, 0.0000000078))
                Line((-6.0960000753, 0), (-6.0960000727, 3.0630883588))
                Line((-6.0960000727, 3.0630883588), (-9.7112770689, 3.0630883619))
                CenterArc((-9.7112770689, 3.1011883619), 0.0381, 179.9999999513, 90)
                Line((-9.7493770689, 3.1011883619), (-9.7493770676, 4.6049388905))
                Line((-9.7493770676, 4.6049388905), (-5.1774133532, 4.6231541185))
                Line((-5.1702870865, 6.1086894198), (-5.1774133532, 4.6231541185))
                Line((-9.7493770663, 6.1086894192), (-5.1702870865, 6.1086894198))
            make_face()
            with BuildLine():
                CenterArc((-6.5799607634, 5.3268736854), 0.5334, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.8476966784, 5.3268736854), 0.5334, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.3780098866, 5.3268736854), 0.5334, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-14.9276805369, 5.3268736854), 0.5334, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2192
        extrude(amount=1.2192)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8938319931, perimeter: 3.3514510428
            with Locations((-14.9276805369, 5.3268736854)):
                Circle(0.5334)
            # Profile area: 0.8938319931, perimeter: 3.3514510428
            with Locations((-8.8476966784, 5.3268736854)):
                Circle(0.5334)
        # OneSide extrude, distance=3.6576
        extrude(amount=3.6576, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8938319931, perimeter: 3.3514510428
            with Locations((-6.5799607634, 5.3268736854)):
                Circle(0.5334)
            # Profile area: 0.8938319931, perimeter: 3.3514510428
            with Locations((-12.3780098866, 5.3268736854)):
                Circle(0.5334)
        # OneSide extrude, distance=1.2192
        extrude(amount=1.2192, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8938319931, perimeter: 3.3514510428
            with Locations((-6.5799607634, 5.3268736854)):
                Circle(0.5334)
            # Profile area: 0.8938319931, perimeter: 3.3514510428
            with Locations((-12.3780098866, 5.3268736854)):
                Circle(0.5334)
        # OneSide extrude, distance=-2.4384
        extrude(amount=-2.4384, mode=Mode.ADD)

        # Sketch4 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.785432978, perimeter: 18.6723702852
            with BuildLine():
                CenterArc((-9.144000113, 9.1440000979), 2.4384000301, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-9.144000113, 9.1440000979), 0.5334, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.1336
        extrude(amount=2.1336)
    return part.part


def model_111042_4f23bf6d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.3561944902, perimeter: 32.7123889804
            with BuildLine():
                Line((4, 1), (4, 4))
                Line((4, 4), (-2, 4))
                CenterArc((-2, 2), 2, 90, 90)
                Line((-4, 2), (-4, -5))
                Line((-4, -5), (-2, -5))
                Line((-2, -5), (-2, 0))
                CenterArc((-1, 0), 1, 90, 90)
                Line((-1, 1), (4, 1))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((-4.5, 0), (-0.5, 0))
                Line((-4.5, -4), (-4.5, 0))
                Line((-0.5, -4), (-4.5, -4))
                Line((-0.5, 0), (-0.5, -4))
            make_face()
            # Profile area: 18, perimeter: 17
            with BuildLine():
                Line((-0.5, 4.5), (-0.5, 0))
                Line((-4.5, 4.5), (-0.5, 4.5))
                Line((-4.5, 0), (-4.5, 4.5))
                Line((-4.5, 0), (-0.5, 0))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.2080068977, perimeter: 11.6369080848
            with BuildLine():
                Line((3.5297603599, 2.7113063175), (-0.5, 2.7113063175))
                Line((3.5297603599, 4.5), (3.5297603599, 2.7113063175))
                Line((-0.5, 4.5), (3.5297603599, 4.5))
                Line((-0.5, 2.7113063175), (-0.5, 4.5))
            make_face()
            # Profile area: 6.1516834648, perimeter: 11.1126469186
            with BuildLine():
                Line((3.5297603599, 0.4734369006), (-0.5, 0.4734369006))
                Line((3.5297603599, 2), (3.5297603599, 0.4734369006))
                Line((-0.5, 2), (3.5297603599, 2))
                Line((-0.5, 0.4734369006), (-0.5, 2))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.3561944902, perimeter: 61.4247779608
            with BuildLine():
                Line((1, -1), (-4, -1))
                Line((-4, -1), (-4, -4))
                Line((-4, -4), (2, -4))
                CenterArc((2, -2), 2, -90, 90)
                Line((4, -2), (4, 5))
                Line((4, 5), (2, 5))
                Line((2, 5), (2, 0))
                CenterArc((1, 0), 1, -90, 90)
            make_face()
            with BuildLine():
                CenterArc((1, 0), 1.5, -90, 90)
                Line((2.5, 4.5), (2.5, 0))
                Line((3.5, 4.5), (2.5, 4.5))
                Line((3.5, -2), (3.5, 4.5))
                CenterArc((2, -2), 1.5, -90, 90)
                Line((-3.5, -3.5), (2, -3.5))
                Line((-3.5, -1.5), (-3.5, -3.5))
                Line((1, -1.5), (-3.5, -1.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)
    return part.part


def model_111046_1e1ef6dc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.7853981634, perimeter: 15.5707963268
            with BuildLine():
                Line((-4, 3), (-1, 3))
                CenterArc((-4, 2), 1, 90, 90)
                Line((-5, -1), (-5, 2))
                Line((-4, -1), (-5, -1))
                Line((-4, 2), (-4, -1))
                Line((-1, 2), (-4, 2))
                Line((-1, 3), (-1, 2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4400000429, perimeter: 6.0000000894
            with BuildLine():
                Line((1.7000000253, 0.200000003), (-0.7000000104, 0.200000003))
                Line((1.7000000253, 0.8000000119), (1.7000000253, 0.200000003))
                Line((-0.7000000104, 0.8000000119), (1.7000000253, 0.8000000119))
                Line((-0.7000000104, 0.200000003), (-0.7000000104, 0.8000000119))
            make_face()
        # OneSide extrude, distance=-5.9
        extrude(amount=-5.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5000000149, perimeter: 5.4000000805
            with BuildLine():
                Line((-1.3000000194, 0.6000000089), (-3.8000000566, 0.6000000089))
                Line((-1.3000000194, 0.8000000119), (-1.3000000194, 0.6000000089))
                Line((-3.8000000566, 0.8000000119), (-1.3000000194, 0.8000000119))
                Line((-3.8000000566, 0.6000000089), (-3.8000000566, 0.8000000119))
            make_face()
            # Profile area: 0.5000000149, perimeter: 5.4000000805
            with BuildLine():
                Line((-1.3000000194, 0.200000003), (-3.8000000566, 0.200000003))
                Line((-1.3000000194, 0.400000006), (-1.3000000194, 0.200000003))
                Line((-3.8000000566, 0.400000006), (-1.3000000194, 0.400000006))
                Line((-3.8000000566, 0.200000003), (-3.8000000566, 0.400000006))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


def model_111049_dbb012af_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2061931861, perimeter: 7.3172705001
            with BuildLine():
                CenterArc((-3.299742668, 1.5876537094), 0.3, 90, 90)
                Line((-3.599742668, 0), (-3.599742668, 1.5876537094))
                Line((-3.2997426635, 0), (-3.599742668, 0))
                Line((-3.2997426635, 1.1876537034), (-3.2997426635, 0))
                CenterArc((-2.9997426635, 1.1876537034), 0.3, 90, 90)
                Line((-1.7000000253, 1.4876537034), (-2.9997426635, 1.4876537034))
                Line((-1.7000000253, 1.8876537094), (-1.7000000253, 1.4876537034))
                Line((-3.299742668, 1.8876537094), (-1.7000000253, 1.8876537094))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.4876537034), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8100000241, perimeter: 3.6000000536
            with BuildLine():
                Line((-1.9000000283, 0.200000003), (-2.8000000417, 0.200000003))
                Line((-1.9000000283, 1.1000000164), (-1.9000000283, 0.200000003))
                Line((-2.8000000417, 1.1000000164), (-1.9000000283, 1.1000000164))
                Line((-2.8000000417, 0.200000003), (-2.8000000417, 1.1000000164))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4487125513, perimeter: 6.4360513839
            with BuildLine():
                Line((2.9997426635, -1.5978060929), (1.8101524149, -1.5978060929))
                Line((1.8101524149, -1.5978060929), (1.8101524149, -1.7775013198))
                Line((1.8101524149, -1.7775013198), (3.299742668, -1.7775013198))
                CenterArc((3.299742668, -1.5876537094), 0.1898476105, -90, 90)
                Line((3.4895902785, -1.5876537094), (3.4895902785, -0.1101523895))
                Line((3.4895902785, -0.1101523895), (3.4098950531, -0.1101523895))
                Line((3.4098950531, -0.1101523895), (3.4098950531, -1.1876537034))
                CenterArc((2.9997426635, -1.1876537034), 0.4101523895, -90, 90)
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)
    return part.part


def model_111053_b2d052a7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.7057014784, perimeter: 27.7026878271
            with BuildLine():
                Line((4.3878485051, -1), (4.3878485051, 1))
                Line((4.3878485051, 1), (-0.5, 1))
                CenterArc((-0.5, -0.5), 1.5, 90, 90)
                Line((-2, -0.5), (-2, -7))
                Line((-2, -7), (-0.6336238727, -7))
                Line((-0.6336238727, -7), (-0.6336238727, -2))
                CenterArc((0.3663761273, -2), 1, 90, 90)
                Line((0.3663761273, -1), (4.3878485051, -1))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.6336238727, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.2645266985, perimeter: 12.1763511324
            with BuildLine():
                Line((-6, 0), (-2.9118244338, 0))
                Line((-6, 0), (-6, -3))
                Line((-6, -3), (-2.9118244338, -3))
                Line((-2.9118244338, -3), (-2.9118244338, 0))
            make_face()
            # Profile area: 11.5922299641, perimeter: 13.68384526
            with BuildLine():
                Line((-2.9118244338, 0), (-2.9118244338, 3.7537470638))
                Line((-2.9118244338, 3.7537470638), (-6, 3.7537470638))
                Line((-6, 3.7537470638), (-6, 0))
                Line((-6, 0), (-2.9118244338, 0))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.4172278017, perimeter: 7.9315360191
            with BuildLine():
                Line((3.7002410809, 2.7344730714), (1, 2.7344730714))
                Line((3.7002410809, 4), (3.7002410809, 2.7344730714))
                Line((1, 4), (3.7002410809, 4))
                Line((1, 2.7344730714), (1, 4))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.268619362, perimeter: 7.857314526
            with BuildLine():
                Line((3.7324221222, 0.8037648592), (1, 0.8037648592))
                Line((3.7324221222, 2), (3.7324221222, 0.8037648592))
                Line((1, 2), (3.7324221222, 2))
                Line((1, 0.8037648592), (1, 2))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5592493919, perimeter: 53.1288735925
            with BuildLine():
                Line((-0.3663761273, 1), (-4.3878485051, 1))
                Line((-4.3878485051, 1), (-4.3878485051, -1))
                Line((-4.3878485051, -1), (0.5, -1))
                CenterArc((0.5, 0.5), 1.5, -90, 90)
                Line((2, 0.5), (2, 7))
                Line((2, 7), (0.6336238727, 7))
                Line((0.6336238727, 7), (0.6336238727, 2))
                CenterArc((-0.3663761273, 2), 1, -90, 90)
            make_face()
            with BuildLine():
                CenterArc((-0.3663761273, 2), 1.2845627577, -90, 90)
                Line((0.9181866304, 6.7154372423), (0.9181866304, 2))
                Line((1.7154372423, 6.7154372423), (0.9181866304, 6.7154372423))
                Line((1.7154372423, 0.5), (1.7154372423, 6.7154372423))
                CenterArc((0.5, 0.5), 1.2154372423, -90, 90)
                Line((-4.1032857474, -0.7154372423), (0.5, -0.7154372423))
                Line((-4.1032857474, 0.7154372423), (-4.1032857474, -0.7154372423))
                Line((-0.3663761273, 0.7154372423), (-4.1032857474, 0.7154372423))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_111062_e59e2d31_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0578661757, perimeter: 0.8527413502
            with Locations((-0.4792742788, 0.4341261391)):
                Circle(0.1357180011)
            # Profile area: 0.0961015964, perimeter: 1.098930515
            with Locations((0.4438746091, 0.4965010639)):
                Circle(0.1749002236)
            # Profile area: 0.0478216211, perimeter: 0.7752059172
            with Locations((-0.4792742788, -0.3486791679)):
                Circle(0.1233778536)
            # Profile area: 0.0655752069, perimeter: 0.9077677862
            with Locations((0.5686244588, -0.3486791679)):
                Circle(0.1444757303)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0465696606, perimeter: 0.7649912514
            with Locations((0.4619827372, 0.3382849846)):
                Circle(0.1217521391)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_111237_40914f5f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8458412445, perimeter: 7.3079934511
            with BuildLine():
                Line((1, 4), (2.8458412445, 1.2470540285))
                Line((1, 4), (1, 2))
                Line((2.8458412445, 1.2470540285), (1, 2))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7207899001, perimeter: 6.9735265859
            with BuildLine():
                Line((-1, 2), (-1, 4))
                Line((-1, 4), (-2.7207899001, 1.3716052129))
                Line((-2.7207899001, 1.3716052129), (-1, 2))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.685999116, perimeter: 6.7088674014
            with BuildLine():
                Line((-1, 2), (-1, 4))
                Line((-1, 4), (-2.685999116, 1.5594771798))
                Line((-2.685999116, 1.5594771798), (-1, 2))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4849193255, perimeter: 6.4296162393
            with BuildLine():
                Line((1, 4), (2.6270520643, 1.6179857085))
                Line((1, 4), (1, 2.1747119737))
                Line((2.6270520643, 1.6179857085), (1, 2.1747119737))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_112181_d498e10b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.6722688298, perimeter: 18.9094220751
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 176.4198658567)
                Line((-2.4951210986, 0.1561111883), (-0.9935324062, -4.0669925917))
                CenterArc((0.0196455272, -3.4239758926), 1.2, -147.5986119676, 107.3063511947)
                Line((2.5, 0), (0.9349523526, -4.2))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1319617477, perimeter: 15.764357922
            with BuildLine():
                CenterArc((0.0213596657, 2.6), 1.25, -54.4957146186, 288.0500514159)
                CenterArc((0, 0), 1.75, 114.3382792632, 310.3820636523)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8456714755, perimeter: 9
            with BuildLine():
                Line((0.7505351559, 1.2987289863), (-0.7494647168, 1.2993470046))
                Line((-0.7494647168, 1.2993470046), (-1.4999998727, 0.0006180183))
                Line((-1.4999998727, 0.0006180183), (-0.7505351559, -1.2987289863))
                Line((-0.7505351559, -1.2987289863), (0.7494647168, -1.2993470046))
                Line((0.7494647168, -1.2993470046), (1.4999998727, -0.0006180183))
                Line((1.4999998727, -0.0006180183), (0.7505351559, 1.2987289863))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_112292_7c09fb5a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2365752407, perimeter: 2.4904352938
            with BuildLine():
                CenterArc((0, -1.9000000283), 0.5000000075, 41.1077642385, 48.8922357615)
                Line((0, -1.4000000209), (0, -1.7475000283))
                CenterArc((0, -1.9000000283), 0.1525, -90, 180)
                Line((0, -2.0525000283), (0, -2.3))
                Line((0, -2.3), (0.25, -2.3))
                Line((0.3767371573, -1.5712613453), (0.25, -2.3))
            make_face()
            # Profile area: 0.2365752407, perimeter: 2.4904352938
            with BuildLine():
                Line((-0.3767371573, -1.5712613453), (-0.25, -2.3))
                Line((0, -2.3), (-0.25, -2.3))
                Line((0, -2.0525000283), (0, -2.3))
                CenterArc((0, -1.9000000283), 0.1525, 90, 180)
                Line((0, -1.4000000209), (0, -1.7475000283))
                CenterArc((0, -1.9000000283), 0.5000000075, 90, 48.8922357615)
            make_face()
            # Profile area: 0.8629854429, perimeter: 5.1918752056
            with BuildLine():
                Line((0.6118348624, 0.2194495413), (0.3767371573, 1.5712613453))
                CenterArc((0, 1.9000000283), 0.5000000075, -138.8922357615, 97.784471523)
                Line((-0.6118348624, 0.2194495413), (-0.3767371573, 1.5712613453))
                CenterArc((0, 0), 0.65, 19.7316138862, 140.5367722277)
            make_face()
            # Profile area: 0.2813138206, perimeter: 2.2126121624
            with BuildLine():
                CenterArc((0, 0), 0.25, -90, 90)
                Line((0, -0.25), (0, -0.65))
                CenterArc((0, 0), 0.65, -90, 70.2683861138)
                Line((0.65, 0), (0.6118348624, -0.2194495413))
                Line((0.25, 0), (0.65, 0))
            make_face()
            # Profile area: 0.4731504813, perimeter: 3.7908706293
            with BuildLine():
                CenterArc((0, 1.9000000283), 0.5000000075, -138.8922357615, 97.784471523)
                Line((0.3767371573, 1.5712613453), (0.25, 2.3))
                Line((0, 2.3), (0.25, 2.3))
                Line((0, 2.3), (-0.25, 2.3))
                Line((-0.3767371573, 1.5712613453), (-0.25, 2.3))
            make_face()
            with BuildLine():
                CenterArc((0, 1.9000000283), 0.1525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.8439414618, perimeter: 5.0378364872
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 270)
                Line((0.25, 0), (0.65, 0))
                Line((0.65, 0), (0.6118348624, 0.2194495413))
                CenterArc((0, 0), 0.65, 19.7316138862, 140.5367722277)
                Line((-0.65, 0), (-0.6118348624, 0.2194495413))
                Line((-0.65, 0), (-0.6118348624, -0.2194495413))
                CenterArc((0, 0), 0.65, -160.2683861138, 70.2683861138)
                Line((0, -0.25), (0, -0.65))
            make_face()
            # Profile area: 0.4314927214, perimeter: 3.3459376237
            with BuildLine():
                Line((0, -0.65), (0, -1.4000000209))
                CenterArc((0, -1.9000000283), 0.5000000075, 41.1077642385, 48.8922357615)
                Line((0.6118348624, -0.2194495413), (0.3767371573, -1.5712613453))
                CenterArc((0, 0), 0.65, -90, 70.2683861138)
            make_face()
            # Profile area: 0.4314927214, perimeter: 3.3459376237
            with BuildLine():
                Line((-0.6118348624, -0.2194495413), (-0.3767371573, -1.5712613453))
                CenterArc((0, -1.9000000283), 0.5000000075, 90, 48.8922357615)
                Line((0, -0.65), (0, -1.4000000209))
                CenterArc((0, 0), 0.65, -160.2683861138, 70.2683861138)
            make_face()
            # Profile area: 0.0365308321, perimeter: 0.7840928797
            with BuildLine():
                Line((0, -1.7475000283), (0, -2.0525000283))
                CenterArc((0, -1.9000000283), 0.1525, -90, 180)
            make_face()
            # Profile area: 0.0365308321, perimeter: 0.7840928797
            with BuildLine():
                CenterArc((0, -1.9000000283), 0.1525, 90, 180)
                Line((0, -1.7475000283), (0, -2.0525000283))
            make_face()
            # Profile area: 0.0730616642, perimeter: 0.9581857593
            with Locations((0, 1.9000000283)):
                Circle(0.1525)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1500000028, perimeter: 1.6000000075
            with BuildLine():
                Line((-0.5500000082, 0.6499999978), (-0.25, 0.6499999978))
                Line((-0.5500000082, 0.1500000022), (-0.5500000082, 0.6499999978))
                Line((-0.25, 0.1500000022), (-0.5500000082, 0.1500000022))
                Line((-0.25, 0.6499999978), (-0.25, 0.1500000022))
            make_face()
            # Profile area: 0.1500000028, perimeter: 1.6000000075
            with BuildLine():
                Line((0.25, 0.1500000022), (0.25, 0.6499999978))
                Line((0.5500000082, 0.1500000022), (0.25, 0.1500000022))
                Line((0.5500000082, 0.6499999978), (0.5500000082, 0.1500000022))
                Line((0.25, 0.6499999978), (0.5500000082, 0.6499999978))
            make_face()
            # Profile area: 0.2499999978, perimeter: 1.9999999911
            with BuildLine():
                Line((-0.25, 0.6499999978), (0.25, 0.6499999978))
                Line((-0.25, 0.6499999978), (-0.25, 0.1500000022))
                Line((0.25, 0.1500000022), (-0.25, 0.1500000022))
                Line((0.25, 0.1500000022), (0.25, 0.6499999978))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1500000028, perimeter: 1.6000000075
            with BuildLine():
                Line((-0.5500000082, 0.6499999978), (-0.25, 0.6499999978))
                Line((-0.5500000082, 0.1500000022), (-0.5500000082, 0.6499999978))
                Line((-0.25, 0.1500000022), (-0.5500000082, 0.1500000022))
                Line((-0.25, 0.6499999978), (-0.25, 0.1500000022))
            make_face()
            # Profile area: 0.1500000028, perimeter: 1.6000000075
            with BuildLine():
                Line((0.25, 0.1500000022), (0.25, 0.6499999978))
                Line((0.5500000082, 0.1500000022), (0.25, 0.1500000022))
                Line((0.5500000082, 0.6499999978), (0.5500000082, 0.1500000022))
                Line((0.25, 0.6499999978), (0.5500000082, 0.6499999978))
            make_face()
            # Profile area: 0.2499999978, perimeter: 1.9999999911
            with BuildLine():
                Line((-0.25, 0.6499999978), (0.25, 0.6499999978))
                Line((-0.25, 0.6499999978), (-0.25, 0.1500000022))
                Line((0.25, 0.1500000022), (-0.25, 0.1500000022))
                Line((0.25, 0.1500000022), (0.25, 0.6499999978))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0365308321, perimeter: 0.7840928797
            with BuildLine():
                Line((0, -1.7475000283), (0, -2.0525000283))
                CenterArc((0, -1.9000000283), 0.1525, -90, 180)
            make_face()
            # Profile area: 0.0365308321, perimeter: 0.7840928797
            with BuildLine():
                CenterArc((0, -1.9000000283), 0.1525, 90, 180)
                Line((0, -1.7475000283), (0, -2.0525000283))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0730616642, perimeter: 0.9581857593
            with Locations((0, 1.9000000283)):
                Circle(0.1525)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


def model_113001_c1b164a3_0002():
    """Model: Spoiler v1 v3 v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1400000042, perimeter: 2.2000000328
            with BuildLine():
                Line((-0.5000000075, 0.200000003), (-0.5000000075, 0))
                Line((-0.5000000075, 0), (-0.1000000015, 0))
                Line((-0.1000000015, 0), (-0.1000000015, 0.200000003))
                Line((-0.1000000015, 0.200000003), (0.3000000045, 0.5000000075))
                Line((0.3000000045, 0.5000000075), (0.1000000015, 0.5000000075))
                Line((0.1000000015, 0.5000000075), (-0.3000000045, 0.200000003))
                Line((-0.3000000045, 0.200000003), (-0.5000000075, 0.200000003))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0000000298, perimeter: 6.6000000238
            with BuildLine():
                Line((0.1000000015, -0.5000000075), (2.6000000015, -0.5000000075))
                Line((2.6000000015, -0.5000000075), (2.6000000015, 0.3000000045))
                Line((0.1000000015, 0.3000000045), (2.6000000015, 0.3000000045))
                Line((0.1000000015, -0.5000000075), (0.1000000015, 0.3000000045))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.1005096296, perimeter: 2.2930352781
            with BuildLine():
                Line((-0.101263669, 0.6000000089), (-0.2012636705, 0.5000000075))
                Line((-0.2012636705, 0.5000000075), (0.1000000015, 0.5000000075))
                Line((0.1000000015, 0.5000000075), (0.3000000045, 0.5000000075))
                Line((0.3000000045, 0.5000000075), (0.8038326102, 0.5000000075))
                Line((0.8038326102, 0.5000000075), (0.9038326117, 0.6000000089))
                Line((0.9038326117, 0.6000000089), (-0.101263669, 0.6000000089))
            make_face()
        # TwoSides extrude, along=4.1, against=-1.3
        extrude(amount=4.1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-1.3, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.244869481, perimeter: 5.319826727
            with BuildLine():
                Line((-0.2012636705, 0.400000006), (0.8000000119, 0.400000006))
                Line((0.8000000119, 0.400000006), (1.1000000164, 0.7000000104))
                Line((1.1000000164, 0.7000000104), (-0.2012636705, 0.7000000104))
                Line((-0.2012636705, 0.7000000104), (-0.2012636705, 0.5000000075))
                Line((-0.101263669, 0.6000000089), (-0.2012636705, 0.5000000075))
                Line((0.9038326117, 0.6000000089), (-0.101263669, 0.6000000089))
                Line((0.8038326102, 0.5000000075), (0.9038326117, 0.6000000089))
                Line((-0.2012636705, 0.5000000075), (0.8038326102, 0.5000000075))
                Line((-0.2012636705, 0.5000000075), (-0.2012636705, 0.400000006))
            make_face()
            # Profile area: 0.1005096296, perimeter: 2.2930352781
            with BuildLine():
                Line((-0.2012636705, 0.5000000075), (0.8038326102, 0.5000000075))
                Line((0.8038326102, 0.5000000075), (0.9038326117, 0.6000000089))
                Line((0.9038326117, 0.6000000089), (-0.101263669, 0.6000000089))
                Line((-0.101263669, 0.6000000089), (-0.2012636705, 0.5000000075))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.244869481, perimeter: 5.319826727
            with BuildLine():
                Line((0.2012636705, 0.5000000075), (0.2012636705, 0.400000006))
                Line((-0.8038326102, 0.5000000075), (0.2012636705, 0.5000000075))
                Line((-0.9038326117, 0.6000000089), (-0.8038326102, 0.5000000075))
                Line((0.101263669, 0.6000000089), (-0.9038326117, 0.6000000089))
                Line((0.2012636705, 0.5000000075), (0.101263669, 0.6000000089))
                Line((0.2012636705, 0.7000000104), (0.2012636705, 0.5000000075))
                Line((-1.1000000164, 0.7000000104), (0.2012636705, 0.7000000104))
                Line((-0.8000000119, 0.400000006), (-1.1000000164, 0.7000000104))
                Line((0.2012636705, 0.400000006), (-0.8000000119, 0.400000006))
            make_face()
            # Profile area: 0.1005096296, perimeter: 2.2930352781
            with BuildLine():
                Line((0.2012636705, 0.5000000075), (0.101263669, 0.6000000089))
                Line((0.101263669, 0.6000000089), (-0.9038326117, 0.6000000089))
                Line((-0.9038326117, 0.6000000089), (-0.8038326102, 0.5000000075))
                Line((-0.8038326102, 0.5000000075), (0.2012636705, 0.5000000075))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_113001_c1b164a3_0004():
    """Model: Wheel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.3373613574, perimeter: 7.3827427359
            Circle(1.175)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.75, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            Circle(0.5000000075)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.55, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0243284935, perimeter: 0.552920307
            Circle(0.088)
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.55, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0, 0.2499999944)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.25, -0.0000000056)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-0.25, -0.0000000056)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0, -0.2500000056)):
                Circle(0.025)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)
    return part.part


def model_113001_c1b164a3_0006():
    """Model: Tail Pipe v1 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0400000012, perimeter: 1.0000000149
            with BuildLine():
                Line((0.1000000015, -0.400000006), (0, -0.400000006))
                Line((0.1000000015, 0), (0.1000000015, -0.400000006))
                Line((0, 0), (0.1000000015, 0))
                Line((0, -0.400000006), (0, 0))
            make_face()
        # TwoSides extrude, along=0.2, against=-0.1
        extrude(amount=0.2)
        extrude(sk.sketch, amount=-0.1)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0426119968, perimeter: 0.8716477479
            with BuildLine():
                CenterArc((0.1799999993, 0.269999994), 0.125, 156.9260808887, 46.1478382226)
                CenterArc((-0.0499999989, 0.269999994), 0.125, 23.0739191113, 223.3479011064)
                Line((-0.1000000015, 0.2), (-0.1000000015, 0.1554356027))
                Line((0, 0.2), (-0.1000000015, 0.2))
                Line((0, 0.1554356011), (0, 0.2))
                CenterArc((-0.0499999989, 0.269999994), 0.125, -66.4218220807, 43.3479029694)
            make_face()
            # Profile area: 0.0013172174, perimeter: 0.2013579299
            with BuildLine():
                CenterArc((0.1799999993, 0.269999994), 0.125, 156.9260808887, 46.1478382226)
                CenterArc((-0.0499999989, 0.269999994), 0.125, -23.0739191113, 46.1478382226)
            make_face()
            # Profile area: 0.005158171, perimeter: 0.2920080108
            with BuildLine():
                CenterArc((-0.0499999989, 0.269999994), 0.125, -113.5781797824, 47.1563577016)
                Line((0, 0.1554356011), (0, 0.2))
                Line((0, 0.2), (-0.1000000015, 0.2))
                Line((-0.1000000015, 0.2), (-0.1000000015, 0.1554356027))
            make_face()
        # TwoSides extrude (symmetric), distance=0.4
        extrude(amount=0.4, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.0499999989, 0.269999994)):
                Circle(0.1)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0477701678, perimeter: 0.7853981634
            with BuildLine():
                CenterArc((-0.0499999989, 0.269999994), 0.125, -23.0739191113, 46.1478382226)
                CenterArc((0.1799999993, 0.269999994), 0.125, -156.9260808887, 313.8521617774)
            make_face()
        # TwoSides extrude (symmetric), distance=0.4
        extrude(amount=0.4, both=True, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.1799999993, 0.269999994)):
                Circle(0.1)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_114429_70217b24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.8867234656, perimeter: 64.7168086639
            with BuildLine():
                CenterArc((0, 0), 5.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.7797286614, perimeter: 60.4756585816
            with BuildLine():
                CenterArc((0, 0), 4.875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.05
        extrude(amount=4.05, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6259088157, perimeter: 3.7074625318
            with BuildLine():
                CenterArc((0, 0), 5.55, -98.081358282, 16.0422038852)
                Line((-0.3976034847, -5.9877853804), (-0.7802140662, -5.4948854411))
                CenterArc((-0.0026339636, -5.6811926906), 0.5, -142.1798152612, 104.7282507706)
                Line((0.7686547198, -5.4965143429), (0.3942998758, -5.9852379622))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.ADD)
    return part.part


def model_115533_da81d57e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 133.4596469955, perimeter: 184.5136219395
            with BuildLine():
                Line((-7.2731493399, -3.660303038), (-7.2731493399, -15.539696962))
                Line((-4.939696962, -17.8731493399), (-7.2731493399, -15.539696962))
                Line((-4.2223611076, -17.1558134855), (-4.939696962, -17.8731493399))
                CenterArc((-2.4545941546, -18.9235804385), 2.5, 90, 45)
                Line((-2.4545941546, -16.4235804385), (4.4545941546, -16.4235804385))
                CenterArc((4.4545941546, -18.9235804385), 2.5, 45, 45)
                Line((6.939696962, -17.8731493399), (6.2223611076, -17.1558134855))
                Line((9.2731493399, -15.539696962), (6.939696962, -17.8731493399))
                Line((9.2731493399, -3.660303038), (9.2731493399, -15.539696962))
                Line((6.939696962, -1.3268506601), (9.2731493399, -3.660303038))
                Line((6.2223611076, -2.0441865145), (6.939696962, -1.3268506601))
                CenterArc((4.4545941546, -0.2764195615), 2.5, -90, 45)
                Line((-2.4545941546, -2.7764195615), (4.4545941546, -2.7764195615))
                CenterArc((-2.4545941546, -0.2764195615), 2.5, -135, 45)
                Line((-4.939696962, -1.3268506601), (-4.2223611076, -2.0441865145))
                Line((-7.2731493399, -3.660303038), (-4.939696962, -1.3268506601))
            make_face()
            with BuildLine():
                CenterArc((-5.3993163697, -3.2006836303), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.3993163697, -3.2006836303), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.3993163697, -15.9993163697), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.3993163697, -15.9993163697), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.2928932188, -9.2464466094), (-3.8444838686, -5.1090695219))
                CenterArc((-0.0606601718, -9.6), 0.5, -45, 90)
                Line((-3.8444838686, -14.0909304781), (0.2928932188, -9.9535533906))
                CenterArc((-3.9859052249, -13.9495091218), 0.2, -169.2288663278, 124.2288663278)
                CenterArc((-3.2, -13.8), 1, 180, 10.7711336722)
                Line((-4.2, -5.4), (-4.2, -13.8))
                CenterArc((-3.2, -5.4), 1, 169.2288663278, 10.7711336722)
                CenterArc((-3.9859052249, -5.2504908782), 0.2, 45, 124.2288663278)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.6464466094, -8.8928932188), (-3.4909304781, -4.7555161314))
                CenterArc((-3.3495091218, -4.6140947751), 0.2, 100.7711336722, 124.2288663278)
                CenterArc((-3.2, -5.4), 1, 90, 10.7711336722)
                Line((5.2, -4.4), (-3.2, -4.4))
                CenterArc((5.2, -5.4), 1, 79.2288663278, 10.7711336722)
                CenterArc((5.3495091218, -4.6140947751), 0.2, -45, 124.2288663278)
                Line((1.3535533906, -8.8928932188), (5.4909304781, -4.7555161314))
                CenterArc((1, -8.5393398282), 0.5, -135, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((5.8444838686, -14.0909304781), (1.7071067812, -9.9535533906))
                CenterArc((2.0606601718, -9.6), 0.5, 135, 90)
                Line((1.7071067812, -9.2464466094), (5.8444838686, -5.1090695219))
                CenterArc((5.9859052249, -5.2504908782), 0.2, 10.7711336722, 124.2288663278)
                CenterArc((5.2, -5.4), 1, 0, 10.7711336722)
                Line((6.2, -13.8), (6.2, -5.4))
                CenterArc((5.2, -13.8), 1, -10.7711336722, 10.7711336722)
                CenterArc((5.9859052249, -13.9495091218), 0.2, -135, 124.2288663278)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.4909304781, -14.4444838686), (0.6464466094, -10.3071067812))
                CenterArc((1, -10.6606601718), 0.5, 45, 90)
                Line((5.4909304781, -14.4444838686), (1.3535533906, -10.3071067812))
                CenterArc((5.3495091218, -14.5859052249), 0.2, -79.2288663278, 124.2288663278)
                CenterArc((5.2, -13.8), 1, -90, 10.7711336722)
                Line((-3.2, -14.8), (5.2, -14.8))
                CenterArc((-3.2, -13.8), 1, -100.7711336722, 10.7711336722)
                CenterArc((-3.3495091218, -14.5859052249), 0.2, 135, 124.2288663278)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.0811183182, -17.0953318806), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.4953318806, -15.6811183182), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.7175144213, -14.9033008589), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.3033008589, -16.3175144213), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.4953318806, -3.5188816818), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.0811183182, -2.1046681194), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.3033008589, -2.8824855787), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.7175144213, -4.2966991411), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.0811183182, -2.1046681194), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.4953318806, -3.5188816818), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.7175144213, -4.2966991411), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3033008589, -2.8824855787), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.4953318806, -15.6811183182), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.0811183182, -17.0953318806), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3033008589, -16.3175144213), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.7175144213, -14.9033008589), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((5.5, 5.85)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((-7.5, 5.85)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((-7.5, 7.85)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((5.5, 7.85)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((5.5, 11.35)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((-7.5, 11.35)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((-7.5, 13.35)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((5.5, 13.35)):
                Circle(0.175)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7500000224, perimeter: 4.0000000596
            with BuildLine():
                Line((-4.5000000671, 11.5000001714), (-5.0000000745, 11.5000001714))
                Line((-4.5000000671, 13.0000001937), (-4.5000000671, 11.5000001714))
                Line((-5.0000000745, 13.0000001937), (-4.5000000671, 13.0000001937))
                Line((-5.0000000745, 11.5000001714), (-5.0000000745, 13.0000001937))
            make_face()
            # Profile area: 0.7500000224, perimeter: 4.0000000596
            with BuildLine():
                Line((-5.0000000745, 7.6999998286), (-5.0000000745, 6.1999998063))
                Line((-5.0000000745, 6.1999998063), (-4.5000000671, 6.1999998063))
                Line((-4.5000000671, 6.1999998063), (-4.5000000671, 7.6999998286))
                Line((-4.5000000671, 7.6999998286), (-5.0000000745, 7.6999998286))
            make_face()
            # Profile area: 0.7500000224, perimeter: 4.0000000596
            with BuildLine():
                Line((6.5000000969, 6.1999998063), (6.5000000969, 7.6999998286))
                Line((7.0000001043, 6.1999998063), (6.5000000969, 6.1999998063))
                Line((7.0000001043, 7.6999998286), (7.0000001043, 6.1999998063))
                Line((6.5000000969, 7.6999998286), (7.0000001043, 7.6999998286))
            make_face()
            # Profile area: 0.7500000224, perimeter: 4.0000000596
            with BuildLine():
                Line((6.5000000969, 13.0000001937), (6.5000000969, 11.5000001714))
                Line((6.5000000969, 11.5000001714), (7.0000001043, 11.5000001714))
                Line((7.0000001043, 11.5000001714), (7.0000001043, 13.0000001937))
                Line((7.0000001043, 13.0000001937), (6.5000000969, 13.0000001937))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.1999998063), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((4.7500000745, -0.45)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-6.7500000969, -0.45)):
                Circle(0.125)
        # OneSide extrude, distance=-6.8
        extrude(amount=-6.8, mode=Mode.SUBTRACT)
    return part.part


def model_115637_b4d41e8a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 361, perimeter: 76
            with BuildLine():
                Line((19, -19), (0, -19))
                Line((19, 0), (19, -19))
                Line((0, 0), (19, 0))
                Line((0, -19), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.44, perimeter: 7.7
            with BuildLine():
                Line((11.025, 0), (11.025, 0.8))
                Line((11.025, 0.8), (7.975, 0.8))
                Line((7.975, 0.8), (7.975, 0))
                Line((7.975, 0), (11.025, 0))
            make_face()
            # Profile area: 2.44, perimeter: 7.7
            with BuildLine():
                Line((7.975, 0), (11.025, 0))
                Line((7.975, 0), (7.975, -0.8))
                Line((7.975, -0.8), (11.025, -0.8))
                Line((11.025, -0.8), (11.025, 0))
            make_face()
        # OneSide extrude, distance=-1.02
        extrude(amount=-1.02, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(19, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.44, perimeter: 7.7
            with BuildLine():
                Line((-7.975, 0.8), (-7.975, 0))
                Line((-11.025, 0.8), (-7.975, 0.8))
                Line((-11.025, 0), (-11.025, 0.8))
                Line((-11.025, 0), (-7.975, 0))
            make_face()
            # Profile area: 2.44, perimeter: 7.7
            with BuildLine():
                Line((-11.025, 0), (-7.975, 0))
                Line((-11.025, -0.8), (-11.025, 0))
                Line((-7.975, -0.8), (-11.025, -0.8))
                Line((-7.975, 0), (-7.975, -0.8))
            make_face()
        # OneSide extrude, distance=-1.02
        extrude(amount=-1.02, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.81, perimeter: 3.6
            with BuildLine():
                Line((-1.9500000224, 13.4500001937), (-1.9500000224, 12.5500001937))
                Line((-1.9500000224, 12.5500001937), (-1.0500000224, 12.5500001937))
                Line((-1.0500000224, 12.5500001937), (-1.0500000224, 13.4500001937))
                Line((-1.0500000224, 13.4500001937), (-1.9500000224, 13.4500001937))
            make_face()
            # Profile area: 0.81, perimeter: 3.6
            with BuildLine():
                Line((-1.9500000224, 1.9500000224), (-1.9500000224, 1.0500000224))
                Line((-1.9500000224, 1.0500000224), (-1.0500000224, 1.0500000224))
                Line((-1.0500000224, 1.0500000224), (-1.0500000224, 1.9500000224))
                Line((-1.0500000224, 1.9500000224), (-1.9500000224, 1.9500000224))
            make_face()
            # Profile area: 0.81, perimeter: 3.6
            with BuildLine():
                Line((-13.4500001937, 1.9500000224), (-13.4500001937, 1.0500000224))
                Line((-13.4500001937, 1.0500000224), (-12.5500001937, 1.0500000224))
                Line((-12.5500001937, 1.0500000224), (-12.5500001937, 1.9500000224))
                Line((-12.5500001937, 1.9500000224), (-13.4500001937, 1.9500000224))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 255.9999985695, perimeter: 63.9999998212
            with BuildLine():
                Line((-3.0000000447, 19), (-3.0000000447, 3.0000000447))
                Line((-19, 19), (-3.0000000447, 19))
                Line((-19, 3.0000000447), (-19, 19))
                Line((-3.0000000447, 3.0000000447), (-19, 3.0000000447))
            make_face()
        # OneSide extrude, distance=-0.07
        extrude(amount=-0.07, mode=Mode.SUBTRACT)
    return part.part


def model_115637_d920ac27_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 361, perimeter: 76
            with BuildLine():
                Line((19, -19), (0, -19))
                Line((19, 0), (19, -19))
                Line((0, 0), (19, 0))
                Line((0, -19), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.25, perimeter: 7.5
            with BuildLine():
                Line((11, 0), (11, 0.75))
                Line((11, 0.75), (8, 0.75))
                Line((8, 0.75), (8, 0))
                Line((8, 0), (11, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(19, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.25, perimeter: 7.5
            with BuildLine():
                Line((-8, 0), (-8, 0.75))
                Line((-8, 0.75), (-11, 0.75))
                Line((-11, 0.75), (-11, 0))
                Line((-11, 0), (-8, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0000000298, perimeter: 4.0000000596
            with BuildLine():
                Line((-1.0000000149, 12.5000001863), (-1.0000000149, 13.5000002012))
                Line((-1.0000000149, 13.5000002012), (-2.0000000298, 13.5000002012))
                Line((-2.0000000298, 13.5000002012), (-2.0000000298, 12.5000001863))
                Line((-2.0000000298, 12.5000001863), (-1.0000000149, 12.5000001863))
            make_face()
            # Profile area: 1.0000000298, perimeter: 4.0000000596
            with BuildLine():
                Line((-2.0000000298, 2.0000000298), (-1.0000000149, 2.0000000298))
                Line((-2.0000000298, 1.0000000149), (-2.0000000298, 2.0000000298))
                Line((-1.0000000149, 1.0000000149), (-2.0000000298, 1.0000000149))
                Line((-1.0000000149, 2.0000000298), (-1.0000000149, 1.0000000149))
            make_face()
            # Profile area: 1.0000000298, perimeter: 4.0000000596
            with BuildLine():
                Line((-13.5000002012, 2.0000000298), (-13.5000002012, 1.0000000149))
                Line((-13.5000002012, 1.0000000149), (-12.5000001863, 1.0000000149))
                Line((-12.5000001863, 1.0000000149), (-12.5000001863, 2.0000000298))
                Line((-12.5000001863, 2.0000000298), (-13.5000002012, 2.0000000298))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 255.9999985695, perimeter: 63.9999998212
            with BuildLine():
                Line((-3.0000000447, 19), (-3.0000000447, 3.0000000447))
                Line((-19, 19), (-3.0000000447, 19))
                Line((-19, 3.0000000447), (-19, 19))
                Line((-3.0000000447, 3.0000000447), (-19, 3.0000000447))
            make_face()
        # OneSide extrude, distance=-0.07
        extrude(amount=-0.07, mode=Mode.SUBTRACT)
    return part.part


def model_116825_d3abda56_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # button base -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0818194671, perimeter: 7.9969911184
            with BuildLine():
                Line((0.6749999978, -0.3344670532), (0.6749999978, 0.9190975078))
                Line((0.6749999978, 0.9190975078), (-0.6750000022, 0.9190975078))
                Line((-0.6750000022, 0.9190975078), (-0.6750000022, -0.3344670532))
                Line((-0.6750000022, -0.3344670532), (-0.6750000022, -0.4273379313))
                Line((-0.6750000022, -0.4273379313), (-0.6750000022, -0.8809024922))
                Line((-0.6750000022, -0.8809024922), (-0.3100000022, -0.8809024922))
                CenterArc((-0.3100000022, -0.7609024922), 0.12, -90, 90)
                Line((-0.1900000022, 0.0190975078), (-0.1900000022, -0.7609024922))
                Line((-0.1375000022, 0.0190975078), (-0.1900000022, 0.0190975078))
                Line((0.1374999978, 0.0190975078), (-0.1375000022, 0.0190975078))
                Line((0.1899999978, 0.0190975078), (0.1374999978, 0.0190975078))
                Line((0.1899999978, -0.7609024922), (0.1899999978, 0.0190975078))
                CenterArc((0.3099999978, -0.7609024922), 0.12, 180, 90)
                Line((0.3099999978, -0.8809024922), (0.6749999978, -0.8809024922))
                Line((0.6749999978, -0.8809024922), (0.6749999978, -0.4273379313))
                Line((0.6749999978, -0.4184024922), (0.6749999978, -0.4273379313))
                Line((0.6749999978, -0.3344670532), (0.6749999978, -0.4184024922))
            make_face()
        # Symmetric extrude, each_side=0.675
        extrude(amount=0.675, both=True)

        # button connection -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1, perimeter: 2.2
            with BuildLine():
                Line((-0.5000000022, 1.0190975078), (0.4999999978, 1.0190975078))
                Line((-0.5000000022, 0.9190975078), (-0.5000000022, 1.0190975078))
                Line((0.4999999978, 0.9190975078), (-0.5000000022, 0.9190975078))
                Line((0.4999999978, 1.0190975078), (0.4999999978, 0.9190975078))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sring mount -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.07425, perimeter: 1.09
            with BuildLine():
                Line((-0.1375000022, -0.2509024922), (0.1374999978, -0.2509024922))
                Line((0.1374999978, 0.0190975078), (0.1374999978, -0.2509024922))
                Line((-0.1375000022, 0.0190975078), (0.1374999978, 0.0190975078))
                Line((-0.1375000022, -0.2509024922), (-0.1375000022, 0.0190975078))
            make_face()
        # Symmetric extrude, each_side=0.1375
        extrude(amount=0.1375, both=True, mode=Mode.ADD)

        # rubber stopper -> Extrude4 (Join)
        # Sketch on Profile plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0097765796, perimeter: 0.4896109197
            with BuildLine():
                Line((-0.0999999978, -0.2899999933), (-0.0999999978, -0.2509024922))
                CenterArc((-0.0899999978, -0.2899999933), 0.01, 180, 90)
                Line((0.0899999978, -0.2999999933), (-0.0899999978, -0.2999999933))
                CenterArc((0.0899999978, -0.2899999933), 0.01, -90, 90)
                Line((0.0999999978, -0.2509024922), (0.0999999978, -0.2899999933))
                Line((-0.0999999978, -0.2509024922), (0.0999999978, -0.2509024922))
            make_face()
        # Symmetric extrude, full_length=True, total=0.18
        extrude(amount=0.09, both=True, mode=Mode.ADD)
    return part.part


def model_117144_bc95d940_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.3573009183, perimeter: 30.5415926536
            with BuildLine():
                Line((-4.7602249355, -0.9924548412), (-4.7602249355, -2.1924548412))
                Line((-4.7602249355, -2.1924548412), (5.2397750645, -2.1924548412))
                Line((5.2397750645, -2.1924548412), (5.2397750645, -0.9924548412))
                Line((5.2397750645, -0.9924548412), (-4.7602249355, -0.9924548412))
            make_face()
            with BuildLine():
                Line((-3.6630407738, -1.7924548412), (-1.1630407738, -1.7924548412))
                CenterArc((-3.6630407738, -1.5424548412), 0.25, 90, 180)
                Line((-1.1630407738, -1.2924548412), (-3.6630407738, -1.2924548412))
                CenterArc((-1.1630407738, -1.5424548412), 0.25, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7397750645, -1.5924548412), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5889185409, perimeter: 26.2241655703
            with BuildLine():
                Line((4.1761724749, 1.6536269376), (0.3836131773, 1.6536269376))
                CenterArc((0.0054928261, 1.4286269376), 0.44, 30.754703633, 118.4905927339)
                Line((-0.3726275251, 1.6536269376), (-4.1651868227, 1.6536269376))
                CenterArc((-4.5433071739, 1.4286269376), 0.44, 30.754703633, 298.4905927339)
                Line((-4.1651868227, 1.2036269376), (-0.3726275251, 1.2036269376))
                CenterArc((0.0054928261, 1.4286269376), 0.44, -149.245296367, 118.4905927339)
                Line((0.3836131773, 1.2036269376), (4.1761724749, 1.2036269376))
                CenterArc((4.5542928261, 1.4286269376), 0.44, -149.245296367, 298.4905927339)
            make_face()
            with BuildLine():
                CenterArc((-4.5433071739, 1.4286269376), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0054928261, 1.4286269376), 0.24, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5542928261, 1.4286269376), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1809557368, perimeter: 1.5079644737
            with Locations((-2.1286105336, 0.3624410352)):
                Circle(0.24)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1809557368, perimeter: 1.5079644737
            with Locations((0.5514100239, 0.236024915)):
                Circle(0.24)
        # OneSide extrude, distance=5.4
        extrude(amount=5.4)
    return part.part


def model_119894_8b172e77_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 34 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 54.6661989701, perimeter: 36.4943265629
            with BuildLine():
                Line((-5.4399207856, -3.513680673), (-5.4399207856, -10.1993535741))
                Line((-19.5480873105, -3.513680673), (-5.4399207856, -3.513680673))
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -125.892997277, 21.074690002)
            make_face()
            # Profile area: 156.2115593008, perimeter: 52.1971894899
            with BuildLine():
                Line((20.3418533905, -8.8023870224), (20.3591299638, -8.9405996084))
                Line((20.1945357937, -7.6238462478), (20.3418533905, -8.8023870224))
                Line((18.5571183646, -7.8285234265), (20.1945357937, -7.6238462478))
                Line((11.254868465, 1.4652491725), (18.5571183646, -7.8285234265))
                Line((1.5107989252, -1.052896862), (11.254868465, 1.4652491725))
                Line((1.5107989252, -1.052896862), (4.1559347211, -11.2883585004))
                Line((4.1559347211, -11.2883585004), (4.2367197399, -11.6009594498))
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -91.6649882617, 22.0698686971)
            make_face()
            # Profile area: 53.5194888159, perimeter: 104.6085894779
            with BuildLine():
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -104.2083363469, 11.0524970179)
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -104.818307275, 0.6099709282)
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -125.892997277, 21.074690002)
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -126.8883172433, 0.9953199662)
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -131.3897760833, 4.50145884)
                Line((-22.7453872272, -0.9575262043), (-23.4357063214, -1.740821238))
                CenterArc((5.4769490275, 31.0659481771), 43.7290036335, -131.3897760833, 67.9750170502)
                Line((24.5796817703, -7.1058840672), (25.0469351204, -8.0395680975))
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -68.8042888543, 5.3895298212)
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -69.5951195646, 0.7908307103)
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -91.6649882617, 22.0698686971)
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -93.155839329, 1.4908510674)
            make_face()
            # Profile area: 11.4085438461, perimeter: 23.6396738961
            with BuildLine():
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -93.155839329, 1.4908510674)
                Line((4.1559347211, -11.2883585004), (4.2367197399, -11.6009594498))
                Line((1.5107989252, -1.052896862), (4.1559347211, -11.2883585004))
                Line((0.4819250245, -1.318787281), (1.5107989252, -1.052896862))
                Line((0.4819250245, -1.318787281), (3.1270608204, -11.5542489194))
            make_face()
            # Profile area: 9.4984946613, perimeter: 44.3742283602
            with BuildLine():
                Line((-5, -3.0737598875), (-5, -10.3132339584))
                Line((-20.1449850993, -3.0737598875), (-5, -3.0737598875))
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -126.8883172433, 0.9953199662)
                Line((-19.5480873105, -3.513680673), (-5.4399207856, -3.513680673))
                Line((-5.4399207856, -3.513680673), (-5.4399207856, -10.1993535741))
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -104.818307275, 0.6099709282)
            make_face()
            # Profile area: 0.7201810333, perimeter: 3.6763324419
            with BuildLine():
                Line((20.7625716064, -7.5528417712), (20.9098892032, -8.7313825458))
                Line((20.1945357937, -7.6238462478), (20.7625716064, -7.5528417712))
                Line((20.1945357937, -7.6238462478), (20.3418533905, -8.8023870224))
                Line((20.3418533905, -8.8023870224), (20.3591299638, -8.9405996084))
                CenterArc((5.4769490275, 31.0659481771), 42.6849291335, -69.5951195646, 0.7908307103)
            make_face()
            # Profile area: 26.0795766853, perimeter: 93.6553802285
            with BuildLine():
                Line((0.4819250245, -1.318787281), (1.5107989252, -1.052896862))
                Line((1.5107989252, -1.052896862), (11.254868465, 1.4652491725))
                Line((11.254868465, 1.4652491725), (18.5571183646, -7.8285234265))
                Line((18.5571183646, -7.8285234265), (20.1945357937, -7.6238462478))
                Line((20.1945357937, -7.6238462478), (20.7625716064, -7.5528417712))
                Line((20.7625716064, -7.5528417712), (20.937304, -7.531000222))
                Line((20.937304, -7.531000222), (20.937304, -7.6702523265))
                Line((20.937304, -7.6702523265), (21.4925578671, -7.6702523265))
                Line((21.4925578671, -6.8945184654), (21.4925578671, -7.6702523265))
                Line((18.803017044, -7.2307110683), (21.4925578671, -6.8945184654))
                Line((11.4696836904, 2.1026222903), (18.803017044, -7.2307110683))
                Line((-0.1389395565, -0.8973777069), (11.4696836904, 2.1026222903))
                Line((-10.3420752573, 12.1375505323), (-0.1389395565, -0.8973777069))
                CenterArc((-10.5177293633, 12.1574411091), 0.1767766953, -6.4604930967, 96.4604930968)
                Line((-13.0303163192, 12.3342178044), (-10.5177293633, 12.3342178044))
                CenterArc((-13.0303163192, 12.0528698044), 0.281348, 89.9999999999, 180)
                Line((-13.0303163192, 11.7715218044), (-10.7700703628, 11.7715218044))
                Line((-0.3551276585, -1.5351056155), (-10.7700703628, 11.7715218044))
                Line((-0.3551276585, -1.5351056155), (0.4819250245, -1.318787281))
            make_face()
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.9182466296, perimeter: 24.7647112105
            with BuildLine():
                CenterArc((-5, 2), 1.2404772104, 180, 90)
                Line((-5, 0.7595227896), (-2.1511066555, 0.7595227896))
                Line((-2.1511066555, 0.7595227896), (-2.3393253746, 1))
                Line((-2.3393253746, 1), (-5, 1))
                CenterArc((-5, 2), 1, 180, 90)
                CenterArc((-7.5452056137, 2), 1.5452056137, 0, 45.7338710024)
                Line((-6.4666643424, 3.1065302141), (-10.5514247051, 7.0879692911))
                CenterArc((-10.9446876739, 6.6845008576), 0.5634203932, 45.7338710024, 88.5322579951)
                CenterArc((-11.2540250493, 7.0018657665), 0.1202386052, 134.2661289976, 180)
                CenterArc((-10.9446876739, 6.6845008576), 0.3229431828, 45.7338710024, 88.5322579951)
                Line((-6.6345155293, 2.9343231649), (-10.7192758919, 6.9157622419))
                CenterArc((-7.5452056137, 2), 1.3047284033, 0, 45.7338710024)
            make_face()
            # Profile area: 1.2731774713, perimeter: 5.2291336895
            with BuildLine():
                Line((22.0822770739, -9.3875910902), (23, -11))
                CenterArc((23.2686013923, -10.8471221201), 0.3090604377, -150.3530844186, 179.9999991462)
                Line((22.6565988131, -9.1470521092), (23.5372027869, -10.6942442441))
                CenterArc((5.4769490275, 31.0659481771), 43.7290036335, -67.6828800084, 0.8158439902)
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5)
    return part.part


def model_119903_14d53edb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36.0380020132, perimeter: 102.9657200377
            with BuildLine():
                CenterArc((-7.5, 2.5), 2.6724579116, 27.5120026239, 180)
                CenterArc((0, 6.40625), 11.1287448664, -152.4879973761, 124.9759947523)
                CenterArc((7.5, 2.5), 2.6724579116, -27.5120026239, 180)
                CenterArc((0, 6.40625), 5.7838290433, -152.4879973761, 124.9759947523)
            make_face()
            with BuildLine():
                CenterArc((0, 6.40625), 6.4838290433, -152.4879973761, 124.9759947523)
                CenterArc((7.5, 2.5), 1.9724579116, -27.5120026239, 180)
                CenterArc((0, 6.40625), 10.4287448664, -152.4879973761, 124.9759947523)
                CenterArc((-7.5, 2.5), 1.9724579116, 27.5120026239, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2761574138, perimeter: 1.8752413689
            with BuildLine():
                CenterArc((8.5, 4.5), 0.3, -89.9436941487, 306.7572859432)
                CenterArc((7.5, 2.5), 1.9724579116, 59.5270757741, 7.8157460977)
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-8.5959199666, 4.6041663358)):
                Circle(0.3)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((5.1136601795, -3.139020816)):
                Circle(0.3)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-5.2146514348, -2.969963352)):
                Circle(0.3)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)
    return part.part


def model_119916_18e9ecf9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 26 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0044462684, perimeter: 6.9478806732
            with BuildLine():
                Line((8.2306804003, -0.5), (8.2306804003, 2.2432599363))
                Line((8.2306804003, 2.2432599363), (7.5, 2.2432599363))
                Line((7.5, 2.2432599363), (7.5, 0))
                Line((7.5, 0), (7.5, -0.5))
                Line((7.5, -0.5), (8.2306804003, -0.5))
            make_face()
            # Profile area: 7, perimeter: 29
            with BuildLine():
                Line((7.5, 0), (7.5, -0.5))
                Line((-4.864086773, 0), (7.5, 0))
                Line((-6.5, 0), (-4.864086773, 0))
                Line((-6.5, -0.5), (-6.5, 0))
                Line((-6.5, -0.5), (-5.5, -0.5))
                Line((6.5, -0.5), (-5.5, -0.5))
                Line((7.5, -0.5), (6.5, -0.5))
            make_face()
            # Profile area: 11.0533302809, perimeter: 29.2376535198
            with BuildLine():
                Line((6.5, -2.2001329697), (-5.5, -2.2001329697))
                Line((-5.5, -2.2001329697), (-5.5, -3))
                Line((-5.5, -3), (8.3189597296, -3))
                Line((8.3189597296, -3), (8.3189597296, -2.2001329697))
                Line((8.3189597296, -2.2001329697), (6.5, -2.2001329697))
            make_face()
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((-5.5, -2.2001329697), (-5.5, -3))
                Line((-5.5, -0.5), (-5.5, -2.2001329697))
                Line((-6.5, -0.5), (-5.5, -0.5))
                Line((-6.5, -3), (-6.5, -0.5))
                Line((-5.5, -3), (-6.5, -3))
            make_face()
            # Profile area: 7.9023453339, perimeter: 30.8977652404
            with BuildLine():
                Line((7.2007548923, 2.2432599363), (-4.864086773, 2.2432599363))
                Line((7.5, 2.2432599363), (7.2007548923, 2.2432599363))
                Line((8.2306804003, 2.2432599363), (7.5, 2.2432599363))
                Line((8.2306804003, 2.7729359119), (8.2306804003, 2.2432599363))
                Line((-6.6885262444, 2.7729359119), (8.2306804003, 2.7729359119))
                Line((-6.6885262444, 2.2432599363), (-6.6885262444, 2.7729359119))
                Line((-4.864086773, 2.2432599363), (-6.6885262444, 2.2432599363))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7002058322, perimeter: 5.1107951257
            with BuildLine():
                Line((-3, 2.2432599363), (-3.3121376265, 2.2432599363))
                Line((-3.3121376265, 0), (-3.3121376265, 2.2432599363))
                Line((-3, 0), (-3.3121376265, 0))
                Line((-3, 2.2432599363), (-3, 0))
            make_face()
            # Profile area: 0.5450915326, perimeter: 4.0414999396
            with BuildLine():
                Line((5.1793829999, -0.5), (5.1793829999, -2.2001329697))
                Line((5.5, -2.2001329697), (5.1793829999, -2.2001329697))
                Line((5.5, -2.2001329697), (5.5, -0.5))
                Line((5.1793829999, -0.5), (5.5, -0.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch10 -> Extrude7 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24, perimeter: 22
            with BuildLine():
                Line((4, -7), (4, -10))
                Line((4, -10), (12, -10))
                Line((12, -10), (12, -7))
                Line((12, -7), (4, -7))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_121027_9ae27724_0000():
    """Model: scrue"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3067961576, perimeter: 1.9634954085
            Circle(0.3125)
        # OneSide extrude, distance=0.72
        extrude(amount=0.72)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.72, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
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
        with BuildSketch(Plane(origin=(0, 8.72, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
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

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1809557368, perimeter: 1.5079644737
            with Locations((0, 9.4)):
                Circle(0.24)
        # Symmetric extrude, full_length=True, total=2
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_121174_1345e289_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.1303960939, perimeter: 12.3464591286
            Circle(1.965)
        # OneSide extrude, distance=2.15
        extrude(amount=2.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.4754082958, perimeter: 10.320131867
            Circle(1.6425)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0360776222, perimeter: 21.2528743015
            with BuildLine():
                CenterArc((0, 0), 1.74, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 8.4754082958, perimeter: 10.320131867
            Circle(1.6425)
        # OneSide extrude, distance=0.375
        extrude(amount=0.375, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.725, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.3782070615, perimeter: 9.6289814833
            Circle(1.5325)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


def model_121869_67b34d49_0000():
    """Model: Slide Switch v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.323, perimeter: 2.46
            with BuildLine():
                Line((-0.425, 0.19), (0.425, 0.19))
                Line((-0.425, -0.19), (-0.425, 0.19))
                Line((0.425, -0.19), (-0.425, -0.19))
                Line((0.425, 0.19), (0.425, -0.19))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.35), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0684, perimeter: 1.12
            with BuildLine():
                Line((0.19, 0.09), (0.19, -0.09))
                Line((-0.19, 0.09), (0.19, 0.09))
                Line((-0.19, -0.09), (-0.19, 0.09))
                Line((0.1602882632, -0.09), (-0.19, -0.09))
                Line((0.19, -0.09), (0.1602882632, -0.09))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.33), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0225, perimeter: 0.6
            with BuildLine():
                Line((0.075, -0.075), (-0.075, -0.075))
                Line((0.075, 0.075), (0.075, -0.075))
                Line((-0.075, 0.075), (0.075, 0.075))
                Line((-0.075, -0.075), (-0.075, 0.075))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0015, perimeter: 0.16
            with BuildLine():
                Line((-0.235, -0.025), (-0.265, -0.025))
                Line((-0.235, 0.025), (-0.235, -0.025))
                Line((-0.265, 0.025), (-0.235, 0.025))
                Line((-0.265, -0.025), (-0.265, 0.025))
            make_face()
            # Profile area: 0.0015, perimeter: 0.16
            with BuildLine():
                Line((-0.015, -0.025), (-0.015, 0.025))
                Line((0.015, -0.025), (-0.015, -0.025))
                Line((0.015, 0.025), (0.015, -0.025))
                Line((-0.015, 0.025), (0.015, 0.025))
            make_face()
            # Profile area: 0.0015, perimeter: 0.16
            with BuildLine():
                Line((0.235, 0.025), (0.265, 0.025))
                Line((0.235, -0.025), (0.235, 0.025))
                Line((0.265, -0.025), (0.235, -0.025))
                Line((0.265, 0.025), (0.265, -0.025))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_122515_758d8b70_0007():
    """Model: Horizontal Beam v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.2853096491, perimeter: 91.4265482457
            with BuildLine():
                CenterArc((-3.4, -7.4), 0.6, 180, 90)
                Line((-3.4, -8), (3.4, -8))
                CenterArc((3.4, -7.4), 0.6, -90, 90)
                Line((4, -7.4), (4, 7.4))
                CenterArc((3.4, 7.4), 0.6, 0, 90)
                Line((3.4, 8), (-3.4, 8))
                CenterArc((-3.4, 7.4), 0.6, 90, 90)
                Line((-4, 7.4), (-4, -7.4))
            make_face()
            with BuildLine():
                Line((3.4, 7.6), (-3.4, 7.6))
                CenterArc((3.4, 7.4), 0.2, 0, 90)
                Line((3.6, -7.4), (3.6, 7.4))
                CenterArc((3.4, -7.4), 0.2, -90, 90)
                Line((-3.4, -7.6), (3.4, -7.6))
                CenterArc((-3.4, -7.4), 0.2, 180, 90)
                Line((-3.6, 7.4), (-3.6, -7.4))
                CenterArc((-3.4, 7.4), 0.2, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=250
        extrude(amount=125, both=True)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -125), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 81.3090266447, perimeter: 106.9699111843
            with BuildLine():
                Line((5.5, -9.5), (5.5, 9.5))
                Line((5.5, 9.5), (-5.5, 9.5))
                Line((-5.5, 9.5), (-5.5, -9.5))
                Line((-5.5, -9.5), (5.5, -9.5))
            make_face()
            with BuildLine():
                CenterArc((-3.4, -7.4), 0.6, 180, 90)
                Line((-4, 7.4), (-4, -7.4))
                CenterArc((-3.4, 7.4), 0.6, 90, 90)
                Line((3.4, 8), (-3.4, 8))
                CenterArc((3.4, 7.4), 0.6, 0, 90)
                Line((4, -7.4), (4, 7.4))
                CenterArc((3.4, -7.4), 0.6, -90, 90)
                Line((-3.4, -8), (3.4, -8))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 18.2853096491, perimeter: 91.4265482457
            with BuildLine():
                Line((-3.4, -8), (3.4, -8))
                CenterArc((3.4, -7.4), 0.6, -90, 90)
                Line((4, -7.4), (4, 7.4))
                CenterArc((3.4, 7.4), 0.6, 0, 90)
                Line((3.4, 8), (-3.4, 8))
                CenterArc((-3.4, 7.4), 0.6, 90, 90)
                Line((-4, 7.4), (-4, -7.4))
                CenterArc((-3.4, -7.4), 0.6, 180, 90)
            make_face()
            with BuildLine():
                Line((-3.6, -7.4), (-3.6, 7.4))
                CenterArc((-3.4, 7.4), 0.2, 90, 90)
                Line((-3.4, 7.6), (3.4, 7.6))
                CenterArc((3.4, 7.4), 0.2, 0, 90)
                Line((3.6, 7.4), (3.6, -7.4))
                CenterArc((3.4, -7.4), 0.2, -90, 90)
                Line((3.4, -7.6), (-3.4, -7.6))
                CenterArc((-3.4, -7.4), 0.2, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 109.4056637061, perimeter: 44.4566370614
            with BuildLine():
                CenterArc((-3.4, -7.4), 0.2, 180, 90)
                Line((3.4, -7.6), (-3.4, -7.6))
                CenterArc((3.4, -7.4), 0.2, -90, 90)
                Line((3.6, 7.4), (3.6, -7.4))
                CenterArc((3.4, 7.4), 0.2, 0, 90)
                Line((-3.4, 7.6), (3.4, 7.6))
                CenterArc((-3.4, 7.4), 0.2, 90, 90)
                Line((-3.6, -7.4), (-3.6, 7.4))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 125), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 18.2853096491, perimeter: 91.4265482457
            with BuildLine():
                CenterArc((-3.4, 7.4), 0.6, 90, 90)
                Line((-4, 7.4), (-4, -7.4))
                CenterArc((-3.4, -7.4), 0.6, 180, 90)
                Line((-3.4, -8), (3.4, -8))
                CenterArc((3.4, -7.4), 0.6, -90, 90)
                Line((4, -7.4), (4, 7.4))
                CenterArc((3.4, 7.4), 0.6, 0, 90)
                Line((3.4, 8), (-3.4, 8))
            make_face()
            with BuildLine():
                Line((3.4, -7.6), (-3.4, -7.6))
                CenterArc((-3.4, -7.4), 0.2, 180, 90)
                Line((-3.6, -7.4), (-3.6, 7.4))
                CenterArc((-3.4, 7.4), 0.2, 90, 90)
                Line((-3.4, 7.6), (3.4, 7.6))
                CenterArc((3.4, 7.4), 0.2, 0, 90)
                Line((3.6, 7.4), (3.6, -7.4))
                CenterArc((3.4, -7.4), 0.2, -90, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 109.4056637061, perimeter: 44.4566370614
            with BuildLine():
                CenterArc((3.4, -7.4), 0.2, -90, 90)
                Line((3.6, 7.4), (3.6, -7.4))
                CenterArc((3.4, 7.4), 0.2, 0, 90)
                Line((-3.4, 7.6), (3.4, 7.6))
                CenterArc((-3.4, 7.4), 0.2, 90, 90)
                Line((-3.6, -7.4), (-3.6, 7.4))
                CenterArc((-3.4, -7.4), 0.2, 180, 90)
                Line((3.4, -7.6), (-3.4, -7.6))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 364.4222263936, perimeter: 82.5867228627
            with BuildLine():
                Line((126.2, 8), (126.2, -8))
                Line((126.2, -8), (143, -8))
                CenterArc((143, 0), 8, -90, 180)
                Line((126.2, 8), (143, 8))
            make_face()
            with BuildLine():
                CenterArc((143, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Start offset: 3 (not directly supported, may affect result)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_122515_758d8b70_0010():
    """Model: Junction Body v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1968, perimeter: 178
            with BuildLine():
                Line((20.5, -24), (20.5, 24))
                Line((20.5, 24), (-20.5, 24))
                Line((-20.5, 24), (-20.5, -24))
                Line((-20.5, -24), (20.5, -24))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 61.5, perimeter: 85
            with BuildLine():
                Line((-20.5, 20.5), (20.5, 20.5))
                Line((-20.5, 19), (-20.5, 20.5))
                Line((20.5, 19), (-20.5, 19))
                Line((20.5, 20.5), (20.5, 19))
            make_face()
            # Profile area: 61.5, perimeter: 85
            with BuildLine():
                Line((20.5, -19), (-20.5, -19))
                Line((-20.5, -19), (-20.5, -20.5))
                Line((-20.5, -20.5), (20.5, -20.5))
                Line((20.5, -20.5), (20.5, -19))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11, mode=Mode.ADD)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 24, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.6569, perimeter: 17.6
            with BuildLine():
                Line((0, 17.51), (0, 20.5))
                Line((2.51, 17.51), (0, 17.51))
                Line((2.51, 15.7), (2.51, 17.51))
                Line((4, 15.7), (2.51, 15.7))
                Line((4, 20.5), (4, 15.7))
                Line((0, 20.5), (4, 20.5))
            make_face()
        # OneSide extrude, distance=-48
        extrude(amount=-48, mode=Mode.ADD)
    return part.part


def model_123687_e9e1613b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # outline of phone -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100.7807006922, perimeter: 41.9407075111
            with BuildLine():
                CenterArc((0.8509312861, 14.0784931369), 0.85, 90, 90)
                Line((0.0009312861, 0.8884931369), (0.0009312861, 14.0784931369))
                CenterArc((0.8509312861, 0.8884931369), 0.85, 180, 90)
                Line((5.9609312861, 0.0384931369), (0.8509312861, 0.0384931369))
                CenterArc((5.9609312861, 0.8884931369), 0.85, -90, 90)
                Line((6.8109312861, 10.4284931369), (6.8109312861, 0.8884931369))
                Line((6.8109312861, 14.0784931369), (6.8109312861, 10.4284931369))
                CenterArc((5.9609312861, 14.0784931369), 0.85, 0, 90)
                Line((5.7489855049, 14.9284931369), (5.9609312861, 14.9284931369))
                Line((0.8509312861, 14.9284931369), (5.7489855049, 14.9284931369))
            make_face()
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Camera -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 55 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.9625, perimeter: 5.9699111843
            with BuildLine():
                CenterArc((-3.6809300432, 11.9534954793), 0.3, 180, 90)
                Line((-3.6809300432, 11.6534954793), (-3.1309300432, 11.6534954793))
                CenterArc((-3.1309300432, 11.9534954793), 0.3, -90, 90)
                Line((-2.8309300432, 12.5034954793), (-2.8309300432, 11.9534954793))
                CenterArc((-3.1309300432, 12.5034954793), 0.3, 0, 90)
                Line((-3.6809300432, 12.8034954793), (-3.1309300432, 12.8034954793))
                CenterArc((-3.6809300432, 12.5034954793), 0.3, 90, 90)
                Line((-3.9809300432, 11.9534954793), (-3.9809300432, 12.5034954793))
            make_face()
            with BuildLine():
                CenterArc((-3.4059312861, 12.2284954793), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1175, perimeter: 8.3699111843
            with BuildLine():
                CenterArc((-3.1059312861, 11.9284954793), 0.3, -90, 90)
                Line((-2.8059312861, 11.9284954793), (-2.8059312861, 12.5284954793))
                CenterArc((-3.1059312861, 12.5284954793), 0.3, 0, 90)
                Line((-3.1059312861, 12.8284954793), (-3.7059312861, 12.8284954793))
                CenterArc((-3.7059312861, 12.5284954793), 0.3, 90, 90)
                Line((-4.0059312861, 12.5284954793), (-4.0059312861, 11.9284954793))
                CenterArc((-3.7059312861, 11.9284954793), 0.3, 180, 90)
                Line((-3.7059312861, 11.6284954793), (-3.1059312861, 11.6284954793))
            make_face()
            with BuildLine():
                Line((-3.9809300432, 11.9534954793), (-3.9809300432, 12.5034954793))
                CenterArc((-3.6809300432, 12.5034954793), 0.3, 90, 90)
                Line((-3.6809300432, 12.8034954793), (-3.1309300432, 12.8034954793))
                CenterArc((-3.1309300432, 12.5034954793), 0.3, 0, 90)
                Line((-2.8309300432, 12.5034954793), (-2.8309300432, 11.9534954793))
                CenterArc((-3.1309300432, 11.9534954793), 0.3, -90, 90)
                Line((-3.6809300432, 11.6534954793), (-3.1309300432, 11.6534954793))
                CenterArc((-3.6809300432, 11.9534954793), 0.3, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)

        # Camera -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 55 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.9625, perimeter: 5.9699111843
            with BuildLine():
                CenterArc((-3.6809300432, 11.9534954793), 0.3, 180, 90)
                Line((-3.6809300432, 11.6534954793), (-3.1309300432, 11.6534954793))
                CenterArc((-3.1309300432, 11.9534954793), 0.3, -90, 90)
                Line((-2.8309300432, 12.5034954793), (-2.8309300432, 11.9534954793))
                CenterArc((-3.1309300432, 12.5034954793), 0.3, 0, 90)
                Line((-3.6809300432, 12.8034954793), (-3.1309300432, 12.8034954793))
                CenterArc((-3.6809300432, 12.5034954793), 0.3, 90, 90)
                Line((-3.9809300432, 11.9534954793), (-3.9809300432, 12.5034954793))
            make_face()
            with BuildLine():
                CenterArc((-3.4059312861, 12.2284954793), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.SUBTRACT)

        # Bottom -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((1.9650001013, 0.0749989535)):
                Circle(0.175)
            # Profile area: 0.0125660706, perimeter: 0.4138594969
            with Locations((5.1249998751, 0)):
                Ellipse(0.08, 0.0499988064, rotation=-89.9998379431)
            # Profile area: 0.0125660706, perimeter: 0.4138594969
            with Locations((5.2799998751, 0)):
                Ellipse(0.08, 0.0499988064, rotation=-89.9998379431)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((4.7550001013, -0.0550010465)):
                Circle(0.025)
            # Profile area: 0.0125660706, perimeter: 0.4138594969
            with Locations((5.4349998751, 0)):
                Ellipse(0.08, 0.0499988064, rotation=-89.9998379431)
            # Profile area: 0.0125660706, perimeter: 0.4138594969
            with Locations((5.5899998751, 0)):
                Ellipse(0.08, 0.0499988064, rotation=-89.9998379431)
            # Profile area: 0.2050929158, perimeter: 3.5168140899
            with BuildLine():
                CenterArc((3.0950001013, 0.0749989535), 0.13, 89.9999999995, 180)
                Line((3.7950001013, -0.0550010465), (3.0950001013, -0.0550010465))
                CenterArc((3.7950001013, 0.0749989535), 0.13, -89.9999999999, 180)
                Line((3.0950001013, 0.2049989535), (3.7950001013, 0.2049989535))
            make_face()
            with BuildLine():
                Line((3.1450001013, 0.0749989535), (3.1450001013, 0.0999989535))
                Line((3.1450001013, 0.0999989535), (3.7450001013, 0.0999989535))
                Line((3.7450001013, 0.0749989535), (3.7450001013, 0.0999989535))
                Line((3.7450001013, 0.0499989535), (3.7450001013, 0.0749989535))
                Line((3.1450001013, 0.0499989535), (3.7450001013, 0.0499989535))
                Line((3.1450001013, 0.0749989535), (3.1450001013, 0.0499989535))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.03, perimeter: 1.3
            with BuildLine():
                Line((3.1450001013, 0.0749989535), (3.1450001013, 0.0499989535))
                Line((3.1450001013, 0.0499989535), (3.7450001013, 0.0499989535))
                Line((3.7450001013, 0.0499989535), (3.7450001013, 0.0749989535))
                Line((3.7450001013, 0.0749989535), (3.7450001013, 0.0999989535))
                Line((3.1450001013, 0.0999989535), (3.7450001013, 0.0999989535))
                Line((3.1450001013, 0.0749989535), (3.1450001013, 0.0999989535))
            make_face()
        # OneSide extrude, distance=0.2843
        extrude(amount=0.2843, mode=Mode.SUBTRACT)

        # Bottom -> Extrude8 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2050929158, perimeter: 3.5168140899
            with BuildLine():
                CenterArc((3.0950001013, 0.0749989535), 0.13, 89.9999999995, 180)
                Line((3.7950001013, -0.0550010465), (3.0950001013, -0.0550010465))
                CenterArc((3.7950001013, 0.0749989535), 0.13, -89.9999999999, 180)
                Line((3.0950001013, 0.2049989535), (3.7950001013, 0.2049989535))
            make_face()
            with BuildLine():
                Line((3.1450001013, 0.0749989535), (3.1450001013, 0.0999989535))
                Line((3.1450001013, 0.0999989535), (3.7450001013, 0.0999989535))
                Line((3.7450001013, 0.0749989535), (3.7450001013, 0.0999989535))
                Line((3.7450001013, 0.0499989535), (3.7450001013, 0.0749989535))
                Line((3.1450001013, 0.0499989535), (3.7450001013, 0.0499989535))
                Line((3.1450001013, 0.0749989535), (3.1450001013, 0.0499989535))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4843
        extrude(amount=0.4843, mode=Mode.SUBTRACT)

        # buttons on left -> Extrude10 (Join)
        # Sketch on YZ construction plane
        # Sketch has 34 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2594097336, perimeter: 4.3469911184
            with BuildLine():
                Line((0.0001969283, 12.4271345914), (-0.0025023768, 12.4271345914))
                CenterArc((-0.0025023768, 12.3671345914), 0.06, 90, 90)
                Line((-0.0625023768, 12.3671345914), (-0.0625023768, 10.3871345914))
                CenterArc((-0.0025023768, 10.3871345914), 0.06, -180, 90)
                Line((-0.0025023768, 10.3271345914), (0.0024976232, 10.3271345914))
                CenterArc((0.0024976232, 10.3871345914), 0.06, -90, 90)
                Line((0.0624976232, 12.3671345914), (0.0624976232, 10.3871345914))
                CenterArc((0.0024976232, 12.3671345914), 0.06, 0, 90)
                Line((0.0001969283, 12.4271345914), (0.0024976232, 12.4271345914))
            make_face()
            # Profile area: 0.1269780149, perimeter: 2.19547159
            with BuildLine():
                Line((-0.0010202644, 9.4271345914), (-0.0035202457, 9.4271442649))
                CenterArc((-0.0037524093, 9.3671447141), 0.06, 89.7782994966, 90.000000005)
                Line((-0.0637519602, 9.3673768777), (-0.0672420619, 8.4654073372))
                CenterArc((-0.0072425111, 8.4651751736), 0.06, 179.7782995058, 90.2548129851)
                Line((-0.0072078357, 8.4051751836), (0.0020702776, 8.4051805456))
                CenterArc((0.0020356022, 8.4651805356), 0.06, -89.9668875091, 89.9999999954)
                Line((0.0615143301, 9.3671743502), (0.0620355922, 8.4652152109))
                CenterArc((0.0015143402, 9.3671396749), 0.06, 0.0331124809, 90.0846668967)
                Line((-0.0010202644, 9.4271345914), (0.001391002, 9.4271395481))
            make_face()
        # Start offset: 0.01 (not directly supported, may affect result)
        # OneSide extrude, distance=-0.051
        extrude(amount=-0.051, mode=Mode.ADD)
    return part.part


def model_123773_63bda323_0000():
    """Model: socket"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5566, perimeter: 3.34
            with BuildLine():
                Line((-0.605, 0.23), (-0.605, -0.23))
                Line((-0.605, -0.23), (0.605, -0.23))
                Line((0.605, -0.23), (0.605, 0.23))
                Line((0.605, 0.23), (-0.605, 0.23))
            make_face()
        # OneSide extrude, distance=1.42
        extrude(amount=1.42)

        # Sketch2 -> 押し出し2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.23), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.018, perimeter: 0.54
            with BuildLine():
                Line((0.225, -0.15), (0.375, -0.15))
                Line((0.225, -0.27), (0.225, -0.15))
                Line((0.375, -0.27), (0.225, -0.27))
                Line((0.375, -0.15), (0.375, -0.27))
            make_face()
            # Profile area: 0.018, perimeter: 0.54
            with BuildLine():
                Line((-0.225, -0.27), (-0.225, -0.15))
                Line((-0.225, -0.15), (-0.375, -0.15))
                Line((-0.375, -0.15), (-0.375, -0.27))
                Line((-0.375, -0.27), (-0.225, -0.27))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch4 -> 押し出し3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.605, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0072, perimeter: 0.36
            with BuildLine():
                Line((0.28, -0.03), (0.16, -0.03))
                Line((0.28, 0.03), (0.28, -0.03))
                Line((0.16, 0.03), (0.28, 0.03))
                Line((0.16, -0.03), (0.16, 0.03))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch5 -> 押し出し4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.23), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.05, perimeter: 0.9
            with BuildLine():
                Line((-0.175, -0.9), (-0.175, -0.7))
                Line((-0.175, -0.7), (-0.425, -0.7))
                Line((-0.425, -0.7), (-0.425, -0.9))
                Line((-0.425, -0.9), (-0.175, -0.9))
            make_face()
            # Profile area: 0.05, perimeter: 0.9
            with BuildLine():
                Line((0.175, -0.7), (0.425, -0.7))
                Line((0.175, -0.9), (0.175, -0.7))
                Line((0.425, -0.9), (0.175, -0.9))
                Line((0.425, -0.7), (0.425, -0.9))
            make_face()
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)
    return part.part


def model_125742_bdbe71f2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 29.9947169677, perimeter: 36.8229349555
            with BuildLine():
                Line((7.9976107172, 1), (7.9976107172, 0.9994954061))
                Line((7.9976107172, 0.9994954061), (6.9981153111, 0))
                Line((6.9981153111, 0), (9.9976107172, 0))
                Line((9.9976107172, 0), (9.9976107172, 2))
                Line((9.9976107172, 2), (3, 2))
                Line((3, 6), (3, 2))
                Line((0, 6), (3, 6))
                Line((0, 0), (0, 6))
                Line((0, 0), (5.9976107172, 0))
                Line((4.9976107172, 1), (5.9976107172, 0))
                Line((4.9976107172, 1), (7.9976107172, 1))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5342917353, perimeter: 7.7123889804
            with BuildLine():
                Line((0, 1), (0, 4))
                CenterArc((0, 2.5), 1.5, -90, 180)
            make_face()
            # Profile area: 3.5342917353, perimeter: 7.7123889804
            with BuildLine():
                CenterArc((0, 2.5), 1.5, 90, 180)
                Line((0, 1), (0, 4))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.9976107172, perimeter: 15.9952214344
            with BuildLine():
                Line((-3, 2), (-9.9976107172, 2))
                Line((-3, 2), (-3, 3))
                Line((-3, 3), (-9.9976107172, 3))
                Line((-9.9976107172, 2), (-9.9976107172, 3))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.9952214344, perimeter: 19.0577940742
            with BuildLine():
                Line((9.9976107172, 6), (3, 6))
                Line((3, 6), (9.9976107172, 2))
                Line((9.9976107172, 2), (9.9976107172, 6))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_125814_188a264c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.25, perimeter: 14
            with BuildLine():
                Line((0.25, 1.75), (1.75, 1.75))
                Line((0.25, -3.75), (0.25, 1.75))
                Line((1.75, -3.75), (0.25, -3.75))
                Line((1.75, 1.75), (1.75, -3.75))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-1.0000000149, 3.01)):
                Circle(0.200000003)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5105088025, perimeter: 4.0840704684
            with BuildLine():
                CenterArc((-1.0000000149, 3.01), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.0000000149, 3.01), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_126912_e0373bb3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.7095988373, perimeter: 25.3999996185
            with BuildLine():
                Line((0, 5.0799999237), (0, 0))
                Line((0, 0), (7.6199998856, 0))
                Line((7.6199998856, 0), (7.6199998856, 5.0799999237))
                Line((7.6199998856, 5.0799999237), (0, 5.0799999237))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((1.2699999809, 1.2699999809)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((3.8099999428, 1.2699999809)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((6.3531356197, 1.27)):
                Circle(0.635)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-3.8099999428, 1.2699999809)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-1.2699999809, 1.2699999809)):
                Circle(0.635)
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((1.2699999809, -3.8099999428)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((3.8099999428, -3.8099999428)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((6.3531356197, -3.8099999428)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((6.3531356197, -1.2699999809)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((3.8099999428, -1.2699999809)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((1.2699999809, -1.2699999809)):
                Circle(0.635)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


def model_127480_74b7071f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.4584319618, perimeter: 15.5538731699
            with BuildLine():
                Line((0.4945310662, 0), (1.9887742938, 0))
                Line((1.9887742938, 0), (2.49165268, 0.5028783862))
                Line((2.49165268, 0.5028783862), (2.49165268, 2.4956374016))
                Line((2.49165268, 2.4956374016), (1.99165268, 2.4956374016))
                Line((1.99165268, 2.4956374016), (1.99165268, 4.0007195965))
                Line((1.99165268, 4.0007195965), (0.49165268, 4.0007195965))
                Line((0.49165268, 2.4956374016), (0.49165268, 4.0007195965))
                Line((-0.00834732, 2.4956374016), (0.49165268, 2.4956374016))
                Line((-0.00834732, 2.4956374016), (-0.00834732, 0.5028783862))
                Line((0.4945310662, 0), (-0.00834732, 0.5028783862))
            make_face()
            with BuildLine():
                CenterArc((1.24165268, 0.8000000119), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.0007195965, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-1.24165268, 0.75)):
                Circle(0.5)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.49165268, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((3.5000000522, 0.7000000104)):
                Circle(0.1)
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.49165268, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.8000000119, 0.8000000119)):
                Circle(0.15)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


def model_127543_95d04a2e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.964943787, perimeter: 44.8987164156
            with BuildLine():
                Line((0, 0), (3.175, 0))
                Line((3.175, 0), (3.175, 0.9525))
                Line((3.175, 0.9525), (1.905, 0.9525))
                Line((1.905, 0.9525), (0.9163410437, 12.9348670437))
                CenterArc((0, 14.605), 1.905, -61.2480295113, 151.2480295113)
                CenterArc((0, 14.605), 1.905, 90, 151.2480295113)
                Line((-1.905, 0.9525), (-0.9163410437, 12.9348670437))
                Line((-3.175, 0.9525), (-1.905, 0.9525))
                Line((-3.175, 0), (-3.175, 0.9525))
                Line((0, 0), (-3.175, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.048375, perimeter: 14.605
            with BuildLine():
                Line((-1.905, 0.9525), (1.905, 0.9525))
                Line((-1.905, 0.9525), (-3.175, 0.9525))
                Line((-3.175, 0.9525), (-3.175, 0))
                Line((-3.175, 0), (3.175, 0))
                Line((3.175, 0), (3.175, 0.9525))
                Line((3.175, 0.9525), (1.905, 0.9525))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((2.2838785583, 2.9254070018)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-2.2838785583, 2.9254070018)):
                Circle(0.3175)
        # OneSide extrude, distance=-3.302
        extrude(amount=-3.302, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 17.7319814503, perimeter: 30.5940394059
            with BuildLine():
                Line((1.0264393546, 11.6004955065), (0.9163410437, 12.9348670437))
                CenterArc((0, 14.605), 3.175, -71.1381146606, 322.2762293213)
                Line((-0.9163410437, 12.9348670437), (-1.0264393546, 11.6004955065))
                CenterArc((0, 14.605), 1.905, -61.2480295113, 302.4960590226)
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 14.605)):
                Circle(0.635)
        # OneSide extrude, distance=-2.286
        extrude(amount=-2.286, mode=Mode.SUBTRACT)
    return part.part


def model_128043_96b40cb2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0803103873, perimeter: 14.1909290668
            with BuildLine():
                Line((0, 0), (1.0913921811, 0))
                Line((1.0913921958, 1.3830755221), (1.0913921811, 0))
                CenterArc((0.0913921809, 1.3830755221), 1.0000000149, 0, 180)
                Line((-0.908607834, 0), (-0.908607834, 1.3830755221))
                Line((0, 0), (-0.908607834, 0))
            make_face()
            with BuildLine():
                CenterArc((0.6217222668, 0.8527454362), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.438937905, 0.8527454362), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.438937905, 1.9134056079), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6217222668, 1.9134056079), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0913921809, 1.3830755221), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.4
        extrude(amount=4.4)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.908607834, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.8399999982, perimeter: 6.1999999881
            with BuildLine():
                Line((-0.3, 3.6), (-0.3, 0.8))
                Line((-0.3, 0.8), (0, 0.8000000119))
                Line((0, 3.6), (0, 0.8000000119))
                Line((0, 3.6), (-0.3, 3.6))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.0913921735, 2.2)):
                Circle(0.15)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.0913921735, 4.025)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.0913921735, 0.375)):
                Circle(0.15)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


def model_128996_24601566_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-4.6
        extrude(amount=-4.6, mode=Mode.SUBTRACT)
    return part.part


def model_128996_36e0e614_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.2, perimeter: 20.8
            with BuildLine():
                Line((0, 0), (4, 0))
                Line((4, 2.4), (4, 0))
                Line((-4, 2.4), (4, 2.4))
                Line((-4, 0), (-4, 2.4))
                Line((-0.5, 0), (-4, 0))
                Line((0, 0), (-0.5, 0))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8073010173, perimeter: 16.3415927416
            with BuildLine():
                Line((-2.3, -1.2), (-2.3, -1.5000000224))
                Line((-2.3, -1.5000000224), (-2.3000000267, -2.2))
                Line((-2.3000000267, -2.2), (2.3, -2.2000000328))
                Line((2.3, -1.2), (2.3, -2.2000000328))
                Line((2.3, -1.2), (2.3, -0.2))
                Line((-2.3000000286, -0.2), (2.3, -0.2))
                Line((-2.3, -1.2), (-2.3000000286, -0.2))
            make_face()
            with BuildLine():
                CenterArc((-1.8, -1.2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.8, -1.2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.9
        extrude(amount=2.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.4176436849, perimeter: 4.8845130209
            with BuildLine():
                Line((0.9500000143, 4.8), (-0.9499999857, 4.8))
                CenterArc((0.0000000143, 4.8), 0.95, 180, 180)
            make_face()
            # Profile area: 1.4176436849, perimeter: 4.8845130209
            with BuildLine():
                CenterArc((0.0000000143, 4.8), 0.95, 0, 180)
                Line((0.9500000143, 4.8), (-0.9499999857, 4.8))
            make_face()
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((3.2, -1.2)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-3.2, -1.2)):
                Circle(0.4)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_128996_89b8cb8b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3006357817, perimeter: 6.4402649399
            Circle(1.025)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7679476889, perimeter: 15.8650429006
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.3006357817, perimeter: 6.4402649399
            Circle(1.025)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_128996_df00e69f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)
    return part.part


def model_129078_9934147b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude8 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 101.6127, perimeter: 40.64
            with BuildLine():
                Line((44.4500003815, -189.2299973297), (35.5600003815, -189.2299973297))
                Line((44.4500003815, -177.7999973297), (44.4500003815, -189.2299973297))
                Line((35.5600003815, -177.7999973297), (44.4500003815, -177.7999973297))
                Line((35.5600003815, -189.2299973297), (35.5600003815, -177.7999973297))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 101.6127, perimeter: 40.64
            with BuildLine():
                Line((24.1300003815, -189.2299973297), (15.2400003815, -189.2299973297))
                Line((24.1300003815, -177.7999973297), (24.1300003815, -189.2299973297))
                Line((15.2400003815, -177.7999973297), (24.1300003815, -177.7999973297))
                Line((15.2400003815, -189.2299973297), (15.2400003815, -177.7999973297))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 101.6127, perimeter: 40.64
            with BuildLine():
                Line((3.8100003815, -177.7999973297), (3.8100003815, -189.2299973297))
                Line((-5.0799996185, -177.7999973297), (3.8100003815, -177.7999973297))
                Line((-5.0799996185, -189.2299973297), (-5.0799996185, -177.7999973297))
                Line((3.8100003815, -189.2299973297), (-5.0799996185, -189.2299973297))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 101.6127, perimeter: 40.64
            with BuildLine():
                Line((-16.5099996185, -189.2299973297), (-25.3999996185, -189.2299973297))
                Line((-16.5099996185, -177.7999973297), (-16.5099996185, -189.2299973297))
                Line((-25.3999996185, -177.7999973297), (-16.5099996185, -177.7999973297))
                Line((-25.3999996185, -189.2299973297), (-25.3999996185, -177.7999973297))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 677.418, perimeter: 170.18
            with BuildLine():
                Line((118.5728232912, -61.4820566067), (127.4628232912, -61.4820566067))
                Line((118.5728232912, -137.6820566067), (118.5728232912, -61.4820566067))
                Line((127.4628232912, -137.6820566067), (118.5728232912, -137.6820566067))
                Line((127.4628232912, -61.4820566067), (127.4628232912, -137.6820566067))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 677.418, perimeter: 170.18
            with BuildLine():
                Line((81.7428232912, -137.6820566067), (72.8528232912, -137.6820566067))
                Line((81.7428232912, -61.4820566067), (81.7428232912, -137.6820566067))
                Line((72.8528232912, -61.4820566067), (81.7428232912, -61.4820566067))
                Line((72.8528232912, -137.6820566067), (72.8528232912, -61.4820566067))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 677.418, perimeter: 170.18
            with BuildLine():
                Line((27.1328232912, -61.4820566067), (36.0228232912, -61.4820566067))
                Line((27.1328232912, -137.6820566067), (27.1328232912, -61.4820566067))
                Line((36.0228232912, -137.6820566067), (27.1328232912, -137.6820566067))
                Line((36.0228232912, -61.4820566067), (36.0228232912, -137.6820566067))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints, 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 677.418, perimeter: 170.18
            with BuildLine():
                Line((-9.6971767088, -137.6820566067), (-18.5871767088, -137.6820566067))
                Line((-9.6971767088, -61.4820566067), (-9.6971767088, -137.6820566067))
                Line((-18.5871767088, -61.4820566067), (-9.6971767088, -61.4820566067))
                Line((-18.5871767088, -137.6820566067), (-18.5871767088, -61.4820566067))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_129414_61c80644_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 105, perimeter: 76
            with BuildLine():
                Line((0, 0), (35, 0))
                Line((0, -3), (0, 0))
                Line((35, -3), (0, -3))
                Line((35, 0), (35, -3))
            make_face()
            # Profile area: 112, perimeter: 64
            with BuildLine():
                Line((35, 0), (35, -3))
                Line((35, -3), (39, -3))
                Line((39, -3), (39, 25))
                Line((35, 25), (39, 25))
                Line((35, 25), (35, 0))
            make_face()
            # Profile area: 12, perimeter: 14
            with BuildLine():
                Line((35, 25), (39, 25))
                Line((39, 25), (39, 28))
                Line((39, 28), (35, 28))
                Line((35, 28), (35, 25))
            make_face()
            # Profile area: 135, perimeter: 96
            with BuildLine():
                Line((35, 28), (35, 25))
                Line((35, 28), (-10, 28))
                Line((-10, 28), (-10, 25))
                Line((-10, 25), (35, 25))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(39, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 60, perimeter: 46
            with BuildLine():
                Line((6, 20), (6, 0))
                Line((3, 20), (6, 20))
                Line((3, 0), (3, 20))
                Line((6, 0), (3, 0))
            make_face()
        # OneSide extrude, distance=42
        extrude(amount=42, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 40, perimeter: 44
            with BuildLine():
                Line((-79, 20), (-79, 0))
                Line((-81, 20), (-79, 20))
                Line((-81, 0), (-81, 20))
                Line((-79, 0), (-81, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -28), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((0, 10)):
                Circle(1.5)
        # OneSide extrude, distance=-31
        extrude(amount=-31, mode=Mode.SUBTRACT)
    return part.part


def model_129580_45a65025_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663709889, perimeter: 12.5663708016
            Circle(2.0000000298)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-1.7999999598, 0)):
                Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8115781022, perimeter: 3.6231562044
            with BuildLine():
                Line((-0.1287595187, -0.2142918252), (-0.6437975936, -1.0714591259))
                CenterArc((0, 0), 1.25, -121, 62)
                Line((0.1287595187, -0.2142918252), (0.6437975936, -1.0714591259))
                CenterArc((0, 0), 0.25, -121, 62)
            make_face()
            # Profile area: 0.8115781022, perimeter: 3.6231562044
            with BuildLine():
                CenterArc((0, 0), 0.25, 59, 62)
                Line((0.1287595187, 0.2142918252), (0.6437975936, 1.0714591259))
                CenterArc((0, 0), 1.25, 59, 62)
                Line((-0.1287595187, 0.2142918252), (-0.6437975936, 1.0714591259))
            make_face()
            # Profile area: 0.0338157543, perimeter: 0.7705260341
            with BuildLine():
                Line((0, 0), (-0.1287595187, 0.2142918252))
                Line((0, 0), (0.1287595187, 0.2142918252))
                CenterArc((0, 0), 0.25, 59, 62)
            make_face()
            # Profile area: 0.0338157543, perimeter: 0.7705260341
            with BuildLine():
                CenterArc((0, 0), 0.25, -121, 62)
                Line((0, 0), (0.1287595187, -0.2142918252))
                Line((0, 0), (-0.1287595187, -0.2142918252))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.SUBTRACT)
    return part.part


def model_130260_262a2214_0000():
    """Model: Led receptor v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2733971007, perimeter: 1.8535396656
            with Locations((3, 2)):
                Circle(0.295)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3, 2)):
                Circle(0.25)
        # OneSide extrude, distance=0.86
        extrude(amount=0.86, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-3.0999908132, 2)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-2.9028350139, 2)):
                Circle(0.025)
        # OneSide extrude, distance=0.015
        extrude(amount=0.015, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.11, perimeter: 4.5
            with BuildLine():
                Line((2.9750000447, 2.5000000045), (3.0000000447, 2.5000000045))
                Line((2.9500000447, 2.5000000045), (2.9750000447, 2.5000000045))
                Line((2.9500000447, 0.3000000045), (2.9500000447, 2.5000000045))
                Line((3.0000000447, 0.3000000045), (2.9500000447, 0.3000000045))
                Line((3.0000000447, 2.5000000045), (3.0000000447, 0.3000000045))
            make_face()
            # Profile area: 0.12, perimeter: 4.9
            with BuildLine():
                Line((3.1000000462, 2.7000000045), (3.1000000462, 0.3000000045))
                Line((3.1000000462, 0.3000000045), (3.1500000462, 0.3000000045))
                Line((3.1500000462, 0.3000000045), (3.1500000462, 2.7000000045))
                Line((3.1500000462, 2.7000000045), (3.1000000462, 2.7000000045))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


def model_130757_854b49f3_0001():
    """Model: Side Bars"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.7643780541, perimeter: 19.4602750618
            with BuildLine():
                Line((1.7725, -2.8119427191), (1.7725, -2.6330572809))
                Line((1.7725, -4.1975), (1.7725, -2.8119427191))
                Line((2.1505572809, -4.1975), (1.7725, -4.1975))
                Line((2.3294427191, -4.1975), (2.1505572809, -4.1975))
                Line((2.7075, -4.1975), (2.3294427191, -4.1975))
                Line((2.7075, -2.8119427191), (2.7075, -4.1975))
                CenterArc((2.6525, -2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((2.7075, 2.6330572809), (2.7075, -2.6330572809))
                CenterArc((2.6525, 2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((2.7075, 4.1975), (2.7075, 2.8119427191))
                Line((2.3294427191, 4.1975), (2.7075, 4.1975))
                CenterArc((2.24, 4.1425), 0.105, 148.4118644948, 243.1762710104)
                Line((1.7725, 4.1975), (2.1505572809, 4.1975))
                Line((1.7725, 2.8119427191), (1.7725, 4.1975))
                Line((1.7725, 2.6330572809), (1.7725, 2.8119427191))
                Line((1.7725, -2.6330572809), (1.7725, 2.6330572809))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((2.6525, -2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((2.7075, -2.6330572809), (2.7075, -2.8119427191))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((2.6525, 2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((2.7075, 2.8119427191), (2.7075, 2.6330572809))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((2.24, 4.1425), 0.105, 148.4118644948, 243.1762710104)
                Line((2.1505572809, 4.1975), (2.3294427191, 4.1975))
            make_face()
        # OneSide extrude, distance=0.84
        extrude(amount=0.84)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                Line((1.7725, 2.6330572809), (1.7725, 2.8119427191))
                CenterArc((1.7175, 2.7225), 0.105, 58.4118644948, 243.1762710104)
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((1.7175, -2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((1.7725, -2.8119427191), (1.7725, -2.6330572809))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                Line((2.3294427191, -4.1975), (2.1505572809, -4.1975))
                CenterArc((2.24, -4.2525), 0.105, 148.4118644948, 243.1762710104)
            make_face()
        # OneSide extrude, distance=0.465
        extrude(amount=0.465, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((2.6525, -2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((2.7075, -2.6330572809), (2.7075, -2.8119427191))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((2.6525, 2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((2.7075, 2.8119427191), (2.7075, 2.6330572809))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((2.24, 4.1425), 0.105, 148.4118644948, 243.1762710104)
                Line((2.1505572809, 4.1975), (2.3294427191, 4.1975))
            make_face()
        # OneSide extrude, distance=0.465
        extrude(amount=0.465, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.84), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((-2.165, -3.5175), (-2.065, -3.5175))
                Line((-2.165, -3.6175), (-2.165, -3.5175))
                Line((-2.065, -3.6175), (-2.165, -3.6175))
                Line((-2.065, -3.5175), (-2.065, -3.6175))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 57 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.84), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2976, perimeter: 14.96
            with BuildLine():
                Line((-2.55, -3.72), (-2.59, -3.72))
                Line((-2.55, 3.72), (-2.55, -3.72))
                Line((-2.59, 3.72), (-2.55, 3.72))
                Line((-2.59, -3.72), (-2.59, 3.72))
            make_face()
            # Profile area: 0.2976, perimeter: 14.96
            with BuildLine():
                Line((-1.93, 3.72), (-1.89, 3.72))
                Line((-1.93, -3.72), (-1.93, 3.72))
                Line((-1.89, -3.72), (-1.93, -3.72))
                Line((-1.89, 3.72), (-1.89, -3.72))
            make_face()
            # Profile area: 0.0034, perimeter: 0.38
            with BuildLine():
                Line((-2.1031832782, 3.94375), (-2.1031832782, 3.92375))
                Line((-2.1031832782, 3.92375), (-1.9331832782, 3.92375))
                Line((-1.9331832782, 3.92375), (-1.9331832782, 3.94375))
                Line((-1.9331832782, 3.94375), (-2.1031832782, 3.94375))
            make_face()
            # Profile area: 0.0064, perimeter: 0.68
            with BuildLine():
                Line((-2.4518167218, 3.92375), (-2.3768167218, 3.92375))
                Line((-2.3768167218, 3.92375), (-2.3768167218, 3.94375))
                Line((-2.3768167218, 3.94375), (-2.4518167218, 3.94375))
                Line((-2.4518167218, 4.01875), (-2.4518167218, 3.94375))
                Line((-2.4718167218, 4.01875), (-2.4518167218, 4.01875))
                Line((-2.4718167218, 3.94375), (-2.4718167218, 4.01875))
                Line((-2.4718167218, 3.94375), (-2.5468167218, 3.94375))
                Line((-2.5468167218, 3.94375), (-2.5468167218, 3.92375))
                Line((-2.5468167218, 3.92375), (-2.4718167218, 3.92375))
                Line((-2.4718167218, 3.84875), (-2.4718167218, 3.92375))
                Line((-2.4518167218, 3.84875), (-2.4718167218, 3.84875))
                Line((-2.4518167218, 3.92375), (-2.4518167218, 3.84875))
            make_face()
            # Profile area: 0.0064, perimeter: 0.68
            with BuildLine():
                Line((-2.4718167218, -4.01875), (-2.4518167218, -4.01875))
                Line((-2.4518167218, -4.01875), (-2.4518167218, -3.94375))
                Line((-2.3768167218, -3.94375), (-2.4518167218, -3.94375))
                Line((-2.3768167218, -3.92375), (-2.3768167218, -3.94375))
                Line((-2.4518167218, -3.92375), (-2.3768167218, -3.92375))
                Line((-2.4518167218, -3.92375), (-2.4518167218, -3.84875))
                Line((-2.4518167218, -3.84875), (-2.4718167218, -3.84875))
                Line((-2.4718167218, -3.84875), (-2.4718167218, -3.92375))
                Line((-2.5468167218, -3.92375), (-2.4718167218, -3.92375))
                Line((-2.5468167218, -3.94375), (-2.5468167218, -3.92375))
                Line((-2.4718167218, -3.94375), (-2.5468167218, -3.94375))
                Line((-2.4718167218, -3.94375), (-2.4718167218, -4.01875))
            make_face()
            # Profile area: 0.0034, perimeter: 0.38
            with BuildLine():
                Line((-2.1031832782, -3.92375), (-1.9331832782, -3.92375))
                Line((-2.1031832782, -3.94375), (-2.1031832782, -3.92375))
                Line((-1.9331832782, -3.94375), (-2.1031832782, -3.94375))
                Line((-1.9331832782, -3.92375), (-1.9331832782, -3.94375))
            make_face()
        # OneSide extrude, distance=0.001
        extrude(amount=0.001, mode=Mode.ADD)
    return part.part


def model_130757_8bbd9729_0002():
    """Model: Main Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3721, perimeter: 2.44
            with BuildLine():
                Line((-0.305, 0.305), (0.305, 0.305))
                Line((-0.305, -0.305), (-0.305, 0.305))
                Line((0.305, -0.305), (-0.305, -0.305))
                Line((0.305, 0.305), (0.305, -0.305))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 73 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0560965645, perimeter: 1.8696990582
            with BuildLine():
                Line((-0.217, 0.155), (-0.2979999933, 0.155))
                CenterArc((-0.2979999933, 0.153), 0.002, 90, 90)
                Line((-0.2999999933, 0.153), (-0.2999999933, 0.107))
                CenterArc((-0.2979999933, 0.107), 0.002, -180, 90)
                Line((-0.2979999933, 0.105), (0.2979999933, 0.105))
                CenterArc((0.2979999933, 0.107), 0.002, -90, 90)
                Line((0.2999999933, 0.153), (0.2999999933, 0.107))
                CenterArc((0.2979999933, 0.153), 0.002, 0, 90)
                Line((0.217, 0.155), (0.2979999933, 0.155))
                CenterArc((0.217, 0.157), 0.002, -180, 90)
                Line((0.215, 0.2979999933), (0.215, 0.157))
                CenterArc((0.213, 0.2979999933), 0.002, 0, 90)
                Line((0.213, 0.2999999933), (0.127, 0.2999999933))
                CenterArc((0.127, 0.2979999933), 0.002, 90, 90)
                Line((0.125, 0.157), (0.125, 0.2979999933))
                CenterArc((0.123, 0.157), 0.002, -90, 90)
                Line((-0.123, 0.155), (0.123, 0.155))
                CenterArc((-0.123, 0.157), 0.002, -180, 90)
                Line((-0.125, 0.2979999933), (-0.125, 0.157))
                CenterArc((-0.127, 0.2979999933), 0.002, 0, 90)
                Line((-0.127, 0.2999999933), (-0.213, 0.2999999933))
                CenterArc((-0.213, 0.2979999933), 0.002, 90, 90)
                Line((-0.215, 0.2979999933), (-0.215, 0.157))
                CenterArc((-0.217, 0.157), 0.002, -90, 90)
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 73 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.014, perimeter: 0.48
            with BuildLine():
                Line((0.15, 0.07), (0.05, 0.07))
                Line((0.05, 0.07), (0.05, -0.07))
                Line((0.05, -0.07), (0.15, -0.07))
                Line((0.15, 0.07), (0.15, -0.07))
            make_face()
            # Profile area: 0.014, perimeter: 0.48
            with BuildLine():
                Line((-0.05, 0.07), (-0.05, -0.07))
                Line((-0.05, 0.07), (-0.15, 0.07))
                Line((-0.15, 0.07), (-0.15, -0.07))
                Line((-0.15, -0.07), (-0.05, -0.07))
            make_face()
        # OneSide extrude, distance=0.008
        extrude(amount=0.008, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 73 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.014, perimeter: 0.48
            with BuildLine():
                Line((-0.15, 0.07), (-0.15, -0.07))
                Line((-0.15, 0.07), (-0.25, 0.07))
                Line((-0.25, 0.07), (-0.25, -0.07))
                Line((-0.25, -0.07), (-0.15, -0.07))
            make_face()
            # Profile area: 0.014, perimeter: 0.48
            with BuildLine():
                Line((0.15, 0.07), (0.15, -0.07))
                Line((0.15, -0.07), (0.25, -0.07))
                Line((0.25, -0.07), (0.25, 0.07))
                Line((0.25, 0.07), (0.15, 0.07))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 73 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.014, perimeter: 0.48
            with BuildLine():
                Line((0.05, 0.07), (0.05, -0.07))
                Line((0.05, 0.07), (-0.05, 0.07))
                Line((-0.05, 0.07), (-0.05, -0.07))
                Line((-0.05, -0.07), (0.05, -0.07))
            make_face()
        # OneSide extrude, distance=-0.002
        extrude(amount=-0.002, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1075210086, perimeter: 1.1623892818
            Circle(0.185)
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


def model_130757_c413e344_0000():
    """Model: Main"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.59, perimeter: 23.6
            with BuildLine():
                Line((-2, 1), (2, 1))
                Line((-2, -1), (-2, 1))
                Line((2, -1), (-2, -1))
                Line((2, 1), (2, -1))
            make_face()
            with BuildLine():
                Line((1.95, 0.95), (1.95, -0.95))
                Line((1.95, -0.95), (-0.9999999987, -0.95))
                Line((-0.9999999987, -0.95), (-1.95, -0.95))
                Line((-1.95, -0.95), (-1.95, 0))
                Line((-1.95, 0), (-1.95, 0.95))
                Line((-1.95, 0.95), (-1, 0.95))
                Line((-1, 0.95), (1.95, 0.95))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.15
        extrude(amount=3.15)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9795049575, perimeter: 14.7575064399
            with BuildLine():
                Line((-1, 0.95), (1.95, 0.95))
                CenterArc((-1, 0), 0.95, 71.328281936, 18.671718064)
                Line((0.25, 0.9), (-0.6958618735, 0.9))
                Line((1.45, 0.9), (0.25, 0.9))
                Line((1.45, 0.45), (1.45, 0.9))
                CenterArc((1.2625, 0), 0.4875, -67.380135052, 134.7602701039)
                Line((1.45, -0.9), (1.45, -0.45))
                Line((0.25, -0.9), (1.45, -0.9))
                Line((0, -0.9), (0.25, -0.9))
                Line((0, -0.9), (-0.6958618735, -0.9))
                CenterArc((-1, 0), 0.95, -89.9999999197, 18.6717179837)
                Line((1.95, -0.95), (-0.9999999987, -0.95))
                Line((1.95, 0.95), (1.95, -0.95))
            make_face()
            # Profile area: 0.1936781575, perimeter: 3.3922565131
            with BuildLine():
                CenterArc((-1, 0), 0.95, 180, 90.0000000803)
                Line((-1.95, -0.95), (-1.95, 0))
                Line((-0.9999999987, -0.95), (-1.95, -0.95))
            make_face()
            # Profile area: 0.1936781575, perimeter: 3.3922565105
            with BuildLine():
                Line((-1.95, 0.95), (-1, 0.95))
                Line((-1.95, 0), (-1.95, 0.95))
                CenterArc((-1, 0), 0.95, 90, 90)
            make_face()
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4942235316, perimeter: 11.2936441016
            with BuildLine():
                CenterArc((-1, 0), 0.95, 90, 90)
                CenterArc((-1, 0), 0.95, 180, 90.0000000803)
                CenterArc((-1, 0), 0.95, -89.9999999197, 18.6717179837)
                Line((0, -0.9), (-0.6958618735, -0.9))
                Line((0, -0.9), (0.25, -0.9))
                Line((0.25, -0.2), (0.25, -0.9))
                CenterArc((0.25, 0), 0.2, 90, 180)
                Line((0.25, 0.9), (0.25, 0.2))
                Line((0.25, 0.9), (-0.6958618735, 0.9))
                CenterArc((-1, 0), 0.95, 71.328281936, 18.671718064)
            make_face()
            with BuildLine():
                CenterArc((-1, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6, perimeter: 5.2
            with BuildLine():
                Line((0.35, 0.8), (0.35, -0.8))
                Line((0.35, -0.8), (1.35, -0.8))
                Line((1.35, -0.8), (1.35, 0.8))
                Line((1.35, 0.8), (0.35, 0.8))
            make_face()
            # Profile area: 0.1951099875, perimeter: 2.0466050769
            with BuildLine():
                Line((1.45, -0.45), (1.45, 0.45))
                CenterArc((1.2625, 0), 0.4875, -67.380135052, 134.7602701039)
            make_face()
        # OneSide extrude, distance=3.6
        extrude(amount=3.6, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6228318531, perimeter: 11.4283185307
            with BuildLine():
                Line((0.25, 0.9), (0.25, 0.2))
                CenterArc((0.25, 0), 0.2, 90, 180)
                Line((0.25, -0.2), (0.25, -0.9))
                Line((0.25, -0.9), (1.45, -0.9))
                Line((1.45, -0.9), (1.45, -0.45))
                Line((1.45, -0.45), (1.45, 0.45))
                Line((1.45, 0.45), (1.45, 0.9))
                Line((1.45, 0.9), (0.25, 0.9))
            make_face()
            with BuildLine():
                Line((1.35, 0.8), (0.35, 0.8))
                Line((1.35, -0.8), (1.35, 0.8))
                Line((0.35, -0.8), (1.35, -0.8))
                Line((0.35, 0.8), (0.35, -0.8))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.62
        extrude(amount=3.62, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3455751919, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((-1, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.75
        extrude(amount=3.75, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-1, 0)):
                Circle(0.5)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8, mode=Mode.ADD)

        # Sketch3 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2733971007, perimeter: 1.8535396656
            with Locations((1, 0)):
                Circle(0.295)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_130819_e0caf878_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 229.240851993, perimeter: 62.1333777581
            with BuildLine():
                Line((-6.0314533947, 9.5018910449), (6.0314533947, 9.5018910449))
                Line((-6.0314533947, -9.5018910449), (-6.0314533947, 9.5018910449))
                Line((6.0314533947, -9.5018910449), (-6.0314533947, -9.5018910449))
                Line((6.0314533947, 9.5018910449), (6.0314533947, -9.5018910449))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.0314533947, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 76.0151283588, perimeter: 46.0075641794
            with BuildLine():
                Line((-9.5018910449, 4.5), (9.5018910449, 4.5))
                Line((-9.5018910449, 0.5), (-9.5018910449, 4.5))
                Line((9.5018910449, 0.5), (-9.5018910449, 0.5))
                Line((9.5018910449, 4.5), (9.5018910449, 0.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -9.5018910449), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 44.2516271573, perimeter: 30.1258135787
            with BuildLine():
                Line((-5.5314533947, 0.5), (5.5314533947, 0.5))
                Line((5.5314533947, 0.5), (5.5314533947, 4.5))
                Line((5.5314533947, 4.5), (-5.5314533947, 4.5))
                Line((-5.5314533947, 4.5), (-5.5314533947, 0.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.5018910449), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 44.2516271573, perimeter: 30.1258135787
            with BuildLine():
                Line((-5.5314533947, 0.5), (-5.5314533947, 4.5))
                Line((5.5314533947, 0.5), (-5.5314533947, 0.5))
                Line((5.5314533947, 4.5), (5.5314533947, 0.5))
                Line((-5.5314533947, 4.5), (5.5314533947, 4.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_130917_2e98fb39_0001():
    """Model: Top 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 112.9831308421, perimeter: 38.8970844738
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1906632659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.4256116527, perimeter: 32.6138991666
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1906632659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.5069228145, perimeter: 12.1935469183
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1906632659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34.5575191895, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, 0), 3.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_131367_7cfc5499_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3600, perimeter: 240
            with BuildLine():
                Line((-30, 30), (30, 30))
                Line((-30, -30), (-30, 30))
                Line((30, -30), (-30, -30))
                Line((30, 30), (30, -30))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))) as sk:
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-25, -25)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-25, 25)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((25, 25)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((25, -25)):
                Circle(2.5)
        # TwoSides extrude, along=7.5, against=-200
        extrude(amount=7.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-200, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1600, perimeter: 160
            with BuildLine():
                Line((20, -15), (20, 25))
                Line((20, 25), (-20, 25))
                Line((-20, 25), (-20, -15))
                Line((-20, -15), (20, -15))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40, mode=Mode.ADD)

        # Sketch14 -> Extrude14 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2146018441, perimeter: 3.5707963417
            with BuildLine():
                Line((-1.0000000149, -1), (-1.0000000149, 0))
                Line((0, -1), (-1.0000000149, -1))
                CenterArc((0, 0), 1, -180, 90)
            make_face()
            # Profile area: 0.2146018441, perimeter: 3.5707963417
            with BuildLine():
                CenterArc((0, 0), 1, -90, 90)
                Line((1.0000000149, -1), (0, -1))
                Line((1.0000000149, 0), (1.0000000149, -1))
            make_face()
            # Profile area: 0.2146018441, perimeter: 3.5707963417
            with BuildLine():
                Line((-1.0000000149, 1), (0, 1))
                Line((-1.0000000149, 0), (-1.0000000149, 1))
                CenterArc((0, 0), 1, 90, 90)
            make_face()
            # Profile area: 0.2146018441, perimeter: 3.5707963417
            with BuildLine():
                CenterArc((0, 0), 1, 0, 90)
                Line((1.0000000149, 1), (1.0000000149, 0))
                Line((0, 1), (1.0000000149, 1))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


MODELS = {
    "model_100893_3ffa90e7_0000": {"func": model_100893_3ffa90e7_0000, "volume": 306.2808638012, "area": 311.2752141049},
    "model_101446_95204330_0002": {"func": model_101446_95204330_0002, "volume": 8.2037256897, "area": 85.2542478517},
    "model_102263_037b99d3_0000": {"func": model_102263_037b99d3_0000, "volume": 176.9107971708, "area": 271.6934493427},
    "model_104524_f829aab2_0003": {"func": model_104524_f829aab2_0003, "volume": 119.9066067278, "area": 172.6234523383},
    "model_106059_5d7ef4ef_0001": {"func": model_106059_5d7ef4ef_0001, "volume": 7.2690091403, "area": 143.5947333032},
    "model_106094_e167f3da_0000": {"func": model_106094_e167f3da_0000, "volume": 143.9138684622, "area": 210.9480550523},
    "model_106645_558b1d4b_0003": {"func": model_106645_558b1d4b_0003, "volume": 176.6340014109, "area": 309.2721685264},
    "model_107386_2a58ec34_0000": {"func": model_107386_2a58ec34_0000, "volume": 294.4091664821, "area": 719.1778978221},
    "model_107386_52beca0a_0000": {"func": model_107386_52beca0a_0000, "volume": 162289, "area": 18531.5},
    "model_107667_92c0fd66_0000": {"func": model_107667_92c0fd66_0000, "volume": 26.885026875, "area": 55.241825},
    "model_107832_665a08a7_0002": {"func": model_107832_665a08a7_0002, "volume": 803.547285921, "area": 715.4914207601},
    "model_110528_cfdc9482_0000": {"func": model_110528_cfdc9482_0000, "volume": 31583.5189255422, "area": 20844.4687690261},
    "model_111042_4f23bf6d_0000": {"func": model_111042_4f23bf6d_0000, "volume": 181.1679628041, "area": 454.0106117484},
    "model_111046_1e1ef6dc_0000": {"func": model_111046_1e1ef6dc_0000, "volume": 4.3453980907, "area": 41.0615927585},
    "model_111049_dbb012af_0000": {"func": model_111049_dbb012af_0000, "volume": 0.9577740758, "area": 19.6980412155},
    "model_111053_b2d052a7_0000": {"func": model_111053_b2d052a7_0000, "volume": 83.511025852, "area": 240.9419047326},
    "model_111062_e59e2d31_0000": {"func": model_111062_e59e2d31_0000, "volume": 1.7905503093, "area": 12.5976630559},
    "model_111237_40914f5f_0000": {"func": model_111237_40914f5f_0000, "volume": 2.0212648758, "area": 21.7011002756},
    "model_112181_d498e10b_0000": {"func": model_112181_d498e10b_0000, "volume": 32.2897401741, "area": 107.4277397317},
    "model_112292_7c09fb5a_0000": {"func": model_112292_7c09fb5a_0000, "volume": 2.4371703307, "area": 18.4182891858},
    "model_113001_c1b164a3_0002": {"func": model_113001_c1b164a3_0002, "volume": 0.6398278226, "area": 15.0882459968},
    "model_113001_c1b164a3_0004": {"func": model_113001_c1b164a3_0004, "volume": 3.0827963287, "area": 15.1143970445},
    "model_113001_c1b164a3_0006": {"func": model_113001_c1b164a3_0006, "volume": 0.0748564037, "area": 1.7934736937},
    "model_114429_70217b24_0000": {"func": model_114429_70217b24_0000, "volume": 31.2154804472, "area": 337.1415159501},
    "model_115533_da81d57e_0000": {"func": model_115533_da81d57e_0000, "volume": 28.343467106, "area": 319.5616200005},
    "model_115637_b4d41e8a_0000": {"func": model_115637_b4d41e8a_0000, "volume": 519.5744001001, "area": 843.584},
    "model_115637_d920ac27_0000": {"func": model_115637_d920ac27_0000, "volume": 529.2800001359, "area": 855.8000000715},
    "model_116825_d3abda56_0000": {"func": model_116825_d3abda56_0000, "volume": 2.9326348149, "area": 15.6922600705},
    "model_117144_bc95d940_0000": {"func": model_117144_bc95d940_0000, "volume": 48.5751811143, "area": 182.0444558687},
    "model_119894_8b172e77_0000": {"func": model_119894_8b172e77_0000, "volume": 3953.6933415193, "area": 3136.8241056466},
    "model_119903_14d53edb_0000": {"func": model_119903_14d53edb_0000, "volume": 46.1574888853, "area": 242.8126973725},
    "model_119916_18e9ecf9_0000": {"func": model_119916_18e9ecf9_0000, "volume": 191.116257744, "area": 510.3412818887},
    "model_121027_9ae27724_0000": {"func": model_121027_9ae27724_0000, "volume": 8.1532322974, "area": 36.4610419326},
    "model_121174_1345e289_0000": {"func": model_121174_1345e289_0000, "volume": 52.7199813088, "area": 85.459291969},
    "model_121869_67b34d49_0000": {"func": model_121869_67b34d49_0000, "volume": 0.125182, "area": 2.0784},
    "model_122515_758d8b70_0007": {"func": model_122515_758d8b70_0007, "volume": 5323.2795706372, "area": 24490.0231032595},
    "model_122515_758d8b70_0010": {"func": model_122515_758d8b70_0010, "volume": 5008.5312, "area": 6660.0738},
    "model_123687_e9e1613b_0000": {"func": model_123687_e9e1613b_0000, "volume": 80.5084064157, "area": 237.5616280172},
    "model_123773_63bda323_0000": {"func": model_123773_63bda323_0000, "volume": 0.78694, "area": 5.9244},
    "model_125742_bdbe71f2_0000": {"func": model_125742_bdbe71f2_0000, "volume": 142.7630558614, "area": 272.3628746335},
    "model_125814_188a264c_0000": {"func": model_125814_188a264c_0000, "volume": 3.1476327556, "area": 22.6654866739},
    "model_126912_e0373bb3_0000": {"func": model_126912_e0373bb3_0000, "volume": 57.7868229086, "area": 214.3655140329},
    "model_127480_74b7071f_0000": {"func": model_127480_74b7071f_0000, "volume": 11.0871074816, "area": 39.7028401544},
    "model_127543_95d04a2e_0000": {"func": model_127543_95d04a2e_0000, "volume": 82.3801795594, "area": 237.8803188671},
    "model_128043_96b40cb2_0000": {"func": model_128043_96b40cb2_0000, "volume": 11.784118813, "area": 69.6204303744},
    "model_128996_24601566_0000": {"func": model_128996_24601566_0000, "volume": 19.5721222319, "area": 64.4654812517},
    "model_128996_36e0e614_0000": {"func": model_128996_36e0e614_0000, "volume": 57.2757972237, "area": 132.184180009},
    "model_128996_89b8cb8b_0000": {"func": model_128996_89b8cb8b_0000, "volume": 4.9882600853, "area": 30.7836810144},
    "model_128996_df00e69f_0000": {"func": model_128996_df00e69f_0000, "volume": 2.8054422397, "area": 17.9856179418},
    "model_129078_9934147b_0000": {"func": model_129078_9934147b_0000, "volume": 1978.737978, "area": 6767.7284},
    "model_129414_61c80644_0000": {"func": model_129414_61c80644_0000, "volume": 9888.1913743824, "area": 7404.2057504117},
    "model_129580_45a65025_0000": {"func": model_129580_45a65025_0000, "volume": 2.5776419406, "area": 29.1799393252},
    "model_130260_262a2214_0000": {"func": model_130260_262a2214_0000, "volume": 0.1985592201, "area": 2.6417453979},
    "model_130757_854b49f3_0001": {"func": model_130757_854b49f3_0001, "volume": 6.5870478, "area": 32.5992396993},
    "model_130757_8bbd9729_0002": {"func": model_130757_8bbd9729_0002, "volume": 0.1099565455, "area": 1.5363847762},
    "model_130757_c413e344_0000": {"func": model_130757_c413e344_0000, "volume": 27.9357309388, "area": 61.161480132},
    "model_130819_e0caf878_0000": {"func": model_130819_e0caf878_0000, "volume": 1063.9450686281, "area": 806.2781884447},
    "model_130917_2e98fb39_0001": {"func": model_130917_2e98fb39_0001, "volume": 207.6987370622, "area": 548.2851728389},
    "model_131367_7cfc5499_0000": {"func": model_131367_7cfc5499_0000, "volume": 97907.7464384224, "area": 27582.2998032582},
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
