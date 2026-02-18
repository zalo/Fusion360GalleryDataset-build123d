"""Batch 003 - passing/02_3ops
129 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_21713_c2dd40e0_0009():
    """Model: Circular_Mech_rim v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2943406933, perimeter: 2.8547248139
            with BuildLine():
                CenterArc((-4.1, -1.098591689), 0.25, 105.0842615686, 179.8314768628)
                Line((-4.2297646551, -0.6157239333), (-4.1650598239, -0.857205651))
                CenterArc((-4.1, -1.098591689), 0.5000001352, 105.0421307615, 179.915738477)
                Line((-4.0356504413, -1.3401680419), (-3.97094561, -1.5816497596))
            make_face()
            # Profile area: 2.0495457327, perimeter: 9.4924609672
            with BuildLine():
                CenterArc((0, 0), 0.25, -15, 105)
                Line((0.2414814566, -0.0647047613), (3.8585185434, -1.0338869277))
                CenterArc((4.1, -1.098591689), 0.25, 74.9157384314, 90.0842615686)
                Line((4.2297646551, -0.6157239333), (4.1650598239, -0.857205651))
                Line((0, 0.5176380902), (4.2297646551, -0.6157239333))
                Line((0, 0.5176380902), (0, 0.25))
            make_face()
            # Profile area: 1.9989208963, perimeter: 9.0936120809
            with BuildLine():
                Line((3.97094561, -1.5816497596), (0, -0.5176380902))
                Line((4.0356504413, -1.3401680419), (3.97094561, -1.5816497596))
                CenterArc((4.1, -1.098591689), 0.25, 165, 90.0842615686)
                Line((0.2414814566, -0.0647047613), (3.8585185434, -1.0338869277))
                CenterArc((0, 0), 0.25, -90, 75)
                Line((0, -0.25), (0, -0.5176380902))
            make_face()
            # Profile area: 0.2943406933, perimeter: 2.8547248139
            with BuildLine():
                Line((4.2297646551, -0.6157239333), (4.1650598239, -0.857205651))
                CenterArc((4.1, -1.098591689), 0.25, -104.9157384314, 179.8314768628)
                Line((4.0356504413, -1.3401680419), (3.97094561, -1.5816497596))
                CenterArc((4.1, -1.098591689), 0.5000001352, -104.9578692385, 179.915738477)
            make_face()
            # Profile area: 4.0484666291, perimeter: 11.0968083688
            with BuildLine():
                Line((-4.0356504413, -1.3401680419), (-3.97094561, -1.5816497596))
                Line((-3.97094561, -1.5816497596), (0, -0.5176380902))
                Line((0, -0.25), (0, -0.5176380902))
                CenterArc((0, 0), 0.25, 90, 180)
                Line((0, 0.5176380902), (0, 0.25))
                Line((0, 0.5176380902), (-4.2297646551, -0.6157239333))
                Line((-4.2297646551, -0.6157239333), (-4.1650598239, -0.857205651))
                CenterArc((-4.1, -1.098591689), 0.25, -75.0842615686, 180.1685231372)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0409061543, perimeter: 0.8272492347
            with BuildLine():
                CenterArc((0, 0), 0.25, -90, 75)
                Line((0, 0), (0.2414814566, -0.0647047613))
                Line((0, 0), (0, -0.25))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                Line((0, 0), (0, -0.25))
                Line((0, 0.25), (0, 0))
                CenterArc((0, 0), 0.25, 90, 180)
            make_face()
            # Profile area: 0.0572686161, perimeter: 0.9581489286
            with BuildLine():
                Line((0, 0.25), (0, 0))
                Line((0, 0), (0.2414814566, -0.0647047613))
                CenterArc((0, 0), 0.25, -15, 105)
            make_face()
            # Profile area: 0.0979909403, perimeter: 1.2846623018
            with BuildLine():
                CenterArc((4.1, -1.098591689), 0.25, -104.9157384314, 179.8314768628)
                Line((4.1650598239, -0.857205651), (4.1003551326, -1.0986868465))
                Line((4.1003551326, -1.0986868465), (4.0356504413, -1.3401680419))
            make_face()
            # Profile area: 0.0491793003, perimeter: 0.8934341321
            with BuildLine():
                Line((4.1003551326, -1.0986868465), (4.0356504413, -1.3401680419))
                Line((3.8585185434, -1.0338869277), (4.1003551326, -1.0986868465))
                CenterArc((4.1, -1.098591689), 0.25, 165, 90.0842615686)
            make_face()
            # Profile area: 0.0491793003, perimeter: 0.8934341321
            with BuildLine():
                Line((3.8585185434, -1.0338869277), (4.1003551326, -1.0986868465))
                Line((4.1650598239, -0.857205651), (4.1003551326, -1.0986868465))
                CenterArc((4.1, -1.098591689), 0.25, 74.9157384314, 90.0842615686)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_21713_c2dd40e0_0022():
    """Model: Circular_Mech_rim_3 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2943406933, perimeter: 2.8547248139
            with BuildLine():
                CenterArc((-4.1, -1.098591689), 0.25, 105.0842615686, 179.8314768628)
                Line((-4.2297646551, -0.6157239333), (-4.1650598239, -0.857205651))
                CenterArc((-4.1, -1.098591689), 0.5000001352, 105.0421307615, 179.915738477)
                Line((-4.0356504413, -1.3401680419), (-3.97094561, -1.5816497596))
            make_face()
            # Profile area: 4.0484666291, perimeter: 11.0968083688
            with BuildLine():
                Line((-4.0356504413, -1.3401680419), (-3.97094561, -1.5816497596))
                Line((-3.97094561, -1.5816497596), (0, -0.5176380902))
                Line((0, -0.25), (0, -0.5176380902))
                CenterArc((0, 0), 0.25, 90, 180)
                Line((0, 0.5176380902), (0, 0.25))
                Line((0, 0.5176380902), (-4.2297646551, -0.6157239333))
                Line((-4.2297646551, -0.6157239333), (-4.1650598239, -0.857205651))
                CenterArc((-4.1, -1.098591689), 0.25, -75.0842615686, 180.1685231372)
            make_face()
            # Profile area: 0.2943406933, perimeter: 2.8547248139
            with BuildLine():
                Line((4.2297646551, -0.6157239333), (4.1650598239, -0.857205651))
                CenterArc((4.1, -1.098591689), 0.25, -104.9157384314, 179.8314768628)
                Line((4.0356504413, -1.3401680419), (3.97094561, -1.5816497596))
                CenterArc((4.1, -1.098591689), 0.5000001352, -104.9578692385, 179.915738477)
            make_face()
            # Profile area: 2.0495457327, perimeter: 9.4924609672
            with BuildLine():
                CenterArc((0, 0), 0.25, -15, 105)
                Line((0.2414814566, -0.0647047613), (3.8585185434, -1.0338869277))
                CenterArc((4.1, -1.098591689), 0.25, 74.9157384314, 90.0842615686)
                Line((4.2297646551, -0.6157239333), (4.1650598239, -0.857205651))
                Line((0, 0.5176380902), (4.2297646551, -0.6157239333))
                Line((0, 0.5176380902), (0, 0.25))
            make_face()
            # Profile area: 1.9989208963, perimeter: 9.0936120809
            with BuildLine():
                Line((3.97094561, -1.5816497596), (0, -0.5176380902))
                Line((4.0356504413, -1.3401680419), (3.97094561, -1.5816497596))
                CenterArc((4.1, -1.098591689), 0.25, 165, 90.0842615686)
                Line((0.2414814566, -0.0647047613), (3.8585185434, -1.0338869277))
                CenterArc((0, 0), 0.25, -90, 75)
                Line((0, -0.25), (0, -0.5176380902))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0572686161, perimeter: 0.9581489286
            with BuildLine():
                Line((0, 0.25), (0, 0))
                Line((0, 0), (0.2414814566, -0.0647047613))
                CenterArc((0, 0), 0.25, -15, 105)
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                Line((0, 0), (0, -0.25))
                Line((0, 0.25), (0, 0))
                CenterArc((0, 0), 0.25, 90, 180)
            make_face()
            # Profile area: 0.0409061543, perimeter: 0.8272492347
            with BuildLine():
                CenterArc((0, 0), 0.25, -90, 75)
                Line((0, 0), (0.2414814566, -0.0647047613))
                Line((0, 0), (0, -0.25))
            make_face()
            # Profile area: 0.0979909403, perimeter: 1.2846623018
            with BuildLine():
                Line((-4.1650598239, -0.857205651), (-4.0356504413, -1.3401680419))
                CenterArc((-4.1, -1.098591689), 0.25, 105.0842615686, 179.8314768628)
            make_face()
            # Profile area: 0.0983586005, perimeter: 1.2861329436
            with BuildLine():
                CenterArc((-4.1, -1.098591689), 0.25, -75.0842615686, 180.1685231372)
                Line((-4.1650598239, -0.857205651), (-4.0356504413, -1.3401680419))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_21717_14f4c79a_0003():
    """Model: Nozzle v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1781393481, perimeter: 1.4961835013
            Circle(0.238125)
        # OneSide extrude, distance=2.8575
        extrude(amount=2.8575)
    return part.part


def model_21732_adaf1650_0025():
    """Model: Stand v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 205.2831853072, perimeter: 62.2831853072
            with BuildLine():
                CenterArc((2, 16), 2, 90, 90)
                Line((0, 16), (0, 9))
                Line((0, 9), (23, 9))
                Line((23, 9), (23, 15.9999991451))
                CenterArc((21, 16), 2, -0.0000244915, 90.000048983)
                Line((20.9999991451, 18), (2, 18))
            make_face()
            # Profile area: 205.2831853072, perimeter: 62.2831853072
            with BuildLine():
                Line((0, 9), (23, 9))
                Line((0, 9), (0, 2.0000008546))
                CenterArc((2, 2), 2, 179.9999755167, 90.0000489747)
                Line((2.0000008549, 0), (20.9999991451, 0))
                CenterArc((21, 2), 2, -90.0000244919, 90.0000489834)
                Line((23, 2.0000008549), (23, 9))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_21740_6f0c9bdb_0007():
    """Model: Bearing Innershell v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.408407045, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_21803_8a36dcda_0003():
    """Model: Stand v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 414, perimeter: 82
            with BuildLine():
                Line((23, -18), (0, -18))
                Line((23, 0), (23, -18))
                Line((0, 0), (23, 0))
                Line((0, -18), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_21803_8a36dcda_0011():
    """Model: Crankcase Gasket v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 33.689363134, perimeter: 64.9938110028
            with BuildLine():
                Line((-3.0599564267, -5.3), (3.0599564267, -5.3))
                Line((3.0599564267, -5.3), (6.1199128534, 0))
                Line((6.1199128534, 0), (3.0599564267, 5.3))
                Line((3.0599564267, 5.3), (-3.0599564267, 5.3))
                Line((-3.0599564267, 5.3), (-6.1199128534, 0))
                Line((-6.1199128534, 0), (-3.0599564267, -5.3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_21822_7d3db422_0029():
    """Model: Valve Fork"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7571680674, perimeter: 9.8283180196
            with BuildLine():
                Line((-22.5, -8), (-22.5, -10.200000152))
                Line((-22.5, -10.200000152), (-21.1000003144, -10.200000152))
                Line((-21.1000003144, -10.200000152), (-21.1000003144, -9.3000001386))
                Line((-21.1000003144, -9.3000001386), (-21.7000003234, -9.3000001386))
                Line((-21.7000003234, -9.3000001386), (-21.7000003234, -8))
                Line((-21.9000003263, -8), (-21.7000003234, -8))
                Line((-21.9000003263, -9.2), (-21.9000003263, -8))
                CenterArc((-22.1000001632, -9.2), 0.1999998368, 180, 180)
                Line((-22.3, -8), (-22.3, -9.2))
                Line((-22.5, -8), (-22.3, -8))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_21822_7d3db422_0048():
    """Model: Screw 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)
    return part.part


def model_21881_f3bee5e5_0003():
    """Model: Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2211604582, perimeter: 13.0262328567
            with BuildLine():
                Line((1.2, 0.692820323), (0, 1.3856406461))
                Line((0, 1.3856406461), (-1.2, 0.692820323))
                Line((-1.2, 0.692820323), (-1.2, -0.692820323))
                Line((-1.2, -0.692820323), (0, -1.3856406461))
                Line((0, -1.3856406461), (1.2, -0.692820323))
                Line((1.2, -0.692820323), (1.2, 0.692820323))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_21908_385686ec_0026():
    """Model: 10A v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.05, perimeter: 2.1
            with BuildLine():
                Line((0, 0.35), (0, 0))
                Line((0, 0), (0.4, 0))
                Line((0.4, 0), (0.4, 0.35))
                Line((0.4, 0.35), (0.35, 0.35))
                Line((0.35, 0.35), (0.35, 0.05))
                Line((0.35, 0.05), (0.05, 0.05))
                Line((0.05, 0.05), (0.05, 0.35))
                Line((0.05, 0.35), (0, 0.35))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_21923_41fa6eda_0000():
    """Model: Sliding Block v4 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.3956307394, perimeter: 19.026990817
            with BuildLine():
                Line((-2.5, 2.85), (-5, 2.85))
                Line((-5, 2.85), (-5, -1.85))
                Line((-5, -1.85), (-5.6, -1.85))
                Line((-5.6, -1.85), (-5.6, -2.85))
                Line((-5.6, -2.85), (-2.5, -2.85))
                Line((-2.5, -0.7), (-2.5, -2.85))
                CenterArc((-2.5, 0.55), 1.25, 90, 180)
                Line((-2.5, 2.85), (-2.5, 1.8))
            make_face()
            # Profile area: 12.3956307394, perimeter: 19.026990817
            with BuildLine():
                Line((0, 2.85), (-2.5, 2.85))
                Line((-2.5, 2.85), (-2.5, 1.8))
                CenterArc((-2.5, 0.55), 1.25, -90, 180)
                Line((-2.5, -0.7), (-2.5, -2.85))
                Line((-2.5, -2.85), (0.6, -2.85))
                Line((0.6, -2.85), (0.6, -1.85))
                Line((0, -1.85), (0.6, -1.85))
                Line((0, 2.85), (0, -1.85))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


def model_21984_3353d033_0002():
    """Model: Stabilizer v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8357293382, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0.0113679333, -0.759333889), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_22002_315afcfc_0011():
    """Model: Thong v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6335513597, perimeter: 2.8216025923
            Circle(0.449072)
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62)
    return part.part


def model_22010_95d37f0e_0003():
    """Model: Base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 600, perimeter: 100
            with BuildLine():
                Line((10, -15), (10, 15))
                Line((10, 15), (-10, 15))
                Line((-10, 15), (-10, -15))
                Line((-10, -15), (10, -15))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_22052_665cc4e0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.99869768, perimeter: 66.8528
            with BuildLine():
                Line((5.207, -3.3401), (5.207, 3.3401))
                Line((5.207, 3.3401), (-5.207, 3.3401))
                Line((-5.207, 3.3401), (-5.207, -3.3401))
                Line((-5.207, -3.3401), (5.207, -3.3401))
            make_face()
            with BuildLine():
                Line((-4.9657, -3.2004), (4.9657, -3.2004))
                Line((-4.9657, 3.2004), (-4.9657, -3.2004))
                Line((4.9657, 3.2004), (-4.9657, 3.2004))
                Line((4.9657, -3.2004), (4.9657, 3.2004))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_22118_1e09e0eb_0004():
    """Model: Bush v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 16.9646003294
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


def model_22124_6f71410e_0011():
    """Model: Screw v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8794791368, perimeter: 6.9821896726
            with Locations((2.7103511474, -1.0031197376)):
                Circle(1.11125)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)
    return part.part


def model_22196_0deb2e34_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 87.6418926536, perimeter: 36.6031853072
            with BuildLine():
                CenterArc((-4.695, -2.885), 1, -180, 90)
                Line((-4.695, -3.885), (4.695, -3.885))
                CenterArc((4.695, -2.885), 1, -90, 90)
                Line((5.695, -2.885), (5.695, 2.885))
                CenterArc((4.695, 2.885), 1, 0, 90)
                Line((4.695, 3.885), (-4.695, 3.885))
                CenterArc((-4.695, 2.885), 1, 90, 90)
                Line((-5.695, 2.885), (-5.695, -2.885))
            make_face()
        # OneSide extrude, distance=1.81
        extrude(amount=1.81)
    return part.part


def model_22201_473a3a65_0007():
    """Model: Face Plate v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.12193324, perimeter: 5.715
            with BuildLine():
                Line((0.4699, 2.06248), (0, 2.06248))
                Line((0, 2.06248), (0, 0))
                Line((0, 0), (0.79502, 0))
                Line((0.79502, 0), (0.79502, 0.4699))
                Line((0.79502, 0.4699), (0.4699, 0.4699))
                Line((0.4699, 0.4699), (0.4699, 2.06248))
            make_face()
        # Symmetric extrude, each_side=3.88874
        extrude(amount=3.88874, both=True)
    return part.part


def model_22204_126d06b5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.61690625, perimeter: 15.5575
            with BuildLine():
                Line((-1.5875, 2.301875), (1.5875, 2.301875))
                Line((-1.5875, -2.301875), (-1.5875, 2.301875))
                Line((1.5875, -2.301875), (-1.5875, -2.301875))
                Line((1.5875, 2.301875), (1.5875, -2.301875))
            make_face()
        # OneSide extrude, distance=3.4925
        extrude(amount=3.4925)
    return part.part


def model_22205_f48b96b3_0005():
    """Model: 11-M28 Nut v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6079404825, perimeter: 23.5766032273
            with BuildLine():
                Line((-2.13333, 1.2316786498), (-2.13333, -1.2316786498))
                Line((-2.13333, -1.2316786498), (0, -2.4633572995))
                Line((0, -2.4633572995), (2.13333, -1.2316786498))
                Line((2.13333, -1.2316786498), (2.13333, 1.2316786498))
                Line((2.13333, 1.2316786498), (0, 2.4633572995))
                Line((0, 2.4633572995), (-2.13333, 1.2316786498))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)
    return part.part


def model_22225_a3ce4d29_0001():
    """Model: Ignition Cam  v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8108333748, perimeter: 7.9327522989
            with BuildLine():
                CenterArc((0, 0), 0.87376, -56.9713632268, 293.9427264536)
                Line((0.47625, -0.7325588544), (-0.47625, -0.7325588544))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.39751, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.47625
        extrude(amount=0.47625, both=True)
    return part.part


def model_22225_a3ce4d29_0006():
    """Model: Side Frame v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59.5020576744, perimeter: 39.5236968589
            with BuildLine():
                CenterArc((3.1970818557, 5.715), 0.635, 30.0107016612, 59.9893268398)
                Line((0.6350004756, 6.35), (3.1970815399, 6.35))
                CenterArc((0.635, 5.715), 0.635, 89.9999570861, 90.0000858291)
                Line((0, 0), (0, 5.7149995244))
                Line((14.2875, 0), (0, 0))
                Line((14.2875, 3.175), (14.2875, 0))
                Line((5.7640381443, 3.175), (14.2875, 3.175))
                CenterArc((5.7640381443, 3.81), 0.635, -149.9892697694, 59.9892697694)
                Line((3.7469486751, 6.0326027092), (5.2141714832, 3.4923970166))
            make_face()
        # OneSide extrude, distance=0.79502
        extrude(amount=0.79502)
    return part.part


