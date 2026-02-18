"""Batch 002 - passing/04_6to7ops
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


def model_129236_61de2aec_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.6271904421, perimeter: 26.4845566751
            with BuildLine():
                Line((1.905, 0), (1.905, -6.35))
                CenterArc((0, 0), 1.905, 0, 180)
                Line((-1.905, -6.35), (-1.905, 0))
                Line((1.905, -6.35), (-1.905, -6.35))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=3.81
        extrude(amount=1.905, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.7004591398, perimeter: 9.7947340051
            with BuildLine():
                CenterArc((-6.35, 0), 1.905, 90, 180)
                Line((-6.35, -1.905), (-6.35, 1.905))
            make_face()
        # Symmetric extrude, full_length=True, total=3.81
        extrude(amount=1.905, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.58063, perimeter: 14.478
            with BuildLine():
                Line((-4.064, 0.635), (1.905, 0.635))
                Line((-4.064, 0), (-4.064, 0.635))
                Line((-4.064, -0.635), (-4.064, 0))
                Line((1.905, -0.635), (-4.064, -0.635))
                Line((1.905, 0.635), (1.905, -0.635))
            make_face()
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            with Locations((-6.35, 0)):
                Circle(0.9525)
        # Symmetric extrude, full_length=True, total=3.81
        extrude(amount=1.905, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_129412_a26d3ef5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.25, perimeter: 10
            with BuildLine():
                Line((4, -2), (0.5, -2))
                Line((4, -0.5), (4, -2))
                Line((0.5, -0.5), (4, -0.5))
                Line((0.5, -2), (0.5, -0.5))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.8000000119, 0.8000000119)):
                Circle(0.2)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 69 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0200000006, perimeter: 0.6000000089
            with BuildLine():
                Line((-1.0000000149, 1.5000000224), (-0.8000000119, 1.5000000224))
                Line((-0.8000000119, 1.5000000224), (-0.8000000119, 1.6000000238))
                Line((-0.8000000119, 1.6000000238), (-1.0000000149, 1.6000000238))
                Line((-1.0000000149, 1.6000000238), (-1.0000000149, 1.5000000224))
            make_face()
            # Profile area: 0.0200000006, perimeter: 0.6000000089
            with BuildLine():
                Line((-1.0000000149, 1.2000000179), (-1.0000000149, 1.3000000194))
                Line((-0.8000000119, 1.2000000179), (-1.0000000149, 1.2000000179))
                Line((-0.8000000119, 1.3000000194), (-0.8000000119, 1.2000000179))
                Line((-1.0000000149, 1.3000000194), (-0.8000000119, 1.3000000194))
            make_face()
            # Profile area: 0.0700000021, perimeter: 1.6000000238
            with BuildLine():
                Line((-0.8000000119, 1.3000000194), (-0.8000000119, 1.2000000179))
                Line((-0.7000000104, 1.2000000179), (-0.8000000119, 1.2000000179))
                Line((-0.7000000104, 1.9000000283), (-0.7000000104, 1.2000000179))
                Line((-0.8000000119, 1.9000000283), (-0.7000000104, 1.9000000283))
                Line((-0.8000000119, 1.6000000238), (-0.8000000119, 1.9000000283))
                Line((-0.8000000119, 1.5000000224), (-0.8000000119, 1.6000000238))
                Line((-0.8000000119, 1.3000000194), (-0.8000000119, 1.5000000224))
            make_face()
            # Profile area: 0.0471238912, perimeter: 1.1424778131
            with BuildLine():
                CenterArc((-1.0000000149, 1.4000000209), 0.1000000015, 90, 180)
                Line((-1.0000000149, 1.6000000238), (-1.0000000149, 1.5000000224))
                CenterArc((-1.0000000149, 1.4000000209), 0.200000003, 90, 180)
                Line((-1.0000000149, 1.2000000179), (-1.0000000149, 1.3000000194))
            make_face()
            # Profile area: 0.0875872968, perimeter: 1.8253993148
            with BuildLine():
                CenterArc((-1.3444440772, 1.7250000257), 0.1988584449, -61.645136412, 123.2902728241)
                Line((-1.2500000186, 1.9000000283), (-1.4000000209, 1.9000000283))
                Line((-1.4000000209, 1.9000000283), (-1.5000000224, 1.9000000283))
                Line((-1.5000000224, 1.8500000276), (-1.5000000224, 1.9000000283))
                Line((-1.4500000216, 1.8500000276), (-1.5000000224, 1.8500000276))
                Line((-1.4500000216, 1.5000000224), (-1.4500000216, 1.8500000276))
                Line((-1.4000000209, 1.5000000224), (-1.4500000216, 1.5000000224))
                Line((-1.4000000209, 1.5000000224), (-1.4000000209, 1.5500000231))
                Line((-1.2500000186, 1.5500000231), (-1.4000000209, 1.5500000231))
            make_face()
            with BuildLine():
                Line((-1.3000000194, 1.6500000246), (-1.3500000201, 1.6500000246))
                Line((-1.3500000201, 1.6500000246), (-1.3500000201, 1.8000000268))
                Line((-1.3500000201, 1.8000000268), (-1.3000000194, 1.8000000268))
                CenterArc((-1.3250000197, 1.7250000257), 0.0790569427, -71.5650511771, 143.1301023542)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0932353429, perimeter: 2.1218147233
            with BuildLine():
                Line((-1.7000000253, 1.7499999609), (-1.7000000253, 1.5000000224))
                Line((-1.7000000253, 1.5000000224), (-1.6000000238, 1.5000000224))
                Line((-1.6000000238, 1.5000000224), (-1.6000000238, 1.8000000268))
                CenterArc((-1.7993981726, 1.6374220385), 0.2572765516, 39.1918587507, 85.7664400401)
                Line((-1.9468125134, 1.8482779991), (-1.9468125134, 1.8999999575))
                Line((-1.9468125134, 1.8999999575), (-1.9999999553, 1.8999999575))
                Line((-1.9999999553, 1.8999999575), (-1.9999999553, 1.500018647))
                Line((-1.8999999575, 1.500018647), (-1.9999999553, 1.500018647))
                Line((-1.8999999575, 1.7499999609), (-1.8999999575, 1.500018647))
                CenterArc((-1.7999999914, 1.6750000259), 0.1249999339, 36.8698831317, 106.2602337366)
            make_face()
            # Profile area: 0.0869185335, perimeter: 1.8746331314
            with BuildLine():
                Line((-2.200000032, 1.2000000179), (-2.200000032, 1.7175054721))
                CenterArc((-2.1500000313, 1.2000000179), 0.0500000007, 180, 180)
                Line((-2.1000000305, 1.2000000179), (-2.1000000305, 1.819284871))
                CenterArc((-2.1901493956, 1.819284871), 0.090149365, 0, 63.5533122457)
                Line((-2.150000032, 1.9000000283), (-2.3000000343, 1.9000000283))
                CenterArc((-2.2681303445, 1.8215651825), 0.084662283, 112.112917885, 82.6440618758)
                CenterArc((-2.2976845383, 1.7175054721), 0.0976845062, 0, 122.3816072805)
            make_face()
            # Profile area: 0.0378539828, perimeter: 0.914159279
            with BuildLine():
                CenterArc((-2.5000000373, 1.5500000231), 0.0500000007, -180, 180)
                Line((-2.4500000365, 1.5500000231), (-2.4500000365, 1.8500000276))
                CenterArc((-2.5000000373, 1.8500000276), 0.0500000007, 0, 180)
                Line((-2.550000038, 1.5500000231), (-2.550000038, 1.8500000276))
            make_face()
            # Profile area: 0.0078539819, perimeter: 0.31415927
            with Locations((-2.5000000373, 1.4000000209)):
                Circle(0.0500000007)
            # Profile area: 0.0909669661, perimeter: 1.9954714432
            with BuildLine():
                Line((-2.6500000395, 1.5000000224), (-2.6500000395, 1.8000000268))
                CenterArc((-2.8500000425, 1.6500000246), 0.2500000037, 36.8698976458, 90)
                CenterArc((-2.8500000425, 1.6500000246), 0.2500000037, 126.8698976458, 16.2602047083)
                Line((-3.0500000454, 1.5000000224), (-3.0500000454, 1.8000000268))
                Line((-2.950000044, 1.5000000224), (-3.0500000454, 1.5000000224))
                Line((-2.950000044, 1.5000000224), (-2.950000044, 1.7500000261))
                CenterArc((-2.8500000425, 1.675000025), 0.1250000019, 36.8698976458, 106.2602047083)
                Line((-2.750000041, 1.5000000224), (-2.750000041, 1.7500000261))
                Line((-2.6500000395, 1.5000000224), (-2.750000041, 1.5000000224))
            make_face()
            # Profile area: 0.0036314342, perimeter: 0.2709485313
            with BuildLine():
                Line((-3.0000000447, 1.9000000283), (-3.0000000447, 1.8500000276))
                Line((-3.0500000454, 1.9000000283), (-3.0000000447, 1.9000000283))
                Line((-3.0500000454, 1.8000000268), (-3.0500000454, 1.9000000283))
                CenterArc((-2.8500000425, 1.6500000246), 0.2500000037, 126.8698976458, 16.2602047083)
            make_face()
            # Profile area: 0.0757487363, perimeter: 1.7467944759
            with BuildLine():
                Line((-3.2499999254, 1.5999325452), (-3.3700001601, 1.5999325452))
                CenterArc((-3.3699999247, 1.5499662559), 0.0499662894, 90.0002699211, 179.9997300792)
                Line((-3.2749999268, 1.4999999665), (-3.3699999247, 1.4999999665))
                CenterArc((-3.2749999268, 1.6250000743), 0.1250001078, -90, 180.0001048579)
                Line((-3.3000069318, 1.750000182), (-3.2750001556, 1.750000182))
                CenterArc((-3.3000069318, 1.7750000714), 0.0249998893, 89.9839444565, 180.0160555434)
                Line((-3.1999999285, 1.7999999598), (-3.2999999262, 1.7999999598))
                CenterArc((-3.1999999285, 1.8499999586), 0.0499999989, -90, 180)
                Line((-3.1999999285, 1.8999999575), (-3.3000716447, 1.8999999575))
                CenterArc((-3.3000716447, 1.7749662514), 0.1250337061, 90, 180)
                Line((-3.2499999254, 1.6499325452), (-3.3000716447, 1.6499325452))
                CenterArc((-3.2499999254, 1.6249325452), 0.025, -90.0000000122, 180)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_129422_621d0a90_0008():
    """Model: break calliper v0 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 201.0619298297, perimeter: 50.2654824574
            Circle(8)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)
    return part.part


