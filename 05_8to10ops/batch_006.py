"""Batch 006 - passing/05_8to10ops
75 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_27707_13288bd1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3326325453, perimeter: 10.3672557568
            with BuildLine():
                CenterArc((0, 0), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.322013247, perimeter: 12.8805298797
            with BuildLine():
                CenterArc((2.9000000298, 0.200000003), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.9000000298, 0.200000003), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.13
        extrude(amount=0.13)
    return part.part


def model_28119_f4fb1c4c_0003():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.7587511105, perimeter: 28.7645691276
            with BuildLine():
                Line((-5.0042419003, 10.1438236158), (4.9957580997, 10.1438236158))
                Line((4.9957580997, 10.1438236158), (4.9957580997, 13.0438236158))
                Line((4.9957580997, 13.0438236158), (3.6957580997, 13.0438236158))
                CenterArc((3.6957580997, 13.4899046396), 0.4460810238, -171.1783262606, 81.1783262606)
                CenterArc((1.3986500383, 13.1334037007), 1.8785261183, 8.8216737394, 81.1783262606)
                Line((1.3986500383, 15.011929819), (1.0000000149, 15.011929819))
                Line((1.0000000149, 13.0438236158), (1.0000000149, 15.011929819))
                Line((-5.0042419003, 13.0438236158), (1.0000000149, 13.0438236158))
                Line((-5.0042419003, 10.1438236158), (-5.0042419003, 13.0438236158))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13.0438236158, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.5000000745, perimeter: 21.0000000298
            with BuildLine():
                Line((4.5, -2.5), (4.5, 2.5))
                Line((4.5, 2.5), (-1.0000000149, 2.5))
                Line((-1.0000000149, 2.5), (-1.0000000149, -2.5))
                Line((4.5, -2.5), (-1.0000000149, -2.5))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.0000000149, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.339692045, perimeter: 13.3358951824
            with BuildLine():
                Line((-2.5, 12.7185377878), (-2.5, 11.0438236158))
                Line((-2.5, 11.0438236158), (2.5, 11.0438236158))
                Line((2.5, 12.7049862618), (2.5, 11.0438236158))
                Line((-2.5, 12.7185377878), (2.5, 12.7049862618))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.9957580997, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0, 11.9397429587)):
                Circle(0.45)
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)
    return part.part


def model_28287_ef6e8c9c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.168155857, perimeter: 11.2866697874
            with BuildLine():
                CenterArc((2.9876509167, 0.3032342327), 4, -174.2045609684, 51.1422833553)
                CenterArc((1.351, -2.211), 1, -123.0622776131, 68.5444555806)
                CenterArc((1.8153597555, -2.8624368868), 0.2, -54.5178220324, 93.4354942484)
                CenterArc((5.3853578547, 0.0200069399), 4.3883950181, -179.787143589, 38.704815805)
                CenterArc((0, 0), 0.997, 0.212856411, 185.5825826206)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.6, 2)):
                Circle(0.3)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0089535772, perimeter: 0.43672916
            with BuildLine():
                Line((-0.9969931199, -0.0037038916), (-1.1409886411, 0.0609927158))
                CenterArc((-5.3853578547, -0.0200069399), 4.3883950181, 0.212856411, 1.6304125593)
                Line((-1.1409886411, 0.0609927158), (-0.9992335923, 0.1211482583))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.ADD)
    return part.part


def model_28455_2e9528aa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3288628718, perimeter: 2.5497667335
            with BuildLine():
                CenterArc((8.6109929493, -3.134145121), 3.4281490963, 58.583996442, 7.513786328)
                CenterArc((0, 0), 10.4, -1.1489936023, 5.7104081447)
                CenterArc((8.6109929493, 3.7620503163), 3.4202014333, -66.4, 7.2932102222)
                CenterArc((0, 0), 10, 0, 3.6)
            make_face()
            # Profile area: 0.2199190462, perimeter: 1.9611393717
            with BuildLine():
                CenterArc((0, 0), 9.5, 1.0685978784, 1.6855192717)
                CenterArc((8.6109929493, -3.134145121), 3.4281490963, 66.09778277, 8.9007539451)
                CenterArc((0, 0), 10, 0, 3.6)
                CenterArc((8.6109929493, 3.7620503163), 3.4202014333, -75.1244757193, 8.7244757193)
            make_face()
        # OneSide extrude, distance=1.75
        extrude(amount=1.75)

        # Sketch1 -> 押し出し2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3288628718, perimeter: 2.5497667335
            with BuildLine():
                CenterArc((8.6109929493, -3.134145121), 3.4281490963, 58.583996442, 7.513786328)
                CenterArc((0, 0), 10.4, -1.1489936023, 5.7104081447)
                CenterArc((8.6109929493, 3.7620503163), 3.4202014333, -66.4, 7.2932102222)
                CenterArc((0, 0), 10, 0, 3.6)
            make_face()
            # Profile area: 25.3065331815, perimeter: 127.3970691243
            with BuildLine():
                CenterArc((0, 0), 10, 3.6, 356.4)
                CenterArc((8.6109929493, 3.7620503163), 3.4202014333, -66.4, 7.2932102222)
                CenterArc((0, 0), 10.4, 4.5614145424, 354.2895918553)
                CenterArc((8.6109929493, -3.134145121), 3.4281490963, 58.583996442, 7.513786328)
            make_face()
            # Profile area: 0.2199190462, perimeter: 1.9611393717
            with BuildLine():
                CenterArc((0, 0), 9.5, 1.0685978784, 1.6855192717)
                CenterArc((8.6109929493, -3.134145121), 3.4281490963, 66.09778277, 8.9007539451)
                CenterArc((0, 0), 10, 0, 3.6)
                CenterArc((8.6109929493, 3.7620503163), 3.4202014333, -75.1244757193, 8.7244757193)
            make_face()
            # Profile area: 283.5287369865, perimeter: 59.6902604182
            with BuildLine():
                CenterArc((0, 0), 9.5, 2.7541171501, 358.3144807283)
                CenterArc((0, 0), 9.5, 1.0685978784, 1.6855192717)
            make_face()
            # Profile area: 30.4106093263, perimeter: 122.6676764432
            with BuildLine():
                CenterArc((8.6109929493, 3.7620503163), 3.4202014333, -75.1244757193, 8.7244757193)
                CenterArc((0, 0), 10, 3.6, 356.4)
                CenterArc((8.6109929493, -3.134145121), 3.4281490963, 66.09778277, 8.9007539451)
                CenterArc((0, 0), 9.5, 2.7541171501, 358.3144807283)
            make_face()
        # OneSide extrude, distance=1.75
        extrude(amount=1.75)

        # Sketch2 -> 押し出し3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 215.0106012117, perimeter: 74.1415866247
            with BuildLine():
                CenterArc((0, 0), 8.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.35
        extrude(amount=-1.35, mode=Mode.SUBTRACT)

        # Sketch2 -> 押し出し4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.2057504117, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch2 -> 押し出し5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> 押し出し6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.732, perimeter: 4.46
            with BuildLine():
                Line((0, -1.83), (0.4, -1.83))
                Line((0.4, 0), (0.4, -1.83))
                Line((0, 0), (0.4, 0))
                Line((0, 0), (0, -1.83))
            make_face()
            # Profile area: 0.732, perimeter: 4.46
            with BuildLine():
                Line((0, 0), (0, -1.83))
                Line((-0.4, 0), (0, 0))
                Line((-0.4, 0), (-0.4, -1.83))
                Line((-0.4, -1.83), (0, -1.83))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.SUBTRACT)
    return part.part


def model_30034_f53308bd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.0043122059, perimeter: 31.7300858013
            with BuildLine():
                CenterArc((0, 0), 3.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((1, -1), (1, 1))
                Line((1, 1), (-1, 1))
                Line((-1, 1), (-1, -1))
                Line((-1, -1), (1, -1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_30375_4ff65965_0007():
    """Model: Receiver"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 144.3096370021, perimeter: 62.6230248871
            with BuildLine():
                CenterArc((-2.3601893446, 2.494523326), 3.2658484198, -36.7045963681, 126.7045963681)
                Line((-2.3601893446, 5.7603717458), (-2.4893174285, 5.7603717458))
                Line((-2.4893174285, 5.7603717458), (-2.4893174285, 8))
                Line((-2.4893174285, 8), (-10, 8))
                Line((-10, 8), (-10, 6))
                Line((-10, 6), (-20, 6))
                Line((-20, -2), (-20, 6))
                Line((-12.3036530143, -2), (-20, -2))
                Line((-12.3036530143, -0.2500000037), (-12.3036530143, -2))
                CenterArc((-9.8018265615, -0.2500000037), 2.5018264528, 0, 180)
                Line((-4.2500000373, -0.2500000037), (-7.3000001088, -0.2500000037))
                Line((-4.0000000596, -0.5000000075), (-4.2500000373, -0.2500000037))
                Line((-3.5, 0), (-4.0000000596, -0.5000000075))
                Line((0, 0), (-3.5, 0))
                CenterArc((1.4915072936, -0.376923557), 1.5383970147, 143.2954036319, 22.5221369261)
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5011467178, perimeter: 13.8660978067
            with BuildLine():
                Line((-12.3036530143, -1.263065466), (-12.3036530143, -2))
                Line((-8.6290594501, -2), (-12.3036530143, -2))
                CenterArc((-8.6290594501, -1), 1, -90, 60.5168366115)
                Line((-7.2572406312, -0.605482557), (-7.758559091, -1.4921677811))
                CenterArc((-6.6478903798, -0.9500000037), 0.7, 90, 60.5168366115)
                Line((-6.6478903798, -0.2500000037), (-7.3000001088, -0.2500000037))
                Line((-7.3000001088, -0.2500000037), (-7.8823401243, -1.2799885811))
                CenterArc((-8.7528404834, -0.7878208), 1, -90, 60.5168366115)
                Line((-8.7528404834, -1.7878208), (-11.0750657213, -1.7878208))
                CenterArc((-11.0750657213, -1.4878208), 0.3, -103.6062034071, 13.6062034071)
                Line((-11.145639925, -1.7794014608), (-12.0742272181, -1.5546461268))
                CenterArc((-12.0036530143, -1.263065466), 0.3, -180, 76.3937965929)
            make_face()
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.7859848933, perimeter: 16.5878129507
            with BuildLine():
                Line((-19, -1.15), (-13.0060935246, -1.15))
                Line((-13.0060935246, -1.15), (-13.0060935246, 1.15))
                Line((-13.0060935246, 1.15), (-19, 1.15))
                Line((-19, 1.15), (-19, -1.15))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch1 (1) -> Extrude1 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2526463725, perimeter: 8.7705252852
            with BuildLine():
                Line((-7.6351812976, 1.0009132227), (-7.6351812976, 3))
                CenterArc((-8.7185039296, 3), 1.083322632, 0, 180)
                Line((-9.8018265615, 2.251826449), (-9.8018265615, 3))
                CenterArc((-9.8018265615, -0.2500000037), 2.5018264528, 30, 60)
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True, mode=Mode.SUBTRACT)

        # Sketch2 (1) -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.7630807309, perimeter: 10.2262911511
            with BuildLine():
                CenterArc((-1.6101893446, 3.4719423556), 0.75, 180, 105)
                Line((-1.4160750608, 2.7474979859), (0.7943779888, 3.3397870955))
                CenterArc((-2.3601893446, 2.494523326), 3.2658484198, 15, 75)
                Line((-2.3601893446, 3.4719423556), (-2.3601893446, 5.7603717458))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_30417_0010bc7c_0002():
    """Model: Motor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.190705401, perimeter: 19.4778744523
            Circle(3.1)
        # OneSide extrude, distance=11.2
        extrude(amount=11.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 51.84, perimeter: 28.8
            with BuildLine():
                Line((3.6, -3.6), (-3.6, -3.6))
                Line((3.6, 3.6), (3.6, -3.6))
                Line((-3.6, 3.6), (3.6, 3.6))
                Line((-3.6, -3.6), (-3.6, 3.6))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.190705401, perimeter: 19.4778744523
            Circle(3.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11.9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)
    return part.part


def model_30421_211edb5e_0001():
    """Model: Rubber Hammer"""
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
        # Sketch7 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((0, 30)):
                Circle(4)
        # Symmetric extrude, each_side=5.5
        extrude(amount=5.5, both=True)
    return part.part


def model_30445_791b6800_0001():
    """Model: Component13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.7081071856, -9.700959302)):
                Circle(0.25)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-2.7081071856, 9.700959302), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.7081071856, 9.700959302), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.7081071856, 9.700959302)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0337239447, perimeter: 1.0325333099
            with BuildLine():
                Line((2.4581071856, 9.700959302), (2.4581071856, 9.4560103277))
                Line((2.4581071856, 9.9459082762), (2.4581071856, 9.700959302))
                CenterArc((2.7081071856, 9.700959302), 0.35, 135.5846914028, 88.8306171944)
            make_face()
            # Profile area: 0.0337239447, perimeter: 1.0325333099
            with BuildLine():
                CenterArc((2.7081071856, 9.700959302), 0.35, -44.4153085972, 88.8306171944)
                Line((2.9581071856, 9.9459082762), (2.9581071856, 9.700959302))
                Line((2.9581071856, 9.700959302), (2.9581071856, 9.4560103277))
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.4581071856, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-9.700959302, -0.5000000075)):
                Circle(0.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_30445_791b6800_0004():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3161154607, perimeter: 4.0667916901
            with Locations((-7.3349286718, -0.7879317909)):
                Circle(0.64725)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6291235638, perimeter: 2.811725425
            with Locations((7.3349286718, 0.7879317909)):
                Circle(0.4475)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6869918969, perimeter: 6.878517115
            with BuildLine():
                CenterArc((7.3349286718, 0.7879317909), 0.64725, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.3349286718, 0.7879317909), 0.4475, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6291235638, perimeter: 2.811725425
            with Locations((7.3349286718, 0.7879317909)):
                Circle(0.4475)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1342242005, perimeter: 1.298734403
            with Locations((-7.3349286718, 0.7879317909)):
                Circle(0.2067)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_30445_791b6800_0008():
    """Model: Component22"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-15.5, 3)):
                Circle(0.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((15.5, 3)):
                Circle(0.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((15.5, 3)):
                Circle(0.25)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((15.9685213497, 3.3748169485)):
                Circle(0.1)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


def model_30667_2511afcb_0003():
    """Model: Liga+º+úo das articula+º+Áes"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.6854437156, perimeter: 27.2584631033
            with BuildLine():
                Line((0, 0), (0, -4.5164))
                Line((0, -4.5164), (5.5, -4.5164))
                Line((5.5, -4.5164), (5.5, 0))
                Line((0, 0), (5.5, 0))
            make_face()
            with BuildLine():
                CenterArc((2.75, -2.2582), 1.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.8077468847, perimeter: 9.3138797401
            with BuildLine():
                CenterArc((2.75, -2.2582), 1.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.75, -2.2582), 0.33235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8077468847, perimeter: 9.3138797401
            with BuildLine():
                CenterArc((-2.75, 2.2582), 1.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.75, 2.2582), 0.33235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 18.9931906004, perimeter: 20.1210166368
            with BuildLine():
                Line((5.5, 0.5), (0, 0.5))
                Line((5.5, 4.0164), (5.5, 0.5))
                Line((0, 4.0164), (5.5, 4.0164))
                Line((0, 4.0164), (0, 0.5))
            make_face()
            with BuildLine():
                CenterArc((2.75, 2.2582), 0.33235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0755711062, perimeter: 9.8507761468
            with BuildLine():
                Line((5.5, -4.5328), (5.9998, -4.5328))
                Line((5.9998, -4.5328), (5.9998, -0.4871638787))
                CenterArc((5.9998, 0.0128), 0.4999638787, -178.5329617808, 88.5329617808)
                Line((5.5, 0), (5.5, -4.5328))
            make_face()
            # Profile area: 0.0596138129, perimeter: 1.3308871448
            with BuildLine():
                CenterArc((4.6598, -6.7262), 2.3488166382, 55.2148971585, 13.8253517273)
                Line((5.9998, -4.7971226039), (5.9998, -4.5328))
                Line((5.5, -4.5328), (5.9998, -4.5328))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


def model_30667_2511afcb_0005():
    """Model: Parafuso-eixo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4948008429, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


def model_30672_73fd9f76_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.167698931, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 7.5000001118), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 7.5000001118), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True, mode=Mode.ADD)

        # Sketch16 -> Extrude7 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5, -7)):
                Circle(0.25)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, taper=0.81846)

        # Sketch17 -> Extrude8 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((-5, -5), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, -5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_30690_3df2c9e2_0011():
    """Model: Pistón"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.8212337735, perimeter: 27.6460153516
            with Locations((-10.986363217, -2.3475712743)):
                Circle(4.4)
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34.2119439976, perimeter: 20.7345115137
            with Locations((10.986363217, 2.3475712743)):
                Circle(3.3)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 7.6340701482, perimeter: 50.8938009882
            with BuildLine():
                CenterArc((-10.986363217, 2.3475712743), 4.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10.986363217, 2.3475712743), 3.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((-10.986363217, 2.3475712743)):
                Circle(0.9)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


def model_30690_3df2c9e2_0017():
    """Model: Pasador"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-25, 26)):
                Circle(0.4)
        # OneSide extrude, distance=2.32
        extrude(amount=2.32)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.32, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4185386813, perimeter: 2.2933626371
            with Locations((-25, 26)):
                Circle(0.365)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.4185386813, perimeter: 2.2933626371
            with Locations((25, 26)):
                Circle(0.365)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.48, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0841161433, perimeter: 4.80663676
            with BuildLine():
                CenterArc((-25, 26), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-25, 26), 0.365, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4185386813, perimeter: 2.2933626371
            with Locations((-25, 26)):
                Circle(0.365)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.16, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0841161433, perimeter: 4.80663676
            with BuildLine():
                CenterArc((25, 26), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((25, 26), 0.365, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4185386813, perimeter: 2.2933626371
            with Locations((25, 26)):
                Circle(0.365)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)
    return part.part


def model_30809_b0bc2529_0000():
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
        # Sketch8 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5855053868, perimeter: 3.6637910033
            with BuildLine():
                Line((1.4012431256, 1.3007243016), (1.4190501627, 1.1253096402))
                Line((1.4190501627, 1.1253096402), (1.4625950419, 1.1155631111))
                CenterArc((2.0632342497, 3.7990580528), 2.7498931907, -102.6164098549, 32.7276023191)
                CenterArc((2.9780480068, 1.3007243016), 0.089337658, -69.8888075358, 139.7776150716)
                CenterArc((2.3033508684, -0.5418569011), 2.0515613245, 69.8888075358, 46.1970605209)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch10 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4530144126, perimeter: 4.7946723213
            with BuildLine():
                CenterArc((0.4658485127, 0.9728223068), 0.4977458937, 46.5591483824, 59.809990497)
                CenterArc((0.6894067981, 0.2117231112), 1.2909988751, 106.3691388794, 48.4269708678)
                Line((-0.5736093922, 0.5597973209), (-0.4786865841, 0.7614830098))
                CenterArc((-0.2153143407, 0.3911667524), 0.3959944602, 154.7961097472, 47.059337466)
                Line((-0.5643716868, 0.1976889092), (-0.5828470975, 0.243751403))
                CenterArc((1.4099192402, -0.6548212331), 2.1504878998, 122.7410119682, 33.9040243075)
                CenterArc((0.5609266731, 0.6655407391), 0.5807286455, 70.3125532186, 52.4284587496)
                Line((0.860947889, 1.1749748302), (0.7565677535, 1.2123225305))
                CenterArc((1.0224802194, 1.6264287722), 0.479482383, -109.6874467814, 19.6874467814)
                Line((1.0969768649, 1.1469463893), (1.0224802194, 1.1469463893))
                Line((1.0855428212, 1.2712577886), (1.0969768649, 1.1469463893))
                Line((1.0455893502, 1.2712577886), (1.0855428212, 1.2712577886))
                CenterArc((0.9645907725, 1.423331901), 0.1723000443, -133.4408516176, 71.4817627354)
                Line((0.8081012673, 1.3342279331), (0.8461163349, 1.2982274929))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


def model_30904_54099e05_0003():
    """Model: Proyector v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1200, perimeter: 140
            with BuildLine():
                Line((20, -15), (20, 15))
                Line((20, 15), (-20, 15))
                Line((-20, 15), (-20, -15))
                Line((-20, -15), (20, -15))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -15), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 56.5486677646, perimeter: 26.657297629
            with Locations((12, 6)):
                Circle(4.2426406871)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.9999872595, perimeter: 50.7999997139
            with BuildLine():
                Line((17.6999997422, -12.5000001863), (17.3000002578, -12.5000001863))
                Line((17.6999997422, 12.5000001863), (17.6999997422, -12.5000001863))
                Line((17.3000002578, 12.5000001863), (17.6999997422, 12.5000001863))
                Line((17.3000002578, -12.5000001863), (17.3000002578, 12.5000001863))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, -5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 118.4292036732, perimeter: 50.2831853072
            with BuildLine():
                Line((5, -7), (-5, -7))
                Line((5, 5), (5, -7))
                Line((-5, 5), (5, 5))
                Line((-5, -7), (-5, 5))
            make_face()
            with BuildLine():
                CenterArc((0, -5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_30905_511b96bf_0002():
    """Model: taki element v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 65, perimeter: 36
            with BuildLine():
                Line((5, 13), (5, 0))
                Line((0, 13), (5, 13))
                Line((0, 0), (0, 13))
                Line((5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5, -12.4552249013)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5, -11.5)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.9389450091, perimeter: 9.9695889938
            with BuildLine():
                Line((12, 5), (12.0305274955, 1))
                Line((12.0305274955, 1), (13, 1))
                Line((13, 1), (13, 5))
                Line((13, 5), (12, 5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5, -12.5032376027)):
                Circle(0.25)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_30905_511b96bf_0006():
    """Model: Metalowy element spod v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.9314165294, perimeter: 33.4247779608
            with BuildLine():
                Line((-3, 3), (-3, -3))
                Line((-3, -3), (3, -3))
                Line((3, -3), (3, 3))
                Line((3, 3), (-3, 3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.32, perimeter: 13.6
            with BuildLine():
                Line((2.6, 2), (2.6, 3.6))
                Line((2.6, 3.6), (-2.6, 3.6))
                Line((-2.6, 3.6), (-2.6, 2))
                Line((-2.6, 2), (2.6, 2))
            make_face()
        # OneSide extrude, distance=-7.6
        extrude(amount=-7.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-5.2
        extrude(amount=-5.2, mode=Mode.SUBTRACT)
    return part.part


def model_30905_511b96bf_0011():
    """Model: PODLOKIETNIK v11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180, perimeter: 72
            with BuildLine():
                Line((-6, -30), (-6, 0))
                Line((0, -30), (-6, -30))
                Line((0, 0), (0, -30))
                Line((-6, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.7857616115, perimeter: 16.2443129015
            with BuildLine():
                Line((0, 0), (-6, 0))
                Line((-4.3168433594, -3.0857871745), (-6, 0))
                CenterArc((-3, -2.3675089785), 1.5, -151.389540334, 122.7790806681)
                Line((0, 0), (-1.6831566406, -3.0857871745))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3, 21.0144297206)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3, 12.3959297206)):
                Circle(0.25)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                Line((2.9930964272, 19.1797631733), (2.9930964272, 18.6797631733))
                CenterArc((2.9930964272, 18.9297631733), 0.25, -90, 180)
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((2.9930964272, 18.9297631733), 0.25, 90, 180)
                Line((2.9930964272, 19.1797631733), (2.9930964272, 18.6797631733))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_30905_511b96bf_0013():
    """Model: Dysza v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # TwoSides offset extrude, full=-19, trim=-1
        extrude(amount=-19, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.SUBTRACT)
    return part.part


def model_31008_8fa25b35_0009():
    """Model: Shaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=11.6
        extrude(amount=11.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.2332961007, perimeter: 15.3938040026
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.69, perimeter: 5.2
            with BuildLine():
                Line((0.65, -0.65), (0.65, 0.65))
                Line((0.65, 0.65), (-0.65, 0.65))
                Line((-0.65, 0.65), (-0.65, -0.65))
                Line((-0.65, -0.65), (0.65, -0.65))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.65, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1809557368, perimeter: 1.5079644737
            with Locations((0, -0.665)):
                Circle(0.24)
        # OneSide extrude, distance=-2.9
        extrude(amount=-2.9, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.8961649822, perimeter: 28.5927781409
            with BuildLine():
                CenterArc((0, 0), 3.2, 55.7711336722, 248.4577326556)
                Line((1.8, -2.6457513111), (1.8, 2.6457513111))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)
    return part.part


def model_31008_8fa25b35_0011():
    """Model: 9 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1786582423, perimeter: 2.2049943307
            with BuildLine():
                CenterArc((0, 0), 0.65, 127.9798724449, 104.0402551103)
                Line((-0.4, 0.5123475383), (-0.4, -0.5123475383))
            make_face()
            # Profile area: 0.5149967942, perimeter: 3.1370408941
            with BuildLine():
                CenterArc((0, 0), 0.65, 52.0201275551, 75.9597448897)
                Line((0.4, 0.5123475383), (0.4, 1.25))
                Line((0.4, 1.25), (-0.4, 1.25))
                Line((-0.4, 1.25), (-0.4, 0.5123475383))
            make_face()
            # Profile area: 0.5149967942, perimeter: 3.1370408941
            with BuildLine():
                CenterArc((0, 0), 0.65, -127.9798724449, 75.9597448897)
                Line((-0.4, -0.5123475383), (-0.4, -1.25))
                Line((-0.4, -1.25), (0.4, -1.25))
                Line((0.4, -1.25), (0.4, -0.5123475383))
            make_face()
            # Profile area: 0.1786582423, perimeter: 2.2049943307
            with BuildLine():
                Line((0.4, -0.5123475383), (0.4, 0.5123475383))
                CenterArc((0, 0), 0.65, -52.0201275551, 104.0402551103)
            make_face()
            # Profile area: 0.9700064116, perimeter: 3.7728620947
            with BuildLine():
                Line((-0.4, 0.5123475383), (-0.4, -0.5123475383))
                CenterArc((0, 0), 0.65, -127.9798724449, 75.9597448897)
                Line((0.4, -0.5123475383), (0.4, 0.5123475383))
                CenterArc((0, 0), 0.65, 52.0201275551, 75.9597448897)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.16, perimeter: 2
            with BuildLine():
                Line((-0.4, 0), (0.4, 0))
                Line((-0.4, 0), (-0.4, -0.2))
                Line((-0.4, -0.2), (0.4, -0.2))
                Line((0.4, -0.2), (0.4, 0))
            make_face()
            # Profile area: 0.16, perimeter: 2
            with BuildLine():
                Line((0.4, 0.2), (-0.4, 0.2))
                Line((-0.4, 0.2), (-0.4, 0))
                Line((-0.4, 0), (0.4, 0))
                Line((0.4, 0), (0.4, 0.2))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.16, perimeter: 2
            with BuildLine():
                Line((-0.4, 0), (0.4, 0))
                Line((-0.4, 0), (-0.4, -0.2))
                Line((-0.4, -0.2), (0.4, -0.2))
                Line((0.4, -0.2), (0.4, 0))
            make_face()
            # Profile area: 0.16, perimeter: 2
            with BuildLine():
                Line((-0.4, 0.2), (-0.4, 0))
                Line((-0.4, 0), (0.4, 0))
                Line((0.4, 0), (0.4, 0.2))
                Line((0.4, 0.2), (-0.4, 0.2))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_31013_d34d1b29_0003():
    """Model: Nakretka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7539822369, perimeter: 15.0796447372
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.4394631186, perimeter: 18.6924762889
            with BuildLine():
                CenterArc((0, 0), 1.725, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7539822369, perimeter: 15.0796447372
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            Circle(1.15)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2170250998, perimeter: 5.5425626668
            with BuildLine():
                Line((0.8000000119, -0.4618802222), (0.8000000119, 0.4618802222))
                Line((0.8000000119, 0.4618802222), (0, 0.9237604445))
                Line((0, 0.9237604445), (-0.8000000119, 0.4618802222))
                Line((-0.8000000119, 0.4618802222), (-0.8000000119, -0.4618802222))
                Line((-0.8000000119, -0.4618802222), (0, -0.9237604445))
                Line((0, -0.9237604445), (0.8000000119, -0.4618802222))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


def model_31016_60e3fd8e_0004():
    """Model: Component32"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4410139867, perimeter: 2.8299923216
            with BuildLine():
                Line((-6.1710180427, -6.435), (-5.63, -6.435))
                Line((-5.63, -6.435), (-5.63, -5.565))
                Line((-6.1710180427, -5.565), (-5.63, -5.565))
                CenterArc((-8, -6), 1.88, -13.3785071609, 26.7570143217)
            make_face()
            # Profile area: 2.2368139694, perimeter: 22.3681396936
            with BuildLine():
                CenterArc((-8, -6), 1.88, -13.3785071609, 26.7570143217)
                CenterArc((-8, -6), 1.88, 13.3785071609, 333.2429856783)
            make_face()
            with BuildLine():
                CenterArc((-8, -6), 1.68, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-5.63, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3572, perimeter: 4.86
            with BuildLine():
                Line((-5.565, 0.2), (-6.435, 0.2))
                Line((-5.565, 0.2), (-5.565, 1.76))
                Line((-6.435, 1.76), (-5.565, 1.76))
                Line((-6.435, 0.2), (-6.435, 1.76))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.76, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.175, perimeter: 6.74
            with BuildLine():
                Line((5.63, 6.435), (5.63, 5.565))
                Line((5.63, 6.435), (3.13, 6.435))
                Line((3.13, 6.435), (3.13, 5.565))
                Line((5.63, 5.565), (3.13, 5.565))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.76, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((4.11, 6)):
                Circle(0.25)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_31280_c8bd4b11_0004():
    """Model: Ball Socket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1453589838, perimeter: 1.8535898385
            with BuildLine():
                Line((2.45, -0.9), (2.25, -0.9))
                Line((2.45, -0.1732050808), (2.45, -0.9))
                Line((2.25, -0.1732050808), (2.45, -0.1732050808))
                Line((2.25, -0.1732050808), (2.25, -0.9))
            make_face()
            # Profile area: 0.1453589838, perimeter: 1.8535898385
            with BuildLine():
                Line((2.25, 0.1732050808), (2.45, 0.1732050808))
                Line((2.45, 0.9), (2.45, 0.1732050808))
                Line((2.25, 0.9), (2.45, 0.9))
                Line((2.25, 0.9), (2.25, 0.1732050808))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4126913803, perimeter: 19.2674618213
            with BuildLine():
                CenterArc((-2.0539279825, -0.4094245763), 0.2162565051, 36.3068548715, 132.8788489675)
                Line((-2.2663438727, -0.4500000067), (-2.2663438727, -0.3688491458))
                CenterArc((-1.875189833, -0.5049983532), 0.3950016468, 171.9963757728, 98.0036242272)
                Line((2.25, -0.9), (-1.875189833, -0.9))
                Line((2.25, -0.1732050808), (2.25, -0.9))
                CenterArc((2.35, 0), 0.2, 120, 120)
                Line((2.25, 0.9), (2.25, 0.1732050808))
                Line((-1.875189833, 0.9), (2.25, 0.9))
                CenterArc((-1.875189833, 0.5049983532), 0.3950016468, 90, 98.0036242272)
                Line((-2.2663438727, 0.3688491458), (-2.2663438727, 0.4500000067))
                CenterArc((-2.0539279825, 0.4094245763), 0.2162565051, -169.1857038389, 132.8788489675)
                CenterArc((-1.4663438727, 0), 0.5, -145.7535266334, 291.5070532668)
            make_face()
            with BuildLine():
                CenterArc((-0.2163438727, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.3836561273, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on Profile plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.36, perimeter: 4
            with BuildLine():
                Line((2.042476209, -1.2141852742), (2.242476209, -1.2141852742))
                Line((2.042476209, -3.0141852742), (2.042476209, -1.2141852742))
                Line((2.242476209, -3.0141852742), (2.042476209, -3.0141852742))
                Line((2.242476209, -1.2141852742), (2.242476209, -3.0141852742))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on Profile plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0776750769, perimeter: 18.7959606411
            with BuildLine():
                Line((-1.882713624, -1.2141852742), (2.042476209, -1.2141852742))
                CenterArc((-1.882713624, -1.609186921), 0.3950016468, 90, 98.0036242272)
                CenterArc((-2.0614517735, -1.704760698), 0.2162565051, 169.1857038389, 154.5074412896)
                CenterArc((-1.4738676638, -2.1141852742), 0.5, -145.7535266334, 291.5070532668)
                CenterArc((-2.0614517735, -2.5236098505), 0.2162565051, 36.3068548715, 154.5074412896)
                CenterArc((-1.882713624, -2.6191836275), 0.3950016468, 171.9963757728, 98.0036242272)
                Line((2.042476209, -3.0141852742), (-1.882713624, -3.0141852742))
                Line((2.042476209, -3.0141852742), (2.042476209, -1.2141852742))
            make_face()
            with BuildLine():
                CenterArc((-0.2238676638, -2.1141852742), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.3761323362, -2.1141852742), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.242476209, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0942422504, perimeter: 1.0882476952
            with Locations((-2.1141852742, 0.400000006)):
                Circle(0.1732)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_31463_c4c75dd7_0000():
    """Model: phone gripper v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.748672584, perimeter: 16.5132741416
            with BuildLine():
                Line((2, -1.5), (2, 1.5))
                Line((2, 1.5), (-2, 1.5))
                Line((-2, 1.5), (-2, -1.5))
                Line((-2, -1.5), (2, -1.5))
            make_face()
            with BuildLine():
                CenterArc((-1.5000000224, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5000000224, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1356232692, perimeter: 1.7874950916
            with BuildLine():
                Line((-0.5937475264, 1), (-0.400000006, 1))
                Line((-0.400000006, 1), (-0.400000006, 1.7000000253))
                Line((-0.400000006, 1.7000000253), (-0.5937475264, 1.7000000253))
                Line((-0.5937475264, 1.7000000253), (-0.5937475264, 1))
            make_face()
            # Profile area: 2.0011696979, perimeter: 6.2192569339
            with BuildLine():
                Line((0.3939646247, 1), (0.6000000089, 1))
                Line((0.6000000089, 1), (1.3071743705, 1))
                Line((1.3000000194, 3.2000000477), (1.3071743705, 1))
                Line((0.3939646247, 3.2000000477), (1.3000000194, 3.2000000477))
                Line((0.3939646247, 3.2000000477), (0.3939646247, 1))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.2000000477, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9301236677, perimeter: 6.6200825253
            with BuildLine():
                Line((-1.5000000224, -0.6899587969), (-1.5000000224, -1.0000000149))
                Line((-1.5000000224, -1.0000000149), (1.5000000224, -1.0000000149))
                Line((1.5000000224, -1.0000000149), (1.5000000224, -0.6899587969))
                Line((1.5000000224, -0.6899587969), (-1.5000000224, -0.6899587969))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2591813939, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((1.5000000224, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5000000224, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2591813902, perimeter: 3.4557519377
            with BuildLine():
                CenterArc((-1.5000000224, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5000000224, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.0042733745, -1.3104215034), x_dir=(-1, 0, 0), z_dir=(0, 0.0032610513, -0.9999946828))):
            # Profile area: 0.0420735663, perimeter: 1.0332626502
            with BuildLine():
                Line((-0.1964603757, 3.1986982937), (0.219088288, 3.1986982937))
                Line((0.2186491478, 3.3000000492), (0.219088288, 3.1986982937))
                Line((-0.1964603757, 3.3000000492), (0.2186491478, 3.3000000492))
                Line((-0.1964603757, 3.1986982937), (-0.1964603757, 3.3000000492))
            make_face()
            # Profile area: 0.6241601539, perimeter: 3.8350468367
            with BuildLine():
                Line((-0.1964603757, 1.696729957), (0.2191010962, 1.696729957))
                Line((0.2191010962, 3.1957436658), (0.2191010962, 1.696729957))
                Line((0.219088288, 3.1986982937), (0.2191010962, 3.1957436658))
                Line((-0.1964603757, 3.1986982937), (0.219088288, 3.1986982937))
                Line((-0.1964603757, 1.696729957), (-0.1964603757, 3.1986982937))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_31463_c4c75dd7_0002():
    """Model: fly v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.078904967, perimeter: 1.1945440231
            with BuildLine():
                CenterArc((0, 0), 0.3, -120, 60)
                Line((-0.15, -0.2598076211), (-0.15, -0.55))
                Line((-0.15, -0.55), (0.15, -0.55))
                Line((0.15, -0.55), (0.15, -0.2598076211))
            make_face()
            # Profile area: 0.078904967, perimeter: 1.1945440231
            with BuildLine():
                CenterArc((0, 0), 0.3, 60, 60)
                Line((0.15, 0.2598076211), (0.15, 0.55))
                Line((0.15, 0.55), (-0.15, 0.55))
                Line((-0.15, 0.55), (-0.15, 0.2598076211))
            make_face()
            # Profile area: 0.0507521156, perimeter: 1.3050134057
            with BuildLine():
                Line((-0.15, 0.2598076211), (-0.15, 0))
                CenterArc((0, 0), 0.15, 0, 180)
                Line((0.15, 0), (0.15, 0.2598076211))
                CenterArc((0, 0), 0.3, 60, 60)
            make_face()
            # Profile area: 0.0507521156, perimeter: 1.3050134057
            with BuildLine():
                Line((0.15, -0.2598076211), (0.15, 0))
                CenterArc((0, 0), 0.15, -180, 180)
                Line((-0.15, 0), (-0.15, -0.2598076211))
                CenterArc((0, 0), 0.3, -120, 60)
            make_face()
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.15, -180, 180)
                CenterArc((0, 0), 0.15, 0, 180)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.15, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                CenterArc((0, 0.8), 0.2, 180, 180)
                Line((0.2, 0.8), (-0.2, 0.8))
            make_face()
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                Line((0.2, 0.8), (-0.2, 0.8))
                CenterArc((0, 0.8), 0.2, 0, 180)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_31464_b2855e3a_0000():
    """Model: Foward"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21.5067520679, perimeter: 20.5555900439
            with BuildLine():
                CenterArc((0, 0), 1.905, -41.8103148958, 263.6206297916)
                Line((-2.54, -1.27), (-1.4199031657, -1.27))
                Line((-2.54, -3.5052), (-2.54, -1.27))
                Line((2.54, -3.5052), (-2.54, -3.5052))
                Line((2.54, -1.27), (2.54, -3.5052))
                Line((1.4199031657, -1.27), (2.54, -1.27))
            make_face()
        # OneSide extrude, distance=9.525
        extrude(amount=9.525)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-1.5875, -3.1877)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((0, -1.9177)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((1.5875, -3.1877)):
                Circle(0.15875)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.54), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((2.54, -2.2352)):
                Circle(0.3175)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9.525, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((1.27, -2.2352)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((0, 0.3048)):
                Circle(0.3175)
            # Profile area: 0.1583460872, perimeter: 1.6324556675
            with BuildLine():
                CenterArc((-1.27, -2.2352), 0.3175, 180, 180)
                Line((-0.9525, -2.2352), (-1.5875, -2.2352))
            make_face()
            # Profile area: 0.1583460872, perimeter: 1.6324556675
            with BuildLine():
                Line((-0.9525, -2.2352), (-1.5875, -2.2352))
                CenterArc((-1.27, -2.2352), 0.3175, 0, 180)
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508, mode=Mode.ADD)
    return part.part


def model_31607_9a2f8140_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21, perimeter: 31
            with BuildLine():
                Line((-7, 1.5), (7, 1.5))
                Line((-7, 1.5), (-7, 0))
                Line((7, 0), (-7, 0))
                Line((7, 1.5), (7, 0))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)

        # Sketch9 -> Extrude8 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8943297187, perimeter: 8.2394189541
            with BuildLine():
                Line((0, 9.8052505151), (0.200000003, 9.8052505151))
                Line((0.200000003, 9.8052505151), (0.200000003, 9.6052505151))
                Line((0.200000003, 9.6052505151), (0.400000003, 9.6052505151))
                Line((0.400000003, 9.6052505151), (0.400000003, 9.4052505151))
                Line((0.400000003, 9.4052505151), (0.600000003, 9.4052505151))
                Line((0.600000003, 9.4052505151), (0.600000003, 9.2052505151))
                Line((0.600000003, 9.2052505151), (0.800000003, 9.2052505151))
                Line((0.800000003, 9.2052505151), (0.800000003, 9.0052505151))
                Line((0.800000003, 9.0052505151), (1.000000003, 9.0052505151))
                Line((1.000000003, 9.0052505151), (1.000000003, 8.8052505151))
                Line((1.000000003, 8.8052505151), (1.200000003, 8.8052505151))
                Line((1.200000003, 8.8052505151), (1.200000003, 8.6052505151))
                Line((1.200000003, 8.6052505151), (1.400000003, 8.6052505151))
                Line((1.400000003, 8.6052505151), (1.400000003, 8.3802905602))
                Line((1.400000003, 8.3802905602), (2.5000000373, 8.3802905602))
                Line((2.5000000373, 10), (2.5000000373, 8.3802905602))
                Line((0, 10), (2.5000000373, 10))
                Line((0, 10), (0, 9.8052505151))
            make_face()
            # Profile area: 2.8943296885, perimeter: 8.2394189168
            with BuildLine():
                Line((0, 9.8052505151), (-0.200000003, 9.8052505151))
                Line((0, 10), (0, 9.8052505151))
                Line((-2.5, 10), (0, 10))
                Line((-2.5000000373, 8.3802905602), (-2.5, 10))
                Line((-1.400000003, 8.3802905602), (-2.5000000373, 8.3802905602))
                Line((-1.400000003, 8.6052505151), (-1.400000003, 8.3802905602))
                Line((-1.200000003, 8.6052505151), (-1.400000003, 8.6052505151))
                Line((-1.200000003, 8.8052505151), (-1.200000003, 8.6052505151))
                Line((-1.000000003, 8.8052505151), (-1.200000003, 8.8052505151))
                Line((-1.000000003, 9.0052505151), (-1.000000003, 8.8052505151))
                Line((-0.800000003, 9.0052505151), (-1.000000003, 9.0052505151))
                Line((-0.800000003, 9.2052505151), (-0.800000003, 9.0052505151))
                Line((-0.600000003, 9.2052505151), (-0.800000003, 9.2052505151))
                Line((-0.600000003, 9.4052505151), (-0.600000003, 9.2052505151))
                Line((-0.400000003, 9.4052505151), (-0.600000003, 9.4052505151))
                Line((-0.400000003, 9.6052505151), (-0.400000003, 9.4052505151))
                Line((-0.200000003, 9.6052505151), (-0.400000003, 9.6052505151))
                Line((-0.200000003, 9.8052505151), (-0.200000003, 9.6052505151))
            make_face()
        # Symmetric extrude, each_side=-0.5
        extrude(amount=-0.5, both=True)

        # Sketch10 -> Extrude9 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.534070767, perimeter: 2.5906237073
            Circle(0.4123105687)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch15 -> Extrude13 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 18, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4432735869, perimeter: 7.575404744
            with BuildLine():
                CenterArc((0, 0), 0.7933525422, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4123105687, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.534070767, perimeter: 2.5906237073
            Circle(0.4123105687)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_31962_e5291336_0022():
    """Model: TENS"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            with Locations((6, 2)):
                Circle(1.7)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            with Locations((6, 2)):
                Circle(1.7)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((6, 2)):
                Circle(1.6)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((6, 2)):
                Circle(0.35)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((6, 2)):
                Circle(0.25)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_31962_e5291336_0028():
    """Model: eje brazo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((42, -1)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1118238045, perimeter: 1.727295218
            with BuildLine():
                Line((41.7, -0.6), (41.7, -1.4))
                CenterArc((42, -1), 0.5, 126.8698976458, 106.2602047083)
            make_face()
            # Profile area: 0.1118238045, perimeter: 1.727295218
            with BuildLine():
                Line((42.3, -0.6), (42.3, -1.4))
                CenterArc((42, -1), 0.5, -53.1301023542, 106.2602047083)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-42, -1)):
                Circle(0.3)
        # OneSide extrude, distance=2.9
        extrude(amount=2.9, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((42, -1)):
                Circle(0.15)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_31962_e5291336_0046():
    """Model: Tope 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((15, 1)):
                Circle(1.6)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((15, 1)):
                Circle(1)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            with Locations((15, 1)):
                Circle(0.85)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((-15, 1)):
                Circle(0.45)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_31962_e5291336_0048():
    """Model: Eje (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0386890711, perimeter: 3.6128315516
            with Locations((8.3915186826, 1.3757720615)):
                Circle(0.575)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((8.3915186826, 1.3757720615)):
                Circle(0.4)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((8.3915186826, 1.3757720615)):
                Circle(0.25)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-8.3915186826, 1.3757720615)):
                Circle(0.15)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_31962_e5291336_0049():
    """Model: base rectangular"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((13, 0.5), (13, 3))
                Line((14, 0.5), (13, 0.5))
                Line((14, 3), (14, 0.5))
                Line((13, 3), (14, 3))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-13.5000002012, 2.4000000358)):
                Circle(0.25)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -13), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((0.5, 1.3)):
                Circle(0.325)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((13.5, 1.3)):
                Circle(0.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_32160_661a301e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1576460362, perimeter: 1.6258524488
            with BuildLine():
                CenterArc((54.8767300141, 2.820996162), 0.3175, 36.0198345875, 178.806316339)
                CenterArc((46.0435004988, 15.24), 15.24, -55.770690904, 2.387367322)
            make_face()
            # Profile area: 0.1590461382, perimeter: 1.6390818547
            with BuildLine():
                CenterArc((46.0435004988, 15.24), 15.24, -55.770690904, 2.387367322)
                CenterArc((54.8767300141, 2.820996162), 0.3175, -145.1738490735, 181.193683661)
            make_face()
        # OneSide extrude, distance=6.858
        extrude(amount=6.858)

        # Sketch9 -> Extrude6 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0767740381, perimeter: 1.5319554625
            with BuildLine():
                Line((54.8131993376, 21.2343997434), (54.1527993456, 21.2343997434))
                Line((54.1527993456, 21.2343997434), (54.60999934, 21.0565997455))
                Line((54.60999934, 21.0565997455), (54.8131993376, 21.0565997455))
                Line((54.8131993376, 21.0565997455), (54.8131993376, 21.2343997434))
            make_face()
        # Symmetric extrude, each_side=6.35
        extrude(amount=6.35, both=True)

        # Sketch10 -> Extrude8 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 208.9260496663, perimeter: 57.8182154289
            with BuildLine():
                Line((-7.2722145099, 7.1823393473), (7.2722145099, 7.1823393473))
                Line((-7.2722145099, -7.1823393473), (-7.2722145099, 7.1823393473))
                Line((7.2722145099, -7.1823393473), (-7.2722145099, -7.1823393473))
                Line((7.2722145099, 7.1823393473), (7.2722145099, -7.1823393473))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54)
    return part.part


def model_32219_e5edc7ce_0043():
    """Model: KROPLOWKA1 v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 200, perimeter: 60
            with BuildLine():
                Line((0, 20), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 20))
                Line((10, 20), (0, 20))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-5, 1.25), (-6, 1.25))
                Line((-5, 1.75), (-5, 1.25))
                Line((-6, 1.75), (-5, 1.75))
                Line((-6, 1.25), (-6, 1.75))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-5, 1.25), (-4, 1.25))
                Line((-4, 1.25), (-4, 1.75))
                Line((-4, 1.75), (-5, 1.75))
                Line((-5, 1.75), (-5, 1.25))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((5, 22)):
                Circle(0.5)
        # OneSide extrude, distance=-3.1
        extrude(amount=-3.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((4.5, 1.5)):
                Circle(0.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_32853_bd6998c3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch12 -> Extrude10 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0358494296, perimeter: 0.6711908957
            with Locations((0, 7.4000001103)):
                Circle(0.1068233488)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1)

        # Sketch24 -> Extrude13 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0157079637, perimeter: 0.4442883004
            with Locations((-1.6000000238, -2.2000000328)):
                Circle(0.0707106792)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch24 -> Extrude14 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1528431579, perimeter: 1.9518553403
            with BuildLine():
                Line((-1.7963149505, -2.3518425732), (-1.6036851001, -2.4481574984))
                Line((-1.6036851001, -2.4481574984), (-1.4082803121, -2.3576047905))
                Line((-1.4082803121, -2.3576047905), (-1.3572443774, -2.1483724855))
                Line((-1.3572443774, -2.1483724855), (-1.4890083958, -1.9780167766))
                Line((-1.4890083958, -1.9780167766), (-1.7043513739, -1.9748189873))
                Line((-1.7043513739, -1.9748189873), (-1.841115657, -2.141187118))
                Line((-1.841115657, -2.141187118), (-1.7963149505, -2.3518425732))
            make_face()
            with BuildLine():
                CenterArc((-1.6000000238, -2.2000000328), 0.0707106792, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0157079637, perimeter: 0.4442883004
            with Locations((-1.6000000238, -2.2000000328)):
                Circle(0.0707106792)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.ADD)
    return part.part


def model_33532_e1c141b1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1451.61, perimeter: 154.94
            with BuildLine():
                Line((0, 31.75), (0, 0))
                Line((0, 0), (45.72, 0))
                Line((45.72, 0), (45.72, 31.75))
                Line((45.72, 31.75), (0, 31.75))
            make_face()
        # OneSide extrude, distance=4.318
        extrude(amount=4.318)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 19 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.318, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.976400756, perimeter: 31.768043795
            with BuildLine():
                Line((0, -15.875), (-13.335, -15.875))
                Line((0, -15.875), (0, -13.2588))
                Line((0, -13.2588), (-12.954, -13.04798))
                CenterArc((-2.6562558, -15.875), 10.6787442, 164.6488894565, 15.3511105435)
            make_face()
            # Profile area: 35.976400756, perimeter: 31.768043795
            with BuildLine():
                Line((0, -18.4912), (0, -15.875))
                Line((0, -15.875), (-13.335, -15.875))
                CenterArc((-2.6562558, -15.875), 10.6787442, 180, 15.3511105435)
                Line((0, -18.4912), (-12.954, -18.70202))
            make_face()
        # OneSide extrude, distance=-1.778
        extrude(amount=-1.778, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 19 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.318, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.8838492, perimeter: 13.64996
            with BuildLine():
                Line((-14.605, -15.875), (-17.145, -15.875))
                Line((-17.145, -20.15998), (-17.145, -15.875))
                Line((-14.605, -20.15998), (-17.145, -20.15998))
                Line((-14.605, -15.875), (-14.605, -20.15998))
            make_face()
            # Profile area: 10.8838492, perimeter: 13.64996
            with BuildLine():
                Line((-14.605, -11.59002), (-14.605, -15.875))
                Line((-17.145, -11.59002), (-14.605, -11.59002))
                Line((-17.145, -15.875), (-17.145, -11.59002))
                Line((-14.605, -15.875), (-17.145, -15.875))
            make_face()
            # Profile area: 10.8838492, perimeter: 13.64996
            with BuildLine():
                Line((-20.574, -15.875), (-20.574, -20.15998))
                Line((-20.574, -15.875), (-23.114, -15.875))
                Line((-23.114, -20.15998), (-23.114, -15.875))
                Line((-20.574, -20.15998), (-23.114, -20.15998))
            make_face()
            # Profile area: 10.8838492, perimeter: 13.64996
            with BuildLine():
                Line((-20.574, -11.59002), (-20.574, -15.875))
                Line((-23.114, -11.59002), (-20.574, -11.59002))
                Line((-23.114, -15.875), (-23.114, -11.59002))
                Line((-20.574, -15.875), (-23.114, -15.875))
            make_face()
            # Profile area: 17.795093442, perimeter: 16.87576
            with BuildLine():
                Line((-25.0825, -15.875), (-29.2354, -15.875))
                Line((-29.2354, -20.15998), (-29.2354, -15.875))
                Line((-25.0825, -20.15998), (-29.2354, -20.15998))
                Line((-25.0825, -15.875), (-25.0825, -20.15998))
            make_face()
            # Profile area: 17.795093442, perimeter: 16.87576
            with BuildLine():
                Line((-25.0825, -11.59002), (-25.0825, -15.875))
                Line((-29.2354, -11.59002), (-25.0825, -11.59002))
                Line((-29.2354, -15.875), (-29.2354, -11.59002))
                Line((-25.0825, -15.875), (-29.2354, -15.875))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


def model_33995_18423507_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.6305887996, perimeter: 11.7133927406
            with BuildLine():
                Line((-0.5188104089, 4.623173594), (-0.5221391057, 4.8968559781))
                Line((-0.5221391057, 4.8968559781), (-0.6312127717, 5.0112060988))
                Line((-0.6312127717, 5.0112060988), (-2.4986916041, 5.0112060988))
                Line((-2.4986916041, 5.0112060988), (-2.6108022662, 4.9023271914))
                Line((-2.6108022662, 4.9023271914), (-2.6108022662, 4.6386383173))
                CenterArc((-2.7578528769, 4.6392287085), 0.1470517959, -77.2429840731, 77.0129493749)
                Line((-2.7253813604, 4.4958068438), (-3.0157530373, 4.4958068438))
                Line((-3.0157530373, 4.4958068438), (-3.1271929782, 4.3859364795))
                Line((-3.1271929782, 4.3859364795), (-3.1271929782, 2.5217046105))
                Line((-3.1271929782, 2.5217046105), (-3.0145653075, 2.4074679731))
                Line((-3.0145653075, 2.4074679731), (-2.7519264349, 2.4074679731))
                CenterArc((-2.7608484456, 2.2553182388), 0.1524111017, 5.5606851585, 81.0833521426)
                Line((-2.6091545717, 2.2700868712), (-2.6091545717, 2.0057967156))
                Line((-2.6091545717, 2.0057967156), (-2.5025090787, 1.8961065066))
                Line((-2.5025090787, 1.8961065066), (-0.6283617915, 1.8961065066))
                Line((-0.6283617915, 1.8961065066), (-0.5189985658, 2.0024340926))
                Line((-0.5189985658, 2.0024340926), (-0.5189985658, 2.268503374))
                CenterArc((-0.3814263613, 2.268503374), 0.1375722045, 92.7094234436, 87.2905765564)
                Line((-0.3879295009, 2.4059217884), (-0.1171146744, 2.4059217884))
                Line((-0.1171146744, 2.4059217884), (-0.0065096092, 2.5171971874))
                Line((-0.0065096092, 2.5171971874), (-0.0065096092, 4.3865946867))
                Line((-0.0065096092, 4.3865946867), (-0.1124053531, 4.4918525045))
                Line((-0.1124053531, 4.4918525045), (-0.3858823971, 4.4918525045))
                CenterArc((-0.3858823971, 4.6247903478), 0.1329378434, -179.3031671502, 89.3031671502)
            make_face()
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.667393888, perimeter: 12.1731424051
            with BuildLine():
                CenterArc((-0.1607471886, 2.0473883383), 0.1542378109, -91.5150899709, 91.4158092354)
                Line((-0.0016865005, 4.8305764522), (-0.0065096092, 2.0471210789))
                CenterArc((-0.1740539294, 4.8308751266), 0.1723676877, -0.0992807355, 91.9243700176)
                Line((-2.9662505412, 5.0031553739), (-0.1795435697, 5.0031553739))
                CenterArc((-2.9621197244, 4.8439859712), 0.1592229958, 91.486625234, 88.513374766)
                Line((-3.1213427202, 2.0565408289), (-3.1213427202, 4.8439859712))
                CenterArc((-2.9581500282, 2.0593228215), 0.163216403, -179.0233570059, 88.9638345775)
                Line((-0.1648252713, 1.8932044495), (-2.9583195876, 1.8961065066))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch33 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.18180926, perimeter: 1.912226429
            with BuildLine():
                Line((-3.1318375128, 0.9019262129), (-3.2530638986, 0.9019262129))
                Line((-3.2530638986, 0.9019262129), (-3.4240567336, 0.7905253825))
                Line((-3.4240567336, 0.7905253825), (-3.6003788591, 0.9029188494))
                Line((-3.7021335941, 0.9029188494), (-3.6003788591, 0.9029188494))
                Line((-3.7021335941, 0.5495367494), (-3.7021335941, 0.9029188494))
                Line((-3.1318375128, 0.5495367494), (-3.7021335941, 0.5495367494))
                Line((-3.1318375128, 0.9019262129), (-3.1318375128, 0.5495367494))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8)
    return part.part


def model_34226_dbed877f_0010():
    """Model: scianaboczna v24"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.1243362939, perimeter: 52.9566370614
            with BuildLine():
                Line((0, 1.25), (0, 0))
                Line((0, 0), (25, 0))
                Line((25, 0), (25, 1.25))
                Line((25, 1.25), (19.7, 1.25))
                CenterArc((19.5, 1.25), 0.2, 180, 180)
                Line((19.3, 1.25), (5.7, 1.25))
                CenterArc((5.5, 1.25), 0.2, 180, 180)
                Line((0, 1.25), (5.3, 1.25))
            make_face()
            # Profile area: 812.2486725877, perimeter: 115.9132741229
            with BuildLine():
                Line((0, 33.75), (5.3, 33.75))
                Line((0, 33.75), (0, 1.25))
                Line((0, 1.25), (5.3, 1.25))
                CenterArc((5.5, 1.25), 0.2, 0, 180)
                Line((19.3, 1.25), (5.7, 1.25))
                CenterArc((19.5, 1.25), 0.2, 0, 180)
                Line((25, 1.25), (19.7, 1.25))
                Line((25, 1.25), (25, 33.75))
                Line((25, 33.75), (19.7, 33.75))
                CenterArc((19.5, 33.75), 0.2, 180, 180)
                Line((19.3, 33.75), (5.7, 33.75))
                CenterArc((5.5, 33.75), 0.2, 180, 180)
            make_face()
            # Profile area: 31.1243362939, perimeter: 52.9566370614
            with BuildLine():
                CenterArc((5.5, 33.75), 0.2, 0, 180)
                Line((19.3, 33.75), (5.7, 33.75))
                CenterArc((19.5, 33.75), 0.2, 0, 180)
                Line((25, 33.75), (19.7, 33.75))
                Line((25, 33.75), (25, 35))
                Line((25, 35), (0, 35))
                Line((0, 35), (0, 33.75))
                Line((0, 33.75), (5.3, 33.75))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0033687696, perimeter: 9.0136566231
            with BuildLine():
                Line((-0.5, 0), (-0.5, -4))
                Line((0, -4.0134750783), (-0.5, -4))
                Line((0, -4.0134750783), (0, 0))
                Line((0, 0), (-0.5, 0))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_34317_e9c65aa6_0021():
    """Model: Holder v6 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 140, perimeter: 54
            with BuildLine():
                Line((13, -4), (-7, -4))
                Line((13, 3), (13, -4))
                Line((-7, 3), (13, 3))
                Line((-7, -4), (-7, 3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20, perimeter: 42
            with BuildLine():
                Line((13, 2), (-7, 2))
                Line((13, 3), (13, 2))
                Line((-7, 3), (13, 3))
                Line((-7, 2), (-7, 3))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -13), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 10.5, perimeter: 16.4462219947
            with BuildLine():
                Line((-1, -4), (-1, 2))
                Line((-1, 2), (-4.5, 2))
                Line((-4.5, 2), (-1, -4))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 10.5, perimeter: 16.4462219947
            with BuildLine():
                Line((1, -4), (1, 2))
                Line((4.5, 2), (1, -4))
                Line((1, 2), (4.5, 2))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


def model_34317_e9c65aa6_0022():
    """Model: Main beam v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((3, -3), (-3, -3))
                Line((3, 3), (3, -3))
                Line((-3, 3), (3, 3))
                Line((-3, -3), (-3, 3))
            make_face()
        # OneSide extrude, distance=140
        extrude(amount=140)

        # Sketch5 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 264.4223882175, perimeter: 75.0251544131
            with BuildLine():
                Line((23, 13), (0, 13))
                Line((0, 13), (0, 3))
                Line((0, 3), (29.8844776435, 3))
                Line((29.8844776435, 3), (23, 13))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.ADD)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(140, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)
    return part.part


def model_34317_e9c65aa6_0024():
    """Model: Pillar v6 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((0, -2.5), (-6, -2.5))
                Line((0, 3.5), (0, -2.5))
                Line((-6, 3.5), (0, 3.5))
                Line((-6, -2.5), (-6, 3.5))
            make_face()
        # OneSide extrude, distance=47
        extrude(amount=47)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 221.0095412762, perimeter: 122.620571722
            with BuildLine():
                Line((-7.3396064258, -2.5), (0, -2.5))
                Line((-49.9916259381, -30.223812683), (-7.3396064258, -2.5))
                Line((-49.9916259381, -30.223812683), (-50, -35))
                Line((0, -2.5), (-50, -35))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 211.2077427234, perimeter: 100.1515791197
            with BuildLine():
                Line((47, -33.05), (50, -35))
                Line((47, -33.05), (47, -37.5))
                Line((47, -37.5), (52.5, -37.5))
                Line((52.5, -37.5), (52.5, 3.5))
                Line((52.5, 3.5), (47, 3.5))
                Line((47, 3.5), (47, -2.5))
                Line((47, -2.5), (47, -28.2792558232))
                Line((49.9916259381, -30.223812683), (47, -28.2792558232))
                Line((50, -35), (49.9916259381, -30.223812683))
            make_face()
            # Profile area: 14.2922572766, perimeter: 16.6930674732
            with BuildLine():
                Line((50, -35), (49.9916259381, -30.223812683))
                Line((49.9916259381, -30.223812683), (47, -28.2792558232))
                Line((47, -28.2792558232), (47, -33.05))
                Line((47, -33.05), (50, -35))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 50.34519703, perimeter: 33.9433426918
            with BuildLine():
                Line((28.703143745, -16.3862992575), (24.703143745, -13.7862992575))
                Line((28.703143745, -16.3862992575), (28.703143745, -2.5))
                Line((24.703143745, -2.5), (28.703143745, -2.5))
                Line((24.703143745, -13.7862992575), (24.703143745, -2.5))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.ADD)
    return part.part


def model_34568_fbe47bf9_0002():
    """Model: pieza 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.032684, perimeter: 0.9552
            with BuildLine():
                Line((0.17, 0), (0.17, 0.1))
                Line((0.17, 0.1), (0.13, 0.1))
                Line((0.13, 0.1), (0.13, 0.0812))
                Line((0.13, 0.0812), (0.095, 0.0812))
                Line((0.095, 0.0812), (0.095, 0.1))
                Line((-0.095, 0.1), (0.095, 0.1))
                Line((-0.095, 0.0812), (-0.095, 0.1))
                Line((-0.13, 0.0812), (-0.095, 0.0812))
                Line((-0.13, 0.1), (-0.13, 0.0812))
                Line((-0.17, 0.1), (-0.13, 0.1))
                Line((-0.17, 0), (-0.17, 0.1))
                Line((-0.17, 0), (0.17, 0))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0175158634, perimeter: 0.4751382282
            with BuildLine():
                CenterArc((-0.0325, 0.0214), 0.0181, 16.6450468919, 101.8000086784)
                CenterArc((0, 0.1000367697), 0.075, -101.6605154464, 11.6605154464)
                CenterArc((0, 0.1000367697), 0.075, -90, 33.2049079994)
                CenterArc((0, 0.1000367697), 0.075, -56.7950920006, 293.5457099092)
            make_face()
            # Profile area: 0.0004123054, perimeter: 0.0988836979
            with BuildLine():
                CenterArc((-0.0325, 0.0214), 0.0181, -90, 106.6450468919)
                CenterArc((0, 0.1000367697), 0.075, -123.2374653257, 21.5769498793)
                CenterArc((-0.0515, 0.0214), 0.019, 0, 56.8430712823)
                Line((-0.0325, 0.0033), (-0.0325, 0.0214))
            make_face()
            # Profile area: 0.0001555953, perimeter: 0.0604188508
            with BuildLine():
                CenterArc((0, 0.1000367697), 0.075, -123.2493820914, 0.0119167657)
                CenterArc((0, 0.1000367697), 0.075, -123.2374653257, 21.5769498793)
                CenterArc((-0.0325, 0.0214), 0.0181, 16.6450468919, 101.8000086784)
            make_face()
            # Profile area: 0.0004984791, perimeter: 0.1097900091
            with BuildLine():
                Line((0, 0), (0, 0.0250367697))
                CenterArc((0, 0.1000367697), 0.075, -101.6605154464, 11.6605154464)
                CenterArc((-0.0325, 0.0214), 0.0181, -90, 106.6450468919)
                Line((-0.0325, 0), (-0.0325, 0.0033))
                Line((0, 0), (-0.0325, 0))
            make_face()
            # Profile area: 0.0009107845, perimeter: 0.1412091514
            with BuildLine():
                Line((0.0325, 0), (0.0325, 0.0214))
                CenterArc((0.0515, 0.0214), 0.019, 123.2854446014, 56.7145553986)
                CenterArc((0, 0.1000367697), 0.075, -90, 33.2049079994)
                Line((0, 0), (0, 0.0250367697))
                Line((0, 0), (0.0325, 0))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0009365254, perimeter: 0.1419631886
            with BuildLine():
                Line((0, 1.2), (0, 1.2283963168))
                Line((0, 1.2), (0.03, 1.2))
                Line((0.03, 1.2), (0.03, 1.2241))
                CenterArc((0.049, 1.2241), 0.019, 123.5764883895, 56.4235116105)
                CenterArc((0, 1.2983963168), 0.07, -90, 33.3593435852)
            make_face()
            # Profile area: 0.0009365254, perimeter: 0.1419631887
            with BuildLine():
                CenterArc((-0.049, 1.2241), 0.019, 0, 56.4235130712)
                Line((-0.03, 1.2), (-0.03, 1.2241))
                Line((0, 1.2), (-0.03, 1.2))
                Line((0, 1.2), (0, 1.2283963168))
                CenterArc((0, 1.2983963168), 0.07, -123.3593433159, 33.3593433159)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0015830413, perimeter: 0.1758515306
            with BuildLine():
                Line((0.0000000002, 1.2283963168), (0, 1.2983963168))
                CenterArc((0.0384921742, 1.2399296381), 0.07, 123.3593435852, 60)
                CenterArc((0, 1.2983963168), 0.07, -116.6406564148, 26.6406565495)
            make_face()
            # Profile area: 0.0093747925, perimeter: 0.4398229715
            with BuildLine():
                CenterArc((0, 1.2983963168), 0.07, -123.3593433159, 6.718686901)
                CenterArc((0.0384921742, 1.2399296381), 0.07, 123.3593435852, 60)
                CenterArc((0.0384921742, 1.2399296381), 0.07, 63.3593435852, 60)
                CenterArc((0, 1.2983963168), 0.07, 3.3593435852, 233.281313099)
            make_face()
            # Profile area: 0.0044359702, perimeter: 0.2573637837
            with BuildLine():
                CenterArc((0.0384921742, 1.2399296381), 0.07, 63.3593435852, 60)
                Line((0.0000000002, 1.2283963168), (0, 1.2983963168))
                CenterArc((0, 1.2983963168), 0.07, -89.9999998653, 33.3593427847)
                CenterArc((0, 1.2983963168), 0.07, -56.6406570806, 60.0000006658)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_34568_fbe47bf9_0003():
    """Model: pieza 8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0740730092, perimeter: 1.7520796327
            with BuildLine():
                Line((0.55, 0.225), (0.55, 0.2725))
                Line((0.55, 0.2725), (0.375, 0.2725))
                Line((0.375, 0.2725), (0.375, 0.0875))
                Line((0.375, 0.0875), (0, 0.0875))
                Line((0, 0.0875), (0, 0))
                Line((0, 0), (0.55, 0))
                Line((0.55, 0), (0.55, 0.125))
                Line((0.55, 0.125), (0.525, 0.125))
                CenterArc((0.525, 0.175), 0.05, 90, 180)
                Line((0.525, 0.225), (0.55, 0.225))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0003017186, perimeter: 0.061575216
            with Locations((-0.4494999877, 0.051)):
                Circle(0.0098)
        # OneSide extrude, distance=-0.0875
        extrude(amount=-0.0875, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0003017186, perimeter: 0.061575216
            with Locations((-0.1005, 0.051)):
                Circle(0.0098)
        # OneSide extrude, distance=-0.0875
        extrude(amount=-0.0875, mode=Mode.SUBTRACT)
    return part.part


def model_34781_4f8a4759_0006():
    """Model: Ajus v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0549778714, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0780575443, perimeter: 1.4888607262
            with BuildLine():
                Line((0.0011742555, 0.1749960603), (-0.3055598853, 0.1770543024))
                CenterArc((-0.3092796778, -0.3772961017), 0.5543628842, 89.6155406207, 38.3084840457)
                Line((-0.6499999855, 0.0599999987), (-0.6504025964, 0))
                Line((-0.6504025964, 0), (-0.175, 0))
                CenterArc((0, 0), 0.175, 89.6155406207, 90.3844593793)
            make_face()
            # Profile area: 0.0241555669, perimeter: 0.6260636215
            with BuildLine():
                CenterArc((0, 0), 0.175, 89.6155406207, 90.3844593793)
                Line((-0.175, 0), (0, 0))
                Line((0, 0), (0.0011742555, 0.1749960603))
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95, mode=Mode.ADD)
    return part.part


def model_34781_4f8a4759_0013():
    """Model: Control v4 (1)"""
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0022887427, perimeter: 0.2264888472
            with BuildLine():
                CenterArc((0, 0), 0.6, -90, 6.3487731754)
                Line((0, -0.5322377557), (0.0663482298, -0.5963203102))
                Line((0, -0.6), (0, -0.5322377557))
            make_face()
            # Profile area: 0.0022887427, perimeter: 0.2264888472
            with BuildLine():
                Line((0, -0.6), (0, -0.5322377557))
                Line((-0.0663482298, -0.5963203102), (0, -0.5322377557))
                CenterArc((0, 0), 0.6, -96.3487731754, 6.3487731754)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            Circle(0.400000006)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_34782_b461066c_0004():
    """Model: screen v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1040, perimeter: 132
            with BuildLine():
                Line((32.4813694721, -21.2973559391), (-7.5186305279, -21.2973559391))
                Line((32.4813694721, 4.7026440609), (32.4813694721, -21.2973559391))
                Line((-7.5186305279, 4.7026440609), (32.4813694721, 4.7026440609))
                Line((-7.5186305279, -21.2973559391), (-7.5186305279, 4.7026440609))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 949.2258186676, perimeter: 126.3788475129
            with BuildLine():
                Line((-6.815986467, 4), (-6.815986467, -20.5947118782))
                Line((-6.815986467, -20.5947118782), (31.7787254112, -20.5947118782))
                Line((31.7787254112, -20.5947118782), (31.7787254112, 4))
                Line((31.7787254112, 4), (-6.815986467, 4))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -21.2973559391, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 20.9088337069, perimeter: 21.7270669655
            with BuildLine():
                Line((2.5, -6.6084956149), (0, -6.6084956149))
                Line((2.5, -6.6084956149), (2.5, 1.7550378678))
                Line((0, 1.7550378678), (2.5, 1.7550378678))
                Line((0, -6.6084956149), (0, 1.7550378678))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6.6084956149), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.5571247112, perimeter: 9.4456997689
            with BuildLine():
                Line((-2.5, -24.0745060546), (0, -24.0745060546))
                Line((-2.5, -26.2973559391), (-2.5, -24.0745060546))
                Line((0, -26.2973559391), (-2.5, -26.2973559391))
                Line((0, -24.0745060546), (0, -26.2973559391))
            make_face()
        # OneSide extrude, distance=17
        extrude(amount=17, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 56.3793274718, perimeter: 55.1727667344
            with BuildLine():
                Line((23.6084956149, -26.2973559391), (23.6084956149, -24.0745060546))
                Line((23.6084956149, -24.0745060546), (6.6084956149, -24.0745060546))
                Line((6.6084956149, -24.0745060546), (-1.7550378678, -24.0745060546))
                Line((-1.7550378678, -24.0745060546), (-1.7550378678, -26.2973559391))
                Line((-1.7550378678, -26.2973559391), (23.6084956149, -26.2973559391))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_34785_dc3b83fa_0000():
    """Model: teleskopowy wysuw1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 226.9800692219, perimeter: 53.407075111
            Circle(8.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 153.9380400259, perimeter: 43.9822971503
            Circle(7)
        # OneSide extrude, distance=50
        extrude(amount=50, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 95.0331777711, perimeter: 34.5575191895
            Circle(5.5)
        # OneSide extrude, distance=-50
        extrude(amount=-50, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 51), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 63.6172512352, perimeter: 28.2743338823
            Circle(4.5)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_34785_dc3b83fa_0020():
    """Model: zew v6 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.223689233, perimeter: 12.4707658145
            with BuildLine():
                Line((1.0392304845, 1.8), (-1.0392304845, 1.8))
                Line((-1.0392304845, 1.8), (-2.0784609691, 0))
                Line((-2.0784609691, 0), (-1.0392304845, -1.8))
                Line((-1.0392304845, -1.8), (1.0392304845, -1.8))
                Line((1.0392304845, -1.8), (2.0784609691, 0))
                Line((2.0784609691, 0), (1.0392304845, 1.8))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_34917_61633e20_0008():
    """Model: valve v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9110618695, perimeter: 18.2212373908
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch11 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2126972171, perimeter: 2.4290536993
            with BuildLine():
                Line((-0.1069480687, 2.4977113746), (-0.1076295761, 1.4961336419))
                CenterArc((0, 0), 1.5, 85.9678704513, 8.1468124297)
                Line((0.1057701993, 2.4977615308), (0.1054737947, 1.4962871645))
                Line((-0.1069480687, 2.4977113746), (0.1057701993, 2.4977615308))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch12 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1086475459, 0, 0.0000739275), x_dir=(0.0006804338, 0, -0.9999997685), z_dir=(0.9999997685, 0, 0.0006804338))):
            # Profile area: 0.5007889823, perimeter: 3.4169077562
            with BuildLine():
                Line((-2.4976380253, 1.3), (-2.4976380253, 0.3))
                Line((-2.4976380253, 0.3), (-1.4960600607, 1.3))
                Line((-1.4960600607, 1.3), (-2.4976380253, 1.3))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


def model_36088_1ea9c8a9_0001():
    """Model: Front Plate"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 27, perimeter: 21
            with BuildLine():
                Line((2.25, -3), (-2.25, -3))
                Line((2.25, 3), (2.25, -3))
                Line((-2.25, 3), (2.25, 3))
                Line((-2.25, -3), (-2.25, 3))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_36088_1ea9c8a9_0002():
    """Model: Engine Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 27, perimeter: 21
            with BuildLine():
                Line((2.25, -3), (-2.25, -3))
                Line((2.25, 3), (2.25, -3))
                Line((-2.25, 3), (2.25, 3))
                Line((-2.25, -3), (-2.25, 3))
            make_face()
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True)
    return part.part


def model_36088_1ea9c8a9_0007():
    """Model: Distance Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.78
        extrude(amount=1.78, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.18, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_37040_ecbcd25e_0033():
    """Model: ścianka szkielet 2 v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.8043080321, perimeter: 30.0807520192
            with BuildLine():
                Line((-6.538882752, -9), (6.538882752, -9))
                Line((-6.538882752, -9), (-7.2654252801, -10))
                Line((-7.2654252801, -10), (7.2654252801, -10))
                Line((6.538882752, -9), (7.2654252801, -10))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 379.1106201639, perimeter: 93.0617011202
            with BuildLine():
                Line((-5.2654252801, 2), (5.2654252801, 2))
                Line((5.2654252801, 2), (5.2654252801, 38))
                Line((-5.2654252801, 38), (5.2654252801, 38))
                Line((-5.2654252801, 2), (-5.2654252801, 38))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 97.0617011202, perimeter: 194.1234022404
            with BuildLine():
                Line((-6.2654252801, 1), (6.2654252801, 1))
                Line((6.2654252801, 1), (6.2654252801, 39))
                Line((6.2654252801, 39), (-6.2654252801, 39))
                Line((-6.2654252801, 1), (-6.2654252801, 39))
            make_face()
            with BuildLine():
                Line((-5.2654252801, 38), (5.2654252801, 38))
                Line((5.2654252801, 38), (5.2654252801, 2))
                Line((5.2654252801, 2), (-5.2654252801, 2))
                Line((-5.2654252801, 2), (-5.2654252801, 38))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.506170112, perimeter: 25.4617011202
            with BuildLine():
                Line((-6.2654252801, 9.4), (6.2654252801, 9.4))
                Line((-6.2654252801, 9.4), (-6.2654252801, 9.2))
                Line((-6.2654252801, 9.2), (6.2654252801, 9.2))
                Line((6.2654252801, 9.2), (6.2654252801, 9.4))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_37117_89aac9d4_0009():
    """Model: noodles"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9500765233, perimeter: 5.9847340051
            with BuildLine():
                CenterArc((13.9699997902, -3.8099999428), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((13.9699997902, -3.8099999428), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4757875, perimeter: 59.69
            with BuildLine():
                Line((-11.9062497902, -1.9050000572), (-11.9062497902, 9.5249999428))
                Line((-11.9062497902, 9.5249999428), (-16.0337497902, 9.5249999428))
                Line((-16.0337497902, 9.5249999428), (-16.0337497902, -1.9050000572))
                Line((-16.0337497902, -1.9050000572), (-11.9062497902, -1.9050000572))
            make_face()
            with BuildLine():
                Line((-15.7162497902, -1.5875000572), (-12.2237497902, -1.5875000572))
                Line((-15.7162497902, 9.2074999428), (-15.7162497902, -1.5875000572))
                Line((-12.2237497902, 9.2074999428), (-15.7162497902, 9.2074999428))
                Line((-12.2237497902, -1.5875000572), (-12.2237497902, 9.2074999428))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 36.4347688023, perimeter: 32.5648226701
            with BuildLine():
                Line((-12.2237497902, -1.5875000572), (-12.2237497902, 9.2074999428))
                Line((-12.2237497902, 9.2074999428), (-15.7162497902, 9.2074999428))
                Line((-15.7162497902, 9.2074999428), (-15.7162497902, -1.5875000572))
                Line((-15.7162497902, -1.5875000572), (-12.2237497902, -1.5875000572))
            make_face()
            with BuildLine():
                CenterArc((-13.9699997902, 3.8099999428), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9500765233, perimeter: 5.9847340051
            with BuildLine():
                CenterArc((-13.9699997902, 3.8099999428), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-13.9699997902, 3.8099999428), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-13.9699997902, 3.8099999428)):
                Circle(0.3175)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4757875, perimeter: 59.69
            with BuildLine():
                Line((-16.0337497902, -1.9050000572), (-11.9062497902, -1.9050000572))
                Line((-11.9062497902, -1.9050000572), (-11.9062497902, 9.5249999428))
                Line((-11.9062497902, 9.5249999428), (-16.0337497902, 9.5249999428))
                Line((-16.0337497902, 9.5249999428), (-16.0337497902, -1.9050000572))
            make_face()
            with BuildLine():
                Line((-15.7162497902, -1.5875000572), (-12.2237497902, -1.5875000572))
                Line((-15.7162497902, 9.2074999428), (-15.7162497902, -1.5875000572))
                Line((-12.2237497902, 9.2074999428), (-15.7162497902, 9.2074999428))
                Line((-12.2237497902, -1.5875000572), (-12.2237497902, 9.2074999428))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11.9062497902, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 25.8064, perimeter: 25.4
            with BuildLine():
                Line((-1.2700000572, 3.4925), (-1.2700000572, 6.0325))
                Line((8.8899999428, 3.4925), (-1.2700000572, 3.4925))
                Line((8.8899999428, 6.0325), (8.8899999428, 3.4925))
                Line((8.8899999428, 6.0325), (-1.2700000572, 6.0325))
            make_face()
        # OneSide extrude, distance=-1.778
        extrude(amount=-1.778, mode=Mode.SUBTRACT)
    return part.part


def model_37377_90529181_0013():
    """Model: stelaz do kola v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((-1, -4), (-4, -4))
                Line((-1, -1.5), (-1, -4))
                Line((-4, -1.5), (-1, -1.5))
                Line((-4, -4), (-4, -1.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((-1, 3.5), (-1, 4))
                Line((-1, 4), (-4, 4))
                Line((-4, 4), (-4, 3.5))
                Line((-4, 3.5), (-1, 3.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5, 2.5000000373)):
                Circle(0.5)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-3, 0.5), (-3, -0.5))
                Line((-3, -0.5), (-2, -0.5))
                Line((-2, -0.5), (-2, 0.5))
                Line((-2, 0.5), (-3, 0.5))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40, perimeter: 82
            with BuildLine():
                Line((3, 44), (2, 44))
                Line((2, 44), (2, 4))
                Line((2, 4), (3, 4))
                Line((3, 4), (3, 44))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25, mode=Mode.ADD)
    return part.part


def model_37615_8399c412_0003():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.5680055708, perimeter: 27.2851378183
            with BuildLine():
                Line((-4.5, -3.9), (0, -3.9))
                Line((0, -3.9), (0, 0))
                Line((0, 0), (-4.8, 0))
                CenterArc((-4.8, -1.3), 1.3, 90, 156.1016290888)
                CenterArc((-5.8938120974, -3.7685167803), 1.4, -5.388965936, 71.4905950249)
            make_face()
            with BuildLine():
                CenterArc((-5.4499923969, -1.3000274167), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.599990392, -1.0000169846), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.6000638632, -3.100022641), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.8000638632, -3.100022641), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2276799454, perimeter: 4.372154496
            with BuildLine():
                CenterArc((-5.4499923969, -1.3000274167), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.4499923969, -1.3000274167), 0.29585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2749748792, perimeter: 1.8588803731
            with Locations((-5.4499923969, -1.3000274167)):
                Circle(0.29585)
        # TwoSides extrude (symmetric), distance=1.6
        extrude(amount=1.6, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2276799454, perimeter: 4.372154496
            with BuildLine():
                CenterArc((-5.4499923969, -1.3000274167), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.4499923969, -1.3000274167), 0.29585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2749748792, perimeter: 1.8588803731
            with Locations((-5.4499923969, -1.3000274167)):
                Circle(0.29585)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2749748792, perimeter: 1.8588803731
            with Locations((-5.4499923969, -1.3000274167)):
                Circle(0.29585)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7, perimeter: 5.4
            with BuildLine():
                Line((4.8, -0.5), (4.8, 0.5))
                Line((4.8, -0.5), (6.5, -0.5))
                Line((6.5, -0.5), (6.5, 0.5))
                Line((6.5, 0.5), (4.8, 0.5))
            make_face()
            # Profile area: 1.9, perimeter: 5.8
            with BuildLine():
                Line((4.8, 0.5), (2.9, 0.5))
                Line((2.9, 0.5), (2.9, 0))
                Line((2.9, 0), (2.9, -0.5))
                Line((2.9, -0.5), (4.8, -0.5))
                Line((4.8, -0.5), (4.8, 0.5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((-1.95, 0)):
                Circle(0.9)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


def model_37846_cde34fcd_0037():
    """Model: Prowadnica lewa v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8979333698, perimeter: 5.6891792805
            with BuildLine():
                Line((0, 0), (0.7000000104, 0))
                Line((0.7000000104, 0), (0.7000000104, 0.2))
                Line((0.7000000104, 0.2), (1.3, 1.0568887891))
                Line((1.3, 1.75), (1.3, 1.0568887891))
                Line((0, 1.75), (1.3, 1.75))
                Line((0, 0), (0, 1.75))
            make_face()
        # OneSide extrude, distance=6.2
        extrude(amount=6.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.87, -0.8)):
                Circle(0.1)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.35, 5.1)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.35, 1.15)):
                Circle(0.3)
        # OneSide extrude, distance=-1.33
        extrude(amount=-1.33, mode=Mode.SUBTRACT)
    return part.part


def model_37846_cde34fcd_0052():
    """Model: Prowadnica prawa v14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8979333588, perimeter: 5.6891792733
            with BuildLine():
                Line((-0.7, 0), (0, 0))
                Line((0, 0), (0, 1.75))
                Line((0, 1.75), (-1.3, 1.75))
                Line((-1.3, 1.75), (-1.3, 1.056888804))
                Line((-1.3, 1.056888804), (-0.7, 0.2))
                Line((-0.7, 0.2), (-0.7, 0))
            make_face()
        # OneSide extrude, distance=6.2
        extrude(amount=6.2)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.6244247719, perimeter: 4.4053096491
            with BuildLine():
                CenterArc((0.35, 2), 0.16, 179.9999020518, 180.0001958513)
                Line((0.51, 2.0000002734), (0.51, 3.7))
                CenterArc((0.35, 3.7), 0.16, 0, 180)
                Line((0.19, 2.0000002735), (0.19, 3.7))
            make_face()
        # OneSide extrude, distance=-0.32
        extrude(amount=-0.32, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.35, 5.1)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.35, 1.15)):
                Circle(0.3)
        # OneSide extrude, distance=-1.33
        extrude(amount=-1.33, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.534561625, perimeter: 2.5918139392
            with Locations((1.1, 2.2)):
                Circle(0.4125)
            # Profile area: 0.534561625, perimeter: 2.5918139392
            with Locations((1.1, 4.1)):
                Circle(0.4125)
        # OneSide extrude, distance=-0.13
        extrude(amount=-0.13, mode=Mode.SUBTRACT)
    return part.part


def model_38288_740bfe5a_0001():
    """Model: Center Plate v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 506.0659241069, perimeter: 143.3809697283
            with BuildLine():
                CenterArc((20.8086740691, 17.27954877), 22.16157028, 114.4659212982, 33.6053634052)
                Line((2, 29), (2, 6))
                CenterArc((-4.8073717738, 23.1885217632), 18.4874441411, -68.3943678098, 41.9154391259)
                CenterArc((19.3385235507, 11.2502004018), 8.4488094318, 111.0636066387, 42.999490229)
                CenterArc((6.2328039616, 40.333711456), 23.4690426324, -64.593282332, 34.3132681703)
                Line((26.5, 28.5), (26.5, 50.5))
                CenterArc((35.7265893135, 29.9296453646), 22.5448317844, 114.1580553024, 34.2210953968)
                CenterArc((5.3494997981, 49.5487851959), 13.6309177719, -62.5622520601, 27.6617101219)
            make_face()
            with BuildLine():
                CenterArc((14, 29), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((25, 40)):
                Circle(0.7)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((5, 20)):
                Circle(0.7)
        # OneSide extrude, distance=18
        extrude(amount=18, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.2203007329, perimeter: 14.8123910684
            with BuildLine():
                CenterArc((19.3385235507, 11.2502004018), 8.4488094318, 124.9378136378, 8.7752235227)
                Line((14.5, 18.1763155224), (14.5, 24.0250628145))
                CenterArc((14, 29), 5, -95.7391704773, 11.4783409545)
                Line((13.5, 24.0250628145), (13.5, 17.3570836954))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4892257072, perimeter: 4.9700111844
            with BuildLine():
                Line((5.8973952264, 8.1155806321), (5.0331465268, 9.341579892))
                CenterArc((-4.8073717738, 23.1885217632), 18.4874441411, -54.6177206982, 3.1009996062)
                Line((5.8504793667, 9.9177456917), (6.6971098703, 8.7167391166))
                Line((5.0331465268, 9.341579892), (5.8504793667, 9.9177456917))
            make_face()
            # Profile area: 1.4761884512, perimeter: 4.9468164893
            with BuildLine():
                Line((20.2255473485, 23.3205712555), (21.0502374207, 22.1337216821))
                Line((19.4043359276, 22.7499472092), (20.2255473485, 23.3205712555))
                Line((20.2602719971, 21.5181300779), (19.4043359276, 22.7499472092))
                CenterArc((6.2328039616, 40.333711456), 23.4690426324, -53.2945860121, 2.4451771845)
            make_face()
            # Profile area: 1.1690398597, perimeter: 4.5318971812
            with BuildLine():
                Line((24.2354522516, 26.3401332611), (24.4556778666, 25.5444305835))
                Line((23.2716839786, 26.0733923457), (24.2354522516, 26.3401332611))
                Line((23.6717953517, 24.6277399362), (23.2716839786, 26.0733923457))
                CenterArc((6.2328039616, 40.333711456), 23.4690426324, -42.0069543384, 2.9449352279)
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.SUBTRACT)
    return part.part


def model_38926_1eaf0b52_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            Circle(7.5)
        # Symmetric extrude, each_side=7
        extrude(amount=7, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9917072884, perimeter: 5.99067774
            with BuildLine():
                Line((8.3000000045, 7), (6, 7))
                CenterArc((6, 5.4846152416), 1.5153847584, 8.1712414909, 81.8287585091)
                Line((7.5000001118, 5.7000000849), (8.3000000045, 7))
            make_face()
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)

        # Sketch15 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 109.3588402715, perimeter: 37.0707933124
            Circle(5.9)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_39109_816b707e_0004():
    """Model: kostka v3 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.04, perimeter: 0.8
            with BuildLine():
                Line((-3.8, 2.3), (-4, 2.3))
                Line((-3.8, 2.5), (-3.8, 2.3))
                Line((-4, 2.5), (-3.8, 2.5))
                Line((-4, 2.3), (-4, 2.5))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.03, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((3.8999999128, -2.3999999464)):
                Circle(0.025)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.03, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.006, perimeter: 0.46
            with BuildLine():
                Line((4, -2.47), (4, -2.5))
                Line((3.8, -2.47), (4, -2.47))
                Line((3.8, -2.5), (3.8, -2.47))
                Line((4, -2.5), (3.8, -2.5))
            make_face()
            # Profile area: 0.006, perimeter: 0.46
            with BuildLine():
                Line((3.8, -2.33), (4, -2.33))
                Line((4, -2.33), (4, -2.3))
                Line((4, -2.3), (3.8, -2.3))
                Line((3.8, -2.3), (3.8, -2.33))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -2.47), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0003141593, perimeter: 0.0628318517
            with Locations((-3.8999999128, 0.1299999971)):
                Circle(0.0099999998)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -2.47), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0003141593, perimeter: 0.0628318517
            with Locations((-3.8999999128, 0.1299999971)):
                Circle(0.0099999998)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


def model_39306_ee445998_0001():
    """Model: Slide v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5139903264, perimeter: 15.1423981062
            with BuildLine():
                CenterArc((-0.3500000052, 1.4999518782), 0.3500000052, 0, 180)
                Line((-0.7000000104, -1.5000000224), (-0.7000000104, 1.4999518782))
                CenterArc((-0.3500000052, -1.4999999665), 0.3500000052, -179.9999908524, 179.9999908842)
                Line((0, 1.4999518782), (0, -1.4999999663))
            make_face()
            with BuildLine():
                Line((-0.200000003, 1.5004508359), (-0.200000003, -1.5000000224))
                CenterArc((-0.3500000052, -1.5000000224), 0.1500000022, -180, 180)
                Line((-0.5000000075, 1.5004508359), (-0.5000000075, -1.5000000224))
                CenterArc((-0.3500000052, 1.5004508359), 0.1500000022, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.7000000104, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0942477767, perimeter: 1.8849555919
            with BuildLine():
                CenterArc((0.200000003, 0), 0.1999999985, -0.0039814908, 180.0039814908)
                CenterArc((0.200000003, 0), 0.1999999985, -180, 179.9960185092)
            make_face()
            with BuildLine():
                CenterArc((0.200000003, 0), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0942477824, perimeter: 1.8849556202
            with BuildLine():
                CenterArc((-0.200000003, 0), 0.200000003, 0, 179.9919238931)
                CenterArc((-0.200000003, 0), 0.200000003, 179.9919238931, 180.0080761069)
            make_face()
            with BuildLine():
                CenterArc((-0.200000003, 0), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0300000182, perimeter: 0.8000001125
            with BuildLine():
                Line((-0.3499999922, 1.7500000261), (-0.3499999922, 1.6499999631))
                Line((-0.3499999922, 1.6499999631), (-0.0499999989, 1.6499999631))
                Line((-0.0499999989, 1.6499999631), (-0.0499999989, 1.7500000261))
                Line((-0.0499999989, 1.7500000261), (-0.3499999922, 1.7500000261))
            make_face()
        # OneSide extrude, distance=-0.74
        extrude(amount=-0.74, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.030000018, perimeter: 0.8000001088
            with BuildLine():
                Line((-0.3499999922, -1.6499999631), (-0.3499999922, -1.7500000261))
                Line((-0.3499999922, -1.7500000261), (-0.0500000007, -1.7500000261))
                Line((-0.0500000007, -1.7500000261), (-0.0500000007, -1.6499999631))
                Line((-0.0500000007, -1.6499999631), (-0.3499999922, -1.6499999631))
            make_face()
        # OneSide extrude, distance=-0.88
        extrude(amount=-0.88, mode=Mode.SUBTRACT)
    return part.part


def model_39390_61cd2601_0000():
    """Model: Clamp Tee"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4784433753, perimeter: 2.835638898
            with BuildLine():
                CenterArc((0, 0), 0.3, 90, 90)
                Line((0, 0.3), (0, 0.7311))
                Line((-0.7511, 0.7311), (0, 0.7311))
                Line((-0.7511, 0), (-0.7511, 0.7311))
                Line((-0.3, 0), (-0.7511, 0))
            make_face()
            # Profile area: 0.4784433753, perimeter: 2.835638898
            with BuildLine():
                Line((0.3, 0), (0.7511, 0))
                Line((0.7511, 0), (0.7511, 0.7311))
                Line((0.7511, 0.7311), (0, 0.7311))
                Line((0, 0.3), (0, 0.7311))
                CenterArc((0, 0), 0.3, 0, 90)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.7311), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                CenterArc((0, 0.75), 0.4, 90, 180)
                Line((0, 1.15), (0, 0.35))
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                Line((0, 1.15), (0, 0.35))
                CenterArc((0, 0.75), 0.4, -90, 180)
            make_face()
        # OneSide extrude, distance=0.27
        extrude(amount=0.27, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.0011), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 0.75)):
                Circle(0.3)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.1011), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0.75), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.75), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 0.75)):
                Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_39637_ca6a9a60_0002():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.89, perimeter: 6.8
            with BuildLine():
                Line((-0.85, 0.85), (0.85, 0.85))
                Line((-0.85, -0.85), (-0.85, 0.85))
                Line((0.85, -0.85), (-0.85, -0.85))
                Line((0.85, 0.85), (0.85, -0.85))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.34, perimeter: 3.8
            with BuildLine():
                Line((0.85, -0.65), (-0.85, -0.65))
                Line((-0.85, -0.65), (-0.85, -0.85))
                Line((-0.85, -0.85), (0.85, -0.85))
                Line((0.85, -0.85), (0.85, -0.65))
            make_face()
            # Profile area: 0.34, perimeter: 3.8
            with BuildLine():
                Line((-0.85, 0.65), (-0.85, 0.85))
                Line((0.85, 0.65), (-0.85, 0.65))
                Line((0.85, 0.85), (0.85, 0.65))
                Line((-0.85, 0.85), (0.85, 0.85))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.81, perimeter: 3.6
            with BuildLine():
                Line((-0.45, 0.45), (0.45, 0.45))
                Line((-0.45, -0.45), (-0.45, 0.45))
                Line((0.45, -0.45), (-0.45, -0.45))
                Line((0.45, 0.45), (0.45, -0.45))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.45, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, -0.75)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_39637_ca6a9a60_0008():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.3101354288, perimeter: 35.5038817757
            with BuildLine():
                Line((5, 0), (10, 0))
                Line((10, 0), (10, 2))
                Line((10, 2), (9.25, 2))
                CenterArc((9.25, 3), 1, 180, 90)
                Line((8.25, 3), (8.25, 6.7))
                CenterArc((7.75, 6.7), 0.5, 0, 90)
                Line((7.75, 7.2), (5, 7.2))
                Line((5, 0), (5, 7.2))
            make_face()
            with BuildLine():
                Line((6.325, 1.4642), (6.325, 6.2984))
                CenterArc((6.575, 6.4642312395), 0.3, -33.5573097619, 247.1146195238)
                Line((6.825, 1.4642), (6.825, 6.2984))
                CenterArc((6.575, 1.4642), 0.25, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 24.3101354288, perimeter: 35.5038817757
            with BuildLine():
                Line((5, 0), (5, 7.2))
                Line((5, 7.2), (2.25, 7.2))
                CenterArc((2.25, 6.7), 0.5, 90, 90)
                Line((1.75, 3), (1.75, 6.7))
                CenterArc((0.75, 3), 1, -90, 90)
                Line((0, 2), (0.75, 2))
                Line((0, 0), (0, 2))
                Line((0, 0), (5, 0))
            make_face()
            with BuildLine():
                Line((3.175, 1.4642), (3.175, 6.2984))
                CenterArc((3.425, 6.4642312395), 0.3, -33.5573097619, 247.1146195238)
                Line((3.675, 1.4642), (3.675, 6.2984))
                CenterArc((3.425, 1.4642), 0.25, 180, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.71750784, perimeter: 43.72
            with BuildLine():
                Line((0, 0), (10, 0))
                Line((0, -2), (0, 0))
                Line((10, -2), (0, -2))
                Line((10, 0), (10, -2))
            make_face()
            with BuildLine():
                Line((0.5336, -1.4636), (9.4664, -1.4636))
                Line((0.5336, -0.5364), (0.5336, -1.4636))
                Line((9.4664, -0.5364), (0.5336, -0.5364))
                Line((9.4664, -1.4636), (9.4664, -0.5364))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5336, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.75, -1)):
                Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.78656, perimeter: 18.2656
            with BuildLine():
                Line((-0.5336, -1.85), (-9.4664, -1.85))
                Line((-0.5336, -1.85), (-0.5336, -1.65))
                Line((-0.5336, -1.65), (-9.4664, -1.65))
                Line((-9.4664, -1.85), (-9.4664, -1.65))
            make_face()
            # Profile area: 1.78656, perimeter: 18.2656
            with BuildLine():
                Line((-0.5336, -0.15), (-0.5336, -0.35))
                Line((-0.5336, -0.15), (-9.4664, -0.15))
                Line((-9.4664, -0.15), (-9.4664, -0.35))
                Line((-0.5336, -0.35), (-9.4664, -0.35))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_39793_5193d5ab_0020():
    """Model: Grill v13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.6868146219, perimeter: 17.2073470754
            with BuildLine():
                Line((1.5875, 7.4083333819), (0, 0))
                Line((0, 0), (1.905, 0))
                Line((1.905, 0), (1.905, 2.54))
                Line((1.905, 2.54), (1.5875, 2.54))
                Line((1.5875, 7.4083333819), (1.5875, 2.54))
            make_face()
        # OneSide extrude, distance=19.05
        extrude(amount=19.05)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.403225, perimeter: 3.175
            with BuildLine():
                Line((-1.5875, 0), (-1.5875, 1.27))
                Line((-1.5875, 1.27), (-1.905, 1.27))
                Line((-1.905, 1.27), (-1.905, 0))
                Line((-1.905, 0), (-1.5875, 0))
            make_face()
            # Profile area: 2.016125, perimeter: 5.715
            with BuildLine():
                Line((0, 0), (0, 1.27))
                Line((0, 1.27), (-1.5875, 1.27))
                Line((-1.5875, 0), (-1.5875, 1.27))
                Line((-1.5875, 0), (0, 0))
            make_face()
            # Profile area: 0.403225, perimeter: 3.175
            with BuildLine():
                Line((-1.5875, 17.78), (-1.5875, 19.05))
                Line((-1.5875, 19.05), (-1.905, 19.05))
                Line((-1.905, 19.05), (-1.905, 17.78))
                Line((-1.905, 17.78), (-1.5875, 17.78))
            make_face()
            # Profile area: 2.016125, perimeter: 5.715
            with BuildLine():
                Line((-1.5875, 17.78), (0, 17.78))
                Line((0, 19.05), (0, 17.78))
                Line((0, 19.05), (-1.5875, 19.05))
                Line((-1.5875, 17.78), (-1.5875, 19.05))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 27 constraints, 27 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5875, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.887075, perimeter: 24.7650134708
            with BuildLine():
                Line((-3.8074671134, 4.4720933819), (-3.8125328866, 5.4245933819))
                Line((-3.8125328866, 5.4245933819), (-15.24, 5.4245933819))
                Line((-15.24, 5.4245933819), (-15.24, 4.4720933819))
                Line((-15.24, 4.4720933819), (-3.8074671134, 4.4720933819))
            make_face()
            # Profile area: 10.887075, perimeter: 24.765
            with BuildLine():
                Line((-3.81, 2.8845933819), (-15.24, 2.8845933819))
                Line((-3.81, 3.8370933819), (-3.81, 2.8845933819))
                Line((-15.24, 3.8370933819), (-3.81, 3.8370933819))
                Line((-15.24, 2.8845933819), (-15.24, 3.8370933819))
            make_face()
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            with Locations((-2.54, 3.81)):
                Circle(0.79375)
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            with Locations((-16.51, 3.8100001216)):
                Circle(0.79375)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 27 constraints, 27 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5875, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            with Locations((-2.54, 6.2970783019)):
                Circle(0.79375)
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            with Locations((-16.51, 6.2970833819)):
                Circle(0.79375)
            # Profile area: 9.274175, perimeter: 35.56
            with BuildLine():
                Line((-15.24, 6.0595933819), (-15.24, 7.0120933819))
                Line((-15.24, 6.0595933819), (-3.81, 6.0595933819))
                Line((-3.81, 7.0120933819), (-3.81, 6.0595933819))
                Line((-15.24, 7.0120933819), (-3.81, 7.0120933819))
            make_face()
            with BuildLine():
                Line((-6.985, 6.6675), (-12.065, 6.6675))
                Line((-6.985, 6.35), (-6.985, 6.6675))
                Line((-12.065, 6.35), (-6.985, 6.35))
                Line((-12.065, 6.6675), (-12.065, 6.35))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6129, perimeter: 10.795
            with BuildLine():
                Line((-12.065, 6.6675), (-12.065, 6.35))
                Line((-12.065, 6.35), (-6.985, 6.35))
                Line((-6.985, 6.35), (-6.985, 6.6675))
                Line((-6.985, 6.6675), (-12.065, 6.6675))
            make_face()
        # OneSide extrude, distance=-0.0635
        extrude(amount=-0.0635, mode=Mode.SUBTRACT)
    return part.part


def model_40070_be9c502b_0064():
    """Model: obramowka na okno v5 (11)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0050158298, perimeter: 0.3009731343
            with BuildLine():
                Line((1.9397164738, 0.200000003), (1.8894443625, 0.200000003))
                CenterArc((0, 0), 1.9, 3.0169613548, 3.0253671546)
                Line((1.9474342093, 0.1000000015), (1.897366596, 0.1000000015))
                CenterArc((0, 0), 1.95, 2.9395345303, 2.9473076965)
            make_face()
            # Profile area: 0.0292986065, perimeter: 1.3456616902
            with BuildLine():
                CenterArc((0, 0), 1.95, 5.8868422267, 19.1789872849)
                Line((1.7663521691, 0.8261355909), (1.7663521691, 0.7000000104))
                CenterArc((0, 0), 1.9, 6.0423285094, 15.5759442511)
                Line((1.9397164738, 0.200000003), (1.8894443625, 0.200000003))
            make_face()
            # Profile area: 0.0254661004, perimeter: 1.2115300046
            with BuildLine():
                CenterArc((0, 0), 1.95, 25.0658295117, 12.9140435997)
                Line((1.5370426009, 1.2000000179), (1.4730919717, 1.2000000179))
                CenterArc((0, 0), 1.9, 21.6182727605, 17.5484386511)
                Line((1.7663521691, 0.8261355909), (1.7663521691, 0.7000000104))
            make_face()
            # Profile area: 0.0065795065, perimeter: 0.3949910047
            with BuildLine():
                Line((1.4534441694, 1.3000000179), (1.3856406293, 1.3000000179))
                CenterArc((0, 0), 1.9, 39.1667114116, 4.006840435)
                Line((1.5370426009, 1.2000000179), (1.4730919717, 1.2000000179))
                CenterArc((0, 0), 1.95, 37.9798731114, 3.8304424893)
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch6 -> Extrude2 (Intersect)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1649336143, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0.7000000097, 1.1065233561), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.7000000097, 1.1065233561), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.INTERSECT)
    return part.part


def model_40072_b44084ae_0000():
    """Model: gora gora v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6880252142, perimeter: 5.8119464091
            Circle(0.925)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 1.130973389, perimeter: 3.7699112405
            Circle(0.6000000089)
        # TwoSides extrude, along=0.9, against=-0.4
        extrude(amount=0.9, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1147664836, perimeter: 9.0822364886
            with BuildLine():
                CenterArc((0, 0), 0.8454828226, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6000000089, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.130973389, perimeter: 3.7699112405
            Circle(0.6000000089)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199115007, perimeter: 4.3982297525
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_40072_b44084ae_0005():
    """Model: tacka v7"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            Circle(6)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.6654860748, perimeter: 76.6548607476
            with BuildLine():
                CenterArc((0, 0), 6.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            Circle(6)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            Circle(2.25)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.SUBTRACT)
    return part.part


def model_40074_4615c9d1_0000():
    """Model: gora v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2352789589, perimeter: 24.8519807481
            with BuildLine():
                Line((1.1547005384, 2), (-1.1547005384, 2))
                Line((-1.1547005384, 2), (-2.3094010768, 0))
                Line((-2.3094010768, 0), (-1.1547005384, -2))
                Line((-1.1547005384, -2), (1.1547005384, -2))
                Line((1.1547005384, -2), (2.3094010768, 0))
                Line((2.3094010768, 0), (1.1547005384, 2))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_40159_583632c6_0003():
    """Model: felga przod v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1492258427, perimeter: 5.9690256158
            with BuildLine():
                CenterArc((-5, 2.5), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, 2.5), 0.4499999322, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5105087044, perimeter: 4.0840695743
            with BuildLine():
                CenterArc((-5, 2.5), 0.4499999322, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, 2.5), 0.1999999285, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256636163, perimeter: 1.256636612
            with Locations((-5, 2.5)):
                Circle(0.1999999285)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5105087044, perimeter: 4.0840695743
            with BuildLine():
                CenterArc((-5, 2.5), 0.4499999322, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, 2.5), 0.1999999285, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5105087044, perimeter: 4.0840695743
            with BuildLine():
                CenterArc((5, -2.5), 0.4499999322, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, -2.5), 0.1999999285, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0314158807, perimeter: 0.6283180719
            with Locations((-5, -2.5)):
                Circle(0.099999927)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_27707_13288bd1_0000": {"func": model_27707_13288bd1_0000, "volume": 6.8386974282, "area": 38.3368551518},
    "model_28119_f4fb1c4c_0003": {"func": model_28119_f4fb1c4c_0003, "volume": 111.7274118534, "area": 327.0632934809},
    "model_28287_ef6e8c9c_0000": {"func": model_28287_ef6e8c9c_0000, "volume": 9.1532779565, "area": 31.0913991492},
    "model_28455_2e9528aa_0000": {"func": model_28455_2e9528aa_0000, "volume": 302.9432180099, "area": 918.4709567127},
    "model_30034_f53308bd_0000": {"func": model_30034_f53308bd_0000, "volume": 320.5967649822, "area": 342.1139093426},
    "model_30375_4ff65965_0007": {"func": model_30375_4ff65965_0007, "volume": 332.4945652049, "area": 637.039948981},
    "model_30417_0010bc7c_0002": {"func": model_30417_0010bc7c_0002, "volume": 369.5002805598, "area": 344.0861754992},
    "model_30421_211edb5e_0001": {"func": model_30421_211edb5e_0001, "volume": 552.9203070318, "area": 376.9911184308},
    "model_30445_791b6800_0001": {"func": model_30445_791b6800_0001, "volume": 0.9417887506, "area": 8.6032127157},
    "model_30445_791b6800_0004": {"func": model_30445_791b6800_0004, "volume": 1.7293954512, "area": 10.8943765196},
    "model_30445_791b6800_0008": {"func": model_30445_791b6800_0008, "volume": 0.9464047869, "area": 7.9482294136},
    "model_30667_2511afcb_0003": {"func": model_30667_2511afcb_0003, "volume": 31.2861871918, "area": 99.4112315997},
    "model_30667_2511afcb_0005": {"func": model_30667_2511afcb_0005, "volume": 10.1826871884, "area": 33.2066343484},
    "model_30672_73fd9f76_0000": {"func": model_30672_73fd9f76_0000, "volume": 71.2817409008, "area": 147.2051738806},
    "model_30690_3df2c9e2_0011": {"func": model_30690_3df2c9e2_0011, "volume": 174.0567993795, "area": 237.5672364645},
    "model_30690_3df2c9e2_0017": {"func": model_30690_3df2c9e2_0017, "volume": 1.380516343, "area": 8.3085700909},
    "model_30809_b0bc2529_0000": {"func": model_30809_b0bc2529_0000, "volume": 0.0991511683, "area": 2.7464750573},
    "model_30904_54099e05_0003": {"func": model_30904_54099e05_0003, "volume": 15000.0951390192, "area": 4213.1620755611},
    "model_30905_511b96bf_0002": {"func": model_30905_511b96bf_0002, "volume": 84.4787405504, "area": 216.1516849831},
    "model_30905_511b96bf_0006": {"func": model_30905_511b96bf_0006, "volume": 633.4339303886, "area": 861.2873700851},
    "model_30905_511b96bf_0011": {"func": model_30905_511b96bf_0011, "volume": 495.5838103032, "area": 560.0253534612},
    "model_30905_511b96bf_0013": {"func": model_30905_511b96bf_0013, "volume": 159.4358271697, "area": 600.0441968357},
    "model_31008_8fa25b35_0009": {"func": model_31008_8fa25b35_0009, "volume": 97.7867222745, "area": 188.5868199111},
    "model_31008_8fa25b35_0011": {"func": model_31008_8fa25b35_0011, "volume": 0.434932332, "area": 6.7142198155},
    "model_31013_d34d1b29_0003": {"func": model_31013_d34d1b29_0003, "volume": 6.264120846, "area": 55.6504149301},
    "model_31016_60e3fd8e_0004": {"func": model_31016_60e3fd8e_0004, "volume": 1.202735683, "area": 18.6539600043},
    "model_31280_c8bd4b11_0004": {"func": model_31280_c8bd4b11_0004, "volume": 3.0579428091, "area": 39.5297621221},
    "model_31463_c4c75dd7_0000": {"func": model_31463_c4c75dd7_0000, "volume": 18.6085160157, "area": 77.42562075},
    "model_31463_c4c75dd7_0002": {"func": model_31463_c4c75dd7_0002, "volume": 0.1861791961, "area": 3.0776550929},
    "model_31464_b2855e3a_0000": {"func": model_31464_b2855e3a_0000, "volume": 203.6502437508, "area": 252.2965859349},
    "model_31607_9a2f8140_0000": {"func": model_31607_9a2f8140_0000, "volume": 118.0272420744, "area": 257.8916491709},
    "model_31962_e5291336_0022": {"func": model_31962_e5291336_0022, "volume": 3.2774665359, "area": 33.6935812098},
    "model_31962_e5291336_0028": {"func": model_31962_e5291336_0028, "volume": 1.4534365616, "area": 11.2333564221},
    "model_31962_e5291336_0046": {"func": model_31962_e5291336_0046, "volume": 4.9668579853, "area": 29.5152629805},
    "model_31962_e5291336_0048": {"func": model_31962_e5291336_0048, "volume": 1.6444274046, "area": 14.9422000586},
    "model_31962_e5291336_0049": {"func": model_31962_e5291336_0049, "volume": 2.6011867939, "area": 17.5082357732},
    "model_32160_661a301e_0000": {"func": model_32160_661a301e_0000, "volume": 533.8190713691, "area": 598.634235257},
    "model_32219_e5edc7ce_0043": {"func": model_32219_e5edc7ce_0043, "volume": 604.1780972451, "area": 601.2831853072},
    "model_32853_bd6998c3_0000": {"func": model_32853_bd6998c3_0000, "volume": 0.086852951, "area": 1.9825379955},
    "model_33532_e1c141b1_0000": {"func": model_33532_e1c141b1_0000, "volume": 5939.1409163544, "area": 3796.701731735},
    "model_33995_18423507_0000": {"func": model_33995_18423507_0000, "volume": 40.4426871815, "area": 77.2579989515},
    "model_34226_dbed877f_0010": {"func": model_34226_dbed877f_0010, "volume": 1744.9879528117, "area": 1995.0144622361},
    "model_34317_e9c65aa6_0021": {"func": model_34317_e9c65aa6_0021, "volume": 231, "area": 517.8924439894},
    "model_34317_e9c65aa6_0022": {"func": model_34317_e9c65aa6_0022, "volume": 6741.9878593246, "area": 4184.3288626424},
    "model_34317_e9c65aa6_0024": {"func": model_34317_e9c65aa6_0024, "volume": 3234.3748861777, "area": 2417.2747665935},
    "model_34568_fbe47bf9_0002": {"func": model_34568_fbe47bf9_0002, "volume": 0.0389981835, "area": 1.2855214891},
    "model_34568_fbe47bf9_0003": {"func": model_34568_fbe47bf9_0003, "volume": 0.0147618011, "area": 0.5093376077},
    "model_34781_4f8a4759_0006": {"func": model_34781_4f8a4759_0006, "volume": 0.4935321786, "area": 5.9290463102},
    "model_34781_4f8a4759_0013": {"func": model_34781_4f8a4759_0013, "volume": 2.4435760342, "area": 14.652414274},
    "model_34782_b461066c_0004": {"func": model_34782_b461066c_0004, "volume": 2929.6100166443, "area": 2912.5411825882},
    "model_34785_dc3b83fa_0000": {"func": model_34785_dc3b83fa_0000, "volume": 3108.6059307271, "area": 4335.3978619539},
    "model_34785_dc3b83fa_0020": {"func": model_34785_dc3b83fa_0020, "volume": 17.1891377621, "area": 62.6884663181},
    "model_34917_61633e20_0008": {"func": model_34917_61633e20_0008, "volume": 4.7870790302, "area": 54.0176444883},
    "model_36088_1ea9c8a9_0001": {"func": model_36088_1ea9c8a9_0001, "volume": 10.8, "area": 62.4},
    "model_36088_1ea9c8a9_0002": {"func": model_36088_1ea9c8a9_0002, "volume": 8.1, "area": 60.3},
    "model_36088_1ea9c8a9_0007": {"func": model_36088_1ea9c8a9_0007, "volume": 0.4296127954, "area": 4.2568580456},
    "model_37040_ecbcd25e_0033": {"func": model_37040_ecbcd25e_0033, "volume": 75.4987659776, "area": 384.6480956084},
    "model_37117_89aac9d4_0009": {"func": model_37117_89aac9d4_0009, "volume": 55.5255677798, "area": 361.2592685932},
    "model_37377_90529181_0013": {"func": model_37377_90529181_0013, "volume": 1045.6073009183, "area": 2241},
    "model_37615_8399c412_0003": {"func": model_37615_8399c412_0003, "volume": 49.000796335, "area": 144.7154095296},
    "model_37846_cde34fcd_0037": {"func": model_37846_cde34fcd_0037, "volume": 10.9993816483, "area": 44.396919419},
    "model_37846_cde34fcd_0052": {"func": model_37846_cde34fcd_0052, "volume": 10.6762875937, "area": 46.1663307993},
    "model_38288_740bfe5a_0001": {"func": model_38288_740bfe5a_0001, "volume": 492.6324085554, "area": 1155.6951436563},
    "model_38926_1eaf0b52_0000": {"func": model_38926_1eaf0b52_0000, "volume": 2464.2583794209, "area": 1026.0429379788},
    "model_39109_816b707e_0004": {"func": model_39109_816b707e_0004, "volume": 0.002934812, "area": 0.2440420352},
    "model_39306_ee445998_0001": {"func": model_39306_ee445998_0001, "volume": 0.6467937865, "area": 11.3321842523},
    "model_39390_61cd2601_0000": {"func": model_39390_61cd2601_0000, "volume": 1.6998522273, "area": 10.9369475638},
    "model_39637_ca6a9a60_0002": {"func": model_39637_ca6a9a60_0002, "volume": 2.3809756887, "area": 20.0361944902},
    "model_39637_ca6a9a60_0008": {"func": model_39637_ca6a9a60_0008, "volume": 55.6530823311, "area": 209.7577851565},
    "model_39793_5193d5ab_0020": {"func": model_39793_5193d5ab_0020, "volume": 111.8209821939, "area": 339.9101676491},
    "model_40070_be9c502b_0064": {"func": model_40070_be9c502b_0064, "volume": 0.0091567405, "area": 0.7328737069},
    "model_40072_b44084ae_0000": {"func": model_40072_b44084ae_0000, "volume": 4.3700986882, "area": 27.8232490413},
    "model_40072_b44084ae_0005": {"func": model_40072_b44084ae_0005, "volume": 121.9927551279, "area": 285.9477633297},
    "model_40074_4615c9d1_0000": {"func": model_40074_4615c9d1_0000, "volume": 23.4775339622, "area": 52.5647936692},
    "model_40159_583632c6_0003": {"func": model_40159_583632c6_0003, "volume": 0.2481858879, "area": 5.4035388305},
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