def model_22225_a3ce4d29_0008():
    """Model: Connecting Rod  v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.395865218, perimeter: 4.9872783376
            with BuildLine():
                CenterArc((0, 0), 0.47625, 34.9924723899, 290.0150552203)
                CenterArc((0, 0), 0.47625, -34.9924723899, 69.9849447797)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.8935482369, perimeter: 7.484907329
            with BuildLine():
                CenterArc((7.78002, 0), 0.71501, 140.7779994664, 78.4440010673)
                CenterArc((7.78002, 0), 0.71501, -140.7779994664, 281.5559989327)
            make_face()
            with BuildLine():
                CenterArc((7.78002, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.39751
        extrude(amount=0.39751, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8261643663, perimeter: 15.2372220879
            with BuildLine():
                CenterArc((0, 0), 0.47625, -34.9924723899, 69.9849447797)
                Line((0.3901570467, -0.2731145207), (7.2261005061, -0.45212))
                CenterArc((7.78002, 0), 0.71501, 140.7779994664, 78.4440010673)
                Line((0.3901570467, 0.2731145207), (7.2261005061, 0.45212))
            make_face()
        # Symmetric extrude, each_side=0.3175
        extrude(amount=0.3175, both=True, mode=Mode.ADD)
    return part.part


def model_22276_69c5036b_0015():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.6672539482, perimeter: 26.3893782902
            with BuildLine():
                CenterArc((0, 0), 3.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.3
        extrude(amount=3.3)
    return part.part


def model_22320_e9f9e6ae_0011():
    """Model: Lever v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 109.0829126562, perimeter: 73.3562265938
            with BuildLine():
                Line((12, 2.5599999982), (12, -1.2000000018))
                Line((0, 3.3999999982), (12, 2.5599999982))
                Line((-9.6, 1.1688627313), (0, 3.3999999982))
                CenterArc((-9.3284122166, 0), 1.2000000036, 103.0806964666, 166.9192794891)
                Line((-9.3284127202, -1.2000000036), (-4.0738190687, -1.2000000048))
                CenterArc((-4.0737349224, -2.4000000018), 1.2, 15.3745483251, 74.6294693623)
                Line((-2.9166789945, -2.0818466116), (-1.7355837185, -6.377231764))
                CenterArc((0, -5.9000010482), 1.8, -164.6254308587, 149.2508617174)
                Line((2.9166789945, -2.0818466116), (1.7355837185, -6.377231764))
                CenterArc((4.0737349224, -2.4000000018), 1.200000003, 89.9959823126, 74.6294693623)
                Line((4.0738190687, -1.2000000018), (12, -1.2000000018))
            make_face()
            with BuildLine():
                Line((0.6, -5.9000000624), (0.6, -4.4000000624))
                CenterArc((0, -5.9000010482), 0.6, -179.9999851059, 180.0000792439)
                Line((-0.6, -4.3999999823), (-0.6, -5.9000012041))
                CenterArc((0, -4.4000000018), 0.6, -0.0000057808, 180.0000039125)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.3284122166, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 77.84, perimeter: 61.6285161703
            with BuildLine():
                Line((40, -1.2000000018), (40, 0.5999999982))
                Line((12, 2.5599999982), (40, 0.5999999982))
                Line((12, 2.5599999982), (12, -1.2000000018))
                Line((12, -1.2000000018), (40, -1.2000000018))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_22340_ec24cd79_0037():
    """Model: split pin v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0323451411, perimeter: 0.7505566449
            with BuildLine():
                CenterArc((0, 0), 0.15, -176.1774463563, 172.3548927126)
                Line((-0.1496662955, -0.0099999998), (0.1496662955, -0.0099999998))
            make_face()
            # Profile area: 0.0323451411, perimeter: 0.7505566449
            with BuildLine():
                Line((0.1496662955, 0.0099999998), (-0.1496662955, 0.0099999998))
                CenterArc((0, 0), 0.15, 3.8225536437, 172.3548927126)
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)
    return part.part


def model_22344_51f483c9_0007():
    """Model: Con Rod 1 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6675884389, perimeter: 5.5907075111
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
                Line((0, -0.3), (0, -0.55))
                CenterArc((0, 0), 0.55, -90, 33.0557311509)
                CenterArc((0, 0), 0.55, -56.9442688491, 293.8885376983)
                CenterArc((0, 0), 0.55, -123.0557311509, 33.0557311509)
            make_face()
            # Profile area: 2.0143702024, perimeter: 8.2253400681
            with BuildLine():
                CenterArc((0, 0), 0.55, -123.0557311509, 33.0557311509)
                Line((-0.3, -0.4609772229), (-0.3, -3.9390227771))
                CenterArc((0, -4.4), 0.55, 56.9442688491, 66.1114623017)
                Line((0.3, -0.4609772229), (0.3, -3.9390227771))
                CenterArc((0, 0), 0.55, -90, 33.0557311509)
            make_face()
            # Profile area: 0.6675884389, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, -4.4), 0.55, 123.0557311509, 293.8885376983)
                CenterArc((0, -4.4), 0.55, 56.9442688491, 66.1114623017)
            make_face()
            with BuildLine():
                CenterArc((0, -4.4), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_22446_20eb3290_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1317698475, perimeter: 2.2023923469
            with BuildLine():
                Line((-0.9344071342, -1.036), (-1.036, -1.036))
                Line((-0.9344071342, -1.036), (-0.3040956899, -0.405))
                Line((-0.405, -0.405), (-0.3040956899, -0.405))
                Line((-0.405, -0.2970769173), (-0.405, -0.405))
                Line((-0.405, -0.2970769173), (-1.036, -0.9287662252))
                Line((-1.036, -1.036), (-1.036, -0.9287662252))
            make_face()
            # Profile area: 0.005751956, perimeter: 0.3661973668
            with BuildLine():
                Line((1.036, 1.25), (1.036, 1.1424868033))
                Line((1.036, 1.1424868033), (1.143, 1.25))
                Line((1.143, 1.25), (1.036, 1.25))
            make_face()
            # Profile area: 0.0049214093, perimeter: 0.3387288456
            with BuildLine():
                Line((1.036, 1.036), (1.036, 0.9365513849))
                Line((1.1349739134, 1.036), (1.036, 0.9365513849))
                Line((1.036, 1.036), (1.1349739134, 1.036))
            make_face()
            # Profile area: 0.0051661926, perimeter: 0.3470492174
            with BuildLine():
                Line((-1.036, -1.1377038464), (-0.9344071342, -1.036))
                Line((-0.9344071342, -1.036), (-1.036, -1.036))
                Line((-1.036, -1.1377038464), (-1.036, -1.036))
            make_face()
            # Profile area: 0.0058173247, perimeter: 0.361531558
            with BuildLine():
                Line((-0.405, -0.2970769173), (-0.405, -0.405))
                Line((-0.405, -0.405), (-0.3040956899, -0.405))
                Line((-0.3040956899, -0.405), (-0.3005312517, -0.4014316679))
                Line((-0.3005312517, -0.4014316679), (-0.405, -0.2970769173))
            make_face()
            # Profile area: 0.436174628, perimeter: 4.5865187828
            with BuildLine():
                Line((-0.3005312517, -0.4014316679), (-0.405, -0.2970769173))
                Line((-0.3040956899, -0.405), (-0.3005312517, -0.4014316679))
                Line((-0.3040956899, -0.405), (0.3061558149, -0.405))
                Line((0.3061558149, -0.405), (0.2974836502, -0.3962433171))
                Line((0.2974836502, -0.3962433171), (0.405, -0.2897646992))
                Line((0.405, -0.2897646992), (0.405, 0.3025249633))
                Line((0.405, 0.3025249633), (0.3020334694, 0.405))
                Line((0.3020334694, 0.405), (-0.2967834719, 0.405))
                Line((-0.4020513588, 0.2995805612), (-0.2967834719, 0.405))
                Line((-0.405, 0.3025249633), (-0.4020513588, 0.2995805612))
                Line((-0.405, 0.3025249633), (-0.405, -0.2970769173))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0115603092, perimeter: 0.7316881087
            with BuildLine():
                Line((1.25, -1.143), (1.1424836502, -1.2494786179))
                Line((1.1424836502, -1.2494786179), (1.036, -1.1419571868))
                Line((1.036, -1.25), (1.036, -1.1419571868))
                Line((1.25, -1.25), (1.036, -1.25))
                Line((1.25, -1.143), (1.25, -1.25))
            make_face()
            # Profile area: 0.1465113438, perimeter: 1.7877707816
            with BuildLine():
                Line((0.325, 1.25), (0.325, 1.036))
                Line((0.325, 1.036), (0.930021494, 1.036))
                Line((0.930021494, 1.036), (1.036, 1.1424868033))
                Line((1.036, 1.25), (1.036, 1.1424868033))
                Line((1.036, 1.25), (0.325, 1.25))
            make_face()
            # Profile area: 0.1464107327, perimeter: 1.7872182045
            with BuildLine():
                Line((-1.1431167598, -1.036), (-1.25, -1.036))
                Line((-1.036, -0.9287662252), (-1.1431167598, -1.036))
                Line((-1.036, -0.9287662252), (-1.036, -0.325))
                Line((-1.036, -0.325), (-1.25, -0.325))
                Line((-1.25, -0.325), (-1.25, -1.036))
            make_face()
            # Profile area: 0.1464047638, perimeter: 1.7871855986
            with BuildLine():
                Line((-1.036, 1.25), (-1.036, 1.1431538241))
                Line((-0.9286919089, 1.036), (-1.036, 1.1431538241))
                Line((-0.325, 1.036), (-0.9286919089, 1.036))
                Line((-0.325, 1.25), (-0.325, 1.036))
                Line((-1.036, 1.25), (-0.325, 1.25))
            make_face()
            # Profile area: 0.14626159, perimeter: 1.7864093055
            with BuildLine():
                Line((1.036, -0.325), (1.25, -0.325))
                Line((1.036, -0.9269143735), (1.036, -0.325))
                Line((1.036, -0.9269143735), (1.1440327482, -1.036))
                Line((1.1440327482, -1.036), (1.25, -1.036))
                Line((1.25, -0.325), (1.25, -1.036))
            make_face()
            # Profile area: 0.0052757495, perimeter: 0.3507111083
            with BuildLine():
                Line((0.405, 0.3025249633), (0.3020334694, 0.405))
                Line((0.405, 0.3025249633), (0.405, 0.405))
                Line((0.405, 0.405), (0.3020334694, 0.405))
            make_face()
            # Profile area: 0.0058551439, perimeter: 0.3638370521
            with BuildLine():
                Line((-0.405, 0.3025249633), (-0.4020513588, 0.2995805612))
                Line((-0.4020513588, 0.2995805612), (-0.2967834719, 0.405))
                Line((-0.2967834719, 0.405), (-0.405, 0.405))
                Line((-0.405, 0.405), (-0.405, 0.3025249633))
            make_face()
            # Profile area: 0.1469878074, perimeter: 1.790455793
            with BuildLine():
                Line((-0.325, -1.25), (-0.325, -1.036))
                Line((-0.325, -1.036), (-0.9344071342, -1.036))
                Line((-1.036, -1.1377038464), (-0.9344071342, -1.036))
                Line((-1.036, -1.25), (-1.036, -1.1377038464))
                Line((-1.036, -1.25), (-0.325, -1.25))
            make_face()
            # Profile area: 0.0277159082, perimeter: 0.6597585683
            with BuildLine():
                Line((1.036, 1.1424868033), (1.143, 1.25))
                Line((1.036, 1.1424868033), (1.036, 1.036))
                Line((1.036, 1.036), (1.1349739134, 1.036))
                Line((1.2459665306, 1.1475249633), (1.1349739134, 1.036))
                Line((1.143, 1.25), (1.2459665306, 1.1475249633))
            make_face()
            # Profile area: 0.0118226688, perimeter: 0.7341141482
            with BuildLine():
                Line((-1.1395310047, 1.036), (-1.25, 1.036))
                Line((-1.248267887, 1.1445805612), (-1.1395310047, 1.036))
                Line((-1.143, 1.25), (-1.248267887, 1.1445805612))
                Line((-1.25, 1.25), (-1.143, 1.25))
                Line((-1.25, 1.036), (-1.25, 1.25))
            make_face()
            # Profile area: 0.1468023702, perimeter: 1.7893965728
            with BuildLine():
                Line((-1.036, 0.325), (-1.25, 0.325))
                Line((-1.036, 0.9326178323), (-1.036, 0.325))
                Line((-1.1395310047, 1.036), (-1.036, 0.9326178323))
                Line((-1.1395310047, 1.036), (-1.25, 1.036))
                Line((-1.25, 0.325), (-1.25, 1.036))
            make_face()
            # Profile area: 0.1472325907, perimeter: 1.7918837884
            with BuildLine():
                Line((1.1349739134, 1.036), (1.25, 1.036))
                Line((1.1349739134, 1.036), (1.036, 0.9365513849))
                Line((1.036, 0.9365513849), (1.036, 0.325))
                Line((1.036, 0.325), (1.25, 0.325))
                Line((1.25, 0.325), (1.25, 1.036))
            make_face()
            # Profile area: 0.0055592824, perimeter: 0.3600163883
            with BuildLine():
                Line((1.036, -1.1419571868), (1.036, -1.036))
                Line((0.9310654963, -1.036), (1.036, -1.036))
                Line((1.036, -1.1419571868), (0.9310654963, -1.036))
            make_face()
            # Profile area: 0.005669248, perimeter: 0.3635596104
            with BuildLine():
                Line((1.1440327482, -1.036), (1.25, -1.036))
                Line((1.1440327482, -1.036), (1.25, -1.143))
                Line((1.25, -1.036), (1.25, -1.143))
            make_face()
            # Profile area: 0.0280556578, perimeter: 0.6627046643
            with BuildLine():
                Line((-1.25, -1.143), (-1.1455312517, -1.2473547506))
                Line((-1.1455312517, -1.2473547506), (-1.036, -1.1377038464))
                Line((-1.036, -1.1377038464), (-1.036, -1.036))
                Line((-1.036, -1.036), (-1.1431167598, -1.036))
                Line((-1.1431167598, -1.036), (-1.25, -1.143))
            make_face()
            # Profile area: 0.006627613, perimeter: 0.3777227591
            with BuildLine():
                Line((0.2974836502, -0.3962433171), (0.405, -0.2897646992))
                Line((0.3061558149, -0.405), (0.2974836502, -0.3962433171))
                Line((0.3061558149, -0.405), (0.405, -0.405))
                Line((0.405, -0.405), (0.405, -0.2897646992))
            make_face()
            # Profile area: 0.0285664429, perimeter: 0.667227589
            with BuildLine():
                Line((1.1440327482, -1.036), (1.25, -1.143))
                Line((1.036, -1.036), (1.1440327482, -1.036))
                Line((1.036, -1.1419571868), (1.036, -1.036))
                Line((1.1424836502, -1.2494786179), (1.036, -1.1419571868))
                Line((1.25, -1.143), (1.1424836502, -1.2494786179))
            make_face()
            # Profile area: 0.1296290712, perimeter: 2.1956215265
            with BuildLine():
                Line((0.405, 0.405), (0.3020334694, 0.405))
                Line((0.405, 0.3025249633), (0.405, 0.405))
                Line((1.036, 0.9365513849), (0.405, 0.3025249633))
                Line((1.036, 1.036), (1.036, 0.9365513849))
                Line((0.930021494, 1.036), (1.036, 1.036))
                Line((0.3020334694, 0.405), (0.930021494, 1.036))
            make_face()
            # Profile area: 0.1329459653, perimeter: 2.2061207245
            with BuildLine():
                Line((-0.405, 0.405), (-0.405, 0.3025249633))
                Line((-0.2967834719, 0.405), (-0.405, 0.405))
                Line((-0.2967834719, 0.405), (-0.9286919089, 1.036))
                Line((-0.9286919089, 1.036), (-1.036, 1.036))
                Line((-1.036, 1.036), (-1.036, 0.9326178323))
                Line((-1.036, 0.9326178323), (-0.405, 0.3025249633))
            make_face()
            # Profile area: 0.0282570608, perimeter: 0.664542102
            with BuildLine():
                Line((-1.143, 1.25), (-1.248267887, 1.1445805612))
                Line((-1.248267887, 1.1445805612), (-1.1395310047, 1.036))
                Line((-1.036, 1.036), (-1.1395310047, 1.036))
                Line((-1.036, 1.1431538241), (-1.036, 1.036))
                Line((-1.036, 1.1431538241), (-1.143, 1.25))
            make_face()
            # Profile area: 0.0123281357, perimeter: 0.738639768
            with BuildLine():
                Line((1.143, 1.25), (1.2459665306, 1.1475249633))
                Line((1.2459665306, 1.1475249633), (1.1349739134, 1.036))
                Line((1.1349739134, 1.036), (1.25, 1.036))
                Line((1.25, 1.036), (1.25, 1.25))
                Line((1.25, 1.25), (1.143, 1.25))
            make_face()
            # Profile area: 0.0056426562, perimeter: 0.3627014002
            with BuildLine():
                Line((0.930021494, 1.036), (1.036, 1.036))
                Line((1.036, 1.1424868033), (1.036, 1.036))
                Line((0.930021494, 1.036), (1.036, 1.1424868033))
            make_face()
            # Profile area: 0.0120220888, perimeter: 0.7359418996
            with BuildLine():
                Line((-1.25, -1.25), (-1.036, -1.25))
                Line((-1.036, -1.25), (-1.036, -1.1377038464))
                Line((-1.1455312517, -1.2473547506), (-1.036, -1.1377038464))
                Line((-1.25, -1.143), (-1.1455312517, -1.2473547506))
                Line((-1.25, -1.143), (-1.25, -1.25))
            make_face()
            # Profile area: 0.1465947176, perimeter: 1.7882330073
            with BuildLine():
                Line((1.036, -1.25), (1.036, -1.1419571868))
                Line((1.036, -1.1419571868), (0.9310654963, -1.036))
                Line((0.325, -1.036), (0.9310654963, -1.036))
                Line((0.325, -1.25), (0.325, -1.036))
                Line((1.036, -1.25), (0.325, -1.25))
            make_face()
            # Profile area: 0.0057182533, perimeter: 0.3651215522
            with BuildLine():
                Line((-1.1431167598, -1.036), (-1.25, -1.143))
                Line((-1.1431167598, -1.036), (-1.25, -1.036))
                Line((-1.25, -1.036), (-1.25, -1.143))
            make_face()
            # Profile area: 0.0053516298, perimeter: 0.3532229176
            with BuildLine():
                Line((-1.036, 1.036), (-1.036, 0.9326178323))
                Line((-1.036, 1.036), (-1.1395310047, 1.036))
                Line((-1.1395310047, 1.036), (-1.036, 0.9326178323))
            make_face()
            # Profile area: 0.0057432673, perimeter: 0.3659192738
            with BuildLine():
                Line((-1.036, -1.036), (-1.1431167598, -1.036))
                Line((-1.036, -1.036), (-1.036, -0.9287662252))
                Line((-1.036, -0.9287662252), (-1.1431167598, -1.036))
            make_face()
            # Profile area: 0.0057492362, perimeter: 0.3661094291
            with BuildLine():
                Line((-0.9286919089, 1.036), (-1.036, 1.036))
                Line((-0.9286919089, 1.036), (-1.036, 1.1431538241))
                Line((-1.036, 1.1431538241), (-1.036, 1.036))
            make_face()
            # Profile area: 0.0057162704, perimeter: 0.3650582961
            with BuildLine():
                Line((-1.036, 1.1431538241), (-1.143, 1.25))
                Line((-1.036, 1.25), (-1.036, 1.1431538241))
                Line((-1.143, 1.25), (-1.036, 1.25))
            make_face()
            # Profile area: 0.1350654289, perimeter: 2.2129000879
            with BuildLine():
                Line((0.405, -0.405), (0.405, -0.2897646992))
                Line((0.3061558149, -0.405), (0.405, -0.405))
                Line((0.9310654963, -1.036), (0.3061558149, -0.405))
                Line((0.9310654963, -1.036), (1.036, -1.036))
                Line((1.036, -1.036), (1.036, -0.9269143735))
                Line((0.405, -0.2897646992), (1.036, -0.9269143735))
            make_face()
            # Profile area: 0.00589241, perimeter: 0.3706460548
            with BuildLine():
                Line((1.036, -1.036), (1.036, -0.9269143735))
                Line((1.036, -1.036), (1.1440327482, -1.036))
                Line((1.036, -0.9269143735), (1.1440327482, -1.036))
            make_face()
        # OneSide extrude, distance=41.6
        extrude(amount=41.6)
    return part.part


def model_22447_4062c6cb_0004():
    """Model: Handle Final v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=9.4
        extrude(amount=9.4)
    return part.part


def model_22461_0ba0e480_0000():
    """Model: Gland Tightening Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.5872494951, perimeter: 8.7988181024
            with BuildLine():
                Line((1.4664696837, 0), (0.7332348419, 1.27))
                Line((0.7332348419, 1.27), (-0.7332348419, 1.27))
                Line((-0.7332348419, 1.27), (-1.4664696837, 0))
                Line((-1.4664696837, 0), (-0.7332348419, -1.27))
                Line((-0.7332348419, -1.27), (0.7332348419, -1.27))
                Line((0.7332348419, -1.27), (1.4664696837, 0))
            make_face()
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)
    return part.part


def model_22461_0ba0e480_0001():
    """Model: Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2986887417, perimeter: 3.681508192
            with BuildLine():
                Line((0.2022436356, 0.3499011935), (-0.2019015045, 0.3500987229))
                Line((-0.2019015045, 0.3500987229), (-0.4041451402, 0.0001975295))
                Line((-0.4041451402, 0.0001975295), (-0.2022436356, -0.3499011935))
                Line((-0.2022436356, -0.3499011935), (0.2019015045, -0.3500987229))
                Line((0.2019015045, -0.3500987229), (0.4041451402, -0.0001975295))
                Line((0.4041451402, -0.0001975295), (0.2022436356, 0.3499011935))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.125
        extrude(amount=0.125, both=True)
    return part.part


def model_22461_0ba0e480_0003():
    """Model: Valve Body v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.6088111964, perimeter: 12.124355653
            with BuildLine():
                Line((-1.75, 1.0103629711), (-1.75, -1.0103629711))
                Line((-1.75, -1.0103629711), (0, -2.0207259422))
                Line((0, -2.0207259422), (1.75, -1.0103629711))
                Line((1.75, -1.0103629711), (1.75, 1.0103629711))
                Line((1.75, 1.0103629711), (0, 2.0207259422))
                Line((0, 2.0207259422), (-1.75, 1.0103629711))
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