def model_129428_edce5555_0001():
    """Model: articulated rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7567475535, perimeter: 12.252211349
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=2.8
        extrude(amount=1.4, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0972340804, perimeter: 18.5353966562
            with BuildLine():
                CenterArc((17.8, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.8, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=4.2
        extrude(amount=2.1, both=True)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 34 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.2466311721, perimeter: 67.5440919828
            with BuildLine():
                CenterArc((0, 0), 1.2, -65.1179557766, 130.2359115532)
                CenterArc((1.3598352602, -2.9319198914), 2.0319198914, 90, 24.8820442234)
                Line((15.2962630264, -0.9), (1.3598352602, -0.9))
                CenterArc((15.2962630264, -3.3), 2.4, 55.7911611379, 34.2088388621)
                CenterArc((17.8, 0), 1.75, -180, 48.7249344039)
                Line((16.05, 0), (15.8998749234, 0))
                CenterArc((15.4, -0.0111830676), 0.5, -90, 91.2815920157)
                Line((15.4, -0.5111830676), (2.4, -0.5111830676))
                CenterArc((2.4, -0.0111830676), 0.5, 178.7184079843, 91.2815920157)
                CenterArc((2.4, 0.0111830676), 0.5, 90, 91.2815920157)
                Line((15.4, 0.5111830676), (2.4, 0.5111830676))
                CenterArc((15.4, 0.0111830676), 0.5, -1.2815920157, 91.2815920157)
                CenterArc((17.8, 0), 1.75, 131.275065596, 48.724934404)
                CenterArc((15.2962630264, 3.3), 2.4, -90, 34.2088388621)
                Line((15.2962630264, 0.9), (15.100000225, 0.9))
                Line((15.100000225, 0.9), (1.3598352602, 0.9))
                CenterArc((1.3598352602, 2.9319198914), 2.0319198914, -114.8820442234, 24.8820442234)
            make_face()
            # Profile area: 14.0985221908, perimeter: 29.1863286543
            with BuildLine():
                CenterArc((15.4, 0.0111830676), 0.5, -1.2815920157, 91.2815920157)
                Line((15.4, 0.5111830676), (2.4, 0.5111830676))
                CenterArc((2.4, 0.0111830676), 0.5, 90, 91.2815920157)
                CenterArc((2.4, -0.0111830676), 0.5, 178.7184079843, 91.2815920157)
                Line((15.4, -0.5111830676), (2.4, -0.5111830676))
                CenterArc((15.4, -0.0111830676), 0.5, -90, 91.2815920157)
            make_face()
        # Symmetric extrude, full_length=True, total=1.8
        extrude(amount=0.9, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 34 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 14.0985221908, perimeter: 29.1863286543
            with BuildLine():
                CenterArc((15.4, 0.0111830676), 0.5, -1.2815920157, 91.2815920157)
                Line((15.4, 0.5111830676), (2.4, 0.5111830676))
                CenterArc((2.4, 0.0111830676), 0.5, 90, 91.2815920157)
                CenterArc((2.4, -0.0111830676), 0.5, 178.7184079843, 91.2815920157)
                Line((15.4, -0.5111830676), (2.4, -0.5111830676))
                CenterArc((15.4, -0.0111830676), 0.5, -90, 91.2815920157)
            make_face()
        # TwoSides offset extrude, full=2.5411, trim=0.25
        extrude(amount=2.5411, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=0.25, mode=Mode.ADD)
    return part.part


def model_129579_5b9f3a25_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.25, perimeter: 38
            with BuildLine():
                Line((15.3402268012, -1.1455887998), (15.3402268012, 1.3544112002))
                Line((14.3402268012, 1.3544112002), (15.3402268012, 1.3544112002))
                Line((14.3402268012, 4.3544112002), (14.3402268012, 1.3544112002))
                Line((14.3402268012, 4.3544112002), (12.3402268012, 4.3544112002))
                Line((12.3402268012, 4.3544112002), (12.3402268012, 3.3544112002))
                Line((12.3402268012, 3.3544112002), (9.8402268012, 3.3544112002))
                Line((9.8402268012, 3.3544112002), (9.8402268012, 4.3544112002))
                Line((9.8402268012, 4.3544112002), (7.8402268012, 4.3544112002))
                Line((7.8402268012, 4.3544112002), (7.8402268012, 1.3544112002))
                Line((7.8402268012, 1.3544112002), (6.8402268012, 1.3544112002))
                Line((6.8402268012, 1.3544112002), (6.8402268012, -1.1455887998))
                Line((7.8402268012, -1.1455887998), (6.8402268012, -1.1455887998))
                Line((7.8402268012, -4.1455887998), (7.8402268012, -1.1455887998))
                Line((9.8402268012, -4.1455887998), (7.8402268012, -4.1455887998))
                Line((9.8402268012, -3.1455887998), (9.8402268012, -4.1455887998))
                Line((12.3402268012, -3.1455887998), (9.8402268012, -3.1455887998))
                Line((12.3402268012, -4.1455887998), (12.3402268012, -3.1455887998))
                Line((14.3402268012, -4.1455887998), (12.3402268012, -4.1455887998))
                Line((14.3402268012, -4.1455887998), (14.3402268012, -1.1455887998))
                Line((14.3402268012, -1.1455887998), (15.3402268012, -1.1455887998))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch8 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.45, perimeter: 8.4
            with BuildLine():
                Line((-12.8402268012, 1.6455887998), (-12.1402268012, 1.6455887998))
                Line((-12.8402268012, -1.8544112002), (-12.8402268012, 1.6455887998))
                Line((-12.1402268012, -1.8544112002), (-12.8402268012, -1.8544112002))
                Line((-12.1402268012, 1.6455887998), (-12.1402268012, -1.8544112002))
            make_face()
            # Profile area: 2.45, perimeter: 8.4
            with BuildLine():
                Line((-11.4402268012, 1.6455887998), (-10.7402268012, 1.6455887998))
                Line((-11.4402268012, -1.8544112002), (-11.4402268012, 1.6455887998))
                Line((-10.7402268012, -1.8544112002), (-11.4402268012, -1.8544112002))
                Line((-10.7402268012, 1.6455887998), (-10.7402268012, -1.8544112002))
            make_face()
            # Profile area: 2.45, perimeter: 8.4
            with BuildLine():
                Line((-10.0402268012, 1.6455887998), (-9.3402268012, 1.6455887998))
                Line((-10.0402268012, -1.8544112002), (-10.0402268012, 1.6455887998))
                Line((-9.3402268012, -1.8544112002), (-10.0402268012, -1.8544112002))
                Line((-9.3402268012, 1.6455887998), (-9.3402268012, -1.8544112002))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_129579_c747a9a1_0000():
    """Model: fan holder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.4, perimeter: 52
            with BuildLine():
                Line((-3.45, 3.45), (3.45, 3.45))
                Line((-3.45, -3.45), (-3.45, 3.45))
                Line((3.45, -3.45), (-3.45, -3.45))
                Line((3.45, 3.45), (3.45, -3.45))
            make_face()
            with BuildLine():
                Line((-3.05, -3.05), (-3.05, -1.05))
                Line((-3.05, -1.05), (-3.05, 0))
                Line((-3.05, 0), (-3.05, 1.05))
                Line((-3.05, 1.05), (-3.05, 3.05))
                Line((-3.05, 3.05), (-1.05, 3.05))
                Line((-1.05, 3.05), (0, 3.05))
                Line((0, 3.05), (1.05, 3.05))
                Line((1.05, 3.05), (3.05, 3.05))
                Line((3.05, 3.05), (3.05, 1.05))
                Line((3.05, 1.05), (3.05, 0))
                Line((3.05, 0), (3.05, -1.05))
                Line((3.05, -1.05), (3.05, -3.05))
                Line((3.05, -3.05), (1.05, -3.05))
                Line((1.05, -3.05), (0, -3.05))
                Line((0, -3.05), (-1.05, -3.05))
                Line((-1.05, -3.05), (-3.05, -3.05))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8036504592, perimeter: 8.3992234515
            with BuildLine():
                Line((-3.05, 1.05), (-1.05, 3.05))
                Line((-3.05, 3.05), (-1.05, 3.05))
                Line((-3.05, 1.05), (-3.05, 3.05))
            make_face()
            with BuildLine():
                CenterArc((-2.5, 2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.8036504592, perimeter: 8.3992234515
            with BuildLine():
                Line((3.05, 1.05), (1.05, 3.05))
                Line((3.05, 3.05), (3.05, 1.05))
                Line((1.05, 3.05), (3.05, 3.05))
            make_face()
            with BuildLine():
                CenterArc((2.5, 2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.8036504592, perimeter: 8.3992234515
            with BuildLine():
                Line((-1.05, -3.05), (-3.05, -3.05))
                Line((-3.05, -1.05), (-1.05, -3.05))
                Line((-3.05, -3.05), (-3.05, -1.05))
            make_face()
            with BuildLine():
                CenterArc((-2.5, -2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.8036504592, perimeter: 8.3992234515
            with BuildLine():
                Line((3.05, -1.05), (1.05, -3.05))
                Line((3.05, -3.05), (1.05, -3.05))
                Line((3.05, -1.05), (3.05, -3.05))
            make_face()
            with BuildLine():
                CenterArc((2.5, -2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.45), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.98, perimeter: 4.2000000417
            with BuildLine():
                Line((0.35, 1.4000000209), (0.35, 0))
                Line((0.35, 0), (1.05, 0))
                Line((1.05, 0), (1.05, 1.4000000209))
                Line((1.05, 1.4000000209), (0.35, 1.4000000209))
            make_face()
            # Profile area: 0.9800000146, perimeter: 4.2000000417
            with BuildLine():
                Line((-1.05, 0), (-1.05, 1.4000000209))
                Line((-0.35, 0), (-1.05, 0))
                Line((-0.35, 1.4000000209), (-0.35, 0))
                Line((-1.05, 1.4000000209), (-0.35, 1.4000000209))
            make_face()
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.ADD)
    return part.part


def model_129848_0bf80366_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.7293800988, perimeter: 14.0548667765
            with BuildLine():
                CenterArc((0, 0), 1.8, 180, 180)
                Line((1.8, 0), (1.8, 2.4))
                Line((1.8, 2.4), (-1.8, 2.4))
                Line((-1.8, 0), (-1.8, 2.4))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.3483575415, perimeter: 10.8453690516
            with BuildLine():
                Line((1.8, -1.4), (-1.8, -1.4))
                CenterArc((-83.95, -93.6833333333), 123.5509454076, 47.7008353443, 0.6239043197)
                Line((0.5, -2.3), (-0.8, -2.3))
                Line((0.5, -3.5), (0.5, -2.3))
                Line((1.8, -3.5), (0.5, -3.5))
                Line((1.8, -1.4), (1.8, -3.5))
            make_face()
            # Profile area: 0.7762649548, perimeter: 4.2691957168
            with BuildLine():
                CenterArc((-83.95, -93.6833333333), 123.5509454076, 46.880384741, 0.8204506034)
                Line((0.5, -3.5), (0.5, -2.3))
                Line((0.5, -2.3), (-0.8, -2.3))
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7762649548, perimeter: 4.2691957168
            with BuildLine():
                CenterArc((-83.95, -93.6833333333), 123.5509454076, 46.880384741, 0.8204506034)
                Line((0.5, -3.5), (0.5, -2.3))
                Line((0.5, -2.3), (-0.8, -2.3))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.6, perimeter: 3.7620499352
            with BuildLine():
                Line((-2.4, 3.5), (-1.4, 2.3))
                Line((-1.4, 2.3), (-1.4, 3.5))
                Line((-1.4, 3.5), (-2.4, 3.5))
            make_face()
        # OneSide extrude, distance=3.3
        extrude(amount=3.3, mode=Mode.SUBTRACT)
    return part.part


def model_130084_a46c084c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 143.5, perimeter: 88.8828666489
            with BuildLine():
                Line((-15, 6), (-14, 4))
                Line((-14, 4), (-13, 2))
                Line((-13, 2), (-10, 1))
                Line((-10, 1), (-8, -2))
                Line((-8, -2), (0, -2))
                Line((0, -2), (5, 3))
                Line((5, 3), (26, 5))
                Line((26, 5), (25, 6))
                Line((25, 6), (-4, 5))
                Line((-4, 5), (-15, 6))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.3517687778, perimeter: 14.990189713
            with BuildLine():
                Line((6.4154759474, 2), (0.5845240526, 2))
                CenterArc((3.5, 2), 2.9154759474, -180, 180)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_130285_74b0bed5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch18 -> Extrude12 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0414914428, perimeter: 1.8892576237
            with BuildLine():
                CenterArc((11.3200001679, 1.0099999774), 0.0199999996, 90.001205968, 89.998794032)
                Line((11.3000001684, 1.0000000149), (11.3000001684, 1.0099999774))
                CenterArc((11.1833335, 1.4000000209), 0.4166666729, -73.7397952917, 73.7397952917)
                Line((11.6000001729, 1.8000000268), (11.6000001729, 1.4000000209))
                Line((11.5511333617, 1.8000000268), (11.6000001729, 1.8000000268))
                Line((11.5511333617, 1.4511213368), (11.5511333617, 1.8000000268))
                CenterArc((11.2585193944, 1.4265392455), 0.2936447054, -25.0588213863, 29.8608843237)
                Line((11.4299997445, 1.0999999754), (11.5245243334, 1.3021664772))
                CenterArc((11.3199971911, 1.1514325621), 0.1214325852, -89.998794032, 64.9399726457)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch20 -> Extrude13 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.205839912, perimeter: 1.608309865
            with Locations((11.3099997472, 1.3199999705)):
                Circle(0.255970465)
        # OneSide extrude, distance=0.31
        extrude(amount=0.31, mode=Mode.SUBTRACT)
    return part.part


def model_130572_f14489d4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 504, perimeter: 100
            with BuildLine():
                Line((0, 0), (0, 14))
                Line((0, 14), (-36, 14))
                Line((-36, 0), (-36, 14))
                Line((0, 0), (-36, 0))
            make_face()
            # Profile area: 514.5, perimeter: 101.1448230048
            with BuildLine():
                Line((0, 14), (0, 35))
                Line((0, 35), (-13, 35))
                Line((-13, 35), (-36, 14))
                Line((0, 14), (-36, 14))
            make_face()
        # OneSide extrude, distance=24
        extrude(amount=24)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 508.9380098815, perimeter: 92.5486677646
            with BuildLine():
                Line((24, -36), (24, 0))
                CenterArc((24, -18), 18, -90, 180)
            make_face()
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 36), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 209, perimeter: 63.8660687473
            with BuildLine():
                Line((24, 24), (24, 35))
                Line((24, 35), (0, 35))
                Line((0, 35), (10, 24))
                Line((24, 24), (10, 24))
            make_face()
        # OneSide extrude, distance=-23
        extrude(amount=-23, mode=Mode.SUBTRACT)
    return part.part


def model_130757_854b49f3_0000():
    """Model: Middle Block"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 37 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.9357, perimeter: 20.11
            with BuildLine():
                Line((-1.7725, 2.6330572809), (-1.7725, 2.8119427191))
                Line((-1.7725, -2.6330572809), (-1.7725, 2.6330572809))
                Line((-1.7725, -2.8119427191), (-1.7725, -2.6330572809))
                Line((-1.7725, -4.1975), (-1.7725, -2.8119427191))
                Line((-0.1125, -4.1975), (-1.7725, -4.1975))
                Line((-0.1125, 4.1975), (-0.1125, -4.1975))
                Line((-1.7725, 4.1975), (-0.1125, 4.1975))
                Line((-1.7725, 2.8119427191), (-1.7725, 4.1975))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((1.7175, -2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((1.7725, -2.6330572809), (1.7725, -2.8119427191))
            make_face()
            # Profile area: 13.8790687027, perimeter: 20.6435167079
            with BuildLine():
                Line((0.1125, -4.1975), (0.1125, 4.1975))
                Line((1.7725, -4.1975), (0.1125, -4.1975))
                Line((1.7725, -2.8119427191), (1.7725, -4.1975))
                CenterArc((1.7175, -2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((1.7725, 2.6330572809), (1.7725, -2.6330572809))
                CenterArc((1.7175, 2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((1.7725, 4.1975), (1.7725, 2.8119427191))
                Line((0.1125, 4.1975), (1.7725, 4.1975))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((1.7175, 2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((1.7725, 2.8119427191), (1.7725, 2.6330572809))
            make_face()
        # OneSide extrude, distance=0.84
        extrude(amount=0.84)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 37 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                Line((0.0894427191, -4.1975), (-0.0894427191, -4.1975))
                CenterArc((0, -4.2525), 0.105, 148.4118644948, 243.1762710104)
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((-1.8275, 2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((-1.7725, 2.6330572809), (-1.7725, 2.8119427191))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((-1.8275, -2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((-1.7725, -2.8119427191), (-1.7725, -2.6330572809))
            make_face()
        # OneSide extrude, distance=0.465
        extrude(amount=0.465, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 37 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8605593514, perimeter: 17.5067583539
            with BuildLine():
                Line((-0.0894427191, -4.1975), (-0.1125, -4.1975))
                Line((0.0894427191, -4.1975), (-0.0894427191, -4.1975))
                Line((0.1125, -4.1975), (0.0894427191, -4.1975))
                Line((0.1125, -4.1975), (0.1125, 4.1975))
                Line((0.0894427191, 4.1975), (0.1125, 4.1975))
                CenterArc((0, 4.1425), 0.105, 148.4118644948, 243.1762710104)
                Line((-0.1125, 4.1975), (-0.0894427191, 4.1975))
                Line((-0.1125, 4.1975), (-0.1125, -4.1975))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((0, 4.1425), 0.105, 148.4118644948, 243.1762710104)
                Line((-0.0894427191, 4.1975), (0.0894427191, 4.1975))
            make_face()
        # OneSide extrude, distance=0.54
        extrude(amount=0.54, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 37 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((1.7175, -2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((1.7725, -2.6330572809), (1.7725, -2.8119427191))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((1.7175, 2.7225), 0.105, 58.4118644948, 243.1762710104)
                Line((1.7725, 2.8119427191), (1.7725, 2.6330572809))
            make_face()
            # Profile area: 0.0283156486, perimeter: 0.6245292303
            with BuildLine():
                CenterArc((0, 4.1425), 0.105, 148.4118644948, 243.1762710104)
                Line((-0.0894427191, 4.1975), (0.0894427191, 4.1975))
            make_face()
        # OneSide extrude, distance=0.465
        extrude(amount=0.465, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 34 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.84), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((1.4125, -3.65), (1.5125, -3.65))
                Line((1.4125, -3.75), (1.4125, -3.65))
                Line((1.5125, -3.75), (1.4125, -3.75))
                Line((1.5125, -3.65), (1.5125, -3.75))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_130757_fc4d165e_0001():
    """Model: Casing"""
    with BuildPart() as part:
        # Base -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3, perimeter: 7.3
            with BuildLine():
                Line((-1.2, 0.625), (1.2, 0.625))
                Line((-1.2, -0.625), (-1.2, 0.625))
                Line((1.2, -0.625), (-1.2, -0.625))
                Line((1.2, 0.625), (1.2, -0.625))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Top Round Part -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 23 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3999455197, perimeter: 8.000605991
            with BuildLine():
                CenterArc((0.485, 0), 0.625, 90, 63.8961188627)
                Line((-0.115, 0.275), (-0.076248608, 0.275))
                CenterArc((-0.115, 0), 0.275, 90, 180)
                Line((-0.115, -0.275), (-0.076248608, -0.275))
                CenterArc((0.485, 0), 0.625, -153.8961188627, 63.8961188627)
                CenterArc((0.485, 0), 0.625, -90, 180)
            make_face()
            with BuildLine():
                Line((-0.115, 0.175), (-0.0099747468, 0.175))
                CenterArc((0.485, 0), 0.525, -160.5287793655, 321.057558731)
                Line((-0.115, -0.175), (-0.0099747468, -0.175))
                CenterArc((-0.115, 0), 0.175, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.39
        extrude(amount=0.39, mode=Mode.ADD)

        # Top Round Part -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 23 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9437189838, perimeter: 3.7016727521
            with BuildLine():
                CenterArc((-0.115, 0), 0.175, 90, 180)
                Line((-0.115, -0.175), (-0.0099747468, -0.175))
                CenterArc((0.485, 0), 0.525, -160.5287793655, 321.057558731)
                Line((-0.115, 0.175), (-0.0099747468, 0.175))
            make_face()
        # OneSide extrude, distance=0.44
        extrude(amount=0.44, mode=Mode.ADD)

        # Top Hole -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.64), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            with Locations((0.485, 0)):
                Circle(0.275)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_131482_e7c8b8d9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7500000056, perimeter: 5.6000000045
            with BuildLine():
                Line((-0.3000000045, -2.5000000373), (-0.3000000045, -2.200000035))
                Line((-0.3000000045, -2.200000035), (-2.8000000045, -2.200000035))
                Line((-2.8000000045, -2.200000035), (-2.8000000045, -2.5000000373))
                Line((-2.8000000045, -2.5000000373), (-0.3000000045, -2.5000000373))
            make_face()
            # Profile area: 1.5000000434, perimeter: 10.600000149
            with BuildLine():
                Line((-0.3000000045, -2.5000000373), (-0.3000000045, -4.70000007))
                Line((-0.3000000045, -4.70000007), (0, -4.70000007))
                Line((0, -4.70000007), (0, 0))
                Line((0, 0), (0, 0.3))
                Line((0, 0.3), (-0.3000000045, 0.3))
                Line((-0.3000000045, 0.3), (-0.3000000045, -2.200000035))
                Line((-0.3000000045, -2.5000000373), (-0.3000000045, -2.200000035))
            make_face()
            # Profile area: 0.9, perimeter: 6.6
            with BuildLine():
                Line((0, 0), (0, 0.3))
                Line((0, 0), (3, 0))
                Line((3, 0), (3, 0.3))
                Line((3, 0.3), (0, 0.3))
            make_face()
            # Profile area: 1.5, perimeter: 10.6
            with BuildLine():
                Line((3, 0), (3, 0.3))
                Line((3, -4.7), (3, 0))
                Line((3.3, -4.7), (3, -4.7))
                Line((3.3, -2.5000000373), (3.3, -4.7))
                Line((3.3, -2.5000000373), (3.3, -2.2))
                Line((3.3, 0.3), (3.3, -2.2))
                Line((3, 0.3), (3.3, 0.3))
            make_face()
            # Profile area: 0.7500001191, perimeter: 5.6000002474
            with BuildLine():
                Line((3.3, -2.5000000373), (3.3, -2.2))
                Line((5.8000000864, -2.5000000373), (3.3, -2.5000000373))
                Line((5.8000000864, -2.2), (5.8000000864, -2.5000000373))
                Line((3.3, -2.2), (5.8000000864, -2.2))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5000000373), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((4.5500000432, 2.0175809117)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-1.5105950923, 2.0175809117)):
                Circle(0.635)
        # TwoSides extrude, along=0.5, against=-17
        extrude(amount=0.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-17, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.3000000045, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((3.783606983, 2)):
                Circle(0.635)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_131816_9dc8a682_0000():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, 2)):
                Circle(0.8)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1441369861, perimeter: 12.252211349
            with BuildLine():
                CenterArc((10, 2), 1.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((10, 2), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, 2)):
                Circle(0.8)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, 2)):
                Circle(0.8)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, 2)):
                Circle(0.8)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.ADD)
    return part.part


def model_131816_9dc8a682_0002():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            with Locations((10, -5)):
                Circle(1.15)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((10, -5)):
                Circle(0.8)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-10, -5)):
                Circle(0.8)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)
    return part.part


def model_131922_cdc111d2_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 5.5)):
                Circle(1)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 15.1689511835
            with BuildLine():
                CenterArc((0, 5.5), 1.4142135624, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 5.5)):
                Circle(1)
        # OneSide extrude, distance=18
        extrude(amount=18, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 13.3080000382
            with BuildLine():
                CenterArc((0, 5.5), 1.1180339887, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 5.5)):
                Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_132168_3c0897d9_0001():
    """Model: Thread"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # Symmetric extrude, each_side=7.5
        extrude(amount=7.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.8168140899, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.5
        extrude(amount=0.75, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.3744467859, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_132230_997ae6e5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0271025222, perimeter: 0.6412233511
            with BuildLine():
                Line((0.1272612199, -0.0349521885), (0.1114982627, -0.0349521885))
                CenterArc((0.0663042325, 0.018399359), 0.0810070486, -41.1934749628, 82.3869499257)
                Line((0.1114982627, 0.0717509065), (0.1272612199, 0.0717509065))
                Line((0.1114982627, 0.0850887933), (0.1114982627, 0.0717509065))
                Line((0.1036167841, 0.0917577368), (0.1114982627, 0.0850887933))
                Line((-0.0255182115, 0.0917577368), (0.1036167841, 0.0917577368))
                Line((-0.0319371651, 0.0851308481), (-0.0255182115, 0.0917577368))
                Line((-0.0319371651, 0.0747634911), (-0.0319371651, 0.0851308481))
                Line((-0.0447912316, 0.0747634911), (-0.0319371651, 0.0747634911))
                CenterArc((0.0371790162, 0.0173258052), 0.1000910051, 144.9805399081, 70.0389201838)
                Line((-0.0319371651, -0.0401118807), (-0.0447912316, -0.0401118807))
                Line((-0.0319371651, -0.0507151457), (-0.0319371651, -0.0401118807))
                Line((-0.0234814676, -0.0556872754), (-0.0319371651, -0.0507151457))
                Line((0.1046223485, -0.0556872754), (-0.0234814676, -0.0556872754))
                Line((0.1114982627, -0.0507151457), (0.1046223485, -0.0556872754))
                Line((0.1114982627, -0.0349521885), (0.1114982627, -0.0507151457))
            make_face()
        # OneSide extrude, distance=0.385
        extrude(amount=0.385)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.385, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0166167513, perimeter: 0.4947613037
            with BuildLine():
                Line((-0.1229170198, -0.0416177325), (-0.1062022255, -0.0702716656))
                Line((-0.1062022255, -0.0702716656), (0.0276663834, -0.0702716656))
                Line((0.0276663834, -0.0702716656), (0.0432075685, -0.0399121413))
                Line((0.0432075685, -0.0399121413), (0.0433741432, 0.0038291627))
                Line((0.0433741432, 0.0038291627), (0.0378701996, 0.0134856351))
                Line((0.0378701996, 0.0134856351), (0.02424304, 0.0357422356))
                Line((0.02424304, 0.0357422356), (-0.1068334801, 0.0357422356))
                Line((-0.1068334801, 0.0357422356), (-0.12313157, 0.0064056739))
                Line((-0.12313157, 0.0064056739), (-0.1229170198, -0.0416177325))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_132593_191a33ed_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 98.317521601, perimeter: 37.5964594301
            with BuildLine():
                CenterArc((-3.6, -3.6), 1.4, 180, 90)
                Line((3.6, -5), (-3.6, -5))
                CenterArc((3.6, -3.6), 1.4, -90, 90)
                Line((5, 3.6), (5, -3.6))
                CenterArc((3.6, 3.6), 1.4, 0, 90)
                Line((-3.6, 5), (3.6, 5))
                CenterArc((-3.6, 3.6), 1.4, 90, 90)
                Line((-5, -3.6), (-5, 3.6))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_132605_8ae2ba54_0000():
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
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 652.795732189, perimeter: 687.1351917288
            with BuildLine():
                Line((0, 0), (103.9993789328, 0.3594184196))
                Line((103.9993789328, 0.3594184196), (103.7920221522, 60.3590601116))
                _nurbs_edge([(-0.2764757074, 79.999522256), (1.0771967452, 80.0344169671), (3.7517951511, 80.0625598653), (7.6654546091, 79.9798371738), (12.6863774536, 79.6186244071), (18.6322667326, 78.7496104289), (24.2516527381, 77.4753893082), (29.5589938498, 75.8296866614), (34.5841166962, 73.8756962035), (39.3801995127, 71.7204710101), (44.022594094, 69.5109621791), (48.5945670872, 67.4041291074), (53.1759426802, 65.5422210817), (57.8319320866, 64.0288236901), (62.5985789513, 62.8962427287), (67.4837577158, 62.1104961427), (72.4779175449, 61.5997492493), (77.5615030394, 61.2747844375), (82.7132690777, 61.0515837444), (87.9184351995, 60.8739680413), (93.1678645237, 60.7088463436), (97.3988619834, 60.5735812329), (100.5889286881, 60.4679443555), (102.7230836625, 60.3956640668), (103.7920221522, 60.3590601116)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (-0.2764757074, 79.999522256))
            make_face()
            with BuildLine():
                Line((1.8934223555, 1.9065549516), (102.0928239811, 2.2528407751))
                Line((1.8934223555, 1.9065549516), (1.6299890915, 78.1321860232))
                _nurbs_edge([(1.6299890915, 78.1321860232), (6.4803915612, 78.1738574599), (11.0510988514, 77.8780805407), (15.3443420455, 77.2525582965), (18.8688192011, 76.7390446751), (22.2057512011, 76.0021136286), (25.381243365, 75.0725265548), (28.2311969096, 74.2382369899), (30.9509836272, 73.2478345687), (33.5863769521, 72.1588739472), (36.8028262705, 70.8298174394), (39.8962144936, 69.3539559515), (42.979033889, 67.9182806048), (45.3283737888, 66.8241881712), (47.672870205, 65.7568637788), (50.0526262359, 64.799214913), (52.2794130025, 63.9031231315), (54.5376082026, 63.1053014691), (56.8354594248, 62.4397366053), (59.4411147038, 61.6850173335), (62.0962076723, 61.1005796724), (64.7887133123, 60.660584185), (68.4350419412, 60.0647198278), (72.1476845199, 59.7277881345), (75.8937791945, 59.4953936031), (79.1582464107, 59.2928775445), (82.4488095826, 59.1654087194), (85.7606530197, 59.0498079389), (89.6523563863, 58.9139669925), (93.5738043966, 58.795859214), (97.5254751811, 58.6671927375), (98.9789472606, 58.6198676587), (100.4365547122, 58.5716278764), (101.8983585115, 58.5223221394)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0140586986, 0.0140586986, 0.0140586986, 0.0140586986, 0.125, 0.125, 0.125, 0.2160756891, 0.2160756891, 0.2160756891, 0.2978146667, 0.2978146667, 0.2978146667, 0.3975755928, 0.3975755928, 0.3975755928, 0.4736009106, 0.4736009106, 0.4736009106, 0.5447393674, 0.5447393674, 0.5447393674, 0.6254070337, 0.6254070337, 0.6254070337, 0.7346513066, 0.7346513066, 0.7346513066, 0.8298502747, 0.8298502747, 0.8298502747, 0.9417173214, 0.9417173214, 0.9417173214, 0.9828633677, 0.9828633677, 0.9828633677, 0.9828633677], 3)
                Line((102.0928239811, 2.2528407751), (101.8983585115, 58.5223221394))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0065662981, 0, -1.8999886536), x_dir=(-0.9999940282, 0, 0.0034559463), z_dir=(-0.0034559463, 0, -0.9999940282))):
            # Profile area: 0.3232970098, perimeter: 4.3232970098
            with BuildLine():
                Line((-95.0000014305, 5.919175837), (-95.0000014305, 6.0808243418))
                Line((-95.0000014305, 6.0808243418), (-97.0000014305, 6.0808243418))
                Line((-97.0000014305, 6.0808243418), (-97.0000014305, 5.919175837))
                Line((-97.0000014305, 5.919175837), (-95.0000014305, 5.919175837))
            make_face()
        # Start offset: 57 (not directly supported, may affect result)
        # OneSide extrude, distance=-2
        extrude(amount=-2)
    return part.part


def model_132706_7f4c63c2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 93.22562, perimeter: 47.1728847566
            with BuildLine():
                Line((2.54, -3.8735), (0, -2.921))
                Line((17.78, -3.8735), (2.54, -3.8735))
                Line((20.32, -2.921), (17.78, -3.8735))
                Line((20.32, 0), (20.32, -2.921))
                Line((17.78, 0.9525), (20.32, 0))
                Line((2.54, 0.9525), (17.78, 0.9525))
                Line((0, 0), (2.54, 0.9525))
                Line((0, -2.921), (0, 0))
            make_face()
        # OneSide extrude, distance=2.413
        extrude(amount=2.413)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 31 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.413, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6314165626, perimeter: 5.6092150261
            with BuildLine():
                Line((-7.6217904351, 1.3335), (-6.639255747, -0.3683))
                Line((-6.639255747, -0.3683), (-5.7996950131, 1.0858618472))
                CenterArc((-5.46608, 1.4605), 0.50165, -165.3351462902, 33.6501043343)
                Line((-5.9513878636, 1.3335), (-7.6217904351, 1.3335))
            make_face()
            # Profile area: 1.6301938916, perimeter: 5.6070592594
            with BuildLine():
                CenterArc((-10.16, 1.4605), 0.50165, -48.3149580442, 33.6501043343)
                Line((-8.9871835475, -0.3676776838), (-9.8263849869, 1.0858618472))
                Line((-8.9871835475, -0.3676776838), (-8.0050081538, 1.3335))
                Line((-8.0050081538, 1.3335), (-9.6746921364, 1.3335))
            make_face()
            # Profile area: 1.6314165626, perimeter: 5.6092150261
            with BuildLine():
                CenterArc((-5.46608, 1.4605), 0.50165, -48.3149580442, 33.6501043343)
                Line((-4.292904253, -0.3683), (-5.1324649869, 1.0858618472))
                Line((-4.292904253, -0.3683), (-3.3103695649, 1.3335))
                Line((-3.3103695649, 1.3335), (-4.9807721364, 1.3335))
            make_face()
            # Profile area: 1.5843133419, perimeter: 5.7680256194
            with BuildLine():
                Line((-4.1755866783, -0.5715), (-3.0757344155, 1.3335))
                Line((-2.794, -0.5715), (-4.1755866783, -0.5715))
                Line((-2.794, 1.3335), (-2.794, -0.5715))
                Line((-2.794, 1.3335), (-3.0757344155, 1.3335))
            make_face()
            # Profile area: 1.9331797384, perimeter: 6.3388000698
            with BuildLine():
                Line((-6.7565733217, -0.5715), (-8.8695066783, -0.5715))
                Line((-7.81304, 1.2583539633), (-6.7565733217, -0.5715))
                Line((-8.8695066783, -0.5715), (-7.81304, 1.2583539633))
            make_face()
            # Profile area: 1.8825432161, perimeter: 6.0253056157
            with BuildLine():
                Line((-6.5219381723, -0.5715), (-4.4102218277, -0.5715))
                Line((-4.4102218277, -0.5715), (-5.308441349, 0.9842618472))
                CenterArc((-5.46608, 1.4605), 0.50165, -108.3149580442, 36.6299160883)
                Line((-6.5219381723, -0.5715), (-5.623718651, 0.9842618472))
            make_face()
            # Profile area: 1.8825432161, perimeter: 6.0253056157
            with BuildLine():
                CenterArc((-10.16, 1.4605), 0.50165, -108.3149580442, 36.6299160883)
                Line((-10.317638651, 0.9842618472), (-11.2158581723, -0.5715))
                Line((-11.2158581723, -0.5715), (-9.1041418277, -0.5715))
                Line((-9.1041418277, -0.5715), (-10.002361349, 0.9842618472))
            make_face()
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 30 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.413, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6321213451, perimeter: 8.1126592562
            with BuildLine():
                Line((0, 0.3797809665), (0, 1.3335))
                Line((0, 1.3335), (-2.54, 1.3335))
                Line((-2.54, -0.5727190335), (-2.54, 1.3335))
                Line((0, 0.3797809665), (-2.54, -0.5727190335))
            make_face()
            # Profile area: 3.6321213451, perimeter: 8.1126592562
            with BuildLine():
                Line((0, 1.5875), (-2.54, 1.5875))
                Line((0, 1.5875), (0, 2.5412190335))
                Line((-2.54, 3.4937190335), (0, 2.5412190335))
                Line((-2.54, 1.5875), (-2.54, 3.4937190335))
            make_face()
            # Profile area: 3.6321213451, perimeter: 8.1126592562
            with BuildLine():
                Line((-17.78, 3.4937190335), (-20.32, 2.5412190335))
                Line((-20.32, 1.5875), (-20.32, 2.5412190335))
                Line((-20.32, 1.5875), (-17.78, 1.5875))
                Line((-17.78, 1.5875), (-17.78, 3.4937190335))
            make_face()
            # Profile area: 3.6321213451, perimeter: 8.1126592562
            with BuildLine():
                Line((-20.32, 1.3335), (-17.78, 1.3335))
                Line((-20.32, 0.3797809665), (-20.32, 1.3335))
                Line((-20.32, 0.3797809665), (-17.78, -0.5727190335))
                Line((-17.78, -0.5727190335), (-17.78, 1.3335))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_132730_2ba993e9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 214.0839099187, perimeter: 51.8676947108
            Circle(8.255)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 182.4146924751, perimeter: 47.8778720407
            Circle(7.62)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 129 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15875, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0349187039, perimeter: 0.8040209305
            with BuildLine():
                Line((-4.0385969983, -4.4139242891), (-4.1655999497, -4.4195999466))
                Line((-4.1655999497, -4.4195999466), (-4.1656028422, -4.6917062834))
                Line((-4.1656028422, -4.6917062834), (-4.0385999512, -4.6917062834))
                Line((-4.0385999512, -4.6917062834), (-4.0385969983, -4.4139242891))
            make_face()
            # Profile area: 0.0375428189, perimeter: 0.8141449285
            with BuildLine():
                Line((-3.9353972769, -4.6869713124), (-3.7965453686, -4.6869713124))
                Line((-3.7965453686, -4.6869713124), (-3.7965453686, -4.4195999466))
                Line((-3.7965453686, -4.4195999466), (-3.9369999524, -4.4195999466))
                Line((-3.9369999524, -4.4195999466), (-3.9369999524, -4.6735999435))
                Line((-3.9353972769, -4.6869713124), (-3.9369999524, -4.6735999435))
            make_face()
            # Profile area: 0.3083864725, perimeter: 4.8259999417
            with BuildLine():
                Line((-2.895599965, -3.9877999518), (-3.6067999564, -3.9877999518))
                Line((-3.6067999564, -3.9877999518), (-3.6067999564, -4.14019995))
                Line((-3.6067999564, -4.14019995), (-3.0733999629, -4.14019995))
                Line((-3.0733999629, -4.14019995), (-3.0733999629, -4.3179999478))
                Line((-3.0733999629, -4.3179999478), (-3.5305999573, -4.3179999478))
                Line((-3.5305999573, -4.3179999478), (-3.5305999573, -4.4195999466))
                Line((-3.5305999573, -4.4195999466), (-3.0733999629, -4.4195999466))
                Line((-3.0733999629, -4.4195999466), (-3.0733999629, -4.5973999444))
                Line((-3.0733999629, -4.5973999444), (-3.6067999564, -4.5973999444))
                Line((-3.6067999564, -4.5973999444), (-3.6067999564, -4.6989999432))
                Line((-3.6067999564, -4.6989999432), (-2.895599965, -4.6989999432))
                Line((-2.895599965, -4.6989999432), (-2.895599965, -3.9877999518))
            make_face()
            # Profile area: 0.1974189552, perimeter: 2.895599965
            with BuildLine():
                Line((-2.3113999721, -3.9877999518), (-2.4891999699, -3.9877999518))
                Line((-2.4891999699, -3.9877999518), (-2.4891999699, -4.5719999447))
                Line((-2.4891999699, -4.5719999447), (-2.7685999665, -4.5719999447))
                Line((-2.7685999665, -4.5719999447), (-2.7685999665, -4.6989999432))
                Line((-2.7685999665, -4.6989999432), (-2.0319999754, -4.6989999432))
                Line((-2.0319999754, -4.6989999432), (-2.0319999754, -4.5719999447))
                Line((-2.0319999754, -4.5719999447), (-2.3113999721, -4.5719999447))
                Line((-2.3113999721, -4.5719999447), (-2.3113999721, -3.9877999518))
            make_face()
            # Profile area: 0.1083868774, perimeter: 1.7271999791
            with BuildLine():
                Line((-1.8795999773, -3.9877999518), (-1.8795999773, -4.6989999432))
                Line((-1.8795999773, -4.6989999432), (-1.7271999791, -4.6989999432))
                Line((-1.7271999791, -3.9877999518), (-1.7271999791, -4.6989999432))
                Line((-1.7271999791, -3.9877999518), (-1.8795999773, -3.9877999518))
            make_face()
            # Profile area: 0.3096767925, perimeter: 4.1655999497
            with BuildLine():
                Line((-1.3461999837, -3.9877999518), (-1.5239999816, -3.9877999518))
                Line((-1.5239999816, -3.9877999518), (-1.5239999816, -4.6989999432))
                Line((-1.5239999816, -4.6989999432), (-1.3461999837, -4.6989999432))
                Line((-1.3461999837, -4.6989999432), (-1.3461999837, -4.4195999466))
                Line((-1.3461999837, -4.4195999466), (-0.9651999883, -4.4195999466))
                Line((-0.9651999883, -4.4195999466), (-0.9651999883, -4.6989999432))
                Line((-0.9651999883, -4.6989999432), (-0.7619999908, -4.6989999432))
                Line((-0.7619999908, -4.6989999432), (-0.7619999908, -3.9877999518))
                Line((-0.7619999908, -3.9877999518), (-0.9651999883, -3.9877999518))
                Line((-0.9651999883, -3.9877999518), (-0.9651999883, -4.3179999478))
                Line((-1.3461999837, -4.3179999478), (-0.9651999883, -4.3179999478))
                Line((-1.3461999837, -4.3179999478), (-1.3461999837, -3.9877999518))
            make_face()
            # Profile area: 0.4260223027, perimeter: 5.5813112181
            with BuildLine():
                Line((0.3047999963, -3.9877999518), (0.5841999929, -4.6735999435))
                Line((0.1015999988, -3.9877999518), (0.3047999963, -3.9877999518))
                Line((-0.0253999997, -4.5465999451), (0.1015999988, -3.9877999518))
                Line((-0.2031999975, -3.9877999518), (-0.0253999997, -4.5465999451))
                Line((-0.3809999954, -3.9877999518), (-0.2031999975, -3.9877999518))
                Line((-0.6349999923, -4.6735999435), (-0.3809999954, -3.9877999518))
                Line((-0.4571999945, -4.6735999435), (-0.6349999923, -4.6735999435))
                Line((-0.2848239962, -4.2001279504), (-0.4571999945, -4.6735999435))
                Line((-0.1269999985, -4.6735999435), (-0.2848239962, -4.2001279504))
                Line((0.0761999991, -4.6735999435), (-0.1269999985, -4.6735999435))
                Line((0.2031999975, -4.216399949), (0.0761999991, -4.6735999435))
                Line((0.3555999957, -4.6735999435), (0.2031999975, -4.216399949))
                Line((0.5841999929, -4.6735999435), (0.3555999957, -4.6735999435))
            make_face()
            # Profile area: 0.0560491197, perimeter: 1.0403527575
            with BuildLine():
                Line((0.990599988, -4.3433999475), (0.990599988, -4.1909999494))
                Line((0.990599988, -4.1909999494), (0.6228236075, -4.1909999494))
                Line((0.6228236075, -4.3433999475), (0.6228236075, -4.1909999494))
                Line((0.6228236075, -4.3433999475), (0.990599988, -4.3433999475))
            make_face()
            # Profile area: 0.1851712216, perimeter: 3.45394868
            with BuildLine():
                Line((1.5239999816, -4.3941999469), (1.5239999816, -4.5973999444))
                Line((1.5239999816, -4.5973999444), (1.0667999871, -4.5973999444))
                Line((1.0667999871, -4.5973999444), (1.0667999871, -4.6735999435))
                Line((1.0667999871, -4.6735999435), (1.7017999794, -4.6735999435))
                Line((1.7017999794, -4.6735999435), (1.7017999794, -4.0131999515))
                Line((1.7017999794, -4.0131999515), (1.5239999816, -4.0131999515))
                Line((1.5239999816, -4.0131999515), (1.5239999816, -4.3179121979))
                Line((1.5239999816, -4.3179121979), (1.0923912856, -4.3179705732))
                Line((1.0924015956, -4.3941999469), (1.0923912856, -4.3179705732))
                Line((1.0924015956, -4.3941999469), (1.5239999816, -4.3941999469))
            make_face()
            # Profile area: 0.1703080289, perimeter: 3.4547686837
            with BuildLine():
                Line((2.5147516814, -4.0130803899), (2.3623674929, -4.0131009999))
                Line((2.3623674929, -4.0131009999), (2.3624087228, -4.3179415185))
                Line((2.3624087228, -4.3179415185), (1.9303999767, -4.3179999478))
                Line((1.9303999767, -4.3179999478), (1.9304102737, -4.3941328252))
                Line((1.9304102737, -4.3941328252), (2.3623894537, -4.3940743998))
                Line((2.3623894537, -4.3940743998), (2.3624169364, -4.5972725792))
                Line((2.3624169364, -4.5972725792), (1.8798040627, -4.5973378528))
                Line((1.8798040627, -4.5973378528), (1.8798143697, -4.6735447953))
                Line((1.8798143697, -4.6735447953), (2.5148409979, -4.6734589077))
                Line((2.5148409979, -4.6734589077), (2.5147516814, -4.0130803899))
            make_face()
            # Profile area: 0.2874482797, perimeter: 4.2194160106
            with BuildLine():
                CenterArc((3.225799961, -4.3687999472), 0.349010599, -92.1069929109, 182.0984020916)
                Line((3.0479521954, -4.0156195152), (3.225852291, -4.0197893521))
                CenterArc((3.047279071, -4.3634311696), 0.3478123058, 89.8891148774, 178.0038922117)
                Line((3.2129683505, -4.7175745851), (3.0344915165, -4.7110083243))
            make_face()
            with BuildLine():
                Line((3.2003999613, -4.5727055003), (3.0524826716, -4.5727055003))
                CenterArc((3.0860817657, -4.3446424027), 0.2305247831, 90, 171.6192606912)
                Line((3.2257327279, -4.1154980224), (3.0860817657, -4.1141176196))
                CenterArc((3.2003999613, -4.3433999475), 0.2293055528, -90, 173.6572428014)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0354837991, perimeter: 0.8127999902
            with BuildLine():
                Line((3.9115999527, -4.4195999466), (3.7845999543, -4.4195999466))
                Line((3.7845999543, -4.4195999466), (3.7845999543, -4.6989999432))
                Line((3.7845999543, -4.6989999432), (3.9115999527, -4.6989999432))
                Line((3.9115999527, -4.6989999432), (3.9115999527, -4.4195999466))
            make_face()
            # Profile area: 0.0354837991, perimeter: 0.8127999902
            with BuildLine():
                Line((4.1655999497, -4.4195999466), (4.0385999512, -4.4195999466))
                Line((4.0385999512, -4.4195999466), (4.0385999512, -4.6989999432))
                Line((4.0385999512, -4.6989999432), (4.1655999497, -4.6989999432))
                Line((4.1655999497, -4.6989999432), (4.1655999497, -4.4195999466))
            make_face()
            # Profile area: 13.8386828833, perimeter: 20.0660006404
            with BuildLine():
                Line((-4.1910001338, -3.4290001094), (-4.1910001338, -1.7780000567))
                Line((4.1910001338, -3.4290001094), (-4.1910001338, -3.4290001094))
                Line((4.1910001338, -1.7780000567), (4.1910001338, -3.4290001094))
                Line((-4.1910001338, -1.7780000567), (4.1910001338, -1.7780000567))
            make_face()
            # Profile area: 27.2561974455, perimeter: 61.5932779867
            with BuildLine():
                Line((4.1361063486, -1.4187331169), (4.1361063486, 0.8406588851))
                Line((4.1361063486, 0.8406588851), (3.1300392391, 0.8406588851))
                Line((3.1300392391, 0.8406588851), (3.1300392391, -0.1505822058))
                Line((3.1300392391, -0.1505822058), (0.7470905226, 1.6106113069))
                Line((0.7470905226, 1.6106113069), (3.1300392391, 3.3390170006))
                Line((3.1300392391, 3.3390170006), (3.1300392391, 2.3828776807))
                Line((3.1300392391, 2.3828776807), (4.1579336735, 2.3828776807))
                Line((4.1579336735, 2.3828776807), (4.1579336735, 4.6227999441))
                Line((4.1579336735, 4.6227999441), (1.0542785237, 4.6227999441))
                Line((1.0542785237, 4.6227999441), (1.0542785237, 3.9001408705))
                Line((1.0542785237, 3.9001408705), (2.413000077, 3.9001408705))
                Line((2.413000077, 3.9001408705), (0.003332023, 2.1337875523))
                Line((0.003332023, 2.1337875523), (-2.4049027178, 3.9001408705))
                Line((-2.4049027178, 3.9001408705), (-1.0560729769, 3.9001408705))
                Line((-1.0560729769, 3.9001408705), (-1.0560729769, 4.6232838253))
                Line((-1.0560729769, 4.6232838253), (-4.1688521478, 4.6232838253))
                Line((-4.1688521478, 4.6232838253), (-4.1688521478, 2.3579734079))
                Line((-4.1688521478, 2.3579734079), (-3.1717174805, 2.3579734079))
                Line((-3.1717174805, 2.3579734079), (-3.1717174805, 3.3527999595))
                Line((-3.1717174805, 3.3527999595), (-0.7549680731, 1.6061466363))
                Line((-0.7549680731, 1.6061466363), (-3.1717174805, -0.1399221978))
                Line((-3.1717174805, -0.1399221978), (-3.1717174805, 0.8488155757))
                Line((-3.1717174805, 0.8488155757), (-4.1707919463, 0.846490657))
                Line((-4.1707919463, 0.846490657), (-4.1707919463, -1.403830673))
                Line((-4.1707919463, -1.403830673), (-1.0160000324, -1.403830673))
                Line((-1.0160000324, -1.403830673), (-1.0160000324, -0.6666564442))
                Line((-1.0160000324, -0.6666564442), (-2.286000073, -0.6666564442))
                Line((-2.286000073, -0.6666564442), (-2.4201237642, -0.6666564442))
                Line((0, 1.0668000318), (-2.4201237642, -0.6666564442))
                Line((0, 1.0668000318), (2.3817050566, -0.6739045232))
                Line((2.3817050566, -0.6739045232), (1.0414000321, -0.6739045232))
                Line((1.0414000321, -1.4187331169), (1.0414000321, -0.6739045232))
                Line((1.0414000321, -1.4187331169), (4.1361063486, -1.4187331169))
            make_face()
            # Profile area: 0.0275924489, perimeter: 0.8381999899
            with BuildLine():
                Line((-4.5238201737, -3.5454875772), (-4.3079201763, -3.5454875772))
                Line((-4.3079201763, -3.5454875772), (-4.3079201763, -3.4946875778))
                Line((-4.3079201763, -3.4946875778), (-4.3639340237, -3.4946875778))
                Line((-4.3639340237, -3.4946875778), (-4.3639340237, -3.3422875797))
                Line((-4.3639340237, -3.3422875797), (-4.4730201743, -3.3422875797))
                Line((-4.4730201743, -3.3422875797), (-4.4730201743, -3.4946875778))
                Line((-4.4730201743, -3.4946875778), (-4.5238201737, -3.4946875778))
                Line((-4.5238201737, -3.4946875778), (-4.5238201737, -3.5454875772))
            make_face()
            # Profile area: 0.0510123554, perimeter: 1.5083821077
            with BuildLine():
                Line((-4.8513999414, -3.5377285447), (-4.7349406115, -3.5377285447))
                Line((-4.6886672005, -3.450560687), (-4.7349406115, -3.5377285447))
                Line((-4.6481999438, -3.5432999572), (-4.6886672005, -3.450560687))
                Line((-4.5439791843, -3.5432999572), (-4.6481999438, -3.5432999572))
                Line((-4.5439791843, -3.3366468722), (-4.5439791843, -3.5432999572))
                Line((-4.6227961992, -3.3366460343), (-4.5439791843, -3.3366468722))
                Line((-4.6227974509, -3.4544009146), (-4.6227961992, -3.3366460343))
                Line((-4.660872431, -3.3595457351), (-4.6227974509, -3.4544009146))
                Line((-4.7116742575, -3.3595457351), (-4.660872431, -3.3595457351))
                Line((-4.7635414512, -3.4632801207), (-4.7116742575, -3.3595457351))
                Line((-4.7635414512, -3.3366273371), (-4.7635414512, -3.4632801207))
                Line((-4.8513999414, -3.3366273371), (-4.7635414512, -3.3366273371))
                Line((-4.8513999414, -3.5377285447), (-4.8513999414, -3.3366273371))
            make_face()
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875, mode=Mode.SUBTRACT)
    return part.part


def model_132796_53ed101d_0005():
    """Model: paddle left"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.5504416669, perimeter: 47.7522083346
            with BuildLine():
                CenterArc((70, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((70, 0), 3.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Start offset: -5 (not directly supported, may affect result)
        # OneSide extrude, distance=-15
        extrude(amount=-15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 314.2116647884, perimeter: 71.8948886384
            with BuildLine():
                Line((-20, 66.2191211494), (-20, 66))
                Line((-20, 45.2716768302), (-20, 66))
                Line((-5, 45.2716768302), (-20, 45.2716768302))
                Line((-5, 66.2191211494), (-5, 45.2716768302))
                Line((-20, 66.2191211494), (-5, 66.2191211494))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 52 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((5, -47), (20, -47))
                Line((20, -47), (20, -46))
                Line((20, -46), (5, -46))
                Line((5, -46), (5, -47))
            make_face()
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((20, -49), (20, -48))
                Line((20, -48), (5, -48))
                Line((5, -48), (5, -49))
                Line((5, -49), (20, -49))
            make_face()
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((5, -51), (5, -50))
                Line((20, -51), (5, -51))
                Line((20, -50), (20, -51))
                Line((5, -50), (20, -50))
            make_face()
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((20, -52), (5, -52))
                Line((5, -52), (5, -53))
                Line((5, -53), (20, -53))
                Line((20, -53), (20, -52))
            make_face()
            # Profile area: 13.6299057966, perimeter: 31.8173207729
            with BuildLine():
                Line((5, -54.7428645454), (20, -54.7428645454))
                Line((5, -55.6515249318), (5, -54.7428645454))
                Line((20, -55.6515249318), (5, -55.6515249318))
                Line((20, -54.7428645454), (20, -55.6515249318))
            make_face()
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((20, -56), (5, -56))
                Line((5, -56), (5, -57))
                Line((5, -57), (20, -57))
                Line((20, -57), (20, -56))
            make_face()
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((5, -58), (20, -58))
                Line((5, -59), (5, -58))
                Line((20, -59), (5, -59))
                Line((20, -58), (20, -59))
            make_face()
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((20, -60), (5, -60))
                Line((5, -60), (5, -61))
                Line((5, -61), (20, -61))
                Line((20, -61), (20, -60))
            make_face()
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((5, -62), (20, -62))
                Line((5, -63), (5, -62))
                Line((20, -63), (5, -63))
                Line((20, -62), (20, -63))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_133211_693043d1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16900, perimeter: 520
            with BuildLine():
                Line((130, -80), (0, -80))
                Line((130, 50), (130, -80))
                Line((0, 50), (130, 50))
                Line((0, -80), (0, 50))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch5 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2994.3988088522, perimeter: 222.4956859781
            with BuildLine():
                Line((-14.3950047367, -10), (-14.3950047367, 35.6428477257))
                Line((-14.3950047367, 35.6428477257), (-80, 35.6428477257))
                Line((-80, 35.6428477257), (-80, -10))
                Line((-80, -10), (-14.3950047367, -10))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.ADD)
    return part.part


def model_134027_a6a95d00_0003():
    """Model: Slider path"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.08), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6128999516, perimeter: 5.0799999237
            with BuildLine():
                Line((-16.509999752, 3.8099999428), (-15.2399997711, 3.8099999428))
                Line((-16.509999752, 2.5399999619), (-16.509999752, 3.8099999428))
                Line((-15.2399997711, 2.5399999619), (-16.509999752, 2.5399999619))
                Line((-15.2399997711, 3.8099999428), (-15.2399997711, 2.5399999619))
            make_face()
            # Profile area: 1.6128999516, perimeter: 5.0799999237
            with BuildLine():
                Line((-25.3999996185, 2.5399999619), (-24.1299996376, 2.5399999619))
                Line((-24.1299996376, 3.8099999428), (-24.1299996376, 2.5399999619))
                Line((-25.3999996185, 3.8099999428), (-24.1299996376, 3.8099999428))
                Line((-25.3999996185, 2.5399999619), (-25.3999996185, 3.8099999428))
            make_face()
            # Profile area: 12.9031996124, perimeter: 22.8599996567
            with BuildLine():
                Line((-24.1299996376, 2.5399999619), (-16.509999752, 2.5399999619))
                Line((-25.3999996185, 2.5399999619), (-24.1299996376, 2.5399999619))
                Line((-25.3999996185, 1.2699999809), (-25.3999996185, 2.5399999619))
                Line((-15.2399997711, 1.2699999809), (-25.3999996185, 1.2699999809))
                Line((-15.2399997711, 2.5399999619), (-15.2399997711, 1.2699999809))
                Line((-15.2399997711, 2.5399999619), (-16.509999752, 2.5399999619))
            make_face()
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5399999619, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 53.2257, perimeter: 29.21
            with BuildLine():
                Line((24.1299996376, 16.51), (17.1449996376, 16.51))
                Line((17.1449996376, 16.51), (17.1449996376, 8.89))
                Line((17.1449996376, 8.89), (24.1299996376, 8.89))
                Line((24.1299996376, 8.89), (24.1299996376, 16.51))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


def model_134044_8027716b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 190.44, perimeter: 55.2
            with BuildLine():
                Line((-6.9, 6.9), (6.9, 6.9))
                Line((-6.9, -6.9), (-6.9, 6.9))
                Line((6.9, -6.9), (-6.9, -6.9))
                Line((6.9, 6.9), (6.9, -6.9))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


def model_134636_501f5634_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30, perimeter: 26
            with BuildLine():
                Line((-5, 3), (-5, 0))
                Line((-5, 0), (5, 0))
                Line((5, 0), (5, 3))
                Line((5, 3), (-5, 3))
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.3283149189, perimeter: 11.4905653643
            with BuildLine():
                Line((-5, 3), (-5, 0.7203336757))
                CenterArc((-3.462972317, 2), 2, -140.2206200517, 50.2206200517)
                CenterArc((-3.462972317, 2), 2, -90, 120)
                Line((-1.7309215094, 3), (-5, 3))
            make_face()
            # Profile area: 9.3283149189, perimeter: 11.4905653643
            with BuildLine():
                CenterArc((3.462972317, 2), 2, 150, 120.0000005833)
                CenterArc((3.462972317, 2), 2, -89.9999994167, 50.2206194685)
                Line((5, 0.7203336757), (5, 3))
                Line((5, 3), (1.7309215094, 3))
            make_face()
            # Profile area: 3.2380556954, perimeter: 12.1732948799
            with BuildLine():
                Line((5, 3), (1.7309215094, 3))
                Line((5, 0.7203336757), (5, 3))
                CenterArc((3.462972317, 2), 2, -39.7793799483, 189.7793799483)
            make_face()
            # Profile area: 3.2380556954, perimeter: 12.1732948799
            with BuildLine():
                Line((-1.7309215094, 3), (-5, 3))
                CenterArc((-3.462972317, 2), 2, 30, 189.7793799483)
                Line((-5, 3), (-5, 0.7203336757))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=183
        extrude(amount=183, mode=Mode.ADD)
    return part.part


def model_135070_b300af8d_0008():
    """Model: pin8.2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.82
        extrude(amount=0.82)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.82, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_135070_b300af8d_0016():
    """Model: pin2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.62
        extrude(amount=0.62)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.62, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_135170_4d921c0e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((0, 10), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 10))
                Line((10, 10), (0, 10))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19, perimeter: 76
            with BuildLine():
                Line((-10, -10), (0, -10))
                Line((0, -10), (0, 0))
                Line((0, 0), (-10, 0))
                Line((-10, 0), (-10, -10))
            make_face()
            with BuildLine():
                Line((-9.5, -9.5), (-0.5, -9.5))
                Line((-9.5, -0.5), (-9.5, -9.5))
                Line((-0.5, -0.5), (-9.5, -0.5))
                Line((-0.5, -9.5), (-0.5, -0.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_135846_a6116c3f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.75, perimeter: 14.4
            with BuildLine():
                Line((-4.7, 0), (0, 0))
                Line((0, 0), (0, 2.5))
                Line((0, 2.5), (-4.7, 2.5))
                Line((-4.7, 2.5), (-4.7, 0))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrusion2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.875, perimeter: 3.9
            with BuildLine():
                Line((1.25, 0.7), (1.25, 0))
                Line((0, 0.7), (1.25, 0.7))
                Line((0, 0), (0, 0.7))
                Line((1.25, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1.15
        extrude(amount=1.15, mode=Mode.ADD)

        # Sketch3 -> Extrusion3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.7, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.875, perimeter: 3.9
            with BuildLine():
                Line((-1.25, 0.7), (-1.25, 0))
                Line((-1.25, 0), (0, 0))
                Line((0, 0), (0, 0.7))
                Line((0, 0.7), (-1.25, 0.7))
            make_face()
        # OneSide extrude, distance=1.15
        extrude(amount=1.15, mode=Mode.ADD)
    return part.part


def model_135892_ab8f21bf_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.452377548, perimeter: 56.9491836536
            with BuildLine():
                Line((0, 0), (0, 11.303))
                Line((0, 11.303), (-6.5, 11.303))
                Line((-6.5, 11.303), (-6.5, 11.003))
                Line((-0.3, 11.003), (-6.5, 11.003))
                Line((-0.3, 0.3), (-0.3, 11.003))
                Line((-0.3, 0.3), (-5.2820678119, 0.3))
                Line((-5.2820678119, 0.3), (-9.2173008589, 4.235233047))
                Line((-9.4294328933, 4.0231010127), (-9.2173008589, 4.235233047))
                Line((-5.4063318806, 0), (-9.4294328933, 4.0231010127))
                Line((0, 0), (-5.4063318806, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=5
        extrude(amount=2.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11.303, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 3.914)):
                Circle(0.5)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.7031659403, 2.7031659403), x_dir=(1, 0, 0), z_dir=(0, -0.7071067812, 0.7071067812))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 7.012377949)):
                Circle(0.5)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_135892_ab8f21bf_0005():
    """Model: Spider"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-1, 1), (1, 1))
                Line((-1, -1), (-1, 1))
                Line((1, -1), (-1, -1))
                Line((1, 1), (1, -1))
            make_face()
        # Symmetric extrude, full_length=True, total=2
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_135918_fd78295e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude8 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 55 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2083072279, perimeter: 1.6179202166
            with Locations((17.2575, 0.2575)):
                Circle(0.2575)
        # OneSide extrude, distance=5.7
        extrude(amount=5.7)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 55 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.9756637061, perimeter: 20.0566370614
            with BuildLine():
                CenterArc((0.4, 0.4), 0.2, 180, 90)
                Line((0.4, 0.2), (6.1, 0.2))
                CenterArc((6.1, 0.4), 0.2, -90, 90)
                Line((6.3, 0.4), (6.3, 4.1))
                CenterArc((6.1, 4.1), 0.2, 0, 90)
                Line((6.1, 4.3), (0.4, 4.3))
                CenterArc((0.4, 4.1), 0.2, 90, 90)
                Line((0.2, 4.1), (0.2, 0.4))
            make_face()
            # Profile area: 24.9756637061, perimeter: 20.0566370614
            with BuildLine():
                CenterArc((8.9, 0.4), 0.2, 180, 90)
                Line((8.9, 0.2), (14.6, 0.2))
                CenterArc((14.6, 0.4), 0.2, -90, 90)
                Line((14.8, 0.4), (14.8, 4.1))
                CenterArc((14.6, 4.1), 0.2, 0, 90)
                Line((14.6, 4.3), (8.9, 4.3))
                CenterArc((8.9, 4.1), 0.2, 90, 90)
                Line((8.7, 4.1), (8.7, 0.4))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 55 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0370796327, perimeter: 40.7415926536
            with BuildLine():
                CenterArc((0.4, 0.4), 0.3, 180, 90)
                Line((0.4, 0.1), (6.1, 0.1))
                CenterArc((6.1, 0.4), 0.3, -90, 90)
                Line((6.4, 0.4), (6.4, 4.1))
                CenterArc((6.1, 4.1), 0.3, 0, 90)
                Line((6.1, 4.4), (0.4, 4.4))
                CenterArc((0.4, 4.1), 0.3, 90, 90)
                Line((0.1, 4.1), (0.1, 0.4))
            make_face()
            with BuildLine():
                Line((0.2, 4.1), (0.2, 0.4))
                CenterArc((0.4, 4.1), 0.2, 90, 90)
                Line((6.1, 4.3), (0.4, 4.3))
                CenterArc((6.1, 4.1), 0.2, 0, 90)
                Line((6.3, 0.4), (6.3, 4.1))
                CenterArc((6.1, 0.4), 0.2, -90, 90)
                Line((0.4, 0.2), (6.1, 0.2))
                CenterArc((0.4, 0.4), 0.2, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 55 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0999114858, perimeter: 41.998229715
            with BuildLine():
                CenterArc((0.4, 0.4), 0.4, 180, 90)
                Line((0.4, 0), (6.1, 0))
                CenterArc((6.1, 0.4), 0.4, -90, 90)
                Line((6.5, 0.4), (6.5, 4.1))
                CenterArc((6.1, 4.1), 0.4, 0, 90)
                Line((6.1, 4.5), (0.4, 4.5))
                CenterArc((0.4, 4.1), 0.4, 90, 90)
                Line((0, 4.1), (0, 0.4))
            make_face()
            with BuildLine():
                Line((0.1, 4.1), (0.1, 0.4))
                CenterArc((0.4, 4.1), 0.3, 90, 90)
                Line((6.1, 4.4), (0.4, 4.4))
                CenterArc((6.1, 4.1), 0.3, 0, 90)
                Line((6.4, 0.4), (6.4, 4.1))
                CenterArc((6.1, 0.4), 0.3, -90, 90)
                Line((0.4, 0.1), (6.1, 0.1))
                CenterArc((0.4, 0.4), 0.3, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 55 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0370796327, perimeter: 40.7415926536
            with BuildLine():
                CenterArc((8.9, 0.4), 0.3, 180, 90)
                Line((8.9, 0.1), (14.6, 0.1))
                CenterArc((14.6, 0.4), 0.3, -90, 90)
                Line((14.9, 0.4), (14.9, 4.1))
                CenterArc((14.6, 4.1), 0.3, 0, 90)
                Line((14.6, 4.4), (8.9, 4.4))
                CenterArc((8.9, 4.1), 0.3, 90, 90)
                Line((8.6, 4.1), (8.6, 0.4))
            make_face()
            with BuildLine():
                Line((8.7, 4.1), (8.7, 0.4))
                CenterArc((8.9, 4.1), 0.2, 90, 90)
                Line((14.6, 4.3), (8.9, 4.3))
                CenterArc((14.6, 4.1), 0.2, 0, 90)
                Line((14.8, 0.4), (14.8, 4.1))
                CenterArc((14.6, 0.4), 0.2, -90, 90)
                Line((8.9, 0.2), (14.6, 0.2))
                CenterArc((8.9, 0.4), 0.2, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 55 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0999114858, perimeter: 41.998229715
            with BuildLine():
                CenterArc((8.9, 4.1), 0.4, 90, 90)
                Line((8.5, 4.1), (8.5, 0.4))
                CenterArc((8.9, 0.4), 0.4, 180, 90)
                Line((8.9, 0), (14.6, 0))
                CenterArc((14.6, 0.4), 0.4, -90, 90)
                Line((15, 0.4), (15, 4.1))
                CenterArc((14.6, 4.1), 0.4, 0, 90)
                Line((14.6, 4.5), (8.9, 4.5))
            make_face()
            with BuildLine():
                Line((8.6, 4.1), (8.6, 0.4))
                CenterArc((8.9, 4.1), 0.3, 90, 90)
                Line((14.6, 4.4), (8.9, 4.4))
                CenterArc((14.6, 4.1), 0.3, 0, 90)
                Line((14.9, 0.4), (14.9, 4.1))
                CenterArc((14.6, 0.4), 0.3, -90, 90)
                Line((8.9, 0.1), (14.6, 0.1))
                CenterArc((8.9, 0.4), 0.3, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


def model_136128_30e5414b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.9, 90, 244.5512886292)
                CenterArc((0, 0), 0.9, -25.4487113708, 115.4487113708)
            make_face()
            # Profile area: 1.2960811215, perimeter: 6.8701174473
            with BuildLine():
                CenterArc((0, 0), 0.9, -25.4487113708, 115.4487113708)
                CenterArc((1.9, -0.9041666667), 1.2041666667, 90, 64.5512886292)
                Line((1.9, 0.3), (2.5, 0.3))
                Line((2.5, 0.9), (2.5, 0.3))
                Line((0, 0.9), (2.5, 0.9))
            make_face()
        # Symmetric extrude, full_length=True, total=2
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4200000125, perimeter: 3.4000000507
            with BuildLine():
                Line((-0.6000000089, 0.7000000104), (-0.3000000045, 0.7000000104))
                Line((-0.6000000089, -0.7000000104), (-0.6000000089, 0.7000000104))
                Line((-0.3000000045, -0.7000000104), (-0.6000000089, -0.7000000104))
                Line((-0.3000000045, 0.7000000104), (-0.3000000045, -0.7000000104))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_136156_c485da18_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 128.9396905257, perimeter: 47.5934457089
            with BuildLine():
                Line((22.5839280637, 10.1722864792), (7.1315106258, 10.1722864792))
                Line((22.5839280637, 18.5165918957), (22.5839280637, 10.1722864792))
                Line((7.1315106258, 18.5165918957), (22.5839280637, 18.5165918957))
                Line((7.1315106258, 10.1722864792), (7.1315106258, 18.5165918957))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11832.5757994679, perimeter: 509.5845942841
            with BuildLine():
                Line((-50, 50), (-50, -50))
                Line((-50, -50), (70, -50))
                Line((70, -50), (70, 50))
                Line((70, 50), (-50, 50))
            make_face()
            with BuildLine():
                Line((7.1315106258, 10.1722864792), (7.1315106258, 18.5165918957))
                Line((7.1315106258, 18.5165918957), (22.5839280637, 18.5165918957))
                Line((22.5839280637, 18.5165918957), (22.5839280637, 10.1722864792))
                Line((22.5839280637, 10.1722864792), (7.1315106258, 10.1722864792))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 128.9396905257, perimeter: 47.5934457089
            with BuildLine():
                Line((22.5839280637, 10.1722864792), (7.1315106258, 10.1722864792))
                Line((22.5839280637, 18.5165918957), (22.5839280637, 10.1722864792))
                Line((7.1315106258, 18.5165918957), (22.5839280637, 18.5165918957))
                Line((7.1315106258, 10.1722864792), (7.1315106258, 18.5165918957))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 115.4535300194, perimeter: 65.9734457254
            with BuildLine():
                CenterArc((0, 0), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)
    return part.part


def model_136620_b4159c31_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # TwoSides extrude, along=4.5, against=-0.5
        extrude(amount=4.5)
        extrude(sk.sketch, amount=-0.5)

        # Sketch11 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_136804_03742933_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0.5, -1), (-0.5, -1))
                Line((0.5, 1), (0.5, -1))
                Line((-0.5, 1), (0.5, 1))
                Line((-0.5, -1), (-0.5, 1))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1500000045, perimeter: 3.2000000477
            with BuildLine():
                Line((-0.400000006, 0.0500000007), (-0.0500000007, 0.0500000007))
                Line((-0.400000006, -0.0500000007), (-0.400000006, 0.0500000007))
                Line((-0.0500000007, -0.0500000007), (-0.400000006, -0.0500000007))
                Line((-0.0500000007, -0.400000006), (-0.0500000007, -0.0500000007))
                Line((0.0500000007, -0.400000006), (-0.0500000007, -0.400000006))
                Line((0.0500000007, -0.0500000007), (0.0500000007, -0.400000006))
                Line((0.400000006, -0.0500000007), (0.0500000007, -0.0500000007))
                Line((0.400000006, 0.0500000007), (0.400000006, -0.0500000007))
                Line((0.0500000007, 0.0500000007), (0.400000006, 0.0500000007))
                Line((0.0500000007, 0.400000006), (0.0500000007, 0.0500000007))
                Line((-0.0500000007, 0.400000006), (0.0500000007, 0.400000006))
                Line((-0.0500000007, 0.0500000007), (-0.0500000007, 0.400000006))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_136804_0979aba6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((1, -2), (0, -2))
                Line((1, 0), (1, -2))
                Line((0, 0), (1, 0))
                Line((0, -2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0800000024, perimeter: 1.8000000268
            with BuildLine():
                Line((-0.1000000015, 0.9500000142), (-0.9000000134, 0.9500000142))
                Line((-0.9000000134, 0.9500000142), (-0.9000000134, 0.8500000127))
                Line((-0.1000000015, 0.8500000127), (-0.9000000134, 0.8500000127))
                Line((-0.1000000015, 0.8500000127), (-0.1000000015, 0.9500000142))
            make_face()
            # Profile area: 0.0800000012, perimeter: 1.8000000238
            with BuildLine():
                Line((-0.9000000134, 1.1500000156), (-0.1000000015, 1.1500000156))
                Line((-0.9000000134, 1.0500000156), (-0.9000000134, 1.1500000156))
                Line((-0.1000000015, 1.0500000156), (-0.9000000134, 1.0500000156))
                Line((-0.1000000015, 1.1500000156), (-0.1000000015, 1.0500000156))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0.5, -1)):
                Circle(0.45)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.SUBTRACT)
    return part.part


def model_136804_629c2c23_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1371669412, perimeter: 14.5326723377
            Ellipse(3, 1.5, rotation=180)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 53 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1884955648, perimeter: 4.0169957654
            with BuildLine():
                EllipticalCenterArc((0.9000000134, 0), 0.5000000075, 0.200000003, 0, 360, 90)
            make_face()
            with BuildLine():
                EllipticalCenterArc((0.9000000134, 0), 0.400000006, 0.1000000015, 0, 360, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1946537357, perimeter: 4.2432234926
            with BuildLine():
                Line((1.7000000253, -0.5000000075), (1.9000000298, -0.1333333344))
                Line((1.9000000298, -0.1333333344), (1.9000000298, -0.5000000075))
                Line((1.9000000298, -0.5000000075), (2.0000000298, -0.5000000075))
                Line((2.0000000298, -0.5000000075), (2.0000000298, 0.5000000075))
                Line((2.0000000298, 0.5000000075), (1.9000000298, 0.5000000075))
                Line((1.9000000298, 0.5000000075), (1.9000000298, 0.0500000007))
                Line((1.7000000253, 0.5000000075), (1.9000000298, 0.0500000007))
                Line((1.6000000238, 0.5000000075), (1.7000000253, 0.5000000075))
                Line((1.6000000238, 0.5000000075), (1.847359233, -0.0465081262))
                Line((1.6000000238, -0.5000000075), (1.847359233, -0.0465081262))
                Line((1.7000000253, -0.5000000075), (1.6000000238, -0.5000000075))
            make_face()
            # Profile area: 0.2200000066, perimeter: 4.6000000685
            with BuildLine():
                Line((0.1000000015, -0.0500000007), (-0.1000000015, -0.0500000007))
                Line((0.1000000015, -0.0500000007), (0.1000000015, -0.5000000075))
                Line((0.1000000015, -0.5000000075), (0.200000003, -0.5000000075))
                Line((0.200000003, -0.5000000075), (0.200000003, 0.5000000075))
                Line((0.200000003, 0.5000000075), (0.1000000015, 0.5000000075))
                Line((0.1000000015, 0.5000000075), (0.1000000015, 0.0500000007))
                Line((-0.1000000015, 0.0500000007), (0.1000000015, 0.0500000007))
                Line((-0.1000000015, 0.5000000075), (-0.1000000015, 0.0500000007))
                Line((-0.200000003, 0.5000000075), (-0.1000000015, 0.5000000075))
                Line((-0.200000003, -0.5000000075), (-0.200000003, 0.5000000075))
                Line((-0.1000000015, -0.5000000075), (-0.200000003, -0.5000000075))
                Line((-0.1000000015, -0.0500000007), (-0.1000000015, -0.5000000075))
            make_face()
            # Profile area: 0.1900000057, perimeter: 4.0000000596
            with BuildLine():
                Line((-1.1000000164, 0.400000006), (-1.1000000164, 0.5000000075))
                Line((-0.8000000119, 0.400000006), (-1.1000000164, 0.400000006))
                Line((-0.8000000119, 0.0500000007), (-0.8000000119, 0.400000006))
                Line((-1.1000000164, 0.0500000007), (-0.8000000119, 0.0500000007))
                Line((-1.1000000164, -0.0500000007), (-1.1000000164, 0.0500000007))
                Line((-0.8000000119, -0.0500000007), (-1.1000000164, -0.0500000007))
                Line((-0.8000000119, -0.400000006), (-0.8000000119, -0.0500000007))
                Line((-1.1000000164, -0.400000006), (-0.8000000119, -0.400000006))
                Line((-1.1000000164, -0.5000000075), (-1.1000000164, -0.400000006))
                Line((-0.7000000104, -0.5000000075), (-1.1000000164, -0.5000000075))
                Line((-0.7000000104, 0.5000000075), (-0.7000000104, -0.5000000075))
                Line((-1.1000000164, 0.5000000075), (-0.7000000104, 0.5000000075))
            make_face()
            # Profile area: 0.2311068105, perimeter: 4.900000073
            with BuildLine():
                Line((-1.9389319932, 0.5000000075), (-1.9389319932, 0.6000000089))
                Line((-1.9389319932, 0.6000000089), (-2.0500000305, 0.6000000089))
                Line((-2.0500000305, 0.6000000089), (-2.0500000305, 0.5000000075))
                Line((-2.0500000305, 0.5000000075), (-2.0000000298, 0.5000000075))
                Line((-2.0000000298, -0.5000000075), (-2.0000000298, 0.5000000075))
                Line((-1.9000000283, -0.5000000075), (-2.0000000298, -0.5000000075))
                Line((-1.9000000283, 0.400000006), (-1.9000000283, -0.5000000075))
                Line((-1.7000000253, 0.400000006), (-1.9000000283, 0.400000006))
                Line((-1.7000000253, -0.5000000075), (-1.7000000253, 0.400000006))
                Line((-1.6000000238, -0.5000000075), (-1.7000000253, -0.5000000075))
                Line((-1.6000000238, 0.5000000075), (-1.6000000238, -0.5000000075))
                Line((-1.9389319932, 0.5000000075), (-1.6000000238, 0.5000000075))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_136804_72e9823d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0.5, -1), (-0.5, -1))
                Line((0.5, 1), (0.5, -1))
                Line((-0.5, 1), (0.5, 1))
                Line((-0.5, -1), (-0.5, 1))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0800000024, perimeter: 1.8000000268
            with BuildLine():
                Line((-0.400000006, 0.0500000007), (0.400000006, 0.0500000007))
                Line((-0.400000006, -0.0500000007), (-0.400000006, 0.0500000007))
                Line((0.400000006, -0.0500000007), (-0.400000006, -0.0500000007))
                Line((0.400000006, 0.0500000007), (0.400000006, -0.0500000007))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.SUBTRACT)
    return part.part


def model_136804_7a5539a3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0.5, -1), (-0.5, -1))
                Line((0.5, 1), (0.5, -1))
                Line((-0.5, 1), (0.5, 1))
                Line((-0.5, -1), (-0.5, 1))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1800000054, perimeter: 4.0626416437
            with BuildLine():
                Line((-0.3000000045, -0.9000000134), (0.400000006, 0.9000000134))
                Line((0.400000006, 0.9000000134), (0.3000000045, 0.9000000134))
                Line((0.3000000045, 0.9000000134), (-0.400000006, -0.9000000134))
                Line((-0.400000006, -0.9000000134), (-0.3000000045, -0.9000000134))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_136804_fc7723ee_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((1, -2), (0, -2))
                Line((1, 0), (1, -2))
                Line((0, 0), (1, 0))
                Line((0, -2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0650000019, perimeter: 1.5000000224
            with BuildLine():
                Line((-0.3000000045, 1.0500000156), (-0.9500000142, 1.0500000156))
                Line((-0.3000000045, 1.0500000156), (-0.3000000045, 1.1500000171))
                Line((-0.9500000142, 1.1500000171), (-0.3000000045, 1.1500000171))
                Line((-0.9500000142, 1.0500000156), (-0.9500000142, 1.1500000171))
            make_face()
            # Profile area: 0.0650000019, perimeter: 1.5000000224
            with BuildLine():
                Line((-0.3000000045, 0.8500000127), (-0.3000000045, 0.9500000142))
                Line((-0.3000000045, 0.9500000142), (-0.9500000142, 0.9500000142))
                Line((-0.9500000142, 0.9500000142), (-0.9500000142, 0.8500000127))
                Line((-0.9500000142, 0.8500000127), (-0.3000000045, 0.8500000127))
            make_face()
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.1500000022, 0.8500000127)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.1500000022, 1.1500000171)):
                Circle(0.1000000015)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0.5000000075, 1.0000000149)):
                Circle(0.45)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_136821_0f4b88d0_0003():
    """Model: Body v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 246.490869978, perimeter: 109.5979214624
            with BuildLine():
                CenterArc((0, 9.1333076528), 22, -82.1625202369, 2.6382019333)
                Line((4, -12.5), (4, 12.5))
                CenterArc((0, -9.1333076528), 22, 79.5243183036, 20.9513633928)
                Line((-4, 12.5), (-4, -12.5))
                CenterArc((0, 9.1333076528), 22, -100.4756816964, 2.6382019333)
                Line((-3, -12.6611870649), (-3, -16.5))
                Line((-3, -16.5), (-5.75, -16.5))
                Line((-5.75, -16.5), (-5.75, -19.5))
                Line((-5.75, -19.5), (5.75, -19.5))
                Line((5.75, -19.5), (5.75, -16.5))
                Line((5.75, -16.5), (3, -16.5))
                Line((3, -12.6611870649), (3, -16.5))
            make_face()
            with BuildLine():
                CenterArc((0, -7.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 7.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.1327287191, perimeter: 20.566367487
            with BuildLine():
                CenterArc((-4, 0), 4, -89.9999775967, 89.9999905841)
                CenterArc((-4, 0), 4, 0.0000129874, 89.9999646192)
                Line((-3.9999984366, 4), (-3.999998436, -4))
            make_face()
            # Profile area: 48.0000125096, perimeter: 28.0000031274
            with BuildLine():
                Line((-3.9999984366, 4), (-3.999998436, -4))
                Line((-10, 4), (-3.9999984366, 4))
                Line((-10, 4), (-10, -4))
                Line((-3.999998436, -4), (-10, -4))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.4778378192, perimeter: 10.956657481
            with BuildLine():
                Line((0, -2.2056756384), (0, 0.0000009067))
                Line((1, -2.25), (0, -2.2056756384))
                Line((1, 2.25), (1, -2.25))
                Line((0, 2.25), (1, 2.25))
                Line((0, 0.0000009067), (0, 2.25))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5.75, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((0, -19.5), (5, -19.5))
                Line((5, -19.5), (5, -16.5))
                Line((5, -16.5), (0, -16.5))
                Line((0, -19.5), (0, -16.5))
            make_face()
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((-10, -16.5), (-10, -19.5))
                Line((-10, -16.5), (-16, -16.5))
                Line((-16, -16.5), (-16, -19.5))
                Line((-16, -19.5), (-10, -19.5))
            make_face()
            # Profile area: 30, perimeter: 26
            with BuildLine():
                Line((0, -19.5), (0, -16.5))
                Line((0, -16.5), (-10, -16.5))
                Line((-10, -16.5), (-10, -19.5))
                Line((-10, -19.5), (0, -19.5))
            make_face()
        # OneSide extrude, distance=-11.5
        extrude(amount=-11.5, mode=Mode.ADD)
    return part.part


def model_136821_0f4b88d0_0004():
    """Model: Piston Road v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 189.7807844457, perimeter: 84.9390479769
            with BuildLine():
                CenterArc((0, 9.1333076528), 22, -100.4756816964, 20.9513633928)
                Line((4, -12.5), (4, 12.5))
                CenterArc((0, -9.1333076528), 22, 79.5243183036, 20.9513633928)
                Line((-4, 12.5), (-4, -12.5))
            make_face()
            with BuildLine():
                CenterArc((0, 7.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -7.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.6, perimeter: 10.6
            with BuildLine():
                Line((-3.5, -2.25), (-2.7, -2.25))
                Line((-2.7, -2.25), (-2.7, 2.25))
                Line((-2.7, 2.25), (-3.5, 2.25))
                Line((-3.5, 2.25), (-3.5, -2.25))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)
    return part.part


def model_137053_59e609b3_0003():
    """Model: Supporter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1593397861, perimeter: 8.3960173933
            with BuildLine():
                CenterArc((0, 0), 0.525, -16.601549599, 33.2030991981)
                Line((4.3968847051, -0.15), (0.5031152949, -0.15))
                CenterArc((4.9, 0), 0.525, 163.398450401, 33.2030991981)
                Line((0.5031152949, 0.15), (4.3968847051, 0.15))
            make_face()
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 0), 0.525, 16.601549599, 326.7969008019)
                CenterArc((0, 0), 0.525, -16.601549599, 33.2030991981)
            make_face()
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((4.9, 0), 0.525, -163.398450401, 326.7969008019)
                CenterArc((4.9, 0), 0.525, 163.398450401, 33.2030991981)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0530929158, perimeter: 0.8168140899
            Circle(0.13)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000067, -0.0000000278, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-4.8999999933, -0.0000000278)):
                Circle(0.225)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_137053_59e609b3_0005():
    """Model: ClutchA"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4005530633, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.5, 17.4576031237, 325.0847937526)
                CenterArc((0, 0), 0.5, -17.4576031237, 34.9152062474)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4469512894, perimeter: 3.6487621492
            with BuildLine():
                CenterArc((0, 0), 0.5, -17.4576031237, 34.9152062474)
                Line((1.9968847051, -0.15), (0.4769696007, -0.15))
                CenterArc((2.5, 0), 0.525, 163.398450401, 33.203099198)
                Line((0.4769696007, 0.15), (1.9968847051, 0.15))
            make_face()
            # Profile area: 0.5831581363, perimeter: 5.1836278784
            with BuildLine():
                CenterArc((2.5, 0), 0.525, -163.398450401, 326.796900802)
                CenterArc((2.5, 0), 0.525, 163.398450401, 33.203099198)
            make_face()
            with BuildLine():
                CenterArc((2.5, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0006359382, perimeter: 0.1039803099
            with BuildLine():
                CenterArc((0, 0), 0.35, -3.0638103827, 6.5489803111)
                CenterArc((0.3499976339, 0.0012869666), 0.02, -91.4265653049, 183.2744901556)
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3999171251, perimeter: 5.3646769327
            with BuildLine():
                CenterArc((0, 0), 0.5, -180, 162.5423968763)
                CenterArc((0, 0), 0.5, -17.4576031237, 34.9152062474)
                CenterArc((0, 0), 0.5, 17.4576031237, 162.5423968763)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 3.4851699284, 353.4510196889)
                CenterArc((0.3499976339, 0.0012869666), 0.02, -91.4265653049, 183.2744901556)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0301094258, perimeter: 8.2239114546
            with BuildLine():
                CenterArc((0, 0), 0.5, -17.4576031237, 34.9152062474)
                Line((0.4769696007, -0.15), (1.9968847051, -0.15))
                CenterArc((2.5, 0), 0.525, -163.398450401, 326.796900802)
                Line((1.9968847051, 0.15), (0.4769696007, 0.15))
            make_face()
            with BuildLine():
                CenterArc((2.5, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3854810383, perimeter: 2.2230842791
            with BuildLine():
                CenterArc((0.3499976339, 0.0012869666), 0.02, -91.4265653049, 183.2744901556)
                CenterArc((0, 0), 0.35, 3.4851699284, 353.4510196889)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_137053_59e609b3_0009():
    """Model: sg90 servo motor_gear v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1661902514, perimeter: 1.4451326207
            Circle(0.23)
        # OneSide extrude, distance=0.72
        extrude(amount=0.72)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.72), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0006167221, perimeter: 0.1011047874
            with BuildLine():
                CenterArc((0, 0), 0.23, 175.1467240329, 9.9676254759)
                CenterArc((-0.2299994031, -0.0005240077), 0.02, -87.3775568602, 175.016187262)
            make_face()
        # OneSide extrude, distance=-0.72
        extrude(amount=-0.72, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.72), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_137098_0a45d1c8_0007():
    """Model: Propeller"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_137099_58f819ec_0004():
    """Model: Stepper Motor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.04, perimeter: 30.4
            with BuildLine():
                Line((-2, 2), (2, 2))
                Line((-2, -2), (-2, 2))
                Line((2, -2), (-2, -2))
                Line((2, 2), (2, -2))
            make_face()
            with BuildLine():
                Line((1.8, 1.8), (1.8, -1.8))
                Line((1.8, -1.8), (-1.8, -1.8))
                Line((-1.8, -1.8), (-1.8, 1.8))
                Line((-1.8, 1.8), (1.8, 1.8))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 12.6772566612, perimeter: 18.1699111843
            with BuildLine():
                Line((-1.8, 1.8), (1.8, 1.8))
                Line((-1.8, -1.8), (-1.8, 1.8))
                Line((1.8, -1.8), (-1.8, -1.8))
                Line((1.8, 1.8), (1.8, -1.8))
            make_face()
            with BuildLine():
                CenterArc((1.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=4
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9040097092, perimeter: 8.0110612667
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)
    return part.part


def model_137099_58f819ec_0005():
    """Model: Nozzle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0169646003, perimeter: 1.6964600329
            with BuildLine():
                CenterArc((0, 0), 0.145, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.9339480145, perimeter: 4.9110618695
            with BuildLine():
                Line((0.5, -0.5), (0.5, 0.5))
                Line((0.5, 0.5), (-0.5, 0.5))
                Line((-0.5, 0.5), (-0.5, -0.5))
                Line((-0.5, -0.5), (0.5, -0.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0169646003, perimeter: 1.6964600329
            with BuildLine():
                CenterArc((0, 0), 0.145, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_137099_58f819ec_0010():
    """Model: Stator"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 34 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1615053451, perimeter: 30.8495559215
            with BuildLine():
                CenterArc((-1.5, 1.5), 0.5, 90, 90)
                Line((-2, -1.5), (-2, 1.5))
                CenterArc((-1.5, -1.5), 0.5, 180, 90)
                Line((1.5, -2), (-1.5, -2))
                CenterArc((1.5, -1.5), 0.5, -90, 90)
                Line((2, 1.5), (2, -1.5))
                CenterArc((1.5, 1.5), 0.5, 0, 90)
                Line((-1.5, 2), (1.5, 2))
            make_face()
            with BuildLine():
                CenterArc((1.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.8
        extrude(amount=0.4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2627714306, perimeter: 3.3992412589
            with BuildLine():
                CenterArc((0, 0), 1.9, 136.3186818283, 2.8231566541)
                Line((-1.4370296067, 1.2429585308), (-1.0684064287, -0.2617397621))
                CenterArc((0, 0), 1.1, 145.7471833027, 48.0181150278)
                Line((-1.3740655148, 1.3122286238), (-0.9092182883, 0.619130119))
            make_face()
            # Profile area: 2.4740042147, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 1.1, 145.7471833027, 48.0181150278)
                CenterArc((0, 0), 1.1, -166.2347016696, 41.9818849722)
                CenterArc((0, 0), 1.1, -124.2528166973, 48.0181150278)
                CenterArc((0, 0), 1.1, -76.2347016696, 42.0538725489)
                CenterArc((0, 0), 1.1, -34.1808291206, 47.9461274511)
                CenterArc((0, 0), 1.1, 13.7652983304, 41.9818849722)
                CenterArc((0, 0), 1.1, 55.7471833027, 48.0181150278)
                CenterArc((0, 0), 1.1, 103.7652983304, 41.9818849722)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2627714306, perimeter: 3.3992412589
            with BuildLine():
                Line((1.2429585308, 1.4370296067), (-0.2617397621, 1.0684064287))
                CenterArc((0, 0), 1.1, 55.7471833027, 48.0181150278)
                Line((1.3122286238, 1.3740655148), (0.619130119, 0.9092182883))
                CenterArc((0, 0), 1.9, 46.3186818283, 2.8231566541)
            make_face()
            # Profile area: 0.2621224378, perimeter: 3.398035794
            with BuildLine():
                Line((1.4370296067, -1.2429585308), (1.0684064287, 0.2617397621))
                CenterArc((0, 0), 1.1, -34.1808291206, 47.9461274511)
                Line((1.3742587624, -1.3120262399), (0.9099954581, -0.6179872703))
                CenterArc((0, 0), 1.9, -43.6728797598, 2.8147182422)
            make_face()
            # Profile area: 0.2627714306, perimeter: 3.3992412589
            with BuildLine():
                Line((-1.2429585308, -1.4370296067), (0.2617397621, -1.0684064287))
                CenterArc((0, 0), 1.1, -124.2528166973, 48.0181150278)
                Line((-1.3122286238, -1.3740655148), (-0.619130119, -0.9092182883))
                CenterArc((0, 0), 1.9, -133.6813181717, 2.8231566541)
            make_face()
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            Circle(0.65)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            Circle(0.65)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5793055603, perimeter: 33.1253157756
            with BuildLine():
                CenterArc((0, 0), 2.8644937617, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, -128.9167196586, 77.8334393171)
                CenterArc((-1.5, -1.5), 0.25, 102.9722398862, 244.0555202276)
                CenterArc((0, 0), 2, 141.0832803414, 77.8334393171)
                CenterArc((-1.5, 1.5), 0.25, 12.9722398862, 244.0555202276)
                CenterArc((0, 0), 2, 51.0832803414, 77.8334393171)
                CenterArc((1.5, 1.5), 0.25, -77.0277601138, 244.0555202276)
                CenterArc((0, 0), 2, -38.9167196586, 77.8334393171)
                CenterArc((1.5, -1.5), 0.25, -167.0277601138, 244.0555202276)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_137246_4216b9c5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 76.2241772467, perimeter: 40.9319178746
            with BuildLine():
                CenterArc((4.5, 0), 2.1, -60.7324224025, 121.4648448049)
                Line((5.5266666667, 1.8319267331), (2.1022222222, 3.7510880726))
                CenterArc((0, 0), 4.3, 60.7324224025, 58.5351551951)
                Line((-2.1022222222, 3.7510880726), (-5.5266666667, 1.8319267331))
                CenterArc((-4.5, 0), 2.1, 119.2675775975, 121.4648448049)
                Line((-5.5266666667, -1.8319267331), (-2.1022222222, -3.7510880726))
                CenterArc((0, 0), 4.3, -119.2675775975, 58.5351551951)
                Line((2.1022222222, -3.7510880726), (5.5266666667, -1.8319267331))
            make_face()
            with BuildLine():
                CenterArc((-4.5, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch7 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            Circle(2.4)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_138139_0602ff54_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 59.469616802, perimeter: 27.3371038157
            with Locations((-9.8023331004, 9.2996493517)):
                Circle(4.3508352021)
        # OneSide extrude, distance=31
        extrude(amount=31)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 61.5390041772, perimeter: 32.969327825
            with BuildLine():
                Line((12.5369941346, -3.5784867969), (12.5369941346, 2.1346097215))
                Line((12.5369941346, 2.1346097215), (1.7654267405, 2.1346097215))
                Line((1.7654267405, 2.1346097215), (1.7654267405, -3.5784867969))
                Line((1.7654267405, -3.5784867969), (12.5369941346, -3.5784867969))
            make_face()
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


def model_138160_4ec5518d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7659602391, perimeter: 3.2578300148
            with BuildLine():
                Line((3.7976464561, -4.180990612), (4.2023535439, -3.819009388))
                Line((4.2023535439, -3.819009388), (4.091222152, -3.2875321568))
                Line((4.091222152, -3.2875321568), (3.5753836724, -3.1180361497))
                Line((3.5753836724, -3.1180361497), (3.1706765846, -3.4800173738))
                Line((3.1706765846, -3.4800173738), (3.2818079765, -4.011494605))
                Line((3.2818079765, -4.011494605), (3.7976464561, -4.180990612))
            make_face()
        # OneSide extrude, distance=22
        extrude(amount=22)

        # Sketch7 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6060390545, perimeter: 4.7174071195
            with BuildLine():
                Line((-10.8532522628, 2.1334768306), (-10.5888129772, 2.8739068304))
                Line((-10.5888129772, 2.8739068304), (-11.0978245239, 3.4731329694))
                Line((-11.0978245239, 3.4731329694), (-11.8712753562, 3.3319291086))
                Line((-11.8712753562, 3.3319291086), (-12.1357146418, 2.5914991089))
                Line((-12.1357146418, 2.5914991089), (-11.6267030951, 1.9922729699))
                Line((-11.6267030951, 1.9922729699), (-10.8532522628, 2.1334768306))
            make_face()
        # OneSide extrude, distance=17
        extrude(amount=17)
    return part.part


def model_138223_4bccf358_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 82.9701819288, perimeter: 36.4053949938
            with BuildLine():
                Line((-5.0378469734, -3.4518665976), (-5.0378469734, 2.5481334024))
                CenterArc((0.9621530266, 9.1293025743), 13.9386447595, -115.496624263, 50.993248526)
                Line((6.9621530266, 2.5481334024), (6.9621530266, -3.4518665976))
                Line((-5.0378469734, 2.5481334024), (6.9621530266, 2.5481334024))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_138233_a664480b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((2.5, -2.5), (-2.5, -2.5))
                Line((2.5, 2.5), (2.5, -2.5))
                Line((-2.5, 2.5), (2.5, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.2698739363, perimeter: 10.9079495745
            with BuildLine():
                Line((-2.5, -2.5), (2.5, -2.5))
                Line((2.5, -2.5), (2.5, -2.0460252127))
                Line((2.5, -2.0460252127), (-2.5, -2.0460252127))
                Line((-2.5, -2.0460252127), (-2.5, -2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch11 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.8188288515, perimeter: 10.7275315406
            with BuildLine():
                Line((2.5, 2.1362342297), (-2.5, 2.1362342297))
                Line((2.5, 2.1362342297), (2.5, 2.5))
                Line((2.5, 2.5), (-2.5, 2.5))
                Line((-2.5, 2.5), (-2.5, 2.1362342297))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_139953_3a23796a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.8968683166, perimeter: 38.9249108879
            with BuildLine():
                Line((0.15, 4.7862248658), (0, 4.7862248658))
                Line((0.15, 24.0986803097), (0.15, 4.7862248658))
                Line((0, 24.0986803097), (0.15, 24.0986803097))
                Line((0, 24.0986803097), (0, 4.7862248658))
            make_face()
            # Profile area: 2.8968683166, perimeter: 38.9249108879
            with BuildLine():
                Line((0, 24.0986803097), (0, 4.7862248658))
                Line((-0.15, 24.0986803097), (0, 24.0986803097))
                Line((-0.15, 4.7862248658), (-0.15, 24.0986803097))
                Line((0, 4.7862248658), (-0.15, 4.7862248658))
            make_face()
        # Symmetric extrude, each_side=0.725
        extrude(amount=0.725, both=True)
    return part.part


def model_141390_ca3867b8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.2, perimeter: 29.2
            with BuildLine():
                Line((-6, 1.3), (6, 1.3))
                Line((-6, -1.3), (-6, 1.3))
                Line((6, -1.3), (-6, -1.3))
                Line((6, 1.3), (6, -1.3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((4.5, 0)):
                Circle(0.255)
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((-4.5, 0)):
                Circle(0.255)
        # OneSide extrude, distance=-1.692
        extrude(amount=-1.692, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.4244639568, perimeter: 24.14179748
            with BuildLine():
                CenterArc((0, -22.0937496587), 22.8939680698, 74.8066147994, 30.3867704012)
                Line((-6, 0), (6, 0))
            make_face()
        # OneSide extrude, distance=-3.634
        extrude(amount=-3.634, mode=Mode.SUBTRACT)
    return part.part


def model_141894_8a60e848_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((0, 0), (1.5, 0))
                Line((0, -1.5), (0, 0))
                Line((1.5, -1.5), (0, -1.5))
                Line((1.5, -1.5), (1.5, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            with Locations((-0.75, 0.75)):
                Circle(0.375)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8855364292, perimeter: 6.4402649399
            with BuildLine():
                CenterArc((-0.75, 0.75), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.75, 0.75), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            with Locations((-0.75, 0.75)):
                Circle(0.375)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_142069_92ddcc78_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3974130691, perimeter: 3.0722252887
            with BuildLine():
                Line((12.1607142857, 13.2773991506), (12.1607142857, 12))
                Line((11.5384920635, 12.7828406646), (12.1607142857, 13.2773991506))
                Line((11.5384920635, 12.7828406646), (12.1607142857, 12))
            make_face()
            # Profile area: 0.6290683912, perimeter: 3.8652796396
            with BuildLine():
                Line((12.1607142857, 12), (13.7678571429, 12))
                Line((12.1607142857, 12), (12.7829365079, 11.2171593354))
                Line((12.7829365079, 11.2171593354), (13.7678571429, 12))
            make_face()
            # Profile area: 88.3525606193, perimeter: 92.1926485359
            with BuildLine():
                Line((13.7678571429, 12), (47.7456870505, 39.0064673273))
                Line((47.7456870505, 40), (47.7456870505, 39.0064673273))
                Line((45.7814013362, 40), (47.7456870505, 40))
                Line((12.1607142857, 13.2773991506), (45.7814013362, 40))
                Line((12.1607142857, 13.2773991506), (12.1607142857, 12))
                Line((12.1607142857, 12), (13.7678571429, 12))
            make_face()
        # OneSide extrude, distance=75
        extrude(amount=75)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5148399254, 0.6477390472, 0), x_dir=(0.7828406646, 0.6222222222, 0), z_dir=(0.6222222222, -0.7828406646, 0))):
            # Profile area: 558.2901234872, perimeter: 487.2255897412
            with BuildLine():
                Line((61.6479561645, 50.75), (61.6479561645, 75))
                Line((61.6479561645, 50.75), (63.9687785499, 49.2942855008))
                Line((63.9687785499, 49.2942855008), (63.9687785499, 77.3208223854))
                Line((63.9687785499, 77.3208223854), (14.6657459349, 77.3208223854))
                Line((14.6657459349, 77.3208223854), (14.6657459349, -2.3208223854))
                Line((14.6657459349, -2.3208223854), (63.9687785499, -2.3208223854))
                Line((63.9687785499, -2.3208223854), (63.9687785499, 43.1962006533))
                Line((61.6479561645, 40.75), (63.9687785499, 43.1962006533))
                Line((61.6479561645, 0), (61.6479561645, 40.75))
                Line((22.9865683203, 0), (61.6479561645, 0))
                Line((16.9865683203, 0), (22.9865683203, 0))
                Line((16.9865683203, 0), (16.9865683203, 45.75))
                Line((16.9865683203, 75), (16.9865683203, 45.75))
                Line((16.9865683203, 75), (22.9865683203, 75))
                Line((61.6479561645, 75), (22.9865683203, 75))
            make_face()
            # Profile area: 468.7693276111, perimeter: 108.548712591
            with BuildLine():
                Line((61.6479561645, 75), (22.9865683203, 75))
                Line((22.9865683203, 75), (61.6479561645, 50.75))
                Line((61.6479561645, 50.75), (61.6479561645, 75))
            make_face()
            # Profile area: 787.7257773259, perimeter: 135.5831370607
            with BuildLine():
                Line((22.9865683203, 0), (61.6479561645, 40.75))
                Line((22.9865683203, 0), (61.6479561645, 0))
                Line((61.6479561645, 0), (61.6479561645, 40.75))
            make_face()
            # Profile area: 838.6292469365, perimeter: 141.0383428962
            with BuildLine():
                Line((16.9865683203, 0), (53.6479561645, 45.75))
                Line((16.9865683203, 45.75), (53.6479561645, 45.75))
                Line((16.9865683203, 0), (16.9865683203, 45.75))
            make_face()
            # Profile area: 536.1727972217, perimeter: 112.8114929471
            with BuildLine():
                Line((16.9865683203, 45.75), (53.6479561645, 45.75))
                Line((53.6479561645, 45.75), (16.9865683203, 75))
                Line((16.9865683203, 75), (16.9865683203, 45.75))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_142071_e505093b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.890419394, perimeter: 18.9237217915
            with BuildLine():
                Line((2.66, 1.12), (1.28, 2.96))
                CenterArc((0, 2), 1.6, 36.8698976458, 106.2602070769)
                Line((-2.6600000003, 1.1199998411), (-1.2800000397, 2.9599999471))
                CenterArc((-2.9000000078, 1.2999998312), 0.3, -90, 53.1301047228)
                Line((-3.2, 0.9999998312), (-2.9000000078, 0.9999998312))
                Line((-3.2, 0.9999998312), (-3.2, -0.0000001688))
                Line((-3.2, -0.0000001688), (-0.8, -0.0000001688))
                Line((-0.8, -0.0000001688), (-0.8, -0.9))
                Line((-0.8, -0.9), (0.8, -0.9))
                Line((0.8, -0.9), (0.8, 0))
                Line((0.8, 0), (3.2, 0))
                Line((3.2, 0), (3.2, 1))
                Line((3.2, 1), (2.9, 1))
                CenterArc((2.9, 1.3), 0.3, -143.1301023542, 53.1301023542)
            make_face()
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 2)):
                Circle(0.6)
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.7947898667, perimeter: 10.1627094123
            with BuildLine():
                Line((-3.2, 1), (-2.9, 0.9999999921))
                CenterArc((-2.9, 1.3), 0.3, -90, 53.1301023542)
                Line((-1.28, 2.96), (-2.66, 1.12))
                CenterArc((0, 2), 1.6, 89.9848046778, 53.1452976763)
                Line((-3.2, 3.5999998312), (0.0004243334, 3.5999998312))
                Line((-3.2, 1), (-3.2, 3.5999998312))
            make_face()
            # Profile area: 3.7947900641, perimeter: 10.1610123792
            with BuildLine():
                CenterArc((0, 2), 1.6, 36.8698952772, 53.1149093995)
                Line((2.6600000003, 1.1199998411), (1.2800000397, 2.9599999471))
                CenterArc((2.9000000078, 1.2999998312), 0.3, -143.1301047228, 53.1301047228)
                Line((2.9000000078, 0.9999998391), (3.2, 0.9999998312))
                Line((3.2, 3.5999998312), (3.2, 0.9999998312))
                Line((0.0004243334, 3.5999998312), (3.2, 3.5999998312))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


def model_142246_0851be5e_0033():
    """Model: Component14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72.3822947387, perimeter: 30.1592894745
            Circle(4.8)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 41.5692193817, perimeter: 24
            with BuildLine():
                Line((2, -3.4641016151), (4, 0))
                Line((4, 0), (2, 3.4641016151))
                Line((2, 3.4641016151), (-2, 3.4641016151))
                Line((-2, 3.4641016151), (-4, 0))
                Line((-4, 0), (-2, -3.4641016151))
                Line((-2, -3.4641016151), (2, -3.4641016151))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_142852_00b5fde9_0002():
    """Model: Post"""
    with BuildPart() as part:
        # profile etc... -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5132633067, perimeter: 4.5128883925
            with BuildLine():
                Line((1.4549677831, -0.635), (1.5875, -0.635))
                CenterArc((0, 0), 1.5875, -90, 66.4218215218)
                Line((1.5875, -1.5875), (0, -1.5875))
                Line((1.5875, -0.635), (1.5875, -1.5875))
            make_face()
            # Profile area: 0.5132633067, perimeter: 4.5128883925
            with BuildLine():
                CenterArc((0, 0), 1.5875, 23.5781784782, 66.4218215218)
                Line((1.5875, 0.635), (1.4549677831, 0.635))
                Line((1.5875, 1.5875), (1.5875, 0.635))
                Line((0, 1.5875), (1.5875, 1.5875))
            make_face()
            # Profile area: 0.5132633067, perimeter: 4.5128883925
            with BuildLine():
                Line((-1.5875, 0.635), (-1.5875, 1.5875))
                Line((-1.5875, 0.635), (-1.4549677831, 0.635))
                CenterArc((0, 0), 1.5875, 90, 66.4218215218)
                Line((-1.5875, 1.5875), (0, 1.5875))
            make_face()
            # Profile area: 0.5132633067, perimeter: 4.5128883925
            with BuildLine():
                CenterArc((0, 0), 1.5875, -156.4218215218, 66.4218215218)
                Line((-1.4549677831, -0.635), (-1.5875, -0.635))
                Line((-1.5875, -1.5875), (-1.5875, -0.635))
                Line((0, -1.5875), (-1.5875, -1.5875))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                CenterArc((0, 0), 1.5875, -23.5781784782, 23.5781784782)
                Line((1.4549677831, -0.635), (1.5875, -0.635))
                Line((1.5875, -0.635), (1.5875, 0))
            make_face()
            # Profile area: 0.7513162939, perimeter: 3.5815015526
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 23.5781784782)
                Line((1.4549677831, 0.635), (0.9525, 0.635))
                Line((0.9525, 0.635), (0.9525, -0.635))
                Line((0.9525, -0.635), (1.4549677831, -0.635))
                CenterArc((0, 0), 1.5875, -23.5781784782, 23.5781784782)
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((1.5875, 0.635), (1.4549677831, 0.635))
                CenterArc((0, 0), 1.5875, 0, 23.5781784782)
                Line((1.5875, 0), (1.5875, 0.635))
            make_face()
            # Profile area: 1.1912108866, perimeter: 7.8606479176
            with BuildLine():
                Line((-1.4549677831, 0.635), (-0.9525, 0.635))
                Line((-0.9525, 0.635), (-0.635, 0.635))
                Line((-0.635, 0.635), (-0.635, 1.27))
                Line((-0.635, 1.27), (0.635, 1.27))
                Line((0.635, 1.27), (0.635, 0.635))
                Line((0.635, 0.635), (0.9525, 0.635))
                Line((1.4549677831, 0.635), (0.9525, 0.635))
                CenterArc((0, 0), 1.5875, 23.5781784782, 66.4218215218)
                CenterArc((0, 0), 1.5875, 90, 66.4218215218)
            make_face()
            # Profile area: 0.7513162939, perimeter: 3.5815015526
            with BuildLine():
                CenterArc((0, 0), 1.5875, 156.4218215218, 23.5781784782)
                CenterArc((0, 0), 1.5875, -180, 23.5781784782)
                Line((-0.9525, -0.635), (-1.4549677831, -0.635))
                Line((-0.9525, -0.635), (-0.9525, 0.635))
                Line((-1.4549677831, 0.635), (-0.9525, 0.635))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((-1.5875, 0), (-1.5875, 0.635))
                CenterArc((0, 0), 1.5875, 156.4218215218, 23.5781784782)
                Line((-1.5875, 0.635), (-1.4549677831, 0.635))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((-1.4549677831, -0.635), (-1.5875, -0.635))
                CenterArc((0, 0), 1.5875, -180, 23.5781784782)
                Line((-1.5875, -0.635), (-1.5875, 0))
            make_face()
            # Profile area: 1.1912108866, perimeter: 7.8606479176
            with BuildLine():
                CenterArc((0, 0), 1.5875, -90, 66.4218215218)
                Line((0.9525, -0.635), (1.4549677831, -0.635))
                Line((0.9525, -0.635), (0.635, -0.635))
                Line((0.635, -0.635), (0.635, -1.27))
                Line((0.635, -1.27), (-0.635, -1.27))
                Line((-0.635, -1.27), (-0.635, -0.635))
                Line((-0.635, -0.635), (-0.9525, -0.635))
                Line((-0.9525, -0.635), (-1.4549677831, -0.635))
                CenterArc((0, 0), 1.5875, -156.4218215218, 66.4218215218)
            make_face()
            # Profile area: 2.41935, perimeter: 6.35
            with BuildLine():
                Line((-0.9525, -0.635), (-0.9525, 0.635))
                Line((-0.635, -0.635), (-0.9525, -0.635))
                Line((-0.635, -0.635), (0.635, -0.635))
                Line((0.9525, -0.635), (0.635, -0.635))
                Line((0.9525, 0.635), (0.9525, -0.635))
                Line((0.635, 0.635), (0.9525, 0.635))
                Line((0.635, 0.635), (-0.635, 0.635))
                Line((-0.9525, 0.635), (-0.635, 0.635))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-0.635, -0.635), (0.635, -0.635))
                Line((-0.635, -1.27), (-0.635, -0.635))
                Line((0.635, -1.27), (-0.635, -1.27))
                Line((0.635, -0.635), (0.635, -1.27))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((0.635, 0.635), (-0.635, 0.635))
                Line((0.635, 1.27), (0.635, 0.635))
                Line((-0.635, 1.27), (0.635, 1.27))
                Line((-0.635, 0.635), (-0.635, 1.27))
            make_face()
        # OneSide extrude, distance=-15.24
        extrude(amount=-15.24)

        # profile etc... -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7513162939, perimeter: 3.5815015526
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 23.5781784782)
                Line((1.4549677831, 0.635), (0.9525, 0.635))
                Line((0.9525, 0.635), (0.9525, -0.635))
                Line((0.9525, -0.635), (1.4549677831, -0.635))
                CenterArc((0, 0), 1.5875, -23.5781784782, 23.5781784782)
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                CenterArc((0, 0), 1.5875, -23.5781784782, 23.5781784782)
                Line((1.4549677831, -0.635), (1.5875, -0.635))
                Line((1.5875, -0.635), (1.5875, 0))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((1.5875, 0.635), (1.4549677831, 0.635))
                CenterArc((0, 0), 1.5875, 0, 23.5781784782)
                Line((1.5875, 0), (1.5875, 0.635))
            make_face()
            # Profile area: 0.7513162939, perimeter: 3.5815015526
            with BuildLine():
                CenterArc((0, 0), 1.5875, 156.4218215218, 23.5781784782)
                CenterArc((0, 0), 1.5875, -180, 23.5781784782)
                Line((-0.9525, -0.635), (-1.4549677831, -0.635))
                Line((-0.9525, -0.635), (-0.9525, 0.635))
                Line((-1.4549677831, 0.635), (-0.9525, 0.635))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((-1.4549677831, -0.635), (-1.5875, -0.635))
                CenterArc((0, 0), 1.5875, -180, 23.5781784782)
                Line((-1.5875, -0.635), (-1.5875, 0))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((-1.5875, 0), (-1.5875, 0.635))
                CenterArc((0, 0), 1.5875, 156.4218215218, 23.5781784782)
                Line((-1.5875, 0.635), (-1.4549677831, 0.635))
            make_face()
        # OneSide extrude, distance=-10.16
        extrude(amount=-10.16, mode=Mode.SUBTRACT)

        # profile etc... -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.41935, perimeter: 6.35
            with BuildLine():
                Line((-0.9525, -0.635), (-0.9525, 0.635))
                Line((-0.635, -0.635), (-0.9525, -0.635))
                Line((-0.635, -0.635), (0.635, -0.635))
                Line((0.9525, -0.635), (0.635, -0.635))
                Line((0.9525, 0.635), (0.9525, -0.635))
                Line((0.635, 0.635), (0.9525, 0.635))
                Line((0.635, 0.635), (-0.635, 0.635))
                Line((-0.9525, 0.635), (-0.635, 0.635))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # profile etc... -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((0.635, 0.635), (-0.635, 0.635))
                Line((0.635, 1.27), (0.635, 0.635))
                Line((-0.635, 1.27), (0.635, 1.27))
                Line((-0.635, 0.635), (-0.635, 1.27))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-0.635, -0.635), (0.635, -0.635))
                Line((-0.635, -1.27), (-0.635, -0.635))
                Line((0.635, -1.27), (-0.635, -1.27))
                Line((0.635, -0.635), (0.635, -1.27))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # profile etc... -> rounding the post (Cut)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                CenterArc((0, 0), 1.5875, -23.5781784782, 23.5781784782)
                Line((1.4549677831, -0.635), (1.5875, -0.635))
                Line((1.5875, -0.635), (1.5875, 0))
            make_face()
            # Profile area: 0.5132633067, perimeter: 4.5128883925
            with BuildLine():
                Line((1.4549677831, -0.635), (1.5875, -0.635))
                CenterArc((0, 0), 1.5875, -90, 66.4218215218)
                Line((1.5875, -1.5875), (0, -1.5875))
                Line((1.5875, -0.635), (1.5875, -1.5875))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((1.5875, 0.635), (1.4549677831, 0.635))
                CenterArc((0, 0), 1.5875, 0, 23.5781784782)
                Line((1.5875, 0), (1.5875, 0.635))
            make_face()
            # Profile area: 0.5132633067, perimeter: 4.5128883925
            with BuildLine():
                CenterArc((0, 0), 1.5875, 23.5781784782, 66.4218215218)
                Line((1.5875, 0.635), (1.4549677831, 0.635))
                Line((1.5875, 1.5875), (1.5875, 0.635))
                Line((0, 1.5875), (1.5875, 1.5875))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((-1.4549677831, -0.635), (-1.5875, -0.635))
                CenterArc((0, 0), 1.5875, -180, 23.5781784782)
                Line((-1.5875, -0.635), (-1.5875, 0))
            make_face()
            # Profile area: 0.0275668531, perimeter: 1.42081521
            with BuildLine():
                Line((-1.5875, 0), (-1.5875, 0.635))
                CenterArc((0, 0), 1.5875, 156.4218215218, 23.5781784782)
                Line((-1.5875, 0.635), (-1.4549677831, 0.635))
            make_face()
            # Profile area: 0.5132633067, perimeter: 4.5128883925
            with BuildLine():
                Line((-1.5875, 0.635), (-1.5875, 1.5875))
                Line((-1.5875, 0.635), (-1.4549677831, 0.635))
                CenterArc((0, 0), 1.5875, 90, 66.4218215218)
                Line((-1.5875, 1.5875), (0, 1.5875))
            make_face()
            # Profile area: 0.5132633067, perimeter: 4.5128883925
            with BuildLine():
                CenterArc((0, 0), 1.5875, -156.4218215218, 66.4218215218)
                Line((-1.4549677831, -0.635), (-1.5875, -0.635))
                Line((-1.5875, -1.5875), (-1.5875, -0.635))
                Line((0, -1.5875), (-1.5875, -1.5875))
            make_face()
        # OneSide extrude, distance=-17.018
        extrude(amount=-17.018, mode=Mode.SUBTRACT)
    return part.part


def model_142852_ae641ada_0001():
    """Model: Leg"""
    with BuildPart() as part:
        # profile -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 79.0321, perimeter: 35.56
            with BuildLine():
                Line((-4.445, 4.445), (4.445, 4.445))
                Line((-4.445, -4.445), (-4.445, 4.445))
                Line((4.445, -4.445), (-4.445, -4.445))
                Line((4.445, 4.445), (4.445, -4.445))
            make_face()
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # foot dovetail outline -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 59.274075, perimeter: 53.34
            with BuildLine():
                Line((-4.445, 4.445), (-4.445, -4.445))
                Line((-4.445, -4.445), (4.445, -4.445))
                Line((4.445, -4.445), (4.445, 4.445))
                Line((4.445, 4.445), (-4.445, 4.445))
            make_face()
            with BuildLine():
                Line((2.2225, 2.2225), (2.2225, -2.2225))
                Line((2.2225, -2.2225), (-2.2225, -2.2225))
                Line((-2.2225, -2.2225), (-2.2225, 2.2225))
                Line((-2.2225, 2.2225), (2.2225, 2.2225))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.758025, perimeter: 17.78
            with BuildLine():
                Line((-2.2225, 2.2225), (2.2225, 2.2225))
                Line((-2.2225, -2.2225), (-2.2225, 2.2225))
                Line((2.2225, -2.2225), (-2.2225, -2.2225))
                Line((2.2225, 2.2225), (2.2225, -2.2225))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # foot dovetail outline -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 19.758025, perimeter: 17.78
            with BuildLine():
                Line((-2.2225, 2.2225), (2.2225, 2.2225))
                Line((-2.2225, -2.2225), (-2.2225, 2.2225))
                Line((2.2225, -2.2225), (-2.2225, -2.2225))
                Line((2.2225, 2.2225), (2.2225, -2.2225))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, taper=-15, mode=Mode.ADD)

        # shaping -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.445, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.9745827346, perimeter: 11.819784055
            with BuildLine():
                CenterArc((-1.11125, 5.715), 5.55625, -53.1301023542, 53.1301023542)
                Line((2.2225, 1.27), (4.445, 1.27))
                Line((4.445, 1.27), (4.445, 5.715))
            make_face()
            # Profile area: 21.5293512178, perimeter: 41.0370340513
            with BuildLine():
                Line((3.33375, 25.4), (3.33375, 6.985))
                CenterArc((4.60375, 6.985), 1.27, 180, 82.8192442185)
                Line((4.445, 5.7249609381), (4.445, 25.4))
                Line((4.445, 25.4), (3.33375, 25.4))
            make_face()
            # Profile area: 2.9745827346, perimeter: 11.819784055
            with BuildLine():
                CenterArc((1.11125, 5.715), 5.55625, 180, 53.1301023542)
                Line((-4.445, 5.715), (-4.445, 1.27))
                Line((-4.445, 1.27), (-2.2225, 1.27))
            make_face()
        # OneSide extrude, distance=-8.89
        extrude(amount=-8.89, mode=Mode.SUBTRACT)
    return part.part


def model_143019_54c55d14_0005():
    """Model: ribbonClips v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((1.0220178214, -0.9392758093), (-0.9779821786, -0.9392758093))
                Line((1.0220178214, 1.0607241907), (1.0220178214, -0.9392758093))
                Line((-0.9779821786, 1.0607241907), (1.0220178214, 1.0607241907))
                Line((-0.9779821786, -0.9392758093), (-0.9779821786, 1.0607241907))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5, perimeter: 4.5
            with BuildLine():
                Line((-0.7279821786, 1.0607241907), (-0.7279821786, -0.9392758093))
                Line((-0.9779821786, 1.0607241907), (-0.7279821786, 1.0607241907))
                Line((-0.9779821786, -0.9392758093), (-0.9779821786, 1.0607241907))
                Line((-0.7279821786, -0.9392758093), (-0.9779821786, -0.9392758093))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.5, perimeter: 7.5
            with BuildLine():
                Line((1.0220178214, -0.9392758093), (-0.7279821786, -0.9392758093))
                Line((1.0220178214, 1.0607241907), (1.0220178214, -0.9392758093))
                Line((-0.7279821786, 1.0607241907), (1.0220178214, 1.0607241907))
                Line((-0.7279821786, -0.9392758093), (-0.7279821786, 1.0607241907))
            make_face()
            # Profile area: 0.5, perimeter: 4.5
            with BuildLine():
                Line((-0.7279821786, -0.9392758093), (-0.7279821786, 1.0607241907))
                Line((-0.9779821786, 1.0607241907), (-0.7279821786, 1.0607241907))
                Line((-0.9779821786, -0.9392758093), (-0.9779821786, 1.0607241907))
                Line((-0.7279821786, -0.9392758093), (-0.9779821786, -0.9392758093))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_143236_19176148_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 88, perimeter: 38
            with BuildLine():
                Line((-5.5, 4), (-5.5, -4))
                Line((-5.5, -4), (5.5, -4))
                Line((5.5, -4), (5.5, 4))
                Line((5.5, 4), (-5.5, 4))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.0178624586, perimeter: 15.1163765961
            with BuildLine():
                Line((-2.5258446069, 0.229766604), (-2.5258446069, 0))
                Line((1.0135544537, 1.118175131), (-2.5258446069, 0.229766604))
                Line((-2.5258446069, 3.8301590556), (1.0135544537, 1.118175131))
                Line((-4, 3.8301590556), (-2.5258446069, 3.8301590556))
                Line((-4, 0), (-4, 3.8301590556))
                Line((-4, 0), (-2.5258446069, 0))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 71.9782318498, perimeter: 35.1958052134
            with BuildLine():
                Line((4, 5), (-4, 5))
                Line((4, 11.4536026441), (4, 5))
                Line((-8.2168960924, 11.4536026441), (4, 11.4536026441))
                Line((-8.2168960924, 8.2558360105), (-8.2168960924, 11.4536026441))
                Line((-4, 5), (-8.2168960924, 8.2558360105))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.ADD)
    return part.part


def model_143346_f9b2dca7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((-0.0094809964, -2.8), 0.5, 180, 271.8587054432)
                CenterArc((-0.0094809964, -2.8), 0.5, 91.8587054432, 88.1412945568)
            make_face()
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((2.8, 0), 0.5, 90, 268.8354713891)
                CenterArc((2.8, 0), 0.5, -1.1645286109, 91.1645286109)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((-0.0076946019, 2.8), 0.5, 180, 180)
                Line((-0.5076946019, 2.8), (0.4923053981, 2.8))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((-0.5076946019, 2.8), (0.4923053981, 2.8))
                CenterArc((-0.0076946019, 2.8), 0.5, 0, 180)
            make_face()
            # Profile area: 8.1007760998, perimeter: 10.0894675149
            Circle(1.6057886282)
        # OneSide extrude, distance=-2.0487
        extrude(amount=-2.0487, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.421304404, perimeter: 15.3757629679
            with BuildLine():
                CenterArc((0, 0), 4, 156.421061508, 47.2468225029)
                Line((-0.0127726575, -1.6057378296), (-3.6635510127, -1.6057378296))
                CenterArc((0, 0), 1.6057886282, 94.8459485683, 174.6983083316)
                Line((-3.6660393321, 1.6000486292), (-0.1356521378, 1.6000486292))
            make_face()
        # OneSide extrude, distance=-1.2654
        extrude(amount=-1.2654, mode=Mode.SUBTRACT)
    return part.part


def model_143373_1271e864_0000():
    """Model: Plate"""
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
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5641136352, perimeter: 7.6579798567
            with BuildLine():
                Line((0, 0), (0.1710100717, -0.4698463104))
                Line((0.1710100717, -0.4698463104), (3.3289899283, -0.4698463104))
                Line((3.5, 0), (3.3289899283, -0.4698463104))
                Line((0, 0), (3.5, 0))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.4698463104), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1728906306, perimeter: 2.5947922695
            with BuildLine():
                _nurbs_edge([(-1.5688040093, -0.6846870903), (-1.5688040093, -0.729005561), (-1.586826872, -0.7544143848), (-1.6168896221, -0.7544143848)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.6168896221, -0.7544143848), (-1.64451473, -0.7544143848), (-1.6589183232, -0.7315906248), (-1.6841797253, -0.6594991737)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.6841797253, -0.6594991737), (-1.7225891567, -0.5477427273), (-1.7790949364, -0.5008391928), (-1.8656639169, -0.4996571145)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.8656639169, -0.4996571145), (-1.9749827211, -0.4996571145), (-2.0567503537, -0.5861517079), (-2.0567503537, -0.7544143848)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.0567503537, -0.7544143848), (-2.0567503537, -0.8313071839), (-2.0387274909, -0.8998524), (-2.0146477164, -0.9443187432)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-2.0146477164, -0.9443187432), (-1.8838342014, -0.9118922873))
                _nurbs_edge([(-1.8838342014, -0.9118922873), (-1.90422077, -0.8782098167), (-1.9281526721, -0.8084825223), (-1.9281526721, -0.7544143848)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.9281526721, -0.7544143848), (-1.9281526721, -0.6991641689), (-1.9088742455, -0.6763404089), (-1.8788854317, -0.6763404089)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.8788854317, -0.6763404089), (-1.8488966179, -0.6763404089), (-1.834566961, -0.6943628209), (-1.8115213923, -0.7628350024)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.8115213923, -0.7628350024), (-1.7706743187, -0.8841941448), (-1.7045662939, -0.9310976793), (-1.6360941124, -0.9299156009)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.6360941124, -0.9299156009), (-1.5252979356, -0.9299156009), (-1.4425700335, -0.8361824682), (-1.4425700335, -0.6907435513)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.4425700335, -0.6907435513), (-1.4425700335, -0.6221974335), (-1.4582291904, -0.5608907567), (-1.4762520532, -0.5248450311)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.4762520532, -0.5248450311), (-1.6024120927, -0.5573454233))
                CenterArc((-1.8572794083, -0.6927159122), 0.2885871062, 1.594239538, 26.3803654252)
            make_face()
            # Profile area: 0.236199626, perimeter: 3.1477140391
            with BuildLine():
                Line((-1.8055379659, -1.2411782), (-1.4559391954, -1.2411782))
                Line((-1.4559391954, -1.2411782), (-1.4559391954, -1.0573303025))
                Line((-1.4559391954, -1.0573303025), (-1.8549530788, -1.0572563663))
                _nurbs_edge([(-1.8549530788, -1.0572563663), (-1.9318454271, -1.0572563663), (-1.9944085694, -1.054819175), (-2.0436758097, -1.0524550183)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-2.0436758097, -1.0524550183), (-2.0436758097, -1.2110410629))
                Line((-2.0436758097, -1.2110410629), (-1.9607265497, -1.2194625822))
                Line((-1.9607265497, -1.2194625822), (-1.9607265497, -1.2230818518))
                _nurbs_edge([(-1.9607265497, -1.2230818518), (-1.9967722752, -1.2459056118), (-2.0567499029, -1.3012297639), (-2.0567499029, -1.4069297493)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.0567499029, -1.4069297493), (-2.0567499029, -1.525924735), (-1.9822208096, -1.6137492793), (-1.8007370688, -1.6137492793)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.8007370688, -1.6137492793), (-1.4557915483, -1.6137492793))
                Line((-1.4557915483, -1.6137492793), (-1.4557915483, -1.4299013818))
                Line((-1.4557915483, -1.4299013818), (-1.7718559462, -1.4299013818))
                _nurbs_edge([(-1.7718559462, -1.4299013818), (-1.8572428484, -1.4299013818), (-1.9088737947, -1.4022023376), (-1.9088737947, -1.3385315041)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.9088737947, -1.3385315041), (-1.9088737947, -1.2880826362), (-1.8740101475, -1.2592015136), (-1.8452029612, -1.2471616264)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.810429594, -1.3432150899), 0.1021540744, 87.2553531294, 22.6459646866)
            make_face()
            # Profile area: 0.235143647, perimeter: 3.142886362
            with BuildLine():
                Line((-1.7044184214, -2.1330143884), (-2.0433809664, -2.1330143884))
                Line((-2.0433809664, -2.1330143884), (-2.0433809664, -2.3155314334))
                Line((-2.0433809664, -2.3155314334), (-1.6431108429, -2.3155314334))
                _nurbs_edge([(-1.6431108429, -2.3155314334), (-1.5698377643, -2.3155314334), (-1.5073485583, -2.3178946884), (-1.4556436758, -2.3203327814)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.4556436758, -2.3203327814), (-1.4556436758, -2.1616728005))
                Line((-1.4556436758, -2.1616728005), (-1.5361555192, -2.1532521829))
                Line((-1.5361555192, -2.1532521829), (-1.5361555192, -2.1496329133))
                CenterArc((-1.6575539172, -1.9719846392), 0.2151661691, -55.6527130007, 56.6740989308)
                _nurbs_edge([(-1.4424219356, -1.9681491724), (-1.4424219356, -1.8479721084), (-1.521751926, -1.7578582453), (-1.6948157254, -1.7578582453)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.6948157254, -1.7578582453), (-2.0433805156, -1.7578582453))
                Line((-2.0433805156, -1.7578582453), (-2.0433805156, -1.9405240645))
                Line((-2.0433805156, -1.9405240645), (-1.7176399362, -1.9405240645))
                _nurbs_edge([(-1.7176399362, -1.9405240645), (-1.6419292154, -1.9405240645), (-1.5902982692, -1.9669670941), (-1.5902982692, -2.0330760206)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.5902982692, -2.0330760206), (-1.5902982692, -2.0835988247), (-1.625088431, -2.1135880893), (-1.6587704507, -2.1256279766)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.702041027, -2.0029614002), 0.130074716, -91.0472615673, 20.4775312183)
            make_face()
            # Profile area: 0.1350411689, perimeter: 2.0241863968
            with BuildLine():
                Line((-1.7456342746, -2.5894949973), (-2.0436758097, -2.5894949973))
                Line((-2.0436758097, -2.5894949973), (-2.0436758097, -2.7721608165))
                Line((-2.0436758097, -2.7721608165), (-1.6494630489, -2.7721599148))
                _nurbs_edge([(-1.6494630489, -2.7721599148), (-1.5628945192, -2.7721599148), (-1.5064622249, -2.7745971061), (-1.45593897, -2.7769612628)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.45593897, -2.7769612628), (-1.45593897, -2.6195563949))
                Line((-1.45593897, -2.6195563949), (-1.5641500829, -2.613499934))
                Line((-1.5641500829, -2.613499934), (-1.5641500829, -2.608698586))
                _nurbs_edge([(-1.5641500829, -2.608698586), (-1.4787631807, -2.5787093213), (-1.4427174552, -2.5065448356), (-1.4427174552, -2.4501125414)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.6284799577, -2.4425596493), 0.1859159852, -2.3282987929, 11.9048730424)
                Line((-1.4451548719, -2.4116296245), (-1.6182186713, -2.4116296245))
                CenterArc((-1.7945879085, -2.4583184106), 0.1824443767, -0.8099197245, 15.6372532449)
                _nurbs_edge([(-1.6121617595, -2.4608973157), (-1.6121617595, -2.5281874189), (-1.6482814214, -2.5738358404), (-1.7047137156, -2.5858757277)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.7438544646, -2.3764783156), 0.213024117, -90.4787100654, 11.0663078699)
            make_face()
            # Profile area: 0.2264926583, perimeter: 3.176648443
            with BuildLine():
                Line((-1.8958001524, -2.9376896554), (-2.019596486, -2.9136838171))
                CenterArc((-1.4783182175, -3.1172228106), 0.5782821854, 159.392036251, 21.5112167737)
                _nurbs_edge([(-2.0565285449, -3.1263389009), (-2.0565285449, -3.3257720191), (-1.9398972652, -3.440039593), (-1.7560493677, -3.440039593)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.7560493677, -3.440039593), (-1.6069916319, -3.440039593), (-1.4423484502, -3.3474876369), (-1.4423484502, -3.1431801362)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.4423484502, -3.1431801362), (-1.4423484502, -2.9532757777), (-1.5900769113, -2.8811843266), (-1.7355888627, -2.8811843266)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.7358473721, -3.3110734203), 0.4298891715, 89.9655457813, 9.6634906507)
                Line((-1.8077542501, -2.8872407875), (-1.8081234806, -3.2660892348))
                _nurbs_edge([(-1.8081234806, -3.2660892348), (-1.8838342014, -3.2600327739), (-1.9198799269, -3.185577166), (-1.9198799269, -3.1001907146)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.4036850869, -3.0936470064), 0.5162363151, 162.4159474704, 18.3103418225)
            make_face()
            with BuildLine():
                Line((-1.6830715832, -3.2672713131), (-1.6830715832, -3.0509230234))
                _nurbs_edge([(-1.6830715832, -3.0509230234), (-1.6387531125, -3.0509230234), (-1.5641505338, -3.07020145), (-1.5641505338, -3.1543327884)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.5641505338, -3.1543327884), (-1.5641505338, -3.2312255876), (-1.6338043428, -3.2624699651), (-1.6830715832, -3.2672713131)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1894432639, perimeter: 2.6905641084
            with BuildLine():
                Line((-1.45593897, -4.0884920704), (-1.4559391954, -3.8897974131))
                Line((-1.4559391954, -3.8897974131), (-1.7287930393, -3.8104674226))
                CenterArc((-2.1122480425, -5.1180469578), 1.3626452144, 73.6559301933, 6.1803604255)
                Line((-1.8717938633, -3.7767849521), (-1.8717938633, -3.7732396187))
                _nurbs_edge([(-1.8717938633, -3.7732396187), (-1.8237082504, -3.7635629865), (-1.7792419072, -3.7539611921), (-1.7287930393, -3.7407392265)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.7287930393, -3.7407392265), (-1.45593897, -3.6650285057))
                Line((-1.45593897, -3.6650285057), (-1.45593897, -3.4729817993))
                Line((-1.45593897, -3.4729817993), (-2.0436758097, -3.6916203095))
                Line((-2.0436758097, -3.6916203095), (-2.0436758097, -3.8742861286))
                Line((-2.0436758097, -3.8742861286), (-1.45593897, -4.0884920704))
            make_face()
            # Profile area: 0.3073841995, perimeter: 3.8488556537
            with BuildLine():
                Line((-1.8357485885, -4.3500451641), (-1.8357485885, -4.5819782237))
                Line((-1.8357485885, -4.5819782237), (-2.0436762606, -4.6396660817))
                Line((-2.0436762606, -4.6396660817), (-2.0436762606, -4.8295708909))
                Line((-2.0436762606, -4.8295708909), (-1.2336086064, -4.5819782237))
                Line((-1.2336086064, -4.5819782237), (-1.2336086064, -4.3416245465))
                Line((-1.2336086064, -4.3416245465), (-2.0436762606, -4.0904865458))
                Line((-2.0436762606, -4.0904865458), (-2.0436762606, -4.2875559581))
                Line((-2.0436762606, -4.2875559581), (-1.8357485885, -4.3500451641))
            make_face()
            with BuildLine():
                Line((-1.6987307401, -4.5558304882), (-1.6987307401, -4.3764881937))
                Line((-1.6987307401, -4.3764881937), (-1.526849019, -4.4269375124))
                _nurbs_edge([(-1.526849019, -4.4269375124), (-1.4787634062, -4.441710336), (-1.4187118423, -4.4558181842), (-1.3706264548, -4.4678580714)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.3706264548, -4.4678580714), (-1.3706264548, -4.4702217773))
                _nurbs_edge([(-1.3706264548, -4.4702217773), (-1.4187120677, -4.4822616646), (-1.4800191953, -4.4942276156), (-1.526849019, -4.5071538362)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.526849019, -4.5071538362), (-1.6987307401, -4.5558304882))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.305135045, perimeter: 3.7601545554
            with BuildLine():
                Line((-2.2815927464, -5.7380995404), (-1.6530823185, -5.7380995404))
                _nurbs_edge([(-1.6530823185, -5.7380995404), (-1.576116034, -5.7380995404), (-1.5100075583, -5.7404632463), (-1.45593897, -5.7429008884)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.45593897, -5.7429008884), (-1.45593897, -5.5842409075))
                Line((-1.45593897, -5.5842409075), (-1.5377066025, -5.5758202899))
                Line((-1.5377066025, -5.5758202899), (-1.5377066025, -5.573456584))
                _nurbs_edge([(-1.5377066025, -5.573456584), (-1.4752176219, -5.5301723192), (-1.4427174552, -5.4626604073), (-1.4427174552, -5.3775687993)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.4427174552, -5.3775687993), (-1.4427174552, -5.2489715685), (-1.5544739015, -5.1338172104), (-1.7420150049, -5.1338172104)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.7420150049, -5.1338172104), (-1.9562209467, -5.1338172104), (-2.0568977754, -5.269579495), (-2.0568977754, -5.400614368)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.0568977754, -5.400614368), (-2.0568977754, -5.4715237408), (-2.0280171037, -5.5267744075), (-1.9896076722, -5.5532174371)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.9896076722, -5.5532174371), (-1.9896076722, -5.5556550792))
                Line((-1.9896076722, -5.5556550792), (-2.2815927464, -5.5556550792))
                Line((-2.2815927464, -5.5556550792), (-2.2815927464, -5.7380995404))
            make_face()
            with BuildLine():
                _nurbs_edge([(-1.916408079, -5.4448589024), (-1.916408079, -5.365528912), (-1.8499303729, -5.3186249266), (-1.7505830442, -5.3186249266)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.7505830442, -5.3186249266), (-1.6567755244, -5.3186249266), (-1.5858661516, -5.360727564), (-1.5858661516, -5.4424212603)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.5858661516, -5.4424212603), (-1.5858661516, -5.4941261428), (-1.6243495193, -5.5397741135), (-1.6784181077, -5.5518140008)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.7104654306, -5.41176827), 0.1436657148, -90.1806902783, 13.0700264697)
                Line((-1.7109184999, -5.5554332704), (-1.7912822453, -5.5554337213))
                CenterArc((-1.7932796435, -5.3702671528), 0.1851773412, -101.363485833, 11.9815134377)
                CenterArc((-1.8056181563, -5.4436816947), 0.1107961768, -179.3912217449, 76.8028686663)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0284978121, perimeter: 0.5989238491
            with BuildLine():
                _nurbs_edge([(-1.2000000721, -5.9761638988), (-1.2000000721, -5.9170726045), (-1.2395911311, -5.8798448006), (-1.2924778665, -5.8786631731)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.2924778665, -5.8786631731), (-1.3430008961, -5.8786631731), (-1.3838477442, -5.9171465408), (-1.3838477442, -5.9771981046)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.3838477442, -5.9771981046), (-1.3838477442, -6.0348859626), (-1.3430008961, -6.0732214578), (-1.2924778665, -6.072187252)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.2924778665, -6.072187252), (-1.2395911311, -6.0733688795), (-1.2000000721, -6.0352551931), (-1.2000000721, -5.9761638988)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 0.2821464762, perimeter: 3.6300127614
            with BuildLine():
                Line((-2.0436758097, -6.3881777137), (-2.0436758097, -6.6018665525))
                Line((-2.0436758097, -6.6018665525), (-1.2336081556, -6.861720465))
                Line((-1.2336081556, -6.861720465), (-1.2336081556, -6.6609578468))
                Line((-1.2336081556, -6.6609578468), (-1.576116034, -6.5623494298))
                _nurbs_edge([(-1.576116034, -6.5623494298), (-1.6721393872, -6.5347243219), (-1.7648387649, -6.5095364052), (-1.8658113386, -6.4902579786)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.8658113386, -6.4902579786), (-1.8658113386, -6.486638709))
                _nurbs_edge([(-1.8658113386, -6.486638709), (-1.7684584854, -6.4662521403), (-1.6722872597, -6.4409907383), (-1.5797357544, -6.4133656303)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.5797357544, -6.4133656303), (-1.2336086064, -6.3099558654))
                Line((-1.2336086064, -6.3099558654), (-1.2336086064, -6.1152501589))
                Line((-1.2336086064, -6.1152501589), (-2.0436758097, -6.3881777137))
            make_face()
            # Profile area: 0.1350355252, perimeter: 2.0241633791
            with BuildLine():
                Line((-1.7456342746, -7.2715184465), (-2.0436758097, -7.2715184465))
                Line((-2.0436758097, -7.2715184465), (-2.0436758097, -7.4541847165))
                Line((-2.0436758097, -7.4541847165), (-1.6494630489, -7.4541847165))
                _nurbs_edge([(-1.6494630489, -7.4541847165), (-1.5628945192, -7.4541847165), (-1.5064622249, -7.4565484224), (-1.45593897, -7.4589860645)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.45593897, -7.4589860645), (-1.45593897, -7.3015816474))
                Line((-1.45593897, -7.3015816474), (-1.5641500829, -7.2955247356))
                Line((-1.5641500829, -7.2955247356), (-1.5641500829, -7.2907233876))
                _nurbs_edge([(-1.5641500829, -7.2907233876), (-1.4787631807, -7.2606606376), (-1.4427174552, -7.1885691864), (-1.4427174552, -7.1320634068)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.6280376723, -7.1245415532), 0.1854728044, -2.3242689891, 11.9106438639)
                Line((-1.4451548719, -7.0936539753), (-1.6182186713, -7.0936539753))
                CenterArc((-1.7945879146, -7.1403427386), 0.1824443767, -0.8097853067, 15.637111403)
                _nurbs_edge([(-1.6121617595, -7.1429212157), (-1.6121617595, -7.2102113189), (-1.6482814214, -7.2558592896), (-1.7047137156, -7.2678991769)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                CenterArc((-1.744390516, -7.0524410046), 0.2190809724, -90.325279273, 10.7594462851)
            make_face()
            # Profile area: 0.1074028452, perimeter: 1.5409527395
            with BuildLine():
                Line((-2.0436758097, -7.6009526826), (-2.0436758097, -7.783692438))
                Line((-2.0436758097, -7.783692438), (-1.4559391954, -7.783692438))
                Line((-1.4559391954, -7.783692438), (-1.4559391954, -7.6009526826))
                Line((-1.4559391954, -7.6009526826), (-2.0436758097, -7.6009526826))
            make_face()
            # Profile area: 0.0284977996, perimeter: 0.5989237128
            with BuildLine():
                _nurbs_edge([(-1.2000000721, -7.692248624), (-1.2000000721, -7.6331573298), (-1.2395911311, -7.5959299767), (-1.2924778665, -7.5947478983)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.2924778665, -7.5947478983), (-1.3430008961, -7.5947478983), (-1.3838477442, -7.633231266), (-1.3838477442, -7.6932828299)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.3838477442, -7.6932828299), (-1.3838477442, -7.7509706879), (-1.3430008961, -7.7893061831), (-1.2924778665, -7.7882719772)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.2924778665, -7.7882719772), (-1.2395911311, -7.7894536048), (-1.2000000721, -7.7513399183), (-1.2000000721, -7.692248624)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            # Profile area: 0.2633378331, perimeter: 3.4670965871
            with BuildLine():
                _nurbs_edge([(-1.3706999403, -8.1437802379), (-1.3706999403, -8.2231102283), (-1.4067456658, -8.2619628264), (-1.4488480778, -8.2619628264)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.4488480778, -8.2619628264), (-1.5005529603, -8.2619628264), (-1.5233030094, -8.2163148557), (-1.5629680046, -8.1117232378)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.5629680046, -8.1117232378), (-1.6158545146, -7.9687224139), (-1.6903836079, -7.9014320853), (-1.8045776963, -7.9014320853)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.8045776963, -7.9014320853), (-1.940339981, -7.9014320853), (-2.0569712608, -8.005949767), (-2.0569712608, -8.2282808067)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-2.0569712608, -8.2282808067), (-2.0569712608, -8.3208325374), (-2.0317098587, -8.4122024151), (-2.0064480058, -8.4578503858)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-2.0064480058, -8.4578503858), (-1.8549530788, -8.420401224))
                CenterArc((-1.4380660094, -8.2088631906), 0.4674860086, -178.9689927784, 25.8732720709)
                _nurbs_edge([(-1.9054763338, -8.2172748999), (-1.9054763338, -8.1331435615), (-1.8706126866, -8.0886774437), (-1.8177257257, -8.0886774437)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.8177257257, -8.0886774437), (-1.7672024708, -8.0886774437), (-1.7383957353, -8.1270868751), (-1.7035316372, -8.2244397284)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.7035316372, -8.2244397284), (-1.6566281027, -8.3590940963), (-1.5821729457, -8.4468447044), (-1.4643595876, -8.4468447044)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.4643595876, -8.4468447044), (-1.3261598862, -8.4468447044), (-1.2206079987, -8.3314689884), (-1.2206079987, -8.1403086153)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(-1.2206079987, -8.1403086153), (-1.2206079987, -8.0490126739), (-1.2398127144, -7.9817223453), (-1.2614548469, -7.9334890854)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((-1.2614548469, -7.9334890854), (-1.4091830825, -7.9743359335))
                CenterArc((-1.7547888481, -8.141919956), 0.3840934128, -0.2775020742, 26.1462200067)
            make_face()
            # Profile area: 0.1074028452, perimeter: 1.5409527395
            with BuildLine():
                Line((-2.0436758097, -5.8846461486), (-2.0436758097, -6.067385904))
                Line((-2.0436758097, -6.067385904), (-1.4559391954, -6.067385904))
                Line((-1.4559391954, -6.067385904), (-1.4559391954, -5.8846461486))
                Line((-1.4559391954, -5.8846461486), (-2.0436758097, -5.8846461486))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_143599_66535745_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 88, perimeter: 38
            with BuildLine():
                Line((0, 8), (0, 0))
                Line((0, 0), (11, 0))
                Line((11, 0), (11, 8))
                Line((11, 8), (0, 8))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 33, perimeter: 28
            with BuildLine():
                Line((0, -3), (0, 0))
                Line((0, 0), (-11, 0))
                Line((-11, 0), (-11, -3))
                Line((-11, -3), (0, -3))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10, perimeter: 13
            with BuildLine():
                Line((-3.5, 3.5), (-7.5, 3.5))
                Line((-3.5, 6), (-3.5, 3.5))
                Line((-7.5, 6), (-3.5, 6))
                Line((-7.5, 3.5), (-7.5, 6))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