def model_22524_0be3da8a_0016():
    """Model: Flare Nut v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1051283081, perimeter: 2.7314299242
            with BuildLine():
                Line((0.23876, -0.1378481503), (0.23876, 0.1378481503))
                Line((0.23876, 0.1378481503), (0, 0.2756963005))
                Line((0, 0.2756963005), (-0.23876, 0.1378481503))
                Line((-0.23876, 0.1378481503), (-0.23876, -0.1378481503))
                Line((-0.23876, -0.1378481503), (0, -0.2756963005))
                Line((0, -0.2756963005), (0.23876, -0.1378481503))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1051283081, perimeter: 2.7314299242
            with BuildLine():
                Line((0.23876, -0.1378481503), (0.23876, 0.1378481503))
                Line((0.23876, 0.1378481503), (0, 0.2756963005))
                Line((0, 0.2756963005), (-0.23876, 0.1378481503))
                Line((-0.23876, 0.1378481503), (-0.23876, -0.1378481503))
                Line((-0.23876, -0.1378481503), (0, -0.2756963005))
                Line((0, -0.2756963005), (0.23876, -0.1378481503))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0485223082, perimeter: 1.8193591375
            with BuildLine():
                CenterArc((0, 0), 0.17145, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.11811, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.07874
        extrude(amount=-0.07874, mode=Mode.ADD)
    return part.part


def model_22534_e899f645_0003():
    """Model: 1012 - Stop Screw (Short) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            Circle(0.79375)
        # OneSide extrude, distance=-0.47625
        extrude(amount=-0.47625)
    return part.part


def model_22645_1ba0af00_0005():
    """Model: oil inlet screw2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8505098688, perimeter: 6.8434011418
            with BuildLine():
                Line((0.4788181951, 0.5399689522), (-0.2282177323, 0.6846531969))
                Line((-0.2282177323, 0.6846531969), (-0.7070359274, 0.1446842447))
                Line((-0.7070359274, 0.1446842447), (-0.4788181951, -0.5399689522))
                Line((-0.4788181951, -0.5399689522), (0.2282177323, -0.6846531969))
                Line((0.2282177323, -0.6846531969), (0.7070359274, -0.1446842447))
                Line((0.7070359274, -0.1446842447), (0.4788181951, 0.5399689522))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_22645_1ba0af00_0009():
    """Model: outline2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4118980033, perimeter: 4.7277879582
            with BuildLine():
                Line((0.0299567517, 0.499087093), (-0.4172437254, 0.2754868544))
                Line((-0.4172437254, 0.2754868544), (-0.447200477, -0.2236002385))
                Line((-0.447200477, -0.2236002385), (-0.0299567517, -0.499087093))
                Line((-0.0299567517, -0.499087093), (0.4172437254, -0.2754868544))
                Line((0.4172437254, -0.2754868544), (0.447200477, 0.2236002385))
                Line((0.447200477, 0.2236002385), (0.0299567517, 0.499087093))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.54
        extrude(amount=0.54)
    return part.part