def model_143678_6d68b8bc_0001():
    """Model: Raptor 2.0 Finger Pin v2"""
    with BuildPart() as part:
        # Sketch15 -> Extrude16 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-5.5, 1.5)):
                Circle(0.2)
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)

        # Sketch16 -> Extrude17 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.95, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0371681469, perimeter: 1.5283185536
            with BuildLine():
                Line((-5.4999999943, 1.7), (-5.75, 1.7))
                Line((-5.75, 1.7), (-5.75, 1.3))
                Line((-5.75, 1.3), (-5.4999999943, 1.3))
                CenterArc((-5.5, 1.5), 0.2, -89.9999983631, -180.0000032737)
            make_face()
            # Profile area: 0.0371681469, perimeter: 1.5283185079
            with BuildLine():
                CenterArc((-5.5, 1.5), 0.2, 89.9999983631, -179.9999967263)
                Line((-5.4999999943, 1.3), (-5.25, 1.3))
                Line((-5.25, 1.3), (-5.25, 1.7))
                Line((-5.25, 1.7), (-5.4999999943, 1.7))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch21 -> Extrude21 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0043488435, perimeter: 0.8354142608
            with BuildLine():
                CenterArc((5.5, 1.5), 0.2, -58.2344738894, 116.4243273782)
                CenterArc((5.53, 1.4999883184), 0.1859534765, -66.116384603, 132.1881488053)
            make_face()

        # Sketch20 -> Extrude21 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0043486401, perimeter: 0.8353994286
            with BuildLine():
                CenterArc((5.5, 1.5), 0.2, 121.7665147229, 116.4223501536)
                CenterArc((5.4700000023, 1.5000116816), 0.1859530041, 113.8846692839, 132.1860410316)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_143718_b25c8fd0_0003():
    """Model: Tommy Bar v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=-6.2
        extrude(amount=-6.2)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=21.3
        extrude(amount=21.3, mode=Mode.ADD)
    return part.part


def model_143826_90d0f0c1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((2.5, 2.5)):
                Circle(2.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((2.5, 2.5)):
                Circle(2)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.3390590365, perimeter: 5.608752772
            with BuildLine():
                Line((2.5, 0), (0, 0))
                CenterArc((2.5, 2.5), 2.5, -126.8698976458, 36.8698976458)
                Line((1, 0.1000000015), (1, 0.5))
                Line((0, 0.1000000015), (1, 0.1000000015))
                Line((0, 0), (0, 0.1000000015))
            make_face()
            # Profile area: 0.3390590365, perimeter: 5.608752772
            with BuildLine():
                Line((5, 0), (2.5, 0))
                Line((5, 0.1000000015), (5, 0))
                Line((4, 0.1000000015), (5, 0.1000000015))
                Line((4, 0.5), (4, 0.1000000015))
                CenterArc((2.5, 2.5), 2.5, -90, 36.8698976458)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_144428_61da44e1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2806858378, perimeter: 2.3424778169
            with BuildLine():
                CenterArc((1.6000000238, 3.2500000462), 0.15, 90, 180)
                Line((1.6000000238, 3.1000000462), (2.3000000343, 3.1000000462))
                CenterArc((2.3000000343, 3.2500000462), 0.15, -90, 180)
                Line((1.6000000238, 3.4000000462), (2.3000000343, 3.4000000462))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-1.7463285364, -3.2456052561)):
                Circle(0.1)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.1497041277, -3.2448356446)):
                Circle(0.1)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_144595_a3491c94_0003():
    """Model: 6 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2411500823, perimeter: 17.9646003294
            with BuildLine():
                CenterArc((0, 0), 6.5, -20, 72)
                Line((6.1080020351, -2.2231309316), (6.5778483455, -2.3941410033))
                CenterArc((0, 0), 7, -20, 72)
                Line((4.0017995896, 5.1220698984), (4.3096303273, 5.5160752752))
            make_face()
            # Profile area: 74.6128255228, perimeter: 67.8657063594
            with BuildLine():
                CenterArc((0, 0), 6.5, 128, 72)
                CenterArc((0, 0), 6.5, -160, 140)
                CenterArc((0, 0), 6.5, -20, 72)
                CenterArc((0, 0), 6.5, 52, 76)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.3011626335, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.2411500823, perimeter: 17.9646003294
            with BuildLine():
                Line((-4.0017995896, 5.1220698984), (-4.3096303273, 5.5160752752))
                CenterArc((0, 0), 7, 128, 72)
                Line((-6.1080020351, -2.2231309316), (-6.5778483455, -2.3941410033))
                CenterArc((0, 0), 6.5, 128, 72)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.4767695314, perimeter: 18.9070781255
            with BuildLine():
                CenterArc((0, 0), 6.5, 52, 76)
                Line((4.0017995896, 5.1220698984), (4.3096303273, 5.5160752752))
                CenterArc((0, 0), 7, 52, 76)
                Line((-4.0017995896, 5.1220698984), (-4.3096303273, 5.5160752752))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.2466807157, perimeter: 33.9867228627
            with BuildLine():
                CenterArc((0, 0), 7, -160, 140)
                Line((6.1080020351, -2.2231309316), (6.5778483455, -2.3941410033))
                CenterArc((0, 0), 6.5, -160, 140)
                Line((-6.1080020351, -2.2231309316), (-6.5778483455, -2.3941410033))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            Circle(2.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 42.2151512826, perimeter: 41.1621688039
            with BuildLine():
                CenterArc((0, 0), 4.3011626335, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


MODELS = {
    "model_129236_61de2aec_0000": {"func": model_129236_61de2aec_0000, "volume": 94.6337065843, "area": 216.6320879819},
    "model_129412_a26d3ef5_0000": {"func": model_129412_a26d3ef5_0000, "volume": 2.2420105682, "area": 18.9705156988},
    "model_129422_621d0a90_0008": {"func": model_129422_621d0a90_0008, "volume": 100.5309649149, "area": 427.2566008882},
    "model_129428_edce5555_0001": {"func": model_129428_edce5555_0001, "volume": 69.184512917, "area": 249.7632610965},
    "model_129579_5b9f3a25_0000": {"func": model_129579_5b9f3a25_0000, "volume": 58.85, "area": 251.7},
    "model_129579_c747a9a1_0000": {"func": model_129579_c747a9a1_0000, "volume": 21.8516505504, "area": 131.948427373},
    "model_129848_0bf80366_0000": {"func": model_129848_0bf80366_0000, "volume": 30.1753198182, "area": 65.3547949384},
    "model_130084_a46c084c_0000": {"func": model_130084_a46c084c_0000, "volume": 65.0741156111, "area": 306.4020387306},
    "model_130285_74b0bed5_0000": {"func": model_130285_74b0bed5_0000, "volume": 0.008825655, "area": 0.6343925282},
    "model_130572_f14489d4_0000": {"func": model_130572_f14489d4_0000, "volume": 30420.592455802, "area": 6533.0231057511},
    "model_130757_854b49f3_0000": {"func": model_130757_854b49f3_0000, "volume": 24.4249685, "area": 85.6758996993},
    "model_130757_fc4d165e_0001": {"func": model_130757_fc4d165e_0001, "volume": 6.9336321611, "area": 25.6495435603},
    "model_131482_e7c8b8d9_0000": {"func": model_131482_e7c8b8d9_0000, "volume": 64.4167826001, "area": 291.7767201449},
    "model_131816_9dc8a682_0000": {"func": model_131816_9dc8a682_0000, "volume": 19.1542904089, "area": 54.930747548},
    "model_131816_9dc8a682_0002": {"func": model_131816_9dc8a682_0002, "volume": 19.1542904089, "area": 54.930747548},
    "model_131922_cdc111d2_0000": {"func": model_131922_cdc111d2_0000, "volume": 130.7687942057, "area": 209.0092866163},
    "model_132168_3c0897d9_0001": {"func": model_132168_3c0897d9_0001, "volume": 28.4235595334, "area": 83.0008779078},
    "model_132230_997ae6e5_0000": {"func": model_132230_997ae6e5_0000, "volume": 0.0137578213, "area": 0.4000282954},
    "model_132593_191a33ed_0000": {"func": model_132593_191a33ed_0000, "volume": 147.4762824016, "area": 253.0297323471},
    "model_132605_8ae2ba54_0000": {"func": model_132605_8ae2ba54_0000, "volume": 7834.2207844494, "area": 9560.4995279081},
    "model_132706_7f4c63c2_0000": {"func": model_132706_7f4c63c2_0000, "volume": 177.1225060714, "area": 406.3425224983},
    "model_132730_2ba993e9_0000": {"func": model_132730_2ba993e9_0000, "volume": 100.1006324271, "area": 487.5343626854},
    "model_132796_53ed101d_0005": {"func": model_132796_53ed101d_0005, "volume": 414.249119082, "area": 1475.2678872521},
    "model_133211_693043d1_0000": {"func": model_133211_693043d1_0000, "volume": 198943.9880885224, "area": 45901.6545722193},
    "model_134027_a6a95d00_0003": {"func": model_134027_a6a95d00_0003, "volume": 212.0076331167, "area": 476.6119426361},
    "model_134044_8027716b_0000": {"func": model_134044_8027716b_0000, "volume": 666.54, "area": 574.08},
    "model_134636_501f5634_0000": {"func": model_134636_501f5634_0000, "volume": 1558.6835163443, "area": 2030.8193308312},
    "model_135070_b300af8d_0008": {"func": model_135070_b300af8d_0008, "volume": 0.0705287551, "area": 1.1655308745},
    "model_135070_b300af8d_0016": {"func": model_135070_b300af8d_0016, "volume": 0.0563915881, "area": 0.9770353153},
    "model_135170_4d921c0e_0000": {"func": model_135170_4d921c0e_0000, "volume": 1190, "area": 1360},
    "model_135846_a6116c3f_0000": {"func": model_135846_a6116c3f_0000, "volume": 10.2375, "area": 42.55},
    "model_135892_ab8f21bf_0001": {"func": model_135892_ab8f21bf_0001, "volume": 41.7906488421, "area": 300.3940363026},
    "model_135892_ab8f21bf_0005": {"func": model_135892_ab8f21bf_0005, "volume": 5.5250740131, "area": 29.4247779608},
    "model_135918_fd78295e_0000": {"func": model_135918_fd78295e_0000, "volume": 31.8625722736, "area": 333.1902623225},
    "model_136128_30e5414b_0000": {"func": model_136128_30e5414b_0000, "volume": 7.555542338, "area": 26.4976543343},
    "model_136156_c485da18_0000": {"func": model_136156_c485da18_0000, "volume": 63175.1378955738, "area": 27934.411098309},
    "model_136620_b4159c31_0000": {"func": model_136620_b4159c31_0000, "volume": 60.4756585816, "area": 193.2079481958},
    "model_136804_03742933_0000": {"func": model_136804_03742933_0000, "volume": 0.7027654984, "area": 7.6054866872},
    "model_136804_0979aba6_0000": {"func": model_136804_0979aba6_0000, "volume": 0.7047654982, "area": 7.6854866878},
    "model_136804_629c2c23_0000": {"func": model_136804_629c2c23_0000, "volume": 14.2438433954, "area": 47.9444482752},
    "model_136804_72e9823d_0000": {"func": model_136804_72e9823d_0000, "volume": 0.688765498, "area": 7.325486683},
    "model_136804_7a5539a3_0000": {"func": model_136804_7a5539a3_0000, "volume": 0.7087654986, "area": 7.7780150064},
    "model_136804_fc7723ee_0000": {"func": model_136804_fc7723ee_0000, "volume": 0.7113318693, "area": 7.8168141026},
    "model_136821_0f4b88d0_0003": {"func": model_136821_0f4b88d0_0003, "volume": 2295.1694725037, "area": 1919.5445623084},
    "model_136821_0f4b88d0_0004": {"func": model_136821_0f4b88d0_0004, "volume": 847.4902496773, "area": 823.8199062222},
    "model_137053_59e609b3_0003": {"func": model_137053_59e609b3_0003, "volume": 0.8037020077, "area": 10.1600940661},
    "model_137053_59e609b3_0005": {"func": model_137053_59e609b3_0005, "volume": 0.973660242, "area": 10.7516117422},
    "model_137053_59e609b3_0009": {"func": model_137053_59e609b3_0009, "volume": 0.1156786493, "area": 1.481067609},
    "model_137098_0a45d1c8_0007": {"func": model_137098_0a45d1c8_0007, "volume": 0.7579092277, "area": 7.681194038},
    "model_137099_58f819ec_0004": {"func": model_137099_58f819ec_0004, "volume": 63.783622806, "area": 114.7867240685},
    "model_137099_58f819ec_0005": {"func": model_137099_58f819ec_0005, "volume": 0.4924209077, "area": 6.0249135449},
    "model_137099_58f819ec_0010": {"func": model_137099_58f819ec_0010, "volume": 2.7863869793, "area": 49.9282771213},
    "model_137246_4216b9c5_0000": {"func": model_137246_4216b9c5_0000, "volume": 95.088127433, "area": 204.5825848904},
    "model_138139_0602ff54_0000": {"func": model_138139_0602ff54_0000, "volume": 2643.5651751662, "area": 1518.0687219695},
    "model_138160_4ec5518d_0000": {"func": model_138160_4ec5518d_0000, "volume": 44.1537891872, "area": 156.6121799449},
    "model_138223_4bccf358_0000": {"func": model_138223_4bccf358_0000, "volume": 165.9403638577, "area": 238.7511538454},
    "model_138233_a664480b_0000": {"func": model_138233_a664480b_0000, "volume": 16.5887027878, "area": 81.6354811151},
    "model_139953_3a23796a_0000": {"func": model_139953_3a23796a_0000, "volume": 8.4009181181, "area": 68.4635940538},
    "model_141390_ca3867b8_0000": {"func": model_141390_ca3867b8_0000, "volume": 14.2320461842, "area": 80.3685090633},
    "model_141894_8a60e848_0000": {"func": model_141894_8a60e848_0000, "volume": 2.0095546815, "area": 12.4912053284},
    "model_142069_92ddcc78_0000": {"func": model_142069_92ddcc78_0000, "volume": 1436.8674734452, "area": 1895.0877243532},
    "model_142071_e505093b_0000": {"func": model_142071_e505093b_0000, "volume": 58.9245862991, "area": 121.4399730957},
    "model_142246_0851be5e_0033": {"func": model_142246_0851be5e_0033, "volume": 264.0941756101, "area": 268.1628131636},
    "model_142852_00b5fde9_0002": {"func": model_142852_00b5fde9_0002, "volume": 101.2962053681, "area": 200.4273223173},
    "model_142852_ae641ada_0001": {"func": model_142852_ae641ada_0001, "volume": 1684.2073031177, "area": 956.643164156},
    "model_143019_54c55d14_0005": {"func": model_143019_54c55d14_0005, "volume": 0.825, "area": 16.825},
    "model_143236_19176148_0000": {"func": model_143236_19176148_0000, "volume": 739.6729040545, "area": 650.6807947487},
    "model_143346_f9b2dca7_0000": {"func": model_143346_f9b2dca7_0000, "volume": 15.6936037317, "area": 84.5911923444},
    "model_143373_1271e864_0000": {"func": model_143373_1271e864_0000, "volume": 14.6290329916, "area": 79.6074114997},
    "model_143599_66535745_0000": {"func": model_143599_66535745_0000, "volume": 305.5, "area": 364},
    "model_143678_6d68b8bc_0001": {"func": model_143678_6d68b8bc_0001, "volume": 0.1276838986, "area": 1.6700601914},
    "model_143718_b25c8fd0_0003": {"func": model_143718_b25c8fd0_0003, "volume": 73.9279583243, "area": 163.4884816928},
    "model_143826_90d0f0c1_0000": {"func": model_143826_90d0f0c1_0000, "volume": 3.8733507718, "area": 32.0218172564},
    "model_144428_61da44e1_0000": {"func": model_144428_61da44e1_0000, "volume": 0.053201325, "area": 1.2982742819},
    "model_144595_a3491c94_0003": {"func": model_144595_a3491c94_0003, "volume": 63.2795300249, "area": 477.2188111736},
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