def model_22719_67a50d6f_0003():
    """Model: P42-Stand"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 345.5424771932, perimeter: 107.506192983
            with BuildLine():
                CenterArc((-9, 7), 2, 90, 90)
                Line((-11, -7), (-11, 7))
                CenterArc((-9, -7), 2, 180, 90)
                Line((9, -9), (-9, -9))
                CenterArc((9, -7), 2, -90, 90)
                Line((11, 7), (11, -7))
                CenterArc((9, 7), 2, 0, 90)
                Line((-9, 9), (9, 9))
            make_face()
            with BuildLine():
                Line((-6.35, -0.7), (-6.35, 0.7))
                CenterArc((-5.15, 0.7), 1.2, 90, 90)
                Line((-5.15, 1.9), (5.15, 1.9))
                CenterArc((5.15, 0.7), 1.2, 0, 90)
                Line((6.35, 0.7), (6.35, -0.7))
                CenterArc((5.15, -0.7), 1.2, -90, 90)
                Line((5.15, -1.9), (-5.15, -1.9))
                CenterArc((-5.15, -0.7), 1.2, -180, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 47.0238934212, perimeter: 30.9398223686
            with BuildLine():
                CenterArc((-5.15, -0.7), 1.2, -180, 90)
                Line((5.15, -1.9), (-5.15, -1.9))
                CenterArc((5.15, -0.7), 1.2, -90, 90)
                Line((6.35, 0.7), (6.35, -0.7))
                CenterArc((5.15, 0.7), 1.2, 0, 90)
                Line((-5.15, 1.9), (5.15, 1.9))
                CenterArc((-5.15, 0.7), 1.2, 90, 90)
                Line((-6.35, -0.7), (-6.35, 0.7))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.0238934212, perimeter: 30.9398223686
            with BuildLine():
                CenterArc((-5.15, -0.7), 1.2, -180, 90)
                Line((5.15, -1.9), (-5.15, -1.9))
                CenterArc((5.15, -0.7), 1.2, -90, 90)
                Line((6.35, 0.7), (6.35, -0.7))
                CenterArc((5.15, 0.7), 1.2, 0, 90)
                Line((-5.15, 1.9), (5.15, 1.9))
                CenterArc((-5.15, 0.7), 1.2, 90, 90)
                Line((-6.35, -0.7), (-6.35, 0.7))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


def model_22719_67a50d6f_0010():
    """Model: P34-Reverse Gear Link Stud"""
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
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.ADD)
    return part.part


def model_22751_90a6225a_0005():
    """Model: Bancada v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2741.9716617121, perimeter: 217.0337314627
            with BuildLine():
                Line((0, 40.0455557703), (0, 0))
                Line((0, 0), (68.471309961, 0))
                Line((68.471309961, 0), (68.471309961, 40.0455557703))
                Line((68.471309961, 40.0455557703), (0, 40.0455557703))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_22753_071ecad9_0000():
    """Model: spade bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7428318531, perimeter: 8.398229715
            with BuildLine():
                CenterArc((11.446549658, 18.5612796486), 0.6, -90, 180)
                Line((11.446549658, 19.1612796486), (10.046549658, 19.1612796486))
                Line((10.046549658, 17.9612796486), (10.046549658, 19.1612796486))
                Line((10.046549658, 17.9612796486), (11.446549658, 17.9612796486))
            make_face()
            with BuildLine():
                CenterArc((11.446549658, 18.5612796486), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


def model_22753_071ecad9_0001():
    """Model: 3. indexing lever"""
    with BuildPart() as part:
        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.56, perimeter: 14.5810079668
            with BuildLine():
                Line((9.4, 5.5108428517), (11.5333333333, 4.3108428517))
                Line((9.4, 5.5108428517), (5, 5.5108428517))
                Line((5, 5.5108428517), (5, 4.3108428517))
                Line((11.5333333333, 4.3108428517), (5, 4.3108428517))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_22756_fc3fdda5_0004():
    """Model: Insert 6 - Rasp"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1603420495, perimeter: 2.3334020295
            with BuildLine():
                CenterArc((-3.2834695893, 0.0977500103), 0.8463190384, 138.7740302493, 82.4519395014)
                Line((-3.9199999124, -0.4599999897), (-3.9199999124, 0.6555000103))
            make_face()
            # Profile area: 8.6967471648, perimeter: 19.3408168611
            with BuildLine():
                Line((-3.9199999124, -0.4599999897), (-3.9199999124, 0.6555000103))
                Line((-1.879999958, -0.4099999908), (-3.9199999124, -0.4599999897))
                Line((-1.8699999582, -0.3099999931), (-1.879999958, -0.4099999908))
                CenterArc((-1.8200019704, -0.307166748), 0.0500781995, -3.447185787, 186.6905075377)
                Line((1.7769780903, -0.2471750065), (-1.77001438, -0.3101778725))
                Line((4.0410312379, -0.0305617485), (1.7769780903, -0.2471750065))
                Line((4.0444883447, 0.5173896751), (4.0410312379, -0.0305617485))
                Line((1.7479119444, 0.9222529006), (4.0444883447, 0.5173896751))
                Line((-2.6499999408, 0.9499999788), (1.7479119444, 0.9222529006))
                Line((-2.6499999408, 0.6555000103), (-2.6499999408, 0.9499999788))
                Line((-3.9199999124, 0.6555000103), (-2.6499999408, 0.6555000103))
            make_face()
            with BuildLine():
                CenterArc((-3.2783404722, 0.0977279568), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_22756_fc3fdda5_0017():
    """Model: Insert 7"""
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
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0793721354, perimeter: 1.3753394605
            with BuildLine():
                CenterArc((-1.5423512566, 0.3127500055), 0.8547127552, 179.9040225313, 40.8307516828)
                Line((-2.189999951, -0.2449999945), (-2.189999951, 0.3141817537))
                Line((-2.3970628126, 0.3141817537), (-2.189999951, 0.3141817537))
            make_face()
            # Profile area: 1.2741623185, perimeter: 6.484912106
            with BuildLine():
                Line((0.359999992, -0.179999996), (-2.189999951, -0.2449999945))
                _nurbs_edge([(0.480337832, 0.0997086368), (0.4819755901, 0.099675279), (0.4850880866, 0.0996227764), (0.4892678207, 0.0995866267), (0.4938597996, 0.0996241603), (0.4980191443, 0.0997533688), (0.5007796057, 0.0997859532), (0.5025408229, 0.0993506408), (0.5039460373, 0.0978556316), (0.5056344818, 0.0946477082), (0.5080559883, 0.0891331337), (0.5112141848, 0.080935275), (0.514737307, 0.0699018321), (0.5180411046, 0.056072315), (0.5204572768, 0.0396616697), (0.5213775439, 0.0210409213), (0.5203843424, 0.0007207039), (0.5172126673, -0.0206969433), (0.5117200819, -0.0425640173), (0.5038562306, -0.0642311543), (0.4936342772, -0.0850937723), (0.4811044267, -0.1046340582), (0.4663254741, -0.1224757373), (0.449355186, -0.1383730473), (0.430247551, -0.1521784927), (0.4090486628, -0.1638195152), (0.3904449976, -0.1713825147), (0.3755773579, -0.1760723235), (0.3652600403, -0.1787633561), (0.359999992, -0.179999996)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0.4140508888, 0.4577579004), 0.3641335387, -156.7779683621, 77.266586803)
                Line((-1.3463571613, 0.3141817537), (0.079418069, 0.3141817537))
                CenterArc((-1.5463500903, 0.312499993), 0.2, 179.5182053863, 180.9635892274)
                Line((-2.189999951, 0.3141817537), (-1.7463430194, 0.3141817537))
                Line((-2.189999951, -0.2449999945), (-2.189999951, 0.3141817537))
            make_face()
            # Profile area: 0.0787792093, perimeter: 1.3696124664
            with BuildLine():
                Line((-2.3970628126, 0.3141817537), (-2.189999951, 0.3141817537))
                Line((-2.189999951, 0.3141817537), (-2.189999951, 0.8705000055))
                CenterArc((-1.5423512566, 0.3127500055), 0.8547127552, 139.2652257859, 40.6387967454)
            make_face()
            # Profile area: 2.3956656426, perimeter: 10.7623194596
            with BuildLine():
                Line((-2.189999951, 0.3141817537), (-1.7463430194, 0.3141817537))
                CenterArc((-1.5463500903, 0.312499993), 0.2, 0.4817946137, 179.0364107726)
                Line((-1.3463571613, 0.3141817537), (0.079418069, 0.3141817537))
                CenterArc((0.4140508888, 0.4577579004), 0.3641335387, 65.2064875572, 138.0155440807)
                _nurbs_edge([(1.6500000246, 0.4599999897), (1.6400932062, 0.4596684796), (1.6197978724, 0.4593189593), (1.5879098051, 0.4597351722), (1.5424902365, 0.4621788425), (1.4808900724, 0.4684116439), (1.4146165929, 0.4778352997), (1.3440792467, 0.4904110304), (1.2700440549, 0.5060168531), (1.1937962676, 0.5244002277), (1.1171254136, 0.5451674142), (1.0420432216, 0.5678287026), (0.9705715171, 0.5918262567), (0.9045000534, 0.6165654628), (0.8451554302, 0.6414422887), (0.7931427462, 0.6658710629), (0.7481093608, 0.6893117047), (0.709093017, 0.7112850314), (0.6748426621, 0.731392317), (0.6441110699, 0.7493314855), (0.6160136465, 0.7649290164), (0.5952947447, 0.7754871958), (0.5806684382, 0.782325613), (0.571322096, 0.7864064965), (0.5667500308, 0.7883274182)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((2.2148538266, 0.4599999897), (1.6500000246, 0.4599999897))
                Line((2.2148538266, 0.9702499908), (2.2148538266, 0.4599999897))
                Line((1.7199999616, 1.0699999761), (2.2148538266, 0.9702499908))
                Line((-0.9199999794, 1.0699999761), (1.7199999616, 1.0699999761))
                Line((-0.9199999794, 0.8705000055), (-0.9199999794, 1.0699999761))
                Line((-2.189999951, 0.8705000055), (-0.9199999794, 0.8705000055))
                Line((-2.189999951, 0.3141817537), (-2.189999951, 0.8705000055))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_22756_fc3fdda5_0027():
    """Model: Spring (1) (4)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3025029128, perimeter: 18.3238935502
            with BuildLine():
                CenterArc((3.7502603558, 0.8935503171), 0.8483628506, -83.7089016779, 42.3071886464)
                Line((1.3199066669, 0.3324988721), (4.386609947, 0.3324988721))
                Line((1.3199066669, 0.484949191), (1.3199066669, 0.3324988721))
                Line((-1.9100933331, 0.484949191), (1.3199066669, 0.484949191))
                Line((-1.9125175841, 0.3024873103), (-1.9100933331, 0.484949191))
                Line((-4.1744920635, 0.1503220659), (-1.9125175841, 0.3024873103))
                Line((-4.3323961931, 0.1260429672), (-4.1744920635, 0.1503220659))
                Line((-4.3323961931, 0.0497005588), (-4.3323961931, 0.1260429672))
                Line((-1.8115780556, 0.1873998661), (-4.3323961931, 0.0497005588))
                Line((-1.8115780556, 0.3767482273), (-1.8115780556, 0.1873998661))
                Line((1.2194684914, 0.3767482273), (-1.8115780556, 0.3767482273))
                Line((1.2194684914, 0.186667696), (1.2194684914, 0.3767482273))
                Line((3.6422338533, 0.0502963143), (1.2194684914, 0.186667696))
                Line((3.8432238589, 0.0502963143), (3.6422338533, 0.0502963143))
            make_face()
        # OneSide extrude, distance=0.18
        extrude(amount=0.18)
    return part.part


def model_22768_620b0a0b_0000():
    """Model: Clamping Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((-2.5, 2.5), (2.5, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
                Line((2.5, -2.5), (-2.5, -2.5))
                Line((2.5, 2.5), (2.5, -2.5))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_22768_620b0a0b_0004():
    """Model: Jaw v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28, perimeter: 25.6
            with BuildLine():
                Line((-5, 1.4), (5, 1.4))
                Line((-5, -1.4), (-5, 1.4))
                Line((5, -1.4), (-5, -1.4))
                Line((5, 1.4), (5, -1.4))
            make_face()
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)
    return part.part


def model_22784_bcace961_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 43.7320337165, perimeter: 47.7240102337
            with BuildLine():
                Line((0, -3.5), (0, 0.5))
                Line((0, 0.5), (0.5, 0.5))
                Line((0.5, 0.5), (0.5, 2.5133049046))
                Line((0.5, 2.5133049046), (-2.5, 2.5133049046))
                Line((-2.5, 2.5133049046), (-2.5, 0.5))
                Line((-2.5, 0.5), (-2, 0.5))
                Line((-2, 0.5), (-2, -3.5))
                CenterArc((1.5, -3.5), 3.5, 180, 180)
                Line((5, -3.5), (5, 0.5))
                Line((5, 0.5), (5.5, 0.5))
                Line((5.5, 0.5), (5.5, 2.4947185782))
                Line((5.5, 2.4947185782), (2.5, 2.4947185782))
                Line((2.5, 2.4947185782), (2.5, 0.5))
                Line((2.5, 0.5), (3, 0.5))
                Line((3, 0.5), (3, -3.5))
                CenterArc((1.5, -3.5), 1.5, 180, 180)
            make_face()
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.966936042, perimeter: 57.412392421
            with BuildLine():
                Line((15, 2.4985509374), (7, 2.4985509374))
                Line((7, 2.4985509374), (7, 0.5))
                Line((7, 0.5), (7.5, 0.5))
                Line((7.5, 0.5), (7.5, -4.9882711918))
                Line((7.5, -4.9882711918), (7, -4.9882711918))
                Line((7, -4.9882711918), (7, -7))
                Line((7, -7), (10, -7))
                Line((10, -7), (10, -5.0033220391))
                Line((10, -5.0033220391), (9.5, -5.0033220391))
                Line((9.5, -5.0033220391), (9.5, -4))
                Line((9.5, -4), (11.5, -4))
                Line((11.5, -4), (12.1789152576, -5.0183728864))
                Line((12.1789152576, -5.0183728864), (12, -5.0183728864))
                Line((12, -5.0183728864), (12, -7))
                Line((12, -7), (15, -7))
                Line((15, -7), (15, -5.0183728864))
                Line((15, -5.0183728864), (14.1789152576, -5.0183728864))
                Line((14.1789152576, -5.0183728864), (13.5, -4))
                Line((13.5, -4), (15, -4))
                Line((15, -4), (15, 2.4985509374))
            make_face()
            with BuildLine():
                Line((9.5, -2.002086273), (9.5, 0.5))
                Line((9.5, 0.5), (13, 0.5))
                Line((13, 0.5), (13, -2.002086273))
                Line((13, -2.002086273), (9.5, -2.002086273))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.2006
        extrude(amount=3.2006)
    return part.part


def model_22790_2bdc9e13_0002():
    """Model: Bag"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 478.9880598419, perimeter: 86.4864619991
            with BuildLine():
                Line((0, 7.62), (0, 0))
                Line((0, 0), (27.94, 0))
                Line((27.94, 0), (27.94, 7.62))
                Line((27.94, 7.62), (23.32488063, 19.05))
                Line((23.32488063, 19.05), (4.7057800453, 19.05))
                Line((4.7057800453, 19.05), (0, 7.62))
            make_face()
        # OneSide extrude, distance=-35.56
        extrude(amount=-35.56)
    return part.part


def model_22822_b5d896dd_0007():
    """Model: Protector Maneta v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.3225663103, perimeter: 17.9115038379
            with BuildLine():
                CenterArc((0, 0), 0.6, 90, 180)
                Line((0, -0.6), (5.5, -0.6))
                CenterArc((5.5, 0), 0.6, -90, 180)
                Line((5.5, 0.6), (0, 0.6))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((5.5, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((5.5, 0)):
                Circle(0.2)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((5.5, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.5, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0942477796, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_22827_f33929ec_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 61.8149031146, perimeter: 30.9758065092
            with BuildLine():
                CenterArc((2.1189617012, -2.0208158503), 2.54, 90, 90)
                Line((-0.4210382988, -2.54), (-0.4210382988, -2.0208158503))
                CenterArc((2.1189617012, -2.54), 2.54, -180, 90)
                Line((9.398, -5.08), (2.1189617012, -5.08))
                CenterArc((9.398, -3.048), 2.032, -90, 90)
                Line((11.43, -1.5128158503), (11.43, -3.048))
                CenterArc((9.398, -1.5128158503), 2.032, 0, 90)
                Line((2.1189617012, 0.5191841497), (9.398, 0.5191841497))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


def model_23011_f267137c_0001():
    """Model: Bolt for Handle v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6495190722, perimeter: 3.0000000447
            with BuildLine():
                Line((0.4330127083, -0.2500000037), (0.4330127083, 0.2500000037))
                Line((0.4330127083, 0.2500000037), (0, 0.5000000075))
                Line((0, 0.5000000075), (-0.4330127083, 0.2500000037))
                Line((-0.4330127083, 0.2500000037), (-0.4330127083, -0.2500000037))
                Line((-0.4330127083, -0.2500000037), (0, -0.5000000075))
                Line((0, -0.5000000075), (0.4330127083, -0.2500000037))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_23018_63087a41_0010():
    """Model: S8G2"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 25.9672267773, perimeter: 18.0641577581
            with BuildLine():
                CenterArc((0, 0), 2.875, -2.2031797598, 4.4063595196)
                CenterArc((0, 0), 2.875, 2.2031797598, 355.5936404804)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0360398107, perimeter: 0.7765590047
            with BuildLine():
                _nurbs_edge([(2.8728747553, -0.110524388), (2.8750598596, -0.1101642208), (2.8877885173, -0.1079890902), (2.911051968, -0.1034107684), (2.9425452838, -0.0956706848), (2.974051368, -0.0866643082), (3.0055562661, -0.0764673467), (3.0370382251, -0.0651452595), (3.0685168434, -0.0528264353), (3.0893045504, -0.0438394748), (3.0997511063, -0.0393232102)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0564531668, 0.0564531668, 0.0564531668, 0.0564531668, 0.0630923935, 0.0951646223, 0.1275821994, 0.1603447122, 0.19345196, 0.2269038241, 0.2607002249, 0.2948411036, 0.2948411036, 0.2948411036, 0.2948411036], 3)
                CenterArc((-0.0065005474, 0), 3.1065005474, -0.7252901203, 1.4505802406)
                _nurbs_edge([(2.8728747553, 0.110524388), (2.8750598596, 0.1101642208), (2.8877885173, 0.1079890902), (2.911051968, 0.1034107684), (2.9425452838, 0.0956706848), (2.974051368, 0.0866643082), (3.0055562661, 0.0764673467), (3.0370382251, 0.0651452595), (3.0685168434, 0.0528264353), (3.0893045504, 0.0438394748), (3.0997511063, 0.0393232102)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0564531668, 0.0564531668, 0.0564531668, 0.0564531668, 0.0630923935, 0.0951646223, 0.1275821994, 0.1603447122, 0.19345196, 0.2269038241, 0.2607002249, 0.2948411036, 0.2948411036, 0.2948411036, 0.2948411036], 3)
                CenterArc((0, 0), 2.875, -2.2031797598, 4.4063595196)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_23018_63087a41_0011():
    """Model: S9G2"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 14.1862543264, perimeter: 13.3517687778
            with BuildLine():
                CenterArc((0, 0), 2.125, -2.8248538203, 5.6497076407)
                CenterArc((0, 0), 2.125, 2.8248538203, 354.3502923593)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0355414188, perimeter: 0.7625563856
            with BuildLine():
                _nurbs_edge([(2.1224178132, -0.1047264352), (2.1276141689, -0.1044910242), (2.1416762488, -0.103650808), (2.1645235671, -0.1000697536), (2.1909823161, -0.0947279077), (2.2174705104, -0.0880017167), (2.2439739245, -0.0801388337), (2.2704779435, -0.0712045795), (2.2969605661, -0.0612556184), (2.3234387362, -0.0504050484), (2.3409040089, -0.0424747656), (2.3496856286, -0.0384873828)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0107324783, 0.0107324783, 0.0107324783, 0.0107324783, 0.0263316097, 0.0529997362, 0.079992692, 0.1073093109, 0.1349491815, 0.1629120958, 0.1911979252, 0.2198065793, 0.2487379889, 0.2487379889, 0.2487379889, 0.2487379889], 3)
                CenterArc((-0.0060948677, 0), 2.3560948677, -0.9359821263, 1.8719642526)
                _nurbs_edge([(2.1224178132, 0.1047264352), (2.1276141689, 0.1044910242), (2.1416762488, 0.103650808), (2.1645235671, 0.1000697536), (2.1909823161, 0.0947279077), (2.2174705104, 0.0880017167), (2.2439739245, 0.0801388337), (2.2704779435, 0.0712045795), (2.2969605661, 0.0612556184), (2.3234387362, 0.0504050484), (2.3409040089, 0.0424747656), (2.3496856286, 0.0384873828)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0107324783, 0.0107324783, 0.0107324783, 0.0107324783, 0.0263316097, 0.0529997362, 0.079992692, 0.1073093109, 0.1349491815, 0.1629120958, 0.1911979252, 0.2198065793, 0.2487379889, 0.2487379889, 0.2487379889, 0.2487379889], 3)
                CenterArc((0, 0), 2.125, -2.8248538203, 5.6497076407)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_23018_63087a41_0017():
    """Model: S8G1"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 1.2271846303, perimeter: 3.926990817
            with BuildLine():
                CenterArc((0, 0), 0.625, 6.8054379143, 346.3891241714)
                CenterArc((0, 0), 0.625, -6.8054379143, 13.6108758286)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0317391624, perimeter: 0.6937364211
            with BuildLine():
                Line((0.6205964162, 0.074061381), (0.6997328735, 0.0835054499))
                CenterArc((0, 0), 0.625, -6.8054379143, 13.6108758286)
                Line((0.6205964162, -0.074061381), (0.6997328735, -0.0835054499))
                _nurbs_edge([(0.6997328735, -0.0835054499), (0.7051745962, -0.0835273528), (0.7161843738, -0.0835716669), (0.7327014331, -0.08093664), (0.7493391031, -0.0772485296), (0.7660488265, -0.0723327486), (0.7827940683, -0.0663855487), (0.7995457367, -0.0594492049), (0.8162654526, -0.0515617735), (0.8329607551, -0.042813041), (0.8438637048, -0.0363370323), (0.849366474, -0.0330685607)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0163000226, 0.0329784576, 0.050020406, 0.0674236715, 0.085187143, 0.1033100561, 0.121791811, 0.1406319069, 0.1598299132, 0.1598299132, 0.1598299132, 0.1598299132], 3)
                CenterArc((-0.013367163, 0), 0.863367163, -2.1950713549, 4.3901427099)
                _nurbs_edge([(0.6997328735, 0.0835054499), (0.7051745962, 0.0835273528), (0.7161843738, 0.0835716669), (0.7327014331, 0.08093664), (0.7493391031, 0.0772485296), (0.7660488265, 0.0723327486), (0.7827940683, 0.0663855487), (0.7995457367, 0.0594492049), (0.8162654526, 0.0515617735), (0.8329607551, 0.042813041), (0.8438637048, 0.0363370323), (0.849366474, 0.0330685607)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0163000226, 0.0329784576, 0.050020406, 0.0674236715, 0.085187143, 0.1033100561, 0.121791811, 0.1406319069, 0.1598299132, 0.1598299132, 0.1598299132, 0.1598299132], 3)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_23018_63087a41_0018():
    """Model: S10G1"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 1.2271846303, perimeter: 3.926990817
            with BuildLine():
                CenterArc((0, 0), 0.625, 6.8054379143, 346.3891241714)
                CenterArc((0, 0), 0.625, -6.8054379143, 13.6108758286)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0317391624, perimeter: 0.6937364211
            with BuildLine():
                Line((0.6205964162, 0.074061381), (0.6997328735, 0.0835054499))
                CenterArc((0, 0), 0.625, -6.8054379143, 13.6108758286)
                Line((0.6205964162, -0.074061381), (0.6997328735, -0.0835054499))
                _nurbs_edge([(0.6997328735, -0.0835054499), (0.7051745962, -0.0835273528), (0.7161843738, -0.0835716669), (0.7327014331, -0.08093664), (0.7493391031, -0.0772485296), (0.7660488265, -0.0723327486), (0.7827940683, -0.0663855487), (0.7995457367, -0.0594492049), (0.8162654526, -0.0515617735), (0.8329607551, -0.042813041), (0.8438637048, -0.0363370323), (0.849366474, -0.0330685607)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0163000226, 0.0329784576, 0.050020406, 0.0674236715, 0.085187143, 0.1033100561, 0.121791811, 0.1406319069, 0.1598299132, 0.1598299132, 0.1598299132, 0.1598299132], 3)
                CenterArc((-0.013367163, 0), 0.863367163, -2.1950713549, 4.3901427099)
                _nurbs_edge([(0.6997328735, 0.0835054499), (0.7051745962, 0.0835273528), (0.7161843738, 0.0835716669), (0.7327014331, 0.08093664), (0.7493391031, 0.0772485296), (0.7660488265, 0.0723327486), (0.7827940683, 0.0663855487), (0.7995457367, 0.0594492049), (0.8162654526, 0.0515617735), (0.8329607551, 0.042813041), (0.8438637048, 0.0363370323), (0.849366474, 0.0330685607)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0163000226, 0.0329784576, 0.050020406, 0.0674236715, 0.085187143, 0.1033100561, 0.121791811, 0.1406319069, 0.1598299132, 0.1598299132, 0.1598299132, 0.1598299132], 3)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_23018_63087a41_0020():
    """Model: Component78"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 25.9672267773, perimeter: 18.0641577581
            with BuildLine():
                CenterArc((0, 0), 2.875, -2.2031797598, 4.4063595196)
                CenterArc((0, 0), 2.875, 2.2031797598, 355.5936404804)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0360398107, perimeter: 0.7765590047
            with BuildLine():
                _nurbs_edge([(2.8728747553, -0.110524388), (2.8750598596, -0.1101642208), (2.8877885173, -0.1079890902), (2.911051968, -0.1034107684), (2.9425452838, -0.0956706848), (2.974051368, -0.0866643082), (3.0055562661, -0.0764673467), (3.0370382251, -0.0651452595), (3.0685168434, -0.0528264353), (3.0893045504, -0.0438394748), (3.0997511063, -0.0393232102)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0564531668, 0.0564531668, 0.0564531668, 0.0564531668, 0.0630923935, 0.0951646223, 0.1275821994, 0.1603447122, 0.19345196, 0.2269038241, 0.2607002249, 0.2948411036, 0.2948411036, 0.2948411036, 0.2948411036], 3)
                CenterArc((-0.0065005474, 0), 3.1065005474, -0.7252901203, 1.4505802406)
                _nurbs_edge([(2.8728747553, 0.110524388), (2.8750598596, 0.1101642208), (2.8877885173, 0.1079890902), (2.911051968, 0.1034107684), (2.9425452838, 0.0956706848), (2.974051368, 0.0866643082), (3.0055562661, 0.0764673467), (3.0370382251, 0.0651452595), (3.0685168434, 0.0528264353), (3.0893045504, 0.0438394748), (3.0997511063, 0.0393232102)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0564531668, 0.0564531668, 0.0564531668, 0.0564531668, 0.0630923935, 0.0951646223, 0.1275821994, 0.1603447122, 0.19345196, 0.2269038241, 0.2607002249, 0.2948411036, 0.2948411036, 0.2948411036, 0.2948411036], 3)
                CenterArc((0, 0), 2.875, -2.2031797598, 4.4063595196)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_23018_63087a41_0021():
    """Model: S9G1"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 5.9395736107, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((0, 0), 1.375, 3.845269174, 352.3094616521)
                CenterArc((0, 0), 1.375, -3.845269174, 7.6905383479)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0343877125, perimeter: 0.7339466922
            with BuildLine():
                Line((1.3719045919, 0.0922105782), (1.4063514173, 0.0945258717))
                CenterArc((0, 0), 1.375, -3.845269174, 7.6905383479)
                Line((1.3719045919, -0.0922105782), (1.4063514173, -0.0945258717))
                _nurbs_edge([(1.4063514173, -0.0945258717), (1.4134572352, -0.0943376013), (1.4277785314, -0.093958155), (1.4491791291, -0.0905347428), (1.4706594238, -0.0860255543), (1.4921785808, -0.0802650073), (1.5137178375, -0.0734707033), (1.5352600388, -0.0656974479), (1.5567806388, -0.0569931364), (1.5782935429, -0.0474569654), (1.5924499629, -0.0404633541), (1.5995752073, -0.0369433123)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213029077, 0.0429345721, 0.0648833728, 0.0871480701, 0.1097281897, 0.1326234683, 0.1558337285, 0.1793588361, 0.2031986819, 0.2031986819, 0.2031986819, 0.2031986819], 3)
                CenterArc((-0.0066528735, 0), 1.6066528735, -1.3175730001, 2.6351460001)
                _nurbs_edge([(1.4063514173, 0.0945258717), (1.4134572352, 0.0943376013), (1.4277785314, 0.093958155), (1.4491791291, 0.0905347428), (1.4706594238, 0.0860255543), (1.4921785808, 0.0802650073), (1.5137178375, 0.0734707033), (1.5352600388, 0.0656974479), (1.5567806388, 0.0569931364), (1.5782935429, 0.0474569654), (1.5924499629, 0.0404633541), (1.5995752073, 0.0369433123)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0213029077, 0.0429345721, 0.0648833728, 0.0871480701, 0.1097281897, 0.1326234683, 0.1558337285, 0.1793588361, 0.2031986819, 0.2031986819, 0.2031986819, 0.2031986819], 3)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_23018_63087a41_0025():
    """Model: Component75"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 90.7625752576, perimeter: 33.7721210261
            with BuildLine():
                CenterArc((0, 0), 5.375, -1.2473143569, 2.4946287137)
                CenterArc((0, 0), 5.375, 1.2473143569, 357.5053712863)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.036673346, perimeter: 0.7928650737
            with BuildLine():
                _nurbs_edge([(5.3737263858, -0.1170031228), (5.3848721569, -0.1140827367), (5.4121889998, -0.1065871903), (5.4555228573, -0.0934451078), (5.5037388823, -0.0772660496), (5.5519522338, -0.0597224714), (5.5838405273, -0.0469577499), (5.5998534548, -0.0405478565)], [1, 1, 1, 1, 1, 1, 1, 1], [0.2107797015, 0.2107797015, 0.2107797015, 0.2107797015, 0.2453440353, 0.2957523151, 0.3466052339, 0.3979027082, 0.4496446801, 0.4496446801, 0.4496446801, 0.4496446801], 3)
                CenterArc((-0.0097041381, 0), 5.6097041381, -0.4141468458, 0.8282936916)
                _nurbs_edge([(5.3737263858, 0.1170031228), (5.3848721569, 0.1140827367), (5.4121889998, 0.1065871903), (5.4555228573, 0.0934451078), (5.5037388823, 0.0772660496), (5.5519522338, 0.0597224714), (5.5838405273, 0.0469577499), (5.5998534548, 0.0405478565)], [1, 1, 1, 1, 1, 1, 1, 1], [0.2107797015, 0.2107797015, 0.2107797015, 0.2107797015, 0.2453440353, 0.2957523151, 0.3466052339, 0.3979027082, 0.4496446801, 0.4496446801, 0.4496446801, 0.4496446801], 3)
                CenterArc((0, 0), 5.375, -1.2473143569, 2.4946287137)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_23018_63087a41_0029():
    """Model: Hour Hand G2"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 3.6305030103, perimeter: 6.7544242052
            with BuildLine():
                CenterArc((0, 0), 1.075, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.075, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0335830414, perimeter: 0.7199796911
            with BuildLine():
                Line((1.0715535766, 0.0860112341), (1.1239926576, 0.090220403))
                CenterArc((0, 0), 1.075, -4.5891664191, 9.1783328383)
                Line((1.0715535766, -0.0860112341), (1.1239926576, -0.090220403))
                _nurbs_edge([(1.1239926576, -0.090220403), (1.1304309289, -0.0900959366), (1.1434195185, -0.0898448376), (1.1628428252, -0.0867155537), (1.1823545909, -0.0825324525), (1.2019128499, -0.0771312931), (1.221494937, -0.0707194592), (1.2410811997, -0.0633473177), (1.2606442815, -0.055059162), (1.2801964472, -0.0459494914), (1.2930390102, -0.0392523772), (1.2995077114, -0.0358790918)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192959231, 0.0389276582, 0.0588831091, 0.0791608969, 0.0997604541, 0.1206814447, 0.1419236292, 0.1634868191, 0.1853708568, 0.1853708568, 0.1853708568, 0.1853708568], 3)
                CenterArc((-0.0077203802, 0), 1.3077203802, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.1239926576, 0.090220403), (1.1304309289, 0.0900959366), (1.1434195185, 0.0898448376), (1.1628428252, 0.0867155537), (1.1823545909, 0.0825324525), (1.2019128499, 0.0771312931), (1.221494937, 0.0707194592), (1.2410811997, 0.0633473177), (1.2606442815, 0.055059162), (1.2801964472, 0.0459494914), (1.2930390102, 0.0392523772), (1.2995077114, 0.0358790918)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192959231, 0.0389276582, 0.0588831091, 0.0791608969, 0.0997604541, 0.1206814447, 0.1419236292, 0.1634868191, 0.1853708568, 0.1853708568, 0.1853708568, 0.1853708568], 3)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_23121_cbdf3ebc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100, perimeter: 50
            with BuildLine():
                Line((0, 0), (0, 5))
                Line((20, 0), (0, 0))
                Line((20, 5), (20, 0))
                Line((0, 5), (20, 5))
            make_face()
            # Profile area: 43.2991048582, perimeter: 26.6477649363
            with BuildLine():
                Line((-4, 0), (-6.6505371193, 7.2889770782))
                Line((-4, 0), (0, 0))
                Line((0, 0), (0, 5))
                Line((0, 5), (-1.5118509879, 9.1575902168))
                Line((-6.6505371193, 7.2889770782), (-1.5118509879, 9.1575902168))
            make_face()
        # Symmetric extrude, each_side=-3.5
        extrude(amount=-3.5, both=True)
    return part.part


def model_23132_1847c4ef_0008():
    """Model: SHAFT v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 85.8448806753, perimeter: 54.2984452374
            with BuildLine():
                CenterArc((-5, 5.907), 2.7, 44.359222629, 180.0003489773)
                Line((-3, 0), (-6.9304087135, 4.0192706235))
                Line((-3, 0), (3, 0))
                Line((3, 0), (6.9304087135, 4.0192706235))
                CenterArc((5, 5.907), 2.7, -44.3595716068, 180.0003489779)
                Line((0, 4.6557), (3.0695797887, 7.7947176187))
                Line((0, 4.6557), (-3.0695797887, 7.7947176187))
            make_face()
            with BuildLine():
                CenterArc((-5, 5.907), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 5.907), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.35
        extrude(amount=1.35, both=True)
    return part.part


def model_23206_b99a5251_0021():
    """Model: 0_002-a v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
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
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_23206_b99a5251_0025():
    """Model: 1_020-a v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2100000063, perimeter: 4.3141593309
            with BuildLine():
                Line((0.1, 1.0000000149), (1.0000000149, 1.0000000149))
                Line((1.0000000149, 1.0000000149), (1.0000000149, 1.1000000164))
                Line((1.0000000149, 1.1000000164), (-0.0000000015, 1.1000000164))
                CenterArc((-0.0000000015, 1.0000000164), 0.1, 90, 90)
                Line((-0.1000000015, 1.0000000164), (-0.1000000015, 0))
                Line((-0.1000000015, 0), (0, 0))
                Line((0, 0), (0, 0.9000000149))
                CenterArc((0.1, 0.9000000149), 0.1, 90, 90)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_23206_b99a5251_0037():
    """Model: 1_005-a v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.3023946399, perimeter: 27.575332235
            with BuildLine():
                Line((6, 0), (-6, 0))
                Line((6, 0), (6, 1.5))
                Line((6, 1.5), (2, 1.5))
                CenterArc((2, 3.0571427976), 1.5571427976, -146.5923661966, 56.5923661966)
                CenterArc((-0.2067891399, 3.6320038628), 1.6952121525, -82.9933683153, 25.3367804023)
                CenterArc((0.2067891399, 3.6320038628), 1.6952121525, -122.343412087, 25.3367804023)
                CenterArc((-2, 3.0571427976), 1.5571427976, -90, 56.5923661966)
                Line((-6, 1.5), (-2, 1.5))
                Line((-6, 0), (-6, 1.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_23206_b99a5251_0039():
    """Model: 0_014-a v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3117691454, perimeter: 2.0784609691
            with BuildLine():
                Line((0.1732050808, 0.3), (-0.1732050808, 0.3))
                Line((-0.1732050808, 0.3), (-0.3464101615, 0))
                Line((-0.3464101615, 0), (-0.1732050808, -0.3))
                Line((-0.1732050808, -0.3), (0.1732050808, -0.3))
                Line((0.1732050808, -0.3), (0.3464101615, 0))
                Line((0.3464101615, 0), (0.1732050808, 0.3))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_23206_b99a5251_0043():
    """Model: 0_013-a v2 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2165063509, perimeter: 1.7320508076
            with BuildLine():
                Line((0.1443375673, 0.25), (-0.1443375673, 0.25))
                Line((-0.1443375673, 0.25), (-0.2886751346, 0))
                Line((-0.2886751346, 0), (-0.1443375673, -0.25))
                Line((-0.1443375673, -0.25), (0.1443375673, -0.25))
                Line((0.1443375673, -0.25), (0.2886751346, 0))
                Line((0.2886751346, 0), (0.1443375673, 0.25))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_23206_b99a5251_0044():
    """Model: 0_008-a v2 (9)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8660254038, perimeter: 3.4641016151
            with BuildLine():
                Line((0.2886751346, 0.5), (-0.2886751346, 0.5))
                Line((-0.2886751346, 0.5), (-0.5773502692, 0))
                Line((-0.5773502692, 0), (-0.2886751346, -0.5))
                Line((-0.2886751346, -0.5), (0.2886751346, -0.5))
                Line((0.2886751346, -0.5), (0.5773502692, 0))
                Line((0.5773502692, 0), (0.2886751346, 0.5))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_23232_8853e95c_0000():
    """Model: Gear"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 7.3285206156, perimeter: 9.5965048904
            with BuildLine():
                CenterArc((0, 0), 1.5273311897, 8.2665492276, 343.4669015447)
                CenterArc((0, 0), 1.5273311897, -8.2665492276, 16.5330984553)
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3183817157, perimeter: 2.191618901
            with BuildLine():
                Line((1.5114620649, 0.2195973347), (1.7936757317, 0.2605996003))
                CenterArc((0, 0), 1.5273311897, -8.2665492276, 16.5330984553)
                Line((1.5114620649, -0.2195973347), (1.7936757317, -0.2605996003))
                _nurbs_edge([(1.7936757317, -0.2605996003), (1.8101124351, -0.2609406834), (1.8434297662, -0.2616320616), (1.8935574261, -0.2538505283), (1.9441528288, -0.2425922627), (1.9950414656, -0.2272581269), (2.0460708069, -0.2084727987), (2.0971227742, -0.1863590847), (2.1480450474, -0.1610297965), (2.1988497674, -0.132772909), (2.2318936925, -0.1117652343), (2.2485906549, -0.1011501407)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0492323485, 0.0997943702, 0.1516290107, 0.2047261251, 0.2590800153, 0.3146865285, 0.3715423122, 0.4296445365, 0.4889907697, 0.4889907697, 0.4889907697, 0.4889907697], 3)
                CenterArc((-0.0617373509, 0), 2.3125412094, -2.5069069843, 5.0138139687)
                _nurbs_edge([(1.7936757317, 0.2605996003), (1.8101124351, 0.2609406834), (1.8434297662, 0.2616320616), (1.8935574261, 0.2538505283), (1.9441528288, 0.2425922627), (1.9950414656, 0.2272581269), (2.0460708069, 0.2084727987), (2.0971227742, 0.1863590847), (2.1480450474, 0.1610297965), (2.1988497674, 0.132772909), (2.2318936925, 0.1117652343), (2.2485906549, 0.1011501407)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0492323485, 0.0997943702, 0.1516290107, 0.2047261251, 0.2590800153, 0.3146865285, 0.3715423122, 0.4296445365, 0.4889907697, 0.4889907697, 0.4889907697, 0.4889907697], 3)
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)
    return part.part


def model_23247_bcd1e84f_0004():
    """Model: Tire and Rim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.0553063333, perimeter: 53.407075111
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


def model_23255_972fbfe6_0012():
    """Model: part1 v13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 85 constraints, 34 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8104676228, perimeter: 4.8975234208
            with BuildLine():
                CenterArc((-5.4103643857, 1.2400892746), 0.7967638433, -167.2491257421, 111.1099556965)
                CenterArc((0, 0), 5, 160.8244356891, 12.5320028828)
                CenterArc((-5.4103643857, 1.2400892746), 0.7967638433, 30.3200443066, 111.1099556934)
                CenterArc((-5.4103643857, 1.2400892746), 0.7967638433, 141.43, 51.3208742579)
            make_face()
            # Profile area: 0.1839178785, perimeter: 2.2959385743
            with BuildLine():
                CenterArc((-5.4103643857, 1.2400892746), 0.7967638433, -56.1391700456, 86.4592143522)
                CenterArc((0, 0), 5, 160.8244356891, 12.5320028828)
            make_face()
            # Profile area: 67.6034368989, perimeter: 43.1865513837
            with BuildLine():
                CenterArc((5.4117849485, 1.2308873513), 0.8, 149.3247112723, 86.9779592858)
                CenterArc((0, 0), 5, 19.1356015827, 38.8026977087)
                CenterArc((2.4102803537, 4.9993048133), 0.8, -159.228769684, 86.9779592858)
                CenterArc((0, 0), 5, 70.5821206265, 38.8027091841)
                CenterArc((-2.4073962355, 5.0006942883), 0.8, -107.7822391648, 86.9779592858)
                CenterArc((0, 0), 5, 122.0286511456, 38.7957845435)
                CenterArc((-5.4103643857, 1.2400892746), 0.7967638433, -56.1391700456, 86.4592143522)
                CenterArc((0, 0), 5, 173.3564385719, 38.7957845438)
                CenterArc((-4.3450345702, -3.4529950166), 0.8, -5.0148458539, 86.9779592728)
                CenterArc((0, 0), 5, -135.2039555508, 38.8026977102)
                CenterArc((-0.0076860229, -5.549994678), 0.8, 46.4316731899, 86.9779592728)
                CenterArc((0, 0), 5, -83.757436507, 38.8026977102)
                CenterArc((4.3354540215, -3.4650163676), 0.8, 97.8781922334, 86.9779592731)
                CenterArc((0, 0), 5, -32.3109174633, 38.8026977109)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1885556767, perimeter: 2.3178229743
            with BuildLine():
                CenterArc((-0.0076860229, -5.549994678), 0.8, 46.4316731899, 86.9779592728)
                CenterArc((0, 0), 5, -96.4012578405, 12.6438213335)
            make_face()
            # Profile area: 3.1397087212, perimeter: 11.2976278725
            with BuildLine():
                CenterArc((4.3354540215, -3.4650163676), 0.8, -175.1438484935, 110.7877608347)
                CenterArc((0, 0), 5, -83.757436507, 38.8026977102)
                CenterArc((-0.0076860229, -5.549994678), 0.8, -64.356087645, 110.7877608348)
                Line((0.338535417, -6.2711955615), (4.6816754613, -4.1862172512))
            make_face()
            # Profile area: 0.1885556768, perimeter: 2.3178229746
            with BuildLine():
                CenterArc((0, 0), 5, 6.4917802476, 12.6438213351)
                CenterArc((5.4117849485, 1.2308873513), 0.8, 149.3247112723, 86.9779592858)
            make_face()
            # Profile area: 1.8220636216, perimeter: 4.9154883945
            with BuildLine():
                CenterArc((4.3354540215, -3.4650163676), 0.8, -12.9095686067, 110.7877608401)
                CenterArc((0, 0), 5, -44.9547387968, 12.6438213336)
                CenterArc((4.3354540215, -3.4650163676), 0.8, -175.1438484935, 110.7877608347)
                CenterArc((4.3354540215, -3.4650163676), 0.8, -64.3560876588, 51.4465190521)
            make_face()
            # Profile area: 1.8220636216, perimeter: 4.9154883945
            with BuildLine():
                CenterArc((-4.3450345702, -3.4529950166), 0.8, -115.8026066887, 110.7877608348)
                CenterArc((0, 0), 5, -147.8477768843, 12.6438213335)
                CenterArc((-4.3450345702, -3.4529950166), 0.8, 81.9631134188, 110.7877608348)
                CenterArc((-4.3450345702, -3.4529950166), 0.8, -167.2491257463, 51.4465190576)
            make_face()
            # Profile area: 3.1397090053, perimeter: 11.2976297151
            with BuildLine():
                CenterArc((-2.4073962355, 5.0006942883), 0.8, -20.804279879, 110.7877550975)
                CenterArc((0, 0), 5, 70.5821206265, 38.8027091841)
                CenterArc((2.4102803537, 4.9993048133), 0.8, 89.9834752185, 110.7877550975)
                Line((-2.407165506, 5.8006942551), (2.4105110832, 5.79930478))
            make_face()
            # Profile area: 0.1885556767, perimeter: 2.3178229743
            with BuildLine():
                CenterArc((4.3354540215, -3.4650163676), 0.8, 97.8781922334, 86.9779592731)
                CenterArc((0, 0), 5, -44.9547387968, 12.6438213336)
            make_face()
            # Profile area: 0.1885556768, perimeter: 2.3178229746
            with BuildLine():
                CenterArc((2.4102803537, 4.9993048133), 0.8, -159.228769684, 86.9779592858)
                CenterArc((0, 0), 5, 57.9382992914, 12.6438213351)
            make_face()
            # Profile area: 3.1366668553, perimeter: 11.2900511494
            with BuildLine():
                CenterArc((-4.3450345702, -3.4529950166), 0.8, 81.9631134188, 110.7877608348)
                CenterArc((0, 0), 5, 173.3564385719, 38.7957845438)
                CenterArc((-5.4103643857, 1.2400892746), 0.7967638433, -167.2491257421, 111.1099556965)
                Line((-6.0983905614, 0.6705464643), (-6.1874791982, 1.0642336804))
                Line((-6.0983905614, 0.6705464643), (-5.1253057324, -3.6295648705))
            make_face()
            # Profile area: 0.1885556768, perimeter: 2.3178229746
            with BuildLine():
                CenterArc((-2.4073962355, 5.0006942883), 0.8, -107.7822391648, 86.9779592858)
                CenterArc((0, 0), 5, 109.3848298106, 12.6438213351)
            make_face()
            # Profile area: 1.8220636216, perimeter: 4.9154883945
            with BuildLine():
                CenterArc((-0.0076860229, -5.549994678), 0.8, -64.356087645, 110.7877608348)
                CenterArc((0, 0), 5, -96.4012578405, 12.6438213335)
                CenterArc((-0.0076860229, -5.549994678), 0.8, 133.4096324626, 110.7877608348)
                CenterArc((-0.0076860229, -5.549994678), 0.8, -115.8026067026, 51.4465190576)
            make_face()
            # Profile area: 3.1397087214, perimeter: 11.2976278729
            with BuildLine():
                Line((6.1915640661, 1.05215703), (5.1152331392, -3.6437466889))
                CenterArc((5.4117849485, 1.2308873513), 0.8, -123.697329442, 110.7877608352)
                CenterArc((0, 0), 5, -32.3109174633, 38.8026977109)
                CenterArc((4.3354540215, -3.4650163676), 0.8, -12.9095686067, 110.7877608401)
            make_face()
            # Profile area: 1.8220636215, perimeter: 4.9154883944
            with BuildLine():
                CenterArc((-2.4073962355, 5.0006942883), 0.8, 141.43, 110.7877608352)
                CenterArc((0, 0), 5, 109.3848298106, 12.6438213351)
                CenterArc((-2.4073962355, 5.0006942883), 0.8, -20.804279879, 110.7877550975)
                CenterArc((-2.4073962355, 5.0006942883), 0.8, 89.9834752185, 51.4465247815)
            make_face()
            # Profile area: 3.1397087212, perimeter: 11.2976278725
            with BuildLine():
                CenterArc((2.4102803537, 4.9993048133), 0.8, -72.2508103982, 110.7877608352)
                CenterArc((0, 0), 5, 19.1356015827, 38.8026977087)
                CenterArc((5.4117849485, 1.2308873513), 0.8, 38.536950437, 110.7877608352)
                Line((3.0360455779, 5.4977201865), (6.0375501726, 1.7293027245))
            make_face()
            # Profile area: 4.7123889804, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1397087212, perimeter: 11.2976278725
            with BuildLine():
                CenterArc((-0.0076860229, -5.549994678), 0.8, 133.4096324626, 110.7877608348)
                CenterArc((0, 0), 5, -135.2039555508, 38.8026977102)
                CenterArc((-4.3450345702, -3.4529950166), 0.8, -115.8026066887, 110.7877608348)
                Line((-0.3559036704, -6.2702338535), (-4.6932522175, -4.1732341921))
            make_face()
            # Profile area: 1.8220636215, perimeter: 4.9154883944
            with BuildLine():
                CenterArc((5.4117849485, 1.2308873513), 0.8, 38.536950437, 110.7877608352)
                CenterArc((0, 0), 5, 6.4917802476, 12.6438213351)
                CenterArc((5.4117849485, 1.2308873513), 0.8, -123.697329442, 110.7877608352)
                CenterArc((5.4117849485, 1.2308873513), 0.8, -12.9095686067, 51.4465190438)
            make_face()
            # Profile area: 0.1885556767, perimeter: 2.3178229743
            with BuildLine():
                CenterArc((-4.3450345702, -3.4529950166), 0.8, -5.0148458539, 86.9779592728)
                CenterArc((0, 0), 5, -147.8477768843, 12.6438213335)
            make_face()
            # Profile area: 1.8220636215, perimeter: 4.9154883944
            with BuildLine():
                CenterArc((2.4102803537, 4.9993048133), 0.8, 89.9834752185, 110.7877550975)
                CenterArc((0, 0), 5, 57.9382992914, 12.6438213351)
                CenterArc((2.4102803537, 4.9993048133), 0.8, -72.2508103982, 110.7877608352)
                CenterArc((2.4102803537, 4.9993048133), 0.8, 38.536950437, 51.4465247815)
            make_face()
            # Profile area: 3.136666855, perimeter: 11.2900511494
            with BuildLine():
                CenterArc((-5.4103643857, 1.2400892746), 0.7967638433, 30.3200443066, 111.1099556934)
                CenterArc((0, 0), 5, 122.0286511456, 38.7957845435)
                CenterArc((-2.4073962355, 5.0006942883), 0.8, 141.43, 110.7877608352)
                Line((-6.0333118285, 1.7368478734), (-3.0328738578, 5.4994705348))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


def model_23264_20be13a0_0005():
    """Model: Plaque v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 317.2868536207, perimeter: 73.982345319
            with BuildLine():
                CenterArc((-0.0000009856, 8.3999997435), 6.5999992982, 46.9687928437, 86.0624209764)
                CenterArc((-11.1, 13), 6.6, -38.0123335244, 39.9614671292)
                Line((-5.9000038293, 8.9355148143), (-5.90001044, -8.935506721))
                CenterArc((-11.1000007587, -12.9999993936), 6.6, -1.9491352426, 39.9615512612)
                CenterArc((0, -8.4), 6.6, -133.0312289242, 86.0624488781)
                CenterArc((11.1, -13), 6.6, 141.9877137432, 39.9614223571)
                Line((5.9000004762, -8.9355191042), (5.9000070869, 8.9355083567))
                CenterArc((11.0999974816, 13.000000932), 6.6, 178.0508699409, 39.9615450061)
            make_face()
        # OneSide extrude, distance=-0.95
        extrude(amount=-0.95)
    return part.part


def model_23393_d47067ad_0002():
    """Model: Smoke Box SA"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 146.6946861306, perimeter: 293.3893722613
            with BuildLine():
                Line((16, -18), (16, 16))
                Line((16, 16), (-16, 16))
                Line((-16, 16), (-16, -18))
                CenterArc((0, -18), 16, 180, 180)
            make_face()
            with BuildLine():
                Line((-15, 15), (-15, -18))
                Line((15, 15), (-15, 15))
                Line((15, -18), (15, 15))
                CenterArc((0, -18), 15, 180, 180)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=7.5
        extrude(amount=7.5, both=True)
    return part.part


def model_23393_d47067ad_0009():
    """Model: TEN7&8-Stay Type 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-14.5, 0)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((14.5, 0)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-20.5, 0)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((20.5, 0)):
                Circle(0.5)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


def model_23393_d47067ad_0024():
    """Model: P11-Stay Type 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-18.25, 0)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((18.25, 0)):
                Circle(0.5)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


def model_23422_f214bd4d_0001():
    """Model: Component40"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 1.7888569779, perimeter: 4.7412487554
            with BuildLine():
                CenterArc((0, 0), 0.7545931759, 7.2244057436, 345.5511885127)
                CenterArc((0, 0), 0.7545931759, -7.2244057436, 14.4488114873)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0541695151, perimeter: 0.905519779
            with BuildLine():
                Line((0.7486026299, 0.0948944866), (0.8562710978, 0.1085427742))
                CenterArc((0, 0), 0.7545931759, -7.2244057436, 14.4488114873)
                Line((0.7486026299, -0.0948944866), (0.8562710978, -0.1085427742))
                _nurbs_edge([(0.8562710978, -0.1085427742), (0.8632679367, -0.1086038188), (0.8774316765, -0.1087273918), (0.8986966805, -0.1053561082), (0.9201289627, -0.1005938309), (0.9416627606, -0.0942073447), (0.9632462115, -0.0864531915), (0.9848384106, -0.0773852665), (1.0063857806, -0.0670523468), (1.0278968935, -0.0555720068), (1.0419287869, -0.0470633222), (1.0490132165, -0.0427674532)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0209573287, 0.0424240368, 0.0643796129, 0.0868208664, 0.1097461292, 0.1331542313, 0.1570442452, 0.1814153932, 0.2062670058, 0.2062670058, 0.2062670058, 0.2062670058], 3)
                CenterArc((-0.0194943188, 0), 1.0693630852, -2.2920636578, 4.5841273156)
                _nurbs_edge([(0.8562710978, 0.1085427742), (0.8632679367, 0.1086038188), (0.8774316765, 0.1087273918), (0.8986966805, 0.1053561082), (0.9201289627, 0.1005938309), (0.9416627606, 0.0942073447), (0.9632462115, 0.0864531915), (0.9848384106, 0.0773852665), (1.0063857806, 0.0670523468), (1.0278968935, 0.0555720068), (1.0419287869, 0.0470633222), (1.0490132165, 0.0427674532)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0209573287, 0.0424240368, 0.0643796129, 0.0868208664, 0.1097461292, 0.1331542313, 0.1570442452, 0.1814153932, 0.2062670058, 0.2062670058, 0.2062670058, 0.2062670058], 3)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_23422_f214bd4d_0003():
    """Model: Component41"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 6.2525454673, perimeter: 8.8640737601
            with BuildLine():
                CenterArc((0, 0), 1.4107611549, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.4107611549, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0578375759, perimeter: 0.9448552377
            with BuildLine():
                Line((1.4062382896, 0.1128756353), (1.4750559811, 0.1183994791))
                CenterArc((0, 0), 1.4107611549, -4.5891664191, 9.1783328383)
                Line((1.4062382896, -0.1128756353), (1.4750559811, -0.1183994791))
                _nurbs_edge([(1.4750559811, -0.1183994791), (1.483505156, -0.1182361373), (1.5005505492, -0.117906611), (1.526040453, -0.1137999393), (1.5516464448, -0.1083103051), (1.5773134514, -0.1012221694), (1.6030117284, -0.0928076893), (1.6287154851, -0.0831329629), (1.6543888208, -0.0722561182), (1.680047831, -0.0603011698), (1.6969015882, -0.051512306), (1.7053906974, -0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0253227337, 0.0510861656, 0.0772744214, 0.1038856914, 0.1309192311, 0.1583745993, 0.1862514819, 0.2145496314, 0.2432688409, 0.2432688409, 0.2432688409, 0.2432688409], 3)
                CenterArc((-0.0101317325, 0), 1.716168478, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.4750559811, 0.1183994791), (1.483505156, 0.1182361373), (1.5005505492, 0.117906611), (1.526040453, 0.1137999393), (1.5516464448, 0.1083103051), (1.5773134514, 0.1012221694), (1.6030117284, 0.0928076893), (1.6287154851, 0.0831329629), (1.6543888208, 0.0722561182), (1.680047831, 0.0603011698), (1.6969015882, 0.051512306), (1.7053906974, 0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0253227337, 0.0510861656, 0.0772744214, 0.1038856914, 0.1309192311, 0.1583745993, 0.1862514819, 0.2145496314, 0.2432688409, 0.2432688409, 0.2432688409, 0.2432688409], 3)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_23422_f214bd4d_0004():
    """Model: Component42"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 23.2957196994, perimeter: 17.1097237696
            with BuildLine():
                CenterArc((0, 0), 2.7230971129, -2.8771448737, 5.7542897473)
                CenterArc((0, 0), 2.7230971129, 2.8771448737, 354.2457102527)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0611265843, perimeter: 0.9989514051
            with BuildLine():
                _nurbs_edge([(2.7196645376, -0.1366846334), (2.7276636183, -0.1363625218), (2.7471573159, -0.1353333771), (2.7780131088, -0.1304910531), (2.8122985653, -0.1235545106), (2.8466231994, -0.1148145121), (2.8809680971, -0.1045932701), (2.9153139644, -0.0929755973), (2.949631837, -0.0800350902), (2.9839437096, -0.0659188802), (3.0065737653, -0.0556001911), (3.0179528082, -0.0504116575)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0101132529, 0.0101132529, 0.0101132529, 0.0101132529, 0.0341156048, 0.0686713391, 0.1036519071, 0.1390557787, 0.1748824128, 0.2111315343, 0.2478029727, 0.2848966074, 0.3224123462, 0.3224123462, 0.3224123462, 0.3224123462], 3)
                CenterArc((-0.0079912319, 0), 3.0263639353, -0.9544485951, 1.9088971902)
                _nurbs_edge([(2.7196645376, 0.1366846334), (2.7276636183, 0.1363625218), (2.7471573159, 0.1353333771), (2.7780131088, 0.1304910531), (2.8122985653, 0.1235545106), (2.8466231994, 0.1148145121), (2.8809680971, 0.1045932701), (2.9153139644, 0.0929755973), (2.949631837, 0.0800350902), (2.9839437096, 0.0659188802), (3.0065737653, 0.0556001911), (3.0179528082, 0.0504116575)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0101132529, 0.0101132529, 0.0101132529, 0.0101132529, 0.0341156048, 0.0686713391, 0.1036519071, 0.1390557787, 0.1748824128, 0.2111315343, 0.2478029727, 0.2848966074, 0.3224123462, 0.3224123462, 0.3224123462, 0.3224123462], 3)
                CenterArc((0, 0), 2.7230971129, -2.8771448737, 5.7542897473)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_23422_f214bd4d_0005():
    """Model: Component43"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 37.2819436327, perimeter: 21.6448312747
            with BuildLine():
                CenterArc((0, 0), 3.4448818898, -2.3829886658, 4.7659773315)
                CenterArc((0, 0), 3.4448818898, 2.3829886658, 355.2340226685)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0618437671, perimeter: 1.0146552284
            with BuildLine():
                _nurbs_edge([(3.4419028217, -0.1432347735), (3.4499588955, -0.1421436438), (3.4711203435, -0.1386914937), (3.5053073456, -0.1319131603), (3.5444449302, -0.1222034641), (3.5836001562, -0.1108908252), (3.6227545597, -0.0980700532), (3.6618796547, -0.0838231946), (3.7010000194, -0.0683119305), (3.7268260312, -0.0569902561), (3.7398064277, -0.0512998761)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0539960479, 0.0539960479, 0.0539960479, 0.0539960479, 0.0783812372, 0.1182460613, 0.158553493, 0.1993029954, 0.2404943049, 0.2821272635, 0.3242017638, 0.366717726, 0.366717726, 0.366717726, 0.366717726], 3)
                CenterArc((-0.0082841834, 0), 3.7484416637, -0.7841546999, 1.5683093997)
                _nurbs_edge([(3.4419028217, 0.1432347735), (3.4499588955, 0.1421436438), (3.4711203435, 0.1386914937), (3.5053073456, 0.1319131603), (3.5444449302, 0.1222034641), (3.5836001562, 0.1108908252), (3.6227545597, 0.0980700532), (3.6618796547, 0.0838231946), (3.7010000194, 0.0683119305), (3.7268260312, 0.0569902561), (3.7398064277, 0.0512998761)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0539960479, 0.0539960479, 0.0539960479, 0.0539960479, 0.0783812372, 0.1182460613, 0.158553493, 0.1993029954, 0.2404943049, 0.2821272635, 0.3242017638, 0.366717726, 0.366717726, 0.366717726, 0.366717726], 3)
                CenterArc((0, 0), 3.4448818898, -2.3829886658, 4.7659773315)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_23422_f214bd4d_0006():
    """Model: Component45"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 3.6825430037, perimeter: 6.8026612578
            with BuildLine():
                CenterArc((0, 0), 1.0826771654, 5.5643725728, 348.8712548545)
                CenterArc((0, 0), 1.0826771654, -5.5643725728, 11.1287451455)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.056294837, perimeter: 0.9273185649
            with BuildLine():
                Line((1.0775754673, 0.1049807441), (1.1659598783, 0.1135914275))
                CenterArc((0, 0), 1.0826771654, -5.5643725728, 11.1287451455)
                Line((1.0775754673, -0.1049807441), (1.1659598783, -0.1135914275))
                _nurbs_edge([(1.1659598783, -0.1135914275), (1.1736811819, -0.1135189171), (1.1892779919, -0.1133724482), (1.2126303462, -0.1096069851), (1.2361161341, -0.1044730266), (1.2596770201, -0.0977512969), (1.2832757784, -0.0897047475), (1.3068816068, -0.0803940997), (1.3304527967, -0.0698732545), (1.3540028133, -0.058262121), (1.3694329308, -0.0496997431), (1.3772120947, -0.0453829814)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0231339989, 0.046730009, 0.0707708305, 0.0952542856, 0.1201793886, 0.145545509, 0.1713521734, 0.1975989954, 0.2242856464, 0.2242856464, 0.2242856464, 0.2242856464], 3)
                CenterArc((-0.012806993, 0), 1.3907597489, -1.8699958744, 3.7399917488)
                _nurbs_edge([(1.1659598783, 0.1135914275), (1.1736811819, 0.1135189171), (1.1892779919, 0.1133724482), (1.2126303462, 0.1096069851), (1.2361161341, 0.1044730266), (1.2596770201, 0.0977512969), (1.2832757784, 0.0897047475), (1.3068816068, 0.0803940997), (1.3304527967, 0.0698732545), (1.3540028133, 0.058262121), (1.3694329308, 0.0496997431), (1.3772120947, 0.0453829814)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0231339989, 0.046730009, 0.0707708305, 0.0952542856, 0.1201793886, 0.145545509, 0.1713521734, 0.1975989954, 0.2242856464, 0.2242856464, 0.2242856464, 0.2242856464], 3)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_23422_f214bd4d_0007():
    """Model: Component44"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 47.8865853771, perimeter: 24.530808778
            with BuildLine():
                CenterArc((0, 0), 3.9041994751, -2.1381356465, 4.276271293)
                CenterArc((0, 0), 3.9041994751, 2.1381356465, 355.723728707)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0621481643, perimeter: 1.0206302861
            with BuildLine():
                _nurbs_edge([(3.9014813036, -0.1456611774), (3.9022795916, -0.1455235671), (3.9172013478, -0.1429315942), (3.9462623728, -0.1372278881), (3.9884696249, -0.126890204), (4.030693317, -0.1148667302), (4.0729151694, -0.1012586404), (4.1151065769, -0.0861533849), (4.1572937128, -0.0697222013), (4.185156159, -0.0577373219), (4.1991572843, -0.0517148141)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.082137056, 0.082137056, 0.082137056, 0.082137056, 0.0845657348, 0.1275457326, 0.1709834139, 0.2148782345, 0.2592299309, 0.3040383479, 0.3493033814, 0.3950249553, 0.3950249553, 0.3950249553, 0.3950249553], 3)
                CenterArc((-0.008643626, 0), 4.2081186916, -0.7041424906, 1.4082849813)
                _nurbs_edge([(3.9014813036, 0.1456611774), (3.9022795916, 0.1455235671), (3.9172013478, 0.1429315942), (3.9462623728, 0.1372278881), (3.9884696249, 0.126890204), (4.030693317, 0.1148667302), (4.0729151694, 0.1012586404), (4.1151065769, 0.0861533849), (4.1572937128, 0.0697222013), (4.185156159, 0.0577373219), (4.1991572843, 0.0517148141)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.082137056, 0.082137056, 0.082137056, 0.082137056, 0.0845657348, 0.1275457326, 0.1709834139, 0.2148782345, 0.2592299309, 0.3040383479, 0.3493033814, 0.3950249553, 0.3950249553, 0.3950249553, 0.3950249553], 3)
                CenterArc((0, 0), 3.9041994751, -2.1381356465, 4.276271293)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


def model_23554_a0845d54_0004():
    """Model: Pistone small v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_23681_932e722e_0002():
    """Model: lockwasher v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8633820375, perimeter: 8.9270725049
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 99.5603836944, 340.8792326112)
                CenterArc((0, 0.6), 0.1, -4.7801918472, 189.5603836944)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1158213342, perimeter: 3.8671522245
            with BuildLine():
                CenterArc((0, 0.6), 0.1, -175.2198081528, 170.4396163056)
                CenterArc((0, 0), 0.6, 99.5603836944, 340.8792326112)
            make_face()
        # Symmetric extrude, each_side=0.025
        extrude(amount=0.025, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1158213342, perimeter: 3.8671522245
            with BuildLine():
                CenterArc((0, 0.6), 0.1, -175.2198081528, 170.4396163056)
                CenterArc((0, 0), 0.6, 99.5603836944, 340.8792326112)
            make_face()
        # Symmetric extrude, each_side=0.025
        extrude(amount=0.025, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_23706_ef15ef9c_0000():
    """Model: Rozrzutnik oleju duży v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7, perimeter: 8.4828427125
            with BuildLine():
                Line((-0.6, 6), (0, 6))
                Line((-0.6, 5), (-0.6, 6))
                Line((-0.4, 4.8), (-0.6, 5))
                Line((-0.4, 2.3), (-0.4, 4.8))
                Line((0, 2.3), (-0.4, 2.3))
                Line((0, 6), (0, 2.3))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_23706_ef15ef9c_0001():
    """Model: Korpus v14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 168.9012385966, perimeter: 76.6265482457
            with BuildLine():
                Line((-17, -4.4), (-17, -7.8))
                CenterArc((-15.4, -7.8), 1.6, -180, 90)
                Line((-15.4, -9.4), (15.4, -9.4))
                CenterArc((15.4, -7.8), 1.6, -90, 90)
                Line((17, -7.8), (17, -4.4))
                Line((-17, -4.4), (17, -4.4))
            make_face()
            # Profile area: 168.9012385966, perimeter: 76.6265482457
            with BuildLine():
                Line((17, 4.4), (-17, 4.4))
                Line((17, 4.4), (17, 7.8))
                CenterArc((15.4, 7.8), 1.6, 0, 90)
                Line((15.4, 9.4), (-15.4, 9.4))
                CenterArc((-15.4, 7.8), 1.6, 90, 90)
                Line((-17, 7.8), (-17, 4.4))
            make_face()
        # OneSide extrude, distance=1.85
        extrude(amount=1.85)
    return part.part


def model_23706_ef15ef9c_0004():
    """Model: Pokrywa wziernika v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 66, perimeter: 32.6
            with BuildLine():
                Line((3.75, -4.4), (3.75, 4.4))
                Line((3.75, 4.4), (-3.75, 4.4))
                Line((-3.75, 4.4), (-3.75, -4.4))
                Line((-3.75, -4.4), (3.75, -4.4))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_23787_1304fb90_0000():
    """Model: The Middliest Middle v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 392.2743338823, perimeter: 74.8495559215
            with BuildLine():
                CenterArc((7, -7), 3, -90, 90)
                Line((10, -7), (10, 7))
                CenterArc((7, 7), 3, 0, 90)
                Line((7, 10), (-7, 10))
                CenterArc((-7, 7), 3, 90, 90)
                Line((-10, 7), (-10, -7))
                CenterArc((-7, -7), 3, -180, 90)
                Line((-7, -10), (7, -10))
            make_face()
        # Symmetric extrude, each_side=9
        extrude(amount=9, both=True)
    return part.part


def model_23790_2abde9b6_0008():
    """Model: CAIXA DE PROTECAO v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36.48, perimeter: 26.8
            with BuildLine():
                Line((0, 3.8), (0, 0))
                Line((0, 0), (9.6, 0))
                Line((9.6, 0), (9.6, 3.8))
                Line((0, 3.8), (9.6, 3.8))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)
    return part.part


def model_23856_6be75f62_0007():
    """Model: Landskap1 v2"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 125853352986.6401062012, perimeter: 1440402.3259778968
            with BuildLine():
                Line((149152.1468050292, -210948.702223441), (-149149.7631339954, -210948.702223441))
                Line((149152.1468050292, 210950.5508264827), (149152.1468050292, -210948.702223441))
                Line((-149149.7631339954, 210950.5508264827), (149152.1468050292, 210950.5508264827))
                Line((-149149.7631339954, -210948.702223441), (-149149.7631339954, 210950.5508264827))
            make_face()
        # OneSide extrude, distance=-2000
        extrude(amount=-2000)
    return part.part


def model_23956_ee17fe48_0014():
    """Model: 2340 - A - 18x50ISO v2 (2)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_24032_d6172503_0030():
    """Model: right torion spring v3 v2"""
    with BuildPart() as part:
        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1652546402, perimeter: 1.4410590044
            with Locations((-10, 0)):
                Circle(0.2293516638)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_24047_9eb475f0_0004():
    """Model: Connecting rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.4312624491, perimeter: 18.9356041417
            with BuildLine():
                CenterArc((0, -17), 2, 120, 300)
                Line((1, -15.8819660113), (1, -15.2679491924))
                CenterArc((0, -17), 1.5, 131.8103148958, 276.3793702084)
                Line((-1, -15.2679491924), (-1, -15.8819660113))
            make_face()
            # Profile area: 1.1780972451, perimeter: 5.7123889804
            with BuildLine():
                CenterArc((0, 3), 1, 180, 180)
                Line((1, 3), (0.5, 3))
                CenterArc((0, 3), 0.5, 180, 180)
                Line((-0.5, 3), (-1, 3))
            make_face()
            # Profile area: 1.1780972451, perimeter: 5.7123889804
            with BuildLine():
                Line((-0.5, 3), (-1, 3))
                CenterArc((0, 3), 0.5, 0, 180)
                Line((1, 3), (0.5, 3))
                CenterArc((0, 3), 1, 0, 180)
            make_face()
            # Profile area: 1.0665246947, perimeter: 5.5116117087
            with BuildLine():
                Line((-1, -15.2679491924), (-1, -15.8819660113))
                CenterArc((0, -17), 1.5, 48.1896851042, 83.6206297916)
                Line((1, -15.8819660113), (1, -15.2679491924))
                CenterArc((0, -17), 2, 60, 60)
            make_face()
            # Profile area: 34.6027577632, perimeter: 41.7718861408
            with BuildLine():
                CenterArc((0, -17), 2, 60, 60)
                Line((1, -15.2679491924), (1, 3))
                CenterArc((0, 3), 1, 180, 180)
                Line((-1, 3), (-1, -15.2679491924))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_24051_4852a192_0001():
    """Model: 60BRS"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9820230334, perimeter: 12.8874413836
            with BuildLine():
                CenterArc((0, 0), 1.10175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.94935, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4554143189, perimeter: 5.9765658642
            with BuildLine():
                CenterArc((0, 0), 0.5518, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3994, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3505
        extrude(amount=0.3505, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8748465203, perimeter: 9.4320036239
            with BuildLine():
                CenterArc((0, 0), 0.94935, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5518, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3251
        extrude(amount=0.3251, both=True, mode=Mode.ADD)
    return part.part


def model_24051_4852a192_0002():
    """Model: Bearing Sleave"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1828729293, perimeter: 14.8462244031
            with BuildLine():
                CenterArc((0, 0), 1.2611, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.10175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7849
        extrude(amount=0.7849)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3900905549, perimeter: 11.1517114424
            with BuildLine():
                CenterArc((0, 0), 1.10175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6731, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1346
        extrude(amount=0.1346, mode=Mode.ADD)
    return part.part


def model_24131_3ea7d5a8_0012():
    """Model: Cylinder Bearing v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7719371752, perimeter: 6.4834618388
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_24195_9791f5d3_0005():
    """Model: Outer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1074114104, perimeter: 14.7654854719
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8168140899, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True, mode=Mode.ADD)
    return part.part


def model_24195_9791f5d3_0040():
    """Model: Outer (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274123, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3141592654, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True, mode=Mode.ADD)
    return part.part


def model_24195_9791f5d3_0042():
    """Model: CF Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 43 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1037190195, perimeter: 10.0122124395
            with BuildLine():
                Line((-0.725, 0.2), (-0.725, -0.2))
                Line((-0.725, -0.2), (-0.8422359313, -0.3172359313))
                CenterArc((0, 0), 0.9, -159.3606543397, 17.9911772663)
                CenterArc((-0.6363961031, -0.6363961031), 0.1, -41.8152614633, 173.6305229266)
                CenterArc((0, 0), 0.9, -128.6305229266, 17.9911772663)
                Line((-0.2, -0.725), (-0.3172359313, -0.8422359313))
                Line((-0.2, -0.725), (0.2, -0.725))
                Line((0.2, -0.725), (0.3172359313, -0.8422359313))
                CenterArc((0, 0), 0.9, -69.3606543397, 17.9911772663)
                CenterArc((0.6363961031, -0.6363961031), 0.1, 48.1847385367, 173.6305229266)
                CenterArc((0, 0), 0.9, -38.6305229266, 17.9911772663)
                Line((0.725, -0.2), (0.8422359313, -0.3172359313))
                Line((0.725, -0.2), (0.725, 0.2))
                Line((0.725, 0.2), (0.8422359313, 0.3172359313))
                CenterArc((0, 0), 0.9, 20.6393456603, 17.9911772663)
                CenterArc((0.6363961031, 0.6363961031), 0.1, 138.1847385367, 173.6305229266)
                CenterArc((0, 0), 0.9, 51.3694770734, 17.9911772663)
                Line((0.2, 0.725), (0.3172359313, 0.8422359313))
                Line((0.2, 0.725), (-0.2, 0.725))
                Line((-0.2, 0.725), (-0.3172359313, 0.8422359313))
                CenterArc((0, 0), 0.9, 110.6393456603, 17.9911772663)
                CenterArc((-0.6363961031, 0.6363961031), 0.1, -131.8152614633, 173.6305229266)
                CenterArc((0, 0), 0.9, 141.3694770734, 17.9911772663)
                Line((-0.725, 0.2), (-0.8422359313, 0.3172359313))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)
    return part.part


def model_24238_df51962d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch58 -> Extrude15 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0589048623, perimeter: 0.9926990817
            with BuildLine():
                CenterArc((-0.4328488673, 3.6472999558), 0.3, 105, 75)
                Line((-0.4328488673, 3.6472999558), (-0.7328488673, 3.6472999558))
                Line((-0.4328488673, 3.6472999558), (-0.5104945808, 3.9370777037))
            make_face()
            # Profile area: 24.2826371259, perimeter: 28.0273153263
            with BuildLine():
                Line((-0.4000000104, -4.7386000373), (-0.5500000104, -4.9984076584))
                Line((-0.5500000104, -4.9984076584), (0.345722879, -5.6242750269))
                Line((0.345722879, -5.6242750269), (0.5999999896, -5.8019457641))
                Line((1.4999999896, -4.2431000373), (0.5999999896, -5.8019457641))
                Line((1.4999999896, -4.2431000373), (3.2999999896, -4.2431000373))
                Line((3.2999999896, -4.2431000373), (3.2999171223, -4.225828229))
                Line((3.2999171223, -4.225828229), (3.2671511327, 2.6034999558))
                Line((1.4671511327, 2.6034999558), (3.2671511327, 2.6034999558))
                Line((1.4671511327, 2.6034999558), (1.0012768515, 4.3421664431))
                CenterArc((1.4671511327, 2.6034999558), 1.8, 105, 0.0007641654)
                Line((-0.5104945808, 3.9370777037), (1.0012536626, 4.3421602295))
                Line((-0.4328488673, 3.6472999558), (-0.5104945808, 3.9370777037))
                Line((-0.4328488673, 3.6472999558), (-0.7328488673, 3.6472999558))
                Line((-0.7328488673, 3.6472999558), (-0.6996087131, 2.6631728464))
                CenterArc((-0.3997796924, 2.6732999558), 0.3, -178.0654970531, 77.3046779387)
                CenterArc((-0.6997796924, 0.9999999558), 1.4, 79.7078233343, 0.2556175476)
                CenterArc((-0.6997796924, 0.9999999558), 1.4, -1.0164929506, 80.7243162849)
                Line((0.6999999896, 0.9751636504), (0.6999999896, -2.5000000373))
                CenterArc((-0.7000000104, -2.5000000373), 1.4, -79.7078233343, 79.7078233343)
                CenterArc((-0.7000000104, -2.5000000373), 1.4, -79.9634408819, 0.2556175476)
                CenterArc((-0.4000000104, -4.1733000373), 0.3, 100.7608191144, 79.2391808856)
                Line((-0.7000000104, -4.1733000373), (-0.7000000104, -4.7386000373))
                Line((-0.4000000104, -4.7386000373), (-0.7000000104, -4.7386000373))
            make_face()
            with BuildLine():
                CenterArc((1.4999999896, -4.2431000373), 1.8, -173.3494609532, 0.2954714953)
                CenterArc((-0.4000000104, -4.7386000373), 0.3, 67.8291278304, 2.5895346482)
                CenterArc((-0.4000000104, -4.1733000373), 0.3, -70.4186624786, 2.3631045324)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.9688050576, perimeter: 6.8986722863
            with BuildLine():
                CenterArc((1.4671511327, 2.6034999558), 1.8, 0, 105)
                Line((1.4671511327, 2.6034999558), (1.0012768515, 4.3421664431))
                Line((1.4671511327, 2.6034999558), (3.2671511327, 2.6034999558))
            make_face()
            # Profile area: 0.0471238898, perimeter: 0.9141592654
            with BuildLine():
                Line((-0.4000000104, -4.7386000373), (-0.7000000104, -4.7386000373))
                CenterArc((-0.4000000104, -4.7386000373), 0.3, 180, 60)
                Line((-0.4000000104, -4.7386000373), (-0.5500000104, -4.9984076584))
            make_face()
            # Profile area: 3.3929200659, perimeter: 7.3699111843
            with BuildLine():
                CenterArc((1.4999999896, -4.2431000373), 1.8, -120, 120)
                Line((1.4999999896, -4.2431000373), (3.2999999896, -4.2431000373))
                Line((1.4999999896, -4.2431000373), (0.5999999896, -5.8019457641))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_24284_3710e946_0010():
    """Model: plaque 1_D‚faut v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.032236, perimeter: 15.3924
            with BuildLine():
                Line((-2.8956, 0.9525), (2.8956, 0.9525))
                Line((-2.8956, -0.9525), (-2.8956, 0.9525))
                Line((2.8956, -0.9525), (-2.8956, -0.9525))
                Line((2.8956, 0.9525), (2.8956, -0.9525))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_24300_ed2686dc_0012():
    """Model: wkretka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0392699082, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_24302_2bcddd22_0002():
    """Model: PIN"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0105683177, perimeter: 0.3644247478
            Circle(0.058)
        # OneSide extrude, distance=1.016
        extrude(amount=1.016)
    return part.part


def model_24308_89c2be2b_0004():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2798292053, perimeter: 1.8752166549
            with Locations((-6.3500002027, 0)):
                Circle(0.29845)
        # OneSide extrude, distance=3.3274
        extrude(amount=3.3274)
    return part.part


def model_24357_8d7d40b1_0002():
    """Model: kolumna up"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.92, perimeter: 6.4
            with BuildLine():
                Line((0.4, -2), (-0.4, -2))
                Line((-0.4, -2), (-0.4, -4.4))
                Line((-0.4, -4.4), (0.4, -4.4))
                Line((0.4, -4.4), (0.4, -2))
            make_face()
        # Symmetric extrude, each_side=1.1
        extrude(amount=1.1, both=True)
    return part.part


def model_24405_b96b34b6_0011():
    """Model: Pieza 5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9409565876, perimeter: 25.6048026557
            with BuildLine():
                CenterArc((2.92, -0.17), 2.62, -145.4961798628, 55.4961798628)
                CenterArc((0.89, -2.69), 1.0438869671, 97.1047399401, 3.4452403941)
                CenterArc((0.46, -1.59), 0.25, -17.1597804749, 257.0215214452)
                CenterArc((0.89, -2.69), 1.0438869671, 122.151980161, 80.9745402277)
                Line((-0.07, -3.1), (3.53, -3.1))
                Line((3.53, -3.1), (3.73, -3.7))
                Line((3.73, -3.7), (7.8, -3.7))
                CenterArc((7.8, -2.85), 0.85, -90, 180)
                Line((7.1363794895, -1.9702856488), (7.8, -2))
                CenterArc((5.9, -1.68), 1.27, -96.1466650221, 82.9336876974)
                Line((2.92, -2.79), (5.7640161689, -2.9426988547))
            make_face()
            with BuildLine():
                CenterArc((0.46, -1.59), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.35, -3.4), 0.125, 7.357616281, 345.2847681047)
                CenterArc((5.3502978633, -3.4), 0.1247045951, -7.3751413923, 14.7502834529)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.65, -2.77), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.25, -3.4), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.81, -2.43), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_24407_2d357602_0002():
    """Model: Pin v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


def model_24409_62adef9c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4417.8646691106, perimeter: 235.6194490192
            Circle(37.5)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_24412_a8e106be_0008():
    """Model: Kurbelwelle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)
    return part.part


def model_24518_b99235fc_0000():
    """Model: Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2643.4267247101, perimeter: 530.0980099478
            with BuildLine():
                CenterArc((0, 0), 91.44, 58.1092081982, 51.3620124363)
                CenterArc((-28.7655131904, 81.3611577651), 5.1434604287, 109.4712206345, 179.9999991462)
                CenterArc((0, 0), 81.1530791426, 58.1092081982, 51.3620124363)
                Line((42.87332483, 68.9035577626), (129.1374757734, 15.2280860645))
                CenterArc((182.88, 101.6), 101.7269208574, -121.8907918018, 41.4848600287)
                CenterArc((198.9772434048, 6.3674237293), 5.1434604287, -80.4059317731, 180)
                CenterArc((182.88, 101.6), 91.44, -121.8907918018, 41.4848600287)
                Line((48.3079245283, 77.6377358491), (134.5720754717, 23.9622641509))
            make_face()
        # Symmetric extrude, each_side=3.175
        extrude(amount=3.175, both=True)
    return part.part


def model_24643_71176e22_0000():
    """Model: Component13"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 7.8757982496, perimeter: 9.9483767364
            with BuildLine():
                CenterArc((0, 0), 1.5833333333, -2.5887690372, 5.1775380744)
                CenterArc((0, 0), 1.5833333333, 2.5887690372, 354.8224619256)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0158882614, perimeter: 0.5124161793
            with BuildLine():
                _nurbs_edge([(1.5817174507, -0.0715146886), (1.582184396, -0.0714739659), (1.5889223658, -0.0708586703), (1.6019306275, -0.0688317669), (1.6206816736, -0.0650824307), (1.6394511693, -0.0603753981), (1.6582301617, -0.0548829775), (1.677009132, -0.0486510247), (1.6957735639, -0.041719265), (1.7145353547, -0.0341664291), (1.7269165944, -0.0286503108), (1.7331406152, -0.0258773708)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0172661483, 0.0172661483, 0.0172661483, 0.0172661483, 0.0186730354, 0.0375747448, 0.0566972065, 0.0760396378, 0.0956017665, 0.1153834573, 0.1353846279, 0.1556052215, 0.1760451953, 0.1760451953, 0.1760451953, 0.1760451953], 3)
                CenterArc((-0.0041144976, 0), 1.737447831, -0.8533890489, 1.7067780978)
                _nurbs_edge([(1.5817174507, 0.0715146886), (1.582184396, 0.0714739659), (1.5889223658, 0.0708586703), (1.6019306275, 0.0688317669), (1.6206816736, 0.0650824307), (1.6394511693, 0.0603753981), (1.6582301617, 0.0548829775), (1.677009132, 0.0486510247), (1.6957735639, 0.041719265), (1.7145353547, 0.0341664291), (1.7269165944, 0.0286503108), (1.7331406152, 0.0258773708)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0172661483, 0.0172661483, 0.0172661483, 0.0172661483, 0.0186730354, 0.0375747448, 0.0566972065, 0.0760396378, 0.0956017665, 0.1153834573, 0.1353846279, 0.1556052215, 0.1760451953, 0.1760451953, 0.1760451953, 0.1760451953], 3)
                CenterArc((0, 0), 1.5833333333, -2.5887690372, 5.1775380744)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_24643_71176e22_0001():
    """Model: Component11"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 0.7648657668, perimeter: 3.1002559081
            with BuildLine():
                CenterArc((0, 0), 0.4934210526, 9.71137289, 340.5772542201)
                CenterArc((0, 0), 0.4934210526, -9.71137289, 19.4227457799)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.051882835, perimeter: 0.8833013663
            with BuildLine():
                Line((0.4863503316, 0.0832327465), (0.6090983502, 0.1042395271))
                CenterArc((0, 0), 0.4934210526, -9.71137289, 19.4227457799)
                Line((0.4863503316, -0.0832327465), (0.6090983502, -0.1042395271))
                _nurbs_edge([(0.6090983502, -0.1042395271), (0.6155360094, -0.1044851535), (0.6286092322, -0.1049839573), (0.6483457189, -0.1020453922), (0.6683093536, -0.0976374782), (0.6884203059, -0.09149744), (0.7086001758, -0.0838796833), (0.7287893151, -0.0748292913), (0.7489120405, -0.064388735), (0.7689673951, -0.0526767178), (0.7819567712, -0.0439319756), (0.788527036, -0.0395087246)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192879284, 0.0391687999, 0.0596143618, 0.0806186169, 0.1021779272, 0.124289545, 0.1469512196, 0.1701610478, 0.1939174078, 0.1939174078, 0.1939174078, 0.1939174078], 3)
                CenterArc((-0.0354554549, 0), 0.8249291391, -2.7451442316, 5.4902884632)
                _nurbs_edge([(0.6090983502, 0.1042395271), (0.6155360094, 0.1044851535), (0.6286092322, 0.1049839573), (0.6483457189, 0.1020453922), (0.6683093536, 0.0976374782), (0.6884203059, 0.09149744), (0.7086001758, 0.0838796833), (0.7287893151, 0.0748292913), (0.7489120405, 0.064388735), (0.7689673951, 0.0526767178), (0.7819567712, 0.0439319756), (0.788527036, 0.0395087246)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192879284, 0.0391687999, 0.0596143618, 0.0806186169, 0.1021779272, 0.124289545, 0.1469512196, 0.1701610478, 0.1939174078, 0.1939174078, 0.1939174078, 0.1939174078], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_24650_dad8c8ee_0000():
    """Model: Component3"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 4.6663695567, perimeter: 7.6576320931
            with BuildLine():
                CenterArc((0, 0), 1.21875, 4.926553838, 350.1468923239)
                CenterArc((0, 0), 1.21875, -4.926553838, 9.8531076761)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0519599585, perimeter: 0.893609733
            with BuildLine():
                Line((1.2142474531, 0.1046646316), (1.2872683736, 0.1109588245))
                CenterArc((0, 0), 1.21875, -4.926553838, 9.8531076761)
                Line((1.2142474531, -0.1046646316), (1.2872683736, -0.1109588245))
                _nurbs_edge([(1.2872683736, -0.1109588245), (1.2950386046, -0.1108348201), (1.3107212122, -0.1105845428), (1.3341823697, -0.1067997971), (1.3577595776, -0.1017061232), (1.3813994276, -0.0950975356), (1.4050712141, -0.0872295028), (1.4287488004, -0.0781630196), (1.4523961826, -0.0679518914), (1.4760278226, -0.0567125385), (1.4915367499, -0.0484408572), (1.4993510039, -0.0442731274)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.023285125, 0.0469962191, 0.0711177793, 0.0956479765, 0.1205860327, 0.1459314737, 0.171683955, 0.1978432009, 0.2244089796, 0.2244089796, 0.2244089796, 0.2244089796], 3)
                CenterArc((-0.0104334792, 0), 1.5104334792, -1.6796679612, 3.3593359224)
                _nurbs_edge([(1.2872683736, 0.1109588245), (1.2950386046, 0.1108348201), (1.3107212122, 0.1105845428), (1.3341823697, 0.1067997971), (1.3577595776, 0.1017061232), (1.3813994276, 0.0950975356), (1.4050712141, 0.0872295028), (1.4287488004, 0.0781630196), (1.4523961826, 0.0679518914), (1.4760278226, 0.0567125385), (1.4915367499, 0.0484408572), (1.4993510039, 0.0442731274)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.023285125, 0.0469962191, 0.0711177793, 0.0956479765, 0.1205860327, 0.1459314737, 0.171683955, 0.1978432009, 0.2244089796, 0.2244089796, 0.2244089796, 0.2244089796], 3)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_24724_c71e66b3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.4149781904, perimeter: 15.2121478035
            Circle(2.421088518)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


def model_24890_5f8a67df_0005():
    """Model: End Cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.8174574075, perimeter: 61.8422513859
            with BuildLine():
                CenterArc((0, 0), 5.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.7625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.1840730586, perimeter: 57.8524287159
            with BuildLine():
                CenterArc((0, 0), 4.7625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.445, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 62.0716661894, perimeter: 27.9287586904
            Circle(4.445)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.1840730586, perimeter: 57.8524287159
            with BuildLine():
                CenterArc((0, 0), 4.7625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.445, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)
    return part.part


def model_24896_58b4730f_0000():
    """Model: kolo zebate"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 8.0173640869, perimeter: 10.0373885282
            with BuildLine():
                CenterArc((0, 0), 1.5975, 3.2172951022, 353.5654097956)
                CenterArc((0, 0), 1.5975, -3.2172951022, 6.4345902044)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0284567818, perimeter: 0.6756837151
            with BuildLine():
                Line((1.5949821301, 0.089656314), (1.6043337276, 0.0901819812))
                CenterArc((0, 0), 1.5975, -3.2172951022, 6.4345902044)
                Line((1.5949821301, -0.089656314), (1.6043337276, -0.0901819812))
                _nurbs_edge([(1.6043337276, -0.0901819812), (1.6115317129, -0.0899501426), (1.6260267307, -0.0894832752), (1.6476767619, -0.0860586279), (1.6693930806, -0.0816033329), (1.6911389274, -0.075963141), (1.7129000841, -0.0693478145), (1.7346626793, -0.061811763), (1.7564062672, -0.0534023086), (1.7781449043, -0.0442151671), (1.7924715059, -0.0374919243), (1.7996777672, -0.0341101422)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0215852599, 0.0434675415, 0.0656364718, 0.0880909935, 0.110830723, 0.13385546, 0.1571650762, 0.180759479, 0.2046385954, 0.2046385954, 0.2046385954, 0.2046385954], 3)
                CenterArc((-0.0055358276, 0), 1.8055358276, -1.082494975, 2.1649899499)
                _nurbs_edge([(1.6043337276, 0.0901819812), (1.6115317129, 0.0899501426), (1.6260267307, 0.0894832752), (1.6476767619, 0.0860586279), (1.6693930806, 0.0816033329), (1.6911389274, 0.075963141), (1.7129000841, 0.0693478145), (1.7346626793, 0.061811763), (1.7564062672, 0.0534023086), (1.7781449043, 0.0442151671), (1.7924715059, 0.0374919243), (1.7996777672, 0.0341101422)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0215852599, 0.0434675415, 0.0656364718, 0.0880909935, 0.110830723, 0.13385546, 0.1571650762, 0.180759479, 0.2046385954, 0.2046385954, 0.2046385954, 0.2046385954], 3)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_24896_58b4730f_0002():
    """Model: tuleja lozyskowa zewnetrzna"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.58
        extrude(amount=-0.58)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6597344573, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.33
        extrude(amount=-0.33, mode=Mode.ADD)
    return part.part


def model_24896_58b4730f_0017():
    """Model: zebnik"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 0.9940195505, perimeter: 3.5342917353
            with BuildLine():
                CenterArc((0, 0), 0.5625, 6.8054379143, 346.3891241714)
                CenterArc((0, 0), 0.5625, -6.8054379143, 13.6108758286)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0257087215, perimeter: 0.624362779
            with BuildLine():
                Line((0.5585367746, 0.0666552429), (0.6297595862, 0.0751549049))
                CenterArc((0, 0), 0.5625, -6.8054379143, 13.6108758286)
                Line((0.5585367746, -0.0666552429), (0.6297595862, -0.0751549049))
                _nurbs_edge([(0.6297595862, -0.0751549049), (0.6346571366, -0.0751746175), (0.6445659364, -0.0752145002), (0.6594312898, -0.072842976), (0.6744051928, -0.0695236767), (0.6894439439, -0.0650994737), (0.7045146615, -0.0597469938), (0.7195911631, -0.0535042844), (0.7346389073, -0.0464055961), (0.7496646796, -0.0385317369), (0.7594773343, -0.032703329), (0.7644298266, -0.0297617046)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0146700203, 0.0296806118, 0.0450183654, 0.0606813044, 0.0766684287, 0.0929790505, 0.1096126299, 0.1265687162, 0.1438469219, 0.1438469219, 0.1438469219, 0.1438469219], 3)
                CenterArc((-0.0120304467, 0), 0.7770304467, -2.1950713549, 4.3901427099)
                _nurbs_edge([(0.6297595862, 0.0751549049), (0.6346571366, 0.0751746175), (0.6445659364, 0.0752145002), (0.6594312898, 0.072842976), (0.6744051928, 0.0695236767), (0.6894439439, 0.0650994737), (0.7045146615, 0.0597469938), (0.7195911631, 0.0535042844), (0.7346389073, 0.0464055961), (0.7496646796, 0.0385317369), (0.7594773343, 0.032703329), (0.7644298266, 0.0297617046)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0146700203, 0.0296806118, 0.0450183654, 0.0606813044, 0.0766684287, 0.0929790505, 0.1096126299, 0.1265687162, 0.1438469219, 0.1438469219, 0.1438469219, 0.1438469219], 3)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_24916_42eacca3_0001():
    """Model: 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0202436354, perimeter: 17.3666873012
            with BuildLine():
                Line((-2.2, 0), (-2.2, -3))
                Line((-2.2, -3), (-2.1, -3))
                Line((0, -1.0000317733), (-2.1, -3))
                Line((0, 0), (0, -1.0000317733))
                Line((0, 0), (-2.2, 0))
            make_face()
            with BuildLine():
                Line((-0.25, -0.1), (-2.1, -0.1))
                Line((-0.25, -0.1), (-0.25, -1.1000290342))
                Line((-0.25, -1.1000290342), (-2.1, -2.8619058054))
                Line((-2.1, -0.1), (-2.1, -2.8619058054))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.4797897266, perimeter: 8.1666774404
            with BuildLine():
                Line((-2.1, -0.1), (-2.1, -2.8619058054))
                Line((-0.25, -1.1000290342), (-2.1, -2.8619058054))
                Line((-0.25, -0.1), (-0.25, -1.1000290342))
                Line((-0.25, -0.1), (-2.1, -0.1))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4797897266, perimeter: 8.1666774404
            with BuildLine():
                Line((-2.1, -0.1), (-2.1, -2.8619058054))
                Line((-0.25, -1.1000290342), (-2.1, -2.8619058054))
                Line((-0.25, -0.1), (-0.25, -1.1000290342))
                Line((-0.25, -0.1), (-2.1, -0.1))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_25132_c8588afc_0003():
    """Model: CounterweightA v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0709623664, perimeter: 7.9411500823
            with BuildLine():
                CenterArc((0, 1.5), 0.6, 0, 180)
                Line((-0.6, 1.5), (-0.6, 0))
                Line((-0.6, 0), (-0.25, 0))
                CenterArc((0, 0), 0.25, 0, 180)
                Line((0.25, 0), (0.6, 0))
                Line((0.6, 0), (0.6, 1.5))
            make_face()
            with BuildLine():
                CenterArc((0, 1.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.719302272, perimeter: 13.1393797974
            with BuildLine():
                Line((0.25, 0), (0.6, 0))
                CenterArc((0, 0), 0.25, -180, 180)
                Line((-0.6, 0), (-0.25, 0))
                Line((-2.5, 0), (-0.6, 0))
                CenterArc((0, 0), 2.5, 180, 180)
                Line((0.6, 0), (2.5, 0))
            make_face()
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 1.5)):
                Circle(0.25)
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                Line((-0.25, 0), (0.25, 0))
                CenterArc((0, 0), 0.25, 0, 180)
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((0, 0), 0.25, -180, 180)
                Line((-0.25, 0), (0.25, 0))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_25168_05818e21_0000():
    """Model: Component25"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_25168_05818e21_0001():
    """Model: Component26"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


def model_25168_05818e21_0002():
    """Model: Component24"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)
    return part.part


def model_25168_05818e21_0003():
    """Model: Component37"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 4.4821024819, perimeter: 7.5049157836
            with BuildLine():
                CenterArc((0, 0), 1.1944444444, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.1944444444, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0414605449, perimeter: 0.7999774345
            with BuildLine():
                Line((1.1906150852, 0.0955680379), (1.2488807306, 0.1002448923))
                CenterArc((0, 0), 1.1944444444, -4.5891664191, 9.1783328383)
                Line((1.1906150852, -0.0955680379), (1.2488807306, -0.1002448923))
                _nurbs_edge([(1.2488807306, -0.1002448923), (1.2560343655, -0.1001065962), (1.2704661317, -0.0998275973), (1.2920475835, -0.0963506153), (1.3137273233, -0.091702725), (1.3354587221, -0.0857014368), (1.3572165967, -0.0785771769), (1.3789791108, -0.0703859086), (1.4007158683, -0.0611768467), (1.4224404969, -0.0510549904), (1.4367100114, -0.0436137524), (1.4438974572, -0.0398656576)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0214399145, 0.0432529536, 0.0654256768, 0.0879565521, 0.110844949, 0.1340904941, 0.1576929214, 0.1816520212, 0.2059676187, 0.2059676187, 0.2059676187, 0.2059676187], 3)
                CenterArc((-0.0085782002, 0), 1.4530226447, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.2488807306, 0.1002448923), (1.2560343655, 0.1001065962), (1.2704661317, 0.0998275973), (1.2920475835, 0.0963506153), (1.3137273233, 0.091702725), (1.3354587221, 0.0857014368), (1.3572165967, 0.0785771769), (1.3789791108, 0.0703859086), (1.4007158683, 0.0611768467), (1.4224404969, 0.0510549904), (1.4367100114, 0.0436137524), (1.4438974572, 0.0398656576)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0214399145, 0.0432529536, 0.0654256768, 0.0879565521, 0.110844949, 0.1340904941, 0.1576929214, 0.1816520212, 0.2059676187, 0.2059676187, 0.2059676187, 0.2059676187], 3)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_25168_05818e21_0005():
    """Model: Component51"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 14.5220120412, perimeter: 13.5088484104
            with BuildLine():
                CenterArc((0, 0), 2.15, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 2.15, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1343321656, perimeter: 1.4399593822
            with BuildLine():
                Line((2.1431071533, 0.1720224681), (2.2479853152, 0.1804408061))
                CenterArc((0, 0), 2.15, -4.5891664191, 9.1783328383)
                Line((2.1431071533, -0.1720224681), (2.2479853152, -0.1804408061))
                _nurbs_edge([(2.2479853152, -0.1804408061), (2.2608618578, -0.1801918732), (2.286839037, -0.1796896752), (2.3256856503, -0.1734311075), (2.3647091819, -0.165064905), (2.4038256999, -0.1542625862), (2.4429898741, -0.1414389185), (2.4821623994, -0.1266946355), (2.521288563, -0.1101183241), (2.5603928944, -0.0918989827), (2.5860780205, -0.0785047544), (2.5990154229, -0.0717581836)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0385918461, 0.0778553164, 0.1177662183, 0.1583217937, 0.1995209082, 0.2413628894, 0.2838472584, 0.3269736382, 0.3707417136, 0.3707417136, 0.3707417136, 0.3707417136], 3)
                CenterArc((-0.0154407604, 0), 2.6154407604, -1.5721851245, 3.144370249)
                _nurbs_edge([(2.2479853152, 0.1804408061), (2.2608618578, 0.1801918732), (2.286839037, 0.1796896752), (2.3256856503, 0.1734311075), (2.3647091819, 0.165064905), (2.4038256999, 0.1542625862), (2.4429898741, 0.1414389185), (2.4821623994, 0.1266946355), (2.521288563, 0.1101183241), (2.5603928944, 0.0918989827), (2.5860780205, 0.0785047544), (2.5990154229, 0.0717581836)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0385918461, 0.0778553164, 0.1177662183, 0.1583217937, 0.1995209082, 0.2413628894, 0.2838472584, 0.3269736382, 0.3707417136, 0.3707417136, 0.3707417136, 0.3707417136], 3)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_25168_05818e21_0006():
    """Model: Component29"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


def model_25168_05818e21_0009():
    """Model: Component18"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_25168_05818e21_0010():
    """Model: Component16"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_25168_05818e21_0011():
    """Model: Component12"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_21713_c2dd40e0_0009": {"func": model_21713_c2dd40e0_0009, "volume": 4.7355064041, "area": 30.5728833738},
    "model_21713_c2dd40e0_0022": {"func": model_21713_c2dd40e0_0022, "volume": 4.7355064041, "area": 30.5728833738},
    "model_21717_14f4c79a_0003": {"func": model_21717_14f4c79a_0003, "volume": 0.5090331873, "area": 4.6316230511},
    "model_21732_adaf1650_0025": {"func": model_21732_adaf1650_0025, "volume": 821.1327412287, "area": 978.2654824574},
    "model_21740_6f0c9bdb_0007": {"func": model_21740_6f0c9bdb_0007, "volume": 0.4209734156, "area": 9.3619461077},
    "model_21803_8a36dcda_0003": {"func": model_21803_8a36dcda_0003, "volume": 828, "area": 992},
    "model_21803_8a36dcda_0011": {"func": model_21803_8a36dcda_0011, "volume": 3.3689363134, "area": 73.8781073683},
    "model_21822_7d3db422_0029": {"func": model_21822_7d3db422_0029, "volume": 1.4057344539, "area": 11.3769905504},
    "model_21822_7d3db422_0048": {"func": model_21822_7d3db422_0048, "volume": 0.0172787596, "area": 0.408407045},
    "model_21881_f3bee5e5_0003": {"func": model_21881_f3bee5e5_0003, "volume": 4.8317406872, "area": 25.9816702014},
    "model_21908_385686ec_0026": {"func": model_21908_385686ec_0026, "volume": 0.015, "area": 0.73},
    "model_21923_41fa6eda_0000": {"func": model_21923_41fa6eda_0000, "volume": 173.5388303514, "area": 271.1603943954},
    "model_21984_3353d033_0002": {"func": model_21984_3353d033_0002, "volume": 4.8105637508, "area": 27.8816348006},
    "model_22002_315afcfc_0011": {"func": model_22002_315afcfc_0011, "volume": 4.8276613606, "area": 22.7677144724},
    "model_22010_95d37f0e_0003": {"func": model_22010_95d37f0e_0003, "volume": 1524, "area": 1454},
    "model_22052_665cc4e0_0000": {"func": model_22052_665cc4e0_0000, "volume": 15.2366921072, "area": 181.80350736},
    "model_22118_1e09e0eb_0004": {"func": model_22118_1e09e0eb_0004, "volume": 8.9064151729, "area": 64.4654812517},
    "model_22124_6f71410e_0011": {"func": model_22124_6f71410e_0011, "volume": 1.8476019389, "area": 11.0842261053},
    "model_22196_0deb2e34_0000": {"func": model_22196_0deb2e34_0000, "volume": 158.631825703, "area": 241.5355507132},
    "model_22201_473a3a65_0007": {"func": model_22201_473a3a65_0007, "volume": 8.7258133354, "area": 46.69216468},
    "model_22204_126d06b5_0000": {"func": model_22204_126d06b5_0000, "volume": 51.0495450781, "area": 83.56838125},
    "model_22205_f48b96b3_0005": {"func": model_22205_f48b96b3_0005, "volume": 7.2059553618, "area": 36.8983333854},
    "model_22225_a3ce4d29_0001": {"func": model_22225_a3ce4d29_0001, "volume": 1.7248187895, "area": 11.1776133143},
    "model_22225_a3ce4d29_0006": {"func": model_22225_a3ce4d29_0006, "volume": 47.3053258923, "area": 150.4262448257},
    "model_22225_a3ce4d29_0008": {"func": model_22225_a3ce4d29_0008, "volume": 4.0897238576, "area": 29.84040506},
    "model_22276_69c5036b_0015": {"func": model_22276_69c5036b_0015, "volume": 104.501938029, "area": 150.4194562539},
    "model_22320_e9f9e6ae_0011": {"func": model_22320_e9f9e6ae_0011, "volume": 177.6034951928, "area": 494.3384069271},
    "model_22340_ec24cd79_0037": {"func": model_22340_ec24cd79_0037, "volume": 0.1552566774, "area": 3.7320524602},
    "model_22344_51f483c9_0007": {"func": model_22344_51f483c9_0007, "volume": 1.3398188321, "area": 13.2463970289},
    "model_22446_20eb3290_0000": {"func": model_22446_20eb3290_0000, "volume": 99.4063937182, "area": 1047.7669774414},
    "model_22447_4062c6cb_0004": {"func": model_22447_4062c6cb_0004, "volume": 90.4385985152, "area": 122.6006533063},
    "model_22461_0ba0e480_0000": {"func": model_22461_0ba0e480_0000, "volume": 8.3808742426, "area": 24.3727261438},
    "model_22461_0ba0e480_0001": {"func": model_22461_0ba0e480_0001, "volume": 0.0746721854, "area": 1.5177545314},
    "model_22461_0ba0e480_0003": {"func": model_22461_0ba0e480_0003, "volume": 84.8704895709, "area": 118.2124676166},
    "model_22524_0be3da8a_0016": {"func": model_22524_0be3da8a_0016, "volume": 0.0454766873, "area": 1.3632137002},
    "model_22534_e899f645_0003": {"func": model_22534_e899f645_0003, "volume": 0.9426540505, "area": 6.3338434887},
    "model_22645_1ba0af00_0005": {"func": model_22645_1ba0af00_0005, "volume": 0.6804078951, "area": 7.1757406511},
    "model_22645_1ba0af00_0009": {"func": model_22645_1ba0af00_0009, "volume": 0.2224249218, "area": 3.376801504},
    "model_22719_67a50d6f_0003": {"func": model_22719_67a50d6f_0003, "volume": 738.1088478075, "area": 969.2053048261},
    "model_22719_67a50d6f_0010": {"func": model_22719_67a50d6f_0010, "volume": 0.2049889206, "area": 2.7331856086},
    "model_22751_90a6225a_0005": {"func": model_22751_90a6225a_0005, "volume": 2741.9716617121, "area": 5700.9770548869},
    "model_22753_071ecad9_0000": {"func": model_22753_071ecad9_0000, "volume": 1.0456991118, "area": 8.5246015352},
    "model_22753_071ecad9_0001": {"func": model_22753_071ecad9_0001, "volume": 7.872, "area": 30.6172095601},
    "model_22756_fc3fdda5_0004": {"func": model_22756_fc3fdda5_0004, "volume": 1.3285633822, "area": 20.6306612623},
    "model_22756_fc3fdda5_0017": {"func": model_22756_fc3fdda5_0017, "volume": 0.5741972298, "area": 9.6971910828},
    "model_22756_fc3fdda5_0027": {"func": model_22756_fc3fdda5_0027, "volume": 0.2344505243, "area": 5.9033066647},
    "model_22768_620b0a0b_0000": {"func": model_22768_620b0a0b_0000, "volume": 20, "area": 66},
    "model_22768_620b0a0b_0004": {"func": model_22768_620b0a0b_0004, "volume": 22.4, "area": 76.48},
    "model_22784_bcace961_0000": {"func": model_22784_bcace961_0000, "volume": 322.297122609, "area": 537.8975098534},
    "model_22790_2bdc9e13_0002": {"func": model_22790_2bdc9e13_0002, "volume": 17032.8154079766, "area": 4033.43470837},
    "model_22822_b5d896dd_0007": {"func": model_22822_b5d896dd_0007, "volume": 1.6215928947, "area": 19.9238934212},
    "model_22827_f33929ec_0000": {"func": model_22827_f33929ec_0000, "volume": 15.7009853911, "area": 131.4976610825},
    "model_23011_f267137c_0001": {"func": model_23011_f267137c_0001, "volume": 0.162379768, "area": 2.0490381556},
    "model_23018_63087a41_0010": {"func": model_23018_63087a41_0010, "volume": 26.0032836316, "area": 70.4050435169},
    "model_23018_63087a41_0011": {"func": model_23018_63087a41_0011, "volume": 7.1108866333, "area": 35.2912168175},
    "model_23018_63087a41_0017": {"func": model_23018_63087a41_0017, "volume": 1.2589284992, "area": 6.8416299397},
    "model_23018_63087a41_0018": {"func": model_23018_63087a41_0018, "volume": 0.6294642496, "area": 4.6797387626},
    "model_23018_63087a41_0020": {"func": model_23018_63087a41_0020, "volume": 13.0016418158, "area": 61.2057883464},
    "model_23018_63087a41_0021": {"func": model_23018_63087a41_0021, "volume": 5.9739845479, "area": 20.9521272828},
    "model_23018_63087a41_0025": {"func": model_23018_63087a41_0025, "volume": 45.3996273483, "area": 198.646965556},
    "model_23018_63087a41_0029": {"func": model_23018_63087a41_0029, "volume": 1.8320508886, "area": 10.8931663386},
    "model_23121_cbdf3ebc_0000": {"func": model_23121_cbdf3ebc_0000, "volume": 1003.0937340073, "area": 753.1325642703},
    "model_23132_1847c4ef_0008": {"func": model_23132_1847c4ef_0008, "volume": 231.781177823, "area": 318.2955634917},
    "model_23206_b99a5251_0021": {"func": model_23206_b99a5251_0021, "volume": 0.7317914662, "area": 5.1788319146},
    "model_23206_b99a5251_0025": {"func": model_23206_b99a5251_0025, "volume": 0.2100000063, "area": 4.7341593434},
    "model_23206_b99a5251_0037": {"func": model_23206_b99a5251_0037, "volume": 19.3023946399, "area": 66.1801215148},
    "model_23206_b99a5251_0039": {"func": model_23206_b99a5251_0039, "volume": 0.0155884573, "area": 0.7274613392},
    "model_23206_b99a5251_0043": {"func": model_23206_b99a5251_0043, "volume": 0.0541265877, "area": 0.8660254038},
    "model_23206_b99a5251_0044": {"func": model_23206_b99a5251_0044, "volume": 0.5196152423, "area": 3.8105117767},
    "model_23232_8853e95c_0000": {"func": model_23232_8853e95c_0000, "volume": 7.2836859016, "area": 25.6824137694},
    "model_23247_bcd1e84f_0004": {"func": model_23247_bcd1e84f_0004, "volume": 120.1659189998, "area": 240.3318379996},
    "model_23255_972fbfe6_0012": {"func": model_23255_972fbfe6_0012, "volume": 650.0748286264, "area": 496.2374283359},
    "model_23264_20be13a0_0005": {"func": model_23264_20be13a0_0005, "volume": 301.4225109396, "area": 704.8569352944},
    "model_23393_d47067ad_0002": {"func": model_23393_d47067ad_0002, "volume": 2200.4202919596, "area": 4694.2299561805},
    "model_23393_d47067ad_0009": {"func": model_23393_d47067ad_0009, "volume": 15.7079632679, "area": 69.115038379},
    "model_23393_d47067ad_0024": {"func": model_23393_d47067ad_0024, "volume": 7.853981634, "area": 34.5575191895},
    "model_23422_f214bd4d_0001": {"func": model_23422_f214bd4d_0001, "volume": 1.1703256525, "area": 7.0300779226},
    "model_23422_f214bd4d_0003": {"func": model_23422_f214bd4d_0003, "volume": 4.00711043, "area": 18.562423145},
    "model_23422_f214bd4d_0004": {"func": model_23422_f214bd4d_0004, "volume": 14.8315308712, "area": 57.8653779842},
    "model_23422_f214bd4d_0005": {"func": model_23422_f214bd4d_0005, "volume": 23.713331954, "area": 88.7124271755},
    "model_23422_f214bd4d_0006": {"func": model_23422_f214bd4d_0006, "volume": 2.3741726001, "area": 12.1191404093},
    "model_23422_f214bd4d_0007": {"func": model_23422_f214bd4d_0007, "volume": 30.4474523951, "area": 111.7525661015},
    "model_23554_a0845d54_0004": {"func": model_23554_a0845d54_0004, "volume": 56.5486677646, "area": 94.2477796077},
    "model_23681_932e722e_0002": {"func": model_23681_932e722e_0002, "volume": 0.0431691019, "area": 2.1731177003},
    "model_23706_ef15ef9c_0000": {"func": model_23706_ef15ef9c_0000, "volume": 0.68, "area": 6.793137085},
    "model_23706_ef15ef9c_0001": {"func": model_23706_ef15ef9c_0001, "volume": 624.9345828074, "area": 959.1231828956},
    "model_23706_ef15ef9c_0004": {"func": model_23706_ef15ef9c_0004, "volume": 26.4, "area": 145.04},
    "model_23787_1304fb90_0000": {"func": model_23787_1304fb90_0000, "volume": 7060.9380098815, "area": 2131.8406743523},
    "model_23790_2abde9b6_0008": {"func": model_23790_2abde9b6_0008, "volume": 69.312, "area": 123.88},
    "model_23856_6be75f62_0007": {"func": model_23856_6be75f62_0007, "volume": 251706705973280.1875, "area": 254587510625.2360229492},
    "model_23956_ee17fe48_0014": {"func": model_23956_ee17fe48_0014, "volume": 12.723450247, "area": 33.3637139811},
    "model_24032_d6172503_0030": {"func": model_24032_d6172503_0030, "volume": 0.016525464, "area": 0.4746151808},
    "model_24047_9eb475f0_0004": {"func": model_24047_9eb475f0_0004, "volume": 42.4567393972, "area": 147.6293159592},
    "model_24051_4852a192_0001": {"func": model_24051_4852a192_0001, "volume": 2.2266687915, "area": 13.7155480697},
    "model_24051_4852a192_0002": {"func": model_24051_4852a192_0002, "volume": 1.2501431509, "area": 18.4362120208},
    "model_24131_3ea7d5a8_0012": {"func": model_24131_3ea7d5a8_0012, "volume": 0.4901801062, "area": 5.660872618},
    "model_24195_9791f5d3_0005": {"func": model_24195_9791f5d3_0005, "volume": 0.6589490591, "area": 10.1002203813},
    "model_24195_9791f5d3_0040": {"func": model_24195_9791f5d3_0040, "volume": 0.2576105976, "area": 4.0212385966},
    "model_24195_9791f5d3_0042": {"func": model_24195_9791f5d3_0042, "volume": 0.1103719019, "area": 3.2086592829},
    "model_24238_df51962d_0000": {"func": model_24238_df51962d_0000, "volume": 9.2251173005, "area": 69.7216091462},
    "model_24284_3710e946_0010": {"func": model_24284_3710e946_0010, "volume": 5.604375888, "area": 29.8838112},
    "model_24300_ed2686dc_0012": {"func": model_24300_ed2686dc_0012, "volume": 0.2953097094, "area": 4.162610266},
    "model_24302_2bcddd22_0002": {"func": model_24302_2bcddd22_0002, "volume": 0.0107374108, "area": 0.3913921792},
    "model_24308_89c2be2b_0004": {"func": model_24308_89c2be2b_0004, "volume": 0.9311036978, "area": 6.7992543083},
    "model_24357_8d7d40b1_0002": {"func": model_24357_8d7d40b1_0002, "volume": 4.224, "area": 17.92},
    "model_24405_b96b34b6_0011": {"func": model_24405_b96b34b6_0011, "volume": 0.3970478294, "area": 17.162153308},
    "model_24407_2d357602_0002": {"func": model_24407_2d357602_0002, "volume": 35.4695235368, "area": 65.9916669628},
    "model_24409_62adef9c_0000": {"func": model_24409_62adef9c_0000, "volume": 22089.3233455532, "area": 10013.8265833175},
    "model_24412_a8e106be_0008": {"func": model_24412_a8e106be_0008, "volume": 1.7090264036, "area": 9.5504416669},
    "model_24518_b99235fc_0000": {"func": model_24518_b99235fc_0000, "volume": 16785.7597059464, "area": 8652.975812589},
    "model_24643_71176e22_0000": {"func": model_24643_71176e22_0000, "volume": 0.7891685996, "area": 16.8008367169},
    "model_24643_71176e22_0001": {"func": model_24643_71176e22_0001, "volume": 1.6334970942, "area": 8.931549657},
    "model_24650_dad8c8ee_0000": {"func": model_24650_dad8c8ee_0000, "volume": 4.7183502934, "area": 17.5687231635},
    "model_24724_c71e66b3_0000": {"func": model_24724_c71e66b3_0000, "volume": 110.4898691424, "area": 128.1028432019},
    "model_24890_5f8a67df_0005": {"func": model_24890_5f8a67df_0005, "volume": 114.6267325371, "area": 276.1555761081},
    "model_24896_58b4730f_0000": {"func": model_24896_58b4730f_0000, "volume": 4.0229242236, "area": 21.2687697664},
    "model_24896_58b4730f_0002": {"func": model_24896_58b4730f_0002, "volume": 0.873676917, "area": 10.3484062009},
    "model_24896_58b4730f_0017": {"func": model_24896_58b4730f_0017, "volume": 0.4078928337, "area": 3.5960181917},
    "model_24916_42eacca3_0001": {"func": model_24916_42eacca3_0001, "volume": 3.2702603163, "area": 30.9667589555},
    "model_25132_c8588afc_0003": {"func": model_25132_c8588afc_0003, "volume": 9.7463709761, "area": 37.5970772211},
    "model_25168_05818e21_0000": {"func": model_25168_05818e21_0000, "volume": 50.890083733, "area": 79.7726042076},
    "model_25168_05818e21_0001": {"func": model_25168_05818e21_0001, "volume": 25.4451512302, "area": 50.0643189141},
    "model_25168_05818e21_0002": {"func": model_25168_05818e21_0002, "volume": 35.6232117223, "area": 61.9476330315},
    "model_25168_05818e21_0003": {"func": model_25168_05818e21_0003, "volume": 6.7853736614, "area": 20.930440171},
    "model_25168_05818e21_0005": {"func": model_25168_05818e21_0005, "volume": 5.8625628434, "area": 35.0166791899},
    "model_25168_05818e21_0006": {"func": model_25168_05818e21_0006, "volume": 12.2136725905, "area": 34.6160105614},
    "model_25168_05818e21_0009": {"func": model_25168_05818e21_0009, "volume": 30.5341814762, "area": 56.0059759728},
    "model_25168_05818e21_0010": {"func": model_25168_05818e21_0010, "volume": 15.2670907381, "area": 38.1810047967},
    "model_25168_05818e21_0011": {"func": model_25168_05818e21_0011, "volume": 40.7120669864, "area": 67.8892900902},
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
